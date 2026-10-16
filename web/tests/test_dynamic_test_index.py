"""The public test catalog discovers only source-verified GitHub banks."""

from __future__ import annotations

import asyncio
import importlib
import json
import sys
from types import SimpleNamespace

from fastapi import HTTPException, Request


api = importlib.import_module("app")
KEY = "rapid-1-month/cybersecurity/en"
MANUSCRIPT = "levels/rapid-1-month/cybersecurity/en/book/MANUSCRIPT.md"
PREFIX = "web/question-banks/rapid-1-month/cybersecurity/en"


def test_live_catalog_adds_verified_bank_and_ignores_invalid_bank(monkeypatch):
    old = {"chapter": 1, "bank_sha256": "a" * 64, "source_sha256": "b" * 64, "git_sha": "c" * 40}
    bundle = {"version": 1, "questions_per_chapter": 10,
              "courses": {KEY: [old]}, "book_git_sha": {KEY: "d" * 40}}
    tree = {"sha": "e" * 40, "truncated": False, "tree": [
        {"path": MANUSCRIPT, "type": "blob", "sha": "d" * 40},
        {"path": f"{PREFIX}/001.json", "type": "blob", "sha": "c" * 40},
        {"path": f"{PREFIX}/002.json", "type": "blob", "sha": "f" * 40},
        {"path": f"{PREFIX}/003.json", "type": "blob", "sha": "1" * 40},
    ]}
    requests = []

    async def asset(_request, _name, _path):
        return bundle

    async def courses(_request):
        return {"courses": [{"level": "rapid-1-month", "area": "cybersecurity"}]}

    async def bank(_request, _level, _area, _language, chapter, check_source=False):
        requests.append((chapter, check_source))
        if chapter == 3:
            raise HTTPException(409, "Source changed")
        return {"source_sha256": "2" * 64}, "3" * 64

    async def github_fetch(_url):
        return SimpleNamespace(status=200, text=lambda: asyncio.sleep(0, result=json.dumps(tree)))

    monkeypatch.setattr(api, "public_asset_json", asset)
    monkeypatch.setattr(api, "catalog", courses)
    monkeypatch.setattr(api, "chapter_test_bank", bank)
    monkeypatch.setattr(api, "_live_test_index", None)
    monkeypatch.setattr(api, "_live_test_index_until", 0.0)
    monkeypatch.setitem(sys.modules, "js", SimpleNamespace(fetch=github_fetch))
    request = Request({"type": "http", "method": "GET", "path": "/api/tests/catalog",
                       "headers": [], "env": object()})

    first = asyncio.run(api.test_index(request))
    again = asyncio.run(api.test_index(request))
    assert first is again
    assert first["live_sync"] == "github"
    assert [item["chapter"] for item in first["courses"][KEY]] == [1, 2]
    assert first["courses"][KEY][0] == old
    assert first["courses"][KEY][1]["bank_sha256"] == "3" * 64
    assert requests == [(2, True), (3, True)]
