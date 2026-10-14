---
name: oca-network-communications-postgraduate-339ffa34
description: "NET Postgraduate Course (12 ch / 60 ex)"
license: CC0-1.0
---

# Network and communications security — Postgraduate course course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 12 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 149, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/network-communications/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Twelve-chapter postgraduate route

This is the two-year **postgraduate course** for network and communications security. The book follows synthetic specialist **Marta Lindqvist** of the fictional **Kestrel Graduate School**, supervised by **Prof. Aiyana Brooks**, as she helps the fictional community provider **Fenwick Valley Broadband** move VPN peers to IKEv2 with certificates (RFC 7296, SP 800-77r1), stage route origin validation (RFC 6480, SP 800-189) and enforce ingress filtering (RFC 2827).

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–4 | Decision-making, current practice, specialist evidence, risk and ethics | lab_peers.py (3); EX001–EX020 |
| 5–8 | Design alternatives, controlled evaluation, organisational integration, difficult cases | lab_rov.py (5), lab_ingress.py (6); EX021–EX040 |
| 9–12 | Leadership and assurance, research critique, applied project, final review and transfer | EX041–EX060 |

Verified lab facts (synthetic): 5 of 8 VPN peers need action (3 IKEv1, 5 pre-shared keys all older than a year); origin validation gives 4 valid, 3 invalid, 1 not found; ingress check drops 3 of 10 packets (30%).

## Teaching guardrails

- Synthetic data only; no exploit code, payloads, attack traffic, scanning or bypass steps.
- Enforcement is staged: monitor or soft-enforce first, with pre-set criteria and a reversal procedure.

## Continue the curriculum

After chapter 12, the next stop is [course 150: Systems, endpoints and hardware security / Postgraduate course](../../systems-endpoints-hardware/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
