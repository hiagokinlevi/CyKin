---
name: cyberabc-application-supply-chain-rapid-2dd7bc2a
description: "APP Rapid course (4 ch / 50 ex)"
license: CC0-1.0
---

# Application and software supply chain security — Rapid course course skill

Use this **one skill for the whole 1 month course**. The course has one principal book per language; each of its 4 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 014, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/application-supply-chain/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Four-subject teaching route

This is the one-month **rapid course** for application and software supply chain security. The book follows **Owen Clarke**, the only IT person at the fictional charity **Riverside Food Network**, who studies at the fictional **Kestrel Skills Centre** with tutor **Nadia Haddad**. It starts when a donation page shows an error mentioning an outdated form component, and nobody knows which components the site uses. From there it covers proportionate decisions, permission and safe practice, and the site's components, data and dependencies, and ends with a guided release lab and lasting routines.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–2 | Foundations and decisions; scope, permission and safe practice | EX001–EX026 |
| 3–4 | Systems, data and dependencies; guided lab and applied synthesis | lab_deps.py (3), lab_release.py (4); EX027–EX050 |

Verified lab facts (synthetic): donate-form needs an update from 3.2.0 to 3.2.4; event-calendar is UNMAINTAINED (1606 days); photo-gallery should be REMOVED because it is not in use; newsletter is ok; the release checklist passes 4 of 5 items and reports NOT READY: admin accounts use MFA.

## Safety, privacy and information boundaries

- Synthetic code and data only; no exploit code, payloads, attack procedures or instructions for bypassing controls.
- Standard-library labs that only read synthetic records.
- Changes need written permission, a tested backup and a staging copy with synthetic donor data.

## Continue the curriculum

After chapter 4, the next stop is [course 015: Security operations and blue team / Rapid course](../../security-operations-blue-team/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
