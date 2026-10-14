"""Read-only OpenCyber Academy REST and stateless MCP API for Cloudflare Python Workers."""

from __future__ import annotations

import asyncio
import hashlib
import json
import re
import time
from pathlib import Path
from typing import Any
from urllib.error import HTTPError
from urllib.request import urlopen

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse, PlainTextResponse, RedirectResponse, Response
from pydantic import BaseModel, Field

from access import identity
from locales import ACTIVE_INTERFACES, LANGUAGES, language_for_host, preferred_language, site_for_language
from seo_pages import lesson_path, render_lesson_page, render_planned_lesson_page


app = FastAPI(title="OpenCyber Academy public learning API", version="0.1.0", docs_url="/api/docs", openapi_url="/api/openapi.json")
GITHUB_RAW = "https://raw.githubusercontent.com/hiagokinlevi/OpenCyberAcademy/main/"
GITHUB_VIEW = "https://github.com/hiagokinlevi/OpenCyberAcademy/blob/main/"
CATALOG_PATH = Path(__file__).resolve().parents[1] / "public" / "catalog.json"
ANCHOR = re.compile(r'^<a id="ch-(\d{2,4})"></a>\s*$', re.M)
LESSON_ANCHOR = re.compile(r'^<a id="lesson-(\d{2,4})"></a>\s*$', re.M)
WEEK_DAY_ANCHOR = re.compile(r'^<a id="week-(\d{2,4})-day-(\d{2})"></a>\s*$', re.M)
EXERCISE = re.compile(r'\bEX(\d{3,4})\b')
EXERCISE_HEADING = re.compile(r'^#{3,6}\s+EX(\d{3,4})\b', re.M)
ANSWER = re.compile(r'^###\s+EX(\d{3,4})\b.*$|^\*\*EX(\d{3,4})\s+[—-]\s+.*$', re.M)
APPENDIX_HEADING = re.compile(
    r'^##\s+(?:final\s+appendix\s+[—–:-]\s+)?'
    r'(?:worked\s+(?:results|answers)|answer\s+key|gabarito|respostas|resultados(?:\s+resueltos)?|soluciones|resoluciones)\b',
    re.M | re.I,
)
REFERENCES_HEADING = re.compile(r'^##\s+(?:references|referências|referencias)\b', re.M | re.I)
MCP_VERSION = "2025-06-18"
EDITORIAL_POLICY_URI = "open-cyber-academy://editorial-policy"
ALLOWED_ORIGINS = {site_for_language(language) for language in LANGUAGES} | {"https://www.opencyber.academy", "http://localhost:4321", "http://localhost:8787", "http://127.0.0.1:8787"}
MAX_SOURCE_CHARS = 24_000_000
PUBLIC_ORIGINS = {site_for_language(language) for language in LANGUAGES} | {"https://www.opencyber.academy"}


class LessonProgress(BaseModel):
    level: str = Field(pattern=r"^[a-z0-9-]+$", max_length=50)
    area: str = Field(pattern=r"^[a-z0-9-]+$", max_length=80)
    language: str = Field(pattern=r"^[a-z]{2}$")
    chapter: int = Field(ge=1, le=9999)
    status: str = Field(pattern=r"^(in_progress|completed)$")


class ExerciseAttempt(LessonProgress):
    exercise_id: str = Field(pattern=r"^EX[0-9]{3,4}$")
    answer: str = Field(default="", max_length=20_000)
    status: str = Field(pattern=r"^(attempted|completed)$")


@app.middleware("http")
async def canonical_domain(request: Request, call_next):
    host = request.headers.get("host", "")
    if host == "www.opencyber.academy":
        return RedirectResponse("https://opencyber.academy" + request.url.path + ("?" + request.url.query if request.url.query else ""), status_code=308)
    host_language = language_for_host(host)
    if host_language == "en" and request.url.path == "/" and not request.query_params:
        preferred = preferred_language(request.headers.get("accept-language", ""))
        if preferred != "en":
            return RedirectResponse(site_for_language(preferred) + "/", status_code=302,
                                    headers={"Vary": "Accept-Language", "Cache-Control": "private, no-store"})
    match = re.fullmatch(r"/courses/[^/]+/[^/]+/(?:lessons|chapters)/([a-z]{2})/\d+/?", request.url.path)
    if host_language and match and match.group(1) in LANGUAGES and match.group(1) != host_language:
        return RedirectResponse(site_for_language(match.group(1)) + request.url.path, status_code=308)
    response = await call_next(request)
    if request.url.path.startswith(("/api/", "/mcp")):
        response.headers["Cache-Control"] = "no-store"
        response.headers["X-Robots-Tag"] = "noindex"
    if request.url.path.startswith("/private/"):
        response.headers["X-Robots-Tag"] = "noindex"
    return response


def same_origin(request: Request) -> None:
    origin = request.headers.get("origin", "")
    if origin not in PUBLIC_ORIGINS:
        raise HTTPException(403, "A progress update must come from the OpenCyber Academy site")


