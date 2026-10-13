# Application and Software Supply Chain Security: Bachelor's Course

- Language: English (`en`); course 106, Bachelor's course (4 years).
- Editorial state: **draft**. Chapters 1–40 of 40 have hand-written teaching text; exercises EX001–EX120 have matching worked results with 0–3 rubrics; Nine offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: undergraduate students learning to build and run secure applications and trustworthy software supply chains.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: test and review only software you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic code and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one student from foundations through application security, supply-chain controls, laboratories, research and a capstone secure project template. Run each lab where it appears, attempt the three exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Lena Fischer** | Computer science student | Invented |
| **Grace Nwosu** | University application security lead and mentor | Invented |
| **CampusEats** | Fictional student-run food ordering app | Invented |
| **Hollowbrook University** | Fictional university | Invented |

### Core sources

[OWASP Top 10:2021](https://owasp.org/Top10/); OWASP [ASVS](https://owasp.org/www-project-application-security-verification-standard/) 4.0.3 and 5.0.0; OWASP [WSTG](https://owasp.org/www-project-web-security-testing-guide/) and [SAMM](https://owaspsamm.org/); NIST [SP 800-218 (SSDF)](https://doi.org/10.6028/NIST.SP.800-218); [CWE Top 25](https://cwe.mitre.org/top25/); [SLSA v1.0](https://slsa.dev/spec/v1.0/); Shostack, *Threat Modeling: Designing for Security* (Wiley, 2014). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |
| [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) |
| [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Mathematical reasoning

### Learning outcomes

You will (1) use logical statements to express security rules precisely; (2) reason with implication and negation; (3) check rules for contradictions and gaps; (4) introduce the course case.

### 1.1 The case

Lena Fischer is a computer science student at the fictional Hollowbrook University. She joins the student developer society that runs CampusEats, a web app for ordering food from campus cafés, and is mentored by Grace Nwosu, the university's application security lead. In her first month, a CampusEats developer accidentally pushed a payment-provider token to the project's public repository; a scanner flagged it two hours later and the token was revoked. The same week, the build stopped because a downloaded package did not match its recorded hash. These two events, a leaked secret and a supply-chain integrity check, start Lena's four-year journey.

### 1.2 Precise rules

Security rules are logical statements. "Only staff may change menu prices" can be written: if a user changes a price, then the user is staff. Writing rules this way exposes ambiguity: does "staff" include student volunteers who run the café till? CampusEats decides they are a separate role, "volunteer", without price rights.

Section one point two develops mathematical reasoning with a Hollowbrook University note Lena Fischer can demo offline.

Under section one point two, Grace Nwosu expects mathematical claims to carry owners and dates.

### 1.3 Implication and negation

The contrapositive of "if price change then staff" is "if not staff then no price change". Tests check the contrapositive: a volunteer tries a price change and must be refused. Negating a rule correctly matters: the opposite of "all requests are logged" is "some request is not logged", not "no requests are logged".

Section one point three develops mathematical reasoning with a Hollowbrook University note Lena Fischer can demo offline.

Under section one point three, Grace Nwosu expects mathematical claims to carry owners and dates.

### 1.4 Gaps and contradictions

Two rules "volunteers may issue refunds up to £5" and "only staff may issue refunds" contradict each other. Lena's table of roles and actions makes such conflicts visible before code is written.

Section one point four develops mathematical reasoning with a Hollowbrook University note Lena Fischer can demo offline.

Under section one point four, Grace Nwosu expects mathematical claims to carry owners and dates.

Section one point four treats the case precise rules as testable only when evidence and ticket IDs are recorded.

### 1.5 Quantifiers

"Every dependency has an owner" is a universal statement; one counterexample disproves it. Lena checks the CampusEats dependency list and finds three packages with no named owner.

Section one point five develops mathematical reasoning with a Hollowbrook University note Lena Fischer can demo offline.

Under section one point five, Grace Nwosu expects mathematical claims to carry owners and dates.

Section one point five treats the case precise rules as testable only when evidence and ticket IDs are recorded.

For section one point five, Hollowbrook University will not accept mathematical work without a written trail.

### Worked example

Lena writes CampusEats' access rules as eight logical statements and a role–action table. She finds the refund contradiction and two actions (export orders, edit opening hours) with no rule at all. The society's lead developer resolves them in a short meeting.

> **Synthetic case.** Hollowbrook University, CampusEats, its people and all events are synthetic.

### Errors and limits

Logic makes rules precise but cannot decide what the right business rule is; people must.

### Exercises

- **EX001 — Contrapositive.** Give the contrapositive of "if a user changes a price, the user is staff". *Rubric:* 3 = if not staff then no price change; 2 = partial; 1 = none; 0 = none.
- **EX002 — Negation.** Negate "all requests are logged". *Rubric:* 3 = some request is not logged; 2 = partial; 1 = wrong; 0 = none.
- **EX003 — Contradiction.** What contradiction did Lena find? *Rubric:* 3 = volunteer refunds up to £5 vs only staff refunds; 2 = partial; 1 = none; 0 = none.

### Synthesis

Precise logical rules expose gaps and contradictions before they become flaws.

### Continue studying — chapter 01 of 40

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Computing systems

### Learning outcomes

You will (1) describe the parts of a web application system; (2) trace a request from browser to database; (3) identify where third-party code runs; (4) relate system parts to security responsibilities.

### 2.1 The parts

CampusEats has a browser front end, a web server running application code, a database, a payment provider and a hosting platform. Its code depends on dozens of open-source packages fetched at build time.

Section two point one develops computing systems with a Hollowbrook University note Lena Fischer can demo offline.

Under section two point one, Grace Nwosu expects computing claims to carry owners and dates.

Section two point one treats the parts following request as testable only when evidence and ticket IDs are recorded.

### 2.2 Following a request

A student taps "order": the browser sends a request over HTTPS; the server checks the session, validates the order, writes to the database, calls the payment provider and returns a confirmation page. Each step is a place where data could be altered, exposed or lost.

Section two point two develops computing systems with a Hollowbrook University note Lena Fischer can demo offline.

Under section two point two, Grace Nwosu expects computing claims to carry owners and dates.

Section two point two treats the parts following request as testable only when evidence and ticket IDs are recorded.

### 2.3 Third-party code

Third-party code runs in three places: packages bundled into the browser code, packages on the server, and services such as payments. A flaw in any of them affects CampusEats even though the society did not write it.

Section two point three develops computing systems with a Hollowbrook University note Lena Fischer can demo offline.

Under section two point three, Grace Nwosu expects computing claims to carry owners and dates.

Section two point three treats the parts following request as testable only when evidence and ticket IDs are recorded.

### 2.4 Build and deploy

Code goes from the repository to a build service that installs dependencies, runs tests and creates a deployable bundle. The integrity check that stopped the build in Lena's first week sits at the install step.

Section two point four develops computing systems with a Hollowbrook University note Lena Fischer can demo offline.

Under section two point four, Grace Nwosu expects computing claims to carry owners and dates.

Section two point four treats the parts following request as testable only when evidence and ticket IDs are recorded.

### 2.5 Responsibilities

The society owns its code and configuration; the hosting platform owns servers; the payment provider owns payments. The university's security office sets policy and helps with reviews.

Section two point five develops computing systems with a Hollowbrook University note Lena Fischer can demo offline.

Under section two point five, Grace Nwosu expects computing claims to carry owners and dates.

Section two point five treats the parts following request as testable only when evidence and ticket IDs are recorded.

For section two point five, Hollowbrook University will not accept computing work without a written trail.

### 2.6 Shared responsibility

When responsibilities overlap or are unclear, gaps appear; Lena lists who owns each part.

Section two point six develops computing systems with a Hollowbrook University note Lena Fischer can demo offline.

Under section two point six, Grace Nwosu expects computing claims to carry owners and dates.

Section two point six treats the parts following request as testable only when evidence and ticket IDs are recorded.

For section two point six, Hollowbrook University will not accept computing work without a written trail.

Section two point six fails closed if computing evidence is missing rather than guessing.

### Inventory

Lena starts a simple inventory: every component, who owns it and where it runs.

### Worked example

Lena's request trace shows the payment provider calls CampusEats back with a "paid" notification. Nobody had checked how CampusEats knows that message is genuine. Grace marks it for chapter 17, which covers message signatures.

> **Synthetic case.** Systems and flows are synthetic.

### Errors and limits

Diagrams simplify; real systems include caches, queues and monitoring tools.

### Exercises

- **EX004 — Request steps.** Trace an order request in four steps. *Rubric:* 3 = HTTPS request, session check, validate, DB write, payment call, response (four); 2 = two; 1 = one; 0 = none.
- **EX005 — Third-party places.** Where does third-party code run? *Rubric:* 3 = browser bundle, server packages, external services; 2 = two; 1 = one; 0 = none.
- **EX006 — Unchecked message.** What gap did the trace reveal? *Rubric:* 3 = payment "paid" callback not verified; 2 = partial; 1 = none; 0 = none.

### Synthesis

Know the parts, the request path and where other people's code runs.

### Continue studying — chapter 02 of 40

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming I

### Learning outcomes

You will (1) write readable functions with clear inputs and outputs; (2) handle errors safely; (3) avoid hard-coding secrets; (4) use version control well.

### 3.1 Clear functions

Lena writes order_total(items) that adds prices from the menu table, never from the browser, because prices sent by the browser can be changed. Business values come from trusted sources.

Section three point one develops programming with a Hollowbrook University note Lena Fischer can demo offline.

Under section three point one, Grace Nwosu expects programming claims to carry owners and dates.

Section three point one treats clear functions errors secrets as testable only when evidence and ticket IDs are recorded.

For section three point one, Hollowbrook University will not accept programming work without a written trail.

### 3.2 Errors

If an item is not on the menu, the function raises an error and the order is refused. Silent defaults, like treating unknown items as free, are dangerous.

Section three point two develops programming with a Hollowbrook University note Lena Fischer can demo offline.

Under section three point two, Grace Nwosu expects programming claims to carry owners and dates.

Section three point two treats clear functions errors secrets as testable only when evidence and ticket IDs are recorded.

For section three point two, Hollowbrook University will not accept programming work without a written trail.

### 3.3 Secrets do not belong in code

The leaked token began as a hard-coded test value in a configuration file. Secrets belong in environment variables or a secrets manager, never in the repository, even for "test" keys, because repositories are copied and kept forever. OWASP Top 10:2021 A05 Security Misconfiguration and A07 Identification and Authentication Failures both relate to mishandled credentials.

Section three point three develops programming with a Hollowbrook University note Lena Fischer can demo offline.

Under section three point three, Grace Nwosu expects programming claims to carry owners and dates.

### 3.4 Version control

Each change is a commit with a clear message. A ".gitignore" file excludes local configuration files. Removing a secret in a later commit does not remove it from history; the secret must be revoked.

Section three point four develops programming with a Hollowbrook University note Lena Fischer can demo offline.

Under section three point four, Grace Nwosu expects programming claims to carry owners and dates.

Section three point four treats clear functions errors secrets as testable only when evidence and ticket IDs are recorded.

### 3.5 Pre-commit checks

A pre-commit hook scans changes for secret-like strings before they leave the developer's machine.

Section three point five develops programming with a Hollowbrook University note Lena Fischer can demo offline.

Under section three point five, Grace Nwosu expects programming claims to carry owners and dates.

Section three point five treats clear functions errors secrets as testable only when evidence and ticket IDs are recorded.

For section three point five, Hollowbrook University will not accept programming work without a written trail.

Section three point five fails closed if programming evidence is missing rather than guessing.

### Code review

Every change to CampusEats is reviewed by a second member of the society. Reviewers use a short checklist: are values from trusted sources, are errors handled, are any secrets or keys present, and are new dependencies justified? The checklist is short enough to use every time, which matters more than covering every possible issue.

### Worked example

Lena reviews the leak: the token was in config/test.env, committed because .gitignore listed "test.env" in the wrong folder. The token was revoked within two hours. The society fixes .gitignore, adds the pre-commit hook and moves all keys to the hosting platform's secret settings.

> **Synthetic case.** The leak and its handling are synthetic.

### Errors and limits

Pre-commit hooks can be skipped; server-side scanning is also needed.

### Exercises

- **EX007 — Trusted prices.** Why compute totals from the menu table? *Rubric:* 3 = browser values can be changed; 2 = partial; 1 = none; 0 = none.
- **EX008 — History lesson.** Does deleting a secret in a later commit fix a leak? *Rubric:* 3 = no; history keeps it; revoke; 2 = partial; 1 = none; 0 = none.
- **EX009 — Leak cause.** Why was the token committed? *Rubric:* 3 = .gitignore rule in wrong folder; 2 = partial; 1 = none; 0 = none.

### Synthesis

Write clear code, use trusted values and keep secrets out of repositories.

### Continue studying — chapter 03 of 40

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Academic writing

### Learning outcomes

You will (1) write clear, evidence-based academic text on security topics; (2) cite sources accurately; (3) structure arguments; (4) avoid publishing harmful detail.

### 4.1 Structure

An academic essay states a question, reviews evidence, argues and concludes. Lena's first essay asks: "Why do secrets leak into source repositories?"

Section four point one develops academic writing with a Hollowbrook University note Lena Fischer can demo offline.

Under section four point one, Grace Nwosu expects academic claims to carry owners and dates.

Section four point one treats structure evidence accurate citation as testable only when evidence and ticket IDs are recorded.

For section four point one, Hollowbrook University will not accept academic work without a written trail.

### 4.2 Evidence

She cites the OWASP Top 10:2021 for categories of failure and NIST SP 800-218 (SSDF) practice PS.1 on protecting code from unauthorised access and tampering. She uses the CampusEats incident as a case, with permission and without the token value.

Section four point two develops academic writing with a Hollowbrook University note Lena Fischer can demo offline.

Under section four point two, Grace Nwosu expects academic claims to carry owners and dates.

Section four point two treats structure evidence accurate citation as testable only when evidence and ticket IDs are recorded.

### 4.3 Accurate citation

Every claim with a source has a citation with author, year and title; quotations are marked. Lena checks each reference against the original.

Section four point three develops academic writing with a Hollowbrook University note Lena Fischer can demo offline.

Under section four point three, Grace Nwosu expects academic claims to carry owners and dates.

Section four point three treats structure evidence accurate citation as testable only when evidence and ticket IDs are recorded.

For section four point three, Hollowbrook University will not accept academic work without a written trail.

### 4.4 Responsible detail

Security writing describes weaknesses, effects and fixes, not instructions for misuse. Lena's essay explains why the token was dangerous without describing how anyone could use it.

Section four point four develops academic writing with a Hollowbrook University note Lena Fischer can demo offline.

Under section four point four, Grace Nwosu expects academic claims to carry owners and dates.

Section four point four treats structure evidence accurate citation as testable only when evidence and ticket IDs are recorded.

For section four point four, Hollowbrook University will not accept academic work without a written trail.

### 4.5 Clarity

Short sentences, defined terms, one idea per paragraph.

Section four point five develops academic writing with a Hollowbrook University note Lena Fischer can demo offline.

Under section four point five, Grace Nwosu expects academic claims to carry owners and dates.

Section four point five treats structure evidence accurate citation as testable only when evidence and ticket IDs are recorded.

For section four point five, Hollowbrook University will not accept academic work without a written trail.

Section four point five fails closed if academic evidence is missing rather than guessing.

### 4.6 Feedback

Grace comments that the essay's best paragraph is the one explaining why "test keys" are still dangerous: they often share infrastructure with live systems.

Section four point six develops academic writing with a Hollowbrook University note Lena Fischer can demo offline.

Under section four point six, Grace Nwosu expects academic claims to carry owners and dates.

Section four point six treats structure evidence accurate citation as testable only when evidence and ticket IDs are recorded.

For section four point six, Hollowbrook University will not accept academic work without a written trail.

### Sources to read

Lena keeps a reading list of standards and papers with notes on each, so she can find and cite them later. She separates standards, which define practice, from research papers, which give evidence, and notes which claims each can support.

### Plagiarism and AI tools

All wording must be the student's own or quoted with a citation. If writing tools are used, the university's rules on declaring them apply, and every citation they suggest must be checked against the real source.

### Worked example

Lena's tutor asks her to support the claim "most leaked secrets are found within hours" with evidence. She cannot find a reliable source and rewrites it as "in our case, the secret was found within two hours", which the evidence supports.

> **Synthetic case.** The essay and feedback are synthetic.

### Errors and limits

Citing a source you have not read is a serious error; read before citing.

### Exercises

- **EX010 — Essay question.** What was Lena's essay question? *Rubric:* 3 = why secrets leak into repositories; 2 = partial; 1 = none; 0 = none.
- **EX011 — Unsupported claim.** How was the unsupported claim fixed? *Rubric:* 3 = narrowed to "in our case, within two hours"; 2 = partial; 1 = none; 0 = none.
- **EX012 — Test keys.** Why are test keys still dangerous? *Rubric:* 3 = share infrastructure with live systems; 2 = partial; 1 = none; 0 = none.

### Synthesis

Write clear, cited arguments that explain without enabling harm.

### Continue studying — chapter 04 of 40

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) explain core security concepts for applications; (2) describe the OWASP Top 10:2021 categories; (3) recognise software supply chain risks; (4) read a security advisory.

### 5.1 CIA

Confidentiality protects student details and order history; integrity protects prices, orders and the code itself; availability keeps ordering working at lunchtime.

Section five point one develops security literacy with a Hollowbrook University note Lena Fischer can demo offline.

Under section five point one, Grace Nwosu expects security claims to carry owners and dates.

Section five point one treats cia owasp top supply as testable only when evidence and ticket IDs are recorded.

For section five point one, Hollowbrook University will not accept security work without a written trail.

### 5.2 OWASP Top 10:2021

The ten categories are Broken Access Control, Cryptographic Failures, Injection, Insecure Design, Security Misconfiguration, Vulnerable and Outdated Components, Identification and Authentication Failures, Software and Data Integrity Failures, Security Logging and Monitoring Failures, and Server-Side Request Forgery. The token leak relates to misconfiguration and authentication; the hash mismatch to software and data integrity.

Section five point two develops security literacy with a Hollowbrook University note Lena Fischer can demo offline.

Under section five point two, Grace Nwosu expects security claims to carry owners and dates.

### 5.3 Supply chain risks

Ohm et al. (2020) reviewed real cases of malicious open-source packages; Ladisa et al. (2023) organised attacks on open-source supply chains into a taxonomy from source to distribution. Consumers like CampusEats face both known vulnerabilities in honest packages and, more rarely, deliberately malicious ones.

Section five point three develops security literacy with a Hollowbrook University note Lena Fischer can demo offline.

Under section five point three, Grace Nwosu expects security claims to carry owners and dates.

Section five point three treats cia owasp top supply as testable only when evidence and ticket IDs are recorded.

### 5.4 Reading advisories

An advisory names the package, affected versions, fixed versions, severity and a description. A CVE identifier allows cross-referencing.

Section five point four develops security literacy with a Hollowbrook University note Lena Fischer can demo offline.

Under section five point four, Grace Nwosu expects security claims to carry owners and dates.

Section five point four treats cia owasp top supply as testable only when evidence and ticket IDs are recorded.

For section five point four, Hollowbrook University will not accept security work without a written trail.

### 5.5 Weakness names

The CWE Top 25 names common weaknesses like cross-site scripting (CWE-79) and SQL injection (CWE-89).

Section five point five develops security literacy with a Hollowbrook University note Lena Fischer can demo offline.

Under section five point five, Grace Nwosu expects security claims to carry owners and dates.

Section five point five treats cia owasp top supply as testable only when evidence and ticket IDs are recorded.

For section five point five, Hollowbrook University will not accept security work without a written trail.

Section five point five fails closed if security evidence is missing rather than guessing.

### Severity

Advisories include severity scores, often using CVSS. Severity describes how bad a flaw could be in general, not how bad it is for CampusEats. Lena learns to ask two more questions: is the affected function used, and is the system exposed to the internet? EPSS (Jacobs et al., 2021) adds an estimate of how likely exploitation is.

### Keeping up

Lena subscribes to advisories for the packages CampusEats uses, through the registry's notification feature.

### Worked example

Lena reads an advisory for date-tools affecting versions below 0.4.0. CampusEats uses 0.4.2, so it is not affected. She records the check in the society's tracker, so nobody repeats it.

> **Synthetic case.** The advisory is synthetic.

### Errors and limits

Advisory version ranges can be wrong; check the fix notes when in doubt.

### Exercises

- **EX013 — Integrity examples.** Give two integrity concerns for CampusEats. *Rubric:* 3 = prices, orders, code (two); 2 = one; 1 = none; 0 = none.
- **EX014 — Two incidents mapped.** Map the two first-week incidents to Top 10 categories. *Rubric:* 3 = leak: misconfiguration/authentication; hash: integrity failures; 2 = partial; 1 = none; 0 = none.
- **EX015 — Advisory check.** Was CampusEats affected by the date-tools advisory? *Rubric:* 3 = no, 0.4.2 above affected range; 2 = partial; 1 = none; 0 = none.

### Synthesis

Shared vocabulary lets you read advisories and reason about risk.

### Continue studying — chapter 05 of 40

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Discrete structures

### Learning outcomes

You will (1) represent version ranges as sets; (2) compare versions as ordered tuples; (3) reason about which version a range selects; (4) avoid text-ordering mistakes.

### 6.1 Versions as tuples

Semantic versions such as 1.10.2 have three numbers: major, minor and patch. They are ordered as tuples: compare major first, then minor, then patch. As text, "1.10.2" sorts before "1.4.7" because the character "1" comes before "4", which is wrong.

Section six point one develops discrete structures with a Hollowbrook University note Lena Fischer can demo offline.

Under section six point one, Grace Nwosu expects discrete claims to carry owners and dates.

Section six point one treats versions as tuples ranges as testable only when evidence and ticket IDs are recorded.

### 6.2 Ranges as sets

A caret range ^1.4.0 means the set of versions at least 1.4.0 and below 2.0.0. Package managers pick the highest version in the set that is available. Understanding the set tells you which fixes you receive automatically and which need a manual change.

Section six point two develops discrete structures with a Hollowbrook University note Lena Fischer can demo offline.

Under section six point two, Grace Nwosu expects discrete claims to carry owners and dates.

Section six point two treats versions as tuples ranges as testable only when evidence and ticket IDs are recorded.

### Lab — Lab — version ranges

```python
"""Which available versions satisfy a caret range ^1.4.0 (>=1.4.0, <2.0.0)? Synthetic versions."""
def v(s): return tuple(int(x) for x in s.split("."))
available = ["1.3.9", "1.4.0", "1.4.7", "1.10.2", "2.0.0", "2.1.0"]
lo, hi = v("1.4.0"), v("2.0.0")
ok = [a for a in available if lo <= v(a) < hi]
print("satisfying:", ok)
print("highest chosen:", max(ok, key=v))
print("text sort would pick:", max(ok))
```

Run with `python3 lab_semver.py`. Verified output:

```text
satisfying: ['1.4.0', '1.4.7', '1.10.2']
highest chosen: 1.10.2
text sort would pick: 1.4.7
```

### 6.3 Lab result

Of six versions, three satisfy ^1.4.0: 1.4.0, 1.4.7 and 1.10.2. The highest, chosen correctly by tuple order, is 1.10.2. Text sorting would wrongly pick 1.4.7, which could leave a project on an older, possibly vulnerable version.

Section six point three develops discrete structures with a Hollowbrook University note Lena Fischer can demo offline.

Under section six point three, Grace Nwosu expects discrete claims to carry owners and dates.

Section six point three treats versions as tuples ranges as testable only when evidence and ticket IDs are recorded.

For section six point three, Hollowbrook University will not accept discrete work without a written trail.

### 6.4 Why it matters

If a fix is released in 1.10.2 and a tool sorts as text, it would think 1.4.7 is newest and report the project as up to date. Kula et al. (2018) showed that many projects already lag behind fixes; errors like this make it worse.

Section six point four develops discrete structures with a Hollowbrook University note Lena Fischer can demo offline.

Under section six point four, Grace Nwosu expects discrete claims to carry owners and dates.

Section six point four treats versions as tuples ranges as testable only when evidence and ticket IDs are recorded.

### 6.5 Lockfiles

A lockfile records the exact version chosen, so builds are repeatable. Ranges decide what may be chosen; lockfiles record what was chosen.

Section six point five develops discrete structures with a Hollowbrook University note Lena Fischer can demo offline.

Under section six point five, Grace Nwosu expects discrete claims to carry owners and dates.

Section six point five treats versions as tuples ranges as testable only when evidence and ticket IDs are recorded.

For section six point five, Hollowbrook University will not accept discrete work without a written trail.

### Pre-releases

Versions like 2.0.0-beta are pre-releases and usually excluded from ranges unless asked for, so tests should include them as edge cases.

### Updating safely

When a range allows a new minor version, CampusEats updates the lockfile weekly in a separate pull request, so tests can confirm nothing broke before the change is merged.

### Worked example

Lena finds a small internal script that reported "latest version" for the society's dashboard by text sorting. She replaces it with tuple comparison and adds a test with 1.4.7 versus 1.10.2.

> **Synthetic case.** Versions are synthetic.

### Errors and limits

Some ecosystems use pre-release labels and other schemes; follow each ecosystem's rules.

### Exercises

- **EX016 — Lab set.** Which versions satisfy ^1.4.0 in the lab? *Rubric:* 3 = 1.4.0, 1.4.7, 1.10.2; 2 = two; 1 = one; 0 = none.
- **EX017 — Text mistake.** What would text sorting pick and why is it wrong? *Rubric:* 3 = 1.4.7; "1" before "4" in text; 2 = partial; 1 = none; 0 = none.
- **EX018 — Range vs lockfile.** Distinguish ranges and lockfiles. *Rubric:* 3 = ranges allow; lockfile records chosen; 2 = partial; 1 = none; 0 = none.

### Synthesis

Treat versions as ordered tuples and ranges as sets, and record exact choices.

### Continue studying — chapter 06 of 40

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Networks and protocols

### Learning outcomes

You will (1) explain HTTP and HTTPS for web applications; (2) describe cookies and their security attributes; (3) explain how dependencies are downloaded over networks; (4) identify network-level protections.

### 7.1 HTTP basics

Browsers send requests with a method (GET, POST), a path, headers and sometimes a body; servers respond with a status, headers and a body. CampusEats uses HTTPS so traffic is encrypted and the server authenticated.

Section seven point one develops networks and protocols with a Hollowbrook University note Lena Fischer can demo offline.

Under section seven point one, Grace Nwosu expects networks claims to carry owners and dates.

Section seven point one treats http basics cookies security as testable only when evidence and ticket IDs are recorded.

### 7.2 Cookies

The session cookie identifies a logged-in student. Attributes protect it: Secure (only sent over HTTPS), HttpOnly (not readable by page scripts) and SameSite (limits sending with requests from other sites). ASVS session-management requirements specify these.

Section seven point two develops networks and protocols with a Hollowbrook University note Lena Fischer can demo offline.

Under section seven point two, Grace Nwosu expects networks claims to carry owners and dates.

Section seven point two treats http basics cookies security as testable only when evidence and ticket IDs are recorded.

### 7.3 Security headers

Response headers such as Strict-Transport-Security and Content-Security-Policy tell browsers to apply extra protections; chapter 25's lab checks them.

Section seven point three develops networks and protocols with a Hollowbrook University note Lena Fischer can demo offline.

Under section seven point three, Grace Nwosu expects networks claims to carry owners and dates.

Section seven point three treats http basics cookies security as testable only when evidence and ticket IDs are recorded.

For section seven point three, Hollowbrook University will not accept networks work without a written trail.

### 7.4 Downloading dependencies

Package managers download over HTTPS from registries. The lockfile's hashes allow checking that the bytes received are the ones expected (chapter 22).

Section seven point four develops networks and protocols with a Hollowbrook University note Lena Fischer can demo offline.

Under section seven point four, Grace Nwosu expects networks claims to carry owners and dates.

Section seven point four treats http basics cookies security as testable only when evidence and ticket IDs are recorded.

For section seven point four, Hollowbrook University will not accept networks work without a written trail.

### 7.5 Network protections

The hosting platform provides a firewall and rate limiting; the database is not reachable from the internet.

Section seven point five develops networks and protocols with a Hollowbrook University note Lena Fischer can demo offline.

Under section seven point five, Grace Nwosu expects networks claims to carry owners and dates.

Section seven point five treats http basics cookies security as testable only when evidence and ticket IDs are recorded.

For section seven point five, Hollowbrook University will not accept networks work without a written trail.

### 7.6 Outbound calls

CampusEats calls the payment provider; it only calls known addresses, which protects against server-side request forgery (OWASP A10).

Section seven point six develops networks and protocols with a Hollowbrook University note Lena Fischer can demo offline.

Under section seven point six, Grace Nwosu expects networks claims to carry owners and dates.

Section seven point six treats http basics cookies security as testable only when evidence and ticket IDs are recorded.

For section seven point six, Hollowbrook University will not accept networks work without a written trail.

### DNS

Before connecting, the browser looks up the server's address using DNS. The society keeps DNS records in the university's managed service with two-person approval for changes, because a changed record could send students to a fake site. Registries and package downloads also rely on DNS, which is one reason hash checks matter.

### Testing headers and cookies

A test in CI requests the home page in the test environment and checks cookie attributes and key headers, failing if any are missing.

### Worked example

Lena checks the session cookie in the browser's developer tools on the test site and finds HttpOnly missing. The fix is one configuration line; a test now checks all three attributes.

> **Synthetic case.** Configuration and findings are synthetic.

### Errors and limits

Cookie attributes reduce risk but do not replace server-side session checks.

### Exercises

- **EX019 — Cookie attributes.** Name the three cookie attributes and their purpose. *Rubric:* 3 = Secure, HttpOnly, SameSite with purposes; 2 = two; 1 = one; 0 = none.
- **EX020 — Missing attribute.** What did Lena find and fix? *Rubric:* 3 = HttpOnly missing; config; test; 2 = partial; 1 = none; 0 = none.
- **EX021 — SSRF protection.** How does CampusEats limit SSRF? *Rubric:* 3 = calls only known addresses; 2 = partial; 1 = none; 0 = none.

### Synthesis

Secure protocols, cookie attributes and headers protect the web layer.

### Continue studying — chapter 07 of 40

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Programming II

### Learning outcomes

You will (1) encode output for its context; (2) explain cross-site scripting as a weakness; (3) use framework defaults safely; (4) test output handling.

### 8.1 Untrusted data in pages

CampusEats shows student reviews of dishes. If review text is inserted into the page as HTML, any markup in it would be interpreted by the browser. This weakness, cross-site scripting (CWE-79), lets one user's text run in another user's browser.

Section eight point one develops programming ii with a Hollowbrook University note Lena Fischer can demo offline.

Under section eight point one, Grace Nwosu expects programming claims to carry owners and dates.

Section eight point one treats untrusted data in pages as testable only when evidence and ticket IDs are recorded.

### 8.2 Encoding

Encoding converts special characters to safe forms: < becomes &lt;, & becomes &amp;, " becomes &quot;. The browser then shows them as text.

Section eight point two develops programming ii with a Hollowbrook University note Lena Fischer can demo offline.

Under section eight point two, Grace Nwosu expects programming claims to carry owners and dates.

Section eight point two treats untrusted data in pages as testable only when evidence and ticket IDs are recorded.

For section eight point two, Hollowbrook University will not accept programming work without a written trail.

### Lab — Lab — escaping output

```python
"""Output encoding: user text placed into HTML with and without escaping (synthetic review)."""
import html
review = 'Great pasta <b>5/5</b> & "fast"'
print("raw:     <p>" + review + "</p>")
print("escaped: <p>" + html.escape(review) + "</p>")
```

Run with `python3 lab_escape.py`. Verified output:

```text
raw:     <p>Great pasta <b>5/5</b> & "fast"</p>
escaped: <p>Great pasta &lt;b&gt;5/5&lt;/b&gt; &amp; &quot;fast&quot;</p>
```

### 8.3 Lab result

The raw version would let the browser treat <b> as bold markup; the escaped version shows "<b>5/5</b>" as literal text, with & and quotes encoded. The review reads the same to people but cannot change the page structure.

Section eight point three develops programming ii with a Hollowbrook University note Lena Fischer can demo offline.

Under section eight point three, Grace Nwosu expects programming claims to carry owners and dates.

Section eight point three treats untrusted data in pages as testable only when evidence and ticket IDs are recorded.

### 8.4 Framework defaults

CampusEats' template engine escapes by default. Developers must not turn this off; the few places that need trusted markup use a reviewed helper.

Section eight point four develops programming ii with a Hollowbrook University note Lena Fischer can demo offline.

Under section eight point four, Grace Nwosu expects programming claims to carry owners and dates.

Section eight point four treats untrusted data in pages as testable only when evidence and ticket IDs are recorded.

For section eight point four, Hollowbrook University will not accept programming work without a written trail.

### 8.5 Context matters

Text inside an attribute, a script or a URL needs different encoding; frameworks handle common cases, which is another reason to rely on them.

Section eight point five develops programming ii with a Hollowbrook University note Lena Fischer can demo offline.

Under section eight point five, Grace Nwosu expects programming claims to carry owners and dates.

Section eight point five treats untrusted data in pages as testable only when evidence and ticket IDs are recorded.

For section eight point five, Hollowbrook University will not accept programming work without a written trail.

### 8.6 Defence in depth

A Content-Security-Policy header limits which scripts can run, reducing harm if encoding is missed somewhere.

Section eight point six develops programming ii with a Hollowbrook University note Lena Fischer can demo offline.

Under section eight point six, Grace Nwosu expects programming claims to carry owners and dates.

Section eight point six treats untrusted data in pages as testable only when evidence and ticket IDs are recorded.

For section eight point six, Hollowbrook University will not accept programming work without a written trail.

### Testing encoding

Tests insert synthetic reviews containing <, >, & and quotes and check the rendered page shows them as text. Each new template that displays user content needs such a test, and the review checklist asks for it.

### Worked example

Lena searches the code for the template engine's "unescaped" marker and finds two uses: one for a trusted logo, one for reviews. The review use is a bug from an old feature; it is removed and a test with markup in a review is added.

> **Synthetic case.** Code and reviews are synthetic.

### Errors and limits

Escaping is about output context; validating input alone cannot prevent cross-site scripting.

### Exercises

- **EX022 — XSS meaning.** What is cross-site scripting? *Rubric:* 3 = user text run as code in another's browser; 2 = partial; 1 = none; 0 = none.
- **EX023 — Lab output.** How does the escaped output differ? *Rubric:* 3 = < > & " encoded; shown as text; 2 = partial; 1 = none; 0 = none.
- **EX024 — Code search.** What did Lena's search find? *Rubric:* 3 = two unescaped uses; review one removed; test; 2 = partial; 1 = none; 0 = none.

### Synthesis

Encode output for its context and trust framework defaults.

### Continue studying — chapter 08 of 40

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Data and databases

### Learning outcomes

You will (1) design simple database tables for an application; (2) use parameterised queries; (3) handle special characters in searches safely; (4) limit database permissions.

### 9.1 Tables

CampusEats has tables for students, menu items, orders and order lines. Each order line refers to a menu item by its identifier, and prices are copied at order time so later price changes do not alter past orders.

Section nine point one develops data and databases with a Hollowbrook University note Lena Fischer can demo offline.

Under section nine point one, Grace Nwosu expects data claims to carry owners and dates.

Section nine point one treats tables parameterised queries lab as testable only when evidence and ticket IDs are recorded.

### 9.2 Parameterised queries

Queries send SQL text and values separately, so values cannot change the query's structure. This prevents SQL injection (CWE-89, OWASP A03).

Section nine point two develops data and databases with a Hollowbrook University note Lena Fischer can demo offline.

Under section nine point two, Grace Nwosu expects data claims to carry owners and dates.

Section nine point two treats tables parameterised queries lab as testable only when evidence and ticket IDs are recorded.

For section nine point two, Hollowbrook University will not accept data work without a written trail.

### Lab — Lab — safe search

```python
"""Parameterised search with LIKE: user text stays data, wildcards are escaped (synthetic menu)."""
import sqlite3
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE menu (item TEXT)")
db.executemany("INSERT INTO menu VALUES (?)", [("100% juice",), ("1000 island salad",), ("veg curry",)])
def search(text):
    pat = "%" + text.replace("\\", "\\\\").replace("%", "\\%").replace("_", "\\_") + "%"
    return [r[0] for r in db.execute("SELECT item FROM menu WHERE item LIKE ? ESCAPE '\\'", (pat,))]
print("search '100%':", search("100%"))
print("search 'curry':", search("curry"))
```

Run with `python3 lab_sqlite.py`. Verified output:

```text
search '100%': ['100% juice']
search 'curry': ['veg curry']
```

### 9.3 Lab result

Searching for "100%" returns only "100% juice". Without escaping, % is a wildcard in LIKE and "100%" would also match "1000 island salad". The lab escapes %, _ and backslash in the user's text and uses a parameter, so the search means exactly what the student typed.

Section nine point three develops data and databases with a Hollowbrook University note Lena Fischer can demo offline.

Under section nine point three, Grace Nwosu expects data claims to carry owners and dates.

Section nine point three treats tables parameterised queries lab as testable only when evidence and ticket IDs are recorded.

### 9.4 Permissions

The application's database account can read and write its tables but cannot drop tables or create users. Reporting uses a read-only account.

Section nine point four develops data and databases with a Hollowbrook University note Lena Fischer can demo offline.

Under section nine point four, Grace Nwosu expects data claims to carry owners and dates.

Section nine point four treats tables parameterised queries lab as testable only when evidence and ticket IDs are recorded.

For section nine point four, Hollowbrook University will not accept data work without a written trail.

### 9.5 Backups

Nightly encrypted backups are tested monthly by restoring to a test database.

Section nine point five develops data and databases with a Hollowbrook University note Lena Fischer can demo offline.

Under section nine point five, Grace Nwosu expects data claims to carry owners and dates.

Section nine point five treats tables parameterised queries lab as testable only when evidence and ticket IDs are recorded.

For section nine point five, Hollowbrook University will not accept data work without a written trail.

Section nine point five fails closed if data evidence is missing rather than guessing.

### Data minimisation

CampusEats stores only what it needs: name, university email, orders and dietary preferences the student chooses to share. It does not store card numbers; the payment provider handles them. Old orders are deleted after two years. Storing less reduces the harm if data leaks and simplifies compliance with data protection rules.

### Database migrations

Changes to tables are written as migration scripts, reviewed like code and applied by the pipeline, never by hand on the live database. Each migration can be rolled back.

### Worked example

A student reports that searching "50% off" shows unrelated dishes. Lena traces it to unescaped wildcards in an older search function and applies the lab's approach.

> **Synthetic case.** Data and reports are synthetic.

### Errors and limits

Parameterising values does not protect dynamic table or column names; use allowlists for those.

### Exercises

- **EX025 — Price copying.** Why copy prices into order lines? *Rubric:* 3 = later price changes do not alter past orders; 2 = partial; 1 = none; 0 = none.
- **EX026 — Wildcard issue.** Why would "100%" match the salad without escaping? *Rubric:* 3 = % wildcard in LIKE; 2 = partial; 1 = none; 0 = none.
- **EX027 — Account limits.** What can the app's database account not do? *Rubric:* 3 = drop tables, create users; 2 = partial; 1 = none; 0 = none.

### Synthesis

Keep user input as data, escape pattern characters and limit database rights.

### Continue studying — chapter 09 of 40

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Ethics and authorized practice

### Learning outcomes

You will (1) distinguish authorised from unauthorised testing; (2) follow responsible disclosure; (3) respect privacy of users; (4) apply professional codes to student projects.

### 10.1 Authorisation

Testing systems without permission is unethical and often illegal, even to "help". Lena tests only CampusEats' test environment, under written permission from the society and Grace.

Section ten point one develops ethics and authorized practice with a Hollowbrook University note Lena Fischer can demo offline.

Under section ten point one, Grace Nwosu expects ethics claims to carry owners and dates.

Section ten point one treats authorisation scope found something as testable only when evidence and ticket IDs are recorded.

For section ten point one, Hollowbrook University will not accept ethics work without a written trail.

### 10.2 Scope

Permission lists systems, time and methods. The payment provider's systems are out of scope; Lena never tests them.

Section ten point two develops ethics and authorized practice with a Hollowbrook University note Lena Fischer can demo offline.

Under section ten point two, Grace Nwosu expects ethics claims to carry owners and dates.

Section ten point two treats authorisation scope found something as testable only when evidence and ticket IDs are recorded.

For section ten point two, Hollowbrook University will not accept ethics work without a written trail.

### 10.3 Found something?

If Lena finds a flaw in another system, such as a café's own website, she reports it through the university security office rather than probing further.

Section ten point three develops ethics and authorized practice with a Hollowbrook University note Lena Fischer can demo offline.

Under section ten point three, Grace Nwosu expects ethics claims to carry owners and dates.

Section ten point three treats authorisation scope found something as testable only when evidence and ticket IDs are recorded.

For section ten point three, Hollowbrook University will not accept ethics work without a written trail.

### 10.4 Disclosure

Flaws in open-source packages used by CampusEats are reported privately to maintainers, with time to fix before publication.

Section ten point four develops ethics and authorized practice with a Hollowbrook University note Lena Fischer can demo offline.

Under section ten point four, Grace Nwosu expects ethics claims to carry owners and dates.

Section ten point four treats authorisation scope found something as testable only when evidence and ticket IDs are recorded.

For section ten point four, Hollowbrook University will not accept ethics work without a written trail.

### 10.5 Privacy

Order histories reveal habits and dietary needs. Developers access real data only when needed and log their access.

Section ten point five develops ethics and authorized practice with a Hollowbrook University note Lena Fischer can demo offline.

Under section ten point five, Grace Nwosu expects ethics claims to carry owners and dates.

Section ten point five treats authorisation scope found something as testable only when evidence and ticket IDs are recorded.

For section ten point five, Hollowbrook University will not accept ethics work without a written trail.

### 10.6 Honesty

Students must not overstate findings or hide mistakes; the society's incident notes describe the token leak honestly.

Section ten point six develops ethics and authorized practice with a Hollowbrook University note Lena Fischer can demo offline.

Under section ten point six, Grace Nwosu expects ethics claims to carry owners and dates.

Section ten point six treats authorisation scope found something as testable only when evidence and ticket IDs are recorded.

For section ten point six, Hollowbrook University will not accept ethics work without a written trail.

### Codes of conduct

Professional codes such as those of computing societies stress public good, honesty and competence. The developer society adopts a short code: test only with permission, protect user data, report problems, and admit mistakes. New members agree to it when they join, and it is discussed at the first meeting each term.

### When mistakes happen

If someone breaks a rule by accident, such as viewing real data without need, they report it and the society reviews how to prevent it. A blame-free approach encourages honest reporting.

### Record keeping

Permission letters and scope documents are stored with the project files.

### Worked example

A friend asks Lena to check whether a rival society's app has the same session-cookie problem. She declines, explaining that she has no permission, and suggests the friend tell that society about the general issue.

> **Synthetic case.** Situations are synthetic.

### Errors and limits

Laws on computer misuse differ by country; when unsure, ask before acting.

### Exercises

- **EX028 — Scope contents.** What does testing permission specify? *Rubric:* 3 = systems, time, methods; 2 = two; 1 = one; 0 = none.
- **EX029 — Rival app.** Why did Lena decline to check the rival app? *Rubric:* 3 = no permission; 2 = partial; 1 = none; 0 = none.
- **EX030 — Privacy rule.** How is developer access to real data controlled? *Rubric:* 3 = only when needed; logged; 2 = partial; 1 = none; 0 = none.

### Synthesis

Act only with permission, disclose responsibly and protect users' privacy.

### Continue studying — chapter 10 of 40

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Operating systems

### Learning outcomes

You will (1) explain processes, users and permissions on servers; (2) apply least privilege to application processes; (3) isolate build steps; (4) protect secrets at runtime.

### 11.1 Processes and users

On the hosting platform, CampusEats runs as a process under its own user with no administrator rights. Files it can change are limited to temporary and log folders. If a flaw let someone control the process, they would gain only these limited rights.

Section eleven point one develops operating systems with a Hollowbrook University note Lena Fischer can demo offline.

Under section eleven point one, Grace Nwosu expects operating claims to carry owners and dates.

Section eleven point one treats processes and users containers as testable only when evidence and ticket IDs are recorded.

### 11.2 Containers

CampusEats runs in a container: a packaged process with its own file system view. The container image is built from a small base image, reducing the number of installed programs that could have flaws. The image is rebuilt weekly to include operating system security updates.

Section eleven point two develops operating systems with a Hollowbrook University note Lena Fischer can demo offline.

Under section eleven point two, Grace Nwosu expects operating claims to carry owners and dates.

Section eleven point two treats processes and users containers as testable only when evidence and ticket IDs are recorded.

### 11.3 Build isolation

Each build runs in a fresh container that is destroyed afterwards. Package install scripts run during builds, and Ohm et al. (2020) found that malicious packages often act at install time; isolation and limited network access during builds reduce what such a script could reach.

Section eleven point three develops operating systems with a Hollowbrook University note Lena Fischer can demo offline.

Under section eleven point three, Grace Nwosu expects operating claims to carry owners and dates.

Section eleven point three treats processes and users containers as testable only when evidence and ticket IDs are recorded.

### 11.4 Secrets at runtime

The payment key is provided to the running container as an environment variable from the platform's secret store. It is never written to logs or files, and only the payment module reads it.

Section eleven point four develops operating systems with a Hollowbrook University note Lena Fischer can demo offline.

Under section eleven point four, Grace Nwosu expects operating claims to carry owners and dates.

Section eleven point four treats processes and users containers as testable only when evidence and ticket IDs are recorded.

### 11.5 Logs

The operating system and platform record process restarts, deployments and errors, which help investigate problems.

Section eleven point five develops operating systems with a Hollowbrook University note Lena Fischer can demo offline.

Under section eleven point five, Grace Nwosu expects operating claims to carry owners and dates.

Section eleven point five treats processes and users containers as testable only when evidence and ticket IDs are recorded.

For section eleven point five, Hollowbrook University will not accept operating work without a written trail.

### 11.6 Updates

Base images are pinned by digest and updated deliberately, so the team knows exactly which image each release used.

Section eleven point six develops operating systems with a Hollowbrook University note Lena Fischer can demo offline.

Under section eleven point six, Grace Nwosu expects operating claims to carry owners and dates.

Section eleven point six treats processes and users containers as testable only when evidence and ticket IDs are recorded.

For section eleven point six, Hollowbrook University will not accept operating work without a written trail.

### Worked example

Lena finds that the build container could reach any internet address. She restricts it to the package registry and the source host. The next week, a build fails because a test helper tried to download a font at install time; the team replaces the helper with one that needs no network access.

> **Synthetic case.** Platform details and events are synthetic.

### Errors and limits

Containers share the host kernel; they are isolation, not a perfect wall.

### Exercises

- **EX031 — Least privilege.** What rights does the CampusEats process have? *Rubric:* 3 = own user, no admin, write only temp/logs; 2 = partial; 1 = none; 0 = none.
- **EX032 — Install-time risk.** Why isolate builds? *Rubric:* 3 = install scripts may act at install time (Ohm et al.); 2 = partial; 1 = none; 0 = none.
- **EX033 — Network restriction.** What happened after restricting build network access? *Rubric:* 3 = font download failed; helper replaced; 2 = partial; 1 = none; 0 = none.

### Synthesis

Limit what processes and builds can do, and keep secrets out of logs and files.

### Continue studying — chapter 11 of 40

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Probability and statistics

### Learning outcomes

You will (1) compute precision and recall for a security check; (2) interpret base rates; (3) choose thresholds; (4) report uncertainty.

### 12.1 Measuring a scanner

After the token leak, CampusEats adds a secret scanner. Lena measures it on 200 synthetic commits whose true status she knows: 10 contain real secrets, 190 do not.

Section twelve point one develops probability and statistics with a Hollowbrook University note Lena Fischer can demo offline.

Under section twelve point one, Grace Nwosu expects probability claims to carry owners and dates.

Section twelve point one treats measuring scanner lab result as testable only when evidence and ticket IDs are recorded.

For section twelve point one, Hollowbrook University will not accept probability work without a written trail.

### Lab — Lab — scanner precision and recall

```python
"""Precision and recall of a secret scanner on 200 synthetic commits."""
tp, fp, fn = 9, 21, 1
print(f"precision {tp / (tp + fp):.2f}  recall {tp / (tp + fn):.2f}  flagged {tp + fp} of 200")
```

Run with `python3 lab_scanner.py`. Verified output:

```text
precision 0.30  recall 0.90  flagged 30 of 200
```

### 12.2 Lab result

The scanner flagged 30 commits: 9 true secrets (true positives) and 21 harmless strings (false positives); it missed 1 secret (false negative). Precision is 0.30: only 30% of flags are real. Recall is 0.90: it finds 90% of real secrets.

Section twelve point two develops probability and statistics with a Hollowbrook University note Lena Fischer can demo offline.

Under section twelve point two, Grace Nwosu expects probability claims to carry owners and dates.

Section twelve point two treats measuring scanner lab result as testable only when evidence and ticket IDs are recorded.

### 12.3 Base rates

With only 10 secrets in 200 commits, even a fairly accurate scanner produces more false than true flags. This is the base-rate effect. A scanner with low precision is tolerable if each flag takes seconds to check; otherwise developers start ignoring it, as Johnson et al. (2013) found for noisy tools.

Section twelve point three develops probability and statistics with a Hollowbrook University note Lena Fischer can demo offline.

Under section twelve point three, Grace Nwosu expects probability claims to carry owners and dates.

Section twelve point three treats measuring scanner lab result as testable only when evidence and ticket IDs are recorded.

### 12.4 Thresholds

Raising the threshold would cut false positives but miss more secrets. For secrets, missing one is costly, so the society keeps high recall and reduces review time instead.

Section twelve point four develops probability and statistics with a Hollowbrook University note Lena Fischer can demo offline.

Under section twelve point four, Grace Nwosu expects probability claims to carry owners and dates.

Section twelve point four treats measuring scanner lab result as testable only when evidence and ticket IDs are recorded.

For section twelve point four, Hollowbrook University will not accept probability work without a written trail.

### 12.5 Uncertainty

Ten real secrets is a small number; recall of 0.90 could easily be 0.7 or 1.0 on another sample. Lena reports counts, not just percentages.

Section twelve point five develops probability and statistics with a Hollowbrook University note Lena Fischer can demo offline.

Under section twelve point five, Grace Nwosu expects probability claims to carry owners and dates.

Section twelve point five treats measuring scanner lab result as testable only when evidence and ticket IDs are recorded.

For section twelve point five, Hollowbrook University will not accept probability work without a written trail.

### Confidence in small samples

Lena explains to the society why she reports 9 of 10 rather than 90%. With ten secrets, one more miss would drop recall to 80%. Readers who see the counts understand how much the figure could move. She plans to grow the test set each term by adding newly found synthetic examples, so the estimate becomes steadier over time.

### Worked example

Lena improves precision by ignoring strings in test fixture files marked as fake and by checking character variety (chapter 23). On a new set of 200 synthetic commits, flags drop to 15 with the same 9 secrets found.

> **Synthetic case.** Counts are synthetic.

### Errors and limits

Test sets made by the evaluator may be easier than real data.

### Exercises

- **EX034 — Lab figures.** Give precision and recall. *Rubric:* 3 = 0.30 and 0.90; 2 = one; 1 = none; 0 = none.
- **EX035 — Base-rate effect.** Why are most flags false? *Rubric:* 3 = few real secrets in many commits; 2 = partial; 1 = none; 0 = none.
- **EX036 — Threshold choice.** Why keep high recall for secrets? *Rubric:* 3 = missing one is costly; 2 = partial; 1 = none; 0 = none.

### Synthesis

Measure checks with precision and recall, mindful of base rates and small samples.

### Continue studying — chapter 12 of 40

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Identity and access

### Learning outcomes

You will (1) implement authentication and sessions securely; (2) generate unpredictable tokens; (3) enforce session expiry; (4) design role-based access control.

### 13.1 Authentication

Students sign in through the university's single sign-on service, so CampusEats never handles their passwords. Staff accounts require multi-factor authentication. OWASP Top 10:2021 A07 covers identification and authentication failures.

Section thirteen point one develops identity and access with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirteen point one, Grace Nwosu expects identity claims to carry owners and dates.

Section thirteen point one treats authentication sessions lab result as testable only when evidence and ticket IDs are recorded.

For section thirteen point one, Hollowbrook University will not accept identity work without a written trail.

### 13.2 Sessions

After sign-in, CampusEats creates a session token stored in a cookie. Tokens must be long and random so they cannot be guessed; Python's secrets module provides suitable randomness.

Section thirteen point two develops identity and access with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirteen point two, Grace Nwosu expects identity claims to carry owners and dates.

Section thirteen point two treats authentication sessions lab result as testable only when evidence and ticket IDs are recorded.

For section thirteen point two, Hollowbrook University will not accept identity work without a written trail.

### Lab — Lab — tokens and expiry

```python
"""Create random session tokens and check expiry (synthetic clock)."""
import secrets
tokens = {secrets.token_urlsafe(32): 0, secrets.token_urlsafe(32): 25}
print("token length (chars):", len(next(iter(tokens))))
now, ttl = 40, 30
for i, created in enumerate(tokens.values(), 1):
    print(f"token {i}: age {now - created} min -> {'expired' if now - created > ttl else 'valid'}")
print("distinct:", len(tokens) == 2)
```

Run with `python3 lab_session.py`. Verified output:

```text
token length (chars): 43
token 1: age 40 min -> expired
token 2: age 15 min -> valid
distinct: True
```

### 13.3 Lab result

Each token is 43 characters (32 random bytes encoded), and the two tokens are distinct. With a 30-minute limit and the clock at minute 40, the token created at minute 0 (age 40) is expired and the token created at minute 25 (age 15) is valid.

Section thirteen point three develops identity and access with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirteen point three, Grace Nwosu expects identity claims to carry owners and dates.

Section thirteen point three treats authentication sessions lab result as testable only when evidence and ticket IDs are recorded.

### 13.4 Expiry and logout

Sessions expire after 30 minutes of inactivity and are deleted on logout on the server, not just in the browser.

Section thirteen point four develops identity and access with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirteen point four, Grace Nwosu expects identity claims to carry owners and dates.

Section thirteen point four treats authentication sessions lab result as testable only when evidence and ticket IDs are recorded.

For section thirteen point four, Hollowbrook University will not accept identity work without a written trail.

### 13.5 Roles

Roles are student, volunteer, staff and admin, each with a defined set of actions from Lena's table in chapter 1. Checks happen on the server for every request.

Section thirteen point five develops identity and access with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirteen point five, Grace Nwosu expects identity claims to carry owners and dates.

Section thirteen point five treats authentication sessions lab result as testable only when evidence and ticket IDs are recorded.

For section thirteen point five, Hollowbrook University will not accept identity work without a written trail.

### 13.6 Least privilege

Admin is limited to two people; actions are logged.

Section thirteen point six develops identity and access with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirteen point six, Grace Nwosu expects identity claims to carry owners and dates.

Section thirteen point six treats authentication sessions lab result as testable only when evidence and ticket IDs are recorded.

For section thirteen point six, Hollowbrook University will not accept identity work without a written trail.

Section thirteen point six fails closed if identity evidence is missing rather than guessing.

### Access reviews

Each term, the society lists who has staff and admin roles and removes those who have left. Last term two graduates still had admin rights; they were removed. A review takes twenty minutes and closes one of the most common gaps in small teams: forgotten accounts with high privileges.

### Logging

Sign-ins, role changes and admin actions are logged with time and user.

### Worked example

Lena's test finds that logging out removed the cookie but left the session valid on the server for 30 minutes. A copied cookie would still work. The logout handler now deletes the server-side session, and a test checks it.

> **Synthetic case.** Tokens and sessions are synthetic.

### Errors and limits

Expiry times balance security against convenience; very short sessions frustrate users.

### Exercises

- **EX037 — SSO benefit.** Why use university single sign-on? *Rubric:* 3 = CampusEats never handles passwords; 2 = partial; 1 = none; 0 = none.
- **EX038 — Lab expiry.** Which token was expired and why? *Rubric:* 3 = token 1, age 40 > 30; 2 = partial; 1 = none; 0 = none.
- **EX039 — Logout fix.** What was wrong with logout? *Rubric:* 3 = server session still valid; now deleted; 2 = partial; 1 = none; 0 = none.

### Synthesis

Use strong identity, random expiring sessions and server-side role checks.

### Continue studying — chapter 13 of 40

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Privacy foundations

### Learning outcomes

You will (1) identify personal data in an application; (2) apply data protection principles; (3) design privacy-friendly features; (4) handle data subject requests.

### 14.1 Personal data

CampusEats holds names, university emails, order histories and optional dietary preferences. Dietary information can reveal health or religious beliefs, making it sensitive.

Section fourteen point one develops privacy foundations with a Hollowbrook University note Lena Fischer can demo offline.

Under section fourteen point one, Grace Nwosu expects privacy claims to carry owners and dates.

Section fourteen point one treats personal data principles privacy as testable only when evidence and ticket IDs are recorded.

For section fourteen point one, Hollowbrook University will not accept privacy work without a written trail.

### 14.2 Principles

Collect only what is needed, use it only for stated purposes, keep it accurate, delete it when no longer needed and protect it. These principles appear in data protection laws in many countries.

Section fourteen point two develops privacy foundations with a Hollowbrook University note Lena Fischer can demo offline.

Under section fourteen point two, Grace Nwosu expects privacy claims to carry owners and dates.

Section fourteen point two treats personal data principles privacy as testable only when evidence and ticket IDs are recorded.

### 14.3 Privacy by design

Dietary preferences are optional and stored separately with tighter access. Analytics use counts, not individual histories.

Section fourteen point three develops privacy foundations with a Hollowbrook University note Lena Fischer can demo offline.

Under section fourteen point three, Grace Nwosu expects privacy claims to carry owners and dates.

Section fourteen point three treats personal data principles privacy as testable only when evidence and ticket IDs are recorded.

For section fourteen point three, Hollowbrook University will not accept privacy work without a written trail.

### 14.4 Requests

Students can download or delete their data from their profile page. Deletion removes personal details but keeps anonymised order counts for café planning.

Section fourteen point four develops privacy foundations with a Hollowbrook University note Lena Fischer can demo offline.

Under section fourteen point four, Grace Nwosu expects privacy claims to carry owners and dates.

Section fourteen point four treats personal data principles privacy as testable only when evidence and ticket IDs are recorded.

For section fourteen point four, Hollowbrook University will not accept privacy work without a written trail.

### 14.5 Supply chain and privacy

Third-party scripts in the browser can see page content. CampusEats removed an analytics script that collected more than needed, replacing it with server-side counts.

Section fourteen point five develops privacy foundations with a Hollowbrook University note Lena Fischer can demo offline.

Under section fourteen point five, Grace Nwosu expects privacy claims to carry owners and dates.

Section fourteen point five treats personal data principles privacy as testable only when evidence and ticket IDs are recorded.

For section fourteen point five, Hollowbrook University will not accept privacy work without a written trail.

### 14.6 Breach response

If personal data might be exposed, the university's data protection officer must be informed quickly.

Section fourteen point six develops privacy foundations with a Hollowbrook University note Lena Fischer can demo offline.

Under section fourteen point six, Grace Nwosu expects privacy claims to carry owners and dates.

Section fourteen point six treats personal data principles privacy as testable only when evidence and ticket IDs are recorded.

For section fourteen point six, Hollowbrook University will not accept privacy work without a written trail.

### Retention schedule

Each data type has a retention period: sessions 30 minutes, order details two years, logs 90 days, deleted accounts' data removed within 30 days. A scheduled job deletes expired records automatically and reports counts, so the society can show it follows its own rules. Lena tests the job on synthetic data before enabling it.

### Privacy notice

A short privacy notice explains in plain words what data CampusEats collects, why and for how long.

### Review

The notice is reviewed yearly with the data protection officer.

### Worked example

Lena reviews the token leak for privacy impact: the token gave access to the payment provider's test environment only, with synthetic data, so no personal data was exposed. She records this assessment with the data protection officer.

> **Synthetic case.** Data and assessments are synthetic.

### Errors and limits

Anonymised data can sometimes be re-identified when combined with other data; aggregate carefully.

### Exercises

- **EX040 — Sensitive data.** Why is dietary information sensitive? *Rubric:* 3 = can reveal health or religion; 2 = partial; 1 = none; 0 = none.
- **EX041 — Analytics change.** What did CampusEats do about the analytics script? *Rubric:* 3 = removed; server-side counts; 2 = partial; 1 = none; 0 = none.
- **EX042 — Leak privacy impact.** Did the token leak expose personal data? *Rubric:* 3 = no; test environment with synthetic data; 2 = partial; 1 = none; 0 = none.

### Synthesis

Collect less, protect more and let users control their data.

### Continue studying — chapter 14 of 40

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Evidence and measurement

### Learning outcomes

You will (1) choose measures that show whether security is improving; (2) collect evidence reliably; (3) distinguish activity from outcomes; (4) present measurements honestly.

### 15.1 Activity versus outcome

"We ran the scanner 400 times" is activity. "Secrets reaching the public repository fell from 2 to 0 per term" is an outcome. Outcomes show whether risk changed.

Section fifteen point one develops evidence and measurement with a Hollowbrook University note Lena Fischer can demo offline.

Under section fifteen point one, Grace Nwosu expects evidence claims to carry owners and dates.

Section fifteen point one treats activity versus outcome measures as testable only when evidence and ticket IDs are recorded.

For section fifteen point one, Hollowbrook University will not accept evidence work without a written trail.

### 15.2 Measures for CampusEats

Time to fix high-severity advisories, number of secrets found after push (should be zero), share of dependencies with an owner, and failed integrity checks investigated.

Section fifteen point two develops evidence and measurement with a Hollowbrook University note Lena Fischer can demo offline.

Under section fifteen point two, Grace Nwosu expects evidence claims to carry owners and dates.

Section fifteen point two treats activity versus outcome measures as testable only when evidence and ticket IDs are recorded.

For section fifteen point two, Hollowbrook University will not accept evidence work without a written trail.

### 15.3 Collecting evidence

Measures come from tools automatically where possible: CI logs, scanner results, advisory tracker. Manual counts are checked by a second person.

Section fifteen point three develops evidence and measurement with a Hollowbrook University note Lena Fischer can demo offline.

Under section fifteen point three, Grace Nwosu expects evidence claims to carry owners and dates.

Section fifteen point three treats activity versus outcome measures as testable only when evidence and ticket IDs are recorded.

For section fifteen point three, Hollowbrook University will not accept evidence work without a written trail.

### 15.4 Baselines

Before changes, Lena records a baseline: last term, 2 secrets reached the public repository and median advisory fix time was 21 days.

Section fifteen point four develops evidence and measurement with a Hollowbrook University note Lena Fischer can demo offline.

Under section fifteen point four, Grace Nwosu expects evidence claims to carry owners and dates.

Section fifteen point four treats activity versus outcome measures as testable only when evidence and ticket IDs are recorded.

For section fifteen point four, Hollowbrook University will not accept evidence work without a written trail.

### 15.5 Presenting

A one-page summary per term with trends and short explanations.

Section fifteen point five develops evidence and measurement with a Hollowbrook University note Lena Fischer can demo offline.

Under section fifteen point five, Grace Nwosu expects evidence claims to carry owners and dates.

Section fifteen point five treats activity versus outcome measures as testable only when evidence and ticket IDs are recorded.

For section fifteen point five, Hollowbrook University will not accept evidence work without a written trail.

Section fifteen point five fails closed if evidence evidence is missing rather than guessing.

### 15.6 Honesty

If a measure gets worse, it is reported with a reason and plan.

Section fifteen point six develops evidence and measurement with a Hollowbrook University note Lena Fischer can demo offline.

Under section fifteen point six, Grace Nwosu expects evidence claims to carry owners and dates.

Section fifteen point six treats activity versus outcome measures as testable only when evidence and ticket IDs are recorded.

For section fifteen point six, Hollowbrook University will not accept evidence work without a written trail.

Section fifteen point six fails closed if evidence evidence is missing rather than guessing.

### Using measures to decide

Measures guide decisions. When the median fix time stayed high for one package family, the society looked closer and found those packages were maintained by a single volunteer who rarely released. The team decided to replace them. Without the measure, the problem would have stayed hidden in the overall average. Lena notes that good measures lead to questions, and questions lead to better decisions.

### Tools for evidence

A small script gathers all measures into one table each term, so collection takes minutes rather than hours.

### Audience

Results are shared with the society and Grace each term.

### Worked example

After one term with the pre-commit hook and server-side scanner, no secrets reached the public repository and the median fix time fell to 9 days. Lena notes that the society also gained two experienced members that term, which may explain part of the improvement.

> **Synthetic case.** Measures are synthetic.

### Errors and limits

Zero incidents in one term may be luck; keep measuring over longer periods.

### Exercises

- **EX043 — Activity vs outcome.** Give one activity and one outcome measure. *Rubric:* 3 = scanner runs; secrets reaching repo; 2 = partial; 1 = none; 0 = none.
- **EX044 — Baseline.** What was the baseline? *Rubric:* 3 = 2 secrets; 21-day median fix; 2 = one; 1 = none; 0 = none.
- **EX045 — Other explanation.** What else may explain the improvement? *Rubric:* 3 = two experienced members joined; 2 = partial; 1 = none; 0 = none.

### Synthesis

Measure outcomes from a baseline and report honestly, including other explanations.

### Continue studying — chapter 15 of 40

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Security architecture

### Learning outcomes

You will (1) design layered defences for a web application; (2) place trust boundaries; (3) separate environments; (4) record architecture decisions.

### 16.1 Layers

CampusEats' defences are layered: the hosting platform's firewall and rate limits at the edge; validation, encoding and authorisation in the application; least-privilege database accounts and encryption for data; and a pipeline that checks code and dependencies before anything is deployed. If one layer fails, others still protect students.

Section sixteen point one develops security architecture with a Hollowbrook University note Lena Fischer can demo offline.

Under section sixteen point one, Grace Nwosu expects security claims to carry owners and dates.

Section sixteen point one treats layers trust boundaries environments as testable only when evidence and ticket IDs are recorded.

### 16.2 Trust boundaries

Boundaries separate the browser from the server, the server from the database, CampusEats from the payment provider, and the build from the internet. At each boundary, data is checked: requests are validated, payment callbacks are verified (chapter 17), downloaded packages are hash-checked (chapter 22).

Section sixteen point two develops security architecture with a Hollowbrook University note Lena Fischer can demo offline.

Under section sixteen point two, Grace Nwosu expects security claims to carry owners and dates.

Section sixteen point two treats layers trust boundaries environments as testable only when evidence and ticket IDs are recorded.

### 16.3 Environments

Development, test and production are separate, with separate secrets. The leaked token was a test key; because test and production were separate, the leak could not touch real payments. Lena records this as evidence that separation limited harm.

Section sixteen point three develops security architecture with a Hollowbrook University note Lena Fischer can demo offline.

Under section sixteen point three, Grace Nwosu expects security claims to carry owners and dates.

Section sixteen point three treats layers trust boundaries environments as testable only when evidence and ticket IDs are recorded.

### 16.4 Secrets architecture

Secrets live in the platform's secret store, scoped per environment, rotated each term and when people leave.

Section sixteen point four develops security architecture with a Hollowbrook University note Lena Fischer can demo offline.

Under section sixteen point four, Grace Nwosu expects security claims to carry owners and dates.

Section sixteen point four treats layers trust boundaries environments as testable only when evidence and ticket IDs are recorded.

For section sixteen point four, Hollowbrook University will not accept security work without a written trail.

### 16.5 Third-party scripts

Only two third-party browser scripts remain, both loaded from CampusEats' own domain at pinned versions with integrity hashes.

Section sixteen point five develops security architecture with a Hollowbrook University note Lena Fischer can demo offline.

Under section sixteen point five, Grace Nwosu expects security claims to carry owners and dates.

Section sixteen point five treats layers trust boundaries environments as testable only when evidence and ticket IDs are recorded.

For section sixteen point five, Hollowbrook University will not accept security work without a written trail.

### 16.6 Decision records

Each architecture choice is recorded briefly: context, options, decision, consequences. When new members ask "why is it like this?", the record answers.

Section sixteen point six develops security architecture with a Hollowbrook University note Lena Fischer can demo offline.

Under section sixteen point six, Grace Nwosu expects security claims to carry owners and dates.

Section sixteen point six treats layers trust boundaries environments as testable only when evidence and ticket IDs are recorded.

For section sixteen point six, Hollowbrook University will not accept security work without a written trail.

### 16.7 Reviews

Grace reviews architecture changes that cross a trust boundary, such as adding a new external service.

Section sixteen point seven develops security architecture with a Hollowbrook University note Lena Fischer can demo offline.

Under section sixteen point seven, Grace Nwosu expects security claims to carry owners and dates.

Section sixteen point seven treats layers trust boundaries environments as testable only when evidence and ticket IDs are recorded.

For section sixteen point seven, Hollowbrook University will not accept security work without a written trail.

### Monitoring

Logs from each layer feed one dashboard, so problems at any layer are seen quickly.

### Worked example

A member proposes letting the café tills connect directly to the CampusEats database for speed. Lena's review notes this would cross a trust boundary and give till machines database credentials. Instead, the tills use a narrow API with its own role, rate-limited and logged.

> **Synthetic case.** The architecture is synthetic.

### Errors and limits

Architecture diagrams drift from reality; check configuration regularly.

### Exercises

- **EX046 — Layers.** List the four layers of defence. *Rubric:* 3 = edge, application, data, pipeline; 2 = three; 1 = one; 0 = none.
- **EX047 — Separation evidence.** How did environment separation limit the token leak? *Rubric:* 3 = test key could not reach real payments; 2 = partial; 1 = none; 0 = none.
- **EX048 — Till proposal.** What replaced direct database access for tills? *Rubric:* 3 = narrow API with own role, rate-limited, logged; 2 = partial; 1 = none; 0 = none.

### Synthesis

Layer defences, guard boundaries and separate environments.

### Continue studying — chapter 16 of 40

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Cryptography concepts

### Learning outcomes

You will (1) distinguish hashing, message authentication and encryption; (2) verify message integrity with HMAC; (3) compare secrets safely; (4) manage keys.

### 17.1 Three tools

A hash such as SHA-256 creates a fingerprint of data; anyone can compute it. A message authentication code (MAC) such as HMAC-SHA256 uses a shared secret, so only holders of the secret can create a valid tag. Encryption hides content. Integrity and secrecy are different goals.

Section seventeen point one develops cryptography concepts with a Hollowbrook University note Lena Fischer can demo offline.

Under section seventeen point one, Grace Nwosu expects cryptography claims to carry owners and dates.

Section seventeen point one treats three tools the payment as testable only when evidence and ticket IDs are recorded.

### 17.2 The payment callback

Chapter 2 found that CampusEats did not verify the payment provider's "paid" messages. Without verification, anyone who could send a request to the callback address could mark an order as paid. The provider signs each message with HMAC-SHA256 using a shared secret; CampusEats must check it.

Section seventeen point two develops cryptography concepts with a Hollowbrook University note Lena Fischer can demo offline.

Under section seventeen point two, Grace Nwosu expects cryptography claims to carry owners and dates.

Section seventeen point two treats three tools the payment as testable only when evidence and ticket IDs are recorded.

### Lab — Lab — verifying a webhook

```python
"""Verify a payment webhook's HMAC-SHA256 signature (synthetic shared secret)."""
import hmac, hashlib
secret = b"synthetic-shared-secret"
body = b'{"order":"CE-1042","status":"paid","amount":"8.50"}'
good_sig = hmac.new(secret, body, hashlib.sha256).hexdigest()
altered = body.replace(b"8.50", b"0.50")
for name, b in (("original", body), ("altered amount", altered)):
    ok = hmac.compare_digest(hmac.new(secret, b, hashlib.sha256).hexdigest(), good_sig)
    print(f"{name:15} {'accept' if ok else 'reject: signature mismatch'}")
```

Run with `python3 lab_hmac.py`. Verified output:

```text
original        accept
altered amount  reject: signature mismatch
```

### 17.3 Lab result

The original message is accepted because its signature matches. When the amount is changed from 8.50 to 0.50, the signature no longer matches and the message is rejected. The lab uses hmac.compare_digest, which compares in constant time and avoids leaking information through timing.

Section seventeen point three develops cryptography concepts with a Hollowbrook University note Lena Fischer can demo offline.

Under section seventeen point three, Grace Nwosu expects cryptography claims to carry owners and dates.

Section seventeen point three treats three tools the payment as testable only when evidence and ticket IDs are recorded.

### 17.4 Key management

The shared secret is stored in the secret store, separate for test and production, and rotated when people with access leave.

Section seventeen point four develops cryptography concepts with a Hollowbrook University note Lena Fischer can demo offline.

Under section seventeen point four, Grace Nwosu expects cryptography claims to carry owners and dates.

Section seventeen point four treats three tools the payment as testable only when evidence and ticket IDs are recorded.

For section seventeen point four, Hollowbrook University will not accept cryptography work without a written trail.

### 17.5 Do not invent crypto

Use standard algorithms and well-maintained libraries; home-made schemes fail in subtle ways. OWASP Top 10:2021 A02 covers cryptographic failures.

Section seventeen point five develops cryptography concepts with a Hollowbrook University note Lena Fischer can demo offline.

Under section seventeen point five, Grace Nwosu expects cryptography claims to carry owners and dates.

Section seventeen point five treats three tools the payment as testable only when evidence and ticket IDs are recorded.

For section seventeen point five, Hollowbrook University will not accept cryptography work without a written trail.

### 17.6 Replay

A valid message could be sent twice. The provider includes a unique event ID; CampusEats stores processed IDs and ignores repeats.

Section seventeen point six develops cryptography concepts with a Hollowbrook University note Lena Fischer can demo offline.

Under section seventeen point six, Grace Nwosu expects cryptography claims to carry owners and dates.

Section seventeen point six treats three tools the payment as testable only when evidence and ticket IDs are recorded.

For section seventeen point six, Hollowbrook University will not accept cryptography work without a written trail.

### Worked example

After adding verification, Lena runs the test suite with synthetic callbacks: valid ones mark orders paid; altered and unsigned ones are rejected and logged. In the first month in production, three unsigned requests to the callback address are logged and rejected; they came from an automated scanner on the internet.

> **Synthetic case.** Secrets and messages are synthetic.

### Errors and limits

HMAC proves the sender knows the secret; if the secret leaks, forged messages pass.

### Exercises

- **EX049 — Hash vs HMAC.** How does HMAC differ from a plain hash? *Rubric:* 3 = uses a shared secret; only holders can create tags; 2 = partial; 1 = none; 0 = none.
- **EX050 — Lab outcome.** What happened when the amount changed? *Rubric:* 3 = signature mismatch; rejected; 2 = partial; 1 = none; 0 = none.
- **EX051 — Replay defence.** How are repeated messages handled? *Rubric:* 3 = store event IDs; ignore repeats; 2 = partial; 1 = none; 0 = none.

### Synthesis

Use the right cryptographic tool for the goal and verify every signed message.

### Continue studying — chapter 17 of 40

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Research methods I

### Learning outcomes

You will (1) form a research question from practice; (2) choose between survey, experiment and case study; (3) plan ethical data collection; (4) analyse simple data.

### 18.1 Question from practice

After the token leak, Lena asks: "Do pre-commit secret hooks reduce secrets pushed by student developers?"

Section eighteen point one develops research methods with a Hollowbrook University note Lena Fischer can demo offline.

Under section eighteen point one, Grace Nwosu expects research claims to carry owners and dates.

Section eighteen point one treats question from practice choosing as testable only when evidence and ticket IDs are recorded.

For section eighteen point one, Hollowbrook University will not accept research work without a written trail.

### 18.2 Choosing a method

A survey could ask developers about their habits; an experiment could compare groups with and without the hook; a case study could examine CampusEats in depth. Lena chooses a small comparison across two terms plus a short survey.

Section eighteen point two develops research methods with a Hollowbrook University note Lena Fischer can demo offline.

Under section eighteen point two, Grace Nwosu expects research claims to carry owners and dates.

Section eighteen point two treats question from practice choosing as testable only when evidence and ticket IDs are recorded.

### 18.3 Ethics

Participants consent; no individual results are reported; data are anonymised. The university ethics process approves the plan.

Section eighteen point three develops research methods with a Hollowbrook University note Lena Fischer can demo offline.

Under section eighteen point three, Grace Nwosu expects research claims to carry owners and dates.

Section eighteen point three treats question from practice choosing as testable only when evidence and ticket IDs are recorded.

For section eighteen point three, Hollowbrook University will not accept research work without a written trail.

### 18.4 Data

Counts of secrets caught by the server-side scanner per term, before and after the hook, and survey answers about whether the hook was ever bypassed.

Section eighteen point four develops research methods with a Hollowbrook University note Lena Fischer can demo offline.

Under section eighteen point four, Grace Nwosu expects research claims to carry owners and dates.

Section eighteen point four treats question from practice choosing as testable only when evidence and ticket IDs are recorded.

For section eighteen point four, Hollowbrook University will not accept research work without a written trail.

### 18.5 Analysis

Counts are small, so Lena reports them directly and avoids percentages that look precise.

Section eighteen point five develops research methods with a Hollowbrook University note Lena Fischer can demo offline.

Under section eighteen point five, Grace Nwosu expects research claims to carry owners and dates.

Section eighteen point five treats question from practice choosing as testable only when evidence and ticket IDs are recorded.

For section eighteen point five, Hollowbrook University will not accept research work without a written trail.

Section eighteen point five fails closed if research evidence is missing rather than guessing.

### 18.6 Results

Server-side detections fell from 5 to 1 per term; 3 of 14 developers said they had bypassed the hook at least once, usually when it flagged a harmless string.

Section eighteen point six develops research methods with a Hollowbrook University note Lena Fischer can demo offline.

Under section eighteen point six, Grace Nwosu expects research claims to carry owners and dates.

Section eighteen point six treats question from practice choosing as testable only when evidence and ticket IDs are recorded.

For section eighteen point six, Hollowbrook University will not accept research work without a written trail.

### 18.7 Interpretation

The hook helps, but false positives cause bypasses, so the precision work from chapter 12 matters.

Section eighteen point seven develops research methods with a Hollowbrook University note Lena Fischer can demo offline.

Under section eighteen point seven, Grace Nwosu expects research claims to carry owners and dates.

Section eighteen point seven treats question from practice choosing as testable only when evidence and ticket IDs are recorded.

For section eighteen point seven, Hollowbrook University will not accept research work without a written trail.

### Literature first

Before collecting data, Lena reads what is known about developer behaviour and security tools. Johnson et al. (2013) found that developers avoid tools that produce many false positives and unclear messages. This prediction, that a noisy hook would be bypassed, turned out to be exactly what her survey found, and it guided the fix. Reading first saves effort and gives a study something to compare against.

### Worked example

Lena presents the results at a society meeting. Members suggest an allowlist file for known harmless strings, with review. Bypasses are reported as zero the next term.

> **Synthetic case.** Study data are synthetic.

### Errors and limits

Two terms and 14 developers cannot support general claims; describe this as a local evaluation.

### Exercises

- **EX052 — Research question.** State Lena's research question. *Rubric:* 3 = do pre-commit hooks reduce secrets pushed; 2 = partial; 1 = none; 0 = none.
- **EX053 — Results.** Give the main results. *Rubric:* 3 = 5 to 1 detections; 3 of 14 bypassed; 2 = partial; 1 = none; 0 = none.
- **EX054 — Bypass fix.** What reduced bypasses? *Rubric:* 3 = reviewed allowlist for harmless strings; 2 = partial; 1 = none; 0 = none.

### Synthesis

Small, ethical studies can test practical changes and reveal side effects.

### Continue studying — chapter 18 of 40

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Application and software supply chain security: scope and theory

### Learning outcomes

You will (1) define application security and software supply chain security; (2) explain why integrity of the whole chain matters; (3) describe frameworks that structure the field; (4) relate theory to CampusEats.

### 19.1 Definitions

Application security protects software from flaws in its design and code. Software supply chain security protects everything that goes into the software and how it reaches users: source code, dependencies, build systems, artifacts and distribution.

Section nineteen point one develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section nineteen point one, Grace Nwosu expects application claims to carry owners and dates.

Section nineteen point one treats definitions why the chain as testable only when evidence and ticket IDs are recorded.

### 19.2 Why the chain matters

CampusEats' code is a small fraction of what runs: most comes from open-source packages. Zimmermann et al. (2019) showed that in the npm ecosystem a few packages and maintainers can affect huge numbers of others, so a single compromise spreads widely.

Section nineteen point two develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section nineteen point two, Grace Nwosu expects application claims to carry owners and dates.

Section nineteen point two treats definitions why the chain as testable only when evidence and ticket IDs are recorded.

### 19.3 Trust theory

Thompson's "Reflections on Trusting Trust" (1984) argued that you cannot fully trust code you did not create yourself, including compilers. Practical security therefore builds evidence, such as hashes, signatures and provenance, rather than assuming trust.

Section nineteen point three develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section nineteen point three, Grace Nwosu expects application claims to carry owners and dates.

Section nineteen point three treats definitions why the chain as testable only when evidence and ticket IDs are recorded.

### 19.4 Frameworks

NIST SP 800-218 (SSDF) structures secure development practices; SLSA v1.0 defines build provenance levels; OWASP SAMM v2 measures programme maturity; OWASP ASVS defines application requirements.

Section nineteen point four develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section nineteen point four, Grace Nwosu expects application claims to carry owners and dates.

Section nineteen point four treats definitions why the chain as testable only when evidence and ticket IDs are recorded.

For section nineteen point four, Hollowbrook University will not accept application work without a written trail.

### 19.5 Taxonomy

Ladisa et al. (2023) organised attacks on open-source supply chains by stage and linked them to safeguards, giving a map of where controls belong.

Section nineteen point five develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section nineteen point five, Grace Nwosu expects application claims to carry owners and dates.

Section nineteen point five treats definitions why the chain as testable only when evidence and ticket IDs are recorded.

For section nineteen point five, Hollowbrook University will not accept application work without a written trail.

### 19.6 CampusEats in theory

The leaked token was a source-stage problem; the hash mismatch was a distribution-stage check working as designed.

Section nineteen point six develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section nineteen point six, Grace Nwosu expects application claims to carry owners and dates.

Section nineteen point six treats definitions why the chain as testable only when evidence and ticket IDs are recorded.

For section nineteen point six, Hollowbrook University will not accept application work without a written trail.

### 19.7 Limits of theory

Frameworks describe what good looks like but not how much is enough for a small student project; judgement is needed.

Section nineteen point seven develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section nineteen point seven, Grace Nwosu expects application claims to carry owners and dates.

Section nineteen point seven treats definitions why the chain as testable only when evidence and ticket IDs are recorded.

For section nineteen point seven, Hollowbrook University will not accept application work without a written trail.

### Worked example

Lena maps CampusEats' controls onto the SSDF's four groups. Prepare: the society's code of conduct and training. Protect: repository access rules and secret scanning. Produce: reviews, tests, dependency checks. Respond: advisory monitoring and the incident notes. The weakest group is Prepare: there is no onboarding training on secure coding.

> **Synthetic case.** Mappings are synthetic.

### Errors and limits

A framework mapping shows practices exist, not that they are effective.

### Exercises

- **EX055 — Two definitions.** Distinguish application and supply chain security. *Rubric:* 3 = design/code flaws vs everything into software and delivery; 2 = partial; 1 = none; 0 = none.
- **EX056 — Trusting trust.** What did Thompson (1984) argue? *Rubric:* 3 = cannot fully trust code you did not create, incl. compilers; 2 = partial; 1 = none; 0 = none.
- **EX057 — Weakest group.** Which SSDF group was weakest and why? *Rubric:* 3 = Prepare; no onboarding training; 2 = partial; 1 = none; 0 = none.

### Synthesis

Supply chain security extends application security to everything that builds and delivers the software.

### Continue studying — chapter 19 of 40

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Application and software supply chain security: foundational cases

### Learning outcomes

You will (1) learn from published supply-chain cases at a conceptual level; (2) classify cases by stage; (3) extract defensive lessons; (4) apply lessons to a small project.

### 20.1 Why cases

Real cases show how failures happen in practice. This chapter uses published research summaries, describing what went wrong and what controls help, without technical details of attacks.

Section twenty point one develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty point one, Grace Nwosu expects application claims to carry owners and dates.

Section twenty point one treats why cases malicious packages as testable only when evidence and ticket IDs are recorded.

For section twenty point one, Hollowbrook University will not accept application work without a written trail.

### 20.2 Malicious packages

Ohm et al. (2020) collected hundreds of malicious packages from public registries. Common patterns included lookalike names, packages that ran code during installation, and takeovers of existing packages. Lesson: check new dependency names, limit install-time network access and watch for unexpected maintainer changes.

Section twenty point two develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty point two, Grace Nwosu expects application claims to carry owners and dates.

Section twenty point two treats why cases malicious packages as testable only when evidence and ticket IDs are recorded.

### 20.3 Vulnerable dependencies

Decan et al. (2018) studied how vulnerabilities in npm packages propagate through dependency networks and how long fixes take to reach dependents. Lesson: monitor transitive dependencies and update promptly.

Section twenty point three develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty point three, Grace Nwosu expects application claims to carry owners and dates.

Section twenty point three treats why cases malicious packages as testable only when evidence and ticket IDs are recorded.

### 20.4 Build and distribution

Ladisa et al. (2023) describe attacks on build systems and distribution channels. Lesson: isolated builds, signed artifacts, hash checks and provenance.

Section twenty point four develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty point four, Grace Nwosu expects application claims to carry owners and dates.

Section twenty point four treats why cases malicious packages as testable only when evidence and ticket IDs are recorded.

For section twenty point four, Hollowbrook University will not accept application work without a written trail.

### 20.5 Trust in open source

Wermke et al. (2022) interviewed open-source maintainers about trust and security, finding varied practices and reliance on personal trust. Lesson: consumers should not assume upstream security processes.

Section twenty point five develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty point five, Grace Nwosu expects application claims to carry owners and dates.

Section twenty point five treats why cases malicious packages as testable only when evidence and ticket IDs are recorded.

For section twenty point five, Hollowbrook University will not accept application work without a written trail.

### 20.6 CampusEats lessons

The society adopts a lookalike-name check, build network restrictions and weekly dependency updates.

Section twenty point six develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty point six, Grace Nwosu expects application claims to carry owners and dates.

Section twenty point six treats why cases malicious packages as testable only when evidence and ticket IDs are recorded.

For section twenty point six, Hollowbrook University will not accept application work without a written trail.

### Updating the cards

The case cards are reviewed each year as new research appears, so the lessons stay current. Lena adds a column for the standard that addresses each stage, such as SLSA for builds and the SSDF for response, linking cases to the frameworks from chapter 19.

### Worked example

Lena prepares a one-page "case cards" handout: for each stage, one sentence on what went wrong in published cases and one on the matching CampusEats control. New members find it the clearest introduction to the topic.

> **Synthetic case.** CampusEats applications are synthetic; the cited studies are real.

### Errors and limits

Published cases are those that were discovered; undiscovered ones may differ.

### Exercises

- **EX058 — Ohm patterns.** List three malicious package patterns from Ohm et al. *Rubric:* 3 = lookalike names, install-time code, takeovers; 2 = two; 1 = one; 0 = none.
- **EX059 — Decan lesson.** What lesson comes from Decan et al.? *Rubric:* 3 = monitor transitive deps; update promptly; 2 = partial; 1 = none; 0 = none.
- **EX060 — Wermke lesson.** What lesson comes from Wermke et al.? *Rubric:* 3 = don't assume upstream security processes; 2 = partial; 1 = none; 0 = none.

### Synthesis

Published cases teach defensive lessons by stage without needing attack details.

### Continue studying — chapter 20 of 40

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Application and software supply chain security: system models

### Learning outcomes

You will (1) draw a data flow diagram for an application and its pipeline; (2) mark trust boundaries; (3) apply STRIDE to elements; (4) prioritise threats for a small project.

### 21.1 Data flow diagrams

Shostack (2014) recommends simple data flow diagrams for threat modelling: external entities (students, payment provider, package registry), processes (web app, build service), data stores (database, artifact store) and data flows between them. Lena draws CampusEats on one page.

Section twenty-one point one develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-one point one, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-one point one treats data flow diagrams trust as testable only when evidence and ticket IDs are recorded.

### 21.2 Trust boundaries

She draws dashed lines where trust changes: between students' browsers and the web app, between the web app and the payment provider, between the build service and the public registry, and between the build service and production.

Section twenty-one point two develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-one point two, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-one point two treats data flow diagrams trust as testable only when evidence and ticket IDs are recorded.

### 21.3 STRIDE

For each element, the team asks Shostack's STRIDE questions: could someone Spoof an identity, Tamper with data, Repudiate an action, cause Information disclosure, Deny service, or Elevate privilege?

Section twenty-one point three develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-one point three, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-one point three treats data flow diagrams trust as testable only when evidence and ticket IDs are recorded.

### 21.4 Example threats

Spoofing: a forged payment callback (fixed in chapter 17). Tampering: a package altered in transit (lockfile hashes, chapter 22). Information disclosure: secrets in the repository (scanning). Elevation: a volunteer reaching staff functions (role checks). Denial: lunchtime traffic spikes (rate limits and caching).

Section twenty-one point four develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-one point four, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-one point four treats data flow diagrams trust as testable only when evidence and ticket IDs are recorded.

### 21.5 Prioritising

Each threat is rated low, medium or high for likelihood and impact. High-high items must have a control and a test.

Section twenty-one point five develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-one point five, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-one point five treats data flow diagrams trust as testable only when evidence and ticket IDs are recorded.

For section twenty-one point five, Hollowbrook University will not accept application work without a written trail.

### 21.6 Four questions

Shostack's four questions frame the session: what are we working on, what can go wrong, what are we going to do about it, did we do a good job?

Section twenty-one point six develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-one point six, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-one point six treats data flow diagrams trust as testable only when evidence and ticket IDs are recorded.

### 21.7 Keeping it small

A one-hour session each term keeps the model current without burdening volunteers.

Section twenty-one point seven develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-one point seven, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-one point seven treats data flow diagrams trust as testable only when evidence and ticket IDs are recorded.

For section twenty-one point seven, Hollowbrook University will not accept application work without a written trail.

### Worked example

The session finds a missed flow: the build service sends build logs to a third-party chat channel. Logs could contain environment values. The team configures masking of secret values in logs and restricts the chat channel to members.

> **Synthetic case.** The model and threats are synthetic.

### Errors and limits

Threat models depend on the people in the room; invite someone from outside the team.

### Exercises

- **EX061 — DFD elements.** List the four kinds of DFD element with a CampusEats example each. *Rubric:* 3 = entity: students; process: web app; store: database; flow: callback; 2 = three; 1 = one; 0 = none.
- **EX062 — STRIDE example.** Give one STRIDE threat and its control. *Rubric:* 3 = e.g. spoofed callback: HMAC verification; 2 = partial; 1 = none; 0 = none.
- **EX063 — Missed flow.** What missed flow did the session find? *Rubric:* 3 = build logs to chat; masking and restriction; 2 = partial; 1 = none; 0 = none.

### Synthesis

A one-page model and STRIDE questions find threats a busy team would miss.

### Continue studying — chapter 21 of 40

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Application and software supply chain security: data and dependencies

### Learning outcomes

You will (1) explain lockfiles and integrity hashes; (2) verify downloaded packages against a lockfile; (3) investigate mismatches safely; (4) generate and use an SBOM.

### 22.1 Lockfiles with hashes

CampusEats' lockfile records each package's exact version and a cryptographic hash of its contents. On install, the package manager compares downloaded bytes with the hash and stops if they differ.

Section twenty-two point one develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-two point one, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-two point one treats lockfiles with hashes lab as testable only when evidence and ticket IDs are recorded.

### Lab — Lab — checking hashes

```python
"""Compare downloaded package hashes with lockfile entries (synthetic)."""
import hashlib
lock = {"menu-ui-2.3.1": hashlib.sha256(b"menu-ui 2.3.1").hexdigest(),
        "pay-client-1.8.0": hashlib.sha256(b"pay-client 1.8.0").hexdigest(),
        "date-tools-0.4.2": hashlib.sha256(b"date-tools 0.4.2").hexdigest()}
downloaded = {"menu-ui-2.3.1": b"menu-ui 2.3.1", "pay-client-1.8.0": b"pay-client 1.8.0 (rebuilt)",
              "date-tools-0.4.2": b"date-tools 0.4.2"}
for name, blob in downloaded.items():
    print(f"{name:17} {'ok' if hashlib.sha256(blob).hexdigest() == lock[name] else 'HASH MISMATCH - stop install'}")
```

Run with `python3 lab_lockfile.py`. Verified output:

```text
menu-ui-2.3.1     ok
pay-client-1.8.0  HASH MISMATCH - stop install
date-tools-0.4.2  ok
```

### 22.2 Lab result

menu-ui and date-tools match their lockfile hashes. pay-client 1.8.0 does not: the downloaded content differs from what was recorded, and installation stops. This is the check that halted the build in Lena's first week.

Section twenty-two point two develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-two point two, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-two point two treats lockfiles with hashes lab as testable only when evidence and ticket IDs are recorded.

### 22.3 Investigating

A mismatch can mean a corrupted download, a registry problem, a republished package or tampering. The society does not override the check. Lena compares the package metadata and finds the maintainer had rebuilt and re-uploaded 1.8.0 with a small change, which good registries usually prevent. The society reports it to the maintainer and pins the previous known-good version until 1.8.1 is published.

Section twenty-two point three develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-two point three, Grace Nwosu expects application claims to carry owners and dates.

### 22.4 SBOMs

A software bill of materials lists every component and version in a build. NTIA (2021) defined minimum elements, including supplier, component name, version, unique identifiers, dependency relationships, the SBOM's author and a timestamp. CampusEats generates an SBOM for every build.

Section twenty-two point four develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-two point four, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-two point four treats lockfiles with hashes lab as testable only when evidence and ticket IDs are recorded.

### 22.5 Using SBOMs

When an advisory appears, searching SBOMs shows which releases contain the affected component.

Section twenty-two point five develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-two point five, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-two point five treats lockfiles with hashes lab as testable only when evidence and ticket IDs are recorded.

For section twenty-two point five, Hollowbrook University will not accept application work without a written trail.

### 22.6 Dependency owners

Each direct dependency has a named owner in the society.

Section twenty-two point six develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-two point six, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-two point six treats lockfiles with hashes lab as testable only when evidence and ticket IDs are recorded.

For section twenty-two point six, Hollowbrook University will not accept application work without a written trail.

Section twenty-two point six fails closed if application evidence is missing rather than guessing.

### Pinning carefully

Pinning an old version is a temporary measure with an expiry date, so CampusEats does not stay on it forever.

### Worked example

When the maintainer releases pay-client 1.8.1 with notes explaining the earlier re-upload, the society updates, regenerates the lockfile and SBOM, and closes the incident with a note linking the evidence.

> **Synthetic case.** Packages and hashes are synthetic.

### Errors and limits

Hashes prove the bytes match the lockfile, not that the original package was safe.

### Exercises

- **EX064 — Lab mismatch.** Which package failed and what happened? *Rubric:* 3 = pay-client 1.8.0; stop install; 2 = partial; 1 = none; 0 = none.
- **EX065 — Mismatch cause.** What caused the real mismatch? *Rubric:* 3 = maintainer re-uploaded 1.8.0; 2 = partial; 1 = none; 0 = none.
- **EX066 — SBOM elements.** Name four NTIA minimum elements. *Rubric:* 3 = supplier, name, version, identifiers, relationships, author, timestamp (four); 2 = two; 1 = one; 0 = none.

### Synthesis

Hash-checked lockfiles and SBOMs show exactly what you build and let you trace problems.

### Continue studying — chapter 22 of 40

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Application and software supply chain security: methods I

### Learning outcomes

You will (1) scan code changes for secrets; (2) combine patterns with character-variety checks; (3) respond to a found secret; (4) prevent recurrence.

### 23.1 Why scan

The token leak showed secrets can slip into repositories. Scanning checks every change before and after it is pushed.

Section twenty-three point one develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-three point one, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-three point one treats why scan patterns and as testable only when evidence and ticket IDs are recorded.

For section twenty-three point one, Hollowbrook University will not accept application work without a written trail.

### 23.2 Patterns and variety

Many tokens have known prefixes or lengths, so scanners use patterns. Random-looking strings also have high character variety (entropy). Combining both reduces false alarms on long but repetitive strings.

Section twenty-three point two develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-three point two, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-three point two treats why scan patterns and as testable only when evidence and ticket IDs are recorded.

### Lab — Lab — scanning a diff

```python
"""Scan a synthetic diff for token-like strings using a pattern plus a character-variety check."""
import re, math
from collections import Counter
diff = ["+ API_URL = 'https://api.campuseats.example'", "+ TOKEN = 'cetk_9fQ2xLr7Vb3mZ8pK1sW4yT6n'",
        "+ COLOR = 'aaaaaaaaaaaaaaaaaaaaaaaa'", "+ # see docs at example.org"]
def entropy(s):
    c = Counter(s); return 0.0 + abs(sum(n / len(s) * math.log2(n / len(s)) for n in c.values()))
for line in diff:
    for m in re.findall(r"'([A-Za-z0-9_]{20,})'", line):
        print(f"{m[:8]}... entropy {entropy(m):.2f} -> {'LIKELY SECRET' if entropy(m) > 3.5 else 'low variety, ignore'}")
```

Run with `python3 lab_secrets.py`. Verified output:

```text
cetk_9fQ... entropy 4.86 -> LIKELY SECRET
aaaaaaaa... entropy 0.00 -> low variety, ignore
```

### 23.3 Lab result

Two long strings match the pattern. The token-like string has entropy 4.86 bits per character and is flagged as a likely secret. The string of repeated "a" characters has entropy 0.00 and is ignored. The URL and comment lines do not match the pattern.

Section twenty-three point three develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-three point three, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-three point three treats why scan patterns and as testable only when evidence and ticket IDs are recorded.

### 23.4 Responding

When a secret is found: revoke or rotate it first, then remove it from the code, then check logs for any use. Rewriting history does not undo exposure, because copies may exist.

Section twenty-three point four develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-three point four, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-three point four treats why scan patterns and as testable only when evidence and ticket IDs are recorded.

### 23.5 Preventing recurrence

Pre-commit hooks, server-side scanning, secret stores, and onboarding training.

Section twenty-three point five develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-three point five, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-three point five treats why scan patterns and as testable only when evidence and ticket IDs are recorded.

For section twenty-three point five, Hollowbrook University will not accept application work without a written trail.

Section twenty-three point five fails closed if application evidence is missing rather than guessing.

### 23.6 Measuring

Lena tracks scanner precision and recall as in chapter 12.

Section twenty-three point six develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-three point six, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-three point six treats why scan patterns and as testable only when evidence and ticket IDs are recorded.

For section twenty-three point six, Hollowbrook University will not accept application work without a written trail.

Section twenty-three point six fails closed if application evidence is missing rather than guessing.

### Where to scan

Scanning covers the code repository, CI logs and configuration files. Lena also scans the society's shared documents folder once, finding an old file with a test database password; it is deleted and the password changed. Secrets turn up in places beyond code.

### Worked example

A month later the server-side scanner flags a new commit containing a high-entropy string in a test file. The developer confirms it is a random test fixture, not a real key; it is added to the reviewed allowlist. No real secret has reached the public repository since the controls were added.

> **Synthetic case.** Strings and events are synthetic.

### Errors and limits

Entropy thresholds miss low-variety secrets such as simple passwords; patterns and reviews are also needed.

### Exercises

- **EX067 — Lab entropy.** What entropies did the lab compute and with what result? *Rubric:* 3 = 4.86 likely secret; 0.00 ignore; 2 = partial; 1 = none; 0 = none.
- **EX068 — Response order.** What is the first step when a secret is found? *Rubric:* 3 = revoke/rotate; 2 = partial; 1 = none; 0 = none.
- **EX069 — History rewrite.** Why does rewriting history not undo exposure? *Rubric:* 3 = copies may exist; 2 = partial; 1 = none; 0 = none.

### Synthesis

Scan with patterns and variety, revoke first, and prevent recurrence.

### Continue studying — chapter 23 of 40

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Application and software supply chain security: controls

### Learning outcomes

You will (1) select preventive, detective and corrective controls for the supply chain; (2) implement policy checks in CI; (3) manage exceptions; (4) review control effectiveness.

### 24.1 Preventive controls

Branch protection with required review; secrets kept out of code; lockfile hashes; lookalike-name checks for new dependencies; isolated builds with limited network.

Section twenty-four point one develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-four point one, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-four point one treats preventive controls detective controls as testable only when evidence and ticket IDs are recorded.

For section twenty-four point one, Hollowbrook University will not accept application work without a written trail.

### 24.2 Detective controls

Secret scanning after push; nightly advisory checks against SBOMs; alerts on failed integrity checks; logs of deployments.

Section twenty-four point two develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-four point two, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-four point two treats preventive controls detective controls as testable only when evidence and ticket IDs are recorded.

For section twenty-four point two, Hollowbrook University will not accept application work without a written trail.

### 24.3 Corrective controls

Secret rotation procedure; dependency update process; rollback to the previous release.

Section twenty-four point three develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-four point three, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-four point three treats preventive controls detective controls as testable only when evidence and ticket IDs are recorded.

For section twenty-four point three, Hollowbrook University will not accept application work without a written trail.

Section twenty-four point three fails closed if application evidence is missing rather than guessing.

### 24.4 Policy in CI

A CI step fails the build when: a high-severity advisory affects a dependency without an approved exception, a new dependency has no owner, or the lockfile is out of date. NIST SP 800-218 practices PW.4 (reuse well-secured software) and RV.1 (identify vulnerabilities continuously) support these checks.

Section twenty-four point four develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-four point four, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-four point four treats preventive controls detective controls as testable only when evidence and ticket IDs are recorded.

### 24.5 Exceptions

An exception records the reason, owner and expiry date; expired exceptions fail the build again.

Section twenty-four point five develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-four point five, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-four point five treats preventive controls detective controls as testable only when evidence and ticket IDs are recorded.

For section twenty-four point five, Hollowbrook University will not accept application work without a written trail.

### 24.6 Effectiveness

Each control has a measure: number of times it caught something, false alarms and time cost.

Section twenty-four point six develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-four point six, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-four point six treats preventive controls detective controls as testable only when evidence and ticket IDs are recorded.

For section twenty-four point six, Hollowbrook University will not accept application work without a written trail.

### 24.7 Proportion

CampusEats is a volunteer project; controls must be light enough that members keep using them.

Section twenty-four point seven develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-four point seven, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-four point seven treats preventive controls detective controls as testable only when evidence and ticket IDs are recorded.

For section twenty-four point seven, Hollowbrook University will not accept application work without a written trail.

### Review cycle

Controls are reviewed each term: are they still catching problems, are false alarms rising, and do members understand them? A control that has caught nothing for a year is checked with a synthetic test to make sure it still works, rather than removed.

### Ownership

Each control has a named owner in the society.

### Worked example

In one term, the CI policy blocks four builds: two for a new high advisory (fixed within a day), one for a dependency without an owner (owner added) and one for an outdated lockfile. Members report the checks are clear and quick.

> **Synthetic case.** Controls and counts are synthetic.

### Errors and limits

Controls in CI protect what goes through CI; manual changes outside it are not covered, so block them.

### Exercises

- **EX070 — Control types.** Give one preventive, one detective and one corrective control. *Rubric:* 3 = e.g. lockfile hash; advisory check; rollback; 2 = two; 1 = one; 0 = none.
- **EX071 — CI policy.** List the three CI policy failures. *Rubric:* 3 = high advisory without exception; no owner; outdated lockfile; 2 = two; 1 = one; 0 = none.
- **EX072 — Term results.** What did the policy block in one term? *Rubric:* 3 = 2 advisory, 1 no owner, 1 outdated lockfile; 2 = partial; 1 = none; 0 = none.

### Synthesis

Combine preventive, detective and corrective controls, enforced in CI and kept proportionate.

### Continue studying — chapter 24 of 40

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Laboratory I

### Learning outcomes

You will (1) check an application's HTTP security headers; (2) interpret missing headers; (3) add headers safely; (4) test them automatically.

### 25.1 Security headers

Browsers apply extra protections when servers send certain headers: Content-Security-Policy limits which scripts and resources can load; Strict-Transport-Security makes the browser use HTTPS only; X-Content-Type-Options stops the browser guessing content types; Referrer-Policy limits information in links to other sites. OWASP's testing guide (WSTG v4.2) includes checks for such configuration.

Section twenty-five point one develops laboratory with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-five point one, Grace Nwosu expects laboratory claims to carry owners and dates.

Section twenty-five point one treats security headers lab result as testable only when evidence and ticket IDs are recorded.

### Lab — Lab — header check

```python
"""Check a synthetic HTTP response for recommended security headers."""
resp = {"Content-Type": "text/html; charset=utf-8", "Strict-Transport-Security": "max-age=31536000",
        "X-Content-Type-Options": "nosniff", "Server": "campuseats/1.0"}
wanted = ["Content-Security-Policy", "Strict-Transport-Security", "X-Content-Type-Options", "Referrer-Policy"]
for h in wanted:
    print(f"{h:27} {'present' if h in resp else 'MISSING'}")
```

Run with `python3 lab_headers.py`. Verified output:

```text
Content-Security-Policy     MISSING
Strict-Transport-Security   present
X-Content-Type-Options      present
Referrer-Policy             MISSING
```

### 25.2 Lab result

Strict-Transport-Security and X-Content-Type-Options are present. Content-Security-Policy and Referrer-Policy are missing. The response also reveals a "Server" header naming the software version, which gives unnecessary information.

Section twenty-five point two develops laboratory with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-five point two, Grace Nwosu expects laboratory claims to carry owners and dates.

Section twenty-five point two treats security headers lab result as testable only when evidence and ticket IDs are recorded.

For section twenty-five point two, Hollowbrook University will not accept laboratory work without a written trail.

### 25.3 Adding headers

Referrer-Policy is simple to add. Content-Security-Policy needs care: a strict policy can break pages that load scripts from other places. Lena starts with a report-only policy that logs violations without blocking, reviews the reports for two weeks, then enforces.

Section twenty-five point three develops laboratory with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-five point three, Grace Nwosu expects laboratory claims to carry owners and dates.

Section twenty-five point three treats security headers lab result as testable only when evidence and ticket IDs are recorded.

### 25.4 Removing information

The Server header is reduced to a generic value.

Section twenty-five point four develops laboratory with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-five point four, Grace Nwosu expects laboratory claims to carry owners and dates.

Section twenty-five point four treats security headers lab result as testable only when evidence and ticket IDs are recorded.

For section twenty-five point four, Hollowbrook University will not accept laboratory work without a written trail.

Section twenty-five point four fails closed if laboratory evidence is missing rather than guessing.

### 25.5 Automated tests

A CI test requests key pages in the test environment and checks headers, so a later change cannot silently remove them.

Section twenty-five point five develops laboratory with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-five point five, Grace Nwosu expects laboratory claims to carry owners and dates.

Section twenty-five point five treats security headers lab result as testable only when evidence and ticket IDs are recorded.

For section twenty-five point five, Hollowbrook University will not accept laboratory work without a written trail.

### 25.6 Lab practice

All checks run against the test environment, never against systems the society does not own.

Section twenty-five point six develops laboratory with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-five point six, Grace Nwosu expects laboratory claims to carry owners and dates.

Section twenty-five point six treats security headers lab result as testable only when evidence and ticket IDs are recorded.

For section twenty-five point six, Hollowbrook University will not accept laboratory work without a written trail.

Section twenty-five point six fails closed if laboratory evidence is missing rather than guessing.

### Recording results

Lena records each header check result with the date and environment in the lab notebook, so later changes can be compared against a known starting point. The notebook also lists which pages were checked and why.

### Sharing

Results are shared with members at the next meeting.

### Worked example

During the report-only period, the reports show one blocked resource: a font loaded from an external site. The font is copied to CampusEats' own domain, and the enforced policy goes live without breaking any page.

> **Synthetic case.** Headers and reports are synthetic.

### Errors and limits

Headers help browsers protect users but do not fix flaws in the application itself.

### Exercises

- **EX073 — Lab missing.** Which headers were missing? *Rubric:* 3 = Content-Security-Policy and Referrer-Policy; 2 = one; 1 = none; 0 = none.
- **EX074 — CSP rollout.** How was CSP introduced safely? *Rubric:* 3 = report-only two weeks; then enforce; 2 = partial; 1 = none; 0 = none.
- **EX075 — Server header.** Why reduce the Server header? *Rubric:* 3 = reveals software version unnecessarily; 2 = partial; 1 = none; 0 = none.

### Synthesis

Check headers, roll out policies carefully and keep them tested.

### Continue studying — chapter 25 of 40

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Application and software supply chain security: methods II

### Learning outcomes

You will (1) sign build artifacts and verify signatures before deployment; (2) record build provenance; (3) explain SLSA build levels; (4) integrate verification into deployment.

### 26.1 Why sign

A hash shows the bytes match a reference; a signature shows who produced them. CampusEats' build service signs each release bundle, and the deployment step verifies the signature before installing.

Section twenty-six point one develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-six point one, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-six point one treats why sign keyless signing as testable only when evidence and ticket IDs are recorded.

### 26.2 Keyless signing

Long-lived signing keys can leak, like the token did. Sigstore (Newman et al., 2022) issues short-lived certificates tied to the build service's identity and records signatures in a public transparency log. CampusEats adopts this approach for its release bundles.

Section twenty-six point two develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-six point two, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-six point two treats why sign keyless signing as testable only when evidence and ticket IDs are recorded.

### 26.3 Provenance

Provenance is a record of how an artifact was built: which source commit, which build service, which steps. SLSA v1.0 defines build levels: Level 1 requires provenance to exist; Level 2 requires a hosted build platform that signs provenance; Level 3 requires a hardened platform that resists tampering by build users.

Section twenty-six point three develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-six point three, Grace Nwosu expects application claims to carry owners and dates.

### 26.4 CampusEats' level

Builds run on a hosted CI service that generates signed provenance, roughly matching Build Level 2. Level 3 depends on the CI provider's guarantees, which the society reviews.

Section twenty-six point four develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-six point four, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-six point four treats why sign keyless signing as testable only when evidence and ticket IDs are recorded.

For section twenty-six point four, Hollowbrook University will not accept application work without a written trail.

### 26.5 Verifying at deployment

The deployment step checks: the signature is valid and from the expected build identity; the provenance shows the expected repository and a reviewed commit. If any check fails, deployment stops.

Section twenty-six point five develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-six point five, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-six point five treats why sign keyless signing as testable only when evidence and ticket IDs are recorded.

### 26.6 in-toto

in-toto (Torres-Arias et al., 2019) generalises this idea, recording and verifying every step in the chain.

Section twenty-six point six develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-six point six, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-six point six treats why sign keyless signing as testable only when evidence and ticket IDs are recorded.

For section twenty-six point six, Hollowbrook University will not accept application work without a written trail.

### Transparency logs

Because signatures are recorded in a public log, the society can check that no unexpected signatures were made with its build identity. A monthly script lists log entries for CampusEats and compares them with known releases.

### Worked example

Lena tests the deployment check in the test environment with a synthetic bundle signed by a personal identity rather than the build service. Deployment is refused with a clear message, as required.

> **Synthetic case.** The signing setup is synthetic.

### Errors and limits

Signatures prove origin, not quality; a signed bundle can still contain a flaw.

### Exercises

- **EX076 — Hash vs signature.** What does a signature add to a hash? *Rubric:* 3 = who produced it; 2 = partial; 1 = none; 0 = none.
- **EX077 — SLSA levels.** Summarise SLSA Build Levels 1–3. *Rubric:* 3 = L1 provenance exists; L2 hosted signed; L3 hardened tamper-resistant; 2 = two; 1 = one; 0 = none.
- **EX078 — Test result.** What did the deployment test show? *Rubric:* 3 = personal-identity bundle refused; 2 = partial; 1 = none; 0 = none.

### Synthesis

Sign releases, record provenance and verify both before deploying.

### Continue studying — chapter 26 of 40

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Application and software supply chain security: verification

### Learning outcomes

You will (1) verify an application against ASVS requirements; (2) plan authorised testing with the WSTG; (3) record evidence per requirement; (4) prioritise fixes.

### 27.1 ASVS

The OWASP Application Security Verification Standard lists testable requirements at three levels. CampusEats targets ASVS 4.0.3 Level 1 for most areas and Level 2 for authentication, session management and access control, because it handles payments and personal data. ASVS 5.0.0 reorganised chapters; Lena notes both identifiers for each requirement she checks.

Section twenty-seven point one develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-seven point one, Grace Nwosu expects application claims to carry owners and dates.

### 27.2 Planning tests

Using the WSTG v4.2, Lena selects tests for configuration, authentication, authorisation, session management, input validation and error handling. Testing happens only in the test environment, under the society's written permission.

Section twenty-seven point two develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-seven point two, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-seven point two treats asvs planning tests evidence as testable only when evidence and ticket IDs are recorded.

### 27.3 Evidence

Each requirement gets pass, fail or not applicable, with evidence: a test log, a configuration screenshot or code reference.

Section twenty-seven point three develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-seven point three, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-seven point three treats asvs planning tests evidence as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point three, Hollowbrook University will not accept application work without a written trail.

### 27.4 Results

46 requirements checked: 41 pass, 4 fail, 1 not applicable. Failures: password reset links valid too long for staff accounts, missing rate limit on login for staff, verbose error page in one admin screen, and missing audit log for menu price changes.

Section twenty-seven point four develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-seven point four, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-seven point four treats asvs planning tests evidence as testable only when evidence and ticket IDs are recorded.

### 27.5 Prioritising

Fixes are ordered by risk: rate limit and reset link first (account takeover risk), then audit log and error page.

Section twenty-seven point five develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-seven point five, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-seven point five treats asvs planning tests evidence as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point five, Hollowbrook University will not accept application work without a written trail.

### 27.6 Retesting

Each fix is retested by someone else.

Section twenty-seven point six develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-seven point six, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-seven point six treats asvs planning tests evidence as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point six, Hollowbrook University will not accept application work without a written trail.

Section twenty-seven point six fails closed if application evidence is missing rather than guessing.

### Automating checks

Many ASVS requirements can be checked automatically after the first manual review: cookie attributes, headers, rate limits and error pages. Lena turns eleven of the 46 checks into CI tests, so they run on every change and regressions are caught early. The remaining checks, which need judgement, stay in the yearly manual review.

### Reporting

The verification report is shared with Grace and kept with the release records for a year.

### Worked example

All four failures are fixed within three weeks and retested. Grace asks the society to repeat the verification yearly and after major changes.

> **Synthetic case.** Results are synthetic.

### Errors and limits

Passing ASVS requirements shows conformance at that time, not absence of all flaws.

### Exercises

- **EX079 — Level choice.** Why use Level 2 for some areas? *Rubric:* 3 = payments and personal data; 2 = partial; 1 = none; 0 = none.
- **EX080 — Results.** Summarise the verification results. *Rubric:* 3 = 46 checked: 41 pass, 4 fail, 1 N/A; 2 = partial; 1 = none; 0 = none.
- **EX081 — Fix order.** Which fixes came first and why? *Rubric:* 3 = rate limit and reset link; account takeover risk; 2 = partial; 1 = none; 0 = none.

### Synthesis

Verify against a standard, with evidence, and fix by risk.

### Continue studying — chapter 27 of 40

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Application and software supply chain security: failure analysis

### Learning outcomes

You will (1) analyse incidents and near misses without blame; (2) find root causes and contributing factors; (3) design actions that prevent recurrence; (4) share lessons.

### 28.1 Blameless analysis

The goal is to understand how the system allowed a failure, not to blame a person. People make mistakes; systems should catch them.

Section twenty-eight point one develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-eight point one, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-eight point one treats blameless analysis the token as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point one, Hollowbrook University will not accept application work without a written trail.

### 28.2 The token leak

Timeline: test token added to config/test.env; .gitignore excluded the wrong path; commit pushed to public repository; server-side scanner flagged it two hours later; token revoked within fifteen minutes of the alert.

Section twenty-eight point two develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-eight point two, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-eight point two treats blameless analysis the token as testable only when evidence and ticket IDs are recorded.

### 28.3 Root cause and factors

Root cause: secrets were kept in files inside the repository folder. Contributing factors: no pre-commit hook; the .gitignore mistake; unclear guidance about test keys.

Section twenty-eight point three develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-eight point three, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-eight point three treats blameless analysis the token as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point three, Hollowbrook University will not accept application work without a written trail.

### 28.4 Actions

Move all secrets to the secret store; add the pre-commit hook; write guidance; add a CI check that fails if any .env file is committed.

Section twenty-eight point four develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-eight point four, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-eight point four treats blameless analysis the token as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point four, Hollowbrook University will not accept application work without a written trail.

### 28.5 Near misses

The pay-client hash mismatch was a near miss handled well; its analysis records what worked (the check, not overriding it) so it is kept.

Section twenty-eight point five develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-eight point five, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-eight point five treats blameless analysis the token as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point five, Hollowbrook University will not accept application work without a written trail.

### 28.6 Sharing

A short write-up is shared with other student projects at the university.

Section twenty-eight point six develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-eight point six, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-eight point six treats blameless analysis the token as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point six, Hollowbrook University will not accept application work without a written trail.

### Tracking actions

Each action from the analysis has an owner and a date and is tracked in the society's issue tracker until closed. Lena checks progress at each fortnightly meeting. Three months later, all four actions are complete, and a test commit containing a fake .env file is correctly blocked by the CI check, confirming the action works.

### Worked example

Lena uses the "five whys" method: why was the token public? It was committed. Why? .gitignore missed it. Why? The path was wrong. Why? Nobody tested the ignore rule. Why? There was no check for committed .env files. The last answer becomes the CI check.

> **Synthetic case.** The analysis is synthetic.

### Errors and limits

Root-cause methods can oversimplify; most incidents have several causes.

### Exercises

- **EX082 — Blameless goal.** What is the goal of blameless analysis? *Rubric:* 3 = how system allowed failure, not blame; 2 = partial; 1 = none; 0 = none.
- **EX083 — Contributing factors.** List the contributing factors to the leak. *Rubric:* 3 = no hook; .gitignore mistake; unclear guidance; 2 = two; 1 = one; 0 = none.
- **EX084 — Five whys.** What final action came from the five whys? *Rubric:* 3 = CI check for committed .env files; 2 = partial; 1 = none; 0 = none.

### Synthesis

Analyse failures without blame and turn causes into system changes.

### Continue studying — chapter 28 of 40

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Application and software supply chain security: operations

### Learning outcomes

You will (1) operate the application securely; (2) monitor logs and alerts; (3) manage dependency updates routinely; (4) run a simple incident process.

### 29.1 Monitoring

CampusEats logs sign-ins, role changes, failed authorisation, payment callback verification failures and deployments. Alerts go to two on-call members during term.

Section twenty-nine point one develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-nine point one, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-nine point one treats monitoring routine updates advisory as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point one, Hollowbrook University will not accept application work without a written trail.

### 29.2 Routine updates

A bot opens weekly pull requests updating dependencies within allowed ranges; tests run automatically, and members merge them on Mondays. Major version updates are planned separately.

Section twenty-nine point two develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-nine point two, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-nine point two treats monitoring routine updates advisory as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point two, Hollowbrook University will not accept application work without a written trail.

### 29.3 Advisory response

High-severity advisories affecting CampusEats are fixed within 7 days, medium within 30.

Section twenty-nine point three develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-nine point three, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-nine point three treats monitoring routine updates advisory as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point three, Hollowbrook University will not accept application work without a written trail.

Section twenty-nine point three fails closed if application evidence is missing rather than guessing.

### 29.4 Incident process

Detect, assess, contain, fix, recover, review. A short template records each incident.

Section twenty-nine point four develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-nine point four, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-nine point four treats monitoring routine updates advisory as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point four, Hollowbrook University will not accept application work without a written trail.

### 29.5 Holidays

During holidays, ordering is closed and the app shows a notice; updates continue so the app is current when term starts.

Section twenty-nine point five develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-nine point five, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-nine point five treats monitoring routine updates advisory as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point five, Hollowbrook University will not accept application work without a written trail.

### 29.6 Hand-over

Each year graduating members hand over roles and access is reviewed.

Section twenty-nine point six develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section twenty-nine point six, Grace Nwosu expects application claims to carry owners and dates.

Section twenty-nine point six treats monitoring routine updates advisory as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point six, Hollowbrook University will not accept application work without a written trail.

Section twenty-nine point six fails closed if application evidence is missing rather than guessing.

### On-call guide

The on-call guide lists each alert, what it means, first checks and who to call. It is short enough to read on a phone. New on-call members shadow an experienced member for one week before taking alerts alone, and the guide is updated whenever an alert causes confusion. During exam weeks, on-call shifts are shared so nobody carries alerts during their own exams.

### Communication with users

When an incident affects ordering, a banner on the app tells students what is happening and when service is expected back. After incidents involving their data, students receive a short email explaining what happened and what was done, approved by the data protection officer.

### Worked example

One Monday, a weekly update pull request fails tests because a date library changed its time zone handling. The team holds that update, opens an issue with the maintainers, and merges the others. The held update is fixed the next week.

> **Synthetic case.** Operations are synthetic.

### Errors and limits

Volunteer projects have limited cover; be honest with users about response times.

### Exercises

- **EX085 — Logged events.** List three logged events. *Rubric:* 3 = sign-ins, role changes, failed authorisation, callback failures, deployments (three); 2 = two; 1 = one; 0 = none.
- **EX086 — Fix targets.** What are the fix targets? *Rubric:* 3 = high 7 days, medium 30; 2 = one; 1 = none; 0 = none.
- **EX087 — Failed update.** How was the failing update handled? *Rubric:* 3 = held; issue opened; others merged; 2 = partial; 1 = none; 0 = none.

### Synthesis

Routine updates, monitoring and a simple incident process keep a small app safe.

### Continue studying — chapter 29 of 40

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Laboratory II

### Learning outcomes

You will (1) run a complete supply-chain check on a release; (2) combine SBOM, hash, signature and provenance checks; (3) produce a release verification report; (4) practise authorised lab conduct.

### 30.1 The exercise

Lena runs a full check on the CampusEats release candidate in the test environment: generate the SBOM, check advisories, verify lockfile hashes, verify the signature and provenance, run ASVS-related tests.

Section thirty point one develops laboratory ii with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty point one, Grace Nwosu expects laboratory claims to carry owners and dates.

Section thirty point one treats the exercise sbom and as testable only when evidence and ticket IDs are recorded.

For section thirty point one, Hollowbrook University will not accept laboratory work without a written trail.

### 30.2 SBOM and advisories

The SBOM lists 84 components; one medium advisory affects a development-only tool that does not ship; it is recorded as not applicable.

Section thirty point two develops laboratory ii with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty point two, Grace Nwosu expects laboratory claims to carry owners and dates.

Section thirty point two treats the exercise sbom and as testable only when evidence and ticket IDs are recorded.

For section thirty point two, Hollowbrook University will not accept laboratory work without a written trail.

### 30.3 Hashes

All packages match lockfile hashes.

Section thirty point three develops laboratory ii with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty point three, Grace Nwosu expects laboratory claims to carry owners and dates.

Section thirty point three treats the exercise sbom and as testable only when evidence and ticket IDs are recorded.

For section thirty point three, Hollowbrook University will not accept laboratory work without a written trail.

Section thirty point three fails closed if laboratory evidence is missing rather than guessing.

### 30.4 Signature and provenance

The bundle is signed by the expected build identity; provenance shows the expected repository and a reviewed commit.

Section thirty point four develops laboratory ii with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty point four, Grace Nwosu expects laboratory claims to carry owners and dates.

Section thirty point four treats the exercise sbom and as testable only when evidence and ticket IDs are recorded.

For section thirty point four, Hollowbrook University will not accept laboratory work without a written trail.

### 30.5 Tests

All authorisation, encoding and header tests pass.

Section thirty point five develops laboratory ii with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty point five, Grace Nwosu expects laboratory claims to carry owners and dates.

Section thirty point five treats the exercise sbom and as testable only when evidence and ticket IDs are recorded.

For section thirty point five, Hollowbrook University will not accept laboratory work without a written trail.

Section thirty point five fails closed if laboratory evidence is missing rather than guessing.

### 30.6 Report

A one-page release verification report lists each check, result and evidence link; it becomes part of the release.

Section thirty point six develops laboratory ii with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty point six, Grace Nwosu expects laboratory claims to carry owners and dates.

Section thirty point six treats the exercise sbom and as testable only when evidence and ticket IDs are recorded.

For section thirty point six, Hollowbrook University will not accept laboratory work without a written trail.

### 30.7 Conduct

All work is done in the test environment under permission; findings are recorded in the private tracker.

Section thirty point seven develops laboratory ii with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty point seven, Grace Nwosu expects laboratory claims to carry owners and dates.

Section thirty point seven treats the exercise sbom and as testable only when evidence and ticket IDs are recorded.

For section thirty point seven, Hollowbrook University will not accept laboratory work without a written trail.

### Comparing releases

Lena compares the new SBOM with the previous release's: five components were added and two removed. Each addition is checked for an owner and a reason. Comparing releases shows changes clearly, which is easier to review than the full list of 84 components each time.

### Lessons from the lab

The exercise shows that most checks are fast when automated, and that the slowest part is reviewing changes in the SBOM. Lena suggests showing only the differences by default, which halves review time in the next release.

### Archive

Each report is stored with its release.

### Worked example

Grace asks how long the full check took: 12 minutes, mostly automated. She suggests making the report generation automatic too; Lena adds a script so every release produces its report.

> **Synthetic case.** The release and results are synthetic.

### Errors and limits

A clean report reflects the checks performed; it does not cover threats outside them.

### Exercises

- **EX088 — Check list.** List the five checks in the release exercise. *Rubric:* 3 = SBOM/advisories, hashes, signature, provenance, tests; 2 = four; 1 = two; 0 = none.
- **EX089 — Advisory result.** What advisory issue was found? *Rubric:* 3 = medium in dev-only tool; not applicable; 2 = partial; 1 = none; 0 = none.
- **EX090 — Automation.** What did Grace suggest? *Rubric:* 3 = automate report generation; 2 = partial; 1 = none; 0 = none.

### Synthesis

Combine checks into one release verification with a clear report.

### Continue studying — chapter 30 of 40

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Application and software supply chain security: advanced cases

### Learning outcomes

You will (1) analyse complex situations combining application and supply-chain issues; (2) reason about maintainer compromise and abandoned packages; (3) plan responses under uncertainty; (4) communicate with upstream projects.

### 31.1 Abandoned dependency

A small image-resizing package CampusEats uses has had no release for three years; an advisory reports a flaw with no fix. Options: replace it, maintain a fixed copy internally, or remove the feature (dish photos). The society replaces it with a maintained library, after checking its maintenance activity and number of maintainers.

Section thirty-one point one develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-one point one, Grace Nwosu expects application claims to carry owners and dates.

### 31.2 Maintainer change

A package's maintainer hands it to a new, unknown account, and a new version adds an install script. Ohm et al. (2020) noted takeovers of existing packages as a pattern in malicious package cases. The society holds the update, checks the change notes and the script's purpose, and asks in the project's issue tracker. The script turns out to be a legitimate build step, but the society keeps the update on hold until other users confirm.

Section thirty-one point two develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

### 31.3 Uncertainty

Often you cannot know quickly whether a change is malicious. Holding updates is safe if the current version has no known issues; pin and wait.

Section thirty-one point three develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-one point three, Grace Nwosu expects application claims to carry owners and dates.

Section thirty-one point three treats abandoned dependency maintainer change as testable only when evidence and ticket IDs are recorded.

For section thirty-one point three, Hollowbrook University will not accept application work without a written trail.

### 31.4 Upstream communication

Polite, specific questions in public trackers help everyone; private reports go through security contacts.

Section thirty-one point four develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-one point four, Grace Nwosu expects application claims to carry owners and dates.

Section thirty-one point four treats abandoned dependency maintainer change as testable only when evidence and ticket IDs are recorded.

For section thirty-one point four, Hollowbrook University will not accept application work without a written trail.

### 31.5 Combined issues

A flaw in a template library could allow cross-site scripting only if the app uses a rare feature. Checking reachability prevents panic: CampusEats does not use it, but updates anyway.

Section thirty-one point five develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-one point five, Grace Nwosu expects application claims to carry owners and dates.

Section thirty-one point five treats abandoned dependency maintainer change as testable only when evidence and ticket IDs are recorded.

### 31.6 Balance

Each response balances risk, effort and the volunteers' time.

Section thirty-one point six develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-one point six, Grace Nwosu expects application claims to carry owners and dates.

Section thirty-one point six treats abandoned dependency maintainer change as testable only when evidence and ticket IDs are recorded.

For section thirty-one point six, Hollowbrook University will not accept application work without a written trail.

Section thirty-one point six fails closed if application evidence is missing rather than guessing.

### Worked example

Three weeks after the maintainer change, the society checks the package again: the new maintainer is now listed on the project's website, other projects report no problems, and a security reviewer from a larger project has looked at the install script. The hold is lifted.

> **Synthetic case.** Packages and events are synthetic.

### Errors and limits

Waiting for others to confirm safety relies on someone else checking; for critical packages, review it yourself.

### Exercises

- **EX091 — Abandoned options.** List the options for the abandoned package. *Rubric:* 3 = replace, maintain copy, remove feature; 2 = two; 1 = one; 0 = none.
- **EX092 — Maintainer response.** How did the society respond to the maintainer change? *Rubric:* 3 = hold update; check notes/script; ask; wait for confirmation; 2 = partial; 1 = none; 0 = none.
- **EX093 — Reachability.** Why did reachability matter for the template flaw? *Rubric:* 3 = rare feature not used; no panic; 2 = partial; 1 = none; 0 = none.

### Synthesis

In complex cases, hold safely, gather evidence and communicate with upstream.

### Continue studying — chapter 31 of 40

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Application and software supply chain security: interdisciplinary interfaces

### Learning outcomes

You will (1) work with legal, procurement and privacy teams on software risks; (2) understand licences and contracts; (3) consider accessibility and usability alongside security; (4) communicate across disciplines.

### 32.1 Legal and licences

Open-source licences set conditions for use. A dependency with a licence incompatible with the university's rules must be replaced. CampusEats checks licences automatically and sends unusual ones to the university's legal team.

Section thirty-two point one develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-two point one, Grace Nwosu expects application claims to carry owners and dates.

Section thirty-two point one treats legal and licences procurement as testable only when evidence and ticket IDs are recorded.

### 32.2 Procurement

When cafés asked for a till integration, the university's procurement team needed security questions for the till vendor: Does it follow secure development practices like the SSDF? Does it provide SBOMs and timely fixes? Lena drafts the questions with Grace.

Section thirty-two point two develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-two point two, Grace Nwosu expects application claims to carry owners and dates.

Section thirty-two point two treats legal and licences procurement as testable only when evidence and ticket IDs are recorded.

### 32.3 Privacy

The data protection officer reviews new features that use personal data, such as loyalty points.

Section thirty-two point three develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-two point three, Grace Nwosu expects application claims to carry owners and dates.

Section thirty-two point three treats legal and licences procurement as testable only when evidence and ticket IDs are recorded.

For section thirty-two point three, Hollowbrook University will not accept application work without a written trail.

### 32.4 Accessibility

Security features must be usable by everyone: multi-factor prompts and error messages must work with screen readers.

Section thirty-two point four develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-two point four, Grace Nwosu expects application claims to carry owners and dates.

Section thirty-two point four treats legal and licences procurement as testable only when evidence and ticket IDs are recorded.

For section thirty-two point four, Hollowbrook University will not accept application work without a written trail.

### 32.5 Usability

Johnson et al. (2013) showed developers avoid tools that are hard to use; the same applies to students facing awkward security steps. Good design reduces workarounds.

Section thirty-two point five develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-two point five, Grace Nwosu expects application claims to carry owners and dates.

Section thirty-two point five treats legal and licences procurement as testable only when evidence and ticket IDs are recorded.

For section thirty-two point five, Hollowbrook University will not accept application work without a written trail.

### 32.6 Communication

Each discipline uses different words; Lena keeps a glossary and explains technical terms in one sentence.

Section thirty-two point six develops application and software supply chain with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-two point six, Grace Nwosu expects application claims to carry owners and dates.

Section thirty-two point six treats legal and licences procurement as testable only when evidence and ticket IDs are recorded.

For section thirty-two point six, Hollowbrook University will not accept application work without a written trail.

### Shared language

Lena writes a one-page explainer on SBOMs for the legal and procurement teams, avoiding jargon. It explains what an SBOM shows, why it helps when a flaw is announced, and what to ask vendors for. Procurement now includes the SBOM question in every software purchase checklist.

### Planning reviews

Reviews by other teams are booked at the start of a feature, not the end.

### Worked example

The loyalty-points feature initially stored students' full order history indefinitely. The privacy review asks for points totals only, with history deleted after two years like other orders. The design changes before any code is written.

> **Synthetic case.** Teams and features are synthetic.

### Errors and limits

Interdisciplinary work takes time; plan reviews early in the design.

### Exercises

- **EX094 — Licence handling.** How are unusual licences handled? *Rubric:* 3 = auto check; legal review; 2 = partial; 1 = none; 0 = none.
- **EX095 — Vendor questions.** Give two procurement questions for the till vendor. *Rubric:* 3 = SSDF practices; SBOMs and timely fixes; 2 = one; 1 = none; 0 = none.
- **EX096 — Loyalty change.** What did the privacy review change? *Rubric:* 3 = totals only; history deleted after 2 years; 2 = partial; 1 = none; 0 = none.

### Synthesis

Security works best alongside legal, procurement, privacy and usability expertise.

### Continue studying — chapter 32 of 40

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Research methods II

### Learning outcomes

You will (1) design a comparative study; (2) choose measures and controls for confounders; (3) analyse with simple statistics and agreement measures; (4) report reproducibly.

### 33.1 Question

Lena's next question: do student projects that adopt dependency update bots fix high-severity advisories faster than those that do not?

Section thirty-three point one develops research methods ii with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-three point one, Grace Nwosu expects research claims to carry owners and dates.

Section thirty-three point one treats question design confounders coding as testable only when evidence and ticket IDs are recorded.

For section thirty-three point one, Hollowbrook University will not accept research work without a written trail.

### 33.2 Design

Compare 12 student projects at Hollowbrook: 6 with bots, 6 without, matched by size. Measure days from advisory publication to fix merged.

Section thirty-three point two develops research methods ii with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-three point two, Grace Nwosu expects research claims to carry owners and dates.

Section thirty-three point two treats question design confounders coding as testable only when evidence and ticket IDs are recorded.

For section thirty-three point two, Hollowbrook University will not accept research work without a written trail.

### 33.3 Confounders

Projects with bots may have more experienced members. Lena records team experience and checks whether it differs between groups.

Section thirty-three point three develops research methods ii with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-three point three, Grace Nwosu expects research claims to carry owners and dates.

Section thirty-three point three treats question design confounders coding as testable only when evidence and ticket IDs are recorded.

For section thirty-three point three, Hollowbrook University will not accept research work without a written trail.

### 33.4 Coding agreement

Two people independently judge whether each fix fully addresses the advisory. Agreement is measured with Cohen's kappa and interpreted with Landis and Koch (1977).

Section thirty-three point four develops research methods ii with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-three point four, Grace Nwosu expects research claims to carry owners and dates.

Section thirty-three point four treats question design confounders coding as testable only when evidence and ticket IDs are recorded.

For section thirty-three point four, Hollowbrook University will not accept research work without a written trail.

### 33.5 Analysis

Medians are compared because fix times are skewed; individual values are shown.

Section thirty-three point five develops research methods ii with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-three point five, Grace Nwosu expects research claims to carry owners and dates.

Section thirty-three point five treats question design confounders coding as testable only when evidence and ticket IDs are recorded.

For section thirty-three point five, Hollowbrook University will not accept research work without a written trail.

Section thirty-three point five fails closed if research evidence is missing rather than guessing.

### 33.6 Reproducibility

Scripts and a synthetic version of the data are shared.

Section thirty-three point six develops research methods ii with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-three point six, Grace Nwosu expects research claims to carry owners and dates.

Section thirty-three point six treats question design confounders coding as testable only when evidence and ticket IDs are recorded.

For section thirty-three point six, Hollowbrook University will not accept research work without a written trail.

Section thirty-three point six fails closed if research evidence is missing rather than guessing.

### 33.7 Prior work

Kula et al. (2018) found developers often do not update dependencies; Lena's study asks whether tooling helps in student projects.

Section thirty-three point seven develops research methods ii with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-three point seven, Grace Nwosu expects research claims to carry owners and dates.

Section thirty-three point seven treats question design confounders coding as testable only when evidence and ticket IDs are recorded.

For section thirty-three point seven, Hollowbrook University will not accept research work without a written trail.

### Ethics and consent

Project leads consent to their repositories' metadata being analysed; results are reported without naming projects. Only public metadata and fix dates are used; no code from projects is copied into the study. The study plan is approved through the university's ethics process before data collection begins.

### Reporting the study

The write-up follows a simple structure: question, method, data, results, limitations and recommendations. Lena includes a table of each project's fix times without names, so readers can see the spread, and states clearly that the study shows association, not proof of cause.

### Worked example

Results: median fix time 6 days with bots, 24 days without; experience levels were similar. Kappa for fix judgement was 0.82. Lena reports the difference as promising for a small sample and recommends bots to all student projects.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Twelve projects cannot establish cause; matched comparison reduces but does not remove bias.

### Exercises

- **EX097 — Confounder.** What confounder did Lena consider? *Rubric:* 3 = team experience; 2 = partial; 1 = none; 0 = none.
- **EX098 — Results.** Give the median fix times and kappa. *Rubric:* 3 = 6 vs 24 days; 0.82; 2 = partial; 1 = one; 0 = none.
- **EX099 — Why medians.** Why compare medians? *Rubric:* 3 = fix times skewed; 2 = partial; 1 = none; 0 = none.

### Synthesis

Comparative studies need matched groups, reliability checks and honest scope.

### Continue studying — chapter 33 of 40

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Comparative project

### Learning outcomes

You will (1) compare two approaches to a supply-chain problem; (2) define criteria; (3) run a fair trial; (4) recommend with evidence.

### 34.1 The problem

CampusEats must choose between two ways of keeping dependencies current: a bot that opens small weekly pull requests, or a monthly manual "update day".

Section thirty-four point one develops comparative project with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-four point one, Grace Nwosu expects comparative claims to carry owners and dates.

Section thirty-four point one treats the problem criteria trial as testable only when evidence and ticket IDs are recorded.

For section thirty-four point one, Hollowbrook University will not accept comparative work without a written trail.

### 34.2 Criteria

Time to apply high-severity fixes, member time spent, number of broken builds and member satisfaction.

Section thirty-four point two develops comparative project with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-four point two, Grace Nwosu expects comparative claims to carry owners and dates.

Section thirty-four point two treats the problem criteria trial as testable only when evidence and ticket IDs are recorded.

For section thirty-four point two, Hollowbrook University will not accept comparative work without a written trail.

### 34.3 Trial

Each approach runs for six weeks in turn, with records kept.

Section thirty-four point three develops comparative project with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-four point three, Grace Nwosu expects comparative claims to carry owners and dates.

Section thirty-four point three treats the problem criteria trial as testable only when evidence and ticket IDs are recorded.

For section thirty-four point three, Hollowbrook University will not accept comparative work without a written trail.

Section thirty-four point three fails closed if comparative evidence is missing rather than guessing.

### 34.4 Results

Bot: high-severity fixes applied in a median of 3 days; 2 hours of member time per week; 3 broken builds, each fixed quickly. Manual: median 16 days; 5 hours on update day each month; 1 large broken build that took a day to fix.

Section thirty-four point four develops comparative project with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-four point four, Grace Nwosu expects comparative claims to carry owners and dates.

Section thirty-four point four treats the problem criteria trial as testable only when evidence and ticket IDs are recorded.

### 34.5 Satisfaction

Members preferred the bot, saying small changes were easier to review.

Section thirty-four point five develops comparative project with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-four point five, Grace Nwosu expects comparative claims to carry owners and dates.

Section thirty-four point five treats the problem criteria trial as testable only when evidence and ticket IDs are recorded.

For section thirty-four point five, Hollowbrook University will not accept comparative work without a written trail.

Section thirty-four point five fails closed if comparative evidence is missing rather than guessing.

### 34.6 Recommendation

Adopt the bot, keep a monthly review of major versions.

Section thirty-four point six develops comparative project with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-four point six, Grace Nwosu expects comparative claims to carry owners and dates.

Section thirty-four point six treats the problem criteria trial as testable only when evidence and ticket IDs are recorded.

For section thirty-four point six, Hollowbrook University will not accept comparative work without a written trail.

Section thirty-four point six fails closed if comparative evidence is missing rather than guessing.

### Fair comparison

To keep the trial fair, the same members ran both approaches and the same tests applied. Records were kept by a member not involved in choosing the approach. Lena also logged unusual events, such as a week when the CI service was down, so they could be excluded or explained. A fair trial is one where the only intended difference is the approach being compared, and where the people recording results do not have a stake in either outcome.

### Decision record

The final recommendation is written as a decision record: context, options compared, evidence, choice and review date. It links to the trial data, so future members can revisit the choice if tools or circumstances change.

### Worked example

Lena's report includes a limitation: the bot trial ran during a quieter term period. She recommends checking the measures again during the busy exam term. The check confirms the result.

> **Synthetic case.** Trial data are synthetic.

### Errors and limits

Sequential trials can be affected by timing; repeat when conditions change.

### Exercises

- **EX100 — Criteria.** List the four criteria. *Rubric:* 3 = fix time, member time, broken builds, satisfaction; 2 = three; 1 = one; 0 = none.
- **EX101 — Results.** Compare fix times. *Rubric:* 3 = bot 3 days vs manual 16; 2 = one; 1 = none; 0 = none.
- **EX102 — Limitation.** What limitation did Lena note? *Rubric:* 3 = bot ran in quieter period; recheck in exam term; 2 = partial; 1 = none; 0 = none.

### Synthesis

Compare approaches on agreed criteria and test the result under different conditions.

### Continue studying — chapter 34 of 40

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Capstone proposal

### Learning outcomes

You will (1) propose a capstone that addresses a real need; (2) set objectives and success criteria; (3) plan method, timeline and risks; (4) obtain approval.

### 35.1 The need

Several student projects at Hollowbrook share the same problems CampusEats faced. Lena proposes a "secure project starter": a template repository with secret scanning, lockfile hash checks, SBOM generation, signing and provenance, update bot configuration and ASVS-based tests.

Section thirty-five point one develops capstone proposal with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-five point one, Grace Nwosu expects capstone claims to carry owners and dates.

Section thirty-five point one treats the need objectives success as testable only when evidence and ticket IDs are recorded.

### 35.2 Objectives

Make it easy for new projects to start with good supply-chain hygiene; measure adoption and effect.

Section thirty-five point two develops capstone proposal with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-five point two, Grace Nwosu expects capstone claims to carry owners and dates.

Section thirty-five point two treats the need objectives success as testable only when evidence and ticket IDs are recorded.

For section thirty-five point two, Hollowbrook University will not accept capstone work without a written trail.

### 35.3 Success criteria

At least four projects adopt it in a term; zero secrets reach public repositories in adopting projects; setup takes under one hour.

Section thirty-five point three develops capstone proposal with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-five point three, Grace Nwosu expects capstone claims to carry owners and dates.

Section thirty-five point three treats the need objectives success as testable only when evidence and ticket IDs are recorded.

For section thirty-five point three, Hollowbrook University will not accept capstone work without a written trail.

### 35.4 Method

Build the template, pilot with two projects, improve, then offer to all.

Section thirty-five point four develops capstone proposal with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-five point four, Grace Nwosu expects capstone claims to carry owners and dates.

Section thirty-five point four treats the need objectives success as testable only when evidence and ticket IDs are recorded.

For section thirty-five point four, Hollowbrook University will not accept capstone work without a written trail.

Section thirty-five point four fails closed if capstone evidence is missing rather than guessing.

### 35.5 Risks

Low adoption (mitigate with a workshop); maintenance burden (Grace's office agrees to own it after Lena graduates).

Section thirty-five point five develops capstone proposal with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-five point five, Grace Nwosu expects capstone claims to carry owners and dates.

Section thirty-five point five treats the need objectives success as testable only when evidence and ticket IDs are recorded.

For section thirty-five point five, Hollowbrook University will not accept capstone work without a written trail.

### 35.6 Approval

Grace and Lena's supervisor sign off.

Section thirty-five point six develops capstone proposal with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-five point six, Grace Nwosu expects capstone claims to carry owners and dates.

Section thirty-five point six treats the need objectives success as testable only when evidence and ticket IDs are recorded.

For section thirty-five point six, Hollowbrook University will not accept capstone work without a written trail.

Section thirty-five point six fails closed if capstone evidence is missing rather than guessing.

### Timeline

The plan runs over two terms: four weeks to build the template, four weeks piloting with two projects, two weeks improving it, and the rest of the year for rollout and measurement. Each phase ends with a short review with Grace. The timeline includes slack for exams, when volunteer time drops sharply, which earlier society projects had forgotten.

### Measuring adoption

Adoption is measured by counting projects created from the template and checking that their CI checks are active, not just present. Lena plans a short survey after one term to learn what projects found hard, so the template can improve. She also plans to compare secrets found in adopting and non-adopting projects, while noting the groups may differ in other ways.

### Worked example

The proposal review asks how the template stays current. Lena adds a monthly automated job that updates the template's own dependencies and checks it still passes.

> **Synthetic case.** The proposal is synthetic.

### Errors and limits

Templates help new projects; existing projects need a migration guide.

### Exercises

- **EX103 — Template contents.** List four features of the starter template. *Rubric:* 3 = secret scanning, hash checks, SBOM, signing/provenance, update bot, ASVS tests (four); 2 = two; 1 = one; 0 = none.
- **EX104 — Success criteria.** Give the success criteria. *Rubric:* 3 = ≥4 projects; zero secrets; setup <1 h; 2 = two; 1 = one; 0 = none.
- **EX105 — Staying current.** How will the template stay current? *Rubric:* 3 = monthly automated update job; 2 = partial; 1 = none; 0 = none.

### Synthesis

A capstone proposal names a real need, measurable success and an owner after you leave.

### Continue studying — chapter 35 of 40

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Field or community practice

### Learning outcomes

You will (1) apply application security skills in a community setting; (2) support other projects responsibly; (3) teach secure practices; (4) reflect on community work.

### 36.1 The setting

Lena volunteers with a local charity that runs a food-bank booking website built by volunteers. Under a written agreement with the charity, she helps review its development practices, not to test live systems without permission.

Section thirty-six point one develops field or community practice with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-six point one, Grace Nwosu expects field claims to carry owners and dates.

Section thirty-six point one treats the setting what she as testable only when evidence and ticket IDs are recorded.

### 36.2 What she finds

The site's repository is private but shared with many past volunteers; three still have write access. Dependencies have not been updated for a year; two have high-severity advisories. A database password is stored in a configuration file in the repository.

Section thirty-six point two develops field or community practice with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-six point two, Grace Nwosu expects field claims to carry owners and dates.

Section thirty-six point two treats the setting what she as testable only when evidence and ticket IDs are recorded.

### 36.3 What she does

She helps the charity remove old access, move the password to the hosting platform's secret settings and rotate it, and set up an update bot. She explains each step so volunteers can continue.

Section thirty-six point three develops field or community practice with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-six point three, Grace Nwosu expects field claims to carry owners and dates.

Section thirty-six point three treats the setting what she as testable only when evidence and ticket IDs are recorded.

### 36.4 Teaching

Lena runs a two-hour workshop for the charity's volunteers on secrets, updates and access, using the CampusEats case cards.

Section thirty-six point four develops field or community practice with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-six point four, Grace Nwosu expects field claims to carry owners and dates.

Section thirty-six point four treats the setting what she as testable only when evidence and ticket IDs are recorded.

For section thirty-six point four, Hollowbrook University will not accept field work without a written trail.

### 36.5 Boundaries

Lena does not access the food bank's client data; she works only on code and configuration with the charity's coordinator present.

Section thirty-six point five develops field or community practice with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-six point five, Grace Nwosu expects field claims to carry owners and dates.

Section thirty-six point five treats the setting what she as testable only when evidence and ticket IDs are recorded.

For section thirty-six point five, Hollowbrook University will not accept field work without a written trail.

### 36.6 Reflection

Lena notes that small organisations need simple, sustainable practices more than advanced tools.

Section thirty-six point six develops field or community practice with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-six point six, Grace Nwosu expects field claims to carry owners and dates.

Section thirty-six point six treats the setting what she as testable only when evidence and ticket IDs are recorded.

For section thirty-six point six, Hollowbrook University will not accept field work without a written trail.

### Agreement

The written agreement states the purpose, what Lena may access, who supervises, and that she will not keep copies of any code or data. Both Lena and the charity's coordinator sign it, and Grace reviews it to make sure it protects the charity and Lena.

### Worked example

Three months later the charity's coordinator reports that the update bot has merged 14 updates and that new volunteers now receive access only for the duration of their project. Lena's community report becomes part of her course portfolio.

> **Synthetic case.** The charity and findings are synthetic.

### Errors and limits

Volunteer help must not create dependency on one person; leave documentation and owners.

### Exercises

- **EX106 — Three findings.** List the three findings at the charity. *Rubric:* 3 = old write access; outdated deps with advisories; password in repo; 2 = two; 1 = one; 0 = none.
- **EX107 — Boundaries.** What boundaries did Lena keep? *Rubric:* 3 = no client data; code/config only; coordinator present; 2 = partial; 1 = none; 0 = none.
- **EX108 — Outcome.** What was the outcome after three months? *Rubric:* 3 = 14 updates merged; time-limited access; 2 = partial; 1 = none; 0 = none.

### Synthesis

Community practice means simple, sustainable improvements within clear boundaries.

### Continue studying — chapter 36 of 40

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Evidence review seminar

### Learning outcomes

You will (1) critically review published evidence on supply-chain security; (2) compare study designs and limits; (3) synthesise findings for practice; (4) present a balanced review.

### 37.1 Choosing studies

Lena's seminar group reviews five studies: Ohm et al. (2020) on malicious packages, Zimmermann et al. (2019) on npm ecosystem risk, Decan et al. (2018) on vulnerability propagation, Kula et al. (2018) on dependency updating and Wermke et al. (2022) on open-source trust.

Section thirty-seven point one develops evidence review seminar with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-seven point one, Grace Nwosu expects evidence claims to carry owners and dates.

Section thirty-seven point one treats choosing studies designs limits as testable only when evidence and ticket IDs are recorded.

### 37.2 Designs

Two are case collections, two are large-scale measurement studies, one is an interview study. Each design answers different questions: what happens, how often, and why.

Section thirty-seven point two develops evidence review seminar with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-seven point two, Grace Nwosu expects evidence claims to carry owners and dates.

Section thirty-seven point two treats choosing studies designs limits as testable only when evidence and ticket IDs are recorded.

For section thirty-seven point two, Hollowbrook University will not accept evidence work without a written trail.

### 37.3 Limits

Case collections show only discovered cases; measurement studies depend on data quality and ecosystem; interview studies have small, self-selected samples.

Section thirty-seven point three develops evidence review seminar with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-seven point three, Grace Nwosu expects evidence claims to carry owners and dates.

Section thirty-seven point three treats choosing studies designs limits as testable only when evidence and ticket IDs are recorded.

For section thirty-seven point three, Hollowbrook University will not accept evidence work without a written trail.

### 37.4 Synthesis

Together they suggest: risk concentrates in widely used packages; updates lag; malicious packages exploit trust and install-time behaviour; maintainers vary widely in security practice.

Section thirty-seven point four develops evidence review seminar with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-seven point four, Grace Nwosu expects evidence claims to carry owners and dates.

Section thirty-seven point four treats choosing studies designs limits as testable only when evidence and ticket IDs are recorded.

For section thirty-seven point four, Hollowbrook University will not accept evidence work without a written trail.

### 37.5 Implications

For small projects: fewer dependencies, prompt updates, install-time restrictions, and checks on new names and maintainers.

Section thirty-seven point five develops evidence review seminar with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-seven point five, Grace Nwosu expects evidence claims to carry owners and dates.

Section thirty-seven point five treats choosing studies designs limits as testable only when evidence and ticket IDs are recorded.

For section thirty-seven point five, Hollowbrook University will not accept evidence work without a written trail.

### 37.6 Presentation

The group presents a balanced view, separating strong findings from tentative ones.

Section thirty-seven point six develops evidence review seminar with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-seven point six, Grace Nwosu expects evidence claims to carry owners and dates.

Section thirty-seven point six treats choosing studies designs limits as testable only when evidence and ticket IDs are recorded.

For section thirty-seven point six, Hollowbrook University will not accept evidence work without a written trail.

Section thirty-seven point six fails closed if evidence evidence is missing rather than guessing.

### Reading critically

For each study the group asks: what question, what data, what method, what results, what limits, and what it means for a small project. Answering the same questions for every study makes comparison easier and stops the group from being swayed by impressive numbers without context. They also check whether each claim they plan to present is actually supported by the study's own results.

### Selection criteria

Studies were chosen for relevance, peer review and clear methods.

### Worked example

A classmate argues the studies focus on one ecosystem (npm) too much. The group agrees and notes that other ecosystems may differ, recommending readers check for studies of their own ecosystem.

> **Synthetic case.** Seminar discussion is synthetic; the cited studies are real.

### Errors and limits

Reviews can be biased by which studies are chosen; state selection criteria.

### Exercises

- **EX109 — Design types.** What three design types were reviewed? *Rubric:* 3 = case collections, measurement studies, interview study; 2 = two; 1 = one; 0 = none.
- **EX110 — Synthesis.** Summarise the synthesis. *Rubric:* 3 = risk concentrated; updates lag; malicious exploit trust/install; maintainers vary; 2 = partial; 1 = one; 0 = none.
- **EX111 — Ecosystem critique.** What critique did the classmate raise? *Rubric:* 3 = too focused on npm; 2 = partial; 1 = none; 0 = none.

### Synthesis

Review evidence by design and limits, then synthesise carefully for practice.

### Continue studying — chapter 37 of 40

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Capstone implementation

### Learning outcomes

You will (1) build the secure project starter template; (2) integrate checks into CI; (3) pilot with real projects; (4) fix problems found in the pilot.

### 38.1 Building

Lena builds the template: CI configuration with tests, secret scanning, lockfile checks, SBOM generation, signing and provenance; an update bot configuration; a set of ASVS-based tests for sessions, headers and authorisation; and a README with setup steps.

Section thirty-eight point one develops capstone implementation with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-eight point one, Grace Nwosu expects capstone claims to carry owners and dates.

Section thirty-eight point one treats building self-application pilot problems as testable only when evidence and ticket IDs are recorded.

### 38.2 Self-application

The template itself follows its own rules: its dependencies are minimal and updated by the bot, and its releases are signed.

Section thirty-eight point two develops capstone implementation with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-eight point two, Grace Nwosu expects capstone claims to carry owners and dates.

Section thirty-eight point two treats building self-application pilot problems as testable only when evidence and ticket IDs are recorded.

For section thirty-eight point two, Hollowbrook University will not accept capstone work without a written trail.

### 38.3 Pilot

Two student projects, a society events app and a study-room booking tool, adopt it.

Section thirty-eight point three develops capstone implementation with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-eight point three, Grace Nwosu expects capstone claims to carry owners and dates.

Section thirty-eight point three treats building self-application pilot problems as testable only when evidence and ticket IDs are recorded.

For section thirty-eight point three, Hollowbrook University will not accept capstone work without a written trail.

Section thirty-eight point three fails closed if capstone evidence is missing rather than guessing.

### 38.4 Problems found

Setup took 2.5 hours, not under one, mainly because of signing configuration. The secret scanner flagged sample keys in the template's own documentation.

Section thirty-eight point four develops capstone implementation with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-eight point four, Grace Nwosu expects capstone claims to carry owners and dates.

Section thirty-eight point four treats building self-application pilot problems as testable only when evidence and ticket IDs are recorded.

For section thirty-eight point four, Hollowbrook University will not accept capstone work without a written trail.

### 38.5 Fixes

A setup script automates signing configuration; documentation sample keys are marked and allowlisted.

Section thirty-eight point five develops capstone implementation with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-eight point five, Grace Nwosu expects capstone claims to carry owners and dates.

Section thirty-eight point five treats building self-application pilot problems as testable only when evidence and ticket IDs are recorded.

For section thirty-eight point five, Hollowbrook University will not accept capstone work without a written trail.

Section thirty-eight point five fails closed if capstone evidence is missing rather than guessing.

### 38.6 After fixes

Setup time falls to 40 minutes in a third trial.

Section thirty-eight point six develops capstone implementation with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-eight point six, Grace Nwosu expects capstone claims to carry owners and dates.

Section thirty-eight point six treats building self-application pilot problems as testable only when evidence and ticket IDs are recorded.

For section thirty-eight point six, Hollowbrook University will not accept capstone work without a written trail.

Section thirty-eight point six fails closed if capstone evidence is missing rather than guessing.

### Documentation

The README explains each check in plain words: what it protects against, what a failure means and how to fix it. Lena tests the README by asking a first-year student to set up a project using only the document; every question the student asks becomes a new line in the README. Short, tested documentation proved as important as the checks themselves.

### Code review of the template

Grace and two experienced society members review the template's CI configuration line by line, since a mistake there would spread to every project using it. They find one check that ran only on the main branch and not on pull requests; it is fixed so problems are caught before merging.

### Worked example

The booking tool's team finds that the template's authorisation tests reveal that any logged-in student could cancel another student's booking. They fix it before launch, the first real flaw caught by the template.

> **Synthetic case.** Projects and results are synthetic.

### Errors and limits

Templates cannot anticipate every project's needs; leave room for customisation.

### Exercises

- **EX112 — Template parts.** List four parts of the template. *Rubric:* 3 = CI checks, update bot, ASVS tests, README (four); 2 = two; 1 = one; 0 = none.
- **EX113 — Pilot problems.** What two problems did the pilot reveal? *Rubric:* 3 = setup 2.5 h due to signing; scanner flagged doc sample keys; 2 = one; 1 = none; 0 = none.
- **EX114 — First flaw.** What flaw did the template catch? *Rubric:* 3 = any student could cancel others' bookings; 2 = partial; 1 = none; 0 = none.

### Synthesis

Build, pilot, fix and let the template prove itself on real projects.

### Continue studying — chapter 38 of 40

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Capstone evaluation

### Learning outcomes

You will (1) evaluate the capstone against success criteria; (2) collect quantitative and qualitative evidence; (3) identify limitations; (4) plan handover.

### 39.1 Adoption

Five projects adopted the template in the term, above the target of four.

Section thirty-nine point one develops capstone evaluation with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-nine point one, Grace Nwosu expects capstone claims to carry owners and dates.

Section thirty-nine point one treats adoption secrets setup time as testable only when evidence and ticket IDs are recorded.

For section thirty-nine point one, Hollowbrook University will not accept capstone work without a written trail.

Section thirty-nine point one fails closed if capstone evidence is missing rather than guessing.

### 39.2 Secrets

No secrets reached public repositories in adopting projects; the scanner caught two before push.

Section thirty-nine point two develops capstone evaluation with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-nine point two, Grace Nwosu expects capstone claims to carry owners and dates.

Section thirty-nine point two treats adoption secrets setup time as testable only when evidence and ticket IDs are recorded.

For section thirty-nine point two, Hollowbrook University will not accept capstone work without a written trail.

Section thirty-nine point two fails closed if capstone evidence is missing rather than guessing.

### 39.3 Setup time

Median setup 40 minutes across five projects.

Section thirty-nine point three develops capstone evaluation with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-nine point three, Grace Nwosu expects capstone claims to carry owners and dates.

Section thirty-nine point three treats adoption secrets setup time as testable only when evidence and ticket IDs are recorded.

For section thirty-nine point three, Hollowbrook University will not accept capstone work without a written trail.

Section thirty-nine point three fails closed if capstone evidence is missing rather than guessing.

### 39.4 Feedback

Teams liked ready-made tests; some found SBOM output confusing. Lena adds a short guide.

Section thirty-nine point four develops capstone evaluation with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-nine point four, Grace Nwosu expects capstone claims to carry owners and dates.

Section thirty-nine point four treats adoption secrets setup time as testable only when evidence and ticket IDs are recorded.

For section thirty-nine point four, Hollowbrook University will not accept capstone work without a written trail.

Section thirty-nine point four fails closed if capstone evidence is missing rather than guessing.

### 39.5 Limits

One term, five projects, volunteers who may have been more security-minded than average.

Section thirty-nine point five develops capstone evaluation with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-nine point five, Grace Nwosu expects capstone claims to carry owners and dates.

Section thirty-nine point five treats adoption secrets setup time as testable only when evidence and ticket IDs are recorded.

For section thirty-nine point five, Hollowbrook University will not accept capstone work without a written trail.

Section thirty-nine point five fails closed if capstone evidence is missing rather than guessing.

### 39.6 Handover

Grace's office takes ownership with a named maintainer; the monthly update job runs automatically.

Section thirty-nine point six develops capstone evaluation with a Hollowbrook University note Lena Fischer can demo offline.

Under section thirty-nine point six, Grace Nwosu expects capstone claims to carry owners and dates.

Section thirty-nine point six treats adoption secrets setup time as testable only when evidence and ticket IDs are recorded.

For section thirty-nine point six, Hollowbrook University will not accept capstone work without a written trail.

Section thirty-nine point six fails closed if capstone evidence is missing rather than guessing.

### Qualitative evidence

Lena interviews one member of each adopting team for fifteen minutes. Common themes: ready-made tests saved time, the update bot reduced worry about old packages, and the setup script made signing painless. One team said the checks felt strict at first but helped them explain security to their users. Interviews explain why the numbers look as they do and suggest improvements, such as clearer messages when the advisory check fails. Lena codes the answers into themes with a classmate and they agree on all but one, which they discuss and resolve.

### Ongoing measures

The template's maintainer will report adoption, secrets caught and setup time each term, using the same measures, so the evaluation continues after Lena leaves and later results can be compared fairly.

### Reporting

Lena writes a two-page evaluation report for Grace and the project leads, with measures, quotes and recommendations.

### Worked example

Lena compares adopting projects with three similar non-adopting ones: the non-adopters had one secret reach a public repository and a median of 20 days to fix high advisories, versus 5 for adopters. She notes that the groups differ in other ways and that the comparison is indicative only.

> **Synthetic case.** Results are synthetic.

### Errors and limits

Success in the first term may fade without continued support.

### Exercises

- **EX115 — Criteria results.** Report results against the three criteria. *Rubric:* 3 = 5 projects; zero secrets; 40 min; 2 = two; 1 = one; 0 = none.
- **EX116 — Feedback.** What feedback led to a change? *Rubric:* 3 = SBOM output confusing; guide added; 2 = partial; 1 = none; 0 = none.
- **EX117 — Comparison caution.** Why is the adopter comparison only indicative? *Rubric:* 3 = groups differ in other ways; 2 = partial; 1 = none; 0 = none.

### Synthesis

Evaluate against criteria with honest limits and hand over to a lasting owner.

### Continue studying — chapter 39 of 40

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Thesis and presentation

### Learning outcomes

You will (1) write a bachelor's thesis on the capstone; (2) connect it to standards and literature; (3) present to examiners and practitioners; (4) reflect on the four-year journey.

### 40.1 Thesis structure

Introduction (CampusEats incidents), background (OWASP, SSDF, SLSA, SBOM, literature), method (template design and pilot), results, discussion, limitations, conclusion.

Section forty point one develops thesis and presentation with a Hollowbrook University note Lena Fischer can demo offline.

Under section forty point one, Grace Nwosu expects thesis claims to carry owners and dates.

Section forty point one treats thesis structure connections presentation as testable only when evidence and ticket IDs are recorded.

For section forty point one, Hollowbrook University will not accept thesis work without a written trail.

### 40.2 Connections

The template implements SSDF practices across all four groups and SLSA build provenance; its tests draw on ASVS. The discussion relates findings to Johnson et al. (2013) on tool adoption: the template worked because it made secure defaults easy.

Section forty point two develops thesis and presentation with a Hollowbrook University note Lena Fischer can demo offline.

Under section forty point two, Grace Nwosu expects thesis claims to carry owners and dates.

Section forty point two treats thesis structure connections presentation as testable only when evidence and ticket IDs are recorded.

### 40.3 Presentation

Fifteen minutes to examiners, Grace and student project leads: the problem, the template, results, limits and handover.

Section forty point three develops thesis and presentation with a Hollowbrook University note Lena Fischer can demo offline.

Under section forty point three, Grace Nwosu expects thesis claims to carry owners and dates.

Section forty point three treats thesis structure connections presentation as testable only when evidence and ticket IDs are recorded.

For section forty point three, Hollowbrook University will not accept thesis work without a written trail.

### 40.4 Questions

"Would this work for larger projects?" Lena explains it would need customisation and stronger review processes, and suggests a study.

Section forty point four develops thesis and presentation with a Hollowbrook University note Lena Fischer can demo offline.

Under section forty point four, Grace Nwosu expects thesis claims to carry owners and dates.

Section forty point four treats thesis structure connections presentation as testable only when evidence and ticket IDs are recorded.

For section forty point four, Hollowbrook University will not accept thesis work without a written trail.

### 40.5 Reflection

From logic statements about access rules in year one to a template used by five projects, Lena sees security as a habit built into everyday tools.

Section forty point five develops thesis and presentation with a Hollowbrook University note Lena Fischer can demo offline.

Under section forty point five, Grace Nwosu expects thesis claims to carry owners and dates.

Section forty point five treats thesis structure connections presentation as testable only when evidence and ticket IDs are recorded.

For section forty point five, Hollowbrook University will not accept thesis work without a written trail.

### 40.6 Next steps

Lena plans a master's degree and continues to maintain the template as a volunteer.

Section forty point six develops thesis and presentation with a Hollowbrook University note Lena Fischer can demo offline.

Under section forty point six, Grace Nwosu expects thesis claims to carry owners and dates.

Section forty point six treats thesis structure connections presentation as testable only when evidence and ticket IDs are recorded.

For section forty point six, Hollowbrook University will not accept thesis work without a written trail.

### Writing the thesis

Lena drafts the thesis over ten weeks, sharing chapters with her supervisor. She keeps a claims table linking each statement to evidence and checks every citation against its source. Grace checks that the descriptions of CampusEats and other projects reveal no sensitive details. The final thesis is shorter than the first draft, because unsupported or repeated points were removed.

### Thanks and credit

The thesis credits the society, Grace and pilot teams.

### Archive

The final thesis is deposited in the university library.

### Worked example

Examiners award a first-class mark and ask Lena to share the template beyond the university. With Grace's approval, it is published under an open licence with all examples synthetic.

> **Synthetic case.** The thesis and presentation are synthetic.

### Errors and limits

A thesis records what was learned; keep updating practice as tools and threats change.

### Exercises

- **EX118 — SSDF link.** How does the template relate to the SSDF? *Rubric:* 3 = implements practices across all four groups; 2 = partial; 1 = none; 0 = none.
- **EX119 — Larger projects.** How did Lena answer the larger-projects question? *Rubric:* 3 = customisation, stronger review; study; 2 = partial; 1 = none; 0 = none.
- **EX120 — Publication.** How was the template shared? *Rubric:* 3 = open licence; synthetic examples; Grace's approval; 2 = partial; 1 = none; 0 = none.

### Synthesis

Secure habits built into tools and shared openly are a lasting contribution.

### Continue studying — chapter 40 of 40

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX120. Lena Fischer, Grace Nwosu, CampusEats, Hollowbrook University and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** If a user is not staff, the user does not change prices.

**EX002.** Some request is not logged.

**EX003.** Volunteers may refund up to £5, yet only staff may issue refunds.

**EX004.** Browser sends HTTPS request; server checks session and validates; writes to database and calls payment; returns confirmation.

**EX005.** In the browser bundle, in server packages and in external services such as payments.

**EX006.** The payment provider's "paid" callback was not verified as genuine.

**EX007.** Because prices sent by the browser can be altered.

**EX008.** No; history keeps it, so the secret must be revoked.

**EX009.** The .gitignore entry pointed to the wrong folder.

**EX010.** Why do secrets leak into source repositories?

**EX011.** It was narrowed to what the case showed: found within two hours.

**EX012.** They often share infrastructure with live systems.

**EX013.** Prices and the code itself.

**EX014.** The leak: security misconfiguration and authentication failures; the hash mismatch: software and data integrity failures.

**EX015.** No; it uses 0.4.2, above the affected range.

**EX016.** 1.4.0, 1.4.7 and 1.10.2.

**EX017.** 1.4.7, because text compares characters, so "1.10" seems lower than "1.4".

**EX018.** Ranges decide which versions may be chosen; lockfiles record the exact version chosen.

**EX019.** Secure: HTTPS only; HttpOnly: not readable by scripts; SameSite: limits cross-site sending.

**EX020.** HttpOnly was missing; it was set and a test added.

**EX021.** It only calls known addresses.

**EX022.** A weakness where one user's input runs as script in another user's browser.

**EX023.** Special characters are encoded so the markup is shown as text.

**EX024.** Two unescaped uses; the review one was a bug and was removed, with a test added.

**EX025.** So later price changes do not alter past orders.

**EX026.** Because % is a wildcard in LIKE, matching anything after "100".

**EX027.** It cannot drop tables or create users.

**EX028.** Systems, time and methods.

**EX029.** Because she had no permission to test it.

**EX030.** Only when needed, and access is logged.

**EX031.** Its own user with no admin rights, writing only to temporary and log folders.

**EX032.** Because malicious packages often act at install time, so isolation limits what scripts reach.

**EX033.** A helper's font download failed and it was replaced with one needing no network.

**EX034.** Precision 0.30 and recall 0.90.

**EX035.** Because real secrets are rare among the commits.

**EX036.** Because missing a real secret is costly.

**EX037.** So CampusEats never handles students' passwords.

**EX038.** Token 1, because its age of 40 minutes exceeds 30.

**EX039.** The server-side session stayed valid; now it is deleted on logout.

**EX040.** It can reveal health conditions or religious beliefs.

**EX041.** Removed it and used server-side counts instead.

**EX042.** No; the token reached only a test environment with synthetic data.

**EX043.** Activity: scanner runs; outcome: secrets reaching the public repository.

**EX044.** Two secrets reached the repository and median fix time was 21 days.

**EX045.** Two experienced members joined that term.

**EX046.** The edge, the application, the data and the pipeline.

**EX047.** The leaked test key could not touch real payments.

**EX048.** A narrow API with its own role, rate limits and logging.

**EX049.** HMAC uses a shared secret, so only holders of the secret can create valid tags.

**EX050.** The signature no longer matched and the message was rejected.

**EX051.** Processed event IDs are stored and repeats ignored.

**EX052.** Do pre-commit secret hooks reduce secrets pushed by student developers?

**EX053.** Detections fell from 5 to 1 per term, and 3 of 14 developers had bypassed the hook.

**EX054.** A reviewed allowlist for known harmless strings.

**EX055.** Application security addresses design and code flaws; supply chain security covers everything that goes into the software and how it reaches users.

**EX056.** That you cannot fully trust code you did not create yourself, even compilers.

**EX057.** Prepare, because there was no onboarding training on secure coding.

**EX058.** Lookalike names, code run during installation and takeovers of existing packages.

**EX059.** Monitor transitive dependencies and update promptly.

**EX060.** Consumers should not assume upstream projects have security processes.

**EX061.** External entity (students), process (web app), data store (database), data flow (payment callback).

**EX062.** Spoofing a payment callback, controlled by HMAC verification.

**EX063.** Build logs sent to a chat channel; secrets were masked and the channel restricted.

**EX064.** pay-client 1.8.0 failed its hash check and installation stopped.

**EX065.** The maintainer had rebuilt and re-uploaded 1.8.0.

**EX066.** Supplier, component name, version and dependency relationship.

**EX067.** 4.86 for the token-like string (likely secret) and 0.00 for the repeated string (ignored).

**EX068.** Revoke or rotate it.

**EX069.** Because copies may already exist elsewhere.

**EX070.** Preventive: lockfile hashes; detective: nightly advisory checks; corrective: rollback.

**EX071.** A high advisory without an exception, a dependency without an owner and an outdated lockfile.

**EX072.** Two advisory blocks, one ownerless dependency and one outdated lockfile.

**EX073.** Content-Security-Policy and Referrer-Policy.

**EX074.** In report-only mode for two weeks, then enforced.

**EX075.** It revealed the software version unnecessarily.

**EX076.** It shows who produced the artifact.

**EX077.** L1: provenance exists; L2: hosted platform signs provenance; L3: hardened platform resists tampering.

**EX078.** A bundle signed by a personal identity was refused.

**EX079.** Because CampusEats handles payments and personal data.

**EX080.** 41 passed, 4 failed and 1 was not applicable out of 46.

**EX081.** The login rate limit and reset link, because of account takeover risk.

**EX082.** To understand how the system allowed the failure, not to blame a person.

**EX083.** No pre-commit hook, the .gitignore mistake and unclear guidance on test keys.

**EX084.** A CI check that fails if any .env file is committed.

**EX085.** Sign-ins, role changes and payment callback verification failures.

**EX086.** High within 7 days, medium within 30.

**EX087.** It was held, an issue opened with maintainers and other updates merged.

**EX088.** SBOM and advisory check, hash verification, signature, provenance and tests.

**EX089.** A medium advisory in a development-only tool, recorded as not applicable.

**EX090.** Automating the report generation.

**EX091.** Replace it, maintain a fixed copy or remove the feature.

**EX092.** It held the update, checked the change and script, asked in the tracker and waited for confirmation.

**EX093.** The flaw needed a rare feature CampusEats does not use, so it was not urgent.

**EX094.** They are flagged automatically and sent to the legal team.

**EX095.** Does it follow the SSDF, and does it provide SBOMs and timely fixes?

**EX096.** Store points totals only, with history deleted after two years.

**EX097.** Team experience.

**EX098.** 6 days with bots, 24 without; kappa 0.82.

**EX099.** Because fix times are skewed.

**EX100.** Fix time, member time, broken builds and satisfaction.

**EX101.** Bot: median 3 days; manual: 16 days.

**EX102.** The bot ran in a quieter period, so she rechecked during exams.

**EX103.** Secret scanning, lockfile hash checks, SBOM generation and an update bot.

**EX104.** At least four projects adopt, zero secrets leak and setup takes under an hour.

**EX105.** A monthly automated job updates and checks it.

**EX106.** Past volunteers with write access, outdated dependencies with advisories and a password in the repository.

**EX107.** She did not access client data and worked only on code and configuration with the coordinator present.

**EX108.** 14 updates merged and access granted only for project duration.

**EX109.** Case collections, large-scale measurement studies and an interview study.

**EX110.** Risk concentrates in widely used packages, updates lag, malicious packages exploit trust and install-time behaviour, and maintainer practices vary.

**EX111.** That the studies focus too much on npm.

**EX112.** CI checks, an update bot configuration, ASVS-based tests and a README.

**EX113.** Setup took 2.5 hours because of signing, and the scanner flagged sample keys in the documentation.

**EX114.** Any logged-in student could cancel another student's booking.

**EX115.** Five projects adopted, no secrets leaked and setup took 40 minutes.

**EX116.** SBOM output was confusing, so a guide was added.

**EX117.** Because the groups may differ in other ways.

**EX118.** It implements SSDF practices across all four groups.

**EX119.** It would need customisation and stronger review, and she suggested a study.

**EX120.** Published under an open licence with synthetic examples, with Grace's approval.

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
