---
name: oca-cryptography-trust-engineering-2aa9d7a7
description: "Guide a learner through the engineering course in Cryptography and trust services: a synthetic five-year design of a smart-meter trust service, with stdlib labs, exercises and verified sources."
license: CC0-1.0
---

# Cryptography and trust services — Engineering course course skill

Use this **one skill for the whole 5 years course**. The course has one principal book per language; each of its 50 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 123, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/cryptography-trust/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Fifty-chapter engineering route

This is the five-year **engineering course** in cryptography and trust services. The book follows synthetic student **Aiyana Torres** of the fictional **Halden Institute of Engineering**, mentored by utility engineer **Marcus Webb**, as she designs, builds and operates the trust service that authenticates readings and firmware for 50,000 smart meters at the fictional **Ridgeway Water Utility**.

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–10 | Growth and key spaces, modular arithmetic, side channels, bytes and hashing, communication, series, birthday bound, architecture, safe wrappers, ethics | lab_keyspace.py (1), lab_modular.py (2), lab_birthday.py (7); EX001–EX030 |
| 11–20 | Networks and TLS 1.3, OS key protection, stored data and Argon2, software lifecycle, threat models, key lifecycle, feedback, trust anchors, HMAC identity, engineering context | lab_hmac.py (19); EX031–EX060 |
| 21–30 | Requirements, data models, threat and failure analysis, HKDF, design studio, alternatives, controls and ceremonies, firmware manifests, cryptoperiod metrics, verification lab | lab_hkdf.py (24), lab_manifest.py (28), lab_rotation.py (29); EX061–EX090 |
| 31–40 | Mutual TLS and ACME, custodian quorum, safe failure, integration, post-quantum studio, scale, operations, validation, agility, physical and failure-injection lab | lab_quorum.py (32); EX091–EX120 |
| 41–50 | Optimisation, applied research, placement, capstone revocation pipeline, design review, recovery trial, evidence dossier, thesis, defense | EX121–EX150 |

Verified lab facts (synthetic): 128-bit key search log10(years) 18.73 at 10^12/s; toy RSA d = 2753 (never real keys); 50,000 random 32-bit ids collide with P = 0.253; edited HMAC reading verifies False; HKDF matches RFC 5869 A.1; one flipped firmware bit rejected; 3 of 5 keys over a 365-day cryptoperiod; 3-of-5 custodian quorum availability 0.9914 vs 0.5905 for 5-of-5.

## Teaching guardrails

- Labs verify understanding against standards and test vectors; production uses vetted libraries and HSMs. Never present hand-written primitives as deployable.
- Synthetic keys and devices only; physical and side-channel testing only on authorised lab samples.

## Continue the curriculum

After chapter 50, the next stop is [course 124: Web3, blockchain and cryptoasset security / Engineering course](../../web3-blockchain-security/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
