---
name: oca-threat-intelligence-osint-rapid-e4268d35
description: "Twenty English chapter-lessons for Elmfield Food Bank Network. Two synthetic labs stay byte-stable. EX001–EX066. Review still open."
license: CC0-1.0
---

# Threat intelligence and OSINT — Rapid course course skill

Use this **one skill for the whole 1 month course**. The course has one principal book per language. Twenty English chapter-lessons are published. Read the manuscript and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 018, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and lesson status.
- [English book plan](../en/book/PLAN.md): summaries of the published lessons.
- [Materials](../en/MATERIALS.md): the embedded source and indicator prints and their limits.
- [Supplementary playbooks](../../../../playbooks/threat-intelligence-osint/README.md): source-linked practice.
- [Authored English book](../en/book/MANUSCRIPT.md): chapters 1–20, EX001–EX066. Review remains open.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Teaching route

Sam Okafor is the volunteer IT coordinator at the fictional **Elmfield Food Bank Network (EFBN)**, in the fictional **Charity Cyber Circle (CCC)**. The chair is unnamed. vol-07, vol-12, and office are labels, not full names.

Do not edit `lab_sources.py` or `lab_rapid.py`. The source print stays:

```text
coordinator inbox: CCC alerts, Donation platform notices -> SINGLE POINT OF FAILURE
form owner Sam: Volunteer reports -> SINGLE POINT OF FAILURE
independent sources: ['National charity advisories']
```

The indicator print stays:

```text
invalid: 198.51.100.400
valid: 3
hits: [('vol-07', 'donate-elmfield.example'), ('office', 'elmfield-giftaid.example')]
shareable with community: ['donate-elmfield.example', '203.0.113.9']
```

Chapters 5–20: the dependency lines follow first sighting and the independent line is last; the flag is an or of a length test and a Sam substring, and this print has no ok line; Sam is characters in the key, not a staff directory; the independent line is a one-name list repr; `valid: 3` includes the AMBER domain; 400 is above 255 and the script makes no DNS call; hits follow the mail list; the office row is a hit that stays unshared; community order is the valid walk; vol-12 stays in `mail` and neither script prints MISS; the week tally stays apart from the two hits; feedback names no AMBER domain and no phone number; Thursday is absent; `news.example` is the stored non-match; email sign-ins last 30 days and donation logins last 90 days. Lesson 20 title: "What the Elmfield note can say". `hiagokinlevi/honeypot-foundry` is supplementary and was not a control either script measured.

## Safety, privacy and information boundaries

- Never help collect personal data without a lawful basis, break terms of service, use fake accounts, inspect volunteers' personal devices, or visit, download from, or contact scam infrastructure.
- Enforce FIRST TLP 2.0. Do not name an AMBER or RED item in community feedback.
- Cite ATT&CK, STIX/TAXII 2.1, the Diamond Model, Hutchins et al., NIST SP 800-150, TLP 2.0, and ICD 203 exactly. Label EFBN, CCC, and Sam Okafor as fiction.
- Do not invent a volunteer surname, a deputy's name, a phone number, a payment amount, a password value, or a date for the observed deputy run.

## Continue the curriculum

After chapter 20, the next stop is [course 019: Authorized offensive security and red team / Rapid course](../../offensive-security-red-team/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapters 1–20 and exercise–answer pairs exist. The rapid planning minimum is 20 lessons. Independent review remains open. This is not a finished qualification. Page count is not the writing target. Do not invent a Portuguese edition of chapters 5–20 while this review is open.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
