# Authorized Offensive Security and Red Team: A Rapid Introduction

- Language: English (`en`); rapid course, one month; approximately 80 hours of planned study.
- Editorial state: **published**. Chapters 1–20 have hand-written teaching text; exercises EX001–EX066 have matching worked results with 0–3 rubrics; two offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. The rapid planning minimum is 20 lessons and there is no maximum. These twenty lessons meet that minimum. Independent review remains open. Page count is not the writing target. This is not a finished qualification.
- Audience: new learners with no prior security role.
- Relation to neighbouring books: the [professional course book](../../../../professional-6-months/offensive-security-red-team/en/book/MANUSCRIPT.md) develops each topic into practice. **These twenty English lessons introduce authorized testing.** They meet the planning minimum. They are not a finished qualification.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not an accredited qualification. **No authority to test real systems.** All organisations, people and numbers are **synthetic** unless a sentence cites a public source. Labs teach scoping, ranking and reporting — never weaponised techniques.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

<!-- open-cyber-academy:chapter-lessons -->
## How to use this book

Maya Chen is a trainee at the fictional Riverside Civic College. Each numbered chapter is one lesson. Lessons 1–4 remain the published introduction. Lessons 5–20 read the two offline scripts: which branch runs first, where the /25 ends, why the rank key puts F1 ahead of F3, and what the college note may quote. The scripts do not send traffic and do not contain exploit code. Review remains open. Page count is not the writing target.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Riverside Civic College (RCC)** — staff portal, grading system, guest Wi-Fi, documentation-range lab addresses | Organisation studied throughout | Invented |
| **Maya Chen** | IT security trainee at RCC | Invented |

### Core sources

