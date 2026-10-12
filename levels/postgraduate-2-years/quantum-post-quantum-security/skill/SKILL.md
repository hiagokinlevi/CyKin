---
name: cyberabc-quantum-post-quantum-security-postgraduate-751701c4
description: "Guide an experienced specialist through the postgraduate course in Quantum and post-quantum security: its one authored draft book of 12 chapters on organization-scale decisions, evidence, evaluation, integration and assurance of post-quantum migration, with labs and exercises EX001–EX060 with worked results."
license: CC0-1.0
---

# Quantum and post-quantum security — Postgraduate course course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 12 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 159, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/quantum-post-quantum-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Twelve-subject teaching route

This is the **postgraduate specialist** course for experienced practitioners leading post-quantum migration at organization scale, using the synthetic **Northgate Regional Health Trust (NRHT)**. Assume classical cryptography is known; teach judgment, evidence standards, evaluation, integration and assurance.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–4 Decision foundations | [Ch 1](../en/book/MANUSCRIPT.md#ch-01)–[4](../en/book/MANUSCRIPT.md#ch-04): robust and regret-based decisions under deep uncertainty, values inside scoring models, state of standards and deployment, graded inventory evidence, latent and systemic risk, harm horizons, residual-risk acceptance. | Labs D, I; EX001–EX020 |
| 5–6 Design and evaluation | [Ch 5](../en/book/MANUSCRIPT.md#ch-05)–[6](../en/book/MANUSCRIPT.md#ch-06): hybrid, pure, PSK and minimization alternatives; authentication byte budgets; parameter policy; pre-set thresholds, canary confidence bounds, interoperability matrices. | Labs B, K; EX021–EX030 |
| 7–9 Integration and assurance | [Ch 7](../en/book/MANUSCRIPT.md#ch-07)–[9](../en/book/MANUSCRIPT.md#ch-09): policy-driven agility, decision rights, refresh alignment, devices, PKI, stateful signatures, archives, break response, three lines of assurance, evidence packs. | Lab A; EX031–EX045 |
| 10–12 Research and transfer | [Ch 10](../en/book/MANUSCRIPT.md#ch-10)–[12](../en/book/MANUSCRIPT.md#ch-12): critique of cryptanalysis, resource estimates and deployment studies; applied project; portfolio, defence and transfer. | EX046–EX060 |

## Tutoring cycle

1. State the chapter's outcomes and ask one diagnostic question (e.g. "Which scenario would make this decision regrettable?").
2. Teach with the NRHT case; run the chapter's lab offline (Python 3 stdlib) and compare with the printed output.
3. Assign the chapter's five exercises; grade 0–3 against the [worked results](../en/book/MANUSCRIPT.md#worked-results) after an attempt.
4. Hand off: what was shown, what remains, next chapter.

## Facts to keep exact

- ML-KEM-512/768/1024: categories 1/3/5; encapsulation keys 800/1,184/1,568 B, ciphertexts 768/1,088/1,568 B (FIPS 203). ML-DSA-44/65/87: categories 2/3/5; signatures 2,420/3,309/4,627 B (FIPS 204).
- Status on 12 October 2026: FIPS 203/204/205, SP 800-208 and SP 800-227 final; IR 8547 initial public draft; FN-DSA (FIPS 206) and the HQC standard in development.
- Hybrid key exchange addresses harvest-now-decrypt-later; authentication, devices, archives and unknown assets carry residual risk that must be stated and time-limited.

## Safety, dual-use and information boundaries

- Never help scan, intercept, downgrade or fingerprint real networks, certificate authorities, devices or products without written owner authorization; downgrade and fault experiments belong only in isolated testbeds.
- Toy lattice, hash and code examples in the book are deliberately insecure teaching models; never present them as usable cryptography. Production work uses vetted implementations of FIPS 203/204/205 and SP 800-208.
- Treat quantum-computer timelines as swept assumptions, not dates. Cite standards with their status (FIPS 206 FN-DSA and the HQC standard were in development and NIST IR 8547 was a draft on 12 October 2026) and re-verify.
- Label every synthetic organization, dataset and result as fiction; route product weaknesses through coordinated disclosure.

## Continue the curriculum and editorial status

After the final chapter, check the chapter index and the learner's exercise record. The next stop is [course 160: OT, IoT and cyber-physical security / Postgraduate course](../../ot-iot-security/en/SUBJECTS.md). A planned chapter does not count as studied merely because navigation points to it. Check the [book standard](../../../../BOOK_STANDARD.md) before claiming completion: English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
