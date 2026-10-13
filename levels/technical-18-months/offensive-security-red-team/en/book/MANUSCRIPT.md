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

Sam Park's ordinary authorized work at Northline Municipal Transit covers the public website, the journey planner API, the staff intranet, Active Directory and the VPN. The fare-collection network is drawn on every diagram in red and stays out of ENG-512 unless a specialised ROE is signed. Confusing those services with fare gates is how operators ask for probes they must not run.

### 1.2 Tiers

Internet-facing web and API tiers sit behind a load balancer; application servers talk to databases; staff identity sits in AD. Trust boundaries are the places where packets or credentials cross from less trusted to more trusted zones.

At NMT the load balancer fronts both the public website and the journey planner API, so one WAF rule set covers both. The AD boundary matters because a phished staff password crosses from the VPN into the staff zone. Sam's ENG-512 checks start outside the WAF and stop before the fare network, because crossing that line without specialised auth is out of scope.

### 1.3 Where testing starts

Authorized technical tests usually start at internet-facing web and API tiers and at staff remote access, because that is what strangers and phished staff reach first.

Strangers reach the website and journey planner API, while phished staff credentials reach the VPN, which is why those three come first. Fare validators and radio gear are not starting points for ordinary windows; Sam's kickoff checklist names web, API and VPN before any tool runs. Sam's ENG-512 kickoff sheet therefore lists website, journey planner API and staff VPN in that order, with fare validators listed under do-not-touch. Starting elsewhere is a scope error even if a tool makes it easy.

### 1.4 Fragile dependencies

Fare gates and radio systems can harm operations if disturbed. They stay excluded unless a specialised engagement says otherwise.

A stuck validator at a busy station during the morning peak would turn a test into a rider-facing incident. Sam's kickoff sheet lists fare validators and radio under do-not-touch, beside the name of the operations contact. Sam's ROE for ENG-512 repeats the exclusion in the same sentence as the Saturday window so nobody treats fare as an interesting side path. Specialised fare work would need separate funding, a different ROE and operators trained on validators; ordinary Saturday windows never inherit those rights. Sam repeats that boundary when managers ask for just a quick look.

### 1.5 Architecture diagram discipline

Sam keeps a dated diagram with owners on each box. Testing against an outdated diagram causes scope errors.

The diagram's date sits in its title block, next to the network owner's initials from the last confirmation. Testing against an outdated diagram causes scope errors such as probing a retired staging host that now shares a name with production. Before ENG-512 he asks the network owner to confirm the diagram date in writing. He files the network owner's confirmation under the ENG-512 ticket before lab_ports runs. A diagram without that confirmation is treated as untrusted even if it looks familiar.

### 1.6 Change windows

Architecture changes (new API gateway, AD upgrade) trigger a review of the ROE before the next test.

The trigger list sits at the top of the ROE, so the network owner knows which changes require a fresh signature. Sam will not reuse last quarter's ENG window if the journey planner moved behind a new WAF rule set without a signed update. After an AD upgrade Sam re-checks tst-sam-web group membership and MFA before the next window. Reusing last quarter's ROE without that check is how stale rights survive.

### 1.7 Owner contacts on the diagram

Every box on Sam's diagram names a person, not only a team. When a finding appears on the journey planner API, he knows whom to call without hunting through a directory.

The journey planner API box, for example, carries the API owner's name and an out-of-hours number. That saves minutes during a stop, when the SOC needs a decision from the owner rather than a directory search. Owner contacts are copied into the ENG-512 kickoff note so the SOC can reach the same people. Diagram contacts are copied into the SOC start message so overnight responders reach the API owner without calling Sam's personal phone. A team-only label is not enough.

### 1.8 Why diagrams go stale

A contractor adds a staging CDN and nobody redraws the picture. Sam's first task each engagement is to confirm the diagram with the network owner in writing.

Contractor changes reach the diagram only when someone files the redraw, so Sam asks the contractor lead what changed since the last engagement. Sam's first task each engagement is to confirm the diagram with the network owner in writing; a stale box is how an approved listener list becomes wrong before lab_ports even runs. When a staging CDN appears without a redraw, Sam opens a model-update ticket before any new listener is trusted. Stale pictures are the root cause of many NOT APPROVED surprises.

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

lab_ports on the synthetic inventory prints 80/http ok, 443/https ok, 22/ssh ok, then 3389/rdp and 8080/http-alt as NOT APPROVED - report. Sam's approved listeners for ENG-512 are only the ones on the signed list; anything else becomes a finding, not a bonus scan target. The verified lab_ports block is pasted into the notebook: 80, 443 and 22 ok; 3389/rdp and 8080/http-alt NOT APPROVED - report. Those two lines become tickets the same day.

### 2.2 Protocol basics

HTTP/HTTPS carry the website and API; SSH reaches jump hosts; RDP on a web VLAN is unexpected. Testers describe what they see without sending exploit traffic.

HTTP and HTTPS on the journey planner, SSH to jump hosts, and RDP that is not approved are the protocol basics Sam names in the method notes. He does not invent exotic protocol checks outside the ROE; protocol identity still needs the port map from lab_ports. Sam's method notes say HTTPS for journey planner checks and SSH only to named jump hosts. Protocol curiosity beyond that list waits for a ROE change.

### 2.3 No freestyle scanning

Even listing ports on production needs authorization. This lab only classifies a synthetic list offline.

No freestyle scanning means Sam does not add ports because a tool suggested them. If 3389 or 8080 appear as NOT APPROVED, he reports them and stops; freestyle expansion of ENG-512 is how fare-adjacent hosts get touched by accident. Kickoff includes reading the no freestyle scanning line aloud. Suggested ports from tools go to a parking lot issue, never into the live inventory mid-window.

Sam pastes the lab_ports block showing 80/443/22 ok and 3389 plus 8080 not approved into the notebook the same hour so network can act before folklore spreads.

### 2.4 Name mismatches

Port 22 labelled only "ssh" still matches the approved ssh-jump family in the lab, but Sam notes the inventory name for cleanup.

Name mismatches — a DNS label that points at a different IP than the ROE host list — are pause conditions. Sam asks the network owner before continuing; guessing that api-staging is safe because the name says staging has already caused scope errors at NMT. A DNS mismatch pause records the queried name, the answer, the ROE address and the owner's reply. Resuming without that written reply fails peer review.

### 2.5 Egress paths

Staff laptops that can reach staging and the Internet may bridge environments; the ROE states which source networks are allowed.

Egress paths from staging jump hosts are listed so Sam knows which outbound destinations his checks may hit. An unexpected egress to a fare-vendor cloud is a stop, not a discovery to chase mid-window. If staging jump hosts suddenly reach a fare-vendor prefix, Sam stops and asks network to classify the path. Chasing that path as discovery is out of scope.

Network closes or authorizes 3389/rdp before the next Saturday rather than leaving the listener as chat folklore that examiners never see.

### 2.6 Logging

Network teams may mirror authorized test sources; Sam coordinates so his traffic is attributable.

Logging of ENG-512 start, stop and pauses goes to the engagement channel with ticket id. The SOC uses those log lines when rider apps slow; silence leaves them guessing whether Sam's checks are involved. ENG-512 start and stop lines always include the ticket id and clock time so the SOC can filter noise. The 10:12 loop drill text is reused when live stops happen.

8080/http-alt becomes a ticket with the network owner named before ENG-512 ends for the week and the SOC clears the watch list.

### 2.7 TCP versus application identity

A port being open is not the same as a service being safe. Sam records both the port and the application banner or certificate name when inventory allows.

TCP open on 443 does not prove the journey planner API is healthy; application identity still needs a method card. Sam records both the port result from lab_ports and the application check so findings are not port-only theatre. After ports classify clean, Sam runs the application method card on the journey planner and records both results. A green TCP port alone never becomes a clean bill of health.

### 2.8 Reporting unapproved listeners

Unapproved does not mean "exploit now". It means open a ticket, attach the synthetic observation, and wait for the owner to confirm whether the service should exist.

Reporting unapproved listeners means 3389/rdp and 8080/http-alt leave ENG-512 as findings with owners, not as quiet notes. Sam files them the same day so the network team can close or authorize them before the next window. Network owners receive the NOT APPROVED listener lines verbatim from lab_ports. Closure is disable or deliberate future authorization — not a quiet ignore.

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

Identity layers at NMT include rider-facing accounts, staff AD accounts, VPN certificates and service accounts for the journey planner. Sam's test identity tst-sam-web sits only on the staff/staging layer; it never receives fare-network rights. tst-sam-web is barred from fare-network AD groups by construction. Sam verifies group membership at kickoff so identity layers stay separated under pressure.

Name-mismatch pauses attach DNS answers and ROE addresses before any resume is allowed on staging hosts that looked safe by name alone.

### 3.2 Test accounts

Authorized tests use named test accounts with the least privilege needed, issued for the window and revoked after. Shared pentest god accounts are themselves a finding.

Test account tst-sam-web has read access to staging only, is vaulted for ENG-512, and auto-expires Sunday night. Sam will not share that password in chat; vault checkout is the only path, and expiry is checked before Monday work. Sunday auto-expiry is tested by attempting a Monday login in the lab; success would be a finding. Vault checkout logs are kept with the ENG-512 pack.

### 3.3 Service accounts

API and automation accounts often have broad rights and weak monitoring. They are high-value review targets when in scope.

Service accounts for the API are out of Sam's ordinary test set unless the ROE names them. Using a shared service password because it was pasted in an old ticket breaks credential handling rules and muddies ATT&CK T1078 notes for the SOC. Service account passwords found in wikis are rotated through identity, not borrowed for testing. Sam files the exposure and uses only vaulted test identities.

### 3.4 Credential handling

Test passwords live in the vault, not in chat or scripts committed to git.

Credentials for ENG-512 live in the vault, not in scripts or screenshots. Sam redacts tokens from evidence before hashing; a token in a PNG fails the two-person evidence rule even if the finding is real. Evidence PNGs are cropped on the jump host before lab_hash runs. Hashing a secret-bearing image and deleting later still leaves the secret in backup history.

Unexpected egress toward a fare-vendor prefix stops the window until network classifies the path in writing and posts the classification.

### 3.5 Admin workstations

Jump hosts should be the only path to admin tasks; tests that find direct admin RDP from email VLANs matter.

Admin workstations used for testing are NMT-issued jump hosts. Personal laptops are not evidence stores; Sam copies nothing from the jump host to a phone or home drive during ENG-512. NMT jump policy blocks personal cloud sync clients. Sam's cleanup checklist includes confirming no ENG files remain in Downloads.

Start and stop lines always carry ENG-512 and a clock so the SOC can filter testing noise away from rider-facing incidents.

### 3.6 ATT&CK link

Abuse of legitimate accounts maps to T1078 Valid Accounts — useful when writing detection recommendations.

ATT&CK link for stolen or reused staff credentials is T1078 Valid Accounts. Sam adds that label when a finding is about auth abuse paths so the SOC can search with a shared name; the label does not prove an external attacker. When auth findings ship, the SOC ticket subject includes T1078 and the time window. Rider identifiers are never pasted into that subject line.

