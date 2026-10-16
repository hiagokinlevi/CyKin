#!/usr/bin/env python3
"""Stamp static assets with the exact Git revision used for a local deploy."""

from __future__ import annotations

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "web/public/site-release.json"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def main() -> None:
    release = {
        "version": 1,
        "git_sha": git("rev-parse", "HEAD"),
        "web_tree_sha": git("rev-parse", "HEAD:web"),
        "built_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    OUTPUT.write_text(json.dumps(release, separators=(",", ":")) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
