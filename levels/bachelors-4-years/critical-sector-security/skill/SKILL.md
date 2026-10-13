---
name: cyberabc-critical-sector-security-bachelor-f369794c
description: "Tutor the forty-chapter bachelor's Critical Infrastructure and Sector Security course (foundations, cross-sector dependencies, evidence evaluation, comparison of methods and controls, applied incident and OT practice) from its English draft, synthetic Calder County case, 14 offline labs, 80 exercises and worked answers; enforce authorisation, safety and infrastructure-information boundaries."
license: CC0-1.0
---

# Critical infrastructure and sector security — Bachelor's course skill

Use this **one skill for the whole 4 years course**. The course has one principal book per language; each of its 40 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 115, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/critical-sector-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## What this course is (and is not)

This is the **bachelor's** course: breadth and judgement. It builds computing, programming, networks, data, identity, privacy, probability and cryptography foundations through critical-service examples, then teaches how healthcare, energy, water, transport, finance and public services work and depend on each other, how to read evidence critically, how to compare risk methods and controls with explicit assumptions, and how to take part safely in OT-aware operations and incident work. Its capstone is a **comparative, evidence-led recommendation**. It is not the [engineering course](../../../engineering-5-years/critical-sector-security/en/book/MANUSCRIPT.md) (design, build and verify one system against requirements), not the [master's course](../../../masters-2-years/critical-sector-security/en/book/MANUSCRIPT.md) (one ethically reviewed empirical study) and not the [doctoral course](../../../doctorate-2-years/critical-sector-security/en/book/MANUSCRIPT.md) (an original contribution to knowledge). Route deep design or research-method questions there.

The whole book uses one **synthetic** region: **Calder County** and its **County Resilience Partnership (CRP)** — Calder Valley Hospital (CVH, 420 beds, BMS, generators), Calder Power Networks (CPN, Substation North, feeder RTUs, VPN-G remote-access gateway), Calder Water (CW, pumps, 10-hour treated storage, telemetry), Calder Transit (CT, light-rail signalling and ticketing), Calder Mutual (regional bank) and the County Emergency Dispatch Centre (CEDC, CAD). Learners keep four headings for every case: **service, dependency, evidence, decision**.

## Forty-subject teaching route

Teach one subject at a time from the authored Markdown book. Exercises are two per chapter: chapter *n* holds EX(2n−1) and EX(2n).

