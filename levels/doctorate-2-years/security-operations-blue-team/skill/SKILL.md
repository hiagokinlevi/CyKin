---
name: cyberabc-security-operations-blue-team-doctorate-61f8c1a0
description: "Doctoral research track (2 years)"
license: CC0-1.0
---

# Security operations and blue team — Doctoral research track course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 8 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 199, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/security-operations-blue-team/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Eight-subject teaching route

This is the two-year **doctoral research track** for security operations and blue team. The book follows synthetic doctoral candidate **Nadia Ferreira** of the fictional **Calder University**, supervised by **Prof. Elias Grant**, through one research project with the fictional **Northgate Shared SOC**: a controlled crossover experiment on whether context-enriched alert cards improve analyst triage, and where enrichment misleads.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–2 | Research integrity, constructs, the research frontier (base rates, alarm quality) | lab_baserate.py (2); EX001–EX014 |
| 3–4 | Contribution proposal, detection replay, baseline replication, label reliability, pilot | lab_replay.py (3), lab_kappa.py (4); EX015–EX026 |
| 5–6 | Main study with intervals, independent validation, peer critique and revision | lab_wilson.py (5); EX027–EX038 |
| 7–8 | Thesis synthesis, reproducibility archive, defense and publication | EX039–EX050 |

Verified lab facts (synthetic): precision 0.087 at prevalence 1e-3 with FPR 1e-2; rule v1 precision 0.50 recall 0.75, v2 1.00/1.00; kappa 0.73 (agreement 0.90, chance 0.625); accuracy 0.738 [0.664, 0.800] baseline vs 0.869 [0.808, 0.913] enriched.

## Safety, privacy and information boundaries

- Synthetic telemetry only; no exploit code, payloads, attack procedures or evasion guidance.
- Standard-library labs.
- Analyst participants consent; individual scores are never shared with managers.

## Continue the curriculum

After chapter 8, the next stop is [course 200: Incident response and cyber resilience / Doctoral research track](../../incident-response-resilience/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
