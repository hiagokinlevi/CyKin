"""Read-only CyKin REST and stateless MCP API for Cloudflare Python Workers."""

from __future__ import annotations

import asyncio
import json
import re
from pathlib import Path
from typing import Any
from urllib.error import HTTPError
from urllib.request import urlopen

from fastapi import FastAPI, HTTPException, Query, Request
from fastapi.responses import FileResponse, JSONResponse, PlainTextResponse, RedirectResponse, Response
from pydantic import BaseModel, Field

from access import identity


app = FastAPI(title="CyKin public learning API", version="0.1.0", docs_url="/api/docs", openapi_url="/api/openapi.json")
GITHUB_RAW = "https://raw.githubusercontent.com/hiagokinlevi/CyKin/main/"
GITHUB_VIEW = "https://github.com/hiagokinlevi/CyKin/blob/main/"
CATALOG_PATH = Path(__file__).resolve().parents[1] / "public" / "catalog.json"
ANCHOR = re.compile(r'^<a id="ch-(\d{2})"></a>\s*$', re.M)
EXERCISE = re.compile(r'\bEX(\d{3})\b')
ANSWER = re.compile(r'^###\s+EX(\d{3})\b.*$', re.M)
MCP_VERSION = "2025-06-18"
ALLOWED_ORIGINS = {"https://cykin.org", "https://www.cykin.org", "http://localhost:4321", "http://localhost:8787", "http://127.0.0.1:8787"}
MAX_SOURCE_CHARS = 3_000_000
PUBLIC_ORIGINS = {"https://cykin.org", "https://www.cykin.org"}


class LessonProgress(BaseModel):
    level: str = Field(pattern=r"^[a-z0-9-]+$", max_length=50)
    area: str = Field(pattern=r"^[a-z0-9-]+$", max_length=80)
    language: str = Field(pattern=r"^[a-z]{2}$")
    chapter: int = Field(ge=1, le=99)
    status: str = Field(pattern=r"^(in_progress|completed)$")


class ExerciseAttempt(LessonProgress):
    exercise_id: str = Field(pattern=r"^EX[0-9]{3}$")
    answer: str = Field(default="", max_length=20_000)
    status: str = Field(pattern=r"^(attempted|completed)$")


@app.middleware("http")
async def canonical_domain(request: Request, call_next):

@app.get("/mcp")
async def mcp_get() -> Response:
    return Response(status_code=405, headers={"Allow": "POST"})


@app.get("/{path:path}", include_in_schema=False)
async def static_assets(path: str, request: Request) -> Response:
    asset = path.strip("/")
    if not asset or "." not in asset.rsplit("/", 1)[-1]:
        asset = (asset + "/" if asset else "") + "index.html"
    env = request.scope.get("env")
    if env is not None:
        response = await env.ASSETS.fetch("https://assets.local/" + asset)
        content = await response.bytes()
        return Response(content=content, status_code=int(response.status), headers=dict(response.headers))
    root = Path(__file__).resolve().parents[1] / "dist"
    target = (root / asset).resolve()
    if not target.is_relative_to(root.resolve()) or not target.is_file():
        raise HTTPException(404, "Page not found")
    return FileResponse(target)
