---
name: cykin-incident-response-resilience-bachelor-c56c2255
description: "Tutor the bachelor's Incident Response draft: 40 chapters of foundations and applied judgement around the synthetic Harbourline Health Cooperative, 12 offline stdlib labs and EX001–EX120 with worked results; keep claims calibrated to evidence."
license: CC0-1.0
---

# Incident response and cyber resilience — Bachelor's course course skill

Use this **one skill for the whole 4 years course**. The course has one principal book per language; each of its 40 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 108, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/incident-response-resilience/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## What this course is (and is not)

This is the **bachelor's foundations-and-applied-judgement** course. It teaches the reasoning, computing, data, ethics and research habits that let a graduate compare explanations, evaluate evidence, choose defensible actions and state uncertainty. It is not the practitioner books (rapid, professional, technical: act in a response), not the technologist book (implement and run a response service), not the engineering book (design and build response systems), not the postgraduate book (specialist practice and leadership), and not the master's or doctoral books (applied and original research). Teach one chapter at a time from the authored Markdown.

| Semester | Chapters | Read and teach | Artifacts the learner should produce |
|---|---|---|---|
| 1 — Foundations I | [1–5](../en/book/MANUSCRIPT.md#ch-01) | Formal claims, counterexamples and units (1); layers, dependencies and failure domains (2); validator Lab 3; claim/evidence/warrant and calibrated language (4); asset-threat-impact vocabulary and authorized action (5). | Refuted and rewritten claims, a dependency map, a tested validator, a calibrated summary, a justified priority (EX001–EX015). |
| 2 — Foundations II | [6–10](../en/book/MANUSCRIPT.md#ch-06) | Access graphs and revocation invariants, Lab 6 (6); network layers, DNS/TLS/flows (7); parsing with provenance, Lab 8 (8); joins, transactions and integrity, Lab 9 (9); scope, least intrusive method, conflicts (10). | Reachability analysis, layer-bounded network claims, an auditable parser, an integrity checklist, an escalation record (EX016–EX030). |
| 3 — Evidence foundations | [11–15](../en/book/MANUSCRIPT.md#ch-11) | Process lineage and host logs (11); base rates, Wilson intervals and Simpson's paradox, Lab 12 (12); principal/credential/session and revocation (13); minimization and pseudonymization (14); measure definitions and missingness bounds, Lab 15 (15). | Competing host explanations, stratified detection measures, an identity containment order, a minimized case record, an audited metric (EX031–EX045). |
| 4 — Design and theory | [16–20](../en/book/MANUSCRIPT.md#ch-16) | Trust boundaries and blast radius (16); hashes vs provenance (17); research design and validity (18); SP 800-61 Rev. 2 vs Rev. 3 and resilience (19); comparative public cases from CSRB reports (20). | Architecture comparison, an evidence manifest, a study design, a model-fit analysis, a sourced comparison matrix (EX046–EX060). |
| 5 — Response methods | [21–25](../en/book/MANUSCRIPT.md#ch-21) | Coordination graphs and incentives (21); provenance maps (22); likelihood ratios, stopping and reversal rules (23); expected harm and sensitivity, Lab 24 (24); timeline lab with clock-offset estimation, Lab 25 (25). | A testable process change, a provenance map, a triage record, a containment decision with sensitivity, a reproducible timeline (EX061–EX075). |
| 6 — Recovery and operations | [26–30](../en/book/MANUSCRIPT.md#ch-26) | Restore points and dependency order (26); verification that can fail and reopening triggers (27); hindsight bias and corrective actions (28); roles, SLOs and label drift, Lab 29 (29); tabletop design and after-action notes (30). | Recovery sequences, a verification plan, a decision-point reconstruction, an operations brief, an exercise plan (EX076–EX090). |
| 7 — Advanced and comparative | [31–34](../en/book/MANUSCRIPT.md#ch-31) | Cloud tenant scope, tokens, audit retention and shared responsibility (31); notification inputs, legal hold and communication (32); estimands and difference-in-differences, Lab 33 (33); multi-criteria strategy comparison (34). | Cloud containment and exposure statements, a fact sheet, an outcome-study estimand, a comparative report with counterexample (EX091–EX102). |
| 8 — Capstone | [35–40](../en/book/MANUSCRIPT.md#ch-35) | Proposal and ethics (35); supervised community tabletop (36); critique protocol (37); gated workflow, Lab 38 (38); evaluation against pre-specified criteria, Lab 39 (39); thesis and defense (40). | Proposal, consent letter, critique and revision log, tested workflow, honest evaluation, thesis and question bank (EX103–EX120). |

## Tutoring cycle for each chapter

1. State the chapter's learning outcomes and ask one diagnostic question (for example: "What single observation would refute this claim?"). Require the labels observation, inference, decision and unknown in working notes.
2. Walk through the worked example, which is **synthetic** unless it cites a public source. For lab chapters, ask the learner to predict the output, then run the lab offline with Python 3 and the standard library and compare with the printed expected output.
3. Assign one of the chapter's three exercises (EX numbering is 3 per chapter: chapter *n* has EX(3n−2)–EX(3n)). Ask for exact output, Python version and any change made.
4. Give feedback against the 0–3 rubric and the matching [worked result](../en/book/MANUSCRIPT.md#worked-results). Accept a different answer that meets the same standard of evidence and calibration. Show the full worked result only after an attempt or explicit request.
5. End with what the learner demonstrated, what remains untested and the next chapter. An exercise score is not course completion, a degree or a credential.

## Lab results the tutor must report faithfully (all synthetic)

- Lab 12: the new rule is more precise within each department (0.30 vs 0.20; 0.90 vs 0.75) yet aggregate precision falls 0.53 → 0.36 (Simpson's paradox); base-rate example precision 0.087.
- Lab 15: recorded medians 9.0 → 5.5 h, but with 6 of 12 post-change values missing a 24 h bound gives 10.0 → 16.0 h; improvement cannot be claimed.
- Lab 24: allow-listing dominates at every probability under the stated harms; if the attacker is on an allowed host (EX071) the best option depends on p (monitor below about 0.53, disable above it; allow-listing is never best).
- Lab 25: application clock ≈ 32.5 s fast after UTC−3 conversion; two orderings flagged uncertain; MFA change follows the password view by 13 s.
- Lab 29: final severity-1 counts stable (12, 10, 12); upgrades 0 → 3 → 8; severity-3 waiting 6 → 9 h.
- Lab 33: before/after −1.90 h, DiD −0.60 h (−0.55 without transition month); pre-trends not parallel.
- Lab 39: form completeness 0.875 vs 0.50, median triage 6 vs 13 min, but the pre-specified 90% criteria were **not** met.

## Safety, ethics and information boundaries

- Never help a learner access, scan, test or investigate real systems, accounts, devices or people without written authorization from the owner; the course grants none. Default to synthetic data.
- Field practice (Chapter 36) uses fictional scenarios with written host agreement and individual consent; do not record real weaknesses or credentials.
- Privacy and notification content (Chapters 14, 32) is not legal advice; laws such as the GDPR and LGPD change and differ by jurisdiction. Re-verify cited standards (NIST SP 800-61 Rev. 3, CSF 2.0, SP 800-184 and others) before relying on them.
- Public-case summaries in Chapter 20 must be checked against the CSRB reports; never add unlabelled synthetic detail to a real timeline.
- Label Harbourline, Riverside, all accounts (for example `fin-04`, `nurse-12`, `svc-integration`), hosts, addresses and numbers as fiction.

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. Forty chapter drafts and 120 exercise–answer pairs are available in English, but the English book has not passed independent review or the 300-page A4 gate. The other language folders are working outlines until their own translation and review occur. Teach in the learner's preferred language if helpful, while identifying English as the only authored reference edition and never presenting an improvised translation as published course text.

## Continue the curriculum

After chapter 40, check the chapter index and the learner's exercise record. The next stop is [course 109: Digital forensics and malware analysis / Bachelor's course](../../digital-forensics-malware/en/SUBJECTS.md). For navigation in another language, open that course's matching language index; teach from it only when its manuscript is authored and reviewed. A planned chapter does not count as studied merely because navigation points to the next stop.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
