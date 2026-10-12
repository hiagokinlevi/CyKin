# Quantum and Post-Quantum Security: Hands-On Operations for Technical Staff

- Language: English (`en`); technical course, 18 months; approximately 1,200 hours of planned study.
- Editorial state: **draft**. Chapters 1–18 of 18 have authored teaching text; exercises EX001–EX054 (three per chapter) have matching worked results; offline labs use the Python 3 standard library with verified outputs. Independent review and the 300-page A4 verification remain open. Draft-chapter coverage is not a completed book.
- Audience: technical operators — service-desk engineers, system and network operators, junior administrators — who must check, configure, troubleshoot and verify post-quantum settings on real services under supervision. Entry knowledge: networks, operating systems, scripting and safe lab practice.
- Relation to neighbouring books: the [technologist book](../../../../technologist-3-years/quantum-post-quantum-security/en/book/MANUSCRIPT.md) covers integration and automation in more depth; the [professional book](../../../../professional-6-months/quantum-post-quantum-security/en/book/MANUSCRIPT.md) covers migration governance. **This book is hands-on**: commands, checks, logs, configuration changes, verification and safe lab work.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Educational boundary: not an accredited qualification. No authority to test real systems. All organizations, people and numbers in examples are **synthetic** unless a sentence cites a public source. Command and configuration examples are illustrative; check your product's current documentation. Production systems must use vetted implementations of [FIPS 203](https://doi.org/10.6028/NIST.FIPS.203), [FIPS 204](https://doi.org/10.6028/NIST.FIPS.204) and [FIPS 205](https://doi.org/10.6028/NIST.FIPS.205).

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Eighteen chapters run over 18 months: technical foundations (1–5), post-quantum operations (6–11), laboratory I (12), troubleshooting, automation and integration (13–15), documentation and safety (16), laboratory II (17) and a supervised project (18). Each chapter has learning outcomes, teaching, a worked example, a hands-on activity, common errors, three exercises scored 0–3 (0 absent or unsafe; 1 major gap; 2 minor gaps; 3 complete and justified), a synthesis and a **Continue studying** block. Labs run offline with Python 3; the printed output is shown so you can check your run.

### The running case: Halden Hotel Group

**Halden Hotel Group (HHG)** is a synthetic chain of 12 hotels. Each property runs a property-management system (PMS), point-of-sale terminals, electronic door locks, guest Wi-Fi and a site VPN to the central data centre, which hosts the booking API, the guest portal, the reservations database and a file-exchange service for travel-agency channels. Guest records with passport details must stay confidential for seven years. You work on HHG's operations team. Every number about HHG is invented.

### Source policy

