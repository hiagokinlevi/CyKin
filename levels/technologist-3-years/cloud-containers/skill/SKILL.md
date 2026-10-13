---
name: cykin-cloud-containers-technologist-308aed90
description: "CLOUD Technologist Course (30 ch / 90 ex)"
license: CC0-1.0
---

# Cloud and container security — Technologist course course skill

Use this **one skill for the whole 3 years course**. The course has one principal book per language; each of its 30 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 082, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/cloud-containers/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Thirty-subject teaching route

This is the three-year **technologist course** for cloud and container security. The book follows synthetic student **Priya Nair** of the fictional **Northgate Polytechnic** on placement at the fictional **Cobalt Hosting**, mentored by **Kwame Asante**, with client **Riverside Dental Group**. It starts with an image advisory that took six hours to answer because nobody knew which workloads ran which images.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–10 | Foundations: computing, networks, scripting, data models, security literacy, virtualization, identity, architecture, evidence, orientation | EX001–EX030 |
| 11–15 | Inventory, data flows, risk scenarios, baseline method, guided lab | lab_inventory.py (11), lab_flows.py (12), lab_baseline.py (15); EX031–EX045 |
| 16–23 | Workload controls, tooling, controls, monitoring, troubleshooting, integration, automation, evaluation | lab_logs.py (19), lab_iac.py (22), lab_compare.py (23); EX046–EX069 |
| 24–30 | Research methods, team studio, handoff, deployment, field practice, capstone | lab_handoff.py (27); EX070–EX090 |

Verified lab facts (synthetic): 3 of 8 workloads ran unapproved images (booking node:14, cron python:3.6, reports); 6 of 8 flows cross a boundary and booking→email is unencrypted; baseline client-a 5/6, client-b 1/6, internal 5/6; 66 audit events with 4 lines for review; 3/5 changes blocked; unapproved images 3→1, baseline failures 7→2, advisory time 6h→0.5h; handoff 6/8 items present.

## Safety, privacy and information boundaries

- Synthetic configurations, records and data only; no exploit code, payloads, attack procedures or instructions for bypassing controls.
- Standard-library labs that only read synthetic records.
- Placement work uses read-only access under supervision; no client systems are tested for weaknesses.

## Continue the curriculum

After chapter 30, the next stop is [course 083: Application and software supply chain security / Technologist course](../../application-supply-chain/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
