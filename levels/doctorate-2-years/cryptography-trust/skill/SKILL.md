---
name: cykin-cryptography-trust-doctorate-108918b8
description: "Guide a learner through the doctoral research track in Cryptography and trust services: a synthetic randomised study of cryptographic misuse in code review, with stdlib labs, exercises and verified sources."
license: CC0-1.0
---

# Cryptography and trust services — Doctoral research track course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 8 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 192, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/cryptography-trust/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Eight-chapter doctoral route

This is the two-year **doctoral research track** in cryptography and trust services. The book follows synthetic candidate **Nadia Haddad** of the fictional **Larkspur University**, supervised by **Prof. Oskar Brandt**, as she tests whether a cryptographic-misuse checklist plus lint in code review reduces confirmed misuse (nonce reuse, key handling, outdated primitives) at the fictional **Meridian Payments Cooperative**.

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–2 | Research integrity, misuse codebook and coder agreement; research frontier and GCM nonce limits | lab_kappa.py (1), lab_nonce.py (2); EX001–EX014 |
| 3–5 | Registered proposal, baseline audit and pilot, cluster-randomised main study | lab_baseline.py (4), lab_trial.py (5); EX015–EX032 |
| 6–8 | Peer critique, synthesis and hashed archive, defense and publication | lab_archive.py (7); EX033–EX050 |

Verified lab facts (synthetic): kappa 0.802 (41/48 agreed); random-nonce repeat probability 1.164e-10 at 2^32 messages, 7.629e-06 at 2^40; baseline 23/80 changes with misuse (28.8%), key-handling 9; misuse per ten changes 0.42 vs 1.58, permutation p = 0.0034 (seed 2026), zero-misuse teams 8/12 vs 2/12; manifest root 4ed0159418d1b231 changes to 1fcc81b868bef821 after a one-word edit.

## Teaching guardrails

- Teach use of vetted libraries and standards (SP 800-38D, SP 800-57, RFC 9106, FIPS 203–205); never present hand-written primitives as production code.
- Synthetic findings only; no key material, exploit procedures or details of live weaknesses.

## Continue the curriculum

After chapter 8, the next stop is [course 193: Web3, blockchain and cryptoasset security / Doctoral research track](../../web3-blockchain-security/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
