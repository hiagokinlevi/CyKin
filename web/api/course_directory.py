"""Render a course's current authored links from its published manuscript."""

from __future__ import annotations

import html


TEXT = {
    "en": ("Published lessons in this course", "Each link opens the current lesson on its permanent page.", "Lesson", "Chapter"),
    "pt": ("Aulas publicadas neste curso", "Cada link abre a aula atual em sua página permanente.", "Aula", "Capítulo"),
    "es": ("Lecciones publicadas en este curso", "Cada enlace abre la lección actual en su página permanente.", "Lección", "Capítulo"),
}


def render_course_directory(guide: dict, level: str, area: str, language: str, course_number: int) -> str:
    ui = TEXT.get(language, TEXT["en"])
    chapter_lessons = guide["chapter_lessons"]
    daily = [] if chapter_lessons else [unit for unit in guide["daily_slots"] if unit["published"]]
    chapters = [unit for unit in guide["legacy_chapters"] if unit["published"]]
    if not daily and not chapters:
        return '<div id="live-lesson-directory"></div>'
    code = f"OCA-{course_number:03d}"
    links = []
    for route, units, letter, label in (
        ("lessons", daily, "A", ui[2]),
        ("chapters", chapters, "A" if chapter_lessons else "C", ui[2] if chapter_lessons else ui[3]),
    ):
        for unit in units:
            number = unit["chapter"]
            title = html.escape(unit["title"])
            path = f"/courses/{level}/{area}/{route}/{language}/{number}/"
            links.append(f'<a href="{path}"><span>{code}-{letter}{number:03d} · {label} {number}:</span> {title}</a>')
    source_hash = html.escape(guide.get("source_sha256") or "", quote=True)
    return (
        f'<section id="live-lesson-directory" class="shell published-lesson-directory" data-source-sha256="{source_hash}" '
        f'aria-labelledby="published-lessons-title"><h2 id="published-lessons-title">{ui[0]}</h2>'
        f'<p>{ui[1]}</p><div class="published-lesson-links">{"".join(links)}</div></section>'
    )
