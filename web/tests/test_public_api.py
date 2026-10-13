"""The public course route must never confuse an outline with a lesson."""

import json
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

from app import app


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

    guide = client.get("/api/courses/rapid-1-month/incident-response-resilience/en")
    assert guide.status_code == 200
    assert guide.json()["planned_chapters"] == 4
    assert guide.json()["published_chapters"] == 4
    assert [lesson["chapter"] for lesson in guide.json()["lessons"]] == [1, 2, 3, 4]

    lesson = client.get("/api/lessons/rapid-1-month/incident-response-resilience/en/1")
    assert lesson.status_code == 200
    assert "Incident readiness" in lesson.json()["title"]
    assert lesson.json()["next"] == 2
    assert lesson.json()["exercise_ids"]
    assert "EX001" in lesson.json()["worked_answers"]


def test_unwritten_chapter_is_not_served_as_lesson(client):
    guide = client.get("/api/courses/rapid-1-month/cybersecurity/en").json()
    assert guide["planned_chapters"] == 4
    assert guide["published_chapters"] == 3
    assert guide["lessons"][3]["published"] is False
    response = client.get("/api/lessons/rapid-1-month/cybersecurity/en/4")
    assert response.status_code == 404


def test_full_book_and_internal_reference_source(client):
    book = client.get('/api/books/rapid-1-month/incident-response-resilience/en')
    assert book.status_code == 200
    assert '<a id="ch-01"></a>' in book.text
    assert '<a id="answers"></a>' in book.text

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
    assert {tool["name"] for tool in tools.json()["result"]["tools"]} == {"list_courses", "list_lessons", "read_lesson", "search_course"}
    assert client.post("/mcp", headers={**headers, "Origin": "https://evil.example"}, json={"jsonrpc": "2.0", "id": 3, "method": "ping"}).status_code == 403
    assert client.get("/private/me").status_code == 503
    assert client.post("/private/progress/lesson", json={"level": "rapid-1-month", "area": "cybersecurity", "language": "en", "chapter": 1, "status": "completed"}).status_code == 403
