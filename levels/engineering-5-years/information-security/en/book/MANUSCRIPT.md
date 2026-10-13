# Information Security: Engineering Course

- Language: English (`en`); course 117, Engineering course (5 years).
- Editorial state: **draft**. Chapters 1–50 of 50 have hand-written teaching text; exercises EX001–EX150 have matching worked results with 0–3 rubrics; four offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: engineering students learning to build, verify and operate information security controls for a logistics company.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs reconcile a synthetic asset register with a synthetic discovery scan, check synthetic server configurations against three baseline rules, detect password-guessing bursts in a synthetic authentication log and verify synthetic backup restores against SHA-256 checksums. Standards are cited by edition and paraphrased. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one engineering student from mathematics, physics, programming and systems foundations through security requirements, models, threats, controls, implementation, verification, operations and validation to a capstone, an independent review, a recovery trial, an evidence dossier, a thesis and a final defense. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Lindiwe Dube** | Engineering student | Invented |
| **Prof. Marcus Hale** | Supervisor | Invented |
| **Brightwater Polytechnic** | Fictional polytechnic | Invented |
| **Saltmarsh Logistics** | Fictional logistics company, about 1,800 staff, twelve depots and 2,400 registered network addresses | Invented |

### Core sources

Anderson (2020), [doi:10.1002/9781119644682](https://doi.org/10.1002/9781119644682); ISO/IEC 27000:2026; ISO/IEC 27001:2022; ISO/IEC 27002:2022; NIST SP 800-53 Rev. 5; NIST SP 800-30 Rev. 1; FIPS 199, [doi:10.6028/NIST.FIPS.199](https://doi.org/10.6028/NIST.FIPS.199); NIST CSWP 29 (CSF 2.0); NIST SP 800-12 Rev. 1; Saltzer and Schroeder (1975), [doi:10.1109/PROC.1975.9939](https://doi.org/10.1109/PROC.1975.9939). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) · [41](#ch-41) · [42](#ch-42) · [43](#ch-43) · [44](#ch-44) · [45](#ch-45) · [46](#ch-46) · [47](#ch-47) · [48](#ch-48) · [49](#ch-49) · [50](#ch-50) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Calculus I

### Learning outcomes

You will (1) use rates of change to describe security event volumes; (2) relate derivatives to log monitoring; (3) estimate log storage with an integral.

### 1.1 The student and the company

Lindiwe Dube begins a five-year engineering course at the fictional Brightwater Polytechnic, supervised by Prof. Marcus Hale. Her placement partner is the fictional Saltmarsh Logistics, which employs about 1,800 people across twelve depots and runs roughly 2,400 networked devices, including 300 servers. Information security at Saltmarsh means protecting the confidentiality, integrity and availability of shipment, customer and payroll data. Prof. Hale explains that every mathematics course will connect to a real security decision at Saltmarsh, so theory is always tested against a working system. She starts in September.

### 1.2 Rates of change

Calculus starts with rates. If the number of stored security log events is a function of time, its derivative tells Saltmarsh how fast log storage grows. Lindiwe estimates that servers, firewalls and laptops together produce about forty million events per day, a steady rate. When Saltmarsh opens a new depot, the rate itself rises, so the second derivative becomes positive. She learns that planning log retention must use the growth rate, because a plan based only on today's total will run out of space early.

### 1.3 Monitoring with derivatives

Lindiwe applies the idea to monitoring. A sudden fall in the rate of incoming events from one depot, a large negative derivative, may mean a log forwarder has stopped, not that the depot became quieter. Attackers sometimes disable logging deliberately, so a silent source is itself a security signal. She proposes computing hourly event rates per source and alerting when a rate drops sharply. Prof. Hale notes that this turns a mathematical idea into a detective control for missing evidence. The depot team agrees.

### 1.4 Planning storage

Saltmarsh's policy keeps security logs for one year online and longer in archive. Lindiwe integrates the event rate over a year, allowing for two new depots, and finds the total grows faster than a simple multiple of today's volume. Prof. Hale asks her to compare full retention with keeping only summarised authentication and firewall events after ninety days. The integral shows large savings, but she notes that summaries can remove detail an investigator later needs, so retention is both a cost and an evidence decision.

### Worked example

Lindiwe models log growth as a rate, uses sudden rate drops to detect silent sources and integrates over a year to compare full and summarised retention.

> **Synthetic case.** Brightwater, Saltmarsh and all people are synthetic.

### Errors and limits

Treating a quiet log source as safe can hide a disabled forwarder.

### Exercises

- **EX001 — Daily events.** About how many events arrive per day? *Rubric:* 3 = about forty million;; 2 = close;; 1 = wrong;; 0 = none.
- **EX002 — Silent source.** What might a sudden drop in a source's event rate mean? *Rubric:* 3 = a stopped forwarder;; 2 = correct;; 1 = vague;; 0 = none.
- **EX003 — Summary risk.** What is the risk of summarising old logs? *Rubric:* 3 = losing detail investigators need;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-02"></a>

## Chapter 2 — Discrete mathematics

### Learning outcomes

You will (1) use sets to describe access rights; (2) model trust and dependencies as graphs; (3) express security rules in logic.

### 2.1 Sets of users and rights

Lindiwe describes Saltmarsh's access as sets: staff, accounts, groups and permissions. The set of accounts with payroll access should be a subset of the finance group. Set difference makes violations visible: payroll-access accounts minus finance staff should be empty. If it is not, someone holds rights outside their role. She writes such conditions as rules that can be checked automatically, noting that set notation makes a security policy precise enough to test rather than merely discuss. She runs the check against a synthetic directory export and finds four such accounts.

### 2.2 Relations and functions

A relation links accounts to people. Lindiwe checks whether it is a function: each named account should belong to exactly one person. Shared accounts break this, because actions cannot be traced to an individual. In a synthetic directory she finds several warehouse terminal accounts used by whole shifts. She explains that accountability, a core security property, depends on this mapping being a function, and that service accounts need a named owner even though no person logs in with them. Each shift account is listed.

### 2.3 Graphs of trust

Lindiwe models Saltmarsh's systems as a directed graph, with an edge where one system trusts another, for example a file server accepting logins from the directory. Reachability shows what an attacker could reach after compromising one node. A compromised depot laptop that can reach the directory can potentially reach almost everything. She learns that graph analysis underlies attack path reasoning, and that removing a few edges, such as unnecessary admin trust, can cut many paths at once. She draws the graph for twenty core systems.

### 2.4 Logic for rules

Security rules can be stated in logic. Lindiwe writes: for every account, if the account is privileged then multi-factor authentication is enabled. She checks the contrapositive: any account without multi-factor authentication must not be privileged. Prof. Hale shows how precise statements avoid arguments between teams over vague phrases such as admins should be protected. She learns that writing rules formally first makes code checks and audit evidence consistent with the policy wording. She lists five privileged accounts that fail the rule in the synthetic directory, and the identity team agrees to enrol each one before the next audit.

### Worked example

Lindiwe uses set difference to find out-of-role payroll access, checks account-to-person mapping, models trust as a graph and writes an MFA rule in logic.

> **Synthetic case.** The directory is synthetic.

### Errors and limits

A formal rule can still encode the wrong policy; confirm it with owners.

### Exercises

- **EX004 — Empty difference.** Which set difference should be empty? *Rubric:* 3 = payroll-access accounts minus finance staff;; 2 = correct;; 1 = vague;; 0 = none.
- **EX005 — Shared accounts.** Why do shared accounts harm accountability? *Rubric:* 3 = actions cannot be traced to a person;; 2 = correct;; 1 = vague;; 0 = none.
- **EX006 — Cutting paths.** How can many attack paths be cut at once? *Rubric:* 3 = remove a few trust edges;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-03"></a>

## Chapter 3 — Physics for computing

### Learning outcomes

You will (1) relate physical properties to security; (2) explain side channels and media remanence; (3) consider environmental threats to availability.

### 3.1 Physics and information

Computers store and move information as physical states: charges, magnetic domains and signals on wires or in the air. Lindiwe learns that physical properties create security effects. Wireless signals from a depot access point leak beyond the building, so an attacker in the car park can receive them. Encryption protects confidentiality where physics cannot. She notes that security design must start from what physically reaches an adversary, not from where the network diagram draws its boundary. She measures signal strength at the depot fence with a simple phone app.

### 3.2 Side channels

Devices emit information through power use, timing, sound and electromagnetic radiation. A cryptographic operation that takes slightly longer for some keys can reveal those keys to a careful observer. Lindiwe reads how such side channels have been exploited in research and why constant-time implementations matter. At Saltmarsh the practical lesson is narrower: use well-reviewed cryptographic libraries rather than home-made code, since library authors handle timing behaviour that application developers rarely consider. Lindiwe checks which libraries Saltmarsh's payment and login services use and confirms that both rely on widely reviewed implementations maintained by large communities.

### 3.3 Remanence and disposal

Data persist physically after deletion. On magnetic disks, deleted files remain until overwritten; on solid-state drives, wear-levelling may keep old copies in blocks the operating system cannot address. Saltmarsh retires about a hundred laptops a year. Lindiwe recommends full-disk encryption from the start, so that destroying the key renders remaining data unreadable, plus certified destruction for drives that held payroll data. She learns that disposal is a physics problem as much as a policy one. The disposal supplier's certificates are now filed with each asset record.

### 3.4 Environment and availability

Heat, power and water threaten availability. A server room above its design temperature throttles processors and shortens component life; a power cut without backup stops depots invoicing. Lindiwe surveys Saltmarsh's main server room and finds cooling adequate but the uninterruptible power supply sized years ago for fewer servers. She calculates that its runtime at current load is under ten minutes. Prof. Hale notes that availability failures often begin with physics nobody rechecked. The facilities manager orders a larger unit after reading her calculation, and Lindiwe adds a yearly load check to the maintenance calendar.

### Worked example

Lindiwe connects radio leakage, side channels, remanence and power capacity to security controls at Saltmarsh, recommending encryption, reviewed libraries and a power supply review.

> **Synthetic case.** Measurements are synthetic.

### Errors and limits

Deleting files does not remove data from storage media.

### Exercises

- **EX007 — Radio leakage.** Why does encryption matter for depot wireless? *Rubric:* 3 = signals reach beyond the building;; 2 = correct;; 1 = vague;; 0 = none.
- **EX008 — SSD remanence.** Why can deleted data survive on solid-state drives? *Rubric:* 3 = wear-levelling keeps old copies;; 2 = correct;; 1 = vague;; 0 = none.
- **EX009 — UPS runtime.** What runtime does the power supply give at current load? *Rubric:* 3 = under ten minutes;; 2 = correct;; 1 = wrong;; 0 = none.

<a id="ch-04"></a>

## Chapter 4 — Programming I

### Learning outcomes

You will (1) write simple Python to process security data; (2) validate untrusted input; (3) handle errors without hiding them.

### 4.1 First scripts

Lindiwe writes her first Python scripts on synthetic Saltmarsh data. One reads a list of user accounts and counts those with no login in ninety days, which are candidates for disabling. She uses only the standard library, so the script runs on any analyst's machine without installing packages. Prof. Hale asks her to print counts with clear labels, because a security report that reads 37 with no context will be misunderstood by the managers who receive it. The script finds thirty-seven inactive accounts in the synthetic file.

### 4.2 Untrusted input

Input from outside a program cannot be trusted. Lindiwe writes a function that accepts a depot code typed by a user and checks it against the twelve valid codes before using it in a file path. Without this check, an input such as dot-dot-slash sequences could make the program read files outside its folder. She learns that validating input against an allow list, rather than trying to block known bad patterns, is the safer default. She tests the function with ten deliberately malformed codes.

### 4.3 Errors and logging

Programs fail, and the way they fail matters. Lindiwe's first script stopped silently when a line in the account file was malformed. She rewrites it to log the line number and reason, skip the bad line and report the count of skipped lines at the end. Prof. Hale explains that silent failures are dangerous in security tooling, because a scan that quietly skips half its targets still produces a reassuring report. In the synthetic file, her new version skips three malformed lines and reports them by number, so the data owner can correct the source records.

### 4.4 Reading code critically

Lindiwe reads a short script a colleague wrote to reset passwords. It builds a shell command by joining strings that include the username. She recognises that a username containing a semicolon could inject a second command. She suggests passing arguments as a list to the subprocess module instead, so no shell interprets them. Prof. Hale says reviewing others' code for such patterns is one of the most valuable habits an engineer can build early. Her colleague agrees, updates the script and asks her to review his next one.

### Worked example

Lindiwe writes standard-library scripts with labelled output, validates depot codes against an allow list, logs skipped lines and spots a command injection risk.

> **Synthetic case.** Scripts and data are synthetic.

### Errors and limits

Blocking known bad input is weaker than allowing only known good input.

### Exercises

- **EX010 — Inactive accounts.** What does the first script count? *Rubric:* 3 = accounts with no login in ninety days;; 2 = correct;; 1 = vague;; 0 = none.
- **EX011 — Allow list.** How is the depot code validated? *Rubric:* 3 = against the twelve valid codes;; 2 = correct;; 1 = vague;; 0 = none.
- **EX012 — Injection fix.** How should the reset script call commands? *Rubric:* 3 = pass arguments as a list;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-05"></a>

## Chapter 5 — Engineering communication

### Learning outcomes

You will (1) write clear security findings; (2) present risk to non-specialists; (3) document decisions for later readers.

### 5.1 Writing findings

Lindiwe's first placement task is writing up a finding: a file share readable by all staff contains scanned driver licences. Prof. Hale shows her a structure: what was found, where, why it matters, how likely misuse is and what to do. She avoids jargon such as world-readable in the summary and writes that any employee can open the folder. The finding is short, specific and gives the owner a clear next action. The folder owner, a depot administrator, moves the scans to a restricted share the same afternoon.

### 5.2 Presenting risk

Lindiwe presents three findings to depot managers. Instead of scores, she describes plausible consequences: a stolen licence scan could support identity fraud against a driver. Managers ask which finding to fix first. She explains likelihood and impact in plain terms and recommends starting with the licence folder because exposure is wide and the fix is quick. She learns that risk communication succeeds when listeners can act on it immediately. Two managers ask for the same briefing for their supervisors, and Lindiwe shortens it to a single page with the three findings and their owners.

### 5.3 Diagrams

Lindiwe draws a simple network diagram for the presentation, showing depots, the head office and the cloud email service. Prof. Hale asks her to mark trust boundaries, where data cross from one zone of control to another, because those are where controls belong. She removes decorative icons and labels every arrow with the data it carries. The diagram becomes a tool for discussion rather than a picture, and later readers can update it. She stores the diagram beside the current network documentation.

### 5.4 Decision records

Decisions fade from memory. Lindiwe writes a short decision record for the licence folder: context, options considered, decision, owner and date. Months later, an auditor asks why the folder was moved rather than deleted, and the record answers immediately: drivers' licences must be retained for insurance checks. She learns that recording reasons protects an organisation from repeating debates and helps auditors see that risks were handled deliberately. Saltmarsh adopts her template for all security decisions, and the records are kept in a shared folder with the owner's name on each, which makes later audits faster.

### Worked example

Lindiwe writes a structured finding about exposed licence scans, presents it by consequence, draws a diagram with trust boundaries and records the decision.

> **Synthetic case.** Findings are synthetic.

### Errors and limits

A finding without a clear owner and action rarely gets fixed.

### Exercises

- **EX013 — Finding structure.** Name the parts of a finding. *Rubric:* 3 = found, where, why, likelihood, action;; 2 = most;; 1 = few;; 0 = none.
- **EX014 — Trust boundaries.** What does Prof. Hale ask her to mark? *Rubric:* 3 = trust boundaries;; 2 = correct;; 1 = other;; 0 = none.
- **EX015 — Record answer.** Why was the folder moved rather than deleted? *Rubric:* 3 = licences are retained for insurance checks;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-06"></a>

## Chapter 6 — Calculus II

### Learning outcomes

You will (1) model growth and decay in security processes; (2) use exponential models for vulnerability backlog; (3) interpret half-life of exposure.

### 6.1 Exponential decay

Many security processes decay roughly exponentially. If Saltmarsh patches a fixed fraction of open vulnerabilities each week, the backlog falls by the same proportion every week. Lindiwe fits such a model to synthetic data: about fifteen percent of open findings are closed weekly. Solving the differential equation gives a curve she can compare with targets. Prof. Hale notes that the model is simple but useful for asking whether a target is achievable at current effort. Lindiwe plots the fitted curve against twelve weeks of synthetic closure data.

### 6.2 Half-life of exposure

From the decay rate, Lindiwe computes a half-life: the time for half of a set of new vulnerabilities to be fixed. At fifteen percent per week, the half-life is a little over four weeks. Critical vulnerabilities exploited in the wild need much faster closure. She concludes that a single weekly rate hides important differences and that Saltmarsh should track separate rates by severity, since an average comfortable for low findings may be dangerous for critical ones. She proposes separate dashboards for each severity.

### 6.3 Inflow and backlog

The backlog also grows as new vulnerabilities are disclosed. Lindiwe writes a differential equation with constant inflow and proportional closure. Its steady state equals inflow divided by the closure rate. With about sixty new findings per week, the backlog settles near four hundred. To halve it, Saltmarsh must double the closure rate or halve inflow, for example by removing unused software. She learns that reducing what is installed can be as effective as working faster. She lists eleven unused applications that could be removed.

### 6.4 Limits of the model

Real closures are lumpy: patch days close many at once and difficult systems linger. Lindiwe compares the smooth model with synthetic weekly data and sees large deviations around monthly patch releases. Prof. Hale explains that models guide thinking but must be checked against observations, and that an engineer should state assumptions next to any projection. She adds a sentence to her report noting that the model ignores systems that cannot be patched without vendor support. She shows the deviations in a chart for her report.

### Worked example

Lindiwe models vulnerability closure as exponential decay, computes a four-week half-life, derives a steady-state backlog near four hundred and notes the model's limits.

> **Synthetic case.** Rates are synthetic.

### Errors and limits

A single average closure rate hides slow handling of critical findings.

### Exercises

- **EX016 — Half-life.** What is the half-life at fifteen percent weekly closure? *Rubric:* 3 = a little over four weeks;; 2 = close;; 1 = wrong;; 0 = none.
- **EX017 — Steady state.** What is the steady-state backlog formula? *Rubric:* 3 = inflow divided by closure rate;; 2 = correct;; 1 = vague;; 0 = none.
- **EX018 — Reduce inflow.** How can inflow be reduced? *Rubric:* 3 = remove unused software;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-07"></a>

## Chapter 7 — Probability and statistics

### Learning outcomes

You will (1) estimate rates from security data; (2) reason about base rates in alerting; (3) quantify uncertainty.

### 7.1 Estimating rates

Lindiwe estimates how often Saltmarsh staff report phishing emails. From synthetic data, 180 of 1,800 staff reported at least one message in a quarter, a proportion of ten percent. She computes a confidence interval and finds it reasonably narrow because the sample is large. Prof. Hale asks her to state what the proportion describes, staff who reported at least once, so nobody mistakes it for the share of phishing emails that get reported. She reports the interval alongside the proportion. The security team uses the figure as a baseline for future awareness campaigns.

### 7.2 Base rates

An alert rule flags suspicious logins with ninety-nine percent sensitivity and ninety-nine percent specificity. Lindiwe calculates what happens when only one login in ten thousand is malicious. Among a million logins, about ninety-nine true attacks are flagged, along with about ten thousand false alarms. Most alerts are false even though the rule seems accurate. She learns that base rates dominate alert quality and that analysts must expect many false positives from rare-event detection. The monitoring team confirms this matches its daily experience with login alerts.

### 7.3 Variation

Weekly counts of malware detections vary even when nothing changes. Lindiwe models them as a Poisson process with a mean of twelve per week and shows that weeks of eighteen or more happen occasionally by chance. Managers had treated one such week as an outbreak. She recommends control limits that mark genuinely unusual weeks. Prof. Hale notes that understanding ordinary variation prevents both panic over noise and complacency about real changes. She plots a year of synthetic weekly counts with the limits drawn as horizontal lines.

### 7.4 Comparing groups

Saltmarsh wants to know whether depots with newer laptops have fewer malware detections. Lindiwe warns that newer laptops went to larger depots, which also have dedicated IT staff, so any difference could reflect staffing rather than hardware. She proposes comparing detection rates per device within depots of similar size. She learns that confounding is the main trap in observational security data and that comparisons need careful design. The IT manager agrees to provide device counts per depot. Lindiwe notes that even within similar depots, laptop age may still correlate with other differences she cannot measure.

### Worked example

Lindiwe estimates a ten percent reporting rate, shows base rates make most alerts false, models weekly detections as Poisson and flags confounding in a laptop comparison.

> **Synthetic case.** Figures are synthetic.

### Errors and limits

An accurate-sounding detector can still produce mostly false alerts.

### Exercises

- **EX019 — False alarms.** About how many false alarms occur per million logins? *Rubric:* 3 = about ten thousand;; 2 = close;; 1 = wrong;; 0 = none.
- **EX020 — Poisson weeks.** What model describes weekly detections? *Rubric:* 3 = Poisson with mean twelve;; 2 = correct;; 1 = other;; 0 = none.
- **EX021 — Laptop confounder.** What might explain fewer detections with new laptops? *Rubric:* 3 = larger depots with IT staff;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-08"></a>

## Chapter 8 — Computer architecture

### Learning outcomes

You will (1) explain how hardware enforces isolation; (2) describe trusted boot; (3) relate firmware to security risk.

### 8.1 Privilege levels

Processors run code at different privilege levels. The operating system kernel runs with full control, while applications run restricted and must ask the kernel to access hardware. Lindiwe learns that this separation stops a compromised application from directly reading another program's memory. Memory management units enforce boundaries between processes. Prof. Hale explains that much of software security depends on these hardware features working correctly, which is why processor flaws affect everyone at once. Lindiwe reads about processor flaws that let programs infer memory contents across this boundary.

### 8.2 Trusted boot

When a laptop starts, firmware loads a bootloader, which loads the operating system. If an attacker alters any stage, later security checks can be bypassed. Secure boot verifies a digital signature at each stage, refusing to run unsigned code. Lindiwe checks a synthetic inventory of Saltmarsh laptops and finds a small group with secure boot disabled for an old driver. She recommends replacing the driver so the feature can be enabled across the fleet. The desktop team schedules the driver replacement for the next quarter.

### 8.3 Firmware

Firmware in network cards, disks and management controllers runs below the operating system and is rarely updated. Lindiwe learns that server management controllers often have their own network interface and passwords. At Saltmarsh, several controllers still use factory credentials on the server network. She recommends moving them to a separate management network and changing credentials. Prof. Hale notes that attackers favour layers defenders forget to monitor. Lindiwe also lists firmware versions from the synthetic inventory and finds that most management controllers have not been updated since installation, which she adds to the patching backlog.

### 8.4 Hardware security modules

Some keys need stronger protection than software provides. A hardware security module stores keys inside tamper-resistant hardware and performs cryptographic operations without revealing them. Lindiwe learns that Saltmarsh's payment provider uses such modules, while Saltmarsh's own code-signing key sits in a file on a build server. She recommends moving it to a hardware token or managed key service, so stealing the build server does not give an attacker the ability to sign malicious updates. The development lead agrees to cost the change before the next release.

### Worked example

Lindiwe connects privilege levels, secure boot, management controller credentials and hardware key protection to concrete improvements at Saltmarsh.

> **Synthetic case.** Inventories are synthetic.

### Errors and limits

Firmware and management controllers are often left with factory credentials.

### Exercises

- **EX022 — Kernel separation.** What does kernel and application separation prevent? *Rubric:* 3 = one application reading another's memory;; 2 = correct;; 1 = vague;; 0 = none.
- **EX023 — Secure boot gap.** Why was secure boot disabled on some laptops? *Rubric:* 3 = an old driver;; 2 = correct;; 1 = other;; 0 = none.
- **EX024 — Signing key.** Where should the code-signing key move? *Rubric:* 3 = a hardware token or managed key service;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-09"></a>

## Chapter 9 — Programming II

### Learning outcomes

You will (1) structure larger security tools; (2) test code with known cases; (3) handle secrets safely in programs.

### 9.1 Structuring tools

Lindiwe's scripts grow, so she organises them into functions with clear inputs and outputs: one reads accounts, one applies rules and one writes reports. Each function does one job and can be tested alone. Prof. Hale explains that structure matters more in security tools than elsewhere, because a hidden bug may report that everything is compliant when it is not, and nobody will notice until an incident proves otherwise. She also writes a short description at the top of each function explaining what it checks.

### 9.2 Testing with known cases

Lindiwe writes tests using small synthetic inputs where she knows the correct answer: an account with no multi-factor authentication and admin rights must be flagged; a normal account must not. She runs the tests after every change using the standard unittest module. When a later change breaks the admin check, a test fails immediately. She learns that tests are the evidence that a security check does what its name claims. By the end of the term her test file holds twenty cases, each named after the rule it checks.

### 9.3 Handling secrets

One tool must call Saltmarsh's directory using a service account password. Lindiwe's first version stored the password in the script, which was then shared in a chat channel. She rewrites the tool to read credentials from an environment variable set by the scheduler, and asks for the exposed password to be changed. Prof. Hale notes that secrets in code end up in backups, repositories and messages, far beyond their intended audience. The directory team rotates the password within an hour of her report.

### 9.4 Dependencies and supply

Lindiwe considers adding a third-party library to parse a log format. She checks who maintains it, when it was last updated and whether it has known vulnerabilities. She decides to write a small parser herself because the format is simple and the library is unmaintained. She learns that every dependency extends the code an organisation trusts, and that keeping security tools small reduces that exposure. Her parser is eighty lines long and covered by its own tests. Prof. Hale asks her to record the reasons for this choice in a short decision record.

### Worked example

Lindiwe structures her tool into testable functions, adds unit tests with known cases, moves a leaked password to an environment variable and avoids an unmaintained dependency.

> **Synthetic case.** Code is synthetic.

### Errors and limits

A password committed to code must be treated as exposed and changed.

### Exercises

- **EX025 — Test module.** Which module runs her tests? *Rubric:* 3 = unittest;; 2 = correct;; 1 = other;; 0 = none.
- **EX026 — Secret storage.** Where does the tool read credentials from? *Rubric:* 3 = an environment variable set by the scheduler;; 2 = correct;; 1 = code;; 0 = none.
- **EX027 — Parser choice.** Why write her own parser? *Rubric:* 3 = simple format, unmaintained library;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-10"></a>

## Chapter 10 — Engineering ethics and safety

### Learning outcomes

You will (1) apply professional ethics to security work; (2) handle discovered vulnerabilities responsibly; (3) respect privacy in monitoring.

### 10.1 Professional duty

Engineers owe duties to the public as well as to employers. Lindiwe reads professional codes that emphasise honesty, competence and protecting people from harm. In security work, this means not overstating assurance, not using access beyond what a task needs and reporting risks even when inconvenient. Prof. Hale discusses a case where an engineer signed off a system as secure under deadline pressure; customers' data were later exposed. Lindiwe notes that signatures carry responsibility. She writes a short reflection on the case for her course portfolio.

### 10.2 Authorised testing

During her placement, Lindiwe notices a depot web page that appears to reveal other customers' tracking details when a number in the address is changed. She does not explore further to see how much data is exposed. She reports what she saw to her placement manager, who confirms she is not authorised to test the site. The security team investigates and fixes it. She learns that curiosity must stay within written authorisation, even with good intentions. Her manager thanks her for stopping when she did.

### 10.3 Privacy in monitoring

Security monitoring records what staff do. Lindiwe helps review Saltmarsh's monitoring notice and finds it does not mention that web browsing is logged. She recommends updating the notice, limiting who can view browsing logs and keeping them only as long as needed for security purposes. Prof. Hale explains that monitoring which staff do not know about damages trust and may breach data protection rules. The human resources director and the security lead approve the revised notice together, and staff receive it by email with a short explanation of what is logged and why.

### 10.4 Safety connections

Some Saltmarsh systems affect physical safety: refrigerated trailers carry medicines, and their temperature data must be accurate. A tampered temperature record could let spoiled medicines reach patients. Lindiwe notes that integrity failures here are safety failures, not just data problems. She recommends integrity protection for sensor records and clear escalation when readings are missing. She learns that security engineering sometimes protects lives as well as information. The fleet team adds a check that raises an alarm when a trailer's temperature record has gaps, and Lindiwe documents the new rule in her placement report.

### Worked example

Lindiwe reports a possible data exposure without testing it, recommends a clearer monitoring notice and links integrity of temperature records to patient safety.

> **Synthetic case.** Incidents are synthetic.

### Errors and limits

Testing a live system without authorisation is not acceptable, even to help.

### Exercises

- **EX028 — Untested report.** What does Lindiwe do on noticing the exposure? *Rubric:* 3 = reports it without testing further;; 2 = correct;; 1 = test;; 0 = none.
- **EX029 — Notice gap.** What did the monitoring notice omit? *Rubric:* 3 = web browsing logging;; 2 = correct;; 1 = other;; 0 = none.
- **EX030 — Safety link.** Why do temperature records matter for safety? *Rubric:* 3 = tampering could let spoiled medicines reach patients;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-11"></a>

## Chapter 11 — Networks and protocols

### Learning outcomes

You will (1) explain how packets move between networks; (2) identify protocol weaknesses; (3) apply segmentation to limit attacks.

### 11.1 Layers and packets

Lindiwe studies how data cross Saltmarsh's network. Applications hand data to transport protocols, which hand packets to the network layer for routing between depots and head office. Each layer adds headers that devices read to decide where packets go. She captures synthetic traffic in a laboratory and identifies addresses, ports and protocols. Prof. Hale explains that attackers exploit the same layers, so understanding normal traffic is the first step towards recognising unusual traffic in Saltmarsh's monitoring tools. She labels each captured flow by depot and application.

### 11.2 Protocol weaknesses

Many older protocols were designed for trusted networks and send data unencrypted. Lindiwe finds that some depot printers are still managed over a protocol that sends passwords in clear text. Anyone capturing traffic on the same network segment could read them. She recommends switching to encrypted management or, where printers cannot support it, isolating them. She learns that protocol choice is a security decision, and that legacy devices often force compromises that must be documented and contained rather than ignored. The printer vendor confirms this.

### 11.3 Name resolution

The domain name system translates names into addresses. If an attacker can alter answers, users may connect to a fake server without noticing. Lindiwe reviews Saltmarsh's resolvers and confirms they forward only to approved upstream services and log queries. The logs help detect malware that contacts unusual domains. Prof. Hale notes that name resolution is a common route for both attack and detection, so its configuration deserves the same attention as firewalls, even though it often receives far less. She shares the resolver review with operations.

### 11.4 Segmentation

Saltmarsh's depots originally shared one flat network, so a compromised laptop could reach payroll servers directly. Lindiwe helps design segments: office devices, warehouse scanners, printers, servers and management interfaces, each with firewall rules allowing only necessary traffic between them. She estimates that segmentation removes most direct paths from depot laptops to sensitive servers. She learns that segmentation does not stop an attacker entering, but limits how far they move, which buys detection time and reduces damage. The network team schedules the first depot migration for the spring shutdown week.

### Worked example

Lindiwe maps traffic by layer, flags clear-text printer management, reviews resolver logging and designs segments that cut direct paths from depot laptops to servers.

> **Synthetic case.** Traffic and designs are synthetic.

### Errors and limits

A flat network lets one compromised device reach everything.

### Exercises

- **EX031 — Clear-text risk.** What risk do the printers' management protocol pose? *Rubric:* 3 = passwords sent in clear text;; 2 = correct;; 1 = vague;; 0 = none.
- **EX032 — Resolver logs.** What can resolver logs help detect? *Rubric:* 3 = malware contacting unusual domains;; 2 = correct;; 1 = vague;; 0 = none.
- **EX033 — Segmentation value.** What does segmentation mainly limit? *Rubric:* 3 = how far attackers move;; 2 = correct;; 1 = entry;; 0 = none.

<a id="ch-12"></a>

## Chapter 12 — Operating systems

### Learning outcomes

You will (1) explain process isolation and permissions; (2) harden operating system configurations; (3) collect useful system logs.

### 12.1 Processes and permissions

Operating systems run programs as processes owned by user accounts, and permissions decide what each account can read, write or execute. Lindiwe examines a synthetic Saltmarsh file server and finds that a backup service runs as the most powerful account. If the service were compromised, the attacker would gain full control. She recommends a dedicated account with only the rights backups need. Prof. Hale notes that running services with least privilege limits the damage any single flaw can cause. The server team agrees.

### 12.2 Hardening

Default installations favour convenience. Lindiwe works through a hardening checklist for Saltmarsh's Linux servers: disable remote root login, remove unused services, apply updates within a set period and encrypt disks. She learns that each item reduces attack surface or limits the impact of a stolen device. She also learns that checklists drift: servers configured correctly last year may have changed since, which is why later chapters measure compliance automatically instead of trusting installation records. She records which checklist items each synthetic server already meets and which need work.

### 12.3 System logging

Operating systems record logins, privilege changes and service failures. Lindiwe configures synthetic servers to forward these logs to a central collector, so an attacker who gains control of a server cannot simply erase local evidence. She chooses events carefully, because logging everything produces noise and cost. Prof. Hale asks her to justify each event type by an investigation question it would answer, such as who used administrator rights on this server last week, which keeps logging purposeful. The collector keeps logs for a year.

### 12.4 Updates

Operating system updates fix vulnerabilities but can break applications. Saltmarsh delays updates on some servers because a warehouse application once failed after an update. Lindiwe proposes a test group of servers that receives updates first, with automatic promotion to the rest after a week without problems. She learns that reliable update processes are a security control in themselves, because fear of breakage is one of the most common reasons organisations leave known vulnerabilities open for months. The warehouse application owner agrees to join the test group.

### Worked example

Lindiwe moves a backup service to a least-privilege account, applies a hardening checklist, forwards purposeful logs centrally and proposes staged updates.

> **Synthetic case.** Servers are synthetic.

### Errors and limits

Logs kept only on the server can be erased by an attacker who controls it.

### Exercises

- **EX034 — Backup account.** What account should the backup service use? *Rubric:* 3 = a dedicated least-privilege account;; 2 = correct;; 1 = admin;; 0 = none.
- **EX035 — Central logs.** Why forward logs to a central collector? *Rubric:* 3 = attackers cannot erase local evidence;; 2 = correct;; 1 = vague;; 0 = none.
- **EX036 — Update staging.** What does Lindiwe propose for updates? *Rubric:* 3 = a test group first, then promotion after a week;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-13"></a>

## Chapter 13 — Data systems

### Learning outcomes

You will (1) protect databases against common attacks; (2) control access to sensitive fields; (3) design backups that support recovery.

### 13.1 Database access

Saltmarsh's shipment database holds customer addresses and delivery notes. Lindiwe finds that the web application connects with an account that can read, change and delete every table. She recommends separate accounts for reading and writing, each limited to the tables needed. If the application were compromised, the attacker could then do less. Prof. Hale explains that database permissions are often granted broadly during development and never narrowed, so reviewing them is valuable early in any assessment. The developers create the two new accounts within a week.

### 13.2 Injection

Lindiwe studies how applications build database queries. Code that inserts user input directly into query text allows injection, where crafted input changes the query's meaning. She reviews a synthetic search page and finds it builds queries by joining strings. She rewrites it to use parameterised queries, so input is always treated as data. She learns that injection remains common because string building is easy, and that code review and testing must look for it specifically. She adds a test that submits a quotation mark and a semicolon.

### 13.3 Sensitive fields

Some fields, such as driver licence numbers, need stronger protection than others. Lindiwe considers encrypting them at the field level, so database administrators and backups see only ciphertext. Applications that need the values decrypt them with keys held separately. She notes the cost: searching and sorting encrypted fields becomes harder. Prof. Hale asks her to justify field encryption by who should and should not see values, not by a general wish to encrypt everything. She concludes that only licence numbers justify field encryption at Saltmarsh.

### 13.4 Backups for recovery

Backups protect availability and integrity, but only if they can be restored. Lindiwe learns that ransomware often targets backups first, so copies must be kept where an attacker who controls the main network cannot delete them. Saltmarsh keeps nightly backups on a network share reachable from servers. She recommends an additional copy that cannot be altered for a set period. She also notes that restores must be tested, a theme the course returns to with a verification lab. The infrastructure team prices the immutable copy.

### Worked example

Lindiwe narrows database accounts, replaces string-built queries with parameterised ones, weighs field encryption for licence numbers and recommends immutable backup copies.

> **Synthetic case.** Databases are synthetic.

### Errors and limits

A backup reachable and deletable from the main network may not survive ransomware.

### Exercises

- **EX037 — Database accounts.** What does Lindiwe recommend for the application's database access? *Rubric:* 3 = separate limited read and write accounts;; 2 = correct;; 1 = vague;; 0 = none.
- **EX038 — Injection fix.** How does she fix the search page? *Rubric:* 3 = parameterised queries;; 2 = correct;; 1 = other;; 0 = none.
- **EX039 — Backup copy.** What extra backup copy does she recommend? *Rubric:* 3 = one that cannot be altered for a set period;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-14"></a>

## Chapter 14 — Software engineering

### Learning outcomes

You will (1) integrate security into the development lifecycle; (2) use threat-aware code review; (3) manage vulnerabilities in dependencies.

### 14.1 Security in the lifecycle

Saltmarsh's developers build a driver app for delivery confirmations. Lindiwe learns that security added at the end is expensive, while security considered from requirements onwards is cheaper. She helps write security requirements: drivers authenticate with their own accounts, confirmations cannot be altered after submission and location data are kept only as long as disputes may arise. Prof. Hale notes that clear requirements give testers something concrete to check, rather than a vague instruction to make the app secure. The product owner accepts all three requirements.

### 14.2 Code review

Lindiwe joins code reviews for the driver app. She looks for the patterns she has learned: string-built queries, secrets in code, missing input validation and permissions checked only in the user interface. In one change, the app hides a delete button from drivers but the server accepts delete requests from anyone logged in. She explains that every check must happen on the server, because attackers do not use the official interface. The developer fixes the server check the same day and adds a test that sends a delete request from a driver account and expects a refusal.

### 14.3 Dependency management

The driver app uses dozens of open-source libraries. Lindiwe sets up a list of dependencies with versions and checks it against public vulnerability databases each week. One library has a known flaw allowing denial of service, and an update exists. The developers update it after running their tests. She learns that most application code is borrowed, so knowing what is included is essential, and that a dependency list is itself a security record. The weekly check takes a few minutes and runs automatically on the build server, sending results to the team channel.

### 14.4 Build integrity

Code is turned into installable packages by a build server. If an attacker changes the build, every user receives malicious software. Lindiwe recommends that builds run from version-controlled scripts, that build servers be isolated and that packages be signed with a protected key. Prof. Hale connects this to her earlier recommendation about the code-signing key. She learns that the path from source code to user device is part of the attack surface and must be protected. The development lead adds these steps to the roadmap.

### Worked example

Lindiwe writes security requirements for a driver app, finds a server-side authorisation gap in review, tracks dependencies weekly and recommends a protected build pipeline.

> **Synthetic case.** The app is synthetic.

### Errors and limits

Hiding a button in the interface does not stop requests to the server.

### Exercises

- **EX040 — Delete flaw.** What flaw does code review find? *Rubric:* 3 = server accepts delete requests from anyone logged in;; 2 = correct;; 1 = vague;; 0 = none.
- **EX041 — Dependency check.** How often are dependencies checked? *Rubric:* 3 = weekly;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX042 — Build protection.** Name one build protection she recommends. *Rubric:* 3 = signed packages;; 2 = one;; 1 = vague;; 0 = none.

<a id="ch-15"></a>

## Chapter 15 — Security fundamentals

### Learning outcomes

You will (1) define confidentiality, integrity and availability; (2) categorise systems by impact; (3) relate threats, vulnerabilities and risk.

### 15.1 Three objectives

Lindiwe studies the security objectives used throughout the field. FIPS 199 defines three: confidentiality, preserving authorised restrictions on access and disclosure; integrity, guarding against improper modification or destruction; and availability, ensuring timely and reliable access. ISO/IEC 27000:2026, the current overview of the ISO/IEC 27000 family, describes information security in the same three terms. She applies them to Saltmarsh: payroll needs confidentiality, delivery records need integrity and the dispatch system needs availability during working hours. Prof. Hale asks her to justify each choice by describing what would happen if that objective failed for a full working day.

### 15.2 Categorising systems

FIPS 199 asks how severe the impact would be if each objective were lost: low, moderate or high. Lindiwe categorises five Saltmarsh systems. Payroll is high for confidentiality; dispatch is high for availability; the public website is low for confidentiality but moderate for integrity, since defacement harms reputation. Prof. Hale explains the high-water mark: the overall category takes the highest of the three. She learns that categorisation focuses effort on systems whose failure would hurt most. She records each categorisation with a one-line reason for the rating.

### 15.3 Threats and vulnerabilities

A threat is something that could cause harm, such as a criminal group seeking ransom. A vulnerability is a weakness that a threat could exploit, such as an unpatched server. Risk combines the likelihood that a threat exploits a vulnerability with the impact if it does. Lindiwe reads NIST SP 800-30 Revision 1, which describes this approach to risk assessment. She notes that risk exists only when threat, vulnerability and impact come together for a particular system. She writes one example of each for the dispatch system in her notes.

### 15.4 Controls

Controls reduce risk by preventing, detecting or correcting harm. Lindiwe classifies examples at Saltmarsh: multi-factor authentication prevents account takeover, log alerts detect suspicious activity and backups correct damage after ransomware. She learns that relying on one type is fragile, because prevention eventually fails. Prof. Hale introduces defence in depth, combining several independent controls so that the failure of one does not expose the system completely, and asks her to show it for payroll. For payroll she lists multi-factor authentication, restricted network access, access reviews, alerts on bulk exports and tested backups as separate layers.

### Worked example

Lindiwe defines the three objectives from FIPS 199, categorises five systems with the high-water mark, separates threat from vulnerability and builds layered controls for payroll.

> **Synthetic case.** Categorisations are synthetic.

### Errors and limits

Calling a vulnerability a risk ignores threat and impact.

### Exercises

- **EX043 — Integrity definition.** How does FIPS 199 define integrity? *Rubric:* 3 = guarding against improper modification or destruction;; 2 = correct;; 1 = vague;; 0 = none.
- **EX044 — High-water mark.** What is the high-water mark? *Rubric:* 3 = overall category is the highest of the three;; 2 = correct;; 1 = vague;; 0 = none.
- **EX045 — Defence in depth.** What is defence in depth? *Rubric:* 3 = several independent controls;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-16"></a>

## Chapter 16 — Systems engineering

### Learning outcomes

You will (1) apply systems thinking to security; (2) manage requirements and interfaces; (3) plan security across the system lifecycle.

### 16.1 Systems thinking

A system's security depends on how its parts interact. Lindiwe studies Saltmarsh's dispatch system: a web application, a database, a message queue, driver phones and an external mapping service. A weakness in any interface could affect the whole. Prof. Hale asks her to list each interface with the data crossing it and the trust assumed. She finds that the mapping service receives full delivery addresses, which nobody had considered when the contract was signed. The procurement team reviews the contract and asks the supplier how long addresses are kept.

### 16.2 Requirements traceability

Lindiwe traces each security requirement to the component that implements it and the test that verifies it. For example, the requirement that confirmations cannot be altered after submission maps to a database constraint and a test that attempts an update. She finds two requirements with no test. Prof. Hale explains that traceability shows gaps early and gives auditors evidence, because a requirement without a test is only an intention that nobody has checked. The developers write the two missing tests before the next release, and Lindiwe updates her traceability table to show each requirement covered.

### 16.3 Lifecycle

Security needs change through a system's life: design, build, operation, change and retirement. Lindiwe notes that retirement is often forgotten. An old dispatch server, replaced last year, still runs with outdated software and holds copies of customer data. She recommends a retirement checklist covering data deletion, account removal and network disconnection. She learns that every lifecycle stage needs explicit security activities, not just design and build. The old server is wiped and disconnected within a month of her report. The infrastructure team adds the retirement checklist to its standard change process, so future decommissioning follows the same steps.

### 16.4 Trade-offs

Systems engineering balances competing needs. Stronger authentication for drivers adds a few seconds per delivery, which matters across thousands of deliveries daily. Lindiwe measures the time added by a synthetic multi-factor prompt and proposes remembering trusted devices for a shift. Prof. Hale notes that security choices that ignore operational cost tend to be bypassed, and that documenting trade-offs openly helps managers accept the remaining risk deliberately. The synthetic prompt adds about four seconds per login. With remembered devices, drivers authenticate once per shift instead of at every delivery, and the operations manager accepts this design.

### Worked example

Lindiwe lists dispatch interfaces and finds addresses shared with a mapping service, traces requirements to tests, adds a retirement checklist and balances authentication delay against delivery time.

> **Synthetic case.** Systems are synthetic.

### Errors and limits

Forgotten retired servers often keep old data and old vulnerabilities.

### Exercises

- **EX046 — Mapping data.** What data does the mapping service receive? *Rubric:* 3 = full delivery addresses;; 2 = correct;; 1 = vague;; 0 = none.
- **EX047 — Untested requirements.** How many requirements had no test? *Rubric:* 3 = two;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX048 — Retirement checklist.** What does the retirement checklist cover? *Rubric:* 3 = data deletion, account removal, disconnection;; 2 = all;; 1 = some;; 0 = none.

<a id="ch-17"></a>

## Chapter 17 — Control and feedback basics

### Learning outcomes

You will (1) describe security processes as feedback loops; (2) measure loop delay; (3) avoid unstable responses.

### 17.1 Feedback loops

Control theory studies systems that measure their output and adjust. Lindiwe sees security operations as a loop: sensors produce logs, analysts detect problems, responders act and the environment changes. If any stage is slow, the loop responds late. She maps Saltmarsh's loop for suspicious logins and finds the slowest stage is waiting for an analyst to review alerts overnight. Prof. Hale notes that feedback thinking shows where delay accumulates. She draws the loop with the time each stage takes in the synthetic records, marking the overnight review stage in red for discussion.

### 17.2 Delay

Delay matters because attackers move during it. Lindiwe estimates times from synthetic records: detection within minutes, triage within hours during the day but up to twelve hours overnight, and response shortly after triage. She recommends automated containment for high-confidence alerts, such as locking an account after confirmed password guessing, so the loop closes without waiting for a person. She learns that reducing the slowest delay helps more than speeding up stages already fast. The security lead approves a trial of automated locking for one month.

### 17.3 Stability

Feedback can overreact. If an automated rule locks accounts after a few failed logins, attackers can lock out many staff deliberately, turning a control into a denial of service. Lindiwe proposes gradual responses: slowing login attempts first, then requiring additional verification, and locking only for strong signals. Prof. Hale compares this with damping in control systems, which prevents oscillation. She learns that response strength should match confidence in the signal. The monitoring team adopts the graduated approach and records how often each step is triggered during the trial.

### 17.4 Measuring the loop

Lindiwe proposes measuring the loop routinely: time to detect, time to triage and time to contain, reported monthly. She notes that averages hide long tails, so she reports medians and the slowest tenth. Prof. Hale asks her to define start and end events precisely, because different analysts may record times differently. She learns that measuring a process consistently is the first step towards improving it, a theme that returns in later chapters on measurement. She drafts a monthly report template for the security lead.

### Worked example

Lindiwe maps the login-alert loop, finds overnight triage the slowest stage, proposes automated containment with graduated responses and defines loop metrics.

> **Synthetic case.** Times are synthetic.

### Errors and limits

Aggressive automatic lockouts can become a denial of service.

### Exercises

- **EX049 — Slowest stage.** What is the slowest stage in the loop? *Rubric:* 3 = overnight analyst review;; 2 = correct;; 1 = other;; 0 = none.
- **EX050 — Gradual response.** What comes before locking an account? *Rubric:* 3 = slowing attempts, then extra verification;; 2 = correct;; 1 = vague;; 0 = none.
- **EX051 — Loop metrics.** Which statistics does she report? *Rubric:* 3 = medians and the slowest tenth;; 2 = correct;; 1 = means;; 0 = none.

<a id="ch-18"></a>

## Chapter 18 — Security architecture

### Learning outcomes

You will (1) apply classic design principles; (2) design zones and trust boundaries; (3) evaluate architectures against principles.

### 18.1 Design principles

Lindiwe reads Saltzer and Schroeder's 1975 paper on protecting information in computer systems. It lists principles that still guide architecture: economy of mechanism, fail-safe defaults, complete mediation, open design, separation of privilege, least privilege, least common mechanism and psychological acceptability. She maps them to Saltmarsh. Fail-safe defaults mean new staff get no access until approved; complete mediation means every request is checked, not just the first. She notes the principles are old but widely cited. Prof. Hale asks her to give one Saltmarsh example for every principle.

### 18.2 Zones and boundaries

Lindiwe designs zones for Saltmarsh: an internet-facing zone for the website and driver app interface, an internal zone for staff, a restricted zone for payroll and a management zone for administrators. Traffic between zones passes through controls that enforce rules. She marks trust boundaries on her earlier diagram. Prof. Hale asks her which principle each boundary supports; she identifies least privilege and complete mediation as the main ones. She lists the permitted traffic between each pair of zones in a table, and the network team uses it as the starting rule set.

### 18.3 Evaluating options

Two architecture options exist for the driver app interface: direct access to the dispatch database or an intermediate service exposing only needed functions. Lindiwe evaluates both against the principles. The intermediate service follows least privilege and economy of mechanism better, because the database is never exposed. It adds development work. She records the evaluation in a decision record, and the developers choose the intermediate service. The decision record lists both options, the principles each supports and the estimated extra development time. Prof. Hale praises the record for making the reasoning visible.

### 18.4 Open design

Saltzer and Schroeder argued that security should not depend on attackers not knowing the design. Lindiwe applies this to Saltmarsh's custom file transfer tool, whose security relied on an undocumented port. She recommends authentication and encryption that remain secure even if the design is published. Prof. Hale notes that open design also enables review, since outside experts can examine a published design and find weaknesses before attackers do. The tool is replaced with a standard encrypted transfer service within the year. Its configuration is documented openly for the operations team.

### Worked example

Lindiwe maps Saltzer and Schroeder's principles to Saltmarsh, designs four zones, chooses an intermediate service for least privilege and replaces reliance on secrecy of design.

> **Synthetic case.** Architectures are synthetic.

### Errors and limits

Relying on an undocumented port is obscurity, not protection.

### Exercises

- **EX052 — Fail-safe defaults.** What does fail-safe defaults mean for new staff? *Rubric:* 3 = no access until approved;; 2 = correct;; 1 = vague;; 0 = none.
- **EX053 — Chosen option.** Which option do developers choose? *Rubric:* 3 = the intermediate service;; 2 = correct;; 1 = direct;; 0 = none.
- **EX054 — Open design.** What did the transfer tool rely on? *Rubric:* 3 = an undocumented port;; 2 = correct;; 1 = other;; 0 = none.

<a id="ch-19"></a>

## Chapter 19 — Identity and cryptography

### Learning outcomes

You will (1) manage identities through their lifecycle; (2) apply multi-factor authentication; (3) use cryptography appropriately.

### 19.1 Identity lifecycle

Every account follows a lifecycle: creation when someone joins, changes when they move roles and removal when they leave. Lindiwe finds that Saltmarsh's leavers are removed from the directory but not from the depot routing system, which has its own accounts. She recommends linking all systems to a single identity source so that leaving triggers removal everywhere. Prof. Hale notes that orphaned accounts are a common route for misuse, because nobody notices them being used. The identity team agrees to connect the routing system next quarter.

### 19.2 Multi-factor authentication

Passwords alone are weak because they can be guessed, reused or phished. Multi-factor authentication requires a second factor, such as a code from an app or a hardware key. Lindiwe compares options for Saltmarsh. Hardware keys resist phishing best; app prompts are easier to deploy but can be approved by tired users who accept unexpected requests. She recommends hardware keys for administrators and app codes for other staff, with phishing-resistant methods expanded later. The security lead approves the plan, starting with the twenty administrators.

### 19.3 Cryptographic basics

Lindiwe studies symmetric encryption, where one key encrypts and decrypts, and public-key cryptography, where a public key encrypts or verifies and a private key decrypts or signs. Hash functions produce fixed-length fingerprints of data. She learns that the security of each depends on keeping keys secret and using well-reviewed algorithms and libraries. Prof. Hale warns that designing new cryptographic schemes is a specialist field and that engineers should use established ones. She practises with Python's hashlib module, computing fingerprints for synthetic files.

### 19.4 Key management

Most cryptographic failures come from key handling, not algorithms. Lindiwe reviews how Saltmarsh manages certificates for its websites. Two certificates expired last year, causing outages, because renewal relied on someone remembering. She recommends an inventory of certificates and keys with owners and expiry dates, plus automated renewal where possible. She learns that key management is an operational discipline as much as a technical one. The inventory lists forty certificates in the synthetic export. Six expire within ninety days, and the operations team renews them at once while automation is set up.

### Worked example

Lindiwe links leaver removal to a single identity source, chooses hardware keys for administrators, reviews cryptographic building blocks and proposes a certificate inventory with automated renewal.

> **Synthetic case.** Systems are synthetic.

### Errors and limits

App-based approval prompts can be accepted by users who did not start a login.

### Exercises

- **EX055 — Orphaned accounts.** Where were leavers not removed? *Rubric:* 3 = the depot routing system;; 2 = correct;; 1 = other;; 0 = none.
- **EX056 — Admin factor.** Which factor does she recommend for administrators? *Rubric:* 3 = hardware keys;; 2 = correct;; 1 = other;; 0 = none.
- **EX057 — Certificate outages.** Why did certificates expire? *Rubric:* 3 = renewal relied on memory;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-20"></a>

## Chapter 20 — Information security: engineering context

### Learning outcomes

You will (1) place engineering work within management standards; (2) use control catalogues and frameworks; (3) understand the scope of an information security management system.

### 20.1 Management systems

Lindiwe learns that ISO/IEC 27001:2022 specifies requirements for an information security management system: a structured way to understand context, assess and treat risks, set objectives, operate controls, monitor performance and improve. Saltmarsh is considering certification because large customers ask for it. Prof. Hale explains that the standard asks the organisation to decide which controls it needs based on risk, and to record those decisions in a statement of applicability with reasons for inclusion or exclusion. Lindiwe drafts a sample entry for multi-factor authentication.

### 20.2 Control guidance

ISO/IEC 27002:2022 gives guidance on information security controls, grouped as organisational, people, physical and technological controls. Lindiwe maps her earlier work onto these groups: the monitoring notice is organisational, phishing awareness concerns people, server room power is physical and multi-factor authentication is technological. She notes that ISO/IEC 27002 guides implementation but does not by itself make an organisation compliant with ISO/IEC 27001, which has its own requirements. Prof. Hale asks her to keep the mapping table, because it will help Saltmarsh prepare its statement of applicability later in the course.

### 20.3 NIST resources

Lindiwe also studies NIST resources. The Cybersecurity Framework 2.0 organises outcomes under six functions: Govern, Identify, Protect, Detect, Respond and Recover. NIST SP 800-53 Revision 5 provides a detailed catalogue of controls in families such as access control and audit and accountability. NIST SP 800-12 Revision 1 introduces information security concepts for a general audience. She learns that frameworks express what to achieve, while catalogues describe controls in detail. She keeps a short table showing which resource answers which question: frameworks for outcomes, catalogues for detailed controls and introductions for terminology. Prof. Hale approves the table.

### 20.4 Scope

Before Saltmarsh can build a management system, it must define scope: which sites, systems and processes are included. Lindiwe helps draft a scope covering head office, all depots and the dispatch, payroll and customer systems, but not a subsidiary run separately. Prof. Hale notes that a narrow scope is easier to certify but may mislead customers, so the scope statement must be clear about what is excluded and why. The draft scope is reviewed by the managing director and the subsidiary's own manager, who agrees to follow later.

### Worked example

Lindiwe places her work within ISO/IEC 27001 and 27002, relates it to CSF 2.0 functions and SP 800-53 families and drafts a scope for Saltmarsh's management system.

> **Synthetic case.** The scope is synthetic; standards are paraphrased.

### Errors and limits

Implementing ISO/IEC 27002 guidance alone does not make an organisation ISO/IEC 27001 compliant.

### Exercises

- **EX058 — Applicability statement.** What records control decisions with reasons? *Rubric:* 3 = statement of applicability;; 2 = correct;; 1 = other;; 0 = none.
- **EX059 — Control groups.** Name the four ISO/IEC 27002 control groups. *Rubric:* 3 = organisational, people, physical, technological;; 2 = all;; 1 = some;; 0 = none.
- **EX060 — CSF functions.** Name the six CSF 2.0 functions. *Rubric:* 3 = Govern, Identify, Protect, Detect, Respond, Recover;; 2 = all;; 1 = some;; 0 = none.

<a id="ch-21"></a>

## Chapter 21 — Information security: requirements

### Learning outcomes

You will (1) derive security requirements from risks and obligations; (2) write testable requirements; (3) prioritise requirements by impact.

### 21.1 Sources of requirements

Lindiwe gathers Saltmarsh's security requirements from several sources: risk assessments, customer contracts, data protection law, insurance conditions and the management system scope. A large retail customer requires suppliers to use multi-factor authentication for remote access and to report incidents within twenty-four hours. The insurer requires tested offline backups. She records each requirement with its source, so later readers know why it exists and whether it can change if the source changes, for example when a contract ends. She keeps the list in a shared register.

### 21.2 Testable wording

Many requirements arrive vague, such as systems must be secure. Lindiwe rewrites them so a test can show pass or fail: remote access to internal systems requires a second factor; server disks are encrypted; security patches rated critical are applied within fourteen days. Prof. Hale asks her to avoid words like adequate and appropriate unless a measurable threshold follows. She learns that testable requirements are the bridge between policy and verification, which later chapters depend on. Each rewritten requirement names its owner as well.

### 21.3 Prioritising

Not every requirement matters equally. Lindiwe ranks them by the impact of failure, using the FIPS 199 categories from earlier: requirements protecting high-impact systems such as payroll and dispatch come first. Requirements imposed by contracts with penalties also rank high. She produces a list of twenty requirements in three priority bands. The security lead uses it to plan the year's work, accepting that lower-band items may wait while high-band gaps are fixed. She marks each requirement with its band and source in the register, so the plan can be traced back to the reasons behind it.

### 21.4 Conflicts

Requirements sometimes conflict. The retail customer wants detailed logs kept for a year; data protection principles push towards keeping personal data only as long as necessary. Lindiwe proposes keeping security logs for a year with access restricted to the security team and personal fields minimised where possible. Prof. Hale notes that resolving conflicts openly, with reasons recorded, is better than letting one team quietly ignore a requirement it finds inconvenient. The data protection officer and the security lead both sign the agreed approach, and Lindiwe records it in the decision log with a review date.

### Worked example

Lindiwe collects requirements from risks, contracts, law and insurance, rewrites them as testable statements, ranks them in three bands and resolves a retention conflict.

> **Synthetic case.** Requirements are synthetic.

### Errors and limits

A requirement without a measurable threshold cannot be verified.

### Exercises

- **EX061 — Customer demands.** What does the retail customer require? *Rubric:* 3 = MFA for remote access and 24-hour incident reports;; 2 = correct;; 1 = vague;; 0 = none.
- **EX062 — Patch requirement.** How quickly must critical patches be applied? *Rubric:* 3 = within fourteen days;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX063 — Retention conflict.** How is the log retention conflict resolved? *Rubric:* 3 = a year with restricted access and minimised fields;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-22"></a>

## Chapter 22 — Information security: system and data models

### Learning outcomes

You will (1) build an asset model; (2) reconcile records with observed reality; (3) assign owners to assets.

### 22.1 Why asset models matter

Organisations cannot protect what they do not know they have. Lindiwe builds a model of Saltmarsh's assets: devices, applications, data stores and the relationships between them. The starting point is the asset register maintained by the IT team. Prof. Hale warns that registers drift from reality, as devices are added without registration and old ones linger after removal, so the register must be checked against what is actually on the network before it is trusted. She asks the IT team for its latest register export first.

### 22.2 The reconciliation lab

The lab compares a synthetic register of 2,400 addresses with a synthetic discovery scan that found 2,373 active hosts. Ninety registered addresses did not respond, so they may be retired, switched off or wrongly recorded. Sixty-three hosts that responded were not in the register at all, all on one address range nobody had documented. Of the hosts seen on the network, 97.3 percent were registered. Lindiwe notes that both gaps need investigation, for different reasons. She presents the three figures in one table for the network team, with the unregistered range highlighted for urgent follow-up.

### Lab — Reconciling a synthetic asset register against a synthetic discovery scan

```python
"""Reconcile a synthetic asset register against a synthetic network discovery scan (stdlib only)."""
import random
random.seed(8)
register = {f"10.20.{i//250}.{i%250+1}" for i in range(2400)}
seen = set(random.sample(sorted(register), 2310))                 # 90 registered hosts not seen
unknown = {f"10.30.0.{i}" for i in range(1, 64)}                   # hosts nobody registered
scan = seen | unknown
print(f"register {len(register)}; scan {len(scan)}")
print(f"registered but not seen {len(register - scan)}; seen but unregistered {len(scan - register)}")
print(f"register coverage of scan {len(scan & register)/len(scan):.1%}")
```

Run with `python3 lab_assets.py`. Verified output:

```text
register 2400; scan 2373
registered but not seen 90; seen but unregistered 63
register coverage of scan 97.3%
```

### 22.3 Investigating gaps

The sixty-three unregistered hosts matter most, because unknown devices miss patches and monitoring. Lindiwe asks the network team about the undocumented range and learns it belongs to a depot's camera system installed by a contractor. The ninety silent registered addresses matter less for immediate risk but undermine trust in the register. She proposes checking them against disposal records and marking confirmed retirements. Prof. Hale notes that a single scan can miss devices switched off at the time, so scans should repeat. The camera range is scanned again.

### 22.4 Owners

Every asset needs an owner who decides how it is protected and answers for it. Lindiwe adds an owner field to the model and finds that the camera system has no owner at all, because the contractor left and the depot manager assumed IT was responsible. She arranges for the depot manager to own it, with IT providing support. She learns that ownership gaps often explain technical gaps, since nobody patches what nobody owns. The depot manager signs the ownership record, and the camera system is added to the patching schedule.

### Worked example

Lindiwe reconciles 2,400 registered addresses with 2,373 scanned hosts, finds 90 silent registrations and 63 unregistered cameras, investigates both and assigns an owner.

> **Synthetic case.** Addresses are synthetic; outputs come from lab_assets.py.

### Errors and limits

An asset register that is never reconciled gives false confidence.

### Exercises

- **EX064 — Unregistered hosts.** How many hosts were seen but not registered? *Rubric:* 3 = sixty-three;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX065 — Silent registrations.** How many registered addresses did not respond? *Rubric:* 3 = ninety;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX066 — Camera owner.** Who becomes owner of the camera system? *Rubric:* 3 = the depot manager;; 2 = correct;; 1 = IT;; 0 = none.

<a id="ch-23"></a>

## Chapter 23 — Information security: threat and failure analysis

### Learning outcomes

You will (1) model threats systematically; (2) analyse failure modes; (3) link threats to controls.

### 23.1 Threat modelling

Lindiwe models threats to the dispatch system using a simple method: for each component and data flow, ask how an attacker could spoof identity, tamper with data, deny actions, disclose information, deny service or gain privilege. The driver app interface faces spoofing if drivers' credentials are stolen and tampering if confirmations can be altered. She records each threat with the component, the likely attacker and existing controls, producing a table the developers can act on. The developers review the table during their next planning meeting.

### 23.2 Attackers

Prof. Hale asks her to name realistic attackers rather than imagining a single all-powerful adversary. For Saltmarsh, she lists criminal groups seeking ransom, fraudsters redirecting deliveries of valuable goods, curious insiders and careless mistakes. Each has different goals and skills. Ransom groups target availability and backups; fraudsters target integrity of addresses; insiders target confidentiality of customer data. She learns that naming attackers sharpens priorities, since controls can be matched to the most likely threats. She notes the attacker type beside each threat in her table for clarity.

### 23.3 Failure analysis

Not every harm is malicious. Lindiwe applies failure mode analysis to dispatch: what happens if the database fails, the message queue fills or the mapping service becomes unavailable? For each, she estimates severity and how quickly it would be noticed. A full message queue would silently delay confirmations, so nobody would notice for hours. She recommends monitoring queue length. She learns that security and reliability analysis overlap, since availability failures look similar whatever their cause. The operations team sets an alert when the queue passes a set length.

### 23.4 Linking to controls

Lindiwe links each significant threat and failure to controls: credential theft to multi-factor authentication, address tampering to change alerts and approvals, queue failures to monitoring and ransomware to immutable backups. Some threats have no adequate control yet, such as insiders exporting customer lists. She records these as gaps for the risk register. Prof. Hale notes that an honest list of gaps is more useful than a long list of controls that implies nothing is missing. The security lead adds the insider gap to the risk register with an owner.

### Worked example

Lindiwe models dispatch threats by category, names four realistic attacker types, analyses failure modes such as a full message queue and links threats to controls and gaps.

> **Synthetic case.** Analyses are synthetic.

### Errors and limits

Modelling only one powerful adversary misses common, simpler threats.

### Exercises

- **EX067 — Fraudster target.** What do fraudsters target? *Rubric:* 3 = integrity of delivery addresses;; 2 = correct;; 1 = other;; 0 = none.
- **EX068 — Silent failure.** Which failure would go unnoticed for hours? *Rubric:* 3 = a full message queue;; 2 = correct;; 1 = other;; 0 = none.
- **EX069 — Open gap.** Which threat lacks an adequate control? *Rubric:* 3 = insiders exporting customer lists;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-24"></a>

## Chapter 24 — Information security: methods I

### Learning outcomes

You will (1) plan a security assessment; (2) collect evidence systematically; (3) separate observations from conclusions.

### 24.1 Planning an assessment

Lindiwe plans her first formal assessment of one depot. She writes the scope, objectives, methods, schedule and authorisation, and the depot manager and security lead sign it. Methods include interviews, configuration review, a network scan within the depot's segment and a walk-through of physical controls. Prof. Hale stresses that written authorisation protects both the assessor and the organisation, especially for scans that might disrupt equipment if run carelessly. The plan also states which hours scans may run, avoiding the busy morning dispatch period when the depot's systems carry their heaviest load.

### 24.2 Evidence collection

During the assessment, Lindiwe records evidence with time, source and method: screenshots of configurations, scan outputs and interview notes signed by interviewees. She stores evidence in a restricted folder with checksums so later readers can confirm it has not changed. She learns that conclusions are only as strong as the evidence beneath them, and that recording how evidence was obtained lets others judge its reliability and repeat the checks. She lists every evidence item in an index with its checksum, so a reviewer can pick any item and confirm it matches the original record.

### 24.3 Observations and conclusions

Lindiwe separates what she observed from what she concludes. She observed that the depot's backup drive sits in an unlocked office; she concludes that backups could be stolen or damaged. She observed that two staff share a login on the goods-in terminal; she concludes that actions there cannot be attributed. Prof. Hale explains that this separation lets readers accept the facts even if they weigh the conclusions differently. She applies this layout to every finding in the report. The depot manager later says the separation made the findings easier to accept and act on.

### 24.4 Reporting

Her report lists eight findings, each with evidence, conclusion, risk rating and recommendation. She shares a draft with the depot manager, who corrects one factual error: a door she thought unlocked has a code lock she had missed. She revises the finding. She learns that checking facts with those responsible improves accuracy and acceptance, and that defending an error to protect one's report damages credibility. The final report goes to the security lead and the depot manager. Within a month, six of the eight findings are closed, and the remaining two have agreed dates.

### Worked example

Lindiwe plans and authorises a depot assessment, records evidence with checksums, separates observations from conclusions and corrects a factual error after review.

> **Synthetic case.** The assessment is synthetic.

### Errors and limits

Mixing observations with conclusions makes reports harder to verify.

### Exercises

- **EX070 — Signed plan.** Who signs the assessment plan? *Rubric:* 3 = the depot manager and security lead;; 2 = correct;; 1 = vague;; 0 = none.
- **EX071 — Evidence integrity.** How does she protect evidence integrity? *Rubric:* 3 = checksums in a restricted folder;; 2 = correct;; 1 = vague;; 0 = none.
- **EX072 — Corrected error.** What factual error is corrected? *Rubric:* 3 = a door with a code lock she missed;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-25"></a>

## Chapter 25 — Design studio I

### Learning outcomes

You will (1) design a security improvement under constraints; (2) present options to stakeholders; (3) iterate a design from critique.

### 25.1 The brief

The design studio brief asks Lindiwe's team to secure remote access for Saltmarsh's depot supervisors, who currently connect from home using passwords alone. Constraints include a small budget, supervisors with little technical experience and the retail customer's requirement for a second factor. The team must deliver a design, a cost estimate and a rollout plan within six weeks. Prof. Hale plays the client and challenges each assumption the team makes. The team has four members, each leading one part of the work: design, cost, rollout and documentation.

### 25.2 Options

The team develops three options: a virtual private network with app-based codes, a web portal with hardware keys and a managed remote desktop service with built-in multi-factor authentication. They compare cost, security, ease of use and support burden. The portal with hardware keys resists phishing best but needs keys posted to supervisors. The virtual private network is familiar but gives broad network access once connected, which conflicts with least privilege. The team records the scores for each option in a shared table, so the client can see how each judgement was reached.

### 25.3 Critique

At the mid-point review, Prof. Hale asks what happens when a supervisor loses a key on a Friday evening. The team has no answer. They add a recovery process using a second registered key kept at home and a verified call to the service desk. Classmates also point out that the remote desktop option depends on one supplier. The team records these points and revises their scoring of each option. They also interview two supervisors about their home setups, learning that one shares a computer with family members.

### 25.4 Final design

The team recommends the web portal with two hardware keys per supervisor, access only to the applications supervisors need and a documented recovery process. They estimate the cost per supervisor and a four-week rollout by depot. Prof. Hale praises the recovery process as the part most designs forget. Lindiwe reflects that critique improved the design more than any single technical choice, because it exposed situations nobody had imagined. The client accepts the design, and Saltmarsh's security lead asks to use the recovery process as a template for other services.

### Worked example

Lindiwe's team compares three remote access options, adds a recovery process after critique and recommends a portal with two hardware keys per supervisor.

> **Synthetic case.** The studio brief is synthetic.

### Errors and limits

A strong authentication design without a recovery process fails at the first lost key.

### Exercises

- **EX073 — Studio constraints.** Name one constraint of the brief. *Rubric:* 3 = small budget;; 2 = one;; 1 = vague;; 0 = none.
- **EX074 — VPN drawback.** What drawback does the VPN option have? *Rubric:* 3 = broad network access once connected;; 2 = correct;; 1 = vague;; 0 = none.
- **EX075 — Recovery process.** What recovery process is added? *Rubric:* 3 = second key at home and verified call;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-26"></a>

## Chapter 26 — Information security: architecture alternatives

### Learning outcomes

You will (1) compare perimeter and identity-centred architectures; (2) evaluate cloud and on-premises options; (3) choose an architecture with recorded reasons.

### 26.1 Perimeter models

Saltmarsh's traditional architecture trusts devices inside the network and defends the edge with firewalls. Lindiwe notes that this model weakens when staff work remotely, applications move to cloud services and attackers enter through phishing. Once inside, an attacker inherits trust. Prof. Hale explains that the perimeter remains useful but is no longer sufficient, because the line between inside and outside has blurred for most organisations. Lindiwe illustrates this with a synthetic incident in which a phished laptop on the internal network reached a file share holding payroll exports, because nothing inside the firewall checked who was asking.

### 26.2 Identity-centred models

An alternative checks identity, device health and context for every request, regardless of network location. Lindiwe sketches how Saltmarsh's dispatch application would work: each request is authenticated, the device is checked for current patches and access is limited to the user's role. This approach follows Saltzer and Schroeder's complete mediation principle. She notes it requires mature identity management, device inventory and logging, which Saltmarsh only partly has. She lists the missing capabilities: a complete device inventory, consistent device health reporting and logging for every application access decision.

### 26.3 Cloud and on-premises

Saltmarsh is considering moving payroll to a cloud service. Lindiwe compares security responsibilities: the provider secures its infrastructure, while Saltmarsh remains responsible for user accounts, configuration and data. She lists questions for the provider about encryption, logging, certifications and incident notification. Prof. Hale warns that cloud services shift responsibilities but do not remove them, and that misconfigured cloud storage has caused many exposures. She drafts the provider questionnaire with twelve questions, and the procurement team agrees to send it with the tender documents.

### 26.4 Choosing

Lindiwe recommends a staged approach: keep segmentation and firewalls, move high-value applications behind identity-aware access first and evaluate cloud payroll with a contract review. She records the decision with reasons: risk reduction for remote access, feasibility given current identity maturity and cost. Prof. Hale notes that architecture choices are rarely all-or-nothing, and that a staged path lets an organisation build the capabilities each step requires. The managing director approves the first stage, starting with dispatch and payroll. Lindiwe sets a review after six months to decide whether the next stage should proceed.

### Worked example

Lindiwe compares perimeter and identity-centred models, lists shared responsibilities for cloud payroll and recommends a staged transition with recorded reasons.

> **Synthetic case.** Architectures are synthetic.

### Errors and limits

Moving to a cloud service does not transfer responsibility for accounts and configuration.

### Exercises

- **EX076 — Perimeter weakness.** Why is the perimeter model insufficient? *Rubric:* 3 = attackers inside inherit trust;; 2 = correct;; 1 = vague;; 0 = none.
- **EX077 — Mediation link.** Which principle does identity-centred checking follow? *Rubric:* 3 = complete mediation;; 2 = correct;; 1 = other;; 0 = none.
- **EX078 — Cloud responsibility.** What remains Saltmarsh's responsibility in the cloud? *Rubric:* 3 = accounts, configuration and data;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-27"></a>

## Chapter 27 — Information security: control design

### Learning outcomes

You will (1) design preventive, detective and corrective controls; (2) specify control operation and evidence; (3) assess control cost and effectiveness.

### 27.1 Designing a control

Lindiwe designs a control for address changes in dispatch, responding to the fraud threat identified earlier. Preventive part: changes to delivery addresses for high-value orders require approval by a second person. Detective part: an alert fires when an address changes within an hour of dispatch. Corrective part: suspicious changes are reversed and the customer contacted. Prof. Hale asks her to specify who operates each part and what evidence shows it ran. She writes the design as a one-page control description with owner, frequency and evidence.

### 27.2 Evidence of operation

A control that cannot show it ran cannot be audited. Lindiwe specifies evidence: approval records with both names and times, alert logs with handling notes and a monthly sample review by the security lead. She notes that ISO/IEC 27001 expects organisations to monitor and measure their controls, so evidence is not optional. She learns to design evidence collection into the control from the start, rather than reconstructing it before an audit. The security lead agrees to perform the monthly sample review and to record any exceptions found.

### 27.3 Cost and friction

Second-person approval slows urgent orders. Lindiwe applies the control only to orders above a value threshold, set where the fraud loss would exceed the cost of delay. She estimates that about five percent of orders exceed it. Prof. Hale notes that controls applied universally often get bypassed, while targeted controls remain sustainable. She records the threshold and its reasoning so it can be adjusted as fraud patterns change. The operations manager agrees to the threshold after seeing the estimate, and asks for a review after three months of operation.

### 27.4 Effectiveness

Lindiwe proposes measuring effectiveness: how many suspicious changes the alert catches, how many approvals are rejected and whether fraud losses fall. She notes that rare events make effectiveness hard to measure quickly, so she will also test the control by staging synthetic suspicious changes and checking that alerts fire. She learns that testing with planted cases gives evidence even when real attacks are too rare to count. She plans to stage one synthetic suspicious change each month and record whether the alert fired and how quickly it was handled.

### Worked example

Lindiwe designs a layered address-change control, specifies its evidence, targets it at high-value orders and plans to test it with planted cases.

> **Synthetic case.** Controls are synthetic.

### Errors and limits

A control that leaves no evidence cannot be shown to work.

### Exercises

- **EX079 — Preventive part.** What is the preventive part of the address control? *Rubric:* 3 = second-person approval;; 2 = correct;; 1 = vague;; 0 = none.
- **EX080 — Targeted share.** About what share of orders exceed the threshold? *Rubric:* 3 = about five percent;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX081 — Planted tests.** How is the control tested despite rare fraud? *Rubric:* 3 = staging synthetic suspicious changes;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-28"></a>

## Chapter 28 — Information security: implementation I

### Learning outcomes

You will (1) implement configuration baselines; (2) measure compliance automatically; (3) prioritise remediation from results.

### 28.1 Baselines

Lindiwe turns the hardening checklist from earlier into a baseline that can be checked automatically. She chooses three rules for the first version: remote root login disabled, security patches no older than thirty days and disks encrypted. Each rule is written so a script can read the configuration and return pass or fail. Prof. Hale advises starting with a few rules that matter rather than hundreds that overwhelm the teams receiving the results. The server teams review the three rules before the first run.

### 28.2 The baseline lab

The lab checks a synthetic set of 300 servers. Remote root login is disabled on 278 servers, 92.7 percent. Patches are no older than thirty days on 253, 84.3 percent. Disks are encrypted on 277, 92.3 percent. Only 216 servers, 72.0 percent, pass all three rules. Lindiwe notes that each rule alone looks fairly good, but the combined figure shows that more than a quarter of servers fail at least one requirement. She shares the results with each server team, along with the list of its failing servers, so the teams can begin work immediately rather than waiting for a formal report.

### Lab — Checking 300 synthetic server configurations against three baseline rules

```python
"""Check synthetic server configurations against three hardening baseline rules (stdlib only)."""
import random
random.seed(29)
servers = []
for i in range(300):
    servers.append({
        "ssh_root_login": random.random() < 0.06,      # True = permitted (fail)
        "patch_age_days": int(random.expovariate(1/18)),
        "disk_encrypted": random.random() < 0.93,
    })
r1 = sum(not s["ssh_root_login"] for s in servers)
r2 = sum(s["patch_age_days"] <= 30 for s in servers)
r3 = sum(s["disk_encrypted"] for s in servers)
allp = sum((not s["ssh_root_login"]) and s["patch_age_days"] <= 30 and s["disk_encrypted"] for s in servers)
n = len(servers)
print(f"root login disabled {r1}/{n} ({r1/n:.1%}); patched within 30 days {r2}/{n} ({r2/n:.1%}); disk encrypted {r3}/{n} ({r3/n:.1%})")
print(f"all three rules {allp}/{n} ({allp/n:.1%})")
```

Run with `python3 lab_baseline.py`. Verified output:

```text
root login disabled 278/300 (92.7%); patched within 30 days 253/300 (84.3%); disk encrypted 277/300 (92.3%)
all three rules 216/300 (72.0%)
```

### 28.3 Prioritising remediation

Lindiwe sorts failures by server category. Servers in high-impact systems such as payroll come first, then those exposed to the internet. Within each group, she fixes the quickest items first: disabling root login takes minutes, while encrypting an existing disk requires downtime. Prof. Hale notes that combining impact with effort produces a plan teams can follow week by week, instead of a single large list that discourages action. The teams agree to close all root login failures within a week and to plan encryption over the next quarter.

### 28.4 Keeping compliance

Compliance measured once decays. Lindiwe schedules the check to run weekly and report the percentage passing all rules, broken down by team. She adds new rules gradually, each announced in advance. Teams can see their own trend. She learns that automated, repeated measurement turns a baseline from a document into an operating control, and that transparency about each team's results encourages improvement without needing a formal audit. After three months, she plans to compare each team's trend with the starting figure of 72.0 percent and report progress to the security lead.

### Worked example

Lindiwe implements three baseline rules, finds 72.0 percent of 300 servers pass all three, prioritises by impact and effort and schedules weekly checks.

> **Synthetic case.** Servers are synthetic; outputs come from lab_baseline.py.

### Errors and limits

Reporting each rule alone can hide how many servers fail at least one.

### Exercises

- **EX082 — Root login rate.** What share has remote root login disabled? *Rubric:* 3 = 278, 92.7 percent;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX083 — Patch rate.** What share is patched within thirty days? *Rubric:* 3 = 253, 84.3 percent;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX084 — All three.** How many servers pass all three rules? *Rubric:* 3 = 216, 72.0 percent;; 2 = correct;; 1 = wrong;; 0 = none.

<a id="ch-29"></a>

## Chapter 29 — Information security: measurement

### Learning outcomes

You will (1) design a detection measure; (2) distinguish attack patterns from benign noise; (3) report detection results honestly.

### 29.1 Measuring password guessing

Saltmarsh wants to know how often accounts face password guessing. Lindiwe defines a measure: an account is flagged if it has ten or more failed logins within any five-minute window. Ordinary mistyping produces a few failures spread across a day, while guessing produces many in quick succession. She chooses the window and threshold before looking at data, and records them so later results can be compared with the same definition. The security lead approves the definition before Lindiwe runs it on any data.

### 29.2 The login lab

The lab builds a synthetic day of 1,672 failed logins across 863 accounts. Three accounts are flagged: u17, u402 and u977, with 40, 42 and 40 failures respectively, all in short bursts. The account with the most failures overall, u1200, has 61, but they are spread every few minutes across the day, so it is not flagged. Lindiwe investigates and finds a broken synchronisation client retrying with an old password. She records the explanation beside the account in her report, so nobody mistakes the client's failures for an attack. The service desk confirms the user had changed her password the previous week.

### Lab — Detecting password-guessing bursts in a synthetic authentication log

```python
"""Detect password-guessing bursts in a synthetic authentication log (stdlib only)."""
import random
from collections import defaultdict
random.seed(5)
events = []
for u in range(1500):                                  # ordinary mistyping
    for _ in range(random.choice([0, 0, 0, 1, 1, 2, 3])):
        events.append((f"u{u}", random.uniform(0, 86400)))
for u in ["u17", "u402", "u977"]:                      # guessing bursts
    start = random.uniform(0, 80000)
    events += [(u, start + random.uniform(0, 240)) for _ in range(40)]
for u in ["u1200"]:                                    # a broken sync client retrying slowly
    events += [(u, k * 400.0) for k in range(60)]
by = defaultdict(list)
for u, t in events: by[u].append(t)
flag = []
for u, ts in by.items():
    ts.sort()
    if any(ts[j + 9] - ts[j] <= 300 for j in range(len(ts) - 9)):
        flag.append(u)
total = sorted(by, key=lambda u: -len(by[u]))[:4]
print(f"failed logins {len(events)}; accounts with failures {len(by)}")
print(f"flagged (10 failures within 5 min): {sorted(flag)}")
print(f"top accounts by total failures: {[(u, len(by[u])) for u in total]}")
```

Run with `python3 lab_logins.py`. Verified output:

```text
failed logins 1672; accounts with failures 863
flagged (10 failures within 5 min): ['u17', 'u402', 'u977']
top accounts by total failures: [('u1200', 61), ('u402', 42), ('u17', 40), ('u977', 40)]
```

### 29.3 Why rate beats total

Ranking accounts by total failures would have put the broken client first and mixed it with real guessing. The window measure separates fast guessing from slow retries. Lindiwe notes that attackers can also guess slowly to avoid detection, so the measure catches noisy attacks but not patient ones. She adds a second, weaker indicator: accounts with failures from many different addresses in a day. Prof. Hale appreciates that she states what the measure cannot see. She documents both indicators together in one short note.

### 29.4 Reporting

Lindiwe reports the three flagged accounts to the security team, which resets their passwords and confirms multi-factor authentication is enabled. She also reports the broken client to the service desk, which fixes it. Her monthly report shows the number of flagged accounts, the definition used and its known blind spot. She learns that a measure is useful only when its definition and limits travel with the number. The security lead circulates the report to the IT managers each month, and the definition is added to the security metrics handbook.

### Worked example

Lindiwe flags three accounts with bursts of 40 to 42 failures among 1,672 failed logins, separates a slow-retrying client with 61 failures and reports the measure with its blind spot.

> **Synthetic case.** Logs are synthetic; outputs come from lab_logins.py.

### Errors and limits

Ranking by total failures confuses broken clients with attacks.

### Exercises

- **EX085 — Flagged accounts.** Which accounts are flagged? *Rubric:* 3 = u17, u402 and u977;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX086 — Top account.** Why is u1200 not flagged? *Rubric:* 3 = failures spread across the day;; 2 = correct;; 1 = vague;; 0 = none.
- **EX087 — Blind spot.** What does the window measure miss? *Rubric:* 3 = slow, patient guessing;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-30"></a>

## Chapter 30 — Verification laboratory I

### Learning outcomes

You will (1) verify controls with planned tests; (2) record test evidence; (3) distinguish test failure from control failure.

### 30.1 Test plan

In the verification laboratory, Lindiwe writes a test plan for four controls she helped build: the baseline check, the password-guessing measure, the address-change alert and the asset reconciliation. For each, she defines inputs, expected results and pass criteria. The baseline check should fail a planted server with root login enabled; the guessing measure should flag a planted burst of ten failures in four minutes. Prof. Hale approves the plan before testing starts. Each test is listed with its planted input and the expected outcome in one table.

### 30.2 Running tests

Lindiwe runs the tests on synthetic data. The baseline check correctly fails the planted server. The guessing measure flags the planted burst and ignores a planted slow sequence, as intended. The address alert fires for a planted change one hour before dispatch. The asset reconciliation correctly lists a planted unregistered host. She records each run with date, inputs, outputs and the version of each script, so results can be reproduced. All four controls pass their first planned cases. She stores the planted inputs alongside the scripts.

### 30.3 A failed test

One test fails: a planted burst of exactly ten failures spanning precisely five minutes is not flagged. Lindiwe examines the code and finds the comparison treats the boundary inconsistently with her written definition. She corrects the code, reruns all tests and confirms the planted case is now flagged and the earlier results unchanged. Prof. Hale notes that boundary cases are where definitions and code most often disagree. She adds the boundary case to the permanent test set, so the same mistake would be caught again. The fix is a single changed comparison.

### 30.4 Test versus control

Lindiwe reflects on what the failed test meant. The control itself, detecting guessing, was sound; the implementation had a boundary error. Had the test not existed, a real attack exactly at the boundary would have been missed. She writes in her laboratory report that tests verify implementations against definitions, and that keeping planted test cases permanently lets future changes be checked quickly. Prof. Hale asks her to present this example to the class, because it shows clearly why verification needs planned cases at every boundary rather than only typical inputs.

### Worked example

Lindiwe tests four controls with planted cases, finds a boundary error in the guessing measure, fixes it and reruns all tests.

> **Synthetic case.** Tests are synthetic.

### Errors and limits

Untested boundary cases often reveal disagreement between definition and code.

### Exercises

- **EX088 — Planted burst.** What planted burst should be flagged? *Rubric:* 3 = ten failures in four minutes;; 2 = correct;; 1 = vague;; 0 = none.
- **EX089 — Failing test.** Which planted case failed at first? *Rubric:* 3 = ten failures spanning exactly five minutes;; 2 = correct;; 1 = vague;; 0 = none.
- **EX090 — Permanent tests.** Why keep planted cases permanently? *Rubric:* 3 = to check future changes quickly;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-31"></a>

## Chapter 31 — Information security: implementation II

### Learning outcomes

You will (1) roll out multi-factor authentication at scale; (2) manage exceptions; (3) track adoption against a plan.

### 31.1 Rollout plan

In her fourth year, Lindiwe helps implement the multi-factor authentication plan approved earlier. Administrators come first with hardware keys, then office staff with app codes, then warehouse staff, who share terminals and need a different approach. She writes a schedule by depot, with training sessions, help desk preparation and a date after which passwords alone stop working. Prof. Hale asks her to plan communication as carefully as configuration, because surprised users generate support calls and workarounds. The security lead approves the schedule and the training dates.

### 31.2 Warehouse terminals

Warehouse staff use shared terminals with gloves on, so phone prompts are impractical. Lindiwe's team tests short-lived badge tap logins combined with a personal code, so each person is identified individually and shared accounts disappear. The test depot reports faster logins than the old shared password. She learns that security improvements that also remove friction spread quickly, while those that add friction need strong justification and support to be accepted by busy staff. The badge readers are added to every warehouse terminal over the following two months.

### 31.3 Exceptions

Some accounts cannot use multi-factor authentication immediately: an old scanner integration and two service accounts used by suppliers. Lindiwe records each exception with an owner, a reason, compensating controls such as network restrictions and an expiry date. Prof. Hale explains that exceptions without expiry dates become permanent weaknesses. She sets reminders three weeks before each expiry so owners must either fix the issue or justify an extension to the security lead. The scanner integration's exception is closed after three months, when the supplier delivers an update supporting certificates.

### 31.4 Tracking adoption

Lindiwe tracks adoption weekly: the share of accounts enrolled, the share of logins using a second factor and the number of open exceptions. Adoption among administrators reaches all accounts in the first fortnight, office staff follow over two months and warehouse depots move one at a time. She reports progress against the plan to the security lead. She notes that counting enrolments alone could mislead, since enrolled users might still log in with old methods until those are disabled. Disabling old methods follows.

### Worked example

Lindiwe phases multi-factor rollout by group, uses badge taps for warehouse terminals, records exceptions with expiry dates and tracks both enrolment and actual second-factor use.

> **Synthetic case.** The rollout is synthetic.

### Errors and limits

Exceptions without expiry dates become permanent weaknesses.

### Exercises

- **EX091 — Rollout order.** Which group comes first? *Rubric:* 3 = administrators with hardware keys;; 2 = correct;; 1 = other;; 0 = none.
- **EX092 — Warehouse method.** How do warehouse staff log in? *Rubric:* 3 = badge tap with a personal code;; 2 = correct;; 1 = vague;; 0 = none.
- **EX093 — Adoption measures.** What three adoption measures are tracked? *Rubric:* 3 = enrolled share, second-factor logins, open exceptions;; 2 = all;; 1 = some;; 0 = none.

<a id="ch-32"></a>

## Chapter 32 — Information security: reliability

### Learning outcomes

You will (1) verify backup integrity with checksums; (2) measure restore success; (3) set recovery objectives.

### 32.1 Restores as evidence

Saltmarsh believes its backups work because backup jobs report success. Lindiwe explains that a successful backup job shows data were copied, not that they can be restored intact. She proposes regular restore tests that compare restored files against checksums recorded at backup time. If a file is missing or its checksum differs, the restore has failed for that file. Prof. Hale notes that only restore testing gives evidence for the insurer's requirement of tested backups. The security lead schedules the first restore test for the following month.

### 32.2 The restore lab

The lab creates 500 synthetic files, records a SHA-256 checksum for each using Python's hashlib module and simulates a restore. Five files are missing from the restore and three have checksum mismatches caused by a single flipped bit. That leaves 492 files verified, 98.4 percent. Lindiwe notes that the backup job would have reported success, and that without checksums the three corrupted files would look normal until someone opened them. She shows the security lead the list of missing and corrupted files, and the team agrees to run the same verification monthly on a rotating sample of folders from every server.

### Lab — Verifying synthetic backup restores against SHA-256 checksums

```python
"""Verify synthetic backup restores against SHA-256 checksums (stdlib only)."""
import hashlib, random
random.seed(12)
files = {f"file{i}": random.randbytes(256) for i in range(500)}
manifest = {k: hashlib.sha256(v).hexdigest() for k, v in files.items()}
restored = {}
for k, v in files.items():
    r = random.random()
    if r < 0.006: continue                                    # missing from restore
    if r < 0.014: v = v[:-1] + bytes([v[-1] ^ 1])            # one bit flipped
    restored[k] = v
missing = [k for k in files if k not in restored]
bad = [k for k in restored if hashlib.sha256(restored[k]).hexdigest() != manifest[k]]
ok = len(files) - len(missing) - len(bad)
print(f"files {len(files)}; missing {len(missing)}; checksum mismatch {len(bad)}; verified {ok} ({ok/len(files):.1%})")
```

Run with `python3 lab_restore.py`. Verified output:

```text
files 500; missing 5; checksum mismatch 3; verified 492 (98.4%)
```

### 32.3 Investigating failures

Lindiwe traces the five missing files to a folder added after the backup selection was configured, so it was never included. The three corrupted files come from a failing disk on the backup server. Both causes are fixable: the selection is changed to include all folders under a parent, and the disk is replaced. She learns that restore tests find configuration and hardware problems that monitoring of backup jobs alone cannot reveal. The next monthly restore test, run after both fixes, verifies every file in its sample.

### 32.4 Recovery objectives

Lindiwe helps Saltmarsh set recovery objectives: how much data the business can afford to lose and how quickly each system must return. Dispatch can lose at most an hour of data and must return within four hours; payroll can lose a day but must be back before pay runs. These objectives decide backup frequency and restore methods. Prof. Hale notes that objectives agreed with business owners turn backups from a technical habit into a commitment. The objectives are approved by the operations director and the finance director.

### Worked example

Lindiwe verifies a synthetic restore of 500 files with SHA-256 checksums, finds 5 missing and 3 corrupted (492 verified, 98.4 percent), traces causes and sets recovery objectives.

> **Synthetic case.** Files are synthetic; outputs come from lab_restore.py.

### Errors and limits

A successful backup job does not prove data can be restored intact.

### Exercises

- **EX094 — Restore figures.** How many files were verified? *Rubric:* 3 = 492, 98.4 percent;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX095 — Missing cause.** Why were five files missing? *Rubric:* 3 = a folder added after selection was configured;; 2 = correct;; 1 = vague;; 0 = none.
- **EX096 — Dispatch objectives.** What are dispatch's recovery objectives? *Rubric:* 3 = lose at most an hour, return within four hours;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-33"></a>

## Chapter 33 — Information security: safety and resilience

### Learning outcomes

You will (1) plan for continued operation during incidents; (2) design manual fallbacks; (3) exercise resilience plans.

### 33.1 Resilience

Resilience means continuing essential work during disruption and recovering quickly. Lindiwe asks Saltmarsh's operations managers what must continue if systems fail: refrigerated medicine deliveries, payroll and customer communication. She builds a list of essential services with the systems each depends on. Prof. Hale explains that resilience planning starts from services the business cannot stop, not from systems, because several systems often support one service and one system can support several. Lindiwe records the services in a table with their dependent systems and the longest tolerable outage for each, as agreed with the managers.

### 33.2 Manual fallbacks

If dispatch fails, depots cannot print delivery lists. Lindiwe works with depot supervisors to design a manual fallback: a nightly printed list of the next day's deliveries kept in a locked cabinet, and paper confirmation forms entered later. For refrigerated loads, drivers carry independent temperature loggers that do not depend on the network. She learns that the best fallbacks are simple, practised and independent of the systems they replace. The supervisors test the printed list and paper forms during one quiet Sunday shift, and drivers find the forms easy to complete.

### 33.3 Exercises

Plans that are never exercised often fail. Lindiwe organises a tabletop exercise: ransomware has encrypted the dispatch server on a Monday morning. Managers walk through their actions. They discover that nobody knows where the printed lists are kept at one depot and that the incident contact list contains two people who have left. Prof. Hale notes that finding such problems in an exercise is exactly the purpose, and that every exercise should produce a short list of improvements. The improvements list has seven items.

### 33.4 Safety and integrity

Lindiwe returns to the safety concern from her first year: temperature records for medicines. During a cyber incident, records might be lost or altered. She recommends that drivers' independent loggers be read at delivery and their results kept separately, so evidence of safe temperatures survives a system compromise. The fleet manager accepts the recommendation. She learns that resilience for safety-related data needs independent evidence, not just backups of the same system. Lindiwe adds this requirement to the resilience plan, and the fleet team includes it in driver training.

### Worked example

Lindiwe identifies essential services, designs printed and independent fallbacks, runs a ransomware tabletop exercise that exposes outdated contacts and protects temperature evidence independently.

> **Synthetic case.** Plans and exercises are synthetic.

### Errors and limits

A resilience plan that has never been exercised usually contains outdated details.

### Exercises

- **EX097 — Essential services.** Name one essential service identified. *Rubric:* 3 = refrigerated medicine deliveries;; 2 = one;; 1 = vague;; 0 = none.
- **EX098 — Exercise discovery.** What did the exercise reveal? *Rubric:* 3 = missing printed lists location and outdated contacts;; 2 = correct;; 1 = vague;; 0 = none.
- **EX099 — Temperature evidence.** How is temperature evidence protected? *Rubric:* 3 = independent loggers read at delivery;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-34"></a>

## Chapter 34 — Information security: integration

### Learning outcomes

You will (1) secure integrations between systems and partners; (2) manage application programming interface credentials; (3) monitor data exchanged with third parties.

### 34.1 Partner integrations

Saltmarsh exchanges data with retailers, carriers and a payroll bureau through automated interfaces. Lindiwe lists each integration with its data, direction, authentication method and owner. She finds that one carrier connection uses a fixed password sent in each request over an encrypted channel, while another uses certificates. Prof. Hale notes that integrations are easily forgotten after setup and often hold broad access, making them attractive to attackers. She completes the list for eleven integrations and confirms an owner for each with the relevant business manager.

### 34.2 Credentials for interfaces

Interface credentials need the same care as staff passwords. Lindiwe recommends that each integration have its own credential, limited to the operations it needs, stored in a managed secret store and rotated on a schedule. She discovers that two carriers share one credential, so revoking access for one would break the other. Separating them takes a week of coordination but means each partner can be managed independently in future. She moves both credentials into the managed secret store and sets rotation every ninety days.

### 34.3 Data minimisation

The payroll bureau receives full employee records, including emergency contacts it does not need. Lindiwe reviews the fields with the human resources team and removes six unnecessary ones from the export. She explains that every field shared is a field that can leak from the partner's systems, and that minimising data shared reduces Saltmarsh's exposure without any technical control. The bureau confirms the reduced export meets its needs. The human resources team updates the export specification and records the reasons for each removed field.

### 34.4 Monitoring exchanges

Lindiwe sets up monitoring for interfaces: volumes per partner per day, error rates and unusual request patterns. A sudden rise in requests for customer addresses from one retailer's credential would suggest misuse. She sets thresholds from three months of synthetic history. Prof. Hale asks who responds to an alert at weekends; she adds the integration owner to the on-call rota so alerts have a clear recipient. The first month produces two alerts, both explained by planned promotions at one retailer, and she adjusts the thresholds accordingly.

### Worked example

Lindiwe inventories partner integrations, separates a shared carrier credential, removes six unneeded payroll fields and monitors interface volumes with a named responder.

> **Synthetic case.** Integrations are synthetic.

### Errors and limits

A credential shared between partners cannot be revoked for one without affecting the other.

### Exercises

- **EX100 — Shared credential.** What problem did two carriers create? *Rubric:* 3 = they shared one credential;; 2 = correct;; 1 = vague;; 0 = none.
- **EX101 — Removed fields.** How many unnecessary fields were removed? *Rubric:* 3 = six;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX102 — Misuse signal.** What would suggest misuse of a retailer credential? *Rubric:* 3 = sudden rise in address requests;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-35"></a>

## Chapter 35 — Design studio II

### Learning outcomes

You will (1) design a security monitoring capability; (2) justify design choices with evidence; (3) present a design to decision-makers.

### 35.1 The brief

The second design studio asks Lindiwe's team to design security monitoring for Saltmarsh within a fixed annual budget. Options range from an in-house team, which Saltmarsh cannot staff around the clock, to an external managed service. The design must use the detection measures already built, meet the retail customer's twenty-four-hour incident reporting requirement and protect staff privacy as promised in the monitoring notice. The team has eight weeks and must present to a panel acting as the board, with a written design, a cost estimate and a one-page summary.

### 35.2 Evidence for choices

The team uses evidence gathered across the course: the event rates from the first year, the loop delays measured in control and feedback work and the false alarm calculation from statistics. They estimate alert volumes and the analyst time needed. In-house monitoring would need at least five analysts for continuous cover, which exceeds the budget. A hybrid design, with an external service at night and Saltmarsh staff during the day, fits. They show the calculation in an appendix so the panel can check every step.

### 35.3 Privacy safeguards

The team designs safeguards: browsing logs visible only to the security team, external analysts seeing pseudonymous account identifiers until an incident is confirmed and quarterly reviews of who accessed logs. Prof. Hale challenges whether pseudonyms slow investigations; the team shows that the mapping can be revealed by an on-call Saltmarsh manager within minutes. Classmates consider this a sensible balance between privacy and response speed. The team writes the safeguards as clauses for the external provider contract, so they are enforceable rather than informal promises.

### 35.4 Presenting

The team presents to a panel acting as Saltmarsh's board. They lead with the business problem, the twenty-four-hour obligation and night-time gaps, then show options, costs and risks. The panel asks what happens if the external provider misses an alert; the team points to contract terms and monthly sample reviews. Lindiwe learns that decision-makers want consequences and trade-offs explained clearly, with technical detail available but not leading. The panel approves the hybrid design for further costing, and Prof. Hale grades the presentation highly for clarity.

### Worked example

Lindiwe's team uses earlier measurements to size monitoring, chooses a hybrid model within budget, adds pseudonymisation with quick reveal and presents risks and costs to a mock board.

> **Synthetic case.** The studio is synthetic.

### Errors and limits

Designing monitoring without estimating alert volume leads to understaffed teams.

### Exercises

- **EX103 — In-house staff.** How many analysts would in-house continuous cover need? *Rubric:* 3 = at least five;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX104 — Hybrid model.** What is the hybrid model? *Rubric:* 3 = external at night, Saltmarsh staff by day;; 2 = correct;; 1 = vague;; 0 = none.
- **EX105 — Pseudonym reveal.** Who can reveal pseudonymous identities? *Rubric:* 3 = an on-call Saltmarsh manager;; 2 = correct;; 1 = analysts;; 0 = none.

<a id="ch-36"></a>

## Chapter 36 — Information security: performance and scale

### Learning outcomes

You will (1) assess the performance cost of security controls; (2) scale security processing with growth; (3) test controls under load.

### 36.1 Cost of controls

Security controls consume resources. Encryption uses processor time, logging uses storage and network capacity, and inspection adds latency. Lindiwe measures a synthetic test: enabling full-disk encryption on modern laptops adds a small processing overhead that users do not notice, while inspecting all encrypted web traffic at the depot firewall roughly doubles its processor load. She recommends inspecting only categories of traffic with clear risk, rather than everything. The network team adopts the selective approach and documents exactly which traffic categories are inspected.

### 36.2 Scaling logs

Saltmarsh plans three new depots. Lindiwe uses her first-year model to estimate the extra events per day and checks whether the log collector can handle them. At current growth, the collector reaches capacity within eighteen months. She proposes filtering low-value events at the source and adding a second collector before the limit. Prof. Hale notes that security systems that silently drop data under load are worse than those that fail loudly. The infrastructure team adds the second collector to next year's budget.

### 36.3 Load testing

Lindiwe tests the password-guessing measure at ten times today's log volume using synthetic data. It completes in a few seconds, well within the reporting window. She also tests the asset reconciliation with ten thousand hosts; it remains fast because it uses set operations. She records the tests so future growth can be checked against them. She learns that standard library tools scale well for moderate volumes when algorithms are chosen sensibly. The test records include data sizes and run times for each script.

### 36.4 Trade-offs at scale

As volumes grow, Saltmarsh must choose between keeping all detail and reducing cost. Lindiwe proposes keeping full authentication and administrative events, which are central to investigations, while summarising routine firewall allow events after thirty days. She documents which investigation questions become harder to answer after summarisation. The security lead accepts the proposal with a review after one year, recognising that the trade-off may need adjusting. She lists the affected questions in an appendix to the retention policy, so investigators know in advance what detail remains available.

### Worked example

Lindiwe measures control overhead, finds the log collector reaches capacity in eighteen months, load-tests detection at ten times volume and proposes keeping full authentication events while summarising routine firewall logs.

> **Synthetic case.** Measurements are synthetic.

### Errors and limits

Security systems that silently drop data under load give false assurance.

### Exercises

- **EX106 — Inspection cost.** What does inspecting all encrypted traffic do? *Rubric:* 3 = roughly doubles firewall processor load;; 2 = correct;; 1 = vague;; 0 = none.
- **EX107 — Collector capacity.** When does the collector reach capacity? *Rubric:* 3 = within eighteen months;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX108 — Kept events.** Which events are kept in full? *Rubric:* 3 = authentication and administrative events;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-37"></a>

## Chapter 37 — Information security: operations

### Learning outcomes

You will (1) run security operations routines; (2) handle incidents with a defined process; (3) learn from incidents without blame.

### 37.1 Daily routines

Security operations at Saltmarsh run on routines: reviewing overnight alerts, checking failed backups, reviewing new exceptions and confirming that scheduled checks ran. Lindiwe writes a checklist for the morning shift and times it at about forty minutes. Prof. Hale notes that routines catch drift before it becomes an incident, and that written checklists let new staff cover absences without missing steps that experienced staff perform from memory. She tests the checklist with two analysts during their first week, and both complete it without needing help from experienced colleagues.

### 37.2 Incident handling

Lindiwe helps write Saltmarsh's incident process using the Detect, Respond and Recover functions of the NIST Cybersecurity Framework 2.0 as a guide, with practical steps to analyse, contain, eradicate, recover and report. Each step has an owner and a template. When a synthetic incident occurs, a phished account sending invoices to customers, the team follows the process: they lock the account, remove forwarding rules, warn customers and report to the retail customer within the required twenty-four hours. The whole incident is closed within two days, and Lindiwe records the timeline in the incident register.

### 37.3 Post-incident review

After the incident, Lindiwe facilitates a review. The question is not who clicked, but why the attack succeeded and how to make it harder. The review finds that the account lacked multi-factor authentication because it was on an exception list whose expiry had been extended twice without review. The fix is a rule that second extensions need the security lead's approval. She learns that blameless reviews uncover process weaknesses that blame would hide. The security lead approves the new rule the same week.

### 37.4 Metrics

Lindiwe reports operational metrics monthly: alerts handled, median time to contain, open exceptions, baseline compliance and restore test results. She avoids targets that encourage gaming, such as rewarding fewer alerts, which could be met by turning detection off. Prof. Hale explains that good security metrics describe the state of controls and the speed of response, and that context should always accompany numbers sent to managers. She includes a short commentary with each monthly report explaining any significant change, so readers do not misread a rise in alerts as a decline in security.

### Worked example

Lindiwe writes a forty-minute morning checklist, runs a phished-account incident through a defined process, holds a blameless review finding a repeatedly extended exception and reports balanced metrics.

> **Synthetic case.** The incident is synthetic.

### Errors and limits

Rewarding fewer alerts can encourage turning detection off.

### Exercises

- **EX109 — Checklist length.** How long does the morning checklist take? *Rubric:* 3 = about forty minutes;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX110 — Incident actions.** Name one containment action taken. *Rubric:* 3 = locking the account;; 2 = one;; 1 = vague;; 0 = none.
- **EX111 — Root cause.** Why did the account lack multi-factor authentication? *Rubric:* 3 = an exception extended twice without review;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-38"></a>

## Chapter 38 — Information security: validation

### Learning outcomes

You will (1) validate that controls meet business needs; (2) gather user and owner feedback; (3) distinguish verification from validation.

### 38.1 Verification and validation

Lindiwe distinguishes two questions. Verification asks whether a control was built as specified; her laboratory tests answered that. Validation asks whether the control meets the real need. The password-guessing measure works as specified, but does it help Saltmarsh reduce account takeover? She designs validation activities: interviews with the security team about alert usefulness, review of incidents to see whether measures detected them and comparison with business objectives. Prof. Hale asks her to apply these activities to every control built during the course and to report the results together.

### 38.2 Owner feedback

Lindiwe interviews system owners about the controls affecting them. The dispatch owner finds the address-change approval useful but says the threshold catches some regular large customers unnecessarily. The payroll owner wants clearer baseline reports. She records each point and proposes adjustments. Prof. Hale notes that owners' views reveal whether controls fit the work, which tests alone cannot show, and that controls owners dislike are often quietly weakened. She raises the threshold slightly for customers with a verified history and records the change with its reasoning.

### 38.3 Incident review evidence

Lindiwe reviews six synthetic incidents from the year. Four were detected by controls built during the course, one by a customer complaint and one by an external notification. The two missed detections point to gaps: no monitoring of email forwarding rules and no alert for bulk downloads from the customer portal. She adds both to the improvement plan. She learns that incidents provide the most direct validation evidence. The two gaps are assigned named owners and target dates in the improvement plan.

### 38.4 Validation report

Her report states for each control whether it is verified, validated, partially validated or not yet validated, with evidence. The password-guessing measure is validated by two detected incidents; the address-change control is verified but not yet validated because no fraud attempt has occurred. Prof. Hale praises the honest distinction. She notes that claiming validation without evidence would mislead the board about how well the controls protect the business. The report is presented to Saltmarsh's security committee, which asks for a repeat assessment after six months.

### Worked example

Lindiwe distinguishes verification from validation, gathers owner feedback, finds two detection gaps from six incidents and reports each control's validation status with evidence.

> **Synthetic case.** Incidents are synthetic.

### Errors and limits

A control can be built correctly and still fail to meet the real need.

### Exercises

- **EX112 — Detected incidents.** How many of six incidents did course controls detect? *Rubric:* 3 = four;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX113 — Missed gaps.** Name one detection gap found. *Rubric:* 3 = email forwarding rules;; 2 = one;; 1 = vague;; 0 = none.
- **EX114 — Address status.** What is the address-change control's status? *Rubric:* 3 = verified but not yet validated;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-39"></a>

## Chapter 39 — Information security: maintainability

### Learning outcomes

You will (1) keep security tools maintainable; (2) document controls for successors; (3) plan for staff turnover.

### 39.1 Maintainable code

Lindiwe's scripts now run Saltmarsh's baseline checks, guessing measure and restore tests. She will leave at the end of her course, so others must maintain them. She reviews her code for clarity: descriptive names, comments explaining why rather than what, tests for every rule and a single configuration file for thresholds. Prof. Hale notes that security tooling often fails when its author leaves, because nobody understands it well enough to change it safely. She also removes two unused functions found during the review.

### 39.2 Runbooks

For each control, Lindiwe writes a runbook: purpose, schedule, inputs, how to read results, common problems and who to contact. The restore test runbook explains what to do when checksums mismatch, including checking disk health and rerunning the restore. She asks a colleague with no involvement to follow each runbook. Two steps prove unclear and she rewrites them. She learns that documentation is tested by use, not by the author's reading. The final runbooks are stored with the scripts in version control.

### 39.3 Ownership transfer

Lindiwe arranges owners for each tool within Saltmarsh's IT team and holds handover sessions. Each owner runs the tool once with her watching, then once alone. She updates the asset model and decision records to name the new owners. Prof. Hale explains that ownership transfer is a control in its own right: without it, tools become orphaned, just like the camera system she found in her third year. The new owners sign the handover records, and Lindiwe remains available by email for questions during her final term.

### 39.4 Dependency on people

Lindiwe notes that some controls depend on single individuals, such as the security lead's monthly sample review. If that person is absent, the control stops. She recommends deputies for each person-dependent control and records them in the runbooks. She learns that maintainability applies to processes and people as well as code, and that resilience against staff absence is part of security engineering. Each deputy performs the control once during the handover period, and the runbooks record their names and the dates on which they last performed it, so the security lead can see who is ready.

### Worked example

Lindiwe improves code clarity, writes runbooks tested by a colleague, transfers tool ownership with supervised runs and adds deputies for person-dependent controls.

> **Synthetic case.** Tools and staff are synthetic.

### Errors and limits

Tools whose authors leave without handover become unmaintained.

### Exercises

- **EX115 — Configuration.** Where are thresholds kept? *Rubric:* 3 = a single configuration file;; 2 = correct;; 1 = code;; 0 = none.
- **EX116 — Runbook test.** How are runbooks tested? *Rubric:* 3 = a colleague follows each one;; 2 = correct;; 1 = vague;; 0 = none.
- **EX117 — Deputies.** Why add deputies? *Rubric:* 3 = controls stop when one person is absent;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-40"></a>

## Chapter 40 — Verification laboratory II

### Learning outcomes

You will (1) verify controls end to end; (2) test detection with simulated attacks; (3) record results for an evidence dossier.

### 40.1 End-to-end tests

In the second verification laboratory, Lindiwe tests controls from event to response. She plants a synthetic password-guessing burst and follows it through: the measure flags the account, the alert reaches the on-call analyst, the analyst locks the account and the ticket records each step with times. Prof. Hale explains that end-to-end testing finds handover failures between tools and people that individual component tests miss. The whole chain completes in eleven minutes in the synthetic test, and she records the time taken at each step.

### 40.2 Simulated attacks

With written authorisation, Lindiwe runs simulated attacks in a test environment that mirrors Saltmarsh's network: a phished account creating a forwarding rule, a bulk download from the customer portal and a change of delivery address an hour before dispatch. She checks which controls detect each. The forwarding rule now triggers an alert, after the gap found in validation was fixed. The bulk download alert fires late because its threshold is too high. The address-change alert fires as designed, within two minutes of the change.

### 40.3 Fixing and retesting

Lindiwe lowers the bulk download threshold using the synthetic history from the integration chapter, then reruns the simulation. The alert now fires within minutes. She records both results, before and after, so the evidence dossier shows the improvement and its cause. Prof. Hale notes that recording failures and fixes together is more convincing than showing only final passing results, because it demonstrates that testing actually influenced the controls. She also adds the bulk download case to the permanent test set used after every configuration change.

### 40.4 Evidence for the dossier

Lindiwe collects all test records: plans, authorisations, inputs, outputs, timings and fixes. She stores them with checksums and an index. She plans to use them in the evidence dossier in her final year, where each claim about Saltmarsh's security must point to specific evidence. She learns that a well-organised test record makes later assurance work faster and more credible. Prof. Hale reviews the index and asks her to add a short description of each test's purpose, so readers unfamiliar with the controls can understand why each test was run and what a pass or failure means.

### Worked example

Lindiwe tests guessing detection end to end, simulates three attacks, fixes a late bulk-download alert and retests, and stores all records for the dossier.

> **Synthetic case.** Tests are synthetic.

### Errors and limits

Showing only final passing tests hides how controls were improved.

### Exercises

- **EX118 — End-to-end steps.** Name one step followed end to end. *Rubric:* 3 = analyst locks the account;; 2 = one;; 1 = vague;; 0 = none.
- **EX119 — Late alert.** Which alert fired late? *Rubric:* 3 = bulk download;; 2 = correct;; 1 = other;; 0 = none.
- **EX120 — Before and after.** Why record results before and after fixing? *Rubric:* 3 = shows the improvement and its cause;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-41"></a>

## Chapter 41 — Information security: system optimization

### Learning outcomes

You will (1) reduce security cost without reducing protection; (2) remove redundant controls; (3) prioritise investment by risk reduction.

### 41.1 Finding waste

In her final year, Lindiwe reviews Saltmarsh's security spending and effort. She finds overlapping tools: two products scanning laptops for vulnerabilities and three separate places where account lists are maintained by hand. Each overlap costs licences and staff time, and inconsistent lists create gaps. Prof. Hale asks her to show which controls each tool supports before recommending removal, because a tool that looks redundant may cover a case the other misses. She lists every security tool with its licence cost, owner and the controls it supports in one shared table.

### 41.2 Consolidation

Lindiwe maps both laptop scanners against the assets they cover. One covers all laptops including warehouse terminals; the other misses terminals but offers reports managers like. She recommends keeping the first and recreating the useful reports from its data. For account lists, she proposes generating all three from the single identity source set up earlier. The changes save licence costs and remove manual updates that had caused errors in past access reviews. The security lead approves both changes, and the licence for the second scanner is not renewed.

### 41.3 Risk per pound

Lindiwe ranks proposed investments by estimated risk reduction per unit of cost. Immutable backups and multi-factor authentication for remaining supplier accounts rank highest, because they address the most damaging threats cheaply. A proposed advanced analytics product ranks low, since Saltmarsh's current detection gaps are basic. She notes that her estimates are rough, but ranking them openly makes assumptions visible and helps managers question them rather than accept vendor claims. She presents the ranking to the finance director with the assumptions listed beside each estimate, inviting challenge.

### 41.4 Measuring after change

After consolidation, Lindiwe checks that nothing was lost: the remaining scanner still covers every asset in the reconciled model, and access reviews based on the single identity source find no missing accounts. She records these checks as evidence. Prof. Hale notes that optimisation must prove protection was preserved, otherwise savings may simply move cost into a future incident. She repeats the coverage check one month later and again finds every asset covered. The finance director receives a short note confirming that the savings did not reduce protection, with the evidence attached for audit.

### Worked example

Lindiwe removes a redundant laptop scanner after checking coverage, generates account lists from one source, ranks investments by risk reduction per cost and verifies coverage after changes.

> **Synthetic case.** Costs and tools are synthetic.

### Errors and limits

Removing a tool without checking coverage can open unnoticed gaps.

### Exercises

- **EX121 — Kept scanner.** Which laptop scanner is kept? *Rubric:* 3 = the one covering warehouse terminals;; 2 = correct;; 1 = other;; 0 = none.
- **EX122 — Account lists.** How are the three account lists produced after change? *Rubric:* 3 = from the single identity source;; 2 = correct;; 1 = vague;; 0 = none.
- **EX123 — Low-ranked purchase.** Which investment ranks low? *Rubric:* 3 = an advanced analytics product;; 2 = correct;; 1 = other;; 0 = none.

<a id="ch-42"></a>

## Chapter 42 — Information security: applied research

### Learning outcomes

You will (1) frame an applied research question from operational data; (2) design a fair comparison; (3) report findings with limits.

### 42.1 Question

Lindiwe's applied research asks whether depots with badge-tap logins on warehouse terminals have fewer account misuse incidents than depots still waiting for rollout. The question arises from the multi-factor rollout, which reached depots in stages for practical reasons. Prof. Hale points out that staged rollouts create natural comparisons, but that the order of depots was chosen by size, which could bias any difference. She writes the question in one sentence and checks it with the security lead, who confirms the incident register records the necessary details for every depot. Prof. Hale approves the question.

### 42.2 Design

Lindiwe compares incident rates per hundred staff before and after rollout in depots that adopted early with depots that adopted late, using the period when late depots had not yet started. She checks that incident rates in both groups were similar before rollout. She defines incidents precisely from the incident register: confirmed use of an account by someone other than its owner. She fixes this definition and the comparison before examining outcomes. Prof. Hale reviews the plan and confirms that it was fixed before outcomes were examined.

### 42.3 Findings

The synthetic data show fewer incidents after rollout in early depots and little change in late depots over the same months. However, incidents are rare, only a handful in each group, so the difference is uncertain. Lindiwe reports counts, rates and the comparison, stating that the direction supports the rollout but the evidence is weak. Prof. Hale praises her for not turning a small count into a confident claim. She presents the counts in a simple table with both periods for both groups, so readers can see the small numbers directly.

### 42.4 Value of the study

Lindiwe argues that the study's main value is a reusable method: defining incidents consistently, using staged rollouts as comparisons and checking pre-rollout similarity. Saltmarsh can repeat it as more data accumulate. She also notes that shared logins ending is itself an accountability gain, regardless of incident counts. She learns that applied research in security often yields methods and modest evidence rather than definitive answers. The security lead asks her to write the method as a short procedure, so the team can rerun the comparison each year as the incident register grows.

### Worked example

Lindiwe compares early and late badge-tap depots using a fixed incident definition, finds a favourable but uncertain direction from small counts and emphasises a reusable method.

> **Synthetic case.** Data are synthetic.

### Errors and limits

Small incident counts cannot support confident conclusions.

### Exercises

- **EX124 — Natural comparison.** What created the natural comparison? *Rubric:* 3 = the staged rollout;; 2 = correct;; 1 = vague;; 0 = none.
- **EX125 — Incident definition.** How is an incident defined? *Rubric:* 3 = use of an account by someone other than its owner;; 2 = correct;; 1 = vague;; 0 = none.
- **EX126 — Evidence strength.** How strong is the evidence? *Rubric:* 3 = favourable but weak;; 2 = correct;; 1 = strong;; 0 = none.

<a id="ch-43"></a>

## Chapter 43 — Industry or public-service practice

### Learning outcomes

You will (1) work within a professional security team; (2) handle confidential information responsibly; (3) reflect on professional practice.

### 43.1 The placement

Lindiwe spends a semester working full-time in Saltmarsh's security team. She joins the daily stand-up, takes a share of alert reviews and supports an audit preparation. She notices how much work involves coordination: persuading owners to fix findings, scheduling changes around depot peaks and explaining risks to finance. Prof. Hale visits mid-placement and asks her which skills she uses most; she answers writing and negotiation, more than coding. She keeps a weekly journal recording what she did, what she learned and which conversations changed decisions.

### 43.2 Confidentiality

The placement gives Lindiwe access to sensitive information: incident details, vulnerability lists and customer complaints. She signs a confidentiality agreement and follows the rule that course work uses only synthetic data. When a classmate asks about a real incident, she declines to share details. Prof. Hale notes that professional trust depends on discretion, and that security staff must model the handling they ask of others. Her reflections for the course describe the kinds of work she did without revealing any real names, systems or incident details.

### 43.3 Audit preparation

Saltmarsh prepares for an external audit against its management system. Lindiwe helps gather evidence: risk assessment records, the statement of applicability, access reviews and restore test results. She finds two controls listed as implemented whose evidence is incomplete. Rather than presenting them as complete, the team marks them as in progress with dates. The auditor later notes the honesty favourably. She learns that audits reward accurate records more than polished claims. Lindiwe adds the evidence gaps to the team's tracker with owners.

### 43.4 Reflection

At the end of the placement, Lindiwe writes a reflection on professional practice. She notes that technical skill earns credibility, but influence comes from understanding the business and communicating clearly. She also notes the emotional side of incidents: staff whose accounts were phished felt embarrassed, and calm, blameless handling helped them report quickly next time. Prof. Hale asks her to carry these lessons into her capstone. She shares the reflection with the security lead, who adds two points from the team's perspective about how her questions improved their own documentation.

### Worked example

Lindiwe works in Saltmarsh's security team, keeps real details confidential, helps prepare honest audit evidence and reflects on communication and blameless handling.

> **Synthetic case.** The placement is synthetic.

### Errors and limits

Presenting incomplete controls as implemented misleads auditors.

### Exercises

- **EX127 — Most-used skills.** Which skills does Lindiwe use most? *Rubric:* 3 = writing and negotiation;; 2 = correct;; 1 = coding;; 0 = none.
- **EX128 — Incomplete evidence.** How are the two incomplete controls presented? *Rubric:* 3 = as in progress with dates;; 2 = correct;; 1 = complete;; 0 = none.
- **EX129 — Blameless effect.** What did blameless handling encourage? *Rubric:* 3 = quicker reporting next time;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-44"></a>

## Chapter 44 — Engineering capstone I

### Learning outcomes

You will (1) define a capstone problem with a client; (2) plan a substantial security engineering project; (3) manage scope and risk.

### 44.1 Problem definition

Lindiwe's capstone addresses a problem Saltmarsh identified: recovering dispatch within four hours after ransomware, the objective agreed earlier. Current backups are verified, but nobody has rebuilt the whole dispatch service from scratch. The capstone will design, build and test a recovery process in an isolated environment. Prof. Hale and the security lead sign the problem statement, which lists deliverables, constraints and the criterion for success. The security lead also confirms which systems may be copied into the isolated environment and that only synthetic customer data will be used.

### 44.2 Plan

Lindiwe divides the project into stages: document dependencies of dispatch, build an isolated recovery environment, script the rebuild of each component, restore data from immutable backups and run timed trials. Each stage has a deliverable and a review. She identifies risks to the project itself, such as delays obtaining test hardware, and plans alternatives, including using virtual machines on a spare server if hardware arrives late. She sets fortnightly review meetings with Prof. Hale and the security lead, each focused on one stage.

### 44.3 Dependencies

Documenting dependencies reveals surprises. Dispatch needs the directory for logins, the message queue, the mapping service, certificates and a licence server for one component. The licence server had not appeared in any diagram. Without it, the rebuilt service would refuse to start. Lindiwe adds it to the asset model and recovery plan. Prof. Hale notes that hidden dependencies are a common reason recovery takes far longer than planned. She also records the version and owner of each dependency, so the recovery plan can be kept current.

### 44.4 Scope control

Midway, the operations manager asks whether the capstone could also cover payroll recovery. Lindiwe assesses the effort and explains that adding payroll would risk finishing neither properly. She proposes documenting payroll dependencies only, as input for a later project. The client agrees. She learns that protecting scope is part of delivering value, and that saying no with a clear reason maintains trust better than overpromising. She records the decision in the project log with the operations manager's agreement and a note of the estimated extra effort.

### Worked example

Lindiwe defines a dispatch recovery capstone with a four-hour target, plans staged deliverables, finds a hidden licence server dependency and protects scope by deferring payroll.

> **Synthetic case.** The capstone is synthetic.

### Errors and limits

Undocumented dependencies make recovery far slower than planned.

### Exercises

- **EX130 — Success criterion.** What is the capstone's success criterion? *Rubric:* 3 = recover dispatch within four hours;; 2 = correct;; 1 = vague;; 0 = none.
- **EX131 — Hidden dependency.** What dependency was missing from diagrams? *Rubric:* 3 = a licence server;; 2 = correct;; 1 = other;; 0 = none.
- **EX132 — Scope decision.** What is done about payroll? *Rubric:* 3 = document dependencies only;; 2 = correct;; 1 = full;; 0 = none.

<a id="ch-45"></a>

## Chapter 45 — Independent design review

### Learning outcomes

You will (1) prepare a design for independent review; (2) respond to reviewer findings; (3) record review outcomes.

### 45.1 Preparing the review

Before building, Lindiwe submits her recovery design for independent review by an engineer from another organisation, arranged by Prof. Hale. She prepares a package: problem statement, architecture, dependency list, recovery steps, test plan and known risks. She writes a short guide explaining what feedback she most needs. Prof. Hale notes that reviewers give better feedback when the author states open questions honestly instead of presenting the design as finished. The reviewer receives the complete package two weeks before the formal review meeting.

### 45.2 Findings

The reviewer raises four findings. The recovery environment uses the same administrator credentials as production, so an attacker holding them could also damage the recovery. Recovery scripts are stored on a server that ransomware could encrypt. The test plan does not include restoring from backups older than a day, in case recent backups are corrupted. Finally, the design does not say who decides to start recovery. She thanks the reviewer and asks a follow-up question about each finding to make sure she has understood it correctly.

### 45.3 Responses

Lindiwe responds to each finding. She creates separate credentials for the recovery environment, held offline. She stores scripts in version control with an offline copy. She adds a test restoring from week-old backups. She writes a decision rule: the security lead and operations director jointly authorise recovery, with deputies named. She records each response in a table, with the reviewer's agreement noted beside each. The reviewer reviews the updated design two weeks later and confirms in writing that all four findings are resolved.

### 45.4 Value of review

Lindiwe reflects that three of the four findings concerned the recovery itself being vulnerable to the same attack it was meant to survive. She had focused on rebuilding speed and overlooked this. Prof. Hale notes that independent reviewers bring different assumptions, which is exactly why reviews find problems authors cannot. The review record joins the evidence dossier. She adds a section to her thesis plan describing the review and its effect on the design, because she believes other engineers would benefit from seeing how her assumptions changed after independent scrutiny.

### Worked example

Lindiwe prepares a review package, receives four findings including shared credentials and exposed scripts, responds with offline credentials, offline scripts, older restore tests and a decision rule.

> **Synthetic case.** The review is synthetic.

### Errors and limits

A recovery environment sharing production credentials can be destroyed by the same attacker.

### Exercises

- **EX133 — Credential finding.** What credential problem did the reviewer find? *Rubric:* 3 = recovery uses production admin credentials;; 2 = correct;; 1 = vague;; 0 = none.
- **EX134 — Older backups.** What test was added for older backups? *Rubric:* 3 = restoring from week-old backups;; 2 = correct;; 1 = vague;; 0 = none.
- **EX135 — Recovery decision.** Who authorises recovery? *Rubric:* 3 = security lead and operations director;; 2 = correct;; 1 = other;; 0 = none.

<a id="ch-46"></a>

## Chapter 46 — Engineering capstone II

### Learning outcomes

You will (1) build and test a recovery capability; (2) measure against an objective; (3) iterate until the objective is met.

### 46.1 Building

Lindiwe builds the recovery environment on isolated virtual machines and writes scripts to rebuild each dispatch component: directory connection, message queue, database, application servers, certificates and the licence server. Each script is idempotent, producing the same result when run twice, so a partial failure can be retried safely. She tests scripts individually before combining them, keeping a log of problems found and fixed. She stores every script in version control and records each test run with its date and outcome in a project log.

### 46.2 First trial

The first timed trial takes six hours and forty minutes, well over the four-hour objective. Most time goes to restoring the database from backup and to manual certificate steps. Lindiwe records the timeline minute by minute. Prof. Hale reminds her that a failed first trial is normal and that the timeline shows exactly where to work, which is more useful than a vague sense that recovery is slow. She shares the timeline with the security lead, highlighting the two largest sources of delay.

### 46.3 Improvements

Lindiwe makes three changes: restoring the database from a more recent snapshot stored in the immutable backup system, automating certificate installation and starting independent components in parallel. The second trial takes four hours and ten minutes. A third change, pre-staging application server images, brings the third trial to three hours and twenty minutes, inside the objective. She records each change and its effect on the timeline. Prof. Hale asks her to chart the three trials side by side, showing how each change shortened a specific part of the timeline.

### 46.4 Repeatability

One successful trial could be luck. Lindiwe runs two more trials on different days with different team members following the runbook. Both finish within four hours. She notes that the slowest remaining step is database restoration, which grows with data volume, so the objective may be missed as dispatch data grow. She recommends repeating the trial every six months and after major changes. The security lead adds the six-monthly trial to the security calendar and assigns an owner. Lindiwe writes the procedure so new staff can lead it.

### Worked example

Lindiwe builds idempotent recovery scripts, measures a first trial at 6 hours 40 minutes, improves to 3 hours 20 minutes and confirms repeatability with different staff.

> **Synthetic case.** Trials are synthetic.

### Errors and limits

A single successful recovery trial does not prove recovery is reliable.

### Exercises

- **EX136 — First trial time.** How long did the first trial take? *Rubric:* 3 = six hours forty minutes;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX137 — Idempotent meaning.** What does idempotent mean for her scripts? *Rubric:* 3 = same result when run twice;; 2 = correct;; 1 = vague;; 0 = none.
- **EX138 — Remaining slow step.** What remains the slowest step? *Rubric:* 3 = database restoration;; 2 = correct;; 1 = other;; 0 = none.

<a id="ch-47"></a>

## Chapter 47 — Failure and recovery trial

### Learning outcomes

You will (1) run a realistic failure exercise; (2) observe human and technical performance; (3) produce lessons for improvement.

### 47.1 Scenario

With approval from Saltmarsh's directors, Lindiwe runs a full recovery trial in the isolated environment, treating it as a live incident. The scenario: at six on a Monday morning, ransomware has encrypted dispatch servers and the nightly backup share. Only immutable backups remain. The incident team does not know the scenario in advance. Prof. Hale and the security lead observe, recording decisions and times without intervening. Lindiwe prepares the scenario materials, a timeline of injected events and an observer sheet for recording what happens.

### 47.2 Performance

The team follows the incident process: detection, decision to recover, authorisation by the named directors and execution of the runbook. The rebuild completes in three hours and thirty-five minutes. Two problems occur. The on-call manager cannot find the offline credentials at first, losing twenty minutes. The restored data are verified with checksums, and one batch fails verification, so the team restores it from the previous snapshot. The team records every action in the incident log, which Lindiwe later uses to reconstruct the timeline accurately.

### 47.3 Human factors

Lindiwe observes that stress affected communication: two people ran the same script simultaneously, and depot supervisors were not told when to switch to printed lists. She notes these are process issues, not individual failings. She recommends a single coordinator role during recovery and a message template for depots. Prof. Hale notes that recovery trials test people and communication as much as technology. She discusses her observations with the participants in a short debrief, and they agree with the proposed changes and add one of their own about shift handovers.

### 47.4 Lessons

The lessons report lists five improvements: label and check offline credential storage monthly, add a coordinator role, use the depot message template, automate checksum verification of restored batches and repeat the trial annually with different staff. Each has an owner and date. Lindiwe notes that the trial met the objective despite problems, which gives confidence while showing exactly where the margin could be lost. The directors approve the improvements and ask for a short progress update in three months, which Lindiwe schedules before her course ends.

### Worked example

Lindiwe runs an unannounced recovery trial completed in 3 hours 35 minutes, observes credential and communication problems and records five owned improvements.

> **Synthetic case.** The trial is synthetic.

### Errors and limits

Recovery trials that test only technology miss communication failures.

### Exercises

- **EX139 — Trial duration.** How long did the rebuild take? *Rubric:* 3 = three hours thirty-five minutes;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX140 — Credential delay.** How much time was lost finding credentials? *Rubric:* 3 = twenty minutes;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX141 — Coordinator role.** Why add a coordinator role? *Rubric:* 3 = two people ran the same script;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-48"></a>

## Chapter 48 — Evidence dossier

### Learning outcomes

You will (1) assemble evidence supporting security claims; (2) link each claim to verifiable records; (3) state limitations of the evidence.

### 48.1 Claims

Lindiwe assembles an evidence dossier for Saltmarsh's directors and auditors. She lists claims: assets are reconciled weekly; servers meet baseline rules at a measured rate; password guessing is detected; backups are verified by restore tests; dispatch can be recovered within four hours. Each claim must point to evidence. Prof. Hale warns her not to include claims she cannot support, however desirable they sound. She drafts each claim as a single sentence, checks it with the owner of the control and removes one claim about phishing awareness she could not support.

### 48.2 Linking evidence

For each claim, Lindiwe links records: the reconciliation reports with the original lab figures of 63 unregistered and 90 silent hosts and later improvements; baseline results starting at 72.0 percent passing all rules; the guessing measure's detections and its boundary test; restore tests starting at 98.4 percent verified; and the recovery trial timelines. Every record is indexed with a checksum. A reader can trace any claim to its source within minutes. The index lists each record's date, owner, file name and checksum, grouped by the claim it supports.

### 48.3 Limitations

The dossier states limits plainly. The guessing measure misses slow attacks. The address-change control is verified but not validated. Recovery trials were run in an isolated environment, which may differ from a real incident. Baseline rules cover three settings, not full hardening. Lindiwe notes that stating limits makes the dossier more credible, because readers can see what has and has not been shown. Prof. Hale reviews the section and asks her to place each limitation directly after the claim it affects, so readers cannot miss it.

### 48.4 Use

The security lead uses the dossier in the external audit and in a tender response for a new customer. The auditor samples five claims and traces each to evidence without difficulty. Lindiwe learns that a dossier built from records created during normal work costs little to maintain, while one assembled under deadline pressure tends to contain gaps and inconsistent figures. The security lead adds the dossier to the team's routine work, assigning each claim's owner the task of updating its evidence after every relevant test or change.

### Worked example

Lindiwe assembles five claims, links each to checksummed records including lab figures, states four limitations and supports an audit that traces sampled claims easily.

> **Synthetic case.** The dossier is synthetic.

### Errors and limits

Including claims without evidence undermines the whole dossier.

### Exercises

- **EX142 — Dossier claim.** Name one claim in the dossier. *Rubric:* 3 = dispatch can be recovered within four hours;; 2 = one;; 1 = vague;; 0 = none.
- **EX143 — Baseline starting rate.** What baseline rate starts the record? *Rubric:* 3 = 72.0 percent passing all rules;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX144 — Auditor sample.** How many claims did the auditor sample? *Rubric:* 3 = five;; 2 = correct;; 1 = wrong;; 0 = none.

<a id="ch-49"></a>

## Chapter 49 — Engineering thesis

### Learning outcomes

You will (1) write an engineering thesis around a central argument; (2) present design, evidence and evaluation; (3) reflect on contribution and limits.

### 49.1 Argument

Lindiwe's thesis argues that a small organisation can achieve verifiable ransomware recovery within business objectives by combining immutable backups, checksum verification, scripted rebuilds and regular trials. The argument rests on her capstone and dossier. Prof. Hale asks her to state the argument in the first paragraph and to make every chapter contribute to it, so readers can follow why each part exists. She writes a one-page outline listing each chapter and the part of the argument it supports, and Prof. Hale uses it to guide his reading of the drafts.

### 49.2 Structure

The thesis has chapters on context and requirements, related work, dependency analysis, design and review, implementation, trials and results, evaluation and limitations. Related work draws on Anderson's Security Engineering, NIST SP 800-30 Revision 1 for risk assessment and ISO/IEC 27001:2022 for management system context. She cites each source for specific points rather than as decoration, and paraphrases standards rather than quoting long passages. Each chapter begins with a short paragraph stating its purpose and ends with a summary of what it has shown. Prof. Hale finds this structure helpful.

### 49.3 Evaluation

Lindiwe evaluates the work against the objective: trials met four hours repeatedly, with the final unannounced trial at three hours and thirty-five minutes. She also evaluates against cost, showing the recovery environment uses existing hardware. She compares with the situation before the project, when no full rebuild had ever been attempted. She is careful to describe results as applying to Saltmarsh's environment and data volumes. She presents all trial times in one table with the changes made between trials, so examiners can see how the result was reached.

### 49.4 Contribution and limits

Lindiwe identifies her contribution as a tested, documented recovery method with a measured timeline, plus the finding that recovery environments must be isolated from production credentials. Limits include one organisation, an isolated trial environment and growing data volumes threatening the objective. Prof. Hale approves the thesis for submission, noting that its honesty about limits strengthens rather than weakens it. She also suggests future work: testing recovery for payroll, measuring how database growth affects restore time and repeating the trial with a real incident team from another organisation.

### Worked example

Lindiwe argues for verifiable small-organisation ransomware recovery, structures chapters around the argument, evaluates against the four-hour objective and states contribution and limits.

> **Synthetic case.** The thesis is synthetic.

### Errors and limits

Citing sources as decoration rather than for specific points weakens a thesis.

### Exercises

- **EX145 — Thesis argument.** What does the thesis argue? *Rubric:* 3 = small organisations can achieve verifiable recovery;; 2 = correct;; 1 = vague;; 0 = none.
- **EX146 — Risk source.** Which source supports risk assessment? *Rubric:* 3 = NIST SP 800-30 Revision 1;; 2 = correct;; 1 = other;; 0 = none.
- **EX147 — Key finding.** What key finding concerns recovery environments? *Rubric:* 3 = must be isolated from production credentials;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-50"></a>

## Chapter 50 — Final defense

### Learning outcomes

You will (1) defend engineering work before examiners; (2) answer challenges about evidence and generalisation; (3) plan continued learning.

### 50.1 Preparation

Lindiwe prepares a thirty-minute presentation: the problem, the design, the review findings, the trials and the evidence. She rehearses with classmates who ask hostile questions. She prepares backup slides with timelines and checksum records. Prof. Hale advises her to answer only what she can support and to say clearly when a question goes beyond her evidence, because examiners respect precise limits more than confident guesses. She also prepares a short demonstration of the restore verification script running on synthetic files, in case examiners ask to see it working.

### 50.2 Challenges

An examiner asks whether the recovery would work if attackers had been inside the network for months. Lindiwe answers that immutable backups cover a fixed period and that week-old restore tests passed, but that longer undetected compromise could contaminate backups; detecting intrusions sooner is the complementary control. Another asks why she trusted checksums recorded on the backup system; she explains that the manifest is itself stored immutably with the backups. A third examiner asks about cost, and she shows the hardware reused for the environment.

### 50.3 Outcome

The examiners pass Lindiwe with commendation, praising the measured trials, the independent review and the dossier. They suggest she publish the recovery method as a practitioner guide. Saltmarsh offers her a role in its security team. She reflects that the course connected mathematics, systems and management into one engineering practice aimed at protecting a real organisation's information. She accepts the role and agrees to lead the next annual recovery trial. The examiners' report recommends her dossier as an example for future students, and Prof. Hale asks her to speak to next year's cohort about the capstone.

### 50.4 Continued learning

Lindiwe plans continued learning: professional certification, deeper study of incident response and keeping her recovery skills current through Saltmarsh's annual trials. Prof. Hale reminds her that standards and threats change; ISO/IEC 27000 itself was revised in 2026. The next course in this area, data governance, examines how decisions about data quality, ownership and use are made, which complements the security controls she has built. She also plans to mentor a placement student at Saltmarsh, passing on the habits she learned: measuring carefully, testing at boundaries and stating limits.

### Worked example

Lindiwe defends her recovery work, answers challenges on long-term compromise and checksum trust, passes with commendation and plans continued learning.

> **Synthetic case.** The defense is synthetic.

### Errors and limits

Answering beyond one's evidence undermines a defense.

### Exercises

- **EX148 — Long compromise.** What complements immutable backups against long compromise? *Rubric:* 3 = detecting intrusions sooner;; 2 = correct;; 1 = vague;; 0 = none.
- **EX149 — Manifest storage.** Where is the checksum manifest stored? *Rubric:* 3 = immutably with the backups;; 2 = correct;; 1 = vague;; 0 = none.
- **EX150 — Defense result.** What is the outcome of the defense? *Rubric:* 3 = pass with commendation;; 2 = correct;; 1 = fail;; 0 = none.

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX150. Lindiwe Dube, Prof. Marcus Hale, Brightwater Polytechnic, Saltmarsh Logistics and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** About forty million events per day.

**EX002.** A stopped or disabled log forwarder.

**EX003.** Losing detail an investigator may later need.

**EX004.** Payroll-access accounts minus finance staff.

**EX005.** Actions cannot be traced to an individual.

**EX006.** By removing a few unnecessary trust edges.

**EX007.** Wireless signals reach attackers outside the building.

**EX008.** Wear-levelling may keep old copies in unaddressable blocks.

**EX009.** Under ten minutes.

**EX010.** Accounts with no login in ninety days.

**EX011.** Against an allow list of the twelve valid codes.

**EX012.** Pass arguments as a list without a shell.

**EX013.** What was found, where, why it matters, likelihood and action.

**EX014.** Trust boundaries where data cross zones of control.

**EX015.** Licences must be retained for insurance checks.

**EX016.** A little over four weeks.

**EX017.** Inflow divided by the closure rate.

**EX018.** By removing unused software.

**EX019.** About ten thousand false alarms.

**EX020.** A Poisson process with a mean of twelve per week.

**EX021.** Larger depots with dedicated IT staff.

**EX022.** A compromised application reading another program's memory.

**EX023.** For an old driver.

**EX024.** To a hardware token or managed key service.

**EX025.** The standard unittest module.

**EX026.** An environment variable set by the scheduler.

**EX027.** The format is simple and the library is unmaintained.

**EX028.** She reports it without exploring further.

**EX029.** That web browsing is logged.

**EX030.** Tampered records could let spoiled medicines reach patients.

**EX031.** Passwords are sent in clear text on the network.

**EX032.** Malware contacting unusual domains.

**EX033.** How far an attacker can move after entering.

**EX034.** A dedicated account with only the rights backups need.

**EX035.** So an attacker on the server cannot erase the evidence.

**EX036.** A test group first, with promotion to the rest after a week.

**EX037.** Separate read and write accounts limited to needed tables.

**EX038.** By using parameterised queries.

**EX039.** An immutable copy that cannot be altered for a set period.

**EX040.** The server accepts delete requests from any logged-in user.

**EX041.** Each week against vulnerability databases.

**EX042.** Signing packages with a protected key.

**EX043.** Guarding against improper modification or destruction of information.

**EX044.** The overall category takes the highest of the three impacts.

**EX045.** Combining several independent controls.

**EX046.** Full delivery addresses.

**EX047.** Two requirements.

**EX048.** Data deletion, account removal and network disconnection.

**EX049.** Waiting overnight for an analyst to review alerts.

**EX050.** Slowing attempts, then requiring additional verification.

**EX051.** Medians and the slowest tenth.

**EX052.** New staff get no access until approved.

**EX053.** The intermediate service exposing only needed functions.

**EX054.** An undocumented port.

**EX055.** From the depot routing system.

**EX056.** Hardware security keys.

**EX057.** Renewal relied on someone remembering.

**EX058.** The statement of applicability.

**EX059.** Organisational, people, physical and technological.

**EX060.** Govern, Identify, Protect, Detect, Respond and Recover.

**EX061.** Multi-factor authentication for remote access and incident reports within 24 hours.

**EX062.** Within fourteen days.

**EX063.** Keep logs a year with restricted access and minimised personal fields.

**EX064.** Sixty-three hosts.

**EX065.** Ninety registered addresses.

**EX066.** The depot manager, with IT support.

**EX067.** The integrity of delivery addresses.

**EX068.** A full message queue delaying confirmations.

**EX069.** Insiders exporting customer lists.

**EX070.** The depot manager and the security lead.

**EX071.** By storing evidence with checksums in a restricted folder.

**EX072.** A door she thought unlocked has a code lock.

**EX073.** A small budget.

**EX074.** It gives broad network access once connected.

**EX075.** A second registered key and a verified service desk call.

**EX076.** Once inside, an attacker inherits trust.

**EX077.** Complete mediation.

**EX078.** User accounts, configuration and data.

**EX079.** Second-person approval for high-value address changes.

**EX080.** About five percent of orders.

**EX081.** By staging synthetic suspicious changes and checking alerts.

**EX082.** 278 servers, 92.7 percent.

**EX083.** 253 servers, 84.3 percent.

**EX084.** 216 servers, 72.0 percent.

**EX085.** u17, u402 and u977.

**EX086.** Its 61 failures are spread across the day, not in bursts.

**EX087.** Slow, patient password guessing.

**EX088.** Ten failures within four minutes.

**EX089.** A burst of ten failures spanning exactly five minutes.

**EX090.** So future changes can be checked quickly.

**EX091.** Administrators with hardware keys.

**EX092.** Badge tap combined with a personal code.

**EX093.** Enrolled accounts, logins using a second factor and open exceptions.

**EX094.** 492 files, 98.4 percent.

**EX095.** They were in a folder added after the backup selection was set.

**EX096.** Lose at most an hour of data and return within four hours.

**EX097.** Refrigerated medicine deliveries.

**EX098.** An unknown printed-list location and departed staff on the contact list.

**EX099.** Independent loggers read at delivery and kept separately.

**EX100.** They shared a single credential.

**EX101.** Six fields.

**EX102.** A sudden rise in requests for customer addresses.

**EX103.** At least five analysts.

**EX104.** An external service at night and Saltmarsh staff by day.

**EX105.** An on-call Saltmarsh manager, within minutes.

**EX106.** It roughly doubles the firewall's processor load.

**EX107.** Within eighteen months.

**EX108.** Authentication and administrative events.

**EX109.** About forty minutes.

**EX110.** Locking the phished account.

**EX111.** Its exception was extended twice without review.

**EX112.** Four incidents.

**EX113.** No monitoring of email forwarding rules.

**EX114.** Verified but not yet validated.

**EX115.** In a single configuration file.

**EX116.** A colleague with no involvement follows each runbook.

**EX117.** Some controls stop if a single person is absent.

**EX118.** The analyst locks the flagged account.

**EX119.** The bulk download alert.

**EX120.** To show the improvement and its cause.

**EX121.** The one covering all laptops including warehouse terminals.

**EX122.** Generated from the single identity source.

**EX123.** An advanced analytics product.

**EX124.** The staged rollout across depots.

**EX125.** Confirmed use of an account by someone other than its owner.

**EX126.** The direction is favourable but the evidence is weak.

**EX127.** Writing and negotiation.

**EX128.** As in progress with target dates.

**EX129.** Staff reporting quickly next time.

**EX130.** Recovering dispatch within four hours.

**EX131.** A licence server for one component.

**EX132.** Only its dependencies are documented for a later project.

**EX133.** The recovery environment uses production administrator credentials.

**EX134.** Restoring from week-old backups.

**EX135.** The security lead and the operations director jointly.

**EX136.** Six hours and forty minutes.

**EX137.** Running a script twice gives the same result.

**EX138.** Database restoration.

**EX139.** Three hours and thirty-five minutes.

**EX140.** Twenty minutes.

**EX141.** Two people ran the same script simultaneously under stress.

**EX142.** Dispatch can be recovered within four hours.

**EX143.** 72.0 percent of servers passing all rules.

**EX144.** Five claims.

**EX145.** That a small organisation can achieve verifiable ransomware recovery within objectives.

**EX146.** NIST SP 800-30 Revision 1.

**EX147.** They must be isolated from production credentials.

**EX148.** Detecting intrusions sooner.

**EX149.** Immutably with the backups.

**EX150.** A pass with commendation.

<a id="references"></a>
## References

Every DOI was resolved through doi.org on 12 October 2026, and ISO/IEC editions were checked against iso.org on the same day. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- Anderson, R. (2020). *Security engineering: A guide to building dependable distributed systems* (3rd ed.). Wiley. https://doi.org/10.1002/9781119644682
- ISO/IEC. (2022). *ISO/IEC 27001:2022 Information security, cybersecurity and privacy protection — Information security management systems — Requirements* (with Amd 1:2024). <https://www.iso.org/standard/27001>
- ISO/IEC. (2022). *ISO/IEC 27002:2022 Information security, cybersecurity and privacy protection — Information security controls*. <https://www.iso.org/standard/75652.html>
- ISO/IEC. (2026). *ISO/IEC 27000:2026 Information security, cybersecurity and privacy protection — Information security management systems — Overview* (6th ed., replacing ISO/IEC 27000:2018). <https://www.iso.org/standard/27000>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-53r5
- Joint Task Force Transformation Initiative. (2012). *Guide for conducting risk assessments* (NIST SP 800-30 Rev. 1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-30r1
- National Institute of Standards and Technology. (2004). *Standards for security categorization of federal information and information systems* (FIPS 199). https://doi.org/10.6028/NIST.FIPS.199
- National Institute of Standards and Technology. (2024). *The NIST Cybersecurity Framework (CSF) 2.0* (NIST CSWP 29). https://doi.org/10.6028/NIST.CSWP.29
- Nieles, M., Dempsey, K., & Pillitteri, V. Y. (2017). *An introduction to information security* (NIST SP 800-12 Rev. 1). National Institute of Standards and Technology. https://doi.org/10.6028/NIST.SP.800-12r1
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE, 63*(9), 1278–1308. https://doi.org/10.1109/PROC.1975.9939