def database(request: Request):
    env = request.scope.get("env")
    db = getattr(env, "DB", None)
    if db is None:
        raise HTTPException(503, "Student progress storage is not configured")
    return db


def d1_rows(result: Any) -> list[dict]:
    if isinstance(result, dict):
        return result.get("results", [])
    from js import JSON  # type: ignore[import-not-found]
    return json.loads(str(JSON.stringify(result))).get("results", [])


async def catalog(request: Request) -> dict[str, Any]:
    """The static catalog lists all courses; selected books are fetched live."""
    if override := getattr(app.state, "catalog_override", None):
        return override
    env = request.scope.get("env")
    if env is not None:
        response = await env.ASSETS.fetch("https://assets.local/catalog.json")
        if int(response.status) != 200:
            raise HTTPException(503, "Catalog asset is unavailable")
        return json.loads(str(await response.text()))
    return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))


def get_course(data: dict[str, Any], level: str, area: str, language: str) -> dict[str, Any]:
    if language not in data["languages"]:
        raise HTTPException(404, "Unknown language")
    for course in data["courses"]:
        if course["level"] == level and course["area"] == area:
            return course
    raise HTTPException(404, "Unknown course")


async def source_text(request: Request, path: str) -> str | None:
    """Read a fixed public GitHub path; 404 means this edition has only a plan."""
    if override := getattr(app.state, "source_override", None):
        return await override(path)
    # Each read resolves main again. A unique query keeps intermediate CDN caches
    # from serving an older version after a lesson is edited in the repository.
    url = GITHUB_RAW + path + f"?source={time.time_ns()}"
    try:
        from js import fetch  # type: ignore[import-not-found]
    except ImportError:
        def local_fetch() -> str | None:
            try:
                with urlopen(url, timeout=12) as response:
                    data = response.read(MAX_SOURCE_CHARS + 1)
            except HTTPError as exc:
                if exc.code == 404:
                    return None
                raise
            if len(data) > MAX_SOURCE_CHARS:
                raise HTTPException(502, "Upstream book exceeds reading limit")
            return data.decode("utf-8")
        try:
            return await asyncio.to_thread(local_fetch)
        except HTTPException:
            raise
        except Exception as exc:
            raise HTTPException(502, "GitHub source temporarily unavailable") from exc
    try:
        response = await fetch(url)
        if int(response.status) == 404:
            return None
        if int(response.status) != 200:
            raise HTTPException(502, "GitHub source temporarily unavailable")
        text = str(await response.text())
        if len(text) > MAX_SOURCE_CHARS:
            raise HTTPException(502, "Upstream book exceeds reading limit")
        return text
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(502, "GitHub source temporarily unavailable") from exc


async def editorial_policy(request: Request) -> str:
    """Serve the current public rule from main, rather than a stale deploy copy."""
    policy = await source_text(request, "BOOK_STANDARD.md")
    if policy is None:
        raise HTTPException(503, "Editorial policy is unavailable")
    return policy


def book_path(level: str, area: str, language: str, filename: str) -> str:
    return f"levels/{level}/{area}/{language}/book/{filename}"


def chapter_sections(markdown: str) -> dict[int, dict[str, str]]:
    anchors = list(ANCHOR.finditer(markdown))
    chapters: dict[int, dict[str, str]] = {}
    for index, match in enumerate(anchors):
        end = anchors[index + 1].start() if index + 1 < len(anchors) else len(markdown)
        body = markdown[match.start():end].strip()
        heading = re.search(r'^#{2,3}\s+(.+)$', body, re.M)
        if heading is None:
            continue
        if index == len(anchors) - 1:
            tail = body[heading.end():]
            endings = [found.start() for pattern in (APPENDIX_HEADING, REFERENCES_HEADING) if (found := pattern.search(tail))]
            if endings:
                body = body[:heading.end() + min(endings)].rstrip()
        chapters[int(match.group(1))] = {"title": heading.group(1).strip(), "markdown": body}
    return chapters


