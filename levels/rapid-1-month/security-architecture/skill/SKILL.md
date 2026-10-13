---
name: cyberabc-security-architecture-rapid-ada7b449
description: "Guide a learner through the ARCH Rapid Course draft: 4 chapters, stdlib labs and EX001–EX050 with worked answers."
license: CC0-1.0
---

# Security architecture and engineering — Rapid course course skill

Use this **one skill for the whole 1 month course**. The course has one principal book per language; each of its 4 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 007, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/security-architecture/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Four-chapter rapid route

This is the one-month **rapid course** in security architecture and engineering. The book follows synthetic learner **Leah Brennan**, taught by **Felix Ortega** at the fictional **Northgate Learning Centre**, working at the fictional **Saltmarsh Community Credit Union**.

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–2 | Foundations and decisions; scope, permission and safe practice | EX001–EX026 |
| 3–4 | Systems, data and dependencies; guided baseline lab and plan | lab_deps.py (3), lab_baseline.py (4); EX027–EX050 |

Verified lab facts (synthetic unless cited): identity provider supports 6 services and the service bureau 4; loan settings meet 4/7 baseline items before fixes and 7/7 after.

## Teaching guardrails

- Labs run standard-library code on synthetic data only; they model, count and check, and never probe real systems. Architecture advice must cite real standards and name its limits.
- Test or review only systems with written authorisation; report found secrets by location, never by value; never present a framework as proof of outcomes.

## Continue the curriculum

After chapter 4, the next stop is [course 008: Cryptography and trust services / Rapid course](../../cryptography-trust/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