Primary sources were checked on 12 October 2026: NIST FIPS 203/204/205 (August 2024), SP 800-208, [SP 800-227](https://doi.org/10.6028/NIST.SP.800-227), [NIST IR 8547 (initial public draft)](https://doi.org/10.6028/NIST.IR.8547.ipd), [RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html) and [RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html). FN-DSA (FIPS 206) and the HQC standard were still in development. Re-verify status before relying on it.

## Contents

| Stage | Chapters |
|---|---|
| Foundations | [1 Computing and service architecture](#ch-01) · [2 Networks and protocols](#ch-02) · [3 Operating systems and identities](#ch-03) · [4 Scripting and data formats](#ch-04) · [5 Security scope and evidence](#ch-05) |
| PQC operations | [6 System model](#ch-06) · [7 Data and telemetry](#ch-07) · [8 Failure modes](#ch-08) · [9 Tools and methods](#ch-09) · [10 Control configuration](#ch-10) · [11 Verification](#ch-11) · [12 Contained laboratory I](#ch-12) |
| Operations practice | [13 Troubleshooting](#ch-13) · [14 Automation](#ch-14) · [15 Integration and dependencies](#ch-15) · [16 Technical documentation and safety](#ch-16) · [17 Contained laboratory II](#ch-17) · [18 Supervised technical project](#ch-18) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Computing and service architecture

### Learning outcomes

You will (1) describe how a hotel's services fit together from device to data centre; (2) point to where encryption and signatures are used; (3) explain in plain terms what quantum computers threaten; and (4) tell which changes you can make yourself and which need a vendor.

### 1.1 The service map

At an HHG property, a front-desk PC runs the PMS client, which talks over the site VPN to the PMS server in the data centre. Card payments go from point-of-sale (POS) terminals to a payment processor. Door locks are programmed by a lock server through a hub. Guests use Wi-Fi to reach the internet and the guest portal. In the data centre, a load balancer fronts the booking API and portal; servers talk to the reservations database; a file-exchange server sends booking files to travel agencies. Drawing this map is the first job of any operator, because every later check refers to a box or arrow on it.

### 1.2 Where cryptography is used

Encryption protects data moving between boxes (TLS, VPNs, SSH) and stored data (disk and database encryption). Signatures prove who is who (certificates on servers, signed software updates, signed lock firmware). Each use has an *owner* and a *change route*: a setting you can change, a package you can upgrade, a vendor update, or a hardware replacement.

### 1.3 What quantum computers threaten

A large, error-corrected quantum computer running Shor's algorithm (Shor, 1997) could break the public-key methods used today to agree keys and sign — RSA and elliptic curves. It would not meaningfully break AES-256 encryption or SHA-256 hashing. No such machine exists yet. Two risks follow: someone could *record* encrypted traffic now and decrypt it later ("harvest now, decrypt later"), and once such a machine exists someone could *forge* signatures. NIST has published replacement algorithms: ML-KEM ([FIPS 203](https://doi.org/10.6028/NIST.FIPS.203)) for key agreement and ML-DSA ([FIPS 204](https://doi.org/10.6028/NIST.FIPS.204)) and SLH-DSA ([FIPS 205](https://doi.org/10.6028/NIST.FIPS.205)) for signatures.

### 1.4 Worked example

The operator lists cryptographic uses at the Harbour property: PMS client to server over site VPN (ECDH key exchange; change route: VPN appliance firmware, vendor); POS to payment processor (TLS; processor and POS vendor); lock firmware signed with RSA (lock vendor; hardware refresh); guest portal TLS at the load balancer (HHG operations; configuration). Only the last one is a change the operations team can make today.

### 1.5 Hands-on activity

Draw the service map for one property from the description above. For each arrow write: protocol, owner, change route.

### 1.6 Common errors and limits

- Missing devices such as locks and POS terminals.
- Assuming every change is a setting.
- Saying quantum computers "break all encryption".

### Exercises

- **EX001 — Change routes.** For five HHG cryptographic uses, give the change route. Rubric: 3 = five correct routes.
- **EX002 — Plain explanation.** Explain harvest-now-decrypt-later to a hotel manager in two sentences. Rubric: 3 = accurate and jargon-free.
- **EX003 — Keep or replace.** Which of RSA, AES-256, ECDH and SHA-256 must be replaced? Rubric: 3 = RSA and ECDH replaced; AES-256 and SHA-256 kept, with reasons.

### Synthesis

A clear service map shows where cryptography is used, who owns it and how it can change. Quantum computers threaten public-key key agreement and signatures, not symmetric encryption.

### Continue studying — chapter 01 of 18

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Networks and protocols

### Learning outcomes

You will (1) explain TLS, SSH and IPsec at the level needed to check them; (2) identify the key-exchange and authentication parts of each; (3) read which key-exchange group a TLS connection used; and (4) explain why post-quantum handshakes are larger.

### 2.1 Three secure channels

TLS protects web and API traffic; SSH protects administrator logins and file transfers (SFTP); IPsec protects site-to-site VPNs. Each first agrees a session key (key exchange) and proves identity (certificates, host keys or pre-shared keys), then encrypts data with a symmetric cipher.

### 2.2 Hybrid key exchange

The transition design combines a post-quantum and a classical method so that both would have to be broken — called *hybrid* ([RFC 9794](https://www.rfc-editor.org/rfc/rfc9794.html)). In TLS 1.3 the hybrid group X25519MLKEM768 is defined in [RFC 10024](https://www.rfc-editor.org/rfc/rfc10024.html). In SSH, OpenSSH offers `mlkem768x25519-sha256` ([OpenSSH release notes](https://www.openssh.com/releasenotes.html)). In IPsec, [RFC 9370](https://www.rfc-editor.org/rfc/rfc9370.html) adds extra key exchanges such as ML-KEM.

### 2.3 Reading the negotiated group

On a lab machine with a current OpenSSL, `openssl s_client -connect lab-server:443 -groups X25519MLKEM768:X25519` prints details of the handshake, including the negotiated group in recent versions. Server logs can record the group if configured. For SSH, `ssh -v` prints the key-exchange algorithm chosen ("kex: algorithm: …"). Only run such commands against systems you are authorized to test.

### 2.4 Bigger handshakes

The client's TLS key share grows from 32 bytes (X25519) to 1,216 bytes (X25519MLKEM768), so the first message often no longer fits in one network packet. Most networks handle this; some old firewalls do not. Post-quantum signatures add more when certificates change: an ML-DSA-44 signature is 2,420 bytes.

### 2.5 Worked example

An HHG operator connects from the lab to the staging guest portal with a current client and sees the hybrid group negotiated. With an older client, the connection succeeds with X25519 — the expected fallback. Through the lab copy of the Summit property's old firewall, the connection times out; the operator records the firewall model and firmware for follow-up.

### 2.6 Hands-on activity

In your lab, run a TLS client against a test server twice — with and without the hybrid group offered — and record the negotiated group each time. Repeat for SSH with `ssh -v`.

### 2.7 Common errors and limits

- Thinking hybrid key exchange changes certificates.
- Testing systems without authorization.
- Blaming the algorithm for a firewall fault.

### Exercises

- **EX004 — Two parts.** For TLS, SSH and IPsec, name the key-exchange and identity part. Rubric: 3 = six correct entries.
- **EX005 — Read output.** An `ssh -v` line reads `kex: algorithm: curve25519-sha256`. Is the session hybrid? What would you check next? Rubric: 3 = not hybrid; check server and client KEX lists/versions.
- **EX006 — Size.** How much larger is the X25519MLKEM768 client share than X25519? Rubric: 3 = 1,184 bytes.

### Synthesis

TLS, SSH and IPsec each agree keys and prove identity. Hybrid key exchange is available in all three; operators read negotiated algorithms from client output and logs.

### Continue studying — chapter 02 of 18

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Operating systems and identities

### Learning outcomes

You will (1) find which cryptographic libraries a system uses; (2) check versions that matter for post-quantum support; (3) explain how certificates and trust stores work on a server; and (4) handle keys safely.

### 3.1 Libraries and versions

Most Linux services use OpenSSL; OpenSSL 3.5 added ML-KEM, ML-DSA and SLH-DSA and offers X25519MLKEM768 by default in TLS ([OpenSSL 3.5 NEWS](https://github.com/openssl/openssl/blob/openssl-3.5/NEWS.md)). Check with `openssl version`. Containers carry their own libraries, so check inside them too. Applications written in Go or Java use their own TLS stacks; record the runtime version. OpenSSH's version is shown by `ssh -V`.

### 3.2 Certificates and trust stores

A server certificate is signed by a certificate authority (CA). Clients trust certificates that chain to a root in their trust store. The operating system has a trust store; Java and some applications have their own. Post-quantum certificates will need new roots added to every relevant trust store before servers use them.

### 3.3 Handling keys

Private keys belong in protected files readable only by the service account, or better in hardware modules or key-management services. Never paste keys into tickets, chat or logs. If you find an exposed private key, stop and report it through your organization's process; do not copy or test it.

### 3.4 Worked example

The operator checks the HHG file-exchange server: `openssl version` shows 3.0.x (no ML-KEM); `ssh -V` shows an OpenSSH release older than the one that introduced `mlkem768x25519-sha256`. Conclusion: both TLS and SSH upgrades are needed before hybrid key exchange is possible. The PMS server runs a Java application with its own TLS stack; its runtime version goes in the inventory for the vendor to confirm support.

### 3.5 Hands-on activity

On a lab VM, record OpenSSL and OpenSSH versions, list the trust stores present, and check permissions on a test private key file.

### 3.6 Common errors and limits

- Checking the host and forgetting containers.
- Adding roots to the OS store only.
- Copying keys while troubleshooting.
### 3.7 Service accounts and permissions

Services should run under their own accounts with access only to their own keys and configuration. When you upgrade a library to gain post-quantum support, check that the upgrade did not reset file ownership or permissions on key files — package scripts sometimes do. A quick `ls -l` on the key directory before and after the change, saved with your evidence, shows nothing was loosened.

### Exercises

- **EX007 — Version check.** List three commands to establish a Linux server's TLS and SSH post-quantum readiness. Rubric: 3 = `openssl version`, `ssh -V`, container/runtime check.
- **EX008 — Trust stores.** Name three trust stores that might need a new root. Rubric: 3 = OS, Java, application/container bundle.
- **EX009 — Found key.** What do you do if you find a private key in a shared folder? Rubric: 3 = stop, don't copy, report via process, document.

### Synthesis

Library and runtime versions determine whether services can use post-quantum algorithms; certificates rely on trust stores that must be updated first; keys are handled with strict care.

### Continue studying — chapter 03 of 18

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Scripting and data formats

### Learning outcomes

You will (1) read and write JSON and CSV in Python; (2) summarise inventory exports; (3) treat missing values as unknown; and (4) write scripts others can rerun.

### 4.1 Formats

Inventories arrive as JSON from APIs and CSV from spreadsheets and scanners. Python's `json` and `csv` modules read both. Always check the fields you need are present and have expected types.

### 4.2 Practical activity — Lab J

```python
# Lab J (ch 4): parse a synthetic JSON export of TLS endpoints and summarise key exchange by property.
import json, collections
export = json.loads("""[
 {"property": "harbour", "host": "pms-01", "group": "X25519MLKEM768"},
 {"property": "harbour", "host": "pos-02", "group": "secp256r1"},
 {"property": "summit",  "host": "pms-01", "group": "X25519"},
 {"property": "summit",  "host": "lock-hub", "group": null},
 {"property": "lakeside","host": "pms-01", "group": "X25519MLKEM768"}]""")
summary = collections.defaultdict(collections.Counter)
for e in export:
    g = e["group"]
    kind = "unknown" if g is None else ("hybrid" if "MLKEM" in g else "classical")
    summary[e["property"]][kind] += 1
for prop, c in sorted(summary.items()):
    print(f"{prop:9s} hybrid={c['hybrid']} classical={c['classical']} unknown={c['unknown']}")
```

Expected output:

```text
harbour   hybrid=1 classical=1 unknown=0
lakeside  hybrid=1 classical=0 unknown=0
summit    hybrid=0 classical=1 unknown=1
```

The Summit lock hub has no recorded group. The script counts it as *unknown*, not *classical*, because nobody has observed it yet.

### 4.3 Unknown is not "no"

Treating missing values as a negative answer makes reports look complete and hides work. An unknown means "find out", and should create a task: ask the vendor, check configuration or observe traffic.

### 4.4 Rerunnable scripts

Put the input path and output format in arguments, print what was read (number of records), and keep scripts in version control with a short README. A script someone else can rerun next month is worth far more than a one-off calculation.

### 4.5 Worked example

An operator receives `endpoints.csv` from a scanner. Their script counts hybrid, classical and unknown per property, prints the total rows read (48), and writes a small CSV for the dashboard. When the scanner output adds a new column next month, the script still works because it reads columns by name.

### 4.6 Hands-on activity

Modify Lab J to also print the share of hybrid endpoints across all properties.

### 4.7 Common errors and limits

- Reading columns by position.
- Silently skipping rows with errors.
- Not printing how many records were read.
### 4.8 A small CSV example

The same idea works for CSV. Read with `csv.DictReader` so each row is a dictionary keyed by column name; check that the column `group` exists before the loop; and for each row decide hybrid, classical or unknown with the same rule as Lab J. Print the counts and the number of rows read, and write any row that failed validation to a separate file for review rather than discarding it. Rejected rows are often the most interesting ones — a scanner that could not complete a handshake may be pointing at exactly the firewall problem Chapter 13 teaches you to diagnose.

When you hand the script to a colleague, include an example input file with a few synthetic rows and the output it should produce. That small test lets them check the script still works after they change it, the same way the labs in this book show their expected output.

### Exercises

- **EX010 — Share.** What share of Lab J's endpoints is hybrid? Rubric: 3 = 2/5 = 40 %.
- **EX011 — Validation.** Name three checks a script should do on each inventory record. Rubric: 3 = required fields, type/allowed values, duplicates.
- **EX012 — Unknown task.** Write the task you would raise for the Summit lock hub. Rubric: 3 = what to find, how, owner.

### Synthesis

Simple, validated, rerunnable scripts turn inventory exports into honest summaries in which unknowns become tasks.

### Continue studying — chapter 04 of 18

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security scope and evidence

### Learning outcomes

You will (1) work only within written scope; (2) collect evidence that others can check; (3) protect sensitive data you encounter; and (4) report findings clearly.

### 5.1 Scope

Before running any check — even a TLS client connection to a production server — confirm it is within your written scope: which systems, which methods, which times, and who to call if something goes wrong. Active tests that try to force downgrades or inject faults are done only in an isolated lab.

### 5.2 Evidence

Good evidence is specific and reproducible: the command, the target, the time, the output, and the tool version. Screenshots alone are weak; saved text output with a note is better. Store evidence where your team agreed, not on your laptop.

### 5.3 Sensitive data

Handshake captures, logs and configuration files can contain hostnames, client addresses and sometimes credentials. Collect only what you need (for example, the negotiated group), avoid full packet payloads, and follow retention rules.

### 5.4 Reporting

A finding states what you observed, where, when, how, why it matters and what you recommend, plus who owns the fix. Keep facts separate from opinions.

### 5.5 Worked example

Finding (synthetic): "On 3 October 10:15, from the lab jump host (in scope per ticket OPS-412), `openssl s_client` to guest-portal.staging.hhg.example negotiated X25519 although the server configuration lists X25519MLKEM768. Output saved in evidence/OPS-412/. Likely cause: group order. Impact: hybrid protection not in use on staging. Recommendation: reorder groups; recheck. Owner: Web Operations."

### 5.6 Hands-on activity

Write a finding in this format for a lab result from Chapter 2.

### 5.7 Common errors and limits

- Testing outside scope "just to check".
- Evidence without time or tool version.
- Collecting full packet captures.
### 5.8 When something goes wrong

If a check you run causes an unexpected effect — an alert, a slow service, a locked account — stop, note the time and what you ran, and call the contact named in your scope. Do not try to fix it quietly. Early, honest reporting is what keeps authorization in place for future work, and the timeline you record helps the service owner separate your test from any real incident happening at the same time.

Afterwards, add a short note to the evidence folder describing what happened and what you would do differently; the next operator using the same scope will benefit from it.

### Exercises

- **EX013 — Scope check.** List the four things you confirm before running a check. Rubric: 3 = systems, methods, times, contact.
- **EX014 — Evidence fields.** List five fields of a good evidence record. Rubric: 3 = command, target, time, output, tool version.
- **EX015 — Finding.** Rewrite "VPN is bad for quantum" as a proper finding. Rubric: 3 = observation, location, time, method, impact, recommendation, owner.

### Synthesis

Operators work inside written scope, collect checkable evidence while minimizing sensitive data, and write findings that separate facts from opinion.

### Continue studying — chapter 05 of 18

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Quantum and post-quantum security: system model

### Learning outcomes

You will (1) build a simple system model listing cryptographic uses per service; (2) classify each use by quantum exposure; (3) record owner and change route; and (4) use the model to pick first actions.

### 6.1 The model

For each service list: function (key exchange, authentication, stored-data encryption, software signing), algorithm, library or device, owner, change route, and data lifetime. Keep it in a shared table.

### 6.2 Exposure classes

*Record-now risk*: classical key exchange protecting data that must stay secret for years (guest passport details, 7 years). *Forge-later risk*: classical signatures that must stay trustworthy for years or cannot be changed quickly (lock firmware, the internal CA). *Fine for now*: AES-256, SHA-256, short-lived tokens. *Unknown*: no evidence yet.

### 6.3 Picking first actions

First actions are record-now risks that operations can change by configuration: for HHG, the guest portal and booking API on the load balancer, and the file-exchange server after upgrade. Vendor-dependent items become vendor questions; unknowns become investigation tasks.

### 6.4 Worked example

HHG model extract: guest portal (TLS, ECDHE → hybrid available by config, 7-year data, Web Ops) — act now; site VPN (IPsec, ECDH, vendor firmware, 7-year data, Network Ops) — vendor question; lock firmware (RSA signature, hardware, lock vendor) — forge-later, procurement note; reservations DB at rest (AES-256) — fine; minibar sensors (unknown) — investigate.

### 6.5 Hands-on activity

Build the model table for six HHG services and mark first actions.

### 6.6 Using Mosca's rule

A simple rule of thumb (Mosca, 2018): add how long the data must stay secret to how long the change will take; if the total is longer than the time until a capable quantum computer might exist, the data is already at risk. Nobody knows that last number, so try several values (for example 10, 15 and 20 years). Guest records (7 years) plus a two-year VPN upgrade give 9 years — at risk only if such a computer came within 9 years, which is uncertain but not impossible, so the VPN goes on the list behind items with longer lifetimes.

### 6.7 Common errors and limits

- No data lifetime in the model.
- Treating unknown as fine.
- Ignoring change route when picking actions.

### Exercises

- **EX016 — Classify.** Classify guest portal TLS, lock firmware signing, AES-256 backups and an unknown sensor. Rubric: 3 = record-now, forge-later, fine, unknown.
- **EX017 — First action.** Which HHG item can operations fix first, and why? Rubric: 3 = load-balancer TLS config; under ops control, long-lived data.
- **EX018 — Mosca.** For data kept secret 7 years and a 2-year change, under which assumed quantum timelines is it at risk? Rubric: 3 = any timeline under 9 years.

### Synthesis

A system model with exposure classes, owners and change routes shows operators where to act first and where to ask vendors.

### Continue studying — chapter 06 of 18

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Quantum and post-quantum security: data and telemetry

### Learning outcomes

You will (1) collect cryptographic facts from configuration, logs and vendors; (2) assemble a cryptographic bill of materials (CBOM); (3) add negotiated-algorithm fields to logs; and (4) report coverage and unknowns.

### 7.1 Sources

Configuration files tell you what a service *offers*. Logs tell you what was *negotiated*. Vendor statements tell you what a closed device *claims*. Each fact in the CBOM should say which source it came from and when.

### 7.2 Practical activity — Lab I

```python
# Lab I (ch 7): aggregate a synthetic cryptographic bill of materials (CBOM) and measure coverage.
records = [  # (asset, function, algorithm, source)
    ("booking-gateway", "key-exchange", "X25519MLKEM768", "passive"), ("booking-gateway", "signature", "RSA-2048", "config"),
    ("door-lock-hub", "key-exchange", "ECDHE-P256", "passive"), ("door-lock-hub", "signature", "ECDSA-P256", "code"),
    ("reservations-db", "key-exchange", "RSA-kex", "config"), ("billing", "data-at-rest", "AES-256-GCM", "code"),
    ("minibar-sensor", "unknown", "unknown", "none"), ("property-vpn", "key-exchange", "ECDHE-P384", "config")]
VULN = {"RSA-2048", "ECDHE-P256", "ECDSA-P256", "RSA-kex", "ECDHE-P384"}
assets = {r[0] for r in records}
unknown = {r[0] for r in records if r[2] == "unknown"}
vuln = [r for r in records if r[2] in VULN]
print(f"assets {len(assets)}, unknown {len(unknown)} ({100*len(unknown)/len(assets):.0f}%)")
print(f"quantum-vulnerable uses {len(vuln)}:", ", ".join(f"{a}/{f}" for a, f, _, _ in vuln))
print("hybrid key exchange present on:", [r[0] for r in records if "MLKEM" in r[2]])
```

Expected output:

```text
assets 6, unknown 1 (17%)
quantum-vulnerable uses 5: booking-gateway/signature, door-lock-hub/key-exchange, door-lock-hub/signature, reservations-db/key-exchange, property-vpn/key-exchange
hybrid key exchange present on: ['booking-gateway']
```

The minibar sensor is unknown; until it is investigated, the CBOM cannot say whether its traffic is at risk.

### 7.3 Logging negotiated algorithms

Web servers and load balancers can usually log the TLS protocol, cipher and group per connection; add those fields to the access log format in staging first, check the log volume, then promote. SSH servers log the key-exchange algorithm at an appropriate log level. VPN appliances log the methods negotiated per tunnel. Log only what you need: algorithm fields, service, time and a coarse client identifier.

### 7.4 Coverage

Report what share of services has evidence, by source. "Hybrid on 40 % of connections" means little unless you say which services and sensors were included. Show unknowns next to every figure.

### 7.5 Worked example

HHG adds the negotiated group to load-balancer logs. After a week, the dashboard shows: booking API 88 % hybrid; guest portal 3 % hybrid (a configuration problem found in Chapter 5); file exchange 0 % (old OpenSSH); property VPNs — configuration evidence only, 0 of 12 hybrid; locks and minibar sensors — unknown.

### 7.6 Hands-on activity

In the lab, add the negotiated TLS group to a web server's access log and confirm it appears for hybrid and classical clients.

### 7.7 Keeping the CBOM up to date

Update the CBOM after every relevant change: library upgrades, new certificates, new devices, vendor firmware. Mark entries older than three months as "needs re-check". An out-of-date CBOM is worse than none if people trust it.

### 7.8 Common errors and limits

- Treating configuration as proof of negotiation.
- Verbose debug logging in production.
- Hiding unknowns.

### Exercises

- **EX019 — Source.** Which source proves a group was negotiated: config, logs or vendor sheet? Rubric: 3 = logs (or client output), with reason.
- **EX020 — Lab I count.** How many quantum-vulnerable uses does Lab I find, and on how many distinct assets? Rubric: 3 = five uses on four assets.
- **EX021 — Coverage line.** Write a coverage line for the HHG dashboard in 7.5. Rubric: 3 = scoped figures with sources and unknowns.

### Synthesis

Operators build the CBOM from configuration, logs and vendor statements with dates and sources, add negotiated-algorithm logging, and report coverage with unknowns visible.

### Continue studying — chapter 07 of 18

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Quantum and post-quantum security: failure modes

### Learning outcomes

You will (1) list ways post-quantum changes can fail; (2) recognise each from symptoms; (3) know the safe first response; and (4) avoid fixes that remove protection everywhere.

### 8.1 Common failure modes

*Large handshake dropped*: an old firewall, proxy or load balancer cannot handle the bigger first message; symptom: timeouts on one path only. *No shared group*: client and server have no algorithm in common, often after removing classical options too early. *Silent fallback*: hybrid is offered but classical is chosen, because of order or old clients; symptom: nothing breaks, but logs show classical. *Certificate failure*: a client cannot check a post-quantum certificate or does not trust the new root. *Slow devices*: small devices take longer for larger messages.

### 8.2 Safe first responses

Collect evidence first (time, client, path, error). Limit impact narrowly: route the affected client group to a compatible listener, or roll back the change on the affected site only. Do not disable hybrid everywhere because of one path; that removes protection from all other traffic.

### 8.3 Silent fallback deserves alerts

Because nothing breaks, silent fallback can last for months. Add an alert when the hybrid share on a service drops sharply, and check the last change on that service first.

### 8.4 Worked example

After a load-balancer update at the data centre, the booking API's hybrid share falls from 88 % to 2 % with no errors. The operator checks the change log: the update restored a default TLS profile. Restoring the approved profile returns the share to 87 % within ten minutes. A note is added to the change checklist: "Re-apply TLS profile after firmware updates."

### 8.5 Hands-on activity

For each failure mode in 8.1, write the symptom you would see on the dashboard or in a ticket, and your first check.

### 8.6 Rollback rules

Every change that touches cryptographic settings needs a written rollback: the exact previous configuration, who may trigger rollback, and how to confirm success. Prefer rolling back one site or listener rather than the whole estate. After rollback, keep the evidence and open a problem ticket so the cause is fixed instead of the change being forgotten.

### 8.7 Common errors and limits

- Global disable to fix a local fault.
- No alert for silent fallback.
- Rollbacks without evidence.

### Exercises

- **EX022 — Symptom match.** Match symptoms to failure modes: timeouts through one proxy; "no shared group" error; hybrid share drops, no errors. Rubric: 3 = three correct matches.
- **EX023 — First response.** A guest portal path through one property firewall times out. Give three first steps. Rubric: 3 = evidence, narrow mitigation, escalate/owner.
- **EX024 — Checklist line.** Write a change-checklist line that would have prevented the incident in 8.4. Rubric: 3 = specific, checkable.

### Synthesis

Post-quantum changes fail in a few recognisable ways; operators collect evidence, limit impact narrowly, alert on silent fallback and keep rollbacks local.

### Continue studying — chapter 08 of 18

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Quantum and post-quantum security: tools and methods

### Learning outcomes

You will (1) use client tools to check negotiation; (2) estimate handshake sizes for certificate choices; (3) validate a tool before trusting it; and (4) follow a repeatable checking method.

### 9.1 Client tools

`openssl s_client` (TLS), `ssh -v` (SSH), and VPN appliance status commands show negotiated algorithms. Use a client with post-quantum support; an old client will always report classical. Record client version with every result.

### 9.2 Practical activity — Lab B

```python
# Lab B (ch 9): bytes of authentication in a TLS handshake for different signature choices.
# Sizes in bytes: (public key, signature). ML-DSA from FIPS 204; SLH-DSA-128s from FIPS 205.
algs = {"ECDSA P-256": (65, 72), "RSA-2048": (270, 256), "ML-DSA-44": (1312, 2420),
        "ML-DSA-65": (1952, 3309), "SLH-DSA-SHA2-128s": (32, 7856)}
def chain_bytes(alg, depth=2, scts=2):
    pk, sig = algs[alg]
    certs = depth * (pk + sig + 400)          # leaf + intermediate: key + CA signature + ~400 B fields
    return certs + sig + scts * sig           # + CertificateVerify + embedded SCT signatures
for a in algs:
    print(f"{a:20s} ~{chain_bytes(a):6d} bytes of certificates and signatures")
```

Expected output:

```text
ECDSA P-256          ~  1290 bytes of certificates and signatures
RSA-2048             ~  2620 bytes of certificates and signatures
ML-DSA-44            ~ 15524 bytes of certificates and signatures
ML-DSA-65            ~ 21249 bytes of certificates and signatures
SLH-DSA-SHA2-128s    ~ 40144 bytes of certificates and signatures
```

Post-quantum certificates make handshakes much bigger. Operators need these numbers when a network team asks why a firewall suddenly sees larger messages after a certificate change.

### 9.3 Validating tools

Before using a scanner on real systems, test it against lab servers with known settings: hybrid preferred, hybrid offered but not preferred, classical only. If the tool cannot tell these apart, do not use its results.

### 9.4 A repeatable method

1. Confirm scope. 2. Record tool and version. 3. Run the check. 4. Save the output. 5. Compare with the expected result. 6. Record the finding or "as expected". Repeating the same steps makes results comparable over time.

### 9.5 Worked example

An HHG operator's scanner reports every server as classical. Testing against the lab shows the scanner bundles an old OpenSSL. After upgrading, it correctly identifies the lab's hybrid server; only then is it used on the staging estate, within scope.

### 9.6 Hands-on activity

Validate one TLS client tool against three lab server settings and record the results.

### 9.7 Reading sizes

Lab B's numbers are estimates under stated assumptions: two certificates in the chain, about 400 bytes of other certificate fields, two certificate-transparency signatures. Real chains can be longer or shorter. When you need exact numbers for a firewall rule or a ticket, capture a lab handshake and measure it, then note the configuration it came from.

### 9.8 Common errors and limits

- Using unvalidated tools.
- Results without client versions.
- Treating size estimates as measurements.
### 9.9 Comparing results over time

Keep each check's saved output in a dated folder so that next month's run can be compared line by line. A simple `diff` between two runs of the same script quickly shows which services changed negotiation, which is often faster than reading a dashboard when you are investigating a specific complaint.

### Exercises

- **EX025 — Tool validation.** Describe the three lab settings and expected results for validating a scanner. Rubric: 3 = three settings with expected outputs.
- **EX026 — Size ratio.** From Lab B, roughly how many times larger is ML-DSA-44 authentication than ECDSA P-256? Rubric: 3 = about 12 (15,524/1,290).
- **EX027 — Method.** List the six steps of a repeatable check. Rubric: 3 = all six in order.

### Synthesis

Operators use validated, current client tools, record versions, follow a repeatable method and understand the size effects of post-quantum certificates.

### Continue studying — chapter 09 of 18

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Quantum and post-quantum security: control configuration

### Learning outcomes

You will (1) configure hybrid key exchange on TLS and SSH servers in a lab; (2) audit configurations for presence and preference; (3) keep classical fallback during transition; and (4) apply changes through change control.

### 10.1 TLS configuration

On OpenSSL-based servers, set the group list with hybrid first, for example `X25519MLKEM768:X25519:secp256r1`. Web servers and load balancers expose this through a directive or profile; check your product documentation for exact names. Order matters when the server decides.

### 10.2 SSH configuration

In OpenSSH's server configuration, put `mlkem768x25519-sha256` first in `KexAlgorithms`, followed by `sntrup761x25519-sha512@openssh.com` and `curve25519-sha256` for compatibility. Reload the service and test with `ssh -v` from a client that supports the hybrid.

### 10.3 Practical activity — Lab T

```python
# Lab T (ch 10): audit synthetic TLS server configurations for post-quantum key exchange and preference order.
configs = {  # service: ordered list of offered groups (server preference) - synthetic
    "booking-api": ["X25519MLKEM768", "X25519", "secp256r1"],
    "guest-portal": ["X25519", "X25519MLKEM768", "secp256r1"],
    "channel-sftp": ["ecdh-sha2-nistp256"],
    "ops-grafana": ["X25519", "secp384r1"]}
HYBRID = {"X25519MLKEM768", "SecP256r1MLKEM768", "SecP384r1MLKEM1024"}
for svc, groups in configs.items():
    offered = [g for g in groups if g in HYBRID]
    if not offered: verdict = "CLASSICAL ONLY"
    elif groups[0] in HYBRID: verdict = "OK (hybrid preferred)"
    else: verdict = "WARN hybrid offered but not preferred"
    print(f"{svc:17s} {verdict}")
```

Expected output:

```text
booking-api       OK (hybrid preferred)
guest-portal      WARN hybrid offered but not preferred
channel-sftp      CLASSICAL ONLY
ops-grafana       CLASSICAL ONLY
```

The guest portal offers hybrid but prefers X25519 — the problem found in Chapter 5. The channel SFTP and ops dashboard are classical only.

### 10.4 Change control

Every production change goes through a change ticket: what, why, when, risk, test evidence, rollback, approver. Make the change in staging, verify, then apply in production in a low-traffic window, verify again and close the ticket with evidence.

### 10.5 Worked example

Ticket OPS-430: reorder groups on guest-portal load balancer to `X25519MLKEM768:X25519:secp256r1`. Staging test: hybrid negotiated by current clients, X25519 by an old client. Production change Tuesday 06:00; verification at 06:10 shows hybrid negotiated; dashboard hybrid share climbs from 3 % to 85 % by noon. Rollback plan (restore previous order) not needed.

### 10.6 Hands-on activity

In the lab, configure a TLS server and an SSH server with hybrid first; verify with clients; write the change ticket you would raise for production.

### 10.7 Keep fallback for now

During transition, keep classical options after the hybrid so that older clients still connect. Removing them is a separate, later decision based on monitoring that shows few remaining classical clients and agreement with service owners and partners.

### 10.8 Common errors and limits

- Hybrid listed after classical.
- Removing fallback too early.
- Changes without tickets or verification.

### Exercises

- **EX028 — TLS line.** Write a group list with hybrid first and two classical fallbacks. Rubric: 3 = hybrid first, valid names.
- **EX029 — SSH line.** Write a `KexAlgorithms` line with hybrid first and compatible fallbacks. Rubric: 3 = valid ordered list.
- **EX030 — Ticket.** Write the change ticket for enabling hybrid SSH on the channel SFTP server. Rubric: 3 = what, why, when, risk, test evidence, rollback, approver.

### Synthesis

Operators configure hybrid first with classical fallback on TLS and SSH, audit preference as well as presence, and make changes through tested, verified tickets.

### Continue studying — chapter 10 of 18

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Quantum and post-quantum security: verification

### Learning outcomes

You will (1) verify that changes achieved their aim; (2) run known-answer and negative tests in the lab; (3) use negative controls; and (4) close work with evidence.

### 11.1 Verify negotiation, not configuration

A configuration can say hybrid while connections negotiate classical. Verify from the client side (tool output) and the server side (logs). For SSH, check the KEX algorithm in `ssh -v`; for VPNs, check tunnel status.

### 11.2 Practical activity — Lab V

```python
# Lab V (ch 11): known-answer and negative tests - the habit behind validating PQC libraries.
import hashlib
KATS = [  # (function, input, expected hex prefix) - published test values for SHA-3 / SHAKE on empty input
    ("sha3_256", b"", "a7ffc6f8bf1ed76651c14756a061d662f580ff4de43b49fa82d80a4b80f8434a"),
    ("shake_128/32", b"", "7f9c2ba4e88f827d616045507605853ed73b8093f6efbc88eb1a6eacfa66ef26"),
]
def run(name, data):
    if name == "sha3_256": return hashlib.sha3_256(data).hexdigest()
    return hashlib.shake_128(data).hexdigest(32)
for name, data, want in KATS:
    print(f"KAT {name:13s}", "PASS" if run(name, data) == want else "FAIL")
SIZES = {"ML-KEM-512": 800, "ML-KEM-768": 1184, "ML-KEM-1024": 1568}   # encapsulation-key bytes, FIPS 203
def validate_ek(param, ek):
    if len(ek) != SIZES[param]: raise ValueError(f"{param}: expected {SIZES[param]} bytes, got {len(ek)}")
    return True
for param, n in [("ML-KEM-768", 1184), ("ML-KEM-768", 1183), ("ML-KEM-512", 1184)]:
    try: validate_ek(param, bytes(n)); print(f"negative/positive test {param} len {n}: accepted")
    except ValueError as e: print(f"negative/positive test {param} len {n}: rejected ({e})")
```

Expected output:

```text
KAT sha3_256      PASS
KAT shake_128/32  PASS
negative/positive test ML-KEM-768 len 1184: accepted
negative/positive test ML-KEM-768 len 1183: rejected (ML-KEM-768: expected 1184 bytes, got 1183)
negative/positive test ML-KEM-512 len 1184: rejected (ML-KEM-512: expected 800 bytes, got 1184)
```

Known-answer tests check that functions produce published outputs; negative tests check that wrong-length inputs are rejected.

### 11.3 Negative controls

To trust a check, show it can fail: run it against a server with hybrid removed and confirm it reports classical. A check that always says "pass" is useless.

### 11.4 Closing with evidence

Attach outputs, dashboard screenshots with times, and the configuration version to the ticket. Note anything unexpected, even if the change worked.

### 11.5 Worked example

After OPS-430, the operator verifies: three client types against the production portal (two hybrid, one older client classical as expected); load-balancer logs show 85 % hybrid; negative control in staging (hybrid removed) correctly shows 0 %. Evidence attached; ticket closed.

### 11.6 Hands-on activity

Verify a lab change from both client and server sides and include a negative control.

### 11.7 Verifying after other changes

Verification is not only for your own changes. Re-check hybrid negotiation after any update that touches the TLS or SSH stack — operating system patches, load-balancer firmware, container image rebuilds — because such updates can reset configuration. A short scripted check run after every patch window catches regressions within hours.

### 11.8 Common errors and limits

- Verifying configuration only.
- No negative control.
- Closing tickets without evidence.
### 11.9 What verification does not show

A successful hybrid negotiation shows that the session key was agreed with ML-KEM and X25519 together. It does not show that the server certificate is post-quantum (it is probably still ECDSA or RSA), that every other hop on the path is protected, or that the library is free of implementation flaws. Write these limits in the ticket so that nobody reads "verified" as "the whole service is quantum-safe". Implementation quality comes from using vetted, updated libraries; past flaws such as the KyberSlash timing issue (Bernstein et al., 2024) were fixed by library updates, not by configuration.

### Exercises

- **EX031 — Two sides.** Name the client-side and server-side evidence for TLS hybrid negotiation. Rubric: 3 = tool output and server logs.
- **EX032 — Negative control.** Design a negative control for SSH hybrid verification. Rubric: 3 = remove hybrid, expect classical.
- **EX033 — Post-patch check.** Write three steps of a post-patch verification. Rubric: 3 = run clients, check logs/dashboard, compare to baseline.

### Synthesis

Verification checks real negotiation from both sides, includes negative controls, is repeated after other updates and closes work with evidence.

### Continue studying — chapter 11 of 18

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Contained laboratory I

### Learning outcomes

You will (1) build an isolated lab with hybrid-capable TLS and SSH; (2) reproduce a hybrid deployment end to end; (3) reproduce a common failure; and (4) write a lab report.

### 12.1 Lab build

Use two or three virtual machines or containers on an isolated network: a server with a current OpenSSL and OpenSSH, a client with current tools, and optionally an old client. No production data, no connection to production networks, no real credentials.

### 12.2 Exercises in the lab

Configure the server with hybrid first; connect with the current client (expect hybrid) and old client (expect classical fallback). Then reorder the groups to put classical first and observe that the current client now negotiates classical — the silent fallback of Chapter 8. Restore the correct order.

### 12.3 Reproducing a size failure

Some labs can emulate a device that drops large first messages, for example a proxy configured with a small buffer. Observe timeouts with hybrid and success without it. This shows why the fix is on the network device, not in removing protection.

### 12.4 Lab report

State purpose, environment (versions), steps, results, interpretation and lessons. Include outputs.

### 12.5 Worked example

An HHG trainee's lab report: server OpenSSL 3.5.x and current OpenSSH; current client negotiated X25519MLKEM768 and `mlkem768x25519-sha256`; old client fell back to classical; reordered groups caused silent fallback; restored. Lesson: always check preference order after edits.

### 12.6 Hands-on activity

Build the lab and complete the steps; write your report.

### 12.7 Lab safety

Keep the lab network separate from home or office networks; use generated test keys; destroy the lab when finished or snapshot it with notes. Never point lab tools at production hosts by mistake: use hostnames that cannot resolve outside the lab, and double-check targets before running commands.

### 12.8 Common errors and limits

- Labs connected to production.
- Skipping the old-client test.
- Reports without versions.
### 12.9 Extending the lab

Once the basics work, extend the lab one step at a time: add a second server behind a reverse proxy to show that each hop negotiates separately; add a log parser that counts hybrid and classical sessions; or add an SSH bastion to practise the SFTP configuration of Chapter 10. Each extension should end with a short note in the report so the lab grows into a reusable training environment for the team.

### Exercises

- **EX034 — Lab design.** List the machines and software versions for the lab. Rubric: 3 = server, current client, old client, versions.
- **EX035 — Silent fallback.** Describe how to reproduce silent fallback in the lab. Rubric: 3 = reorder groups, observe classical with current client.
- **EX036 — Report.** List the six sections of the lab report. Rubric: 3 = purpose, environment, steps, results, interpretation, lessons.

### Synthesis

A contained lab lets operators reproduce hybrid deployment, silent fallback and size failures safely, and document lessons.

### Continue studying — chapter 12 of 18

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Quantum and post-quantum security: troubleshooting

### Learning outcomes

You will (1) follow a step-by-step troubleshooting method; (2) triage failure logs into likely causes; (3) fix common problems without removing protection broadly; and (4) record the cause and fix.

### 13.1 Method

Reproduce → isolate → hypothesise → test → fix → verify → record. Reproduce with the same client and path in the lab if possible. Isolate by trying a direct path, a different client, or hybrid off for one test connection. Change one thing at a time.

### 13.2 Practical activity — Lab H

```python
# Lab H (ch 13): triage synthetic handshake failure logs into likely causes.
import re, collections
logs = """2026-10-01T10:00Z client=10.0.4.7 err=handshake_timeout size_clienthello=1530 path=proxy-b
2026-10-01T10:01Z client=10.0.4.9 err=handshake_timeout size_clienthello=1530 path=proxy-b
2026-10-01T10:02Z client=10.0.7.2 err=no_shared_group offered=x25519mlkem768
2026-10-01T10:03Z client=10.0.4.8 err=handshake_timeout size_clienthello=1530 path=proxy-b
2026-10-01T10:04Z client=10.0.9.1 err=bad_certificate alg=mldsa65
2026-10-01T10:05Z client=10.0.4.3 err=handshake_timeout size_clienthello=300 path=direct""".splitlines()
causes = collections.Counter()
for line in logs:
    f = dict(re.findall(r"(\w+)=(\S+)", line))
    if f["err"] == "handshake_timeout" and int(f.get("size_clienthello", 0)) > 1400: c = "large ClientHello dropped (" + f["path"] + ")"
    elif f["err"] == "no_shared_group": c = "client/server group mismatch"
    elif f["err"] == "bad_certificate": c = "client cannot verify PQ certificate"
    else: c = "other / investigate"
    causes[c] += 1
for c, n in causes.most_common(): print(f"{n}  {c}")
```

Expected output:

```text
3  large ClientHello dropped (proxy-b)
1  client/server group mismatch
1  client cannot verify PQ certificate
1  other / investigate
```

Three timeouts share one proxy and a large first message: the proxy is the likely cause. The group mismatch and certificate error need separate tickets.

### 13.3 Typical fixes

Proxy or firewall drops large messages → firmware update or configuration fix on that device; meanwhile route affected users to a compatible listener. No shared group → restore classical fallback on the server or upgrade the client. Certificate verification failure → add the new root to the client's trust store or keep the classical certificate for that client group. Silent fallback → fix the group order and add an alert.

### 13.4 Recording

Write the symptoms, evidence, cause, fix, verification and anything left to do. Link related tickets so patterns are visible: three properties with the same firewall model should become one vendor case.

### 13.5 Worked example

Ticket: "Summit front desk cannot load guest portal since Monday." Evidence: timeouts only from Summit; Lab H-style triage shows large ClientHello via the property firewall. Lab test with the same firewall firmware reproduces it. Interim: a policy routes Summit's front-desk subnet to a listener without the hybrid group, recorded as an exception. Fix: firewall firmware update Thursday; exception removed; hybrid negotiations from Summit confirmed.

### 13.6 Hands-on activity

Using Lab H's output, write three tickets — one per distinct cause — with first checks.

### 13.7 Asking for help

Escalate when the cause is outside your control or the fix needs a change you are not authorized to make. Include evidence, what you tried and what you need. Good escalations are short, specific and reproducible; they are answered faster.

### 13.8 Common errors and limits

- Turning hybrid off everywhere.
- Changing several settings at once.
- Fixes without verification.

### Exercises

- **EX037 — Triage.** In Lab H, which cause would you investigate first and why? Rubric: 3 = proxy timeouts, most frequent and shared pattern.
- **EX038 — Interim fix.** Describe a narrow interim fix for the Summit problem. Rubric: 3 = route subnet to compatible listener with exception and expiry.
- **EX039 — Escalation.** Write a three-line escalation to the firewall vendor. Rubric: 3 = product/version, evidence, request.

### Synthesis

Methodical troubleshooting, log triage and narrow interim fixes resolve post-quantum problems while keeping protection for everyone else.

### Continue studying — chapter 13 of 18

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Quantum and post-quantum security: automation

### Learning outcomes

You will (1) automate routine checks of negotiation and configuration; (2) use confidence bounds to decide when a rollout stage is safe; (3) schedule checks after patches; and (4) keep scripts maintainable.

### 14.1 Routine checks

Schedule scripts to: run a client check against each in-scope service daily; parse logs for hybrid share; audit configuration exports for presence and preference. Send results to the dashboard and alert on changes.

### 14.2 Practical activity — Lab K

```python
# Lab K (ch 14): canary gate for enabling a hybrid group - promote only if failures stay within budget.
import math
def upper95(k, n):                      # Wilson upper bound
    z = 1.96; p = k / n; d = 1 + z*z/n
    return ((p + z*z/(2*n)) + z*math.sqrt(p*(1-p)/n + z*z/(4*n*n))) / d
baseline, budget = 5e-4, 4e-4            # baseline failure rate, allowed increase
for stage, k, n in [("1% canary", 3, 5000), ("10% canary", 28, 50000), ("10% canary (proxy site)", 96, 50000)]:
    ub = upper95(k, n); ok = ub <= baseline + budget
    print(f"{stage:24s} {k}/{n}  upper95={ub:.5f}  {'PROMOTE' if ok else 'HOLD'}")
```

Expected output:

```text
1% canary                3/5000  upper95=0.00176  HOLD
10% canary               28/50000  upper95=0.00081  PROMOTE
10% canary (proxy site)  96/50000  upper95=0.00234  HOLD
```

When a change is rolled out in stages, the decision to move to the next stage should use the upper confidence bound on the failure rate, not just the observed rate. A small sample can look good by luck.

### 14.3 After patch windows

Run the full check set automatically after each patch window and compare with the previous run. Differences go to the on-call operator.

### 14.4 Maintainable scripts

Version control, a README, clear inputs and outputs, error messages that say what went wrong, and a small test with known input. Avoid hard-coded passwords; use the approved secret store.

### 14.5 Worked example

HHG schedules a nightly job that runs `openssl s_client` checks against 14 staging and production endpoints in scope, extracts the negotiated group, and writes a CSV. A diff with the previous night flags two endpoints that changed from hybrid to classical after a load-balancer patch; the morning operator restores the profile.

### 14.6 Hands-on activity

Write a script that reads a list of lab hosts, runs a TLS check on each, and prints host and negotiated group.

### 14.7 Automation and scope

Automated checks are still checks: they need to be inside written scope, run at agreed times and stop if a target behaves unexpectedly. Keep the target list in the repository, reviewed like code, so nobody adds an out-of-scope host by accident.

### 14.8 Common errors and limits

- Promoting a stage on a small, lucky sample.
- Scripts with embedded secrets.
- Unreviewed target lists.
### 14.9 Alert quality

An alert that fires every night for a known, accepted exception teaches operators to ignore alerts. Suppress known exceptions explicitly, with an expiry date that matches the exception record, and review suppressions monthly. Each alert should link to its runbook so the person woken at 03:00 knows what to do first.

### Exercises

- **EX040 — Stage decision.** Using Lab K, explain why the first canary is held. Rubric: 3 = upper bound above budget due to small sample.
- **EX041 — Diff alert.** Describe how a nightly diff detects silent fallback. Rubric: 3 = compare negotiated group per host, alert on hybrid→classical.
- **EX042 — Script hygiene.** List four features of a maintainable check script. Rubric: 3 = version control, README, clear errors, test.

### Synthesis

Automation runs routine checks, gates rollout stages with confidence bounds, re-checks after patches and stays within scope and maintainable.

### Continue studying — chapter 14 of 18

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Quantum and post-quantum security: integration and dependencies

### Learning outcomes

You will (1) trace a flow across all hops; (2) identify who controls each hop; (3) prepare vendor and partner requests; and (4) understand agility through policy rather than code.

### 15.1 Every hop counts

A booking from a travel agency reaches HHG through the agency's system, the file-exchange server, an internal processor and the reservations database. Each hop negotiates separately. A hybrid connection at one hop says nothing about the next.

### 15.2 Controllers

Write who controls each hop: HHG operations, a vendor, a cloud provider or a partner. HHG can change its own servers; for the rest it can only ask, require in contracts or route around.

### 15.3 Requests

A good vendor or partner request names the product and version, asks which post-quantum algorithms and protocols are supported, by which version and date, and asks for a test system. Record answers as vendor evidence until verified.

### 15.4 Practical activity — Lab A

```python
# Lab A (ch 15): crypto-agility through a policy-driven registry instead of hard-coded algorithms.
import hashlib, hmac
REGISTRY = {"hmac-sha256": lambda k, m: hmac.new(k, m, hashlib.sha256).digest(),
            "hmac-sha3-256": lambda k, m: hmac.new(k, m, hashlib.sha3_256).digest()}
POLICY = {"tag-algorithm": "hmac-sha256", "accept": ["hmac-sha256", "hmac-sha3-256"]}
def protect(key, msg):
    alg = POLICY["tag-algorithm"]; return alg, REGISTRY[alg](key, msg)
def check(key, msg, alg, tag):
    if alg not in POLICY["accept"]: return False            # algorithm identifier is authenticated by policy
    return hmac.compare_digest(REGISTRY[alg](key, msg), tag)
k, m = b"k" * 32, b"guest folio 42"
a1, t1 = protect(k, m)
POLICY["tag-algorithm"] = "hmac-sha3-256"                   # migration = one policy change
a2, t2 = protect(k, m)
print("old tag still verifies during transition:", check(k, m, a1, t1))
print("new tag verifies:", check(k, m, a2, t2), "| algorithms:", a1, "->", a2)
POLICY["accept"] = ["hmac-sha3-256"]                        # retire the old algorithm
print("old tag after retirement:", check(k, m, a1, t1))
```

Expected output:

```text
old tag still verifies during transition: True
new tag verifies: True | algorithms: hmac-sha256 -> hmac-sha3-256
old tag after retirement: False
```

Systems that read algorithm choices from policy can change them without code changes. When you ask vendors about readiness, ask whether algorithms are configurable.

### 15.5 Worked example

The channel SFTP flow: travel agency client (partner) → HHG SFTP server (HHG) → internal processor (HHG) → reservations DB (HHG, managed service). After upgrading OpenSSH and enabling hybrid KEX, 5 of 9 agencies negotiate hybrid; four use old clients. HHG sends them a notice with a test endpoint and a twelve-month window.

### 15.6 Hands-on activity

Trace one HHG flow with all hops and controllers and draft one vendor request.

### 15.7 Tracking dependencies

Keep a simple dependency list: hop, controller, request sent, answer, evidence grade, next follow-up date. Review it monthly. Dependencies that never get answered are risks to raise with your manager, not tasks to forget.

### 15.8 Common errors and limits

- Judging a flow by one hop.
- Treating vendor claims as facts.
- No follow-up on unanswered requests.
### 15.9 Routing around a dependency

When a controller cannot or will not change soon, sometimes HHG can protect the data another way: move the sensitive part of a transfer to a channel HHG controls, reduce what is sent, or terminate a hybrid connection at an HHG gateway close to the partner. Each workaround needs approval and an entry in the exception register, because it changes the service design.

### Exercises

- **EX043 — Hop list.** List the hops and controllers for the guest portal flow. Rubric: 3 = client, CDN/LB, app, DB with controllers.
- **EX044 — Vendor request.** Write a four-question vendor request for the door-lock hub. Rubric: 3 = algorithms, protocols, version/date, test system.
- **EX045 — Agility question.** Why ask vendors whether algorithms are configurable? Rubric: 3 = future change without replacement.

### Synthesis

Integration means every hop and its controller; operators send precise requests, track answers and favour configurable products.

### Continue studying — chapter 15 of 18

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Technical documentation and safety

### Learning outcomes

You will (1) write runbooks for post-quantum operations; (2) document configuration baselines; (3) follow safety and authorization rules; and (4) keep documentation current.

### 16.1 Runbooks

A runbook says: when to use it (symptoms), what to check, safe actions, rollback, how to confirm, who to call. Write runbooks for hybrid share drops, large-handshake timeouts, no shared group, and certificate verification errors.

### 16.2 Baselines

A configuration baseline lists the approved settings for each service type: TLS versions, groups and order, SSH `KexAlgorithms`, certificate types, logging fields. Store it in version control; changes go through review.

### 16.3 Safety and authorization

Never run active tests on production without written approval; never try to force downgrades outside the isolated lab; never handle keys outside approved tools; report exposed keys immediately. Label synthetic data as such in all documents and training material.

### 16.4 Keeping documents current

Review runbooks after every incident and every major change. Put a "last reviewed" date and owner at the top. Remove steps that no longer apply.

### 16.5 Worked example

HHG runbook "Hybrid share drop on a TLS service": symptoms — dashboard alert, hybrid share below 50 %; checks — last change on the service, current TLS profile vs baseline; actions — re-apply baseline profile on the affected listener; rollback — previous profile from version control; confirm — hybrid share recovers within 30 minutes; call — Web Ops on-call, then platform lead. Last reviewed 2 October; owner Web Ops.

### 16.6 Hands-on activity

Write a runbook for "No shared group on SFTP" using the format above.

### 16.7 Writing for the night shift

Runbooks are read under pressure, often at night. Use short numbered steps, exact commands, expected outputs and clear stop points ("if the share has not recovered after step 4, call the platform lead"). Avoid long explanations in the steps; link to background instead.

### 16.8 Common errors and limits

- Runbooks without rollback.
- Baselines kept only in someone's head.
- Out-of-date documents.
### 16.9 Sharing documentation

Store runbooks and baselines where on-call staff can reach them during an outage — not only in a system that might itself be down. Many teams keep a read-only copy in a second location. Mark documents that contain sensitive configuration detail and restrict them accordingly, while keeping general procedures widely readable.

### Exercises

- **EX046 — Runbook.** Write the "no shared group" runbook. Rubric: 3 = symptoms, checks, actions, rollback, confirm, contacts.
- **EX047 — Baseline.** List five items in a TLS baseline. Rubric: 3 = versions, groups/order, cert types, logging, cipher suites.
- **EX048 — Safety rule.** Explain why downgrade tests belong only in the lab. Rubric: 3 = risk to production sessions, authorization.

### Synthesis

Runbooks, baselines and safety rules turn individual skill into reliable team operations; documents stay useful only when owned and reviewed.

### Continue studying — chapter 16 of 18

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Contained laboratory II

### Learning outcomes

You will (1) run a multi-hop lab with monitoring; (2) inject and diagnose failures; (3) practise runbooks under time pressure; and (4) debrief and improve documents.

### 17.1 Lab layout

Client → reverse proxy → web server, plus an SSH server, all hybrid-capable; a log parser feeding a simple dashboard; a "legacy" client; and a proxy that can be set to drop large first messages.

### 17.2 Scenarios

The instructor (or a teammate) injects one failure at a time: reorder groups on the proxy; restrict the proxy buffer; remove classical fallback on SSH; replace the server certificate with one from an untrusted lab root. You diagnose with logs and tools and fix using runbooks.

### 17.3 Timing

Record time to detect, time to diagnose and time to fix. The goal is not speed for its own sake but finding which steps of the runbook slowed you down.

### 17.4 Debrief

After each scenario: what happened, what you did, what helped, what to change in the runbook or dashboard. Update the documents immediately.

### 17.5 Worked example

Scenario 2 (proxy buffer): detection 3 minutes (timeouts in logs), diagnosis 11 minutes (operator first suspected the server), fix 2 minutes (proxy setting restored). Debrief: add "check proxy before server when timeouts appear on one path" to the runbook; add per-path panels to the dashboard.

### 17.6 Hands-on activity

Run all four scenarios; record times and debrief notes.

### 17.7 Working as a pair

Practise in pairs: one operator drives, the other reads the runbook and records times and observations. Swap roles each scenario. Pairing exposes unclear steps quickly and mirrors how incidents are handled on real on-call rotations.

### 17.8 Common errors and limits

- Skipping debriefs.
- Fixing without diagnosing.
- Not updating documents after lessons.
### 17.9 Recording the exercise

Keep a short log of each lab session — date, scenarios, times, debrief actions and who took part — in the team repository. Over several sessions the log shows whether detection and fix times are improving and which runbooks have changed as a result. It is also evidence for supervisors and auditors that the team practises its procedures rather than merely writing them.

### Exercises

- **EX049 — Scenario plan.** Design a fifth scenario for the lab. Rubric: 3 = realistic injection, expected symptom, fix.
- **EX050 — Timing analysis.** In the worked example, which phase took longest and how would you shorten it? Rubric: 3 = diagnosis; runbook ordering/panels.
- **EX051 — Certificate scenario.** What symptom and fix do you expect for the untrusted lab root scenario? Rubric: 3 = verification error; add root or restore trusted cert.

### Synthesis

Multi-hop labs with injected failures and timed, debriefed runbook practice build operators who can find and fix problems quickly and improve their tools.

### Continue studying — chapter 17 of 18

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Supervised technical project

### Learning outcomes

You will (1) plan and complete a supervised operations project; (2) apply checks, configuration, verification and documentation end to end; (3) report results with evidence; and (4) hand over to the team.

### 18.1 Project choices

Examples: enable and verify hybrid key exchange on one service in staging and production under supervision; build the negotiated-group dashboard for a set of services; write and test runbooks for post-quantum failure modes; build the CBOM for one property.

### 18.2 Plan

Scope and authorization; steps with evidence for each; risks and rollback; timeline; supervisor checkpoints.

### 18.3 Execution

Follow change control; save evidence; verify from both sides; update documents. Ask for help early when blocked.

### 18.4 Report and handover

Report: aim, what was done, evidence, results, remaining issues and recommendations. Handover: runbooks, scripts, dashboards and the list of open items, each with an owner.

### 18.5 Worked example

Project (synthetic): "Hybrid SSH for channel SFTP." Steps: upgrade OpenSSH in staging; configure `KexAlgorithms`; test six agency client types; production change under ticket; verify; dashboard panel for KEX share; runbook for "no shared group"; partner notice. Results: 5 of 9 agencies hybrid after a month; four on notice. Handover to Network Ops with open items for the four agencies.

### 18.6 Hands-on activity

Write your project plan and get it approved by your supervisor.

### 18.7 Reflecting on the project

Finish with a short reflection: what went as planned, what surprised you, which skill you used most, and what you would do differently. Share it with your supervisor; it is often the most useful input for the next trainee's project.

### 18.8 Common errors and limits

- Starting without approval.
- Reports without evidence.
- Handovers without owners.
### 18.9 Assessment

Your supervisor will assess the project on: staying within scope; quality of evidence; correctness of configuration (hybrid preferred with controlled fallback); verification from both sides with a negative control; usefulness of the documentation; and the handover. Before the assessment, check each item yourself and link the evidence. Being able to show where each piece of evidence lives is part of the skill being assessed.

Finally, present the project to your team in ten minutes: the problem, what you changed, the evidence, what remains and who owns it. Short, factual presentations of completed work are how operators build trust with the teams whose systems they change.

### Exercises

- **EX052 — Plan.** Write a one-page plan for the dashboard project. Rubric: 3 = scope, steps with evidence, risks, timeline, checkpoints.
- **EX053 — Results.** Express "5 of 9 agencies" as a percentage and state what remains. Rubric: 3 = 56 %, four agencies on notice.
- **EX054 — Handover list.** List five handover items. Rubric: 3 = runbooks, scripts, dashboards, open items, owners.

### Synthesis

A supervised project puts every hands-on skill together — scope, configuration, verification, documentation and handover — and leaves the team better equipped.

### Continue studying — chapter 18 of 18

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers; any answer meeting the rubric scores equally. Numbers about HHG are synthetic.

**EX001.** Guest portal TLS: configuration (HHG ops). File-exchange SSH: package upgrade then configuration (HHG ops). Site VPN: vendor firmware (network vendor). POS to processor: vendor/processor update. Door-lock firmware signing: hardware refresh (lock vendor).

**EX002.** "Someone could secretly record our encrypted guest data today and keep it until future quantum computers can unlock it. Because passport details must stay private for years, we are updating how our systems agree secret keys now."

**EX003.** Replace RSA and ECDH (Shor's algorithm breaks them). Keep AES-256 (Grover leaves ~128-bit work) and SHA-256 (no practical quantum break).

**EX004.** TLS: (EC)DHE or hybrid group / certificate signatures. SSH: KEX algorithm / host and user keys. IPsec (IKEv2): Diffie–Hellman plus additional key exchanges / certificates or pre-shared keys.

**EX005.** Not hybrid (`curve25519-sha256` is classical). Check the server's `KexAlgorithms` order and both client and server OpenSSH versions.

**EX006.** 1,216 − 32 = 1,184 bytes (the ML-KEM-768 encapsulation key).

**EX007.** `openssl version` (host and inside containers), `ssh -V`, and the application runtime version (Java/Go) or container image SBOM.

**EX008.** Operating-system trust store; Java truststore; application or container CA bundles (also appliance trust lists).

**EX009.** Stop; do not open, copy or test the key; report immediately via the security process; record where and when you saw it.

**EX010.** 2 of 5 = 40 %.

**EX011.** Required fields present; values of allowed type/known algorithm names (or null → unknown); duplicate host entries detected.

**EX012.** "Find the TLS/key-exchange algorithms used by the Summit lock hub (model, firmware). Method: vendor documentation request and configuration export. Owner: Summit property IT with the lock vendor. Due: 30 days."

**EX013.** Which systems; which methods; which times; who to contact if something goes wrong.

**EX014.** Exact command; target; date and time; saved output; tool and version (plus scope reference).

**EX015.** "On (date/time), configuration export of the Harbour site VPN (ticket ref) shows IKEv2 with ECDH group 19 only and no additional ML-KEM key exchange. Guest records (7-year confidentiality) cross this tunnel, so recorded traffic could be decrypted by a future quantum computer. Recommendation: ask the vendor for RFC 9370 hybrid support and date. Owner: Network Ops."

**EX016.** Guest portal TLS: record-now. Lock firmware signing: forge-later. AES-256 backups: fine for now. Unknown sensor: unknown.

**EX017.** The guest portal/booking API TLS on the load balancer: operations controls the configuration, the change is quick, and it carries 7-year guest data.

**EX018.** 7 + 2 = 9 years: at risk under any assumed timeline shorter than 9 years.

**EX019.** Logs (or client tool output): they record what was actually negotiated; configuration only shows what is offered; vendor sheets are claims.

**EX020.** Five uses on four assets (booking-gateway, door-lock-hub ×2, reservations-db, property-vpn).

**EX021.** "Booking API 88 % hybrid (LB logs, all data-centre listeners); guest portal 3 % (LB logs); file exchange 0 % (sshd logs); property VPNs 0/12 (configuration only); locks and minibar sensors unknown (no source)."

**EX022.** Timeouts through one proxy → large handshake dropped. "No shared group" → no common algorithm. Share drops, no errors → silent fallback.

**EX023.** Collect evidence (time, client, path, error, firewall model); route that property's affected subnet to a compatible listener as a recorded exception; escalate to the firewall owner/vendor.

**EX024.** "After any load-balancer firmware update, re-apply the approved TLS profile and confirm hybrid share on the dashboard within 30 minutes."

**EX025.** Hybrid preferred → tool reports hybrid; hybrid offered after classical → tool reports classical negotiated (and ideally the offer); classical only → tool reports classical. Tool must distinguish all three.

**EX026.** 15,524 / 1,290 ≈ 12 times.

**EX027.** Confirm scope; record tool and version; run the check; save the output; compare with expected; record finding or "as expected".

**EX028.** `X25519MLKEM768:X25519:secp256r1`

**EX029.** `KexAlgorithms mlkem768x25519-sha256,sntrup761x25519-sha512@openssh.com,curve25519-sha256`

**EX030.** What: enable hybrid KEX on channel-sftp. Why: 7-year booking data, record-now risk. When: Tuesday 06:00. Risk: old agency clients — fallback kept. Test evidence: staging `ssh -v` outputs for six clients. Rollback: restore previous sshd_config from version control and reload. Approver: Network Ops lead.

**EX031.** Client: tool output showing the negotiated group. Server: access/TLS logs with the group field.

**EX032.** In staging, remove `mlkem768x25519-sha256` from `KexAlgorithms`; the check must report classical; restore and re-check.

**EX033.** Run the client check against in-scope services; check dashboard/logs for hybrid share; compare with the pre-patch baseline and alert on differences.

**EX034.** Server VM (current OpenSSL ≥ 3.5, current OpenSSH); current client VM (same); old client VM (older OpenSSL/OpenSSH); isolated network; versions recorded.

**EX035.** Put the classical group first in the server's list (`X25519:X25519MLKEM768`); connect with the current client and observe X25519 negotiated although hybrid is offered.

**EX036.** Purpose; environment; steps; results; interpretation; lessons.

**EX037.** The proxy timeouts: three of six failures, a shared path and a clear pattern (large ClientHello), affecting a whole site.

**EX038.** Route Summit's front-desk subnet to a listener without the hybrid group, recorded as an exception with owner and expiry tied to the firewall update.

**EX039.** "Product: firewall model X, firmware 5.2.1 at Summit. Evidence: TLS ClientHello of 1,530 bytes dropped (lab reproduction attached). Request: fix or configuration guidance and target release date."

**EX040.** 3/5,000 has a Wilson upper bound of about 0.18 %, above the 0.09 % budget; the sample is too small to show safety.

**EX041.** Store each night's negotiated group per host; diff with the previous night; alert when any host changes from hybrid to classical.

**EX042.** Version control; README; clear error messages; a test with known input (also: no embedded secrets).

**EX043.** Guest device (guest) → CDN or load balancer (HHG or CDN provider) → portal application (HHG) → reservations DB (HHG/managed provider).

**EX044.** Which algorithms does the hub use for key exchange and firmware signing? Does it support post-quantum or hybrid key exchange, in which protocol? From which firmware version and date? Can we get a test unit or test system?

**EX045.** Configurable products can switch algorithms by policy later (including future changes), avoiding hardware replacement or code changes.

**EX046.** Symptoms: partner reports "no shared group". Checks: partner client version; current sshd `KexAlgorithms`; recent changes. Actions: restore approved list with classical fallback. Rollback: previous config. Confirm: partner connects; KEX in logs. Contacts: Network Ops on-call, partner contact.

**EX047.** TLS versions (1.3, 1.2 if needed); groups and order; certificate type; logging fields (protocol, cipher, group); cipher suites.

**EX048.** Downgrade tests can break or weaken real sessions for guests and partners, and require explicit authorization; an isolated lab avoids harm.

**EX049.** Example: set the server to hybrid-only and connect with the legacy client — symptom "no shared group"; fix: restore classical fallback.

**EX050.** Diagnosis (11 minutes); shorten by ordering runbook checks (proxy before server on single-path timeouts) and adding per-path dashboard panels.

**EX051.** Symptom: certificate verification error on clients; fix: add the lab root to the client trust store (if intended) or restore the trusted certificate.

**EX052.** Scope: list of services and log sources, approval. Steps: add log fields (staging evidence), parser, dashboard panels, alerts. Risks: log volume — staged rollout. Timeline: four weeks. Checkpoints: weekly with supervisor.

**EX053.** 5/9 ≈ 56 %; four agencies remain on classical, under notice with a twelve-month window.

**EX054.** Runbooks; scripts; dashboards; list of open items; named owners for each.

## Eighteen-subject teaching route

This is the **technical** course for hands-on operators, following the synthetic **Halden Hotel Group (HHG)** through checks, configuration, verification, troubleshooting, automation, documentation and contained labs.

## References

Links checked 12 October 2026; standards status changes, so re-verify.

- Bernstein, D. J., et al. (2024). KyberSlash. IACR ePrint 2024/1049. <https://eprint.iacr.org/2024/1049>
- IETF RFCs: 9370 (multiple key exchanges in IKEv2), 9794 (PQ/T hybrid terminology), 10024 (hybrid TLS 1.3 groups). <https://www.rfc-editor.org/>
- Mosca, M. (2018). Cybersecurity in an era with quantum computers: will we be ready? *IEEE Security & Privacy* 16(5). <https://doi.org/10.1109/MSP.2018.3761723>
- NIST FIPS 203, 204, 205 (2024). <https://doi.org/10.6028/NIST.FIPS.203> · <https://doi.org/10.6028/NIST.FIPS.204> · <https://doi.org/10.6028/NIST.FIPS.205>
- NIST SP 800-208 (2020); SP 800-227 (2025); IR 8547 initial public draft (2024). <https://doi.org/10.6028/NIST.SP.800-208> · <https://doi.org/10.6028/NIST.SP.800-227> · <https://doi.org/10.6028/NIST.IR.8547.ipd>
- OpenSSH release notes. <https://www.openssh.com/releasenotes.html>
- OpenSSL 3.5 NEWS. <https://github.com/openssl/openssl/blob/openssl-3.5/NEWS.md>
- Shor, P. W. (1997). *SIAM J. Computing* 26(5), 1484–1509. <https://doi.org/10.1137/S0097539795293172>
