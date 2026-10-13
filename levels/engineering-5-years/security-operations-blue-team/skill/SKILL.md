---
name: cyberabc-security-operations-blue-team-engineering-5448d608
description: "Engineering course (5 years)"
license: CC0-1.0
---

# Security operations and blue team — Engineering course course skill

Use this **one skill for the whole 5 years course**. The course has one principal book per language; each of its 50 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 130, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/security-operations-blue-team/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Fifty-subject teaching route

This is the five-year **engineering course** for security operations and blue team. The book follows synthetic engineering student **Amara Osei** of the fictional **Kingsbridge Engineering University** on placement in the SOC of the fictional **Lindqvist Freight**, mentored by detection engineer **Paolo Ricci**: from a customer-portal credential-stuffing and account-takeover incident to a validated capstone that closes a monitoring gap in agentless depot networks.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–10 | Calculus, discrete maths, physics, programming, communication, probability, architecture, ethics | lab_queue.py (1), lab_bayes.py (7); EX001–EX030 |
| 11–19 | Networks, operating systems, data systems, software engineering, security fundamentals, systems engineering, control, architecture, identity | lab_failed.py (11); EX031–EX057 |
| 20–30 | SOC context, requirements, models, threat and failure analysis, methods, studio I, alternatives, control design, implementation, measurement, verification lab I | lab_rule.py (24), lab_latency.py (29), lab_unittest.py (30); EX058–EX090 |
| 31–41 | Implementation II, reliability, safety and resilience, integration, studio II, scale, operations, validation, maintainability, verification lab II, optimisation | lab_capacity.py (36), lab_e2e.py (40); EX091–EX123 |
| 42–50 | Applied research, practice, capstone I and II, independent review, failure and recovery trial, dossier, thesis, defense | lab_silence.py (47); EX124–EX150 |

Verified lab facts (synthetic): backlog peaks at 65 at 13:00; precision 0.153 at 0.2% prevalence; 203.0.113.0/24 shows 6 failures over 7 users; rule variants 2/0/1, 1/0/2, 3/2/0; median 7, p90 16.4 min; 4 unit tests pass; 6,000 EPS, 285.1 GB/day, 25.7 TB hot; 2 of 5 end-to-end runs fail (busy, handover); portal-web-3 SILENT.

## Safety, privacy and information boundaries

- Synthetic telemetry only; no exploit code, payloads, attack procedures or evasion guidance.
- Standard-library labs; purple-team simulations only under signed authorisation.
- Minimise monitoring to purpose; withhold detection details that would aid evasion.

## Continue the curriculum

After chapter 50, the next stop is [course 131: Incident response and cyber resilience / Engineering course](../../incident-response-resilience/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
