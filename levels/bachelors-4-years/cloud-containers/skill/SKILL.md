---
name: oca-cloud-containers-bachelor-5d95a195
description: "CLOUD Bachelor's course (40 ch / 120 ex)"
license: CC0-1.0
---

# Cloud and container security — Bachelor's course course skill

Use this **one skill for the whole 4 years course**. The course has one principal book per language; each of its 40 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 105, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/cloud-containers/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Forty-subject teaching route

This is the four-year **bachelor's course** for cloud and container security. The book follows synthetic student **Samuel Osei** of the fictional **Westmere University**, supervised by **Dr Clara Jensen** and working with cloud lead **Tom Becker**. It starts when Westmere's StudyHub registry is found allowing anonymous pulls of an image containing a database connection string, while audit logging was off in one account. From there it covers foundations, models, reviews, controls, verification and operations, and ends with a weekly posture report and pipeline secret-scan capstone.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–10 | Reasoning, computing, programming, writing, literacy, discrete structures, networks, data, ethics | lab_graph.py (6), lab_retention.py (9); EX001–EX030 |
| 11–20 | OS, statistics, identity, privacy, evidence, architecture, cryptography, research I, scope, cases | lab_stats.py (12), lab_mfa.py (13), lab_logging.py (15); EX031–EX060 |
| 21–30 | Models, dependencies, methods I, controls, lab I, methods II, verification, failure analysis, operations, lab II | lab_registry.py (23), lab_cis.py (26), lab_verify.py (27), lab_alerts.py (29); EX061–EX090 |
| 31–40 | Advanced cases, interfaces, research II, comparison, capstone, practice, evidence seminar, thesis | EX091–EX120 |

Verified lab facts (synthetic):
- **Role paths:** dev-alice and support-cy can reach cluster-admin.
- **Retention:** app-logs (120 days) and one test snapshot (210 days) are over retention.
- **Remediation stats:** mean 19.3, median 12.5, 11/20 fixed within 14 days, interval 0.33–0.77.
- **Accounts:** old-contractor has no MFA, a 400-day key and 220 days inactive.
- **Logging:** coverage 3/6.
- **Registry:** legacy-import is anonymous, 540 days old and never scanned.
- **Benchmark:** CIS-style score 4/7 = 57%.
- **Verification:** 4/5 passed (privileged pod admitted).
- **Alerts:** login-new-country was actionable 0/3, with a median acknowledgement of 45 min.

## Safety, privacy and information boundaries

- Synthetic configurations, logs and data only; no exploit code, payloads, attack procedures or instructions for bypassing controls.
- Standard-library labs that only read synthetic records; injected test events stay in test accounts.
- Credentials that are found are reported, never used or tested; student data never enters labs.

## Continue the curriculum

After chapter 40, the next stop is [course 106: Application and software supply chain security / Bachelor's course](../../application-supply-chain/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
