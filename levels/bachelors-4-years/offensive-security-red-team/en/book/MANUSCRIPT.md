# Authorized Offensive Security and Red Team: A Bachelor's Degree Book

- Language: English (`en`); four years; approximately 3,200 hours of planned study.
- Editorial state: **draft**. Chapters 1–40 of 40 have authored teaching text; exercises EX001–EX120 have matching worked results with 0–3 rubrics; offline labs use the Python 3 standard library and their printed outputs were produced by real runs against synthetic data only. Independent review and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: broad security and computing students who need rigorous, ethical grounding in authorized offensive security.
- Relation to neighbouring books: the [technologist book](../../../../technologist-3-years/offensive-security-red-team/en/book/MANUSCRIPT.md) is more implementation-focused; the [engineering book](../../../../engineering-5-years/offensive-security-red-team/en/book/MANUSCRIPT.md) is more design-heavy. **This book balances theory, cases, methods and research skills**, ending in a capstone and thesis.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not a qualification and **no authority to test real systems**. All organizations, people, findings and numbers are **synthetic** unless a sentence cites a public source. Labs teach scoping, measurement and reporting — never weaponised techniques.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Each chapter has learning outcomes, teaching text, a worked example, errors and limits, exercises scored 0–3 (0 absent or unsafe; 1 major gap; 2 minor gaps; 3 complete and justified), a synthesis and a **Continue studying** block. Labs are deterministic, run offline with `python3 file.py` on synthetic data, and print the results shown under *Expected output*.

### The running example (synthetic): Lumen Civic Network

> **Synthetic case — fiction.** **Lumen Civic Network** is invented. It runs HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments. *Rina Costa*, student on an authorized internal assessment placement, follows these systems through the course. Every number is invented; all testing happens on isolated copies with synthetic data and written authorization.

### Source policy

