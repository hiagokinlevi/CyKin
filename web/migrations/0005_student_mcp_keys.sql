CREATE TABLE IF NOT EXISTS student_mcp_keys (
  id TEXT PRIMARY KEY,
  user_id TEXT NOT NULL,
  label TEXT NOT NULL,
  token_digest TEXT NOT NULL UNIQUE,
  token_prefix TEXT NOT NULL,
  created_at INTEGER NOT NULL,
  expires_at INTEGER NOT NULL,
  last_used_at INTEGER,
  use_count INTEGER NOT NULL DEFAULT 0,
  revoked_at INTEGER,
  FOREIGN KEY (user_id) REFERENCES student_accounts(id)
);

CREATE INDEX IF NOT EXISTS student_mcp_keys_owner
  ON student_mcp_keys (user_id, created_at DESC);
