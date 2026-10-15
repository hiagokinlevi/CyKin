# OpenCyber Academy study-book standard

Each of the 23 current academic areas has nine course tracks. Each track has a book location in each planned language: `en`, `pt`, `es`, `he`, `fr`, `ru`, `de`, `zh`, `ja`. This yields 207 distinct books in English and 1,863 planned language editions. A plan file is not a finished book. Markdown is the canonical authoring and public reading format; an A4 PDF is a derived format for page verification.

Every authored chapter and every `PLAN.md` chapter summary ends with a visible **Continue studying** block showing its position in the book and links to the previous chapter, course chapter index and next chapter. If a destination is only an outline, label it as a plan; after the last chapter, the course index supplies the next course in the full study path. This navigation is required in future manuscript editions as well as existing drafts.

## Lesson quality, not a fixed size

For **every area and every language edition**, one course has one principal `book/MANUSCRIPT.md`. Curricular subjects are **modules**. The default book structure is one substantial **weekly chapter** with five numbered weekday lessons. Study one lesson per weekday. The [curriculum grid](CURRICULUM_GRID.md) sets baseline weekly chapter counts of 4, 26, 78, 156, 208, 260, 104, 104 and 104, and daily lesson counts of 20, 130, 390, 780, 1,040, 1,300, 520, 520 and 520. These are planning baselines, not claims of authored content or page quotas. There is no maximum lesson, chapter, word or page count. Group a different number of lessons when the subject requires it; give longer courses more and deeper chapters. A learner may study at another pace.

A lesson is ready when the learner can explain the idea, tell it apart from a nearby idea, test it, and justify a decision. Follow **definition → mechanism → assumptions → evidence → decision → limitation → practice → explanation of the result**. Each daily lesson needs at least one worked example and one independently solvable exercise whose worked answer is in the final appendix. Add a safe reproducible lab when it teaches the mechanism. Add a Mermaid flowchart, diagram or labeled logical drawing only when the specific content needs a visual explanation of a process, structure, decision or comparison, and explain it in prose. Do not generate a lesson map that merely chains section headings, a worked example and an exercise, or a second diagram that repeats the same chain in another orientation. The chapter index and previous/next links already provide navigation. Do not add length, exercises or pictures to approach a word count, a page count, or a lesson count. A short precise lesson is acceptable; a chapter grows when its set of ideas requires more room. There is no word ceiling or floor.

An edition may use one numbered chapter as one weekday lesson when each chapter itself contains the required teaching, example, exercise and answer. Identify that structure in the manuscript with `<!-- open-cyber-academy:chapter-lessons -->` only after verifying the authored chapters. The study guide then groups consecutive sets of five for pacing. The chapter page remains the single canonical reading URL; this marker does not create duplicate lessons or convert an outline into teaching.

The English reference must meet a demanding university-level standard of explanation and evidence at each course's stated level: precise terminology, justified methods, counterexamples and limitations, reproducible results, original worked reasoning, substantial independent practice and checked primary sources. Higher-level courses must deepen the analysis and critique rather than reuse beginner text with a new title. This is an editorial quality target, not a claim of affiliation or accreditation by any university.

**Expansion rule:** Keep every authored chapter, example, exercise, answer, source and link. Deepen the English teaching until each mechanism is precise, then add the next lesson and weekly chapter when needed. Update the subject index, plan, manuscript, skill and navigation together. Do not stop at the old subject-module count or at the baseline when another lesson is required. Do not insert empty lessons or mechanically split a chapter to reach a number. Do not mark an outline as published teaching. English is the current authoring reference; translation follows from reviewed teaching, one language at a time, never from a plan alone.

This hierarchy is required for **every** cataloged area, including Web3, AI and LLM security, cryptography, post-quantum security and incident response. Each course has one skill linking its chapter index and book; subjects do not have separate skills. Preserve authored manuscripts, exercises, sources and history when a curriculum changes. The catalog is extensible, and the current count is a snapshot rather than a limit.

Original educational material owned by the maintainer is dedicated under [CC0 1.0](LICENSE), with the scope and exceptions described in [RIGHTS.md](RIGHTS.md). Sources cited inside a book retain their own rights and are not relicensed by this repository. Accurate source citation remains an editorial requirement, not a CC0 condition.

## Publication gate for each volume

1. Original teaching that completes the learning chain for each idea the lesson claims. Use direct links to primary sources for factual claims and separate those claims from teaching inferences.
2. A worked example and a numbered exercise for each authored daily lesson. Every exercise needs a learning objective, inputs, constraints, expected evidence and an assessment rubric. Match each exercise to a worked answer; a global exercise total by itself is not a quality measure.
3. A final worked-results appendix in the same book, with a matching answer and explanation for every exercise ID. An exercise with no answer is unfinished.
4. Review citations, rights, accuracy, privacy, ethics, accessibility, language quality and technical reproducibility. Use descriptive link text, ordered headings, text alternatives for figures, labeled code blocks and plain-language summaries for complex tables. Record reviewer, date and edition in the book metadata.
5. Public works in progress may be read with their real availability shown. Mark a volume **complete** only after its intended course scope is taught across the weekly sequence and each authored lesson meets this gate. Page count, word count and lesson count alone are not evidence of completion.

