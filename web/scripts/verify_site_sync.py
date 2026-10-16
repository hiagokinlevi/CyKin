#!/usr/bin/env python3
"""Verify that the public Academy serves the current GitHub content and site build."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
import time
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[2]
SITE = "https://opencyber.academy"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def fetch(path: str) -> bytes:
    request = Request(SITE + path, headers={"User-Agent": "OpenCyberAcademy-local-site-check",
                                            "Cache-Control": "no-cache"})
    with urlopen(request, timeout=45) as response:
        if response.status != 200:
            raise ValueError(f"Unexpected HTTP {response.status} for {path}")
        return response.read()


def fetch_json(path: str) -> dict:
    data = json.loads(fetch(path))
    if not isinstance(data, dict):
        raise ValueError(f"Expected JSON object at {path}")
    return data


def test_rows(courses: dict) -> dict[str, list[tuple]]:
    return {key: [(item["chapter"], item["bank_sha256"], item["source_sha256"])
                  for item in chapters] for key, chapters in courses.items()}


def changed_markdown(previous: str, current: str) -> list[str]:
    if not re.fullmatch(r"[a-f0-9]{40}", previous or ""):
        return ["README.md", "BOOK_STANDARD.md",
                "levels/rapid-1-month/data-governance/en/book/MANUSCRIPT.md"]
    if subprocess.run(["git", "merge-base", "--is-ancestor", previous, current],
                      cwd=ROOT, check=False).returncode:
        raise ValueError("Previous verified commit is not an ancestor of main")
    paths = git("diff", "--name-only", "--diff-filter=AM", previous, current).splitlines()
    return sorted(path for path in paths if path.endswith(".md") and (ROOT / path).is_file())


def verify(previous: str) -> dict:
    current = git("rev-parse", "HEAD")
    web_tree = git("rev-parse", "HEAD:web")
    release = fetch_json(f"/site-release.json?check={time.time_ns()}")
    if release.get("version") != 1 or release.get("web_tree_sha") != web_tree:
        raise ValueError("The deployed site assets do not match the GitHub web tree")

    health = fetch_json("/api/health")
    if health.get("status") != "ok":
        raise ValueError("The public Academy health check failed")
    catalog = fetch_json("/api/catalog")
    if len(catalog.get("courses", [])) != 207 or len(catalog.get("languages", [])) != 9:
        raise ValueError("The public course catalog is incomplete")

    expected = json.loads((ROOT / "web/public/test-index.json").read_text(encoding="utf-8"))
    live = fetch_json("/api/tests/catalog")
    # Some Worker isolates temporarily use the deployed index when GitHub is
    # unavailable. That is safe only when it exactly matches the current banks.
    if live.get("live_sync") not in {"github", "bundled"} or test_rows(live.get("courses", {})) != test_rows(expected["courses"]):
        raise ValueError("The public test catalog differs from the validated GitHub banks")

    documents = sorted(set(changed_markdown(previous, current)) | {
        "BOOK_STANDARD.md",
        "levels/rapid-1-month/data-governance/en/book/MANUSCRIPT.md",
    })
    for path in documents:
        public = fetch("/api/source?path=" + quote(path, safe="/"))
        if hashlib.sha256(public).digest() != hashlib.sha256((ROOT / path).read_bytes()).digest():
            raise ValueError(f"The public reader differs from GitHub: {path}")

    tabletop = fetch("/tabletop/").decode("utf-8")
    scenarios = json.loads((ROOT / "web/tabletop/scenarios.json").read_text(encoding="utf-8"))["scenarios"]
    if len(scenarios) != 10 or any(f'/tabletop/{item["id"]}/' not in tabletop for item in scenarios):
        raise ValueError("The public TableTop index is incomplete")
    if previous and "web/tabletop/scenarios.json" in git("diff", "--name-only", previous, current).splitlines():
        for item in scenarios:
            fetch(f'/tabletop/{quote(item["id"])}/')

    return {"git_sha": current, "web_tree_sha": web_tree,
            "deployed_git_sha": release.get("git_sha"), "books_and_docs_checked": len(documents),
            "courses": len(catalog["courses"]), "question_banks": sum(map(len, live["courses"].values())),
            "tabletop_scenarios": len(scenarios), "test_catalog_mode": live.get("live_sync"),
            "test_catalog_source_head": live.get("source_head")}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--previous", default="")
    result = verify(parser.parse_args().previous)
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
