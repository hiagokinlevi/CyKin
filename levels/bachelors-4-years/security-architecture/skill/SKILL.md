---
name: cyberabc-security-architecture-bachelor-7d649956
description: "Guide a learner through the ARCH Bachelor's Course draft: 40 chapters, stdlib labs and EX001–EX120 with worked answers."
license: CC0-1.0
---

# Security architecture and engineering — Bachelor's course course skill

Use this **one skill for the whole 4 years course**. The course has one principal book per language; each of its 40 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 099, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/security-architecture/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Forty-chapter bachelor's route

This is the four-year **bachelor's course** in security architecture and engineering. The book follows synthetic student **Lucas Haddon**, tutored by **Dr Marco Bellini** at the fictional **Ashgrove University**, on placement with **Hannah Osei** at the fictional **Fernway Outdoor Co-operative**.

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–14 | Mathematics, computing, networks, data, probability, privacy | lab_truth.py (1), lab_paths.py (6), lab_sample.py (12), lab_pseudo.py (14); EX001–EX042 |
| 15–24 | Measurement, architecture, cryptography concepts, research methods, scope, cases, models, dependencies, risk method, controls | lab_coverage.py (15), lab_deps.py (22); EX043–EX072 |
| 25–34 | Laboratories, attack trees, verification, failure analysis, operations, advanced and interdisciplinary cases, research methods II, comparative project | lab_excess.py (25), lab_detect.py (30), lab_did.py (33), lab_weighted.py (34); EX073–EX102 |
| 35–40 | Capstone proposal, field practice, evidence review, implementation, evaluation, thesis | EX103–EX120 |

Verified lab facts (synthetic unless cited): audit sample 26/200 with Wilson interval 9.0% to 18.4%; phishing-resistant coverage 47/81 with warehouse at 2/15; 3 of 7 users exceed job needs; 2-hour travel rule catches 4 of 4 with 0 false positives; DiD +0.29 reports per staff per month; weighted totals A 3.05, B 4.10.

## Teaching guardrails

- Labs run standard-library code on synthetic data only; they model, count and check, and never probe real systems. Architecture advice must cite real standards and name its limits.
- Test or review only systems with written authorisation; report found secrets by location, never by value; never present a framework as proof of outcomes.

## Continue the curriculum

After chapter 40, the next stop is [course 100: Cryptography and trust services / Bachelor's course](../../cryptography-trust/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
