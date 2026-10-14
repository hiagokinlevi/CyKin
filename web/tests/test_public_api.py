"""The public course route must never confuse an outline with a lesson."""

import json
import hashlib
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app import app, chapter_sections, worked_answers


ROOT = Path(__file__).resolve().parents[2]


@pytest.fixture
def client():
    app.state.catalog_override = json.loads((ROOT / "web/public/catalog.json").read_text())

    async def local_source(path):
        target = ROOT / path
        return target.read_text(encoding="utf-8") if target.is_file() else None

    app.state.source_override = local_source
    try:
        yield TestClient(app)
    finally:
        del app.state.catalog_override
        del app.state.source_override


def test_public_guide_and_lesson(client):
    catalog = client.get("/api/catalog")
    assert catalog.status_code == 200
    assert len(catalog.json()["courses"]) == 207
    rapid = next(course for course in catalog.json()["courses"] if course["level"] == "rapid-1-month")
    engineering = next(course for course in catalog.json()["courses"] if course["level"] == "engineering-5-years")
    assert (rapid["instructional_weeks"], rapid["daily_lesson_target"]) == (4, 20)
    assert (engineering["instructional_weeks"], engineering["daily_lesson_target"]) == (260, 1300)
    assert "minimum_a4_pages" not in rapid
    assert "minimum_exercises" not in rapid

    guide = client.get("/api/courses/rapid-1-month/incident-response-resilience/en")
    assert guide.status_code == 200
    assert guide.json()["planned_chapters"] == 4
    assert guide.json()["published_chapters"] == 4
    assert guide.json()["planned_lessons"] == guide.json()["published_lessons"] == 20
    assert [lesson["chapter"] for lesson in guide.json()["lessons"]] == list(range(1, 21))
    assert [(module["kind"], module["number"], module["chapters"]) for module in guide.json()["modules"]] == [
        ("Chapter", number, list(range((number - 1) * 5 + 1, number * 5 + 1))) for number in range(1, 5)
    ]
    assert guide.json()["lessons"][0]["subject"] == "Incident readiness, roles and authorized scope"
    assert guide.json()["daily_schedule_ready"] is True
    assert len(guide.json()["legacy_chapters"]) == 4
    assert guide.json()["legacy_chapters"][0]["published"] is True

    lesson = client.get("/api/lessons/rapid-1-month/incident-response-resilience/en/1")
    assert lesson.status_code == 200
    assert lesson.json()["title"] == "Evidence readiness and the first case question"
    assert lesson.json()["next"] == 2
    assert lesson.json()["week_chapter"] == 1
    assert lesson.json()["exercise_ids"] == ["001"]
    assert "EX001" in lesson.json()["worked_answers"]
    assert "EX002" not in lesson.json()["worked_answers"]
    assert client.get("/api/chapters/rapid-1-month/incident-response-resilience/en/1").status_code == 200


def test_unwritten_chapter_is_not_served_as_lesson(client):
    guide = client.get("/api/courses/rapid-1-month/cybersecurity/en").json()
    assert guide["planned_chapters"] == 10
    assert guide["published_chapters"] == 10
    assert guide["lessons"][3]["published"] is True
    assert guide["lessons"][9]["published"] is True
    response = client.get("/api/lessons/rapid-1-month/cybersecurity/en/11")
    assert response.status_code == 404
    assert response.json()["detail"] == "This chapter is still a plan"


def test_full_book_and_internal_reference_source(client):
    book = client.get('/api/books/rapid-1-month/incident-response-resilience/en')
    assert book.status_code == 200
    assert '<a id="ch-01"></a>' in book.text
    assert '<a id="answers"></a>' in book.text
    assert book.headers['x-opencyberacademy-source-sha256'] == hashlib.sha256(book.content).hexdigest()

    plan = client.get('/api/source', params={
        'path': 'levels/rapid-1-month/incident-response-resilience/en/book/PLAN.md',
    })
    assert plan.status_code == 200
    assert '<a id="ch-01"></a>' in plan.text
    for forbidden in ('../README.md', '/README.md', 'levels//README.md', 'missing.md'):
        assert client.get('/api/source', params={'path': forbidden}).status_code == 404


