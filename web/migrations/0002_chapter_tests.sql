CREATE TABLE IF NOT EXISTS chapter_test_attempts (
  id TEXT PRIMARY KEY,
  user_id TEXT NOT NULL,
  level TEXT NOT NULL,
  area TEXT NOT NULL,
  language TEXT NOT NULL,
  chapter INTEGER NOT NULL,
  bank_sha256 TEXT NOT NULL,
  next_index INTEGER NOT NULL DEFAULT 0,
  score INTEGER NOT NULL DEFAULT 0,
  deadline_ms INTEGER NOT NULL,
  answers_json TEXT NOT NULL DEFAULT '[]',
  status TEXT NOT NULL CHECK (status IN ('active', 'complete')),
  created_at TEXT NOT NULL DEFAULT (datetime('now')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS chapter_test_attempts_student_course
  ON chapter_test_attempts (user_id, level, area, language, chapter, score);

CREATE TABLE IF NOT EXISTS course_certificates (
  id TEXT PRIMARY KEY,
  user_id TEXT NOT NULL,
  level TEXT NOT NULL,
  area TEXT NOT NULL,
  language TEXT NOT NULL,
  book_sha256 TEXT NOT NULL,
  issued_at TEXT NOT NULL DEFAULT (datetime('now')),
  UNIQUE (user_id, level, area, language, book_sha256)
);
