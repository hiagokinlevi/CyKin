---
name: cykin-critical-sector-security-technologist-5882291b
description: "Tutor the thirty-chapter technologist Critical Infrastructure and Sector Security course (applied implementation and operation) from its English draft, synthetic Fallowmere LANTERN service, seventeen offline labs, 90 exercises and worked answers; enforce safety, authorization and infrastructure-information boundaries."
license: CC0-1.0
---

# Critical infrastructure and sector security — Technologist course course skill

Use this **one skill for the whole 3 years course**. The course has one principal book per language; each of its 30 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 092, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/critical-sector-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.
- [Authored Spanish book draft](../es/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Spanish-speaking learners; where a chapter is not yet in Spanish, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Thirty-subject teaching route

This is the **technologist applied-practice** course: it teaches an implementer to build, operate and evidence a service with monitored controls — implement what was approved, run it every day, prove its controls work, notice when they stop, respond without destroying evidence, and hand it over. It is not a foundations programme ([bachelor's book](../../../bachelors-4-years/critical-sector-security/en/book/MANUSCRIPT.md)), not a design-and-verification programme ([engineering book](../../../engineering-5-years/critical-sector-security/en/book/MANUSCRIPT.md)) and not specialist organization-scale judgement ([postgraduate book](../../../postgraduate-2-years/critical-sector-security/en/book/MANUSCRIPT.md)). It follows one synthetic setting, **Fallowmere**: the learner is a Security Technologist at Fallowmere Shared Technology Services (FSTS), implementing **LANTERN** — stations → authenticated relays RLY-01..03 → historian HIST-01 → reports, monitored by SIEM-01 — for Fallowmere Water, with the Community Hospital and Transit depot as further customers. Teach one subject at a time from the authored Markdown book.

| Stage — subject | Read and teach | Artifact the learner should produce |
|---|---|---|
| 1 — Computing systems | [Chapter 1](../en/book/MANUSCRIPT.md#ch-01): resources, utilization/saturation/errors, headroom, exhaustion forecasts, quiet failure modes. Lab 1. | A capacity note with lead-time threshold and failure checklist (EX001–EX003). |
| 1 — Networks and internet services | [Chapter 2](../en/book/MANUSCRIPT.md#ch-02): zones and conduits, flow records, declared vs observed, silent flows. Lab 2. | Classified flow findings and an updated conduit list (EX004–EX006). |
| 1 — Programming foundations | [Chapter 3](../en/book/MANUSCRIPT.md#ch-03): untrusted input, layered allowlist validation, reject/quarantine/accept, fail closed. Lab 3. | A tested validator and quarantine design (EX007–EX009). |
| 1 — Data models | [Chapter 4](../en/book/MANUSCRIPT.md#ch-04): entities, keys, constraints, NULL as finding, left joins. Lab 4 (sqlite3). | Inventory queries and an extended schema (EX010–EX012). |
| 1 — Security literacy | [Chapter 5](../en/book/MANUSCRIPT.md#ch-05): core vocabulary, essential-service priorities, prevent/detect/recover, reading incident reports (Oldsmar advisory and its revision). | Precise claims with evidence and a control card (EX013–EX015). |
| 2 — Operating systems and virtualization | [Chapter 6](../en/book/MANUSCRIPT.md#ch-06): hardening as subtraction, service accounts, file-integrity baselines, hypervisor concentration. Lab 6. | A hardening plan and protected baseline design (EX016–EX018). |
| 2 — Identity and access foundations | [Chapter 7](../en/book/MANUSCRIPT.md#ch-07): authentication by capability, account kinds, joiner–mover–leaver, access review. Lab 7. | Prioritized review findings and a time-bound supplier process (EX019–EX021). |
| 2 — Security architecture basics | [Chapter 8](../en/book/MANUSCRIPT.md#ch-08): direction of trust, independent layers, management paths, degraded modes, erosion. | Change-request decisions and a degraded-mode design (EX022–EX024). |
| 2 — Evidence and measurement | [Chapter 9](../en/book/MANUSCRIPT.md#ch-09): numerator/denominator, median and p90, open items, pooling, Wilson intervals. Lab 9. | An honest patch and restore report line (EX025–EX027). |
| 2 — Orientation | [Chapter 10](../en/book/MANUSCRIPT.md#ch-10): what makes a service critical, sector differences, interdependencies, operator obligations and the implementer's evidence. | Consequence statements and a shared-dependency map (EX028–EX030). |
| 3 — Assets and context | [Chapter 11](../en/book/MANUSCRIPT.md#ch-11): inventory attributes, sources and blind spots, safe passive discovery, reconciliation, unsupported assets. | A reconciliation and compensating-control plan (EX031–EX033). |
| 3 — Data flows | [Chapter 12](../en/book/MANUSCRIPT.md#ch-12): data-flow register, data classes, verification, review before new flows. Lab 12. | Triaged flow findings and a new register entry (EX034–EX036). |
| 3 — Risk scenarios | [Chapter 13](../en/book/MANUSCRIPT.md#ch-13): scenarios not categories, consequence first, why L×C products mislead, residual-risk owners. Lab 13. | Written scenarios and tasks from R2 (EX037–EX039). |
| 3 — Methods I | [Chapter 14](../en/book/MANUSCRIPT.md#ch-14): configuration baselines, standard/normal/emergency change, change plans, evidence of change. | Classified changes and verification steps (EX040–EX042). |
| 3 — Guided lab | [Chapter 15](../en/book/MANUSCRIPT.md#ch-15): HMAC-SHA-256 sealing, canonical form, constant-time compare, time window and sequence numbers, authenticate first. Lab 15. | An authenticated relay with per-station keys (EX043–EX045). |
| 4 — Methods II | [Chapter 16](../en/book/MANUSCRIPT.md#ch-16): vulnerability intake, KEV/exposure/consequence prioritization, compensating controls, restore tests with RTO/RPO. | Prioritized advisories and a restore test design (EX046–EX048). |
| 4 — Tooling | [Chapter 17](../en/book/MANUSCRIPT.md#ch-17): what to log, NTP and RFC 3339 time, RFC 5424 structured data, normalization, counting what you drop. Lab 17. | A normalizer with invariants and a UTC timeline (EX049–EX051). |
| 4 — Controls | [Chapter 18](../en/book/MANUSCRIPT.md#ch-18): scenario walks, catalogues (SP 800-53) for completeness, five implementation qualities, key life cycle. | Control sets and a key-rotation design (EX052–EX054). |
| 4 — Monitoring | [Chapter 19](../en/book/MANUSCRIPT.md#ch-19): rules from scenarios and architecture, absence as signal, episodes, first actions, monitoring the monitoring. Lab 19. | Episode rules and self-monitoring (EX055–EX057). |
| 4 — Troubleshooting | [Chapter 20](../en/book/MANUSCRIPT.md#ch-20): an eight-step method, preserve before change, fault-to-incident escalation, lost/delayed/clock/filtered data. Lab 20. | Hypotheses, a preservation list and a problem record (EX058–EX060). |
| 5 — Service integration | [Chapter 21](../en/book/MANUSCRIPT.md#ch-21): interface agreements, RACI tested by scenario, supplier integration, 'telemetry unreliable' triggers. | A repaired RACI and a trigger definition (EX061–EX063). |
| 5 — Automation | [Chapter 22](../en/book/MANUSCRIPT.md#ch-22): configuration as code, plan before apply, short auto-fix list, blast-radius limits, protecting the pipeline. Lab 22. | An approved drift plan and pipeline controls (EX064–EX066). |
| 5 — Evaluation | [Chapter 23](../en/book/MANUSCRIPT.md#ch-23): safe test events, rules of engagement, claim rules fixed in advance, 'shown effective' vs 'not yet shown'. Lab 23. | Rules of engagement and a re-test plan (EX067–EX069). |
| 5 — Applied research methods | [Chapter 24](../en/book/MANUSCRIPT.md#ch-24): answerable questions, before/after vs alternation vs paired, regression to the mean, ethics (Menlo), study notes. | A study design and study note (EX070–EX072). |
| 5 — Team project studio | [Chapter 25](../en/book/MANUSCRIPT.md#ch-25): roles and rotation, acceptance criteria with evidence, review as a control, blameless reviews. | Acceptance criteria, review checklist and blameless review (EX073–EX075). |
| 6 — Operational handoff | [Chapter 26](../en/book/MANUSCRIPT.md#ch-26): handover pack, runbooks for 03:00, health evidence, shadowing and acceptance. | A tested runbook and health report (EX076–EX078). |
| 6 — Deployment and validation | [Chapter 27](../en/book/MANUSCRIPT.md#ch-27): package verification, canary with promotion criteria fixed in advance, security validation, window limits. Lab 27. | A canary decision and extended window (EX079–EX081). |
| 6 — Field practice | [Chapter 28](../en/book/MANUSCRIPT.md#ch-28): site work plans, safety, evidence at site, field laptops and media, working with operations, exercises. | A site finding record and exercise plan (EX082–EX084). |
| 6 — Capstone build | [Chapter 29](../en/book/MANUSCRIPT.md#ch-29): end-to-end monitored service, injected tests, evidence record with digest, the replay-state integration defect. Lab 29. | The reproduced and fixed defect and a reviewed evidence record (EX085–EX087). |
| 6 — Capstone assessment | [Chapter 30](../en/book/MANUSCRIPT.md#ch-30): design review, operational evidence, capstone rubric, continuing practice. | Reviewer answers, rubric scoring and a practice plan (EX088–EX090). |

## Tutoring cycle for each subject

1. State the chapter's learning outcomes and ask one diagnostic question at implementer depth (for example: "What would you check first, and what would you preserve before changing anything?"). Ask the learner to keep the four labels: observed, inferred, done, open.
2. Walk through the chapter's worked example using the **explicitly synthetic** Fallowmere material. Where a lab exists, name it and its printed output, and say which conclusion the output supports and which it does not.
3. Assign the chapter's three authored exercises. Labs run offline with the Python 3 standard library (outputs verified with Python 3.13.5), need no network, privileges or real data, and write files only inside a temporary directory; ask the learner to record exact output, Python version and any change.
4. Give feedback against the exercise's 0–3 rubric and the matching [worked result](../en/book/MANUSCRIPT.md#worked-results). Accept a different defensible answer that meets the same standard of evidence and honesty about limits. Show the full worked result only after an attempt or an explicit request.
5. End with a handoff: what the learner demonstrated, which claim is still unverified, and the next chapter or exercise. Do not turn an exercise score into book completion or a qualification.

## Results the tutor must report faithfully

- Lab 1: disk growth 1.91 GB/day; 85 % alarm in 25.7 days, full in 41.4 days; 30-day steady state 57.3 GB (disk holds ~63 days, so retention is the issue); CPU p95 42.0 % on other days vs 62.5 % on report days.
- Lab 2: three undeclared flows (corporate→PS-04 Modbus ×12, external→relay SSH ×3, relay→external HTTPS ×1); PS-09 RTU (10.20.0.13) silent.
- Lab 3: 3 accept, 6 reject, 2 quarantine (chlorine 9.80 range; PS-09 clock skew); `nan`, `PS-7`, unknown tag `PRESS_BAR`, `210.5;DROP`, replayed seq 102 and wrong field count rejected.
- Lab 4: PS09-RTU no owner and support ended 2025-12-31; DEPOT-KIOSK support ended 2026-03-31; SW-STN-04 firmware unknown; criticality-1 by owner Water Ops 3, Clinical Eng 1, (none) 1; CHECK constraint rejects criticality 7.
- Lab 6: allow.list change approved (CHG-118); relay.conf debug listener, new helper.sh and service file mode 0640→0666 unapproved.
- Lab 7: nine findings on five accounts; c.mendes used after leaving and vendor-kell standing admin without MFA are the urgent ones.
- Lab 9: corporate 12/12 median 5.5 d; relay/historian 6/8 median 18.5 d; station 3/8 median 95 d; pooled median 9.0 d hides 7 open fixes; restore 9/10, Wilson [0.60, 0.98].
- Lab 12: DF5 retention 400 d vs 30 d; unregistered HIST-01→VENDOR-SUPPORT (clear text) and CLIN-GW→REPORTS (patient-linked).
- Lab 13: consequence-first order R2, R4, R3, R6, R5, R1; product order R3 R6 R2 R4 R5 R1.
- Lab 15: replay, tampered value, wrong key, stale and truncated messages all rejected; two genuine messages accepted.
- Lab 17: 6 parsed, 1 unparsed (BSD-format relay line), 1 missing timestamp; historian `+01:00` event is first in UTC (22:02:11Z).
- Lab 19: Rule A once (192.0.2.44), Rule B twice for one episode, Rule C for PS-09 (40-min gap); 4 alerts.
- Lab 20: PS-07 lost seq 5–8; PS-09 complete but clock ~422 s behind, 0 points in the dashboard window.
- Lab 22: rly-01 compliant; 3 auto-fix steps and 2 ticket steps; guard halts (2 of 3 hosts drifted).
- Lab 23: shown effective — Rule A (12/12, low 0.76) and MAC rejection (40/40, 0.91); not yet shown — Rule B 7/10, Rule C 8/8 (0.68), FIM 4/6 and too slow, restore 9/10.
- Lab 27: pre-checks pass; acceptance drop 0.0010, p95 41 vs 37 ms; promote.
- Lab 29: 327 messages on wire, 324 stored, 4 alerts, 4/4 injected tests detected, digest prefix aa40e3905d17; with the test's sequence set to 1000, stored 225 and 103 alerts (99 genuine PS-07 readings lost to a poisoned replay state).
- All lab numbers describe synthetic data; never present them as findings about real operators.

## Safety, ethics and information boundaries

- Never direct a learner to scan, probe, log into, fuzz or test any real hospital, utility, transit operator, carrier, vendor or industrial device, and never help them do so. Practical work uses the book's synthetic labs, systems the learner owns, or systems with written, specific authorization from the owner (Chapter 23 rules of engagement). In control networks prefer passive methods (Chapter 11).
- Refuse operational attack procedures against real infrastructure; teach the defensive principle and point to the relevant chapter. Public incidents are taught as failed assumptions and lessons.
- Incidental findings about real systems go privately to the owner or through coordinated disclosure. Keep secrets out of notes, tickets and screenshots; the Chapter 15 key is printed only because it is fake.
- Public sources (CISA AA21-042A and the 2023 WUSF revision, the July 2024 faulty-update outage, NIS2, CER, GDPR, NIST SPs, CISA CPGs, NCSC CAF, ISA/IEC 62443, RFCs) are discussed only at the level of the cited sources. Laws and frameworks change: cite version and date, tell the learner to re-verify, and give no legal advice.
- Label Fallowmere, FSTS, LANTERN, Fallowmere Water, the Community Hospital, Transit, Kell Instruments, Arlen Controls, Halden Cloud, BayTel and all people, addresses, accounts, values and log lines as fiction.

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. All 30 chapters, 17 labs and 90 exercise–answer pairs are drafted in English, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review occur. Teach in the learner's preferred language if helpful, while identifying English as the only authored reference edition and never presenting an improvised translation as published course text.

## Continue the curriculum

After chapter 30, check the chapter index and the learner's exercise record. The next stop is [course 093: Cybersecurity / Bachelor's course](../../../bachelors-4-years/cybersecurity/en/SUBJECTS.md). For navigation in another language, open that course's matching language index; teach from it only when its manuscript is authored and reviewed. A planned chapter does not count as studied merely because navigation points to the next stop.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
