"""Email-code authentication must protect student records without changing public study."""

from __future__ import annotations

import importlib
import base64
import json
import re
import sqlite3
from pathlib import Path
from types import SimpleNamespace

from fastapi.testclient import TestClient


ROOT = Path(__file__).resolve().parents[2]
api = importlib.import_module("app")
student_auth = importlib.import_module("student_auth")
ORIGIN = {"Origin": "https://opencyber.academy"}


def test_legacy_login_points_to_branded_account_without_open_redirect():
    with TestClient(api.app, base_url="https://opencyber.academy") as client:
        response = client.get("/private/login?next=%2Ftests%2F%3Flang%3Dpt", follow_redirects=False)
        assert response.status_code == 302
        assert response.headers["location"] == "/account/?next=%2Ftests%2F%3Flang%3Dpt"
        blocked = client.get("/private/login?next=https%3A%2F%2Fexample.invalid", follow_redirects=False)
        assert blocked.headers["location"] == "/account/"


def test_provisioned_password_digest_remains_stable():
    assert student_auth.PASSWORD_ITERATIONS == 100_000
    assert student_auth.password_digest(
        "synthetic-local-passphrase", "00112233445566778899aabbccddeeff"
    ) == "6ad6020e82138280a404d2d85310b359cfcb17222c9004a5d6725e4364086119"


