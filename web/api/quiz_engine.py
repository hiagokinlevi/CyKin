"""Validation and scoring for authored chapter question banks.

The bank is public study material. This is a timed self-assessment, not a
proctored or accredited exam: publishing the source also publishes its key.
"""

from __future__ import annotations

import hashlib
import json
import re
from typing import Any


QUESTION_IDS = tuple(f"Q{number:02d}" for number in range(1, 11))
OPTION_IDS = ("a", "b", "c", "d")
SLUG = re.compile(r"^[a-z0-9-]+$")


class InvalidBank(ValueError):
    pass


def validate_bank(raw: str, level: str, area: str, language: str, chapter: int) -> tuple[dict[str, Any], str]:
    try:
        bank = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise InvalidBank("Question bank is not valid JSON") from exc
    if not isinstance(bank, dict) or bank.get("version") != 1:
        raise InvalidBank("Question bank version is unsupported")
    if (bank.get("level"), bank.get("area"), bank.get("language"), bank.get("chapter")) != (level, area, language, chapter):
        raise InvalidBank("Question bank belongs to a different chapter")
    if not all(SLUG.fullmatch(value) for value in (level, area, language)):
        raise InvalidBank("Invalid course identity")
    if bank.get("source_anchor") != f"ch-{chapter:02d}":
        raise InvalidBank("Question bank has no matching chapter anchor")
    if not isinstance(bank.get("source_sha256"), str) or not re.fullmatch(r"[a-f0-9]{64}", bank["source_sha256"]):
        raise InvalidBank("Question bank has no pinned source chapter")
    questions = bank.get("questions")
    if not isinstance(questions, list) or len(questions) != 10:
        raise InvalidBank("A published chapter test needs exactly ten questions")
    prompts: set[str] = set()
    for number, question in enumerate(questions):
        if not isinstance(question, dict) or question.get("id") != QUESTION_IDS[number]:
            raise InvalidBank("Question IDs must run from Q01 to Q10")
        prompt = question.get("prompt")
        if not isinstance(prompt, str) or len(prompt.strip()) < 20 or prompt.casefold() in prompts:
            raise InvalidBank("Every question needs a distinct, substantial prompt")
        prompts.add(prompt.casefold())
        options = question.get("options")
        if not isinstance(options, list) or len(options) != 4 or [item.get("id") for item in options if isinstance(item, dict)] != list(OPTION_IDS):
            raise InvalidBank("Every question needs four labeled options")
        labels = [item.get("text") for item in options]
        if any(not isinstance(label, str) or len(label.strip()) < 3 for label in labels) or len({label.strip().casefold() for label in labels}) != 4:
            raise InvalidBank("Question options must be distinct and meaningful")
        if question.get("correct") not in OPTION_IDS:
            raise InvalidBank("Question has no valid answer")
        if not isinstance(question.get("explanation"), str) or len(question["explanation"].strip()) < 30:
            raise InvalidBank("Question needs a worked explanation")
        if not isinstance(question.get("source"), str) or not question["source"].strip():
            raise InvalidBank("Question needs a source section")
    return bank, hashlib.sha256(raw.encode("utf-8")).hexdigest()


def public_question(bank: dict[str, Any], index: int, deadline_ms: int, now_ms: int) -> dict[str, Any]:
    item = bank["questions"][index]
    return {
        "number": index + 1,
        "total": 10,
        "id": item["id"],
        "prompt": item["prompt"],
        "options": item["options"],
        "deadline_ms": deadline_ms,
        "server_now_ms": now_ms,
        "seconds": 10,
    }


def score_answer(bank: dict[str, Any], index: int, selected: str | None, on_time: bool) -> dict[str, Any]:
    item = bank["questions"][index]
    return {
        "id": item["id"],
        "selected": selected,
        "correct": selected == item["correct"] and on_time,
        "timed_out": not on_time,
    }


def feedback(bank: dict[str, Any], answers: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        {**answer, "answer": item["correct"], "explanation": item["explanation"], "source": item["source"]}
        for item, answer in zip(bank["questions"], answers, strict=True)
    ]