def test_stateless_mcp_public_and_progress_private(client):
    headers = {"Content-Type": "application/json", "Accept": "application/json, text/event-stream"}
    initialize = client.post("/mcp", headers=headers, json={"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {}})
    assert initialize.status_code == 200
    assert initialize.json()["result"]["protocolVersion"] == "2025-06-18"
    tools = client.post("/mcp", headers=headers, json={"jsonrpc": "2.0", "id": 2, "method": "tools/list"})
    assert {tool["name"] for tool in tools.json()["result"]["tools"]} == {"list_courses", "list_lessons", "read_lesson", "read_chapter", "search_course"}
    assert client.post("/mcp", headers={**headers, "Origin": "https://evil.example"}, json={"jsonrpc": "2.0", "id": 3, "method": "ping"}).status_code == 403
    assert client.get("/private/me").status_code == 503
    assert client.post("/private/progress/lesson", json={"level": "rapid-1-month", "area": "cybersecurity", "language": "en", "chapter": 1, "status": "completed"}).status_code == 403


def test_long_course_chapter_and_exercise_numbers():
    book = '<a id="ch-1300"></a>\n## Lesson 1300\n\n### Exercise EX1300\nSolve it.\n\n## Worked answers\n\n### EX1300\nA worked answer.\n'
    chapter = chapter_sections(book)[1300]["markdown"]
    assert "EX1300" in chapter
    assert "A worked answer" in worked_answers(book, chapter)


def test_weekly_chapters_group_130_daily_lessons_into_26_weeks(client):
    plan = "\n\n".join(
        f'<a id="ch-{week:02d}"></a>\n## Chapter {week}\n' +
        "\n".join(f'<a id="lesson-{n:02d}"></a>\n### Lesson {n}' for n in range((week - 1) * 5 + 1, week * 5 + 1))
        for week in range(1, 27)
    )
    book = '<a id="ch-20"></a>\n## Chapter 20\n<a id="lesson-100"></a>\n### Lesson 100\n\n#### Practice\n\n##### EX1000 — Test\nSolve it.\n\n## Worked answers\n\n### EX1000\nWorked result.\n'

    async def source(path):
        if path.endswith('/book/PLAN.md'):
            return plan
        if path.endswith('/book/MANUSCRIPT.md'):
            return book
        return None

    original_source = app.state.source_override
    app.state.source_override = source
    try:
        guide = client.get('/api/courses/professional-6-months/incident-response-resilience/en').json()
        assert guide['daily_schedule_ready'] is True
        assert len(guide['modules']) == 26
        assert guide['modules'][19]['chapters'] == [96, 97, 98, 99, 100]
        assert guide['published_chapters'] == 1
        assert guide['published_lessons'] == 1
        assert guide['planned_lessons'] == 130
        lesson = client.get('/api/lessons/professional-6-months/incident-response-resilience/en/100').json()
        assert lesson['exercise_ids'] == ['1000']
        assert lesson['week_chapter'] == 20
        assert 'Worked result' in lesson['worked_answers']
    finally:
        app.state.source_override = original_source


def test_partial_daily_conversion_keeps_chapters_and_reads_new_public_text(client):
    path = 'levels/professional-6-months/incident-response-resilience/en/book/MANUSCRIPT.md'
    original_source = app.state.source_override
    revised = None

    async def source(filename):
        text = await original_source(filename)
        if filename == path and revised is not None:
            return revised
        return text

    app.state.source_override = source
    try:
        guide = client.get('/api/courses/professional-6-months/incident-response-resilience/en').json()
        assert guide['planned_lessons'] == 130
        assert guide['published_lessons'] == 10
        assert guide['published_chapters'] == 12
        assert [day['published'] for day in guide['daily_slots'][:11]] == [True] * 10 + [False]
        assert len(guide['legacy_chapters']) == 12

        day = client.get('/api/lessons/professional-6-months/incident-response-resilience/en/1')
        assert day.status_code == 200
        assert day.headers['cache-control'] == 'no-store'
        assert day.json()['content_kind'] == 'daily_lesson'
        assert day.json()['source_sha256'] == hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
        assert '#week-01-day-01' in day.json()['source_url']
        assert '<a id="exercise-ex001"></a>' in day.json()['markdown']
        assert '<a id="answer-ex001"></a>' in day.json()['worked_answers']
        assert 'answer-ex002' not in day.json()['worked_answers']

        chapter = client.get('/api/chapters/professional-6-months/incident-response-resilience/en/2')
        assert chapter.status_code == 200
        assert chapter.json()['content_kind'] == 'legacy_chapter'
        assert 'EX006' in chapter.json()['markdown']
        second_week = client.get('/api/lessons/professional-6-months/incident-response-resilience/en/6')
        assert second_week.status_code == 200
        assert second_week.json()['content_kind'] == 'daily_lesson'
        assert '#week-02-day-01' in second_week.json()['source_url']
        assert '<a id="exercise-ex006"></a>' in second_week.json()['markdown']
        assert '<a id="answer-ex006"></a>' in second_week.json()['worked_answers']
        assert client.get('/api/lessons/professional-6-months/incident-response-resilience/en/11').status_code == 404

        original = (ROOT / path).read_text(encoding='utf-8')
        revised = original.replace('The write path and the observation path have different failure points:', 'The updated write path and observation path have different failure points:', 1)
        assert revised != original
        updated = client.get('/api/lessons/professional-6-months/incident-response-resilience/en/1').json()
        assert 'updated write path' in updated['markdown']
        assert updated['content_sha256'] != day.json()['content_sha256']
    finally:
        app.state.source_override = original_source
