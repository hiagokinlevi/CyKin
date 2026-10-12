# Authorized Offensive Security and Red Team: A One-Month Rapid Course Book

- Language: English (`en`); one month; approximately 60 hours of planned study.
- Editorial state: **draft**. Chapters 1–4 of 4 have authored teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; offline labs use the Python 3 standard library and their printed outputs were produced by real runs against synthetic data only. Independent review and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: busy professionals who need a safe orientation to authorized offensive security.
- Relation to neighbouring books: the [professional book](../../../../professional-6-months/offensive-security-red-team/en/book/MANUSCRIPT.md) develops practice. **This book is an orientation**.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not a qualification and **no authority to test real systems**. All organizations, people, findings and numbers are **synthetic** unless a sentence cites a public source. Labs teach scoping, measurement and reporting — never weaponised techniques.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Each chapter has learning outcomes, teaching text, a worked example, errors and limits, exercises scored 0–3 (0 absent or unsafe; 1 major gap; 2 minor gaps; 3 complete and justified), a synthesis and a **Continue studying** block. Labs are deterministic, run offline with `python3 file.py` on synthetic data, and print the results shown under *Expected output*.

### The running example (synthetic): Tallis & Co

> **Synthetic case — fiction.** **Tallis & Co** is invented. It runs InboxAide pilot tenant and ReceiptSort evaluation. *Omar Haddou*, IT lead deciding how to buy authorized testing, follows these systems through the course. Every number is invented; all testing happens on isolated copies with synthetic data and written authorization.

### Source policy