class Statement:
    def __init__(self, conn: sqlite3.Connection, query: str, args: tuple = ()):
        self.conn, self.query, self.args = conn, query, args

    def bind(self, *args):
        return Statement(self.conn, self.query, args)

    async def all(self):
        return {"results": [dict(row) for row in self.conn.execute(self.query, self.args).fetchall()]}

    async def run(self):
        before = self.conn.total_changes
        self.conn.execute(self.query, self.args)
        self.conn.commit()
        return {"meta": {"changes": self.conn.total_changes - before}}


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(":memory:", check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        for migration in ("0001_progress.sql", "0002_chapter_tests.sql", "0003_student_auth.sql", "0004_student_password_activity.sql", "0005_student_mcp_keys.sql", "0006_student_activity_source.sql"):
            self.conn.executescript((ROOT / "web/migrations" / migration).read_text())

    def prepare(self, query: str):
        return Statement(self.conn, query)


class EmailSender:
    def __init__(self):
        self.messages = []

    async def send(self, message):
        self.messages.append(message)


class Environment:
    def __init__(self, app, env):
        self.app, self.env = app, env

    async def __call__(self, scope, receive, send):
        scope["env"] = self.env
        await self.app(scope, receive, send)


def test_activity_source_migration_preserves_existing_records():
    connection = sqlite3.connect(":memory:")
    try:
        connection.executescript((ROOT / "web/migrations/0004_student_password_activity.sql").read_text())
        connection.execute(
            "INSERT INTO student_activity (id, user_id, kind, level, area, language, chapter) "
            "VALUES ('old', 'student', 'lesson_opened', 'rapid-1-month', 'cybersecurity', 'en', 1)"
        )
        connection.executescript((ROOT / "web/migrations/0006_student_activity_source.sql").read_text())
        assert connection.execute("SELECT source FROM student_activity WHERE id = 'old'").fetchone()[0] == "site"
    finally:
        connection.close()


def test_email_code_session_and_legacy_boundary(monkeypatch):
    db, sender = Database(), EmailSender()
    now = [1_000_000.0]
    monkeypatch.setattr(student_auth.time, "time", lambda: now[0])
    env = SimpleNamespace(DB=db, EMAIL=sender, AUTH_HMAC_KEY="a" * 64)
    try:
        with TestClient(Environment(api.app, env), base_url="https://opencyber.academy") as client:
            assert client.get("/auth/me").status_code == 401
            assert client.get("/student/progress").status_code == 401
            assert client.get("/student/analyses").status_code == 401
            assert client.post("/auth/request-code", json={"email": "student@example.test"}, headers={"Origin": "https://attacker.invalid"}).status_code == 403
            created = client.post("/auth/request-code", json={"email": "Student@Example.test", "language": "en"}, headers=ORIGIN)
            assert created.status_code == 200
            flow_id = created.json()["flow_id"]
            assert sender.messages[0]["to"] == "student@example.test"
            code = re.search(r"\b[0-9]{6}\b", sender.messages[0]["text"]).group()
            stored = dict(db.conn.execute("SELECT * FROM login_challenges").fetchone())
            assert code not in stored.values()
            assert stored["code_digest"] != code
            assert client.post("/auth/verify-code", json={"flow_id": flow_id, "code": "000000"}, headers=ORIGIN).status_code == 400
            verified = client.post("/auth/verify-code", json={"flow_id": flow_id, "code": code}, headers=ORIGIN)
            assert verified.status_code == 200
            cookie = verified.headers["set-cookie"].lower()
            assert "httponly" in cookie and "secure" in cookie and "samesite=lax" in cookie
            assert "domain=opencyber.academy" in cookie
            assert client.get("/auth/me").json()["email"] == "student@example.test"
            assert client.get("/student/progress").json() == {"lessons": [], "exercises": []}
            assert client.get("/private/me").status_code == 503  # old Access route still needs its JWT
            assert client.post("/auth/verify-code", json={"flow_id": flow_id, "code": code}, headers=ORIGIN).status_code == 400
            assert client.post("/auth/logout", json={}, headers=ORIGIN).status_code == 200
            assert client.get("/auth/me").status_code == 401
            assert client.get("/student/progress").status_code == 401
    finally:
        db.conn.close()


def test_expiry_attempt_limit_and_email_request_limit(monkeypatch):
    db, sender = Database(), EmailSender()
    now = [2_000_000.0]
    monkeypatch.setattr(student_auth.time, "time", lambda: now[0])
    env = SimpleNamespace(DB=db, EMAIL=sender, AUTH_HMAC_KEY="b" * 64)
    try:
        with TestClient(Environment(api.app, env), base_url="https://opencyber.academy") as client:
            def ask(address):
                return client.post("/auth/request-code", json={"email": address}, headers=ORIGIN)
            first = ask("learner@example.test")
            assert first.status_code == 200
            flow_id = first.json()["flow_id"]
            code = re.search(r"\b[0-9]{6}\b", sender.messages[-1]["text"]).group()
            for _ in range(5):
                assert client.post("/auth/verify-code", json={"flow_id": flow_id, "code": "999999" if code != "999999" else "000000"}, headers=ORIGIN).status_code == 400
            assert client.post("/auth/verify-code", json={"flow_id": flow_id, "code": code}, headers=ORIGIN).status_code == 400
            assert ask("learner@example.test").status_code == 200
            assert ask("learner@example.test").status_code == 200
            assert ask("learner@example.test").status_code == 429
            newer = db.conn.execute("SELECT id FROM login_challenges ORDER BY created_at DESC, rowid DESC LIMIT 1").fetchone()[0]
            newer_code = re.search(r"\b[0-9]{6}\b", sender.messages[-1]["text"]).group()
            now[0] += 901
            assert client.post("/auth/verify-code", json={"flow_id": newer, "code": newer_code}, headers=ORIGIN).status_code == 400
    finally:
        db.conn.close()


def test_provisioned_password_student_and_private_mcp(monkeypatch):
    db = Database()
    env = SimpleNamespace(DB=db, EMAIL=EmailSender(), AUTH_HMAC_KEY="c" * 64)
    salt = "ab" * 16
    password = "synthetic-test-passphrase"
    db.conn.execute(
        "INSERT INTO student_accounts (id, email, created_at, last_login_at) VALUES (?, ?, 1, 1)",
        ("synthetic-student", "learner@students.invalid"),
    )
    db.conn.execute(
        "INSERT INTO student_password_credentials (user_id, username, password_salt, password_digest) VALUES (?, ?, ?, ?)",
        ("synthetic-student", "learner", salt, student_auth.password_digest(password, salt)),
    )
    db.conn.commit()
    # Deploys run the D1 migration file again; credentials and records must survive.
    db.conn.executescript((ROOT / "web/migrations/0004_student_password_activity.sql").read_text())
    assert db.conn.execute("SELECT username FROM student_password_credentials WHERE user_id = ?", ("synthetic-student",)).fetchone()[0] == "learner"
    api.app.state.catalog_override = json.loads((ROOT / "web/public/catalog.json").read_text())

    async def local_source(path):
        source = ROOT / path
        return source.read_text(encoding="utf-8") if source.is_file() else None

    api.app.state.source_override = local_source
    mcp_headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}

    def rpc(client, name, args=None, headers=None):
        return client.post("/mcp", json={"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                                         "params": {"name": name, "arguments": args or {}}},
                           headers={**mcp_headers, **(headers or {})})

    try:
        with TestClient(Environment(api.app, env), base_url="https://opencyber.academy") as client:
            invalid = client.post("/auth/password-login", json={"username": "learner", "password": "wrong"}, headers=ORIGIN)
            assert invalid.status_code == 401
            assert client.post("/auth/password-login", json={"username": "learner", "password": password}, headers={"Origin": "https://evil.invalid"}).status_code == 403
            login = client.post("/auth/password-login", json={"username": "learner", "password": password}, headers=ORIGIN)
            assert login.status_code == 200
            assert client.get("/auth/me").json()["username"] == "learner"
            assert client.get("/auth/me").json()["email"] is None
            assert client.post("/student/activity", json={"level": "rapid-1-month", "area": "incident-response-resilience",
                                                          "language": "en", "chapter": 1, "kind": "lesson_opened"}, headers=ORIGIN).status_code == 200
            note = {"level": "rapid-1-month", "area": "incident-response-resilience", "language": "en",
                    "chapter": 1, "note": "Synthetic analysis of authorized scope"}
            assert client.post("/student/analysis", json=note, headers=ORIGIN).status_code == 200
            assert client.get("/student/analysis", params={k: v for k, v in note.items() if k != "note"}).json()["analysis"]["note"] == note["note"]
            assert len(client.get("/student/analyses").json()["analyses"]) == 1
            assert client.get("/student/stats").json()["summary"]["analyses_saved"] == 1
            assert client.post("/auth/logout", json={}, headers=ORIGIN).status_code == 200
            assert client.get("/student/stats").status_code == 401

            no_auth = rpc(client, "student_get_stats")
            assert no_auth.status_code == 401
            assert no_auth.headers["www-authenticate"] == "Bearer"
            basic = base64.b64encode(f"learner:{password}".encode()).decode()
            signin = rpc(client, "student_sign_in", headers={"Authorization": f"Basic {basic}"})
            assert signin.status_code == 200
            token = json.loads(signin.json()["result"]["content"][0]["text"])["access_token"]
            bearer = {"Authorization": f"Bearer {token}"}
            result = rpc(client, "student_read_lesson", {"level": "rapid-1-month", "area": "incident-response-resilience",
                                                         "language": "en", "chapter": 1}, bearer)
            assert result.status_code == 200
            assert "EX001" in json.loads(result.json()["result"]["content"][0]["text"])["worked_answers"]
            course = {"level": "professional-6-months", "area": "ot-iot-security", "language": "en", "chapter": 1}
            started = rpc(client, "student_start_test", course, bearer)
            assert started.status_code == 200
            attempt_id = json.loads(started.json()["result"]["content"][0]["text"])["attempt_id"]
            bank = json.loads((ROOT / "web/question-banks/professional-6-months/ot-iot-security/en/001.json").read_text())
            for index, question in enumerate(bank["questions"]):
                answered = rpc(client, "student_answer_test", {"attempt_id": attempt_id, "index": index,
                                                                "selected": question["correct"]}, bearer)
                assert answered.status_code == 200
            final = json.loads(answered.json()["result"]["content"][0]["text"])
            assert final["complete"] is True and final["score"] == 10
            state = rpc(client, "student_test_state", {"attempt_id": attempt_id}, bearer)
            assert json.loads(state.json()["result"]["content"][0]["text"])["score"] == 10
            results = rpc(client, "student_test_results", {key: value for key, value in course.items() if key != "chapter"}, bearer)
            assert json.loads(results.json()["result"]["content"][0]["text"])["results"][0]["best_score"] == 10
            summary = rpc(client, "student_get_stats", headers=bearer)
            report = json.loads(summary.json()["result"]["content"][0]["text"])
            assert report["activity"]["lesson_opened"]["events"] == 2
            assert report["activity"]["test_answered"]["events"] == 10
            assert report["sources"]["site"] == 2
            assert report["sources"]["mcp"] == 12
            assert any(item["source"] == "mcp" for item in report["recent"])
            assert next(item for item in report["courses"] if item["area"] == "ot-iot-security")["best_correct"] == 10
            assert password not in json.dumps(db.conn.execute("SELECT * FROM student_accounts").fetchall(), default=str)
    finally:
        del api.app.state.catalog_override
        del api.app.state.source_override
        db.conn.close()


def test_student_mcp_keys_are_one_time_scoped_revocable_and_expiring(monkeypatch):
    db = Database()
    now = [1_800_000_000]
    monkeypatch.setattr(student_auth.time, "time", lambda: now[0])
    env = SimpleNamespace(DB=db, EMAIL=EmailSender(), AUTH_HMAC_KEY="d" * 64)
    db.conn.executemany(
        "INSERT INTO student_accounts (id, email, created_at, last_login_at) VALUES (?, ?, 1, 1)",
        [("student-one", "one@example.test"), ("student-two", "two@example.test")],
    )
    db.conn.commit()
    headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}

    api.app.state.catalog_override = json.loads((ROOT / "web/public/catalog.json").read_text())

    async def local_source(path):
        source = ROOT / path
        return source.read_text(encoding="utf-8") if source.is_file() else None

    api.app.state.source_override = local_source

    def rpc(client, token, name="student_get_stats", args=None):
        return client.post("/mcp", headers={**headers, "Authorization": f"Bearer {token}"},
                           json={"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                                 "params": {"name": name, "arguments": args or {}}})

    try:
        with TestClient(Environment(api.app, env), base_url="https://opencyber.academy") as client:
            assert client.get("/auth/mcp-keys").status_code == 401
            cookie_token = "browser-session-for-student-one-token-123"
            db.conn.execute("INSERT INTO student_sessions (token_digest, user_id, created_at, expires_at) VALUES (?, ?, ?, ?)",
                            (student_auth.hashlib.sha256(cookie_token.encode()).hexdigest(), "student-one",
                             now[0], now[0] + student_auth.SESSION_LIFETIME))
            db.conn.commit()
            client.cookies.set(student_auth.COOKIE, cookie_token, domain="opencyber.academy")
            assert client.post("/auth/mcp-keys", json={"label": "DAI"}).status_code == 403
            assert client.post("/auth/mcp-keys", json={"label": "DAI"}, headers={"Origin": "https://evil.invalid"}).status_code == 403
            created = client.post("/auth/mcp-keys", json={"label": "DAI"}, headers=ORIGIN)
            assert created.status_code == 200
            key = created.json()["token"]
            key_id = created.json()["id"]
            assert key.startswith("oca_")
            stored = dict(db.conn.execute("SELECT * FROM student_mcp_keys WHERE id = ?", (key_id,)).fetchone())
            assert key not in stored.values()
            assert stored["token_digest"] == student_auth.hashlib.sha256(key.encode()).hexdigest()
            listed = client.get("/auth/mcp-keys").json()["keys"]
            assert listed[0]["label"] == "DAI" and "token" not in listed[0]
            assert rpc(client, key).status_code == 200
            lesson = {"level": "rapid-1-month", "area": "incident-response-resilience", "language": "en", "chapter": 1}
            saved_lesson = rpc(client, key, "student_save_lesson", {**lesson, "status": "completed"})
            assert json.loads(saved_lesson.json()["result"]["content"][0]["text"])["saved"] is True
            saved_exercise = rpc(client, key, "student_save_exercise", {**lesson, "exercise_id": "EX001", "answer": "Synthetic student answer"})
            assert json.loads(saved_exercise.json()["result"]["content"][0]["text"])["saved"] is True
            saved_analysis = rpc(client, key, "student_save_analysis", {**lesson, "note": "Synthetic private analysis"})
            assert json.loads(saved_analysis.json()["result"]["content"][0]["text"])["saved"] is True
            listed_analyses = rpc(client, key, "student_list_analyses")
            assert json.loads(listed_analyses.json()["result"]["content"][0]["text"])["analyses"][0]["chapter"] == 1
            retrieved_analysis = rpc(client, key, "student_get_analysis", lesson)
            assert json.loads(retrieved_analysis.json()["result"]["content"][0]["text"])["analysis"]["note"] == "Synthetic private analysis"
            assert client.get("/student/stats").json()["summary"]["exercises_saved"] == 1
            assert client.get("/student/stats").json()["summary"]["sources"]["mcp"] == 3
            assert client.get("/student/stats").json()["courses"][0]["ai_actions"] == 3
            assert client.get("/student/progress").json()["lessons"][0]["status"] == "completed"
            assert client.get("/student/analyses").json()["analyses"][0]["chapter"] == 1
            assert client.get("/student/stats", headers={"Authorization": f"Bearer {key}"}).status_code == 401
            assert client.get("/student/analyses", headers={"Authorization": f"Bearer {key}"}).status_code == 401
            assert client.get("/auth/mcp-keys", headers={"Authorization": f"Bearer {key}"}).status_code == 401
            assert client.get("/auth/mcp-keys").json()["keys"][0]["use_count"] == 6
            assert rpc(client, key + "x").status_code == 401

            second_cookie = "browser-session-for-student-two-token-123"
            db.conn.execute("INSERT INTO student_sessions (token_digest, user_id, created_at, expires_at) VALUES (?, ?, ?, ?)",
                            (student_auth.hashlib.sha256(second_cookie.encode()).hexdigest(), "student-two",
                             now[0], now[0] + student_auth.SESSION_LIFETIME))
            db.conn.commit()
            client.cookies.set(student_auth.COOKIE, second_cookie, domain="opencyber.academy")
            assert client.get("/auth/mcp-keys").json()["keys"] == []
            assert client.get("/student/progress").json() == {"lessons": [], "exercises": []}
            assert client.get("/student/analyses").json() == {"analyses": []}
            other_key = client.post("/auth/mcp-keys", json={"label": "Another student"}, headers=ORIGIN).json()["token"]
            assert json.loads(rpc(client, other_key, "student_get_analysis", lesson).json()["result"]["content"][0]["text"])["analysis"] is None
            assert client.delete(f"/auth/mcp-keys/{key_id}", headers=ORIGIN).status_code == 404
            client.cookies.set(student_auth.COOKIE, cookie_token, domain="opencyber.academy")
            assert client.delete(f"/auth/mcp-keys/{key_id}", headers=ORIGIN).status_code == 200
            assert rpc(client, key).status_code == 401

            expiring = client.post("/auth/mcp-keys", json={"label": "Temporary"}, headers=ORIGIN).json()["token"]
            for index in range(4):
                assert client.post("/auth/mcp-keys", json={"label": f"Agent {index}"}, headers=ORIGIN).status_code == 200
            assert client.post("/auth/mcp-keys", json={"label": "Too many"}, headers=ORIGIN).status_code == 409
            now[0] += student_auth.MCP_KEY_LIFETIME + 1
            assert rpc(client, expiring).status_code == 401
    finally:
        del api.app.state.catalog_override
        del api.app.state.source_override
        db.conn.close()
