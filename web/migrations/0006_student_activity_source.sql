ALTER TABLE student_activity
  ADD COLUMN source TEXT NOT NULL DEFAULT 'site' CHECK (source IN ('site', 'mcp'));