Application method cards run only after ports classify because green TCP alone is an incomplete story for the journey planner API.

### 3.7 Revocation day

On Sunday night Sam verifies tst-sam-web is disabled. Leftover test accounts are among the most common findings he writes about other teams — he will not become one.

Revocation day is Sunday night when tst-sam-web expires. If ENG-512 overruns into Monday, Sam requests a fresh time-boxed account rather than asking someone to extend the old one quietly. If Monday jobs still authenticate as tst-sam-web, Sam opens a severity ticket before any other work. Revocation day is a control, not a suggestion.

Unapproved listener tickets quote lab_ports lines verbatim so closure means disable or deliberate future authorization with a signed ROE update.

### 3.8 MFA on test accounts

Where NMT enforces MFA, test accounts get MFA too. Skipping MFA "because it is staging" trains bad habits and weakens staging as a proving ground.

MFA on test accounts is required the same as on staff VPN. A test account without MFA is itself a finding; Sam will not argue for an MFA exception to make scripting easier. Live MFA challenge at kickoff is mandatory. A test account with MFA enrolled but SMS undeliverable stops ENG-512 until identity repairs it.

tst-sam-web is checked for zero fare-network AD groups at every kickoff before vault checkout proceeds for the Saturday window.

### 3.9 3.x Field discipline

When Sam receives a new test account he walks a four-step checklist: confirm the account is named to him, confirm its groups match the ROE, store the secret in the vault under the engagement id, and set a calendar reminder for revocation day. Skipping any step has bitten NMT before — a shared account left in Domain Admins after a contractor left. He treats account hygiene as part of testing craft, not as paperwork for someone else.

Field discipline for identity means vaulted test accounts, Sunday expiry, MFA on, and no fare-network groups on tst-sam-web. Sam's kickoff reads those four lines aloud so peers catch drift before the window opens. Identity field discipline is checked with a four-question peer quiz: vaulted, expiry, MFA, no fare groups. Wrong answers delay the window.

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

Scripts exist so Sam can repeat lab_ports-style checks and hash evidence the same way every Saturday. They do not exist to invent new attack paths; every script for ENG-512 maps to a method card on the signed list. Script headers cite method card ids so automation cannot drift from the signed list. Orphan scripts without cites are deleted from the Saturday job folder.

Sunday expiry is proven by a failed Monday login attempt filed in the lab pack as evidence the control worked.

### 4.2 Untrusted data

Files from targets are data, not code. Do not run unknown binaries or macros from a test target on an admin workstation.

Untrusted data includes API JSON from staging and any file a tool writes. Sam validates shapes before parsing; a surprise field that looks like a fare transaction id is redacted and escalated, not logged in full. Schema validation drops unknown JSON keys before logging. Payment-shaped fields from staging responses are treated as sensitive even in non-prod.

Service passwords found in wikis are rotated through identity and never borrowed for ENG-512 test traffic on staging.

### 4.3 Reproducibility

Pin Python versions, seed any randomness and keep input files beside the script in the evidence pack.

Reproducibility means another technician can run the same script on the same inventory and get the same ok / NOT APPROVED lines. Sam pins script versions in the notebook beside the ENG-512 ticket id. Peers reproduce using the notebook's script hash; mismatched hashes abort comparison. Reproducibility fights are version fights until pins match.

PNGs are cropped on the jump host before lab_hash so secret bytes never enter vault backup history that outlives the engagement.

### 4.4 Formats

JSON and CSV are common for tool exports. Sam validates schema before trusting fields for a finding.

Formats for inventories and evidence indexes are CSV or plain text agreed in the runbook. Binary dumps and undocumented JSON blobs fail peer check because the next operator cannot read them under time pressure. Inventory CSV columns are name, ip, port, proto, approved. Reordering breaks lab_ports; Sam validates the header row before the job runs.

Cleanup confirms the jump-host Downloads folder holds no ENG files after the window and before portfolio credit.

### 4.5 Secrets in scripts

No hard-coded passwords. Read from the vault or environment injected by the jump host.

Secrets in scripts are forbidden. Vault references or environment injection at run time are the only patterns Sam accepts in code review for ENG-512 automation. Pre-merge secret scanning on the automation repo fails the build on tokens. Sam rotates any token that ever landed in a pull request diff.

SOC subjects for auth findings include T1078 and the time window while omitting rider identifiers entirely from the ticket text. Pass bar ignores charm without plant, stop, hashes and peer pass artefacts present in the pack.

### 4.6 Code review

Another technician reads Sam's script before it runs in an engagement window.

Code review catches freestyle port lists and hardcoded passwords before a window. A peer score below pass means the script stays out of Saturday's job list. Reviewers grep for host patterns that look like fare subnets and reject those loops. Code review is a scope control, not only a style club.

Monday jobs that still authenticate as tst-sam-web open a severity ticket before any other work starts that day. Lab II stress stays synthetic; real fare gear is never a prop for any cohort exercise.

### 4.7 Input size limits

Scripts that read tool exports cap file size so a huge dump cannot exhaust the jump host. Caps are safety features, not pessimism.

Input size limits stop a runaway inventory from locking the jump host. Sam caps rows processed per run and fails closed with a non-zero exit when the cap trips. Row caps print ERROR: inventory exceeds cap and exit 2. Truncation without error would hide 8080/http-alt past the cut line.

Live MFA challenge failure stops ENG-512 until identity repairs SMS or app delivery for the test account in use.

### 4.8 Exit codes

Sam's scripts exit non-zero on MISMATCH or NOT APPROVED so CI and humans notice failures instead of skimming green-looking logs.

Exit codes distinguish ok listeners from NOT APPROVED findings so CI and humans agree. lab_ports-style jobs that always exit zero hide 3389/rdp until someone reads stdout carefully. SOC monitors non-zero exits from ENG job users. Scripts that exit 0 while printing NOT APPROVED are bugs fixed before the next Saturday.

Identity peer quiz covers vaulted status, expiry, MFA and no fare groups before tools are permitted to start on Saturday.

### 4.9 4.x Field discipline

Sam's scripting standard is short enough to remember: one purpose per script, argparse or explicit constants at the top, no network calls unless the ROE file path is passed in, and a --dry-run mode that prints what would happen. Dry-run saved him when a path typo would have pointed a hash job at a production share listing. Reviewers look for dry-run and for the absence of hard-coded hosts more than for clever code.

Field discipline for scripting means pinned versions, no secrets in files, size caps, and exit codes that match the report. Sam's ENG-512 notebook links each script hash to the method card it implements. Scripting field discipline is pinned hashes, secret-free trees, caps and honest exits. Sam links each job to a method card in the notebook index.

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

Technician ROE for ENG-512 states staging web/API and VPN checks, Saturday window, emergency contact, and fare network excluded. Sam will not start if emergency_contact is empty; the checklist is the same habit taught in professional labs. Empty emergency_contact on the technician ROE cancels ENG-512 before tools start. Sam posts the cancel with the missing field named so the SOC does not expect traffic.

Script headers without method-card ids are deleted from the Saturday job folder during code review the week before.

### 5.2 Hashing

Hashing evidence detects accidental edits. A mismatch means do not attach the file until the lineage is clear.

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

lab_hash prints shot1.png b81db4df801a MISMATCH and config.txt 44c91857f34b MATCH. Sam treats MISMATCH as a stop on that artefact until the file is re-exported or the expected hash is updated with two-person approval. lab_hash MISMATCH on shot1.png blocks that artefact until two people agree on a re-export or an updated expected hash. MATCH on config.txt is the pattern tickets should show after fixes.

### 5.3 Minimisation

Blur rider faces and badge numbers in screenshots; keep the pixels that prove the issue.

Minimisation means screenshots without rider names or card numbers. Evidence that proves a cookie flag or open port does not need a real journey history; Sam crops before hashing. Rider names and card numbers never appear in ENG-512 screenshots. Sam proves cookie or port issues with synthetic sessions and cropped UI chrome only.

Unknown JSON keys that look payment-shaped are stripped before any log write leaves the jump host toward the vault. Three after-action improvements file before Lab II sign-off or the lab stays incomplete on the roster.

### 5.4 Evidence index

Each file has an id, hash, time, collector and related finding id.

The evidence index lists filename, sha256 prefix, ticket id and owner. An artefact not on the index is not in ENG-512; personal chat links do not count. Index rows carry filename, twelve-hex hash prefix, ENG-512 id and owner. Artefacts missing from the index are deleted as unverified copies.

Peer reproduction aborts when notebook script hashes disagree so version fights do not masquerade as finding fights in retest. Failed stop drill blocks project start until the halt is rehearsed clean with a passing peer score.

### 5.5 Integrity vs truth

A matching hash proves the file is unchanged since hashing, not that the underlying system finding is still true.

Integrity versus truth: a MATCH hash proves the file is unchanged, not that the finding is correct. Sam still validates impact with a method card before the report ships. A MATCH hash on a wrong screenshot still fails truth checks. Sam validates the finding path with the method card before calling evidence complete.

Inventory CSV must open with name,ip,port,proto,approved or lab_ports refuses to run against the malformed file. Lab II stop text becomes the live ENG-512 halt template copied into the runbook for real windows.

### 5.6 Retention

Follow NMT's engagement retention schedule; delete local caches after vaulting.

Retention follows the ROE delete-within rule. Sam diaries deletion for ENG-512 evidence and confirms it; leftover PNGs on the jump host fail cleanup. Deletion diary entries for ENG-512 include date, path and witness. Leftover PNGs on the jump host fail the cleanup gate for portfolio credit.

CI secret scanning failure rotates the exposed token before anyone reconsidering the merge presses approve on the pull request. Project packs include diagram, ROE checklist, lab_ports, hashes, FIXED/STILL OPEN and stop record on synthetic NMT only.

### 5.7 Photographing screens

When a screenshot is required, Sam uses the jump host's tools, names the file with finding id and time, and hashes it before editing anything for redaction on a copy.

Photographing screens with a phone is refused when the jump host can capture a redacted PNG. Phones leave NMT control; vaulted screenshots stay in the engagement path. Phone photos of screens are rejected in peer review. Jump-host capture with redaction is the only accepted screenshot path.

Reviewers reject automation loops whose host patterns resemble fare subnets even when the author meant only staging ranges.

### 5.8 Two-person evidence rule

For high-impact findings, a second technician confirms the hash and the observation. Disagreement pauses filing.

Two-person evidence rule means a peer watches hash generation for high-impact items. MISMATCH on shot1.png is reviewed by both before anyone updates the expected hash. High-impact MISMATCH events require a peer at the keyboard during re-hash. Solo hash updates on shot1.png are refused.

Row-cap trips print a clear error and exit code 2 rather than truncate the inventory quietly and hide listeners. Supervisor presentations lead with exclusions and open items before any evidence theatre or tool praise.

### 5.9 5.x Field discipline