def lesson_sections(markdown: str) -> dict[int, dict[str, Any]]:
    """Return authored daily lessons and their enclosing weekly chapters."""
    lessons: dict[int, dict[str, Any]] = {}
    anchors = sorted(
        [(match, int(match.group(1)), None, f"lesson-{match.group(1)}") for match in LESSON_ANCHOR.finditer(markdown)]
        + [(match, (int(match.group(1)) - 1) * 5 + int(match.group(2)), int(match.group(1)),
            f"week-{match.group(1)}-day-{match.group(2)}") for match in WEEK_DAY_ANCHOR.finditer(markdown)
           if 1 <= int(match.group(2)) <= 5],
        key=lambda item: item[0].start(),
    )
    chapters = list(ANCHOR.finditer(markdown))
    appendix = APPENDIX_HEADING.search(markdown)
    for index, (match, number, declared_week, anchor) in enumerate(anchors):
        stops = [chap.start() for chap in chapters if chap.start() > match.start()]
        if index + 1 < len(anchors):
            stops.append(anchors[index + 1][0].start())
        if appendix and appendix.start() > match.start():
            stops.append(appendix.start())
        if declared_week is not None:
            end_marker = re.search(rf'^<a id="week-{declared_week:02d}-end"></a>\s*$', markdown[match.end():], re.M)
            if end_marker:
                stops.append(match.end() + end_marker.start())
        body = markdown[match.start():min(stops) if stops else len(markdown)].strip()
        heading = re.search(r'^#{3,4}\s+(.+)$', body, re.M)
        if heading is None:
            continue
        week = declared_week or next((int(chap.group(1)) for chap in reversed(chapters) if chap.start() < match.start()), None)
        exercises = set(EXERCISE_HEADING.findall(body))
        if declared_week is not None:
            exercises.update(re.findall(r'\[EX(\d{3,4})\]\(#exercise-ex\d{3,4}\)', body))
        lessons[number] = {
            "title": re.sub(r'^(?:Lesson|Aula|Lección|Day)\s+\d+\s+[—-]\s*', '', heading.group(1).strip()),
            "markdown": body, "chapter": week, "anchor": anchor,
            "exercise_ids": sorted(exercises),
        }
    return lessons


def worked_answers(book: str, chapter: str, exercise_ids: list[str] | None = None) -> str:
    numbers = set(exercise_ids) if exercise_ids is not None else set(EXERCISE.findall(chapter))
    supplementary = list(dict.fromkeys(re.findall(r'\]\(#(w\d+-answer-\d{2})\)', chapter)))
    if not numbers and not supplementary:
        return ""
    appendix = APPENDIX_HEADING.search(book)
    if not appendix:
        return ""
    answers = book[appendix.end():]
    matches = list(ANSWER.finditer(answers))
    pieces = []
    for index, match in enumerate(matches):
        if (match.group(1) or match.group(2)) not in numbers:
            continue
        end = matches[index + 1].start() if index + 1 < len(matches) else len(answers)
        piece = answers[match.start():end]
        next_section = re.search(r'^#{2,3}\s+(?!EX\d{3,4}\b)', piece[match.end() - match.start():], re.M)
        if next_section:
            piece = piece[:match.end() - match.start() + next_section.start()]
        digits = match.group(1) or match.group(2)
        piece = re.sub(r'(?:\n\s*<a id="answer-ex\d{3,4}"></a>\s*)+$', '', piece)
        pieces.append(f'<a id="answer-ex{digits}"></a>\n' + piece.strip())
    for anchor in supplementary:
        match = re.search(rf'^<a id="{re.escape(anchor)}"></a>\s*$', answers, re.M)
        if not match:
            continue
        tail = answers[match.end():]
        end = re.search(r'^<a id="w\d+-answer-\d{2}"></a>\s*$|^##\s', tail, re.M)
        pieces.append((f'<a id="{anchor}"></a>' + tail[:end.start() if end else None]).strip())
    return "\n\n".join(pieces)


def exercise_prompts(book: str, exercise_ids: list[str]) -> str:
    """Bring a linked legacy prompt into an individual daily lesson."""
    if not exercise_ids:
        return ""
    appendix = APPENDIX_HEADING.search(book)
    teaching = book[:appendix.start()] if appendix else book
    pieces = []
    for digits in exercise_ids:
        match = re.search(rf'^\*\*EX{re.escape(digits)}\s+[—-]\s+[^\n]+|^#{{3,6}}\s+EX{re.escape(digits)}\b[^\n]*', teaching, re.M)
        if match:
            pieces.append(f'<a id="exercise-ex{digits}"></a>\n' + match.group(0))
    return "\n\n".join(pieces)


def course_schedule(subjects: str) -> tuple[str, dict[int, tuple[int, str]]]:
    """Read the published curricular periods and subject names from SUBJECTS.md."""
    period_kind = "Module"
    schedule: dict[int, tuple[int, str]] = {}
    for line in subjects.splitlines():
        if not line.startswith("|"):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 3:
            continue
        if cells[0] in {"Week", "Month", "Semester", "Term", "Year", "Module"}:
            period_kind = cells[0]
            continue
        chapter = re.search(r"\[(\d{2,4})\]\(book/PLAN\.md#ch-\d{2,4}\)", cells[1])
        if cells[0].isdigit() and chapter:
            schedule[int(chapter.group(1))] = (int(cells[0]), cells[2])
    return period_kind, schedule


