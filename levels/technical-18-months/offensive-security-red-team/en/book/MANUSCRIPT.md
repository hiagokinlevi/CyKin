# Authorized Offensive Security and Red Team: A Technical Course Book

- Language: English (`en`); 18 months; approximately 1,200 hours of planned study.
- Editorial state: **draft**. Chapters 1–18 of 18 have authored teaching text; exercises EX001–EX072 have matching worked results with 0–3 rubrics; offline labs use the Python 3 standard library and their printed outputs were produced by real runs against synthetic data only. Independent review and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: technicians who install, configure, operate and troubleshoot authorized assessment tooling under supervision.
- Relation to neighbouring books: the [technologist book](../../../../technologist-3-years/offensive-security-red-team/en/book/MANUSCRIPT.md) goes deeper; the [professional book](../../../../professional-6-months/offensive-security-red-team/en/book/MANUSCRIPT.md) is shorter. **This book is procedural**.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not a qualification and **no authority to test real systems**. All organizations, people, findings and numbers are **synthetic** unless a sentence cites a public source. Labs teach scoping, measurement and reporting — never weaponised techniques.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Each chapter has learning outcomes, teaching text, a worked example, errors and limits, exercises scored 0–3 (0 absent or unsafe; 1 major gap; 2 minor gaps; 3 complete and justified), a synthesis and a **Continue studying** block. Labs are deterministic, run offline with `python3 file.py` on synthetic data, and print the results shown under *Expected output*.

### The running example (synthetic): Kestrel Telecom

> **Synthetic case — fiction.** **Kestrel Telecom** is invented. It runs HelpBot staging, SpamShield lab API and LineWatch synthetic feeds. *Ana Ribeiro*, trainee technician in service operations, follows these systems through the course. Every number is invented; all testing happens on isolated copies with synthetic data and written authorization.

### Source policy

