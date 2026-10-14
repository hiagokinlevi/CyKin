"""Email-code authentication must protect student records without changing public study."""

from __future__ import annotations

import importlib
import re
import sqlite3
from pathlib import Path
from types import SimpleNamespace

from fastapi.testclient import TestClient


ROOT = Path(__file__).resolve().parents[2]
api = importlib.import_module("app")
student_auth = importlib.import_module("student_auth")
ORIGIN = {"Origin": "https://opencyber.academy"}


class Statement:
    def __init__(self, conn: sqlite3.Connection, query: str, args: tuple = ()):
        self.conn, self.query, self.args = conn, query, args

    def bind(self, *args):
        return Statement(self.conn, self.query, args)

    async def all(self):
        return {"results": [dict(row) for row in self.conn.execute(self.query, self.args).fetchall()]}

    async def run(self):
        before = self.conn.total_changes
        self.conn.execute(self.query, self.args)
        self.conn.commit()
        return {"meta": {"changes": self.conn.total_changes - before}}


class Database:
    def __init__(self):
        self.conn = sqlite3.connect(":memory:", check_same_thread=False)
        self.conn.row_factory = sqlite3.Row
        for migration in ("0001_progress.sql", "0002_chapter_tests.sql", "0003_student_auth.sql"):
            self.conn.executescript((ROOT / "web/migrations" / migration).read_text())

    def prepare(self, query: str):
        return Statement(self.conn, query)


class EmailSender:
    def __init__(self):
        self.messages = []

    async def send(self, message):
        self.messages.append(message)


class Environment:
    def __init__(self, app, env):
        self.app, self.env = app, env

    async def __call__(self, scope, receive, send):
        scope["env"] = self.env
        await self.app(scope, receive, send)


def test_email_code_session_and_legacy_boundary(monkeypatch):
    db, sender = Database(), EmailSender()
    now = [1_000_000.0]
    monkeypatch.setattr(student_auth.time, "time", lambda: now[0])
    env = SimpleNamespace(DB=db, EMAIL=sender, AUTH_HMAC_KEY="a" * 64)
    try:
        with TestClient(Environment(api.app, env), base_url="https://opencyber.academy") as client:
            assert client.get("/auth/me").status_code == 401
            assert client.get("/student/progress").status_code == 401
            assert client.post("/auth/request-code", json={"email": "student@example.test"}, headers={"Origin": "https://attacker.invalid"}).status_code == 403
            created = client.post("/auth/request-code", json={"email": "Student@Example.test", "language": "en"}, headers=ORIGIN)
            assert created.status_code == 200
            flow_id = created.json()["flow_id"]
            assert sender.messages[0]["to"] == "student@example.test"
            code = re.search(r"\b[0-9]{6}\b", sender.messages[0]["text"]).group()
            stored = dict(db.conn.execute("SELECT * FROM login_challenges").fetchone())
            assert code not in stored.values()
            assert stored["code_digest"] != code
            assert client.post("/auth/verify-code", json={"flow_id": flow_id, "code": "000000"}, headers=ORIGIN).status_code == 400
            verified = client.post("/auth/verify-code", json={"flow_id": flow_id, "code": code}, headers=ORIGIN)
            assert verified.status_code == 200
            cookie = verified.headers["set-cookie"].lower()
            assert "httponly" in cookie and "secure" in cookie and "samesite=lax" in cookie
            assert "domain=opencyber.academy" in cookie
            assert client.get("/auth/me").json()["email"] == "student@example.test"
            assert client.get("/student/progress").json() == {"lessons": [], "exercises": []}
            assert client.get("/private/me").status_code == 503  # old Access route still needs its JWT
            assert client.post("/auth/verify-code", json={"flow_id": flow_id, "code": code}, headers=ORIGIN).status_code == 400
            assert client.post("/auth/logout", json={}, headers=ORIGIN).status_code == 200
            assert client.get("/auth/me").status_code == 401
            assert client.get("/student/progress").status_code == 401
    finally:
        db.conn.close()


def test_expiry_attempt_limit_and_email_request_limit(monkeypatch):
    db, sender = Database(), EmailSender()
    now = [2_000_000.0]
    monkeypatch.setattr(student_auth.time, "time", lambda: now[0])
    env = SimpleNamespace(DB=db, EMAIL=sender, AUTH_HMAC_KEY="b" * 64)
    try:
        with TestClient(Environment(api.app, env), base_url="https://opencyber.academy") as client:
            def ask(address):
                return client.post("/auth/request-code", json={"email": address}, headers=ORIGIN)
            first = ask("learner@example.test")
            assert first.status_code == 200
            flow_id = first.json()["flow_id"]
            code = re.search(r"\b[0-9]{6}\b", sender.messages[-1]["text"]).group()
            for _ in range(5):
                assert client.post("/auth/verify-code", json={"flow_id": flow_id, "code": "999999" if code != "999999" else "000000"}, headers=ORIGIN).status_code == 400
            assert client.post("/auth/verify-code", json={"flow_id": flow_id, "code": code}, headers=ORIGIN).status_code == 400
            assert ask("learner@example.test").status_code == 200
            assert ask("learner@example.test").status_code == 200
            assert ask("learner@example.test").status_code == 429
            newer = db.conn.execute("SELECT id FROM login_challenges ORDER BY created_at DESC, rowid DESC LIMIT 1").fetchone()[0]
            newer_code = re.search(r"\b[0-9]{6}\b", sender.messages[-1]["text"]).group()
            now[0] += 901
            assert client.post("/auth/verify-code", json={"flow_id": newer, "code": newer_code}, headers=ORIGIN).status_code == 400
    finally:
        db.conn.close()
