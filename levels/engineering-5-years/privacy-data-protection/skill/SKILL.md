---
name: cyberabc-privacy-data-protection-engineering-846e642b
description: "Guide a learner through the privacy Engineering Course draft: 50 chapters, stdlib labs and EX001–EX150 with worked answers."
license: CC0-1.0
---

# Privacy and data protection — Engineering course course skill

Use this **one skill for the whole 5 years course**. The course has one principal book per language; each of its 50 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 119, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/privacy-data-protection/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Fifty-chapter engineering route

This is the five-year **engineering course** in privacy and data protection. The book follows synthetic student **Zara Mbeki**, supervised by **Prof. Anders Holm** at the fictional **Corwen Polytechnic**, engineering privacy into the fictional **Pellmore Telehealth** platform.

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–10 | Foundations read through privacy, randomised response and ethics | lab_rr (7); EX001–EX030 |
| 11–20 | Networks, systems, data, software, security, architecture, identity and legal context | lab_retention (13); EX031–EX060 |
| 21–30 | Requirements, flow models, threats, DPIA, studio, architectures, controls, implementation, measurement, verification | lab_flow (22), lab_dpia (24), lab_minimise (29); EX061–EX090 |
| 31–40 | Portability, erasure reliability, resilience, integration, studio, privacy budgets, operations, validation, maintainability, adversarial testing | lab_erasure (32), lab_budget (36); EX091–EX120 |
| 41–50 | Optimisation, research, practice, capstone, review, breach trial, dossier, thesis and defense | lab_breach (47), lab_dossier (48); EX121–EX150 |

Verified lab facts (synthetic unless cited): randomised response estimate 0.189 (CI 0.147–0.231), SE 0.021 vs 0.009; 262 of 400 records past retention (video 96/101); 3 of 7 flows need action; DPIA residual: vendor breach medium 6, no high; 8 of 18 fields (44%) unneeded; erasure 0.825 → 0.987 with one retry; yearly epsilon 3: monthly error 4.0, daily 121.7; breach notified 44 h after awareness, vendor delay 35.5 h; dossier erasure_test.log MISMATCH.

## Teaching guardrails

- Labs run standard-library code on synthetic data only; they score, simulate and check, and never probe real systems. Records and people are invented; no real personal data is processed.
- Cite laws by article and standards by edition; paraphrase rather than reproduce copyrighted standard text. Legal analysis here is teaching, not legal advice, and a synthetic DPIA or audit is never presented as a real regulatory decision.

## Continue the curriculum

After chapter 50, the next stop is [course 120: Security governance, risk and compliance / Engineering course](../../security-governance-risk-compliance/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
