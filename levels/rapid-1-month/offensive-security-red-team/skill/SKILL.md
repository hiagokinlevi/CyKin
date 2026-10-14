---
name: oca-offensive-security-red-team-rapid-bcdc3fa9
description: "Twenty English chapter-lessons for Riverside Civic College. Two synthetic labs stay byte-stable. EX001–EX066. No exploit code. Review still open."
license: CC0-1.0
---

# Authorized offensive security and red team — Rapid course course skill

Use this **one skill for the whole 1 month course**. The course has one principal book per language. Twenty English chapter-lessons are published. Read the manuscript and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 019, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and lesson status.
- [English book plan](../en/book/PLAN.md): summaries of the published lessons.
- [Materials](../en/MATERIALS.md): the embedded scope and ranking prints and their limits.
- [Supplementary playbooks](../../../../playbooks/offensive-security-red-team/README.md): source-linked practice.
- [Authored English book](../en/book/MANUSCRIPT.md): chapters 1–20, EX001–EX066. Review remains open.
- [Authored Portuguese (PT-BR) book](../pt/book/MANUSCRIPT.md): chapters 1–4 and EX001–EX050 only. It is not a translation of English chapters 5–20. Do not invent those Portuguese chapters while this review is open.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Teaching route

Maya Chen is a trainee at the fictional **Riverside Civic College**. This Riverside is the college in this course. The portal owner, the IT security lead, the manager, the classmate, and the emergency contact stay unnamed.

Do not edit `lab_scope.py` or `lab_findings.py`. The scope print stays:

```text
192.0.2.5      in scope
192.0.2.10     EXCLUDED - do not test
192.0.2.130    OUT OF SCOPE - do not test
198.51.100.7   OUT OF SCOPE - do not test
```

The ranking print stays:

```text
F1 score=6 high   Staff portal allows reused passwords
F3 score=6 high   Shared admin account on grading system
F4 score=4 medium Guest Wi-Fi reaches printer admin page
F2 score=2 low    Old web server banner shows version
```

Chapters 5–20: the scope lines follow `requested`; the excluded set is tested before the `/25`; that network ends at `.127`; `198.51.100.7` is outside even though it is a documentation address; width 14 is padding; the `else` sends no packet; the rank key is the negated product then the id; F1 precedes F3 on the id and F2 prints last; 6 is high and 4 is medium; F2 is 2 × 1; an impact of 3 for F4 is not this print; thirty days is prose; the blog and the clinic are outside both prints; the October dates and the weekday hours are not columns; T1078 names F3 and does not multiply. Lesson 20 title: "What the college note can say". `hiagokinlevi/offensive-gvuln` is supplementary and was not a control either script measured.

## Safety, privacy and information boundaries

- No exploit code, payloads, scan procedures, or instructions for attacking a system.
- The labs parse addresses and rank synthetic findings. They send no traffic.
- Written authorization is required before any real test. This course grants none.
- Do not invent a password, a phone number, a classmate's name, or a clinic address.

## Continue the curriculum

After chapter 20, the next stop is [course 020: AI and machine-learning security / Rapid course](../../ai-security/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapters 1–20 and exercise–answer pairs exist. The rapid planning minimum is 20 lessons. Independent review remains open. This is not a finished qualification. Page count is not the writing target. The Portuguese edition remains its own four-chapter manuscript. Do not translate chapters 5–20 while review is open.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
