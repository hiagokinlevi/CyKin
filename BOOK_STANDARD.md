# CyKin study-book standard

Each of the 23 current academic areas has nine course tracks. Each track has a book location in each planned language: `en`, `pt`, `es`, `he`, `fr`, `ru`, `de`, `zh`, `ja`. This yields 207 distinct books in English and 1,863 planned language editions. A plan file is not a finished book. Markdown is the canonical authoring and public reading format; an A4 PDF is a derived format for page verification.

Every authored chapter and every `PLAN.md` chapter summary ends with a visible **Continue studying** block showing its position in the book and links to the previous chapter, course chapter index and next chapter. If a destination is only an outline, label it as a plan; after the last chapter, the course index supplies the next course in the full study path. This navigation is required in future manuscript editions as well as existing drafts.

## One weekday, one book chapter

For **every area and every language edition**, one course has one principal `book/MANUSCRIPT.md`. Its curricular subjects are **modules**; each instructional weekday within a module is **one distinct numbered chapter/lesson** of that book. Study runs Monday through Friday, five lessons per instructional week. A year means 52 instructional weeks. The short one-month course uses four instructional weeks. These are curriculum targets, not a promise about an individual's calendar, public holidays, vacations, or academic accreditation. A learner may move at another pace.

The [curriculum grid](CURRICULUM_GRID.md) gives the targets: 20, 130, 390, 780, 1,040, 1,300, 520, 520 and 520 daily chapters from rapid through doctorate. Longer programs require correspondingly larger books and at least one substantive exercise **per daily chapter**; the rapid course still needs at least 50 in total. Each daily lesson teaches a specific technical concept at its level, includes **at least one fully worked example** and **at least one independently solvable exercise**, points to its worked answer in the final appendix, and has previous/index/next navigation. Include a safe reproducible lab when useful. Add a purposeful visual explanation when it clarifies a process, structure, decision or comparison: a GitHub-renderable Mermaid flowchart or diagram, an accessible figure, or a labeled logical drawing. Supply text alternatives and explain the visual in prose; do not add decorative or repeated diagrams merely to satisfy a count. Keep subjects as module headings in `SUBJECTS.md` and distribute daily chapters across them in curricular order. The nine editions follow the same schedule but must each contain actual teaching in their stated language.

**Migration rule:** Existing `SUBJECTS.md` rows and `book/PLAN.md` anchors describe the older one-subject-one-chapter structure. They remain public as current content and source material. They are **not** automatically 20–1,300 daily lessons, and their old percentages are not daily-lesson completion. Expand each edition deliberately, retaining accurate sources, exercises, links, history and authored text; update its subject index, plan, manuscript, skill and navigation together. Do not create empty lesson files, copy one chapter into multiple weekdays, or mark a target as published before its teaching, example and exercise exist. The site shows the daily target separately from current authored chapters until an edition is migrated.

This hierarchy is required for **every** cataloged area, including Web3, AI and LLM security, cryptography, post-quantum security and incident response. Each course has one skill linking its chapter index and book; subjects do not have separate skills. Preserve authored manuscripts, exercises, sources and history when a curriculum changes. The catalog is extensible, and the current count is a snapshot rather than a limit.

Original educational material owned by the maintainer is dedicated under [CC0 1.0](LICENSE), with the scope and exceptions described in [RIGHTS.md](RIGHTS.md). Sources cited inside a book retain their own rights and are not relicensed by this repository. Accurate source citation remains an editorial requirement, not a CC0 condition.

## Publication gate for each volume

1. Complete original instructional prose, diagrams, references, realistic sourced examples, and safe practical labs for the course level. Use direct links to primary sources for factual examples and distinguish documented facts from teaching inferences.
2. At least **one** numbered, substantial exercise for **every daily chapter**, and at least **50** per book. Every exercise needs a learning objective, inputs, constraints, reproducible steps, expected evidence, and an assessment rubric.
3. A final worked-results appendix in the same book, with a matching answer and explanation for every exercise ID. Exercises with no answer fail the gate.
4. Render the manuscript to **A4 PDF** and verify at least the level-specific floor in the [curriculum grid](CURRICULUM_GRID.md), never less than **300 actual pages**. Historical page budgets in `book/PLAN.md` are superseded by this schedule and are not evidence of a rendered book.
5. Review citations, rights, accuracy, privacy, ethics, accessibility, language quality, and technical reproducibility. Use descriptive link text, ordered headings, text alternatives for figures, labeled code blocks, and plain-language summaries for complex tables. Record reviewer, date, and edition in the book metadata.
6. Public works in progress may be read and studied with their real availability shown. Mark a volume **complete** only after all daily chapters, examples, exercises and answers exist and this gate passes.

