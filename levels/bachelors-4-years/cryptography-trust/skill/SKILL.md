---
name: oca-cryptography-trust-bachelor-fab8343b
description: "Guide a learner through the bachelor's course in Cryptography and trust services: a synthetic four-year path protecting a library consortium's patron data, with stdlib labs, exercises and verified sources."
license: CC0-1.0
---

# Cryptography and trust services — Bachelor's course course skill

Use this **one skill for the whole 4 years course**. The course has one principal book per language; each of its 40 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 100, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/cryptography-trust/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Forty-chapter bachelor's route

This is the four-year **bachelor's course** in cryptography and trust services. The book follows synthetic student **Priya Raman** of the fictional **Ashford University**, taught by **Dr. Tomás Echeverría**, as she helps IT lead **Grace Okafor** protect patron data at the fictional **Tidewell Public Library Consortium**.

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–10 | Proof and XOR, data states, bytes and SHA-256, writing, security literacy, groups and Diffie-Hellman, TLS 1.3, safe APIs, password storage, authorised practice | lab_xor.py (1), lab_pbkdf2.py (9); EX001–EX030 |
| 11–20 | OS key stores, password bits, authentication factors, privacy, tamper-evident logs, architecture, Kerckhoffs and classical ciphers, research design, PKI theory, failure cases | lab_entropy.py (12), lab_chain.py (15), lab_caesar.py (17); EX031–EX060 |
| 21–30 | System models, inventory, AES-GCM, key controls, export lab, signatures, verification, key-compromise analysis, certificate operations, public-key export lab | lab_certdays.py (29); EX061–EX090 |
| 31–40 | Post-quantum and messaging, law and usability, study analysis, comparative project, capstone inventory, community workshops, evidence review, thesis | EX091–EX120 |

Verified lab facts (synthetic): reused pad reveals "FINE PAID  0938"; Caesar shift 11 found from letter P; salted PBKDF2 values differ for one password; random 6-word passphrase 77.5 bits vs 47.6 for 8 mixed characters; editing log entry 2 changes head 4492b592 → c3664171; patron-portal certificate flagged with 17 days left.

## Teaching guardrails

- Toy ciphers and stdlib labs explain concepts only; production uses vetted libraries. Never present hand-written primitives as deployable.
- Synthetic patrons and data only; any scanning or testing requires written authorisation.

## Continue the curriculum

After chapter 40, the next stop is [course 101: Web3, blockchain and cryptoasset security / Bachelor's course](../../web3-blockchain-security/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