Evidence disputes are expensive. Sam therefore hashes immediately after capture, writes the hash into the activity log line, and only then redacts a copy for the report appendix. If legal later asks whether a screenshot was altered, he can show the original digest and the redacted derivative. The MISMATCH result in the lab is the classroom version of that discipline — edited bytes must never silently replace originals.

Field discipline for evidence is hash, minimise, index, retain, and two-person on mismatches. Sam's ENG-512 pack fails peer check if any of those five is missing. In the lab, MISMATCH on an edited file is the cue to call a second person, not to re-hash until it matches. Missing any one fails the ENG-512 pack.

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

Model elements for NMT are rider → HTTPS → API → trip DB; staff → VPN → admin UI; map tiles as external; fare cloud crossed out. Sam's one-page model is the scope picture before tools run. Sam's one-page model crosses out fare cloud and map-tile vendor boxes with owners named on web, API and VPN only. Tools stay closed until that page is current.

Scripts that exit zero while printing NOT APPROVED are fixed before the next Saturday job list is published to operators.

### 6.2 Entry points

Each entry point gets a short list of WSTG themes: auth, session, access control, input handling.

Entry points are the public website, journey planner API and staff VPN. Fare validators are not entry points for ENG-512; listing them as interesting is a model error. Entry-point lists that include fare validators are corrected before kickoff. Each of the three gets its own WSTG theme list, so VPN checks never borrow web input-handling tests.

For the staff VPN the themes stop at authentication and session handling, because input handling belongs to the website and journey planner API. Keeping the lists separate also makes the coverage statement precise: the report can say which themes were exercised on which entry point and which were left out.

### 6.3 Assumptions

Staging mirrors production auth is an assumption to validate, not a fact.

Assumptions such as staging equals production config are written in the assumption log with an owner. Unwritten assumptions become scope fights mid-window. Each assumption log line names who believed it and the date last checked. Staging-mirrors-prod without a check date is marked invalid.

Empty emergency_contact posts a cancel naming the missing field so the SOC does not expect ENG traffic that morning. Limits pages state fare out of scope, synthetic only and no real-system authority in plain examiner-facing words.

### 6.4 Data flows

Note where personal data (saved journeys) flows so tests minimise exposure.

Data flows show trip queries and staff admin actions; they do not show fare settlement. Sam refuses to draw fare flows into the ordinary model because drawing invites probing. Data-flow arrows stop at trip DB and staff admin UI. Drawing fare settlement into the ordinary model is a documentation defect Sam fixes before ENG-512.

lab_hash MISMATCH on shot1.png needs two-person approval before anyone updates expected hashes in the evidence pack. Technologist course is next; this book ends at procedural ROE competence for technicians doing ENG-512 work.

### 6.5 Out of model

Fare validators are omitted because they are out of scope.

Out of model means fare network, radio and card processors. Those boxes stay black on the colour map; ENG-512 findings never claim coverage there. Black boxes for fare, radio and card processors carry the caption specialised ROE only. Ordinary findings never claim coverage there.

MATCH on config.txt is the pattern after-fix tickets should show when cookie or sshd baselines finally land. Safety cover is repo page one with staging first, fare black, stops and retention rules before any code. Repos ban secrets and real inventories; README shows disable and stop instructions before a clone is used.

### 6.6 Living model

Update the model when the API gains a new payment callback — even if payment is third-party.

Living model updates when a CDN or gateway changes. Sam dates each revision beside the ROE; a model older than the last architecture change is invalid for the next window. Model revision dates sit beside the ROE hash. If architecture changed after the model date, Sam updates the picture before the window.

Rider names never appear in ENG-512 screenshots because synthetic sessions prove cookie and port issues without PII. Supervisor feedback becomes runbook patches the same week rather than unread archives collecting dust.

### 6.7 Trust zone colours

Sam colours Internet red, staging amber, staff green and fare black (do not enter). Colour makes scope visible in reviews.

Black is reserved for fare so it cannot be confused with any zone where testing is allowed. Colour makes scope visible in reviews when managers skim too fast to read exclusions. Colour maps are printed for the kickoff huddle: red Internet, amber staging, green staff, black fare. Managers who only skim text still see the exclusion.

Evidence index rows carry filename, hash prefix, ticket id and owner or the unlisted file is deleted as unverified copy.

### 6.8 Assumption log

A running list of assumptions sits under the model. Each is marked confirmed, rejected or open before the report is issued.

Assumption log entries name who believed staging mirrored prod and when that was checked. Failed assumptions become findings or ROE updates, not silent footnotes. Failed assumptions become either ROE text or findings. Sam will not leave a broken staging-mirrors-prod belief as an unspoken footnote.

MATCH integrity still needs method-card truth checks before findings are allowed into the report body for the CISO. Project field discipline is brief, limits, safety cover, clean repo and honest STILL OPEN scored together.

### 6.9 6.x Field discipline

Building the system model with the product owner takes an hour and prevents days of confusion. Sam projects a blank diagram, asks the owner to place boxes, and only then adds his own arrows. Owners correct mistaken assumptions about which database holds saved journeys and whether the admin UI shares authentication with the rider API. Those corrections change which WSTG themes matter most.

Field discipline for modelling is dated diagram, coloured zones, assumption log, and fare black. Sam will not open ENG-512 tools until those four are current. The assumption log records each owner correction, such as which database holds saved journeys, with the date it was confirmed. Any gap delays tool start.

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

Useful logs for ENG-512 are WAF allow/deny, API auth failures, VPN session starts and jump-host commands. Full production dumps are refused; Sam asks for time-bounded samples around his window only. Sam requests WAF and API auth samples only for the ENG-512 clock window. Useful logs are those slices, not multi-day dumps.

Retention diaries list date, path and witness for ENG-512 deletions on the diary day required by the signed ROE. Portfolio credit needs artefacts proving solo ENG-512 habits rather than intention statements without files.

### 7.2 Access path

Sam requests read-only log access for the window via the ROE, not by sharing someone else's SIEM password.

Access path to logs is read-only through the SOC ticket, not a personal admin role on prod. Sam's tst-sam-web account never becomes a log-admin shortcut. Read-only SOC ticket access is enough; elevating tst-sam-web to prod log admin is refused. Access path discipline protects blast radius.

Phone photos of screens fail peer review because jump-host capture with redaction is the only accepted screenshot path. Appendices paste lab_ports and lab_hash outputs so examiners reproduce MATCH/MISMATCH without asking Sam questions.

### 7.3 No production dumps

Exporting whole member tables for analysis is out of bounds. Use synthetic or minimised samples.

No production dumps means no full table export of trip history to prove a finding. A redacted sample that shows the class of issue is enough for staging-focused ENG-512 work. Production trip-table dumps are never a teaching aid. Redacted staging samples that show the issue class are the maximum Sam will attach.

High-impact re-hashes require a peer standing at the keyboard while the new digest is generated and spoken aloud. Diagram confirmation emails file under the ticket before lab_ports is allowed to run against inventory.

### 7.4 Confirming findings

An access-control finding is stronger when logs show the unauthorized request succeeded.

Confirming findings with logs means matching timestamps after clock sync. A 401 loop at 10:12 in the synthetic drill is confirmed when API logs show the same minute. Confirming the 10:12 loop means API logs and jump-host clock agree within two minutes. Without that, the stop message time is not evidence-grade.

Evidence field discipline scores hash, minimise, index, retain and two-person mismatch handling as one pass-fail gate. Specialised fare engagements need separate funding and ROE rather than borrowed Saturday rights from ordinary ENG-512.

### 7.5 Clock sync

Note time zones and NTP status when correlating logs with activity notes.

Clock sync between Sam's jump host and the API hosts is checked at kickoff. Skew larger than two minutes is fixed before evidence timestamps are trusted. Kickoff includes an NTP check on the jump host against the API VIP. Skew above two minutes is fixed before hashes and log compares.

One-page models cross out fare cloud and map-tile vendors before any scanner process is started on Saturday. Written network-owner confirmation beats familiar-looking diagrams that may hide a new CDN edge.

### 7.6 Detection feedback

Share technique names with the SOC so they can build detections after the test.

Detection feedback to the SOC includes which method cards ran and when they stopped. Silence after ENG-512 start is a coordination failure, not a stealth goal. Detection feedback lists method cards run and the stop time. The SOC should never learn ENG-512 ended only from silence.

Entry lists that mention validators are corrected at kickoff so ENG-512 cannot claim those surfaces by accident. AD upgrades re-check tst-sam-web groups and MFA before anyone reuses old ROE text from last quarter.

### 7.7 Sample not full export

When a log query returns thousands of lines, Sam exports a time-bounded sample around his test activity, not the whole day, unless the ROE asks for more.

Sample not full export: Sam requests five minutes of API auth logs around a finding, not a day's dump. Smaller samples protect riders and still confirm the issue. Five-minute auth-log samples around a finding beat day-long exports for rider privacy and for Sam's review time.

Assumption log lines without check dates are marked invalid until someone re-validates staging versus production beliefs. Owner contacts copy into SOC start messages so overnight responders need not call Sam's personal phone number.

### 7.8 PII in logs

If logs contain rider phone numbers, he stores them in the restricted vault path and mentions PII presence in the evidence index.

PII in logs — names, card numbers, precise GPS — is redacted before screenshots enter the vault. A log line with a rider email fails minimisation even if the finding is about auth. Log redaction removes emails, card PANs and precise GPS before vault entry. PII left in a teaching screenshot fails minimisation.

Data-flow arrows stop before fare settlement by design so a pretty drawing cannot invite unauthorized probing. Staging CDN additions open model-update tickets before new listeners are trusted inside the inventory file.

### 7.9 7.x Field discipline

Sam books SIEM access in the same ticket as the ROE, with an end date. When the engagement ends, he confirms his access is removed — leftover read access is itself a finding he would write about anyone else. During the window he saves queries, not raw dumps, so another technician can replay the investigation without holding excess rider data.

Field discipline for telemetry is sample, redact, sync clocks, and tell the SOC. Sam's ENG-512 stop message after the 401 loop named the time and the system so detection could correlate.

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

Harm modes include API lockout, VPN saturation, and any touch of fare validators. Sam's method cards list which harm each check could cause so stop conditions are not invented under stress. Harm-mode lists on each method card include API lockout and VPN saturation. Cards without harm modes are incomplete for ENG-512.

Black boxes read specialised ROE only and stay out of ordinary coverage claims in any board or exam language. Kickoff sheets list website, API and VPN with validators under do-not-touch in the same one-page view.

### 8.2 Stop conditions

Owner asks stop; unexplained outage; fare system alerts anywhere; personal data exposed in a ticket; tool loops.

Each condition has a one-line stop message prepared on the ROE card, so Sam posts it without composing under stress. Any one is enough; Sam does not finish one more objective first. Fare system alerts anywhere — even unrelated — stop ENG-512 until operations clears the line. Sam does not argue correlation in the moment.

Personal data turning up in a ticket is a stop even though nothing is broken, because the ticket system may be read by people the agreement never covered. A tool caught in a loop is a stop for a different reason: it can push traffic past the agreed rate before anyone notices.

