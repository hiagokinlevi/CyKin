# CyberABC study-book standard

Each of the 23 current academic areas has nine course tracks. Each track has a book location in each planned language: `en`, `pt`, `es`, `he`, `fr`, `ru`, `de`, `zh`, `ja`. This yields 207 distinct books in English and 1,863 planned language editions. A plan file is not a finished book. Markdown is the canonical authoring and public reading format; an A4 PDF is a derived format for page verification.

The [curriculum grid](CURRICULUM_GRID.md) organizes each course by **subjects**: 4, 12, 18, 30, 40, 50, 12, 8 or 8 by level. Each course edition has a `SUBJECTS.md` showing their order. **Each subject is exactly one chapter in the course's single principal book for that language.** The chapter contains explanation, examples, practice and its own exercises. A final appendix in that same book contains every worked answer. In a long program, supplementary cited readings, labs and research work may support the chapters. The 300-page rule below is a floor; larger page budgets are planned for longer courses. Exercise planning targets now rise with study depth: 50 for rapid, 60 for professional, 72 for technical, 90 for technologist, 120 for bachelor's, 150 for engineering, 60 for postgraduate, and 50 each for master's and doctoral tracks. These targets are **planned allocations, not written exercises**; the publication gate below remains a minimum of 50 substantive worked exercises in every completed edition.

This hierarchy is required for **every** cataloged area, including Web3, AI and LLM security, cryptography, post-quantum security and incident response. Each course has one skill linking its chapter index and book; subjects do not have separate skills. Preserve authored manuscripts, exercises, sources and history when a curriculum changes. The catalog is extensible, and the current count is a snapshot rather than a limit.

Original educational material owned by the maintainer is dedicated under [CC0 1.0](LICENSE), with the scope and exceptions described in [RIGHTS.md](RIGHTS.md). Sources cited inside a book retain their own rights and are not relicensed by this repository. Accurate source citation remains an editorial requirement, not a CC0 condition.

## Publication gate for each volume

1. Complete original instructional prose, diagrams, references, realistic sourced examples, and safe practical labs for the course level. Use direct links to primary sources for factual examples and distinguish documented facts from teaching inferences.
2. At least **50** numbered, substantial exercises distributed across the subject-chapters, with at least one exercise in every chapter. Every exercise needs a learning objective, inputs, constraints, reproducible steps, expected evidence, and an assessment rubric.
3. A final worked-results appendix in the same book, with a matching answer and explanation for every exercise ID. Exercises with no answer fail the gate.
4. Render the manuscript to **A4 PDF** and verify at least **300 actual pages**. The level-specific page budget in each `book/PLAN.md` is a target, not evidence of a rendered book.
5. Review citations, rights, accuracy, privacy, ethics, accessibility, language quality, and technical reproducibility. Use descriptive link text, ordered headings, text alternatives for figures, labeled code blocks, and plain-language summaries for complex tables. Record reviewer, date, and edition in the book metadata.
6. Public drafts may be read and studied while marked as drafts. Mark a volume **complete** and release its verified edition only after this gate passes.

## A4 verification edition

Render from the same public Markdown source used for reading. Fix the verification layout to A4 portrait (210 × 297 mm), 25 mm margins on all sides, a readable 11 pt body font, 1.3 line spacing, and 9 pt or larger monospaced code. Keep heading levels, running page numbers, figure alternatives/captions, and a bibliography. Tables must remain legible: wrap or split them rather than shrinking type to inflate or force page counts. Code blocks may break across pages only when line labels and context remain clear. Record the build tool, version, command, font, edition date and page count in a book release note; inspect the rendered PDF, not a planned word or page budget. Exclude blank pages, front-matter padding and layout tricks from the 300-page minimum. This specification is the validation target; no existing plan has yet been rendered and approved against it.

The course tracks are independent educational blueprints. Names such as bachelor's, engineering, master's, and doctorate describe intended depth and duration. They are not accredited programs or promises of a formal degree. The requested two-year doctoral research timeline is particularly dependent on institutional and jurisdictional rules.

## Sequential production order

Begin with [Incident Response](levels/rapid-1-month/incident-response-resilience/README.md), then work through the remaining [academic areas](AREA_MAP.md) and nine levels per area. Author **one distinct book per course in English**. Review and edit the whole English set and validate each book against the publication gate **before beginning Portuguese**. Then translate, review and edit Portuguese, Spanish, Hebrew, French, Russian, German, Chinese and Japanese in that order. The remaining language folders are structural placeholders until their turn. This is a long-term production sequence, not a claim that any language set is complete.

The first authored priority is the [Incident Response / Rapid / English draft](levels/rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md). Earlier [Cybersecurity](levels/rapid-1-month/cybersecurity/en/book/MANUSCRIPT.md) and [Security Governance](levels/rapid-1-month/security-governance-risk-compliance/en/book/MANUSCRIPT.md) drafts remain available for their later editorial turns.

The [complete course guide](COURSE_GUIDE.md) links every planned book and course level. Each `book/PLAN.md` records one planned chapter summary per curricular subject: 4 to 50 depending on level. These are editorial summaries of intended chapters, not abstracts of finished manuscripts.

## Book directory

Each `book/` starts with `PLAN.md`. Later authored content belongs beside it: manuscript sources, figure sources, safe lab data, exercise assets, worked solutions, references, and release evidence. Avoid publishing private data, access credentials, or unsafe offensive instructions.

## Editorial status

The generated files are **outlines and production plans**. No generated file should be counted as a completed 300-page book, a completed set of 50 exercises, or a verified translation. Progress is measured per volume against the publication gate above.
