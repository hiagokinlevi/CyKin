---
name: oca-cloud-containers-rapid-4331f7e6
description: "Guide a learner through the published rapid cloud book: twenty English chapters, two synthetic labs, and EX001–EX066. Review is still open."
license: CC0-1.0
---

# Cloud and container security — Rapid course course skill

Use this **one skill for the whole 1 month course**. The English manuscript publishes twenty chapter-lessons. Other language folders are working outlines, not translations of those twenty English chapters. Read the actual manuscript and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 013, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/cloud-containers/README.md): source-linked practice.
- [Authored English book](../en/book/MANUSCRIPT.md): twenty chapters, two labs and EX001–EX066. Review remains open. This is not a finished qualification.

## Navigation rule

At the end of an authored chapter, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. The course chapter index connects its final row to the next course in the same language.

## Twenty-chapter rapid route

This is the one-month **rapid course** in cloud and container security. The book follows synthetic practice manager **Leila Ahmadi** of the fictional **Oakfield Physiotherapy**, taught by **Ben Hartley** at the fictional **Westbrook Community College**. The clinic owner is physiotherapist **Mark Ellis**. Eight staff. No servers. The provider is unnamed. Lessons 1–4 teach the forwarded letter, written authority, the sharing filter, and the three-month routine. Lessons 5–20 teach the mechanisms those two scripts do not settle. `hiagokinlevi/cloud-posture-watch` is supplementary. It is not a control the clinic checklist measured, and Oakfield did not deploy it.

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–2 | Services, authority, the four-view log, accounts and factors | EX001–EX026 |
| 3–4 | Sharing filter, image agreement, secrets, monthly routine | lab_sharing.py; lab_routine.py; EX027–EX050 |
| 5–20 | One mechanism or evidence limit each | EX051–EX066 |

Verified lab facts (synthetic). Do not say either print was replaced.

```text
items 8, sensitive 5, shared too widely 3
  patient-letters/: anyone-with-link
  invoices/: anyone-with-link
  old-backup.zip: anyone-with-link
```

```text
May: 3/6 done; missed: check backups restored, update booking app image, read provider security notices
June: 5/6 done; missed: update booking app image
July: 6/6 done
```

## Teaching guardrails

- Do not edit `lab_sharing.py` or `lab_routine.py`. Do not print a second matrix. August's watched routine stays prose and is not a fourth key.
- The sharing list has eight triples. `allowed[True]` is `staff` and `admins`. `allowed[False]` adds `public`. The failure token is `anyone-with-link`, which is in neither set. The three failures are sensitive only in this file; that coincidence is not the predicate. No link string is printed.
- `patient-letters/` stays a failure line because the triple is the April export. The afternoon staff-only change stays in the decision log.
- Sensitive 5 is the Boolean sum: patient-letters, referrals, invoices, old-backup.zip, and booking-app-config. Referrals at `staff` and the config at `admins` pass. Eight staff are not eight triples. No kappa is defined.
- Deleting `old-backup.zip` stays prose after a retention check with Mark. No sanitization method, recycler, or date is recorded.
- Do not name a cloud vendor. The three public responsibility pages are references, not Oakfield's contract. No SaaS, PaaS, or IaaS label is stored. The clinic owns no servers.
- Four outside views: three match the hospital domain and one is the patient's forwarded view. No unknown address appears among those four. That extract is not a proof that no other copy exists. No cross-tenant finding is recorded. SP 800-207 was not adopted as a scored design.
- Named accounts replace the shared reception login. The January colleague stays unnamed. Leaver bits stay 1, 1, 1 with no name. `staff`, `admins`, and `public` are not a role hierarchy.
- Second factors are prose. Two hardware keys were issued to staff without smartphones. No serial is printed. Routine index 1 stays 1, 1, 1 and is not a factor roster.
- The image was last rebuilt a year ago. The confirmation is a one-line message, not a digest. No vulnerability count, EPSS value, tag, or cluster size is stored. The platform is not Kubernetes.
- The database password was moved to the platform secret settings and changed. The value is not printed. The config triple remains sensitive, `admins`, and out of the failure list. That passing row does not prove the object is empty.
- Routine vectors are length 6. The denominator is `len(tasks)`. May is `[1, 1, 0, 0, 1, 0]`, June is `[1, 1, 1, 0, 1, 1]`, July is `[1, 1, 1, 1, 1, 1]`. A 1 does not store quality. Fourteen ones in eighteen cells may be derived beside the print and must not replace the three month lines. The image column is 0, 0, 1.
- May's restore zero stays. June's practice used a test folder, not the patient letters and not the zip.
- The backup contact stays unnamed. July's image 1 is not a digest. No pod profile and no network policy are recorded. `price-list.pdf` being public is a storage token, not a packet rule.
- Do not teach exploit steps, link guessing, payloads, or bypasses. Defender-side synthetic material only.
- After chapter 20 the next stop in this level is course 014. Do not call the clinic secure. Twenty lessons meet the planning minimum and leave review open.

## Continue the curriculum

After chapter 20, the next stop is [course 014: Application and software supply chain security / Rapid course](../../application-supply-chain/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapters 1–20 and EX001–EX066 are published, and independent review remains open. Page count is not the writing target. This is not a finished qualification. Other language folders keep their own state until their own writing and review.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
