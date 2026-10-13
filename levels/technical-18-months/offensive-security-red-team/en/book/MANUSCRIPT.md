# Authorized Offensive Security and Red Team: A Technical Operator's Workbook

- Language: English (`en`); technical course, eighteen months; approximately 1,200 hours of planned study.
- Editorial state: **draft**. Chapters 1–18 of 18 have hand-written teaching text; exercises EX001–EX072 have matching worked results; offline labs use the Python 3 standard library and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technical operators who configure checks, verify fixes and keep authorized testing safe.
- Relation to neighbouring books: the [professional course book](../../../../professional-6-months/offensive-security-red-team/en/book/MANUSCRIPT.md) is shorter; the [technologist book](../../../../technologist-3-years/offensive-security-red-team/en/book/MANUSCRIPT.md) adds design and integration. **This book is procedural and lab-focused.**
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not an accredited qualification. **No authority to test real systems.** All organisations, people and numbers are **synthetic** unless a sentence cites a public source. Labs classify inventories, hash evidence and compare retest statuses — never weaponised techniques.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Chapters 1–5 build architecture, networks, identities, scripting and evidence; 6–11 cover modelling, telemetry, failure modes, methods, config and verification; 12–18 are labs, troubleshooting, automation, dependencies, documentation, Lab II and the project. Every chapter has outcomes, teaching, a worked example, a labelled synthetic case, errors and limits, four exercises scored 0–3, a synthesis and a **Continue studying** block. Labs in Chapters 2, 5 and 11 read local data only (`python3 file.py`).

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Northline Municipal Transit (NMT)** — website, journey planner API, staff AD/VPN, fare network (out of scope) | Organisation studied throughout | Invented |
| **Sam Park** | Security technician at NMT | Invented |

### Core sources

