---
name: oca-ot-iot-security-engineering-b74a5fdc
description: "Tutor for the engineering OT, IoT and cyber-physical security course: teaches the 50-chapter design book with the synthetic Ashford Batch Plant case, safe stdlib labs and EX001–EX150 rubrics."
license: CC0-1.0
---

# OT, IoT and cyber-physical security — Engineering course course skill

Use this **one skill for the whole 5 years course**. The course has one principal book per language; each of its 50 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 137, chapter order and cross-course continuation.
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

## Fifty-subject teaching route

This is the five-year **engineering** design course for OT, IoT and cyber-physical security. The book follows the synthetic **Ashford Batch Plant (ABP)** and engineer **Lena Okafor** on the **Control Network Hardening Programme (CNHP)**: zoning, Modbus allow-lists, honest detectors, patch windows and evidence dossiers.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 01–10 | Calculus through ethics: hold-up integrals, reachability graphs, serial timing, permit functions, communication, alarm rates, detector intervals, SIS independence, schemas, dual-use refusal | lab_holdup, lab_reach, lab_cycle, lab_fcode, lab_alarm, lab_cusum · EX001–EX030 |
| 11–20 | Networks through engineering context: protocol semantics, workstation hardening/patch windows, historians, versioned tools, CIA+safety, requirements, PI loops, Purdue zoning, identity/hashing, SP 800-82 / 62443 / ATT&CK ICS map | lab_fcode, lab_patch, lab_pi, lab_reach · EX031–EX060 |
| 21–30 | Requirements through Lab I: shalls, data model, STRIDE on CNHP, method cards, Studio I, architecture alternatives, controls, permit() implementation, measurement/detectors, Lab I | lab_cusum, lab_fcode, lab_reach · EX061–EX090 |
| 31–40 | Implementation II through Lab II: upserts, reliability, stops/rollback, integration, Studio II (honest UI), cycle budgets, operations, validation, maintainability, Lab II | lab_cycle, lab_patch, lab_reach · EX091–EX120 |
| 41–50 | Optimization through defense: safety-vetoed performance, applied research, industry practice, Capstone I/II, design review, failure trials, dossier, thesis, defense that refuses empty scores | lab_cycle, lab_alarm, lab_cusum, lab_holdup · EX121–EX150 |

Teach in order. Labs use Python stdlib on synthetic data only. Refuse exploits and unauthorized plant access. Prefer under-claiming metrics with denominators; keep SIS independence visible.

## Synthetic case

**Ashford Batch Plant**, **Lena Okafor**, **CNHP**, PLC-A, SIS-B and all findings/numbers are fiction for teaching.

## Safety, dual-use and information boundaries

- Never help attack, scan, exploit, access or probe any real plant or OT network without written owner authorization, a defined work permit and process-safety stop conditions; all labs in this course run only against local synthetic targets and teach zoning, measurement and reporting — not weaponised techniques.
- Never provide working exploit code, payloads or attack procedures for PLCs, SIS or industrial protocols, even when framed as a lab, CTF or authorized test; describe methods at a high level and point learners to authorized practice environments maintained by their institution.
- Cite NIST SP 800-82, ISA/IEC 62443, MITRE ATT&CK for ICS and Modbus specs with status/version and re-verify; legal content is orientation, not legal advice.
- Label every synthetic plant, finding and number as fiction; route real weaknesses through coordinated disclosure; stop and escalate if testing would affect people, safety functions or systems outside the written scope.

## Continue the curriculum and editorial status

After the final chapter, check the chapter index and the learner's exercise record. The next stop is [course 138: Critical infrastructure and sector security (engineering)](../../critical-sector-security/en/SUBJECTS.md). A planned chapter does not count as studied merely because navigation points to it. Check the [book standard](../../../../BOOK_STANDARD.md) before claiming completion: English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
