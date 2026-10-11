# CyberABC structure and progress review

Reviewed 11 October 2026. [Project introduction](README.md) · [academic area map](AREA_MAP.md) · [course guide](guia-geral-cursos-e-livros.md) · [source audit](SOURCE_AUDIT.md).

## Verified structural snapshot

| Layer | Current count | Meaning |
|---|---:|---|
| Schools | 5 | Navigation groups for the broad academic areas |
| Academic areas | 23 | One course under each level, nine editions per course and a separate playbook index |
| Distinct course designs | 207 | Nine levels per area; one principal English book planned per course |
| Planned language editions | 1,863 | Nine language folders per course; most are structural plans only |
| English curricular subjects | 4,186 | One subject is one planned chapter within its course's book |
| Course AI skills | 207 | One skill per area-and-level course; no separate subject skills |
| Book chapter summaries across nine languages | 37,674 | Editorial summaries; other languages still contain English working outlines |
| Individually tailored English chapter briefs | 336 of 4,186 (8.03%) | All 182 Incident Response chapters and 154 Cybersecurity chapters; 3,850 remain template-based working summaries |
| Authored English chapter drafts | [Current generated count](WRITING_PROGRESS.md) | Area-by-area percentages measure manuscript draft teaching; they do not certify chapter or book completion |
| Revision-pinned source playbook links | 14 | Supplementary references in matching area playbook indexes |
| Authored English manuscripts | 3 drafts | Incident Response rapid: four chapters, 50 exercises, nine supplementary labs or drills across Chapters 1–4, a cited British Library source-reading activity and a Chapter 4 model tabletop with after-action report; Cybersecurity rapid: three chapters and 15; Security Governance rapid: one chapter and 5 |
| Complete verified books | 0 | No 300-page A4 volume and complete 50-exercise answer set has passed review |

## Completion measure

