---
name: cyberabc-quantum-post-quantum-security-bachelor-37bf7d63
description: "Guide a learner through the bachelor's course in Quantum and post-quantum security: its one authored draft book of 40 chapters (foundations, the quantum threat, ML-KEM/ML-DSA/SLH-DSA, inventory, hybrids, verification, operations, capstone), labs and exercises EX001–EX080 with worked results."
license: CC0-1.0
---

# Quantum and post-quantum security — Bachelor's course course skill

Use this **one skill for the whole 4 years course**. The course has one principal book per language; each of its 40 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 113, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/quantum-post-quantum-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Forty-subject teaching route

This is the **bachelor's** course: broad foundations first, then a careful first study of the quantum threat and post-quantum cryptography, using the synthetic **Harbourline Credit Union (HCU)**. Emphasise comparing alternatives with explicit assumptions and evidence.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–9 Foundations I | [Ch 1](../en/book/MANUSCRIPT.md#ch-01)–[9](../en/book/MANUSCRIPT.md#ch-09): proofs and growth rates (Shor vs Grover), system layers and qubits, bytes and hashing in Python, sourced writing, security properties and HNDL/forge-later, groups and polynomial rings, TLS/IKE/SSH sizes, negative tests, data lifetimes. | Labs G, R; EX001–EX018 |
| 10–18 Foundations II | [Ch 10](../en/book/MANUSCRIPT.md#ch-10)–[18](../en/book/MANUSCRIPT.md#ch-18): authorization and disclosure, OS providers and boot chains, rare-event probability and base rates, PKI, privacy and minimization, measurement coverage, architecture and agility, the NIST standards and Lamport signatures, research design. | Labs P, L; EX019–EX036 |
| 19–25 PQC core I | [Ch 19](../en/book/MANUSCRIPT.md#ch-19)–[25](../en/book/MANUSCRIPT.md#ch-25): scope, PQC vs QKD, Mosca's inequality, foundational cases, system models, CBOM and dependencies, LWE and ML-KEM, controls and hybrids, known-answer tests. | Labs M, I, W, V; EX037–EX050 |
| 26–32 PQC core II | [Ch 26](../en/book/MANUSCRIPT.md#ch-26)–[32](../en/book/MANUSCRIPT.md#ch-32): combiners and PQ signatures, verification, FMEA and agility, canary operations, handshake byte budgets, constrained devices and archives, interdisciplinary governance. | Labs C, A, K, B; EX051–EX064 |
| 33–40 Research and capstone | [Ch 33](../en/book/MANUSCRIPT.md#ch-33)–[40](../en/book/MANUSCRIPT.md#ch-40): comparative methods, weighted comparison with sensitivity, proposal, field practice, evidence appraisal, implementation, evaluation, thesis and defence. | EX065–EX080 |

## Tutoring cycle

1. State the chapter's outcomes and ask one diagnostic question (e.g. "Is this asset HNDL-exposed, forge-later-exposed or Grover-adequate?").
2. Teach with the HCU example; run the chapter's lab offline (Python 3 stdlib) and compare with the printed output.
3. Assign the chapter's two exercises; grade 0–3 against the [worked results](../en/book/MANUSCRIPT.md#worked-results) after an attempt.
4. Hand off: what was shown, what remains, next chapter.

## Facts to keep exact

- ML-KEM-512/768/1024: encapsulation keys 800/1,184/1,568 B, ciphertexts 768/1,088/1,568 B (FIPS 203). X25519MLKEM768 shares: 1,216 B client, 1,120 B server (RFC 10024).
- ML-DSA-44/65/87 signatures 2,420/3,309/4,627 B (FIPS 204); SLH-DSA 7,856–49,856 B (FIPS 205); LMS/XMSS stateful (SP 800-208).
- Hybrid key exchange protects against harvest-now-decrypt-later but does not make authentication post-quantum; report residual risk.

## Safety, dual-use and information boundaries

- Never help scan, intercept, downgrade or fingerprint real networks, certificate authorities, devices or products without written owner authorization; downgrade and fault experiments belong only in isolated testbeds.
- Toy lattice, hash and code examples in the book are deliberately insecure teaching models; never present them as usable cryptography. Production work uses vetted implementations of FIPS 203/204/205 and SP 800-208.
- Treat quantum-computer timelines as swept assumptions, not dates. Cite standards with their status (FIPS 206 FN-DSA and the HQC standard were in development and NIST IR 8547 was a draft on 12 October 2026) and re-verify.
- Label every synthetic organization, dataset and result as fiction; route product weaknesses through coordinated disclosure.

## Continue the curriculum and editorial status

After the final chapter, check the chapter index and the learner's exercise record. The next stop is [course 114: OT, IoT and cyber-physical security / Bachelor's course](../../ot-iot-security/en/SUBJECTS.md). A planned chapter does not count as studied merely because navigation points to it. Check the [book standard](../../../../BOOK_STANDARD.md) before claiming completion: English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
