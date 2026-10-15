#!/usr/bin/env python3
"""Require an authored worked answer for every published exercise ID."""

from __future__ import annotations

from collections import Counter
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[2]
PROMPT = re.compile(r'^[ \t]*(?:#{3,6}[ \t]+|[-*][ \t]+)?(?:\*\*)?EX(\d{3,4})\b', re.M)
ANSWER = re.compile(r'^###\s+EX(\d{3,4})\b.*$|^\*\*EX(\d{3,4})(?:\s+[—-]|\.)[^\n]*$', re.M)
APPENDIX = re.compile(
    r'^##\s+(?:(?:final\s+appendix|apêndice\s+final|apendice\s+final|apéndice\s+final)\s+[—–:-]\s+)?'
    r'(?:worked\s+(?:results|answers)|answer\s+key|gabarito|respostas|resoluções|resultados(?:\s+resueltos)?|soluciones|resoluciones)\b',
    re.M | re.I,
)


def check() -> dict[str, Counter]:
    totals: dict[str, Counter] = {}
    gaps: list[str] = []
    for path in sorted((ROOT / "levels").glob("*/*/*/book/MANUSCRIPT.md")):
        language = path.parts[-3]
        text = path.read_text(encoding="utf-8")
        appendix = APPENDIX.search(text)
        teaching = text[:appendix.start()] if appendix else text
        prompts = set(PROMPT.findall(teaching))
        answers = ({match.group(1) or match.group(2) for match in ANSWER.finditer(text[appendix.end():])}
                   if appendix else set())
        missing = sorted(prompts - answers)
        if missing:
            gaps.append(f"{path.relative_to(ROOT)}: missing worked answers for {', '.join('EX' + item for item in missing)}")
        count = totals.setdefault(language, Counter())
        count["books"] += 1
        count["exercise_answer_pairs"] += len(prompts & answers)
    if gaps:
        raise ValueError("\n".join(gaps))
    return totals


if __name__ == "__main__":
    for language, count in sorted(check().items()):
        print(f"{language}: {count['books']} authored books, {count['exercise_answer_pairs']} exercise/answer pairs")
