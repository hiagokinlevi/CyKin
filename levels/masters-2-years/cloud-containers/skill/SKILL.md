---
name: cyberabc-cloud-containers-masters-8a675037
description: "CLOUD Master's course (8 ch / 50 ex)"
license: CC0-1.0
---

# Cloud and container security — Master's course course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 8 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 174, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/cloud-containers/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Eight-subject teaching route

This is the two-year **master's course** for cloud and container security. The book follows synthetic master's student **Lucas Moreau** of the fictional **Ashcombe University**, supervised by **Dr Mei Tanaka**, studying the fictional **Larkspur Retail**. It starts with a storage bucket created by hand in the console that stayed public for nine days. It then tests three competing explanations (console error, weak IaC defaults and identity breadth) against a year of change records.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–3 | Question and literature, advanced seminar, study design and ethics | lab_iam.py (2); EX001–EX020 |
| 4–6 | Competing explanations, proposal and pilot, data collection and analysis | lab_buckets.py (5), lab_origin.py (6); EX021–EX038 |
| 7–8 | Writing and limitations, independent review and defence | EX039–EX050 |

Verified lab facts (synthetic): 4/11 granted permissions (36%) went unused, and analytics-job did not use db.admin or storage.write; 3 of 6 buckets are public (marketing-assets, tmp-export-0412, partner-drop); exposure was 1.0% for IaC (12/1200) and 4.5% for console changes (27/600), chi-square 23.1 (df 1), p 1.5e-06, risk ratio 4.5.

## Safety, privacy and information boundaries

- Synthetic configurations, records and data only; no exploit code, payloads, attack procedures or instructions for bypassing controls.
- Standard-library labs that only read synthetic records.
- Engineer identities are pseudonymised, small teams are merged, and results are never used to assess individuals.

## Continue the curriculum

After chapter 8, the next stop is [course 175: Application and software supply chain security / Master's course](../../application-supply-chain/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