## A4 verification edition

Render from the same public Markdown source used for reading. Fix the verification layout to A4 portrait (210 × 297 mm), 25 mm margins on all sides, a readable 11 pt body font, 1.3 line spacing, and 9 pt or larger monospaced code. Keep heading levels, running page numbers, figure alternatives/captions, and a bibliography. Tables must remain legible: wrap or split them rather than shrinking type to inflate or force page counts. Code blocks may break across pages only when line labels and context remain clear. Record the build tool, version, command, font, edition date and page count in a book release note; inspect the rendered PDF, not a planned word or page budget. Exclude blank pages, front-matter padding and layout tricks from the 300-page minimum. This specification is the validation target; no existing plan has yet been rendered and approved against it.

The course tracks are independent educational blueprints. Names such as bachelor's, engineering, master's, and doctorate describe intended depth and duration. They are not accredited programs or promises of a formal degree. The requested two-year doctoral research timeline is particularly dependent on institutional and jurisdictional rules.

## Sequential production order

Begin with [Incident Response](levels/rapid-1-month/incident-response-resilience/README.md), then work through the remaining [academic areas](AREA_MAP.md) and nine levels per area. Author one distinct public book per course and language, prioritizing English, Portuguese and Spanish editions with independent technical and language review. Translate and review the remaining languages in sequence. A language folder or plan is a production location, not evidence that the lessons have been written or that a volume is complete.

The first authored priority is the [Incident Response / Rapid / English draft](levels/rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md). Earlier [Cybersecurity](levels/rapid-1-month/cybersecurity/en/book/MANUSCRIPT.md) and [Security Governance](levels/rapid-1-month/security-governance-risk-compliance/en/book/MANUSCRIPT.md) drafts remain available for their later editorial turns.

The [complete course guide](COURSE_GUIDE.md) links every planned book and course level. Existing `book/PLAN.md` files record the previous one-chapter-per-subject structure; expand them into the daily sequence as each edition is authored. Their summaries are not abstracts of finished manuscripts.

## Complete translations and cross-language parity

**Required destination:** every course at every level must have its complete instructional content available in all nine editions: English (`en`), Portuguese (`pt`), Spanish (`es`), Hebrew (`he`), French (`fr`), Russian (`ru`), German (`de`), Chinese (`zh`) and Japanese (`ja`). This is a production obligation, not a declaration of current availability. For one area, there are nine level-specific books in each language, not one book combining all levels. Keep one principal `MANUSCRIPT.md` per course and language and one shared course skill.

The daily targets in the [curriculum grid](CURRICULUM_GRID.md) apply independently to each edition. Their sum is 5,220 lessons per area and language; with the current 23 areas, the target is 120,060 lessons per language and 1,080,540 lesson-editions across nine languages. Of those lesson-editions, 960,480 are the eight non-English counterparts. These are arithmetic planning totals, not existing lessons, new books, translated pages or verified completion. There is no maximum lesson count. Existing English teaching, including legacy subject-chapters and their supplements, must not be dropped when mapping to the daily curriculum or translating it.

