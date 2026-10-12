# Authorized Offensive Security and Red Team: A Professional Practice Book

- Language: English (`en`); six months; approximately 300 hours of planned study.
- Editorial state: **draft**. Chapters 1–12 of 12 have authored teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; offline labs use the Python 3 standard library and their printed outputs were produced by real runs against synthetic data only. Independent review and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: working practitioners who handle authorized offensive-security work under supervision.
- Relation to neighbouring books: the [technical book](../../../../technical-18-months/offensive-security-red-team/en/book/MANUSCRIPT.md) is longer; the [rapid book](../../../../rapid-1-month/offensive-security-red-team/en/book/MANUSCRIPT.md) is orientation. **This book is workflow-focused**.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not a qualification and **no authority to test real systems**. All organizations, people, findings and numbers are **synthetic** unless a sentence cites a public source. Labs teach scoping, measurement and reporting — never weaponised techniques.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Each chapter has learning outcomes, teaching text, a worked example, errors and limits, exercises scored 0–3 (0 absent or unsafe; 1 major gap; 2 minor gaps; 3 complete and justified), a synthesis and a **Continue studying** block. Labs are deterministic, run offline with `python3 file.py` on synthetic data, and print the results shown under *Expected output*.

### The running example (synthetic): Meridian Mutual

> **Synthetic case — fiction.** **Meridian Mutual** is invented. It runs ClaimChat staging and FraudFlag lab scoring API. *Sofia Lind*, practitioner moving into authorized assurance, follows these systems through the course. Every number is invented; all testing happens on isolated copies with synthetic data and written authorization.

### Source policy

