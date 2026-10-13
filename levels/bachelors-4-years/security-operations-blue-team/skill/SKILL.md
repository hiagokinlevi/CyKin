---
name: cykin-security-operations-blue-team-bachelor-64af527c
description: "Bachelor's course (4 years)"
license: CC0-1.0
---

# Security operations and blue team — Bachelor's course course skill

Use this **one skill for the whole 4 years course**. The course has one principal book per language; each of its 40 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 107, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/security-operations-blue-team/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Forty-subject teaching route

This is the four-year **bachelor's course** for security operations and blue team. The book follows synthetic student analyst **Lucas Moreau** in the student-staffed SOC of the fictional **Riverton University**, supervised by information security manager **Dr. Hana Kim**: from a "Library fines overdue" phishing campaign that compromised student mail accounts, through a blameless review, to a capstone detection package measured on authorised test scenarios.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–10 | Mathematical reasoning, computing, programming, writing, security literacy, discrete structures, networks, programming II, databases, ethics | lab_rates.py (1), lab_sqlite.py (9); EX001–EX030 |
| 11–18 | Operating systems, statistics, identity, privacy, evidence, architecture, cryptography, research methods I | lab_zscore.py (12); EX031–EX054 |
| 19–30 | SOC scope, cases, system models, data, methods I–II, controls, laboratories, verification, failure analysis, operations | lab_spray.py (23), lab_queue_order.py (25), lab_coverage.py (27), lab_correlate.py (30); EX055–EX090 |
| 31–40 | Advanced cases, interfaces, research methods II, comparative project, capstone, community practice, evidence seminar, thesis | lab_wilson.py (39); EX091–EX120 |

Verified lab facts (synthetic): staff report 12.8 vs students 3.0 per 1,000; s2047 z ≈ 214.7; spray from 198.51.100.77 (30 users); queue A3, A1, A2, A5, A4; coverage 4/8 tested; correlation catches s2047, misses s3310 (149 min); detection 0.55 → 0.90.

## Safety, privacy and information boundaries

- Synthetic telemetry only; no exploit code, payloads, attack procedures or evasion guidance.
- Standard-library labs; test scenarios use university test accounts under written approval.
- Metadata by default; message content only with case approval.

## Continue the curriculum

After chapter 40, the next stop is [course 108: Incident response and cyber resilience / Bachelor's course](../../incident-response-resilience/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