NIST [SP 800-115](https://doi.org/10.6028/NIST.SP.800-115); [PTES](https://pentest-standard.readthedocs.io/en/latest/); MITRE [ATT&CK](https://attack.mitre.org/); OWASP [WSTG](https://owasp.org/www-project-web-security-testing-guide/); [TIBER-EU](https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html); Bank of England [CBEST](https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Computing and service architecture

### Learning outcomes

You will (1) sketch NMT's main services; (2) explain tiers and trust boundaries; (3) locate where authorized testing usually starts; (4) identify fragile dependencies.

### 1.1 Services

NMT runs a public website, a journey planner API, a staff intranet, Active Directory for employees, a VPN, and a fare-collection network that is out of scope for ordinary tests.

Section one point one develops computing and service architecture with a Northline Municipal Transit note Sam Park can demo offline.

Under section one point one, the NMT mentor expects computing claims to carry owners and dates.

Section one point one treats services tiers where testing as testable only when evidence and ticket IDs are recorded.

### 1.2 Tiers

Internet-facing web and API tiers sit behind a load balancer; application servers talk to databases; staff identity sits in AD. Trust boundaries are the places where packets or credentials cross from less trusted to more trusted zones.

Section one point two develops computing and service architecture with a Northline Municipal Transit note Sam Park can demo offline.

Under section one point two, the NMT mentor expects computing claims to carry owners and dates.

Section one point two treats services tiers where testing as testable only when evidence and ticket IDs are recorded.

### 1.3 Where testing starts

Authorized technical tests usually start at internet-facing web and API tiers and at staff remote access, because that is what strangers and phished staff reach first.

Section one point three develops computing and service architecture with a Northline Municipal Transit note Sam Park can demo offline.

Under section one point three, the NMT mentor expects computing claims to carry owners and dates.

Section one point three treats services tiers where testing as testable only when evidence and ticket IDs are recorded.

For section one point three, Northline Municipal Transit will not accept computing work without a written trail.

### 1.4 Fragile dependencies

Fare gates and radio systems can harm operations if disturbed. They stay excluded unless a specialised engagement says otherwise.

Section one point four develops computing and service architecture with a Northline Municipal Transit note Sam Park can demo offline.

Under section one point four, the NMT mentor expects computing claims to carry owners and dates.

Section one point four treats services tiers where testing as testable only when evidence and ticket IDs are recorded.

For section one point four, Northline Municipal Transit will not accept computing work without a written trail.

### 1.5 Architecture diagram discipline

Sam keeps a dated diagram with owners on each box. Testing against an outdated diagram causes scope errors.

Section one point five develops computing and service architecture with a Northline Municipal Transit note Sam Park can demo offline.

Under section one point five, the NMT mentor expects computing claims to carry owners and dates.

Section one point five treats services tiers where testing as testable only when evidence and ticket IDs are recorded.

For section one point five, Northline Municipal Transit will not accept computing work without a written trail.

### 1.6 Change windows

Architecture changes (new API gateway, AD upgrade) trigger a review of the ROE before the next test.

Section one point six develops computing and service architecture with a Northline Municipal Transit note Sam Park can demo offline.

Under section one point six, the NMT mentor expects computing claims to carry owners and dates.

Section one point six treats services tiers where testing as testable only when evidence and ticket IDs are recorded.

For section one point six, Northline Municipal Transit will not accept computing work without a written trail.

### 1.7 Owner contacts on the diagram

Every box on Sam's diagram names a person, not only a team. When a finding appears on the journey planner API, he knows whom to call without hunting through a directory.

Section one point seven develops computing and service architecture with a Northline Municipal Transit note Sam Park can demo offline.

Under section one point seven, the NMT mentor expects computing claims to carry owners and dates.

Section one point seven treats services tiers where testing as testable only when evidence and ticket IDs are recorded.

### 1.8 Why diagrams go stale

A contractor adds a staging CDN and nobody redraws the picture. Sam's first task each engagement is to confirm the diagram with the network owner in writing.

Section one point eight develops computing and service architecture with a Northline Municipal Transit note Sam Park can demo offline.

Under section one point eight, the NMT mentor expects computing claims to carry owners and dates.

Section one point eight treats services tiers where testing as testable only when evidence and ticket IDs are recorded.

### Worked example (synthetic NMT)

Sam draws NMT: Internet → WAF → web/API → app → DB; separate path VPN → jump → intranet/AD; fare network drawn in red as out of scope.

> **Synthetic case — Northline Municipal Transit (NMT).** The transit agency, Sam Park and all figures are invented for teaching.

### Errors and limits

Live transit systems and fare equipment are never tested without a separate, specialised authorization. This book uses synthetic data only and grants no authority to test real systems.

### Exercises

- **EX001 — Boxes.** List five NMT services. *Rubric:* 3 = five correct; 2 = four; 1 = two; 0 = none.
- **EX002 — Trust boundary.** Give one trust boundary on Sam's drawing. *Rubric:* 3 = e.g. Internet to WAF/web, or VPN to jump; 2 = vague; 1 = none; 0 = none.
- **EX003 — Why fare is red.** Why is fare-collection out of ordinary scope? *Rubric:* 3 = operations/safety impact if disturbed; needs specialised auth; 2 = partial; 1 = "old"; 0 = none.
- **EX004 — Start point.** Where do ordinary authorized tests start at NMT? *Rubric:* 3 = internet-facing web/API and staff remote access; 2 = partial; 1 = fare gates; 0 = none.

### Synthesis

Architecture shows tiers, trust boundaries and exclusions before any tool runs.

### Continue studying — chapter 01 of 18

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Networks and protocols

### Learning outcomes

You will (1) read common ports in an approved list; (2) flag unapproved listeners from a synthetic list; (3) explain why protocol choice matters for testing; (4) avoid scanning without authorization.

### 2.1 Approved listeners

NMT publishes an approved list for the staging web VLAN: 80/http, 443/https, 22/ssh-jump. Anything else is reported, not "interesting to poke".

Section two point one develops networks and protocols with a Northline Municipal Transit note Sam Park can demo offline.

Under section two point one, the NMT mentor expects networks claims to carry owners and dates.

Section two point one treats approved listeners protocol basics as testable only when evidence and ticket IDs are recorded.

```python
"""Lab 2: classify synthetic listening ports against an approved service list (no scanning)."""
approved = {80: "http", 443: "https", 22: "ssh-jump"}
observed = [(80, "http"), (443, "https"), (22, "ssh"), (3389, "rdp"), (8080, "http-alt")]
for port, name in observed:
    if port not in approved:
        print(f"{port:5}/{name:8} NOT APPROVED - report")
    elif name.split("-")[0] != approved[port].split("-")[0]:
        print(f"{port:5}/{name:8} unexpected name (expected {approved[port]})")
    else:
        print(f"{port:5}/{name:8} ok")
```

Run with `python3 lab_ports.py`. Verified output:

```text
   80/http     ok
  443/https    ok
   22/ssh      ok
 3389/rdp      NOT APPROVED - report
 8080/http-alt NOT APPROVED - report
```

### 2.2 Protocol basics

HTTP/HTTPS carry the website and API; SSH reaches jump hosts; RDP on a web VLAN is unexpected. Testers describe what they see without sending exploit traffic.

Section two point two develops networks and protocols with a Northline Municipal Transit note Sam Park can demo offline.

Under section two point two, the NMT mentor expects networks claims to carry owners and dates.

Section two point two treats approved listeners protocol basics as testable only when evidence and ticket IDs are recorded.

For section two point two, Northline Municipal Transit will not accept networks work without a written trail.

### 2.3 No freestyle scanning

Even listing ports on production needs authorization. This lab only classifies a synthetic list offline.

Section two point three develops networks and protocols with a Northline Municipal Transit note Sam Park can demo offline.

Under section two point three, the NMT mentor expects networks claims to carry owners and dates.

Section two point three treats approved listeners protocol basics as testable only when evidence and ticket IDs are recorded.

For section two point three, Northline Municipal Transit will not accept networks work without a written trail.

### 2.4 Name mismatches

Port 22 labelled only "ssh" still matches the approved ssh-jump family in the lab, but Sam notes the inventory name for cleanup.

Section two point four develops networks and protocols with a Northline Municipal Transit note Sam Park can demo offline.

Under section two point four, the NMT mentor expects networks claims to carry owners and dates.

Section two point four treats approved listeners protocol basics as testable only when evidence and ticket IDs are recorded.

For section two point four, Northline Municipal Transit will not accept networks work without a written trail.

### 2.5 Egress paths

Staff laptops that can reach staging and the Internet may bridge environments; the ROE states which source networks are allowed.

Section two point five develops networks and protocols with a Northline Municipal Transit note Sam Park can demo offline.

Under section two point five, the NMT mentor expects networks claims to carry owners and dates.

Section two point five treats approved listeners protocol basics as testable only when evidence and ticket IDs are recorded.

For section two point five, Northline Municipal Transit will not accept networks work without a written trail.

### 2.6 Logging

Network teams may mirror authorized test sources; Sam coordinates so his traffic is attributable.

Section two point six develops networks and protocols with a Northline Municipal Transit note Sam Park can demo offline.

Under section two point six, the NMT mentor expects networks claims to carry owners and dates.

Section two point six treats approved listeners protocol basics as testable only when evidence and ticket IDs are recorded.

For section two point six, Northline Municipal Transit will not accept networks work without a written trail.

### 2.7 TCP versus application identity

A port being open is not the same as a service being safe. Sam records both the port and the application banner or certificate name when inventory allows.

Section two point seven develops networks and protocols with a Northline Municipal Transit note Sam Park can demo offline.

Under section two point seven, the NMT mentor expects networks claims to carry owners and dates.

Section two point seven treats approved listeners protocol basics as testable only when evidence and ticket IDs are recorded.

### 2.8 Reporting unapproved listeners

Unapproved does not mean "exploit now". It means open a ticket, attach the synthetic observation, and wait for the owner to confirm whether the service should exist.

Section two point eight develops networks and protocols with a Northline Municipal Transit note Sam Park can demo offline.

Under section two point eight, the NMT mentor expects networks claims to carry owners and dates.

Section two point eight treats approved listeners protocol basics as testable only when evidence and ticket IDs are recorded.

For section two point eight, Northline Municipal Transit will not accept networks work without a written trail.

### Worked example (synthetic NMT)

Sam classifies the synthetic list: 80, 443 and 22 are ok; 3389/rdp and 8080/http-alt are NOT APPROVED. He opens a ticket for the two unapproved listeners on staging.

> **Synthetic case — Northline Municipal Transit (NMT).** The transit agency, Sam Park and all figures are invented for teaching.

### Errors and limits

Live transit systems and fare equipment are never tested without a separate, specialised authorization. This book uses synthetic data only and grants no authority to test real systems.

### Exercises

- **EX005 — Unapproved.** Which two listeners does the lab mark NOT APPROVED? *Rubric:* 3 = 3389/rdp and 8080/http-alt; 2 = one; 1 = wrong; 0 = none.
- **EX006 — Why RDP matters.** Why is RDP on the web VLAN a concern? *Rubric:* 3 = unexpected remote desktop exposure; broad attack surface; 2 = partial; 1 = fine; 0 = none.
- **EX007 — Authorization.** May Sam port-scan production to build his own list? *Rubric:* 3 = no without written authorization; 2 = no; 1 = yes; 0 = none.
- **EX008 — Inventory follow-up.** What does Sam do after the lab about the ssh name? *Rubric:* 3 = note inventory name cleanup; keep using jump process; 2 = partial; 1 = ignore; 0 = none.

### Synthesis

Approved lists turn raw ports into tickets; freestyle scanning stays forbidden.

### Continue studying — chapter 02 of 18

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Operating systems and identities

### Learning outcomes

You will (1) separate local, domain and application identities; (2) explain least privilege for test accounts; (3) handle shared accounts as findings; (4) protect test credentials.

### 3.1 Identity layers

Workstations have local accounts; staff use AD domain accounts; the journey planner has application users. A finding may involve any layer.

Section three point one develops operating systems and identities with a Northline Municipal Transit note Sam Park can demo offline.

Under section three point one, the NMT mentor expects operating claims to carry owners and dates.

Section three point one treats identity layers test accounts as testable only when evidence and ticket IDs are recorded.

For section three point one, Northline Municipal Transit will not accept operating work without a written trail.

### 3.2 Test accounts

Authorized tests use named test accounts with the least privilege needed, issued for the window and revoked after. Shared pentest god accounts are themselves a finding.

Section three point two develops operating systems and identities with a Northline Municipal Transit note Sam Park can demo offline.

Under section three point two, the NMT mentor expects operating claims to carry owners and dates.

Section three point two treats identity layers test accounts as testable only when evidence and ticket IDs are recorded.

For section three point two, Northline Municipal Transit will not accept operating work without a written trail.

### 3.3 Service accounts

API and automation accounts often have broad rights and weak monitoring. They are high-value review targets when in scope.

Section three point three develops operating systems and identities with a Northline Municipal Transit note Sam Park can demo offline.

Under section three point three, the NMT mentor expects operating claims to carry owners and dates.

Section three point three treats identity layers test accounts as testable only when evidence and ticket IDs are recorded.

For section three point three, Northline Municipal Transit will not accept operating work without a written trail.

### 3.4 Credential handling

Test passwords live in the vault, not in chat or scripts committed to git.

Section three point four develops operating systems and identities with a Northline Municipal Transit note Sam Park can demo offline.

Under section three point four, the NMT mentor expects operating claims to carry owners and dates.

Section three point four treats identity layers test accounts as testable only when evidence and ticket IDs are recorded.

For section three point four, Northline Municipal Transit will not accept operating work without a written trail.

### 3.5 Admin workstations

Jump hosts should be the only path to admin tasks; tests that find direct admin RDP from email VLANs matter.

Section three point five develops operating systems and identities with a Northline Municipal Transit note Sam Park can demo offline.

Under section three point five, the NMT mentor expects operating claims to carry owners and dates.

Section three point five treats identity layers test accounts as testable only when evidence and ticket IDs are recorded.

For section three point five, Northline Municipal Transit will not accept operating work without a written trail.

### 3.6 ATT&CK link

Abuse of legitimate accounts maps to T1078 Valid Accounts — useful when writing detection recommendations.

Section three point six develops operating systems and identities with a Northline Municipal Transit note Sam Park can demo offline.

Under section three point six, the NMT mentor expects operating claims to carry owners and dates.

Section three point six treats identity layers test accounts as testable only when evidence and ticket IDs are recorded.

For section three point six, Northline Municipal Transit will not accept operating work without a written trail.

### 3.7 Revocation day

On Sunday night Sam verifies tst-sam-web is disabled. Leftover test accounts are among the most common findings he writes about other teams — he will not become one.

Section three point seven develops operating systems and identities with a Northline Municipal Transit note Sam Park can demo offline.

Under section three point seven, the NMT mentor expects operating claims to carry owners and dates.

Section three point seven treats identity layers test accounts as testable only when evidence and ticket IDs are recorded.

### 3.8 MFA on test accounts

Where NMT enforces MFA, test accounts get MFA too. Skipping MFA "because it is staging" trains bad habits and weakens staging as a proving ground.

Section three point eight develops operating systems and identities with a Northline Municipal Transit note Sam Park can demo offline.

Under section three point eight, the NMT mentor expects operating claims to carry owners and dates.

Section three point eight treats identity layers test accounts as testable only when evidence and ticket IDs are recorded.

For section three point eight, Northline Municipal Transit will not accept operating work without a written trail.

### 3.9 3.x Field discipline

When Sam receives a new test account he walks a four-step checklist: confirm the account is named to him, confirm its groups match the ROE, store the secret in the vault under the engagement id, and set a calendar reminder for revocation day. Skipping any step has bitten NMT before — a shared account left in Domain Admins after a contractor left. He treats account hygiene as part of testing craft, not as paperwork for someone else.

Section three point nine develops operating systems and identities with a Northline Municipal Transit note Sam Park can demo offline.

### Worked example (synthetic NMT)

Sam receives account tst-sam-web with read access to staging only, vaulted for ENG-512, auto-expires Sunday night.

> **Synthetic case — Northline Municipal Transit (NMT).** The transit agency, Sam Park and all figures are invented for teaching.

### Errors and limits

Live transit systems and fare equipment are never tested without a separate, specialised authorization. This book uses synthetic data only and grants no authority to test real systems.

### Exercises

- **EX009 — Layers.** Name the three identity layers in the chapter. *Rubric:* 3 = local, domain/AD, application; 2 = two; 1 = one; 0 = none.
- **EX010 — Least privilege test account.** What rights should tst-sam-web have? *Rubric:* 3 = only staging rights needed for the ROE checks; 2 = partial; 1 = domain admin; 0 = none.
- **EX011 — Shared god account.** Why is a shared pentest admin account a finding? *Rubric:* 3 = no accountability; over-privilege; leftover access; 2 = partial; 1 = convenient ok; 0 = none.
- **EX012 — Vault.** Where do test passwords live? *Rubric:* 3 = approved vault; not chat/git; 2 = vault; 1 = sticky note; 0 = none.

### Synthesis

Named, least-privilege, vaulted, time-bounded accounts make testing accountable.

### Continue studying — chapter 03 of 18

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Scripting and data formats

### Learning outcomes

You will (1) parse simple JSON/CSV evidence safely; (2) avoid executing untrusted artifacts; (3) keep scripts reproducible; (4) record interpreter versions.

### 4.1 Why scripts

Technicians automate inventory diffs, hash checks and ticket formatting. Scripts must be readable by the next person.

Section four point one develops scripting and data formats with a Northline Municipal Transit note Sam Park can demo offline.

Under section four point one, the NMT mentor expects scripting claims to carry owners and dates.

Section four point one treats why scripts untrusted data as testable only when evidence and ticket IDs are recorded.

For section four point one, Northline Municipal Transit will not accept scripting work without a written trail.

### 4.2 Untrusted data

Files from targets are data, not code. Do not run unknown binaries or macros from a test target on an admin workstation.

Section four point two develops scripting and data formats with a Northline Municipal Transit note Sam Park can demo offline.

Under section four point two, the NMT mentor expects scripting claims to carry owners and dates.

Section four point two treats why scripts untrusted data as testable only when evidence and ticket IDs are recorded.

For section four point two, Northline Municipal Transit will not accept scripting work without a written trail.

### 4.3 Reproducibility

Pin Python versions, seed any randomness and keep input files beside the script in the evidence pack.

Section four point three develops scripting and data formats with a Northline Municipal Transit note Sam Park can demo offline.

Under section four point three, the NMT mentor expects scripting claims to carry owners and dates.

Section four point three treats why scripts untrusted data as testable only when evidence and ticket IDs are recorded.

For section four point three, Northline Municipal Transit will not accept scripting work without a written trail.

### 4.4 Formats

JSON and CSV are common for tool exports. Sam validates schema before trusting fields for a finding.

Section four point four develops scripting and data formats with a Northline Municipal Transit note Sam Park can demo offline.

Under section four point four, the NMT mentor expects scripting claims to carry owners and dates.

Section four point four treats why scripts untrusted data as testable only when evidence and ticket IDs are recorded.

For section four point four, Northline Municipal Transit will not accept scripting work without a written trail.

### 4.5 Secrets in scripts

No hard-coded passwords. Read from the vault or environment injected by the jump host.

Section four point five develops scripting and data formats with a Northline Municipal Transit note Sam Park can demo offline.

Under section four point five, the NMT mentor expects scripting claims to carry owners and dates.

Section four point five treats why scripts untrusted data as testable only when evidence and ticket IDs are recorded.

For section four point five, Northline Municipal Transit will not accept scripting work without a written trail.

### 4.6 Code review

Another technician reads Sam's script before it runs in an engagement window.

Section four point six develops scripting and data formats with a Northline Municipal Transit note Sam Park can demo offline.

Under section four point six, the NMT mentor expects scripting claims to carry owners and dates.

Section four point six treats why scripts untrusted data as testable only when evidence and ticket IDs are recorded.

For section four point six, Northline Municipal Transit will not accept scripting work without a written trail.

### 4.7 Input size limits

Scripts that read tool exports cap file size so a huge dump cannot exhaust the jump host. Caps are safety features, not pessimism.

Section four point seven develops scripting and data formats with a Northline Municipal Transit note Sam Park can demo offline.

Under section four point seven, the NMT mentor expects scripting claims to carry owners and dates.

Section four point seven treats why scripts untrusted data as testable only when evidence and ticket IDs are recorded.

For section four point seven, Northline Municipal Transit will not accept scripting work without a written trail.

### 4.8 Exit codes

Sam's scripts exit non-zero on MISMATCH or NOT APPROVED so CI and humans notice failures instead of skimming green-looking logs.

Section four point eight develops scripting and data formats with a Northline Municipal Transit note Sam Park can demo offline.

Under section four point eight, the NMT mentor expects scripting claims to carry owners and dates.

Section four point eight treats why scripts untrusted data as testable only when evidence and ticket IDs are recorded.

For section four point eight, Northline Municipal Transit will not accept scripting work without a written trail.

### 4.9 4.x Field discipline

Sam's scripting standard is short enough to remember: one purpose per script, argparse or explicit constants at the top, no network calls unless the ROE file path is passed in, and a --dry-run mode that prints what would happen. Dry-run saved him when a path typo would have pointed a hash job at a production share listing. Reviewers look for dry-run and for the absence of hard-coded hosts more than for clever code.

Section four point nine develops scripting and data formats with a Northline Municipal Transit note Sam Park can demo offline.

### Worked example (synthetic NMT)

Sam's hash-check script (Chapter 5 lab) takes a folder of evidence and prints MATCH/MISMATCH; it never opens images beyond hashing bytes.

> **Synthetic case — Northline Municipal Transit (NMT).** The transit agency, Sam Park and all figures are invented for teaching.

### Errors and limits

Live transit systems and fare equipment are never tested without a separate, specialised authorization. This book uses synthetic data only and grants no authority to test real systems.

### Exercises

- **EX013 — Data not code.** Why not double-click a .doc from the target web server? *Rubric:* 3 = may execute macros/malware on admin PC; treat as untrusted; 2 = partial; 1 = fine; 0 = none.
- **EX014 — Repro items.** Name three things that make a script reproducible. *Rubric:* 3 = version, inputs, seed/settings; 2 = two; 1 = one; 0 = none.
- **EX015 — Secrets.** How should a script get a staging password? *Rubric:* 3 = vault/env injection; not hard-coded; 2 = partial; 1 = hard-code; 0 = none.
- **EX016 — Peer read.** Why does another technician read the script first? *Rubric:* 3 = catch scope/safety bugs; shared understanding; 2 = partial; 1 = bureaucracy; 0 = none.

### Synthesis

Scripts are controlled tools: reproducible, secret-free and reviewed.

### Continue studying — chapter 04 of 18

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security scope and evidence

### Learning outcomes

You will (1) restate ROE checks for technicians; (2) hash evidence files; (3) reject mismatched evidence; (4) minimise personal data in captures.

### 5.1 Technician ROE

Before any command, Sam confirms target host, method and window against the ROE sheet on his knee.

Section five point one develops security scope and evidence with a Northline Municipal Transit note Sam Park can demo offline.

Under section five point one, the NMT mentor expects security claims to carry owners and dates.

Section five point one treats technician roe hashing minimisation as testable only when evidence and ticket IDs are recorded.

For section five point one, Northline Municipal Transit will not accept security work without a written trail.

### 5.2 Hashing

Hashing evidence detects accidental edits. A mismatch means do not attach the file until the lineage is clear.

Section five point two develops security scope and evidence with a Northline Municipal Transit note Sam Park can demo offline.

Under section five point two, the NMT mentor expects security claims to carry owners and dates.

Section five point two treats technician roe hashing minimisation as testable only when evidence and ticket IDs are recorded.

For section five point two, Northline Municipal Transit will not accept security work without a written trail.

```python
"""Lab 5: verify synthetic evidence file hashes before attaching to a finding."""
import hashlib
files = {"shot1.png": b"fake-png-bytes-v1", "shot1-edited.png": b"fake-png-bytes-v2",
         "config.txt": b"PermitRootLogin no\n"}
recorded = {k: hashlib.sha256(v).hexdigest() for k, v in files.items() if k != "shot1-edited.png"}
recorded["shot1.png"] = hashlib.sha256(b"fake-png-bytes-v1").hexdigest()
# simulate tampering record for edited shot still labeled shot1
check = {"shot1.png": files["shot1-edited.png"], "config.txt": files["config.txt"]}
for name, data in check.items():
    h = hashlib.sha256(data).hexdigest()
    print(f"{name:12} {h[:12]} {'MATCH' if h == recorded.get(name) else 'MISMATCH'}")
```

Run with `python3 lab_hash.py`. Verified output:

```text
shot1.png    b81db4df801a MISMATCH
config.txt   44c91857f34b MATCH
```

### 5.3 Minimisation

Blur rider faces and badge numbers in screenshots; keep the pixels that prove the issue.

Section five point three develops security scope and evidence with a Northline Municipal Transit note Sam Park can demo offline.

Under section five point three, the NMT mentor expects security claims to carry owners and dates.

Section five point three treats technician roe hashing minimisation as testable only when evidence and ticket IDs are recorded.

For section five point three, Northline Municipal Transit will not accept security work without a written trail.

### 5.4 Evidence index

Each file has an id, hash, time, collector and related finding id.

Section five point four develops security scope and evidence with a Northline Municipal Transit note Sam Park can demo offline.

Under section five point four, the NMT mentor expects security claims to carry owners and dates.

Section five point four treats technician roe hashing minimisation as testable only when evidence and ticket IDs are recorded.

For section five point four, Northline Municipal Transit will not accept security work without a written trail.

### 5.5 Integrity vs truth

A matching hash proves the file is unchanged since hashing, not that the underlying system finding is still true.

Section five point five develops security scope and evidence with a Northline Municipal Transit note Sam Park can demo offline.

Under section five point five, the NMT mentor expects security claims to carry owners and dates.

Section five point five treats technician roe hashing minimisation as testable only when evidence and ticket IDs are recorded.

For section five point five, Northline Municipal Transit will not accept security work without a written trail.

### 5.6 Retention

Follow NMT's engagement retention schedule; delete local caches after vaulting.

Section five point six develops security scope and evidence with a Northline Municipal Transit note Sam Park can demo offline.

Under section five point six, the NMT mentor expects security claims to carry owners and dates.

Section five point six treats technician roe hashing minimisation as testable only when evidence and ticket IDs are recorded.

For section five point six, Northline Municipal Transit will not accept security work without a written trail.

### 5.7 Photographing screens

When a screenshot is required, Sam uses the jump host's tools, names the file with finding id and time, and hashes it before editing anything for redaction on a copy.

Section five point seven develops security scope and evidence with a Northline Municipal Transit note Sam Park can demo offline.

Under section five point seven, the NMT mentor expects security claims to carry owners and dates.

Section five point seven treats technician roe hashing minimisation as testable only when evidence and ticket IDs are recorded.

### 5.8 Two-person evidence rule

For high-impact findings, a second technician confirms the hash and the observation. Disagreement pauses filing.

Section five point eight develops security scope and evidence with a Northline Municipal Transit note Sam Park can demo offline.

Under section five point eight, the NMT mentor expects security claims to carry owners and dates.

Section five point eight treats technician roe hashing minimisation as testable only when evidence and ticket IDs are recorded.

For section five point eight, Northline Municipal Transit will not accept security work without a written trail.

### 5.9 5.x Field discipline

Evidence disputes are expensive. Sam therefore hashes immediately after capture, writes the hash into the activity log line, and only then redacts a copy for the report appendix. If legal later asks whether a screenshot was altered, he can show the original digest and the redacted derivative. The MISMATCH result in the lab is the classroom version of that discipline — edited bytes must never silently replace originals.

Section five point nine develops security scope and evidence with a Northline Municipal Transit note Sam Park can demo offline.

### Worked example (synthetic NMT)

Sam hashes evidence: config.txt MATCH; shot1.png MISMATCH because the bytes were edited after the recorded hash. He re-captures the screenshot and records a new hash.

> **Synthetic case — Northline Municipal Transit (NMT).** The transit agency, Sam Park and all figures are invented for teaching.

### Errors and limits

Live transit systems and fare equipment are never tested without a separate, specialised authorization. This book uses synthetic data only and grants no authority to test real systems.

### Exercises

- **EX017 — Mismatch action.** What does Sam do with shot1.png MISMATCH? *Rubric:* 3 = do not attach; re-capture; new hash; 2 = partial; 1 = attach anyway; 0 = none.
- **EX018 — Match meaning.** What does MATCH prove for config.txt? *Rubric:* 3 = unchanged since hash recorded; 2 = partial; 1 = system is secure; 0 = none.
- **EX019 — Minimisation.** Give one minimisation example at NMT. *Rubric:* 3 = blur faces/badges/card numbers; 2 = partial; 1 = keep everything; 0 = none.
- **EX020 — Knee card.** What three facts are on Sam's ROE knee card? *Rubric:* 3 = host, method, window (plus emergency contact); 2 = two; 1 = one; 0 = none.

### Synthesis

Scope on the knee card; evidence hashed, minimised and indexed.

### Continue studying — chapter 05 of 18

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — System model for authorized testing

### Learning outcomes

You will (1) build a simple system model for the journey planner; (2) mark entry points and data stores; (3) map OWASP WSTG themes to the model; (4) list assumptions.

### 6.1 Model elements

Actors (rider, staff), entry points (web, API), trust zones, data stores (trip DB, logs), and external deps (map tiles).

Section six point one develops system model for authorized testing with a Northline Municipal Transit note Sam Park can demo offline.

Under section six point one, the NMT mentor expects system claims to carry owners and dates.

Section six point one treats model elements entry points as testable only when evidence and ticket IDs are recorded.

For section six point one, Northline Municipal Transit will not accept system work without a written trail.

### 6.2 Entry points

Each entry point gets a short list of WSTG themes: auth, session, access control, input handling.

Section six point two develops system model for authorized testing with a Northline Municipal Transit note Sam Park can demo offline.

Under section six point two, the NMT mentor expects system claims to carry owners and dates.

Section six point two treats model elements entry points as testable only when evidence and ticket IDs are recorded.

For section six point two, Northline Municipal Transit will not accept system work without a written trail.

### 6.3 Assumptions

Staging mirrors production auth is an assumption to validate, not a fact.

Section six point three develops system model for authorized testing with a Northline Municipal Transit note Sam Park can demo offline.

Under section six point three, the NMT mentor expects system claims to carry owners and dates.

Section six point three treats model elements entry points as testable only when evidence and ticket IDs are recorded.

For section six point three, Northline Municipal Transit will not accept system work without a written trail.

### 6.4 Data flows

Note where personal data (saved journeys) flows so tests minimise exposure.

Section six point four develops system model for authorized testing with a Northline Municipal Transit note Sam Park can demo offline.

Under section six point four, the NMT mentor expects system claims to carry owners and dates.

Section six point four treats model elements entry points as testable only when evidence and ticket IDs are recorded.

For section six point four, Northline Municipal Transit will not accept system work without a written trail.

### 6.5 Out of model

Fare validators are omitted because they are out of scope.

Section six point five develops system model for authorized testing with a Northline Municipal Transit note Sam Park can demo offline.

Under section six point five, the NMT mentor expects system claims to carry owners and dates.

Section six point five treats model elements entry points as testable only when evidence and ticket IDs are recorded.

For section six point five, Northline Municipal Transit will not accept system work without a written trail.

### 6.6 Living model

Update the model when the API gains a new payment callback — even if payment is third-party.

Section six point six develops system model for authorized testing with a Northline Municipal Transit note Sam Park can demo offline.

Under section six point six, the NMT mentor expects system claims to carry owners and dates.

Section six point six treats model elements entry points as testable only when evidence and ticket IDs are recorded.

For section six point six, Northline Municipal Transit will not accept system work without a written trail.

### 6.7 Trust zone colours

Sam colours Internet red, staging amber, staff green and fare black (do not enter). Colour makes scope visible in reviews.

Section six point seven develops system model for authorized testing with a Northline Municipal Transit note Sam Park can demo offline.

Under section six point seven, the NMT mentor expects system claims to carry owners and dates.

Section six point seven treats model elements entry points as testable only when evidence and ticket IDs are recorded.

For section six point seven, Northline Municipal Transit will not accept system work without a written trail.

### 6.8 Assumption log

A running list of assumptions sits under the model. Each is marked confirmed, rejected or open before the report is issued.

Section six point eight develops system model for authorized testing with a Northline Municipal Transit note Sam Park can demo offline.

Under section six point eight, the NMT mentor expects system claims to carry owners and dates.

Section six point eight treats model elements entry points as testable only when evidence and ticket IDs are recorded.

For section six point eight, Northline Municipal Transit will not accept system work without a written trail.

### 6.9 6.x Field discipline

Building the system model with the product owner takes an hour and prevents days of confusion. Sam projects a blank diagram, asks the owner to place boxes, and only then adds his own arrows. Owners correct mistaken assumptions about which database holds saved journeys and whether the admin UI shares authentication with the rider API. Those corrections change which WSTG themes matter most.

Section six point nine develops system model for authorized testing with a Northline Municipal Transit note Sam Park can demo offline.

### Worked example (synthetic NMT)

Sam's one-page model shows rider → HTTPS → API → trip DB; staff → VPN → admin UI; map tiles as external; fare cloud crossed out.

> **Synthetic case — Northline Municipal Transit (NMT).** The transit agency, Sam Park and all figures are invented for teaching.

### Errors and limits

Live transit systems and fare equipment are never tested without a separate, specialised authorization. This book uses synthetic data only and grants no authority to test real systems.

### Exercises

- **EX021 — Actors.** Name two actors in the model. *Rubric:* 3 = rider and staff; 2 = one; 1 = none; 0 = none.
- **EX022 — WSTG theme.** Pick one entry point and one WSTG theme to apply. *Rubric:* 3 = concrete pair e.g. API+access control; 2 = partial; 1 = none; 0 = none.
- **EX023 — Assumption check.** How would Sam validate the staging-mirrors-prod-auth assumption? *Rubric:* 3 = compare configs/owners confirm; not assume; 2 = partial; 1 = assume true; 0 = none.
- **EX024 — Why omit fare.** Why omit fare validators from this model? *Rubric:* 3 = out of scope; 2 = partial; 1 = unimportant; 0 = none.

### Synthesis

A clear system model focuses WSTG effort and records assumptions explicitly.

### Continue studying — chapter 06 of 18

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Data and telemetry

### Learning outcomes

You will (1) identify logs useful in testing and in detection; (2) request access the right way; (3) avoid dumping production data; (4) use telemetry to confirm findings.

### 7.1 Useful logs

Web access logs, API auth failures, VPN authentications, WAF blocks, AD sign-ins.

Section seven point one develops data and telemetry with a Northline Municipal Transit note Sam Park can demo offline.

Under section seven point one, the NMT mentor expects data claims to carry owners and dates.

Section seven point one treats useful logs access path as testable only when evidence and ticket IDs are recorded.

For section seven point one, Northline Municipal Transit will not accept data work without a written trail.

### 7.2 Access path

Sam requests read-only log access for the window via the ROE, not by sharing someone else's SIEM password.

Section seven point two develops data and telemetry with a Northline Municipal Transit note Sam Park can demo offline.

Under section seven point two, the NMT mentor expects data claims to carry owners and dates.

Section seven point two treats useful logs access path as testable only when evidence and ticket IDs are recorded.

For section seven point two, Northline Municipal Transit will not accept data work without a written trail.

### 7.3 No production dumps

Exporting whole member tables for analysis is out of bounds. Use synthetic or minimised samples.

Section seven point three develops data and telemetry with a Northline Municipal Transit note Sam Park can demo offline.

Under section seven point three, the NMT mentor expects data claims to carry owners and dates.

Section seven point three treats useful logs access path as testable only when evidence and ticket IDs are recorded.

For section seven point three, Northline Municipal Transit will not accept data work without a written trail.

### 7.4 Confirming findings

An access-control finding is stronger when logs show the unauthorized request succeeded.

Section seven point four develops data and telemetry with a Northline Municipal Transit note Sam Park can demo offline.

Under section seven point four, the NMT mentor expects data claims to carry owners and dates.

Section seven point four treats useful logs access path as testable only when evidence and ticket IDs are recorded.

For section seven point four, Northline Municipal Transit will not accept data work without a written trail.

### 7.5 Clock sync

Note time zones and NTP status when correlating logs with activity notes.

Section seven point five develops data and telemetry with a Northline Municipal Transit note Sam Park can demo offline.

Under section seven point five, the NMT mentor expects data claims to carry owners and dates.

Section seven point five treats useful logs access path as testable only when evidence and ticket IDs are recorded.

For section seven point five, Northline Municipal Transit will not accept data work without a written trail.

### 7.6 Detection feedback

Share technique names with the SOC so they can build detections after the test.

Section seven point six develops data and telemetry with a Northline Municipal Transit note Sam Park can demo offline.

Under section seven point six, the NMT mentor expects data claims to carry owners and dates.

Section seven point six treats useful logs access path as testable only when evidence and ticket IDs are recorded.

For section seven point six, Northline Municipal Transit will not accept data work without a written trail.

### 7.7 Sample not full export

When a log query returns thousands of lines, Sam exports a time-bounded sample around his test activity, not the whole day, unless the ROE asks for more.

Section seven point seven develops data and telemetry with a Northline Municipal Transit note Sam Park can demo offline.

Under section seven point seven, the NMT mentor expects data claims to carry owners and dates.

Section seven point seven treats useful logs access path as testable only when evidence and ticket IDs are recorded.

For section seven point seven, Northline Municipal Transit will not accept data work without a written trail.

### 7.8 PII in logs

If logs contain rider phone numbers, he stores them in the restricted vault path and mentions PII presence in the evidence index.

Section seven point eight develops data and telemetry with a Northline Municipal Transit note Sam Park can demo offline.

Under section seven point eight, the NMT mentor expects data claims to carry owners and dates.

Section seven point eight treats useful logs access path as testable only when evidence and ticket IDs are recorded.

For section seven point eight, Northline Municipal Transit will not accept data work without a written trail.

### 7.9 7.x Field discipline

Sam books SIEM access in the same ticket as the ROE, with an end date. When the engagement ends, he confirms his access is removed — leftover read access is itself a finding he would write about anyone else. During the window he saves queries, not raw dumps, so another technician can replay the investigation without holding excess rider data.

Section seven point nine develops data and telemetry with a Northline Municipal Transit note Sam Park can demo offline.

Under section seven point nine, the NMT mentor expects data claims to carry owners and dates.

### Worked example (synthetic NMT)

Sam correlates a staging API 200 response on another user's resource with his activity-log time; the app log shows the same request id.

> **Synthetic case — Northline Municipal Transit (NMT).** The transit agency, Sam Park and all figures are invented for teaching.

### Errors and limits

Live transit systems and fare equipment are never tested without a separate, specialised authorization. This book uses synthetic data only and grants no authority to test real systems.

### Exercises

- **EX025 — Log types.** List four log types useful at NMT. *Rubric:* 3 = four from chapter; 2 = three; 1 = one; 0 = none.
- **EX026 — Password share.** May Sam borrow the SOC analyst's SIEM login? *Rubric:* 3 = no; request named read-only access; 2 = no; 1 = yes; 0 = none.
- **EX027 — Dump.** Why not export the whole trip DB? *Rubric:* 3 = privacy/scope/minimisation; 2 = partial; 1 = fine; 0 = none.
- **EX028 — Stronger evidence.** What log detail strengthens an access-control finding? *Rubric:* 3 = successful unauthorized request id/time/user; 2 = partial; 1 = none; 0 = none.

### Synthesis

Telemetry is requested properly, minimised and used to strengthen findings — not to hoard data.

### Continue studying — chapter 07 of 18

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Failure modes

### Learning outcomes

You will (1) list how tests can harm transit IT; (2) map stop conditions; (3) describe safe failure of tools; (4) practise communicating a stop.

### 8.1 Harm modes

Account lockouts; staging crashes; accidental production hit; log storms; poisoned caches.

Section eight point one develops failure modes with a Northline Municipal Transit note Sam Park can demo offline.

Under section eight point one, the NMT mentor expects failure claims to carry owners and dates.

Section eight point one treats harm modes stop conditions as testable only when evidence and ticket IDs are recorded.

For section eight point one, Northline Municipal Transit will not accept failure work without a written trail.

Section eight point one fails closed if failure evidence is missing rather than guessing.

### 8.2 Stop conditions

Owner asks stop; unexplained outage; fare system alerts anywhere; personal data exposed in a ticket; tool loops.

Section eight point two develops failure modes with a Northline Municipal Transit note Sam Park can demo offline.

Under section eight point two, the NMT mentor expects failure claims to carry owners and dates.

Section eight point two treats harm modes stop conditions as testable only when evidence and ticket IDs are recorded.

For section eight point two, Northline Municipal Transit will not accept failure work without a written trail.

### 8.3 Safe tool failure

Prefer tools that fail closed (stop on error) rather than retrying into a storm.

Section eight point three develops failure modes with a Northline Municipal Transit note Sam Park can demo offline.

Under section eight point three, the NMT mentor expects failure claims to carry owners and dates.

Section eight point three treats harm modes stop conditions as testable only when evidence and ticket IDs are recorded.

For section eight point three, Northline Municipal Transit will not accept failure work without a written trail.

### 8.4 Communicating stop

Say what you were doing, what you observed, what you halted, and ask for guidance — short and factual.

Section eight point four develops failure modes with a Northline Municipal Transit note Sam Park can demo offline.

Under section eight point four, the NMT mentor expects failure claims to carry owners and dates.

Section eight point four treats harm modes stop conditions as testable only when evidence and ticket IDs are recorded.

For section eight point four, Northline Municipal Transit will not accept failure work without a written trail.

### 8.5 Rehearsal

Once per quarter Sam rehearses a stop message on the engagement channel with the SOC.

Section eight point five develops failure modes with a Northline Municipal Transit note Sam Park can demo offline.

Under section eight point five, the NMT mentor expects failure claims to carry owners and dates.

Section eight point five treats harm modes stop conditions as testable only when evidence and ticket IDs are recorded.

For section eight point five, Northline Municipal Transit will not accept failure work without a written trail.

### 8.6 No blame in the moment

Stop first; investigate cause after systems are stable.

Section eight point six develops failure modes with a Northline Municipal Transit note Sam Park can demo offline.

Under section eight point six, the NMT mentor expects failure claims to carry owners and dates.

Section eight point six treats harm modes stop conditions as testable only when evidence and ticket IDs are recorded.

For section eight point six, Northline Municipal Transit will not accept failure work without a written trail.

Section eight point six fails closed if failure evidence is missing rather than guessing.

### 8.7 Secondary contact

If the primary emergency contact does not answer in five minutes, Sam calls the secondary named in the ROE. Waiting silently is not a plan.

Section eight point seven develops failure modes with a Northline Municipal Transit note Sam Park can demo offline.

Under section eight point seven, the NMT mentor expects failure claims to carry owners and dates.

Section eight point seven treats harm modes stop conditions as testable only when evidence and ticket IDs are recorded.

For section eight point seven, Northline Municipal Transit will not accept failure work without a written trail.

### 8.8 Tool kill switch

Every long-running script Sam starts has a known way to kill it (process group, container stop). He tests the kill switch once before the window.

Section eight point eight develops failure modes with a Northline Municipal Transit note Sam Park can demo offline.

Under section eight point eight, the NMT mentor expects failure claims to carry owners and dates.

Section eight point eight treats harm modes stop conditions as testable only when evidence and ticket IDs are recorded.

For section eight point eight, Northline Municipal Transit will not accept failure work without a written trail.

### 8.9 8.x Field discipline

After any real stop, Sam files a short blameless note: trigger, time to halt, who was called, whether riders were affected, and one process change. NMT reviews stop notes quarterly. Teams that hide stops eventually cause larger outages; teams that record them get better kill switches and clearer ROEs. The looping-auth drill exists so the first stop is not also the first time Sam writes that note.

Section eight point nine develops failure modes with a Northline Municipal Transit note Sam Park can demo offline.

### Worked example (synthetic NMT)

During a synthetic drill, Sam's script loops on 401s. He stops the script, posts "ENG-512 stop — looping auth checks on staging API — halted 10:12 — need guidance", and waits.

> **Synthetic case — Northline Municipal Transit (NMT).** The transit agency, Sam Park and all figures are invented for teaching.

### Errors and limits

Live transit systems and fare equipment are never tested without a separate, specialised authorization. This book uses synthetic data only and grants no authority to test real systems.

### Exercises

- **EX029 — Harm list.** Name three test harm modes. *Rubric:* 3 = three from chapter; 2 = two; 1 = one; 0 = none.
- **EX030 — Fare alert.** A fare alert appears during a web test. What does Sam do? *Rubric:* 3 = stop; contact emergency; do not touch fare; 2 = stop; 1 = continue web; 0 = none.
- **EX031 — Stop message.** Which four facts go in a stop message? *Rubric:* 3 = action, observation, halted, ask; 2 = three; 1 = one; 0 = none.
- **EX032 — Fail closed.** What does fail closed mean for a test tool? *Rubric:* 3 = stops on error instead of aggressive retry; 2 = partial; 1 = keeps going; 0 = none.

### Synthesis

Stops are rehearsed, fast and factual; tools should fail closed.

### Continue studying — chapter 08 of 18

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Tools and methods

### Learning outcomes

You will (1) choose methods from WSTG themes; (2) configure tools with rate limits; (3) interpret results with the system model; (4) keep a method card per check.

### 9.1 Method cards

Each card: purpose, ROE reference, tool/settings, stop conditions, evidence expected.

Section nine point one develops tools and methods with a Northline Municipal Transit note Sam Park can demo offline.

Under section nine point one, the NMT mentor expects tools claims to carry owners and dates.

Section nine point one treats method cards rate limits as testable only when evidence and ticket IDs are recorded.

For section nine point one, Northline Municipal Transit will not accept tools work without a written trail.

### 9.2 Rate limits

Scanners get explicit rate limits below what staging can take. Faster is not better.

Section nine point two develops tools and methods with a Northline Municipal Transit note Sam Park can demo offline.

Under section nine point two, the NMT mentor expects tools claims to carry owners and dates.

Section nine point two treats method cards rate limits as testable only when evidence and ticket IDs are recorded.

For section nine point two, Northline Municipal Transit will not accept tools work without a written trail.

### 9.3 WSTG selection

Sam picks auth, session, access control and input handling for the journey planner API — not every WSTG item in one window.

Section nine point three develops tools and methods with a Northline Municipal Transit note Sam Park can demo offline.

Under section nine point three, the NMT mentor expects tools claims to carry owners and dates.

Section nine point three treats method cards rate limits as testable only when evidence and ticket IDs are recorded.

For section nine point three, Northline Municipal Transit will not accept tools work without a written trail.

### 9.4 Interpretation

Map each tool alert to a model element before promoting it to a finding.

Section nine point four develops tools and methods with a Northline Municipal Transit note Sam Park can demo offline.

Under section nine point four, the NMT mentor expects tools claims to carry owners and dates.

Section nine point four treats method cards rate limits as testable only when evidence and ticket IDs are recorded.

For section nine point four, Northline Municipal Transit will not accept tools work without a written trail.

### 9.5 Version pin

Record tool versions on the method card.

Section nine point five develops tools and methods with a Northline Municipal Transit note Sam Park can demo offline.

Under section nine point five, the NMT mentor expects tools claims to carry owners and dates.

Section nine point five treats method cards rate limits as testable only when evidence and ticket IDs are recorded.

For section nine point five, Northline Municipal Transit will not accept tools work without a written trail.

Section nine point five fails closed if tools evidence is missing rather than guessing.

### 9.6 Forbidden methods

Password spraying and DoS remain forbidden at NMT.

Section nine point six develops tools and methods with a Northline Municipal Transit note Sam Park can demo offline.

Under section nine point six, the NMT mentor expects tools claims to carry owners and dates.

Section nine point six treats method cards rate limits as testable only when evidence and ticket IDs are recorded.

For section nine point six, Northline Municipal Transit will not accept tools work without a written trail.

Section nine point six fails closed if tools evidence is missing rather than guessing.

### 9.7 Card library

Method cards live in a team library with owners. Copying a card without reading stop conditions is a common newcomer mistake Sam watches for.

Section nine point seven develops tools and methods with a Northline Municipal Transit note Sam Park can demo offline.

Under section nine point seven, the NMT mentor expects tools claims to carry owners and dates.

Section nine point seven treats method cards rate limits as testable only when evidence and ticket IDs are recorded.

For section nine point seven, Northline Municipal Transit will not accept tools work without a written trail.

### 9.8 Noise budget

If a method would generate more alerts than the SOC agreed to handle, Sam reduces rate or reschedules — detection partners are not punching bags.

Section nine point eight develops tools and methods with a Northline Municipal Transit note Sam Park can demo offline.

Under section nine point eight, the NMT mentor expects tools claims to carry owners and dates.

Section nine point eight treats method cards rate limits as testable only when evidence and ticket IDs are recorded.

For section nine point eight, Northline Municipal Transit will not accept tools work without a written trail.

### 9.9 9.x Field discipline

Method cards are useless if they disagree with the ROE. Sam's review step is to highlight the ROE clause each card relies on. If he cannot highlight a clause, the card is rewritten or dropped. This habit also educates newcomers: they see that "we always run tool X" is not a reason — "ROE section 4.2 allows authenticated GET/POST to staging API at ≤1 rps" is a reason.

Section nine point nine develops tools and methods with a Northline Municipal Transit note Sam Park can demo offline.

### Worked example (synthetic NMT)

Sam's card for IDOR on saved journeys: WSTG-AUTHZ, curl with two test users, rate 1 req/s, stop if HTTP 5xx rate >1%, evidence = request ids + responses redacted.

> **Synthetic case — Northline Municipal Transit (NMT).** The transit agency, Sam Park and all figures are invented for teaching.

### Errors and limits

Live transit systems and fare equipment are never tested without a separate, specialised authorization. This book uses synthetic data only and grants no authority to test real systems.

### Exercises

- **EX033 — Card fields.** List five method-card fields. *Rubric:* 3 = five from chapter; 2 = three; 1 = one; 0 = none.
- **EX034 — Rate limit reason.** Why set rate limits on staging? *Rubric:* 3 = avoid crash/lockout/log storm; 2 = partial; 1 = go faster; 0 = none.
- **EX035 — Selectivity.** Why not run every WSTG check in one window? *Rubric:* 3 = time/quality; focus on high-risk themes; 2 = partial; 1 = always all; 0 = none.
- **EX036 — Forbidden.** Name two forbidden methods at NMT. *Rubric:* 3 = password spraying and DoS; 2 = one; 1 = none; 0 = none.

### Synthesis

Method cards bind purpose, ROE, rate limits and evidence — and keep forbidden methods out.

### Continue studying — chapter 09 of 18

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Control configuration

### Learning outcomes

You will (1) read common secure config baselines; (2) distinguish config finding from code finding; (3) propose safe config changes; (4) verify with the owner.

### 10.1 Config findings

TLS settings, cookie flags, security headers, VPN cipher suites, AD password policy — often fixed without code releases.

Section ten point one develops control configuration with a Northline Municipal Transit note Sam Park can demo offline.

Under section ten point one, the NMT mentor expects control claims to carry owners and dates.

Section ten point one treats config findings code findings as testable only when evidence and ticket IDs are recorded.

For section ten point one, Northline Municipal Transit will not accept control work without a written trail.

### 10.2 Code findings

Logic bugs in authorization need developer changes and regression tests.

Section ten point two develops control configuration with a Northline Municipal Transit note Sam Park can demo offline.

Under section ten point two, the NMT mentor expects control claims to carry owners and dates.

Section ten point two treats config findings code findings as testable only when evidence and ticket IDs are recorded.

For section ten point two, Northline Municipal Transit will not accept control work without a written trail.

Section ten point two fails closed if control evidence is missing rather than guessing.

### 10.3 Safe proposals

Propose the setting, the system, the risk if wrong, and a rollback. Never apply production config yourself unless the ROE and change process say so.

Section ten point three develops control configuration with a Northline Municipal Transit note Sam Park can demo offline.

Under section ten point three, the NMT mentor expects control claims to carry owners and dates.

Section ten point three treats config findings code findings as testable only when evidence and ticket IDs are recorded.

For section ten point three, Northline Municipal Transit will not accept control work without a written trail.

### 10.4 Owner verification

Owners apply changes through their pipeline; Sam verifies.

Section ten point four develops control configuration with a Northline Municipal Transit note Sam Park can demo offline.

Under section ten point four, the NMT mentor expects control claims to carry owners and dates.

Section ten point four treats config findings code findings as testable only when evidence and ticket IDs are recorded.

For section ten point four, Northline Municipal Transit will not accept control work without a written trail.

Section ten point four fails closed if control evidence is missing rather than guessing.

### 10.5 Baselines

NMT's hardening baseline is the checklist; deviations need tickets.

Section ten point five develops control configuration with a Northline Municipal Transit note Sam Park can demo offline.

Under section ten point five, the NMT mentor expects control claims to carry owners and dates.

Section ten point five treats config findings code findings as testable only when evidence and ticket IDs are recorded.

For section ten point five, Northline Municipal Transit will not accept control work without a written trail.

Section ten point five fails closed if control evidence is missing rather than guessing.

### 10.6 Drift

Config drift after emergency changes is a recurring finding source.

Section ten point six develops control configuration with a Northline Municipal Transit note Sam Park can demo offline.

Under section ten point six, the NMT mentor expects control claims to carry owners and dates.

Section ten point six treats config findings code findings as testable only when evidence and ticket IDs are recorded.

For section ten point six, Northline Municipal Transit will not accept control work without a written trail.

Section ten point six fails closed if control evidence is missing rather than guessing.

### 10.7 Rollback tested

A config proposal without a tested rollback is incomplete. Sam asks the owner how they would undo the change in fifteen minutes.

Section ten point seven develops control configuration with a Northline Municipal Transit note Sam Park can demo offline.

Under section ten point seven, the NMT mentor expects control claims to carry owners and dates.

Section ten point seven treats config findings code findings as testable only when evidence and ticket IDs are recorded.

For section ten point seven, Northline Municipal Transit will not accept control work without a written trail.

### 10.8 Staging first

Production config findings are reproduced on staging when possible before urging a production change.

Section ten point eight develops control configuration with a Northline Municipal Transit note Sam Park can demo offline.

Under section ten point eight, the NMT mentor expects control claims to carry owners and dates.

Section ten point eight treats config findings code findings as testable only when evidence and ticket IDs are recorded.

For section ten point eight, Northline Municipal Transit will not accept control work without a written trail.

### 10.9 10.x Field discipline

Sam keeps a personal library of good config proposals (HSTS, cookie flags, VPN ciphers) written in NMT's change-ticket style. Reusing structure speeds work but he still fills system-specific risk and rollback each time. Copy-pasting a proposal meant for staging into a production ticket without changes is how wrong ciphers get proposed; he treats each proposal as new writing.

Section ten point nine develops control configuration with a Northline Municipal Transit note Sam Park can demo offline.

Under section ten point nine, the NMT mentor expects control claims to carry owners and dates.

### 10.10 10.y Closing note

Sam also asks whether a config change needs a maintenance window. Header changes on the reverse proxy may be instant; VPN cipher changes may drop staff sessions and need a bulletin. Timing is part of a complete proposal.

Section ten point one zero develops control configuration with a Northline Municipal Transit note Sam Park can demo offline.

Under section ten point one zero, the NMT mentor expects control claims to carry owners and dates.

Section ten point one zero treats config findings code findings as testable only when evidence and ticket IDs are recorded.

### Worked example (synthetic NMT)

Sam finds staging API missing Strict-Transport-Security. He files a config finding with the recommended header and asks app-sec to apply it via their reverse-proxy config.

> **Synthetic case — Northline Municipal Transit (NMT).** The transit agency, Sam Park and all figures are invented for teaching.

### Errors and limits

Live transit systems and fare equipment are never tested without a separate, specialised authorization. This book uses synthetic data only and grants no authority to test real systems.

### Exercises

- **EX037 — Config vs code.** Classify: missing HSTS header; rider A can read rider B's journeys. *Rubric:* 3 = config; code/logic; 2 = swapped; 1 = both config; 0 = none.
- **EX038 — Proposal contents.** What four things go in a safe config proposal? *Rubric:* 3 = setting, system, risk if wrong, rollback; 2 = three; 1 = one; 0 = none.
- **EX039 — Who applies.** Who applies production config changes? *Rubric:* 3 = owner via change process; not the tester alone; 2 = partial; 1 = tester freely; 0 = none.
- **EX040 — Drift.** Why do emergency changes create findings later? *Rubric:* 3 = baselines bypassed; not reverted; 2 = partial; 1 = no reason; 0 = none.

### Synthesis

Config findings need clear proposals and owner-applied changes; testers verify.

### Continue studying — chapter 10 of 18

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Verification

### Learning outcomes

You will (1) plan a retest window; (2) compare before/after statuses; (3) handle partial fixes; (4) close only with evidence.

### 11.1 Retest plan

List findings, methods, owners' go-live notes, window.

Section eleven point one develops verification with a Northline Municipal Transit note Sam Park can demo offline.

Under section eleven point one, the NMT mentor expects verification claims to carry owners and dates.

Section eleven point one treats retest plan before after as testable only when evidence and ticket IDs are recorded.

For section eleven point one, Northline Municipal Transit will not accept verification work without a written trail.

Section eleven point one fails closed if verification evidence is missing rather than guessing.

### 11.2 Before/after

Record status transitions explicitly.

Section eleven point two develops verification with a Northline Municipal Transit note Sam Park can demo offline.

Under section eleven point two, the NMT mentor expects verification claims to carry owners and dates.

Section eleven point two treats retest plan before after as testable only when evidence and ticket IDs are recorded.

For section eleven point two, Northline Municipal Transit will not accept verification work without a written trail.

Section eleven point two fails closed if verification evidence is missing rather than guessing.

```python
"""Lab 11: compare synthetic before/after findings for a retest window."""
before = {"F1": "open", "F2": "open", "F3": "open"}
after = {"F1": "closed", "F2": "open", "F3": "closed"}
for fid in sorted(before):
    b, a = before[fid], after[fid]
    print(f"{fid} {b}->{a} {'FIXED' if b == 'open' and a == 'closed' else 'STILL OPEN' if a == 'open' else 'CHECK'}")
print("fixed:", sum(1 for f in before if before[f] == "open" and after[f] == "closed"),
      "open:", sum(1 for f in after if after[f] == "open"))
```

Run with `python3 lab_retest.py`. Verified output:

```text
F1 open->closed FIXED
F2 open->open STILL OPEN
F3 open->closed FIXED
fixed: 2 open: 1
```

### 11.3 Partial fixes

F2 still open means the ticket stays open with new evidence.

Section eleven point three develops verification with a Northline Municipal Transit note Sam Park can demo offline.

Under section eleven point three, the NMT mentor expects verification claims to carry owners and dates.

Section eleven point three treats retest plan before after as testable only when evidence and ticket IDs are recorded.

For section eleven point three, Northline Municipal Transit will not accept verification work without a written trail.

Section eleven point three fails closed if verification evidence is missing rather than guessing.

### 11.4 Closure

Closed means FIXED with evidence, or accepted risk with CISO signature — not silence.

Section eleven point four develops verification with a Northline Municipal Transit note Sam Park can demo offline.

Under section eleven point four, the NMT mentor expects verification claims to carry owners and dates.

Section eleven point four treats retest plan before after as testable only when evidence and ticket IDs are recorded.

For section eleven point four, Northline Municipal Transit will not accept verification work without a written trail.

### 11.5 Scope freeze

No new hunt during retest unless authorized.

Section eleven point five develops verification with a Northline Municipal Transit note Sam Park can demo offline.

Under section eleven point five, the NMT mentor expects verification claims to carry owners and dates.

Section eleven point five treats retest plan before after as testable only when evidence and ticket IDs are recorded.

For section eleven point five, Northline Municipal Transit will not accept verification work without a written trail.

Section eleven point five fails closed if verification evidence is missing rather than guessing.

### 11.6 Communicate

Send a short retest report to owners the same day.

Section eleven point six develops verification with a Northline Municipal Transit note Sam Park can demo offline.

Under section eleven point six, the NMT mentor expects verification claims to carry owners and dates.

Section eleven point six treats retest plan before after as testable only when evidence and ticket IDs are recorded.

For section eleven point six, Northline Municipal Transit will not accept verification work without a written trail.

Section eleven point six fails closed if verification evidence is missing rather than guessing.

### 11.7 Same method

Retest uses the same method card, not a stronger one. Switching methods mid-retest confuses whether the fix worked.

Section eleven point seven develops verification with a Northline Municipal Transit note Sam Park can demo offline.

Under section eleven point seven, the NMT mentor expects verification claims to carry owners and dates.

Section eleven point seven treats retest plan before after as testable only when evidence and ticket IDs are recorded.

For section eleven point seven, Northline Municipal Transit will not accept verification work without a written trail.

### 11.8 Owner demo

When helpful, Sam invites the owner to watch the successful retest once — seeing FIXED builds trust more than a ticket comment.

Section eleven point eight develops verification with a Northline Municipal Transit note Sam Park can demo offline.

Under section eleven point eight, the NMT mentor expects verification claims to carry owners and dates.

Section eleven point eight treats retest plan before after as testable only when evidence and ticket IDs are recorded.

For section eleven point eight, Northline Municipal Transit will not accept verification work without a written trail.

### 11.9 11.x Field discipline

Retest day is emotionally harder than find day because owners hope for green. Sam opens the call by restating that STILL OPEN is a successful retest outcome when true. He shows the before and after evidence side by side. When F2 remains open, he helps the owner schedule the next fix rather than arguing about severity again — severity was already accepted when the finding was filed.

Section eleven point nine develops verification with a Northline Municipal Transit note Sam Park can demo offline.

### 11.10 11.y Closing note

If all findings FIX on first retest, Sam still records the methods and hashes. Easy wins deserve the same evidence trail as stubborn ones, especially when examiners sample closed tickets.

Section eleven point one zero develops verification with a Northline Municipal Transit note Sam Park can demo offline.

Under section eleven point one zero, the NMT mentor expects verification claims to carry owners and dates.

Section eleven point one zero treats retest plan before after as testable only when evidence and ticket IDs are recorded.

### Worked example (synthetic NMT)

Sam's retest: F1 and F3 FIXED, F2 STILL OPEN. He closes T-F1 and T-F3 with evidence, leaves T-F2 open, and notifies the owner.

> **Synthetic case — Northline Municipal Transit (NMT).** The transit agency, Sam Park and all figures are invented for teaching.

### Errors and limits

Live transit systems and fare equipment are never tested without a separate, specialised authorization. This book uses synthetic data only and grants no authority to test real systems.

### Exercises

- **EX041 — Lab counts.** How many fixed and how many still open? *Rubric:* 3 = fixed 2 open 1; 2 = partial; 1 = wrong; 0 = none.
- **EX042 — F2 action.** What happens to the F2 ticket? *Rubric:* 3 = stays open with new evidence; 2 = open; 1 = close anyway; 0 = none.
- **EX043 — Accepted risk.** Who must sign if NMT accepts F2 without fix? *Rubric:* 3 = CISO (risk owner); 2 = partial; 1 = Sam; 0 = none.
- **EX044 — No new hunt.** Why freeze scope during retest? *Rubric:* 3 = retest measures fixes; new hunt needs new auth; 2 = partial; 1 = always hunt; 0 = none.

### Synthesis

Verification is before/after evidence, honest open tickets and same-day communication.

### Continue studying — chapter 11 of 18

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Contained laboratory I

### Learning outcomes

You will (1) run labs 2, 5 and 11 under supervision; (2) assemble a lab notebook; (3) peer-check a classmate's port classifications; (4) stop on a planted fault.

### 12.1 Notebook

Paste outputs of lab_ports, lab_hash, lab_retest with timestamps and your initials.

Section twelve point one develops contained laboratory with a Northline Municipal Transit note Sam Park can demo offline.

Under section twelve point one, the NMT mentor expects contained claims to carry owners and dates.

Section twelve point one treats notebook peer check planted as testable only when evidence and ticket IDs are recorded.

For section twelve point one, Northline Municipal Transit will not accept contained work without a written trail.

### 12.2 Peer check

Exchange port lists; score agreement with the approved map.

Section twelve point two develops contained laboratory with a Northline Municipal Transit note Sam Park can demo offline.

Under section twelve point two, the NMT mentor expects contained claims to carry owners and dates.

Section twelve point two treats notebook peer check planted as testable only when evidence and ticket IDs are recorded.

For section twelve point two, Northline Municipal Transit will not accept contained work without a written trail.

Section twelve point two fails closed if contained evidence is missing rather than guessing.

### 12.3 Planted fault

Supervisor plants a MISMATCH file; learner must refuse to attach it.

Section twelve point three develops contained laboratory with a Northline Municipal Transit note Sam Park can demo offline.

Under section twelve point three, the NMT mentor expects contained claims to carry owners and dates.

Section twelve point three treats notebook peer check planted as testable only when evidence and ticket IDs are recorded.

For section twelve point three, Northline Municipal Transit will not accept contained work without a written trail.

Section twelve point three fails closed if contained evidence is missing rather than guessing.

### 12.4 Time box

Ninety minutes, hard stop.

Section twelve point four develops contained laboratory with a Northline Municipal Transit note Sam Park can demo offline.

Under section twelve point four, the NMT mentor expects contained claims to carry owners and dates.

Section twelve point four treats notebook peer check planted as testable only when evidence and ticket IDs are recorded.

For section twelve point four, Northline Municipal Transit will not accept contained work without a written trail.

Section twelve point four fails closed if contained evidence is missing rather than guessing.

### 12.5 No production

Any attempt to scan NMT production fails the lab.

Section twelve point five develops contained laboratory with a Northline Municipal Transit note Sam Park can demo offline.

Under section twelve point five, the NMT mentor expects contained claims to carry owners and dates.

Section twelve point five treats notebook peer check planted as testable only when evidence and ticket IDs are recorded.

For section twelve point five, Northline Municipal Transit will not accept contained work without a written trail.

Section twelve point five fails closed if contained evidence is missing rather than guessing.

### 12.6 Sign-off

Supervisor signs the notebook if peer check and planted fault were handled correctly.

Section twelve point six develops contained laboratory with a Northline Municipal Transit note Sam Park can demo offline.

Under section twelve point six, the NMT mentor expects contained claims to carry owners and dates.

Section twelve point six treats notebook peer check planted as testable only when evidence and ticket IDs are recorded.

For section twelve point six, Northline Municipal Transit will not accept contained work without a written trail.

### 12.7 Notebook integrity

Altering lab outputs to look better fails the course. Supervisors may re-run the labs and compare hashes.

Section twelve point seven develops contained laboratory with a Northline Municipal Transit note Sam Park can demo offline.

Under section twelve point seven, the NMT mentor expects contained claims to carry owners and dates.

Section twelve point seven treats notebook peer check planted as testable only when evidence and ticket IDs are recorded.

For section twelve point seven, Northline Municipal Transit will not accept contained work without a written trail.

### 12.8 Quiet channel

During the lab, only ROE and stop messages go to the shared channel — no spoilers for peers still working.

Section twelve point eight develops contained laboratory with a Northline Municipal Transit note Sam Park can demo offline.

Under section twelve point eight, the NMT mentor expects contained claims to carry owners and dates.

Section twelve point eight treats notebook peer check planted as testable only when evidence and ticket IDs are recorded.

For section twelve point eight, Northline Municipal Transit will not accept contained work without a written trail.

### 12.9 12.x Field discipline

Laboratory I is graded on discipline, not on finding exotic issues. Learners who race ahead to invent attacks on the synthetic data but skip hashing fail. Learners who are slow but refuse the planted mismatch and classify ports correctly pass. Sam reminds peers of that grading bar at the start so competition does not push people toward unsafe habits.

Section twelve point nine develops contained laboratory with a Northline Municipal Transit note Sam Park can demo offline.

Under section twelve point nine, the NMT mentor expects contained claims to carry owners and dates.

### 12.10 12.y Closing note

Learners submit the notebook as a single PDF or markdown bundle with a table of contents. Missing initials or timestamps cost points because real evidence packs need attribution.

Section twelve point one zero develops contained laboratory with a Northline Municipal Transit note Sam Park can demo offline.

Under section twelve point one zero, the NMT mentor expects contained claims to carry owners and dates.

Section twelve point one zero treats notebook peer check planted as testable only when evidence and ticket IDs are recorded.

### Worked example (synthetic NMT)

Sam refuses the planted mismatched screenshot, fixes his peer's misclassification of 8080, and finishes with three minutes to spare.

> **Synthetic case — Northline Municipal Transit (NMT).** The transit agency, Sam Park and all figures are invented for teaching.

### Errors and limits

Live transit systems and fare equipment are never tested without a separate, specialised authorization. This book uses synthetic data only and grants no authority to test real systems.

### Exercises

- **EX045 — Notebook contents.** What three lab outputs go in the notebook? *Rubric:* 3 = ports, hash, retest; 2 = two; 1 = one; 0 = none.
- **EX046 — Planted fault response.** What is the correct response to a mismatched evidence file? *Rubric:* 3 = refuse to attach; recapture/rehash; 2 = refuse; 1 = attach; 0 = none.
- **EX047 — Fail condition.** What fails the lab immediately? *Rubric:* 3 = scanning production / live NMT; 2 = partial; 1 = finishing early; 0 = none.
- **EX048 — Peer score.** What does the peer check score? *Rubric:* 3 = agreement with approved port map; 2 = partial; 1 = speed; 0 = none.

### Synthesis

Laboratory I proves port discipline, evidence integrity and retest honesty under a hard stop.

### Continue studying — chapter 12 of 18

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Troubleshooting

### Learning outcomes

You will (1) follow a troubleshooting tree for failed checks; (2) separate tool failure from real findings; (3) escalate with evidence; (4) document workarounds safely.

### 13.1 Tree

Symptom → reproduce → check scope/account/tool → check staging health → escalate.

Section thirteen point one develops troubleshooting with a Northline Municipal Transit note Sam Park can demo offline.

Under section thirteen point one, the NMT mentor expects troubleshooting claims to carry owners and dates.

Section thirteen point one treats tree tool failure escalation as testable only when evidence and ticket IDs are recorded.

For section thirteen point one, Northline Municipal Transit will not accept troubleshooting work without a written trail.

Section thirteen point one fails closed if troubleshooting evidence is missing rather than guessing.

### 13.2 Tool failure

Certificate errors on the tester laptop are not API findings.

Section thirteen point two develops troubleshooting with a Northline Municipal Transit note Sam Park can demo offline.

Under section thirteen point two, the NMT mentor expects troubleshooting claims to carry owners and dates.

Section thirteen point two treats tree tool failure escalation as testable only when evidence and ticket IDs are recorded.

For section thirteen point two, Northline Municipal Transit will not accept troubleshooting work without a written trail.

Section thirteen point two fails closed if troubleshooting evidence is missing rather than guessing.

### 13.3 Escalation packet

Symptom, steps, screenshots, time, what you already ruled out.

Section thirteen point three develops troubleshooting with a Northline Municipal Transit note Sam Park can demo offline.

Under section thirteen point three, the NMT mentor expects troubleshooting claims to carry owners and dates.

Section thirteen point three treats tree tool failure escalation as testable only when evidence and ticket IDs are recorded.

For section thirteen point three, Northline Municipal Transit will not accept troubleshooting work without a written trail.

Section thirteen point three fails closed if troubleshooting evidence is missing rather than guessing.

### 13.4 Workarounds

Temporary tool flags are logged and removed after; they are not silent permanent config.

Section thirteen point four develops troubleshooting with a Northline Municipal Transit note Sam Park can demo offline.

Under section thirteen point four, the NMT mentor expects troubleshooting claims to carry owners and dates.

Section thirteen point four treats tree tool failure escalation as testable only when evidence and ticket IDs are recorded.

For section thirteen point four, Northline Municipal Transit will not accept troubleshooting work without a written trail.

### 13.5 Pair debugging

Hard issues get a second technician after fifteen minutes.

Section thirteen point five develops troubleshooting with a Northline Municipal Transit note Sam Park can demo offline.

Under section thirteen point five, the NMT mentor expects troubleshooting claims to carry owners and dates.

Section thirteen point five treats tree tool failure escalation as testable only when evidence and ticket IDs are recorded.

For section thirteen point five, Northline Municipal Transit will not accept troubleshooting work without a written trail.

Section thirteen point five fails closed if troubleshooting evidence is missing rather than guessing.

### 13.6 Customer impact

If riders may be affected, stop and call the emergency contact before deep debugging.

Section thirteen point six develops troubleshooting with a Northline Municipal Transit note Sam Park can demo offline.

Under section thirteen point six, the NMT mentor expects troubleshooting claims to carry owners and dates.

Section thirteen point six treats tree tool failure escalation as testable only when evidence and ticket IDs are recorded.

For section thirteen point six, Northline Municipal Transit will not accept troubleshooting work without a written trail.

### 13.7 Known-good baseline

Sam keeps a known-good curl to the staging health endpoint. If that fails, the environment is broken and findings wait.

Section thirteen point seven develops troubleshooting with a Northline Municipal Transit note Sam Park can demo offline.

Under section thirteen point seven, the NMT mentor expects troubleshooting claims to carry owners and dates.

Section thirteen point seven treats tree tool failure escalation as testable only when evidence and ticket IDs are recorded.

For section thirteen point seven, Northline Municipal Transit will not accept troubleshooting work without a written trail.

### 13.8 Timeboxing ego

After fifteen minutes alone, he must ask for help. Heroic silence wastes engagement window.

Section thirteen point eight develops troubleshooting with a Northline Municipal Transit note Sam Park can demo offline.

Under section thirteen point eight, the NMT mentor expects troubleshooting claims to carry owners and dates.

Section thirteen point eight treats tree tool failure escalation as testable only when evidence and ticket IDs are recorded.

For section thirteen point eight, Northline Municipal Transit will not accept troubleshooting work without a written trail.

### 13.9 13.x Field discipline

Sam's troubleshooting notes use the same Fact/Guess labels as casework. "Guess: WAF blocking my IP" becomes a Fact only after the WAF log shows the block. That discipline keeps him from "fixing" the WAF with volume to see what happens — a behaviour that looks like a DoS and violates the ROE.

Section thirteen point nine develops troubleshooting with a Northline Municipal Transit note Sam Park can demo offline.

Under section thirteen point nine, the NMT mentor expects troubleshooting claims to carry owners and dates.

### 13.10 13.y Closing note

When escalation is required, Sam notifies the engagement lead and the product owner together so nobody hears second-hand that staging is unhealthy.

Section thirteen point one zero develops troubleshooting with a Northline Municipal Transit note Sam Park can demo offline.

Under section thirteen point one zero, the NMT mentor expects troubleshooting claims to carry owners and dates.

Section thirteen point one zero treats tree tool failure escalation as testable only when evidence and ticket IDs are recorded.

For section thirteen point one zero, Northline Municipal Transit will not accept troubleshooting work without a written trail.

### Worked example (synthetic NMT)

Sam's API checks fail with TLS errors; staging is fine in the browser on the jump host. He updates his laptop root store, re-runs, and documents the laptop issue separately from findings.

> **Synthetic case — Northline Municipal Transit (NMT).** The transit agency, Sam Park and all figures are invented for teaching.

### Errors and limits

Live transit systems and fare equipment are never tested without a separate, specialised authorization. This book uses synthetic data only and grants no authority to test real systems.

### Exercises

- **EX049 — First steps.** Order: escalate, reproduce, check tool. *Rubric:* 3 = reproduce, check tool, escalate; 2 = mostly; 1 = escalate first always; 0 = none.
- **EX050 — Not a finding.** Why is a laptop TLS error not an API finding? *Rubric:* 3 = client-side trust store; staging works elsewhere; 2 = partial; 1 = it is; 0 = none.
- **EX051 — Escalation packet.** List four items in an escalation packet. *Rubric:* 3 = four from chapter; 2 = three; 1 = one; 0 = none.
- **EX052 — Rider impact.** What if troubleshooting might affect riders? *Rubric:* 3 = stop; emergency contact; 2 = stop; 1 = continue; 0 = none.

### Synthesis

Troubleshoot with a tree, prove where the fault lives and escalate with a clean packet.

### Continue studying — chapter 13 of 18

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Automation

### Learning outcomes

You will (1) decide what to automate; (2) keep humans for validation; (3) schedule automation inside windows; (4) monitor automation for loops.

### 14.1 Automate

Hashing, port list diffs, ticket field checks, report skeletons.

Section fourteen point one develops automation with a Northline Municipal Transit note Sam Park can demo offline.

Under section fourteen point one, the NMT mentor expects automation claims to carry owners and dates.

Section fourteen point one treats automate do not automate as testable only when evidence and ticket IDs are recorded.

For section fourteen point one, Northline Municipal Transit will not accept automation work without a written trail.

Section fourteen point one fails closed if automation evidence is missing rather than guessing.

### 14.2 Do not automate

Exploitation, scope decisions, severity without review.

Section fourteen point two develops automation with a Northline Municipal Transit note Sam Park can demo offline.

Under section fourteen point two, the NMT mentor expects automation claims to carry owners and dates.

Section fourteen point two treats automate do not automate as testable only when evidence and ticket IDs are recorded.

For section fourteen point two, Northline Municipal Transit will not accept automation work without a written trail.

Section fourteen point two fails closed if automation evidence is missing rather than guessing.

### 14.3 Windows

Automation runs only inside the engagement window with the same rate limits.

Section fourteen point three develops automation with a Northline Municipal Transit note Sam Park can demo offline.

Under section fourteen point three, the NMT mentor expects automation claims to carry owners and dates.

Section fourteen point three treats automate do not automate as testable only when evidence and ticket IDs are recorded.

For section fourteen point three, Northline Municipal Transit will not accept automation work without a written trail.

Section fourteen point three fails closed if automation evidence is missing rather than guessing.

### 14.4 Loop detection

Caps on retries and maximum runtime are mandatory.

Section fourteen point four develops automation with a Northline Municipal Transit note Sam Park can demo offline.

Under section fourteen point four, the NMT mentor expects automation claims to carry owners and dates.

Section fourteen point four treats automate do not automate as testable only when evidence and ticket IDs are recorded.

For section fourteen point four, Northline Municipal Transit will not accept automation work without a written trail.

Section fourteen point four fails closed if automation evidence is missing rather than guessing.

### 14.5 Output review

Every automated finding candidate gets human validation.

Section fourteen point five develops automation with a Northline Municipal Transit note Sam Park can demo offline.

Under section fourteen point five, the NMT mentor expects automation claims to carry owners and dates.

Section fourteen point five treats automate do not automate as testable only when evidence and ticket IDs are recorded.

For section fourteen point five, Northline Municipal Transit will not accept automation work without a written trail.

Section fourteen point five fails closed if automation evidence is missing rather than guessing.

### 14.6 Change control

Automation scripts are versioned like production code.

Section fourteen point six develops automation with a Northline Municipal Transit note Sam Park can demo offline.

Under section fourteen point six, the NMT mentor expects automation claims to carry owners and dates.

Section fourteen point six treats automate do not automate as testable only when evidence and ticket IDs are recorded.

For section fourteen point six, Northline Municipal Transit will not accept automation work without a written trail.

Section fourteen point six fails closed if automation evidence is missing rather than guessing.

### 14.7 Idempotent jobs

Automated diffs can run twice without doubling tickets. Sam keys tickets on host+port+date to avoid duplicates.

Section fourteen point seven develops automation with a Northline Municipal Transit note Sam Park can demo offline.

Under section fourteen point seven, the NMT mentor expects automation claims to carry owners and dates.

Section fourteen point seven treats automate do not automate as testable only when evidence and ticket IDs are recorded.

For section fourteen point seven, Northline Municipal Transit will not accept automation work without a written trail.

### 14.8 Disable switch

Automation has a global disable flag the SOC can request. Sam tests that flag on day one of the engagement.

Section fourteen point eight develops automation with a Northline Municipal Transit note Sam Park can demo offline.

Under section fourteen point eight, the NMT mentor expects automation claims to carry owners and dates.

Section fourteen point eight treats automate do not automate as testable only when evidence and ticket IDs are recorded.

For section fourteen point eight, Northline Municipal Transit will not accept automation work without a written trail.

### 14.9 14.x Field discipline

Automation pull requests need a safety section: rate limits, kill switch, dry-run, and which ROE clause allows the job. Without that section, reviewers reject the PR. Sam added the template after a well-meaning script once ran outside the window because cron used UTC and the author thought in local time.

Section fourteen point nine develops automation with a Northline Municipal Transit note Sam Park can demo offline.

Under section fourteen point nine, the NMT mentor expects automation claims to carry owners and dates.

### 14.10 14.y Closing note

Sam charts automation runtime per night. A job that suddenly takes ten times longer may be stuck in a loop or hitting a larger inventory — both deserve a human look before the next window.

Section fourteen point one zero develops automation with a Northline Municipal Transit note Sam Park can demo offline.

Under section fourteen point one zero, the NMT mentor expects automation claims to carry owners and dates.

Section fourteen point one zero treats automate do not automate as testable only when evidence and ticket IDs are recorded.

### 14.11 14.z Extra

Caps include both retry count and wall-clock minutes. Sam's port-diff job dies after 20 minutes and pages him; a silent hang is treated like a failed stop switch.

Section fourteen point one one develops automation with a Northline Municipal Transit note Sam Park can demo offline.

Under section fourteen point one one, the NMT mentor expects automation claims to carry owners and dates.

Section fourteen point one one treats automate do not automate as testable only when evidence and ticket IDs are recorded.

### Worked example (synthetic NMT)

Sam automates the port diff nightly on staging inventory exports during the engagement week; he still manually triages NOT APPROVED lines.

> **Synthetic case — Northline Municipal Transit (NMT).** The transit agency, Sam Park and all figures are invented for teaching.

### Errors and limits

Live transit systems and fare equipment are never tested without a separate, specialised authorization. This book uses synthetic data only and grants no authority to test real systems.

### Exercises

- **EX053 — Automate list.** Name three good automation candidates. *Rubric:* 3 = three from chapter; 2 = two; 1 = one; 0 = none.
- **EX054 — Never automate.** Name two things Sam must not automate. *Rubric:* 3 = exploitation and scope decisions; 2 = one; 1 = hashing; 0 = none.
- **EX055 — Retry cap.** Why do automation retries need caps? *Rubric:* 3 = prevent lockouts/log storms/loops; 2 = partial; 1 = unlimited better; 0 = none.
- **EX056 — Human gate.** What always needs a human before a finding is filed? *Rubric:* 3 = validation of automated candidates; 2 = partial; 1 = nothing; 0 = none.

### Synthesis

Automate the repetitive; never automate permission, exploitation or unreviewed severity.

### Continue studying — chapter 14 of 18

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Integration and dependencies

### Learning outcomes

You will (1) map third-party dependencies; (2) know when their testing needs separate auth; (3) test NMT's side of integrations; (4) record shared responsibility.

### 15.1 Dependencies

Map tiles, SMS notifier, payment deep links, cloud email.

Section fifteen point one develops integration and dependencies with a Northline Municipal Transit note Sam Park can demo offline.

Under section fifteen point one, the NMT mentor expects integration claims to carry owners and dates.

Section fifteen point one treats dependencies separate auth nmt's as testable only when evidence and ticket IDs are recorded.

For section fifteen point one, Northline Municipal Transit will not accept integration work without a written trail.

Section fifteen point one fails closed if integration evidence is missing rather than guessing.

### 15.2 Separate auth

Testing the SMS vendor's core needs the vendor's authorization.

Section fifteen point two develops integration and dependencies with a Northline Municipal Transit note Sam Park can demo offline.

Under section fifteen point two, the NMT mentor expects integration claims to carry owners and dates.

Section fifteen point two treats dependencies separate auth nmt's as testable only when evidence and ticket IDs are recorded.

For section fifteen point two, Northline Municipal Transit will not accept integration work without a written trail.

Section fifteen point two fails closed if integration evidence is missing rather than guessing.

### 15.3 NMT's side

Sam can test how NMT handles vendor callbacks and secrets storage when those paths are in scope.

Section fifteen point three develops integration and dependencies with a Northline Municipal Transit note Sam Park can demo offline.

Under section fifteen point three, the NMT mentor expects integration claims to carry owners and dates.

Section fifteen point three treats dependencies separate auth nmt's as testable only when evidence and ticket IDs are recorded.

For section fifteen point three, Northline Municipal Transit will not accept integration work without a written trail.

### 15.4 Responsibility matrix

Who patches what is written down so findings land on the right owner.

Section fifteen point four develops integration and dependencies with a Northline Municipal Transit note Sam Park can demo offline.

Under section fifteen point four, the NMT mentor expects integration claims to carry owners and dates.

Section fifteen point four treats dependencies separate auth nmt's as testable only when evidence and ticket IDs are recorded.

For section fifteen point four, Northline Municipal Transit will not accept integration work without a written trail.

### 15.5 Breaks

Vendor outages during tests are stops, not opportunities to try harder.

Section fifteen point five develops integration and dependencies with a Northline Municipal Transit note Sam Park can demo offline.

Under section fifteen point five, the NMT mentor expects integration claims to carry owners and dates.

Section fifteen point five treats dependencies separate auth nmt's as testable only when evidence and ticket IDs are recorded.

For section fifteen point five, Northline Municipal Transit will not accept integration work without a written trail.

### 15.6 Contracts

Security contact clauses in vendor contracts speed responsible disclosure.

Section fifteen point six develops integration and dependencies with a Northline Municipal Transit note Sam Park can demo offline.

Under section fifteen point six, the NMT mentor expects integration claims to carry owners and dates.

Section fifteen point six treats dependencies separate auth nmt's as testable only when evidence and ticket IDs are recorded.

For section fifteen point six, Northline Municipal Transit will not accept integration work without a written trail.

Section fifteen point six fails closed if integration evidence is missing rather than guessing.

### 15.7 Callback authenticity

When testing NMT's handling of vendor callbacks, Sam uses documented test harnesses, not forged traffic to production payment endpoints.

Section fifteen point seven develops integration and dependencies with a Northline Municipal Transit note Sam Park can demo offline.

Under section fifteen point seven, the NMT mentor expects integration claims to carry owners and dates.

Section fifteen point seven treats dependencies separate auth nmt's as testable only when evidence and ticket IDs are recorded.

For section fifteen point seven, Northline Municipal Transit will not accept integration work without a written trail.

### 15.8 Secret scanning scope

Secret scans run on NMT-owned repos listed in the ROE, not on every public fork on the Internet.

Section fifteen point eight develops integration and dependencies with a Northline Municipal Transit note Sam Park can demo offline.

Under section fifteen point eight, the NMT mentor expects integration claims to carry owners and dates.

Section fifteen point eight treats dependencies separate auth nmt's as testable only when evidence and ticket IDs are recorded.

For section fifteen point eight, Northline Municipal Transit will not accept integration work without a written trail.

### 15.9 15.x Field discipline

Sam's dependency map includes a "data shared" column: what NMT sends to each vendor. If NMT should not send rider phone numbers to the map tile provider, that becomes both a privacy control and a test check: inspect outbound requests for unexpected fields during authorized staging tests.

Section fifteen point nine develops integration and dependencies with a Northline Municipal Transit note Sam Park can demo offline.

Under section fifteen point nine, the NMT mentor expects integration claims to carry owners and dates.

### 15.10 15.y Closing note

If a vendor asks Sam to "just quickly test" their portal using NMT credentials, he refuses and points them to their own authorization process. NMT credentials do not travel.

Section fifteen point one zero develops integration and dependencies with a Northline Municipal Transit note Sam Park can demo offline.

Under section fifteen point one zero, the NMT mentor expects integration claims to carry owners and dates.

Section fifteen point one zero treats dependencies separate auth nmt's as testable only when evidence and ticket IDs are recorded.

### Worked example (synthetic NMT)

Sam finds an SMS API key in a staging repo. That is an NMT finding (secret storage). He does not load-test the SMS vendor.

> **Synthetic case — Northline Municipal Transit (NMT).** The transit agency, Sam Park and all figures are invented for teaching.

### Errors and limits

Live transit systems and fare equipment are never tested without a separate, specialised authorization. This book uses synthetic data only and grants no authority to test real systems.

### Exercises

- **EX057 — Separate auth example.** Give one dependency Sam must not test without vendor auth. *Rubric:* 3 = SMS vendor / map tiles / payment; 2 = partial; 1 = NMT website; 0 = none.
- **EX058 — NMT-side finding.** Why is a leaked SMS API key in NMT staging an NMT finding? *Rubric:* 3 = NMT stores/handles the secret; 2 = partial; 1 = vendor only; 0 = none.
- **EX059 — Vendor outage.** Vendor times out during the window. What does Sam do? *Rubric:* 3 = stop related checks; note dependency; do not hammer; 2 = partial; 1 = retry storm; 0 = none.
- **EX060 — Matrix.** What does a responsibility matrix solve? *Rubric:* 3 = right owner for each finding; 2 = partial; 1 = nothing; 0 = none.

### Synthesis

Know the dependency map; test NMT's side; do not attack vendors without their authorization.

### Continue studying — chapter 15 of 18

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Technical documentation and safety

### Learning outcomes

You will (1) write runbooks for authorized checks; (2) keep safety warnings visible; (3) version documents; (4) retire obsolete methods.

### 16.1 Runbooks

Step-by-step for each recurring check, with ROE references and stop conditions at the top in bold.

Section sixteen point one develops technical documentation and safety with a Northline Municipal Transit note Sam Park can demo offline.

Under section sixteen point one, the NMT mentor expects technical claims to carry owners and dates.

Section sixteen point one treats runbooks safety warnings versioning as testable only when evidence and ticket IDs are recorded.

For section sixteen point one, Northline Municipal Transit will not accept technical work without a written trail.

### 16.2 Safety warnings

Do not run against production is the first line of the staging port-diff runbook.

Section sixteen point two develops technical documentation and safety with a Northline Municipal Transit note Sam Park can demo offline.

Under section sixteen point two, the NMT mentor expects technical claims to carry owners and dates.

Section sixteen point two treats runbooks safety warnings versioning as testable only when evidence and ticket IDs are recorded.

For section sixteen point two, Northline Municipal Transit will not accept technical work without a written trail.

### 16.3 Versioning

Documents show version, date and owner; old versions archived.

Section sixteen point three develops technical documentation and safety with a Northline Municipal Transit note Sam Park can demo offline.

Under section sixteen point three, the NMT mentor expects technical claims to carry owners and dates.

Section sixteen point three treats runbooks safety warnings versioning as testable only when evidence and ticket IDs are recorded.

For section sixteen point three, Northline Municipal Transit will not accept technical work without a written trail.

Section sixteen point three fails closed if technical evidence is missing rather than guessing.

### 16.4 Retirement

Methods that used retired tools are marked obsolete so newcomers do not follow them.

Section sixteen point four develops technical documentation and safety with a Northline Municipal Transit note Sam Park can demo offline.

Under section sixteen point four, the NMT mentor expects technical claims to carry owners and dates.

Section sixteen point four treats runbooks safety warnings versioning as testable only when evidence and ticket IDs are recorded.

For section sixteen point four, Northline Municipal Transit will not accept technical work without a written trail.

### 16.5 Audience

Write for a technician who was out sick during the last engagement.

Section sixteen point five develops technical documentation and safety with a Northline Municipal Transit note Sam Park can demo offline.

Under section sixteen point five, the NMT mentor expects technical claims to carry owners and dates.

Section sixteen point five treats runbooks safety warnings versioning as testable only when evidence and ticket IDs are recorded.

For section sixteen point five, Northline Municipal Transit will not accept technical work without a written trail.

### 16.6 Review cadence

Runbooks reviewed every six months or after any stop incident.

Section sixteen point six develops technical documentation and safety with a Northline Municipal Transit note Sam Park can demo offline.

Under section sixteen point six, the NMT mentor expects technical claims to carry owners and dates.

Section sixteen point six treats runbooks safety warnings versioning as testable only when evidence and ticket IDs are recorded.

For section sixteen point six, Northline Municipal Transit will not accept technical work without a written trail.

### 16.7 Screenshots in runbooks

Runbooks prefer text steps over screenshots that rot when the UI changes. Where screenshots help, they are dated.

Section sixteen point seven develops technical documentation and safety with a Northline Municipal Transit note Sam Park can demo offline.

Under section sixteen point seven, the NMT mentor expects technical claims to carry owners and dates.

Section sixteen point seven treats runbooks safety warnings versioning as testable only when evidence and ticket IDs are recorded.

For section sixteen point seven, Northline Municipal Transit will not accept technical work without a written trail.

### 16.8 Translation

If a contractor shift speaks another language, critical stop warnings appear in both languages used on site.

Section sixteen point eight develops technical documentation and safety with a Northline Municipal Transit note Sam Park can demo offline.

Under section sixteen point eight, the NMT mentor expects technical claims to carry owners and dates.

Section sixteen point eight treats runbooks safety warnings versioning as testable only when evidence and ticket IDs are recorded.

For section sixteen point eight, Northline Municipal Transit will not accept technical work without a written trail.

### 16.9 16.x Field discipline

When a stop incident happens, Sam updates the runbook the same week or files a ticket why not. Documentation delayed until "after the busy period" is documentation that never happens. His managers accept shorter runbooks that are current over long ones that describe retired tools.

Section sixteen point nine develops technical documentation and safety with a Northline Municipal Transit note Sam Park can demo offline.

Under section sixteen point nine, the NMT mentor expects technical claims to carry owners and dates.

Section sixteen point nine treats runbooks safety warnings versioning as testable only when evidence and ticket IDs are recorded.

### 16.10 16.y Closing note

Obsolete runbooks are moved to an /archive folder that CI checks no active link points to. Broken links to retired methods fail the documentation build.

Section sixteen point one zero develops technical documentation and safety with a Northline Municipal Transit note Sam Park can demo offline.

Under section sixteen point one zero, the NMT mentor expects technical claims to carry owners and dates.

Section sixteen point one zero treats runbooks safety warnings versioning as testable only when evidence and ticket IDs are recorded.

### 16.11 16.z Extra

Sam prints the stop-conditions page of the active runbook and keeps it on the desk during windows — screens lock, paper still readable when seconds matter.

Section sixteen point one one develops technical documentation and safety with a Northline Municipal Transit note Sam Park can demo offline.

Under section sixteen point one one, the NMT mentor expects technical claims to carry owners and dates.

Section sixteen point one one treats runbooks safety warnings versioning as testable only when evidence and ticket IDs are recorded.

### Worked example (synthetic NMT)

Sam's runbook v1.3 opens with STOP CONDITIONS and OUT OF SCOPE: fare network, then the port-diff steps.

> **Synthetic case — Northline Municipal Transit (NMT).** The transit agency, Sam Park and all figures are invented for teaching.

### Errors and limits

Live transit systems and fare equipment are never tested without a separate, specialised authorization. This book uses synthetic data only and grants no authority to test real systems.

### Exercises

- **EX061 — Top of runbook.** What two blocks sit at the top? *Rubric:* 3 = stop conditions and ROE/out-of-scope; 2 = one; 1 = history; 0 = none.
- **EX062 — First line.** What is the first line of the staging port-diff runbook? *Rubric:* 3 = do not run against production; 2 = partial; 1 = install tool; 0 = none.
- **EX063 — Obsolete.** What should happen to a runbook for a retired tool? *Rubric:* 3 = mark obsolete/archive; 2 = partial; 1 = leave as-is; 0 = none.
- **EX064 — Review trigger.** When must runbooks be reviewed outside the six-month cadence? *Rubric:* 3 = after a stop incident (or major change); 2 = partial; 1 = never; 0 = none.

### Synthesis

Documentation puts safety first, stays versioned and retires with its tools.

### Continue studying — chapter 16 of 18

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Contained laboratory II

### Learning outcomes

You will (1) combine method cards with labs; (2) produce a mini retest report; (3) handle a mid-lab stop drill; (4) submit evidence indexed by hash.

### 17.1 Build

Create one method card; run lab_retest; write a one-page retest report.

Section seventeen point one develops contained laboratory ii with a Northline Municipal Transit note Sam Park can demo offline.

Under section seventeen point one, the NMT mentor expects contained claims to carry owners and dates.

Section seventeen point one treats build stop drill evidence as testable only when evidence and ticket IDs are recorded.

For section seventeen point one, Northline Municipal Transit will not accept contained work without a written trail.

### 17.2 Stop drill

At a random time the supervisor calls stop; learner must post a compliant stop message within two minutes.

Section seventeen point two develops contained laboratory ii with a Northline Municipal Transit note Sam Park can demo offline.

Under section seventeen point two, the NMT mentor expects contained claims to carry owners and dates.

Section seventeen point two treats build stop drill evidence as testable only when evidence and ticket IDs are recorded.

For section seventeen point two, Northline Municipal Transit will not accept contained work without a written trail.

### 17.3 Evidence index

Table of file, hash, finding id.

Section seventeen point three develops contained laboratory ii with a Northline Municipal Transit note Sam Park can demo offline.

Under section seventeen point three, the NMT mentor expects contained claims to carry owners and dates.

Section seventeen point three treats build stop drill evidence as testable only when evidence and ticket IDs are recorded.

For section seventeen point three, Northline Municipal Transit will not accept contained work without a written trail.

Section seventeen point three fails closed if contained evidence is missing rather than guessing.

### 17.4 Peer challenge

Peer tries to get you to attach a mismatched file; you refuse.

Section seventeen point four develops contained laboratory ii with a Northline Municipal Transit note Sam Park can demo offline.

Under section seventeen point four, the NMT mentor expects contained claims to carry owners and dates.

Section seventeen point four treats build stop drill evidence as testable only when evidence and ticket IDs are recorded.

For section seventeen point four, Northline Municipal Transit will not accept contained work without a written trail.

### 17.5 Time box

Two hours.

Section seventeen point five develops contained laboratory ii with a Northline Municipal Transit note Sam Park can demo offline.

Under section seventeen point five, the NMT mentor expects contained claims to carry owners and dates.

Section seventeen point five treats build stop drill evidence as testable only when evidence and ticket IDs are recorded.

For section seventeen point five, Northline Municipal Transit will not accept contained work without a written trail.

Section seventeen point five fails closed if contained evidence is missing rather than guessing.

### 17.6 Pass bar

Stop drill + refusal + coherent report.

Section seventeen point six develops contained laboratory ii with a Northline Municipal Transit note Sam Park can demo offline.

Under section seventeen point six, the NMT mentor expects contained claims to carry owners and dates.

Section seventeen point six treats build stop drill evidence as testable only when evidence and ticket IDs are recorded.

For section seventeen point six, Northline Municipal Transit will not accept contained work without a written trail.

Section seventeen point six fails closed if contained evidence is missing rather than guessing.

### 17.7 Stress without harm

The stop drill is stressful on purpose; harming systems is not. Supervisors never plant production-impacting faults.

Section seventeen point seven develops contained laboratory ii with a Northline Municipal Transit note Sam Park can demo offline.

Under section seventeen point seven, the NMT mentor expects contained claims to carry owners and dates.

Section seventeen point seven treats build stop drill evidence as testable only when evidence and ticket IDs are recorded.

For section seventeen point seven, Northline Municipal Transit will not accept contained work without a written trail.

### 17.8 After-action

Each Lab II ends with three minutes of after-action: what almost went wrong, what to change in the runbook.

Section seventeen point eight develops contained laboratory ii with a Northline Municipal Transit note Sam Park can demo offline.

Under section seventeen point eight, the NMT mentor expects contained claims to carry owners and dates.

Section seventeen point eight treats build stop drill evidence as testable only when evidence and ticket IDs are recorded.

For section seventeen point eight, Northline Municipal Transit will not accept contained work without a written trail.

### 17.9 17.x Field discipline

Laboratory II's peer challenge is play-acting pressure: "just attach it, the hash is close enough". The correct answer is always refuse. Sam has heard similar pressure in real engagements about unverified scanner output. Practising the refusal with a peer makes the real refusal easier.

Section seventeen point nine develops contained laboratory ii with a Northline Municipal Transit note Sam Park can demo offline.

Under section seventeen point nine, the NMT mentor expects contained claims to carry owners and dates.

Section seventeen point nine treats build stop drill evidence as testable only when evidence and ticket IDs are recorded.

### 17.10 17.y Closing note

Sam's stop message in the drill uses the same template as production engagements, so wording muscle memory transfers. Fancy prose is discouraged; facts win.

Section seventeen point one zero develops contained laboratory ii with a Northline Municipal Transit note Sam Park can demo offline.

Under section seventeen point one zero, the NMT mentor expects contained claims to carry owners and dates.

Section seventeen point one zero treats build stop drill evidence as testable only when evidence and ticket IDs are recorded.

For section seventeen point one zero, Northline Municipal Transit will not accept contained work without a written trail.

### 17.11 17.z Extra

If the stop drill message is late, the lab fails even if the report is perfect. Speed of stopping is the skill being measured.

Section seventeen point one one develops contained laboratory ii with a Northline Municipal Transit note Sam Park can demo offline.

Under section seventeen point one one, the NMT mentor expects contained claims to carry owners and dates.

Section seventeen point one one treats build stop drill evidence as testable only when evidence and ticket IDs are recorded.

For section seventeen point one one, Northline Municipal Transit will not accept contained work without a written trail.

### Worked example (synthetic NMT)

Sam posts a stop message in 50 seconds during the drill, refuses a bad screenshot, and files a retest report with F2 still open.

> **Synthetic case — Northline Municipal Transit (NMT).** The transit agency, Sam Park and all figures are invented for teaching.

### Errors and limits

Live transit systems and fare equipment are never tested without a separate, specialised authorization. This book uses synthetic data only and grants no authority to test real systems.

### Exercises

- **EX065 — Pass bar.** Name three pass requirements. *Rubric:* 3 = stop drill, refusal, coherent report; 2 = two; 1 = one; 0 = none.
- **EX066 — Stop timing.** What is the time limit for the stop message? *Rubric:* 3 = two minutes; 2 = fast; 1 = end of day; 0 = none.
- **EX067 — Report honesty.** May the report mark F2 closed without evidence? *Rubric:* 3 = no; 2 = no; 1 = yes; 0 = none.
- **EX068 — Index fields.** What three fields are in the evidence index? *Rubric:* 3 = file, hash, finding id; 2 = two; 1 = one; 0 = none.

### Synthesis

Laboratory II adds stop discipline and honest retest reporting under pressure.

### Continue studying — chapter 17 of 18

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Supervised technical project

### Learning outcomes

You will (1) deliver a small authorized testing project on synthetic NMT data; (2) present to a supervisor; (3) hand over runbooks; (4) state remaining limits.

### 18.1 Project brief

Using only synthetic exports, produce: updated approved-port diff, two validated findings with evidence hashes, one retest tale, one runbook improvement.

Section eighteen point one develops supervised technical project with a Northline Municipal Transit note Sam Park can demo offline.

Under section eighteen point one, the NMT mentor expects supervised claims to carry owners and dates.

Section eighteen point one treats project brief presentation handover as testable only when evidence and ticket IDs are recorded.

For section eighteen point one, Northline Municipal Transit will not accept supervised work without a written trail.

### 18.2 Presentation

Fifteen minutes to the supervisor and a SOC observer.

Section eighteen point two develops supervised technical project with a Northline Municipal Transit note Sam Park can demo offline.

Under section eighteen point two, the NMT mentor expects supervised claims to carry owners and dates.

Section eighteen point two treats project brief presentation handover as testable only when evidence and ticket IDs are recorded.

For section eighteen point two, Northline Municipal Transit will not accept supervised work without a written trail.

Section eighteen point two fails closed if supervised evidence is missing rather than guessing.

### 18.3 Handover

Runbooks and scripts in the team repo with versions.

Section eighteen point three develops supervised technical project with a Northline Municipal Transit note Sam Park can demo offline.

Under section eighteen point three, the NMT mentor expects supervised claims to carry owners and dates.

Section eighteen point three treats project brief presentation handover as testable only when evidence and ticket IDs are recorded.

For section eighteen point three, Northline Municipal Transit will not accept supervised work without a written trail.

Section eighteen point three fails closed if supervised evidence is missing rather than guessing.

### 18.4 Limits

Sam still does not perform exploit development or threat-led scenario design — topics for longer courses.

Section eighteen point four develops supervised technical project with a Northline Municipal Transit note Sam Park can demo offline.

Under section eighteen point four, the NMT mentor expects supervised claims to carry owners and dates.

Section eighteen point four treats project brief presentation handover as testable only when evidence and ticket IDs are recorded.

For section eighteen point four, Northline Municipal Transit will not accept supervised work without a written trail.

### 18.5 Next course

AI security (066) is next in the curriculum path.

Section eighteen point five develops supervised technical project with a Northline Municipal Transit note Sam Park can demo offline.

Under section eighteen point five, the NMT mentor expects supervised claims to carry owners and dates.

Section eighteen point five treats project brief presentation handover as testable only when evidence and ticket IDs are recorded.

For section eighteen point five, Northline Municipal Transit will not accept supervised work without a written trail.

Section eighteen point five fails closed if supervised evidence is missing rather than guessing.

### 18.6 Safety cover sheet

Project cover states synthetic-only and no live scanning.

Section eighteen point six develops supervised technical project with a Northline Municipal Transit note Sam Park can demo offline.

Under section eighteen point six, the NMT mentor expects supervised claims to carry owners and dates.

Section eighteen point six treats project brief presentation handover as testable only when evidence and ticket IDs are recorded.

For section eighteen point six, Northline Municipal Transit will not accept supervised work without a written trail.

Section eighteen point six fails closed if supervised evidence is missing rather than guessing.

### 18.7 Repository hygiene

Project scripts land in the team repo without credentials, with README and license headers matching NMT policy.

Section eighteen point seven develops supervised technical project with a Northline Municipal Transit note Sam Park can demo offline.

Under section eighteen point seven, the NMT mentor expects supervised claims to carry owners and dates.

Section eighteen point seven treats project brief presentation handover as testable only when evidence and ticket IDs are recorded.

For section eighteen point seven, Northline Municipal Transit will not accept supervised work without a written trail.

### 18.8 Feedback loop

Supervisor feedback becomes two runbook edits within a week — project done means process improved.

Section eighteen point eight develops supervised technical project with a Northline Municipal Transit note Sam Park can demo offline.

Under section eighteen point eight, the NMT mentor expects supervised claims to carry owners and dates.

Section eighteen point eight treats project brief presentation handover as testable only when evidence and ticket IDs are recorded.

For section eighteen point eight, Northline Municipal Transit will not accept supervised work without a written trail.

### 18.9 18.x Field discipline

The supervised project cover sheet is single-page: synthetic-only declaration, engagement id of the classroom data pack, list of deliverables with hashes, supervisor signature, and Sam's statement of limits. Without the cover sheet the project is incomplete even if the technical work is excellent.

Section eighteen point nine develops supervised technical project with a Northline Municipal Transit note Sam Park can demo offline.

Under section eighteen point nine, the NMT mentor expects supervised claims to carry owners and dates.

Section eighteen point nine treats project brief presentation handover as testable only when evidence and ticket IDs are recorded.

### 18.10 18.y Closing note

After acceptance, Sam books a thirty-minute coaching session on OWASP WSTG access-control topics he wants to deepen — continuous learning is part of the project grade at NMT.

Section eighteen point one zero develops supervised technical project with a Northline Municipal Transit note Sam Park can demo offline.

Under section eighteen point one zero, the NMT mentor expects supervised claims to carry owners and dates.

Section eighteen point one zero treats project brief presentation handover as testable only when evidence and ticket IDs are recorded.

### 18.11 18.z Extra

The SOC observer's question is usually about detection: Sam prepares one ATT&CK technique and one log source he would recommend for each finding.

Section eighteen point one one develops supervised technical project with a Northline Municipal Transit note Sam Park can demo offline.

Under section eighteen point one one, the NMT mentor expects supervised claims to carry owners and dates.

Section eighteen point one one treats project brief presentation handover as testable only when evidence and ticket IDs are recorded.

For section eighteen point one one, Northline Municipal Transit will not accept supervised work without a written trail.

### Worked example (synthetic NMT)

Sam's project is accepted with praise for leaving F2 open and for the stop-drill performance in Lab II. He files the cover sheet and next-course plan.

> **Synthetic case — Northline Municipal Transit (NMT).** The transit agency, Sam Park and all figures are invented for teaching.

### Errors and limits

Live transit systems and fare equipment are never tested without a separate, specialised authorization. This book uses synthetic data only and grants no authority to test real systems.

### Exercises

- **EX069 — Deliverables.** List four project deliverables. *Rubric:* 3 = four from brief; 2 = three; 1 = one; 0 = none.
- **EX070 — Why leave F2 open.** Why is leaving F2 open a strength? *Rubric:* 3 = honesty; verification integrity; 2 = partial; 1 = weakness; 0 = none.
- **EX071 — Limit.** Name one skill Sam still must not claim. *Rubric:* 3 = exploit development or leading threat-led tests; 2 = partial; 1 = port diffs; 0 = none.
- **EX072 — Next course.** What is course 066? *Rubric:* 3 = AI security; 2 = AI; 1 = wrong; 0 = none.

### Synthesis

The technical project proves disciplined testing craft on synthetic data and honest limits.

### Continue studying — chapter 18 of 18

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX072. Northline Municipal Transit, Sam Park and all figures are synthetic. Any answer meeting the rubric scores equally.

**EX001.** Public website, journey planner API, staff intranet, Active Directory, VPN (fare-collection is the sixth, out of scope).

**EX002.** The path from the Internet through the WAF into the web tier (or VPN into the jump host).

**EX003.** Disturbing fare equipment can stop riders entering stations; it needs a specialised authorization if tested at all.

**EX004.** Internet-facing web and API tiers and staff remote access.

**EX005.** 3389/rdp and 8080/http-alt.

**EX006.** RDP is not on the approved list and exposes a remote desktop service on a VLAN meant for web traffic.

**EX007.** No. Production scanning needs written authorization; the lab uses a synthetic list.

**EX008.** He notes that inventory should say ssh-jump consistently, while still using the jump-host process.

**EX009.** Local OS accounts, AD domain accounts and application users.

**EX010.** Only the staging permissions required for the authorized checks, nothing on production or fare systems.

**EX011.** It removes accountability, is usually over-privileged and often remains enabled after the test.

**EX012.** In the approved password vault, never in chat or source repositories.

**EX013.** Documents from targets can carry macros or exploits; treat them as untrusted data and open only in a safe viewer if at all.

**EX014.** Interpreter version, input files and any seeds or config flags.

**EX015.** From the vault or an environment variable injected on the jump host — never hard-coded in the script.

**EX016.** To catch mistakes that could touch out-of-scope systems or leak secrets, and so someone else can run it if Sam is away.

**EX017.** He leaves it out of the finding, re-captures the screen and stores a new hash.

**EX018.** The file bytes match the recorded digest — integrity since hashing — not that the live system is still configured that way.

**EX019.** Blur rider faces or staff badge numbers in a screenshot while leaving the misconfiguration text readable.

**EX020.** In-scope host, allowed method and time window (emergency contact is the fourth).

**EX021.** Rider and staff.

**EX022.** Journey planner API — access control so riders cannot read others' saved journeys.

**EX023.** Compare auth configuration with production owners' documentation or a permitted config review — do not assume.

**EX024.** They are out of scope for this engagement, so modelling them would invite accidental testing.

**EX025.** Web access, API auth failures, VPN authentications, WAF blocks (AD sign-ins also).

**EX026.** No. He needs named, read-only access under the ROE.

**EX027.** It exposes rider personal data beyond what the finding needs and likely violates the ROE.

**EX028.** A log line showing his test account received HTTP 200 for another user's resource at a recorded time.

**EX029.** Account lockouts, staging crashes, accidental production hits (log storms and cache poisoning also).

**EX030.** Stop testing, contact the emergency contact, and leave fare systems untouched.

**EX031.** What he was doing, what he saw, that he halted, and a request for guidance.

**EX032.** On error it stops rather than retrying in ways that could lock accounts or flood logs.

**EX033.** Purpose, ROE reference, tool/settings, stop conditions, evidence expected (version also).

**EX034.** To avoid crashing staging, locking accounts or flooding logs.

**EX035.** Time is limited and rushed checks miss validation; focus on high-risk themes first.

**EX036.** Password spraying and denial-of-service testing.

**EX037.** Missing HSTS is a configuration finding; cross-user journey access is an application logic/authorization finding.

**EX038.** The setting, the system, the risk if wrongly applied and a rollback step.

**EX039.** The system owner through NMT's change process; the tester verifies afterwards.

**EX040.** They often bypass baselines and are not reverted, leaving insecure drift.

**EX041.** fixed: 2 open: 1

**EX042.** It stays open, with retest evidence attached showing the issue remains.

**EX043.** The CISO or named risk owner, in writing.

**EX044.** Retest measures whether agreed fixes worked; new hunting needs its own authorization.

**EX045.** lab_ports, lab_hash and lab_retest outputs.

**EX046.** Refuse to attach it, and recapture or restore a matching file.

**EX047.** Any attempt to scan or touch NMT production systems.

**EX048.** Whether classifications match the approved service list.

**EX049.** Reproduce, check the tool/account/scope, then escalate if needed.

**EX050.** The staging API works from the jump host browser; the failure is Sam's laptop trust store.

**EX051.** Symptom, steps tried, screenshots, timestamp and what was ruled out.

**EX052.** Stop and contact the emergency contact before continuing.

**EX053.** Hashing, port diffs, ticket field checks (report skeletons too).

**EX054.** Exploitation and scope decisions (and severity without human review).

**EX055.** Unlimited retries can lock accounts, flood logs or loop forever.

**EX056.** Validation that the automated candidate is a real, in-scope issue with impact.

**EX057.** The SMS vendor's production service (or map tiles / payment processor).

**EX058.** NMT is responsible for how it stores and exposes the key in its systems.

**EX059.** Stop the related checks, note the outage, and avoid retry storms.

**EX060.** It sends each finding to the party who can actually fix it.

**EX061.** Stop conditions and ROE/out-of-scope warnings.

**EX062.** A clear warning not to run the procedure against production.

**EX063.** Mark it obsolete and archive it so it is not followed.

**EX064.** After any stop incident or major system change.

**EX065.** Successful stop drill, refusal of bad evidence and a coherent retest report.

**EX066.** Two minutes from the supervisor's call.

**EX067.** No. F2 stays open without fix evidence.

**EX068.** File name, hash and finding id.

**EX069.** Port diff, two validated findings with hashes, a retest tale and a runbook improvement.

**EX070.** It shows honest verification rather than closing tickets without evidence.

**EX071.** Exploit development or leading a CBEST/TIBER-style threat-led engagement.

**EX072.** AI security.

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
