---
name: cyberabc-cryptography-trust-masters-b74713d6
description: "Guide a learner through the master's course in Cryptography and trust services: a synthetic study of TLS certificate expiry and ACME renewal, with stdlib labs, exercises and verified sources."
license: CC0-1.0
---

# Cryptography and trust services — Master's course course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 8 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 169, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/cryptography-trust/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Eight-chapter master's route

This is the two-year **master's course** in cryptography and trust services. The book follows synthetic student **Felipe Arantes** of the fictional **Coldwater Polytechnic**, supervised by **Dr. Ingrid Solberg**, as he studies whether ACME automated renewal (RFC 8555) is associated with fewer TLS certificate expiry incidents than manual renewal at the fictional **Briarwood Health Network**, and what else explains them.

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–2 | Literature method and screening funnel; X.509, TLS 1.3 and certificate inventories | lab_screen.py (1), lab_inventory.py (2); EX001–EX014 |
| 3–5 | Observational design, HMAC pseudonyms, competing explanations, proposal and pilot | lab_pseudo.py (3), lab_explain.py (4); EX015–EX032 |
| 6–8 | Rates and bootstrap analysis, dissertation and limitations, independent review | lab_rate.py (6); EX033–EX050 |

Verified lab facts (synthetic): screening 412 → 297 → 64 → 21 → 9 (3.0%); 4 of 8 sampled certificates urgent, all manual; HMAC pseudonym h-6f292159ff for portal.briarwood.example; owner missing in 61% of manual and 71% of ACME incidents; 4.26 vs 0.78 incidents per 100 certificate-years, rate ratio 5.48, bootstrap 2.50–17.50 (seed 7).

## Teaching guardrails

- Teach operation of maintained TLS, X.509 and ACME tooling; never suggest custom crypto or home-grown renewal scripts for production.
- Synthetic hosts only; real pseudonymisation keys belong in a managed secret store and are destroyed at study end.

## Continue the curriculum

After chapter 8, the next stop is [course 170: Web3, blockchain and cryptoasset security / Master's course](../../web3-blockchain-security/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
