---
name: cyberabc-security-operations-blue-team-technical-5a2e6d97
description: "SOC technical course: 18 chapters, 72 exercises, 4 stdlib labs"
license: CC0-1.0
---

# Security operations and blue team — Technical course course skill

Use this **one skill for the whole 18 months course**. The course has one principal book per language; each of its 18 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 061, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/security-operations-blue-team/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Eighteen-subject teaching route

This is the 18-month **technical course** for security operations and blue team. The book follows synthetic trainee analyst **Carlos Mendes** and SOC lead **Aisha Rahman** at the fictional **Northgate Borough Council**: from 46 failed portal logons and a compromised shared "parks01" account, through logs, triage, phishing, response, detection engineering, tuning, metrics and maturity.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–6 | SOC role, logs, SIEM, authentication, triage, endpoints | lab_failed.py (4), lab_triage.py (5); EX001–EX024 |
| 7–12 | Phishing, proxy logs, intelligence, incident response, containment, detection engineering | lab_ioc.py (8); EX025–EX048 |
| 13–18 | Tuning, coverage, metrics, shifts and wellbeing, maturity, review | lab_mttr.py (15); EX049–EX072 |

Verified lab facts (synthetic): 203.0.113.80 had 46 failures (threshold 20) then parks01 success at 09:09; triage scores A2 9 P1, A4 6 P2, A5 4 P3; indicator hits on 10.2.0.31 and 10.2.0.77 (2 of 4 hosts); median acknowledge 7 min, median contain 45.5 min, 4 of 6 acknowledged within 10 min.

## Safety, privacy and information boundaries

- Synthetic telemetry only; no exploit code, payloads, attack procedures or evasion guidance.
- Standard-library labs; reserved example addresses and domains.
- Monitoring of staff activity only for security purposes under policy.

## Continue the curriculum

After chapter 18, the next stop is [course 062: Incident response and cyber resilience / Technical course](../../incident-response-resilience/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
