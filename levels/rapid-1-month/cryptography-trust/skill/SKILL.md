---
name: oca-cryptography-trust-rapid-a49d4b1a
description: "Guide a learner through the CRYPT rapid course draft: 4 chapters following synthetic new learner Leo Fernandes at Willow Lane Community Library, three stdlib labs and EX001–EX050 with worked answers."
license: CC0-1.0
---

# Cryptography and trust services — Rapid course course skill

Use this **one skill for the whole 1 month course**. The course has one principal book per language; each of its 4 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 008, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/cryptography-trust/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Four-chapter rapid route

This is the one-month **rapid course** in cryptography and trust services. The book follows synthetic new learner **Leo Fernandes**, guided by volunteer **Inês Hartley** at the fictional **Willow Lane Community Library**: the three promises of cryptography, permission and safe practice, the library's systems and suppliers, and one guided task verifying a download fingerprint.

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1 | Promises, encoding vs hashing vs encryption vs signatures, the padlock, safe decisions | lab_fingerprint.py; EX001–EX013 |
| 2 | Permission, small scope, personal data and secrets, coordinated disclosure | EX014–EX026 |
| 3 | Systems and suppliers, salted password storage, expiry | lab_salted.py; EX027–EX038 |
| 4 | Guided fingerprint check, interpreting results, staff summary, next steps | lab_checkfile.py; EX039–EX050 |

Verified lab facts (synthetic): one changed character gives an unrelated SHA-256 (match False); two members with the same password get different salted scrypt values and both verify; the good download prints MATCH and the tampered one MISMATCH.

## Teaching guardrails

- Labs call standard-library functions on synthetic data; never suggest custom cryptography or clicking through certificate warnings.
- No checks without written permission; report found secrets by location, never by value.

## Continue the curriculum

After chapter 4, the next stop is [course 009: Web3, blockchain and cryptoasset security / Rapid course](../../web3-blockchain-security/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
