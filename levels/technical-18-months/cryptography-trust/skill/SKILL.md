---
name: oca-cryptography-trust-technical-4fd2c9bb
description: "Guide a learner through the CRYPT technical course draft: 18 chapters following synthetic student Tomás Reyes at Lumen Freight Logistics, seven stdlib labs and EX001–EX072 with worked answers."
license: CC0-1.0
---

# Cryptography and trust services — Technical course course skill

Use this **one skill for the whole 18 months course**. The course has one principal book per language; each of its 18 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 054, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/cryptography-trust/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Eighteen-chapter technical route

This is the eighteen-month **technical course** in cryptography and trust services. The book follows synthetic student **Tomás Reyes** of the fictional **Eastbrook Technical Institute**, on placement with mentor **Priya Nandakumar** in IT operations at the fictional **Lumen Freight Logistics**: key files, integrity manifests, certificate expiry, TLS configuration, HMAC callbacks, troubleshooting, rotation planning, password storage and a supervised Wi-Fi trust-chain project.

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–6 | Architecture, protocol layers, key files and service accounts, encoding vs hashing, scope and evidence, trust model | lab_manifest.py (4); EX001–EX024 |
| 7–12 | Telemetry and expiry, failure classes, inspection tools, TLS control configuration, verification, contained lab I | lab_expiry.py (7), lab_tlsctx.py (10), lab_hmac.py (11); EX025–EX048 |
| 13–18 | Troubleshooting, automation and rotation, integrations, documentation and safety, password storage lab, supervised project | lab_triage.py (13), lab_rotation.py (14), lab_scrypt.py (17); EX049–EX072 |

Verified lab facts (synthetic unless cited): manifest flags routes_tue.csv as CHANGED; staging certificate expired 12 days before review; default context CERT_REQUIRED with check_hostname True; RFC 4231 TC1 matches, edited and stale callbacks fail; 12 of 20 failures are unknown_ca from handhelds; sftp-partner-b key overdue by 41 days; hashlib.scrypt matches the RFC 7914 vector and salted hashes differ.

## Teaching guardrails

- Labs call standard-library functions on synthetic data; production uses vetted libraries, ACME clients, vaults and HSMs. Never suggest custom cryptography or disabling certificate verification.
- Scan and test only in-scope systems with approval; report found secrets by location, never by value.

## Continue the curriculum

After chapter 18, the next stop is [course 055: Web3, blockchain and cryptoasset security / Technical course](../../web3-blockchain-security/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
