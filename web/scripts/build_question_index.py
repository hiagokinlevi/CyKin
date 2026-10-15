#!/usr/bin/env python3
"""Publish the availability of reviewed chapter tests, never their answer keys."""

from __future__ import annotations

import json
import hashlib
import re
import sys
from pathlib import Path

WEB = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(WEB / "api"))

from quiz_engine import InvalidBank, validate_bank  # noqa: E402


def authored_chapter(markdown: str, number: int) -> str | None:
    anchors = list(re.finditer(r'^<a id="ch-(\d{2,4})"></a>\s*$', markdown, re.M))
    for index, match in enumerate(anchors):
        if int(match.group(1)) != number:
            continue
        stop = anchors[index + 1].start() if index + 1 < len(anchors) else len(markdown)
        body = markdown[match.start():stop].strip()
        heading = re.search(r'^#{2,3}\s+(.+)$', body, re.M)
        if heading is None:
            return None
        if index == len(anchors) - 1:
            tail = body[heading.end():]
            endings = [found.start() for pattern in (
                re.compile(r'^##\s+(?:(?:final\s+appendix|apêndice\s+final|apendice\s+final|apéndice\s+final)\s+[—–:-]\s+)?(?:worked\s+(?:results|answers)|answer\s+key|gabarito|respostas|resoluções|resultados(?:\s+resueltos)?|soluciones|resoluciones)\b', re.M | re.I),
                re.compile(r'^##\s+(?:references|referências|referencias)\b', re.M | re.I),
            ) if (found := pattern.search(tail))]
            if endings:
                body = body[:heading.end() + min(endings)].rstrip()
        return body
    return None


def build() -> dict:
    courses: dict[str, list[dict]] = {}
    root = WEB / "question-banks"
    for path in sorted(root.glob("*/*/*/*.json")):
        level, area, language = path.parts[-4:-1]
        try:
            chapter = int(path.stem)
        except ValueError as exc:
            raise ValueError(f"Question bank filename must be a chapter number: {path}") from exc
        if path.name != f"{chapter:03d}.json":
            raise ValueError(f"Question bank filename must use three digits: {path}")
        try:
            bank, digest = validate_bank(path.read_text(encoding="utf-8"), level, area, language, chapter)
        except InvalidBank as exc:
            raise ValueError(f"{path}: {exc}") from exc
        manuscript = WEB.parent / "levels" / level / area / language / "book" / "MANUSCRIPT.md"
        section = authored_chapter(manuscript.read_text(encoding="utf-8"), chapter) if manuscript.is_file() else None
        if section is None:
            raise ValueError(f"Question bank has no authored chapter: {path}")
        if hashlib.sha256(section.encode("utf-8")).hexdigest() != bank["source_sha256"]:
            raise ValueError(f"Question bank needs review after chapter changed: {path}")
        key = f"{level}/{area}/{language}"
        courses.setdefault(key, []).append({"chapter": chapter, "bank_sha256": digest, "source_sha256": bank["source_sha256"]})
    for chapters in courses.values():
        chapters.sort(key=lambda item: item["chapter"])
    return {"version": 1, "questions_per_chapter": 10, "courses": dict(sorted(courses.items()))}


if __name__ == "__main__":
    output = WEB / "public" / "test-index.json"
    output.write_text(json.dumps(build(), ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
