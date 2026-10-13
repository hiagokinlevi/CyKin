"""Public, read-only daily study views over the single canonical course book.

Editorial responsibility: hiagokinlevi. No progress writes or deployments.
A mapping is not a new manuscript, review certificate or learner completion.
"""
from __future__ import annotations

import asyncio
import calendar
import hashlib
import json
import re
from datetime import date, timedelta
from typing import Any

from fastapi import HTTPException, Query, Request

POLICY_PATH = "DAILY_STUDY_STANDARD.md"
VIEW = "https://github.com/hiagokinlevi/CyKin/blob/main/"
LANGUAGES = ("en", "pt", "es", "he", "fr", "ru", "de", "zh", "ja")


def json_block(text: str, name: str) -> dict[str, Any]:
    start, end = f"<!-- cykin:{name}:start -->", f"<!-- cykin:{name}:end -->"
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError("Missing or duplicated manifest boundary")
    body = text.split(start, 1)[1].split(end, 1)[0].strip()
    if not body.startswith("```json\n") or not body.endswith("\n```"):
        raise ValueError("Manifest must contain one JSON code block")
    def no_duplicates(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError("Duplicate manifest key: " + key)
            result[key] = value
        return result
    result = json.loads(body[8:-4], object_pairs_hook=no_duplicates)
    if not isinstance(result, dict) or type(result.get("schema")) is not int or result.get("schema") != 1:
        raise ValueError("Unsupported manifest schema")
    return result


def policy_level(text: str, level: str) -> dict[str, int]:
    policy = json_block(text, "daily-policy")
    if policy.get("weekdays") != [0, 1, 2, 3, 4] or policy.get("languages") != list(LANGUAGES):
        raise ValueError("Unsupported weekday or language policy")
    item = policy.get("levels", {}).get(level)
    if not isinstance(item, dict):
        raise ValueError("Unknown level in daily policy")
    for field in ("months", "reference_lessons", "chapters", "planned_hours"):
        if type(item.get(field)) is not int or item[field] <= 0:
            raise ValueError("Invalid level field: " + field)
    if item["months"] > 120 or item["reference_lessons"] != (item["months"] * 260 + 11) // 12:
        raise ValueError("Inconsistent reference duration")
    return item


def calendar_plan(start: str | None, months: int, lessons: int) -> dict[str, Any]:
    """Civil dates only; no host timezone, DST, holidays or guessed recesses."""
    if start is None:
        return {"first_study_date": None, "period_end_exclusive": None,
                "calendar_weekdays": None, "sequence_end": None,
                "alignment": "undated", "dates": [None] * lessons}
    if not re.fullmatch(r"[0-9]{4}-[0-9]{2}-[0-9]{2}", start):
        raise ValueError("Use a YYYY-MM-DD start date")
    first = date.fromisoformat(start)
    if not 1900 <= first.year <= 2090:
        raise ValueError("Start year must be between 1900 and 2090")
    while first.weekday() >= 5:
        first += timedelta(days=1)
    year, month0 = divmod(first.year * 12 + first.month - 1 + months, 12)
    end = date(year, month0 + 1, min(first.day, calendar.monthrange(year, month0 + 1)[1]))
    cursor, period_dates = first, []
    while cursor < end:
        if cursor.weekday() < 5:
            period_dates.append(cursor.isoformat())
        cursor += timedelta(days=1)
    dates, cursor = [], first
    while len(dates) < lessons:
        if cursor.weekday() < 5:
            dates.append(cursor.isoformat())
        cursor += timedelta(days=1)
    return {"requested_start": start, "first_study_date": first.isoformat(),
            "period_end_exclusive": end.isoformat(), "calendar_weekdays": len(period_dates),
            "sequence_end": dates[-1] if dates else None,
            "alignment": "aligned" if len(period_dates) == lessons else "review_required",
            "difference_days": len(period_dates) - lessons, "dates": dates}


def heading_index(book: str) -> list[tuple[int, int, str]]:
    """Index ATX headings outside fenced code; never interpret a code example as a lesson."""
    result, offset, fence = [], 0, None
    for line in book.splitlines(keepends=True):
        raw = line.rstrip("\r\n")
        marker = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", raw)
        if fence is not None:
            if marker and marker[1][0] == fence[0] and len(marker[1]) >= fence[1] and not marker[2].strip():
                fence = None
        elif marker:
            fence = (marker[1][0], len(marker[1]))
        elif match := re.match(r"^(#{1,6})\s+\S", raw):
            result.append((offset, len(match[1]), raw))
        offset += len(line)
    if fence is not None:
        raise ValueError("Unclosed source code fence")
    return result


def unique_heading(index: list[tuple[int, int, str]], name: str) -> tuple[int, int, str]:
    found = [entry for entry in index if entry[2] == name]
    if len(found) != 1:
        raise ValueError("Missing or ambiguous heading: " + name)
    return found[0]


def section(book: str, index: list[tuple[int, int, str]], heading: tuple[int, int, str]) -> str:
    begin, depth, _ = heading
    end = next((pos for pos, level, _ in index if pos > begin and level <= depth), len(book))
    return book[begin:end].strip()


def git_blob_sha(text: str) -> str:
    data = text.encode("utf-8")
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def mapped_units(text: str, book: str, *, level: str, area: str, language: str,
                 chapters: int) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    plan = json_block(text, "daily-plan")
    if (plan.get("level"), plan.get("area"), plan.get("language")) != (level, area, language):
        raise ValueError("Manifest belongs to another course or language")
    if plan.get("state") != "mapped-draft" or not isinstance(plan.get("lessons"), list):
        raise ValueError("Only explicit mapped-draft manifests are supported in version 1")
    if not re.fullmatch(r"[0-9a-f]{40}", str(plan.get("source_blob_sha", ""))):
        raise ValueError("Missing source revision")
    if git_blob_sha(book) != plan["source_blob_sha"]:
        raise ValueError("SOURCE_CHANGED: revalidate the daily mapping")
    lessons = plan["lessons"]
    if not lessons or len(lessons) > 3000:
        raise ValueError("Invalid daily allocation size")
    index, units, used_exercises = heading_index(book), [], set()
    anchors = list(re.finditer(r'^<a id="ch-([0-9]{2})"></a>\s*$', book, re.M))
    if len({m[1] for m in anchors}) != len(anchors):
        raise ValueError("Duplicate chapter anchors")
    answer_anchor = book.find('<a id="answers"></a>')
    if answer_anchor < 0:
        raise ValueError("Missing final answer appendix")
    previous_chapter, previous_end = 0, -1
    for number, entry in enumerate(lessons, 1):
        if not isinstance(entry, dict) or entry.get("id") != f"D{number:04d}":
            raise ValueError("Daily IDs must be unique and consecutive")
        chapter = entry.get("chapter")
        if type(chapter) is not int or not previous_chapter <= chapter <= chapters or chapter < 1:
            raise ValueError("Invalid chapter order")
        if not isinstance(entry.get("title"), str) or not entry["title"].strip():
            raise ValueError("Missing daily title")
        begin = unique_heading(index, entry.get("start", ""))[0]
        end = unique_heading(index, entry.get("end", ""))[0]
        chapter_anchor = next((m for m in anchors if int(m[1]) == chapter), None)
        chapter_end = next((m.start() for m in anchors if int(m[1]) > chapter), answer_anchor)
        if chapter_anchor is None or not chapter_anchor.start() <= begin < end <= chapter_end or begin < previous_end:
            raise ValueError("Overlapping, reversed or out-of-chapter reading")
        example_heading = unique_heading(index, entry.get("example", ""))
        if not chapter_anchor.start() <= example_heading[0] < chapter_end:
            raise ValueError("Example belongs to another chapter")
        exercise_ids = entry.get("exercises")
        if not isinstance(exercise_ids, list) or not exercise_ids:
            raise ValueError("A day needs its own exercise")
        pairs = []
        for exercise_id in exercise_ids:
            if not isinstance(exercise_id, str) or not re.fullmatch(r"EX[0-9]{3,}", exercise_id) or exercise_id in used_exercises:
                raise ValueError("Invalid or reused exercise allocation")
            if int(exercise_id[2:]) < 1 or exercise_id != f"EX{int(exercise_id[2:]):03d}":
                raise ValueError("Noncanonical exercise ID")
            used_exercises.add(exercise_id)
            prompt = [h for h in index if h[1] == 4 and re.match(r"^#### " + re.escape(exercise_id) + r"\b", h[2])]
            answer = [h for h in index if h[1] == 3 and re.match(r"^### " + re.escape(exercise_id) + r"\b", h[2])]
            if len(prompt) != 1 or len(answer) != 1 or not chapter_anchor.start() <= prompt[0][0] < chapter_end or answer[0][0] < answer_anchor:
                raise ValueError("Missing, ambiguous or misplaced exercise/answer: " + exercise_id)
            prompt_text, answer_text = section(book, index, prompt[0]), section(book, index, answer[0])
            if not all("\n" in text and text.split("\n", 1)[1].strip() for text in (prompt_text, answer_text)):
                raise ValueError("Empty exercise or answer: " + exercise_id)
            pairs.append({"id": exercise_id, "prompt": prompt_text, "answer": answer_text})
        if not book[begin:end].split("\n", 1)[-1].strip():
            raise ValueError("Empty daily reading")
        example_text = section(book, index, example_heading)
        if "\n" not in example_text or not example_text.split("\n", 1)[1].strip():
            raise ValueError("Empty example")
        units.append({"id": entry["id"], "day": number, "chapter": chapter,
                      "title": entry["title"], "state": "mapped-draft",
                      "markdown": book[begin:end].strip(),
                      "example": example_text, "exercises": pairs,
                      "source_line_start": book.count("\n", 0, begin) + 1,
                      "source_line_end": book.count("\n", 0, end)})
        previous_chapter, previous_end = chapter, end
    return plan, units


def install_daily_routes(app, *, catalog, get_course, source_text) -> None:
    """Register before the application's catch-all static route. Reuse its source and RBAC boundaries."""
    async def load(request, level, area, language):
        get_course(await catalog(request), level, area, language)
        policy_text, plan_text = await asyncio.gather(
            source_text(request, POLICY_PATH),
            source_text(request, f"levels/{level}/{area}/{language}/DAILY_PLAN.md"),
        )
        if policy_text is None:
            raise HTTPException(503, "Daily-study policy is unavailable")
        try:
            profile = policy_level(policy_text, level)
        except (ValueError, TypeError, KeyError) as exc:
            raise HTTPException(502, "Invalid daily-study policy") from exc
        result = {"profile": profile, "units": [], "mapping_state": "not_mapped", "mapping_issue": None,
                  "source_blob_sha": None, "source_url": VIEW + f"levels/{level}/{area}/{language}/book/MANUSCRIPT.md"}
        if plan_text is not None:
            book = await source_text(request, f"levels/{level}/{area}/{language}/book/MANUSCRIPT.md")
            if book is None:
                result.update(mapping_state="blocked", mapping_issue="MANUSCRIPT_UNAVAILABLE")
            else:
                try:
                    plan, units = mapped_units(plan_text, book, level=level, area=area,
                                               language=language, chapters=profile["chapters"])
                    result.update(units=units, mapping_state="mapped-draft", source_blob_sha=plan["source_blob_sha"])
                except (ValueError, TypeError, KeyError) as exc:
                    result.update(mapping_state="blocked", mapping_issue=str(exc))
        return result

    @app.get("/api/daily/{level}/{area}/{language}")
    async def daily_plan(request: Request, level: str, area: str, language: str,
                         start: str | None = Query(default=None, max_length=10)) -> dict:
        data = await load(request, level, area, language)
        profile, units = data["profile"], data["units"]
        total = max(profile["reference_lessons"], len(units))
        try:
            dates = calendar_plan(start, profile["months"], total)
        except ValueError as exc:
            raise HTTPException(422, str(exc)) from exc
        slots = []
        for n in range(1, total + 1):
            unit = units[n - 1] if n <= len(units) else None
            # Balanced placement is only a planning fallback, never authored teaching.
            chapter = unit["chapter"] if unit else max(units[-1]["chapter"] if units else 1,
                       min(profile["chapters"], ((n - 1) * profile["chapters"] // total) + 1))
            if dates["dates"][n - 1] is not None:
                actual_day = date.fromisoformat(dates["dates"][n - 1])
                first = date.fromisoformat(dates["first_study_date"])
                monday = first - timedelta(days=first.weekday())
                week, weekday = (actual_day - monday).days // 7 + 1, actual_day.weekday() + 1
            else:
                week, weekday = (n - 1) // 5 + 1, (n - 1) % 5 + 1
            slots.append({"day": n, "id": f"D{n:04d}", "chapter": chapter,
                          "week": week, "study_day": weekday,
                          "date": dates["dates"][n - 1], "title": unit["title"] if unit else None,
                          "state": "mapped-draft" if unit else "planned",
                          "exercise_ids": [x["id"] for x in unit["exercises"]] if unit else []})
        return {"level": level, "area": area, "language": language, **profile,
                "planned_daily_positions": total, "mapped_draft_readings": len(units),
                "native_daily_lessons": 0, "reviewed_daily_lessons": 0,
                "mapping_state": data["mapping_state"], "mapping_issue": data["mapping_issue"],
                "source_blob_sha": data["source_blob_sha"], "calendar": {k: v for k, v in dates.items() if k != "dates"},
                "days": slots, "policy_url": VIEW + POLICY_PATH,
                "notice": "Mapped readings reuse the one book; slots, code checks and chapter progress do not certify daily review or learner completion."}

    @app.get("/api/daily/{level}/{area}/{language}/{day}")
    async def daily_lesson(request: Request, level: str, area: str, language: str, day: int) -> dict:
        if day < 1 or day > 3000:
            raise HTTPException(404, "Unknown study day")
        data = await load(request, level, area, language)
        if data["mapping_state"] == "blocked":
            raise HTTPException(409, "Daily mapping needs source review: " + str(data["mapping_issue"]))
        if day > len(data["units"]):
            raise HTTPException(404, "Daily teaching is not mapped in this language; no English substitution")
        return {**data["units"][day - 1], "language": language,
                "source_url": data["source_url"], "source_blob_sha": data["source_blob_sha"],
                "previous": day - 1 if day > 1 else None,
                "next": day + 1 if day < max(data["profile"]["reference_lessons"], len(data["units"])) else None,
                "editorial_note": "Mapped draft reading; daily workload, specialist and language review remain pending. No learner completion is inferred."}