### 8.3 Safe tool failure

Prefer tools that fail closed (stop on error) rather than retrying into a storm.

Safe tool failure means scripts exit and release hosts when errors repeat. The 401 loop drill teaches failing closed rather than retrying forever against staging. Safe failure exits release sockets and print a halt reason. Retry storms are treated as tool defects, not thoroughness.

Colour maps print red amber green black for managers who only skim exclusion paragraphs in the ROE appendix.

When auth checks loop, Sam's script exits, drops sockets and prints a halt reason instead of retrying into a storm against staging.

### 8.4 Communicating stop

Say what you were doing, what you observed, what you halted, and ask for guidance — short and factual.

Communicating stop uses the engagement channel: ENG-512 stop — looping auth checks on staging API — halted 10:12 — need guidance. Factual headers beat apologies in the moment. Stop messages follow ENG-512 stop — cause — halted HH:MM — need guidance. Softener words are deleted before send.

Broken staging-mirrors-prod beliefs become ROE text or findings rather than unspoken footnotes that surprise retests.

His channel post mirrors the drill: ENG-512 stop, looping auth on staging API, halted 10:12, need guidance — no apologies in the first line.

### 8.5 Rehearsal

Once per quarter Sam rehearses a stop message on the engagement channel with the SOC.

Rehearsal of the stop message happens in Lab II before a real window. Sam practises posting the 10:12 pattern so the first live stop is not the first time he writes one. Lab II grades the rehearsal stop post before any live window. An unrehearsed first stop is a programme failure waiting to happen.

Modelling field discipline delays tool start when dated diagram, colours, assumption log or fare black marking is stale.

### 8.6 No blame in the moment

Stop first; investigate cause after systems are stable.

No blame in the moment: stop first, analyse later. The after-action can discuss the loop; the channel message during ENG-512 only states halt and need guidance. After-action owns the learning; the live channel owns only halt facts. Blame language in the stop thread is moderated out.

Log requests cover only ENG-512 clock-window slices rather than multi-day production dumps that expose riders.

During the halt he forbids blame talk; the after-action later owns learning while the live thread stays factual.

### 8.7 Secondary contact

If the primary emergency contact does not answer in five minutes, Sam calls the secondary named in the ROE. Waiting silently is not a plan.

The five-minute mark is timed from the first unanswered call, and both call times go into the activity log. Sam's ROE lists both; calling only the primary is not a complete stop path. Secondary contact answers when primary misses the five-minute mark. Sam dials both numbers from the ROE card, not from memory.

tst-sam-web never becomes a production log-admin shortcut even when the SOC is slow to reply to the ticket.

### 8.8 Tool kill switch

Every long-running script Sam starts has a known way to kill it (process group, container stop). He tests the kill switch once before the window.

Tool kill switch is the script's disable flag and the jump-host kill command practised in rehearsal. Sam can stop his own jobs without waiting for a vendor support line. Kill-switch rehearsal is a Lab II checkbox. An untested disable flag keeps automation off the Saturday list.

Production trip dumps are refused; redacted staging samples that show the issue class are the maximum attachable proof.

### 8.9 8.x Field discipline

After any real stop, Sam files a short blameless note: trigger, time to halt, who was called, whether riders were affected, and one process change. NMT reviews stop notes quarterly. Teams that hide stops eventually cause larger outages; teams that record them get better kill switches and clearer ROEs. The looping-auth drill exists so the first stop is not also the first time Sam writes that note.

Field discipline for failure modes is written stop conditions, rehearsed messages, secondary contact, and kill switch. ENG-512 does not rely on heroics when a loop starts. Failure-mode field discipline is stops written, messages rehearsed, secondary named, kill switch tested. Heroics are out of scope.

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

Method cards name the check, the rate limit, the harm mode and the evidence expected. Cards without those four fields stay out of Sam's Saturday stack for ENG-512. Method cards missing rate, harm, evidence or check name are rejected from the stack. Four fields are the minimum for ENG-512.

Ten-twelve loop confirmation needs API logs and jump clock agreeing within two minutes before evidence is graded usable.

A card enters the Saturday stack only when check name, rate limit, harm mode and expected evidence are all filled.

### 9.2 Rate limits

Scanners get explicit rate limits below what staging can take. Faster is not better.

Rate limits on API auth checks prevent the 401 loop pattern. Sam's card for staging login checks caps attempts per minute and fails closed when the cap trips. Auth check cards hard-cap attempts per minute to protect the noise budget. Cap trip equals fail closed, not slow down quietly.

Kickoff NTP checks fail the start if skew exceeds two minutes on the jump host versus the API VIP address.

Journey-planner auth cards hard-stop at the agreed attempts-per-minute; a cap trip ends the job rather than whispering slower retries.

### 9.3 WSTG selection

Sam picks auth, session, access control and input handling for the journey planner API — not every WSTG item in one window.

WSTG selection for NMT staging focuses on session, auth and input checks that match rider-facing risk. Cards that need fare backends are not selected for ordinary ENG-512. WSTG picks for NMT staging emphasise session and auth on the journey planner. Fare-backed checks stay off the ordinary selection list.

Detection feedback lists method cards and stop times because silence must never be the SOC's only end-of-window signal.

### 9.4 Interpretation

Map each tool alert to a model element before promoting it to a finding.

Interpretation of a tool hit still needs a human path. An outdated banner at low confidence stays discovery until Sam confirms exposure and impact with evidence. Human interpretation turns tool hits into findings with impact. Banner-only noise stays in discovery until exposure is shown.

Five-minute auth samples beat day-long exports for rider privacy and for Sam's review time when writing findings.

An outdated banner stays discovery until Sam shows exposure and impact a peer can reproduce on staging.

### 9.5 Version pin

Record tool versions on the method card.

Version pin on scanners and scripts goes in the notebook beside ENG-512. Unpinned tools make retests argue about setup instead of fixes. Scanner and script versions are pinned in the notebook before the window. Unpinned tools make FIXED versus STILL OPEN arguments about setup.

Emails, PANs and precise GPS are redacted before vault entry even when the finding itself is about authentication flaws.

Scanner and script digests sit in the notebook before kickoff so FIXED versus STILL OPEN cannot become a setup argument.

### 9.6 Forbidden methods

Password spraying and DoS remain forbidden at NMT.

Forbidden methods include password spraying, fare-network probes and anything not on a method card. Sam's card library lists forbidden items on the cover so peers see them at kickoff. Forbidden methods cover password spraying and any fare touch. The cover of the card library prints that list for kickoff reading.

Telemetry field discipline is sample, redact, sync and notify using the four-oh-one loop stop as the coordination model.

The card-library cover lists password spraying and fare probes as forbidden; kickoff reads that cover aloud.

### 9.7 Card library

Method cards live in a team library with owners. Copying a card without reading stop conditions is a common newcomer mistake Sam watches for.

Card library lives in the runbook repo with owners and review dates. A card without a review in twelve months is retired before it enters ENG-512. Cards without a review in twelve months are retired to archive. Sam will not run stale cards on ENG-512 hosts.

Method cards without harm modes are incomplete for ENG-512 and stay out of the Saturday stack until rewritten.

### 9.8 Noise budget

If a method would generate more alerts than the SOC agreed to handle, Sam reduces rate or reschedules — detection partners are not punching bags.

Noise budget agreed with the SOC caps how many auth failures ENG-512 may generate. Exceeding the budget is a stop condition, not a badge of thoroughness. SOC-agreed noise budget is a number on the kickoff sheet. Crossing it is a stop, celebrated as discipline rather than weakness.

Fare alerts anywhere stop work until operations clears the line regardless of correlation arguments shouted in the moment.

### 9.9 9.x Field discipline

Method cards are useless if they disagree with the ROE. Sam's review step is to highlight the ROE clause each card relies on. If he cannot highlight a clause, the card is rewritten or dropped. This habit also educates newcomers: they see that "we always run tool X" is not a reason — "ROE clause 4.2 allows authenticated GET/POST to staging API at ≤1 rps" is a reason.

Field discipline for methods is cards, rates, pins, forbidden list and noise budget. Sam will not add a clever check mid-window without a written card and SOC notice.

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

Config findings such as missing cookie flags or open 8080 listeners name the file or listener, the expected baseline and the owner. Vague harden servers lines are rewritten before tickets open. Config tickets quote the baseline line and the observed drift — for example missing Secure on a session cookie — with the journey planner owner named. Vague harden lines are rewritten first.

Safe failure releases sockets and prints halt reasons instead of building retry storms against staging authentication.

### 10.2 Code findings

Logic bugs in authorization need developer changes and regression tests.

Code findings in NMT apps are reported with file and line when the ROE allows read access; Sam does not decompile fare vendor binaries under ENG-512. When ROE allows read of app config, Sam cites file and key. Decompiling fare vendor code stays forbidden under ENG-512.

Stop messages follow cause and clock pattern without softener words that muddy the engagement channel for responders.

When ROE allows config read, findings cite file and key; fare-vendor binaries stay off-limits for decompilation under ENG-512.

### 10.3 Safe proposals

Propose the setting, the system, the risk if wrong, and a rollback. Never apply production config yourself unless the ROE and change process say so.

Safe proposals prefer staging config changes with rollback. Sam never proposes a production-only tweak that cannot be tested first on the amber zone. Safe proposals always include a staging patch path and a rollback note. Production-only ideas wait for change windows Sam does not own.

Lab II grades rehearsal stop posts before any live window is scheduled for that technician cohort.

### 10.4 Owner verification

Owners apply changes through their pipeline; Sam verifies.

Owner verification means the journey planner owner confirms the fix before Sam retests. A fix without an owner name stays open. Owner verification is a checkbox on the ticket before retest. Unowned fixes cannot reach FIXED in lab_retest language.

Live channels carry halt facts; after-action owns learning without blame language appearing in the stop thread.

Retest cannot show FIXED until the journey planner owner checkbox is ticked on the ticket.

Sam leaves the owner checkbox blank until the journey planner lead confirms in the ticket thread.

### 10.5 Baselines

NMT's hardening baseline is the checklist; deviations need tickets.

Baselines for TLS and cookie flags are written in the runbook. Drift from baseline is the finding language Sam uses instead of looks bad. Baselines for TLS versions and cookie flags live in the runbook tag named by the ROE. Looks bad is not baseline language.

Secondary contacts are dialled from the ROE card at five minutes when the primary on-call does not answer.

TLS and cookie baselines live in the runbook tag the ROE cites; looks-bad wording is rewritten into drift language.

### 10.6 Drift

Config drift after emergency changes is a recurring finding source.

Drift after a CDN change is checked against the dated model. Sam opens a ticket when staging cookies regress even if no new ENG window is booked. Post-CDN cookie drift opens a ticket even between ENG windows. Sam does not wait for the next Saturday to name a regression.

Untested kill switches keep automation off the Saturday list until Lab II checks the disable path end to end.

Cookie regressions after a CDN cut open tickets mid-week; Sam does not wait for the next Saturday slot.

### 10.7 Rollback tested

