---
name: oca-identity-access-rapid-e00b477c
description: "Guide a learner through the published rapid identity and access book: twenty English chapters, two synthetic labs, and EX001–EX066. Review is still open."
license: CC0-1.0
---

# Identity and access management — Rapid course course skill

Use this **one skill for the whole 1 month course**. The English manuscript publishes twenty chapter-lessons. Other language folders are working outlines, not translations of those twenty English chapters. Read the actual manuscript and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 010, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/identity-access/README.md): source-linked practice.
- [Authored English book](../en/book/MANUSCRIPT.md): twenty chapters, two labs and EX001–EX066. Review remains open. This is not a finished qualification.

## Navigation rule

At the end of an authored chapter, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. The course chapter index connects its final row to the next course in the same language.

## Twenty-chapter rapid route

This is the one-month **rapid course** in identity and access management. The book follows synthetic learner **Mia Clarke**, coached by **Joseph Mensah** at the fictional **Eastgate Skills Centre**, as she helps **Rosa** at the fictional **Willow Lane Florist** (one shop, six staff). This florist is not the cryptography library case. Lessons 1–4 teach what the accounts protect, written permission and safe habits, the account list, and the checklist with the short report. Lessons 5–20 each settle one later question without replacing either laboratory print.

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–2 | Foundations, permission, password habits and stop cases | EX001–EX026 |
| 3–4 | The account list, the changes and the checklist | lab_accounts.py; lab_checklist.py; EX027–EX050 |
| 5–20 | One later florist question each | EX051–EX066 |

Verified lab facts (synthetic). Do not say either print was replaced.

```text
accounts 7, MFA on 3
no MFA: email (orders@shop) - shared
no MFA: online shop (admin) - shared
no MFA: social media (shop-page) - shared
no MFA: supplier portal (willowlane)
shared accounts: 3
```

```text
before: 2/8
after: 7/8
still to do: recovery details up to date
```

## Teaching guardrails

- Do not edit `lab_accounts.py` or `lab_checklist.py`. Do not print MFA on 7, shared 0, or 8/8.
- The account print is the week-three list. Week-four changes stay prose and do not rewrite that print.
- Three second-step rows stay Rosa's own email, card payments `rosa.m`, and accounting `rosa.m`. The four no-MFA lines stay.
- Shared stays 3: the orders mailbox, the shop admin, and the social page. The supplier portal stays not shared.
- The orders mailbox line stays `no MFA: email (orders@shop) - shared`. "MFA on email" stays a separate before-item.
- The shop admin users stay Rosa and Mia. The staff role stays prose. No new name is added.
- The social page stays `shop-page`, all staff, no MFA, and shared. The former helpers stay unnamed.
- The supplier portal stays `willowlane`, Rosa, no MFA, not shared, and next. "If time allows" is not done.
- Recovery details stay the remaining item. No phone number is printed. The after score stays 7/8.
- The before set stays the owner line and "MFA on email." Three former staff were removed, and no date or name is printed.
- No password is written. The till note stays shredded in the story. The manager stays the store.
- No permission date is printed. Rosa contacts the provider or the bank. Payments stay hers. Mia stops and does not investigate.
- The three-month check is a habit, not a second run. Six staff and one shop stay the size. Joseph is not shop staff.
- Admin stays Rosa and Mia. The staff role may view and pack orders, not change prices or payment settings. No lockout is recorded.
- Do not teach exploit steps, payloads or bypasses. Defender-side synthetic material only. Never collect a password.
- Willow Lane Florist is not Willow Lane Community Library. Do not merge the cases.
- After chapter 20 the next stop in this level is course 011. Do not call the florist secure. Twenty lessons meet the planning minimum and leave review open.

## Continue the curriculum

After chapter 20, the next stop is [course 011: Network and communications security / Rapid course](../../network-communications/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapters 1–20 and EX001–EX066 are published, and independent review remains open. Page count is not the writing target. This is not a finished qualification. Other language folders keep their own state until their own writing and review.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