async def course_details(request: Request, level: str, area: str, language: str) -> dict[str, Any]:
    item = get_course(await catalog(request), level, area, language)
    plan_path = book_path(level, area, language, "PLAN.md")
    manuscript_path = book_path(level, area, language, "MANUSCRIPT.md")
    book = await source_text(request, manuscript_path)
    plan = await source_text(request, plan_path)
    if plan is None:
        raise HTTPException(502, "Course plan is unavailable")
    try:
        subjects = await source_text(request, f"levels/{level}/{area}/{language}/SUBJECTS.md")
    except HTTPException:
        subjects = None
    period_kind, schedule = course_schedule(subjects or "")
    planned = chapter_sections(plan)
    authored = chapter_sections(book) if book is not None else {}
    planned_daily = lesson_sections(plan)
    authored_daily = lesson_sections(book) if book is not None else {}
    has_daily_lessons = bool(planned_daily or authored_daily)
    daily_schedule_ready = has_daily_lessons and len(planned_daily.keys() | authored_daily.keys()) >= item["daily_lesson_target"]
    daily_target = max(item["daily_lesson_target"], *(planned_daily.keys() | authored_daily.keys()), 0)
    daily_slots: list[dict[str, Any]] = []
    for number in range(1, daily_target + 1):
        section = authored_daily.get(number) or planned_daily.get(number)
        period = section.get("chapter") if section else (number - 1) // 5 + 1
        published = number in authored_daily
        source_anchor = section.get("anchor") if section else None
        daily_slots.append({
            "chapter": number,
            "module": period,
            "title": section["title"] if section else (
                f"Dia de estudo {number} — conteúdo ainda não escrito" if language == "pt" else
                f"Día de estudio {number} — contenido aún no escrito" if language == "es" else
                f"Study day {number} — teaching not yet written"
            ),
            "published": published,
            "source_url": (GITHUB_VIEW + (manuscript_path if published else plan_path) + "#" + source_anchor)
            if source_anchor else None,
        })
    legacy_chapters = [
        {"chapter": number, "title": (authored.get(number) or planned[number])["title"],
         "published": number in authored, "module": schedule.get(number, (1, ""))[0],
         "source_url": GITHUB_VIEW + manuscript_path + f"#ch-{number:02d}" if number in authored else None}
        for number in sorted(planned.keys() | authored.keys())
    ]
    lessons = []
    modules: list[dict[str, Any]] = []
    source_planned = planned_daily if has_daily_lessons else planned
    source_authored = authored_daily if has_daily_lessons else authored
    for number in sorted(source_planned.keys() | source_authored.keys()):
        section = source_authored[number] if number in source_authored else source_planned[number]
        title = section["title"]
        if has_daily_lessons:
            period = section.get("chapter") or (number - 1) // 5 + 1
            subject = re.sub(r'^(?:Chapter|Capítulo)\s+\d+\s+[—-]\s*', '', (authored.get(period) or planned.get(period) or {"title": title})["title"])
        else:
            period, subject = schedule.get(number, (1, title))
        lessons.append({
            "chapter": number,
            "title": title,
            "subject": subject,
            "module": period,
            "published": number in source_authored,
            "source_url": GITHUB_VIEW + (manuscript_path if number in source_authored else plan_path) + "#" + (
                section.get("anchor", f"lesson-{number:02d}") if has_daily_lessons else f"ch-{number:02d}"),
        })
        if not modules or modules[-1]["number"] != period:
            modules.append({"number": period, "kind": "Chapter" if has_daily_lessons else period_kind, "title": subject, "chapters": []})
        modules[-1]["chapters"].append(number)
    return {
        "course": item,
        "language": language,
        "lessons": lessons,
        "modules": modules,
        "daily_slots": daily_slots,
        "legacy_chapters": legacy_chapters,
        "published_chapters": len(authored),
        "planned_chapters": len(planned.keys() | authored.keys()),
        "published_lessons": len(authored_daily),
        "planned_lessons": daily_target,
        "has_daily_lessons": has_daily_lessons,
        "daily_schedule_ready": daily_schedule_ready,
        "book_url": GITHUB_VIEW + manuscript_path if authored else None,
        "source_sha256": hashlib.sha256(book.encode("utf-8")).hexdigest() if book is not None else None,
        "source_branch": "main",
        "notice": "A published lesson may still need editorial review. A plan is not a lesson. Lesson length is not a quota.",
    }


