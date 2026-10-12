---
name: cyberabc-application-supply-chain-masters-326326c2
description: "APP master's course (8 ch / 50 ex)"
license: CC0-1.0
---

# Application and software supply chain security — Master's course course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 8 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 175, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/application-supply-chain/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Eight-subject teaching route

This is the two-year **master's course** for application and software supply chain security. The book follows synthetic student **Sofia Almeida** at the fictional **Kingsreach University**, supervised by **Dr Marcus Lee**, studying the fictional invoicing app **Tallyline**: do automated authorisation tests derived from a role matrix reduce the reintroduction of broken access control (OWASP A01), and what else explains the change?

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–2 | Research question, literature method, advanced seminar | EX001–EX014 |
| 3–5 | Study design and ethics, competing explanations, proposal and pilot | lab_authz.py (5); EX015–EX032 |
| 6–8 | Data and analysis, writing and limitations, review and defense | lab_regress.py, lab_rate.py (6); EX033–EX050 |

Verified lab facts (synthetic): 2 of 6 access decisions wrong (customer GET /invoices/other, support POST /refunds); findings 17 over 6 releases (2.83 per release) before vs 3 (0.50) after; 0.415 vs 0.058 findings per KLOC, rate ratio 0.14.

## Safety, privacy and information boundaries

- Synthetic code and data only; no exploit code, payloads, attack procedures or instructions for bypassing controls.
- Standard-library labs; authorisation testing only on systems you own or are permitted to test.
- Findings are attributed to releases, not people, and unfixed flaws are never published.

## Continue the curriculum

After chapter 8, the next stop is [course 176: Security operations and blue team / Master's course](../../security-operations-blue-team/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
