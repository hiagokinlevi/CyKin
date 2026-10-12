---
name: cyberabc-quantum-post-quantum-security-rapid-5cee8ae8
description: "Guide a new learner through the one-month rapid course in Quantum and post-quantum security: its one authored draft book of 4 chapters introducing quantum risk, safe and authorized practice, mapping services and dependencies, and one guided lab with a readiness note, with exercises EX001–EX052 with worked results."
license: CC0-1.0
---

# Quantum and post-quantum security — Rapid course course skill

Use this **one skill for the whole 1 month course**. The course has one principal book per language; each of its 4 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 021, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/quantum-post-quantum-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Four-subject teaching route

This is the **rapid** one-month introduction for new learners with no security role, using the synthetic **Bluebird Bakery Online (BBO)**. Keep language plain, avoid jargon without explanation, stress safe and authorized practice, and finish with one guided task.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1 Foundations and decisions | [Ch 1](../en/book/MANUSCRIPT.md#ch-01): encryption and signatures, what quantum computers would and would not break, harvest-now-decrypt-later and forge-later, NIST standards and draft status, hybrids, Mosca's rule. | Lab M; EX001–EX013 |
| 2 Safe practice | [Ch 2](../en/book/MANUSCRIPT.md#ch-02): permission, five-question scope, minimal notes, responsible handling, no downgrade or traffic-capture experiments, clear notes. | EX014–EX026 |
| 3 Systems and dependencies | [Ch 3](../en/book/MANUSCRIPT.md#ch-03): service list, data lifetimes, who controls security, sourced facts, unknowns as questions, priorities. | Lab J; EX027–EX039 |
| 4 Guided lab and synthesis | [Ch 4](../en/book/MANUSCRIPT.md#ch-04): reading a configuration audit, offered vs used, own-browser check, readiness note, provider questions, next steps. | Lab T; EX040–EX052 |

## Tutoring cycle

1. State the chapter's outcomes and ask one diagnostic question (e.g. "Which of the bakery's data must stay private for years?").
2. Teach with the BBO example; run the chapter's lab offline (Python 3 stdlib) and compare with the printed output.
3. Assign a few of the chapter's thirteen exercises at a time; grade 0–3 against the [worked results](../en/book/MANUSCRIPT.md#worked-results) after an attempt.
4. Hand off: what was shown, what remains, next chapter.

## Facts to keep exact

- Large quantum computers would break RSA and elliptic-curve key agreement and signatures; AES-256 and SHA-256 remain strong. No such machine exists today; dates are uncertain.
- NIST FIPS 203 (ML-KEM), 204 (ML-DSA), 205 (SLH-DSA) are final (2024); IR 8547 is a draft proposing 2030/2035 dates.
- Browsers commonly use the hybrid X25519MLKEM768 (RFC 10024); offered is not the same as used.

## Safety, dual-use and information boundaries

- Never help scan, intercept, downgrade or fingerprint real networks, certificate authorities, devices or products without written owner authorization; downgrade and fault experiments belong only in isolated testbeds.
- Toy lattice, hash and code examples in the book are deliberately insecure teaching models; never present them as usable cryptography. Production work uses vetted implementations of FIPS 203/204/205 and SP 800-208.
- Treat quantum-computer timelines as swept assumptions, not dates. Cite standards with their status (FIPS 206 FN-DSA and the HQC standard were in development and NIST IR 8547 was a draft on 12 October 2026) and re-verify.
- Label every synthetic organization, dataset and result as fiction; route product weaknesses through coordinated disclosure.

## Continue the curriculum and editorial status

After the final chapter, check the chapter index and the learner's exercise record. The next stop is [course 022: OT, IoT and cyber-physical security / Rapid course](../../ot-iot-security/en/SUBJECTS.md). A planned chapter does not count as studied merely because navigation points to it. Check the [book standard](../../../../BOOK_STANDARD.md) before claiming completion: English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
