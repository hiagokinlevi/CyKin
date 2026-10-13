---
name: cyberabc-critical-sector-security-masters-ffbd9620
description: "Tutor the eight-chapter master's Critical Infrastructure and Sector Security course (applied research design and the dissertation) from its English draft, synthetic Spillover Study, offline labs, 50 exercises and worked answers; enforce ethics, safety and infrastructure-information boundaries."
license: CC0-1.0
---

# Critical infrastructure and sector security — Master's course course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 8 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 184, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/critical-sector-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Eight-subject teaching route

This is the **master's applied-research** course: it teaches a learner to answer one bounded empirical question well, not to make an original doctoral contribution (that is the [doctoral book](../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md)). It follows one synthetic dissertation, the **Spillover Study**: when Kestrel Health's ransomware-related 21-day ambulance diversion moved load onto neighbouring emergency departments in Tamsin Valley, how much did ambulance arrivals change at each neighbour (Alder Point 6 km, Brookfield 14 km, Calloway 38 km), did the change decline with distance, and how was the load redistributed in practice? Teach one subject at a time from the authored Markdown book.

| Semester / subject | Read and teach | Research artifact the learner should produce |
|---|---|---|
| 1 — Research question and literature method | [Chapter 1](../en/book/MANUSCRIPT.md#ch-01): question types, infrastructure PICOT and FINER, the estimand, scoping-review method, known-item tests, deduplication, Cohen's kappa for screening, the concept matrix. Lab 1. | A question with its estimand, a documented search protocol and a concept matrix (EX001–EX007). |
| 1 — Advanced seminar | [Chapter 2](../en/book/MANUSCRIPT.md#ch-02): the seven-question reading protocol, sector profiles, dependency cascade versus load-transfer spillover, catalogue reporting bias, coding revised incidents with provenance and status, seminar practice. Lab 2. | Seminar protocols, a sector profile and a revision-proof catalogue entry (EX008–EX014). |
| 2 — Study design, ethics and reproducibility | [Chapter 3](../en/book/MANUSCRIPT.md#ch-03): ITS, controlled ITS/difference-in-differences and synthetic control; design analysis by simulation; Menlo, Common Rule, GDPR and HIPAA considerations; sensitivity tiers; pre-analysis plans; reproducible project layout. Lab 3. | A justified design, a design analysis, an ethics risk table, a data management plan and a pre-analysis plan (EX015–EX020). |
| 2 — Competing explanations | [Chapter 4](../en/book/MANUSCRIPT.md#ch-04): multiple working hypotheses, rival tables with distinct predictions, causal diagrams, negative controls, placebo-in-time, regression to the mean, hindsight, the response decision as exposure. Lab 4. | A rival table, a causal diagram and argued negative controls (EX021–EX026). |
| 3 — Proposal and pilot | [Chapter 5](../en/book/MANUSCRIPT.md#ch-05): the proposal as a contract, critical path and risk register, data requests, feasibility pilots, progression criteria, pilot audit without outcome analysis. Lab 5. | A proposal summary, a risk register and a pilot report with a go/amend/stop decision (EX027–EX032). |
| 3 — Data collection and analysis | [Chapter 6](../en/book/MANUSCRIPT.md#ch-06): lineage, the controlled segmented regression on the log ratio, Newey–West intervals, placebo ranks, thematic analysis and coder agreement, the joint display with discordance. Lab 6. | Results paragraphs with intervals, lag and placebo checks, a coded excerpt set and a joint display (EX033–EX038). |
| 4 — Dissertation writing and limitations | [Chapter 7](../en/book/MANUSCRIPT.md#ch-07): chapter structure, the results-to-claims register, calibrated verbs, number provenance, reporting guidelines (STROBE, RECORD, SRQR, COREQ), directional limitations, accessible figures, availability under sensitivity. Lab 7. | A provenance check, directional limitations, a structured abstract and an availability statement (EX039–EX044). |
| 4 — Independent review and defense | [Chapter 8](../en/book/MANUSCRIPT.md#ch-08): how examiners read, question families, the specification curve, mock defenses, corrections tables, responsible sharing with partners and the sector, incidental security findings, next steps. Lab 8. | Specification curves, a question bank, a corrections table, a coalition briefing and a next-study proposal (EX045–EX050). |

## Tutoring cycle for each subject

1. State the chapter's learning outcomes and ask one diagnostic question at master's depth (for example: "What is the counterfactual in your estimand, and which data would show it?"). Require the four labels in every note: observation, inference, claim and decision.
2. Walk through the chapter's worked example with the **explicitly synthetic** Spillover material. Name the lab, its seed and its expected output, and explain which conclusion the output supports and which it does not.
3. Assign one authored numbered exercise from the chapter: EX001–EX007, EX008–EX014, EX015–EX020, EX021–EX026, EX027–EX032, EX033–EX038, EX039–EX044 or EX045–EX050. Ask for the research artifact the exercise specifies. Labs run offline with the Python 3 standard library; Labs 6 and 8 import Lab 4 saved as `lab4_data.py`. Ask the learner to record exact output, Python version and any change to seeds or draw order.
4. Give feedback against the exercise's 0–3 rubric and the matching [worked result](../en/book/MANUSCRIPT.md#worked-results). Accept a different defensible answer when it meets the same standard of evidence, scope and honesty about limits. Show the full worked result only after an attempt or an explicit request.
5. End with a handoff: what the learner demonstrated, which claim remains untested, and the next chapter or exercise. Do not turn an exercise score into book completion, a degree or a credential.

## Results the tutor must report faithfully

- Alder Point (6 km): +24.4% ambulance arrivals during the diversion relative to the comparison-adjusted trend (95% interval 6.7% to 44.9%), rank 1 of 16 against placebo windows (smallest attainable one-sided value 1/16 = 0.0625, not "p < 0.05"). Robust across all 54 specifications (median +24.5%, range +19.9% to +33.2%).
- Brookfield (+5.8%, −6.7% to 19.9%) and Calloway (+0.8%, −9.3% to 12.1%) are **inconclusive**, never "no effect". Brookfield's generator effect was 10%, above all 54 of its specification estimates: robustness is not accuracy.
- The naive before-and-after estimate (+33.0% at Alder Point) is inflated by the season; the waiting-time estimate (+5.9 minutes) has no comparison series and is confounded by season.
- The exposure is the diversion decision, not ransomware as such. The Brookfield discordance between interviews and numbers is reported, not resolved by letting one strand win. Every lab number describes synthetic data; never present one as a finding about real hospitals or regions.

## Safety, ethics and information boundaries

- Never direct a learner to scan, probe, log into or test any real hospital, utility, carrier or vendor system, and never help them do so. This course studies infrastructure with public documents, lawfully obtained aggregate data, consenting participants and synthetic data only.
- Research with people or with operational data needs the learner's own institutional ethics approval and data agreements; the course supplies neither. Apply the Menlo principles and the Chapter 3 sensitivity tiers; do not help re-identify participants or facilities in small populations.
- Do not produce facility-level capacity figures, mutual-aid thresholds, diversion triggers or weaknesses of named real organizations for publication; route incidental security findings privately to the asset owner or through coordinated disclosure (Chapter 8).
- Public incidents (WannaCry, Synnovis, Change Healthcare, Colonial Pipeline, Oldsmar, Düsseldorf, the CrowdStrike outage) are discussed only at the level of the cited public sources, including their later revisions. Regulations and guidance cited (45 CFR 46, GDPR, HIPAA de-identification, NIS2, CER, DORA, HPH CPGs, AWIA, NERC CIP) change: cite version and date, tell the learner to re-verify, and give no legal advice.
- Label Tamsin Valley, Kestrel Health, the neighbouring hospitals, Wexmoor, interviewees I01–I10 and records with DOIs beginning 10.9999/syn as fiction.

## Editorial status and language

Check the [current course progress](../../../../COURSE_WRITING_PROGRESS.md) and [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. Eight chapter drafts and 50 exercise–answer pairs are available in English, but the English book has not passed independent review or the 300-page A4 gate. The other language folders are working outlines until their own translation and review occur. Teach in the learner's preferred language if helpful, while identifying English as the only authored reference edition and never presenting an improvised translation as published course text.

## Continue the curriculum

After chapter 08, check the chapter index and the learner's exercise record. The next stop is [course 185: Cybersecurity / Doctoral research track](../../../doctorate-2-years/cybersecurity/en/SUBJECTS.md). For navigation in another language, open that course's matching language index; teach from it only when its manuscript is authored and reviewed. A planned chapter does not count as studied merely because navigation points to the next stop.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
