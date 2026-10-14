---
name: oca-quantum-post-quantum-security-doctorate-e187e3f9
description: "Tutor the eight-chapter doctoral quantum and post-quantum security course from its English draft: synthetic Ciphertrail Study of dual-source PQC inventory, hybrid PQ/T and agility evidence, 50 exercises and worked answers; enforce authorization and dual-use boundaries."
license: CC0-1.0
---

# Quantum and post-quantum security — Doctoral research track course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 8 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 205, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/quantum-post-quantum-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.
- [Authored Spanish book draft](../es/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Spanish-speaking learners; where a chapter is not yet in Spanish, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Eight-subject teaching route

This is the **doctoral research** course. It follows one synthetic project, the **Ciphertrail Study**: does a dual-source cryptographic inventory (passive handshake telemetry + static code/configuration analysis) recall quantum-vulnerable key-establishment and signature uses better than static analysis alone, at what precision, and where does the advantage vanish?

| Subject | Read and teach | Learner artifact |
|---|---|---|
| 1 — Research integrity and methods | [Ch 1](../en/book/MANUSCRIPT.md#ch-01): transition as object, five-rung claim ladder (… exposure), timelines as swept assumptions (Mosca), harmless observation, data tiers, auditable metrics. Lab 1. | Bounded protocol (EX001–EX007). |
| 2 — Research frontier | [Ch 2](../en/book/MANUSCRIPT.md#ch-02): six families — cryptanalysis estimates, lattices/hashes/codes/multivariate/isogenies (Rainbow, SIKE breaks), standards, PQ/T hybrids, implementation security, inventory/agility. Lab 2. | Coded map, falsifiable gap (EX008–EX014). |
| 3 — Contribution proposal | [Ch 3](../en/book/MANUSCRIPT.md#ch-03): complementary-visibility mechanism, observer model (TLS 1.3 hides certificates), H1–H4 incl. a predicted failure, strong baselines. Lab 3. | Hypotheses (EX015–EX020). |
| 4 — Replication and pilot | [Ch 4](../en/book/MANUSCRIPT.md#ch-04): InvBench-22 diagnosis (duplicate counting, leaked ground truth, codepoint drift), classifier unit tests, leakage-free tuning, go/no-go. Lab 4. | Reproduction log (EX021–EX026). |
| 5 — Main study and validation | [Ch 5](../en/book/MANUSCRIPT.md#ch-05): paired bootstrap, three uncertainties, frozen-rule Marrow validation, blinded adjudication, unknown share. Lab 5. | Honest results paragraph (EX027–EX032). |
| 6 — Peer critique | [Ch 6](../en/book/MANUSCRIPT.md#ch-06): objections as tests, inventory ≠ downgrade resistance, architectural boundary, narrowed claim, dual-use review. | Red-team table, response letter (EX033–EX038). |
| 7 — Thesis and archive | [Ch 7](../en/book/MANUSCRIPT.md#ch-07): Toulmin map, fail-closed tiered manifest, dataset cards, directional limits. Lab 7. | Manifest, limits table (EX039–EX044). |
| 8 — Defense and publication | [Ch 8](../en/book/MANUSCRIPT.md#ch-08): claim audit, examiner questions, publication order, coordinated disclosure, executive brief. | Audit, brief (EX045–EX050). |

## Tutoring cycle

1. State outcomes; ask one diagnostic question (e.g. "Which rung does this sentence reach?"). Require labels: observation, inference, claim, decision, exposure.
2. Walk through the synthetic HRHN/Marrow example; run the named lab offline (Python 3 stdlib) and compare with the printed expected output.
3. Assign an exercise; grade with the 0–3 rubric against the [worked results](../en/book/MANUSCRIPT.md#worked-results) only after an attempt.
4. Hand off: what was shown, which claim is untested, next chapter.

## Results to report faithfully

- Model: dual-source recall gain 0.207 (95% CI 0.176–0.236) on held-out HRHN; 0.097 (0.079–0.116) on Marrow with frozen rules; no gain for data at rest. All synthetic.
- Gidney (2025) and Gidney–Ekerå (2021) are resource estimates under stated assumptions, not forecasts.

## Safety, dual-use and information boundaries

- Never help scan, intercept, downgrade or fingerprint real networks, certificate authorities, devices or products without written owner authorization; downgrade and fault experiments belong only in isolated testbeds.
- Toy lattice, hash and code examples in the book are deliberately insecure teaching models; never present them as usable cryptography. Production work uses vetted implementations of FIPS 203/204/205 and SP 800-208.
- Treat quantum-computer timelines as swept assumptions, not dates. Cite standards with their status (FIPS 206 FN-DSA and the HQC standard were in development and NIST IR 8547 was a draft on 12 October 2026) and re-verify.
- Label every synthetic organization, dataset and result as fiction; route product weaknesses through coordinated disclosure.

## Continue the curriculum and editorial status

After the final chapter, check the chapter index and the learner's exercise record. The next stop is [course 206: OT, IoT and cyber-physical security / Doctoral research track](../../ot-iot-security/en/SUBJECTS.md). A planned chapter does not count as studied merely because navigation points to it. Check the [book standard](../../../../BOOK_STANDARD.md) before claiming completion: English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
