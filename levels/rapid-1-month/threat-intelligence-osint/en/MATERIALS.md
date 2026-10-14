# Materials — Threat intelligence and OSINT / Rapid course / English

[Edition overview](README.md) · [Chapters](SUBJECTS.md) · [One principal book plan](book/PLAN.md) · [Supplementary playbooks](../../../../playbooks/threat-intelligence-osint/README.md) · [Course skill](../skill/SKILL.md)

**Teaching and examples:** each subject-chapter belongs to the one principal book. Plans describe intended content; only the linked manuscript contains authored lessons.

**Labs and practice:** the published English manuscript contains two offline labs. Do not edit the scripts. The source print stays:

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

Use synthetic data only. Do not replace either print. `valid: 3` includes the AMBER domain. The community list does not. `198.51.100.400` does not parse. The script makes no DNS call. Email sign-ins last 30 days and donation logins last 90 days, and neither script prints those integers.

**Projects and assessment:** score the authored exercises with their 0–3 rubrics. Review of the edition is still open. Page count is not the writing target.

**Exercises and answers:** EX001–EX066 have worked results in the final appendix of the same book. The exercise baseline in the chapter index is a planning aid, not a quota.

**References and glossary:** verifiable primary sources and clear terms belong in the authored manuscript; linked project playbooks retain their source rights.