async def lesson_details(request: Request, level: str, area: str, language: str, chapter: int, legacy: bool = False) -> dict[str, Any]:
    get_course(await catalog(request), level, area, language)
    if chapter < 1 or chapter > 9999:
        raise HTTPException(404, "Unknown chapter")
    path = book_path(level, area, language, "MANUSCRIPT.md")
    book = await source_text(request, path)
    if book is None:
        raise HTTPException(404, "This edition has no authored manuscript yet")
    daily = lesson_sections(book)
    sections = chapter_sections(book) if legacy or not daily else daily
    section = sections.get(chapter)
    if section is None:
        raise HTTPException(404, "This chapter is still a plan")
    chapters = sorted(sections)
    exercise_ids = section.get("exercise_ids", sorted(set(EXERCISE.findall(section["markdown"]))))
    markdown = section["markdown"]
    if daily and not legacy and not EXERCISE_HEADING.search(markdown):
        prompts = exercise_prompts(book, exercise_ids)
        if prompts:
            markdown += "\n\n### Exercise for this lesson\n\n" + prompts
    return {
        "course": {"level": level, "area": area, "language": language},
        "chapter": chapter,
        "title": section["title"],
        "markdown": markdown,
        "worked_answers": worked_answers(book, markdown, exercise_ids),
        "exercise_ids": exercise_ids,
        "week_chapter": section.get("chapter"),
        "content_kind": "legacy_chapter" if legacy or not daily else "daily_lesson",
        "previous": max((n for n in chapters if n < chapter), default=None),
        "next": min((n for n in chapters if n > chapter), default=None),
        "source_url": GITHUB_VIEW + path + "#" + (section.get("anchor", f"lesson-{chapter:02d}") if daily and not legacy else f"ch-{chapter:02d}"),
        "source_sha256": hashlib.sha256(book.encode("utf-8")).hexdigest(),
        "content_sha256": hashlib.sha256(markdown.encode("utf-8")).hexdigest(),
        "source_branch": "main",
        "editorial_note": "Public teaching text; publication does not certify that the complete book passed editorial review.",
    }


@app.get("/api/health")
async def health() -> dict[str, str]:
    return {"service": "OpenCyber Academy", "status": "ok", "source": "https://github.com/hiagokinlevi/OpenCyberAcademy"}


@app.get("/private/login")
async def private_login(request: Request) -> Response:
    await identity(request)
    return RedirectResponse("/account/", status_code=302)


@app.get("/private/me")
async def api_me(request: Request) -> Response:
    user = await identity(request)
    return JSONResponse({"email": user.get("email"), "student_id": user["sub"]}, headers={"Cache-Control": "no-store"})


@app.get("/private/progress")
async def api_progress(request: Request) -> Response:
    user = await identity(request)
    db = database(request)
    lessons = await db.prepare("SELECT level, area, language, chapter, status, updated_at FROM lesson_progress WHERE user_id = ? ORDER BY updated_at DESC LIMIT 500").bind(user["sub"]).all()
    exercises = await db.prepare("SELECT level, area, language, chapter, exercise_id, answer, status, updated_at FROM exercise_attempts WHERE user_id = ? ORDER BY updated_at DESC LIMIT 500").bind(user["sub"]).all()
    return JSONResponse({"lessons": d1_rows(lessons), "exercises": d1_rows(exercises)}, headers={"Cache-Control": "no-store"})


@app.post("/private/progress/lesson")
async def api_progress_lesson(request: Request, payload: LessonProgress) -> Response:
    same_origin(request)
    user = await identity(request)
    await lesson_details(request, payload.level, payload.area, payload.language, payload.chapter)
    db = database(request)
    await db.prepare("INSERT INTO lesson_progress (user_id, level, area, language, chapter, status) VALUES (?, ?, ?, ?, ?, ?) ON CONFLICT (user_id, level, area, language, chapter) DO UPDATE SET status = excluded.status, updated_at = datetime('now')").bind(user["sub"], payload.level, payload.area, payload.language, payload.chapter, payload.status).run()
    return JSONResponse({"saved": True}, headers={"Cache-Control": "no-store"})


@app.post("/private/progress/exercise")
async def api_progress_exercise(request: Request, payload: ExerciseAttempt) -> Response:
    same_origin(request)
    user = await identity(request)
    lesson = await lesson_details(request, payload.level, payload.area, payload.language, payload.chapter)
    if payload.exercise_id.removeprefix("EX") not in lesson["exercise_ids"]:
        raise HTTPException(404, "Exercise is not in this lesson")
    db = database(request)
    await db.prepare("INSERT INTO exercise_attempts (user_id, level, area, language, chapter, exercise_id, answer, status) VALUES (?, ?, ?, ?, ?, ?, ?, ?) ON CONFLICT (user_id, level, area, language, chapter, exercise_id) DO UPDATE SET answer = excluded.answer, status = excluded.status, updated_at = datetime('now')").bind(user["sub"], payload.level, payload.area, payload.language, payload.chapter, payload.exercise_id, payload.answer, payload.status).run()
    return JSONResponse({"saved": True}, headers={"Cache-Control": "no-store"})


@app.get("/api/catalog")
async def api_catalog(request: Request) -> dict[str, Any]:
    return await catalog(request)


@app.get("/api/courses/{level}/{area}/{language}")
async def api_course(request: Request, level: str, area: str, language: str) -> dict[str, Any]:
    return await course_details(request, level, area, language)


@app.get("/api/lessons/{level}/{area}/{language}/{chapter}")
async def api_lesson(request: Request, level: str, area: str, language: str, chapter: int) -> dict[str, Any]:
    return await lesson_details(request, level, area, language, chapter)


@app.get("/api/chapters/{level}/{area}/{language}/{chapter}")
async def api_chapter(request: Request, level: str, area: str, language: str, chapter: int) -> dict[str, Any]:
    """Read an authored subject chapter even during a partial daily conversion."""
    return await lesson_details(request, level, area, language, chapter, legacy=True)


