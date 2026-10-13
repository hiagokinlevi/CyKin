# CyKin daily-study and content-expansion standard

**Editorial responsibility: hiagokinlevi. Effective: 2026-10-13.** This standard applies to every area, all nine levels and all nine language editions. It supersedes the former equation **one subject = one lesson**. It does not rename existing levels, delete chapters, declare translations complete or grant academic accreditation.

[Home](README.md) · [Book standard](BOOK_STANDARD.md) · [Curriculum grid](CURRICULUM_GRID.md) · [Study path](STUDY_PATH.md) · [Daily migration status](DAILY_STUDY_PROGRESS.md)

## One book, chapters containing daily lessons

Retain one principal `book/MANUSCRIPT.md` per area, level and language. A curricular subject remains one chapter; subdivide that chapter into consecutive daily lessons. A student follows **area → level → language → book → chapter → daily lesson**. Cybersecurity therefore has nine distinct level-books per language, not one common book for every level and not a separate book for each day. The same rule applies to every other area. Retain one `skill/SKILL.md` per course; do not create skills per lesson.

Every weekday study session has **one substantive lesson, at least one explained worked example, and at least one distinct substantial exercise with its worked answer in the final appendix of that same book**. Additional practice is welcome. An example is not the student's exercise; assigning the same exercise again does not create another new exercise. A review or research day still needs an explicit learning question, a worked methodological example, an independently attemptable task and an assessment model. A title, an empty day slot or a generic instruction to read is not authored teaching.

## Duration and the five-day week

Study Monday through Friday; Saturday and Sunday are not required study days. These are the maintainer's chosen teaching days, not a jurisdiction's legal holiday calendar. No public holiday, vacation, recess or reading week is silently removed. Any exception requires an explicit, versioned calendar and a revised end date or a separately approved allocation; do not compensate by assigning several daily lessons on one day without the learner's agreement.

The following **reference planning counts** use `ceil(months × 52 × 5 / 12)`. They are not a claim that every civil month has the same number of weekdays. Existing catalog names and paths remain stable: rapid is one month; the six-month track is professional.

| Existing level | Duration | Subject-chapters | Reference daily lessons | Reference minimum distinct exercises |
|---|---:|---:|---:|---:|
| Rapid | 1 month | 4 | 22 | 50 |
| Professional | 6 months | 12 | 130 | 130 |
| Technical | 18 months | 18 | 390 | 390 |
| Technologist | 3 years | 30 | 780 | 780 |
| Bachelor's | 4 years | 40 | 1,040 | 1,040 |
| Engineering | 5 years | 50 | 1,300 | 1,300 |
| Postgraduate | 2 years | 12 | 520 | 520 |
| Master's | 2 years | 8 | 520 | 520 |
| Doctoral | 2 years | 8 | 520 | 520 |

For a dated cohort, record the chosen start, first study weekday, exclusive end, timezone/date convention and all exceptions. Add the stated number of **calendar months** to the first study date, clamping an unavailable anniversary day to the last day of its month. Count Monday–Friday dates in `[first study date, end)`. This exact count can differ from the reference. Before claiming the complete duration is covered, allocate one fully supported lesson to every required date. Where a fixed lesson sequence and the calendar differ, expose the difference: add genuinely authored alignment lessons, revise the calendar explicitly, or leave alignment pending. Never silently truncate the book, repeat one task as new teaching, or advertise an exact six-month completion using an approximate 130-day count.

An undated book uses stable lesson IDs, not calendar dates. A student's schedule maps those IDs to dates. Changing a start date must not change an exercise's identity or rewrite completed work. The website may show a projected end for the full fixed sequence and a separate calendar-month boundary; a difference is a pending alignment decision, not a completed curriculum.

## Allocate depth, not just slots

First read the existing chapter, its prerequisites, examples and answer appendix. Define which new capability each day develops; allocate more days to demanding mechanisms, design comparisons, laboratories and research tasks. A balanced arithmetic allocation is a **planning fallback only**, never evidence of a reviewed instructional sequence. Preserve chapter order and existing anchors. Break a long laboratory into meaningful milestones with separate questions and evaluation, not arbitrary equal-length fragments.

Longer programs require materially larger and deeper books because they contain more distinct learning units, examples and practice. Engineering should develop requirements, models, design alternatives, implementation constraints, failure analysis, validation and integrated projects over its five-year plan. Postgraduate work specializes; master's work develops and evaluates research questions; doctoral work examines a defensible contribution and its limitations. Equal duration does not imply equal technical depth or interchangeable prose. Do not reuse a lower-level book with superficial changes.

The prior page budgets are historical planning estimates, not ceilings. The **300 verified A4 pages remain a floor**, never a reason to compress hundreds of lessons or pad a short book. Estimate new length from the actual daily learning design, then verify the final rendering. Existing hour budgets also require workload calibration against reading, example analysis, practical work, exercise attempts and feedback; the website must not present a division of planned hours as a measured lesson duration.

## Required daily unit and identifiers

A native daily unit inside the manuscript has a stable `day-0001` anchor, title, chapter membership, prerequisites, objectives, definitions, progressive mechanism explanation, assumptions, comparison or boundary case, an explained example, safe practice, an independently attemptable exercise, expected evidence and assessment, common errors, synthesis and **Continue studying** links to previous day, daily index and next day. The final day also points to the course review and next course without asserting completion.

