---
name: cykin-application-supply-chain-professional-2f79da44
description: "APP Professional course (12 ch / 60 ex)"
license: CC0-1.0
---

# Application and software supply chain security — Professional course course skill

Use this **one skill for the whole 6 months course**. The course has one principal book per language; each of its 12 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 037, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/application-supply-chain/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Twelve-subject teaching route

This is the six-month **professional course** for application and software supply chain security. The book follows synthetic quality engineer **Priya Nair** of the fictional **Harbourline Freight**, who studies at the fictional **Westgate Professional Institute** under her mentor, security lead **Marcus Bell**. It starts with an internal package, hl-auth, that the build resolved from the public registry. From there it covers the service context, authorised practice, source controls, scanner triage, workflow and targets, controls and provenance, a supervised case, reporting, quality and a supervised lab, and ends with a portfolio.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–4 | Foundations, stakeholder context, authorised practice, source and name checks | lab_sources.py (4); EX001–EX020 |
| 5–8 | Scanner triage, workflow, controls and verification, supervised case | lab_triage.py (5); EX021–EX040 |
| 9–12 | Reporting and ethics, quality and remediation targets, supervised lab, portfolio | lab_sla.py (10); EX041–EX060 |

Verified lab facts (synthetic): the source check flags hl-auth as an internal name resolved from the PUBLIC registry and flags yamkit as close to yamlkit; triage turns 7 raw findings into 6 unique ones, ranks sql-concat, ADV-22 and missing-authz first, and puts critical ADV-21 fourth because it is not reachable; targets were met for critical 1/2 (50%, longest 9d), high 3/4 (75%, 41d) and medium 3/4 (75%, 120d).

## Safety, privacy and information boundaries

- Synthetic code and data only; no exploit code, payloads, attack procedures or instructions for bypassing controls.
- Standard-library labs that only read synthetic records; nothing is published to public registries and no public names are tested.
- Findings are reported only through official channels and private disclosure.

## Continue the curriculum

After chapter 12, the next stop is [course 038: Security operations and blue team / Professional course](../../security-operations-blue-team/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
