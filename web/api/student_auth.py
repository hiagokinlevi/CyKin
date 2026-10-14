"""Passwordless student accounts backed by D1 and Cloudflare Email Sending.

The public books stay anonymous. Only a verified email code creates a student
account; the browser receives an opaque, revocable session cookie. Neither the
one-time code nor the session token is stored in plaintext in D1.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import re
import secrets
import time
from typing import Any

from fastapi import APIRouter, HTTPException, Request
from fastapi.responses import JSONResponse, Response
from pydantic import BaseModel, Field

from locales import LANGUAGES, site_for_language


router = APIRouter()
COOKIE = "__Secure-oca_session"
SENDER = "login@auth.opencyber.academy"
CODE_LIFETIME = 600
SESSION_LIFETIME = 7 * 24 * 60 * 60
PUBLIC_ORIGINS = {site_for_language(language) for language in LANGUAGES} | {"https://www.opencyber.academy", "http://localhost:4321", "http://localhost:8787", "http://127.0.0.1:8787"}
EMAIL_PATTERN = re.compile(r"^[A-Za-z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Za-z0-9](?:[A-Za-z0-9.-]*[A-Za-z0-9])?\.[A-Za-z]{2,63}$")


class CodeRequest(BaseModel):
    email: str = Field(min_length=3, max_length=254)
    language: str = Field(default="en", pattern=r"^(en|pt|es)$")


class CodeVerification(BaseModel):
    flow_id: str = Field(pattern=r"^[A-Za-z0-9_-]{24,80}$")
    code: str = Field(pattern=r"^[0-9]{6}$")


def _database(request: Request):
    db = getattr(request.scope.get("env"), "DB", None)
    if db is None:
        raise HTTPException(503, "Student account storage is unavailable")
    return db


def _secret(request: Request) -> bytes:
    value = str(getattr(request.scope.get("env"), "AUTH_HMAC_KEY", "") or "")
    if len(value) < 64:
        raise HTTPException(503, "Student sign-in is not configured")
    return value.encode("utf-8")


def _origin(request: Request) -> None:
    if request.headers.get("origin", "") not in PUBLIC_ORIGINS:
        raise HTTPException(403, "Sign-in must begin on OpenCyber Academy")


def _rows(result: Any) -> list[dict]:
    if isinstance(result, dict):
        return result.get("results", [])
    from js import JSON  # type: ignore[import-not-found]
    return json.loads(str(JSON.stringify(result))).get("results", [])


def _changes(result: Any) -> int:
    if isinstance(result, dict):
        return int(result.get("meta", {}).get("changes", 0))
    from js import JSON  # type: ignore[import-not-found]
    return int(json.loads(str(JSON.stringify(result))).get("meta", {}).get("changes", 0))


def _digest(key: bytes, value: str) -> str:
    return hmac.new(key, value.encode("utf-8"), hashlib.sha256).hexdigest()


def _email(value: str) -> str:
    normalized = value.strip().lower()
    if not EMAIL_PATTERN.fullmatch(normalized) or ".." in normalized or len(normalized) > 254:
        raise HTTPException(422, "Enter a valid email address")
    return normalized


async def _limit(db: Any, key: str, expiry: int, maximum: int) -> None:
    result = await db.prepare(
        "INSERT INTO auth_limits (key, count, expires_at) VALUES (?, 1, ?) "
        "ON CONFLICT(key) DO UPDATE SET count = count + 1 WHERE count < ?"
    ).bind(key, expiry, maximum).run()
    if _changes(result) != 1:
        raise HTTPException(429, "Too many sign-in requests. Try again later")


async def _prune_expired(db: Any, now: int) -> None:
    # This runs occasionally on new requests, avoiding a separate scheduler
    # while keeping short-lived challenges and sessions out of D1 indefinitely.
    if secrets.randbelow(64) != 0:
        return
    await db.prepare("DELETE FROM login_challenges WHERE expires_at < ?").bind(now - 86400).run()
    await db.prepare("DELETE FROM student_sessions WHERE expires_at < ?").bind(now - 86400).run()
    await db.prepare("DELETE FROM auth_limits WHERE expires_at < ?").bind(now - 86400).run()


def _mail(language: str, code: str) -> tuple[str, str]:
    if language == "pt":
        return "Seu código de acesso à OpenCyber Academy", f"Seu código de acesso é {code}. Ele expira em 10 minutos. Se você não solicitou este código, ignore este email."
    if language == "es":
        return "Tu código de acceso a OpenCyber Academy", f"Tu código de acceso es {code}. Caduca en 10 minutos. Si no lo solicitaste, ignora este correo."
    return "Your OpenCyber Academy sign-in code", f"Your sign-in code is {code}. It expires in 10 minutes. If you did not request it, ignore this email."


async def _send(request: Request, recipient: str, language: str, code: str) -> None:
    binding = getattr(request.scope.get("env"), "EMAIL", None)
    if binding is None:
        raise HTTPException(503, "Email sign-in is unavailable")
    subject, body = _mail(language, code)
    message: Any = {"to": recipient, "from": SENDER, "subject": subject, "text": body}
    try:
        from js import Object  # type: ignore[import-not-found]
        from pyodide.ffi import to_js  # type: ignore[import-not-found]
    except ImportError:
        pass  # Local tests supply a Python email binding.
    else:
        message = to_js(message, dict_converter=Object.fromEntries)
    try:
        await binding.send(message)
    except Exception as exc:
        raise HTTPException(503, "Email sign-in is temporarily unavailable") from exc


@router.post("/auth/request-code")
async def request_code(request: Request, payload: CodeRequest) -> Response:
    _origin(request)
    key = _secret(request)
    db = _database(request)
    if getattr(request.scope.get("env"), "EMAIL", None) is None:
        raise HTTPException(503, "Email sign-in is unavailable")
    email = _email(payload.email)
    now = int(time.time())
    await _prune_expired(db, now)
    email_key = _digest(key, "email:" + email)
    ip = request.headers.get("cf-connecting-ip") or (request.client.host if request.client else "unknown")
    ip_key = _digest(key, "ip:" + ip)
    await _limit(db, f"email:{email_key}:{now // 900}", (now // 900 + 1) * 900, 3)
    await _limit(db, f"ip:{ip_key}:{now // 3600}", (now // 3600 + 1) * 3600, 10)
    # Stay below Email Sending's account-wide included allocation unless an
    # operator explicitly changes this cap after reviewing usage.
    month = time.strftime("%Y-%m", time.gmtime(now))
    await _limit(db, f"monthly:{month}", now + 35 * 86400, 2500)
    flow_id = secrets.token_urlsafe(24)
    code = f"{secrets.randbelow(1_000_000):06d}"
    code_digest = _digest(key, f"code:{flow_id}:{code}")
    await db.prepare(
        "INSERT INTO login_challenges (id, email, code_digest, expires_at, created_at) VALUES (?, ?, ?, ?, ?)"
    ).bind(flow_id, email, code_digest, now + CODE_LIFETIME, now).run()
    try:
        await _send(request, email, payload.language, code)
    except HTTPException:
        await db.prepare("DELETE FROM login_challenges WHERE id = ?").bind(flow_id).run()
        raise
    return JSONResponse({"flow_id": flow_id, "expires_in": CODE_LIFETIME,
                         "message": "If the address can receive mail, a sign-in code has been sent."},
                        headers={"Cache-Control": "no-store"})


@router.post("/auth/verify-code")
async def verify_code(request: Request, payload: CodeVerification) -> Response:
    _origin(request)
    key = _secret(request)
    db = _database(request)
    now = int(time.time())
    found = _rows(await db.prepare(
        "SELECT email, code_digest, expires_at, attempts, used_at FROM login_challenges WHERE id = ?"
    ).bind(payload.flow_id).all())
    if not found:
        raise HTTPException(400, "Invalid or expired code")
    challenge = found[0]
    if challenge["used_at"] is not None or int(challenge["expires_at"]) <= now or int(challenge["attempts"]) >= 5:
        raise HTTPException(400, "Invalid or expired code")
    digest = _digest(key, f"code:{payload.flow_id}:{payload.code}")
    if not hmac.compare_digest(digest, challenge["code_digest"]):
        await db.prepare(
            "UPDATE login_challenges SET attempts = attempts + 1 WHERE id = ? AND used_at IS NULL AND attempts < 5"
        ).bind(payload.flow_id).run()
        raise HTTPException(400, "Invalid or expired code")
    consumed = await db.prepare(
        "UPDATE login_challenges SET used_at = ? WHERE id = ? AND used_at IS NULL AND attempts < 5 AND expires_at > ? AND code_digest = ?"
    ).bind(now, payload.flow_id, now, digest).run()
    if _changes(consumed) != 1:
        raise HTTPException(400, "Invalid or expired code")
    candidate_id = secrets.token_urlsafe(18)
    await db.prepare(
        "INSERT OR IGNORE INTO student_accounts (id, email, created_at, last_login_at) VALUES (?, ?, ?, ?)"
    ).bind(candidate_id, challenge["email"], now, now).run()
    account = _rows(await db.prepare("SELECT id FROM student_accounts WHERE email = ?").bind(challenge["email"]).all())
    if not account:
        raise HTTPException(503, "Student account storage is unavailable")
    student_id = account[0]["id"]
    await db.prepare("UPDATE student_accounts SET last_login_at = ? WHERE id = ?").bind(now, student_id).run()
    token = secrets.token_urlsafe(32)
    await db.prepare(
        "INSERT INTO student_sessions (token_digest, user_id, created_at, expires_at) VALUES (?, ?, ?, ?)"
    ).bind(hashlib.sha256(token.encode()).hexdigest(), student_id, now, now + SESSION_LIFETIME).run()
    response = JSONResponse({"signed_in": True}, headers={"Cache-Control": "no-store"})
    response.set_cookie(COOKIE, token, max_age=SESSION_LIFETIME, domain="opencyber.academy", path="/",
                        secure=True, httponly=True, samesite="lax")
    return response


async def student_identity(request: Request) -> dict:
    token = request.cookies.get(COOKIE, "")
    if len(token) < 32 or len(token) > 100 or not re.fullmatch(r"[A-Za-z0-9_-]+", token):
        raise HTTPException(401, "Sign in to save your progress")
    db = _database(request)
    now = int(time.time())
    rows = _rows(await db.prepare(
        "SELECT a.id, a.email FROM student_sessions s JOIN student_accounts a ON a.id = s.user_id "
        "WHERE s.token_digest = ? AND s.expires_at > ? AND s.revoked_at IS NULL"
    ).bind(hashlib.sha256(token.encode()).hexdigest(), now).all())
    if not rows:
        raise HTTPException(401, "Sign in to save your progress")
    return {"sub": rows[0]["id"], "email": rows[0]["email"]}


@router.get("/auth/me")
async def auth_me(request: Request) -> Response:
    user = await student_identity(request)
    return JSONResponse({"student_id": user["sub"], "email": user["email"]}, headers={"Cache-Control": "no-store"})


@router.post("/auth/logout")
async def auth_logout(request: Request) -> Response:
    _origin(request)
    token = request.cookies.get(COOKIE, "")
    if token and re.fullmatch(r"[A-Za-z0-9_-]{32,100}", token):
        await _database(request).prepare(
            "UPDATE student_sessions SET revoked_at = ? WHERE token_digest = ? AND revoked_at IS NULL"
        ).bind(int(time.time()), hashlib.sha256(token.encode()).hexdigest()).run()
    response = JSONResponse({"signed_out": True}, headers={"Cache-Control": "no-store"})
    response.delete_cookie(COOKIE, domain="opencyber.academy", path="/")
    return response
