#!/usr/bin/env python3
"""Build the website's discovery catalog from the public Git repository.

The Worker reads each selected manuscript from GitHub main at request time;
this file only holds stable course metadata and a build-time availability hint.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from xml.sax.saxutils import escape



ROOT = Path(__file__).resolve().parents[2]
OUTPUT = Path(__file__).resolve().parents[1] / "public" / "catalog.json"
SITEMAP = OUTPUT.with_name("sitemap.xml")
LESSON_INDEX = OUTPUT.with_name("lesson-index.json")
SUBJECT_TITLES = json.loads((ROOT / "web/src/lib/subject-titles.json").read_text(encoding="utf-8"))
LANGUAGES = ("en", "pt", "es", "he", "fr", "ru", "de", "zh", "ja")
INDEXED_LANGUAGES = {"en", "pt", "es"}


def site_for_language(language: str) -> str:
    return "https://opencyber.academy" if language == "en" else f"https://{language}.opencyber.academy"


def sitemap_xml(routes: list[str], language: str, alternates: dict[str, dict[str, str]]) -> str:
    site = site_for_language(language)
    urls = dict.fromkeys(site + route for route in routes)
    xhtml_namespace = (' xmlns:xhtml="http://www.w3.org/1999/xhtml"'
                       if any(url in alternates for url in urls) else '')

    def entry(url: str) -> str:
        variants = alternates.get(url, {})
        links = "".join(
            f'<xhtml:link rel="alternate" hreflang="{code}" href="{escape(href)}" />'
            for code, href in variants.items()
        )
        return f"  <url><loc>{escape(url)}</loc>{links}</url>\n"
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"{xhtml_namespace}>\n'
            + "".join(entry(url) for url in urls)
            + "</urlset>\n")
LEVELS = {
    "rapid-1-month": {"en": "Rapid course", "pt": "Curso rápido", "es": "Curso rápido"},
    "professional-6-months": {"en": "Professional", "pt": "Profissionalizante", "es": "Profesional"},
    "technical-18-months": {"en": "Technical", "pt": "Técnico", "es": "Técnico"},
    "technologist-3-years": {"en": "Technologist", "pt": "Tecnólogo", "es": "Tecnólogo"},
    "bachelors-4-years": {"en": "Bachelor's", "pt": "Graduação", "es": "Grado"},
    "engineering-5-years": {"en": "Engineering", "pt": "Engenharia", "es": "Ingeniería"},
    "postgraduate-2-years": {"en": "Postgraduate", "pt": "Pós-graduação", "es": "Posgrado"},
    "masters-2-years": {"en": "Master's", "pt": "Mestrado", "es": "Máster"},
    "doctorate-2-years": {"en": "Doctoral research", "pt": "Pesquisa doutoral", "es": "Investigación doctoral"},
}
INSTRUCTIONAL_WEEKS = {
    "rapid-1-month": 4,
    "professional-6-months": 26,
    "technical-18-months": 78,
    "technologist-3-years": 156,
    "bachelors-4-years": 208,
    "engineering-5-years": 260,
    "postgraduate-2-years": 104,
    "masters-2-years": 104,
    "doctorate-2-years": 104,
}
ANCHOR = re.compile(r'^<a id="ch-(\d{2,4})"></a>$', re.M)
LESSON_ANCHOR = re.compile(r'^<a id="lesson-(\d{2,4})"></a>$', re.M)
WEEK_DAY_ANCHOR = re.compile(r'^<a id="week-(\d{2,4})-day-(\d{2})"></a>$', re.M)
NUMBER = re.compile(r'Course\s+(\d{3})\s+of\s+207')


def authored_index() -> dict:
    """Only source-backed lesson and chapter links belong in discovery maps."""
    index = {}
    for book in ROOT.glob("levels/*/*/*/book/MANUSCRIPT.md"):
        level, area, language = book.parts[-5:-2]
        if level not in LEVELS or language not in LANGUAGES:
            continue
        source = book.read_text(encoding="utf-8")
        daily: dict[int, str] = {}
        chapters: dict[int, str] = {}
        def title_after(match: re.Match, depth: str) -> str:
            heading = re.search(rf'^#{{{depth}}}\s+(.+)$', source[match.end():match.end() + 600], re.M)
            return heading.group(1).strip() if heading else ""
        for match in LESSON_ANCHOR.finditer(source):
            if title := title_after(match, "3,4"):
                daily[int(match.group(1))] = title
        for match in WEEK_DAY_ANCHOR.finditer(source):
            if 1 <= int(match.group(2)) <= 5 and (title := title_after(match, "3,4")):
                daily[(int(match.group(1)) - 1) * 5 + int(match.group(2))] = title
        for match in ANCHOR.finditer(source):
            if title := title_after(match, "2,3"):
                chapters[int(match.group(1))] = title
        if daily or chapters:
            index[f"{level}/{area}/{language}"] = {
                "lessons": [{"number": number, "title": daily[number]} for number in sorted(daily)],
                "chapters": [{"number": number, "title": chapters[number]} for number in sorted(chapters)],
            }
    return index


def build() -> dict:
    courses = []
    for home in ROOT.glob("levels/*/*/README.md"):
        level, area = home.parts[-3:-1]
        if level not in LEVELS:
            continue
        text = home.read_text(encoding="utf-8")
        number_match = NUMBER.search(text)
        if not number_match:
            raise ValueError(f"Missing course number: {home}")
        title = text.splitlines()[0].removeprefix("# ").split(" — ")[0]
        if title not in SUBJECT_TITLES:
            raise ValueError(f"Missing translated course title: {title}")
        plan = home.parent / "en" / "book" / "PLAN.md"
        chapters = len(ANCHOR.findall(plan.read_text(encoding="utf-8")))
        if not chapters:
            raise ValueError(f"Missing plan chapters: {plan}")
        editions = {}
        for language in LANGUAGES:
            book = home.parent / language / "book" / "MANUSCRIPT.md"
            authored = len(ANCHOR.findall(book.read_text(encoding="utf-8"))) if book.exists() else 0
            editions[language] = {"authored_at_build": authored, "planned": chapters}
        courses.append({
            "number": int(number_match.group(1)),
            "level": level,
            "area": area,
            "title": title,
            "titles": {"en": title, **SUBJECT_TITLES[title]},
            "planned_chapters": chapters,
            "instructional_weeks": INSTRUCTIONAL_WEEKS[level],
            "study_days_per_week": 5,
            "daily_lesson_target": INSTRUCTIONAL_WEEKS[level] * 5,
            "editions": editions,
            "github": f"https://github.com/hiagokinlevi/OpenCyberAcademy/tree/main/levels/{level}/{area}",
        })
    courses.sort(key=lambda item: item["number"])
    if [item["number"] for item in courses] != list(range(1, 208)):
        raise ValueError("Expected courses numbered 001–207 exactly once")
    return {
        "name": "OpenCyber Academy",
        "source": "https://github.com/hiagokinlevi/OpenCyberAcademy",
        "source_branch": "main",
        "level_order": list(LEVELS),
        "level_names": LEVELS,
        "languages": list(LANGUAGES),
        "courses": courses,
        "note": "Counts are a build-time discovery hint. The API reads selected books from GitHub main live; published text and editorial approval are different states.",
    }


if __name__ == "__main__":
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    data = build()
    index = authored_index()
    OUTPUT.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    LESSON_INDEX.write_text(json.dumps(index, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    common = ["/", "/about/", "/levels/", "/subjects/", "/for-ai/", "/privacy/"]
    common.extend(f"/levels/{level}/" for level in data["level_order"])
    common.extend(f"/subjects/{course['area']}/" for course in data["courses"] if course["level"] == data["level_order"][0])
    common.extend(f"/courses/{course['level']}/{course['area']}/" for course in data["courses"])
    by_language = {language: (["/", "/about/"] if language in INDEXED_LANGUAGES else [])
                   for language in LANGUAGES}
    by_language["en"] = common
    for course_language, units in index.items():
        level, area, language = course_language.split("/")
        if language not in INDEXED_LANGUAGES:
            continue
        by_language[language].extend(f"/courses/{level}/{area}/lessons/{language}/{lesson['number']}/" for lesson in units["lessons"])
        by_language[language].extend(f"/courses/{level}/{area}/chapters/{language}/{chapter['number']}/" for chapter in units["chapters"])
    translation_groups: dict[tuple[str, ...], dict[str, str]] = {}
    for language in INDEXED_LANGUAGES:
        for route in ("/", "/about/"):
            translation_groups.setdefault((route,), {})[language] = site_for_language(language) + route
    for course_language, units in index.items():
        level, area, language = course_language.split("/")
        if language not in INDEXED_LANGUAGES:
            continue
        for kind in ("lessons", "chapters"):
            for unit in units[kind]:
                number = unit["number"]
                route = f"/courses/{level}/{area}/{kind}/{language}/{number}/"
                translation_groups.setdefault((level, area, kind, str(number)), {})[language] = site_for_language(language) + route
    alternates = {
        url: dict(sorted(variants.items()))
        for variants in translation_groups.values() if len(variants) > 1
        for url in variants.values()
    }
    for language, routes in by_language.items():
        xml = sitemap_xml(routes, language, alternates)
        OUTPUT.with_name(f"sitemap-{language}.xml").write_text(xml, encoding="utf-8")
        if language == "en":
            SITEMAP.write_text(xml, encoding="utf-8")
        print(f"{language}: {len(dict.fromkeys(routes))} canonical routes at {site_for_language(language)}")
