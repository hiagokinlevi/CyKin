"""The public test pilot must enforce identity, timing and certificate gates."""

from __future__ import annotations

import importlib
import hashlib
import json
import sqlite3
from pathlib import Path
from types import SimpleNamespace

import pytest
from fastapi.testclient import TestClient

from quiz_engine import InvalidBank, validate_bank


ROOT = Path(__file__).resolve().parents[2]
api = importlib.import_module("app")
ORIGIN = {"Origin": "https://opencyber.academy"}
COURSE = {"level": "professional-6-months", "area": "ot-iot-security", "language": "en", "chapter": 1}


class Statement:
    def __init__(self, connection: sqlite3.Connection, query: str, args: tuple = ()):
        self.connection, self.query, self.args = connection, query, args

    def bind(self, *args):
        return Statement(self.connection, self.query, args)

    async def all(self):
        rows = self.connection.execute(self.query, self.args).fetchall()
        return {"results": [dict(row) for row in rows]}

    async def run(self):
        before = self.connection.total_changes
        self.connection.execute(self.query, self.args)
        self.connection.commit()
        return {"meta": {"changes": self.connection.total_changes - before}}


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(":memory:", check_same_thread=False)
        self.connection.row_factory = sqlite3.Row
        for migration in ("0001_progress.sql", "0002_chapter_tests.sql", "0003_student_auth.sql", "0004_student_password_activity.sql", "0005_student_mcp_keys.sql", "0006_student_activity_source.sql"):
            self.connection.executescript((ROOT / "web/migrations" / migration).read_text())

    def prepare(self, query: str):
        return Statement(self.connection, query)


@pytest.fixture
def pilot(monkeypatch):
    db = Database()
    now = [1_000.0]
    api.app.state.catalog_override = json.loads((ROOT / "web/public/catalog.json").read_text())

    async def source(path):
        target = ROOT / path
        return target.read_text(encoding="utf-8") if target.is_file() else None

    async def student(_request):
        return {"sub": "student-1", "email": "learner@example.test"}

    api.app.state.source_override = source
    monkeypatch.setattr(api, "database", lambda _request: db)
    monkeypatch.setattr(api, "identity", student)
    monkeypatch.setattr(api, "time", SimpleNamespace(time=lambda: now[0]))
    try:
        yield TestClient(api.app), db, now
    finally:
        db.connection.close()
        del api.app.state.catalog_override
        del api.app.state.source_override


def test_question_bank_is_pinned_to_authored_text_and_has_no_duplicate_prompts():
    for language in ("en", "pt", "es"):
        bank_path = ROOT / f"web/question-banks/professional-6-months/ot-iot-security/{language}/001.json"
        bank, _digest = validate_bank(bank_path.read_text(), "professional-6-months", "ot-iot-security", language, 1)
        manuscript = (ROOT / f"levels/professional-6-months/ot-iot-security/{language}/book/MANUSCRIPT.md").read_text()
        import hashlib
        chapter = api.chapter_sections(manuscript)[1]["markdown"]
        assert bank["source_sha256"] == hashlib.sha256(chapter.encode()).hexdigest()
        assert len({item["prompt"].casefold() for item in bank["questions"]}) == 10
    broken = {**bank, "questions": bank["questions"][:9]}
    with pytest.raises(InvalidBank, match="exactly ten"):
        validate_bank(json.dumps(broken), "professional-6-months", "ot-iot-security", "es", 1)


def test_rapid_incident_response_banks_cover_four_weeks_and_start(pilot):
    manuscript = (ROOT / "levels/rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md").read_text()
    client, _db, _now = pilot
    public_index = client.get("/api/tests/catalog").json()
    entries = public_index["courses"]["rapid-1-month/incident-response-resilience/en"]
    assert [entry["chapter"] for entry in entries] == [1, 2, 3, 4]
    assert all("questions" not in entry and "correct" not in entry for entry in entries)
    for number in range(1, 5):
        path = ROOT / f"web/question-banks/rapid-1-month/incident-response-resilience/en/{number:03d}.json"
        bank, _digest = validate_bank(path.read_text(), "rapid-1-month", "incident-response-resilience", "en", number)
        chapter = api.chapter_sections(manuscript)[number]["markdown"]
        assert bank["source_sha256"] == hashlib.sha256(chapter.encode()).hexdigest()
        assert len({item["prompt"].casefold() for item in bank["questions"]}) == 10
        response = client.post("/student/tests/start", json={
            "level": "rapid-1-month", "area": "incident-response-resilience", "language": "en", "chapter": number,
        }, headers=ORIGIN)
        assert response.status_code == 200
        assert response.json()["question"]["seconds"] == 10
        assert "correct" not in response.json()["question"]


def test_full_rapid_ir_bank_coverage_does_not_bypass_book_review(pilot):
    client, _db, now = pilot
    course = {"level": "rapid-1-month", "area": "incident-response-resilience", "language": "en"}
    for chapter in range(1, 5):
        started = client.post("/student/tests/start", json={**course, "chapter": chapter}, headers=ORIGIN)
        assert started.status_code == 200
        attempt_id = started.json()["attempt_id"]
        bank = json.loads((ROOT / f"web/question-banks/rapid-1-month/incident-response-resilience/en/{chapter:03d}.json").read_text())
        for index, question in enumerate(bank["questions"]):
            now[0] += 0.2
            response = client.post("/student/tests/answer", json={
                "attempt_id": attempt_id, "index": index, "selected": question["correct"],
            }, headers=ORIGIN)
            assert response.status_code == 200
        assert response.json()["score"] == 10
    certificate = client.post("/student/tests/certificate", json=course, headers=ORIGIN)
    assert certificate.status_code == 409
    assert "editorial gate" in certificate.json()["detail"]


