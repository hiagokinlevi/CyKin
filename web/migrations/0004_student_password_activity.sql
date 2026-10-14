CREATE TABLE IF NOT EXISTS student_password_credentials (
  user_id TEXT PRIMARY KEY,
  username TEXT NOT NULL UNIQUE,
  password_salt TEXT NOT NULL,
  password_digest TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS student_activity (
  id TEXT PRIMARY KEY,
  user_id TEXT NOT NULL,
  kind TEXT NOT NULL CHECK (kind IN ('lesson_opened', 'lesson_read', 'lesson_completed', 'exercise_answered', 'test_started', 'test_answered', 'analysis_saved')),
  level TEXT NOT NULL,
  area TEXT NOT NULL,
  language TEXT NOT NULL,
  chapter INTEGER NOT NULL,
  exercise_id TEXT,
  seconds INTEGER NOT NULL DEFAULT 0 CHECK (seconds BETWEEN 0 AND 3600),
  score INTEGER,
  occurred_at TEXT NOT NULL DEFAULT (datetime('now'))
);

CREATE INDEX IF NOT EXISTS student_activity_user_time
  ON student_activity (user_id, occurred_at DESC);
CREATE INDEX IF NOT EXISTS student_activity_course
  ON student_activity (user_id, level, area, language, chapter);

CREATE TABLE IF NOT EXISTS student_analysis (
  user_id TEXT NOT NULL,
  level TEXT NOT NULL,
  area TEXT NOT NULL,
  language TEXT NOT NULL,
  chapter INTEGER NOT NULL,
  note TEXT NOT NULL CHECK (length(note) <= 10000),
  updated_at TEXT NOT NULL DEFAULT (datetime('now')),
  PRIMARY KEY (user_id, level, area, language, chapter)
);
