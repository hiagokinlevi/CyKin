"""Verify Cloudflare Access JWTs before any private progress operation.

Uses the account's live JWKS so Access key rotation does not require a deploy.
RSA PKCS#1 v1.5 verification is implemented with stdlib to run in Python Workers.
"""

from __future__ import annotations

import asyncio
import base64
import hashlib
import hmac
import json
import time
from urllib.request import urlopen

from fastapi import HTTPException, Request


SHA256_DIGEST_INFO = bytes.fromhex("3031300d060960864801650304020105000420")
_key_cache: dict[str, tuple[float, list[dict]]] = {}


def decode_url64(value: str) -> bytes:
    return base64.urlsafe_b64decode(value + "=" * (-len(value) % 4))


def verify_rs256(message: bytes, signature: bytes, jwk: dict) -> bool:
    if jwk.get("kty") != "RSA" or jwk.get("alg") not in (None, "RS256") or jwk.get("use") not in (None, "sig"):
        return False
    try:
        modulus = int.from_bytes(decode_url64(jwk["n"]), "big")
        exponent = int.from_bytes(decode_url64(jwk["e"]), "big")
    except (KeyError, ValueError, TypeError):
        return False
    size = (modulus.bit_length() + 7) // 8
    if size < 256 or len(signature) != size or exponent < 3 or exponent % 2 == 0:
        return False
    decoded = pow(int.from_bytes(signature, "big"), exponent, modulus).to_bytes(size, "big")
    digest_info = SHA256_DIGEST_INFO + hashlib.sha256(message).digest()
    padding_length = size - len(digest_info) - 3
    if padding_length < 8:
        return False
    expected = b"\x00\x01" + b"\xff" * padding_length + b"\x00" + digest_info
    return hmac.compare_digest(decoded, expected)


async def signing_keys(team_domain: str) -> list[dict]:
    now = time.time()
    cached = _key_cache.get(team_domain)
    if cached and cached[0] > now:
        return cached[1]
    url = team_domain + "/cdn-cgi/access/certs"
    try:
        from js import fetch  # type: ignore[import-not-found]
    except ImportError:
        def load():
            with urlopen(url, timeout=8) as response:
                return json.loads(response.read(100_000))
        payload = await asyncio.to_thread(load)
    else:
        response = await fetch(url)
        if int(response.status) != 200:
            raise HTTPException(503, "Access signing keys are unavailable")
        payload = json.loads(str(await response.text()))
    keys = payload.get("keys", [])
    if not isinstance(keys, list) or not keys:
        raise HTTPException(503, "Access signing keys are unavailable")
    _key_cache[team_domain] = (now + 300, keys)
    return keys


async def identity(request: Request) -> dict:
    env = request.scope.get("env")
    team_domain = str(getattr(env, "ACCESS_TEAM_DOMAIN", "") or "").rstrip("/")
    audience = str(getattr(env, "ACCESS_AUD", "") or "")
    if not team_domain.startswith("https://") or not team_domain.endswith(".cloudflareaccess.com") or not audience:
        raise HTTPException(503, "Student sign-in is not configured")
    token = request.headers.get("cf-access-jwt-assertion", "")
    if not token or len(token) > 16_000:
        raise HTTPException(401, "Sign in to save your progress")
    try:
        first, second, third = token.split(".")
        header = json.loads(decode_url64(first))
        claims = json.loads(decode_url64(second))
        signature = decode_url64(third)
    except (ValueError, TypeError):
        raise HTTPException(401, "Invalid sign-in token") from None
    if not isinstance(header, dict) or not isinstance(claims, dict) or header.get("alg") != "RS256" or not isinstance(header.get("kid"), str):
        raise HTTPException(401, "Invalid sign-in token")
    now = int(time.time())
    aud = claims.get("aud")
    valid_audience = audience in aud if isinstance(aud, list) else aud == audience
    if claims.get("iss") != team_domain or claims.get("type") != "app" or not valid_audience or not isinstance(claims.get("exp"), (int, float)) or claims["exp"] <= now or not isinstance(claims.get("nbf"), (int, float)) or claims["nbf"] > now + 60 or not isinstance(claims.get("sub"), str) or not claims["sub"]:
        raise HTTPException(401, "Invalid sign-in token")
    try:
        keys = await signing_keys(team_domain)
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(503, "Access signing keys are unavailable") from exc
    key = next((item for item in keys if item.get("kid") == header["kid"]), None)
    if not key or not verify_rs256((first + "." + second).encode("ascii"), signature, key):
        raise HTTPException(401, "Invalid sign-in token")
    return {"sub": claims["sub"], "email": claims.get("email")}
