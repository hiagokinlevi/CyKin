---
name: cyberabc-ai-security-engineering-820de9ed
description: "Guide a learner through the five-year engineering course in AI and machine-learning security using its authored English book draft: mathematical and computing foundations, security architecture, AI-security requirements, controls, measurement, verification, operations and a capstone with evidence dossier and defence, with exercises, worked answers and offline labs."
license: CC0-1.0
---

# AI and machine-learning security — Engineering course course skill

Use this **one skill for the whole 5 years course**. The course has one principal book per language; each of its 50 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 135, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/ai-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Fifty-subject teaching route

This is the five-year **engineering** course for future security systems designers. The book follows the synthetic **Northgate Rail Systems (NRS)** — TrackEye (vision defect detection), Wrench (LLM maintenance assistant with tools) and Pulse (bearing anomaly model) — through intern Sam Ito.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–10 Foundations | [Ch 1](../en/book/MANUSCRIPT.md#ch-01)–[Ch 10](../en/book/MANUSCRIPT.md#ch-10): derivatives and gradients as attack maps, policies as predicates, physics of inputs, safe programming of model output, honest communication, Bayes and base rates, hardware, modular code and supply chain, ethics and the AI Act. | Labs G, B; EX001–EX030 |
| 11–19 Systems and security | [Ch 11](../en/book/MANUSCRIPT.md#ch-11)–[Ch 19](../en/book/MANUSCRIPT.md#ch-19): networks and quotas, OS sandboxes, data and RAG permissions, secure lifecycle and CI gates, CIA and taxonomy, systems engineering and FMEA, feedback loops, security architecture, identity and signed manifests. | Labs R, H; EX031–EX057 |
| 20–29 AI-security engineering I | [Ch 20](../en/book/MANUSCRIPT.md#ch-20)–[Ch 29](../en/book/MANUSCRIPT.md#ch-29): lifecycle and frameworks, verifiable requirements, DFDs and taint, threat analysis with ATLAS/OWASP, evasion/poisoning/privacy methods, studio, architecture patterns, control design, enforcement point, measurement. | Labs E, P, M, I, S; EX058–EX087 |
| 30–42 AI-security engineering II | [Ch 30](../en/book/MANUSCRIPT.md#ch-30)–[Ch 42](../en/book/MANUSCRIPT.md#ch-42): verification labs, monitoring and integrity, reliability and calibration, safety/resilience and oversight, integration, studio II safety case, unbounded consumption, operations and runbooks, validation and red teams, maintainability, optimisation, applied research. | Labs X, A, R, S, B; EX088–EX126 |
| 43–50 Practice and capstone | [Ch 43](../en/book/MANUSCRIPT.md#ch-43)–[Ch 50](../en/book/MANUSCRIPT.md#ch-50): placement and inventory, capstone baseline, independent design review, build, recovery trial, evidence dossier, thesis, defence. | Labs V, H, I; EX127–EX150 |

## Tutoring cycle

1. State the chapter's outcomes and ask one diagnostic question (e.g. "Where is the trust boundary in this agent?").
2. Teach with the NRS example; run the chapter's lab offline (Python 3 stdlib) and compare with the printed output. Labs are toy models, not production defences.
3. Assign the chapter's three exercises; grade 0–3 against the [worked results](../en/book/MANUSCRIPT.md#worked-results) after an attempt.
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

After the final chapter, check the chapter index and the learner's exercise record. The next stop is [course 136: Quantum and post-quantum security / Engineering course](../../quantum-post-quantum-security/en/SUBJECTS.md). A planned chapter does not count as studied merely because navigation points to it. Check the [book standard](../../../../BOOK_STANDARD.md) before claiming completion: English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