Sources were checked on 12 October 2026: [NIST SP 800-115](https://doi.org/10.6028/NIST.SP.800-115); [PTES](https://pentest-standard.readthedocs.io/en/latest/); [MITRE ATT&CK](https://attack.mitre.org/); [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/); [TIBER-EU](https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html); [CBEST](https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide) (2024 Implementation Guide). Albrecht and Jensen (arXiv:2010.06377) critique empty security scores. Legal content is orientation, not advice.

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Authorized offensive security and red team: foundations and decisions

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Omar Haddou could hand to a reviewer.

### 1.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: foundations and decisions** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Omar Haddou at Tallis & Co uses the chapter to make one design or process decision that can be checked later.

### 1.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 1.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 1.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Tallis & Co's InboxAide pilot tenant and ReceiptSort evaluation.


### 1.5 Implementation notes

Implementation notes for Omar Haddou: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 1.6 Worked example (synthetic Tallis case)

Omar Haddou applies the chapter to Tallis & Co. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 1.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX001 — Apply this chapter to Tallis & Co.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX002 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX003 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX004 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.
- **EX005 — Write a stop or escalation rule.** Rubric: 3 = trigger, action, owner; 2 = two; 1 = one; 0 = none.
- **EX006 — Apply this chapter to Tallis & Co.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX007 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX008 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX009 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.
- **EX010 — Write a stop or escalation rule.** Rubric: 3 = trigger, action, owner; 2 = two; 1 = one; 0 = none.
- **EX011 — Apply this chapter to Tallis & Co.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX012 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX013 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Authorized offensive security and red team: foundations and decisions matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 01 of 04

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Scope, permission and safe practice

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Omar Haddou could hand to a reviewer.

### 2.1 Why this chapter exists

This chapter develops **Scope, permission and safe practice** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Omar Haddou at Tallis & Co uses the chapter to make one design or process decision that can be checked later.

### 2.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 2.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 2.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Tallis & Co's InboxAide pilot tenant and ReceiptSort evaluation.

```python
"""Check proposed engagement targets against a written scope (synthetic)."""
SCOPE_CIDRS = [("10.20.0.0", 16), ("192.168.50.0", 24)]  # inclusive synthetic ranges
SCOPE_PORTS = {22, 80, 443, 8080}
DENY_HOSTS = {"10.20.0.1", "192.168.50.1"}  # out-of-scope infra

def ip_int(s):
    a,b,c,d = map(int, s.split("."))
    return (a<<24)|(b<<16)|(c<<8)|d

def in_cidr(ip, net, bits):
    mask = (0xFFFFFFFF << (32-bits)) & 0xFFFFFFFF
    return (ip_int(ip) & mask) == (ip_int(net) & mask)

def check(host, port):
    reasons = []
    if host in DENY_HOSTS:
        reasons.append("deny-list")
    if not any(in_cidr(host, n, b) for n,b in SCOPE_CIDRS):
        reasons.append("outside-cidr")
    if port not in SCOPE_PORTS:
        reasons.append("port-not-in-scope")
    return ("ALLOW" if not reasons else "DENY"), reasons

tests = [
    ("10.20.1.10", 443),
    ("10.20.0.1", 443),
    ("192.168.50.20", 22),
    ("192.168.50.20", 3389),
    ("8.8.8.8", 80),
    ("192.168.1.10", 80),
]
for h,p in tests:
    v, r = check(h,p)
    print(f"target={h}:{p} decision={v} reasons={','.join(r) or '-'}")
```

Expected output:

```text
target=10.20.1.10:443 decision=ALLOW reasons=-
target=10.20.0.1:443 decision=DENY reasons=deny-list
target=192.168.50.20:22 decision=ALLOW reasons=-
target=192.168.50.20:3389 decision=DENY reasons=port-not-in-scope
target=8.8.8.8:80 decision=DENY reasons=outside-cidr
target=192.168.1.10:80 decision=DENY reasons=outside-cidr
```

### 2.5 Implementation notes

Implementation notes for Omar Haddou: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 2.6 Worked example (synthetic Tallis case)

Omar Haddou applies the chapter to Tallis & Co. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 2.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX014 — Apply this chapter to Tallis & Co.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX015 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX016 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX017 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.
- **EX018 — Write a stop or escalation rule.** Rubric: 3 = trigger, action, owner; 2 = two; 1 = one; 0 = none.
- **EX019 — Apply this chapter to Tallis & Co.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX020 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX021 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX022 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.
- **EX023 — Write a stop or escalation rule.** Rubric: 3 = trigger, action, owner; 2 = two; 1 = one; 0 = none.
- **EX024 — Apply this chapter to Tallis & Co.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX025 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX026 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Scope, permission and safe practice matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 02 of 04

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Authorized offensive security and red team: systems, data and dependencies

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Omar Haddou could hand to a reviewer.

### 3.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: systems, data and dependencies** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Omar Haddou at Tallis & Co uses the chapter to make one design or process decision that can be checked later.

### 3.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 3.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 3.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Tallis & Co's InboxAide pilot tenant and ReceiptSort evaluation.


### 3.5 Implementation notes

Implementation notes for Omar Haddou: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 3.6 Worked example (synthetic Tallis case)

Omar Haddou applies the chapter to Tallis & Co. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 3.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX027 — Apply this chapter to Tallis & Co.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX028 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX029 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX030 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.
- **EX031 — Write a stop or escalation rule.** Rubric: 3 = trigger, action, owner; 2 = two; 1 = one; 0 = none.
- **EX032 — Apply this chapter to Tallis & Co.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX033 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX034 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX035 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.
- **EX036 — Write a stop or escalation rule.** Rubric: 3 = trigger, action, owner; 2 = two; 1 = one; 0 = none.
- **EX037 — Apply this chapter to Tallis & Co.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX038 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Authorized offensive security and red team: systems, data and dependencies matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 03 of 04

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Authorized offensive security and red team: guided lab and applied synthesis

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Omar Haddou could hand to a reviewer.

### 4.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: guided lab and applied synthesis** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Omar Haddou at Tallis & Co uses the chapter to make one design or process decision that can be checked later.

### 4.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 4.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 4.4 Practice discipline

Capstone evidence maps requirement → control → test → result. Demonstrations show a normal path, a blocked out-of-scope action, an alert and a rollback — never a weaponised exploit. Defence answers point to evidence and limits.

```python
"""Check proposed engagement targets against a written scope (synthetic)."""
SCOPE_CIDRS = [("10.20.0.0", 16), ("192.168.50.0", 24)]  # inclusive synthetic ranges
SCOPE_PORTS = {22, 80, 443, 8080}
DENY_HOSTS = {"10.20.0.1", "192.168.50.1"}  # out-of-scope infra

def ip_int(s):
    a,b,c,d = map(int, s.split("."))
    return (a<<24)|(b<<16)|(c<<8)|d

def in_cidr(ip, net, bits):
    mask = (0xFFFFFFFF << (32-bits)) & 0xFFFFFFFF
    return (ip_int(ip) & mask) == (ip_int(net) & mask)

def check(host, port):
    reasons = []
    if host in DENY_HOSTS:
        reasons.append("deny-list")
    if not any(in_cidr(host, n, b) for n,b in SCOPE_CIDRS):
        reasons.append("outside-cidr")
    if port not in SCOPE_PORTS:
        reasons.append("port-not-in-scope")
    return ("ALLOW" if not reasons else "DENY"), reasons

tests = [
    ("10.20.1.10", 443),
    ("10.20.0.1", 443),
    ("192.168.50.20", 22),
    ("192.168.50.20", 3389),
    ("8.8.8.8", 80),
    ("192.168.1.10", 80),
]
for h,p in tests:
    v, r = check(h,p)
    print(f"target={h}:{p} decision={v} reasons={','.join(r) or '-'}")
```

Expected output:

```text
target=10.20.1.10:443 decision=ALLOW reasons=-
target=10.20.0.1:443 decision=DENY reasons=deny-list
target=192.168.50.20:22 decision=ALLOW reasons=-
target=192.168.50.20:3389 decision=DENY reasons=port-not-in-scope
target=8.8.8.8:80 decision=DENY reasons=outside-cidr
target=192.168.1.10:80 decision=DENY reasons=outside-cidr
```

### 4.5 Implementation notes

Implementation notes for Omar Haddou: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 4.6 Worked example (synthetic Tallis case)

Omar Haddou applies the chapter to Tallis & Co. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 4.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX039 — Apply this chapter to Tallis & Co.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX040 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX041 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX042 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.
- **EX043 — Write a stop or escalation rule.** Rubric: 3 = trigger, action, owner; 2 = two; 1 = one; 0 = none.
- **EX044 — Apply this chapter to Tallis & Co.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX045 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX046 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX047 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.
- **EX048 — Write a stop or escalation rule.** Rubric: 3 = trigger, action, owner; 2 = two; 1 = one; 0 = none.
- **EX049 — Apply this chapter to Tallis & Co.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX050 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Authorized offensive security and red team: guided lab and applied synthesis matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 04 of 04

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers; any answer meeting the rubric scores equally. Tallis & Co, Omar Haddou and all their numbers are synthetic.

**EX001.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX002.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX003.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX004.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX005.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX006.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX007.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX008.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX009.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX010.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX011.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX012.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX013.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX014.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX015.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX016.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX017.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX018.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX019.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX020.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX021.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX022.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX023.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX024.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX025.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX026.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX027.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX028.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX029.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX030.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX031.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX032.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX033.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX034.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX035.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX036.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX037.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX038.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX039.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX040.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX041.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX042.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX043.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX044.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX045.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX046.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX047.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX048.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX049.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX050.** Example acceptable answer: Omar Haddou produces a concrete, authorized artefact for Tallis & Co (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

<a id="references"></a>

## References

Links checked 12 October 2026; frameworks change, so re-verify. arXiv identifiers were opened and titles checked.

- Albrecht, M. R., Jensen, R. B. (2020). The Vacuity of the Open Source Security Testing Methodology Manual. arXiv:2010.06377.
- Bank of England / PRA. CBEST Threat Intelligence-Led Assessments — Implementation Guide (2024 update). <https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide>
- European Central Bank. TIBER-EU Framework. <https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html>
- MITRE ATT&CK. <https://attack.mitre.org/>
- NIST SP 800-115 (2008). Technical Guide to Information Security Testing and Assessment. <https://doi.org/10.6028/NIST.SP.800-115>
- OWASP Web Security Testing Guide (WSTG). <https://owasp.org/www-project-web-security-testing-guide/>
- Penetration Testing Execution Standard (PTES). <https://pentest-standard.readthedocs.io/en/latest/>