| Semesters / chapters | Read and teach | Artefact the learner should produce |
|---|---|---|
| 1 — Ch. 1–5: Mathematical reasoning, Computing systems, Programming I, Academic writing, Security literacy | [Ch 1](../en/book/MANUSCRIPT.md#ch-01) expected loss vs worst credible event (Lab 1); [Ch 2](../en/book/MANUSCRIPT.md#ch-02) layers, IT/OT, device life cycle; [Ch 3](../en/book/MANUSCRIPT.md#ch-03) inventory triage in Python (Lab 2); [Ch 4](../en/book/MANUSCRIPT.md#ch-04) claim–evidence–warrant, citation; [Ch 5](../en/book/MANUSCRIPT.md#ch-05) vocabulary, CIA in critical services, reading advisories | Unit-checked comparison, life-cycle note, tested inventory script, decision summary, advisory extract (EX001–EX010) |
| 2 — Ch. 6–10: Discrete structures, Networks and protocols, Programming II, Data and databases, Ethics and authorized practice | [Ch 6](../en/book/MANUSCRIPT.md#ch-06) sets, logic, dependency graphs (Lab 3); [Ch 7](../en/book/MANUSCRIPT.md#ch-07) zones, conduits, flow checks (Lab 4); [Ch 8](../en/book/MANUSCRIPT.md#ch-08) input validation, the NaN lesson; [Ch 9](../en/book/MANUSCRIPT.md#ch-09) SQL joins, version types, injection (Lab 5); [Ch 10](../en/book/MANUSCRIPT.md#ch-10) authorisation, RoE, disclosure | Set triage, flow-violation hypotheses, validator with tests, advisory query, rules of engagement (EX011–EX020) |
| 3 — Ch. 11–15: Operating systems, Probability and statistics, Identity and access, Privacy foundations, Evidence and measurement | [Ch 11](../en/book/MANUSCRIPT.md#ch-11) hardening, risk-based patching; [Ch 12](../en/book/MANUSCRIPT.md#ch-12) base rates, repeated trials, binomial redundancy (Lab 6); [Ch 13](../en/book/MANUSCRIPT.md#ch-13) RBAC, toxic combinations, access review (Lab 7); [Ch 14](../en/book/MANUSCRIPT.md#ch-14) minimisation, re-identification; [Ch 15](../en/book/MANUSCRIPT.md#ch-15) evidence grading, metrics, sensitivity | Patch decision, alert-value analysis, role design, minimised log design, graded evidence table (EX021–EX030) |
| 4 — Ch. 16–20: Security architecture, Cryptography concepts, Research methods I, Scope and theory, Foundational cases | [Ch 16](../en/book/MANUSCRIPT.md#ch-16) principles, layered architecture, remote access; [Ch 17](../en/book/MANUSCRIPT.md#ch-17) HMAC with freshness, hash chains and anchors (Lab 8); [Ch 18](../en/book/MANUSCRIPT.md#ch-18) questions, designs, validity; [Ch 19](../en/book/MANUSCRIPT.md#ch-19) sectors, functions, NIS2/CER/DORA/CAF, risk–resilience–systems lenses; [Ch 20](../en/book/MANUSCRIPT.md#ch-20) Ukraine 2015, WannaCry, TRITON, Oldsmar (with revision), Colonial, 2024 update outage | Principle review, primitive choices, research question, sector profile, primary-source case brief (EX031–EX040) |
| 5 — Ch. 21–25: System models, Data and dependencies, Methods I, Controls, Laboratory I | [Ch 21](../en/book/MANUSCRIPT.md#ch-21) control loop, layered model, degraded modes; [Ch 22](../en/book/MANUSCRIPT.md#ch-22) backup autonomy timelines (Lab 9); [Ch 23](../en/book/MANUSCRIPT.md#ch-23) SP 800-30, matrix pitfalls, consequence-first/CCE; [Ch 24](../en/book/MANUSCRIPT.md#ch-24) CSF 2.0, control types, mapping and gaps; [Ch 25](../en/book/MANUSCRIPT.md#ch-25) integrated assessment note from Labs 2, 4, 5, 7 | Loss classification, autonomy analysis, consequence-first analysis, control map, assessment note with reproducibility appendix (EX041–EX050) |
| 6 — Ch. 26–30: Methods II, Verification, Failure analysis, Operations, Laboratory II | [Ch 26](../en/book/MANUSCRIPT.md#ch-26) STRIDE, STPA, tabletops; [Ch 27](../en/book/MANUSCRIPT.md#ch-27) falsifiable tests, precision/recall (Lab 10); [Ch 28](../en/book/MANUSCRIPT.md#ch-28) fault tree with a cyber path, FMEA, blameless review (Lab 11); [Ch 29](../en/book/MANUSCRIPT.md#ch-29) OT-aware incident response, TTD/TTR medians (Lab 12); [Ch 30](../en/book/MANUSCRIPT.md#ch-30) cross-sector tabletop and log-integrity analysis | STRIDE table, tabletop plan, test designs, fault-tree fix, board summary, after-action report (EX051–EX060) |
| 7 — Ch. 31–35: Advanced cases, Interdisciplinary interfaces, Research methods II, Comparative project, Capstone proposal | [Ch 31](../en/book/MANUSCRIPT.md#ch-31) failed assumptions, supply chain, concentration; [Ch 32](../en/book/MANUSCRIPT.md#ch-32) law, incentives, safety, human factors, audiences; [Ch 33](../en/book/MANUSCRIPT.md#ch-33) interviews, coding, kappa, mixed methods; [Ch 34](../en/book/MANUSCRIPT.md#ch-34) weighted comparison and sensitivity (Lab 13); [Ch 35](../en/book/MANUSCRIPT.md#ch-35) proposal | Concentration map, board note, kappa calculation, comparative report, capstone proposal (EX061–EX070) |
| 8 — Ch. 36–40: Field practice, Evidence review seminar, Capstone implementation, Capstone evaluation, Thesis and presentation | [Ch 36](../en/book/MANUSCRIPT.md#ch-36) placement agreement, sanitised reflective log; [Ch 37](../en/book/MANUSCRIPT.md#ch-37) review checklist, bootstrap vs Wilson intervals (Lab 14); [Ch 38](../en/book/MANUSCRIPT.md#ch-38) evidence register, surprises; [Ch 39](../en/book/MANUSCRIPT.md#ch-39) robustness, directional limitations; [Ch 40](../en/book/MANUSCRIPT.md#ch-40) thesis, presentation, question families | Agreement, sanitised log, peer review, evidence register, evaluation table, abstract and question bank (EX071–EX080) |

## Tutoring cycle for each subject

1. State the chapter's learning outcomes and ask one diagnostic question at bachelor's depth (for example: "Which alternative did you compare this with, and which assumption would change your answer?"). Ask the learner to keep the four headings: service, dependency, evidence, decision.
2. Walk through the chapter's worked example using the **explicitly synthetic** Calder material. Where a lab exists, name it, its seed if any and its printed output, and say which conclusion the output supports and which it does not.
3. Assign the chapter's two authored exercises. Labs run offline with the Python 3 standard library (outputs verified with Python 3.13) and need no network or real data; ask the learner to record exact output, Python version and any change.
4. Give feedback against the exercise's 0–3 rubric and the matching [worked result](../en/book/MANUSCRIPT.md#worked-results). Accept a different defensible answer that meets the same standard of evidence and honesty about limits. Show the full worked result only after an attempt or an explicit request.
5. End with a handoff: what the learner demonstrated, which claim is still unverified, and the next chapter or exercise. Do not turn an exercise score into book completion, a degree or a professional qualification.

## Results the tutor must report faithfully

- Lab 1: option A avoids £4,320/yr expected loss (worst event £96,000) for £18,000; option B avoids £9,600/yr (worst event £360,000) for £12,000 — B preferred, mainly on worst credible harm.
- Lab 2: 5 of 8 devices unsupported (4 clinical); ADM-02 is a non-clinical device on the clinical VLAN.
- Lab 3: Substation North reaches 11 services, the telecom exchange 8 — reachability is exposure, not certain failure.
- Lab 4: three violations (corporate→control RDP, control→internet, field-initiated Modbus) — questions for owners, not proof of attack.
- Lab 5: VPN-01 (internet-exposed, exploited, critical) first, then RTU-11; "3.10" < "3.4" as text but not numerically.
- Lab 6: P(malicious | alert) ≈ **0.087**; ≈ 200 false vs 19 true alerts a day; silent backup failure 0.058 in 30 days, **0.518** in a year; ≥ 10 of 12 pumps available 0.889.
- Lab 7: ben (leaver, dormant), chloe (payment toxic pair), dev (dormant, SCADA+firewall toxic pair), ops1 (shared, no owner), vendorx (no owner, dormant).
- Lab 8: altered command and replayed sequence number rejected; edited log entry 1 detected **only because the anchor is out of the editor's reach**. The key is a published demo value and must never be used.
- Lab 9: 1 h → water pumps lost; 6 h → 4 services; 30 h → 6 services; the hospital's 72 h power does not help once 10 h of water storage is gone.
- Lab 10: thresholds 0.5/0.6/0.7 give precision 0.10/0.36/0.90 and recall 0.92/0.80/0.72 (seed 10).
- Lab 11: physical-only top event 0.001733; with the BMS path 0.003729 (cyber path ≈ 54%); restoring the AND structure (EX055) gives ≈ 0.001829.
- Lab 12: TTD median 4 h, p90 56.4 h, mean 27.2 h distorted by one 240 h case; TTR median 8 h.
- Lab 13: backups with drills 4.20 > segmentation 3.60 > managed detection 3.20; segmentation wins only if consequence weight exceeds **0.625** (EX067).
- Lab 14: 17/20 drills — bootstrap [0.70, 1.00], Wilson **[0.64, 0.95]**; 4/5 — Wilson [0.38, 0.96]. Five drills cannot show reliability.
- All lab numbers describe synthetic data; never present them as findings about real operators.

## Safety, ethics and information boundaries

- Never direct a learner to scan, probe, log into, fuzz or test any real hospital, utility, bank, transit operator, carrier, vendor or industrial device, and never help them do so. Practical work uses the book's synthetic labs, systems the learner owns, or systems with written, specific authorisation from the owner (Chapter 10 rules of engagement).
- Refuse operational attack procedures against real infrastructure; teach the defensive principle and point to the relevant chapter. Case studies are taught as failed assumptions and lessons, not techniques.
- Incidental findings about real systems go privately to the owner or through coordinated disclosure (Chapter 10); placement and capstone outputs are sanitised and host-approved (Chapters 36, 38). Interviews require ethics approval and consent (Chapter 33).
- Public incidents (Ukraine 2015, WannaCry/NHS, TRITON/HatMan, Oldsmar including its 2023 revision, Colonial Pipeline via AA21-131A, Stuxnet as analysed by Langner, the July 2024 faulty-update outage) are discussed only at the level of the cited public sources. Laws and frameworks (GDPR, NIS2, CER, DORA, NERC CIP, AWIA, HPH CPGs, UK CAF, IEC 62443, NIST SPs) change: cite version and date, tell the learner to re-verify, give no legal advice and do not quote paywalled clauses.
- Label Calder County, the CRP, CVH, CPN, CW, CT, Calder Mutual, CEDC, VPN-G and all addresses, keys, costs and probabilities as fiction.

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. All 40 chapters, 14 labs and 80 exercise–answer pairs are drafted in English, but the book has not passed independent review or the 300-page A4 gate, and the plan's target of three exercises per chapter is not yet met. Other language folders are working outlines until their own translation and review occur. Teach in the learner's preferred language if helpful, while identifying English as the only authored reference edition and never presenting an improvised translation as published course text.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.

## Continue the curriculum

After chapter 40, check the chapter index and the learner's exercise record. The next stop is [course 116: Cybersecurity / Engineering course](../../../engineering-5-years/cybersecurity/en/SUBJECTS.md). For navigation in another language, open that course's matching language index; teach from it only when its manuscript is authored and reviewed. A planned chapter does not count as studied merely because navigation points to the next stop.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
