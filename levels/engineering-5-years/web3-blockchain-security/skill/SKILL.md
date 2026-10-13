---
name: cykin-web3-blockchain-security-engineering-7a92cee2
description: "WEB3 Engineering Degree (50 ch / 150 ex)"
license: CC0-1.0
---

# Web3, blockchain and cryptoasset security — Engineering course course skill

Use this **one skill for the whole 5 years course**. The course has one principal book per language; each of its 50 subjects is a chapter of that book. Read the actual manuscript when available and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 124, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/web3-blockchain-security/README.md): source-linked practice.
- [Authored English book draft](../en/book/MANUSCRIPT.md): use only chapters, labs and exercises actually present; review is pending.

## Navigation rule

At the end of an authored chapter or a book-plan chapter summary, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. If the next link is a plan, explain that the lesson is not yet authored and do not mark it complete. The course chapter index connects its final row to the next course in the same language.

## Fifty-chapter engineering route

This is the five-year **engineering degree** in Web3, blockchain and cryptoasset security. The book follows synthetic student **Jonas Weber** of the fictional **Avalon Polytechnic University**, supervised by **Dr Amara Nwosu**, engineering a permissioned EVM energy-token ledger for the fictional **Brightwater Community Energy Cooperative** (about 400 households, three validators).

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–14 | Foundations: mathematics, computing, hashing, cryptography, data and key management | lab_chain.py (2); EX001–EX042 |
| 15–30 | Requirements, architecture, control, invariants, roles and reconciliation | lab_merkle.py (19), lab_invariant.py (24), lab_roles.py (27), lab_reconcile.py (30); EX043–EX090 |
| 31–40 | Finality, operations, monitoring, capacity and assurance | lab_finality.py (32), lab_monitor.py (37); EX091–EX120 |
| 41–50 | Evaluation, review, deployment, trials, dossier and thesis defense | EX121–EX150 |

Verified lab facts (synthetic): hash chain breaks at index 2; Merkle proof length 3, altered reading rejected; invariant check flags overdraft at step 5 and supply 1470 > cap 1400 at step 7; 3 role breaches (Market.setFee, Market.upgrade 24 h, Oracle.setSource); reconciliation of 7 accounts finds 3 mismatches, totals 355 vs 330; Nakamoto catch-up for q=0.1 gives 0.0509779 at z=2 and 0.0002428 at z=6 (z=5 for <0.1%), for q=0.3 0.1321112 at z=6 (z=24); monitor raises 2 of 4 alerts.

## Teaching guardrails

- Synthetic data only; no protocol is named and no attack steps are given.
- Labs detect and verify; none construct transactions or exploits.

## Continue the curriculum

After chapter 50, the next stop is [course 125: Identity and access management / Engineering course](../../identity-access/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapter drafts and exercise–answer pairs exist, but the book has not passed independent review or the 300-page A4 gate. Other language folders are working outlines until their own translation and review. Teach in the learner's language if helpful while identifying English as the only authored reference edition.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
