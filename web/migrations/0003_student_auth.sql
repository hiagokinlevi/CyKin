CREATE TABLE IF NOT EXISTS student_accounts (
  id TEXT PRIMARY KEY,
  email TEXT NOT NULL UNIQUE,
  created_at INTEGER NOT NULL,
  last_login_at INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS login_challenges (
  id TEXT PRIMARY KEY,
  email TEXT NOT NULL,
  code_digest TEXT NOT NULL,
  expires_at INTEGER NOT NULL,
  attempts INTEGER NOT NULL DEFAULT 0,
  used_at INTEGER,
  created_at INTEGER NOT NULL
);

CREATE INDEX IF NOT EXISTS login_challenges_expires_at ON login_challenges (expires_at);

CREATE TABLE IF NOT EXISTS student_sessions (
  token_digest TEXT PRIMARY KEY,
  user_id TEXT NOT NULL,
  created_at INTEGER NOT NULL,
  expires_at INTEGER NOT NULL,
  revoked_at INTEGER
);

CREATE INDEX IF NOT EXISTS student_sessions_user_id ON student_sessions (user_id, expires_at);

CREATE TABLE IF NOT EXISTS auth_limits (
  key TEXT PRIMARY KEY,
  count INTEGER NOT NULL,
  expires_at INTEGER NOT NULL
);