## A4 verification edition

Render from the same public Markdown source used for reading. Fix the verification layout to A4 portrait (210 × 297 mm), 25 mm margins on all sides, a readable 11 pt body font, 1.3 line spacing, and 9 pt or larger monospaced code. Keep heading levels, running page numbers, figure alternatives/captions, and a bibliography. Tables must remain legible: wrap or split them rather than shrinking type to inflate or force page counts. Code blocks may break across pages only when line labels and context remain clear. Record the build tool, version, command, font, edition date and page count in a book release note when a render is actually made. Inspect the rendered PDF rather than a planned word budget. Page count is a record of that render. It is not a writing target and not a completion gate. Do not add blank pages, front matter or layout tricks to change the count. No current book is claimed complete because of a page measurement.

The course tracks are independent educational blueprints. Names such as bachelor's, engineering, master's, and doctorate describe intended depth and duration. They are not accredited programs or promises of a formal degree. The requested two-year doctoral research timeline is particularly dependent on institutional and jurisdictional rules.

## Sequential production order

Begin with [Incident Response](levels/rapid-1-month/incident-response-resilience/README.md), then work through the remaining [academic areas](AREA_MAP.md) and nine levels per area. The active production sequence is **English → Portuguese → Spanish**. Complete and review the full English reference collection first; translate the complete approved teaching into Portuguese and review it; then do the same independently for Spanish. Translate from a pinned, reviewed English source, never from a plan or an unreviewed draft. A language folder or plan is a production location, not evidence that the lessons have been written. Existing translations stay; do not replace them with a shorter outline.

**Gate before other languages:** Do not start planned authoring or translation for Hebrew, French, Russian, German, Chinese or Japanese until **English, Portuguese and Spanish have each reached 100% verified collection completion**. This means that all 207 course editions in each of those three languages teach their full intended weekday curriculum and pass the publication gate above, with every required lesson's worked example, exercise, worked answer, source and navigation checked. Portuguese and Spanish additionally need complete, current, reviewed parity with the pinned English editions. Verify each book on the public `main` branch and in the public reader and MCP; keep the source and target revisions and review evidence. A manuscript file, structural chapter percentage, daily anchor, translated interface, page render or partial batch cannot make the collection 100%. If an English revision changes translated teaching, recheck the affected Portuguese and Spanish units before retaining a 100% claim. Existing public material in the six later languages remains available and may receive maintenance corrections, but it does not advance the production queue before this gate.

The first authored priority is the [Incident Response / Rapid / English draft](levels/rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md). Earlier [Cybersecurity](levels/rapid-1-month/cybersecurity/en/book/MANUSCRIPT.md) and [Security Governance](levels/rapid-1-month/security-governance-risk-compliance/en/book/MANUSCRIPT.md) drafts remain available for their later editorial turns.

The [complete course guide](COURSE_GUIDE.md) links every planned book and course level. Existing `book/PLAN.md` files often record the previous one-chapter-per-subject structure; expand them into weekly chapters with daily lessons as each edition is authored. Their summaries are not abstracts of finished manuscripts.

## Complete translations and cross-language parity

**Required destination:** every course at every level must have its complete instructional content available in all nine editions: English (`en`), Portuguese (`pt`), Spanish (`es`), Hebrew (`he`), French (`fr`), Russian (`ru`), German (`de`), Chinese (`zh`) and Japanese (`ja`). This is a production obligation, not a declaration of current availability. For one area, there are nine level-specific books in each language, not one book combining all levels. Keep one principal `MANUSCRIPT.md` per course and language and one shared course skill.

The daily targets in the [curriculum grid](CURRICULUM_GRID.md) apply independently to each edition. Their sum is 5,220 lessons per area and language; with the current 23 areas, the target is 120,060 lessons per language and 1,080,540 lesson-editions across nine languages. Of those lesson-editions, 960,480 are the eight non-English counterparts. These are arithmetic planning totals, not existing lessons, new books, translated pages or verified completion. There is no maximum lesson count. Existing English teaching, including legacy subject-chapters and their supplements, must not be dropped when mapping to the daily curriculum or translating it.

Follow the [AI guide's language order](AI_GUIDE.md#language-and-citation-rules): finish English, then Portuguese, then Spanish; begin the remaining six only after the three-language gate above passes. Inventory and preserve existing translations while the reference is reviewed. Do not restart a valid manual translation merely because the English source has changed; compare the actual changes and reconcile them. Public, accurate existing translations remain readable. Reference defects discovered during translation require an explicit correction and renewed comparison, not a silent change to the learner's task.

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

The generated files are **outlines and production plans**. No generated file is a finished lesson or a verified translation. Progress is the quality of the teaching that is actually present, judged against the publication gate above.
