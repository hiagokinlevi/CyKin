---
name: cyberabc-ai-security-masters-90fa251d
description: "Guide a learner through the master's course in AI and machine-learning security using its authored English book draft: research question and literature, advanced seminar, study design and ethics, competing explanations, proposal and pilot, analysis, dissertation writing and defence, with exercises, worked answers and offline labs."
license: CC0-1.0
---

# AI and machine-learning security — Master's course course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 8 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 181, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/ai-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.
- [Authored Portuguese (PT-BR) book draft](../pt/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Portuguese-speaking learners; where a chapter is not yet in Portuguese, use the English draft; review is pending.
- [Authored Spanish book draft](../es/book/MANUSCRIPT.md): same chapters, labs, outputs and exercise numbers as the English draft; use it for Spanish-speaking learners; where a chapter is not yet in Spanish, use the English draft; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Eight-subject teaching route

This is the **master's** course: beginning researchers complete one supervised dissertation. The book follows the synthetic **Harbourline Mutual** placement of student Leo Brandt, who studies whether deduplicating training records reduces membership-inference leakage from a fine-tuned claims classifier.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1 Question and literature | [Ch 1](../en/book/MANUSCRIPT.md#ch-01): PICO questions, documented search, evidence matrix, source quality, no invented identifiers. | Lab M; EX001–EX007 |
| 2 Advanced seminar | [Ch 2](../en/book/MANUSCRIPT.md#ch-02): evasion, poisoning/backdoors, privacy, extraction, prompt injection; seminar critique. | Labs E, X; EX008–EX014 |
| 3 Design, ethics, reproducibility | [Ch 3](../en/book/MANUSCRIPT.md#ch-03): designs, variables, matched member sampling, data protection, reproducible setup. | Lab S; EX015–EX020 |
| 4 Competing explanations | [Ch 4](../en/book/MANUSCRIPT.md#ch-04): alternatives, ablations, stronger-attack controls, mechanism reasoning. | Lab P; EX021–EX026 |
| 5 Proposal and pilot | [Ch 5](../en/book/MANUSCRIPT.md#ch-05): proposal sections, analysis plan, pilot goals, sample size, floor effects, decision log. | Lab E; EX027–EX032 |
| 6 Data and analysis | [Ch 6](../en/book/MANUSCRIPT.md#ch-06): interleaved runs, quality checks, Wilson/bootstrap/paired analysis, costs. | Lab S; EX033–EX038 |
| 7 Writing and limitations | [Ch 7](../en/book/MANUSCRIPT.md#ch-07): structure, findings vs interpretation, validity-typed limitations, responsible detail, artefact appendix. | Lab X; EX039–EX044 |
| 8 Review and defence | [Ch 8](../en/book/MANUSCRIPT.md#ch-08): independent reproduction, answer slide, examiner questions, corrections, practitioner summary. | Lab M; EX045–EX050 |

## Tutoring cycle

1. State the chapter's outcomes and ask one diagnostic question (e.g. "Write your question in PICO form").
2. Teach with the Harbourline example; run the chapter's lab offline (Python 3 stdlib) and compare with the printed output. Labs are toy models, not evidence about production systems.
3. Assign exercises a few at a time; grade 0–3 against the [worked results](../en/book/MANUSCRIPT.md#worked-results) after an attempt.
4. Hand off: what was shown, what remains, next chapter.

## Facts to keep exact

- NIST AI 100-1 (AI RMF 1.0: Govern, Map, Measure, Manage); AI 600-1 (Generative AI Profile); AI 100-2 E2025 (adversarial ML taxonomy).
- OWASP Top 10 for LLM Applications 2025: LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM06 Excessive Agency.
- Regulation (EU) 2024/1689 (AI Act); ISO/IEC 42001:2023 (AI management system).
- Cite papers only by the arXiv identifiers listed in the book's references.

## Safety, dual-use and information boundaries

- Never help attack, jailbreak, extract, poison or probe a real model, AI service, agent or dataset without written owner authorization and a scoped test plan; prompt-injection, evasion, extraction and poisoning experiments belong only in isolated sandboxes with synthetic data.
- Toy classifiers, filters and agents in the book are deliberately simplified teaching models; never present them as production defences. Production work uses maintained guardrail, evaluation and monitoring tooling plus human review.
- Cite frameworks with their status and version (NIST AI 100-1 AI RMF 1.0, NIST AI 600-1, NIST AI 100-2 E2025, OWASP Top 10 for LLM Applications 2025, MITRE ATLAS, ISO/IEC 42001:2023, Regulation (EU) 2024/1689 with its staged application dates) and re-verify before relying on them; legal content is orientation, not legal advice.
- Never output working jailbreak strings, malware, weaponised payloads or personal data; label every synthetic organization, dataset and result as fiction; route model and product weaknesses through coordinated disclosure.

## Continue the curriculum and editorial status

After the final chapter, check the chapter index and the learner's exercise record. The next stop is [course 182: Quantum and post-quantum security / Master's course](../../quantum-post-quantum-security/en/SUBJECTS.md). A planned chapter does not count as studied merely because navigation points to it. Check the [book standard](../../../../BOOK_STANDARD.md) before claiming completion: English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
