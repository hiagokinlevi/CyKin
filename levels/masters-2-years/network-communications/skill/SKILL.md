---
name: cykin-network-communications-masters-1c76d953
description: "NET Master's Course (8 ch / 50 ex)"
license: CC0-1.0
---

# Network and communications security — Master's course course skill

Use this **one skill for the whole 2 years course**. The course has one principal book per language; each of its 8 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 172, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/network-communications/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Eight-subject research route

This is the two-year **master's course** for network and communications security. The book follows synthetic student **Amara Okoye** of the fictional **Easterly University**, supervised by **Dr Felix Brandt**, as she studies whether governed tuning of intrusion detection rules can cut alert volume while keeping detections at the fictional **Corvane Logistics**.

| Subjects | Read and teach | Labs / exercises |
|---|---|---|
| 1–3 | Question and literature method, advanced seminar on detection and base rates, design, ethics and reproducibility | lab_baserate.py (2); EX001–EX020 |
| 4–6 | Competing explanations, proposal and pilot, data collection and analysis | lab_normalise.py (4), lab_tuning.py (6); EX021–EX038 |
| 7–8 | Dissertation and limitations, independent review and viva | EX039–EX050 |

Verified lab facts (synthetic): with TPR 0.95 and FPR 0.01, precision 0.913/0.490/0.087/0.009 at base rates 0.1/0.01/0.001/0.0001; alerts per 100 GB 512.1→190.9 while traffic fell 25.5%; alerts 4210→1180 (−72.0%), precision 0.009→0.031, recall 0.950→0.925 (one detection lost, then restored by narrowing an exception).

## Teaching guardrails

- Synthetic data only; no exploit code, payloads, attack traffic or bypass steps.
- Tuning is governed: narrow, documented, expiring exceptions; recall checked on a fixed labelled set.

## Continue the curriculum

After chapter 8, the next stop is [course 173: Systems, endpoints and hardware security / Master's course](../../systems-endpoints-hardware/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
