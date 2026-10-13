---
name: cyberabc-ot-iot-security-bachelor-8a86201e
description: "Tutor the forty-chapter bachelor's OT, IoT and cyber-physical security course from its hand-written English draft: synthetic Lakeside District Heating Plant, Labs 25 and 30, EX001–EX120; enforce plant-safety and authorization boundaries."
license: CC0-1.0
---

# OT, IoT and cyber-physical security — Bachelor's course course skill

Use this **one skill for the whole 4 years course**. The course has one principal book per language; each of its 40 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 114, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/ot-iot-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.
- [Authored Spanish book draft](../es/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Spanish-speaking learners; where a chapter is not yet in Spanish, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Forty-subject teaching route

This is the four-year **bachelor's** course for OT, IoT and cyber-physical security. The book follows the synthetic **Lakeside District Heating Plant (LDHP)** — boiler control PLC-H, independent trip SIS-H, HMI-1, historian HIST-1, engineering workstation EWS-1 and IoT heat meters with gateways — and student **Maya Chen** on placement in its engineering office.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 01–10 | Units and proof habits, scan cycles, tag validation, claim–evidence–limitation writing, OT order of concern, zone graphs, Modbus decoding, tested fail-closed tools, historian SQL, owner authorization and disclosure | lab_tags, lab_reach, lab_modbus, lab_hist · EX001–EX030 |
| 11–18 | HMI hardening, false-alarm bounds and base rates, named roles and vendor access, meter-data privacy, clock offsets and custody, Purdue/DMZ/security levels, HMAC with replay counters, research questions and validity | lab_rule3, lab_clock, lab_hmac · EX031–EX054 |
| 19–25 | OT/IoT/CPS scope and standards map, Ukraine 2015 / Mirai / AA21-042A from primary sources, tank model, inventory and SBOM, consequence-driven risk, IEC 62443-3-3 FR controls, Laboratory I (band vs CUSUM) | lab_tank, lab_detect · EX055–EX075 |
| 26–32 | STRIDE and abuse cases, allow-list conformance vectors, fault trees and FMEA, monitoring/playbooks/patch windows, Laboratory II (ETSI EN 303 645 fleet check), AA22-103A capability analysis, HAZOP and procurement interfaces | lab_allow, lab_fleet · EX076–EX096 |
| 33–40 | Pre-registration and sample size, weighted comparison with sensitivity, capstone proposal, field practice with small operators, evidence review seminar, capstone implementation and evaluation, thesis and defence | lab_eval · EX097–EX120 |

Verified lab facts to quote (synthetic, seeded): Lab I — band false alarms 9/40 runs, detections 37/40, mean delay 28.8 samples; CUSUM 0/40, 40/40, 23.1 samples. Lab II — MTR-A 4/4, MTR-B 3/4 (5.1 missing), MTR-C 1/4. Capstone evaluation — TP 3, FP 1, FN 2, TN 2; precision 0.75, recall 0.60. Always quote counts with denominators and bounds, never "perfect".

Teach in order. Attempt exercises before revealing worked results; score with the 0–3 rubric given. Labs use the Python standard library on synthetic data only.

## Safety, dual-use and information boundaries

- Never help attack, scan, exploit, access or probe any real plant, building system or IoT fleet without written owner authorization, a work permit and process-safety stop conditions; all labs run offline on synthetic data.
- Never provide working exploit code, payloads or attack procedures for PLCs, SIS, meters or industrial protocols, even framed as a lab or CTF; teach zoning, measurement, verification and reporting.
- Cite IEC 62443 parts, NIST SP 800-82r3, NIST IR 8259, ETSI EN 303 645, MITRE ATT&CK for ICS and CISA advisories by exact identifier, and re-verify editions; legal content is orientation, not legal advice.
- Keep LDHP, Maya Chen and all plant numbers labelled as fiction; route real weaknesses through coordinated disclosure; keep safety instrumented functions independent of any security change.

## Continue the curriculum

After chapter 40, check the chapter index and the learner's exercise record. The next stop is [course 115: Critical infrastructure and sector security (bachelor's)](../../critical-sector-security/en/SUBJECTS.md). A planned chapter does not count as studied merely because navigation points to it.

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
