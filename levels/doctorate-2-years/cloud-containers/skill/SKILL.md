---
name: cyberabc-cloud-containers-doctorate-8a31192f
description: "CLOUD Doctoral research book (8 ch / 50 ex)"
license: CC0-1.0
---

# Cloud and container security — Doctoral research track course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 8 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 197, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/cloud-containers/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Eight-subject teaching route

This is the two-year **doctoral research track** for cloud and container security. The book follows synthetic doctoral candidate **Amara Okoye** of the fictional **Thornfield University**, supervised by **Prof. Henrik Lund**, with the fictional partner **Meridian Health Cloud**. It starts with a privileged log collector that stayed live for eleven months even though the daily scan reported it. From there it covers a measured comparison of admission-time Pod Security enforcement against daily scanning, and ends with a verified archive and the defence.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–3 | Integrity and method, research frontier, contribution proposal | lab_kappa.py (3); EX001–EX020 |
| 4–5 | Baseline replication and pilot, main study and validation | lab_baseline.py (4), lab_window.py (5); EX021–EX032 |
| 6–8 | Critique and revision, thesis and archive, defence and publication | lab_archive.py (7); EX033–EX050 |

Verified lab facts (synthetic): labelling agreement is 0.94 against 0.51 by chance, kappa 0.88; the pod checks find 7 violations, with 1/5 pods compliant and log-agent showing all 4; median exposure is 14.5 h under daily scanning and 0.0 h under admission, a difference of 14.5 h (95% bootstrap interval 10.5–18.5, seed 7); the archive check verifies 3/4 files, with config/policies.yaml changed.

## Safety, privacy and information boundaries

- Synthetic configurations, logs and data only; no exploit code, payloads, attack procedures or instructions for bypassing controls.
- Standard-library labs that only read synthetic records; partner data never leaves the partner and holds no patient data or secrets.
- Research is reviewed by an ethics board, and no individual performance data are used.

## Continue the curriculum

After chapter 8, the next stop is [course 198: Application and software supply chain security / Doctoral research track](../../application-supply-chain/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