A config proposal without a tested rollback is incomplete. Sam asks the owner how they would undo the change in fifteen minutes.

Rollback tested on staging is required before Sam agrees a risky config change is the fix. Untested rollback is itself a risk note in the ticket. Rollback drills on staging are attached as evidence when risky fixes are proposed. Untested rollback keeps the ticket open.

Failure-mode field discipline requires written stops, rehearsed messages, secondary names and tested kills in one checklist.

Risky fixes attach a staging rollback drill as evidence before anyone claims production readiness.

### 10.8 Staging first

Production config findings are reproduced on staging when possible before urging a production change.

Staging first is absolute for ENG-512 config work. Production changes wait for owner change windows; Sam's retests stay on amber until then.

Method cards missing rate, harm, evidence or check name are rejected from the stack at peer review before Saturday.

Amber-zone verification finishes first; production change claims wait on owner windows Sam does not control.

He will not type a production-ready claim while amber retests are still running.

Production-ready wording waits until amber is green and owners control the change window.

### 10.9 10.x Field discipline

Sam keeps a personal library of good config proposals (HSTS, cookie flags, VPN ciphers) written in NMT's change-ticket style. Reusing structure speeds work but he still fills system-specific risk and rollback each time. Copy-pasting a proposal meant for staging into a production ticket without changes is how wrong ciphers get proposed; he treats each proposal as new writing.

Field discipline for config is baseline, owner, staging first, rollback tested. Sam's tickets fail peer review without those four. A rollback that has never been run on staging counts as untested, however simple it looks on paper. Peer review rejects tickets missing those.

### 10.10 10.y Closing note

Sam also asks whether a config change needs a maintenance window. Header changes on the reverse proxy may be instant; VPN cipher changes may drop staff sessions and need a bulletin. Timing is part of a complete proposal.

Closing note: config work at NMT protects riders by staying off fare gear and by naming owners. ENG-512 success is verified baselines, not a long list of unverified tool noise. Closing config work means verified baselines on web and API — never a promise about fare gear Sam did not touch.

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

Retest plan for ENG-512 uses the same method cards and pinned tool versions. lab_retest-style status shows F1 open->closed FIXED, F2 open->open STILL OPEN, F3 open->closed FIXED — fixed: 2 open: 1.

Using the same cards and tool versions is what makes the split meaningful: if F2 is still open, the cause is the fix and not a change in how Sam looked. The notebook places the two-fixed, one-open summary beside the digests of the pinned tools, so an examiner can see that the retest and the original test used identical inputs.

### 11.2 Before/after

Record status transitions explicitly.

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

Before/after evidence hashes sit on the ticket. FIXED without a MATCH hash on the after artefact is not closure at NMT. Before/after hashes on the ticket prove the artefact changed with the fix. FIXED without after-hash is incomplete.

Each transition is written with its date and the evidence that justified it, for example F1 moving from open to closed FIXED with an after-artefact whose digest matches the vaulted copy. A status that changes without a recorded reason cannot be audited later, and NMT's examiners sample exactly these rows when they review closed tickets.

### 11.3 Partial fixes

F2 still open means the ticket stays open with new evidence.

Partial fixes that leave F2 STILL OPEN stay on the tracker with an owner and due date. Sam does not close the engagement as clean while open items remain.

The supervisor review checks that the summary slide shows F2 as STILL OPEN with its owner and due date rather than hiding it under a clean headline. Wording such as partly fixed is not used; the ticket either meets the check on its method card or it does not, and the new evidence explains which part of the fix is missing.

### 11.4 Closure

Closed means FIXED with evidence, or accepted risk with CISO signature — not silence.

Closure requires owner sign-off and verified status FIXED with evidence. Verbal done in chat is rejected in the weekly review.

Risk acceptance is the only other route, and it needs the CISO's signature on the ticket rather than an agreement in a meeting. The weekly review reopens any item that was closed on enthusiasm without vaulted evidence. The pair the review accepts is a stored hash of the after-artefact plus the owner's sign-off.

### 11.5 Scope freeze

No new hunt during retest unless authorized.

During retest the scope is frozen: no new hosts are added to ENG-512, even when a tool suggests another listener. The retest statuses therefore cover only listeners from the original list. The freeze text is read aloud at retest kickoff, and any newly suggested host is written into a parking list as a candidate for the next ROE, where owners can decide whether to authorise it. Retesting a new host without that decision would produce a result nobody had agreed to receive.

### 11.6 Communicate

Send a short retest report to owners the same day.

Communicate retest results to the SOC and owners the same day. STILL OPEN on F2 is not buried until the monthly pack.

Sam sends one message to the SOC lead and the finding owner together, so both hear about F2 at the same moment and neither learns it second-hand. The message timestamps are kept beside the ticket for exam packs. Waiting for the monthly pack would leave the owner a month behind on a weakness that is still open.

### 11.7 Same method

Retest uses the same method card, not a stronger one. Switching methods mid-retest confuses whether the fix worked.

Same method on retest: if F1 was a cookie flag check, retest uses that card, not a different scanner profile that invents a new pass.

If the original check used the cookie card, a different scanner profile might simply not test the same flag and report a pass that means nothing. A peer initials the ticket to confirm that the method card on the retest matches the one used for the finding. Changing the method is a new test, and it needs its own card and ROE line.

### 11.8 Owner demo

When helpful, Sam invites the owner to watch the successful retest once — seeing FIXED builds trust more than a ticket comment.

Owner demo on staging shows the FIXED state before Sam marks closure. Screenshots alone without the owner present are weak for examiner packs.

The owner sees the FIXED state on staging with their own eyes, which makes later disputes about whether the fix was real much less likely. The calendar invitation for the demo is filed as evidence of who witnessed it. Screenshots still go into the vault, but they support the demo rather than replace it.

### 11.9 11.x Field discipline

Retest day is emotionally harder than find day because owners hope for green. Sam opens the call by restating that STILL OPEN is a successful retest outcome when true. He shows the before and after evidence side by side. When F2 remains open, he helps the owner schedule the next fix rather than arguing about severity again — severity was already accepted when the finding was filed.

Field discipline for verification is same method, hashed before/after, owner demo, and honest STILL OPEN counts. Two fixed and one open is the ENG-512 teaching result.

### 11.10 11.y Closing note

If all findings FIX on first retest, Sam still records the methods and hashes. Easy wins deserve the same evidence trail as stubborn ones, especially when examiners sample closed tickets.

The closing note for ENG-512 makes the same point: verification is how NMT comes to trust the programme. Sam's reputation rests on reporting honest open counts, including F2, rather than producing a zero-open slide. A programme that pushes testers towards forced zero-open stories has a defect of its own, and supervisors are expected to name it.

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

The Lab I notebook holds the inventory, the method cards used, the hashes and every stop message. It is kept in ink or in an append-only digital file, so a paused minute stays visible when stop discipline is graded later. Erasing an awkward entry fails the integrity review, because a real evidence pack would lose exactly the record an examiner most wants to see. Corrections are added as new dated lines that point back to the entry they correct.

### 12.2 Peer check

Exchange port lists; score agreement with the approved map.

Peer check scores notebook completeness before sign-off. Missing emergency contact or fare exclusion fails the peer gate. Those two fields are checked first because either gap would have stopped a real ENG-512 window at kickoff. Completeness beats neat handwriting.

Safe proposals include staging paths and rollback notes before anyone discusses production tweaks with managers.

Peers fail the notebook if fare exclusion or emergency contact is missing, neat penmanship notwithstanding.

Emergency contact and fare exclusion are the first two peer-check boxes every time.

Those two boxes fail closed; everything else in peer check is secondary.

### 12.3 Planted fault

Supervisor plants a MISMATCH file; learner must refuse to attach it.

A report that lists the plant must also say what Sam would do next: stop, notify the owner and log the listener.

The supervisor adds a 3389/rdp listener to the lab inventory without telling Sam, so only the lab_ports output reveals it as NOT APPROVED. Sam's report must list the planted listener, or the lab fails. The planted MISMATCH file tests the evidence habit in the same way: attaching it would mean a finding rests on an artefact whose digest no longer matches.

### 12.4 Time box

Ninety minutes, hard stop.

The ninety minutes match the length of a short ENG-512 window on a Saturday. When the clock stops, Sam vaults the artefacts and takes his hands off the keyboard, and the supervisor scores that moment. Typing after the bell counts as silent overtime, a window-discipline failure, because on a real engagement work past the agreed end would be outside the authorisation. Learning to stop mid-task, with a note of what was left undone, is harder than learning to work fast, which is why the bell is scored separately from the findings.

### 12.5 No production

Any attempt to scan NMT production fails the lab.

Lab I uses synthetic inventories only, and rider exports are a hard zero even as illustrations or screenshots. Keeping production data out of the classroom pack means no rider's personal data can leak from a learner's laptop or a shared forum. The rule also keeps the exercise honest about what it can teach: decision habits, not facts about NMT's live estate. A learner who needs a realistic-looking record builds one from the synthetic inventory instead.

### 12.6 Sign-off

Supervisor signs the notebook if peer check and planted fault were handled correctly.

Without that signature the lab stays practice and does not enter Sam's examined portfolio folder. The peer check comes first, so the supervisor signs work that another learner has already checked for the emergency contact and fare exclusion. Requiring both steps mirrors a real engagement, where evidence is reviewed by a peer before anyone signs it off. The supervisor also confirms that the planted fault was found before signing.

### 12.7 Notebook integrity

Altering lab outputs to look better fails the course. Supervisors may re-run the labs and compare hashes.

Integrity also covers the notebook itself: pages are dated, and the final export is hashed. Peers verify that hash and date after sign-off, and any edit made later restarts the review cycle. A supervisor who reruns a lab and finds a different digest knows the output was changed, whatever the reason given. The learner then explains the change in a new review cycle rather than in a quiet correction.

### 12.8 Quiet channel

During the lab, only ROE and stop messages go to the shared channel — no spoilers for peers still working.

Lab questions go to the course forum rather than personal SMS. Sam never pastes the tst-sam-web credentials into any chat, because they belong only on the vault path. Keeping questions in one channel also gives the supervisor a record of what was asked, which helps when grading whether learners stayed within the ROE. Answers posted there also help peers who hit the same question later in the session.

### 12.9 12.x Field discipline

Laboratory I is graded on discipline, not on finding exotic issues. Learners who race ahead to invent attacks on the synthetic data but skip hashing fail. Learners who are slow but refuse the planted mismatch and classify ports correctly pass. Sam reminds peers of that grading bar at the start so competition does not push people toward unsafe habits.

The five field-discipline gates for portfolio entry are the notebook, the peer check, finding the planted fault, keeping to the time box and using synthetic data only. Each gate is marked pass or fail with no partial credit. A learner who meets all five but finds nothing unusual has done exactly what the lab asks.

### 12.10 12.y Closing note

Learners submit the notebook as a single PDF or markdown bundle with a table of contents. Missing initials or timestamps cost points because real evidence packs need attribution.

