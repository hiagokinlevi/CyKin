-- Optional, first-party aggregate measurement. No IP, email, or user account is stored.
CREATE TABLE IF NOT EXISTS public_usage_events (
  visitor_hash TEXT NOT NULL,
  event TEXT NOT NULL CHECK (event IN ('view', 'read', 'exercise')),
  path TEXT NOT NULL,
  course_key TEXT NOT NULL DEFAULT '',
  exercise_id TEXT NOT NULL DEFAULT '',
  window_start INTEGER NOT NULL,
  occurred_at INTEGER NOT NULL,
  PRIMARY KEY (visitor_hash, event, path, exercise_id, window_start)
);

CREATE INDEX IF NOT EXISTS public_usage_time ON public_usage_events (occurred_at);
CREATE INDEX IF NOT EXISTS public_usage_course_time ON public_usage_events (course_key, occurred_at);
CREATE INDEX IF NOT EXISTS public_usage_path_time ON public_usage_events (path, occurred_at);
