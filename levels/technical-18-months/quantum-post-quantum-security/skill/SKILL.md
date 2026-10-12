---
name: cyberabc-quantum-post-quantum-security-technical-34318756
description: "Guide a technical operator through the 18-month course in Quantum and post-quantum security: its one authored draft book of 18 chapters on hands-on checks, hybrid TLS/SSH configuration, verification, troubleshooting, automation, runbooks and contained labs, with exercises EX001–EX054 with worked results."
license: CC0-1.0
---

# Quantum and post-quantum security — Technical course course skill

Use this **one skill for the whole 18 months course**. The course has one principal book per language; each of its 18 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 067, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/quantum-post-quantum-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Eighteen-subject teaching route

This is the **technical** course for hands-on operators, using the synthetic **Halden Hotel Group (HHG)**. Teach checks, commands, logs, configuration, verification and safe labs; keep theory brief and practical.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–5 Foundations | [Ch 1](../en/book/MANUSCRIPT.md#ch-01)–[5](../en/book/MANUSCRIPT.md#ch-05): service maps and change routes, reading negotiated TLS/SSH algorithms, library versions and trust stores, JSON/CSV inventory scripts, scope and evidence. | Lab J; EX001–EX015 |
| 6–12 PQC operations | [Ch 6](../en/book/MANUSCRIPT.md#ch-06)–[12](../en/book/MANUSCRIPT.md#ch-12): system model and exposure classes, CBOM and log fields, failure modes and rollback, validated tools and size estimates, hybrid-first TLS/SSH configuration, verification with negative controls, contained lab I. | Labs I, B, T, V; EX016–EX036 |
| 13–18 Operations practice | [Ch 13](../en/book/MANUSCRIPT.md#ch-13)–[18](../en/book/MANUSCRIPT.md#ch-18): troubleshooting and log triage, scheduled checks and canary gates, hops and controllers, runbooks and baselines, failure-injection lab II, supervised project. | Labs H, K, A; EX037–EX054 |

## Tutoring cycle

1. State the chapter's outcomes and ask one diagnostic question (e.g. "Does this output show hybrid key exchange, and how do you know?").
2. Teach with the HHG example; run the chapter's lab offline (Python 3 stdlib) and compare with the printed output. Commands are illustrative; check current product documentation and stay within written scope.
3. Assign the chapter's three exercises; grade 0–3 against the [worked results](../en/book/MANUSCRIPT.md#worked-results) after an attempt.
4. Hand off: what was shown, what remains, next chapter.

## Facts to keep exact

- X25519MLKEM768 (RFC 10024): client share 1,216 B, server share 1,120 B; OpenSSH hybrid KEX `mlkem768x25519-sha256`; IKEv2 additional key exchanges RFC 9370.
- ML-KEM-768 encapsulation key 1,184 B, ciphertext 1,088 B (FIPS 203); ML-DSA-44 signature 2,420 B (FIPS 204).
- Offered is not negotiated; keep classical fallback during transition; never disable hybrid globally to fix one path.

## Safety, dual-use and information boundaries

- Never help scan, intercept, downgrade or fingerprint real networks, certificate authorities, devices or products without written owner authorization; downgrade and fault experiments belong only in isolated testbeds.
- Toy lattice, hash and code examples in the book are deliberately insecure teaching models; never present them as usable cryptography. Production work uses vetted implementations of FIPS 203/204/205 and SP 800-208.
- Treat quantum-computer timelines as swept assumptions, not dates. Cite standards with their status (FIPS 206 FN-DSA and the HQC standard were in development and NIST IR 8547 was a draft on 12 October 2026) and re-verify.
- Label every synthetic organization, dataset and result as fiction; route product weaknesses through coordinated disclosure.

## Continue the curriculum and editorial status

After the final chapter, check the chapter index and the learner's exercise record. The next stop is [course 068: OT, IoT and cyber-physical security / Technical course](../../ot-iot-security/en/SUBJECTS.md). A planned chapter does not count as studied merely because navigation points to it. Check the [book standard](../../../../BOOK_STANDARD.md) before claiming completion: English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
