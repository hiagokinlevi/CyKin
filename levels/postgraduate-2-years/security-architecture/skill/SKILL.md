---
name: oca-security-architecture-postgraduate-008471f8
description: "Guide a learner through the ARCH Postgraduate Course draft: 12 chapters, stdlib labs and EX001–EX060 with worked answers."
license: CC0-1.0
---

# Security architecture and engineering — Postgraduate course course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 12 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 145, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/security-architecture/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Twelve-chapter postgraduate route

This is the two-year **postgraduate course** in security architecture and engineering. The book follows synthetic architect **Priya Ramanathan**, supervised by **Dr Elena Voss** at the fictional **Brookmere University**, leading architecture at the fictional **Corvane Health Network**.

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–4 | Decision-making, current practice, specialist evidence, risk and ethics | lab_reach.py (3); EX001–EX020 |
| 5–8 | Design alternatives, controlled pilot, organisational integration, difficult cases | lab_options.py (5); EX021–EX040 |
| 9–12 | Leadership and assurance, research critique, applied project, final transfer | lab_assure.py (9), lab_rubric.py (11); EX041–EX060 |

Verified lab facts (synthetic unless cited): admin zone reaches clinical devices via the print server before segmentation, not after; hybrid scores 4.10 versus cloud 3.75, cloud wins only at availability weight 0.20 or lower; 40 controls: 36 designed, 29 implemented, 19 verified; rubric totals 11/15 for both self and assessors.

## Teaching guardrails

- Labs run standard-library code on synthetic data only; they model, count and check, and never probe real systems. Architecture advice must cite real standards and name its limits.
- Test or review only systems with written authorisation; report found secrets by location, never by value; never present a framework as proof of outcomes.

## Continue the curriculum

After chapter 12, the next stop is [course 146: Cryptography and trust services / Postgraduate course](../../cryptography-trust/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
