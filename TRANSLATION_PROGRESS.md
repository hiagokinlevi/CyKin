# Translation progress — availability and verified equivalence

[Home](README.md) · [Edition inventory](LANGUAGE_LESSON_PROGRESS.md) · [Translation standard](BOOK_STANDARD.md#complete-translations-and-cross-language-parity) · [Curriculum baselines](CURRICULUM_GRID.md)

**Editorial responsibility:** hiagokinlevi. **Measurement snapshot:** `b542b64316b8fd413b764ac4c2710f35b22af1ac`. This is a dated inventory and scoped comparison, not a live counter or approval of any book. The later checked main `2deeac1c795e31830d149628e53dc97f930d2985` changed website files only; it did not change the inventory or the manuscript pair examined here.

## What the percentages mean

There are 207 courses, each with one principal book per language. Therefore a course with a manuscript and a book manuscript are the same availability unit here; do not add those counts together. A partial manuscript counts as present, not as an entirely translated course. Across nine languages the catalog plans 1,863 book editions, not 1,863 different courses.

The English, Portuguese and Spanish quantities below are the figures reported by `LANGUAGE_LESSON_PROGRESS.md` at the snapshot, blob `b0d959da9ff8b3962d66f960acc089abb914f64b`. Their percentages were recalculated locally. This pass did not independently recount the full bodies of all manuscripts. The source inventory explicitly counts chapter anchors and daily `lesson-NN` anchors, not semantic completeness.

For Hebrew, French, Russian, German, Chinese and Japanese, the complete recursive Git tree obtained for `e04b47bccf302a8fa67fbff6d893afd8c17132ee` reported `truncated: false`. Searches found no canonical `/<language>/book/MANUSCRIPT.md` path for any of those six languages; a Portuguese manuscript path was found as a positive control. The comparison from that revision to the measurement snapshot added no manuscript in those languages. The snapshot README independently identifies these six editions as indexes/plans only. These zeroes do not count plans or navigation as translated books.

## Courses and books with publicly available text

**Availability percentage = courses with a principal manuscript in the language / 207 × 100.** These are availability percentages, not percentages of faithfully translated English text.

| Language | Courses with a manuscript / 207 | Principal book manuscripts / 207 | Catalog availability | Whole-book reviewed translation equivalence |
|---|---:|---:|---:|---|
| English (`en`) | 199 / 207 | 199 / 207 | 96.14% | Reference language; completion is separate |
| Portuguese (`pt`) | 124 / 207 | 124 / 207 | 59.90% | Not measured for the complete catalog |
| Spanish (`es`) | 27 / 207 | 27 / 207 | 13.04% | Not measured for the complete catalog |
| Hebrew (`he`) | 0 / 207 | 0 / 207 | 0.00% | No principal translated manuscript found |
| French (`fr`) | 0 / 207 | 0 / 207 | 0.00% | No principal translated manuscript found |
| Russian (`ru`) | 0 / 207 | 0 / 207 | 0.00% | No principal translated manuscript found |
| German (`de`) | 0 / 207 | 0 / 207 | 0.00% | No principal translated manuscript found |
| Chinese (`zh`) | 0 / 207 | 0 / 207 | 0.00% | No principal translated manuscript found |
| Japanese (`ja`) | 0 / 207 | 0 / 207 | 0.00% | No principal translated manuscript found |

An unmeasured equivalence percentage is **unknown**, not an asserted 0% or 100%. In particular, 59.90% means Portuguese manuscripts are reported for 124 courses; it does not establish that 59.90% of all English teaching has been translated or reviewed.

## Chapters and daily lessons — different denominators

The source inventory has **4,190 current chapter positions in English and 4,186 in Portuguese and Spanish**. Preserve the edition-specific denominators. Their difference is itself a reason not to equate structural chapter coverage with aligned translation coverage.

The daily planning baseline is `23 × (20 + 130 + 390 + 780 + 1040 + 1300 + 520 + 520 + 520) = 120,060` lessons per language. Most existing chapters still use the legacy structure; they must not be relabeled as that many daily lessons.

| Language | Reported chapters / current indexed positions | Structural chapter coverage | Explicit daily lesson anchors / 120,060 | Daily-anchor baseline coverage |
|---|---:|---:|---:|---:|
| English | 4,012 / 4,190 | 95.75% | 20 / 120,060 | 0.0167% |
| Portuguese | 2,509 / 4,186 | 59.94% | 0 / 120,060 | 0.0000% |
| Spanish | 516 / 4,186 | 12.33% | 0 / 120,060 | 0.0000% |
| Hebrew | 0; indexed denominator not recounted | Not applicable | 0 / 120,060 | 0.0000% |
| French | 0; indexed denominator not recounted | Not applicable | 0 / 120,060 | 0.0000% |
| Russian | 0; indexed denominator not recounted | Not applicable | 0 / 120,060 | 0.0000% |
| German | 0; indexed denominator not recounted | Not applicable | 0 / 120,060 | 0.0000% |
| Chinese | 0; indexed denominator not recounted | Not applicable | 0 / 120,060 | 0.0000% |
| Japanese | 0; indexed denominator not recounted | Not applicable | 0 / 120,060 | 0.0000% |

Zero explicit daily anchors in Portuguese or Spanish does **not** erase their existing instructional chapters. It means the inventory has not detected the new daily marker structure in those editions. Likewise, twenty English anchors do not independently prove twenty fully reviewed lessons. The [rapid Incident Response English index](levels/rapid-1-month/incident-response-resilience/en/SUBJECTS.md) identifies the reported twenty-lesson migration; another edition does not inherit it automatically.

## Scoped comparison actually performed

**Course:** 002, Information security / Rapid. This pass inspected existing Portuguese teaching, not a new translation pass. No manuscript was overwritten and no new translation was added.

| Item | Inspected source |
|---|---|
| English reference | [Principal manuscript](levels/rapid-1-month/information-security/en/book/MANUSCRIPT.md#ch-02); blob `d5fcfbebf1ad1c44f3184b42305b159d3d0d694c` |
| Portuguese counterpart | [Principal manuscript](levels/rapid-1-month/information-security/pt/book/MANUSCRIPT.md#ch-02); blob `ffd0e65dc6c8ce3e864060c593a04b1db501f4ec` |
| Final English answer location | [Worked results](levels/rapid-1-month/information-security/en/book/MANUSCRIPT.md#worked-results), EX054 |
| Final Portuguese answer location | [Worked results](levels/rapid-1-month/information-security/pt/book/MANUSCRIPT.md#worked-results), EX054 |

The common complete Python listing for the Chapter 2 synthetic sharing laboratory was compared across the two editions. Its machine-readable labels and output remain English in the Portuguese book; the surrounding instructions, data table and explanations are Portuguese. Preserving those exact executable literals is not an untranslated-prose defect.

**Execution performed:** the common listing was transcribed and run locally with Python **3.13.5**, standard library only, on synthetic in-memory data. Its five lines matched both published transcripts exactly: clients 8/140, finance 4/60, marketing 25/80, rotas 10/20, and total 47/300. This confirms this transcript, not real sharing permissions or the technical quality of the whole book.

Two additional synthetic controls were run without modifying the public lesson. An empty generation list printed `all files: 0 of 0`; this is an empty input, not demonstrated coverage or absence of exposure. Duplicating all generated client rows printed clients 16/280 and total 55/440, while the other folder counts stayed unchanged. The program counts supplied/generated rows and does not establish unique-file identity. Those adversarial inputs are not new canonical case facts.

**EX054 comparison:** the English and Portuguese prompt, 0–3 rubric, data and final answer were read together. Both require closing the eight client and four finance files first, moving rotas behind sign-in, and explaining why the twenty-five already-public marketing files may remain. That one assessment retained its requested decisions and numeric inputs. This pass does not certify the other 57 exercise pairs, every chapter, the bibliography or the course's complete translation.

**Open visual finding:** the Chapter 2 generated lesson-map label for the laboratory is incomplete in both editions: the English label ends in `by`, and the Portuguese label ends in `qual`. Their full laboratory headings are present. The generated maps also select different heading lists. Consequence: a matched diagram count does not prove equivalent or readable visual guidance. Proposed correction: use a complete, semantically matched compact label in the source and target, reconcile the selected map nodes against their lesson sections, then inspect the rendered diagrams. No diagram rendering or label correction was performed in this pass.

## Change ledger and next checks

| Delivery in this pass | Actual result |
|---|---|
| New translated manuscripts | 0 |
| New translated daily lessons | 0 |
| New translated course completions | 0 |
| Existing executable example checked across EN/PT | 1 common listing; five-line transcript reproduced |
| Additional synthetic controls executed | 2 |
| Existing prompt/rubric/answer pairs compared in detail | 1: EX054, EN/PT |
| New whole-book equivalence approvals | 0 |
| Website deployment or live-route test | Not performed |

This report establishes an honest baseline, not translation throughput. The [agent guidance](AGENTS.md) and [study path](STUDY_PATH.md#language-rule) still require the English collection to be written and reviewed before new sequential language passes. Preserve existing translations while inspecting them; do not replace valid manual work with shorter summaries. This pass did not change that production order.

The next **translation-quality checkpoint** is the same course's Chapter 2 EX014–EX026 and EX053, with both final answer sets, followed by the incomplete map labels. The main **authoring priority** remains Incident Response in the published production order; this sample does not move another area ahead in that queue. For the catalog table, refresh the pinned source, reconcile any changed edition denominators, and keep manuscript presence, daily structure and reviewed source-to-target equivalence separate.

Each subsequent report should state the source and target revisions, new translations actually published, existing translations reconciled, exercises/answers checked, the current table and the difference from the preceding measured snapshot. A changed English reference makes the affected translation units pending comparison; unchanged translations remain available. Until every source unit is mapped and checked, the catalog's faithful-translation percentage remains unmeasured.