Sources were checked on 12 October 2026: [NIST SP 800-115](https://doi.org/10.6028/NIST.SP.800-115); [PTES](https://pentest-standard.readthedocs.io/en/latest/); [MITRE ATT&CK](https://attack.mitre.org/); [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/); [TIBER-EU](https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html); [CBEST](https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide) (2024 Implementation Guide). Albrecht and Jensen (arXiv:2010.06377) critique empty security scores. Legal content is orientation, not advice.

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Computing and service architecture

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Ana Ribeiro could hand to a reviewer.

### 1.1 Why this chapter exists

This chapter develops **Computing and service architecture** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Ana Ribeiro at Kestrel Telecom uses the chapter to make one design or process decision that can be checked later.

### 1.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 1.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 1.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Kestrel Telecom's HelpBot staging, SpamShield lab API and LineWatch synthetic feeds.


### 1.5 Implementation notes

Implementation notes for Ana Ribeiro: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 1.6 Worked example (synthetic Kestrel case)

Ana Ribeiro applies the chapter to Kestrel Telecom. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 1.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX001 — Apply this chapter to Kestrel Telecom.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX002 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX003 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX004 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.

### Synthesis

Computing and service architecture matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 01 of 18

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Networks and protocols

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Ana Ribeiro could hand to a reviewer.

### 2.1 Why this chapter exists

This chapter develops **Networks and protocols** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Ana Ribeiro at Kestrel Telecom uses the chapter to make one design or process decision that can be checked later.

### 2.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 2.3 Engineering substance

Network paths for assessment tooling need segmentation, TLS, rate limits and deny-by-default egress. Unbounded scanning against shared lab infrastructure is an availability risk (and often an ROE violation). Design quotas the way you would for any multi-tenant service.

### 2.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Kestrel Telecom's HelpBot staging, SpamShield lab API and LineWatch synthetic feeds.

```python
"""Lab R: token-bucket limits against unbounded consumption (synthetic).
Simulates 60 seconds of requests from a normal client and a flooding client
against a model endpoint with a per-client token bucket."""
import random
rng = random.Random(4)
def simulate(rate_per_s, burst, reqs):
    tokens, last, ok = burst, 0.0, 0
    for t in reqs:
        tokens = min(burst, tokens + (t - last) * rate_per_s); last = t
        if tokens >= 1: tokens -= 1; ok += 1
    return ok
normal = sorted(rng.uniform(0, 60) for _ in range(90))
flood = sorted(rng.uniform(0, 60) for _ in range(3000))
for rate, burst in ((5, 20), (2, 10), (1, 5)):
    print(f"limit={rate}/s burst={burst:2d} normal_served={simulate(rate, burst, normal):3d}/90 "
          f"flood_served={simulate(rate, burst, flood):4d}/3000")
```

Expected output:

```text
limit=5/s burst=20 normal_served= 90/90 flood_served= 319/3000
limit=2/s burst=10 normal_served= 90/90 flood_served= 129/3000
limit=1/s burst= 5 normal_served= 62/90 flood_served=  64/3000
```

### 2.5 Implementation notes

Implementation notes for Ana Ribeiro: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 2.6 Worked example (synthetic Kestrel case)

Ana Ribeiro applies the chapter to Kestrel Telecom. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 2.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX005 — Apply this chapter to Kestrel Telecom.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX006 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX007 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX008 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.

### Synthesis

Networks and protocols matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 02 of 18

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Operating systems and identities

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Ana Ribeiro could hand to a reviewer.

### 3.1 Why this chapter exists

This chapter develops **Operating systems and identities** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Ana Ribeiro at Kestrel Telecom uses the chapter to make one design or process decision that can be checked later.

### 3.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 3.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 3.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Kestrel Telecom's HelpBot staging, SpamShield lab API and LineWatch synthetic feeds.


### 3.5 Implementation notes

Implementation notes for Ana Ribeiro: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 3.6 Worked example (synthetic Kestrel case)

Ana Ribeiro applies the chapter to Kestrel Telecom. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 3.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX009 — Apply this chapter to Kestrel Telecom.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX010 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX011 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX012 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.

### Synthesis

Operating systems and identities matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 03 of 18

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Scripting and data formats

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Ana Ribeiro could hand to a reviewer.

### 4.1 Why this chapter exists

This chapter develops **Scripting and data formats** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Ana Ribeiro at Kestrel Telecom uses the chapter to make one design or process decision that can be checked later.

### 4.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 4.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 4.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Kestrel Telecom's HelpBot staging, SpamShield lab API and LineWatch synthetic feeds.

```python
"""Rank synthetic assets for authorized engagement scoping."""
assets = [
    ("public-web-portal", 3, 3, 3),      # exposure, data_sensitivity, blast_radius 1-3
    ("staging-admin-ui", 2, 3, 2),
    ("corp-vpn-edge", 3, 2, 3),
    ("internal-wiki", 1, 2, 1),
    ("printer-fleet", 2, 1, 1),
    ("lab-jump-host", 1, 1, 2),
]
print(f"{'asset':20} score exposure data blast")
for name, e, d, b in sorted(assets, key=lambda x: -(x[1]+x[2]+x[3])):
    print(f"{name:20} {e+d+b:5} {e:8} {d:4} {b:5}")
```

Expected output:

```text
asset                score exposure data blast
public-web-portal        9        3    3     3
corp-vpn-edge            8        3    2     3
staging-admin-ui         7        2    3     2
internal-wiki            4        1    2     1
printer-fleet            4        2    1     1
lab-jump-host            4        1    1     2
```

### 4.5 Implementation notes

Implementation notes for Ana Ribeiro: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 4.6 Worked example (synthetic Kestrel case)

Ana Ribeiro applies the chapter to Kestrel Telecom. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 4.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX013 — Apply this chapter to Kestrel Telecom.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX014 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX015 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX016 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.

### Synthesis

Scripting and data formats matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 04 of 18

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security scope and evidence

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Ana Ribeiro could hand to a reviewer.

### 5.1 Why this chapter exists

This chapter develops **Security scope and evidence** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Ana Ribeiro at Kestrel Telecom uses the chapter to make one design or process decision that can be checked later.

### 5.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 5.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 5.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Kestrel Telecom's HelpBot staging, SpamShield lab API and LineWatch synthetic feeds.

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

### 5.5 Implementation notes

Implementation notes for Ana Ribeiro: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 5.6 Worked example (synthetic Kestrel case)

Ana Ribeiro applies the chapter to Kestrel Telecom. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 5.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX017 — Apply this chapter to Kestrel Telecom.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX018 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX019 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX020 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.

### Synthesis

Security scope and evidence matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 05 of 18

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Authorized offensive security and red team: system model

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Ana Ribeiro could hand to a reviewer.

### 6.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: system model** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Ana Ribeiro at Kestrel Telecom uses the chapter to make one design or process decision that can be checked later.

### 6.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 6.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 6.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Kestrel Telecom's HelpBot staging, SpamShield lab API and LineWatch synthetic feeds.

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

Implementation notes for Ana Ribeiro: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 6.6 Worked example (synthetic Kestrel case)

Ana Ribeiro applies the chapter to Kestrel Telecom. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 6.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX021 — Apply this chapter to Kestrel Telecom.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX022 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX023 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX024 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.

### Synthesis

Authorized offensive security and red team: system model matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 06 of 18

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Authorized offensive security and red team: data and telemetry

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Ana Ribeiro could hand to a reviewer.

### 7.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: data and telemetry** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Ana Ribeiro at Kestrel Telecom uses the chapter to make one design or process decision that can be checked later.

### 7.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 7.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 7.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Kestrel Telecom's HelpBot staging, SpamShield lab API and LineWatch synthetic feeds.


### 7.5 Implementation notes

Implementation notes for Ana Ribeiro: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 7.6 Worked example (synthetic Kestrel case)

Ana Ribeiro applies the chapter to Kestrel Telecom. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 7.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX025 — Apply this chapter to Kestrel Telecom.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX026 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX027 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX028 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.

### Synthesis

Authorized offensive security and red team: data and telemetry matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 07 of 18

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Authorized offensive security and red team: failure modes

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Ana Ribeiro could hand to a reviewer.

### 8.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: failure modes** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Ana Ribeiro at Kestrel Telecom uses the chapter to make one design or process decision that can be checked later.

### 8.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 8.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 8.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Kestrel Telecom's HelpBot staging, SpamShield lab API and LineWatch synthetic feeds.

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

Implementation notes for Ana Ribeiro: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 8.6 Worked example (synthetic Kestrel case)

Ana Ribeiro applies the chapter to Kestrel Telecom. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 8.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX029 — Apply this chapter to Kestrel Telecom.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX030 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX031 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX032 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.

### Synthesis

Authorized offensive security and red team: failure modes matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 08 of 18

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Authorized offensive security and red team: tools and methods

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Ana Ribeiro could hand to a reviewer.

### 9.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: tools and methods** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Ana Ribeiro at Kestrel Telecom uses the chapter to make one design or process decision that can be checked later.

### 9.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 9.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 9.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Kestrel Telecom's HelpBot staging, SpamShield lab API and LineWatch synthetic feeds.


### 9.5 Implementation notes

Implementation notes for Ana Ribeiro: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 9.6 Worked example (synthetic Kestrel case)

Ana Ribeiro applies the chapter to Kestrel Telecom. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 9.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX033 — Apply this chapter to Kestrel Telecom.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX034 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX035 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX036 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.

### Synthesis

Authorized offensive security and red team: tools and methods matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 09 of 18

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Authorized offensive security and red team: control configuration

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Ana Ribeiro could hand to a reviewer.

### 10.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: control configuration** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Ana Ribeiro at Kestrel Telecom uses the chapter to make one design or process decision that can be checked later.

### 10.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 10.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 10.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Kestrel Telecom's HelpBot staging, SpamShield lab API and LineWatch synthetic feeds.

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

Implementation notes for Ana Ribeiro: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 10.6 Worked example (synthetic Kestrel case)

Ana Ribeiro applies the chapter to Kestrel Telecom. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 10.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX037 — Apply this chapter to Kestrel Telecom.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX038 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX039 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX040 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.

### Synthesis

Authorized offensive security and red team: control configuration matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 10 of 18

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Authorized offensive security and red team: verification

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Ana Ribeiro could hand to a reviewer.

### 11.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: verification** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Ana Ribeiro at Kestrel Telecom uses the chapter to make one design or process decision that can be checked later.

### 11.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 11.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 11.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Kestrel Telecom's HelpBot staging, SpamShield lab API and LineWatch synthetic feeds.


### 11.5 Implementation notes

Implementation notes for Ana Ribeiro: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 11.6 Worked example (synthetic Kestrel case)

Ana Ribeiro applies the chapter to Kestrel Telecom. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 11.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX041 — Apply this chapter to Kestrel Telecom.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX042 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX043 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX044 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.

### Synthesis

Authorized offensive security and red team: verification matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 11 of 18

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Contained laboratory I

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Ana Ribeiro could hand to a reviewer.

### 12.1 Why this chapter exists

This chapter develops **Contained laboratory I** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Ana Ribeiro at Kestrel Telecom uses the chapter to make one design or process decision that can be checked later.

### 12.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 12.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 12.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Kestrel Telecom's HelpBot staging, SpamShield lab API and LineWatch synthetic feeds.

```python
"""Lab S: reporting attack-success rates honestly: Wilson intervals,
seed variation and a paired bootstrap. Synthetic trial outcomes only."""
import math, random
def wilson(k, n, z=1.96):
    p = k/n; d = 1 + z*z/n
    c = (p + z*z/(2*n))/d; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/d
    return c - h, c + h
for k, n in ((3, 20), (30, 200), (300, 2000)):
    lo, hi = wilson(k, n); print(f"successes={k}/{n} rate={k/n:.3f} wilson95=[{lo:.3f}, {hi:.3f}]")
# five seeds of a synthetic defence evaluation: per-seed attack success rate
rates = []
for seed in range(5):
    r = random.Random(seed); rates.append(sum(r.random() < 0.12 for _ in range(200))/200)
m = sum(rates)/5; sd = math.sqrt(sum((x-m)**2 for x in rates)/4)
print("per-seed rates:", " ".join(f"{x:.3f}" for x in rates), f"mean={m:.3f} sd={sd:.3f}")
# paired bootstrap: baseline vs defence on the same 300 synthetic prompts
r = random.Random(42)
base = [r.random() < 0.30 for _ in range(300)]
defn = [b and r.random() < 0.6 for b in base]   # defence blocks ~40% of successes
diffs = []
for _ in range(2000):
    idx = [r.randrange(300) for _ in range(300)]
    diffs.append(sum(base[i] for i in idx)/300 - sum(defn[i] for i in idx)/300)
diffs.sort()
print(f"baseline_asr={sum(base)/300:.3f} defended_asr={sum(defn)/300:.3f} "
      f"reduction_ci95=[{diffs[50]:.3f}, {diffs[1949]:.3f}]")
```

Expected output:

```text
successes=3/20 rate=0.150 wilson95=[0.052, 0.360]
successes=30/200 rate=0.150 wilson95=[0.107, 0.206]
successes=300/2000 rate=0.150 wilson95=[0.135, 0.166]
per-seed rates: 0.110 0.130 0.135 0.105 0.145 mean=0.125 sd=0.017
baseline_asr=0.350 defended_asr=0.190 reduction_ci95=[0.120, 0.203]
```

### 12.5 Implementation notes

Implementation notes for Ana Ribeiro: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 12.6 Worked example (synthetic Kestrel case)

Ana Ribeiro applies the chapter to Kestrel Telecom. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 12.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX045 — Apply this chapter to Kestrel Telecom.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX046 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX047 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX048 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.

### Synthesis

Contained laboratory I matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 12 of 18

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Authorized offensive security and red team: troubleshooting

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Ana Ribeiro could hand to a reviewer.

### 13.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: troubleshooting** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Ana Ribeiro at Kestrel Telecom uses the chapter to make one design or process decision that can be checked later.

### 13.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 13.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 13.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Kestrel Telecom's HelpBot staging, SpamShield lab API and LineWatch synthetic feeds.


### 13.5 Implementation notes

Implementation notes for Ana Ribeiro: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 13.6 Worked example (synthetic Kestrel case)

Ana Ribeiro applies the chapter to Kestrel Telecom. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 13.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX049 — Apply this chapter to Kestrel Telecom.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX050 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX051 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX052 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.

### Synthesis

Authorized offensive security and red team: troubleshooting matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 13 of 18

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Authorized offensive security and red team: automation

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Ana Ribeiro could hand to a reviewer.

### 14.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: automation** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Ana Ribeiro at Kestrel Telecom uses the chapter to make one design or process decision that can be checked later.

### 14.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 14.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 14.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Kestrel Telecom's HelpBot staging, SpamShield lab API and LineWatch synthetic feeds.

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

### 14.5 Implementation notes

Implementation notes for Ana Ribeiro: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 14.6 Worked example (synthetic Kestrel case)

Ana Ribeiro applies the chapter to Kestrel Telecom. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 14.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX053 — Apply this chapter to Kestrel Telecom.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX054 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX055 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX056 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.

### Synthesis

Authorized offensive security and red team: automation matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 14 of 18

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Authorized offensive security and red team: integration and dependencies

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Ana Ribeiro could hand to a reviewer.

### 15.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: integration and dependencies** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Ana Ribeiro at Kestrel Telecom uses the chapter to make one design or process decision that can be checked later.

### 15.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 15.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 15.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Kestrel Telecom's HelpBot staging, SpamShield lab API and LineWatch synthetic feeds.


### 15.5 Implementation notes

Implementation notes for Ana Ribeiro: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 15.6 Worked example (synthetic Kestrel case)

Ana Ribeiro applies the chapter to Kestrel Telecom. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 15.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX057 — Apply this chapter to Kestrel Telecom.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX058 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX059 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX060 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.

### Synthesis

Authorized offensive security and red team: integration and dependencies matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 15 of 18

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Technical documentation and safety

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Ana Ribeiro could hand to a reviewer.

### 16.1 Why this chapter exists

This chapter develops **Technical documentation and safety** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Ana Ribeiro at Kestrel Telecom uses the chapter to make one design or process decision that can be checked later.

### 16.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 16.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 16.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Kestrel Telecom's HelpBot staging, SpamShield lab API and LineWatch synthetic feeds.

```python
"""Rank synthetic assets for authorized engagement scoping."""
assets = [
    ("public-web-portal", 3, 3, 3),      # exposure, data_sensitivity, blast_radius 1-3
    ("staging-admin-ui", 2, 3, 2),
    ("corp-vpn-edge", 3, 2, 3),
    ("internal-wiki", 1, 2, 1),
    ("printer-fleet", 2, 1, 1),
    ("lab-jump-host", 1, 1, 2),
]
print(f"{'asset':20} score exposure data blast")
for name, e, d, b in sorted(assets, key=lambda x: -(x[1]+x[2]+x[3])):
    print(f"{name:20} {e+d+b:5} {e:8} {d:4} {b:5}")
```

Expected output:

```text
asset                score exposure data blast
public-web-portal        9        3    3     3
corp-vpn-edge            8        3    2     3
staging-admin-ui         7        2    3     2
internal-wiki            4        1    2     1
printer-fleet            4        2    1     1
lab-jump-host            4        1    1     2
```

### 16.5 Implementation notes

Implementation notes for Ana Ribeiro: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 16.6 Worked example (synthetic Kestrel case)

Ana Ribeiro applies the chapter to Kestrel Telecom. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 16.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX061 — Apply this chapter to Kestrel Telecom.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX062 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX063 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX064 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.

### Synthesis

Technical documentation and safety matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 16 of 18

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Contained laboratory II

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Ana Ribeiro could hand to a reviewer.

### 17.1 Why this chapter exists

This chapter develops **Contained laboratory II** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Ana Ribeiro at Kestrel Telecom uses the chapter to make one design or process decision that can be checked later.

### 17.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 17.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 17.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Kestrel Telecom's HelpBot staging, SpamShield lab API and LineWatch synthetic feeds.

```python
"""Lab S: reporting attack-success rates honestly: Wilson intervals,
seed variation and a paired bootstrap. Synthetic trial outcomes only."""
import math, random
def wilson(k, n, z=1.96):
    p = k/n; d = 1 + z*z/n
    c = (p + z*z/(2*n))/d; h = z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))/d
    return c - h, c + h
for k, n in ((3, 20), (30, 200), (300, 2000)):
    lo, hi = wilson(k, n); print(f"successes={k}/{n} rate={k/n:.3f} wilson95=[{lo:.3f}, {hi:.3f}]")
# five seeds of a synthetic defence evaluation: per-seed attack success rate
rates = []
for seed in range(5):
    r = random.Random(seed); rates.append(sum(r.random() < 0.12 for _ in range(200))/200)
m = sum(rates)/5; sd = math.sqrt(sum((x-m)**2 for x in rates)/4)
print("per-seed rates:", " ".join(f"{x:.3f}" for x in rates), f"mean={m:.3f} sd={sd:.3f}")
# paired bootstrap: baseline vs defence on the same 300 synthetic prompts
r = random.Random(42)
base = [r.random() < 0.30 for _ in range(300)]
defn = [b and r.random() < 0.6 for b in base]   # defence blocks ~40% of successes
diffs = []
for _ in range(2000):
    idx = [r.randrange(300) for _ in range(300)]
    diffs.append(sum(base[i] for i in idx)/300 - sum(defn[i] for i in idx)/300)
diffs.sort()
print(f"baseline_asr={sum(base)/300:.3f} defended_asr={sum(defn)/300:.3f} "
      f"reduction_ci95=[{diffs[50]:.3f}, {diffs[1949]:.3f}]")
```

Expected output:

```text
successes=3/20 rate=0.150 wilson95=[0.052, 0.360]
successes=30/200 rate=0.150 wilson95=[0.107, 0.206]
successes=300/2000 rate=0.150 wilson95=[0.135, 0.166]
per-seed rates: 0.110 0.130 0.135 0.105 0.145 mean=0.125 sd=0.017
baseline_asr=0.350 defended_asr=0.190 reduction_ci95=[0.120, 0.203]
```

### 17.5 Implementation notes

Implementation notes for Ana Ribeiro: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 17.6 Worked example (synthetic Kestrel case)

Ana Ribeiro applies the chapter to Kestrel Telecom. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 17.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX065 — Apply this chapter to Kestrel Telecom.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX066 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX067 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX068 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.

### Synthesis

Contained laboratory II matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 17 of 18

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Supervised technical project

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Ana Ribeiro could hand to a reviewer.

### 18.1 Why this chapter exists

This chapter develops **Supervised technical project** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Ana Ribeiro at Kestrel Telecom uses the chapter to make one design or process decision that can be checked later.

### 18.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 18.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 18.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Kestrel Telecom's HelpBot staging, SpamShield lab API and LineWatch synthetic feeds.

```python
"""ATT&CK-style coverage matrix over synthetic authorized techniques (names only)."""
# Synthetic engagement log: technique_id -> observed (True/False)
PLAN = ["T1046", "T1595", "T1082", "T1083", "T1059", "T1078", "T1021"]
OBSERVED = {"T1046", "T1595", "T1082", "T1083", "T1078"}
LABELS = {
    "T1046": "Network Service Discovery",
    "T1595": "Active Scanning",
    "T1082": "System Information Discovery",
    "T1083": "File and Directory Discovery",
    "T1059": "Command and Scripting Interpreter",
    "T1078": "Valid Accounts",
    "T1021": "Remote Services",
}
covered = 0
for tid in PLAN:
    hit = tid in OBSERVED
    covered += hit
    print(f"{tid} {LABELS[tid]:34} {'COVERED' if hit else 'PLANNED-NOT-SEEN'}")
print(f"coverage={covered}/{len(PLAN)} ({100*covered/len(PLAN):.0f}%)")
```

Expected output:

```text
T1046 Network Service Discovery          COVERED
T1595 Active Scanning                    COVERED
T1082 System Information Discovery       COVERED
T1083 File and Directory Discovery       COVERED
T1059 Command and Scripting Interpreter  PLANNED-NOT-SEEN
T1078 Valid Accounts                     COVERED
T1021 Remote Services                    PLANNED-NOT-SEEN
coverage=5/7 (71%)
```

### 18.5 Implementation notes

Implementation notes for Ana Ribeiro: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 18.6 Worked example (synthetic Kestrel case)

Ana Ribeiro applies the chapter to Kestrel Telecom. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 18.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX069 — Apply this chapter to Kestrel Telecom.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX070 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX071 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.
- **EX072 — Critique an empty score or unsafe ask.** Rubric: 3 = validity/ethics reason + alternative; 2 = partial; 1 = accepts unsafe ask; 0 = none.

### Synthesis

Supervised technical project matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 18 of 18

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers; any answer meeting the rubric scores equally. Kestrel Telecom, Ana Ribeiro and all their numbers are synthetic.

**EX001.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX002.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX003.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX004.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX005.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX006.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX007.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX008.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX009.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX010.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX011.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX012.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX013.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX014.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX015.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX016.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX017.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX018.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX019.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX020.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX021.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX022.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX023.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX024.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX025.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX026.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX027.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX028.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX029.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX030.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX031.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX032.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX033.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX034.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX035.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX036.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX037.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX038.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX039.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX040.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX041.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX042.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX043.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX044.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX045.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX046.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX047.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX048.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX049.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX050.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX051.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX052.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX053.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX054.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX055.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX056.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX057.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX058.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX059.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX060.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX061.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX062.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX063.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX064.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX065.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX066.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX067.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX068.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX069.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX070.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX071.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX072.** Example acceptable answer: Ana Ribeiro produces a concrete, authorized artefact for Kestrel Telecom (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

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
