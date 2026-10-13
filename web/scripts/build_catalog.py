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
LANGUAGES = ("en", "pt", "es", "he", "fr", "ru", "de", "zh", "ja")
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
NUMBER = re.compile(r'Course\s+(\d{3})\s+of\s+207')


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
            "planned_chapters": chapters,
            "instructional_weeks": INSTRUCTIONAL_WEEKS[level],
            "study_days_per_week": 5,
            "daily_lesson_target": INSTRUCTIONAL_WEEKS[level] * 5,
            "minimum_exercises": max(50, INSTRUCTIONAL_WEEKS[level] * 5),
            "minimum_a4_pages": 300 + INSTRUCTIONAL_WEEKS[level] * 5 - 20,
            "editions": editions,
            "github": f"https://github.com/hiagokinlevi/CyKin/tree/main/levels/{level}/{area}",
        })
    courses.sort(key=lambda item: item["number"])
    if [item["number"] for item in courses] != list(range(1, 208)):
        raise ValueError("Expected courses numbered 001–207 exactly once")
    return {
        "name": "CyKin",
        "source": "https://github.com/hiagokinlevi/CyKin",
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
    OUTPUT.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    routes = ["/", "/levels/", "/subjects/", "/for-ai/"]
    routes.extend(f"/levels/{level}/" for level in data["level_order"])
    routes.extend(f"/subjects/{course['area']}/" for course in data["courses"] if course["level"] == data["level_order"][0])
    routes.extend(f"/courses/{course['level']}/{course['area']}/" for course in data["courses"])
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml += "".join(f"  <url><loc>{escape('https://cykin.org' + route)}</loc></url>\n" for route in routes)
    xml += "</urlset>\n"
    SITEMAP.write_text(xml, encoding="utf-8")
    print(f"Wrote {OUTPUT} with 207 courses and {SITEMAP} with {len(routes)} routes")
