---
name: cykin-security-architecture-technical-babc0539
description: "Guide a learner through the ARCH Technical Course draft: 18 chapters, stdlib labs and EX001–EX072 with worked answers."
license: CC0-1.0
---

# Security architecture and engineering — Technical course course skill

Use this **one skill for the whole 18 months course**. The course has one principal book per language; each of its 18 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 053, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/security-architecture/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Eighteen-chapter technical route

This is the eighteen-month **technical course** in security architecture and engineering. The book follows synthetic trainee **Nadia Kowalczyk**, taught by **Daniel Mercer** at the fictional **Harbourside Technical College**, on placement with **Grace Mwangi** at the fictional **Linden Dental Group**.

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–5 | Services, networks, accounts, scripting, scope and evidence | lab_backups.py (4); EX001–EX020 |
| 6–12 | System model, telemetry, failure modes, methods, configuration, verification, contained lab I | lab_fw.py (10), lab_spread.py (12); EX021–EX048 |
| 13–18 | Troubleshooting, automation, dependencies, documentation, contained lab II, supervised project | lab_drift.py (14), lab_signin.py (17); EX049–EX072 |

Verified lab facts (synthetic unless cited): Elmfield 4/7 backup nights ok; first rule draft passes 6/7 flow tests, split segments 7/7; simulated spread reaches 8 machines flat versus 3 segmented; Westcott drifts with WAN remote admin on; Rule B catches 3 attacks with 0 false alarms.

## Teaching guardrails

- Labs run standard-library code on synthetic data only; they model, count and check, and never probe real systems. Architecture advice must cite real standards and name its limits.
- Test or review only systems with written authorisation; report found secrets by location, never by value; never present a framework as proof of outcomes.

## Continue the curriculum

After chapter 18, the next stop is [course 054: Cryptography and trust services / Technical course](../../cryptography-trust/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
