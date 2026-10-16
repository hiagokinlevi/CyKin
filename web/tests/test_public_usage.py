"""Public counters count consented browser activity without inventing people."""

import asyncio
import sqlite3
from pathlib import Path

import pytest
from fastapi import HTTPException

import public_usage


ROOT = Path(__file__).resolve().parents[2]
UNIT = "/courses/rapid-1-month/cybersecurity/chapters/en/1/"


class Statement:
    def __init__(self, connection, query, params=()):
        self.connection, self.query, self.params = connection, query, params

    def bind(self, *params):
        return Statement(self.connection, self.query, params)

    async def all(self):
        return {"results": [dict(row) for row in self.connection.execute(self.query, self.params)]}

    async def run(self):
        self.connection.execute(self.query, self.params)
        self.connection.commit()


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(":memory:")
        self.connection.row_factory = sqlite3.Row
        for migration in ("0002_chapter_tests.sql", "0003_student_auth.sql", "0008_public_usage.sql"):
            self.connection.executescript((ROOT / "web/migrations" / migration).read_text())

    def prepare(self, query):
        return Statement(self.connection, query)


def test_public_counts_deduplicate_and_retain_only_hashed_identifier(monkeypatch):
    db = Database()
    clock = [1_800_000_000]
    monkeypatch.setattr(public_usage.time, "time", lambda: clock[0])
    async def scenario():
        person = "a" * 32
        await public_usage.collect(db, visitor=person, event="view", path=UNIT, language="en")
        await public_usage.collect(db, visitor=person, event="view", path=UNIT, language="en")
        await public_usage.collect(db, visitor=person, event="read", path=UNIT, language="en")
        await public_usage.collect(db, visitor=person, event="exercise", path=UNIT,
                                   language="en", exercise_id="EX001")
        await public_usage.collect(db, visitor="b" * 32, event="view", path=UNIT, language="en")
        result = await public_usage.counts(db, path=UNIT, language="en", breakdown=True)
        assert result["site"] == {"views": 2, "reads": 1, "exercises": 1, "browsers": 2}
        assert result["page"] == result["course"] == result["site"]
        assert result["exercises_by_id"]["EX001"] == {"opens": 1, "browsers": 1}
        assert result["top_courses"][0]["label"] == "rapid-1-month/cybersecurity/en"
        assert result["top_pages"][0]["label"] == UNIT
        assert db.connection.execute("SELECT COUNT(*) FROM public_usage_events WHERE visitor_hash = ?", (person,)).fetchone()[0] == 0
        clock[0] += public_usage.RETENTION_SECONDS + 1
        expired = await public_usage.counts(db, path=UNIT, language="en")
        assert expired["site"]["views"] == 0
    asyncio.run(scenario())


def test_reading_and_exercise_events_require_real_unit_routes():
    db = Database()
    with pytest.raises(HTTPException):
        asyncio.run(public_usage.collect(db, visitor="a" * 32, event="read", path="/", language="en"))
    with pytest.raises(HTTPException):
        asyncio.run(public_usage.collect(db, visitor="a" * 32, event="exercise", path=UNIT,
                                         language="en", exercise_id="nope"))
    with pytest.raises(HTTPException):
        asyncio.run(public_usage.counts(db, path="/api/health", language="en"))


def test_course_portal_counts_follow_selected_edition():
    db = Database()
    portal = "/courses/rapid-1-month/cybersecurity/"
    asyncio.run(public_usage.collect(db, visitor="a" * 32, event="view", path=portal,
                                     language="en", edition="pt"))
    portuguese = asyncio.run(public_usage.counts(db, path=portal, language="en", edition="pt"))
    english = asyncio.run(public_usage.counts(db, path=portal, language="en"))
    assert portuguese["course"]["views"] == 1
    assert english["course"]["views"] == 0
    with pytest.raises(HTTPException):
        public_usage.classify(portal, "en", "zz")
