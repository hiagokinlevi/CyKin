# Application and Software Supply Chain Security: Professional Course

- Language: English (`en`); course 037, Professional course (6 months).
- Editorial state: **published**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; three offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: working practitioners moving into application security who must find, explain and help fix dependency and build risks with development teams.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: test and review only software you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic code and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one quality engineer becoming an application security engineer at a freight company, starting from an internal package resolved from a public registry and moving through context, authorised practice, source controls, scanner triage, workflow, controls, a supervised case, reporting, quality and a supervised lab, to a portfolio. Run each lab where it appears, attempt the five exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Priya Nair** | Professional course student and application security engineer | Invented |
| **Marcus Bell** | Security lead and mentor | Invented |
| **Harbourline Freight** | Fictional freight company | Invented |
| **Westgate Professional Institute** | Fictional institute | Invented |
| **TrackPort** | Fictional shipment-tracking application | Invented |

### Core sources

[OWASP Top 10:2021](https://owasp.org/Top10/); OWASP [ASVS](https://owasp.org/www-project-application-security-verification-standard/) 4.0.3 and 5.0.0; OWASP [WSTG](https://owasp.org/www-project-web-security-testing-guide/) and [SAMM](https://owaspsamm.org/); NIST [SP 800-218 (SSDF)](https://doi.org/10.6028/NIST.SP.800-218); [CWE Top 25](https://cwe.mitre.org/top25/); [SLSA v1.0](https://slsa.dev/spec/v1.0/); Shostack, *Threat Modeling: Designing for Security* (Wiley, 2014). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Security foundations for practitioners

### Learning outcomes

You will (1) state the core security goals for an internal business application; (2) connect them to the software supply chain; (3) frame the opening case; (4) set the course plan.

### 1.1 The opening case

Priya Nair, a quality engineer moving into application security, takes the six-month professional course at the fictional Westgate Professional Institute while working at the fictional freight company Harbourline Freight, mentored by security lead Marcus Bell. During a routine build review she noticed that one internal package, hl-auth, had been resolved from the public package registry rather than Harbourline's internal one. Nothing harmful was found in the published package, but the build had trusted a source nobody intended. Marcus asks her to treat the finding as a question about the whole build, not one package.

### 1.2 Security goals

Confidentiality, integrity and availability apply to TrackPort, Harbourline's shipment-tracking application: customer addresses must stay private, shipment records must not be altered and the service must stay up for depots. Supply chain security protects integrity before the software even runs: everything built into TrackPort must be what the team intended. For depot staff, availability matters most during shifts, when drivers and loaders update shipments in real time. Priya writes the three goals at the top of her project notes, so each later finding can be judged by which goal it threatens.

### 1.3 Why the case matters

If a build can take a package from an unintended source, someone else's code could run with TrackPort's access to customer and shipment data. Ladisa et al. (2023) catalogue this and other supply chain attack paths; the defensive response is to control and check where every dependency comes from. For TrackPort, that access includes customer addresses and phone numbers, shipment contents and delivery photos. The hl-auth package was harmless, but the same path could carry harmful code next time. Priya therefore treats the finding as a gap in source control, not a one-off incident.

### 1.4 Frameworks used

NIST SP 800-218 (SSDF) for secure development practices; OWASP ASVS 4.0.3 for application requirements; SLSA v1.0 for build integrity; OWASP SAMM v2 to judge maturity; OWASP Top 10:2021, whose A06 and A08 cover vulnerable components and software integrity failures. Each framework serves a different purpose in the project. SSDF names the development practices Harbourline should follow; ASVS gives requirements the TrackPort team can test; SLSA describes how trustworthy a build is; SAMM lets Priya judge where Harbourline's maturity stands; and the Top 10 categories give developers familiar labels for the findings. She cites each one only where it supports a specific decision.

### 1.5 The professional role

Priya's role is to find, explain and help fix risks with developers, not to work alone. Most fixes are made by the team that owns the code. Working with developers also matters because they know TrackPort better than she does: which functions are called, which packages were added for what reason and which changes would break the depot app. Priya's job is to make findings clear enough that the owning team can act quickly, and to check afterwards that the fix worked. Marcus reviews her work and helps when a decision needs security authority.

### 1.6 Course plan

Context, authorised practice, methods, tools, workflow, controls, a supervised case, reporting, quality, a lab and a portfolio. Each part builds on the previous one. Context and authorised practice come first, because Priya needs to know the service and her limits before she reviews anything. Methods and tools follow, then the workflow that turns findings into fixes and the controls that prevent the hl-auth problem returning. The supervised case, reporting and quality checks build professional judgement, and the lab and portfolio show assessors what she can do.

### Worked example

Priya writes a one-paragraph summary of the hl-auth finding for Marcus: what was seen, why it matters, and what is not yet known (whether other internal names are affected). Marcus approves a review of all build dependencies as the first piece of work.

> **Synthetic case.** Harbourline, TrackPort and all events are synthetic.

### Errors and limits

A single finding is a starting point; avoid concluding more than the evidence shows.

### Exercises

- **EX001 — Opening finding.** What did Priya notice? *Rubric:* 3 = hl-auth resolved from public registry; 2 = partial; 1 = vague; 0 = none.
- **EX002 — Integrity link.** How does supply chain security relate to integrity? *Rubric:* 3 = ensures what is built is intended; 2 = partial; 1 = vague; 0 = none.
- **EX003 — Top 10 categories.** Which Top 10:2021 categories apply? *Rubric:* 3 = A06 and A08; 2 = one; 1 = vague; 0 = none.
- **EX004 — Role.** What is Priya's professional role? *Rubric:* 3 = find, explain, help fix with teams; 2 = partial; 1 = vague; 0 = none.
- **EX005 — Summary contents.** What did Priya's summary include? *Rubric:* 3 = seen, why matters, unknown; 2 = two; 1 = one; 0 = none.

### Synthesis

Security goals extend to everything that goes into the software.

### Continue studying — chapter 01 of 12

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Application and software supply chain security: service and stakeholder context

### Learning outcomes

You will (1) map TrackPort's users, data and dependencies; (2) identify stakeholders for supply chain decisions; (3) understand their priorities; (4) agree how to work together.

### 2.1 The service

TrackPort is a web and mobile application used by customers to track shipments and by depot staff to update them. It holds customer names, addresses and phone numbers, shipment contents and delivery photos. It depends on about 180 open-source packages and four internal packages. The four internal packages include hl-auth, hl-geo and hl-ledger, which are shared with other Harbourline applications. The data TrackPort holds makes any code in its build sensitive, whether from an open-source package or an internal one. Priya lists the packages and their sources before starting the review.

### 2.2 Stakeholders

The TrackPort developers own the code and fixes. The platform team runs the build service and the internal registry. Marcus's security team sets requirements. The product manager decides priorities. Depot managers need TrackPort available during shifts. Each stakeholder controls part of the fix: developers change TrackPort's code and lock files, the platform team changes registry settings, Marcus sets requirements and the product manager decides when work happens. Depot managers are affected by any outage caused by a change, so Priya keeps them informed about planned releases. She records these roles in the stakeholder map, so she knows whom to ask before a change touches the build service or a depot release.

### 2.3 Their priorities

Developers want few interruptions and clear findings; platform wants changes that apply to all teams; product wants features shipped; depots want no outages. A supply chain fix that ignores these will be resisted. Priya plans her approach around these priorities. Findings arrive checked and ranked, so developers spend little time on noise; the registry fix is proposed as one platform setting that protects every team; security work goes into normal sprint planning, so it competes fairly with features; and changes are released at times agreed with depot managers. Framing fixes this way makes it easier for each group to agree.

### 2.4 Agreeing ways of working

Priya agrees with the TrackPort lead that findings arrive as tickets with evidence and a suggested fix, high findings are discussed within a day, and security work fits into normal sprint planning. These agreements set expectations on both sides. Tickets with evidence mean developers do not have to repeat Priya's analysis, and a suggested fix gives them a starting point. Discussing high findings within a day means urgent issues are not left waiting for the next sprint. Fitting work into sprint planning lets the product manager see security work alongside features. The lead and Priya review the arrangement after the first month.

### 2.5 The registry decision

Who should decide how package sources are configured? The platform team, because one change protects every team using the build service. If each development team configured package sources separately, some would miss the rule and the hl-auth problem could recur elsewhere. The platform team runs the build service for every team, so a single setting there gives the same protection to all. Priya explains the finding to the platform team in terms of their priority: one change instead of many. They agree to change the configuration within two weeks.

### 2.6 Stakeholder map

A one-page map lists each stakeholder, what they need and how they are informed. The map includes the TrackPort developers, the platform team, Marcus's security team, the product manager and depot managers. For each, it records what they need from the project and how they hear about it: tickets for developers, a short meeting for the platform team, a fortnightly note for the product manager and release notices for depot managers. Priya updates the map when people change roles, as the late medium finding later showed is necessary.

### Keeping stakeholders informed

A short monthly note to all stakeholders lists fixes made, open highs and decisions needed.

### Worked example

In a short meeting, Priya explains the hl-auth finding to the platform team in terms of their priority: a single registry setting would stop internal names being taken from the public registry for every team. They agree to change the build service configuration within two weeks.

> **Synthetic case.** People and systems are synthetic.

### Errors and limits

Stakeholder priorities change; revisit the map each quarter.

### Exercises

- **EX006 — Data held.** What data does TrackPort hold? *Rubric:* 3 = names, addresses, phones, contents, photos; 2 = three; 1 = one; 0 = none.
- **EX007 — Fix owner.** Who owns fixes in TrackPort code? *Rubric:* 3 = TrackPort developers; 2 = partial; 1 = vague; 0 = none.
- **EX008 — Registry owner.** Why does the platform team own the registry fix? *Rubric:* 3 = one change protects all teams; 2 = partial; 1 = vague; 0 = none.
- **EX009 — Ways of working.** What did Priya agree with the lead? *Rubric:* 3 = tickets with evidence; highs in a day; sprint planning; 2 = two; 1 = one; 0 = none.
- **EX010 — Framing.** How did Priya frame the finding for platform? *Rubric:* 3 = single setting protects all teams; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Know the service and speak to each stakeholder's priority.

### Continue studying — chapter 02 of 12

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Authorized practice and evidence handling

### Learning outcomes

You will (1) confirm authorisation before reviewing systems; (2) handle code, logs and findings as evidence; (3) protect personal data; (4) record decisions.

### 3.1 Authorisation

Priya's review of build dependencies is authorised in writing by Marcus and the TrackPort lead, naming the repositories, build logs and registry settings in scope. Reviewing other teams' systems needs their owners' agreement. Written authorisation protects Priya and Harbourline: she cannot be accused of reviewing systems without permission, and owners know exactly what she can see. The scope covers TrackPort's repositories, build logs and the registry settings that affect them. If she needs to look at another team's systems, she asks the owner and records the agreement before starting. Marcus keeps a copy of each authorisation with the project records.

### 3.2 Defensive scope

The work reads configurations, lock files and logs; it does not publish packages to public registries or test whether a public name could be taken. Such tests could affect other organisations and are not needed to fix the configuration. The question of whether someone could take an internal name on the public registry is answered by evidence already in the logs: hl-auth was resolved publicly. Testing it again by publishing a package would add nothing and could mislead other organisations' builds. Priya's evidence shows the configuration gap, and fixing the configuration is the defensive response. The limit is written into her authorisation, so nobody at Harbourline can later ask her to prove the gap by publishing a test package.

### 3.3 Evidence

The build log showing hl-auth fetched from the public registry, the lock file entry with its hash and the registry configuration are saved with dates and hashes. Hashes show that saved evidence has not changed since it was collected, which matters if the finding is challenged or later reviewed. The build log shows when hl-auth was fetched publicly, the lock file shows which version and hash were used, and the registry configuration shows why. Priya stores the evidence in a restricted folder with a short register listing each item, its date and its source.

### 3.4 Personal data

Build logs rarely contain personal data, but application logs do; Priya uses synthetic test data in any reproduction. TrackPort's application logs include customer names, addresses and shipment details, which are not needed to understand a build problem. When Priya needs to reproduce an issue, such as how a package is resolved, she uses synthetic customers and shipments in a test environment. This keeps customer data out of her evidence and her reports. Marcus confirms the approach before she begins. Test environments used for reproductions are cleared afterwards, so not even synthetic shipment data is left behind.

### 3.5 Decision records

Decisions such as "the published public hl-auth was not harmful, based on comparing its contents with our internal version" are recorded with who decided and on what evidence. Recording decisions with their evidence means a later reviewer can check whether the decision was reasonable, rather than relying on memory. For hl-auth, the comparison showed the public package was an older copy of Harbourline's own code. Each decision record names who decided, the date, the evidence and any follow-up, such as Marcus's request to the registry operator.

### 3.6 Sharing findings

Findings are shared within the teams that need them; external reporting to the registry operator is decided by Marcus. Sharing only with teams that need findings limits the spread of information about weaknesses that are not yet fixed. Decisions about contacting outside organisations rest with Marcus, because they affect Harbourline's relationships and reputation. For hl-auth, he contacted the registry operator through its official process to ask for the name to be transferred or removed. Priya records each external report with its date and outcome.

### Handling credentials found

If a review finds a real credential, Priya does not use it or test it. She reports it to the owner, who revokes and replaces it, and the finding records only where it was found.

### Worked example

Comparing the public hl-auth package with the internal one, Priya finds it is an older copy of Harbourline's own code, apparently published by mistake years ago by a former contractor. Marcus asks the registry operator, through its official process, to transfer or remove the name, and records the decision.

> **Synthetic case.** Events are synthetic.

### Errors and limits

Without written authorisation, even well-meant review can cause harm or conflict.

### Exercises

- **EX011 — Authorisation contents.** What did the authorisation name? *Rubric:* 3 = repositories, build logs, registry settings; 2 = two; 1 = one; 0 = none.
- **EX012 — Out of scope.** What did the review not do? *Rubric:* 3 = publish or test public names; 2 = partial; 1 = vague; 0 = none.
- **EX013 — Evidence saved.** What evidence was saved? *Rubric:* 3 = build log, lock entry and hash, config; 2 = two; 1 = one; 0 = none.
- **EX014 — Public package.** What was the public hl-auth? *Rubric:* 3 = old copy published by mistake; 2 = partial; 1 = vague; 0 = none.
- **EX015 — External report.** Who decides external reporting? *Rubric:* 3 = Marcus; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Work with written scope, careful evidence and recorded decisions.

### Continue studying — chapter 03 of 12

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Application and software supply chain security: core methods

### Learning outcomes

You will (1) check where each dependency is resolved from; (2) identify names close to popular packages; (3) apply source controls in the build; (4) review new dependencies.

### 4.1 Dependency sources

Every dependency should come from an intended source: internal packages from the internal registry, public packages from the public registry through a controlled proxy. A rule that internal name prefixes may only resolve internally prevents the hl-auth problem. A controlled proxy lets Harbourline record which public packages are used and block ones it does not want. The internal-prefix rule works because internal packages share a recognisable name prefix, so the build service can refuse to fetch them from anywhere else. With the rule in place, hl-auth could not have been taken from the public registry.

### Lab — dependency sources

```python
"""Check synthetic dependency sources and flag names close to well-known packages (stdlib only)."""
import difflib
internal_prefix = "hl-"
popular = ["requests-lite", "dateparse", "yamlkit", "httpwire"]
deps = [  # name, resolved source
    ("hl-geo", "internal"), ("hl-auth", "public"), ("dateparse", "public"),
    ("yamkit", "public"), ("httpwire", "public"), ("hl-ledger", "internal"),
]
for name, src in deps:
    notes = []
    if name.startswith(internal_prefix) and src != "internal":
        notes.append("internal name resolved from PUBLIC registry")
    close = [p for p in difflib.get_close_matches(name, popular, n=1, cutoff=0.8) if p != name]
    if close:
        notes.append(f"name close to '{close[0]}' - confirm intended")
    print(f"{name:10} {src:8} {'; '.join(notes) or 'ok'}")
```

Run with `python3 lab_sources.py`. Verified output:

```text
hl-geo     internal ok
hl-auth    public   internal name resolved from PUBLIC registry
dateparse  public   ok
yamkit     public   name close to 'yamlkit' - confirm intended
httpwire   public   ok
hl-ledger  internal ok
```

### 4.2 Lab result

hl-geo and hl-ledger resolve internally (ok). hl-auth is flagged: internal name resolved from PUBLIC registry. yamkit is flagged as close to the popular yamlkit, to confirm it was intended. dateparse and httpwire are ok. The close-name check uses Python's difflib and is only a prompt for a person to check. The lab confirms what the build review found and adds one more question about yamkit. A flag from difflib does not mean a package is harmful; it only asks a person to confirm the name was intended. Priya checks both flagged items with the TrackPort team before recording a decision. Yamkit later turned out to be a typing mistake for yamlkit, which the team replaced.

### 4.3 Similar names

Packages with names similar to popular ones can be installed by mistake. Ohm et al. (2020) describe how such names have been used to spread harmful packages. Reviewers confirm the intended name before approving a new dependency. At Harbourline, the yamkit flag showed how easily a similar name can slip in: a developer typed one letter wrong and nobody noticed during review. The package was unmaintained but harmless. After it was replaced, Priya added "confirm exact name" to the dependency review note, so reviewers check the name against the intended package's official page.

### 4.4 Source controls

The build service is configured so that internal prefixes resolve only from the internal registry, lock files pin versions with hashes, and builds fail on a hash mismatch. Each control closes a different gap. The prefix rule stops internal names resolving publicly. Pinned versions with hashes mean a build uses the exact package that was reviewed. Failing on a hash mismatch stops a build if a package has changed since it was pinned. The platform team applies these settings in the build service for all teams, and Priya checks them with safe tests using synthetic packages.

### 4.5 Reviewing new dependencies

A new dependency requires a short note: purpose, maintainer activity, licence and source. The note gives reviewers what they need to decide quickly. Purpose shows whether the package is needed or duplicates something already used. Maintainer activity shows whether it is likely to receive fixes. Licence shows whether Harbourline may use it. Source shows where it comes from. After yamkit, the note also asks the author to confirm the exact name. Reviewers check the note before approving the pull request that adds the dependency.

### Proxy registry

Public packages are fetched through the platform team's proxy, which records every package downloaded. The record lets Harbourline answer which builds used a package if an advisory or harmful version is announced later.

### Worked example

The yamkit flag turns out to be a real mistake: a developer meant yamlkit. yamkit is a small, unmaintained package with no harmful content found, but it is replaced, and the dependency review note now includes "confirm exact name".

> **Synthetic case.** Package names and results are synthetic.

### Errors and limits

Similar-name checks produce false alarms; they guide review, not decisions.

### Exercises

- **EX016 — Lab flags.** Which dependencies did the lab flag? *Rubric:* 3 = hl-auth public; yamkit close to yamlkit; 2 = one; 1 = vague; 0 = none.
- **EX017 — Prefix rule.** What rule prevents the hl-auth problem? *Rubric:* 3 = internal prefixes only from internal registry; 2 = partial; 1 = vague; 0 = none.
- **EX018 — Build failure.** When does the build fail? *Rubric:* 3 = hash mismatch; 2 = partial; 1 = vague; 0 = none.
- **EX019 — yamkit outcome.** What was yamkit? *Rubric:* 3 = mistaken name for yamlkit; replaced; 2 = partial; 1 = vague; 0 = none.
- **EX020 — Review note.** What does a new dependency note contain? *Rubric:* 3 = purpose, maintainers, licence, source, exact name; 2 = three; 1 = one; 0 = none.

### Synthesis

Control sources, pin hashes and review names.

### Continue studying — chapter 04 of 12

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Application and software supply chain security: tools and interpretation

### Learning outcomes

You will (1) interpret output from code, dependency and secret scanners; (2) deduplicate and rank findings; (3) judge reachability; (4) avoid alert fatigue.

### 5.1 Scanner types

Static analysis (SAST) reads code for risky patterns; software composition analysis (SCA) matches dependencies to advisories; secret scanners look for credentials. Each produces findings with different accuracy. At Harbourline, each scanner runs on every TrackPort build and produces its own list. SAST may flag code that is safe in context, SCA may report a vulnerability in a function TrackPort never calls, and secret scanners may flag test placeholders. Priya treats all scanner output as candidates to check, not as confirmed findings. She records which scanner and version produced each finding, because a changed advisory database can make the same TrackPort code produce different results.

### Lab — finding triage

```python
"""Deduplicate and rank synthetic scanner findings by severity and reachability (stdlib only)."""
from collections import Counter
findings = [  # tool, rule, file, severity, reachable
    ("sast", "sql-concat", "orders.py", "high", True),
    ("sast", "sql-concat", "orders.py", "high", True),
    ("sca", "ADV-21", "lockfile", "critical", False),
    ("sca", "ADV-22", "lockfile", "high", True),
    ("sast", "weak-hash", "legacy_export.py", "medium", False),
    ("secrets", "api-key", "tests/fixtures.py", "high", False),
    ("sast", "missing-authz", "shipments.py", "high", True),
]
unique = list(dict.fromkeys(findings))
rank = {"critical": 4, "high": 3, "medium": 2, "low": 1}
ordered = sorted(unique, key=lambda f: (f[4], rank[f[3]]), reverse=True)
print(f"raw {len(findings)}, unique {len(unique)}")
for i, (tool, rule, path, sev, reach) in enumerate(ordered, 1):
    print(f"{i}. {rule:13} {path:18} {sev:8} {'reachable' if reach else 'not reachable'}")
print("by severity:", dict(Counter(f[3] for f in unique)))
```

Run with `python3 lab_triage.py`. Verified output:

```text
raw 7, unique 6
1. sql-concat    orders.py          high     reachable
2. ADV-22        lockfile           high     reachable
3. missing-authz shipments.py       high     reachable
4. ADV-21        lockfile           critical not reachable
5. api-key       tests/fixtures.py  high     not reachable
6. weak-hash     legacy_export.py   medium   not reachable
by severity: {'high': 4, 'critical': 1, 'medium': 1}
```

### 5.2 Lab result

Seven raw findings reduce to six unique ones (the sql-concat finding in orders.py appeared twice). Ranked by reachability then severity: sql-concat in orders.py, ADV-22 and missing-authz in shipments.py are reachable highs and come first. The critical ADV-21 ranks fourth because the affected function is not reachable from TrackPort's code. The api-key in tests/fixtures.py and weak-hash in legacy_export.py follow. The ranking reflects TrackPort's real risk rather than scanner labels alone. Reachable findings come first, because an attacker could use them through TrackPort's code. The test-fixture key and the weak hash in legacy_export.py are checked separately, since neither is reachable through TrackPort's customer-facing code.

### 5.3 Reachability

A vulnerable function that the application never calls is less urgent than a reachable one, but it is still fixed in normal updates because code changes can make it reachable later. ADV-21 is a good example: it is critical, but TrackPort's code does not call the affected function, so it ranks fourth rather than first. It still gets a target date and is fixed in the next dependency update. Priya records her reachability judgement with the evidence, so a later reviewer can check it. Without a call graph tool, reachability is judged by reading code, which she notes as a limitation.

### 5.4 Checking findings

Priya reads each high finding in context. The test fixture api-key is a synthetic placeholder, so the secret scanner gets an allow-list entry with a review date. Checking in context avoids sending developers false alarms. The api-key in tests/fixtures.py is not a real credential, so it needs no rotation, but the allow-list entry has a review date so it is not ignored forever. Priya also reads the reachable highs to confirm they apply to TrackPort's code, and adds a suggested fix for each before creating the ticket.

### 5.5 Alert fatigue

Johnson et al. (2013) found that developers avoid static analysis tools largely because of false positives and poor explanations. Priya sends only checked, ranked findings with explanations. The TrackPort team's response shows why this matters: given three checked high findings with suggested fixes instead of the raw scanner list, they fixed all three in one sprint and asked for the same format in future. Priya's explanations describe the issue, where it occurs, why it matters and how to fix it, so developers do not have to research each finding themselves.

### Explaining findings

Each finding sent to developers states what the scanner saw, why it matters in TrackPort, and a suggested fix, in a few sentences, with a link to the relevant ASVS requirement.

### Worked example

The TrackPort team receives three checked high findings with suggested fixes instead of the raw scanner list. They fix all three in the sprint, and the team lead asks for the same format for future scans.

> **Synthetic case.** Findings are synthetic.

### Errors and limits

Reachability analysis can be wrong; record why something was judged unreachable.

### Exercises

- **EX021 — Dedup.** How many unique findings were there? *Rubric:* 3 = 6 of 7; 2 = partial; 1 = vague; 0 = none.
- **EX022 — Top three.** Which findings ranked first? *Rubric:* 3 = sql-concat, ADV-22, missing-authz; 2 = two; 1 = one; 0 = none.
- **EX023 — Critical rank.** Why did critical ADV-21 rank fourth? *Rubric:* 3 = not reachable; 2 = partial; 1 = vague; 0 = none.
- **EX024 — Fixture key.** How was the fixture api-key handled? *Rubric:* 3 = allow-list with review date; 2 = partial; 1 = vague; 0 = none.
- **EX025 — Fatigue.** What did Johnson et al. find? *Rubric:* 3 = false positives deter use; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Deduplicate, rank by reachability and send checked findings.

### Continue studying — chapter 05 of 12

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Application and software supply chain security: operational workflow

### Learning outcomes

You will (1) design a workflow from finding to fix; (2) assign owners and targets; (3) track progress; (4) escalate fairly.

### 6.1 The workflow

Scanner or review finding → Priya checks and ranks → ticket in TrackPort's backlog with evidence and suggested fix → developer fixes → reviewer confirms → scanner re-run closes the ticket. Each step has an owner, so a finding cannot stall without someone noticing. Priya checks and ranks, the TrackPort developer fixes, a reviewer confirms the change, and the scanner re-run gives independent confirmation that the finding has gone. A ticket closes only after the re-run, not when the developer marks it done. Ticket dates provide the data for measuring remediation against targets.

### 6.2 Targets

Remediation targets by severity: critical 7 days, high 30, medium 90. Targets are agreed with the product manager so they compete fairly with features. Agreeing targets with the product manager makes them part of planning rather than a demand from security. A critical finding needs a fix within a week, which may displace feature work, so the product manager must accept that trade-off in advance. Priya measures each finding against its target from the ticket dates. The targets are reviewed each quarter. Each ticket shows its target date from creation, so developers can plan around it without asking security.

### 6.3 Ownership

Each ticket has one owner. Platform issues go to the platform team, application issues to TrackPort. One owner means one person is responsible for moving the ticket forward. Platform issues, such as registry settings, go to the platform team because only they can change the build service. When an owner moves teams, the ticket must be reassigned, as the late medium finding later showed. Priya checks the weekly view for tickets without an active owner. A ticket left without an active owner is reassigned within a day, which is the fix for the medium finding that was forgotten when its owner moved teams.

### 6.4 Tracking

A weekly view shows open findings by age and severity. The view shows Priya and the TrackPort lead which findings are approaching their target and which have passed it. Sorting by age makes old findings visible before they are forgotten. They review it in a short meeting each week, and any finding near its target is discussed so that blocked work can be raised early. The same data feeds the remediation measures Priya reports each quarter. Marcus sees the same view at month end, so he can spot findings that need his authority, such as a risk acceptance for the product manager.

### 6.5 Escalation

Findings past their target are discussed with the lead; repeated misses go to the product manager with the risk explained. Escalation is a way to make a decision visible, not a punishment. A finding past its target may be blocked for good reasons, such as a framework upgrade. Discussing it with the lead first gives the team a chance to explain and plan. If targets keep being missed, the product manager decides whether to change priorities or accept the risk, with the risk explained in plain terms.

### 6.6 Exceptions

If a fix is not possible in time, a risk acceptance records the reason, compensating controls and a new date, signed by the product manager. A risk acceptance turns a missed target into a recorded decision. In the first month, one high finding needed a major framework upgrade, so Priya and the lead recorded an acceptance with a compensating input check and a date tied to the planned upgrade. The product manager's signature shows who accepted the risk. Each acceptance is reviewed on its date, and Priya tracks it in the weekly view.

### Weekly review

Each week Priya and the TrackPort lead spend fifteen minutes on the open-findings view: what closed, what is nearing its target and what is blocked. Blocked items get a decision in the meeting, either help from another team or a risk acceptance. The short regular meeting prevents surprises at the end of the quarter. Over three months, the number of findings past target falls from nine to two, and both have signed risk acceptances. The lead remarks that the meeting saves time, because questions are answered in one place instead of across many messages.

### Worked example

In the first month, one high finding is blocked because the fix needs a major framework upgrade. Instead of letting it age quietly, Priya and the lead record a risk acceptance with a compensating input check and a date tied to the planned upgrade.

> **Synthetic case.** Workflow and events are synthetic.

### Errors and limits

Targets without tracking are ignored; tracking without fair escalation creates resentment.

### Exercises

- **EX026 — Workflow.** Outline the workflow. *Rubric:* 3 = finding, check, ticket, fix, confirm, rescan; 2 = four; 1 = two; 0 = none.
- **EX027 — Targets.** What are the targets? *Rubric:* 3 = critical 7, high 30, medium 90; 2 = two; 1 = one; 0 = none.
- **EX028 — Agreed with.** Who agreed the targets? *Rubric:* 3 = product manager; 2 = partial; 1 = vague; 0 = none.
- **EX029 — Exception record.** What does a risk acceptance contain? *Rubric:* 3 = reason, compensating controls, new date, signature; 2 = three; 1 = one; 0 = none.
- **EX030 — Blocked fix.** How was the blocked fix handled? *Rubric:* 3 = risk acceptance with compensating check; 2 = partial; 1 = vague; 0 = none.

### Synthesis

A clear workflow turns findings into tracked fixes.

### Continue studying — chapter 06 of 12

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Application and software supply chain security: controls and verification

### Learning outcomes

You will (1) put build and dependency controls in place; (2) verify each with safe tests; (3) record provenance for releases; (4) check controls stay effective.

### 7.1 Controls chosen

Internal-prefix rule in the build service; lock files with hashes; build failure on mismatch; dependency review notes; pinned build actions; least-privilege build tokens; and provenance for each TrackPort release. Together the controls cover the path from source to release. The prefix rule, lock files, hash checks and review notes protect what goes into the build. Pinned build actions stop a build step changing without review, and least-privilege tokens limit what a compromised build could do. Provenance records how each release was built. Priya records each control with its owner and how it is tested.

### 7.2 Provenance

The build service produces a signed provenance statement naming the source commit, builder and inputs. SLSA v1.0 build level 2 requires provenance signed by a hosted build platform. Tools such as in-toto (Torres-Arias et al., 2019) and Sigstore (Newman et al., 2022) support creating and verifying such statements. For TrackPort, provenance means the deployment system can check that a release came from Harbourline's build service and a known commit. A release built elsewhere, or with unexpected inputs, can be refused. Priya records which SLSA level the build meets and how verification is done at deployment.

### 7.3 Verifying controls

Each control gets a safe test using synthetic internal packages: a test project naming a fake internal package confirms the build refuses to resolve it publicly; a lock file with an altered hash confirms the build fails; a release without provenance is refused by deployment. Each test uses synthetic packages and releases, so no real system or public registry is touched. A control that passes the test has shown it works, not only that it is configured. Priya records each test with its date and result, and the tests become the weekly checks.

### 7.4 Recording results

Tests and results are stored with dates; failures become tickets. Storing results gives auditors and Marcus evidence that controls worked on a given date. When a test fails, a ticket goes to the control's owner with the result and date, so the failure is fixed rather than noted. Two months after the controls were introduced, a build service upgrade reset the registry configuration, and the weekly test failed the next morning. The platform team restored the internal-prefix rule the same day.

### 7.5 Ongoing checks

The tests run automatically each week, so a configuration change that weakens a control is caught quickly. Configuration can change without anyone intending to weaken a control, for example when a build service upgrade resets settings to defaults. Running the tests automatically each week means such a change is noticed within days. When the registry rule was reset, the test caught it before any build used the default. The platform team receives the results, and Priya reviews them each month.

### 7.6 SSDF mapping

These controls address SSDF practices for protecting all forms of code and verifying third-party software. The prefix rule, hashes and provenance protect code and builds from tampering, while review notes and the source check support verifying third-party software before it is used. Mapping controls to SSDF practices shows Marcus and auditors which practices Harbourline now follows and where gaps remain. Priya records the mapping in her portfolio, with the evidence for each control. Gaps, such as manual reachability checks, are listed beside the mapped practices.

### Rolling out controls

Controls are introduced one at a time with a week's notice to developers, starting with lock-file hash checks in warning mode. Once warnings are cleared, the check becomes blocking, which avoids surprising teams with failed builds.

### Worked example

Two months later, a build service upgrade resets the registry configuration to defaults. The weekly test fails the next morning, and the platform team restores the internal-prefix rule the same day, before any build used the default.

> **Synthetic case.** Controls and events are synthetic.

### Errors and limits

Provenance shows how a release was built; it does not show the code is free of flaws.

### Exercises

- **EX031 — Controls.** List four controls. *Rubric:* 3 = prefix rule, hashes, mismatch failure, review notes, pinned actions, tokens, provenance; 2 = three; 1 = one; 0 = none.
- **EX032 — SLSA L2.** What does SLSA build L2 require? *Rubric:* 3 = provenance signed by hosted platform; 2 = partial; 1 = vague; 0 = none.
- **EX033 — Prefix test.** How is the prefix rule tested? *Rubric:* 3 = fake internal package must not resolve publicly; 2 = partial; 1 = vague; 0 = none.
- **EX034 — Upgrade catch.** What did the weekly test catch? *Rubric:* 3 = upgrade reset registry config; 2 = partial; 1 = vague; 0 = none.
- **EX035 — Provenance limit.** What does provenance not prove? *Rubric:* 3 = code free of flaws; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Controls need tests that keep running.

### Continue studying — chapter 07 of 12

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Application and software supply chain security: supervised case analysis

### Learning outcomes

You will (1) analyse a supply chain case under supervision; (2) build a timeline; (3) identify causes and missed signals; (4) recommend proportionate changes.

### 8.1 The case

Marcus asks Priya to analyse a synthetic case from another Harbourline team: a mobile app release included an analytics library update that began collecting device identifiers the privacy notice did not mention. The case is relevant because the same kind of dependency update happens in TrackPort every week. The library was not harmful in the usual sense, but it changed what the app did with customers' device data without anyone noticing. Priya's task is to explain how this happened and recommend changes that would catch similar updates without slowing the team.

### 8.2 Timeline

Day 0 the update was merged with a lock file change of 400 lines; day 3 released; day 20 a customer asked about data collection; day 22 the library was rolled back. The timeline shows that the change was released three days after merging and ran for nearly three weeks before a customer noticed. Rolling it back took two days once the question arrived. Priya lists each step with its source, such as the merge record and release log. The mobile team confirms each date from its merge and release records, so the timeline rests on evidence rather than memory.

### 8.3 Causes

The update was bundled with dozens of other changes, so reviewers did not notice a new data collection feature. There was no rule requiring privacy review for analytics libraries. The causes lie in the process, not in one reviewer's attention. A 400-line lock file change hides individual updates, and without a rule for analytics libraries, nobody thought to ask whether data collection had changed. Priya describes both causes without naming the developer or reviewer, since anyone could have missed the change under the same process.

### 8.4 Missed signals

The library's release notes mentioned the new collection feature; nobody read them because updates were routine. The information needed to catch the change was public all along. Release notes for most updates contain only fixes, so reading them seemed unnecessary. For analytics and advertising libraries, however, a new feature can mean new data collection. Priya recommends reading release notes for those libraries only, which is a small, targeted change. The mobile team agrees, and adds a short checklist of the libraries this applies to.

### 8.5 Recommendations

Separate pull requests for analytics and advertising libraries; release-note reading for those libraries; a privacy check in the release checklist. Each recommendation addresses a cause. Separate pull requests make analytics updates visible instead of hiding them among others. Reading release notes for those libraries catches new features. A privacy check in the release checklist gives a final chance to ask whether data collection changed. The mobile team adopts all three, and Priya records them in the case report. Each recommendation has a named owner in the mobile team and a date for the first check that it is being followed.

### 8.6 Proportion

The recommendations add minutes to a few updates rather than slowing all updates. Marcus asked Priya to remove a recommendation that would have required security sign-off for every update; it would have slowed all work to address a risk in a few libraries. The remaining recommendations apply only to analytics and advertising libraries. This proportion is why the mobile team accepted them, and why they are likely to be followed. The team reviews them after three months to check that they still fit.

### Interviewing the team

Priya talks to the mobile developers and reviewer involved, asking what they saw and what they would have needed to notice the change. The conversations are framed around the process, and people speak openly. Their main point is that the 400-line lock file change gave no hint of which library mattered; a short summary of updated libraries in the pull request would have helped. This becomes a fourth, lightweight improvement: the update bot now lists changed libraries at the top of each pull request.

### Worked example

Marcus reviews Priya's analysis and asks her to cut one recommendation that would have required security sign-off for every update. She agrees it was disproportionate, and the final report keeps the three targeted changes, which the mobile team adopts.

> **Synthetic case.** The case is synthetic.

### Errors and limits

Hindsight makes signals look obvious; judge decisions by what was knowable at the time.

### Exercises

- **EX036 — Case.** What happened? *Rubric:* 3 = analytics update collected identifiers without notice; 2 = partial; 1 = vague; 0 = none.
- **EX037 — Cause.** Why was it missed? *Rubric:* 3 = bundled in large change; no privacy rule; 2 = partial; 1 = vague; 0 = none.
- **EX038 — Missed signal.** What signal was missed? *Rubric:* 3 = release notes; 2 = partial; 1 = vague; 0 = none.
- **EX039 — Recommendations.** List the recommendations. *Rubric:* 3 = separate PRs; read notes; privacy check; 2 = two; 1 = one; 0 = none.
- **EX040 — Cut item.** What did Marcus ask Priya to cut and why? *Rubric:* 3 = sign-off for every update; disproportionate; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Analyse cases fairly and recommend proportionate changes.

### Continue studying — chapter 08 of 12

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Communication, ethics and reporting

### Learning outcomes

You will (1) write clear findings and reports for different readers; (2) communicate uncertainty; (3) act ethically with information; (4) report externally through proper channels.

### 9.1 Readers

Developers need precise locations and fixes; managers need risk, cost and decisions; customers need plain explanations of impact. One finding may need three versions. For hl-auth, developers needed the registry setting and the build log; the platform team needed the configuration change; Marcus and the product manager needed the risk, the decision and the cost. Priya writes each version from the same evidence, so they do not contradict each other. Customers would only need an explanation if their data had been affected, which it was not.

### 9.2 Structure

A finding report: summary, what was found, evidence, impact in TrackPort's context, recommendation, owner and target date. The same structure is used for every finding, so readers know where to look. The summary gives the main point in one or two sentences. Evidence and impact explain why the finding matters for TrackPort specifically. The recommendation, owner and date tell the team what happens next. The TrackPort team found this format easy to act on and asked for it in future scans.

### 9.3 Uncertainty

Say what is known and unknown: "No harmful content was found in the public hl-auth package; we cannot rule out that it was downloaded by others." Stating what is unknown prevents readers from assuming a problem is fully resolved. For hl-auth, the comparison showed no harmful content, but Harbourline cannot know who else downloaded the public package. Priya writes such sentences carefully, separating evidence from inference, and asks Marcus to check them. Readers can then judge the remaining hl-auth risk for themselves instead of assuming the finding is fully closed.

### 9.4 Ethics

Findings about other organisations' packages are reported through official channels, never publicised to embarrass. Information about weaknesses is shared only with those who need it. The public hl-auth package was published by mistake, apparently by a former contractor, and reporting it through the registry operator's official process fixed the problem without blame. Publicising it would have exposed Harbourline's mistake and helped nobody. Priya and Marcus share details of unfixed weaknesses only with the teams that need them to act. Any exception, such as sharing details with a vendor's support team, needs Marcus's approval and is recorded with its reason.

### 9.5 External reporting

Vulnerabilities in open-source dependencies found by Harbourline are reported privately to maintainers following their security policy, with time to fix. Private reporting gives maintainers time to release a fix before details are public. When Priya found a minor flaw in a library TrackPort uses, she reported it following the project's security policy, with a description and a suggested fix. The maintainer released a fix in three weeks, and TrackPort updated within the high target. Marcus approved the report before it was sent, because a disclosure in Harbourline's name affects its relationship with the project's maintainers.

### 9.6 Tone

Reports describe systems and processes, not individual blame. Blaming individuals discourages people from reporting problems and rarely fixes the cause. The analytics case was a process gap, not a careless reviewer, and the public hl-auth package came from a mistake years ago. Priya writes findings about missing rules, settings and checks, which teams can fix. Marcus reviews reports for tone before they are shared. Where a person's action is relevant, the report describes the action and the missing safeguard, not the person's name.

### Reporting to managers

For the product manager, Priya writes one page: the risk in plain terms, what was done, what remains, the cost in developer days, and the decision needed. She avoids jargon such as CVE identifiers unless asked. Decisions come faster when options and their costs are laid out side by side. Over the course, the product manager starts asking for the same format from other teams, and Marcus adopts it for quarterly risk reviews. Priya keeps a small library of example reports, with all names synthetic, for new team members.

### Worked example

Priya finds a minor flaw in an open-source library TrackPort uses. Following the project's security policy, she reports it privately with a description and a suggested fix. The maintainer releases a fix in three weeks and credits Harbourline, and TrackPort updates within the high target.

> **Synthetic case.** Events are synthetic.

### Errors and limits

Overconfident reports damage trust when facts change; state uncertainty early.

### Exercises

- **EX041 — Report structure.** List the finding report sections. *Rubric:* 3 = summary, finding, evidence, impact, recommendation, owner, date; 2 = four; 1 = two; 0 = none.
- **EX042 — Readers.** What do managers need? *Rubric:* 3 = risk, cost, decisions; 2 = partial; 1 = vague; 0 = none.
- **EX043 — Uncertainty.** How is uncertainty expressed? *Rubric:* 3 = state known and unknown; 2 = partial; 1 = vague; 0 = none.
- **EX044 — External report.** How was the library flaw reported? *Rubric:* 3 = privately per security policy; 2 = partial; 1 = vague; 0 = none.
- **EX045 — Tone.** What should reports avoid? *Rubric:* 3 = individual blame; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Write for the reader, state uncertainty and report responsibly.

### Continue studying — chapter 09 of 12

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Application and software supply chain security: quality and troubleshooting

### Learning outcomes

You will (1) measure whether the workflow meets its targets; (2) find where it fails; (3) troubleshoot slow fixes; (4) improve the process.

### 10.1 Measuring

Priya measures how many findings were fixed within target, by severity, from the ticket records. Ticket records show when each finding was created, ranked and closed after the scanner re-run, so time to fix can be calculated without extra reporting. Measuring by severity shows whether the most important findings are fixed fastest. Priya counts findings as on time if they closed within their target, and records the definition so later figures are comparable. Reopened tickets count from their first creation date, so a fix that failed the scanner re-run cannot reset the clock.

### Lab — remediation targets

```python
"""Measure remediation within target days per severity on synthetic records (stdlib only)."""
targets = {"critical": 7, "high": 30, "medium": 90}
records = [("critical", 3), ("critical", 9), ("high", 12), ("high", 25), ("high", 41), ("high", 18),
           ("medium", 60), ("medium", 120), ("medium", 45), ("medium", 80)]
for sev, t in targets.items():
    days = [d for s, d in records if s == sev]
    ok = sum(d <= t for d in days)
    print(f"{sev:8} target {t:>3}d: {ok}/{len(days)} on time ({100*ok/len(days):.0f}%), longest {max(days)}d")
```

Run with `python3 lab_sla.py`. Verified output:

```text
critical target   7d: 1/2 on time (50%), longest 9d
high     target  30d: 3/4 on time (75%), longest 41d
medium   target  90d: 3/4 on time (75%), longest 120d
```

### 10.2 Lab result

Critical: 1 of 2 on time (50%), longest 9 days against a 7-day target. High: 3 of 4 on time (75%), longest 41 days against 30. Medium: 3 of 4 on time (75%), longest 120 days against 90. The critical miss matters most despite the small numbers. The numbers are small, so percentages change sharply with one finding. Priya reports the counts beside each percentage, so readers do not overread them. The critical miss matters because criticals carry the most risk, even though only two occurred. She presents the counts to Marcus and the product manager with the causes of each miss.

### 10.3 Finding causes

Priya reviews each missed target. The late critical waited two days for a platform change; the late high was the blocked framework upgrade; the late medium was forgotten after its owner moved teams. Each miss had a different cause, which points to a different fix. The late critical shows a dependency on another team's speed; the late high shows a blocked item without an early risk decision; the late medium shows that tickets can be lost when people move. Priya records each cause with its evidence from the ticket history, without blaming the people involved.

### 10.4 Improvements

Platform requests for criticals get a same-day contact; ownership transfers when people move; blocked items get risk acceptances earlier. Each improvement answers one cause. A same-day platform contact means criticals are not left waiting for another team's queue. Transferring ownership when people move keeps tickets alive. Earlier risk acceptances make blocked items visible and controlled rather than quietly late. In the next quarter, all criticals were fixed on time and highs reached 90% on time, with small sample sizes stated. Each improvement is recorded with an owner and a review date, so Priya can check next quarter whether it was actually used.

### 10.5 Troubleshooting tools

When scanners produce odd results, Priya checks versions of the scanner and its advisory data first, then the project's lock file. Odd results often come from outdated advisory data or a scanner update rather than a change in TrackPort. Checking versions first avoids chasing problems that do not exist. The lock file then shows exactly which package versions the scanner saw. Priya records what she checked and what she found, so the same problem can be diagnosed faster next time.

### Reading the lab

The lab groups records by severity, counts those within target, and prints the longest time. Priya adds the longest time because averages hide the cases that matter most, such as a critical left open for days beyond its target. She also tries changing the critical target to 10 days to show the product manager how much a target choice changes the result, which helps the discussion about what targets should be. Both runs are kept with their settings.

### Quarterly review

Every quarter the target results and causes are reviewed with the lead and product manager.

### Worked example

The next quarter, with the improvements in place, all criticals are fixed on time and highs reach 90% on time. Priya reports the numbers with their small sample sizes clearly stated.

> **Synthetic case.** Records are synthetic.

### Errors and limits

Small numbers swing widely; look at causes as well as percentages.

### Exercises

- **EX046 — Lab critical.** What was the critical result? *Rubric:* 3 = 1/2, longest 9 days; 2 = partial; 1 = vague; 0 = none.
- **EX047 — Lab high.** What was the high result? *Rubric:* 3 = 3/4, longest 41; 2 = partial; 1 = vague; 0 = none.
- **EX048 — Causes.** Name the causes of misses. *Rubric:* 3 = platform wait; blocked upgrade; owner moved; 2 = two; 1 = one; 0 = none.
- **EX049 — Fixes.** Name two improvements. *Rubric:* 3 = same-day contact; ownership transfer; early acceptance; 2 = one; 1 = vague; 0 = none.
- **EX050 — Small numbers.** Why state sample sizes? *Rubric:* 3 = percentages swing with few items; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Measure targets, find causes and improve the workflow.

### Continue studying — chapter 10 of 12

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Supervised laboratory

### Learning outcomes

You will (1) run a supervised end-to-end exercise on synthetic projects; (2) apply source checks, triage and targets; (3) produce a report; (4) reflect.

### 11.1 The exercise

Marcus sets a supervised lab with a synthetic project, depot-scan, containing lock files, scanner outputs and ticket records. Priya has three hours to produce a report. Using a synthetic project means Priya can practise the whole workflow without any risk to real systems. The project includes the same kinds of problems as TrackPort: an internal name resolved publicly, a similar name, duplicated scanner findings and past tickets. Three hours is enough to work carefully but tests whether she can prioritise. She completed the report in two hours forty minutes.

### 11.2 Steps

Run the source check (one internal name resolved publicly, one similar name); triage scanner findings (deduplicate, rank by reachability); assign targets and owners; measure past remediation; write the report. Each step repeats a method Priya used at Harbourline, applied to a project she has not seen. The steps follow the order of the real workflow, so she cannot measure remediation before she knows what was found. Marcus checks whether she explains each result and decides what matters, rather than copying lab output into the report.

### 11.3 Supervision

Marcus observes, answers questions about context, and stops any step that would touch real systems. The lab environment has no network access to public registries. Marcus answers questions that a real team would answer, such as whether a function is called from production code, but does not give hints about findings. The lab has no network access to public registries, so no step could reach a real system even by mistake. He records any question Priya asked and how she used the answer in her report.

### 11.4 The report

A two-page report with findings, evidence, recommendations and an executive summary of five lines. Keeping the report to two pages forces Priya to choose what matters. The five-line summary is written for a manager who will read nothing else. Findings follow the standard structure with evidence, impact, recommendation, owner and target. Marcus marked one recommendation as unclear about its owner, and Priya fixed it. The report became a training example for the next trainee. Marcus keeps the original draft beside the corrected one, so the training example shows how an unclear owner was fixed.

### 11.5 Assessment

Marcus scores completeness, accuracy, prioritisation and clarity. Completeness checks that every part of the task was done; accuracy checks the findings against the lab's known answers; prioritisation checks that the most important issues come first with reasons; clarity checks that the report can be acted on by its readers. Marcus records a score and a comment for each criterion, which go into Priya's portfolio. Priya's score passes each criterion, with clarity the lowest because of the unclear recommendation owner, which she fixed before the report was filed.

### 11.6 Reflection

Priya notes where she hesitated: deciding reachability without the call graph. Without a call graph, Priya had to read code to decide whether vulnerable functions were reachable, and she was not always sure. She records this as a skill to develop and as a limitation of manual review. Her development plan includes learning a call-graph tool, so reachability decisions can be checked more reliably. Marcus agrees this is the right next step. She plans to repeat the depot-scan lab with such a tool and compare the results with her manual judgements.

### Preparing for the lab

Before the lab, Priya reviews her scripts, the workflow and the report template. She practises on a smaller synthetic project to check her timing. On the day, she reads all inputs before starting, which helps her see that two scanner outputs overlapped. The lab instructions also remind her that the depot-scan names and data are synthetic and must not be compared with real registries. Her notes from the lab, including the questions she asked Marcus, are added to the portfolio as evidence of method.

### Timing

Priya keeps a timestamp for each step, showing triage took longest at about an hour.

### Worked example

Priya completes the report in two hours forty minutes. Marcus marks one recommendation as unclear about its owner; Priya fixes it. The lab report becomes a training example for the next security trainee.

> **Synthetic case.** The lab is synthetic.

### Errors and limits

A supervised lab tests method under time; real cases add politics and missing data.

### Exercises

- **EX051 — Steps.** List the lab steps. *Rubric:* 3 = sources, triage, targets, measure, report; 2 = three; 1 = one; 0 = none.
- **EX052 — Safety.** How was the lab kept safe? *Rubric:* 3 = no network to public registries; supervised; 2 = partial; 1 = vague; 0 = none.
- **EX053 — Scoring.** What did Marcus score? *Rubric:* 3 = completeness, accuracy, prioritisation, clarity; 2 = two; 1 = one; 0 = none.
- **EX054 — Fix.** What did Marcus flag? *Rubric:* 3 = unclear owner; 2 = partial; 1 = vague; 0 = none.
- **EX055 — Hesitation.** Where did Priya hesitate? *Rubric:* 3 = reachability without call graph; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Practise the whole method under supervision.

### Continue studying — chapter 11 of 12

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Practice portfolio and final review

### Learning outcomes

You will (1) assemble a portfolio of practice evidence; (2) map it to frameworks; (3) reflect on growth; (4) plan continued development.

### 12.1 Portfolio contents

The hl-auth finding and its resolution; the dependency source review; the triage format adopted by TrackPort; the workflow and its metrics; the case analysis; the private disclosure; the supervised lab report. Each item shows a different competence: the hl-auth finding shows investigation and communication; the source review shows method; the triage format shows working with developers; the workflow and metrics show sustained improvement; the case analysis shows judgement; the private disclosure shows ethics; and the lab report shows independent work. Priya arranges the items in the order the work happened, each with its date and a pointer to the ticket, log or test result behind it.

### 12.2 Mapping

Priya maps each item to SSDF practice groups and to OWASP SAMM v2 practices such as Threat Assessment, Security Requirements, Secure Build and Defect Management, showing where Harbourline's maturity rose. Mapping to recognised practices lets assessors and Harbourline compare her work with an external standard. SAMM practices show where maturity rose, such as Secure Build after the source controls and Defect Management after the workflow. Priya includes the evidence for each mapping, so assessors can judge the claim rather than accept it.

### 12.3 Outcomes

Internal names can no longer resolve publicly; criticals are fixed on time; findings arrive checked and ranked; releases carry provenance. Each outcome is supported by evidence in the portfolio: the weekly tests show internal names cannot resolve publicly, the next quarter's tickets show criticals fixed on time, the TrackPort team's tickets show findings arriving checked and ranked, and the deployment system's records show releases carry provenance. Priya states each outcome only as far as the evidence supports. Marcus checks each outcome against the evidence before the portfolio goes to the assessor, and notes the weekly test log as the strongest item.

### 12.4 Limits

Coverage is TrackPort and the shared build service; other teams have not yet adopted the triage workflow; reachability is judged manually. These limits show where further work is needed. Other teams use the shared build service but not the triage workflow, so their findings may still arrive unchecked. Manual reachability judgements depend on Priya's reading of the code. She records each limit in her portfolio, so assessors and Marcus can see what the project did not cover. Marcus agrees with her list and adds that the next teams to adopt the workflow should be chosen with their leads' agreement.

### 12.5 Reflection

Priya writes that her quality-engineering habits, careful reproduction and clear evidence, transferred directly to security work. Careful reproduction helped her confirm the hl-auth finding and check each scanner result before sending it to developers. Clear evidence made her tickets easy to act on. She also notes what was new: judging risk, deciding priorities and writing for managers. Marcus agrees and adds that her careful approach made the platform team trust her findings quickly. In her new role for the logistics product group, she plans to keep both habits by reproducing every finding before raising a ticket.

### 12.6 Development plan

Next: threat modelling with Shostack's (2014) four questions for new TrackPort features, and extending the workflow to two more teams. Threat modelling would help the team find risks in new features before they are built, which complements finding issues in dependencies and code. Shostack's four questions are simple enough for developers to use in planning meetings. Extending the workflow to two more teams tests whether it works beyond TrackPort. Marcus agrees to review progress after three months. The plan is filed with her portfolio, with dates for the threat-modelling sessions and the first meeting with each of the two new teams.

### Assessor feedback

The assessor praises the disclosure handling and the measured improvements, and suggests adding a short threat model to the portfolio's next revision. Marcus adds that the triage format had the biggest effect, since it changed how developers saw security findings. Priya records both points and sets dates for each item in her plan. She also offers to present the course work to other teams, which spreads the triage format and the internal-prefix rule beyond TrackPort and gives her practice explaining security to new audiences.

### Keeping the portfolio

The portfolio is kept current after the course as a living record.

### Worked example

Marcus and the course assessor review the portfolio. It passes, and Harbourline appoints Priya as application security engineer for the logistics product group.

> **Synthetic case.** People and outcomes are synthetic.

### Errors and limits

A portfolio shows what was done; reviewers also look for honest limits.

### Exercises

- **EX056 — Contents.** Name four portfolio items. *Rubric:* 3 = finding, review, triage, workflow, case, disclosure, lab; 2 = three; 1 = one; 0 = none.
- **EX057 — SAMM practices.** Which SAMM practices were mapped? *Rubric:* 3 = threat assessment, requirements, secure build, defect management; 2 = two; 1 = one; 0 = none.
- **EX058 — Outcomes.** State two outcomes. *Rubric:* 3 = no public internal names; criticals on time; ranked findings; provenance; 2 = one; 1 = vague; 0 = none.
- **EX059 — Limits.** Name a limit. *Rubric:* 3 = only TrackPort; manual reachability; 2 = partial; 1 = vague; 0 = none.
- **EX060 — Next step.** What is Priya's next development step? *Rubric:* 3 = threat modelling; extend to more teams; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Evidence, mapping and honest limits make a strong portfolio.

### Continue studying — chapter 12 of 12

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Priya Nair, Marcus Bell, Harbourline Freight, Westgate Professional Institute, TrackPort and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** The internal package hl-auth was resolved from the public registry.

**EX002.** It ensures everything built into the application is what the team intended.

**EX003.** A06 vulnerable and outdated components and A08 software and data integrity failures.

**EX004.** To find, explain and help fix risks with the owning teams.

**EX005.** What was seen, why it matters, and what is not yet known.

**EX006.** Customer names, addresses, phone numbers, shipment contents and delivery photos.

**EX007.** The TrackPort developers.

**EX008.** One change to the build service protects every team.

**EX009.** Tickets with evidence and fixes, highs discussed within a day, security work in sprint planning.

**EX010.** As one registry setting protecting every team.

**EX011.** The repositories, build logs and registry settings in scope.

**EX012.** Publish packages or test whether public names could be taken.

**EX013.** The build log, lock file entry with hash and registry configuration.

**EX014.** An older copy of Harbourline's code published by mistake.

**EX015.** Marcus, the security lead.

**EX016.** hl-auth (internal name from public registry) and yamkit (close to yamlkit).

**EX017.** Internal name prefixes may only resolve from the internal registry.

**EX018.** When a downloaded package's hash does not match the lock file.

**EX019.** A mistaken name for yamlkit; it was replaced.

**EX020.** Purpose, maintainer activity, licence, source and confirmed exact name.

**EX021.** Six unique findings from seven raw.

**EX022.** sql-concat in orders.py, ADV-22 and missing-authz in shipments.py.

**EX023.** The affected function is not reachable from TrackPort's code.

**EX024.** An allow-list entry with a review date.

**EX025.** False positives and poor explanations deter developers from using static analysis.

**EX026.** Finding, check and rank, ticket, fix, review, rescan to close.

**EX027.** Critical 7 days, high 30, medium 90.

**EX028.** The product manager.

**EX029.** Reason, compensating controls, new date and the product manager's signature.

**EX030.** A risk acceptance with a compensating input check and a dated plan.

**EX031.** Internal-prefix rule, hash-pinned lock files, failure on mismatch, review notes, pinned actions, least-privilege tokens, provenance.

**EX032.** Provenance signed by a hosted build platform.

**EX033.** A test project naming a fake internal package must fail to resolve publicly.

**EX034.** A build service upgrade that reset the registry configuration.

**EX035.** That the code is free of flaws.

**EX036.** An analytics library update collected device identifiers not in the privacy notice.

**EX037.** It was bundled in a large change and no privacy review rule existed.

**EX038.** The release notes describing the new feature.

**EX039.** Separate pull requests, release-note reading, privacy check in releases.

**EX040.** Security sign-off for every update, because it was disproportionate.

**EX041.** Summary, finding, evidence, impact, recommendation, owner and target date.

**EX042.** Risk, cost and the decisions required.

**EX043.** By stating clearly what is known and what is not.

**EX044.** Privately to the maintainer following the project's security policy.

**EX045.** Blaming individuals.

**EX046.** 1 of 2 on time, longest 9 days.

**EX047.** 3 of 4 on time, longest 41 days.

**EX048.** A platform wait, a blocked upgrade and an owner moving teams.

**EX049.** Same-day platform contact, ownership transfer on moves, earlier risk acceptances.

**EX050.** With few items, percentages swing widely.

**EX051.** Source check, triage, targets and owners, measure remediation, write report.

**EX052.** No network access to public registries and supervision by Marcus.

**EX053.** Completeness, accuracy, prioritisation and clarity.

**EX054.** A recommendation with an unclear owner.

**EX055.** Judging reachability without a call graph.

**EX056.** hl-auth finding, source review, triage format, workflow metrics, case analysis, disclosure, lab report.

**EX057.** Threat Assessment, Security Requirements, Secure Build and Defect Management.

**EX058.** Internal names cannot resolve publicly; criticals fixed on time; ranked findings; release provenance.

**EX059.** Coverage limited to TrackPort; reachability judged manually.

**EX060.** Threat modelling for new features and extending the workflow to more teams.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, code and data in this book are synthetic unless a sentence cites a public source.

- Decan, A., Mens, T., & Constantinou, E. (2018). On the impact of security vulnerabilities in the npm package dependency network. *Proceedings of the 15th International Conference on Mining Software Repositories (MSR '18)*, 181–191. <https://doi.org/10.1145/3196398.3196401>
- Jacobs, J., Romanosky, S., Edwards, B., Adjerid, I., & Roytman, M. (2021). Exploit Prediction Scoring System (EPSS). *Digital Threats: Research and Practice*, 2(3), 1–17. <https://doi.org/10.1145/3436242>
- Johnson, B., Song, Y., Murphy-Hill, E., & Bowdidge, R. (2013). Why don't software developers use static analysis tools to find bugs? *35th International Conference on Software Engineering (ICSE)*, 672–681. <https://doi.org/10.1109/ICSE.2013.6606613>
- Kula, R. G., German, D. M., Ouni, A., Ishio, T., & Inoue, K. (2018). Do developers update their library dependencies? *Empirical Software Engineering*, 23(1), 384–417. <https://doi.org/10.1007/s10664-017-9521-5>
- Ladisa, P., Plate, H., Martinez, M., & Barais, O. (2023). SoK: Taxonomy of attacks on open-source software supply chains. *IEEE Symposium on Security and Privacy*, 1509–1526. <https://doi.org/10.1109/SP46215.2023.10179304>
- Lamb, C., & Zacchiroli, S. (2022). Reproducible builds: Increasing the integrity of software supply chains. *IEEE Software*, 39(2), 62–70. <https://doi.org/10.1109/MS.2021.3073045>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- MITRE. (2024). *CWE Top 25 Most Dangerous Software Weaknesses*. <https://cwe.mitre.org/top25/>
- Newman, Z., Meyers, J. S., & Torres-Arias, S. (2022). Sigstore: Software signing for everybody. *ACM SIGSAC Conference on Computer and Communications Security (CCS '22)*, 2353–2367. <https://doi.org/10.1145/3548606.3560596>
- NTIA. (2021). *The minimum elements for a software bill of materials (SBOM)*. U.S. Department of Commerce. <https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom>
- Ohm, M., Plate, H., Sykosch, A., & Meier, M. (2020). Backstabber's knife collection: A review of open source software supply chain attacks. *DIMVA 2020*, LNCS 12223, 23–43. <https://doi.org/10.1007/978-3-030-52683-2_2>
- OpenSSF. (2023). *SLSA: Supply-chain Levels for Software Artifacts, version 1.0*. <https://slsa.dev/spec/v1.0/>
- OWASP Foundation. (2020). *Software Assurance Maturity Model (SAMM) v2.0*. <https://owaspsamm.org/model/>
- OWASP Foundation. (2020). *Web Security Testing Guide v4.2*. <https://owasp.org/www-project-web-security-testing-guide/>
- OWASP Foundation. (2021). *Application Security Verification Standard 4.0.3*. <https://owasp.org/www-project-application-security-verification-standard/>
- OWASP Foundation. (2021). *OWASP Top 10:2021*. <https://owasp.org/Top10/>
- OWASP Foundation. (2025). *Application Security Verification Standard 5.0.0*. <https://owasp.org/www-project-application-security-verification-standard/>
- Shostack, A. (2014). *Threat modeling: Designing for security*. Wiley. ISBN 978-1-118-80999-0.
- Souppaya, M., Scarfone, K., & Dodson, D. (2022). *Secure Software Development Framework (SSDF) version 1.1* (NIST SP 800-218). NIST. <https://doi.org/10.6028/NIST.SP.800-218>
- Thompson, K. (1984). Reflections on trusting trust. *Communications of the ACM*, 27(8), 761–763. <https://doi.org/10.1145/358198.358210>
- Torres-Arias, S., Afzali, H., Kuppusamy, T. K., Curtmola, R., & Cappos, J. (2019). in-toto: Providing farm-to-table guarantees for bits and bytes. *28th USENIX Security Symposium*, 1393–1410. <https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias>
- Wermke, D., Wöhler, N., Klemmer, J. H., Fourné, M., Acar, Y., & Fahl, S. (2022). Committed to trust: A qualitative study on security & trust in open source software projects. *IEEE Symposium on Security and Privacy*, 1880–1896. <https://doi.org/10.1109/SP46214.2022.9833686>
- Zimmermann, M., Staicu, C.-A., Tenny, C., & Pradel, M. (2019). Small world with high risks: A study of security threats in the npm ecosystem. *28th USENIX Security Symposium*, 995–1010. <https://www.usenix.org/conference/usenixsecurity19/presentation/zimmerman>
