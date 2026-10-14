---
name: oca-security-operations-blue-team-rapid-10bf3a49
description: "Twenty English chapter-lessons for Marlow & Finch. One synthetic lab stays byte-stable. EX001–EX066. Review still open."
license: CC0-1.0
---

# Security operations and blue team — Rapid course course skill

Use this **one skill for the whole 1 month course**. The course has one principal book per language. Twenty English chapter-lessons are published. Read the manuscript and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 015, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and lesson status.
- [English book plan](../en/book/PLAN.md): summaries of the published lessons.
- [Materials](../en/MATERIALS.md): the embedded sign-in print and its limits.
- [Supplementary playbooks](../../../../playbooks/security-operations-blue-team/README.md): source-linked practice.
- [Authored English book](../en/book/MANUSCRIPT.md): chapters 1–20, EX001–EX066. Review remains open.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Teaching route

Leo Barros is office manager at the fictional 12-person accountancy **Marlow & Finch**. Partner Elaine Finch's mailbox was misused. **BrightPath IT** is the fictional outside support. A client phones on Monday because an email asked for payment to a new bank account. Elaine sent no such email.

Do not edit `lab_signins.py`. The only lab print stays:

```text
e.finch   Fri 08:52 UK ok
e.finch   Fri 13:05 UK ok
e.finch   Fri 23:47 BR CHECK: new country, night
s.marlow  Fri 09:10 UK ok
l.barros  Fri 08:30 UK ok
e.finch   Sat 00:02 BR CHECK: new country, night
```

Chapters 5–20: the six tuples stay in list order and width 9 is padding; the two flags are independent tests and this print has no one-flag row; night is `hour < 6 or hour >= 22`, so 22:00 is night and 06:00 is not; `usual` is `{"UK"}` and `BR` is a stored label; 23:51 minus 23:47 is four minutes and the rule is not a lab column; twelve mailboxes are prose and the script prints six rows; 10:08 to 10:20 is twelve minutes and 10:09 to 10:20 is eleven; £3,100 is not the whole £4,800; the client warning has no phone number; 8 plus 2 plus 1 is 11 and attacks were 0; the travel list does not delete the abroad signal; MFA and the phone-check are done, training is booked, and the admin check was not done in the meeting; the weekly summary is not the yearly plan check; the later phish report is not a seventh tuple; one client folder is a plan, not a score. Lesson 20 title: "What the firm note can say". No digest, bank name, outside address, or success rate is printed. `hiagokinlevi/honeypot-foundry` is supplementary and was not a row the sign-in script measured.

## Safety, privacy and information boundaries

- Synthetic data only; no exploit code, payloads, attack procedures or evasion guidance.
- Standard-library lab that only reads synthetic sign-in tuples.
- Mailbox checks only by authorised IT support under the firm's signed plan.
- Do not name the bank, the email provider, the outside address, or a phone number.

## Continue the curriculum

After chapter 20, the next stop is [course 016: Incident response and cyber resilience / Rapid course](../../incident-response-resilience/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapters 1–20 and exercise–answer pairs exist. The rapid planning minimum is 20 lessons. Independent review remains open. This is not a finished qualification. Page count is not the writing target. Portuguese and Spanish remain plans until their own manuscripts exist. Do not translate this book while review is open.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