Lab I exists so that ENG-512 habits form before any real rider is affected by a mistake. Sam treats the planted 3389 line as seriously as a live finding, writing it up with the same fields and evidence. The retest part of the lab teaches the same honesty with pinned tools and identical method cards: two fixed, one open.

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

Troubleshooting tree starts with scope, then tool health, then environment. Sam checks whether 8080 was ever approved before debugging why lab_ports reported it. Troubleshooting asks whether 8080 was approved before debugging lab_ports. Scope first prevents false tool hunts.

FIXED without after-hash remains incomplete regardless of owner enthusiasm typed into chat threads.

The tree asks whether 8080 was ever approved before anyone debugs lab_ports output about it.

Approval status of the listener is question one on the troubleshooting card.

### 13.2 Tool failure

Certificate errors on the tester laptop are not API findings.

Tool failure — crash or empty output — is logged with version pin. Sam switches to a known-good baseline script rather than improvising flags. Crashes log version pins and switch to the known-good script. Improvised flags mid-incident are forbidden.

Clean slides that hide STILL OPEN fail supervisors and are sent back for rewrite before the meeting.

On crash, Sam logs the pin and switches to last week's known-good script instead of inventing flags.

Known-good rollback is a script path in the notebook, not a memory of flags.

### 13.3 Escalation packet

Symptom, steps, screenshots, time, what you already ruled out.

The last good hash tells on-call which evidence file was intact before the problem, so nobody re-collects it blindly.

Sam's ENG-512 escalation packet has four fields: the ticket identifier, the last good hash, the exact stop message that was posted and the owner's contact details. It takes about five minutes to assemble and saves the on-call engineer a long verbal story. Listing what has already been ruled out stops the engineer repeating checks Sam made an hour earlier.

### 13.4 Workarounds

Temporary tool flags are logged and removed after; they are not silent permanent config.

Workarounds that change scope are forbidden. A workaround that probes a new host waits for ROE update. Workarounds that touch new hosts wait for ROE text. Scope-changing cleverness is not troubleshooting.

Tool-suggested hosts during retest wait for the next ROE instead of widening a frozen scope mid-flight.

Workarounds that touch new hosts wait for ROE language; clever scope changes are not troubleshooting.

ROE update requests are the only legal way a workaround may add a host.

### 13.5 Pair debugging

Hard issues get a second technician after fifteen minutes.

Pair debugging puts a second technician on the jump host view. Solo rabbit holes past the time box are cut by the peer.

SOC hears STILL OPEN the same day rather than discovering the gap inside a monthly management pack.

A second technician on the jump-host view cuts rabbit holes that burn past the time box.

Pair sessions are scheduled; hoping someone wanders by is not pairing.

Calendar holds the pair slot before the stuck engineer keeps solo digging.

### 13.6 Customer impact

If riders may be affected, stop and call the emergency contact before deep debugging.

Customer impact means riders seeing errors on the journey planner. Any hint of rider-facing harm is a stop before root-cause analysis continues. Rider-facing errors on the journey planner stop all ENG work immediately. Impact beats root-cause curiosity.

Cookie retests reuse the cookie card rather than a new scanner profile that invents an easy pass.

Journey-planner errors visible to riders halt ENG immediately; impact outranks unfinished root cause.

Rider-visible errors trigger the same stop template used for auth loops.

### 13.7 Known-good baseline

Sam keeps a known-good curl to the staging health endpoint. If that fails, the environment is broken and findings wait.

Known-good baseline is last week's pinned script that printed the expected ok lines. Sam diffs against that before blaming the network.

Owner demos beat screenshot-only closure when examiners ask who personally saw the FIXED state on staging.

Diff against last week's pinned ok lines before blaming network for a sudden NOT APPROVED storm.

Pinned ok output from last week is opened before any network blame thread starts.

### 13.8 Timeboxing ego

After fifteen minutes alone, he must ask for help. Heroic silence wastes engagement window.

Timeboxing ego: thirty minutes on a stuck tool, then escalate. Pride that burns the ENG-512 window helps nobody. Thirty minutes stuck, then escalate. Ego that burns the Saturday window is called out in after-action.

Verification field discipline accepts two-fixed one-open truth as a legitimate ENG-512 result worth publishing.

Thirty minutes stuck, then escalate; after-action names ego that burned the Saturday window.

After-action bullets name the minute count when ego delayed the escalate call.

### 13.9 13.x Field discipline

Sam's troubleshooting notes use the same Fact/Guess labels as casework. "Guess: WAF blocking my IP" becomes a Fact only after the WAF log shows the block. That discipline keeps him from "fixing" the WAF with volume to see what happens — a behaviour that looks like a DoS and violates the ROE.

Field discipline for troubleshooting is tree, baseline, pair, time box, stop on rider impact. Sam's after-action rewards early escalation.

Forced zero-open narratives are programme defects Sam refuses to publish to leadership or examiners.

### 13.10 13.y Closing note

When escalation is required, Sam notifies the engagement lead and the product owner together so nobody hears second-hand that staging is unhealthy.

Closing note: troubleshooting protects the window. Finding the planted fault matters less than stopping when fare alerts appear anywhere. Good troubleshooting stops for fare alerts even when the plant is unsolved. Safety outranks completion.

Lab I notebooks stay append-only including ugly pauses that later teach stop discipline under time pressure.

Fare alerts end troubleshooting even when the planted fault is still unsolved — safety first.

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

Automate inventory checks and hashing that Sam already performs the same way every week. Automation that invents new methods is refused for ENG-512. Automation covers inventory classify and hashing Sam already does weekly. New attack methods are never the automation goal.

Missing fare exclusion fails peer check regardless of neat handwriting on every other notebook page.

Jobs may classify inventories and hash evidence Sam already runs weekly; they may not invent new methods.

Method invention stays off the automation backlog; only proven weekly paths qualify.

### 14.2 Do not automate

Exploitation, scope decisions, severity without review.

Do not automate stop decisions or scope expansion. Humans halt on fare alerts; jobs do not decide to continue. Stop and scope decisions stay human. Jobs must not continue after a fare alert flag.

Missing the planted 3389 fails Lab I despite otherwise excellent prose filling the rest of the notebook.

Stop and scope choices stay human; automation must freeze when a fare alert flag appears.

Fare-alert flags are hard stops in job code, not soft suggestions operators may ignore.

### 14.3 Windows

Automation runs only inside the engagement window with the same rate limits.

Windows for automated jobs match the ROE Saturday window. Overnight freestyle jobs against staging are change-control violations. Job schedules match the ROE Saturday window only. Overnight freestyle against staging violates change control.

Lab I clock stop means vault and hands off the keyboard with no silent overtime minutes afterward.

Schedulers match the ROE Saturday window; overnight freestyle against staging violates change control.

Scheduler ACLs deny overnight ENG users outside the signed Saturday window.

### 14.4 Loop detection

Caps on retries and maximum runtime are mandatory.

Loop detection kills jobs that repeat 401s beyond the noise budget. The synthetic drill's 10:12 stop is the pattern automation must copy. Loop detectors kill 401 storms past the noise budget, copying the 10:12 drill behaviour.

Production rider data in classroom packs is a hard zero even when someone wants it only for illustration.

Loop detectors halt auth storms past the noise budget using the same 10:12 behaviour as the drill.

Noise-budget counters in the job emit the same halt string the drill taught.

### 14.5 Output review

Every automated finding candidate gets human validation.

Output review is mandatory before findings ship. Automated NOT APPROVED lines still need Sam's eyes for name mismatches. Humans still read NOT APPROVED lines for name mismatches before tickets open. Blind auto-filing is refused.

Unsigned labs stay practice outside portfolios until supervisor signature follows a passed peer check.

Before tickets open, a human scans NOT APPROVED lines for DNS name mismatches the job cannot judge.

Name-mismatch review is a required human gate before auto-ticket creation runs.

Auto-ticket jobs stay dark until the human mismatch gate returns approve.

### 14.6 Change control

Automation scripts are versioned like production code.

Change control on automation matches ROE change control. A new job cannot enter Saturday without peer review and SOC notice. New jobs need peer review and SOC notice like ROE changes. Silent job adds are defects.

Post-sign-off notebook edits need a new review cycle rather than quiet fixes nobody can audit later.

New automation needs peer review and SOC notice equal to a ROE change before it may run.

SOC notice for new jobs uses the same template as ROE change announcements.

### 14.7 Idempotent jobs

Automated diffs can run twice without doubling tickets. Sam keys tickets on host+port+date to avoid duplicates.

Idempotent jobs can re-run without doubling tickets. Sam designs ENG-512 reporters to upsert by listener key. Idempotent reporters upsert by listener key so re-runs do not double tickets.

SMS with passwords is forbidden; the course forum holds questions without ever carrying vault secrets.

Reporters upsert by listener key so a re-run cannot open duplicate tickets for the same port.

Listener-key upserts are covered by a unit test in the automation repo.

### 14.8 Disable switch

Automation has a global disable flag the SOC can request. Sam tests that flag on day one of the engagement.

Disable switch is tested in rehearsal. Sam can turn off all ENG automation with one flag if the journey planner misbehaves. Disable-switch tests are Lab II items. Untested disables keep jobs dark.

Lab I credit needs notebook, peer, plant, time box and synthetic-only as five gates that all must pass.

Lab II must exercise the disable flag; paper-only switches leave the job off the Saturday list.

### 14.9 14.x Field discipline

Automation pull requests need a safety block: rate limits, kill switch, dry-run, and which ROE clause allows the job. Without that block, reviewers reject the PR. Sam added the template after a well-meaning script once ran outside the window because cron used UTC and the author thought in local time.

Field discipline for automation is windowed, loop-aware, reviewed, disableable. Unattended cleverness is not a goal at NMT.

Lab I builds muscle memory without putting riders in the blast radius of early technician mistakes.

Windowed, loop-aware, reviewed and disableable — those four adjectives gate every ENG automation job.

### 14.10 14.y Closing note

Sam charts automation runtime per night. A job that suddenly takes ten times longer may be stuck in a loop or hitting a larger inventory — both deserve a human look before the next window.

Closing note: automation multiplies good method cards and also multiplies mistakes. Sam ships jobs only after a manual ENG-512 proved the path.

Troubleshooting asks approval status of a listener before debugging why lab_ports reported it as NOT APPROVED.

Manual ENG-512 success is the prerequisite; automation multiplies mistakes if the path was never proven.

### 14.11 14.z Extra

Caps include both retry count and wall-clock minutes. Sam's port-diff job dies after 20 minutes and pages him; a silent hang is treated like a failed stop switch.

Extra practice: Sam writes a disable drill into every automation README. If the disable switch is untested, the job stays off the Saturday list. Every automation README includes a disable drill Sam has actually run. Paper switches do not count.

Crashes log version pins and switch to known-good scripts instead of improvised flags invented under stress.

Each automation README contains a disable drill Sam has actually executed on the jump host.

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