The folder and plan scaffold covers **207 of 207 courses and 1,863 of 1,863 planned editions (100% of the current catalog's structural coverage)**. This is a coverage measure, not an educational-completion score. Every edition still requires authored teaching, chapter exercises and worked answers, source and technical review, and an A4 release check. **Completed editions: 0 of 1,863 (0%); 1,863 of 1,863 (100%) remain to pass the book gate.** Three English manuscripts are drafts and do not count as completed books. The first manuscript currently has **38,820 whitespace-separated words**, including exercises, answers and references. A local A4 preflight of that exact source produced **82 actual pages**, well below the 300-page minimum; this is not a completed-book or final-release verification. The [course-level table](COURSE_WRITING_PROGRESS.md) reports chapter-draft coverage, manuscript words and hash-checked A4 length for every English course where a measurement exists.

### A4 preflight

Measured 11 October 2026. Source SHA-256 `55a3304ecd32ff08256f98a462930dd043bca03fd022b57508b567620dbb9678`; A4 portrait, 25 mm margins, 11 pt body at 1.3 line spacing and 9 pt code, rendered locally with Chrome 154.0.8037.99. The 82-page PDF has no empty page by extracted-text screening. Pages 35–37, 70–71 and 82 were visually inspected for the new backup-candidate table, decision gates, worked result and final references; the opening and older code-listing pages were inspected in preceding preflights. The answer matrix spans pages 70–71 with a repeated header and remains readable; final pagination can improve. This preflight is **218 pages short of the minimum** under the current layout, and the manuscript still needs substantive expansion, independent technical/source review and a final edition review. Any source or layout change requires a new count. The derived PDF is an editorial check; the public teaching source remains Markdown.

At the chapter-planning level, **336 of 4,186 English briefs (8.03%)** have been individually tailored to their subject: all 182 Incident Response chapters and 154 Cybersecurity chapters. **3,850 (91.97%)** English briefs remain template-based and need editorial refinement before they can be treated as complete chapter designs. Non-English outlines are English working copies; no translated edition has been completed. A single percentage for all authoring work would be misleading until completed pages, exercises and reviews are measured consistently.

The [README bookshelf](README.md) displays a separate **draft-writing coverage** percentage for every academic area. Its [sigil key and current counts](WRITING_PROGRESS.md) and the [207 course percentages](COURSE_WRITING_PROGRESS.md) are regenerated locally from English manuscripts before publication. The draft threshold is at least 300 words of teaching before exercises; this does not verify that any counted chapter or its book meets the publication standard.

The 23-area curriculum consolidates the earlier, overly fragmented specialization scaffold. Its generated folders were removed from the public reading tree. The two previously authored manuscripts were integrated into the new Cybersecurity and Security Governance course folders; no authored chapter was discarded. The earlier catalog and playbook mapping are retained in the private construction workspace for migration traceability. Fourteen linked source playbooks were reassigned to the broader areas. The [public area map](AREA_MAP.md) distinguishes this project taxonomy from official frameworks and cites the ACM/IEEE/AIS/IFIP curricular guidance, NIST and ENISA.

## What a reader can use now

All nine [Incident Response course levels](levels/rapid-1-month/incident-response-resilience/README.md) now have distinct subject sequences, with shared foundations retained where appropriate. All **182 English chapter briefs** specify a distinct purpose, concepts, synthetic example, activity and learning sequence. The nine English plans also link [primary-source starting points](SOURCE_AUDIT.md#incident-response-primary-source-leads); full chapter bibliographies remain pending. The [rapid book draft](levels/rapid-1-month/incident-response-resilience/en/book/MANUSCRIPT.md) has initial teaching for all four subjects, 50 exercises and worked results. Chapter 1 explains the preparation-versus-case distinction in NIST SP 800-61 Rev. 3, separates response recommendation from approval, execution and verification, and includes a bounded 09:05 decision gate and readiness workshop. Chapter 2 distinguishes event, discovery, ingestion, query-run and collection times; it adds a bounded query-coverage example, two synthetic labs, a separate delayed-arrival T2 replay and a three-variant evidence-package peer audit. All three published Chapter 2 Python examples and their expected outputs were run locally. Chapter 3 compares bounded containment options, distinguishes RTO/RPO targets from demonstrated recovery, and adds guided booking reconciliation, a read-only CSV comparison and an optional three-candidate isolated-restore replay. The replay separately screens provenance, byte integrity, data-point age, booking correctness and service acceptance; its matrix and worked result do not claim a production restore. The two-part Python comparison listing and its worked output were checked locally. Chapter 3 also compares the fictional case with the [British Library's cited 2024 incident review](https://www.bl.uk/files/v5dwkion/production/99206a2d1e9f07b35712b78f7d75fbb09560c08d.pdf/british-library-cyber-incident-review-8-march-2024.pdf?dl=), explicitly separating reported facts from teaching inferences. R17's wording was corrected so the training owner does not anticipate the later B20 edit. Chapter 4 releases later evidence in sequence, includes a claim ledger, a six-artifact tabletop handoff, a measurement contract, an original model after-action report and an optional approval-route replay lab with a worked result. R21's tolerable pause is no longer described as formal service-owner approval. All **50 numbered exercises** now have objectives, inputs, required artifacts, assessment criteria and expanded worked results; the Chapter 4 answers respect card-release order. The [subject index](levels/rapid-1-month/incident-response-resilience/en/SUBJECTS.md) links the course skill and marks all four chapters as drafts. The rapid lessons still need substantial expansion and technical review; the other eight books need authored chapters.

An internal structural pass found no duplicate chapter title within any Incident Response course, matched all 182 briefs to their grade and checked the planned study hours, pages and exercise allocations. Specialist review of the proposed depth and cases is still pending. The [curriculum grid](CURRICULUM_GRID.md) now shows exercise targets that rise with study level; these allocations are plans, not written exercises or completed-book evidence.

The [Cybersecurity rapid draft](levels/rapid-1-month/cybersecurity/en/book/MANUSCRIPT.md) contains three chapters and 15 worked exercises. Its four rapid chapter briefs now match the existing manuscript. The professional, technical, technologist, bachelor's and engineering plans have distinct subject-specific titles and briefs for 12, 18, 30, 40 and 50 chapters respectively. The postgraduate, master's and doctoral Cybersecurity plans still contain **28 provisional summaries**. The [Security Governance rapid draft](levels/rapid-1-month/security-governance-risk-compliance/en/book/MANUSCRIPT.md) contains one chapter and five worked exercises. These are available for study as drafts and will be edited in the English production cycle.

Each level links all 23 area course homes; each course home links its one skill, nine editions and separate playbooks. Every course has one book; its subjects are chapters with planned explanations, examples and exercises. Chapter summaries are **not** authored lessons. Non-English plans remain structural placeholders until translation, technical review and language editing.

## Publication and rights

Original maintainer-owned text is dedicated under [CC0 1.0](LICENSE), subject to [rights exceptions](RIGHTS.md). Linked third-party material and independent repositories retain their own rights. The [book standard](BOOK_STANDARD.md) requires an original complete manuscript, at least 50 substantial exercises with worked answers, technical and editorial review, accessible Markdown and at least 300 actual A4 pages in a fixed verification layout. No current draft passes that gate.

## Sequential progress

| Step | State | Next evidence |
|---|---|---|
| Review existing course, project and playbook material | Sample reviewed; migration recorded | Continue per-source technical and rights checks before adaptation |
| Consolidate broad academic areas | Structured: 23 areas across five schools; each has a distinct scope, boundary, competencies and reuse decision | Specialist check of boundaries and ACM/NICE coverage |
| Create all language, course and book-plan trees | Structured | Keep links and counts verified on each change |
| Define course subjects and one skill per course | English structure generated; 336 chapter briefs tailored across Incident Response and Cybersecurity | Review these briefs and refine the other 3,850 English briefs, subject grids and skill guidance during authorship |
| Author Incident Response in English | Rapid four-chapter draft and 50 specified exercises with worked answers; nine supplementary labs or drills, a cited source-reading case and a Chapter 4 model tabletop and report; 82-page A4 preflight | Deepen substantive teaching and independently check all exercise answers; validate the rapid book against the complete-book gate, then author professional through doctoral levels |
| Author other English areas | Two earlier drafts retained | Resume after Incident Response priority, then cover all 207 courses |
| Review and edit the entire English set | Pending | Complete manuscripts and specialist reviews first |
| Translate and review Portuguese | Pending | Approved English reference set first |
| Translate Spanish and other DAI languages sequentially | Pending | Portuguese edition reviewed first |
| Validate finished books | Preliminary 82-page A4 count for the first draft only; no approved book | Final 300-page-or-longer A4 evidence and reviewer record per edition |

The learning paths are public educational plans, not accredited degrees or professional licenses.
