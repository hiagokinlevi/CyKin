# Materials — AI and machine-learning security / Rapid course / English

[Edition overview](README.md) · [Chapters](SUBJECTS.md) · [One principal book plan](book/PLAN.md) · [Supplementary playbooks](../../../../playbooks/ai-security/README.md) · [Course skill](../skill/SKILL.md)

**Teaching and examples:** each subject-chapter belongs to the one principal book. Plans describe intended content; only the linked manuscript contains authored lessons.

**Labs and practice:** the published English manuscript contains six offline labs. Do not edit the scripts. They use the Python 3 standard library and open no network connection. The Wilson rows stay:

```text
successes=3/20 rate=0.150 wilson95=[0.052, 0.360]
successes=30/200 rate=0.150 wilson95=[0.107, 0.206]
successes=300/2000 rate=0.150 wilson95=[0.135, 0.166]
```

The seed line stays `per-seed rates: 0.110 0.130 0.135 0.105 0.145 mean=0.125 sd=0.017`. The bootstrap line stays `baseline_asr=0.350 defended_asr=0.190 reduction_ci95=[0.120, 0.203]`. The hash check stays `config.yaml MISMATCH`, `model.bin MISMATCH`, `tokenizer.json OK`. The four defence rows, the five epsilon accuracies, the three token-bucket lines and the nine precision lines stay as printed. A sixth epsilon and a tenth precision row are not results. `hiagokinlevi/ai-security-guardrails` was not a control either script measured.

**Projects and assessment:** score the authored exercises with their 0–3 rubrics. Review of the edition is still open. Page count is not the writing target.

**Exercises and answers:** EX001–EX066 have worked results in the final appendix of the same book. The exercise baseline in the chapter index is a planning aid, not a quota.

**References and glossary:** verifiable primary sources and clear terms belong in the authored manuscript; linked project playbooks retain their source rights.
