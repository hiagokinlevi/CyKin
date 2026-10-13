---
name: cyberabc-cryptography-trust-professional-a4206bdb
description: "Guide a learner through the CRYPT professional course draft: 12 chapters following synthetic analyst Dana Whitlock at Copperleaf Managed Services, four stdlib labs and EX001–EX060 with worked answers."
license: CC0-1.0
---

# Cryptography and trust services — Professional course course skill

Use this **one skill for the whole 6 months course**. The course has one principal book per language; each of its 12 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 031, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/cryptography-trust/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Twelve-chapter professional route

This is the six-month **professional course** in cryptography and trust services. The book follows synthetic junior analyst **Dana Whitlock**, mentored by **Marcus Oyelaran** at the fictional **Copperleaf Managed Services**, serving the fictional **Bayside Dental Group**: stakeholders, authorised evidence handling, core methods, baseline checks, a monthly workflow, notification verification, an exposed-key case, reporting, password storage, a rehearsal lab and a portfolio.

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–4 | Goals and context, stakeholders and owners, authorisation and evidence, core methods and certificates | EX001–EX020 |
| 5–8 | Tool interpretation, monthly workflow, controls and verification, exposed-key case | lab_inventory.py (5), lab_notify.py (7); EX021–EX040 |
| 9–12 | Reporting and ethics, quality and password storage, rehearsal lab, portfolio and trends | lab_pbkdf2.py (10), lab_trends.py (12); EX041–EX060 |

Verified lab facts (synthetic unless cited): 4 endpoints flagged and 1 clean (expiry 17 d, RSA-1024, SHA-1 + TLS 1.0, TLS 1.1); authentic notification accepted, changed amount and 1-hour replay rejected; salted PBKDF2 gives distinct stored values and costs over 10,000x a single SHA-256; expiry/chain is the top category, median 11 days to close, oldest open weak key at 142 days.

## Teaching guardrails

- Labs call standard-library functions on synthetic data; production uses vetted libraries, ACME clients and managed key stores. Never suggest custom cryptography or disabling certificate verification.
- Test only authorised systems; report found secrets by location, never by value; use coordinated disclosure for supplier flaws.

## Continue the curriculum

After chapter 12, the next stop is [course 032: Web3, blockchain and cryptoasset security / Professional course](../../web3-blockchain-security/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
