---
name: cyberabc-systems-endpoints-hardware-bachelor-c42ef6f0
description: "SYS Bachelor's Course (40 ch / 120 ex)"
license: CC0-1.0
---

# Systems, endpoints and hardware security — Bachelor's course course skill

Use this **one skill for the whole 4 years course**. The course has one principal book per language; each of its 40 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 104, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/systems-endpoints-hardware/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Forty-subject teaching route

This is the four-year **bachelor's course** for systems, endpoint and hardware security. The book follows synthetic student **Aisha Rahman** of the fictional **Thornbury University**, tutored by **Dr Lewis Grant**, as she works with IT officer **Gareth Lloyd** to secure the 45 laptops and 4 servers of the fictional **Bramley Housing Association** after an unencrypted laptop was stolen.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–18 | Mathematics, computing, programming, writing, security literacy, discrete structures, networks, data, ethics, operating systems, statistics, identity, privacy, measurement, architecture, cryptography, research methods | lab_latency.py (12); EX001–EX054 |
| 19–30 | Scope and theory, cases, system models, inventory, baseline methods, controls, patch triage, server roles, encryption verification, failure analysis, operations, service reduction | lab_inventory.py (22), lab_baseline.py (23), lab_triage.py (25), lab_encrypt.py (27), lab_failures.py (28), lab_logons.py (29), lab_services.py (30); EX055–EX090 |
| 31–40 | Routine, recovery, research methods II, board reporting, proposal, practice, evidence review, implementation, evaluation, thesis | lab_compare.py (39); EX091–EX120 |

Verified lab facts (synthetic): patch latency mean 22.4 / median 12 / max 104 days, 26 of 45 within 14 days; register 49 vs reporting 47; baseline gaps encryption 13, local admin 25, screen lock 7, updates 6, firewall 1; 4 of 8 updates overdue; 40/45 encrypted at first check; 34 update failures (reboot 14); 2 of 7 logons flagged; 4 unneeded services; before/after encrypted 32→45, patched 26→41, services 4→0, unmanaged 6→1.

## Teaching guardrails

- Synthetic data only; no exploit code, payloads or bypass steps.
- Changes are piloted, logged and reversible; logs are used only for security and kept for a fixed period.

## Continue the curriculum

After chapter 40, the next stop is [course 105: Cloud and container security / Bachelor's course](../../cloud-containers/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