Follow the [AI guide's language order](AI_GUIDE.md#language-and-citation-rules): complete the English writing and review pass, then Portuguese, Spanish, Hebrew, French, Russian, German, Chinese and Japanese, one language pass at a time. Inventory and preserve existing translations while the reference is reviewed. Do not restart a valid manual translation merely because the English source has changed; compare the actual changes and reconcile them. Public, accurate existing translations remain readable. Reference defects discovered during translation require an explicit correction and renewed comparison, not a silent change to the learner's task.

### What must be translated

Translate the complete instructional package, not an abridgment. Equivalent technical depth means the same concepts, mechanisms, assumptions, reasoning steps, evidence limits and assessment demands at the specified level. Natural language may differ; the learning burden must not be reduced.

| Component | Required language-edition coverage |
|---|---|
| Course and lesson guides | Course overview, audience, prerequisites, subject/module names, daily sequence, objectives, materials and previous/index/next navigation |
| Teaching and examples | All substantive prose, definitions, comparisons, intermediate reasoning, worked examples, case descriptions, counterexamples, common errors, limitations, summaries and glossary entries |
| Tables and visuals | Table headings and explanatory cells, diagram and flowchart labels, legends, captions, text alternatives and the prose explaining what each relationship means |
| Laboratories | Prerequisites, authorized or isolated scope, setup and execution instructions, input explanations, expected observations, failure checks, interpretation and safe cleanup |
| Assessment | Every exercise prompt, learning objective, input, constraint, required artifact, rubric and full worked answer, with accepted alternatives and reasoning, in the same principal book |
| Sources and rights | Citation explanations, source links, provenance, permissions and third-party notices; referenced external works remain external unless reuse and translation rights have actually been checked |
| Tutoring and discovery | Edition-aware links and terminology in the single course skill, onboarding and course catalog, without creating a skill per lesson or counting a translated interface as a translated book |

Preserve stable exercise IDs, source record IDs, explicit anchors, formulas, units, chronology, scope, uncertainty and safety conditions. Keep protocol names, API identifiers, commands and machine-readable fields unchanged where translation would alter behavior. Exact lab fixtures, bytes, hashes and literal program output remain exact; translate their explanations rather than silently changing the test. A necessary localized executable variant must be labeled separately and have its own reproduced output. Retaining these technical literals, proper source titles or permitted original quotations is not an untranslated teaching gap; retaining English instructional paragraphs without a translation is.

Check language-specific typography and reading order as well as vocabulary. For Hebrew, verify right-to-left prose alongside left-to-right code, numbers and identifiers. For every language, inspect readable tables, figures, code and exercise/answer navigation in the actual rendered edition. A language detector, matching heading count or same number of words cannot establish fidelity. Do not transplant a different jurisdiction's rules into a case as an unmarked translation.

### Pin the reference and prove completeness

For each translated book, record its source manuscript path and revision, target revision, review scope and date, and the reviewer actually responsible. For each lesson or legacy source unit, map the source anchor to the target anchor and its exercise/answer IDs. Record the source revision last compared. An explicit one-to-many mapping is needed when a legacy chapter becomes several daily lessons; merely splitting headings must not count as new teaching.

Track three distinct quantities rather than one misleading percentage:

| Measure | Denominator and evidence |
|---|---|
| Daily curriculum coverage | Required daily lessons for this course; count only actual lessons containing teaching, a worked example, an independently solvable exercise and its worked answer |
| Translation coverage of available English content | All instructional units in the declared, pinned English book scope, including supplementary teaching and final answers; count a unit only when all required components above have a target counterpart |
| Reviewed translation parity | The same declared source scope; count only units checked for technical and linguistic equivalence, source/target freshness and the relevant executable and rendering checks |

Report the scope with every percentage: a lesson, a batch, a book or the catalog. A fully translated batch is not a fully translated book. A complete translation of a partial English book is not a complete daily curriculum. Missing sources, inaccessible files, unexamined translations and absent review evidence are **unknown or pending**, never automatically passed. The legacy structural counters in [language coverage](LANGUAGE_LESSON_PROGRESS.md) remain discovery aids until a source-to-target audit is recorded; do not relabel them as translation fidelity or daily-lesson completion.

Before claiming 100% reviewed parity for a book, check every mapped unit and exercise/answer pair, terminology and negation, all required non-prose components, anchors and edition-specific navigation. Run complete executable examples and relevant negative controls where applicable; preserve reported output only when reproduced under the stated environment, or label the run unperformed. A different implementation may corroborate a result but does not establish that the published program executed. Recheck source citations and rights without copying entire third-party works. Record technical, linguistic and rendering limitations rather than inferring approval from a translation tool.

An English revision makes affected target units pending reconciliation until the changed passages and their dependent examples, figures, exercises and answers have been compared again. Keep unaffected translations and their evidence; do not erase the whole edition or pretend it updated automatically. The current book's 100% claim cannot remain valid merely because an earlier snapshot passed. A4 verification is specific to the translated source and layout; an English page count does not verify another edition.

### Public reading and site availability

Publish translated teaching directly in the public edition's principal manuscript, including its worked-answer appendix; do not keep student-facing translation drafts in the private Engine or create duplicate instructional books. Preserve manual changes using the current file SHA and read back the actual published revision. A branch, proposed merge, index entry or language selector alone is not evidence that students can read the translation from `main` or the site.

For both onboarding routes, the selected content language must lead to that language's real course guide, lessons, examples, exercises and worked answers. An English fallback must be explicitly labeled, never counted as translated content. Report interface language, manuscript language, source revision, translation coverage and review state separately. All nine languages are in scope even when the current interface exposes fewer languages. Catalog generation, frontend changes, deployment and live-route verification are separate deliverables; do not report a documentation change or a repository commit as a tested website release. Complete-book approval still requires the full publication gate above.

## Book directory

Each `book/` starts with `PLAN.md`. Later authored content belongs beside it: manuscript sources, figure sources, safe lab data, exercise assets, worked solutions, references, and release evidence. Avoid publishing private data, access credentials, or unsafe offensive instructions.

## Editorial status

The generated files are **outlines and production plans**. No generated file should be counted as a completed 300-page book, a completed set of 50 exercises, or a verified translation. Progress is measured per volume against the publication gate above.
