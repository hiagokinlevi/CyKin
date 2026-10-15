"""Validate the public, source-pinned five-choice practice for authored exercises."""

from __future__ import annotations

import json
from typing import Any


class InvalidPractice(ValueError):
    pass


def validate_practice(raw: str, level: str, area: str, language: str, route: str,
                      unit: int, source_sha256: str, exercise_ids: list[str]) -> dict[str, Any]:
    try:
        bank = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise InvalidPractice("Practice bank is not valid JSON") from exc
    if not isinstance(bank, dict) or bank.get("version") != 1:
        raise InvalidPractice("Unsupported practice bank version")
    if (bank.get("level"), bank.get("area"), bank.get("language"), bank.get("route"), bank.get("unit")) != (
        level, area, language, route, unit
    ):
        raise InvalidPractice("Practice bank belongs to another lesson")
    if bank.get("source_sha256") != source_sha256:
        raise InvalidPractice("The lesson changed; review its practice choices")
    questions = bank.get("questions")
    if not isinstance(questions, list) or not questions:
        raise InvalidPractice("Practice bank has no questions")
    allowed = {f"EX{digits}" for digits in exercise_ids}
    seen: set[str] = set()
    for question in questions:
        if not isinstance(question, dict):
            raise InvalidPractice("Malformed practice question")
        exercise_id = question.get("exercise_id")
        if exercise_id not in allowed or exercise_id in seen:
            raise InvalidPractice("Question has no unique authored exercise")
        seen.add(exercise_id)
        if not isinstance(question.get("prompt"), str) or len(question["prompt"].strip()) < 20:
            raise InvalidPractice("Question needs a substantial prompt")
        options = question.get("options")
        if not isinstance(options, list) or len(options) != 5 or any(not isinstance(item, dict) for item in options):
            raise InvalidPractice("Question needs exactly five options")
        if [item.get("id") for item in options] != list("abcde"):
            raise InvalidPractice("Question options must be labeled a through e")
        labels = [item.get("text") for item in options]
        if any(not isinstance(label, str) or len(label.strip()) < 8 for label in labels):
            raise InvalidPractice("Question options need meaningful text")
        if len({label.strip().casefold() for label in labels}) != 5:
            raise InvalidPractice("Question options must be distinct")
        if question.get("correct") not in "abcde":
            raise InvalidPractice("Question has no valid answer")
        if not isinstance(question.get("explanation"), str) or len(question["explanation"].strip()) < 40:
            raise InvalidPractice("Question needs a worked explanation")
    return bank
