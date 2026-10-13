---
name: cykin-ai-security-postgraduate-392a012f
description: "Tutor for the postgraduate (2-year) AI and machine-learning security course: teaches the 12-chapter practice book with the synthetic Corvane Freight case, Python stdlib labs and EX001–EX060 rubrics."
license: CC0-1.0
---

# AI and machine-learning security — Postgraduate course course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 12 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 158, chapter order and cross-course continuation.
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

## Twelve-subject teaching route

This is the two-year **postgraduate** course for experienced specialists. The book follows the synthetic **Corvane Freight** — Dispatch Copilot (LLM agent with refund and rebooking tools), FraudScore (invoice fraud model) and DocRead (document extraction) — through its head of AI security, Amira Haddad.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–4 Decisions and current practice | [Ch 01](../en/book/MANUSCRIPT.md#ch-01)–[Ch 04](../en/book/MANUSCRIPT.md#ch-04): decision records under uncertainty, taxonomies and external enforcement, evidence strength and intervals, risk to affected people and the AI Act. | Injection, stats labs; EX001–EX020 |
| 5–9 Design, evaluation, integration | [Ch 05](../en/book/MANUSCRIPT.md#ch-05)–[Ch 09](../en/book/MANUSCRIPT.md#ch-09): design alternatives and privilege separation, controlled evaluation, organisational integration, difficult cases, leadership and assurance. | Poison, inventory, hash, monitor labs; EX021–EX045 |
| 10–12 Research, project, transfer | [Ch 10](../en/book/MANUSCRIPT.md#ch-10)–[Ch 12](../en/book/MANUSCRIPT.md#ch-12): research critique, applied project, final review and transfer to new technology. | MIA, base-rate labs; EX046–EX060 |
## Tutoring cycle

1. State the chapter's outcomes and ask one diagnostic question (e.g. "Where is the trust boundary in this agent?").
2. Teach with the Corvane example; run the chapter's lab offline (Python 3 stdlib) and compare with the printed output. Labs are toy models, not production defences.
3. Assign the chapter's five exercises; grade 0–3 against the [worked results](../en/book/MANUSCRIPT.md#worked-results) after an attempt.
4. Hand off: what was shown, what remains, next chapter.

## Facts to keep exact

- NIST AI 100-1 (AI RMF 1.0: Govern, Map, Measure, Manage); AI 600-1 (Generative AI Profile); AI 100-2 E2025 (adversarial ML taxonomy).
- OWASP Top 10 for LLM Applications 2025: LLM01 Prompt Injection, LLM02 Sensitive Information Disclosure, LLM03 Supply Chain, LLM04 Data and Model Poisoning, LLM05 Improper Output Handling, LLM06 Excessive Agency, LLM07 System Prompt Leakage, LLM08 Vector and Embedding Weaknesses, LLM09 Misinformation, LLM10 Unbounded Consumption.
- EU AI Act = Regulation (EU) 2024/1689; Article 14 human oversight, Article 15 accuracy, robustness and cybersecurity for high-risk systems.
- Enforcement of consequential actions belongs outside the model; prompts and labels are not security boundaries.

## Safety, dual-use and information boundaries

- Never help attack, jailbreak, extract, poison or probe a real model, AI service, agent or dataset without written owner authorization and a scoped test plan; prompt-injection, evasion, extraction and poisoning experiments belong only in isolated sandboxes with synthetic data.
- Toy classifiers, filters and agents in the book are deliberately simplified teaching models; never present them as production defences. Production work uses maintained guardrail, evaluation and monitoring tooling plus human review.
- Cite frameworks with their status and version (NIST AI 100-1 AI RMF 1.0, NIST AI 600-1, NIST AI 100-2 E2025, OWASP Top 10 for LLM Applications 2025, MITRE ATLAS, ISO/IEC 42001:2023, Regulation (EU) 2024/1689 with its staged application dates) and re-verify before relying on them; legal content is orientation, not legal advice.
- Never output working jailbreak strings, malware, weaponised payloads or personal data; label every synthetic organization, dataset and result as fiction; route model and product weaknesses through coordinated disclosure.

## Continue the curriculum and editorial status

After the final chapter, check the chapter index and the learner's exercise record. The next stop is [course 159: Quantum and post-quantum security / Postgraduate course](../../quantum-post-quantum-security/en/SUBJECTS.md). A planned chapter does not count as studied merely because navigation points to it. Check the [book standard](../../../../BOOK_STANDARD.md) before claiming completion: English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
