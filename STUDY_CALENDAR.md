# Study calendar: instructional weeks and actual dates

**Editorial responsibility: hiagokinlevi. Policy clarification: 2026-10-13.** Applies to all catalog areas, nine levels and nine language editions. Read the [curriculum grid](CURRICULUM_GRID.md), [book standard](BOOK_STANDARD.md) and the selected edition's actual `SUBJECTS.md` and `MANUSCRIPT.md` first.

## Preserve the current book hierarchy

Keep **area → level-specific course → language edition → one principal book → weekly chapters → daily lessons**. Curricular subjects organize modules. A weekly chapter normally contains five daily lessons. Each required study day needs substantive teaching, a worked example and a distinct independently attemptable exercise with a reasoned answer in the same book's final appendix. No book, chapter or lesson-count baseline is a ceiling on depth. There is one course skill, not a skill per day.

The current grid's rapid baseline is **four instructional weeks / 20 lessons**; professional is 26 weeks / 130 lessons; engineering is 260 weeks / 1,300 lessons. Preserve these baselines and the actual native lesson anchors. The current rapid English Incident Response index contains [20 daily lessons in four weekly chapters](levels/rapid-1-month/incident-response-resilience/en/SUBJECTS.md). Its actual source is authoritative, not an older conversation or a proposed 22-reading map. This calendar change does not rewrite that manuscript, replace its exercises, create another book or certify its technical/editorial completion.

## One lesson on every required weekday of the chosen duration

Instructional-week baselines and civil-calendar durations answer different questions. Four instructional weeks contain 20 study days, but a civil month can contain a different number of Monday–Friday dates. A 26-week baseline is not automatically the exact count of weekdays in every six-month period. Before promising full daily coverage of a dated course, record its start convention, nominal end, required dates and lesson allocation.

The website's calendar uses this explicit convention:

1. The learner selects a civil start date. If it is Saturday or Sunday, the first study date is the following Monday; the adjustment is shown.
2. Add the course's stated number of **calendar months** to that first study date. When the anniversary day does not exist, use the last day of the resulting month. This defines an **exclusive** nominal end.
3. Keep every Monday–Friday date from the first study date up to, but not including, that end. Do not silently remove holidays, vacations or recesses. A special calendar requires explicit exceptions and revised coverage, not a hidden reduction.
4. Assign the stable daily lesson number to its ordinal study date. Lesson 3 never moves to day 2 merely because lesson 2 is missing. Keep extra indexed lessons visible after the nominal end instead of truncating the book.
5. Show the instructional baseline, actual required weekday count, fixed/indexed sequence end, missing daily positions and any extension separately. A first partial calendar week does not change the book's five-lesson chapter identity.

For example, this convention applied to **13 October–13 November 2026, end excluded**, produces **23 Monday–Friday dates**. A 20-lesson reference therefore leaves three dated positions that require a reviewed allocation. The calendar must not fill them by repeating one exercise as if it were new teaching or by claiming an empty position is a lesson. A longer sequence may explicitly extend the schedule. A shorter one requires additional substantive authored units, or an openly revised instructional-duration description, before promising that every weekday of the nominal month is covered.

Review, synthesis, engineering-project and research days are real instructional units only when they contain a defined learning question, explained example, independently attemptable task and worked assessment guidance. They are not filler. Keep their teaching, exercise and answer inside the same principal manuscript, preserving stable IDs and existing links. Apply this coverage rule independently to every language: an English lesson or a translated menu does not supply a missing translated lesson.

## Source availability, review and learner work are different

The date view reads the existing course API for the selected edition. It distinguishes **source-indexed daily text**, **planned daily text**, **no daily allocation**, and **unknown availability** when the source request fails. It does not authenticate the source content or independently verify that each indexed lesson satisfies the example, exercise, answer, safety and editorial gates. A date-count match is not course completion. Existing legacy subject-chapters remain readable but are not counted as daily lessons.

A malformed or duplicate daily ID blocks the availability interpretation rather than allowing last-row-wins replacement. A missing intermediate daily ID stays a gap. Source failure must not become a claim that the edition has zero written content. No English fallback, content generation, progress write, automatic completion or interpretation of existing account records is performed by the calendar. The ordinary course reader and its source links remain authoritative for opening a lesson.

## Implementation and bounded verification

The new date view is [calendar.astro](web/src/pages/calendar.astro), using the pure [study-calendar module](web/src/lib/study-calendar.mjs) and the already existing `/api/courses/{level}/{area}/{language}` endpoint. It adds no competing daily API, no second manuscript and no changes to private student progress storage. The baseline comes from the selected catalog course; durations retain the nine current level paths. The header/footer link provides access to the calendar for both subject-first and level-first browsing.

**Actually executed for this addition:** [72 Node.js contract tests](web/tests/study-calendar.test.mjs), repeated under UTC, America/New_York and Asia/Jerusalem. They cover all nine durations across five starting dates, independently enumerated weekday conservation, weekend adjustment, month-end/leap-day clamping, missing and duplicate IDs, planned versus source-indexed entries, legacy chapter exclusion, extra lessons, four-digit lesson IDs and malformed inputs. The calendar client also passed TypeScript syntax transpilation. These are calculations and synthetic metadata tests, not an end-to-end test of the published manuscripts or observed student performance.

**Still required before a website release:** run the complete existing API tests and Astro build; inspect browser behavior, mobile layout, keyboard access, selected-language navigation, source failures and links; confirm the authorized Cloudflare account and current public source revision; deploy and verify through [the local procedure](web/README.md#publish-from-an-authorized-local-computer). A commit does not prove production deployment. No GitHub Actions are authorized.

## Continuing production

Continue improving the **current native daily lessons**, not an obsolete allocation: review the first five rapid Incident Response English lessons for prerequisites, workload, technical depth, worked examples and exercise-answer coherence, then advance in sequence. Resolve any chosen calendar's remaining daily positions with genuine teaching. Continue the other levels and areas in the established production order, with the English collection fully written and reviewed before the ordered translation passes. Report chapter/module coverage, daily curriculum coverage, translation parity and complete-book status separately.
