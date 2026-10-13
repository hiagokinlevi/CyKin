# Daily-study migration status

**Editorial responsibility: hiagokinlevi. Checkpoint: 2026-10-13.** This report concerns the weekday-allocation migration, not a completed rewrite of all books.

[Daily standard](DAILY_STUDY_STANDARD.md) · [Curriculum grid](CURRICULUM_GRID.md) · [Legacy chapter coverage](COURSE_WRITING_PROGRESS.md) · [Book gate](BOOK_STANDARD.md)

## Scope and available work

The policy covers all **23 areas × 9 levels**, and all nine language editions. One manuscript per area/level/language and one skill per course remain mandatory. Subjects stay chapters; each chapter expands into daily lessons with substantive teaching, a worked example and a distinct exercise-answer pair. The English reference allocations are 22/130/390/780/1,040/1,300/520/520/520, depending on level. They are targets, not authored counts or exact civil-calendar counts.

The [rapid English Incident Response daily index](levels/rapid-1-month/incident-response-resilience/en/DAILY_PLAN.md) proposes **22 mapped readings** of its existing manuscript, assigning all **50 existing numbered exercises** once each. Each entry identifies a reading interval and an example, plus its exercise IDs. The mapping binds to source blob `b91edc4bd76d02822e634cbb90e904bc337b6fc2`; a changed source blocks the runtime mapping until reviewed. The underlying instructional manuscript was not rewritten in this migration step. The map does not claim 22 new native daily lessons or a completed 80-hour workload review.

| Dimension | State of this migration |
|---|---|
| Global daily creation/expansion rule | Defined for every course and language |
| Reference durations and weekday counts | Defined for all nine existing level paths |
| First detailed allocation | 22 proposed mapped readings, rapid Incident Response / English only |
| Other course-specific daily maps | Not created in this pass; show planned positions, not invented teaching |
| New native daily lessons | Not claimed by the mapping |
| Reviewed daily workload | Pending; long existing units need prerequisite and effort review |
| Translated daily maps and lessons | Not produced in this pass; existing translations preserved |
| Legacy ≥300-word chapter coverage | Method and historical denominator retained separately; no full-catalog recount |
| Current A4 measurement | Not performed; existing stale renders remain stale |
| Website deployment | Code publication is not deployment; authorized local build and Cloudflare verification still required |

## Code and bounded validation

The new read-only [daily API](web/api/daily_study.py) reads the public Markdown policy and the selected edition's optional daily manifest. It separates reference slots, mapped draft readings, native daily lessons and reviewed daily lessons. It does not write learner progress or reinterpret existing completed chapters. Unsupported languages/courses, stale source fingerprints, ambiguous headings, missing examples or missing/duplicate exercise-answer pairs block the affected result. No English teaching is silently substituted for another edition.

The [daily page](web/src/pages/daily.astro) and [reader](web/src/lib/daily-reader.ts) provide course/language selection, optional start date, week/day navigation, separate teaching/example/task views, answers behind disclosure controls and full-book access. A dated view compares actual calendar weekdays with the fixed reference sequence and exposes alignment differences rather than silently dropping or repeating lessons. Controls support the nine edition codes; broader site interface localization remains a separate task.

**Executed locally:** 171 tests in [the daily contract suite](web/tests/test_daily_study.py), covering nine level profiles, 45 independently enumerated calendar cases, 81 level/language API combinations, negative source/manifest inputs, four-digit exercise IDs, unavailable/stale content and the metadata uniqueness of the 22-unit/50-exercise allocation. The API tests use explicitly synthetic source fixtures. TypeScript transpilation and strict type checking of the new reader were also performed with declared dependency interfaces.

**Not established by those checks:** a full extraction run against the entire live Incident Response manuscript, all existing application tests, an Astro production build, browser rendering, production Cloudflare deployment, complete link validation across the corpus, student workload, specialist review, translated teaching or book completion. The runtime must recheck the actual selected manuscript before displaying a mapped day. Do not convert the synthetic test result into a production acceptance claim.

## Next exact editorial and release work

Review **Incident Response / rapid / English / D0001–D0005**, starting at D0001: confirm case-input prerequisites before each assigned exercise, inspect the complete source mapping, measure realistic reading and practice effort, and revise the one manuscript into native daily units with daily navigation and corresponding final answers. Preserve all original content and exercises; move or split only with a traceable mapping and meaningful learning objectives. Continue sequentially through the remaining daily units and then the professional level. The previously recorded Chapter 2 VQ2 technical review remains open within that volume; a calendar mapping does not resolve it.

Before deploying the new site, run the complete local build and existing tests, inspect mapped and plan-only editions in a browser including right-to-left reading, check links and source-size/performance behavior, verify the current GitHub revision and approved Cloudflare destination, and use [the local deployment procedure](web/README.md). Do not run GitHub Actions or infer successful deployment from a commit. Long future books may require a revision-indexed extraction/cache design beyond the current upstream reader limits; technical limits are not editorial word ceilings.
