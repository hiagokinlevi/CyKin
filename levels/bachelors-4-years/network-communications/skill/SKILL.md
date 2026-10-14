---
name: oca-network-communications-bachelor-b22a2301
description: "NET Bachelor's Course (40 ch / 120 ex)"
license: CC0-1.0
---

# Network and communications security — Bachelor's course course skill

Use this **one skill for the whole 4 years course**. The course has one principal book per language; each of its 40 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 103, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/network-communications/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Forty-chapter bachelor's route

This is the four-year **bachelor's course** for network and communications security. The book follows synthetic student **Priya Nair** of the fictional **Northbridge University**, supervised by **Dr Tomasz Kowal**, as she replaces the single shared wireless network of the fictional **Harbourside Community Clinics** with separate staff, clinical, guest and management groups, a default-deny firewall, individual staff accounts, current TLS and central logging.

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–18 | Foundations: reasoning, computing, programming, writing, security literacy, graphs, addressing, data, ethics, hosts, statistics, identity, privacy, measurement, architecture, cryptography, research methods | lab_cidr.py (7), lab_tls.py (17); EX001–EX054 |
| 19–30 | Field scope and cases, system models, logging, requirements and threats, firewall rules, labs, wireless and VPN, verification, failure analysis, operations | lab_syslog.py (22), lab_rules.py (24); EX055–EX090 |
| 31–40 | Advanced cases, interdisciplinary work, study design, option comparison, capstone proposal, field practice, evidence review, deployment, evaluation, thesis | lab_kappa.py (37); EX091–EX120 |

Verified lab facts (synthetic): clinical /25 has 126 usable hosts and one device (10.20.1.200) is unplanned; 3 of 8 services below TLS 1.2 (37.5%); syslog parse gives 3 warning, 1 error, 1 critical, 2 info, 1 malformed; rule 3 shadowed by rule 1 and rule 6 redundant to rule 5; reviewer agreement 0.85, chance 0.50, kappa 0.70.

## Teaching guardrails

- Synthetic data only; no exploit code, payloads, attack traffic, scanning or bypass steps.
- On-site tests only with written permission, in scheduled windows, against the partner's agreed scope.

## Continue the curriculum

After chapter 40, the next stop is [course 104: Systems, endpoints and hardware security / Bachelor's course](../../systems-endpoints-hardware/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
