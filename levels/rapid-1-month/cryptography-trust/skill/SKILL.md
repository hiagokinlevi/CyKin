---
name: oca-cryptography-trust-rapid-a49d4b1a
description: "Guide a learner through the published rapid cryptography book: twenty English chapters, three synthetic labs, and EX001–EX066. Review is still open."
license: CC0-1.0
---

# Cryptography and trust services — Rapid course course skill

Use this **one skill for the whole 1 month course**. The English manuscript publishes twenty chapter-lessons. The Portuguese manuscript is its own earlier edition, not a translation of those twenty English chapters. Read the actual manuscript and never present a plan as a completed lesson.

## Course sources

- [Complete 207-course study path](../../../../STUDY_PATH.md): course 008, chapter order and cross-course continuation.
- [Course home](../README.md): objectives, prerequisites, all language editions and current state.
- [English chapter index](../en/SUBJECTS.md): subject order, chapter links and draft status.
- [English book plan](../en/book/PLAN.md): summaries and planned exercises.
- [Materials](../en/MATERIALS.md): practice and assessment links.
- [Supplementary playbooks](../../../../playbooks/cryptography-trust/README.md): source-linked practice.
- [Authored English book](../en/book/MANUSCRIPT.md): twenty chapters, three labs and EX001–EX066. Review remains open. This is not a finished qualification.
- [Authored Portuguese (PT-BR) book](../pt/book/MANUSCRIPT.md): its own earlier edition. Do not treat it as a translation of the twenty English chapters.

## Navigation rule

At the end of an authored chapter, use its **Continue studying** block for the previous chapter, course index and next chapter. Keep the learner's course and chapter position visible. The course chapter index connects its final row to the next course in the same language.

## Twenty-chapter rapid route

This is the one-month **rapid course** in cryptography and trust services. The book follows synthetic new learner **Leo Fernandes**, guided by volunteer **Inês Hartley** at the fictional **Willow Lane Community Library**. Lessons 1–4 teach the three promises, permission and scope, the library's systems and one guided fingerprint check. Lessons 5–20 each settle one later question without replacing a laboratory print.

| Chapters | Read and teach | Labs / exercises |
|---|---|---|
| 1–2 | Promises, encoding, hashing, encryption, signatures, permission and scope | lab_fingerprint.py; EX001–EX026 |
| 3–4 | Systems, salted storage, expiry, and the download check | lab_salted.py; lab_checkfile.py; EX027–EX050 |
| 5–20 | One later Willow Lane question each | EX051–EX066 |

Verified lab facts (synthetic). Do not say either print was replaced.

```text
A: 7a5d91566f93af7abf7fc2c33d868004...
B: c029501271e71ec3fc765840b69dfabd...
match: False
```

```text
same password, same stored value? False
member 1 right password: True
member 2 right password: True
member 1 wrong password: False
```

```text
published: 215e60edb672063786f8bb92...
download_ok.bin MATCH
download_bad.bin MISMATCH
```

## Teaching guardrails

- Do not edit `lab_fingerprint.py`, `lab_salted.py`, or `lab_checkfile.py`.
- Do not invent the hidden fingerprint digits, a timetable, a supplier algorithm, a policy grade, an on/off laptop result, a password, a Wi-Fi secret, a signing key, a calendar date, or an attack.
- The supervised download matched. The laboratory still prints both MATCH and MISMATCH.
- `v2.1` stays inside the synthetic bytes. The tool stays on one laptop.
- Scrypt is the laboratory call. Argon2id stays a citation. The supplier's algorithm stays unnamed.
- Inês's suggestion of the Professional course stays a suggestion. After chapter 20 the next stop in this level is course 009.
- Do not call Willow Lane secure. Twenty lessons meet the planning minimum and leave review open.

## Continue the curriculum

After chapter 20, the next stop is [course 009: Web3, blockchain and cryptoasset security / Rapid course](../../web3-blockchain-security/en/SUBJECTS.md).

## Editorial status and language

Check the [book standard](../../../../BOOK_STANDARD.md) before claiming a chapter or edition is complete. English chapters 1–20 and EX001–EX066 are published, and independent review remains open. Page count is not the writing target. This is not a finished qualification. Other language folders keep their own state until their own writing and review.

Original maintainer-owned content is dedicated under [CC0 1.0](../../../../LICENSE); third-party sources retain their own rights.
