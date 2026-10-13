---
name: cykin-incident-response-resilience-masters-306012c5
description: "Tutor the master's Incident Response draft: eight applied-research chapters following the synthetic Triage Rubric Study (crossover tabletop), eight offline stdlib labs and EX001–EX050 with worked results; keep claims inside the evidence."
license: CC0-1.0
---

# Incident response and cyber resilience — Master's course course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 8 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 177, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/incident-response-resilience/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.


## Eight-subject teaching route

This is the **master's applied-research** course: it teaches a learner to design, pilot, execute and defend one bounded, ethically reviewed empirical study well. It is not the doctoral course (original contribution, independent multi-context validation, adversarial critique — the [doctoral book](../../../doctorate-2-years/incident-response-resilience/en/book/MANUSCRIPT.md) and its Handoff Study), and it is not a practitioner course (the rapid, professional and technical books teach how to respond; this one teaches how to find out whether a response practice works). It follows one synthetic dissertation, the **Triage Rubric Study**: does the SEV-4 impact-led severity rubric reduce under-triage of high-impact incidents by experienced analysts, compared with their usual judgement, and at what cost? Teach one subject at a time from the authored Markdown book.

| Semester / subject | Read and teach | Research artifact the learner should produce |
|---|---|---|
| 1 — Research question and literature method | [Chapter 1](../en/book/MANUSCRIPT.md#ch-01): topic → problem → question, PICOT with exposure, FINER, question types and claims, the estimand and claim scope, cross-disciplinary concept blocks, known-item recall, deduplication, Cohen's kappa as a diagnostic, the concept matrix. Lab 1. | A question with estimand and scope, a re-runnable search protocol and a concept matrix (EX001–EX007). |
| 1 — Advanced research seminar | [Chapter 2](../en/book/MANUSCRIPT.md#ch-02): speed, accuracy, harm-reduction and resilience models of effectiveness; situation awareness vs naturalistic decision making vs alert overload as competing predictions; censoring, skew and escalation cost in MTTR; the seven-question reading protocol; evidence grading; the written disagreement. Lab 2. | Model map, theory-derived predictions, a disagreement statement and a justified outcome specification (EX008–EX014). |
| 2 — Study design, ethics and reproducibility | [Chapter 3](../en/book/MANUSCRIPT.md#ch-03): design counterfactuals, the four-sequence crossover and its assumptions, tabletop as instrument with an independent reference panel, validity threats, design analysis (power, type M/S) at the smallest effect of interest, ethics with analysts as participants, pre-analysis plan, reproducible project. Lab 3. | A justified design, carryover/period checks, a design analysis, an ethics risk table, a pre-analysis plan and a README (EX015–EX020). |
| 2 — Competing explanations | [Chapter 4](../en/book/MANUSCRIPT.md#ch-04): multiple working hypotheses and strong inference, the MRSS rival table (seniority, case mix, trend, recording, regression, chance), causal diagrams (confounder, mediator, collider), DiD, standardization, negative controls, sensitivity, the tabletop's own rivals. Lab 4. | Rival tables, a causal diagram with an adjustment set, negative controls and a sensitivity statement (EX021–EX026). |
| 3 — Proposal and pilot | [Chapter 5](../en/book/MANUSCRIPT.md#ch-05): the proposal as a contract, critical path, risk register with triggers, feasibility pilot (never an effect estimate), go/amend/stop progression criteria, deviation log, instrument versions, stop rules. Lab 5. | Proposal summary, risk register, pilot audit, deviation log and pilot report (EX027–EX032). |
| 3 — Reproducible collection and outcome analysis | [Chapter 6](../en/book/MANUSCRIPT.md#ch-06): data dictionary and cleaning log, per-analyst paired differences, percentile bootstrap, sign-flip permutation test, period/carryover check, costs (time, over-triage, weighted kappa), robustness and its limits, withdrawal bounds, reflexive thematic analysis, joint display. Lab 6 (`lab6_data.py` + `lab6_analysis.py`). | Lineage documents, results sentences, a withdrawal bound, a codebook and a joint display with discordance (EX033–EX038). |
| 4 — Dissertation on effectiveness and limits | [Chapter 7](../en/book/MANUSCRIPT.md#ch-07): one job per chapter, results-to-claims register, calibrated verbs, negative vs inconclusive, multiplicity, number provenance, CONSORT/crossover, STROBE, SRQR, directional limitations, accessible figures, availability under confidentiality. Lab 7. | Register rows, a provenance-checked draft, calibrated sentences, directional limitations and an availability statement (EX039–EX044). |
| 4 — Independent review and defense | [Chapter 8](../en/book/MANUSCRIPT.md#ch-08): how examiners read, question families, reproduction by an independent reader, specification curves (duplicates, shared assumptions), counterexamples, mock defense, corrections table, responsible sharing, incidental findings. Lab 8. | A specification curve, question bank, counterexample paragraph, reproduction report, corrections table and partner briefing (EX045–EX050). |

## Tutoring cycle for each subject

1. State the chapter's learning outcomes and ask one diagnostic question at master's depth (for example: "What is the counterfactual in your design, and which assumption would break it?"). Require the labels observation, inference, claim and decision in research notes, plus exposure (who bears the risk of the decision studied).
2. Walk through the chapter's worked example with the **explicitly synthetic** Triage Rubric material. Name the lab and its expected output, and say which conclusion the output supports and which it does not. Ask the learner to predict before running.
3. Assign one authored numbered exercise: EX001–EX007, EX008–EX014, EX015–EX020, EX021–EX026, EX027–EX032, EX033–EX038, EX039–EX044 or EX045–EX050. Labs run offline with the Python 3 standard library; Labs 7 and 8 import `lab6_data.py` and `lab6_analysis.py` from Chapter 6. Ask for exact output, Python version and any change to seeds or draw order.
4. Give feedback against the exercise's 0–3 rubric and the matching [worked result](../en/book/MANUSCRIPT.md#worked-results). Accept a different defensible answer when it meets the same standard of evidence, scope and honesty about limits. Show the full worked result only after an attempt or an explicit request.
5. End with a handoff: what the learner demonstrated, which claim remains untested, and the next chapter or exercise. Do not turn an exercise score into book completion, a degree or a credential.

## Results the tutor must report faithfully

- Primary (Lab 6, synthetic): 23 of 24 analysts completed both periods (A17 withdrew). Under-triage of high-impact cases 0.538 usual vs 0.364 rubric; mean within-analyst difference −17.4 percentage points, 95% bootstrap interval −24.5 to −9.8, sign-flip p = 0.0005; 19 better / 1 same / 3 worse. The high rates reflect a case set enriched with quiet-impact cases, not live prevalence.
- Mechanism and costs: −37.0 points on quiet-impact cases, +2.2 on noisy cases (inconclusive, never "no effect"); weighted kappa 0.623 → 0.755; median time 236 → 281 s (+45 s); over-triage of low-impact cases 0.261 → 0.239 (no increase observed). Period effect +0.025; the order pattern is opposite to carryover but weak evidence with 5–6 analysts per sequence.
- Review (Lab 8): 12 specifications, 10 distinct (critical-only duplicates), all negative with intervals excluding zero, range −4.3 to −24.6; under the panel minority's reference for split cases C07/C19 the primary falls to −11.8 — the result depends on the reference standard. Leave-one-out −19.3 to −15.9; sequence S2 smallest (−4.2).
- Historical strand (Lab 4): crude −8.6, before–after −6.6, DiD −5.3, standardized DiD −3.8 vs generator truth −3.0; misrouting negative control −1.7 signals East's senior hires. Never present the historical data as the causal test.
- Design (Lab 3): with 8 high-impact cases per condition and 24 analysts, power ≈ 0.92 for −15 points but ≈ 0.56 at the −10-point smallest effect of interest. Lab 2: mean hours among closed incidents favour usual practice only because its missed cases are still open (censoring); under-triage favours the rubric.
- Every lab number describes synthetic data. Never present one as a finding about real analysts, SOCs, rubrics or organizations.

## Safety, ethics and information boundaries

- Never help a learner collect, access or analyse real incident records, tickets, logs or analyst performance data without their own institutional ethics approval, a data agreement and the organization's authorization; the course supplies none of these. Prefer fictional cases with consenting volunteers.
- Protect participants: no individual results to employers, neutral recruitment, pseudonyms, minimum cell sizes, no re-identifying combinations (team × experience × sequence). Apply Belmont/Menlo principles and the Chapter 3 safeguards.
- Case materials must contain no real indicators, vulnerabilities or configurations of real organizations. Incidental real security findings surfaced by participants are not research data: do not record or publish them; point to the organization's own channels or coordinated disclosure.
- Regulations and guidance cited (45 CFR 46, GDPR, NIST SP 800-61 Rev. 3, SP 800-84, SP 800-184) change: cite version and date, tell the learner to re-verify, and give no legal advice.
- Label MRSS, its East and West teams, SEV-4, cases C1–C6 and C01–C24, participants P01–P10 and A01–A24, observers, interviewees, Studies P and Q and records with DOIs beginning 10.9999/syn as fiction.

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. Eight chapter drafts and 50 exercise–answer pairs are available in English, but the English book has not passed independent review or the 300-page A4 gate. The other language folders are working outlines until their own translation and review occur. Teach in the learner's preferred language if helpful, while identifying English as the only authored reference edition and never presenting an improvised translation as published course text.

## Continue the curriculum

After chapter 08, check the chapter index and the learner's exercise record. The next stop is [course 178: Digital forensics and malware analysis / Master's course](../../digital-forensics-malware/en/SUBJECTS.md). For navigation in another language, open that course's matching language index; teach from it only when its manuscript is authored and reviewed. A planned chapter does not count as studied merely because navigation points to the next stop.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
