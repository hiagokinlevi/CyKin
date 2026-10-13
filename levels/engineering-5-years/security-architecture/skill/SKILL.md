---
name: cyberabc-security-architecture-engineering-80b397da
description: "Guide a learner through the ARCH Engineering Course draft: 50 chapters, stdlib labs and EX001–EX150 with worked answers."
license: CC0-1.0
---

# Security architecture and engineering — Engineering course course skill

Use this **one skill for the whole 5 years course**. The course has one principal book per language; each of its 50 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 122, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/security-architecture/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Fifty-chapter engineering route

This is the five-year **engineering course** in security architecture and engineering. The book follows synthetic student **Sofia Mbeki** of the fictional **Kestrel Polytechnic University**, mentored by architect **Daniel Ferreira** at the fictional **Corvia Regional Transit**, from foundations to a fare back-office capstone.

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–19 | Mathematics, physics, programming, communication, ethics, networks, OS, data, software engineering, fundamentals, systems engineering, control, architecture, identity and cryptography | lab_growth (1), lab_closure (2), lab_exposure (6), lab_bayes (7), lab_sqli (13), lab_feedback (17); EX001–EX057 |
| 20–34 | Context, requirements, models, threat and fault analysis, risk methods, studio I, alternatives, control design, implementation, measurement, verification lab I, reliability, resilience, integration | lab_fta (23), lab_metrics (29), lab_ingest (30), lab_avail (32); EX058–EX102 |
| 35–50 | Studio II, scale, operations, validation, maintainability, verification lab II, optimisation, applied research, practice, capstone, review, recovery trial, dossier, thesis, defense | lab_bucket (36), lab_flows (40), lab_knapsack (41), lab_recovery (47), lab_dossier (48); EX103–EX150 |

Verified lab facts (synthetic unless cited): storage budget exceeded month 24 (linear forecast 39); dina holds create and approve; misuse 12.6 vs 3.1 uses/day; P(fraud|flag)=0.045; injection 4 rows vs 0; gain 2.5 oscillates (9 changes); fault-tree top 0.0090/day; revocation median 8 d, 3 of 20 never; ingestion accepts only the authentic record; availability 0.9960 to 0.9980; bucket 200 vs 20 rejects 20 vs 200; flows: 2 excess, 1 missing; greedy 63 vs optimum 74; recovery 325 min vs 240 objective.

## Teaching guardrails

- Labs run standard-library code on synthetic data only; they model, count and check, and never probe real systems. Architecture advice must cite real standards and name its limits.
- Test or review only systems with written authorisation; report found secrets by location, never by value; never present a framework as proof of outcomes.

## Continue the curriculum

After chapter 50, the next stop is [course 123: Cryptography and trust services / Engineering course](../../cryptography-trust/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
