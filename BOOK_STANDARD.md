# CyKin study-book standard

Each of the 23 current academic areas has nine course tracks. Each track has one principal book location in each planned language: `en`, `pt`, `es`, `he`, `fr`, `ru`, `de`, `zh`, `ja`. This yields 207 distinct English books and 1,863 planned language editions. A plan is not a finished book. Markdown is canonical; an A4 PDF is a derived verification format.

## Chapters and daily lessons

The [daily-study standard](DAILY_STUDY_STANDARD.md), effective 2026-10-13, governs creation and expansion across **every course and language**. It replaces the former one-subject/one-lesson equivalence: **one subject remains one chapter, and that chapter contains multiple daily lessons**. The [curriculum grid](CURRICULUM_GRID.md) retains 4, 12, 18, 30, 40, 50, 12, 8 or 8 subject-chapters by level. It now plans 22, 130, 390, 780, 1,040, 1,300, 520, 520 or 520 daily positions respectively. These are reference allocations; dated courses must also resolve their actual Monday–Friday calendar.

Every required study day has substantive instruction, defined objectives and prerequisites, progressive technical explanation, at least one worked example and a distinct independently attemptable exercise. Explain assumptions, mechanisms, alternatives, evidence, failure modes and limits. Provide safe reproducible practice and a meaningful assessment. The final appendix in the **same manuscript** contains every worked answer with its reasoning. A reading title, repeated task or generated slot does not satisfy the requirement.

Keep `SUBJECTS.md` for chapter order and `<language>/DAILY_PLAN.md` for daily allocation and navigation. The latter is not a second textbook: student-facing instruction remains in `book/MANUSCRIPT.md`. A mapped reading of existing text must be labeled as such until its daily prerequisites, workload and learning progression are reviewed. Source changes require revalidation; a manifest cannot authenticate or complete a lesson merely by naming it.

Every native daily lesson and every authored subject-chapter ends with **Continue studying** links to previous position, appropriate index and next position. Preserve legacy `ch-01` links and exercise identities during migration; use stable `day-0001` anchors for native daily units. A plan labels its destinations as planned or authored. After the final day, return to the course review and the next course in the same language without implying the learner completed anything automatically.

Use purposeful visual explanations for processes, structures, decisions or comparisons: accessible figures, labeled logical drawings or GitHub-renderable Mermaid with explanatory prose and text alternatives. Inspect rendering. Do not add decorative repeated diagrams to inflate counts. Each course still has **one skill**, not separate chapter or day skills. Preserve authored manuscripts, sources, exercises, translations and history when the curriculum changes.

Original maintainer-owned material is dedicated under [CC0 1.0](LICENSE), within [RIGHTS.md](RIGHTS.md). Third-party works retain their rights. Citation accuracy remains an editorial requirement.

## Publication gate for each volume

1. Complete original instructional prose, useful diagrams, references, explained examples and safe practical work appropriate to the level. Cover every required daily position and every curricular subject with distinct learning; verify prerequisite and workload coherence. Cite primary sources beside factual claims and distinguish documented facts, inferences and synthetic cases.
2. At least **`max(50, required daily lessons)` distinct numbered substantial exercises**, including a separate primary exercise for each required day. Every task needs objective, inputs, constraints, reproducible steps, expected evidence and assessment. Preserve existing IDs; allow `EX1000` and beyond rather than truncating long-course IDs to three digits. Do not count repeated assignments as new exercises.
3. A final worked-answer appendix in the same book, matching every exercise ID, with method, intermediate reasoning, conclusion, limitations and acceptable alternatives. Missing, duplicate or mismatched answers fail the gate.
4. Render the actual manuscript as **A4 PDF** and verify at least **300 qualifying pages**. Longer courses require materially greater learning depth and volume; old page budgets are not ceilings. Do not pad a short text or compress a long daily curriculum merely to hit a number. A page estimate is not a measured rendering.
5. Review technical accuracy, sources, rights, privacy, ethics, accessibility, language, reproducibility and the daily example/exercise/answer relationships. Record reviewer, date, source revision and actual scope. No template or passing code test substitutes for this review.
6. Show actual source state: planned allocation, mapped draft reading, native daily draft, reviewed daily lesson and complete volume are distinct. Public drafts can be read as drafts. Release a complete edition only after all gates pass; calendar passage and chapter coverage do not certify completion.

The reference exercise minima by level are now **50, 130, 390, 780, 1,040, 1,300, 520, 520 and 520**. A dated allocation or additional substantial practice may raise them. Earlier smaller targets remain historical planning records only and do not override this gate. Progress uses separate chapter and daily denominators; see [migration status](DAILY_STUDY_PROGRESS.md).

## A4 verification edition

Render from the same public Markdown used for reading: A4 portrait (210 × 297 mm), 25 mm margins, readable 11 pt body text, 1.3 line spacing and monospaced code of at least 9 pt. Keep ordered headings, running page numbers, figure alternatives/captions and bibliography. Wrap or split tables rather than shrinking them. Split code only with enough labeling and context to remain usable. Record build tool, version, command, font, source hash, edition date and measured page count; inspect the actual PDF. Exclude blank-page padding and layout tricks. Old renders apply only to their exact source hashes and must be marked stale after source changes.

## Sequential production and languages

Begin with [Incident Response](levels/rapid-1-month/incident-response-resilience/README.md), progressing through its levels, then the remaining [areas](AREA_MAP.md). **Write and review the English collection first**, then Portuguese, Spanish, Hebrew, French, Russian, German, Chinese and Japanese, one language pass at a time. Preserve and accurately label existing translations while improving the reference. Every edition inherits the same daily identities, durations and learning/assessment burden; no folder, translated menu or English outline proves translated teaching exists.

Work in sequential batches of five to ten native daily lessons or equivalent substantive daily revisions within the chapter curriculum. Reconcile the chapter, examples, tasks and final answers after every batch. Update the daily manifest, one course skill, indexes and progress only for what was actually authored, revised and checked. Keep the [complete course guide](COURSE_GUIDE.md) and [study path](STUDY_PATH.md) as navigation, not evidence of completed books.

## Book directory and honest publication

`book/PLAN.md` describes scope; `book/MANUSCRIPT.md` holds the sole instructional text. Supporting figures and authorized synthetic assets may accompany it. All student-facing drafts, examples, labs, tasks, answers and course skills belong in this public repository. The private Engine is only for construction tools, tests, measurements and operational records. Do not publish private data, secrets or unsafe instructions.

Course names such as bachelor's, engineering, master's and doctoral describe educational depth and duration, not accreditation, enrollment in an institution or a promised degree. The two-year doctoral track is the maintainer's educational plan, not a universal institutional rule. The [website](web/README.md) must distinguish reference daily slots, actual edition availability and separately recorded learner work. Source publication does not prove a frontend/API deployment; use only the approved local deployment procedure, never GitHub Actions.
