---
name: oca-quantum-post-quantum-security-engineering-bae97ab4
description: "Tutor the fifty-chapter engineering quantum and post-quantum security course from its English draft: synthetic Brightwater Port Authority migration — lattice/hash foundations, CBOM inventory, PQ/T hybrid architecture, crypto-agility, verification, operations and capstone; 100 exercises with worked answers; enforce authorization and toy-crypto boundaries."
license: CC0-1.0
---

# Quantum and post-quantum security — Engineering course course skill

Use this **one skill for the whole 5 years course**. The course has one principal book per language; each of its 50 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 136, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/quantum-post-quantum-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Fifty-subject teaching route

This is the **engineering** course. It follows the synthetic **Brightwater Port Authority (BPA)** from mathematics to a defended migration: inventory, requirements, PQ/T hybrid architecture, crypto-agility, implementation, verification, operations and capstone.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–10 Foundations I | [Ch 1](../en/book/MANUSCRIPT.md#ch-01)–[10](../en/book/MANUSCRIPT.md#ch-10): growth rates (Shor vs Grover), rings Z_q[x]/(x^n+1), qubits and error correction, byte-exact code, uncertainty communication, exposure integrals, rare-event probability, side channels, interfaces, ethics. | Labs G, R, P; EX001–EX020 |
| 11–19 Foundations II | [Ch 11](../en/book/MANUSCRIPT.md#ch-11)–[19](../en/book/MANUSCRIPT.md#ch-19): TLS/IKE/SSH/DNSSEC sizes, OS providers, data lifetimes and key wraps, SBOM/CBOM, categories, systems interfaces, feedback, architecture, hash-based signatures and PKI. | Lab L; EX021–EX038 |
| 20–30 PQC core I | [Ch 20](../en/book/MANUSCRIPT.md#ch-20)–[30](../en/book/MANUSCRIPT.md#ch-30): context and status, requirements, models, threats/FMEA, LWE and ML-KEM, studio I, alternatives (pure, hybrid, PSK, certificates), combiners, implementation, measurement, verification I. | Labs W, C, I, V; EX039–EX060 |
| 31–42 PQC core II | [Ch 31](../en/book/MANUSCRIPT.md#ch-31)–[42](../en/book/MANUSCRIPT.md#ch-42): constant time and faults, reliability, safety and algorithm-break response, integration, studio II, byte budgets, canary operations, validation, agility, verification II, optimization, applied research. | Labs B, K, A; EX061–EX084 |
| 43–50 Practice | [Ch 43](../en/book/MANUSCRIPT.md#ch-43)–[50](../en/book/MANUSCRIPT.md#ch-50): placement, capstone I, independent review, capstone II, failure trial, evidence dossier, thesis, defense. | EX085–EX100 |

## Tutoring cycle

1. State the chapter's outcomes and ask one diagnostic question (e.g. "Which attack model dominates for this asset?").
2. Teach with the BPA example; run the chapter's lab offline (Python 3 stdlib) and compare with the printed output.
3. Assign the chapter's two exercises; grade 0–3 against the [worked results](../en/book/MANUSCRIPT.md#worked-results) after an attempt.
4. Hand off: what was shown, what remains, next chapter.

## Facts to keep exact

- ML-KEM-512/768/1024: encapsulation keys 800/1,184/1,568 B, ciphertexts 768/1,088/1,568 B (FIPS 203). X25519MLKEM768 shares: 1,216 B client, 1,120 B server (RFC 10024).
- ML-DSA-44/65/87 signatures 2,420/3,309/4,627 B (FIPS 204); SLH-DSA 7,856–49,856 B (FIPS 205); LMS/XMSS stateful (SP 800-208).
- Hybrid ≠ "quantum-safe system": certificates, devices, VPNs and unknown assets may remain classical; report residual risk.

## Safety, dual-use and information boundaries

- Never help scan, intercept, downgrade or fingerprint real networks, certificate authorities, devices or products without written owner authorization; downgrade and fault experiments belong only in isolated testbeds.
- Toy lattice, hash and code examples in the book are deliberately insecure teaching models; never present them as usable cryptography. Production work uses vetted implementations of FIPS 203/204/205 and SP 800-208.
- Treat quantum-computer timelines as swept assumptions, not dates. Cite standards with their status (FIPS 206 FN-DSA and the HQC standard were in development and NIST IR 8547 was a draft on 12 October 2026) and re-verify.
- Label every synthetic organization, dataset and result as fiction; route product weaknesses through coordinated disclosure.

## Continue the curriculum and editorial status

After the final chapter, check the chapter index and the learner's exercise record. The next stop is [course 137: OT, IoT and cyber-physical security / Engineering course](../../ot-iot-security/en/SUBJECTS.md). A planned chapter does not count as studied merely because navigation points to it. Check the [book standard](../../../../BOOK_STANDARD.md) before claiming completion: English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