@app.get("/courses/{level}/{area}/lessons/{language}/{chapter}/", include_in_schema=False)
async def public_lesson_page(request: Request, level: str, area: str, language: str, chapter: int) -> Response:
    data = await catalog(request)
    course = get_course(data, level, area, language)
    try:
        lesson = await lesson_details(request, level, area, language, chapter)
    except HTTPException as exc:
        if exc.status_code != 404:
            raise
        guide = await course_details(request, level, area, language)
        if chapter < 1 or chapter > guide["planned_lessons"]:
            raise
        slot = guide["daily_slots"][chapter - 1]
        published_chapter = next((item for item in guide["legacy_chapters"]
                                  if item["chapter"] == slot["module"] and item["published"]), None)
        page = render_planned_lesson_page(course, slot, language, data["level_names"][level].get(language, data["level_names"][level]["en"]), published_chapter)
        return HTMLResponse(page, headers={"Cache-Control": "no-store", "Content-Language": language,
                                           "X-Robots-Tag": "noindex, follow", "X-Content-Type-Options": "nosniff"})
    if lesson["content_kind"] == "legacy_chapter":
        return RedirectResponse(lesson_path(level, area, language, chapter, "chapter"), status_code=308)
    level_name = data["level_names"][level].get(language, data["level_names"][level]["en"])
    return HTMLResponse(render_lesson_page(lesson, course, level_name), headers={"Cache-Control": "no-store", "Content-Language": language, "X-Content-Type-Options": "nosniff"})


@app.get("/courses/{level}/{area}/chapters/{language}/{chapter}/", include_in_schema=False)
async def public_chapter_page(request: Request, level: str, area: str, language: str, chapter: int) -> Response:
    data = await catalog(request)
    course = get_course(data, level, area, language)
    lesson = await lesson_details(request, level, area, language, chapter, legacy=True)
    level_name = data["level_names"][level].get(language, data["level_names"][level]["en"])
    return HTMLResponse(render_lesson_page(lesson, course, level_name, "chapter"), headers={"Cache-Control": "no-store", "Content-Language": language, "X-Content-Type-Options": "nosniff"})


@app.get("/api/books/{level}/{area}/{language}")
async def api_book(request: Request, level: str, area: str, language: str) -> Response:
    get_course(await catalog(request), level, area, language)
    book = await source_text(request, book_path(level, area, language, "MANUSCRIPT.md"))
    if book is None:
        raise HTTPException(404, "This edition has no authored manuscript yet")
    return PlainTextResponse(book, media_type="text/markdown; charset=utf-8", headers={"Cache-Control": "no-store", "X-OpenCyberAcademy-Source-SHA256": hashlib.sha256(book.encode("utf-8")).hexdigest()})


@app.get("/api/source")
async def api_source(request: Request, path: str = Query(min_length=1, max_length=320)) -> Response:
    """Serve a public Markdown reference so course navigation stays on OpenCyber Academy."""
    if (not path.endswith(".md") or path.startswith("/") or "\\" in path
            or any(part in ("", ".", "..") for part in path.split("/"))
            or not re.fullmatch(r"[\w./-]+", path, re.UNICODE)):
        raise HTTPException(404, "Unknown public document")
    document = await source_text(request, path)
    if document is None:
        raise HTTPException(404, "Public document not found")
    return PlainTextResponse(document, media_type="text/markdown; charset=utf-8", headers={"Cache-Control": "public, max-age=60"})


@app.get("/api/search/{level}/{area}/{language}")
async def api_search(request: Request, level: str, area: str, language: str, q: str = Query(min_length=3, max_length=80)) -> dict[str, Any]:
    get_course(await catalog(request), level, area, language)
    book = await source_text(request, book_path(level, area, language, "MANUSCRIPT.md"))
    if book is None:
        raise HTTPException(404, "This edition has no authored manuscript yet")
    matches = []
    for chapter, section in chapter_sections(book).items():
        for match in re.finditer(re.escape(q), section["markdown"], re.I):
            start, end = max(0, match.start() - 100), min(len(section["markdown"]), match.end() + 100)
            matches.append({"chapter": chapter, "title": section["title"], "snippet": re.sub(r'\s+', ' ', section["markdown"][start:end])})
            if len(matches) == 20:
                return {"query": q, "results": matches, "truncated": True}
    return {"query": q, "results": matches, "truncated": False}


def rpc_result(identifier: Any, result: Any) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": identifier, "result": result}


def rpc_error(identifier: Any, code: int, message: str) -> dict[str, Any]:
    return {"jsonrpc": "2.0", "id": identifier, "error": {"code": code, "message": message}}


