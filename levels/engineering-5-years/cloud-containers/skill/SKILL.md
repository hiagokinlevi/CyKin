---
name: cyberabc-cloud-containers-engineering-9b1133e6
description: "CLOUD Engineering course (50 ch / 150 ex)"
license: CC0-1.0
---

# Cloud and container security — Engineering course course skill

Use this **one skill for the whole 5 years course**. The course has one principal book per language; each of its 50 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 128, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/cloud-containers/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Fifty-subject teaching route

This is the five-year **engineering course** for cloud and container security. The book follows synthetic engineering student **Elena Petrova** of the fictional **Brackenridge Institute of Technology**, supervised by **Rosa Delgado** in industry and **Dr Felix Wagner** academically. The project is with the fictional **Solent Energy Co-op**, whose smart-meter platform meterhub pushed an image with a cloud key built in to a public registry and ran without network policies. From there it covers engineering foundations, requirements, models, controls, verification, operations and a secure-namespace capstone, and ends with the defence.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–10 | Mathematics, physics, programming, communication, ethics | lab_policy.py (2), lab_latency.py (7); EX001–EX030 |
| 11–20 | Networks, OS, data, software, security, systems, feedback, architecture, identity, context | lab_caps.py (12), lab_autoscale.py (17), lab_secrets.py (19); EX031–EX060 |
| 21–30 | Requirements, models, threats, methods, studio, alternatives, control design, implementation, measurement, verification I | lab_netpol.py (24), lab_coverage.py (29); EX061–EX090 |
| 31–40 | Implementation II, reliability, resilience, integration, studio II, performance, operations, validation, maintainability, verification II | lab_overhead.py (36), lab_drift.py (40); EX091–EX120 |
| 41–50 | Optimisation, applied research, practice, capstone, review, trial, dossier, thesis, defence | EX121–EX150 |

Verified lab facts (synthetic):
- **Policy:** default deny and explicit deny override, with 2 ALLOW, 2 DENY (explicit) and 1 DENY (default).
- **Latency:** mean 13.2, median 6.5, p95 40.9 min.
- **Capabilities:** node-agent has NET_ADMIN and SYS_ADMIN extra.
- **Autoscaling:** 2→3→8→10 (capped)→10→7.
- **Secrets:** CLOUD_ACCESS_KEY entropy 4.50, likely secret.
- **Network reachability:** 12/12 → 4/12.
- **Coverage:** 10/16 = 62%.
- **Admission overhead:** median 265.0→284.5 ms, p95 505.5→541.8 ms.
- **Drift:** 3/6 settings drifted.

## Safety, privacy and information boundaries

- Synthetic configurations, logs and data only; no exploit code, payloads, attack procedures or instructions for bypassing controls.
- Standard-library labs that only read synthetic records; verification uses synthetic test workloads in test clusters.
- Trials need written approval, synthetic data, abort criteria and named observers.

## Continue the curriculum

After chapter 50, the next stop is [course 129: Application and software supply chain security / Engineering course](../../application-supply-chain/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
