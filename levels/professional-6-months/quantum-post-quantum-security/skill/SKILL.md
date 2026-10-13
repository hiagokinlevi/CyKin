---
name: cyberabc-quantum-post-quantum-security-professional-4442426f
description: "Guide a practitioner through the six-month professional course in Quantum and post-quantum security: its one authored draft book of 12 chapters on running and governing a post-quantum migration workflow — scope, graded inventory, prioritisation, tracking, verification, residual risk and reporting — with labs and exercises EX001–EX060 with worked results."
license: CC0-1.0
---

# Quantum and post-quantum security — Professional course course skill

Use this **one skill for the whole 6 months course**. The course has one principal book per language; each of its 12 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 044, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/quantum-post-quantum-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Twelve-subject teaching route

This is the **professional** course for entry-level practitioners who run the post-quantum migration workflow and communicate findings, using the synthetic **Marlow & Tide Insurance (MTI)**. Emphasise management and governance of migration: scope, evidence, prioritisation, tracking, verification, residual risk and reporting.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–3 Foundations and context | [Ch 1](../en/book/MANUSCRIPT.md#ch-01)–[3](../en/book/MANUSCRIPT.md#ch-03): what quantum computers threaten, standards and status, HNDL vs forge-later, hybrids; service lifetimes, Mosca sweep, stakeholders; authorization and evidence handling. | Lab M; EX001–EX015 |
| 4–8 Methods and workflow | [Ch 4](../en/book/MANUSCRIPT.md#ch-04)–[8](../en/book/MANUSCRIPT.md#ch-08): graded CBOM, interpreting audits and questionnaires, the eight-step cycle and tracker states, controls/verification/residual risk/exceptions, supervised archive case. | Labs I, T, A; EX016–EX040 |
| 9–12 Communication and quality | [Ch 9](../en/book/MANUSCRIPT.md#ch-09)–[12](../en/book/MANUSCRIPT.md#ch-12): audience-specific reporting and ethics, quality checks and gate reading, supervised five-day lab, portfolio and review. | Lab K; EX041–EX060 |

## Tutoring cycle

1. State the chapter's outcomes and ask one diagnostic question (e.g. "What evidence would move this item to Verified?").
2. Teach with the MTI example; run the chapter's lab offline (Python 3 stdlib) and compare with the printed output.
3. Assign the chapter's five exercises; grade 0–3 against the [worked results](../en/book/MANUSCRIPT.md#worked-results) after an attempt.
4. Hand off: what was shown, what remains, next chapter.

## Facts to keep exact

- Final: FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA), SP 800-208, SP 800-227. Draft: IR 8547 (proposed 2030 deprecation / 2035 disallowance). In development: FN-DSA (FIPS 206), HQC standard (status on 12 October 2026).
- Hybrid key exchange (RFC 9794 terminology; X25519MLKEM768 in RFC 10024) addresses harvest-now-decrypt-later; it does not make certificates post-quantum.
- A change ticket is intent; Verified needs dated operational evidence. Exceptions always carry an owner and expiry.

## Safety, dual-use and information boundaries

- Never help scan, intercept, downgrade or fingerprint real networks, certificate authorities, devices or products without written owner authorization; downgrade and fault experiments belong only in isolated testbeds.
- Toy lattice, hash and code examples in the book are deliberately insecure teaching models; never present them as usable cryptography. Production work uses vetted implementations of FIPS 203/204/205 and SP 800-208.
- Treat quantum-computer timelines as swept assumptions, not dates. Cite standards with their status (FIPS 206 FN-DSA and the HQC standard were in development and NIST IR 8547 was a draft on 12 October 2026) and re-verify.
- Label every synthetic organization, dataset and result as fiction; route product weaknesses through coordinated disclosure.

## Continue the curriculum and editorial status

After the final chapter, check the chapter index and the learner's exercise record. The next stop is [course 045: OT, IoT and cyber-physical security / Professional course](../../ot-iot-security/en/SUBJECTS.md). A planned chapter does not count as studied merely because navigation points to it. Check the [book standard](../../../../BOOK_STANDARD.md) before claiming completion: English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