Dependencies also include map-tile CDNs and identity providers, and Sam lists them so ENG-512 does not report a CDN timeout as a finding against NMT's API. He compares each timeout with the ENG-512 activity times before deciding where it belongs, and keeps that comparison beside the CDN ticket. The SMS notifier and payment deep links get the same treatment, because their failures appear inside NMT's rider screens. Sam records an external contact for each dependency where one is known, so a ticket can go straight to the party that can fix it.

### 15.2 Separate auth

Testing the SMS vendor's core needs the vendor's authorization.

Separate auth for vendors means NMT's signature never authorizes a fare processor's systems. Sam records third parties as out of scope explicitly. Fare processors need their own written auth; NMT's ROE never covers them. Third parties are explicit exclusions.

Scope-changing workarounds wait for ROE text before any new host is touched during a stuck investigation.

Fare processors appear as explicit exclusions; NMT's signature never authorizes another company's systems.

Exclusion rows for processors quote the contract clause id next to the name.

### 15.3 NMT's side

Sam can test how NMT handles vendor callbacks and secrets storage when those paths are in scope.

NMT's side of a dependency finding is the config NMT controls — redirects, API keys stored at NMT, WAF rules. Vendor patch schedules are noted but not owned by Sam. NMT-side fixes are WAF rules, stored keys and redirects Sam's owners control. Vendor patch dates are notes, not Sam's tickets.

Pair debugging cuts solo rabbit holes that burn past the troubleshoot time box without escalating.

Sam's tickets target WAF rules, NMT-stored keys and redirects — vendor patch calendars are notes only.

### 15.4 Responsibility matrix

Who patches what is written down so findings land on the right owner.

Responsibility matrix names NMT owner versus vendor owner for each dependency. Tickets without that split bounce in review.

Rider-facing journey planner errors stop ENG immediately before root-cause curiosity continues on the jump host.

Every dependency ticket names an NMT owner column and a vendor owner column before review accepts it.

Blank vendor-owner cells bounce at triage with a checklist comment.

Triage bots comment need matrix when either owner cell is empty.

Empty cells mean the ticket returns to the reporter before anyone assigns work.

### 15.5 Breaks

Vendor outages during tests are stops, not opportunities to try harder.

Breaks in a CDN path are correlated with ENG-512 times before Sam claims causation. Clock sync and SOC notice prevent false blame. CDN breaks during ENG-512 need clock-aligned SOC notice before causation claims.

Last week's pinned ok output is the known-good diff base before anyone blames the network team wrongly.

Causation claims about CDN breaks wait on clock-aligned SOC notice matching the ENG window.

ENG clock brackets are pasted into CDN incident notes before causation language.

### 15.6 Contracts

Security contact clauses in vendor contracts speed responsible disclosure.

Contracts may forbid testing vendor systems. Sam reads the clause before proposing any vendor-facing check. Contract clauses forbidding vendor tests are pasted into the exclusion list. Sam reads before proposing.

Thirty minutes stuck then escalate; ego that burns the Saturday window is named in the after-action note.

Forbid-test clauses from contracts are pasted into the ROE exclusion list before any vendor proposal.

Legal review initials appear beside pasted forbid-test clauses in the ROE appendix.

Without legal initials the forbid-test paste is treated as incomplete ROE text.

### 15.7 Callback authenticity

When testing NMT's handling of vendor callbacks, Sam uses documented test harnesses, not forged traffic to production payment endpoints.

Callback authenticity for vendor webhooks is verified with staging secrets, not production. Sam's tests never replay live rider callbacks. Webhook tests use staging secrets only. Live rider callbacks are never replayed.

Troubleshooting field discipline lists tree, baseline, pair, time box and rider-stop as the required order.

Webhook exercises use staging secrets exclusively; live rider callbacks are never replayed for demos.

Staging secret IDs used for webhook tests are listed in the evidence index.

### 15.8 Secret scanning scope

Secret scans run on NMT-owned repos listed in the ROE, not on every public fork on the Internet.

Secret scanning scope stays inside NMT repos authorized for ENG-512. Scanning a vendor's public GitHub without written leave is out of scope.

Unsolved plants still yield to fare alerts because safety outranks lab completion every time.

Secret scanning stays inside authorized NMT repositories; vendor GitHub fishing remains out of scope.

Scope text for secret scanning names repository paths, not the whole internet.

Path allow lists for scanners are reviewed when new NMT repos appear.

### 15.9 15.x Field discipline

Sam's dependency map includes a "data shared" column: what NMT sends to each vendor. If NMT should not send rider phone numbers to the map tile provider, that becomes both a privacy control and a test check: inspect outbound requests for unexpected fields during authorized staging tests.

Field discipline for dependencies is matrix, separate auth, NMT-side fixes first. Fare vendors stay out of ordinary probes.

Automation only repeats weekly inventory and hash paths already proven manually on a prior ENG-512.

Matrix, separate auth and NMT-side-first fixes are the dependency field discipline Sam teaches shadows.

### 15.10 15.y Closing note

If a vendor asks Sam to "just quickly test" their portal using NMT credentials, he refuses and points them to their own authorization process. NMT credentials do not travel.

Closing note: dependency clarity keeps Sam from promising SWIFT-like coverage NMT never bought — here, fare-processor coverage it never authorized.

Jobs must not continue after fare alert flags even if the inventory classify run is only half finished.

Clear exclusions stop Sam from promising fare-processor coverage Northline never purchased or authorized.

Closing dependency work restates what NMT did not authorize vendors to undergo.

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

Runbooks for ENG-512 list kickoff, method cards, stop messages and cleanup. Sam links the runbook hash in the ticket so peers share one version.

Overnight freestyle staging jobs violate change control and are disabled when found in the scheduler.

ENG-512 tickets cite the runbook git hash so every peer works from the same kickoff and stop chapters.

Peers paste the runbook hash into their own notebook at kickoff as a receipt.

### 16.2 Safety warnings

Do not run against production is the first line of the staging port-diff runbook.

Safety warnings on the first page restate fare black and no freestyle scanning. Buried warnings fail review.

Loop detectors copy ten-twelve halt behaviour when the agreed noise budget is exceeded by auth checks.

Page one opens with fare black and no freestyle scanning; warnings buried on page nine fail audit.

Audit samples open page one first; buried fare warnings fail that sample.

Sample audits that find fare warnings only on late pages reopen the runbook ticket.

### 16.3 Versioning

Documents show version, date and owner; old versions archived.

Versioning of runbooks uses git tags. Sam will not follow a printed copy older than the tag named in the ROE. Git tags beat printed copies. Sam follows only the tag named in the ROE.

Humans read NOT APPROVED lines for name mismatches before any auto-filing creates tickets for owners.

Kickoff refuses printed copies older than the git tag named in the ROE.

Kickoff checklist includes a git describe against the ROE-named tag.

Mismatch between git describe and the ROE tag cancels kickoff until aligned.

### 16.4 Retirement

Methods that used retired tools are marked obsolete so newcomers do not follow them.

Retirement removes cards that mention decommissioned hosts. Retired pages are archived, not left to confuse the next ENG window. Retired cards for dead hosts move to archive the week of decommission. Stale pages confuse the next window.

New jobs need peer review and SOC notice the same way ROE changes need signatures before effect.

Cards for decommissioned hosts move to archive the same week so stale checks cannot return next Saturday.

### 16.5 Audience

Write for a technician who was out sick during the last engagement.

The readers are technicians and the SOC, not marketing, so each step is written so that a technician who missed ENG-512 can follow it at night without calling Sam. Stop conditions appear in plain words, with an example of the halt message to post. Slogans and praise for tools are edited out before the technician edition is published, because they add length without helping anyone decide what to do.

### 16.6 Review cadence

Runbooks reviewed every six months or after any stop incident.

Review cadence is quarterly or after any architecture change. Missed reviews open a programme debt ticket. Quarterly review or post-architecture-change review opens debt tickets when missed.

Untested disables keep jobs dark until Lab II checks the switch path from README to halt.

Missed quarterly reviews — or skipped post-architecture reviews — open visible programme debt tickets.

Debt tickets for missed reviews carry owners and due dates like any finding.

CISO packs list open documentation debt beside technical findings.

### 16.7 Screenshots in runbooks

Runbooks prefer text steps over screenshots that rot when the UI changes. Where screenshots help, they are dated.

Screenshots in runbooks are synthetic and redacted. Real rider screens never illustrate a procedure. Illustrations are synthetic redacted UI only. Real rider screens never teach procedures.

Automation field discipline is windowed, loop-aware, reviewed and disableable without exception for clever jobs.

Procedure figures use synthetic redacted UI only; real rider screens never teach a step.

Course materials CI rejects PRs that add non-synthetic rider screenshots.

Synthetic-only screenshot policy is enforced by the same CI that builds the book.

### 16.8 Translation

If a contractor shift speaks another language, critical stop warnings appear in both languages used on site.

Translation of stop phrases into the SOC's preferred wording is agreed once and reused. Freelanced empathy in a stop message is not a control.

Jobs ship only after a manual ENG-512 proved the path end to end with peers watching.

SOC-preferred halt phrases are agreed once; freelanced soft wording is not treated as a control.

Agreed halt phrases are versioned beside the ethics charter excerpt.

Charter-adjacent versioning means halt phrase edits need the same owners as ethics text.

### 16.9 16.x Field discipline

When a stop incident happens, Sam updates the runbook the same week or files a ticket why not. Documentation delayed until "after the busy period" is documentation that never happens. His managers accept shorter runbooks that are current over long ones that describe retired tools.

Field discipline for documentation is versioned, warned, retired cleanly, synthetic screenshots. Sam's ENG-512 depends on the tagged runbook, not memory.

Automation READMEs include disable drills Sam has actually run on the jump host during Lab II.

Versioned, warned, cleanly retired and synthetic-illustrated — that is documentation field discipline at NMT.

### 16.10 16.y Closing note

Obsolete runbooks are moved to an /archive folder that CI checks no active link points to. Broken links to retired methods fail the documentation build.

Closing note: documentation is how NMT survives Sam's holiday. A missing stop phrase in the runbook is a defect, not a style choice. Missing stop phrases are defects. Docs keep NMT safe when Sam is on leave.

CDN timeouts need ENG-time correlation before anyone blames the journey planner API for a vendor blip.

Deputies must find stop phrases without Sam; missing phrases are defects, not style choices.

### 16.11 16.z Extra

Sam prints the stop-conditions page of the active runbook and keeps it on the desk during windows — screens lock, paper still readable when seconds matter.

Extra: Sam adds a one-page ENG-512 cheat sheet with emergency contacts and fare exclusion. The cheat sheet hangs beside the jump host and matches the ROE date.

Fare processors need their own written auth listed in exclusions beside NMT signatures on the ROE.

The taped jump-host cheat sheet mirrors ROE date, emergency contacts and fare exclusion on one page.

Tape on the jump host is replaced whenever the ROE date rolls forward.

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

Lab II builds a mini ENG-512: inventory, lab_ports, hash evidence, stop drill, retest statuses. Pass requires planted NOT APPROVED found and a rehearsed stop message.

NMT-side fixes are WAF rules, stored keys and redirects that NMT owners control without vendor tickets.

