---
name: cyberabc-security-operations-blue-team-technologist-08377b03
description: "SOC technologist course: 30 chapters, 90 exercises, 7 stdlib labs"
license: CC0-1.0
---

# Security operations and blue team — Technologist course course skill

Use this **one skill for the whole 3 years course**. The course has one principal book per language; each of its 30 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 084, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/security-operations-blue-team/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Thirty-subject teaching route

This is the three-year **technologist course** for security operations and blue team. The book follows synthetic student **Mei Tanaka** of the fictional **Harbourside Polytechnic** on placement with mentor **Raj Patel** at the fictional **Copperleaf Managed Security**: from a night-time RDP-guessing and new-admin-account incident at client **BrightSmile Dental**, through logging, baselines, detection, response, automation and evaluation, to a capstone ransomware early-warning package.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–10 | Foundations, log parsing, baselines, client onboarding | lab_parse.py (3), lab_baseline.py (9); EX001–EX030 |
| 11–20 | Detection, response, coverage, telemetry health | lab_rdp.py (14), lab_renames.py (15), lab_heartbeat.py (20); EX031–EX060 |
| 21–30 | Integration, automation, evaluation, research, handoff, field practice, capstone | lab_guard.py (22), lab_quality.py (23); EX061–EX090 |

Verified lab facts (synthetic): RDP guessing from 203.0.113.45 at 01:12, "reception" logon 01:19, support2 added to Administrators 01:22, rename spike from 01:34 above limit 30, isolation 01:36; CLINIC2-SRV heartbeat missing 95 min, CLINIC3-SRV stale 18 min; AV-disabled rule precision 0.10, recall 0.50.

## Safety, privacy and information boundaries

- Synthetic telemetry only; no exploit code, payloads, attack procedures or evasion guidance.
- Standard-library labs; automated actions only as allowed by client agreements and guarded.
- Validation tests use dedicated test accounts, scheduled and announced to the client.

## Continue the curriculum

After chapter 30, the next stop is [course 085: Incident response and cyber resilience / Technologist course](../../incident-response-resilience/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