NIST [SP 800-115](https://doi.org/10.6028/NIST.SP.800-115); [PTES](https://pentest-standard.readthedocs.io/en/latest/); MITRE [ATT&CK](https://attack.mitre.org/); OWASP [WSTG](https://owasp.org/www-project-web-security-testing-guide/); [TIBER-EU](https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html); Bank of England [CBEST](https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — What authorized offensive security is

### Learning outcomes

You will (1) define authorized offensive security and red teaming; (2) explain how they differ from crime and from everyday IT work; (3) name the main public frameworks that guide them; and (4) describe who decides when testing is allowed.

### 1.1 Authorized testing, not hacking for thrills

Authorized offensive security means looking for weaknesses in systems with the owner's written permission, for the purpose of making them safer. A red team is a group that simulates a realistic attacker under those same rules. Both are jobs done for a client or for one's own organisation. Breaking into systems without permission is a crime, even if you plan to tell someone afterwards. This course teaches how authorized testing is planned, limited and reported — never how to attack systems you do not own.

### 1.2 Why organisations pay for it

Defenders need to know what an attacker could actually do, not only what a checklist says. NIST SP 800-115 describes several kinds of security testing and assessment, from reviews to technical tests. The Penetration Testing Execution Standard (PTES) organises a pentest into stages such as scoping, intelligence gathering, vulnerability analysis, exploitation, post-exploitation and reporting. Threat-led programmes such as TIBER-EU and CBEST use intelligence to make the test look like a real adversary against financial institutions.

For Riverside Civic College, the value is practical: the outside firm's test of the staff portal will show whether a real attacker could misuse it, and Maya's team will use the report to decide which fixes come first.

### 1.3 What this course will not teach

You will not be given exploit code, payloads or step-by-step attack procedures for real products. Labs use synthetic data and offline scripts. You will learn to check scope, keep evidence, write findings and stay inside the rules.

Instead, the labs are short Python scripts that read local, invented data, such as a target list and four draft findings for Riverside Civic College. You will practise the decisions that keep testing safe and useful: what may be touched, what must be left alone, how serious a finding is and how to tell the people who must act. Those skills are needed before any technical testing is allowed.

### 1.4 Who says yes

Permission comes from someone who owns or is authorised to speak for the system — often a business owner and a security lead, recorded in a signed document. Your manager, a friend or a public website's "report a bug" page is not enough unless the written rules say so. When in doubt, do not test.

At Riverside Civic College, the staff portal test is allowed because the college's portal owner and IT security lead have signed an agreement with the outside firm. Maya's manager cannot add systems to that agreement by asking, and neither can Maya. A bug bounty page counts only for its own published scope and rules. If a system's owner is unclear, find out who it is before anything is tested.

### 1.5 Shared language for techniques

MITRE ATT&CK gives public names for adversary techniques, such as T1078 Valid Accounts. Testers and defenders use those names so a finding and a detection rule describe the same behaviour.

For example, a grading system where several staff share one admin login relates to T1078 Valid Accounts, because anyone with the password acts as a legitimate user and nobody can tell who did what. Maya will use this name in Chapter 3. A name does not score the finding or prove an attack happened; it gives testers and defenders a common reference, so a detection team can look up the technique and check whether they would notice it.

### Worked example (synthetic RCC)

Maya Chen joins Riverside Civic College's IT security team as a trainee. Her manager explains that next month an outside firm will test the college's staff portal under a signed agreement. Maya's job this month is to learn what that agreement means and how the college will prepare, so she can help review the report afterwards.

> **Synthetic case — Riverside Civic College (RCC).** The college, Maya Chen, systems and all figures in this book are invented for teaching.

### Errors and limits

Framework names and editions change; check the current published versions before citing them in real work. This book grants no authority to test any real system.

### Exercises

- **EX001 — Defining the work.** In one sentence, what is authorized offensive security? *Rubric:* 3 = testing with owner's written permission to improve security; 2 = partial; 1 = "hacking"; 0 = none.
- **EX002 — Crime versus job.** Explain the difference between authorized testing and unauthorized access. *Rubric:* 3 = permission vs no permission; legal vs illegal; purpose of improvement; 2 = two; 1 = one; 0 = none.
- **EX003 — Red team in plain words.** What does a red team do that a short vulnerability scan might not? *Rubric:* 3 = simulates a realistic attacker under rules; may chain findings; 2 = partial; 1 = "scans more"; 0 = none.
- **EX004 — NIST SP 800-115.** What kind of document is NIST SP 800-115? *Rubric:* 3 = NIST guide to information security testing and assessment; 2 = "a standard"; 1 = wrong; 0 = none.
- **EX005 — PTES stages.** Name three stages from the Penetration Testing Execution Standard. *Rubric:* 3 = three of scoping, intelligence gathering, vulnerability analysis, exploitation, post-exploitation, reporting; 2 = two; 1 = one; 0 = none.
- **EX006 — TIBER-EU and CBEST.** What do TIBER-EU and CBEST have in common? *Rubric:* 3 = threat-led tests for financial sector, use intelligence, authorized; 2 = two; 1 = one; 0 = none.
- **EX007 — What this course refuses.** Why does this course refuse to share exploit code? *Rubric:* 3 = dual-use / could harm real systems; learning goal is authorized defence improvement; 2 = partial; 1 = "too hard"; 0 = none.
- **EX008 — Who grants permission.** Who can authorize a test of RCC's staff portal? *Rubric:* 3 = the college (owners) via signed agreement, typically business + security leads; 2 = partial; 1 = Maya alone / a friend; 0 = none.
- **EX009 — Bug bounty confusion.** A public website offers a bug bounty. May Maya test it for practice? *Rubric:* 3 = only under that programme's written rules and scope; otherwise no; 2 = partial; 1 = yes freely; 0 = none.
- **EX010 — Maya's role this month.** What is Maya preparing to do after the outside firm's test? *Rubric:* 3 = help review the report; understand the agreement; 2 = one; 1 = run exploits; 0 = none.
- **EX011 — Lab data only.** Where do this course's lab numbers come from? *Rubric:* 3 = synthetic offline data / scripts; no live targets; 2 = partial; 1 = the internet; 0 = none.
- **EX012 — ATT&CK role.** What is MITRE ATT&CK used for in this field? *Rubric:* 3 = shared names for adversary techniques; map findings / plan detection; 2 = partial; 1 = a scanner; 0 = none.
- **EX013 — First rule when unsure.** What should Maya do if she is unsure whether something is in scope? *Rubric:* 3 = do not test; ask the authorizing contact / stop; 2 = ask only; 1 = try carefully; 0 = none.

### Synthesis

Authorized offensive security is permissioned testing done to improve defence; frameworks guide it, and this course stays inside those rules.

<!-- open-cyber-academy:chapter-navigation:start ch-01 -->
### Continue studying — lesson 01 (chapter 01 of 20)

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-02"></a>

## Chapter 2 — Scope, permission and safe practice

### Learning outcomes

You will (1) list what a written authorization must contain; (2) check proposed targets against a scope with a short script; (3) explain stop conditions and out-of-bounds rules; and (4) handle a request that would break the rules.

### 2.1 What the paper must say

Before any testing, a written agreement — sometimes called rules of engagement — must name the systems and people in scope, what is out of scope, which methods are allowed, the start and end times, who to call in an emergency, how findings will be reported, and how data will be handled afterwards. NIST SP 800-115 and PTES both treat scoping as a first-class stage, not a formality.

If any of these items is missing, testing waits until the agreement is corrected and signed again. Maya's classroom pack covers 192.0.2.0/25, excludes the payroll server at 192.0.2.10 and allows only a configuration and policy review.

### 2.2 Checking a target list

Testers compare every proposed address or hostname with the written scope. Excluded systems — payroll, medical devices, safety systems — must never be touched even if they share a network. A simple local check catches mistakes before anyone sends a packet.

```python
"""Lab 2: check synthetic targets against a written scope (no network traffic is sent)."""
import ipaddress
in_scope = [ipaddress.ip_network("192.0.2.0/25")]          # documentation range, synthetic
excluded = {ipaddress.ip_address("192.0.2.10")}             # payroll server: owner excluded it
requested = ["192.0.2.5", "192.0.2.10", "192.0.2.130", "198.51.100.7"]
for t in requested:
    ip = ipaddress.ip_address(t)
    if ip in excluded:
        verdict = "EXCLUDED - do not test"
    elif any(ip in n for n in in_scope):
        verdict = "in scope"
    else:
        verdict = "OUT OF SCOPE - do not test"
    print(f"{t:14} {verdict}")
```

Run with `python3 lab_scope.py`. Verified output:

```text
192.0.2.5      in scope
192.0.2.10     EXCLUDED - do not test
192.0.2.130    OUT OF SCOPE - do not test
198.51.100.7   OUT OF SCOPE - do not test
```

The lab script compares four addresses with one allowed range and one excluded address, and sends no traffic. Only 192.0.2.5 is in scope: 192.0.2.10 is the excluded payroll server, and 192.0.2.130 and 198.51.100.7 fall outside 192.0.2.0/25. Run it whenever the list changes, and keep the output with the plan as a record that the check happened before any work began.

### 2.3 Stop conditions and out of bounds

Stop conditions are events that end or pause testing at once: the owner asks to stop, an unexpected outage appears, safety systems are involved, or sensitive data is exposed beyond the test's purpose. Out-of-bounds rules list methods that are never allowed, such as denial-of-service or social engineering of students, unless the paper explicitly permits them.

When a stop condition occurs, pause at once, contact the emergency contact named in the agreement and write down the time and what you were doing. Testing resumes only when the authorizing contact says so. For Maya's classroom exercise, a slow staff portal test page is enough reason to pause and call.

### 2.4 When someone asks you to break the rules

Colleagues sometimes ask for a "quick check" of a system that is not in scope. The answer is always no until the authorization is changed in writing. Being helpful does not create permission.

If the request is genuine, the person should ask the system's owner to change the agreement in writing. In Maya's exercise, a classmate asks her to add a personal blog, and she refuses: the college's authorization covers only agreed college systems, and pressure or friendship does not change that. Record each refused request, so your manager can see that the rules held.

### Worked example (synthetic RCC)

Maya is given a draft target list for a classroom exercise that uses documentation addresses only: 192.0.2.5, 192.0.2.10 (payroll, excluded), 192.0.2.130 and 198.51.100.7. She runs the check script. Only 192.0.2.5 is in scope; the others are excluded or outside the agreed network. She removes them from the list before any further work.

> **Synthetic case — RCC.** The addresses come from documentation ranges (RFC 5737); the college and exclusions are invented.

### Errors and limits

A script only checks the list you give it; it cannot discover whether the real network matches the paper. Live scanning needs separate, explicit authorization.

### Exercises

- **EX014 — Rules contents.** Name five things a rules-of-engagement document must state. *Rubric:* 3 = five of scope, exclusions, methods, times, contacts, reporting, data handling; 2 = three; 1 = one; 0 = none.
- **EX015 — Payroll exclusion.** Why is 192.0.2.10 marked EXCLUDED even if it sits in the same /25? *Rubric:* 3 = owner excluded it (payroll); scope is not only the network range; 2 = partial; 1 = script bug; 0 = none.
- **EX016 — Out of scope address.** What does the lab print for 198.51.100.7, and what must Maya do? *Rubric:* 3 = OUT OF SCOPE - do not test; remove it and do not contact it; 2 = print only; 1 = test carefully; 0 = none.
- **EX017 — Adding an address.** If Maya adds 192.0.2.20 (not excluded) to `requested`, what should the lab print for it? *Rubric:* 3 = "in scope"; 2 = in scope without format; 1 = OUT OF SCOPE; 0 = none.
- **EX018 — Friend's request.** A classmate asks Maya to "quickly check" their personal blog with the college's scanner. What does she say? *Rubric:* 3 = refuse; no authorization for that system; personal systems out of college scope; 2 = refuse; 1 = do it after hours; 0 = agree.
- **EX019 — Stop conditions.** Give three stop conditions for a test. *Rubric:* 3 = three specific (owner asks stop, unexpected outage, data exposure, safety issue); 2 = two; 1 = one; 0 = none.
- **EX020 — Emergency contact.** Who does Maya call if the staff portal becomes unavailable during a test? *Rubric:* 3 = the emergency contact named in the rules; then stop testing; 2 = partial; 1 = social media; 0 = none.
- **EX021 — Time window.** The rules say testing is allowed 09:00–17:00 weekdays. May the firm start at 20:00 to "avoid users"? *Rubric:* 3 = no; outside agreed window needs written change first; 2 = no; 1 = yes if quieter; 0 = none.
- **EX022 — Data handling.** What should happen to test data after the engagement ends? *Rubric:* 3 = follow the agreement: retain only as allowed, then delete/return; 2 = partial; 1 = keep forever; 0 = none.
- **EX023 — Documentation ranges.** Why does the lab use 192.0.2.0/24 style addresses? *Rubric:* 3 = RFC documentation ranges; safe for examples; not real RCC internet; 2 = partial; 1 = real campus; 0 = none.
- **EX024 — Scope change mid-test.** The firm finds a related server and wants to add it. What is the correct process? *Rubric:* 3 = pause; written scope change from authorizing contact; then resume if approved; 2 = partial; 1 = just add it; 0 = none.
- **EX025 — PTES and scoping.** Where does PTES place scoping among its stages? *Rubric:* 3 = at the beginning / first-class stage before technical work; 2 = "early"; 1 = at the end; 0 = none.
- **EX026 — Safe practice summary.** State the one-line rule Maya writes on her notepad. *Rubric:* 3 = if it is not clearly in the written scope, do not test it; 2 = partial; 1 = scan everything; 0 = none.

### Synthesis

Written scope, exclusions and stop conditions decide every action; anything unclear is out of bounds.

<!-- open-cyber-academy:chapter-navigation:start ch-02 -->
### Continue studying — lesson 02 (chapter 02 of 20)

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-03"></a>

## Chapter 3 — Findings, evidence and responsible reporting

### Learning outcomes

You will (1) describe what makes a useful finding; (2) keep simple evidence without attacking systems; (3) map a finding to an ATT&CK technique name; and (4) write a short, audience-aware report.

### 3.1 What a finding is

A finding is a specific, evidenced weakness or gap that matters to the organisation. It states what was observed, where, when, why it matters, how to reproduce the observation within the rules, and a suggested fix. Vague statements such as "security is weak" are not findings.

For example, Maya's finding F3 states that the grading system uses one shared admin account, so logs cannot show which staff member changed a mark. It names the system, gives the evidence, explains the harm to student records and suggests named accounts as the fix. An owner can check it and act on it.

### 3.2 Evidence without harm

Evidence can be configuration screenshots, log lines, policy excerpts or the output of authorized tools. You keep only what the agreement allows, mark it with time and source, and never share it beyond the agreed audience. This course's labs never touch live targets.

If evidence contains personal data, such as student names in a screenshot, redact them or replace the screenshot with a synthetic sample that still shows the issue. Store evidence where only the agreed people can read it, and delete or return it when the agreement says.

### 3.3 Naming techniques

Linking a finding to MITRE ATT&CK helps defenders search for related detections. For example, a shared password reused across systems relates to T1078 Valid Accounts. The name describes the behaviour; it does not prove who the attacker would be.

Use the technique name as a pointer, not a conclusion. Maya's F3 maps to T1078 because shared credentials let anyone holding them act as a legitimate user without leaving their own name in the logs. Defenders can then check whether their monitoring would notice that behaviour on the grading system. Map a finding only when the behaviour clearly matches.

### 3.4 Honest severity

Severity combines how easy the issue is to use and how much harm it could cause. Industry scores such as CVSS exist, but many organisations also use a simple likelihood × impact scale agreed with the client. Overstating severity destroys trust; understating it leaves risk unaddressed.

Maya's scale multiplies likelihood and impact, each from 1 to 3. F3 scores 2 × 3 = 6: the shared admin account is not trivial to misuse, but altered grades with no accountability would harm students and the college's trust. Use CVSS only if the organisation already does and the scores follow its method.

### 3.5 Who reads the report

Executives need short risk language and decisions; system owners need reproduction steps and fixes; defenders need technique names and detection ideas. One report often has a summary for leaders and detail for engineers.

For F3, Maya writes one paragraph telling the IT director why shared admin access threatens grade integrity, and a fix list telling the application owner to replace the shared login with named accounts and record user identity in the audit log. Detailed evidence sits in an attachment for engineers. Check that every version tells the same facts.

### Worked example (synthetic RCC)

After a synthetic classroom review of RCC policies (no live scan), Maya drafts finding F3: "The grading system uses one shared admin account; logs cannot show which staff member changed a mark." She links it to ATT&CK T1078 Valid Accounts, rates likelihood 2 and impact 3, and writes a one-paragraph summary for the IT director plus a detailed fix list for the application owner.

> **Synthetic case — RCC.** The finding and ratings are invented for the classroom.

### Errors and limits

ATT&CK mappings are aids, not proof of an intrusion. Severity without an agreed scale confuses readers.

### Exercises

- **EX027 — Finding parts.** List five parts of a useful finding. *Rubric:* 3 = what, where, when, why it matters, reproduction within rules, suggested fix; 2 = four; 1 = two; 0 = none.
- **EX028 — Not a finding.** Why is "the network is insecure" a poor finding? *Rubric:* 3 = not specific, no evidence, no location, no fix; 2 = two; 1 = one; 0 = none.
- **EX029 — Evidence examples.** Name three kinds of evidence allowed in a typical authorized test. *Rubric:* 3 = three of screenshots, logs, configs, authorized tool output, policy excerpts; 2 = two; 1 = one; 0 = none.
- **EX030 — ATT&CK for shared admin.** Which ATT&CK technique best fits a shared admin account on the grading system? *Rubric:* 3 = T1078 Valid Accounts; 2 = name only; 1 = wrong; 0 = none.
- **EX031 — Likelihood × impact.** Using Maya's ratings for F3, what is the score and why is impact 3? *Rubric:* 3 = 6; impact high because grade integrity / student records; 2 = score only; 1 = wrong; 0 = none.
- **EX032 — Overstating severity.** What goes wrong if every finding is labelled critical? *Rubric:* 3 = trust collapses; owners cannot prioritise; real criticals ignored; 2 = partial; 1 = vague; 0 = none.
- **EX033 — Two audiences.** Write one sentence for the IT director and one for the application owner about F3. *Rubric:* 3 = director: risk/accountability; owner: shared account, logging, named accounts fix; 2 = one good; 1 = same jargon both; 0 = none.
- **EX034 — Reproduction within rules.** What does "reproduce within the rules" mean? *Rubric:* 3 = steps that stay inside authorization and avoid harm; 2 = partial; 1 = full exploit; 0 = none.
- **EX035 — Data minimisation.** Maya captured a screenshot with three student names visible. What should she do before filing it? *Rubric:* 3 = redact names / use synthetic sample; keep only what agreement allows; 2 = partial; 1 = file as-is; 0 = none.
- **EX036 — OWASP WSTG role.** What is the OWASP Web Security Testing Guide used for? *Rubric:* 3 = structured web testing checks / methodology; 2 = "web list"; 1 = malware; 0 = none.
- **EX037 — Report section order.** In what order should summary, findings and appendices usually appear? *Rubric:* 3 = executive summary, findings, appendices/evidence; 2 = partial; 1 = appendices first; 0 = none.
- **EX038 — No blame language.** Rewrite "the lazy admin reused passwords" into professional finding language. *Rubric:* 3 = describes system condition without insulting people; 2 = partial; 1 = keeps insult; 0 = none.

### Synthesis

Findings are specific, evidenced and mapped to shared technique names; reports tell each audience what to do.

<!-- open-cyber-academy:chapter-navigation:start ch-03 -->
### Continue studying — lesson 03 (chapter 03 of 20)

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-04"></a>

## Chapter 4 — Guided synthesis: plan, check, report

### Learning outcomes

You will (1) combine scope checking and finding ranking into one short exercise; (2) produce a one-page report for RCC; (3) apply stop rules under pressure; and (4) state your next learning step.

### 4.1 The classroom engagement

Maya is given a synthetic engagement pack: a one-page authorization for documentation addresses in 192.0.2.0/25, an exclusion of 192.0.2.10, a list of four draft findings from a policy and configuration review (no live exploitation), and a request for a one-page summary for the IT director.

Before starting, Maya runs the scope check on any address mentioned in the pack, and confirms that her work is limited to the review the authorization permits. The four findings cover reused portal passwords, an old web server banner, a shared grading admin account and guest Wi-Fi reaching a printer admin page. Her output is a ranked list and a one-page summary for the IT director, with evidence attached.

### 4.2 Ranking for the summary

Not every finding fits the first page. Ranking by likelihood × impact puts the issues that most need decisions first.

```python
"""Lab 4: rank synthetic findings by likelihood x impact (1-3 each) for the report summary."""
findings = [("F1", "Staff portal allows reused passwords", 3, 2),
            ("F2", "Old web server banner shows version", 2, 1),
            ("F3", "Shared admin account on grading system", 2, 3),
            ("F4", "Guest Wi-Fi reaches printer admin page", 2, 2)]
for fid, title, lik, imp in sorted(findings, key=lambda f: (-f[2] * f[3], f[0])):
    score = lik * imp
    band = "high" if score >= 6 else "medium" if score >= 4 else "low"
    print(f"{fid} score={score} {band:6} {title}")
```

Run with `python3 lab_findings.py`. Verified output:

```text
F1 score=6 high   Staff portal allows reused passwords
F3 score=6 high   Shared admin account on grading system
F4 score=4 medium Guest Wi-Fi reaches printer admin page
F2 score=2 low    Old web server banner shows version
```

The script multiplies likelihood by impact, sorts by score and breaks ties by finding id. F1 and F3 both score 6 and are high; F4 scores 4 and is medium; F2 scores 2 and is low. The first page gives F1 and F3 most space, and F2 can sit in the attachment, since a version banner alone rarely enables much harm.

### 4.3 Writing the page

The summary states the authorization, the window, how testing was limited (configuration and policy review only), the top findings with scores, and the decisions needed. Detail sits in an attachment.

Maya's page states that the work covered 192.0.2.0/25 except 192.0.2.10, that it was a configuration and policy review with no live exploitation, and that F1 and F3 scored highest. It asks the director to approve named grading accounts and a password-reuse control for the portal within thirty days. Full write-ups, evidence and reproduction steps go in the attachment.

### 4.4 Pressure scenarios

During the exercise a classmate asks Maya to add their blog to the target list, and a draft finding mentions a medical clinic server that is not in the college scope. She refuses the blog and removes the clinic server note as out of scope.

The blog is a personal system outside the college's agreement, and the clinic server belongs to another owner, so even listing it as a target would be improper. Maya records both decisions in her notes. If the portal test page becomes slow during a permitted check, she pauses, calls the emergency contact and records the time.

### 4.5 After the course

The next course in this curriculum is about AI security. Longer red-team courses deepen scoping, methods, tooling, reporting and threat-led testing. Keep a record of exercises completed.

This course gives no authority to test real systems. Before any real engagement you will need further training, supervised practice and, above all, a signed agreement from the system's owner. Maya's next step is to help her team review the outside firm's staff portal report, using the scope, evidence and severity skills from this course.

### 4.6 Recording the exercise

Maya files the one-pager, the ranked list, the scope-check output and a note of the two refused requests. That packet is what her manager reviews, and it becomes her evidence that the classroom engagement stayed inside the rules.

A reviewer should be able to trace each finding on the page back to its evidence, and each address back to the scope-check output. If something is missing, Maya adds it before filing. Keep the packet only for as long as the agreement allows, and store it where only her manager and the team can read it.

### Worked example (synthetic)

Maya's ranked list puts F1 (reused portal passwords) and F3 (shared grading admin) first with score 6, then F4 (guest Wi-Fi to printer admin) at 4, then F2 (banner) at 2. Her one-pager asks the director to approve named accounts for grading and a password-reuse control for the portal within thirty days. She notes that no live exploitation was performed.

> **Synthetic case — RCC.** Findings and scores are invented.

### Errors and limits

A classroom ranking is not a full professional report. Real engagements need the complete authorization trail and technical detail.

### Exercises

- **EX039 — Authorization one-liner.** Write the authorization sentence Maya puts at the top of the page. *Rubric:* 3 = who authorized, what scope, what methods, what window; 2 = three; 1 = one; 0 = none.
- **EX040 — Why F2 is last.** Why does the banner finding rank below password reuse? *Rubric:* 3 = lower likelihood×impact; less harm than credential issues; 2 = partial; 1 = banners always first; 0 = none.
- **EX041 — Lab reorder.** If F4's impact rises to 3, what new order does the lab print? *Rubric:* 3 = F4 rises from 4 to 6 (2 × 3), so F1, F3 and F4 all score 6 and are sorted by id, then F2; 2 = partial; 1 = same; 0 = none.
- **EX042 — Blog request again.** Under time pressure the classmate repeats the blog ask. Maya's answer? *Rubric:* 3 = still refuse; no written authorization; 2 = refuse; 1 = quick scan; 0 = agree.
- **EX043 — Clinic server note.** Why remove the medical clinic server from the draft? *Rubric:* 3 = out of college scope / authorization; possible separate legal duties; 2 = partial; 1 = keep it; 0 = none.
- **EX044 — Decision request.** What decision does Maya ask of the IT director? *Rubric:* 3 = approve named grading accounts and portal password-reuse control within 30 days; 2 = partial; 1 = "fix security"; 0 = none.
- **EX045 — Methods limitation.** Why must the summary say "no live exploitation"? *Rubric:* 3 = honest about methods; reader must not think systems were attacked; matches authorization; 2 = partial; 1 = hide it; 0 = none.
- **EX046 — Evidence attachment.** What goes in the attachment rather than the one-pager? *Rubric:* 3 = detailed reproduction, screenshots/logs, full finding text; 2 = partial; 1 = vague; 0 = none.
- **EX047 — Stop during synthesis.** The portal test page becomes slow during a permitted check. What does Maya do? *Rubric:* 3 = stop / pause; contact emergency contact; record time; 2 = partial; 1 = continue; 0 = none.
- **EX048 — CVSS mention.** When might Maya mention CVSS in a beginner report? *Rubric:* 3 = if the organisation uses it and scores are agreed; else keep simple scale; 2 = partial; 1 = always invent scores; 0 = none.
- **EX049 — Next course.** What does the next course in the curriculum cover? *Rubric:* 3 = AI security (course 020); 2 = vague; 1 = wrong; 0 = none.
- **EX050 — Personal limit.** State one thing Maya still must not do after this course. *Rubric:* 3 = test systems without written authorization / use exploits on real targets; 2 = partial; 1 = anything; 0 = none.

### Synthesis

A short authorized engagement checks scope, ranks real findings and asks for clear decisions — without crossing the rules.

<!-- open-cyber-academy:chapter-navigation:start ch-04 -->
### Continue studying — lesson 04 (chapter 04 of 20)

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-05"></a>

## Chapter 5 — The scope print follows the request list

### Learning outcomes

After this chapter, you should be able to:

1. Name the four strings in `requested`, in the order they are stored.
2. Say why `.10` prints second even though its verdict is a refusal.
3. Refuse a print that leads with the payroll address because it feels more important.

### 5.1 The loop emits `requested`. It does not call `sorted`.

`lab_scope.py` stores four strings. The first is `192.0.2.5`. The second is `192.0.2.10`. The third is `192.0.2.130`. The fourth is `198.51.100.7`. The `for` loop takes them in that stored sequence. Each pass builds one line and prints it before the next pass starts. Nothing in the file sorts those strings, and nothing reorders them after the verdict is chosen.

A refusal is still a line. The payroll address is second in the list, so its refusal is the second line. Putting the two `OUT OF SCOPE` lines first would be a different list. This file does not build that list.

| What chooses the row order | What does not |
|---|---|
| Position in `requested` | The verdict word |
| One forward pass | `sorted` |
| Print during the pass | A severity score |

### 5.2 Worked example

| Offered result | What produced it | Decision |
|---|---|---|
| `.5`, then `.10`, then `.130`, then `198.51.100.7` | The list, top to bottom | Keep |
| Payroll line second, and still a refusal | Position, not importance | Keep |
| "The script printed safe rows first." | No such reorder exists | Refuse |
| "Drop the refused lines so the page looks cleaner." | Those lines are the record | Refuse |

> **Synthetic case.** These four lines are the only scope-lab output.

### Errors and limits

Do not rebuild `requested` so a preferred verdict prints first.

### Apply

- **EX051 — List order.** The print names `.5`, then the payroll address, then `.130`, then `198.51.100.7`. May a preference for "in scope" rows, or a later note, replace that order? *Rubric:* 3 = no; the lines follow `requested`; a refusal still occupies its slot; do not sort the script;; 2 = the four lines stay and the note stays prose;; 1 = one line;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-05 -->
### Continue studying — lesson 05 (chapter 05 of 20)

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-06"></a>

## Chapter 6 — Exclusion is the first branch

### Learning outcomes

After this chapter, you should be able to:

1. Say which test runs first.
2. Explain why membership in the `/25` does not save `.10`.
3. Refuse a reading that calls the exclusion a script bug.

### 6.1 `if` then `elif`. The first true branch wins.

The excluded object is a set with one member, `192.0.2.10`. The allowed object is a list with one network, `192.0.2.0/25`. For each string, `ip_address` builds an address, then the `if` asks whether that address is in the set. Only if that test is false does the `elif` ask whether the address sits in any network in the list.

`192.0.2.10` makes the set test true. Python skips the `elif`. The network object still contains that address; the branch structure is what keeps the verdict at `EXCLUDED - do not test`. Reversing the two tests would be a different program. This file does not reverse them.

| Address | In the set? | In the `/25`? | Branch that runs |
|---|---|---|---|
| `192.0.2.5` | No | Yes | `elif` → `in scope` |
| `192.0.2.10` | Yes | Yes, unused | `if` → `EXCLUDED` |
| `192.0.2.130` | No | No | `else` |
| `198.51.100.7` | No | No | `else` |

### 6.2 Worked example

| Offered claim | What the branch does | Decision |
|---|---|---|
| "Payroll is excluded because the owner said so, and the `if` encodes that." | Set test first | Keep |
| "`.10` is in the range, so the range line should win." | The `elif` does not run | Refuse |
| "The set removes `.10` from the network object." | The network is unchanged | Refuse |

> **Synthetic case.** The payroll server is a label in a comment. The set holds the address.

### Errors and limits

Do not treat "inside the range" as permission when the set test is true.

### Apply

- **EX052 — First branch.** `192.0.2.10` is inside `192.0.2.0/25` and inside the excluded set. Which test decides the printed verdict, and does the other test still get evaluated? *Rubric:* 3 = the set test is first and true; the `elif` is skipped; the verdict is `EXCLUDED - do not test`;; 2 = exclusion wins and the range does not override it;; 1 = one fact;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-06 -->
### Continue studying — lesson 06 (chapter 06 of 20)

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-07"></a>

## Chapter 7 — The /25 ends at .127

### Learning outcomes

After this chapter, you should be able to:

1. Name the first and last addresses of `192.0.2.0/25`.
2. Place `192.0.2.130` in the following block.
3. Refuse the idea that "130 is close, so the lab should have allowed it."

### 7.1 Prefix length is a count of bits, not a guess about nearby hosts.

`ip_network("192.0.2.0/25")` builds one network. A prefix of 25 means the first 25 bits are fixed and the last 7 bits vary. Two to the power 7 is 128, so the object covers `192.0.2.0` through `192.0.2.127` inclusive. The next address, `192.0.2.128`, is the start of `192.0.2.128/25`. `192.0.2.130` is that later block plus two. Membership is false.

The script never prints `.127` or `.128`. Those two addresses are how you check the object, not extra rows in the output. `.5` and `.10` fall inside the 128. `.130` does not. Closeness of the decimal is not the test `ip in n` uses.

| Address | Inside this object? | Why |
|---|---|---|
| `192.0.2.0` | Yes | First address of the object |
| `192.0.2.127` | Yes | Last address of the object |
| `192.0.2.128` | No | First address of the next `/25` |
| `192.0.2.130` | No | Two past that boundary |

### 7.2 Worked example

| Offered claim | Check | Decision |
|---|---|---|
| "`.130` is outside because 130 is greater than 127." | The last address is `.127` | Keep |
| "The script printed a boundary row for `.127`." | No such line exists | Refuse |
| "A `/24` was what the file stored." | The literal is `/25` | Refuse |

> **Synthetic case.** The boundary is a property of the network object. It is not a fifth printed line.

### Errors and limits

Do not widen the literal to a `/24` so `.130` becomes a member.

### Apply

- **EX053 — Block edge.** Where does `192.0.2.0/25` stop, and why is `192.0.2.130` outside it? *Rubric:* 3 = the object holds 128 addresses, `.0` through `.127`; `.128` starts the next block; `.130` is past that edge; the script does not print the edge;; 2 = `.127` is the last member and `.130` is not;; 1 = one address;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-07 -->
### Continue studying — lesson 07 (chapter 07 of 20)

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-08"></a>

## Chapter 8 — A second documentation range is still outside

### Learning outcomes

After this chapter, you should be able to:

1. Say what the script compares `198.51.100.7` against.
2. Explain why "also a documentation address" does not make it in scope.
3. Refuse a print that treats every RFC 5737 address as allowed.

### 8.1 The allowed object is one network. A cousin range is a miss.

`198.51.100.7` parses as an address. It is not in the excluded set. It is also not inside `192.0.2.0/25`, which lives in `192.0.2.0/24`'s neighbourhood, not in `198.51.100.0/24`. Both the passing address and this one come from documentation ranges. The script never asks "is this documentation?" It asks the set, then the network list. The second answer is no, so the `else` assigns `OUT OF SCOPE - do not test`.

Maya's pack uses documentation addresses so a classroom example cannot be mistaken for a campus she can reach. That reason does not enlarge the network object. An address can be safe to write down and still be a forbidden target.

| Question the script asks | `192.0.2.5` | `198.51.100.7` |
|---|---|---|
| In the excluded set? | No | No |
| In `192.0.2.0/25`? | Yes | No |
| Printed verdict | `in scope` | `OUT OF SCOPE - do not test` |

### 8.2 Worked example

| Offered claim | What was tested | Decision |
|---|---|---|
| "Same RFC family, therefore allowed." | Family is not the predicate | Refuse |
| "The fourth line is a miss on the network test." | `else` after two false tests | Keep |
| "The script looked up a host name." | No name is stored | Refuse |

> **Synthetic case.** `198.51.100.7` is a string in `requested`. It is not a host the script contacts.

### Errors and limits

Do not add `198.51.100.0/24` to `in_scope` to make the fourth line pass.

### Apply

- **EX054 — Cousin range.** Why does `198.51.100.7` print `OUT OF SCOPE - do not test` even though it is a documentation address, like `192.0.2.5`? *Rubric:* 3 = the predicate is the excluded set, then `192.0.2.0/25`; this address fails both; documentation status is not a test;; 2 = it is outside the one allowed network;; 1 = one label;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-08 -->
### Continue studying — lesson 08 (chapter 08 of 20)

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 →](#ch-09)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-09"></a>

## Chapter 9 — Width 14 does not edit the address

### Learning outcomes

After this chapter, you should be able to:

1. Say what `{t:14}` changes on the line.
2. Count the characters in `192.0.2.130` before padding.
3. Refuse a reading that treats the spaces as part of the address.

### 9.1 The format width is a column. The address object is already built.

Each pass prints `f"{t:14} {verdict}"`. For a string, `:14` means a width of at least 14, aligned to the left. `192.0.2.5` has 9 characters, so five spaces follow it inside the field. `192.0.2.10` has 10. `192.0.2.130` has 11. `198.51.100.7` has 12. A further space, the one written between the field and `{verdict}`, separates the column from the words.

Those spaces are not fed back into `ip_address`. The membership tests used the original string. Changing the 14 would move the verdict column. It would not move `.130` into the network, and it would not take `.10` out of the set.

| String | Characters before padding | What the width adds |
|---|---:|---|
| `192.0.2.5` | 9 | Spaces to reach 14 |
| `192.0.2.10` | 10 | Spaces to reach 14 |
| `192.0.2.130` | 11 | Spaces to reach 14 |
| `198.51.100.7` | 12 | Spaces to reach 14 |

### 9.2 Worked example

| Offered claim | What the format did | Decision |
|---|---|---|
| "The gaps line the verdicts up." | Left pad to 14, then one space | Keep |
| "The address grew extra zero digits." | Only spaces were added | Refuse |
| "A shorter field would have changed `EXCLUDED`." | The word was chosen earlier | Refuse |

> **Synthetic case.** Width 14 is presentation. The four verdicts were already chosen.

### Errors and limits

Do not read a space in the column as a digit of the address.

### Apply

- **EX055 — Column width.** What does `{t:14}` change, and what does it leave alone? *Rubric:* 3 = it pads each stored string out to 14 characters with spaces; the address tested by `ip_address` is unchanged; the verdict word is unchanged;; 2 = the spaces are padding and not a new address;; 1 = one fact;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-09 -->
### Continue studying — lesson 09 (chapter 09 of 20)

[← Chapter 08](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 →](#ch-10)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-10"></a>

## Chapter 10 — The else branch sends nothing

### Learning outcomes

After this chapter, you should be able to:

1. Name the only import.
2. Say which two lines come from the `else`.
3. Refuse a claim that the script probed those addresses.

### 10.1 A verdict string is not a packet.

The file imports `ipaddress` and nothing else. `ip_address` and `ip_network` parse text into objects in memory. The `else` stores the words `OUT OF SCOPE - do not test` and the `print` writes them. There is no socket, no name lookup, and no connection. The comment at the top says no network traffic is sent. The branch structure agrees with that comment: every path ends at `print`.

Two of the four lines take the `else`. That means the branch is used. It is not a leftover. Using it still does not contact `192.0.2.130` or `198.51.100.7`. A later reader who "finishes the lab" by reaching those addresses has left the file.

| Path | Lines that take it | Leaves the machine? |
|---|---|---|
| `if` excluded | The payroll line | No |
| `elif` in network | The `.5` line | No |
| `else` | `.130` and `198.51.100.7` | No |

### 10.2 Worked example

| Offered claim | What the file contains | Decision |
|---|---|---|
| "The miss lines are local prints." | `print` of a string | Keep |
| "The else is dead, so those rows were typed by hand." | Two inputs take it | Refuse |
| "Out of scope means the script checked the host and found it down." | No such check | Refuse |

> **Synthetic case.** The classroom pack never leaves the interpreter.

### Errors and limits

Do not add a network call so the refusal "really" checks a host.

### Apply

- **EX056 — No packet.** Which import does the scope script use, which lines take the `else`, and does that branch contact a host? *Rubric:* 3 = `ipaddress` only; `.130` and `198.51.100.7` take the `else`; the branch prints and does not contact a host;; 2 = the miss lines are prints and no packet is sent;; 1 = one fact;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-10 -->
### Continue studying — lesson 10 (chapter 10 of 20)

[← Chapter 09](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 →](#ch-11)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-11"></a>

## Chapter 11 — The rank key is a pair

### Learning outcomes

After this chapter, you should be able to:

1. Name the two parts of the sort key.
2. Say which tuple indexes supply the product.
3. Refuse a sort that uses the title text.

### 11.1 Unary minus on the product, then the id string.

Each finding is `(id, title, likelihood, impact)`. `sorted` receives `key=lambda f: (-f[2] * f[3], f[0])`. Index 2 is likelihood. Index 3 is impact. Their product is the score. The unary minus makes a larger product sort first, because `-6` is less than `-4`, and `sorted` goes low to high. The second key component is `f[0]`, the id, with no minus, so ids go in ordinary string order when products match.

The title sits at index 1. The key never reads it. "Staff portal" does not outrank "Shared admin" because of those words. The printed order of this file is F1, F3, F4, F2, which is the order of the four keys `(-6, "F1")`, `(-6, "F3")`, `(-4, "F4")`, `(-2, "F2")`.

| Id | Likelihood | Impact | Key |
|---|---:|---:|---|
| F1 | 3 | 2 | `(-6, "F1")` |
| F3 | 2 | 3 | `(-6, "F3")` |
| F4 | 2 | 2 | `(-4, "F4")` |
| F2 | 2 | 1 | `(-2, "F2")` |

### 11.2 Worked example

| Offered claim | What the lambda reads | Decision |
|---|---|---|
| "High products first, and the minus is why." | `-f[2] * f[3]` | Keep |
| "The title's topic sets the order." | Index 1 is unread by the key | Refuse |
| "F2 is last because it was typed last." | F2 is second in the list and last in the print | Refuse |

> **Synthetic case.** The four tuples are the whole ranking input.

### Errors and limits

Do not sort on the title when the lambda does not read it.

### Apply

- **EX057 — Key pair.** What does the ranking lambda return, and which part of the tuple does it ignore? *Rubric:* 3 = it returns the negated product of indexes 2 and 3, then the id; the title is not in the key;; 2 = score descending, then id; title unused;; 1 = one fact;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-11 -->
### Continue studying — lesson 11 (chapter 11 of 20)

[← Chapter 10](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 →](#ch-12)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-12"></a>

## Chapter 12 — A tie uses the id, and F2 still finishes last

### Learning outcomes

After this chapter, you should be able to:

1. Say why F1 prints before F3.
2. Say where F2 sat in the original list.
3. Refuse a claim that the print kept written order.

### 12.1 `"F1" < "F3"`. That comparison is the tie. F2 is a different product.

F1 and F3 both produce 6. Their keys are `(-6, "F1")` and `(-6, "F3")`. The first components match, so `sorted` compares the strings. `"F1"` is less than `"F3"`, so F1 comes first. This list has no `F10`. A longer id would be a different string comparison, and this file does not contain one.

F2 is the second tuple in the source and the last line of the print. Written order would have been F1, F2, F3, F4. The print is F1, F3, F4, F2. Those sequences differ at the second line. Quoting the print as "the order Maya typed" would hide the sort.

The id tie happens to agree with F1 appearing before F3 in the source. Agreement is not the mechanism. The mechanism is the second component of the key. Removing that component would make this a different program, even if one run still looked the same.

| Position | Written tuple | Printed line |
|---|---|---|
| First | F1 | F1 |
| Second | F2 | F3 |
| Third | F3 | F4 |
| Fourth | F4 | F2 |

### 12.2 Worked example

| Offered claim | Comparison | Decision |
|---|---|---|
| "F1 before F3 because the id string says so." | `"F1" < "F3"` | Keep |
| "The print matches the source line for line." | Second lines differ | Refuse |
| "F2 finishes last because its title is dull." | Product 2 is the cause | Refuse |

> **Synthetic case.** Four ids, one tie, one reordered tail.

### Errors and limits

Do not invent an id such as F10 and treat it as part of this print.

### Apply

- **EX058 — Tie and tail.** Why does F1 print before F3, and why is F2 last even though it was typed second? *Rubric:* 3 = the shared product defers to the id string, and `"F1"` precedes `"F3"`; F2's product is 2, so its key sorts last; written order is not the print;; 2 = id breaks the tie and the low product finishes last;; 1 = one id;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-12 -->
### Continue studying — lesson 12 (chapter 12 of 20)

[← Chapter 11](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 →](#ch-13)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-13"></a>

## Chapter 13 — Six is high and four is medium

### Learning outcomes

After this chapter, you should be able to:

1. State the two thresholds.
2. Place each printed score in its band.
3. Refuse a band the file does not compute for a score it does not hold.

### 13.1 The band is computed. `medium` already fills the width.

After the sort, the loop sets `score = lik * imp` again and then chooses a word. `score >= 6` yields `high`. Otherwise `score >= 4` yields `medium`. Otherwise the word is `low`. The tests are inclusive. Six is not "almost high." Four is not low.

This print contains 6, 6, 4, and 2. It does not contain 5, 3, or 9. A 5 would be medium and a 3 would be low, but saying the lab printed those bands would add rows. The format `{band:6}` asks for a width of 6. `medium` is already six letters, so it receives no extra pad. `high` is four letters, so two spaces are added inside the field before the separator space. `low` is three letters, so three spaces are added. The pad is not a second score.

| Score in this print | Test that matches | Word |
|---:|---|---|
| 6 | `>= 6` | `high` |
| 4 | not `>= 6`, then `>= 4` | `medium` |
| 2 | neither test | `low` |

### 13.2 Worked example

| Offered claim | Threshold | Decision |
|---|---|---|
| "F4 is medium because 4 meets the second test." | `>= 4` after `>= 6` failed | Keep |
| "High starts above 6, so F1 is medium." | 6 passes the first test | Refuse |
| "The lab printed a score of 9." | No tuple multiplies to 9 | Refuse |

> **Synthetic case.** Four products, three words, no extra row.

### Errors and limits

Do not lower the 6 so that F1 and F3 become medium.

### Apply

- **EX059 — Bands.** Which scores in this print are high, medium, and low, and what would a 5 be if it existed? *Rubric:* 3 = 6 is high, 4 is medium, 2 is low; a 5 would be medium because it fails `>= 6` and meets `>= 4`; this print has no 5;; 2 = the three printed bands are right and no extra score is claimed;; 1 = one band;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-13 -->
### Continue studying — lesson 13 (chapter 13 of 20)

[← Chapter 12](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 →](#ch-14)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-14"></a>

## Chapter 14 — F2 is the product two times one

### Learning outcomes

After this chapter, you should be able to:

1. Multiply F2's two ratings.
2. Say why that product is `low`.
3. Refuse a reading that treats the banner words as the score.

### 14.1 Index 2 is 2. Index 3 is 1. The product is the whole score.

F2's tuple is `("F2", "Old web server banner shows version", 2, 1)`. Likelihood 2 times impact 1 is 2. Two fails both `>= 6` and `>= 4`, so the word is `low`. The key `(-2, "F2")` is the greatest of the four first-components once the minus is applied, meaning it sorts last. The title is evidence language for the page. It is not an integer, and the lambda does not parse it.

A version banner can still matter to an owner. This script does not measure that. It multiplies the two ratings Maya stored. Changing the title without changing `2, 1` would leave the line's score and band alone.

| Field | F2's value | Used in the product? |
|---|---|---|
| Id | F2 | Only as the tie key |
| Title | Old web server banner shows version | No |
| Likelihood | 2 | Yes |
| Impact | 1 | Yes |

### 14.2 Worked example

| Offered claim | Arithmetic | Decision |
|---|---|---|
| "Score 2, band low, last line." | `2 * 1`, then the thresholds, then the key | Keep |
| "The word banner lowers the score by itself." | The integers are the product | Refuse |
| "F2 is medium because 2 is a small high." | 2 fails `>= 4` | Refuse |

> **Synthetic case.** F2 is one tuple. Its harm is not re-scored in the script.

### Errors and limits

Do not edit F2's title and expect the product to move.

### Apply

- **EX060 — Product two.** How does F2 arrive at score 2 and the word `low`? *Rubric:* 3 = likelihood 2 times impact 1 is 2; 2 fails both thresholds, so the word is `low`; the title is not the arithmetic;; 2 = the product is 2 and the band is low;; 1 = one number;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-14 -->
### Continue studying — lesson 14 (chapter 14 of 20)

[← Chapter 13](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 →](#ch-15)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-15"></a>

## Chapter 15 — A changed impact is not this print

### Learning outcomes

After this chapter, you should be able to:

1. Read F4's impact from the tuple that was actually sorted.
2. Compute the product if that impact were 3.
3. Refuse to replace the embedded print with the hypothetical.

### 15.1 Impact 2 is what `sorted` saw. Impact 3 is a different key.

The stored F4 tuple ends in `2, 2`. Likelihood 2 times impact 2 is 4. The key is `(-4, "F4")`, which sits between the sixes and F2. The third printed line is that result: `F4 score=4 medium`.

If the last integer were 3, the product would be 6 and the key would be `(-6, "F4")`. Three keys would then start with `-6`, and the id strings would order them F1, F3, F4, with F2 still last on product 2. That order is a calculation about a tuple this file does not hold. Pasting it under the lab's output fence would report a run that did not happen.

| | Impact stored | Product | Place in the embedded print |
|---|---:|---:|---|
| F4 as written | 2 | 4 | Third line |
| F4 with the last integer replaced by 3 | 3 | 6 | Not a line in this file |

### 15.2 Worked example

| Offered page | Matches the file? | Decision |
|---|---|---|
| F4 on the third line at score 4 | Yes | Keep |
| "F4 now ties the sixes, so quote that as the lab." | The file was not edited | Refuse |
| "Delete F4 from the list so the tie goes away." | The tuple stays | Refuse |

> **Synthetic case.** One ranking print. The alternate impact stays in the notebook.

### Errors and limits

Do not overwrite the embedded F4 line with the alternate product.

### Apply

- **EX061 — Unprinted change.** What does this file print for F4, and where would F4 sit if its impact were 3? *Rubric:* 3 = the file prints score 4 in third place; impact 3 would make product 6 and the id order would be F1, F3, F4, then F2; that order is not the embedded print;; 2 = score 4 is the print and the alternate is not;; 1 = one score;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-15 -->
### Continue studying — lesson 15 (chapter 15 of 20)

[← Chapter 14](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 →](#ch-16)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-16"></a>

## Chapter 16 — Thirty days is a sentence, not a column

### Learning outcomes

After this chapter, you should be able to:

1. Name the two decisions the one-pager asks for.
2. Say where "thirty days" is stored.
3. Refuse a lab line that shows a deadline.

### 16.1 The scripts rank and classify. The page asks for two decisions.

F1 is the reused-password row at score 6. F3 is the shared grading admin row at score 6. Maya's one-pager asks the IT director to approve named accounts for the grading system and a control against password reuse on the staff portal, and it gives those decisions thirty days. That sentence is part of the written page. `lab_scope.py` has no finding tuples. `lab_findings.py` prints id, score, band, and title. Neither format string contains a day count.

The attachment can hold the longer write-up. The scripts do not build that attachment. Calling the college finished because two highs were named would go past both the print and the page. The page asks for decisions. It does not record that the decisions were carried out.

| Item | Where it lives | Printed by a lab? |
|---|---|---|
| F1 and F3 at score 6 | Ranking print | Yes |
| Named grading accounts | One-pager | No |
| Portal password-reuse control | One-pager | No |
| Thirty days | One-pager | No |

### 16.2 Worked example

| Offered sentence | Source | Decision |
|---|---|---|
| "The page asks for two approvals inside thirty days." | The written summary | Keep |
| "The ranking print includes `days=30`." | No such field | Refuse |
| "Naming the highs means the fixes are done." | The page is a request | Refuse |

> **Synthetic case.** Thirty days is a deadline in prose. It is not a measured duration from a clock in the script.

### Errors and limits

Do not insert `30` into either lab's format string.

### Apply

- **EX062 — Deadline.** What two decisions does the one-pager request, and does either lab print the thirty-day figure? *Rubric:* 3 = named grading accounts and a portal password-reuse control; the figure is prose; neither script prints it;; 2 = both decisions are named and the labs do not print the figure;; 1 = one decision;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-16 -->
### Continue studying — lesson 16 (chapter 16 of 20)

[← Chapter 15](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 →](#ch-17)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-17"></a>

## Chapter 17 — Two refusals are outside both prints

### Learning outcomes

After this chapter, you should be able to:

1. Name the two things Maya turns away.
2. Say why neither one is a row in the scope print.
3. Refuse a page that adds either target to `requested`.

### 17.1 The blog and the clinic are notes. They are not elements of either list.

A classmate, who is not given a name in this book, asks Maya to put a personal blog on the target list. She refuses. A draft finding mentions a medical clinic server that is not a college system. She takes that note out. Both decisions go into the packet her manager reviews. The classmate's name, the blog's name, and the clinic's name are not in the file, and this chapter does not invent them.

`requested` holds four addresses. None of them is a blog. `findings` holds F1 through F4. None of them is a clinic. Pressure does not append a fifth string. Listing the clinic "just as a note" would still put another owner's system into the college packet as if it were a target. The recorded act is removal, not a new scope line.

| Item | In `requested`? | In `findings`? | What Maya records |
|---|---|---|---|
| Personal blog | No | No | Refusal |
| Clinic server | No | No | Removal of the note |
| `192.0.2.5` | Yes | No | The scope line |
| F3 | No | Yes | The rank line |

### 17.2 Worked example

| Offered addition | In either script? | Decision |
|---|---|---|
| "Two refusals sit in the packet, beside the prints." | The prints stay four and four | Keep |
| "Add the blog as `198.51.100.7`." | That address is already a different row | Refuse |
| "The clinic is F2." | F2 is the banner tuple | Refuse |

> **Synthetic case.** The classmate stays unnamed. The clinic stays an out-of-scope note.

### Errors and limits

Do not invent a blog host name or a clinic address and call it lab output.

### Apply

- **EX063 — Two nos.** What does Maya refuse, what does she remove, and which script prints either one? *Rubric:* 3 = she refuses the unnamed classmate's blog and removes the clinic note; neither item is in `requested` or `findings`; neither script prints it;; 2 = both decisions stay outside the two prints;; 1 = one decision;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-17 -->
### Continue studying — lesson 17 (chapter 17 of 20)

[← Chapter 16](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 →](#ch-18)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-18"></a>

## Chapter 18 — Two calendars are not lab columns

### Learning outcomes

After this chapter, you should be able to:

1. Keep the October dates and the weekday hours as two different rules.
2. Say that neither rule is a lab column.
3. Refuse a print that shows a clock the file does not store.

### 18.1 One sentence names five dates. Another sentence names a daily window. The scripts name neither.

The authorization sentence Maya is asked to write names a configuration and policy review of `192.0.2.0/25`, excluding `192.0.2.10`, during 12–16 October 2026, with no live exploitation. A separate rule says testing is allowed from 09:00 to 17:00 on weekdays, and that 20:00 is outside that window until the paper changes. Those are two constraints. The October span says which civil dates were agreed. The clock span says which hours inside a day were agreed. Neither constraint is computed by `ipaddress` or by `sorted`.

A slow staff-portal page is a reason to pause and call the emergency contact. This book does not give that contact a name, a phone number, or a clock time for the pause. Adding any of those would invent a measurement. The scripts print addresses and findings only.

| Rule | What it constrains | Printed by either lab? |
|---|---|---|
| 12–16 October 2026 | The agreed dates | No |
| 09:00–17:00 weekdays | The agreed hours | No |
| Pause if the portal page slows | A stop condition | No |

### 18.2 Worked example

| Offered line | Stored in a script? | Decision |
|---|---|---|
| "Dates and hours stay in the prose rules." | No time field | Keep |
| "The scope print ends with `09:00`." | The fourth line is an address | Refuse |
| "The pause happened at a stated minute." | No minute is recorded | Refuse |

> **Synthetic case.** Two calendars, zero time columns.

### Errors and limits

Do not invent a phone number or a minute for the pause.

### Apply

- **EX064 — Calendars.** What do 12–16 October 2026 and 09:00–17:00 each constrain, and does either lab print them? *Rubric:* 3 = the dates are the agreed span and the hours are the daily window; they are different rules; neither script prints a date or a clock;; 2 = both stay prose and the labs print neither;; 1 = one rule;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-18 -->
### Continue studying — lesson 18 (chapter 18 of 20)

[← Chapter 17](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 →](#ch-19)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-19"></a>

## Chapter 19 — T1078 does not multiply

### Learning outcomes

After this chapter, you should be able to:

1. Say which finding the technique name is attached to.
2. Show that the product uses 2 and 3.
3. Refuse to treat the technique id as proof or as a score.

### 19.1 The name sits in the paragraph. The integers sit in the tuple.

F3 is the shared admin account on the grading system. The prose links that condition to T1078 Valid Accounts, because a shared credential lets a person act as a legitimate user without a separate name in the log. The tuple does not store `T1078`. It stores likelihood 2 and impact 3. The product is 6, from those two integers. The ranking lambda cannot see a technique id that is not in the tuple, so renaming the technique would not move F3 relative to F1.

The name is also not evidence that an intrusion occurred. It gives the detection team a public label to look up. Maya can write the label beside the finding. She cannot write it into the score, and she cannot treat it as a procedure for using the shared account. This course does not supply that procedure.

| Object | Holds T1078? | Holds the product? |
|---|---|---|
| The F3 paragraph | Yes, as a name | No |
| The F3 tuple | No | Yes, as 2 × 3 |
| The sort key | No | Yes, as `-6` and then the id |

### 19.2 Worked example

| Offered claim | Where the fact lives | Decision |
|---|---|---|
| "T1078 labels F3. The score is still 2 × 3." | Paragraph versus tuple | Keep |
| "The technique id is why F3 scores 6." | The integers are why | Refuse |
| "The label proves someone broke in." | A label is not an event | Refuse |

> **Synthetic case.** One technique name, one product, no attack steps.

### Errors and limits

Do not turn T1078 into a score or into a way to use the shared account.

### Apply

- **EX065 — Name versus product.** What does T1078 do for F3, and what does it not do to the ranking? *Rubric:* 3 = it names the shared-account behaviour; the product remains 2 × 3; the id is not in the tuple and is not proof of an intrusion;; 2 = the name and the product stay separate;; 1 = one label;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-19 -->
### Continue studying — lesson 19 (chapter 19 of 20)

[← Chapter 18](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 →](#ch-20)

Continue to the next authored lesson.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="ch-20"></a>

## Chapter 20 — What the college note can say

### Learning outcomes

After this chapter, you should be able to:

1. Quote the scope print and the rank print without rearranging them.
2. Keep the deadline, the refusals, and the calendars out of those prints.
3. Reject a note that calls Riverside Civic College finished.

### 20.1 The note's permission is the two prints, plus the rules that were written beside them.

The scope print is four lines, in list order: `192.0.2.5` in scope, `192.0.2.10` excluded, `192.0.2.130` out of scope, and `198.51.100.7` out of scope. The rank print is F1 at 6 high, F3 at 6 high, F4 at 4 medium, and F2 at 2 low. Those lines are what the scripts emitted. A note can quote them.

Beside the prints, the note can say that the set test runs before the network test, that `192.0.2.0/25` ends at `.127`, that thirty days is a sentence on the one-pager, that the blog was refused and the clinic note was removed, and that 12–16 October 2026 and 09:00–17:00 are rules rather than columns. It can say the work was a configuration and policy review. It cannot say a packet was sent, a password was recovered, or an exploit was run. No script in this book does those things.

`hiagokinlevi/offensive-gvuln` is supplementary reading and was not a control either script measured. Authorized offensive security stays this course. AI and machine-learning security is the learner's following subject, and that subject is not started here.

| The note may quote | The note may not add |
|---|---|
| Both embedded prints | A reordered scope list |
| F4 at score 4 | The alternate impact as if it had printed |
| Two refusals, as prose | A blog host or a clinic address |
| Thirty days, as prose | `days=30` inside a lab line |
| T1078 as a name for F3 | A procedure for using the account |

### 20.2 Worked example

| Sentence in the note | Allowed? | Why |
|---|---|---|
| The four scope lines, copied in order | Yes | That is the print |
| F1 before F3, then F4, then F2 | Yes | That is the other print |
| "Payroll was tested because it shares the range." | No | The first branch refused it |
| "The college is secure, and this course awards a credential." | No | The review is open |

> **Synthetic case.** Riverside Civic College and Maya Chen remain invented. The packet is a classroom record.

### Errors and limits

These chapters do not call Riverside Civic College finished, and they do not award a credential. Twenty English lessons meet the college's planning minimum and leave this review open. These English chapters do not publish another language edition. A fresh classroom-packet question can still earn its own later college lesson.

### Apply

- **EX066 — The note.** Which sentences may the college note contain, and which must it reject? *Rubric:* 3 = keep both prints, the first-branch exclusion, the `/25` edge, and the prose for the deadline, the two refusals, and the two calendars; reject a sent packet, the alternate F4 print, a password, a phone number, and a secure or credential claim;; 2 = both prints stay and the false claims stay out;; 1 = one print;; 0 = none.

<!-- open-cyber-academy:chapter-navigation:start ch-20 -->
### Continue studying — lesson 20 (chapter 20 of 20)

[← Chapter 19](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

The chapter index leads to the next course in the study path.
<!-- open-cyber-academy:chapter-navigation:end -->

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX066. Riverside Civic College, Maya Chen and all figures are synthetic. Any answer meeting the rubric scores equally.

**EX001.** Authorized offensive security is looking for weaknesses in systems with the owner's written permission, so the organisation can fix them.

**EX002.** Authorized testing has written permission and a defined purpose of improving security; unauthorized access lacks that permission and is illegal regardless of intent.

**EX003.** A red team tries to act like a real attacker within agreed rules, often chaining weaknesses and testing detection and response, not only listing known software flaws.

**EX004.** It is NIST's Technical Guide to Information Security Testing and Assessment — a public guide that describes types of testing and how to plan them.

**EX005.** Scoping, intelligence gathering and reporting (vulnerability analysis, exploitation and post-exploitation are also stages).

**EX006.** Both are threat intelligence-led assessment frameworks used mainly for financial institutions; tests are authorized and shaped by realistic adversary intelligence.

**EX007.** Exploit code can be used against real systems without permission, which is illegal and harmful; the course teaches authorized testing and reporting, which does not need attack payloads.

**EX008.** Riverside Civic College itself, through people authorised to speak for the system — typically the business owner of the portal and the security lead — in a signed agreement.

**EX009.** Only if she follows that programme's published rules and stays inside its scope; outside those rules she has no permission.

**EX010.** Understand the signed agreement and help her team review the firm's report afterwards — not perform the offensive testing herself yet.

**EX011.** From synthetic data processed by offline Python scripts; no live systems are scanned or attacked.

**EX012.** It is a public knowledge base of adversary techniques with shared names, used to describe what an attacker did or might do and to plan detections.

**EX013.** Stop and do not test; ask the person named in the authorization until the answer is clear.

**EX014.** In-scope systems, out-of-scope systems, allowed methods, start and end times, emergency contacts, how findings will be reported, and how data will be handled.

**EX015.** The owner explicitly excluded the payroll server; being inside the network range does not override a written exclusion.

**EX016.** `198.51.100.7 OUT OF SCOPE - do not test` — she removes it from the plan and never sends traffic to it.

**EX017.** `192.0.2.20 in scope` because it lies in 192.0.2.0/25 and is not on the excluded list.

**EX018.** Refuse: the college's authorization and tools cover only agreed college systems; testing a personal blog with them would be unauthorized.

**EX019.** Stop if the owner or emergency contact asks; stop if a service outage appears that may be caused by testing; stop if sensitive personal data appears in a place it should not.

**EX020.** The emergency contact named in the rules of engagement, and she stops testing until told otherwise.

**EX021.** No. Changing the window needs a written change to the authorization before any out-of-hours testing.

**EX022.** It is retained only for the period and purposes written in the agreement, then deleted or returned as that document requires.

**EX023.** They are reserved documentation addresses (RFC 5737), so examples cannot be mistaken for a real attack on someone's network.

**EX024.** Pause testing of that target, request a written scope change from the authorizing contact, and continue only if approval is recorded.

**EX025.** Scoping is an early, first-class stage; technical testing follows only after scope and rules are agreed.

**EX026.** If it is not clearly in the written scope, do not test it.

**EX027.** What was observed, where, when, why it matters, how to reproduce it within the rules, and a suggested fix.

**EX028.** It names no system, gives no evidence, and suggests no action, so owners cannot verify or fix anything.

**EX029.** Configuration screenshots, application log lines, and authorized tool output (policy excerpts and hashed file samples are also common).

**EX030.** T1078 Valid Accounts — legitimate credentials used in a way that hides individual responsibility and aids misuse.

**EX031.** Score 6 (2×3). Impact is high because altered grades and lost accountability affect student records and trust.

**EX032.** Readers stop trusting the report, cannot prioritise work, and may ignore the few issues that truly need immediate action.

**EX033.** Director: "A shared admin account means we cannot tell who changed grades, which risks academic integrity." Owner: "Replace the shared admin login with named accounts and ensure the audit log records user identity on every mark change."

**EX034.** Describe how to observe the issue using only methods and targets the authorization allows, without causing damage or going out of scope.

**EX035.** Redact the names or replace the screenshot with a synthetic sample so the evidence shows the issue without exposing student personal data.

**EX036.** It is a public methodology of checks for testing web applications in a structured, repeatable way.

**EX037.** A short executive summary, then the findings with severity and fixes, then appendices with detailed evidence.

**EX038.** "Multiple systems accept the same privileged password, so a single compromise grants broad access; individual accountability for changes is not available."

**EX039.** "Authorized by RCC (portal owner and IT security lead) for a configuration and policy review of 192.0.2.0/25 excluding 192.0.2.10, 12–16 October 2026, no live exploitation."

**EX040.** Its score is 2 against 6 for credential issues; a version banner alone rarely enables the same harm as reused or shared privileged passwords.

**EX041.** With F4's impact changed from 2 to 3 (the lab as printed gives F4 score=4), the output becomes F1 score=6, F3 score=6, F4 score=6, F2 score=2 — with equal scores the lab sorts by finding id, so F1, F3, F4, then F2.

**EX042.** Still refuse; pressure does not create permission, and college tools must not touch personal systems.

**EX043.** It is outside RCC's authorization; testing or even listing it as a target without its owner's permission is improper.

**EX044.** Approve replacing the shared grading admin with named accounts and implementing a control against password reuse on the staff portal within thirty days.

**EX045.** So readers know the work stayed inside the agreed methods and do not assume a full attack simulation was performed.

**EX046.** Full finding write-ups, evidence screenshots or log excerpts, and reproduction steps for system owners.

**EX047.** Pause the check, contact the emergency contact named in the rules, and record the time and what she was doing.

**EX048.** Only if RCC uses CVSS and the scores follow that method; otherwise the agreed likelihood × impact scale is clearer for a one-pager.

**EX049.** Course 020: AI security.

**EX050.** She must not test any real system without written authorization, and she must not use exploit code against systems she does not own.

**EX051.** No. The four lines follow `requested`. The payroll refusal stays in the second slot. A later note does not sort the script.

**EX052.** The set test is first and true, so the `elif` does not run. The verdict is `EXCLUDED - do not test`. The network object still contains the address.

**EX053.** The object holds 128 addresses, from `192.0.2.0` through `192.0.2.127`. `192.0.2.128` starts the next block, and `.130` is past that edge. The script does not print the edge.

**EX054.** The tests are the excluded set and then `192.0.2.0/25`. This address fails both. Being a documentation address is not a test, which is why `192.0.2.5` can pass while this one does not.

**EX055.** `{t:14}` pads the stored string with spaces out to 14 characters. `ip_address` already used the unpadded string. The verdict word is unchanged.

**EX056.** The only import is `ipaddress`. The `else` covers `192.0.2.130` and `198.51.100.7`. That branch prints and does not contact a host.

**EX057.** The lambda returns the negated product of likelihood and impact, then the id. The title is not in the key.

**EX058.** F1 and F3 share product 6, and `"F1"` precedes `"F3"`. F2's product is 2, so it sorts last even though it was typed second.

**EX059.** Scores 6 are high, 4 is medium, and 2 is low. A 5 would be medium. This print has no 5.

**EX060.** Likelihood 2 times impact 1 is 2. That product fails both thresholds, so the word is `low`. The title is not the arithmetic.

**EX061.** The file prints F4 at score 4 in third place. Impact 3 would make product 6, and the id order would be F1, F3, F4, then F2. That order is not the embedded print.

**EX062.** The page asks for named grading accounts and a portal password-reuse control within thirty days. Neither script prints 30.

**EX063.** She refuses the unnamed classmate's blog and removes the clinic note. Neither item is in the two lists, and neither script prints it.

**EX064.** 12–16 October 2026 is the agreed date span. 09:00–17:00 is the daily window. Neither script prints a date or a clock.

**EX065.** T1078 names the shared-account behaviour. The product remains 2 × 3. The technique id is not in the tuple and is not proof of an intrusion.

**EX066.** Keep both prints, the first-branch exclusion, the `/25` edge, and the prose for the deadline, the two refusals, and the two calendars. Reject a sent packet, the alternate F4 print, a password, a phone number, and any claim that the college is finished or that a credential was awarded. Twenty lessons meet the planning minimum and leave review open.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing.

- Bank of England / PRA. CBEST Threat Intelligence-Led Assessments — Implementation Guide. <https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide>
- European Central Bank. TIBER-EU Framework. <https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html>
- FIRST. CVSS v3.1 Specification Document. <https://www.first.org/cvss/v3.1/specification-document>
- MITRE ATT&CK, including T1078 Valid Accounts. <https://attack.mitre.org/>
- NIST SP 800-115 (2008). Technical Guide to Information Security Testing and Assessment. <https://doi.org/10.6028/NIST.SP.800-115>
- OWASP Web Security Testing Guide (WSTG). <https://owasp.org/www-project-web-security-testing-guide/>
- Penetration Testing Execution Standard (PTES). <https://pentest-standard.readthedocs.io/en/latest/>