Learners reuse the Lab I inventory with a fresh planted fault, so a remembered answer does not pass.

Planted fault, hashes, stop drill and retest table are the Lab II deliverable set.

### 17.2 Stop drill

At a random time the supervisor calls stop; learner must post a compliant stop message within two minutes.

Stop drill replays the 401 loop: halt, post ENG-512 stop with time, wait for guidance. Continuing for one more objective fails Lab II. Stop drill fails if Sam continues after the loop for one more objective. Halt and post first.

Tickets without NMT-versus-vendor split bounce in review until the responsibility matrix cells are filled.

Continuing for one more objective after the loop fails the stop drill; halt and post come first.

### 17.3 Evidence index

Table of file, hash, finding id.

Evidence index for Lab II lists every PNG and TXT with hash prefixes. MISMATCH handling must show two-person approval to update expected hashes.

Clock-aligned SOC notice precedes CDN causation claims in after-action write-ups that examiners may read.

Every Lab II artefact appears in the evidence index; MISMATCH rows show two-person hash handling.

Index completeness is graded before any narrative prose in Lab II.

Narrative chapters in Lab II earn zero points if the index is incomplete.

Graders open the index first and only then read Lab II narrative pages.

### 17.4 Peer challenge

Peer tries to get you to attach a mismatched file; you refuse.

Peer challenge tries to find a missing fare exclusion or empty emergency contact. Calm repair scores; defensiveness fails.

Contract forbid-test clauses are pasted into exclusion lists before proposals for vendor checks are drafted.

Challengers hunt empty emergency_contact or missing fare exclusion; calm repair scores, defensiveness fails.

Defensive arguing during peer challenge loses points even if the artefact is later fixed.

Score sheets separate artefact quality from tone during the challenge.

Tone scores and artefact scores are separate columns on the challenge sheet.

### 17.5 Time box

Two hours.

Time box for Lab II is fixed on the course calendar. Overruns become notes, not silent extra minutes. Lab II clock is calendar-fixed. Overrun notes replace silent extra minutes.

Webhook tests use staging secrets; live rider callbacks are never replayed for convenience or demos.

The Lab II calendar clock is fixed; overruns become written notes instead of silent extra minutes.

Calendar-fixed Lab II ends write notes titled overrun rather than hidden typing.

Overrun notes list what remained unfinished when the calendar bell rang.

### 17.6 Pass bar

Stop drill + refusal + coherent report.

Pass bar: planted fault reported, stop drill clean, hashes MATCH or explained, peer check passed. Charm without those artefacts does not pass. Pass bar is plant reported, stop clean, hashes explained, peer passed — charm optional.

Secret scanning stays inside authorized NMT repos and never wanders into vendor public GitHub without leave.

Plant reported, stop clean, hashes explained, peer passed — charm without those artefacts does not pass.

Charm is irrelevant when plant, stop, hashes or peer pass is missing.

Missing any of the four artefacts fails Lab II even with perfect demeanour.

### 17.7 Stress without harm

The stop drill is stressful on purpose; harming systems is not. Supervisors never plant production-impacting faults.

Stress without harm means synthetic load only. No Lab II scenario touches real fare gear or rider production. Stress scenarios stay synthetic. Real fare gear is never a Lab II prop.

Runbook hashes land in tickets so peers share one version during the entire ENG-512 window.

Stress scenarios stay on synthetic data; real fare gear is never a Lab II prop.

Prop lists for Lab II explicitly forbid fare hardware and production data.

### 17.8 After-action

Each Lab II ends with three minutes of after-action: what almost went wrong, what to change in the runbook.

After-action notes three improvements for the next ENG-512. Sam files them before sign-off or Lab II stays incomplete.

Buried safety warnings fail audit; fare black must open page one of every runbook used on Saturday.

Three improvement lines file before sign-off or Lab II remains incomplete on the roster.

Improvement lines are ticketed before the supervisor will ink Lab II sign-off.

Sign-off ink waits on three ticketed improvements linked from the Lab II report.

### 17.9 17.x Field discipline

Laboratory II's peer challenge is play-acting pressure: "just attach it, the hash is close enough". The correct answer is always refuse. Sam has heard similar pressure in real engagements about unverified scanner output. Practising the refusal with a peer makes the real refusal easier.

Field discipline for Lab II is drill, evidence, peer challenge, pass bar. The lab exists to make ENG-512 boringly safe. The pass bar is the planted NOT APPROVED listener found and a stop message rehearsed, with nothing negotiable below that.

Printed runbooks older than the ROE git tag are refused at kickoff and replaced from the tagged tree.

### 17.10 17.y Closing note

Sam's stop message in the drill uses the same template as production engagements, so wording muscle memory transfers. Fancy prose is discouraged; facts win.

Closing note: Lab II is the last gate before Sam's project. A failed stop drill blocks portfolio credit until rehearsed clean.

Retired cards for dead hosts archive the same week as decommission so stale checks cannot return.

A failed stop drill blocks project start until a clean rehearsal earns peer pass.

Project repos stay locked until Lab II stop drill shows a clean peer pass.

### 17.11 17.z Extra

If the stop drill message is late, the lab fails even if the report is perfect. Speed of stopping is the skill being measured.

Extra: Sam keeps the Lab II stop message text as a template in the runbook. Real ENG-512 stops copy the structure, not freestyle prose.

Swagger marketing language is edited out of technician runbooks before they are published to the team.

The Lab II halt sentence is copied into the runbook as the live ENG-512 stop template.

Runbook PRs that update the live stop template require Lab II cohort sign-off.

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

Project brief: deliver a scoped ENG-style pack for synthetic NMT — diagram, ROE checklist, lab_ports result, hashes, retest FIXED/STILL OPEN, stop drill record. No fare probes, no production data.

Missed quarterly reviews open programme debt tickets visible in the CISO pack until closed.

The project delivers diagram, ROE checklist, lab_ports, hashes, FIXED/STILL OPEN and stop record for synthetic NMT with fare untouched.

### 18.2 Presentation

Fifteen minutes to the supervisor and a SOC observer.

Sam's presentation opens with the exclusions and the items still open, such as F2, and only then moves to the evidence. Slides that praise tools without hashes behind them fail the presentation gate; any tool praise belongs in an appendix. The SOC observer checks that the stop path shown on the slides matches the one the SOC actually received during the window. Questions from the supervisor about any open item are answered from the evidence, not from memory.

### 18.3 Handover

Runbooks and scripts in the team repo with versions.

Handover includes vault path, open items, and emergency contacts. Email alone is incomplete; a jump-host walkthrough is scheduled.

SOC-preferred stop wording is agreed once and reused rather than freelanced differently each halt.

Handover books a jump-host walkthrough plus vault path and open tickets; email alone fails transfer.

Transfer checklists require the walkthrough calendar invite as an attachment.

Invite attachments prove the walkthrough was scheduled, not merely promised.

Promised walkthroughs without calendar proof fail the handover checklist.

### 18.4 Limits

Sam still does not perform exploit development or threat-led scenario design — topics for longer courses.

Limits page states fare out of scope, synthetic only, and no authority to test real systems. Hidden limits invent coverage.

Documentation field discipline is versioned, warned, retired clean and synthetic in every illustration.

Each limit points to the ROE line that sets it, so examiners can check that the page does not overstate authority.

Plain examiner-facing limits language is reviewed by a peer before project submit.

Peer-reviewed limits language is the first appendix examiners are told to read.

### 18.5 Next course

AI security (066) is next in the curriculum path.

Next course is the technologist book for design and integration depth. This technical book ends at procedural competence under ROE. Technologist course is next for design depth; this book stops at procedural ROE competence.

Missing stop phrases are defects when Sam is on leave and deputies must halt without him.

Design-heavy work waits for the technologist book; this course ends at procedural ROE competence.

Sam tells finishers which habits transfer and which authority does not carry forward.

### 18.6 Safety cover sheet

Project cover states synthetic-only and no live scanning.

Safety cover sheet restates staging first, fare black, stop conditions, and delete-within retention. It is page one of the project repo.

Jump-host cheat sheets mirror ROE date, emergency contacts and fare exclusion on a single taped page.

Repo page one is the safety cover: staging first, fare black, stop conditions, retention — before any code.

Merges fail if safety cover is not the first file reviewers see in the tree.

First-file checks in review bots reject trees whose safety cover is nested away.

### 18.7 Repository hygiene

Project scripts land in the team repo without credentials, with README and license headers matching NMT policy.

Repository hygiene: no secrets, synthetic inventories only, README with disable and stop instructions. A secret in git fails the project regardless of findings quality. Repo hygiene bans secrets and real inventories. README must show disable and stop instructions.

Lab II pass needs planted NOT APPROVED found and a clean stop drill before any portfolio credit.

Clones with secrets or real inventories fail; README must show disable and stop instructions up front.

### 18.8 Feedback loop

Supervisor feedback becomes two runbook edits within a week — project done means process improved.

Feedback loop from supervisor comments becomes runbook patches the same week. Sam does not archive feedback unread.

Continuing after the loop for one more objective fails Lab II with no partial-credit middle grade.

Supervisor comments become runbook patches the same week; unread feedback archives are defects.

Same-week patch links from feedback are pasted into the project handover note.

Handover notes without same-week patch links are sent back incomplete.

Incomplete handover notes bounce until patch links from feedback are present.

### 18.9 18.x Field discipline

The supervised project cover sheet is single-page: synthetic-only declaration, engagement id of the classroom data pack, list of deliverables with hashes, supervisor signature, and Sam's statement of limits. Without the cover sheet the project is incomplete even if the technical work is excellent.

Field discipline for the project is brief, limits, safety cover, clean repo, honest STILL OPEN. Those five are the pass bar.

Lab II evidence indexes list every hash; MISMATCH rows must show two-person handling in the notes.

Brief, limits, safety cover, clean repo and honest STILL OPEN form the project pass bar together.

### 18.10 18.y Closing note

After acceptance, Sam books a thirty-minute coaching session on OWASP WSTG access-control topics he wants to deepen — continuous learning is part of the project grade at NMT.

Closing note: the project proves Sam can run ENG-512 habits without a teacher in the room. Portfolio credit needs artefacts, not intention. Portfolio credit needs artefacts proving solo ENG-512 habits — intention is not enough.

Peer challenge hunts empty emergency contact; calm repair scores well and defensiveness fails the challenge.

Portfolio credit needs solo ENG-512 artefacts; intention without files does not earn the mark.

### 18.11 18.z Extra

The SOC observer's question is usually about detection: Sam prepares one ATT&CK technique and one log source he would recommend for each finding.

Extra: Sam attaches lab_ports and lab_hash outputs verbatim in an appendix. Examiners should reproduce MATCH/MISMATCH and NOT APPROVED lines without asking him.

Lab II overruns become notes, not silent extra minutes past the calendar clock printed for the cohort.

Appendices paste lab_ports and lab_hash verbatim so examiners reproduce NOT APPROVED and MATCH/MISMATCH alone.

Verbatim lab appendices let examiners diff MATCH/MISMATCH without a meeting.

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
