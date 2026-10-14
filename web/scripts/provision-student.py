#!/usr/bin/env python3
"""Provision one password student from a secret supplied only through Keychain.

Run with the local decripte-secrets vault's suppressed-output `run` adapter.
The plaintext password never enters Git, SQL, command arguments or Wrangler's
environment. This script sends only a salted digest to D1.
"""

from __future__ import annotations

import argparse
import os
import re
import secrets
import subprocess
import sys
import time
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "api"))
from student_auth import password_digest  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("username")
    parser.add_argument("--dns-fallback", type=Path)
    parser.add_argument("--rotate", action="store_true", help="replace only this existing username's digest")
    args = parser.parse_args()
    if not re.fullmatch(r"[a-z][a-z0-9_-]{2,39}", args.username):
        return 2
    password = os.environ.get("STUDENT_PASSWORD", "")
    if not 12 <= len(password) <= 256:
        return 2
    salt = secrets.token_hex(16)
    digest = password_digest(password, salt)
    del password
    os.environ.pop("STUDENT_PASSWORD", None)
    child_env = dict(os.environ)
    if args.dns_fallback:
        if not args.dns_fallback.is_file() or args.dns_fallback.parent != Path("/tmp"):
            return 2
        child_env["NODE_OPTIONS"] = f"--require={args.dns_fallback}"
    def execute(sql: str) -> int:
        return subprocess.run(
            ["npx", "wrangler", "d1", "execute", "open-cyber-academy-progress", "--remote", "--command", sql],
            cwd=ROOT, env=child_env, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
            timeout=90, check=False,
        ).returncode

    if args.rotate:
        # The account is checked independently before and after this operation.
        update_sql = (
            "UPDATE student_password_credentials SET "
            f"password_salt = '{salt}', password_digest = '{digest}' "
            f"WHERE username = '{args.username}'"
        )
        return 0 if execute(update_sql) == 0 else 1
    now = int(time.time())
    student_id = secrets.token_urlsafe(18)
    email = f"{args.username}@students.invalid"
    account_sql = (
        "INSERT INTO student_accounts (id, email, created_at, last_login_at) "
        f"VALUES ('{student_id}', '{email}', {now}, {now})"
    )
    credential_sql = (
        "INSERT INTO student_password_credentials (user_id, username, password_salt, password_digest) "
        f"VALUES ('{student_id}', '{args.username}', '{salt}', '{digest}')"
    )
    if execute(account_sql) != 0:
        return 1
    if execute(credential_sql) != 0:
        execute(f"DELETE FROM student_accounts WHERE id = '{student_id}'")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