Keep existing `EX001`–style IDs. IDs may expand to `EX1000` and beyond; parsers must not truncate them to three digits. Numbered exercises are unique within an edition, remain aligned across translations, and have exactly one corresponding final worked-answer heading. A day may reference additional exercises, but each day's primary exercise must be distinct. A complete edition needs at least `max(50, required daily lessons)` substantive exercises, and every required daily lesson must have its own example and exercise-answer relationship. Counting tokens or headings is not a technical or linguistic review.

Use `<language>/DAILY_PLAN.md` as a navigation and allocation manifest, **not another textbook**. All teaching, examples, exercises and worked answers stay in the one manuscript. A migration manifest may select exact existing heading ranges and paired exercises in that book. Label these units **mapped draft readings** until their daily workload and teaching coherence have been reviewed; they are not newly written native lessons. A changed source invalidates a revision-bound mapping until checked. Missing, ambiguous or out-of-chapter selectors must fail closed.

## Languages, progress and tutoring

The same durations, chapter identities, daily IDs, primary exercise identities and safety requirements apply to `en`, `pt`, `es`, `he`, `fr`, `ru`, `de`, `zh` and `ja`. Author and review the English collection first, then Portuguese, Spanish, Hebrew, French, Russian, German, Chinese and Japanese, one language pass at a time. Preserve valid existing translations. An English daily plan is not evidence of a translated lesson, and a translated menu is not a translated book. Never substitute English teaching silently when the selected edition lacks a unit.

Keep separate counters for **planned daily positions**, **mapped draft readings**, **native authored daily lessons**, **reviewed daily lessons**, **learner exercise attempts**, **legacy chapter-draft coverage** and **complete verified books**. The published ≥300-word-per-chapter method remains the historical chapter metric; do not replace its denominator with days or infer daily completion from it. An available lesson is not a completed learner task. Calendar passage is not learning progress. A source or server error means availability is unknown, not zero published content.

Tutors retain `{language, course, chapter, daily_id, source_revision, source_state, attempted_exercises, feedback, next_required_unit}`. Teach only available source text, reveal worked answers after an attempt, preserve synthetic-case release boundaries and stop completion at the first missing required unit. Consult this standard in addition to the course's single skill. Write or substantially review sequential batches of five to ten daily units, preserving the chapter-level curriculum and the English-first production order beginning with Incident Response. After each batch, check every example/prompt/answer pairing, links, safety, workload and source revision; update the course manifest and public progress honestly.

## Website and publication requirements

Every course page must separate the **daily study plan** from the **whole-chapter reader**. Show level, duration, five-day rhythm, reference target, edition, actual availability and a day/week navigator. Each available daily view needs teaching, example, exercise and a separately revealed answer, plus previous/index/next navigation. Planned or stale units have no completion action. Preserve existing chapter URLs and chapter-based saved progress; never reinterpret an old completed chapter as dozens of completed days.

A calendar is a view over a course, not a second source of teaching. Read Markdown from this public repository and identify its revision. Validate the selected language and course; do not invent lesson contents for empty slots. A changed frontend/API requires the authorized local build, tests and Cloudflare deployment described in [web/README.md](web/README.md). Committing code does not demonstrate production deployment. Do not use GitHub Actions.

## Machine-readable reference policy

This block is the shared planning policy for the website. Its values are **targets and catalog metadata**, not counts of written lessons. Python weekday numbers use Monday=0 through Friday=4. Unknown levels or malformed policy data must not be assigned guessed durations.

<!-- cykin:daily-policy:start -->
```json
{
  "schema": 1,
  "version": "2026-10-13",
  "weekdays": [0, 1, 2, 3, 4],
  "languages": ["en", "pt", "es", "he", "fr", "ru", "de", "zh", "ja"],
  "levels": {
    "rapid-1-month": {"months": 1, "reference_lessons": 22, "chapters": 4, "planned_hours": 80},
    "professional-6-months": {"months": 6, "reference_lessons": 130, "chapters": 12, "planned_hours": 360},
    "technical-18-months": {"months": 18, "reference_lessons": 390, "chapters": 18, "planned_hours": 1200},
    "technologist-3-years": {"months": 36, "reference_lessons": 780, "chapters": 30, "planned_hours": 2400},
    "bachelors-4-years": {"months": 48, "reference_lessons": 1040, "chapters": 40, "planned_hours": 3200},
    "engineering-5-years": {"months": 60, "reference_lessons": 1300, "chapters": 50, "planned_hours": 4000},
    "postgraduate-2-years": {"months": 24, "reference_lessons": 520, "chapters": 12, "planned_hours": 600},
    "masters-2-years": {"months": 24, "reference_lessons": 520, "chapters": 8, "planned_hours": 1200},
    "doctorate-2-years": {"months": 24, "reference_lessons": 520, "chapters": 8, "planned_hours": 1600}
  }
}
```
<!-- cykin:daily-policy:end -->

[Continue to the daily migration status](DAILY_STUDY_PROGRESS.md). Original maintainer-owned material follows [RIGHTS.md](RIGHTS.md); third-party sources retain their rights.