def test_timeout_duplicate_answer_and_student_isolation(pilot, monkeypatch):
    client, _db, now = pilot
    started = client.post("/private/tests/start", json=COURSE, headers=ORIGIN)
    assert started.status_code == 200
    initial = started.json()
    assert "correct" not in initial["question"]
    assert initial["question"]["seconds"] == 10
    attempt_id = initial["attempt_id"]
    now[0] += 12
    late = client.post("/private/tests/answer", json={"attempt_id": attempt_id, "index": 0, "selected": "a"}, headers=ORIGIN)
    assert late.status_code == 200
    assert late.json()["question"]["number"] == 2
    assert client.post("/private/tests/answer", json={"attempt_id": attempt_id, "index": 0, "selected": "a"}, headers=ORIGIN).status_code == 409
    resumed = client.get("/private/tests/state", params={"attempt_id": attempt_id})
    assert resumed.status_code == 200
    assert resumed.json()["question"]["number"] == 2

    async def other_student(_request):
        return {"sub": "student-2", "email": "other@example.test"}

    monkeypatch.setattr(api, "identity", other_student)
    assert client.post("/private/tests/answer", json={"attempt_id": attempt_id, "index": 1, "selected": "a"}, headers=ORIGIN).status_code == 404


def test_perfect_attempt_is_saved_but_certificate_waits_for_editorial_approval(pilot):
    client, _db, now = pilot
    started = client.post("/private/tests/start", json=COURSE, headers=ORIGIN)
    assert started.status_code == 200
    attempt_id = started.json()["attempt_id"]
    bank = json.loads((ROOT / "web/question-banks/professional-6-months/ot-iot-security/en/001.json").read_text())
    for index, question in enumerate(bank["questions"]):
        now[0] += 0.2
        response = client.post("/private/tests/answer", json={"attempt_id": attempt_id, "index": index, "selected": question["correct"]}, headers=ORIGIN)
        assert response.status_code == 200
        if index < 9:
            assert response.json()["question"]["number"] == index + 2
    result = response.json()
    assert (result["score"], result["perfect"], len(result["feedback"])) == (10, True, 10)
    resumed = client.get("/private/tests/state", params={"attempt_id": attempt_id})
    assert resumed.status_code == 200
    assert resumed.json()["score"] == 10
    scores = client.get("/private/tests/results", params={key: value for key, value in COURSE.items() if key != "chapter"})
    assert scores.status_code == 200
    assert scores.json()["results"][0]["best_score"] == 10
    certificate = client.post("/private/tests/certificate", json={key: value for key, value in COURSE.items() if key != "chapter"}, headers=ORIGIN)
    assert certificate.status_code == 409
    assert "editorial gate" in certificate.json()["detail"]


def test_mutating_origin_or_chapter_prevents_new_attempt(pilot):
    client, _db, _now = pilot
    assert client.post("/private/tests/start", json=COURSE, headers={"Origin": "https://evil.example"}).status_code == 403
    original_source = api.app.state.source_override

    async def changed(path):
        content = await original_source(path)
        return content.replace('<a id="ch-01"></a>', '<a id="ch-01"></a>\nChanged teaching text.\n', 1) if content and path.endswith("MANUSCRIPT.md") else content

    api.app.state.source_override = changed
    assert client.post("/private/tests/start", json=COURSE, headers=ORIGIN).status_code == 409


def test_certificate_requires_full_approval_and_is_private_to_its_owner(pilot, monkeypatch):
    client, _db, now = pilot
    book = (ROOT / "levels/professional-6-months/ot-iot-security/en/book/MANUSCRIPT.md").read_text()
    one_chapter_book = api.chapter_sections(book)[1]["markdown"]
    original_source = api.app.state.source_override

    async def one_chapter_source(path):
        if path == "levels/professional-6-months/ot-iot-security/en/book/MANUSCRIPT.md":
            return one_chapter_book
        return await original_source(path)

    async def approved(_request):
        return {"version": 1, "books": [{**{key: value for key, value in COURSE.items() if key != "chapter"},
                                         "book_sha256": hashlib.sha256(one_chapter_book.encode()).hexdigest()}]}

    api.app.state.source_override = one_chapter_source
    monkeypatch.setattr(api, "approved_books", approved)
    course = api.get_course(api.app.state.catalog_override, "professional-6-months", "ot-iot-security", "en")
    course["planned_chapters"] = 1
    bank = json.loads((ROOT / "web/question-banks/professional-6-months/ot-iot-security/en/001.json").read_text())
    started = client.post("/private/tests/start", json=COURSE, headers=ORIGIN)
    assert started.status_code == 200
    attempt_id = started.json()["attempt_id"]
    for index, question in enumerate(bank["questions"]):
        now[0] += 0.1
        response = client.post("/private/tests/answer", json={"attempt_id": attempt_id, "index": index, "selected": question["correct"]}, headers=ORIGIN)
        assert response.status_code == 200
    claim = client.post("/private/tests/certificate", json={key: value for key, value in COURSE.items() if key != "chapter"}, headers=ORIGIN)
    assert claim.status_code == 200
    issued = claim.json()
    assert client.get(issued["certificate_url"]).status_code == 200
    assert "learner@example.test" in client.get(issued["certificate_url"]).text
    public = client.get(f'/api/certificates/{issued["certificate_id"]}')
    assert public.status_code == 200
    assert "learner@example.test" not in public.text

    async def other_student(_request):
        return {"sub": "student-2", "email": "other@example.test"}

    monkeypatch.setattr(api, "identity", other_student)
    assert client.get(issued["certificate_url"]).status_code == 404
