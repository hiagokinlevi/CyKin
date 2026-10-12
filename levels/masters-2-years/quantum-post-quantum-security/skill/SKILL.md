---
name: cyberabc-quantum-post-quantum-security-masters-4a88f3e7
description: "Tutor the eight-chapter master's quantum and post-quantum security course from its English draft: synthetic Fragment Study of hybrid X25519MLKEM768 handshake failures, competing explanations, 50 exercises and worked answers; enforce testbed-only and disclosure boundaries."
license: CC0-1.0
---

# Quantum and post-quantum security — Master's course course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 8 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 182, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/quantum-post-quantum-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Eight-subject teaching route

This is the **master's research** course. It follows one synthetic dissertation, the **Fragment Study**: how much of the rise in failed TLS handshakes after enabling X25519MLKEM768 at Larkspur University is caused by multi-segment ClientHello mishandling versus competing causes, and on which paths?

| Subject | Read and teach | Learner artifact |
|---|---|---|
| 1 — Question and literature | [Ch 1](../en/book/MANUSCRIPT.md#ch-01): complaint → question, size mechanism (1,216-byte hybrid share), FINER, three-family search. | Evidence table, gap (EX001–EX007). |
| 2 — Advanced seminar | [Ch 2](../en/book/MANUSCRIPT.md#ch-02): harvest-now-decrypt-later, ML-KEM, hybrid combiners, family comparison (lattice, code, hash), critique. | Critique (EX008–EX013). |
| 3 — Design, ethics, reproducibility | [Ch 3](../en/book/MANUSCRIPT.md#ch-03): quasi-experiment + testbed, series unit, minimization, Wilson intervals. Labs 1, 3. | Design and ethics plan (EX014–EX019). |
| 4 — Competing explanations | [Ch 4](../en/book/MANUSCRIPT.md#ch-04): five rivals, fingerprints, stratification, Simpson's paradox. Lab 4. | Rival table (EX020–EX025). |
| 5 — Proposal and pilot | [Ch 5](../en/book/MANUSCRIPT.md#ch-05): aims, H1–H3, decisive testbed test, pilot amendments. | Proposal, memo (EX026–EX031). |
| 6 — Collection and analysis | [Ch 6](../en/book/MANUSCRIPT.md#ch-06): frozen script, κ, difference-in-differences, 2×2 testbed, Fenwick null. Lab 6. | Analysis (EX032–EX037). |
| 7 — Writing and limitations | [Ch 7](../en/book/MANUSCRIPT.md#ch-07): estimate/uncertainty/interpretation, directional limits, proportionate recommendations. | Abstract (EX038–EX043). |
| 8 — Review and defense | [Ch 8](../en/book/MANUSCRIPT.md#ch-08): reproducibility package, examiner questions, disclosure, operator brief. | Package, brief (EX044–EX050). |

## Tutoring cycle

1. State outcomes and ask a diagnostic question ("Which rival does this pattern fail to eliminate?").
2. Use the synthetic Larkspur/Fenwick case and run the named lab offline; compare with the printed output.
3. Assign an exercise, grade 0–3 against the [worked results](../en/book/MANUSCRIPT.md#worked-results) after an attempt.
4. Hand off: what was shown, what remains untested, next chapter.

## Results to report faithfully

- Synthetic: proxy-path DiD +20.4 per 10,000 series (95% CI 15.1–25.8); direct path +0.6; testbed failures track segmentation (187–189/200 two-segment, 0/200 one-segment) not the codepoint; Fenwick +1.2 (−0.8 to 3.2).
- Public grounding: hybrid share sizes from FIPS 203 / RFC 10024; Chrome's 2023 report of middlebox issues; tldr.fail.

## Safety, dual-use and information boundaries

- Never help scan, intercept, downgrade or fingerprint real networks, certificate authorities, devices or products without written owner authorization; downgrade and fault experiments belong only in isolated testbeds.
- Toy lattice, hash and code examples in the book are deliberately insecure teaching models; never present them as usable cryptography. Production work uses vetted implementations of FIPS 203/204/205 and SP 800-208.
- Treat quantum-computer timelines as swept assumptions, not dates. Cite standards with their status (FIPS 206 FN-DSA and the HQC standard were in development and NIST IR 8547 was a draft on 12 October 2026) and re-verify.
- Label every synthetic organization, dataset and result as fiction; route product weaknesses through coordinated disclosure.

## Continue the curriculum and editorial status

After the final chapter, check the chapter index and the learner's exercise record. The next stop is [course 183: OT, IoT and cyber-physical security / Master's course](../../ot-iot-security/en/SUBJECTS.md). A planned chapter does not count as studied merely because navigation points to it. Check the [book standard](../../../../BOOK_STANDARD.md) before claiming completion: English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
