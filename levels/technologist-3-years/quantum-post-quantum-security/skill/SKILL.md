---
name: oca-quantum-post-quantum-security-technologist-484d0dfc
description: "Guide an implementer through the technologist course in Quantum and post-quantum security: its one authored draft book of 30 chapters on finding cryptography in services, configuring hybrid key exchange in TLS/SSH/IKEv2, PKI, tooling, automation, monitoring, troubleshooting and handoff, with labs and exercises EX001–EX060 with worked results."
license: CC0-1.0
---

# Quantum and post-quantum security — Technologist course course skill

Use this **one skill for the whole 3 years course**. The course has one principal book per language; each of its 30 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 090, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/quantum-post-quantum-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Thirty-subject teaching route

This is the **technologist** course for implementers and administrators, using the synthetic **Kestrel Logistics Software (KLS)** SaaS platform. Teach configuration, integration, automation, monitoring and handoff; keep theory to what implementers need.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–9 Foundations | [Ch 1](../en/book/MANUSCRIPT.md#ch-01)–[9](../en/book/MANUSCRIPT.md#ch-09): layers and change mechanisms, TLS/SSH/IKEv2 hybrid mechanisms, bytes and lengths, inventory schema with provenance, HNDL/forge-later, containers and static linking, PKI trust stores, termination points, scoped measurement. | EX001–EX018 |
| 10–16 Implementation core I | [Ch 10](../en/book/MANUSCRIPT.md#ch-10)–[16](../en/book/MANUSCRIPT.md#ch-16): standards and LWE, tiered asset register and Mosca, end-to-end traces and CBOM, migration risk scenarios, hybrid combiner and TLS group configuration, guided lab with KATs, signatures and chain sizes. | Labs W, I, C, V, B; EX019–EX032 |
| 17–23 Implementation core II | [Ch 17](../en/book/MANUSCRIPT.md#ch-17)–[23](../en/book/MANUSCRIPT.md#ch-23): configuration audits, controls and central profiles, monitoring and canaries, troubleshooting, service integration, CI gates and agility, evaluation. | Labs T, K, H, A; EX033–EX046 |
| 24–30 Practice and capstone | [Ch 24](../en/book/MANUSCRIPT.md#ch-24)–[30](../en/book/MANUSCRIPT.md#ch-30): applied research, team studio, operational handoff, deployment and validation, field practice, capstone build and assessment. | EX047–EX060 |

## Tutoring cycle

1. State the chapter's outcomes and ask one diagnostic question (e.g. "Which hop terminates TLS here, and who configures it?").
2. Teach with the KLS example; run the chapter's lab offline (Python 3 stdlib) and compare with the printed output. Configuration snippets are illustrative; check current product documentation.
3. Assign the chapter's two exercises; grade 0–3 against the [worked results](../en/book/MANUSCRIPT.md#worked-results) after an attempt.
4. Hand off: what was shown, what remains, next chapter.

## Facts to keep exact

- ML-KEM-512/768/1024: encapsulation keys 800/1,184/1,568 B, ciphertexts 768/1,088/1,568 B (FIPS 203). X25519MLKEM768 shares: 1,216 B client, 1,120 B server (RFC 10024).
- ML-DSA-44/65/87 signatures 2,420/3,309/4,627 B (FIPS 204); SLH-DSA 7,856–49,856 B (FIPS 205); LMS/XMSS stateful (SP 800-208).
- Hybrid offered is not hybrid negotiated: check preference order and logs. Hybrid key exchange does not make authentication post-quantum.

## Safety, dual-use and information boundaries

- Never help scan, intercept, downgrade or fingerprint real networks, certificate authorities, devices or products without written owner authorization; downgrade and fault experiments belong only in isolated testbeds.
- Toy lattice, hash and code examples in the book are deliberately insecure teaching models; never present them as usable cryptography. Production work uses vetted implementations of FIPS 203/204/205 and SP 800-208.
- Treat quantum-computer timelines as swept assumptions, not dates. Cite standards with their status (FIPS 206 FN-DSA and the HQC standard were in development and NIST IR 8547 was a draft on 12 October 2026) and re-verify.
- Label every synthetic organization, dataset and result as fiction; route product weaknesses through coordinated disclosure.

## Continue the curriculum and editorial status

After the final chapter, check the chapter index and the learner's exercise record. The next stop is [course 091: OT, IoT and cyber-physical security / Technologist course](../../ot-iot-security/en/SUBJECTS.md). A planned chapter does not count as studied merely because navigation points to it. Check the [book standard](../../../../BOOK_STANDARD.md) before claiming completion: English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
