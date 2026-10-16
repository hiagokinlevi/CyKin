"""Consent-based, first-party usage counts for public learning pages.

Counts describe participating browsers, never people. No address, account,
query string, user agent, or raw browser identifier is persisted.
"""

from __future__ import annotations

import hashlib
import re
import time
from typing import Any

from fastapi import HTTPException

from student_activity import rows


RETENTION_SECONDS = 30 * 24 * 60 * 60
WINDOW_SECONDS = 30 * 60
PATH = re.compile(r"^/[a-zA-Z0-9/_-]{0,300}$")
COURSE = re.compile(r"^/courses/([a-z0-9-]+)/([a-z0-9-]+)(?:/(?:lessons|chapters)/([a-z]{2})/(\d+))?/?$")
UNIT = re.compile(r"^/courses/[a-z0-9-]+/[a-z0-9-]+/(?:lessons|chapters)/[a-z]{2}/\d+/$")
EXERCISE = re.compile(r"^EX\d{3,4}$")
VISITOR = re.compile(r"^[a-f0-9]{32}$")
LANGUAGES = {"en", "pt", "es", "he", "fr", "ru", "de", "zh", "ja"}


def classify(path: str, language: str, edition: str = "") -> tuple[str, str]:
    """Return canonical public path and its edition key, if any."""
    if not PATH.fullmatch(path) or "//" in path or "/../" in path:
        raise HTTPException(400, "Invalid public page")
    canonical = path.rstrip("/") + "/" if path != "/" else "/"
    match = COURSE.fullmatch(canonical)
    if match:
        selected = match.group(3) or edition or language
        if selected not in LANGUAGES:
            raise HTTPException(400, "Invalid course language")
        return canonical, f"{match.group(1)}/{match.group(2)}/{selected}"
    if canonical.startswith(("/courses/", "/student/", "/auth/", "/api/", "/mcp/")):
        raise HTTPException(400, "Invalid public page")
    return canonical, ""


async def collect(db: Any, *, visitor: str, event: str, path: str,
                  language: str, exercise_id: str = "", edition: str = "") -> None:
    if not VISITOR.fullmatch(visitor) or event not in {"view", "read", "exercise"}:
        raise HTTPException(400, "Invalid usage event")
    canonical, course = classify(path, language, edition)
    if event in {"read", "exercise"} and not UNIT.fullmatch(canonical):
        raise HTTPException(400, "This event requires an authored lesson page")
    if event == "exercise" and not EXERCISE.fullmatch(exercise_id):
        raise HTTPException(400, "Invalid exercise")
    if event != "exercise" and exercise_id:
        raise HTTPException(400, "Unexpected exercise")
    now = int(time.time())
    # An address can be loaded repeatedly. Count at most once per half-hour
    # per participating browser, page and action.
    await db.prepare(
        "INSERT OR IGNORE INTO public_usage_events "
        "(visitor_hash, event, path, course_key, exercise_id, window_start, occurred_at) "
        "VALUES (?, ?, ?, ?, ?, ?, ?)"
    ).bind(hashlib.sha256(visitor.encode()).hexdigest(), event, canonical, course,
           exercise_id, now // WINDOW_SECONDS * WINDOW_SECONDS, now).run()
    await db.prepare("DELETE FROM public_usage_events WHERE occurred_at < ?").bind(now - RETENTION_SECONDS).run()


async def counts(db: Any, *, path: str = "/", language: str = "en",
                 exercise_id: str = "", breakdown: bool = False, edition: str = "") -> dict[str, Any]:
    canonical, course = classify(path, language, edition)
    if exercise_id and (not UNIT.fullmatch(canonical) or not EXERCISE.fullmatch(exercise_id)):
        raise HTTPException(400, "Invalid exercise")
    since = int(time.time()) - RETENTION_SECONDS

    async def aggregate(where: str, values: tuple[Any, ...]) -> dict:
        result = rows(await db.prepare(
            "SELECT COALESCE(SUM(CASE WHEN event = 'view' THEN 1 ELSE 0 END), 0) AS views, "
            "COALESCE(SUM(CASE WHEN event = 'read' THEN 1 ELSE 0 END), 0) AS reads, "
            "COALESCE(SUM(CASE WHEN event = 'exercise' THEN 1 ELSE 0 END), 0) AS exercises, "
            "COUNT(DISTINCT CASE WHEN event = 'view' THEN visitor_hash END) AS browsers "
            f"FROM public_usage_events WHERE occurred_at >= ? {where}"
        ).bind(since, *values).all())[0]
        return {key: int(result.get(key) or 0) for key in ("views", "reads", "exercises", "browsers")}

    site = await aggregate("", ())
    page = await aggregate("AND path = ?", (canonical,))
    course_counts = await aggregate("AND course_key = ?", (course,)) if course else None
    exercise_counts = await aggregate("AND path = ? AND exercise_id = ?", (canonical, exercise_id)) if exercise_id else None
    exercise_rows = rows(await db.prepare(
        "SELECT exercise_id, COUNT(*) AS opens, COUNT(DISTINCT visitor_hash) AS browsers "
        "FROM public_usage_events WHERE occurred_at >= ? AND path = ? "
        "AND event = 'exercise' GROUP BY exercise_id"
    ).bind(since, canonical).all()) if UNIT.fullmatch(canonical) else []
    learners = rows(await db.prepare("SELECT COUNT(*) AS total FROM student_accounts").all())[0]
    attempts = rows(await db.prepare(
        "SELECT COUNT(*) AS total FROM chapter_test_attempts WHERE status = 'complete'"
    ).all())[0]
    result = {"window_days": 30, "method": "opt_in_browsers", "site": site,
            "page": page, "course": course_counts, "exercise": exercise_counts,
            "exercises_by_id": {row["exercise_id"]: {"opens": int(row["opens"]),
                                               "browsers": int(row["browsers"])} for row in exercise_rows},
            "registered_learners": int(learners.get("total") or 0),
            "tests_completed": int(attempts.get("total") or 0)}
    if breakdown:
        metrics = (
            "COUNT(DISTINCT CASE WHEN event = 'view' THEN visitor_hash END) AS browsers, "
            "SUM(CASE WHEN event = 'view' THEN 1 ELSE 0 END) AS views, "
            "SUM(CASE WHEN event = 'read' THEN 1 ELSE 0 END) AS reads, "
            "SUM(CASE WHEN event = 'exercise' THEN 1 ELSE 0 END) AS exercises "
        )
        for column, name, predicate in (
            ("course_key", "top_courses", "AND course_key != ''"),
            ("path", "top_pages", ""),
        ):
            data = rows(await db.prepare(
                f"SELECT {column} AS label, {metrics} FROM public_usage_events "
                f"WHERE occurred_at >= ? {predicate} GROUP BY {column} "
                "ORDER BY views DESC, reads DESC LIMIT 12"
            ).bind(since).all())
            result[name] = [{"label": str(row["label"]), **{
                key: int(row.get(key) or 0) for key in ("browsers", "views", "reads", "exercises")
            }} for row in data]
    return result
