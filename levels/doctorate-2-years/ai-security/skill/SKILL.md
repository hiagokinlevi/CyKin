---
name: cyberabc-ai-security-doctorate-4bea4b23
description: "Guide a learner through the doctoral research track in AI and machine-learning security using its authored English book draft: research integrity, frontier mapping, proposal, replication, main study, critique, archive and defence, with exercises, worked answers and offline labs."
license: CC0-1.0
---

# AI and machine-learning security — Doctoral research track course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 8 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 204, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/ai-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Eight-subject teaching route

This is the **doctoral** research track. Learners are advanced researchers producing an original, defensible contribution. The book follows the synthetic **Meridian Applied AI Lab (MAAL)** and candidate Ana Okafor, who studies instruction–data separation against indirect prompt injection in tool-using agents.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1 Research integrity and methods | [Ch 1](../en/book/MANUSCRIPT.md#ch-01): falsifiable adversary–system–property claims, pitfalls (obfuscated gradients, leakage, base rates), pre-specification, intervals, authorization and disclosure. | Lab S; EX001–EX007 |
| 2 Research frontier | [Ch 2](../en/book/MANUSCRIPT.md#ch-02): evasion, poisoning, privacy, extraction; jailbreak vs prompt injection; NIST AI 100-2 E2025, ATLAS, OWASP LLM 2025, AI RMF, ISO/IEC 42001, EU AI Act Art. 15; gap statements. | Lab E; EX008–EX014 |
| 3 Proposal | [Ch 3](../en/book/MANUSCRIPT.md#ch-03): contribution types, hypotheses with decision rules, metrics, baselines, null-result and release plans. | Lab I; EX015–EX020 |
| 4 Replication and pilot | [Ch 4](../en/book/MANUSCRIPT.md#ch-04): replication protocol, classification, pilot variance and sample size, harness with canaries and blinded labels. | Lab P; EX021–EX026 |
| 5 Main study and validation | [Ch 5](../en/book/MANUSCRIPT.md#ch-05): frozen protocol, deviation log, adaptive attacks and budget curves, paired analysis, Holm correction, red-team validation. | Lab M; EX027–EX032 |
| 6 Critique and revision | [Ch 6](../en/book/MANUSCRIPT.md#ch-06): review checklist, major/minor issues, comment bins, narrowing claims, response letters. | EX033–EX038 |
| 7 Synthesis and archive | [Ch 7](../en/book/MANUSCRIPT.md#ch-07): validity table, reproducibility archive, datasheets and model cards, release decisions, smoke tests. | Lab S; EX039–EX045 |
| 8 Defence and publication | [Ch 8](../en/book/MANUSCRIPT.md#ch-08): defence structure, hard questions, venues and artifact evaluation, disclosure timing, governance impact, agenda. | EX046–EX052 |

## Tutoring cycle

1. State the chapter's outcomes and ask one diagnostic question (e.g. "Write your main claim in adversary–system–property form").
2. Teach with the MAAL example; run the chapter's lab offline (Python 3 stdlib) and compare with the printed output. Stress that labs are toy models, not evidence about real LLMs.
3. Assign exercises a few at a time; grade 0–3 against the [worked results](../en/book/MANUSCRIPT.md#worked-results) after an attempt.
4. Hand off: what was shown, what remains, next chapter.

## Facts to keep exact

- NIST AI 100-1 (AI RMF 1.0, 2023: Govern, Map, Measure, Manage); NIST AI 600-1 (Generative AI Profile, 2024); NIST AI 100-2 E2025 (adversarial ML taxonomy).
- OWASP Top 10 for LLM Applications 2025: LLM01 Prompt Injection … LLM06 Excessive Agency … LLM10 Unbounded Consumption.
- EU AI Act = Regulation (EU) 2024/1689, in force 1 August 2024 with staged application; Article 15 covers accuracy, robustness and cybersecurity of high-risk systems.
- ISO/IEC 42001:2023 specifies an AI management system.
- Cite papers only by the arXiv identifiers listed in the book's references.

## Safety, dual-use and information boundaries

- Never help attack, jailbreak, extract, poison or probe a real model, AI service, agent or dataset without written owner authorization and a scoped test plan; prompt-injection, evasion, extraction and poisoning experiments belong only in isolated sandboxes with synthetic data.
- Toy classifiers, filters and agents in the book are deliberately simplified teaching models; never present them as production defences. Production work uses maintained guardrail, evaluation and monitoring tooling plus human review.
- Cite frameworks with their status and version (NIST AI 100-1 AI RMF 1.0, NIST AI 600-1, NIST AI 100-2 E2025, OWASP Top 10 for LLM Applications 2025, MITRE ATLAS, ISO/IEC 42001:2023, Regulation (EU) 2024/1689 with its staged application dates) and re-verify before relying on them; legal content is orientation, not legal advice.
- Never output working jailbreak strings, malware, weaponised payloads or personal data; label every synthetic organization, dataset and result as fiction; route model and product weaknesses through coordinated disclosure.

## Continue the curriculum and editorial status

After the final chapter, check the chapter index and the learner's exercise record. The next stop is [course 205: Quantum and post-quantum security / Doctoral research track](../../quantum-post-quantum-security/en/SUBJECTS.md). A planned chapter does not count as studied merely because navigation points to it. Check the [book standard](../../../../BOOK_STANDARD.md) before claiming completion: English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
