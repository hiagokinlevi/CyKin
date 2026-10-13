CREATE TABLE IF NOT EXISTS lesson_progress (
  user_id TEXT NOT NULL,
  level TEXT NOT NULL,
  area TEXT NOT NULL,
  language TEXT NOT NULL,
  chapter INTEGER NOT NULL,
  status TEXT NOT NULL CHECK (status IN ('in_progress', 'completed')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now')),
  PRIMARY KEY (user_id, level, area, language, chapter)
);

CREATE TABLE IF NOT EXISTS exercise_attempts (
  user_id TEXT NOT NULL,
  level TEXT NOT NULL,
  area TEXT NOT NULL,
  language TEXT NOT NULL,
  chapter INTEGER NOT NULL,
  exercise_id TEXT NOT NULL,
  answer TEXT NOT NULL DEFAULT '',
  status TEXT NOT NULL CHECK (status IN ('attempted', 'completed')),
  updated_at TEXT NOT NULL DEFAULT (datetime('now')),
  PRIMARY KEY (user_id, level, area, language, chapter, exercise_id)
);
