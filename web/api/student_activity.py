"""Private, bounded learning events and per-student summaries in D1."""

from __future__ import annotations

import json
import secrets
from typing import Any


def rows(result: Any) -> list[dict]:
    if isinstance(result, dict):
        return result.get("results", [])
    from js import JSON  # type: ignore[import-not-found]
    return json.loads(str(JSON.stringify(result))).get("results", [])


async def record(db: Any, user_id: str, kind: str, level: str, area: str,
                 language: str, chapter: int, *, exercise_id: str | None = None,
                 seconds: int = 0, score: int | None = None) -> None:
    await db.prepare(
        "INSERT INTO student_activity (id, user_id, kind, level, area, language, chapter, exercise_id, seconds, score) "
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
    ).bind(secrets.token_urlsafe(18), user_id, kind, level, area, language,
           chapter, exercise_id, seconds, score).run()


async def summary(db: Any, user_id: str) -> dict:
    activity = rows(await db.prepare(
        "SELECT kind, COUNT(*) AS events, COALESCE(SUM(seconds), 0) AS seconds "
        "FROM student_activity WHERE user_id = ? GROUP BY kind"
    ).bind(user_id).all())
    lessons = rows(await db.prepare(
        "SELECT COUNT(*) AS total, SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) AS completed "
        "FROM lesson_progress WHERE user_id = ?"
    ).bind(user_id).all())[0]
    exercises = rows(await db.prepare(
        "SELECT COUNT(*) AS total FROM exercise_attempts WHERE user_id = ?"
    ).bind(user_id).all())[0]
    tests = rows(await db.prepare(
        "SELECT COUNT(*) AS total, COALESCE(SUM(score), 0) AS correct_answers "
        "FROM chapter_test_attempts WHERE user_id = ? AND status = 'complete'"
    ).bind(user_id).all())[0]
    notes = rows(await db.prepare(
        "SELECT COUNT(*) AS total FROM student_analysis WHERE user_id = ?"
    ).bind(user_id).all())[0]
    return {
        "activity": {item["kind"]: {"events": item["events"], "seconds": item["seconds"]} for item in activity},
        "lessons_marked": lessons["total"], "lessons_completed": lessons["completed"] or 0,
        "exercises_saved": exercises["total"], "tests_completed": tests["total"],
        "test_answers_correct": tests["correct_answers"], "analyses_saved": notes["total"],
    }


async def course_performance(db: Any, user_id: str) -> list[dict]:
    """Private per-edition study totals, with the best ten-question score per chapter."""
    courses: dict[tuple[str, str, str], dict] = {}

    def entry(row: dict) -> dict:
        key = (row["level"], row["area"], row["language"])
        return courses.setdefault(key, {"level": key[0], "area": key[1], "language": key[2],
                                        "lesson_visits": 0, "read_seconds": 0,
                                        "lessons_completed": 0, "exercises_saved": 0,
                                        "analyses_saved": 0, "chapters_tested": 0,
                                        "best_correct": 0, "best_possible": 0})

    activity = rows(await db.prepare(
        "SELECT level, area, language, "
        "SUM(CASE WHEN kind = 'lesson_opened' THEN 1 ELSE 0 END) AS lesson_visits, "
        "SUM(CASE WHEN kind = 'lesson_read' THEN seconds ELSE 0 END) AS read_seconds "
        "FROM student_activity WHERE user_id = ? GROUP BY level, area, language"
    ).bind(user_id).all())
    for row in activity:
        entry(row).update(lesson_visits=row["lesson_visits"], read_seconds=row["read_seconds"])

    for table, field, condition in (
        ("lesson_progress", "lessons_completed", "AND status = 'completed'"),
        ("exercise_attempts", "exercises_saved", ""),
        ("student_analysis", "analyses_saved", ""),
    ):
        result = rows(await db.prepare(
            f"SELECT level, area, language, COUNT(*) AS count FROM {table} "
            f"WHERE user_id = ? {condition} GROUP BY level, area, language"
        ).bind(user_id).all())
        for row in result:
            entry(row)[field] = row["count"]

    scores = rows(await db.prepare(
        "SELECT level, area, language, COUNT(*) AS chapters_tested, "
        "COALESCE(SUM(best_score), 0) AS best_correct "
        "FROM (SELECT level, area, language, chapter, MAX(score) AS best_score "
        "FROM chapter_test_attempts WHERE user_id = ? AND status = 'complete' "
        "GROUP BY level, area, language, chapter) GROUP BY level, area, language"
    ).bind(user_id).all())
    for row in scores:
        entry(row).update(chapters_tested=row["chapters_tested"], best_correct=row["best_correct"],
                          best_possible=row["chapters_tested"] * 10)
    return sorted(courses.values(), key=lambda item: (item["level"], item["area"], item["language"]))