TOOLS = [
    {"name": "get_editorial_policy", "description": "Read the current public book standard and language production gate: English, then Portuguese, then Spanish; later languages begin only when all three collections are verified complete.", "inputSchema": {"type": "object", "properties": {}}},
    {"name": "list_courses", "description": "Discover the 207 public OpenCyber Academy courses. Optional language, level, area or title query filters.", "inputSchema": {"type": "object", "properties": {"language": {"type": "string"}, "level": {"type": "string"}, "area": {"type": "string"}, "query": {"type": "string"}}}},
    {"name": "list_lessons", "description": "List planned and authored lessons for one course. Only published=true represents written teaching.", "inputSchema": {"type": "object", "properties": {"level": {"type": "string"}, "area": {"type": "string"}, "language": {"type": "string"}}, "required": ["level", "area", "language"]}},
    {"name": "read_lesson", "description": "Read the public Markdown for an authored lesson and its worked answers, with its GitHub source URL.", "inputSchema": {"type": "object", "properties": {"level": {"type": "string"}, "area": {"type": "string"}, "language": {"type": "string"}, "chapter": {"type": "integer"}, "start": {"type": "integer", "minimum": 0}, "max_chars": {"type": "integer", "minimum": 1000, "maximum": 50000}}, "required": ["level", "area", "language", "chapter"]}},
    {"name": "read_chapter", "description": "Read an authored legacy subject chapter during conversion to weekday lessons; plans are not returned as teaching.", "inputSchema": {"type": "object", "properties": {"level": {"type": "string"}, "area": {"type": "string"}, "language": {"type": "string"}, "chapter": {"type": "integer"}, "start": {"type": "integer", "minimum": 0}, "max_chars": {"type": "integer", "minimum": 1000, "maximum": 50000}}, "required": ["level", "area", "language", "chapter"]}},
    {"name": "search_course", "description": "Search within one authored manuscript; returns bounded snippets and chapter numbers.", "inputSchema": {"type": "object", "properties": {"level": {"type": "string"}, "area": {"type": "string"}, "language": {"type": "string"}, "query": {"type": "string"}}, "required": ["level", "area", "language", "query"]}},
]


@app.post("/mcp")
async def mcp(request: Request) -> Response:
    origin = request.headers.get("origin")
    if origin and origin not in ALLOWED_ORIGINS:
        raise HTTPException(403, "Origin is not allowed")
    if "application/json" not in request.headers.get("content-type", ""):
        raise HTTPException(415, "MCP expects application/json")
    if "application/json" not in request.headers.get("accept", "") or "text/event-stream" not in request.headers.get("accept", ""):
        raise HTTPException(406, "MCP client must accept JSON and event stream")
    body = await request.body()
    if len(body) > 65_536:
        raise HTTPException(413, "MCP request too large")
    try:
        payload = json.loads(body)
    except ValueError:
        return JSONResponse(rpc_error(None, -32700, "Parse error"), status_code=400)
    if not isinstance(payload, dict) or payload.get("jsonrpc") != "2.0" or not isinstance(payload.get("method"), str):
        return JSONResponse(rpc_error(payload.get("id") if isinstance(payload, dict) else None, -32600, "Invalid Request"), status_code=400)
    if "id" not in payload:
        return Response(status_code=202)
    identifier, method = payload["id"], payload["method"]
    params = payload.get("params") or {}
    if not isinstance(params, dict):
        return JSONResponse(rpc_error(identifier, -32602, "Invalid params"))
    try:
        if method == "initialize":
            return JSONResponse(rpc_result(identifier, {"protocolVersion": MCP_VERSION, "capabilities": {"resources": {}, "tools": {}}, "serverInfo": {"name": "OpenCyber Academy", "version": "0.1.0"}}))
        if method == "ping":
            return JSONResponse(rpc_result(identifier, {}))
        if method == "tools/list":
            return JSONResponse(rpc_result(identifier, {"tools": TOOLS}))
        if method == "resources/list":
            return JSONResponse(rpc_result(identifier, {"resources": [
                {"uri": "open-cyber-academy://catalog", "name": "OpenCyber Academy course catalog", "mimeType": "application/json", "description": "207 courses in study order"},
                {"uri": EDITORIAL_POLICY_URI, "name": "OpenCyber Academy editorial policy", "mimeType": "text/markdown", "description": "Current public book standard and three-language production gate"},
            ]}))
        if method == "resources/templates/list":
            return JSONResponse(rpc_result(identifier, {"resourceTemplates": [
                {"uriTemplate": "open-cyber-academy://lesson/{level}/{area}/{language}/{chapter}", "name": "OpenCyber Academy lesson", "mimeType": "text/markdown", "description": "A published daily lesson, or a legacy chapter when this edition has no daily lessons"},
                {"uriTemplate": "open-cyber-academy://chapter/{level}/{area}/{language}/{chapter}", "name": "OpenCyber Academy subject chapter", "mimeType": "text/markdown", "description": "An authored legacy chapter retained during the daily lesson conversion"},
            ]}))
        if method == "resources/read":
            uri = params.get("uri", "")
            if uri == "open-cyber-academy://catalog":
                contents = [{"uri": uri, "mimeType": "application/json", "text": json.dumps(await catalog(request), ensure_ascii=False)}]
            elif uri == EDITORIAL_POLICY_URI:
                contents = [{"uri": uri, "mimeType": "text/markdown", "text": await editorial_policy(request)}]
            else:
                match = re.fullmatch(r'open-cyber-academy://(lesson|chapter)/([a-z0-9-]+)/([a-z0-9-]+)/([a-z]{2})/(\d{1,4})', str(uri))
                if not match:
                    return JSONResponse(rpc_error(identifier, -32602, "Unknown resource URI"))
                result = await lesson_details(request, match[2], match[3], match[4], int(match[5]), legacy=match[1] == "chapter")
                contents = [{"uri": uri, "mimeType": "text/markdown", "text": result["markdown"] + "\n\n## Worked answers for this lesson\n\n" + result["worked_answers"] + "\n\nSource: " + result["source_url"]}]
            return JSONResponse(rpc_result(identifier, {"contents": contents}))
        if method == "tools/call":
            name, args = params.get("name"), params.get("arguments") or {}
            if not isinstance(args, dict):
                return JSONResponse(rpc_error(identifier, -32602, "Invalid tool arguments"))
            if name == "get_editorial_policy":
                result = {"markdown": await editorial_policy(request), "source_url": GITHUB_VIEW + "BOOK_STANDARD.md"}
            elif name == "list_courses":
                data = await catalog(request)
                courses = data["courses"]
                for key in ("level", "area"):
                    if args.get(key):
                        courses = [item for item in courses if item[key] == args[key]]
                if args.get("query"):
                    courses = [item for item in courses if str(args["query"]).casefold() in item["title"].casefold()]
                result = {"courses": courses, "total": len(courses), "source": data["source"]}
            elif name == "list_lessons":
                result = await course_details(request, args["level"], args["area"], args["language"])
            elif name in {"read_lesson", "read_chapter"}:
                result = await lesson_details(request, args["level"], args["area"], args["language"], int(args["chapter"]), legacy=name == "read_chapter")
                start = max(0, int(args.get("start", 0)))
                length = min(50_000, max(1000, int(args.get("max_chars", 30000))))
                text = result.pop("markdown")
                result["markdown"] = text[start:start + length]
                result["next_start"] = start + length if start + length < len(text) else None
                result["total_chars"] = len(text)
            elif name == "search_course":
                result = await api_search(request, args["level"], args["area"], args["language"], str(args["query"]))
            else:
                return JSONResponse(rpc_error(identifier, -32602, "Unknown tool"))
            return JSONResponse(rpc_result(identifier, {"content": [{"type": "text", "text": json.dumps(result, ensure_ascii=False)}]}))
        return JSONResponse(rpc_error(identifier, -32601, "Method not found"))
    except (KeyError, ValueError, TypeError):
        return JSONResponse(rpc_error(identifier, -32602, "Invalid params"))
    except HTTPException as exc:
        return JSONResponse(rpc_result(identifier, {"content": [{"type": "text", "text": str(exc.detail)}], "isError": True}))


