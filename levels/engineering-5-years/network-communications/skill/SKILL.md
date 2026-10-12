---
name: cyberabc-network-communications-engineering-7541b9e3
description: "NET Engineering Course (50 ch / 150 ex)"
license: CC0-1.0
---

# Network and communications security — Engineering course course skill

Use this **one skill for the whole 5 years course**. The course has one principal book per language; each of its 50 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 126, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/network-communications/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Fifty-chapter engineering route

This is the five-year **engineering course** for network and communications security. The book follows synthetic student **Kofi Mensah** of the fictional **Ravenmoor Institute of Technology**, supervised by **Dr Elena Vasquez**, as he replaces the flat network of the fictional **Ashcombe District Council** (eight offices, a guest-malware incident and a CCTV supplier appliance bypassing the firewall) with six zones, office firewalls, IKEv2 VPNs and monitoring.

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–17 | Foundations: probability, addressing, protocols, data, change, systems and feedback | lab_poisson.py (7), lab_subnet.py (11); EX001–EX051 |
| 18–34 | Requirements, threats, architecture options, zone policy, migration, monitoring, redundancy, integration | lab_reach.py (22), lab_policy.py (27), lab_flows.py (29), lab_avail.py (32); EX052–EX102 |
| 35–50 | Performance, operations, validation, optimisation, research, capstone, recovery trial, thesis and defense | lab_latency.py (36), lab_trace.py (38); EX103–EX150 |

Verified lab facts (synthetic): P(≥10 events) = 0.1904 at λ = 7.2; staff /22, guest and voice /23, servers and cctv /25, mgmt /27 with no overlaps; reachable zone pairs 30→7 (−76.7%); 4 of 8 flows allowed; 173 denies, 118 expected, 55 investigated; availability 0.995→0.999975 (43.80 h→0.22 h a year); added latency median 0.250, p95 0.918, max 0.950 ms within a 1.0 ms budget; 6 of 8 requirements covered before gaps were closed.

## Teaching guardrails

- Synthetic data only; no exploit code, payloads, attack traffic, scanning or bypass steps.
- Every policy change is reviewed, lab-tested against the regression suite and reversible.

## Continue the curriculum

After chapter 50, the next stop is [course 127: Systems, endpoints and hardware security / Engineering course](../../systems-endpoints-hardware/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
