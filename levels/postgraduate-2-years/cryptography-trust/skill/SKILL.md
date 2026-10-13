---
name: cykin-cryptography-trust-postgraduate-3967a9b8
description: "Guide a learner through the postgraduate course in Cryptography and trust services: a synthetic organisation-scale cryptographic modernisation programme, with stdlib labs, exercises and verified sources."
license: CC0-1.0
---

# Cryptography and trust services — Postgraduate course course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 12 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 146, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/cryptography-trust/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Twelve-chapter postgraduate route

This is the two-year **postgraduate course** in cryptography and trust services. The book follows synthetic security architect **Leila Moradi** of the fictional **Corvane Logistics**, studying under **Prof. Anika Rao** at the fictional **Westbrook School of Security**, as she leads a company-wide cryptographic modernisation: TLS baseline, key-management consolidation, post-quantum readiness and legacy EDI retirement.

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–4 | Decision framing, current practice and endpoint inventory, post-quantum size evidence, long-lived risk and ethics | lab_inventory.py (2), lab_sizes.py (3); EX001–EX020 |
| 5–8 | Key-management alternatives and sensitivity, paired evaluation, organisational integration, difficult cases | lab_matrix.py (5), lab_eval.py (6); EX021–EX040 |
| 9–12 | Leadership and assurance, research critique, applied EDI project, final review and transfer | EX041–EX060 |

Verified lab facts (synthetic unless cited): 114/160 endpoints on TLS 1.3, 25 legacy-accepting (EDI 12); ML-DSA-65 signature 3,309 bytes ≈ 52× Ed25519, hybrid X25519+ML-KEM-768 share 1,216 bytes (sizes from FIPS 203/204, RFC 7748/8032); matrix cloud 3.90, hybrid 3.65, HSM 3.25, hybrid wins when custody weight is 0.45; mean reduction 5.62 misconfigured endpoints per site, sign-flip p = 0.0036.

## Teaching guardrails

- Decisions rely on vetted products, libraries and HSMs; never suggest custom cryptography or plaintext key export.
- Synthetic organisations only; supplier weaknesses go through coordinated disclosure.

## Continue the curriculum

After chapter 12, the next stop is [course 147: Web3, blockchain and cryptoasset security / Postgraduate course](../../web3-blockchain-security/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