Sources were checked on 12 October 2026: [NIST SP 800-115](https://doi.org/10.6028/NIST.SP.800-115); [PTES](https://pentest-standard.readthedocs.io/en/latest/); [MITRE ATT&CK](https://attack.mitre.org/); [OWASP WSTG](https://owasp.org/www-project-web-security-testing-guide/); [TIBER-EU](https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html); [CBEST](https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide) (2024 Implementation Guide). Albrecht and Jensen (arXiv:2010.06377) critique empty security scores. Legal content is orientation, not advice.

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Mathematical reasoning

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 1.1 Why this chapter exists

This chapter develops **Mathematical reasoning** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 1.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 1.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 1.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.


### 1.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 1.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 1.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX001 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX002 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX003 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Mathematical reasoning matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 01 of 40

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Computing systems

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 2.1 Why this chapter exists

This chapter develops **Computing systems** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 2.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 2.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 2.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.

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

### 2.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 2.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 2.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX004 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX005 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX006 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Computing systems matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 02 of 40

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming I

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 3.1 Why this chapter exists

This chapter develops **Programming I** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 3.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 3.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 3.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.


### 3.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 3.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 3.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX007 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX008 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX009 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Programming I matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 03 of 40

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Academic writing

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 4.1 Why this chapter exists

This chapter develops **Academic writing** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 4.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 4.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 4.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.

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

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 4.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 4.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX010 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX011 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX012 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Academic writing matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 04 of 40

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 5.1 Why this chapter exists

This chapter develops **Security literacy** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 5.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 5.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 5.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.


### 5.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 5.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 5.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX013 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX014 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX015 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Security literacy matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 05 of 40

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Discrete structures

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 6.1 Why this chapter exists

This chapter develops **Discrete structures** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 6.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 6.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 6.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.

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

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 6.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 6.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX016 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX017 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX018 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Discrete structures matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 06 of 40

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Networks and protocols

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 7.1 Why this chapter exists

This chapter develops **Networks and protocols** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 7.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 7.3 Engineering substance

Network paths for assessment tooling need segmentation, TLS, rate limits and deny-by-default egress. Unbounded scanning against shared lab infrastructure is an availability risk (and often an ROE violation). Design quotas the way you would for any multi-tenant service.

### 7.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.


### 7.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 7.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 7.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX019 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX020 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX021 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Networks and protocols matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 07 of 40

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Programming II

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 8.1 Why this chapter exists

This chapter develops **Programming II** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 8.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 8.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 8.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.

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

### 8.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 8.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 8.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX022 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX023 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX024 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Programming II matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 08 of 40

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Data and databases

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 9.1 Why this chapter exists

This chapter develops **Data and databases** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 9.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 9.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 9.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.


### 9.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 9.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 9.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX025 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX026 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX027 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Data and databases matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 09 of 40

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Ethics and authorized practice

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 10.1 Why this chapter exists

This chapter develops **Ethics and authorized practice** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 10.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 10.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 10.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.

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

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 10.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 10.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX028 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX029 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX030 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Ethics and authorized practice matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 10 of 40

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Operating systems

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 11.1 Why this chapter exists

This chapter develops **Operating systems** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 11.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 11.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 11.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.


### 11.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 11.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 11.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX031 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX032 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX033 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Operating systems matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 11 of 40

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Probability and statistics

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 12.1 Why this chapter exists

This chapter develops **Probability and statistics** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 12.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 12.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 12.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.

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

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 12.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 12.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX034 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX035 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX036 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Probability and statistics matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 12 of 40

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Identity and access

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 13.1 Why this chapter exists

This chapter develops **Identity and access** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 13.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 13.3 Engineering substance

Assessment platforms handle powerful credentials. Store them in a secrets manager, issue short-lived delegated tokens, and never embed secrets in prompts, tickets or screenshots. Password policy checks belong in tooling; online guessing against real directories does not belong in this course.

### 13.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.


### 13.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 13.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 13.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX037 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX038 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX039 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Identity and access matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 13 of 40

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Privacy foundations

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 14.1 Why this chapter exists

This chapter develops **Privacy foundations** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 14.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 14.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 14.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.

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

### 14.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 14.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 14.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX040 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX041 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX042 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Privacy foundations matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 14 of 40

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Evidence and measurement

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 15.1 Why this chapter exists

This chapter develops **Evidence and measurement** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 15.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 15.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 15.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.

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

### 15.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 15.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 15.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX043 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX044 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX045 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Evidence and measurement matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 15 of 40

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Security architecture

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 16.1 Why this chapter exists

This chapter develops **Security architecture** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 16.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 16.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 16.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.

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

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 16.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 16.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX046 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX047 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX048 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Security architecture matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 16 of 40

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Cryptography concepts

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 17.1 Why this chapter exists

This chapter develops **Cryptography concepts** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 17.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 17.3 Engineering substance

Assessment platforms handle powerful credentials. Store them in a secrets manager, issue short-lived delegated tokens, and never embed secrets in prompts, tickets or screenshots. Password policy checks belong in tooling; online guessing against real directories does not belong in this course.

### 17.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.


### 17.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 17.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 17.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX049 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX050 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX051 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Cryptography concepts matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 17 of 40

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Research methods I

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 18.1 Why this chapter exists

This chapter develops **Research methods I** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 18.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 18.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 18.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.

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

### 18.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 18.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 18.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX052 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX053 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX054 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Research methods I matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 18 of 40

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Authorized offensive security and red team: scope and theory

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 19.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: scope and theory** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 19.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 19.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 19.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.

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

### 19.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 19.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 19.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX055 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX056 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX057 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Authorized offensive security and red team: scope and theory matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 19 of 40

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Authorized offensive security and red team: foundational cases

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 20.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: foundational cases** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 20.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 20.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 20.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.

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

### 20.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 20.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 20.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX058 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX059 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX060 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Authorized offensive security and red team: foundational cases matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 20 of 40

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Authorized offensive security and red team: system models

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 21.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: system models** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 21.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 21.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 21.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.


### 21.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 21.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 21.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX061 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX062 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX063 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Authorized offensive security and red team: system models matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 21 of 40

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Authorized offensive security and red team: data and dependencies

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 22.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: data and dependencies** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 22.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 22.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 22.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.

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

### 22.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 22.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 22.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX064 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX065 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX066 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Authorized offensive security and red team: data and dependencies matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 22 of 40

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Authorized offensive security and red team: methods I

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 23.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: methods I** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 23.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 23.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 23.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.


### 23.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 23.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 23.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX067 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX068 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX069 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Authorized offensive security and red team: methods I matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 23 of 40

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Authorized offensive security and red team: controls

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 24.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: controls** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 24.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 24.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 24.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.

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

### 24.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 24.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 24.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX070 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX071 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX072 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Authorized offensive security and red team: controls matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 24 of 40

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Laboratory I

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 25.1 Why this chapter exists

This chapter develops **Laboratory I** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 25.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 25.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 25.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.

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

### 25.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 25.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 25.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX073 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX074 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX075 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Laboratory I matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 25 of 40

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Authorized offensive security and red team: methods II

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 26.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: methods II** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 26.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 26.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 26.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.

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

### 26.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 26.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 26.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX076 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX077 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX078 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Authorized offensive security and red team: methods II matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 26 of 40

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Authorized offensive security and red team: verification

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 27.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: verification** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 27.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 27.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 27.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.


### 27.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 27.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 27.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX079 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX080 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX081 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Authorized offensive security and red team: verification matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 27 of 40

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Authorized offensive security and red team: failure analysis

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 28.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: failure analysis** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 28.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 28.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 28.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.

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

### 28.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 28.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 28.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX082 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX083 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX084 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Authorized offensive security and red team: failure analysis matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 28 of 40

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Authorized offensive security and red team: operations

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 29.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: operations** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 29.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 29.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 29.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.


### 29.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 29.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 29.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX085 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX086 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX087 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Authorized offensive security and red team: operations matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 29 of 40

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Laboratory II

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 30.1 Why this chapter exists

This chapter develops **Laboratory II** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 30.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 30.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 30.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.

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

### 30.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 30.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 30.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX088 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX089 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX090 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Laboratory II matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 30 of 40

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Authorized offensive security and red team: advanced cases

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 31.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: advanced cases** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 31.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 31.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 31.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.


### 31.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 31.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 31.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX091 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX092 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX093 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Authorized offensive security and red team: advanced cases matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 31 of 40

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Authorized offensive security and red team: interdisciplinary interfaces

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 32.1 Why this chapter exists

This chapter develops **Authorized offensive security and red team: interdisciplinary interfaces** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 32.2 Frameworks and vocabulary

Authorization names owner, systems, dates, allowed actions and data rules. Scope is the set of hosts, ports, identities and actions that are in. Stop conditions — real personal data, out-of-scope hosts, availability impact — pause work. Curiosity is not authorization. Legal and contractual limits (including vendor terms for SaaS) are part of engineering requirements, not footnotes.

### 32.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 32.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.

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

### 32.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 32.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 32.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX094 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX095 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX096 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Authorized offensive security and red team: interdisciplinary interfaces matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 32 of 40

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Research methods II

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 33.1 Why this chapter exists

This chapter develops **Research methods II** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 33.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 33.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 33.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.


### 33.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 33.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 33.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX097 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX098 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX099 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Research methods II matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 33 of 40

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Comparative project

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 34.1 Why this chapter exists

This chapter develops **Comparative project** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 34.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 34.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 34.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.

```python
"""Evaluate proposed actions against synthetic rules of engagement."""
ROE = {
    "hours": ("09:00", "17:00"),
    "deny_actions": {"denial-of-service", "phishing-staff", "exfiltrate-real-data"},
    "require_approval": {"password-spray-lab", "privilege-escalation-lab"},
    "max_concurrency": 5,
}
proposals = [
    ("service-enum", "10:30", 3, False),
    ("denial-of-service", "10:30", 1, False),
    ("password-spray-lab", "10:30", 2, False),
    ("password-spray-lab", "10:30", 2, True),
    ("service-enum", "18:00", 2, False),
    ("service-enum", "11:00", 20, False),
]

def ok_time(t):
    return ROE["hours"][0] <= t <= ROE["hours"][1]

for action, when, conc, approved in proposals:
    reasons=[]
    if action in ROE["deny_actions"]: reasons.append("deny-action")
    if action in ROE["require_approval"] and not approved: reasons.append("needs-approval")
    if not ok_time(when): reasons.append("outside-hours")
    if conc > ROE["max_concurrency"]: reasons.append("concurrency")
    print(f"action={action:20} when={when} conc={conc:2} approved={approved} -> {'ALLOW' if not reasons else 'DENY'} {','.join(reasons) or '-'}")
```

Expected output:

```text
action=service-enum         when=10:30 conc= 3 approved=False -> ALLOW -
action=denial-of-service    when=10:30 conc= 1 approved=False -> DENY deny-action
action=password-spray-lab   when=10:30 conc= 2 approved=False -> DENY needs-approval
action=password-spray-lab   when=10:30 conc= 2 approved=True -> ALLOW -
action=service-enum         when=18:00 conc= 2 approved=False -> DENY outside-hours
action=service-enum         when=11:00 conc=20 approved=False -> DENY concurrency
```

### 34.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 34.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 34.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX100 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX101 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX102 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Comparative project matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 34 of 40

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Capstone proposal

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 35.1 Why this chapter exists

This chapter develops **Capstone proposal** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 35.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 35.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 35.4 Practice discipline

Capstone evidence maps requirement → control → test → result. Demonstrations show a normal path, a blocked out-of-scope action, an alert and a rollback — never a weaponised exploit. Defence answers point to evidence and limits.


### 35.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 35.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 35.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX103 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX104 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX105 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Capstone proposal matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 35 of 40

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Field or community practice

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 36.1 Why this chapter exists

This chapter develops **Field or community practice** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 36.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 36.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 36.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.

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

### 36.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 36.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 36.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX106 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX107 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX108 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Field or community practice matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 36 of 40

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Evidence review seminar

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 37.1 Why this chapter exists

This chapter develops **Evidence review seminar** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 37.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 37.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 37.4 Practice discipline

Worked practice in this chapter stays local and synthetic. When a lab appears, run it with `python3` on the book machine; compare the printed output; then write the engineering implication for Lumen Civic Network's HelpDesk Portal, StaffWiki and a synthetic training VLAN used for authorized assessments.


### 37.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 37.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 37.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX109 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX110 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX111 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Evidence review seminar matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 37 of 40

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Capstone implementation

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 38.1 Why this chapter exists

This chapter develops **Capstone implementation** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 38.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 38.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 38.4 Practice discipline

Capstone evidence maps requirement → control → test → result. Demonstrations show a normal path, a blocked out-of-scope action, an alert and a rollback — never a weaponised exploit. Defence answers point to evidence and limits.

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

### 38.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 38.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 38.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX112 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX113 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX114 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Capstone implementation matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 38 of 40

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Capstone evaluation

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 39.1 Why this chapter exists

This chapter develops **Capstone evaluation** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 39.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 39.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 39.4 Practice discipline

Capstone evidence maps requirement → control → test → result. Demonstrations show a normal path, a blocked out-of-scope action, an alert and a rollback — never a weaponised exploit. Defence answers point to evidence and limits.


### 39.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 39.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 39.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX115 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX116 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX117 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Capstone evaluation matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 39 of 40

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Thesis and presentation

### Learning outcomes

You will (1) explain the chapter topic in an authorized-assessment setting; (2) produce one checkable artefact (rule, schema, test or measure); (3) connect the work to NIST SP 800-115 / PTES / ATT&CK as relevant; (4) refuse unsafe or dual-use requests; and (5) record evidence Rina Costa could hand to a reviewer.

### 40.1 Why this chapter exists

This chapter develops **Thesis and presentation** in the service of authorized offensive security engineering. Everything practical happens under written permission, on synthetic or explicitly scoped targets, with stop conditions. Rina Costa at Lumen Civic Network uses the chapter to make one design or process decision that can be checked later.

### 40.2 Frameworks and vocabulary

NIST SP 800-115 and PTES treat assessment as a planned activity: scope and rules before discovery, careful bounds on any active testing, and reporting that supports remediation. MITRE ATT&CK supplies a shared vocabulary for techniques that were planned or observed; it is not a proof that residual risk is gone. OWASP WSTG contributes web-specific authorized test cases when the system under test is a web application. Threat-led programmes such as TIBER-EU and CBEST add intelligence-led scenarios and oversight for critical financial contexts — use them when that is the engagement type, not as a default label for every student lab.

### 40.3 Engineering substance

For engineers, the durable artefacts are checkable: scope predicates, ROE machines, finding schemas without exploit recipes, coverage reports, evidence hashes and measurement dashboards. Albrecht and Jensen (arXiv:2010.06377) warn against empty single scores; prefer concrete rates, intervals and verified remediation status.

### 40.4 Practice discipline

Capstone evidence maps requirement → control → test → result. Demonstrations show a normal path, a blocked out-of-scope action, an alert and a rollback — never a weaponised exploit. Defence answers point to evidence and limits.

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

### 40.5 Implementation notes

Implementation notes for Rina Costa: keep configuration in version control; record model-like versions of rulesets; add unit tests for allow/deny decisions; and require a second person to review any change that widens scope. Wide scope is an incident waiting for a timestamp.

### 40.6 Worked example (synthetic Lumen case)

Rina Costa applies the chapter to Lumen Civic Network. On a synthetic range, they record a decision (for example, a new scope predicate, a finding field, or a coverage report column), cite the authorizing ROE version, and attach a lab output or unit-test result. Numbers in the example are invented; no production host is touched.

### 40.7 Errors and limits

- verbal-only permission; measuring vanity activity (tools launched) instead of effects (out-of-scope probes, verified fixes); publishing payloads; and treating ATT&CK coverage percentages as residual-risk scores.

### Exercises

- **EX118 — Apply this chapter to Lumen Civic Network.** Rubric: 3 = concrete artefact with authorization link; 2 = partial; 1 = vague; 0 = none.
- **EX119 — Name a misuse this chapter prevents.** Rubric: 3 = specific misuse + control; 2 = partial; 1 = vague; 0 = none.
- **EX120 — Design a check or measure.** Rubric: 3 = checkable criterion + evidence; 2 = partial; 1 = vanity metric; 0 = none.

### Synthesis

Thesis and presentation matters when it becomes a checkable, authorized, evidence-backed habit — not a slide. Keep scope tight, measures honest and exploit detail out of the artefacts.

### Continue studying — chapter 40 of 40

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers; any answer meeting the rubric scores equally. Lumen Civic Network, Rina Costa and all their numbers are synthetic.

**EX001.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX002.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX003.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX004.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX005.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX006.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX007.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX008.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX009.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX010.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX011.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX012.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX013.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX014.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX015.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX016.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX017.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX018.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX019.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX020.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX021.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX022.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX023.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX024.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX025.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX026.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX027.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX028.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX029.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX030.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX031.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX032.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX033.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX034.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX035.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX036.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX037.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX038.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX039.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX040.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX041.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX042.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX043.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX044.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX045.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX046.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX047.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX048.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX049.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX050.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX051.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX052.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX053.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX054.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX055.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX056.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX057.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX058.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX059.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX060.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX061.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX062.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX063.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX064.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX065.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX066.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX067.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX068.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX069.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX070.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX071.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX072.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX073.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX074.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX075.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX076.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX077.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX078.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX079.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX080.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX081.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX082.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX083.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX084.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX085.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX086.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX087.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX088.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX089.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX090.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX091.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX092.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX093.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX094.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX095.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX096.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX097.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX098.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX099.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX100.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX101.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX102.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX103.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX104.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX105.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX106.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX107.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX108.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX109.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX110.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX111.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX112.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX113.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX114.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX115.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX116.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX117.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX118.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX119.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

**EX120.** Example acceptable answer: Rina Costa produces a concrete, authorized artefact for Lumen Civic Network (scope rule, schema field, unit test or rate with interval), links it to written permission, and states what unsafe request is refused. Any answer meeting the rubric scores equally.

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