Sources were checked on 12 October 2026: [NIST SP 800-115](https://doi.org/10.6028/NIST.SP.800-115); [PTES](https://pentest-standard.readthedocs.io/en/latest/); [MITRE ATT&CK](https://attack.mitre.org/); [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/); [TIBER-EU](https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html); [CBEST](https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide) (2024 Implementation Guide). Albrecht and Jensen (arXiv:2010.06377) critique empty security scores. Legal content is orientation, not advice.

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Security foundations for practitioners

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Sofia Lind could hand to a reviewer.

### 1.1 Why this chapter exists

This chapter develops **Security foundations for practitioners** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Sofia Lind at Meridian Mutual uses the chapter to make one design or process decision that can be checked later.

### 1.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 1.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 1.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Meridian Mutual's ClaimChat staging and FraudFlag lab scoring API.


### 1.5 Implementation notes

Implementation notes for Sofia Lind: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 1.6 Worked example (synthetic Meridian case)

Sofia Lind applies the chapter to Meridian Mutual. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 1.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX001 — Apply this chapter to Meridian Mutual.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX002 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX003 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX004 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.
- **EX005 — Write a stop or escalation rule.** Rubric: 3 = trigger, action, owner; 2 = two; 1 = one; 0 = none.

### Synthesis

Security foundations for practitioners matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Authorized offensive security and red team: service and stakeholder context

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Sofia Lind could hand to a reviewer.

### 2.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: service and stakeholder context** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Sofia Lind at Meridian Mutual uses the chapter to make one design or process decision that can be checked later.

### 2.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 2.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 2.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Meridian Mutual's ClaimChat staging and FraudFlag lab scoring API.

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

Implementation notes for Sofia Lind: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 2.6 Worked example (synthetic Meridian case)

Sofia Lind applies the chapter to Meridian Mutual. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 2.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX006 — Apply this chapter to Meridian Mutual.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX007 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX008 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX009 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.
- **EX010 — Write a stop or escalation rule.** Rubric: 3 = trigger, action, owner; 2 = two; 1 = one; 0 = none.

### Synthesis

Authorized offensive security and red team: service and stakeholder context matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 02 of 12

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Authorized practice and evidence handling

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Sofia Lind could hand to a reviewer.

### 3.1 Why this chapter exists

This chapter develops **Authorized practice and evidence handling** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Sofia Lind at Meridian Mutual uses the chapter to make one design or process decision that can be checked later.

### 3.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 3.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 3.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Meridian Mutual's ClaimChat staging and FraudFlag lab scoring API.


### 3.5 Implementation notes

Implementation notes for Sofia Lind: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 3.6 Worked example (synthetic Meridian case)

Sofia Lind applies the chapter to Meridian Mutual. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 3.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX011 — Apply this chapter to Meridian Mutual.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX012 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX013 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX014 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.
- **EX015 — Write a stop or escalation rule.** Rubric: 3 = trigger, action, owner; 2 = two; 1 = one; 0 = none.

### Synthesis

Authorized practice and evidence handling matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 03 of 12

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Authorized offensive security and red team: core methods

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Sofia Lind could hand to a reviewer.

### 4.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: core methods** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Sofia Lind at Meridian Mutual uses the chapter to make one design or process decision that can be checked later.

### 4.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 4.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 4.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Meridian Mutual's ClaimChat staging and FraudFlag lab scoring API.

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

Implementation notes for Sofia Lind: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 4.6 Worked example (synthetic Meridian case)

Sofia Lind applies the chapter to Meridian Mutual. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 4.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX016 — Apply this chapter to Meridian Mutual.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX017 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX018 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX019 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.
- **EX020 — Write a stop or escalation rule.** Rubric: 3 = trigger, action, owner; 2 = two; 1 = one; 0 = none.

### Synthesis

Authorized offensive security and red team: core methods matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 04 of 12

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Authorized offensive security and red team: tools and interpretation

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Sofia Lind could hand to a reviewer.

### 5.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: tools and interpretation** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Sofia Lind at Meridian Mutual uses the chapter to make one design or process decision that can be checked later.

### 5.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 5.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 5.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Meridian Mutual's ClaimChat staging and FraudFlag lab scoring API.


### 5.5 Implementation notes

Implementation notes for Sofia Lind: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 5.6 Worked example (synthetic Meridian case)

Sofia Lind applies the chapter to Meridian Mutual. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 5.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX021 — Apply this chapter to Meridian Mutual.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX022 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX023 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX024 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.
- **EX025 — Write a stop or escalation rule.** Rubric: 3 = trigger, action, owner; 2 = two; 1 = one; 0 = none.

### Synthesis

Authorized offensive security and red team: tools and interpretation matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 05 of 12

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Authorized offensive security and red team: operational workflow

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Sofia Lind could hand to a reviewer.

### 6.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: operational workflow** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Sofia Lind at Meridian Mutual uses the chapter to make one design or process decision that can be checked later.

### 6.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 6.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 6.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Meridian Mutual's ClaimChat staging and FraudFlag lab scoring API.

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

### 6.5 Implementation notes

Implementation notes for Sofia Lind: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 6.6 Worked example (synthetic Meridian case)

Sofia Lind applies the chapter to Meridian Mutual. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 6.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX026 — Apply this chapter to Meridian Mutual.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX027 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX028 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX029 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.
- **EX030 — Write a stop or escalation rule.** Rubric: 3 = trigger, action, owner; 2 = two; 1 = one; 0 = none.

### Synthesis

Authorized offensive security and red team: operational workflow matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 06 of 12

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Authorized offensive security and red team: controls and verification

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Sofia Lind could hand to a reviewer.

### 7.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: controls and verification** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Sofia Lind at Meridian Mutual uses the chapter to make one design or process decision that can be checked later.

### 7.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 7.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 7.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Meridian Mutual's ClaimChat staging and FraudFlag lab scoring API.


### 7.5 Implementation notes

Implementation notes for Sofia Lind: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 7.6 Worked example (synthetic Meridian case)

Sofia Lind applies the chapter to Meridian Mutual. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 7.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX031 — Apply this chapter to Meridian Mutual.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX032 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX033 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX034 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.
- **EX035 — Write a stop or escalation rule.** Rubric: 3 = trigger, action, owner; 2 = two; 1 = one; 0 = none.

### Synthesis

Authorized offensive security and red team: controls and verification matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 07 of 12

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Authorized offensive security and red team: supervised case analysis

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Sofia Lind could hand to a reviewer.

### 8.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: supervised case analysis** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Sofia Lind at Meridian Mutual uses the chapter to make one design or process decision that can be checked later.

### 8.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 8.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 8.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Meridian Mutual's ClaimChat staging and FraudFlag lab scoring API.

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

### 8.5 Implementation notes

Implementation notes for Sofia Lind: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 8.6 Worked example (synthetic Meridian case)

Sofia Lind applies the chapter to Meridian Mutual. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 8.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX036 — Apply this chapter to Meridian Mutual.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX037 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX038 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX039 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.
- **EX040 — Write a stop or escalation rule.** Rubric: 3 = trigger, action, owner; 2 = two; 1 = one; 0 = none.

### Synthesis

Authorized offensive security and red team: supervised case analysis matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 08 of 12

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Communication, ethics and reporting

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Sofia Lind could hand to a reviewer.

### 9.1 Why this chapter exists

This chapter develops **Communication, ethics and reporting** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Sofia Lind at Meridian Mutual uses the chapter to make one design or process decision that can be checked later.

### 9.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 9.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 9.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Meridian Mutual's ClaimChat staging and FraudFlag lab scoring API.


### 9.5 Implementation notes

Implementation notes for Sofia Lind: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 9.6 Worked example (synthetic Meridian case)

Sofia Lind applies the chapter to Meridian Mutual. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 9.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX041 — Apply this chapter to Meridian Mutual.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX042 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX043 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX044 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.
- **EX045 — Write a stop or escalation rule.** Rubric: 3 = trigger, action, owner; 2 = two; 1 = one; 0 = none.

### Synthesis

Communication, ethics and reporting matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 09 of 12

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Authorized offensive security and red team: quality and troubleshooting

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Sofia Lind could hand to a reviewer.

### 10.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: quality and troubleshooting** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Sofia Lind at Meridian Mutual uses the chapter to make one design or process decision that can be checked later.

### 10.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 10.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 10.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Meridian Mutual's ClaimChat staging and FraudFlag lab scoring API.

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

### 10.5 Implementation notes

Implementation notes for Sofia Lind: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 10.6 Worked example (synthetic Meridian case)

Sofia Lind applies the chapter to Meridian Mutual. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 10.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX046 — Apply this chapter to Meridian Mutual.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX047 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX048 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX049 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.
- **EX050 — Write a stop or escalation rule.** Rubric: 3 = trigger, action, owner; 2 = two; 1 = one; 0 = none.

### Synthesis

Authorized offensive security and red team: quality and troubleshooting matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 10 of 12

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Supervised laboratory

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Sofia Lind could hand to a reviewer.

### 11.1 Why this chapter exists

This chapter develops **Supervised laboratory** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Sofia Lind at Meridian Mutual uses the chapter to make one design or process decision that can be checked later.

### 11.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 11.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 11.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Meridian Mutual's ClaimChat staging and FraudFlag lab scoring API.

```python
"""Score synthetic findings for report priority (no exploit details)."""
# impact 0-3, exploitability 0-3, exposure 0-3  -> priority
findings = [
    ("SYN-001", "default admin password on staging web UI", 3, 3, 2),
    ("SYN-002", "missing security headers on public site", 1, 1, 3),
    ("SYN-003", "outdated TLS on internal admin port", 2, 2, 1),
    ("SYN-004", "verbose error messages disclose paths", 1, 2, 2),
    ("SYN-005", "service account with domain admin in lab AD", 3, 2, 1),
]

def priority(impact, exploitability, exposure):
    score = impact*4 + exploitability*2 + exposure
    if score >= 16: return "critical", score
    if score >= 11: return "high", score
    if score >= 7: return "medium", score
    return "low", score

for fid, title, i, e, x in findings:
    p, s = priority(i, e, x)
    print(f"{fid} priority={p:8} score={s:2} impact={i} exploitability={e} exposure={x} :: {title}")
```

Expected output:

```text
SYN-001 priority=critical score=20 impact=3 exploitability=3 exposure=2 :: default admin password on staging web UI
SYN-002 priority=medium   score= 9 impact=1 exploitability=1 exposure=3 :: missing security headers on public site
SYN-003 priority=high     score=13 impact=2 exploitability=2 exposure=1 :: outdated TLS on internal admin port
SYN-004 priority=medium   score=10 impact=1 exploitability=2 exposure=2 :: verbose error messages disclose paths
SYN-005 priority=critical score=17 impact=3 exploitability=2 exposure=1 :: service account with domain admin in lab AD
```

### 11.5 Implementation notes

Implementation notes for Sofia Lind: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 11.6 Worked example (synthetic Meridian case)

Sofia Lind applies the chapter to Meridian Mutual. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 11.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX051 — Apply this chapter to Meridian Mutual.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX052 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX053 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX054 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.
- **EX055 — Write a stop or escalation rule.** Rubric: 3 = trigger, action, owner; 2 = two; 1 = one; 0 = none.

### Synthesis

Supervised laboratory matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Practice portfolio and final review

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Sofia Lind could hand to a reviewer.

### 12.1 Why this chapter exists

This chapter develops **Practice portfolio and final review** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Sofia Lind at Meridian Mutual uses the chapter to make one design or process decision that can be checked later.

### 12.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 12.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 12.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Meridian Mutual's ClaimChat staging and FraudFlag lab scoring API.

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

### 12.5 Implementation notes

Implementation notes for Sofia Lind: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 12.6 Worked example (synthetic Meridian case)

Sofia Lind applies the chapter to Meridian Mutual. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 12.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX056 — Apply this chapter to Meridian Mutual.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX057 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX058 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX059 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.
- **EX060 — Write a stop or escalation rule.** Rubric: 3 = trigger, action, owner; 2 = two; 1 = one; 0 = none.

### Synthesis

Practice portfolio and final review matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 12 of 12

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers; any answer meeting the rubric scores equally. Meridian Mutual, Sofia Lind and all their numbers are synthetic.

**EX001.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX002.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX003.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX004.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX005.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX006.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX007.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX008.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX009.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX010.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX011.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX012.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX013.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX014.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX015.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX016.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX017.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX018.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX019.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX020.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX021.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX022.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX023.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX024.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX025.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX026.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX027.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX028.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX029.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX030.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX031.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX032.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX033.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX034.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX035.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX036.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX037.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX038.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX039.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX040.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX041.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX042.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX043.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX044.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX045.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX046.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX047.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX048.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX049.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX050.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX051.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX052.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX053.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX054.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX055.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX056.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX057.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX058.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX059.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX060.** Example acceptable answer: Sofia Lind produces a concrete, authorized artefact for Meridian Mutual (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

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
