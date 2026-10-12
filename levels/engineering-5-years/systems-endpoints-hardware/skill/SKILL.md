---
name: cyberabc-systems-endpoints-hardware-engineering-74cfa3e1
description: "SYS Engineering Course (50 ch / 150 ex)"
license: CC0-1.0
---

# Systems, endpoints and hardware security — Engineering course course skill

Use this **one skill for the whole 5 years course**. The course has one principal book per language; each of its 50 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 127, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/systems-endpoints-hardware/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Fifty-subject teaching route

This is the five-year **engineering course** for systems, endpoint and hardware security. The book follows synthetic student **Mateo Rossi** of the fictional **Ardmore Institute of Technology**, supervised by **Dr Hana Novak**, as he designs a hardened, self-restoring public PC service for the fictional **Fernhill Library Network** (IT lead **Marta Silva**) after a patron's personal files were found on a public PC.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–19 | Mathematics, physics, programming, communication, networks, OS, data, software and systems engineering, security, architecture, identity and cryptography | lab_binomial.py (7); EX001–EX057 |
| 20–30 | Context, requirements, boot-chain model, scenarios, hardening, studio, alternatives, control design, restore implementation, measurement, verification lab | lab_boot.py (22), lab_scenarios.py (23), lab_harden.py (24), lab_restore.py (28), lab_timing.py (29); EX058–EX090 |
| 31–40 | Application control, reliability, resilience, integration, studio II, scale, operations, validation, maintainability, verification lab II | lab_allow.py (31), lab_avail.py (32), lab_trace.py (38); EX091–EX120 |
| 41–50 | Optimisation, research, practice, capstone, review, trial, dossier, thesis, defense | EX121–EX150 |

Verified lab facts (synthetic): P(at least 1/3/5 of 300 restores fail) 0.700/0.120/0.008; 1 of 5 boot components mismatched (kiosk-policy); top scenario unauthorised software (16); image meets 8 of 10 hardening requirements; 2 session changes, 0 after restore; restore medians 6.3/9.2/5.3 min, 21/21 in window; 23 of 2,003 executions blocked (14 accessibility reader); downtime 756→21 PC-hours, availability 0.9965→0.9999; traceability 8 pass, 1 fail, 1 untested.

## Safety, privacy and information boundaries

- Synthetic configurations, records and data only; no exploit code, payloads, attack procedures or instructions for bypassing controls.
- Standard-library labs that only read synthetic records.
- Logs record system events, never patron content; accessibility is protected by audit-before-enforce; tests run on lab PCs or agreed trials outside opening hours.

## Continue the curriculum

After chapter 50, the next stop is [course 128: Cloud and container security / Engineering course](../../cloud-containers/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
