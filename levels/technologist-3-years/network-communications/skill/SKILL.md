---
name: cykin-network-communications-technologist-1f3a9d0c
description: "NET Technologist Course (30 ch / 90 ex)"
license: CC0-1.0
---

# Network and communications security — Technologist course course skill

Use this **one skill for the whole 3 years course**. The course has one principal book per language; each of its 30 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 080, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/network-communications/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Thirty-chapter technologist route

This is the three-year **technologist course** for network and communications security. The book follows synthetic student **Tomás Rivera** of the fictional **Greystone Polytechnic**, taught by **Hannah Okafor**, on placement at the fictional **Ridgeway Secondary School**, where one technician runs a flat network. Together they build six zones, default-deny rules, individual wireless accounts, encrypted management, central logs, tuned alerts and safe automation.

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–10 | Computing, networks, scripting, data, security literacy, OS and virtualisation, identity, architecture, measurement, orientation | EX001–EX030 |
| 11–20 | Assets, flows, scenarios, requirements, guided lab, wireless and remote access, tooling, controls, monitoring, troubleshooting | lab_dns.py (12), lab_services.py (15), lab_alerts.py (19); EX031–EX060 |
| 21–30 | Supplier integration, automation, evaluation, applied research, team studio, handoff, deployment, field practice, capstone | lab_diff.py (22), lab_mttr.py (23); EX061–EX090 |

Verified lab facts (synthetic): 6 of 12 DNS lookups blocked (50%), one newly registered domain repeated 3 times; 4 unapproved services, 0 missing; alert precision 0.56 overall, 0.10 for the DNS heuristic; drift shows 2 changed lines (port 2 zone, Telnet); median ticket time 92.5→47.5 min (−48.6%).

## Teaching guardrails

- Synthetic data only; no exploit code, payloads, attack traffic, scanning or bypass steps.
- Observed services come from the systems' own authorised exports, never from scanning.

## Continue the curriculum

After chapter 30, the next stop is [course 081: Systems, endpoints and hardware security / Technologist course](../../systems-endpoints-hardware/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
