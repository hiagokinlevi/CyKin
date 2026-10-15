# Translation progress — availability and verified equivalence

**Visual-record update (14 October 2026):** Automatic section-title lesson maps and duplicate logical drawings were removed from all published manuscripts. Earlier dated checks of those figures below are historical evidence, not a description of the current lessons. Content-specific technical diagrams remain available where needed.

[Home](README.md) · [Edition inventory](LANGUAGE_LESSON_PROGRESS.md) · [Translation standard](BOOK_STANDARD.md#complete-translations-and-cross-language-parity) · [Curriculum baselines](CURRICULUM_GRID.md)

**Latest integration:** [14 October 2026 — Portuguese Chapters 05–20 incorporated](#pt-ch05-20-integration-20261014): sixteen previously prepared chapter translations and sixteen exercise/answer pairs are incorporated into the existing public Portuguese book. That entry records the source and target blobs, actual checks and scoped increase. Complete-book translation parity remains unapproved. The earlier catalog tables below are historical, not live counters.

**Earlier scoped maintenance:** [14 October 2026 — Portuguese Chapter 2 reconciliation](#pt-ch02-reconciliation-20261014). The catalog tables and earlier findings below remain the historical snapshot named in the next paragraph; that update did not recount the catalog or present those numbers as live translation fidelity.

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

<a id="pt-ch02-reconciliation-20261014"></a>

## 14 October 2026 — Existing Portuguese Chapter 2 reconciled

This entry supersedes the earlier next-checkpoint instruction for Chapter 2 and records maintenance actually incorporated into the existing EN/PT manuscripts. It does not supersede the dated catalog inventory or certify a complete translation.

**Base revision:** `a27b199e2fc8c97362ada3f8aa4c57191aa887f1`. English source before correction: `e633a0668e2a9df35ce115a11b072a2714616aaa`; Portuguese before correction: `6aa62199e0ffe7ea73de3a4577174a908a2fc7cd`. The corrected [English manuscript](levels/rapid-1-month/information-security/en/book/MANUSCRIPT.md#ch-02) has blob `0b3a1361ae822a4602a8336e1e47ce8cecd6ddc6`; the reconciled [Portuguese manuscript](levels/rapid-1-month/information-security/pt/book/MANUSCRIPT.md#ch-02) has blob `4d7a912d0c5becb92dd4512a7388ff28fa356bf3`. These blob IDs identify the exact compared publication contents. Review responsibility remains hiagokinlevi; no independent human review is asserted.

| Reviewed unit | Source-to-target mapping and result |
|---|---|
| Chapter map and logical drawing | `ch-02` to `ch-02`: two Mermaid maps and one text drawing per edition now carry corresponding complete labels; the previous truncated-label finding is corrected in source, while rendered appearance remains unchecked |
| Objective and section 2.2 | Synthetic interpretation replaces a claim that the script closes shares; authentication language no longer implies universal takeover prevention or an unspecified phishing-resistant protocol |
| Laboratory explanation | Same complete Python listing and five output lines; corresponding explanation of generated rows, fixed seed, empty input, duplicated rows and absence of cloud operations |
| Concepts table | Matching distinctions between account attribution and a person, authentication and authorization, and authorized accounts versus building location |
| Assessment | EX014–EX026, EX053 and EX054: 15 English/Portuguese prompt, 0–3 rubric and final-answer pairs compared; IDs, inputs, requested decisions and original answers preserved |
| Discovery and navigation | Portuguese plan no longer claims the existing manuscript is unwritten; Portuguese index and final available chapter identify the untranslated continuation rather than implying completion |

**Reproduced tests:** Python 3.13.5; exact baseline `8/140`, `4/60`, `25/80`, `10/20`, total `47/300`. Six additional in-memory variants: empty input `0/0`; duplicated client rows `55/440`; all flags false `0/300`; all flags true `300/300`; finance omitted `43/240`; reversed rows retain `47/300` with a different first-seen folder print order. Code extracted from the staged Markdown matched the original common listing and reproduced the literal output independently in both editions. Markdown parsing and matching map node/edge structure were checked; Mermaid was not rendered. No actual cloud account, permission change or source export was tested.

| This course's measure | Before this maintenance | After this maintenance | Interpretation |
|---|---:|---:|---|
| Available Portuguese chapters / current 20 English chapters | 4 / 20 | 4 / 20 | 20% chapter presence, not 20% of all English teaching verified as translated |
| Available Portuguese exercise IDs / current 74 English exercise IDs | 58 / 74 | 58 / 74 | 78.38% ID presence, not reviewed parity |
| Existing Chapter 2 pairs explicitly compared | Earlier log recorded EX054 only | EX014–EX026, EX053–EX054: 15 / 15 selected pairs | Fourteen additional IDs compared, with EX054 rechecked; no extrapolation to other chapters |
| New Portuguese principal manuscripts or numbered lessons | — | 0 | Existing translation maintenance and corresponding technical corrections |
| Whole-book translation approvals | — | 0 | Complete technical, linguistic and rendering reviews remain open |

Catalog availability and daily-anchor counts were not raised. No other language was edited or re-audited in this maintenance pass. The six later-language zeroes in the historical table must not be presented as a fresh absence audit. The English book still has twenty chapter-lessons and the Portuguese book still has four published chapters. Translated navigation and repaired text are not additional lessons.

**Next Portuguese maintenance checkpoint:** Chapter 3 with EX027–EX038 and EX055–EX056, including their final answers, incomplete figure labels and overly broad MFA claims. Correct source defects explicitly before reconciling the corresponding Portuguese passage; preserve valid manual translations. Chapters 05–20 remain a separate untranslated continuation, not filled by this maintenance. The current production order and whole-collection gates remain unchanged. No current A4 render, site deployment or live-route test was performed.

<a id="pt-ch05-20-integration-20261014"></a>

## 14 October 2026 — Portuguese Chapters 05–20 incorporated

This entry records integration of the previously prepared Portuguese translations requested by the maintainer. It supersedes the earlier statement that Chapters 05–20 are absent from this course's public Portuguese manuscript. It does not claim complete English-collection review, approve the translated book or silently revise the global production rules. No other language manuscript or private Engine file is changed.

**Pinned base:** `0d7712574de969d8a745dc6c9de3d20d5c434412`. **English reference:** `levels/rapid-1-month/information-security/en/book/MANUSCRIPT.md`, blob `0b3a1361ae822a4602a8336e1e47ce8cecd6ddc6`. **Portuguese before:** blob `4d7a912d0c5becb92dd4512a7388ff28fa356bf3`. **Integrated Portuguese:** blob `9b61655266ce147aabb06bf5e59a9a4efdd6dc62`, 151,907 UTF-8 bytes. These are exact content identities, not review scores. Editorial responsibility remains hiagokinlevi; no independent human reviewer is asserted.

[Read Chapter 05](levels/rapid-1-month/information-security/pt/book/MANUSCRIPT.md#ch-05) · [Read Chapter 20](levels/rapid-1-month/information-security/pt/book/MANUSCRIPT.md#ch-20) · [Worked answers](levels/rapid-1-month/information-security/pt/book/MANUSCRIPT.md#worked-results) · [Portuguese course guide](levels/rapid-1-month/information-security/pt/SUBJECTS.md) · [Translation limitations](levels/rapid-1-month/information-security/pt/book/MANUSCRIPT.md#pt-translation-ch11-20)

### Source-to-target mapping

| English source anchors | Portuguese target anchors | Exercise/answer IDs in the same Portuguese book | Integration scope |
|---|---|---|---|
| `ch-05`–`ch-10` | `ch-05`–`ch-10` | EX059–EX064 | Six prepared chapter translations, figures, examples, prompts, rubrics and final answers |
| `ch-11`–`ch-20` | `ch-11`–`ch-20` | EX065–EX074 | Ten prepared chapter translations, figures, examples, prompts, rubrics and final answers |
| Earlier `ch-01`–`ch-04` | Existing `ch-01`–`ch-04` | EX001–EX058 preserved | No replacement of their teaching or answers; presentation and continuation navigation updated |

The sixteen new chapter bodies and answers match the previously delivered translation-package units. They include 48 stated learning objectives, sixteen worked-example tables with four rows each, sixteen Mermaid diagrams, sixteen logical text drawings and sixteen 0–3 prompt/answer pairs. These are content-presence and integration checks, not an independent linguistic certification. Source defects remain separately identified in the translated book rather than being silently rewritten in the learner's task.

### Verified increase in this book

| Measure | Before integration | After integration | What the increase means |
|---|---:|---:|---|
| Portuguese chapter positions / 20 English positions | 4/20 — 20% | 20/20 — 100% of positions | Sixteen newly available translated chapter positions, not 100% reviewed equivalence |
| Portuguese prompt IDs with final answers / 74 English IDs | 58/74 — 78.38% | 74/74 — 100% of IDs | Sixteen additional IDs and answers; original 58 preserved |
| Prepared continuation units still awaiting incorporation in this book | 16 | 0 | This package is incorporated, not a second book |
| New Portuguese book files | 0 | 0 | An existing principal manuscript was completed structurally, not duplicated |
| New complete-book translation approvals | 0 | 0 | Full technical, linguistic, rights and visual review remains open |

**Catalog delta, not a full recount:** the edition inventory at the pinned base, blob `e5e59418b09649b552c742dc939f64e3004df844`, reported 2,509 Portuguese chapter anchors and 124/207 Portuguese manuscripts. This commit adds sixteen chapter anchors to one existing manuscript: **2,509 + 16 = 2,525** as an inventory-plus-verified-delta ledger. The Portuguese plan also gains sixteen chapter positions, so its analogous indexed denominator is **4,186 + 16 = 4,202**. These derived totals are not a new full-catalog inspection and are not percentages of faithful translation. The existing 124/207 manuscript-availability figure is not increased by extending an existing book. The full edition inventory, root bookshelf, generated website catalog and lesson-index assets were not rebuilt by this integration; their earlier counters must not be silently presented as a new recount.

The manuscript's documented chapter-lesson marker allows a supporting reader to group the twenty positions into four pacing weeks. It creates no duplicate reading pages. The contribution adds sixteen translated chapter lessons, not twenty newly authored lessons; the first four already existed. A detector that only counts `lesson-NN` anchors will not measure this marker's semantics. No global daily-lesson or 120,060-lesson completion percentage is inferred from this update.

### Checks executed for this integration

Python **3.13.5** and markdown-it-py **4.2.0** were used locally. The complete original Portuguese text was recovered and its Git blob recomputed before editing. The candidate's blob matches the integrated blob named above. Direct comparisons confirmed that all four earlier teaching bodies, all 58 original prompts and answers, the executable code and the references remain unchanged. The only earlier-book changes are presentation, contents and navigation needed for the continuation. Twenty ordered unique chapter anchors, 74 unique prompt IDs and 74 unique answer IDs were checked. All twenty chapter navigation blocks are present; **62 in-book fragment destinations** resolve to explicit anchors. This does not claim that every external link was revalidated.

The original complete Chapter 2 program was extracted from the candidate Markdown and executed unchanged. Its five lines matched exactly: clients 8/140, finance 4/60, marketing 25/80, rotas 10/20, total 47/300. Two separate local adverse inputs were run: an empty list produced `all files: 0 of 0`; duplicated client rows produced clients 16/280 and total 55/440, with other folder counts unchanged. These are synthetic controls, not measurements of a real clinic or newly observed source data.

The package's **sixteen integration tests** were rerun successfully in temporary synthetic Git repositories, including refusal of manual edits, changed source or target, missing or repeated context, duplicate/missing exercise or answer IDs, symlink destinations, wrong origin, noncurrent checkout and repeated application. They test the local applicator, not a production deployment. The applicator was not run on a complete real repository checkout. A separate direct integration check used the exact recovered real manuscript and compared the complete resulting text. The package's structural verifier also passed: sixteen graphs with **75 corresponding connections**, original branch topology and required chapter components. Mermaid diagrams were not rendered.

**Limits:** no independent human review, complete semantic review of the first four chapters, resolution of the enumerated source defects, A4 rendering, real account/source operation, website deployment or live-route test is asserted. Source citations retained in the translation were not all externally revalidated in this integration. A successful Markdown parse, matching code or a matched graph is not proof of full linguistic or technical parity.

**Next Portuguese checkpoint:** finish reconciliation of the earlier chapters, starting with Chapter 3 and EX027–EX038, EX055–EX056, and then reconcile the source findings carried by Chapters 05–20. Preserve the now-published continuation instead of re-adding or counting it twice. Continue the Portuguese collection before the Spanish stage; this single-course integration is not collection completion.