@app.get("/mcp")
async def mcp_get() -> Response:
    return Response(status_code=405, headers={"Allow": "POST"})


@app.get("/robots.txt", include_in_schema=False)
async def robots(request: Request) -> Response:
    language = language_for_host(request.headers.get("host", "")) or "en"
    site = site_for_language(language)
    return PlainTextResponse(f"User-agent: *\nAllow: /\nSitemap: {site}/sitemap.xml\n")


@app.get("/sitemap.xml", include_in_schema=False)
async def localized_sitemap(request: Request) -> Response:
    language = language_for_host(request.headers.get("host", "")) or "en"
    return await static_assets(f"sitemap-{language}.xml", request)


@app.get("/{path:path}", include_in_schema=False)
async def static_assets(path: str, request: Request) -> Response:
    asset = path.strip("/")
    if not asset or "." not in asset.rsplit("/", 1)[-1]:
        asset = (asset + "/" if asset else "") + "index.html"
    language = language_for_host(request.headers.get("host", "")) or "en"
    if language not in ACTIVE_INTERFACES and asset.endswith("index.html"):
        if asset != "index.html":
            return RedirectResponse(site_for_language(language) + "/", status_code=302)
        asset = f"_locales/{language}/index.html"
    elif language in {"pt", "es"} and asset.endswith("index.html"):
        asset = f"_locales/{language}/{asset}"
    env = request.scope.get("env")
    if env is not None:
        response = await env.ASSETS.fetch("https://assets.local/" + asset)
        content = await response.bytes()
        headers = dict(response.headers)
        if asset.endswith("index.html"):
            headers["Content-Language"] = language
        return Response(content=content, status_code=int(response.status), headers=headers)
    root = Path(__file__).resolve().parents[1] / "dist"
    target = (root / asset).resolve()
    if not target.is_relative_to(root.resolve()) or not target.is_file():
        raise HTTPException(404, "Page not found")
    return FileResponse(target, headers={"Content-Language": language} if asset.endswith("index.html") else None)
