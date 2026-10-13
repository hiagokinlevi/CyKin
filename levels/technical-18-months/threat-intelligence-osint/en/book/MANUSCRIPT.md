# Threat Intelligence and OSINT: A Technical Course Book

- Language: English (`en`); technical course, eighteen months.
- Editorial state: **draft**. Chapters 1–18 of 18 have hand-written teaching text; exercises EX001–EX072 have matching worked results with 0–3 rubrics; three offline labs use only the Python 3 standard library on synthetic data, with outputs embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technical-course students preparing for practical cyber threat intelligence (CTI) support work in IT and security teams.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical boundary: no collection on real private individuals, no terms-of-service evasion, no deanonymisation, no contact with adversary infrastructure. Organisations, people and indicators are **synthetic** unless a sentence cites a public source; addresses use RFC 5737 ranges and domains use `.example`.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Chapters 1–5 build service, network, identity, scripting and evidence foundations (with an email-authentication lab). Chapters 6–12 teach the CTI system model, data and telemetry, failure modes, tools, control configuration, verification and a contained laboratory on enriching matches with asset owners. Chapters 13–18 cover troubleshooting, automation, integration, documentation and safety, a second contained laboratory on weekly summaries with TLP filtering, and a supervised project. Each chapter has outcomes, teaching, a worked example, a labelled synthetic case, errors and limits, four exercises scored 0–3, a synthesis and a **Continue studying** block.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Ashgrove College** — a further-education college with campuses, a learning platform, library and finance office | Organisation served by CTI | Invented |
| **Tomás Reyes** | Technical-course student on placement in the college IT security team | Invented |
| **Education Security Exchange (ESX)** | Community of colleges and universities sharing intelligence under TLP 2.0 | Invented |

### Core sources

MITRE [ATT&CK](https://attack.mitre.org/); OASIS [STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html) and [TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/taxii-v2.1.html); [Diamond Model](https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf); Hutchins et al. [kill chain](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf); NIST [SP 800-150](https://doi.org/10.6028/NIST.SP.800-150); FIRST [TLP 2.0](https://www.first.org/tlp/); [ICD 203](https://www.odni.gov/files/documents/ICD/ICD-203.pdf). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) |
| [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Computing and service architecture

### Learning outcomes

You will (1) describe the services a college runs and how they connect; (2) mark which services are internet-facing; (3) find where each service keeps logs; (4) explain why architecture knowledge makes intelligence usable.

### 1.1 College services

Ashgrove College runs a learning platform used by 6,000 students, staff and student email, a library catalogue, a finance system, a student-records database, Wi-Fi for campus visitors and a website. Some are hosted on campus servers, others by cloud suppliers.

Section one point one develops computing and service architecture with a Ashgrove College note Tomás Reyes can demo offline.

Under section one point one, ESX expects computing claims to carry owners and dates.

Section one point one treats college services exposure logs as testable only when evidence and ticket IDs are recorded.

### 1.2 Exposure

The learning platform, email, website and remote-access gateway are reachable from the internet. Exploit Public-Facing Application (T1190) and Phishing (T1566) are therefore the first ATT&CK techniques Tomás reads about. The finance system is internal only, but reachable from staff desktops.

Section one point two develops computing and service architecture with a Ashgrove College note Tomás Reyes can demo offline.

Under section one point two, ESX expects computing claims to carry owners and dates.

Section one point two treats college services exposure logs as testable only when evidence and ticket IDs are recorded.

### 1.3 Logs and owners

Each service has an owner and logs: the email gateway logs messages; the remote-access gateway logs connections; the learning platform logs logins. Tomás builds a table with service, owner, log location, retention and who can search it.

Section one point three develops computing and service architecture with a Ashgrove College note Tomás Reyes can demo offline.

Under section one point three, ESX expects computing claims to carry owners and dates.

Section one point three treats college services exposure logs as testable only when evidence and ticket IDs are recorded.

### 1.4 Dependencies

The learning platform depends on the directory for logins. If attackers steal directory credentials, they reach every service that trusts it.

Section one point four develops computing and service architecture with a Ashgrove College note Tomás Reyes can demo offline.

Under section one point four, ESX expects computing claims to carry owners and dates.

Section one point four treats college services exposure logs as testable only when evidence and ticket IDs are recorded.

For section one point four, Ashgrove College will not accept computing work without a written trail.

### 1.5 Supplier-hosted services

Cloud email logs sit with the supplier. Ashgrove's contract allows downloading sign-in logs for 30 days; older ones are gone. Tomás notes that limit, because intelligence about last quarter's attacks cannot be checked there.

Section one point five develops computing and service architecture with a Ashgrove College note Tomás Reyes can demo offline.

Under section one point five, ESX expects computing claims to carry owners and dates.

Section one point five treats college services exposure logs as testable only when evidence and ticket IDs are recorded.

### 1.6 Students as users

Students use personal devices on campus Wi-Fi. The college cannot install agents on them, so intelligence about malware on student laptops leads to network controls and advice, not endpoint rules.

Section one point six develops computing and service architecture with a Ashgrove College note Tomás Reyes can demo offline.

Under section one point six, ESX expects computing claims to carry owners and dates.

Section one point six treats college services exposure logs as testable only when evidence and ticket IDs are recorded.

### 1.7 A service diagram

A one-page diagram showing services, users, internet exposure and log locations helps everyone place an advisory quickly.

Section one point seven develops computing and service architecture with a Ashgrove College note Tomás Reyes can demo offline.

Under section one point seven, ESX expects computing claims to carry owners and dates.

Section one point seven treats college services exposure logs as testable only when evidence and ticket IDs are recorded.

For section one point seven, Ashgrove College will not accept computing work without a written trail.

### Worked example

ESX shares an advisory about attacks on a learning-platform plugin. Tomás checks the service table: Ashgrove's platform is internet-facing, uses the plugin and has an owner in the e-learning team. He sends the advisory to that owner with the version number, marked TLP:GREEN, within the hour.

> **Synthetic case.** Ashgrove College and the advisory are invented.

### Errors and limits

Diagrams drift; review them each term.

### Exercises

- **EX001 — First techniques.** Which two ATT&CK techniques match Ashgrove's internet-facing services first, and why? *Rubric:* 3 = T1190 and T1566 with reasons; 2 = names; 1 = one; 0 = none.
- **EX002 — Log retention gap.** Why can't Tomás check last quarter's attacks in cloud email sign-in logs? *Rubric:* 3 = 30-day retention by contract; 2 = partial; 1 = no access at all; 0 = none.
- **EX003 — Directory dependency.** Why does stolen directory access matter so much? *Rubric:* 3 = all services trusting directory become reachable; 2 = partial; 1 = only directory affected; 0 = none.
- **EX004 — Student devices.** What kind of controls follow from malware intelligence about student laptops? *Rubric:* 3 = network controls and advice, not endpoint agents; 2 = partial; 1 = install agents; 0 = none.

### Synthesis

Map services, exposure, owners, logs and dependencies so each intelligence item finds its target quickly.

### Continue studying — chapter 01 of 18

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Networks and protocols

### Learning outcomes

You will (1) explain DNS, HTTPS and SMTP as sources of intelligence matches; (2) read firewall and proxy log fields; (3) recognise address translation effects; (4) describe Application Layer Protocol abuse.

### 2.1 DNS

Every connection by name begins with a DNS lookup. Ashgrove's resolvers log client address, name and time. Because students' devices also use them, DNS logs cover devices the college cannot otherwise see.

Section two point one develops networks and protocols with a Ashgrove College note Tomás Reyes can demo offline.

Under section two point one, ESX expects networks claims to carry owners and dates.

Section two point one treats dns https and the as testable only when evidence and ticket IDs are recorded.

### 2.2 HTTPS and the proxy

Staff web traffic goes through a proxy that records destination name, bytes and category. With encryption, the proxy sees the server name but not page content, unless inspection is enabled — which Ashgrove has not done for privacy and legal reasons.

Section two point two develops networks and protocols with a Ashgrove College note Tomás Reyes can demo offline.

Under section two point two, ESX expects networks claims to carry owners and dates.

Section two point two treats dns https and the as testable only when evidence and ticket IDs are recorded.

### 2.3 SMTP

Mail servers exchange messages over SMTP. The gateway records sender, recipient, subject, attachment names and authentication results.

Section two point three develops networks and protocols with a Ashgrove College note Tomás Reyes can demo offline.

Under section two point three, ESX expects networks claims to carry owners and dates.

Section two point three treats dns https and the as testable only when evidence and ticket IDs are recorded.

For section two point three, Ashgrove College will not accept networks work without a written trail.

### 2.4 Firewall logs

Firewall entries show source, destination, port, action and time. They are useful for checking addresses from intelligence feeds.

Section two point four develops networks and protocols with a Ashgrove College note Tomás Reyes can demo offline.

Under section two point four, ESX expects networks claims to carry owners and dates.

Section two point four treats dns https and the as testable only when evidence and ticket IDs are recorded.

For section two point four, Ashgrove College will not accept networks work without a written trail.

### 2.5 Address translation

Campus Wi-Fi translates many student devices to a few public addresses. Externally, one address represents thousands of people; internally, the translation log maps back to a device for a given time.

Section two point five develops networks and protocols with a Ashgrove College note Tomás Reyes can demo offline.

Under section two point five, ESX expects networks claims to carry owners and dates.

Section two point five treats dns https and the as testable only when evidence and ticket IDs are recorded.

### 2.6 Protocol abuse

Application Layer Protocol (T1071) describes attackers hiding command traffic in web, DNS or mail protocols so it blends in. Unusual regular connections to a rare domain are a clue worth checking.

Section two point six develops networks and protocols with a Ashgrove College note Tomás Reyes can demo offline.

Under section two point six, ESX expects networks claims to carry owners and dates.

Section two point six treats dns https and the as testable only when evidence and ticket IDs are recorded.

### 2.7 Time zones

Logs from cloud suppliers use UTC; campus devices use local time. Convert before correlating.

Section two point seven develops networks and protocols with a Ashgrove College note Tomás Reyes can demo offline.

Under section two point seven, ESX expects networks claims to carry owners and dates.

Section two point seven treats dns https and the as testable only when evidence and ticket IDs are recorded.

For section two point seven, Ashgrove College will not accept networks work without a written trail.

### Worked example

ESX shares an address used for command traffic. The firewall shows two connections from a public Wi-Fi address. Tomás uses the translation log and the timestamps (converted to UTC) to identify one student laptop. He gives the device identifier to the network team, who block it from Wi-Fi and email the student advice through the help desk; no one inspects the student's personal device.

> **Synthetic case.** The address and device are invented.

### Errors and limits

Translation logs are kept briefly; delays lose the mapping.

### Exercises

- **EX005 — DNS coverage.** Why do DNS logs cover devices the college cannot otherwise monitor? *Rubric:* 3 = student devices use campus resolvers; 2 = partial; 1 = they don't; 0 = none.
- **EX006 — Translation mapping.** How did Tomás link a public address to one laptop? *Rubric:* 3 = translation log + UTC-converted timestamps; 2 = partial; 1 = guessed; 0 = none.
- **EX007 — Hidden channel.** What does T1071 describe, and what clue may reveal it? *Rubric:* 3 = command traffic in normal protocols; regular connections to rare domain; 2 = one; 1 = wrong; 0 = none.
- **EX008 — Personal device limit.** Why didn't anyone inspect the student's laptop? *Rubric:* 3 = personal device; no authority/privacy; network block + advice instead; 2 = partial; 1 = should inspect; 0 = none.

### Synthesis

Use DNS, proxy, mail and firewall logs, handle address translation and time zones, and respect limits on personal devices.

### Continue studying — chapter 02 of 18

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Operating systems and identities

### Learning outcomes

You will (1) relate account and process activity to ATT&CK; (2) search sign-in records for intelligence matches; (3) explain privileged-account risk; (4) handle credential notices correctly.

### 3.1 Accounts

Students, staff, contractors and service accounts all authenticate through the directory. Valid Accounts (T1078) — attackers using real credentials — is common in education because student passwords are often reused.

Section three point one develops operating systems and identities with a Ashgrove College note Tomás Reyes can demo offline.

Under section three point one, ESX expects operating claims to carry owners and dates.

Section three point one treats accounts sign-in records privileged as testable only when evidence and ticket IDs are recorded.

For section three point one, Ashgrove College will not accept operating work without a written trail.

### 3.2 Sign-in records

The directory logs user, time, source address, application and result. Tomás searches for successful sign-ins from addresses shared by ESX as attack sources.

Section three point two develops operating systems and identities with a Ashgrove College note Tomás Reyes can demo offline.

Under section three point two, ESX expects operating claims to carry owners and dates.

Section three point two treats accounts sign-in records privileged as testable only when evidence and ticket IDs are recorded.

For section three point two, Ashgrove College will not accept operating work without a written trail.

### 3.3 Privileged accounts

IT administrators hold accounts that can change any system. Intelligence about attackers targeting administrators justifies separate admin accounts, stronger authentication and no email on admin accounts.

Section three point three develops operating systems and identities with a Ashgrove College note Tomás Reyes can demo offline.

Under section three point three, ESX expects operating claims to carry owners and dates.

Section three point three treats accounts sign-in records privileged as testable only when evidence and ticket IDs are recorded.

For section three point three, Ashgrove College will not accept operating work without a written trail.

### 3.4 Processes

On staff machines, endpoint agents log process starts. Reports about attackers running scripts (T1059) are checked against these logs by the endpoint team.

Section three point four develops operating systems and identities with a Ashgrove College note Tomás Reyes can demo offline.

Under section three point four, ESX expects operating claims to carry owners and dates.

Section three point four treats accounts sign-in records privileged as testable only when evidence and ticket IDs are recorded.

For section three point four, Ashgrove College will not accept operating work without a written trail.

### 3.5 Credential notices

When ESX reports Ashgrove addresses in a password dump, Tomás never tries the passwords. He sends the list to the identity team in a restricted ticket; they reset and notify users.

Section three point five develops operating systems and identities with a Ashgrove College note Tomás Reyes can demo offline.

Under section three point five, ESX expects operating claims to carry owners and dates.

Section three point five treats accounts sign-in records privileged as testable only when evidence and ticket IDs are recorded.

### 3.6 Student privacy

Sign-in data about students is personal data. Searches are tied to a specific intelligence item and recorded; no browsing of individual students' activity.

Section three point six develops operating systems and identities with a Ashgrove College note Tomás Reyes can demo offline.

Under section three point six, ESX expects operating claims to carry owners and dates.

Section three point six treats accounts sign-in records privileged as testable only when evidence and ticket IDs are recorded.

For section three point six, Ashgrove College will not accept operating work without a written trail.

### 3.7 Lockout and spraying

Password spraying tries a few common passwords across many accounts. Lockout settings and multi-factor authentication blunt it; intelligence about spraying against colleges supports tighter settings.

Section three point seven develops operating systems and identities with a Ashgrove College note Tomás Reyes can demo offline.

Under section three point seven, ESX expects operating claims to carry owners and dates.

Section three point seven treats accounts sign-in records privileged as testable only when evidence and ticket IDs are recorded.

For section three point seven, Ashgrove College will not accept operating work without a written trail.

### Contractor accounts

Contractors maintaining campus systems often keep accounts long after their work ends. A quarterly review with each contract manager disables accounts no longer needed and shortens the list of credentials attackers could use.

### Worked example

ESX shares four addresses used in spraying against colleges. Tomás finds 300 failed and two successful sign-ins at Ashgrove, both student accounts. The identity team resets both, revokes sessions and checks what was accessed: course materials only. Multi-factor authentication for students is moved up the plan.

> **Synthetic case.** The addresses and accounts are invented.

### Errors and limits

Address-based searches miss attackers using residential proxies.

### Exercises

- **EX009 — Why education.** Why is T1078 common in education? *Rubric:* 3 = student password reuse/many accounts; 2 = partial; 1 = no reason; 0 = none.
- **EX010 — Admin separation.** Give two controls for administrator accounts supported by intelligence. *Rubric:* 3 = separate admin accounts, strong MFA, no email; 2 = one; 1 = none; 0 = none.
- **EX011 — Search discipline.** How is student privacy protected during sign-in searches? *Rubric:* 3 = tied to intelligence item, recorded, no browsing; 2 = partial; 1 = none; 0 = none.
- **EX012 — Spray outcome.** What three actions followed the two successful spray logins? *Rubric:* 3 = reset, revoke sessions, check access (and MFA plan); 2 = two; 1 = one; 0 = none.

### Synthesis

Accounts are the main target; search sign-ins purposefully, protect admins, handle credential notices properly and respect student privacy.

### Continue studying — chapter 03 of 18

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Scripting and data formats

### Learning outcomes

You will (1) parse simple key-value data with Python; (2) read email authentication results; (3) handle JSON, CSV and STIX at a basic level; (4) write scripts that report clearly.

### 4.1 Formats

Intelligence arrives as CSV lists, JSON (including STIX 2.1 bundles), plain email and log lines with key=value pairs. Python's standard library reads all of them: `csv`, `json` and simple string splitting.

Section four point one develops scripting and data formats with a Ashgrove College note Tomás Reyes can demo offline.

Under section four point one, ESX expects scripting claims to carry owners and dates.

Section four point one treats formats authentication results reading as testable only when evidence and ticket IDs are recorded.

### 4.2 Authentication results

Mail gateways add an Authentication-Results header with SPF, DKIM and DMARC outcomes. DMARC passes only when the visible From domain aligns with an SPF or DKIM pass. A message failing DMARC that claims to come from the college deserves attention.

Section four point two develops scripting and data formats with a Ashgrove College note Tomás Reyes can demo offline.

Under section four point two, ESX expects scripting claims to carry owners and dates.

Section four point two treats formats authentication results reading as testable only when evidence and ticket IDs are recorded.

### Lab — reading authentication results

```python
"""Lab (ch 04): parse synthetic Authentication-Results headers and flag messages failing DMARC."""
msgs = [("M1", "fees@ashgrove.example", "spf=pass dkim=pass dmarc=pass"),
        ("M2", "fees@ashgrove-payments.example", "spf=pass dkim=none dmarc=fail"),
        ("M3", "it-helpdesk@ashgrove.example", "spf=fail dkim=fail dmarc=fail"),
        ("M4", "library@partner-uni.example", "spf=pass dkim=pass dmarc=pass")]
for mid, sender, ar in msgs:
    res = dict(kv.split("=") for kv in ar.split())
    flag = "SUSPECT" if res["dmarc"] != "pass" else "ok"
    print(mid, sender.split("@")[1], res, flag)
```

Run with `python3 lab_headers.py`. Verified output:

```text
M1 ashgrove.example {'spf': 'pass', 'dkim': 'pass', 'dmarc': 'pass'} ok
M2 ashgrove-payments.example {'spf': 'pass', 'dkim': 'none', 'dmarc': 'fail'} SUSPECT
M3 ashgrove.example {'spf': 'fail', 'dkim': 'fail', 'dmarc': 'fail'} SUSPECT
M4 partner-uni.example {'spf': 'pass', 'dkim': 'pass', 'dmarc': 'pass'} ok
```

### 4.3 Reading the result

M1 and M4 pass all checks. M2 comes from ashgrove-payments.example, a lookalike; SPF passes for that domain but DMARC fails — flagged suspect. M3 claims the real ashgrove.example domain but fails everything — likely spoofed, flagged suspect.

Section four point three develops scripting and data formats with a Ashgrove College note Tomás Reyes can demo offline.

Under section four point three, ESX expects scripting claims to carry owners and dates.

Section four point three treats formats authentication results reading as testable only when evidence and ticket IDs are recorded.

### 4.4 Passing is not trust

M4 passes because partner-uni.example's records are correct; it shows the sender controls that domain, not that the message is safe. A compromised partner mailbox would also pass.

Section four point four develops scripting and data formats with a Ashgrove College note Tomás Reyes can demo offline.

Under section four point four, ESX expects scripting claims to carry owners and dates.

Section four point four treats formats authentication results reading as testable only when evidence and ticket IDs are recorded.

For section four point four, Ashgrove College will not accept scripting work without a written trail.

### 4.5 Clear output

Each line shows message, domain, parsed results and verdict. Anyone can check it without reading code.

Section four point five develops scripting and data formats with a Ashgrove College note Tomás Reyes can demo offline.

Under section four point five, ESX expects scripting claims to carry owners and dates.

Section four point five treats formats authentication results reading as testable only when evidence and ticket IDs are recorded.

For section four point five, Ashgrove College will not accept scripting work without a written trail.

### 4.6 Bad input

Malformed headers should produce "unparsed" with the raw text, not a crash.

Section four point six develops scripting and data formats with a Ashgrove College note Tomás Reyes can demo offline.

Under section four point six, ESX expects scripting claims to carry owners and dates.

Section four point six treats formats authentication results reading as testable only when evidence and ticket IDs are recorded.

For section four point six, Ashgrove College will not accept scripting work without a written trail.

Section four point six fails closed if scripting evidence is missing rather than guessing.

### 4.7 STIX basics

A STIX indicator object holds a pattern, a valid_from time and an id. Tomás reads bundles with `json.load` and prints each object's type and id before using any value.

Section four point seven develops scripting and data formats with a Ashgrove College note Tomás Reyes can demo offline.

Under section four point seven, ESX expects scripting claims to carry owners and dates.

Section four point seven treats formats authentication results reading as testable only when evidence and ticket IDs are recorded.

### Worked example

The finance office reports an invoice from ashgrove-payments.example. Tomás runs his parser on the saved header: DMARC fails, and the domain is a lookalike registered last week. He sends the sender domain to the email team for blocking and to ESX at TLP:GREEN without the staff recipient's name.

> **Synthetic case.** The messages are invented.

### Errors and limits

Headers added before the college gateway may be forged; trust only those added by Ashgrove's own gateway.

### Exercises

- **EX013 — Lab verdicts.** Which lab messages were suspect and why? *Rubric:* 3 = M2 lookalike DMARC fail; M3 spoofed all fail; 2 = one; 1 = wrong; 0 = none.
- **EX014 — Partner pass.** What does M4's pass prove, and what does it not? *Rubric:* 3 = sender controls domain; not message safety/compromise possible; 2 = partial; 1 = safe; 0 = none.
- **EX015 — Trusted headers.** Which authentication headers should Tomás trust? *Rubric:* 3 = those added by Ashgrove's gateway; others forgeable; 2 = partial; 1 = all; 0 = none.
- **EX016 — Malformed header.** How should the script treat a malformed header? *Rubric:* 3 = report unparsed with raw text, no crash; 2 = partial; 1 = crash/skip; 0 = none.

### Synthesis

Parse common formats with the standard library, read authentication results carefully and report clearly.

### Continue studying — chapter 04 of 18

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security scope and evidence

### Learning outcomes

You will (1) define the scope of CTI support work; (2) apply TLP 2.0 to everyday handling; (3) keep evidence with provenance; (4) avoid actions outside authorisation.

### 5.1 Scope

Tomás may: read intelligence from ESX and approved public sources, match indicators against college logs, draft notes and requests, and maintain the indicator list. He may not: block on production systems himself, contact attackers, visit suspicious sites from college devices, or share restricted material.

Section five point one develops security scope and evidence with a Ashgrove College note Tomás Reyes can demo offline.

Under section five point one, ESX expects security claims to carry owners and dates.

Section five point one treats scope tlp evidence and as testable only when evidence and ticket IDs are recorded.

### 5.2 TLP 2.0

CLEAR — public. GREEN — community, not public. AMBER — Ashgrove and its clients on a need-to-know basis. AMBER+STRICT — Ashgrove only. RED — named people only. Unlabelled material is treated as AMBER until the sender confirms.

Section five point two develops security scope and evidence with a Ashgrove College note Tomás Reyes can demo offline.

Under section five point two, ESX expects security claims to carry owners and dates.

Section five point two treats scope tlp evidence and as testable only when evidence and ticket IDs are recorded.

### 5.3 Evidence and provenance

Every item records source, date received, TLP, what the source based it on, and Tomás's checks. Exported log extracts used as evidence are saved with the ticket.

Section five point three develops security scope and evidence with a Ashgrove College note Tomás Reyes can demo offline.

Under section five point three, ESX expects security claims to carry owners and dates.

Section five point three treats scope tlp evidence and as testable only when evidence and ticket IDs are recorded.

For section five point three, Ashgrove College will not accept security work without a written trail.

### 5.4 Personal data

Logs include student and staff identities. Extracts contain only what the question needs; names are removed before sharing with ESX.

Section five point four develops security scope and evidence with a Ashgrove College note Tomás Reyes can demo offline.

Under section five point four, ESX expects security claims to carry owners and dates.

Section five point four treats scope tlp evidence and as testable only when evidence and ticket IDs are recorded.

For section five point four, Ashgrove College will not accept security work without a written trail.

### 5.5 Authorisation

The placement agreement and IT security policy define what Tomás may do. When unsure, he asks his supervisor and records the answer.

Section five point five develops security scope and evidence with a Ashgrove College note Tomás Reyes can demo offline.

Under section five point five, ESX expects security claims to carry owners and dates.

Section five point five treats scope tlp evidence and as testable only when evidence and ticket IDs are recorded.

For section five point five, Ashgrove College will not accept security work without a written trail.

### 5.6 Public sources

Government advisories and vendor blogs are useful, but their terms vary. Quoting short parts with attribution is usually fine; republishing whole reports is not.

Section five point six develops security scope and evidence with a Ashgrove College note Tomás Reyes can demo offline.

Under section five point six, ESX expects security claims to carry owners and dates.

Section five point six treats scope tlp evidence and as testable only when evidence and ticket IDs are recorded.

For section five point six, Ashgrove College will not accept security work without a written trail.

### 5.7 Mistakes

If he shares something wrongly, he reports it at once so the recipient can delete it. Hiding mistakes breaks trust far more.

Section five point seven develops security scope and evidence with a Ashgrove College note Tomás Reyes can demo offline.

Under section five point seven, ESX expects security claims to carry owners and dates.

Section five point seven treats scope tlp evidence and as testable only when evidence and ticket IDs are recorded.

For section five point seven, Ashgrove College will not accept security work without a written trail.

### Checklists

A short pre-share checklist — label checked, personal data removed, recipient allowed — takes a minute and prevents most handling errors.

### Worked example

A vendor email contains an unlabelled report naming other colleges. Tomás treats it as AMBER, asks the vendor for its intended label, and in the meantime shares only a summary with the Ashgrove email team. The vendor replies "AMBER+STRICT", so the summary stays inside Ashgrove.

> **Synthetic case.** The report is invented.

### Errors and limits

Policies cannot foresee every case; asking is part of the job.

### Exercises

- **EX017 — In or out.** Is visiting a suspicious site from a college device within Tomás's scope? *Rubric:* 3 = no, with reason; 2 = no; 1 = yes; 0 = none.
- **EX018 — Unlabelled default.** How should unlabelled material be treated? *Rubric:* 3 = as AMBER until sender confirms; 2 = restricted vaguely; 1 = CLEAR; 0 = none.
- **EX019 — Wrong share.** What should Tomás do if he shares something wrongly? *Rubric:* 3 = report immediately so recipient deletes; 2 = partial; 1 = hide; 0 = none.
- **EX020 — Republishing.** May Tomás republish a whole vendor report on the college intranet? *Rubric:* 3 = no; check terms; summarise with attribution; 2 = no; 1 = yes; 0 = none.

### Synthesis

Know your scope, apply TLP strictly, record provenance, minimise personal data and ask when unsure.

### Continue studying — chapter 05 of 18

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Threat intelligence and OSINT: system model

### Learning outcomes

You will (1) draw the college's CTI system as sources, processing, storage and outputs; (2) identify who owns each part; (3) map the system to STIX and TAXII concepts; (4) find weak points.

### 6.1 Sources

ESX's TAXII 2.1 collection, ESX email alerts, a national education advisory page, the help desk's reports of suspicious messages, and college logs.

Section six point one develops threat intelligence and osint system with a Ashgrove College note Tomás Reyes can demo offline.

Under section six point one, ESX expects threat claims to carry owners and dates.

Section six point one treats sources processing storage outputs as testable only when evidence and ticket IDs are recorded.

For section six point one, Ashgrove College will not accept threat work without a written trail.

### 6.2 Processing

Tomás's scripts validate and normalise indicators; his supervisor reviews relevance and grades sources; requests go to system owners.

Section six point two develops threat intelligence and osint system with a Ashgrove College note Tomás Reyes can demo offline.

Under section six point two, ESX expects threat claims to carry owners and dates.

Section six point two treats sources processing storage outputs as testable only when evidence and ticket IDs are recorded.

For section six point two, Ashgrove College will not accept threat work without a written trail.

### 6.3 Storage

A small threat intelligence platform stores STIX 2.1 objects: indicators, attack patterns, reports and relationships, each with a TLP marking definition.

Section six point three develops threat intelligence and osint system with a Ashgrove College note Tomás Reyes can demo offline.

Under section six point three, ESX expects threat claims to carry owners and dates.

Section six point three treats sources processing storage outputs as testable only when evidence and ticket IDs are recorded.

For section six point three, Ashgrove College will not accept threat work without a written trail.

### 6.4 Outputs

DNS filter and email gateway block lists, notes to owners, monthly summaries for management and feedback to ESX.

Section six point four develops threat intelligence and osint system with a Ashgrove College note Tomás Reyes can demo offline.

Under section six point four, ESX expects threat claims to carry owners and dates.

Section six point four treats sources processing storage outputs as testable only when evidence and ticket IDs are recorded.

For section six point four, Ashgrove College will not accept threat work without a written trail.

### 6.5 Owners

The network team owns the DNS filter; the email team the gateway; the supervisor the platform; Tomás the scripts.

Section six point five develops threat intelligence and osint system with a Ashgrove College note Tomás Reyes can demo offline.

Under section six point five, ESX expects threat claims to carry owners and dates.

Section six point five treats sources processing storage outputs as testable only when evidence and ticket IDs are recorded.

For section six point five, Ashgrove College will not accept threat work without a written trail.

### 6.6 Weak points

Single-person knowledge of scripts; email alerts arriving in a personal inbox; no check that block lists actually loaded.

Section six point six develops threat intelligence and osint system with a Ashgrove College note Tomás Reyes can demo offline.

Under section six point six, ESX expects threat claims to carry owners and dates.

Section six point six treats sources processing storage outputs as testable only when evidence and ticket IDs are recorded.

For section six point six, Ashgrove College will not accept threat work without a written trail.

### 6.7 Kill chain view

Mapping outputs to the Hutchins et al. phases shows coverage: email blocks act at delivery; DNS blocks at command and control; account resets after exploitation. No output addresses reconnaissance — a gap to discuss.

Section six point seven develops threat intelligence and osint system with a Ashgrove College note Tomás Reyes can demo offline.

Under section six point seven, ESX expects threat claims to carry owners and dates.

Section six point seven treats sources processing storage outputs as testable only when evidence and ticket IDs are recorded.

### 6.8 Diagram

One page, boxes and arrows, names of owners on each box.

Section six point eight develops threat intelligence and osint system with a Ashgrove College note Tomás Reyes can demo offline.

Under section six point eight, ESX expects threat claims to carry owners and dates.

Section six point eight treats sources processing storage outputs as testable only when evidence and ticket IDs are recorded.

For section six point eight, Ashgrove College will not accept threat work without a written trail.

Section six point eight fails closed if threat evidence is missing rather than guessing.

### Using the model in training

New placement students study the diagram on their first day. Tracing one indicator from an ESX alert to a DNS block, naming each owner on the way, teaches the whole flow in less than an hour. Asking them where they think the flow could break often surfaces fresh weak points that long-serving staff no longer notice.

### Worked example

Drawing the model reveals that ESX email alerts go only to the supervisor's inbox. When she was ill for a week, nobody read them. The team creates a shared mailbox with two readers and records the change.

> **Synthetic case.** The discovery is invented.

### Errors and limits

Models show structure, not quality; pair them with evaluation.

### Exercises

- **EX021 — Output owners.** Who owns the DNS filter and the email gateway? *Rubric:* 3 = network team; email team; 2 = one; 1 = Tomás; 0 = none.
- **EX022 — Inbox weakness.** What weakness did the diagram reveal, and what fixed it? *Rubric:* 3 = alerts to one inbox; shared mailbox with two readers; 2 = one; 1 = vague; 0 = none.
- **EX023 — Phase coverage.** At which kill-chain phase do email blocks act? *Rubric:* 3 = delivery; 2 = close; 1 = actions on objectives; 0 = none.
- **EX024 — Missing phase.** Which phase had no output, and why discuss it? *Rubric:* 3 = reconnaissance; coverage gap; 2 = phase only; 1 = wrong; 0 = none.

### Synthesis

Model sources, processing, storage and outputs with owners; use the model to find weak points and coverage gaps.

### Continue studying — chapter 06 of 18

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Threat intelligence and OSINT: data and telemetry

### Learning outcomes

You will (1) list telemetry sources that confirm or refute intelligence; (2) judge each source's coverage; (3) request log access properly; (4) keep extracts minimal.

### 7.1 Telemetry list

DNS resolver logs, proxy logs, email gateway logs, firewall logs, directory sign-ins, endpoint process events on staff machines, learning-platform login logs. Each answers different questions.

Section seven point one develops threat intelligence and osint data with a Ashgrove College note Tomás Reyes can demo offline.

Under section seven point one, ESX expects threat claims to carry owners and dates.

Section seven point one treats telemetry list coverage retention as testable only when evidence and ticket IDs are recorded.

For section seven point one, Ashgrove College will not accept threat work without a written trail.

### 7.2 Coverage

DNS covers all campus devices; endpoint events cover only college-managed machines; the proxy covers staff only. Tomás writes coverage beside each source so negative results are honest.

Section seven point two develops threat intelligence and osint data with a Ashgrove College note Tomás Reyes can demo offline.

Under section seven point two, ESX expects threat claims to carry owners and dates.

Section seven point two treats telemetry list coverage retention as testable only when evidence and ticket IDs are recorded.

### 7.3 Retention

DNS 90 days, proxy 30 days, cloud sign-ins 30 days, endpoint 60 days. An indicator from 45 days ago can still be checked in DNS but not in the proxy.

Section seven point three develops threat intelligence and osint data with a Ashgrove College note Tomás Reyes can demo offline.

Under section seven point three, ESX expects threat claims to carry owners and dates.

Section seven point three treats telemetry list coverage retention as testable only when evidence and ticket IDs are recorded.

For section seven point three, Ashgrove College will not accept threat work without a written trail.

### 7.4 Access

Tomás has read-only access to DNS and email logs. Others are searched on request by owning teams. Access requests are justified in writing.

Section seven point four develops threat intelligence and osint data with a Ashgrove College note Tomás Reyes can demo offline.

Under section seven point four, ESX expects threat claims to carry owners and dates.

Section seven point four treats telemetry list coverage retention as testable only when evidence and ticket IDs are recorded.

For section seven point four, Ashgrove College will not accept threat work without a written trail.

### 7.5 Minimal extracts

When evidence is needed, export only matching lines with needed fields — time, host, indicator — not full logs with every user's browsing.

Section seven point five develops threat intelligence and osint data with a Ashgrove College note Tomás Reyes can demo offline.

Under section seven point five, ESX expects threat claims to carry owners and dates.

Section seven point five treats telemetry list coverage retention as testable only when evidence and ticket IDs are recorded.

For section seven point five, Ashgrove College will not accept threat work without a written trail.

### 7.6 Clock accuracy

All servers synchronise time. A server with drifting time makes correlation unreliable; Tomás reports such drift.

Section seven point six develops threat intelligence and osint data with a Ashgrove College note Tomás Reyes can demo offline.

Under section seven point six, ESX expects threat claims to carry owners and dates.

Section seven point six treats telemetry list coverage retention as testable only when evidence and ticket IDs are recorded.

For section seven point six, Ashgrove College will not accept threat work without a written trail.

### 7.7 Quality checks

Daily volume per source shows gaps: a resolver that logged nothing overnight probably failed.

Section seven point seven develops threat intelligence and osint data with a Ashgrove College note Tomás Reyes can demo offline.

Under section seven point seven, ESX expects threat claims to carry owners and dates.

Section seven point seven treats telemetry list coverage retention as testable only when evidence and ticket IDs are recorded.

For section seven point seven, Ashgrove College will not accept threat work without a written trail.

### 7.8 Telemetry for techniques

Technique intelligence needs behavioural data. Phishing needs email logs; valid-account abuse needs sign-ins; command channels need DNS and proxy. A matrix of techniques against sources shows blind spots.

Section seven point eight develops threat intelligence and osint data with a Ashgrove College note Tomás Reyes can demo offline.

Under section seven point eight, ESX expects threat claims to carry owners and dates.

Section seven point eight treats telemetry list coverage retention as testable only when evidence and ticket IDs are recorded.

### Learning-platform logs

The learning platform records logins, file downloads and administrator changes. Intelligence about attackers abusing course platforms to host malicious files makes upload logs relevant too; Tomás asks the e-learning team which fields they keep and for how long.

### Worked example

ESX reports a domain used in attacks 40 days ago. Tomás searches DNS (90-day retention): two lookups from the library. The proxy has no record because its retention is 30 days. His note states both facts so readers do not misread the proxy's silence.

> **Synthetic case.** The domain and lookups are invented.

### Errors and limits

Telemetry shows activity, not intent; interpret with care.

### Exercises

- **EX025 — Retention check.** Why was the proxy silent about the 40-day-old domain? *Rubric:* 3 = 30-day retention; 2 = partial; 1 = no visits; 0 = none.
- **EX026 — Minimal extract.** What should an evidence extract contain? *Rubric:* 3 = only matching lines with needed fields; 2 = partial; 1 = full logs; 0 = none.
- **EX027 — Source coverage.** Which source covers all campus devices, and which only managed machines? *Rubric:* 3 = DNS all; endpoint managed only; 2 = one; 1 = wrong; 0 = none.
- **EX028 — Technique matrix.** What does a technique-by-source matrix reveal? *Rubric:* 3 = blind spots where no telemetry covers a technique; 2 = partial; 1 = nothing; 0 = none.

### Synthesis

Know each source's coverage and retention, request access properly, extract minimally and map techniques to telemetry.

### Continue studying — chapter 07 of 18

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Threat intelligence and OSINT: failure modes

### Learning outcomes

You will (1) recognise how CTI support fails; (2) classify failures by stage; (3) spot false positives and their causes; (4) recommend fixes.

### 8.1 Stages

Failures happen in collection (missed alert), processing (parsing error), analysis (wrong relevance call), dissemination (wrong recipient) and action (owner never acted).

Section eight point one develops threat intelligence and osint failure with a Ashgrove College note Tomás Reyes can demo offline.

Under section eight point one, ESX expects threat claims to carry owners and dates.

Section eight point one treats stages false positives false as testable only when evidence and ticket IDs are recorded.

For section eight point one, Ashgrove College will not accept threat work without a written trail.

### 8.2 False positives

Blocking a legitimate site because an indicator was stale or shared. Typical causes: old cloud addresses, popular file-sharing domains in feeds, typing errors.

Section eight point two develops threat intelligence and osint failure with a Ashgrove College note Tomás Reyes can demo offline.

Under section eight point two, ESX expects threat claims to carry owners and dates.

Section eight point two treats stages false positives false as testable only when evidence and ticket IDs are recorded.

For section eight point two, Ashgrove College will not accept threat work without a written trail.

### 8.3 False negatives

Missing a real match because of normalisation differences (trailing dot, capital letters), missing logs or retention expiry.

Section eight point three develops threat intelligence and osint failure with a Ashgrove College note Tomás Reyes can demo offline.

Under section eight point three, ESX expects threat claims to carry owners and dates.

Section eight point three treats stages false positives false as testable only when evidence and ticket IDs are recorded.

For section eight point three, Ashgrove College will not accept threat work without a written trail.

### 8.4 Label failures

Sharing AMBER material with ESX at large. Causes: missing label in source, copy-paste stripping labels, unclear rules.

Section eight point four develops threat intelligence and osint failure with a Ashgrove College note Tomás Reyes can demo offline.

Under section eight point four, ESX expects threat claims to carry owners and dates.

Section eight point four treats stages false positives false as testable only when evidence and ticket IDs are recorded.

For section eight point four, Ashgrove College will not accept threat work without a written trail.

### 8.5 Overload

Too many low-value alerts mean owners stop reading. Cause: no triage before dissemination.

Section eight point five develops threat intelligence and osint failure with a Ashgrove College note Tomás Reyes can demo offline.

Under section eight point five, ESX expects threat claims to carry owners and dates.

Section eight point five treats stages false positives false as testable only when evidence and ticket IDs are recorded.

For section eight point five, Ashgrove College will not accept threat work without a written trail.

### 8.6 Learning

Each failure gets a short blameless review: what happened, why, what changed. Patterns guide improvement.

Section eight point six develops threat intelligence and osint failure with a Ashgrove College note Tomás Reyes can demo offline.

Under section eight point six, ESX expects threat claims to carry owners and dates.

Section eight point six treats stages false positives false as testable only when evidence and ticket IDs are recorded.

For section eight point six, Ashgrove College will not accept threat work without a written trail.

### 8.7 Recording failures

A shared failure log with date, stage, cause and fix shows recurring issues. Three label failures in a term indicate a process problem, not three careless people.

Section eight point seven develops threat intelligence and osint failure with a Ashgrove College note Tomás Reyes can demo offline.

Under section eight point seven, ESX expects threat claims to carry owners and dates.

Section eight point seven treats stages false positives false as testable only when evidence and ticket IDs are recorded.

For section eight point seven, Ashgrove College will not accept threat work without a written trail.

### 8.8 Bias

Assuming every issue is an attack leads to over-blocking; assuming none is leads to missing real ones. Check evidence each time.

Section eight point eight develops threat intelligence and osint failure with a Ashgrove College note Tomás Reyes can demo offline.

Under section eight point eight, ESX expects threat claims to carry owners and dates.

Section eight point eight treats stages false positives false as testable only when evidence and ticket IDs are recorded.

For section eight point eight, Ashgrove College will not accept threat work without a written trail.

### Dissemination failures

An advisory sent to a general IT mailbox that nobody owns will wait for days. Each item type has a named recipient, and the sender asks for acknowledgement so silence is noticed. When no acknowledgement arrives within the agreed time, the item is escalated to the supervisor rather than left waiting.

### Worked example

Students complain that a revision website is blocked. Tomás finds the address came from a feed six months old; the site moved to that cloud address last month. He requests removal, the network team unblocks it within an hour, and the expiry rule for addresses is shortened to 30 days.

> **Synthetic case.** The site and feed are invented.

### Errors and limits

Fixing one failure can create another; test changes.

### Exercises

- **EX029 — Revision site.** Classify the revision-site block and its cause. *Rubric:* 3 = false positive; stale cloud address; 2 = one; 1 = attack; 0 = none.
- **EX030 — Missed match.** Give two causes of false negatives. *Rubric:* 3 = normalisation, missing logs, retention; 2 = one; 1 = none; 0 = none.
- **EX031 — Pattern meaning.** What do three label failures in one term suggest? *Rubric:* 3 = process problem; fix process; 2 = partial; 1 = careless people; 0 = none.
- **EX032 — Fix applied.** What process change followed the revision-site case? *Rubric:* 3 = address expiry shortened to 30 days; 2 = partial; 1 = none; 0 = none.

### Synthesis

Classify failures by stage, trace causes, review without blame and fix the process.

### Continue studying — chapter 08 of 18

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Threat intelligence and OSINT: tools and methods

### Learning outcomes

You will (1) use a CTI platform's basic functions; (2) apply triage and grading methods; (3) tag items with ATT&CK techniques; (4) use OSINT tools ethically.

### 9.1 Platform basics

The college platform imports STIX bundles, shows objects and relationships, applies TLP markings and exports lists for the DNS filter and email gateway. Tomás uses it for storage and search, his scripts for checks.

Section nine point one develops threat intelligence and osint tools with a Ashgrove College note Tomás Reyes can demo offline.

Under section nine point one, ESX expects threat claims to carry owners and dates.

Section nine point one treats platform basics triage grading as testable only when evidence and ticket IDs are recorded.

### 9.2 Triage

Four questions: relevant to Ashgrove? timely? actionable? source known? Items failing the first are logged and closed.

Section nine point two develops threat intelligence and osint tools with a Ashgrove College note Tomás Reyes can demo offline.

Under section nine point two, ESX expects threat claims to carry owners and dates.

Section nine point two treats platform basics triage grading as testable only when evidence and ticket IDs are recorded.

For section nine point two, Ashgrove College will not accept threat work without a written trail.

### 9.3 Grading

The Admiralty scale: source reliability A–F, information credibility 1–6. ESX is usually B; an unverified social-media claim F6.

Section nine point three develops threat intelligence and osint tools with a Ashgrove College note Tomás Reyes can demo offline.

Under section nine point three, ESX expects threat claims to carry owners and dates.

Section nine point three treats platform basics triage grading as testable only when evidence and ticket IDs are recorded.

For section nine point three, Ashgrove College will not accept threat work without a written trail.

### 9.4 Tagging

Tag only what the text supports: "students received fake grade notices with links" supports T1566.

Section nine point four develops threat intelligence and osint tools with a Ashgrove College note Tomás Reyes can demo offline.

Under section nine point four, ESX expects threat claims to carry owners and dates.

Section nine point four treats platform basics triage grading as testable only when evidence and ticket IDs are recorded.

For section nine point four, Ashgrove College will not accept threat work without a written trail.

### 9.5 OSINT tools

Certificate-transparency search for lookalike college domains; approved passive DNS; public vulnerability databases. All used within their terms; nothing that contacts suspicious sites.

Section nine point five develops threat intelligence and osint tools with a Ashgrove College note Tomás Reyes can demo offline.

Under section nine point five, ESX expects threat claims to carry owners and dates.

Section nine point five treats platform basics triage grading as testable only when evidence and ticket IDs are recorded.

For section nine point five, Ashgrove College will not accept threat work without a written trail.

### 9.6 Notes

Three lines: what, why it matters here with confidence, action and owner.

Section nine point six develops threat intelligence and osint tools with a Ashgrove College note Tomás Reyes can demo offline.

Under section nine point six, ESX expects threat claims to carry owners and dates.

Section nine point six treats platform basics triage grading as testable only when evidence and ticket IDs are recorded.

For section nine point six, Ashgrove College will not accept threat work without a written trail.

### 9.7 Tool limits

A platform shows what it was given. If ESX did not share an object, it is absent; absence in the platform is not absence in the world.

Section nine point seven develops threat intelligence and osint tools with a Ashgrove College note Tomás Reyes can demo offline.

Under section nine point seven, ESX expects threat claims to carry owners and dates.

Section nine point seven treats platform basics triage grading as testable only when evidence and ticket IDs are recorded.

For section nine point seven, Ashgrove College will not accept threat work without a written trail.

### 9.8 Practice

Tomás triages twenty items each week with his supervisor and compares decisions to build consistency.

Section nine point eight develops threat intelligence and osint tools with a Ashgrove College note Tomás Reyes can demo offline.

Under section nine point eight, ESX expects threat claims to carry owners and dates.

Section nine point eight treats platform basics triage grading as testable only when evidence and ticket IDs are recorded.

For section nine point eight, Ashgrove College will not accept threat work without a written trail.

### Recording methods

Each triage decision and grade is logged with a one-line reason. Reviewing these reasons monthly shows whether Tomás and his supervisor apply the same standards, and new placement students learn from real examples.

### Worked example

A certificate-transparency search finds "ashgrove-studentportal.example" issued yesterday. Not a college domain. Tomás grades the finding B2 (reliable log, probable impersonation), tags T1583 (Acquire Infrastructure), and writes: "New lookalike of student portal registered yesterday; likely phishing preparation; moderate confidence. Action: email team to block; supervisor to request takedown."

> **Synthetic case.** The domain is invented.

### Errors and limits

Lookalike names can be innocent, such as a student society site; check before takedown.

### Exercises

- **EX033 — Lookalike tag.** Why tag the new lookalike with T1583 rather than T1566? *Rubric:* 3 = preparation, infrastructure acquired, no emails seen yet; 2 = partial; 1 = no difference; 0 = none.
- **EX034 — Grade explanation.** Explain the B2 grade for the lookalike finding. *Rubric:* 3 = B reliable log source; 2 probably true impersonation; 2 = one; 1 = wrong; 0 = none.
- **EX035 — Absence caution.** Why is absence from the platform not proof of absence? *Rubric:* 3 = platform only holds what was shared; 2 = partial; 1 = it is proof; 0 = none.
- **EX036 — Innocent lookalike.** What should be checked before requesting takedown? *Rubric:* 3 = whether legitimate (e.g. student society); 2 = partial; 1 = nothing; 0 = none.

### Synthesis

Use the platform for storage and search, triage and grade consistently, tag carefully and keep OSINT passive and lawful.

### Continue studying — chapter 09 of 18

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Threat intelligence and OSINT: control configuration

### Learning outcomes

You will (1) prepare indicator lists in formats controls accept; (2) choose enforcement points by indicator type; (3) set expiry and review on each entry; (4) document configuration requests.

### 10.1 Formats

The DNS filter accepts one domain per line; the email gateway accepts sender domains and attachment hashes through its management interface; the firewall accepts address objects. Tomás prepares each list from the platform export and validates it before handing it over.

Section ten point one develops threat intelligence and osint control with a Ashgrove College note Tomás Reyes can demo offline.

Under section ten point one, ESX expects threat claims to carry owners and dates.

Section ten point one treats formats choosing points expiry as testable only when evidence and ticket IDs are recorded.

### 10.2 Choosing points

Domains to DNS; sender domains to email; hashes to email attachment scanning and endpoint; addresses only when not shared hosting. Techniques inform configuration too: intelligence on macro-laden attachments (User Execution, T1204) supports quarantining macro documents from outside.

Section ten point two develops threat intelligence and osint control with a Ashgrove College note Tomás Reyes can demo offline.

Under section ten point two, ESX expects threat claims to carry owners and dates.

Section ten point two treats formats choosing points expiry as testable only when evidence and ticket IDs are recorded.

### 10.3 Expiry

Every entry carries an expiry date: 30 days for addresses, 90 for domains, longer for hashes. Lists without expiry grow until they break things.

Section ten point three develops threat intelligence and osint control with a Ashgrove College note Tomás Reyes can demo offline.

Under section ten point three, ESX expects threat claims to carry owners and dates.

Section ten point three treats formats choosing points expiry as testable only when evidence and ticket IDs are recorded.

For section ten point three, Ashgrove College will not accept threat work without a written trail.

### 10.4 Requests

Tomás drafts; the owning team configures. The request includes list, source, TLP, reason, expiry and verification plan.

Section ten point four develops threat intelligence and osint control with a Ashgrove College note Tomás Reyes can demo offline.

Under section ten point four, ESX expects threat claims to carry owners and dates.

Section ten point four treats formats choosing points expiry as testable only when evidence and ticket IDs are recorded.

For section ten point four, Ashgrove College will not accept threat work without a written trail.

### 10.5 Allow lists

Some domains must never be blocked: the learning platform, examination boards, the student loan service. An allow list checked before every export prevents accidents.

Section ten point five develops threat intelligence and osint control with a Ashgrove College note Tomás Reyes can demo offline.

Under section ten point five, ESX expects threat claims to carry owners and dates.

Section ten point five treats formats choosing points expiry as testable only when evidence and ticket IDs are recorded.

For section ten point five, Ashgrove College will not accept threat work without a written trail.

### 10.6 Testing

After loading, a test lookup of one blocked domain from a test machine must fail; a test of an allowed domain must succeed.

Section ten point six develops threat intelligence and osint control with a Ashgrove College note Tomás Reyes can demo offline.

Under section ten point six, ESX expects threat claims to carry owners and dates.

Section ten point six treats formats choosing points expiry as testable only when evidence and ticket IDs are recorded.

For section ten point six, Ashgrove College will not accept threat work without a written trail.

### 10.7 Change windows

Large list changes happen outside exam periods, when disruption would hurt most.

Section ten point seven develops threat intelligence and osint control with a Ashgrove College note Tomás Reyes can demo offline.

Under section ten point seven, ESX expects threat claims to carry owners and dates.

Section ten point seven treats formats choosing points expiry as testable only when evidence and ticket IDs are recorded.

For section ten point seven, Ashgrove College will not accept threat work without a written trail.

### 10.8 Documentation

The configuration register lists every list, owner, last change and expiry policy.

Section ten point eight develops threat intelligence and osint control with a Ashgrove College note Tomás Reyes can demo offline.

Under section ten point eight, ESX expects threat claims to carry owners and dates.

Section ten point eight treats formats choosing points expiry as testable only when evidence and ticket IDs are recorded.

For section ten point eight, Ashgrove College will not accept threat work without a written trail.

### 10.9 Size limits

Some tools cap list size. When near the cap, remove expired entries first rather than raising the cap blindly.

Section ten point nine develops threat intelligence and osint control with a Ashgrove College note Tomás Reyes can demo offline.

Under section ten point nine, ESX expects threat claims to carry owners and dates.

Section ten point nine treats formats choosing points expiry as testable only when evidence and ticket IDs are recorded.

For section ten point nine, Ashgrove College will not accept threat work without a written trail.

### Worked example

Tomás's export includes a file-sharing domain from a vendor feed. The allow-list check stops it: lecturers use that service to share materials. He removes it from the request and reports the feed's error to the vendor through his supervisor.

> **Synthetic case.** The domain and feed are invented.

### Errors and limits

Controls vary by product; read their documentation before formatting.

### Exercises

- **EX037 — Expiry periods.** State expiry periods for addresses and domains and why they differ. *Rubric:* 3 = 30 vs 90 days; addresses reassigned faster; 2 = numbers; 1 = same; 0 = none.
- **EX038 — Allow-list catch.** What did the allow-list check prevent? *Rubric:* 3 = blocking lecturer file-sharing service; 2 = partial; 1 = nothing; 0 = none.
- **EX039 — Macro intelligence.** Which control does T1204 macro intelligence support? *Rubric:* 3 = quarantine external macro documents; 2 = partial; 1 = firewall; 0 = none.
- **EX040 — Exam timing.** Why avoid large list changes during exams? *Rubric:* 3 = disruption most harmful; 2 = partial; 1 = no reason; 0 = none.

### Synthesis

Format lists for each control, pick enforcement points by type, add expiry, check allow lists and test after loading.

### Continue studying — chapter 10 of 18

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Threat intelligence and OSINT: verification

### Learning outcomes

You will (1) verify intelligence before acting; (2) corroborate with independent and internal evidence; (3) verify that controls took effect; (4) record verification.

### 11.1 Verify the intelligence

Check the indicator's form, its age, whether other independent sources report it, and whether it belongs to shared infrastructure. Use passive sources only.

Section eleven point one develops threat intelligence and osint verification with a Ashgrove College note Tomás Reyes can demo offline.

Under section eleven point one, ESX expects threat claims to carry owners and dates.

Section eleven point one treats verify the intelligence internal as testable only when evidence and ticket IDs are recorded.

For section eleven point one, Ashgrove College will not accept threat work without a written trail.

### 11.2 Internal corroboration

Did college logs see it? Internal sightings both confirm relevance and show urgency.

Section eleven point two develops threat intelligence and osint verification with a Ashgrove College note Tomás Reyes can demo offline.

Under section eleven point two, ESX expects threat claims to carry owners and dates.

Section eleven point two treats verify the intelligence internal as testable only when evidence and ticket IDs are recorded.

For section eleven point two, Ashgrove College will not accept threat work without a written trail.

### 11.3 Independence

Two reports citing the same original are one source. Ask what each is based on.

Section eleven point three develops threat intelligence and osint verification with a Ashgrove College note Tomás Reyes can demo offline.

Under section eleven point three, ESX expects threat claims to carry owners and dates.

Section eleven point three treats verify the intelligence internal as testable only when evidence and ticket IDs are recorded.

For section eleven point three, Ashgrove College will not accept threat work without a written trail.

### 11.4 Verify the control

After blocking, test from an approved machine. After an email rule, send a harmless test message. Record results.

Section eleven point four develops threat intelligence and osint verification with a Ashgrove College note Tomás Reyes can demo offline.

Under section eleven point four, ESX expects threat claims to carry owners and dates.

Section eleven point four treats verify the intelligence internal as testable only when evidence and ticket IDs are recorded.

For section eleven point four, Ashgrove College will not accept threat work without a written trail.

### 11.5 Verify the outcome

A week later, check whether matches dropped. If blocked lookups continue from one machine, that machine may be infected and needs attention.

Section eleven point five develops threat intelligence and osint verification with a Ashgrove College note Tomás Reyes can demo offline.

Under section eleven point five, ESX expects threat claims to carry owners and dates.

Section eleven point five treats verify the intelligence internal as testable only when evidence and ticket IDs are recorded.

For section eleven point five, Ashgrove College will not accept threat work without a written trail.

### 11.6 Record

Checks, results, time and person. Others can repeat them.

Section eleven point six develops threat intelligence and osint verification with a Ashgrove College note Tomás Reyes can demo offline.

Under section eleven point six, ESX expects threat claims to carry owners and dates.

Section eleven point six treats verify the intelligence internal as testable only when evidence and ticket IDs are recorded.

For section eleven point six, Ashgrove College will not accept threat work without a written trail.

Section eleven point six fails closed if threat evidence is missing rather than guessing.

### 11.7 Time limits

Urgent items get quick checks; strategic claims can wait for fuller verification. Report what was and was not verified.

Section eleven point seven develops threat intelligence and osint verification with a Ashgrove College note Tomás Reyes can demo offline.

Under section eleven point seven, ESX expects threat claims to carry owners and dates.

Section eleven point seven treats verify the intelligence internal as testable only when evidence and ticket IDs are recorded.

For section eleven point seven, Ashgrove College will not accept threat work without a written trail.

### 11.8 Disagreement

If verification contradicts the source, tell the source politely with evidence. Communities improve through such feedback.

Section eleven point eight develops threat intelligence and osint verification with a Ashgrove College note Tomás Reyes can demo offline.

Under section eleven point eight, ESX expects threat claims to carry owners and dates.

Section eleven point eight treats verify the intelligence internal as testable only when evidence and ticket IDs are recorded.

For section eleven point eight, Ashgrove College will not accept threat work without a written trail.

### 11.9 Never active

Verification never includes visiting suspicious pages, downloading files from them or scanning their servers from college systems.

Section eleven point nine develops threat intelligence and osint verification with a Ashgrove College note Tomás Reyes can demo offline.

Under section eleven point nine, ESX expects threat claims to carry owners and dates.

Section eleven point nine treats verify the intelligence internal as testable only when evidence and ticket IDs are recorded.

For section eleven point nine, Ashgrove College will not accept threat work without a written trail.

### Verifying with owners

System owners know whether a connection is expected. Before escalating a match on the library server, Tomás asks the library systems officer whether the server legitimately talks to that supplier. A two-minute call often settles what hours of log reading cannot, and owners appreciate being asked rather than surprised by an incident ticket.

### Worked example

ESX shares a domain as a phishing site. Tomás finds it on a large content-delivery service, with a long legitimate history and no college lookups. Certificate records show a reputable owner. He tells ESX the domain appears legitimate; ESX checks and withdraws it — the original report had a typing error.

> **Synthetic case.** The domain is invented.

### Errors and limits

Verification reduces errors but cannot remove them.

### Exercises

- **EX041 — Withdrawn domain.** What evidence suggested the ESX domain was legitimate? *Rubric:* 3 = CDN, long history, no lookups, reputable certificate owner; 2 = two; 1 = one; 0 = none.
- **EX042 — Ongoing lookups.** What do continued blocked lookups from one machine suggest? *Rubric:* 3 = machine may be infected; investigate; 2 = partial; 1 = nothing; 0 = none.
- **EX043 — Independence question.** What should Tomás ask to test independence? *Rubric:* 3 = what each report is based on; 2 = partial; 1 = dates; 0 = none.
- **EX044 — Forbidden check.** Name one verification step that is never allowed. *Rubric:* 3 = visiting/downloading/scanning suspicious servers; 2 = vague; 1 = passive DNS; 0 = none.

### Synthesis

Verify intelligence, controls and outcomes passively, record each check and give sources honest feedback.

### Continue studying — chapter 11 of 18

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Contained laboratory I

### Learning outcomes

You will (1) enrich indicator matches with asset ownership; (2) route each match to the right team; (3) handle matches on unknown assets; (4) write a lab report.

### 12.1 Lab rules

The lab runs offline in the course virtual machine on synthetic data, using only the standard library. No real college logs.

Section twelve point one develops contained laboratory with a Ashgrove College note Tomás Reyes can demo offline.

Under section twelve point one, ESX expects contained claims to carry owners and dates.

Section twelve point one treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

For section twelve point one, Ashgrove College will not accept contained work without a written trail.

### Lab — enrich and route

```python
"""Lab (ch 12): join matched indicators with asset owners and choose a route (synthetic)."""
owners = {"ws-lib-03": ("Library", "staff"), "srv-lms-01": ("Learning platform", "server"), "ws-fin-11": ("Finance", "staff")}
hits = [("ws-fin-11", "invoice-portal.example", "T1566"), ("srv-lms-01", "198.51.100.77", "T1071"),
        ("ws-lab-99", "update-svc.example", "T1071")]
for host, ioc, tech in hits:
    if host not in owners:
        print(host, ioc, tech, "-> UNKNOWN ASSET: ask network team"); continue
    dept, kind = owners[host]
    route = "incident response (server)" if kind == "server" else "service desk + " + dept
    print(host, ioc, tech, "->", route)
```

Run with `python3 lab_enrich.py`. Verified output:

```text
ws-fin-11 invoice-portal.example T1566 -> service desk + Finance
srv-lms-01 198.51.100.77 T1071 -> incident response (server)
ws-lab-99 update-svc.example T1071 -> UNKNOWN ASSET: ask network team
```

### 12.2 Reading the result

ws-fin-11 matched invoice-portal.example (Phishing, T1566); it is a Finance staff machine, so the route is service desk plus the Finance department. srv-lms-01, the learning-platform server, matched an address associated with Application Layer Protocol (T1071) command traffic; servers go to incident response. ws-lab-99 is not in the owner list — the script asks the network team rather than guessing.

Section twelve point two develops contained laboratory with a Ashgrove College note Tomás Reyes can demo offline.

Under section twelve point two, ESX expects contained claims to carry owners and dates.

### 12.3 Why route by asset

A staff machine contacting a phishing domain may need a password reset and a conversation; a server talking to a command address may be compromised and needs incident response immediately.

Section twelve point three develops contained laboratory with a Ashgrove College note Tomás Reyes can demo offline.

Under section twelve point three, ESX expects contained claims to carry owners and dates.

Section twelve point three treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

For section twelve point three, Ashgrove College will not accept contained work without a written trail.

### 12.4 Unknown assets

Unknown hosts are common: new machines, lab equipment, devices named differently. Each is a gap in the inventory to close.

Section twelve point four develops contained laboratory with a Ashgrove College note Tomás Reyes can demo offline.

Under section twelve point four, ESX expects contained claims to carry owners and dates.

Section twelve point four treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

For section twelve point four, Ashgrove College will not accept contained work without a written trail.

### 12.5 Lab report

Aim, method, results with exact outputs, interpretation, problems and one improvement.

Section twelve point five develops contained laboratory with a Ashgrove College note Tomás Reyes can demo offline.

Under section twelve point five, ESX expects contained claims to carry owners and dates.

Section twelve point five treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

For section twelve point five, Ashgrove College will not accept contained work without a written trail.

Section twelve point five fails closed if contained evidence is missing rather than guessing.

### 12.6 Improvement ideas

Add last-seen times; add severity by technique; read the owner list from a file maintained by the network team.

Section twelve point six develops contained laboratory with a Ashgrove College note Tomás Reyes can demo offline.

Under section twelve point six, ESX expects contained claims to carry owners and dates.

Section twelve point six treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

For section twelve point six, Ashgrove College will not accept contained work without a written trail.

### 12.7 Pair work

One student runs, the other checks outputs against expectations, then swap.

Section twelve point seven develops contained laboratory with a Ashgrove College note Tomás Reyes can demo offline.

Under section twelve point seven, ESX expects contained claims to carry owners and dates.

Section twelve point seven treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

For section twelve point seven, Ashgrove College will not accept contained work without a written trail.

Section twelve point seven fails closed if contained evidence is missing rather than guessing.

### 12.8 Safety

No real hostnames or addresses in submitted reports; use the lab's synthetic values.

Section twelve point eight develops contained laboratory with a Ashgrove College note Tomás Reyes can demo offline.

Under section twelve point eight, ESX expects contained claims to carry owners and dates.

Section twelve point eight treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

For section twelve point eight, Ashgrove College will not accept contained work without a written trail.

Section twelve point eight fails closed if contained evidence is missing rather than guessing.

### Extending the lab

Students may extend the script to read matches from a CSV file and write routes to another file. Any extension must keep the unknown-asset rule.

### Worked example

Tomás's pair notices the server route ignores Finance's own server. They add a rule: servers owned by Finance also notify the Finance manager, and record the change in their report's improvements section.

> **Synthetic case.** The lab data is invented teaching material.

### Errors and limits

Owner lists go stale; enrichment is only as good as the list.

### Exercises

- **EX045 — Lab routes.** Give the route for each lab match. *Rubric:* 3 = ws-fin-11 service desk+Finance; srv-lms-01 incident response; ws-lab-99 ask network team; 2 = two; 1 = one; 0 = none.
- **EX046 — Server urgency.** Why do server matches go to incident response? *Rubric:* 3 = possible compromise of shared service; urgent; 2 = partial; 1 = same as desktops; 0 = none.
- **EX047 — Unknown host.** What does an unknown host reveal, and what is done? *Rubric:* 3 = inventory gap; ask network team, add to list; 2 = partial; 1 = ignore; 0 = none.
- **EX048 — Report hygiene.** Why must lab reports avoid real hostnames? *Rubric:* 3 = confidentiality; synthetic only; 2 = partial; 1 = fine; 0 = none.

### Synthesis

Enrich matches with ownership, route by asset type, treat unknown hosts as inventory gaps and report carefully.

### Continue studying — chapter 12 of 18

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Threat intelligence and OSINT: troubleshooting

### Learning outcomes

You will (1) diagnose problems in imports, matching and exports; (2) use logs of your own tools; (3) communicate pipeline problems; (4) add checks to prevent repeats.

### 13.1 Common problems

TAXII import fails; a CSV column renamed; matches drop to zero; a block list fails to load; a label value appears that scripts do not recognise.

Section thirteen point one develops threat intelligence and osint troubleshooting with a Ashgrove College note Tomás Reyes can demo offline.

Under section thirteen point one, ESX expects threat claims to carry owners and dates.

Section thirteen point one treats common problems step by as testable only when evidence and ticket IDs are recorded.

For section thirteen point one, Ashgrove College will not accept threat work without a written trail.

### 13.2 Step by step

Check input arrived, parsing succeeded, storage updated, export produced, control loaded. At each step compare counts with yesterday.

Section thirteen point two develops threat intelligence and osint troubleshooting with a Ashgrove College note Tomás Reyes can demo offline.

Under section thirteen point two, ESX expects threat claims to carry owners and dates.

Section thirteen point two treats common problems step by as testable only when evidence and ticket IDs are recorded.

For section thirteen point two, Ashgrove College will not accept threat work without a written trail.

### 13.3 Tool logs

Scripts write their own logs: start time, inputs, counts, errors. Without them, troubleshooting is guesswork.

Section thirteen point three develops threat intelligence and osint troubleshooting with a Ashgrove College note Tomás Reyes can demo offline.

Under section thirteen point three, ESX expects threat claims to carry owners and dates.

Section thirteen point three treats common problems step by as testable only when evidence and ticket IDs are recorded.

For section thirteen point three, Ashgrove College will not accept threat work without a written trail.

### 13.4 Communicating

If protection lapsed, tell owners plainly: what stopped, since when, what still works, when a fix is expected.

Section thirteen point four develops threat intelligence and osint troubleshooting with a Ashgrove College note Tomás Reyes can demo offline.

Under section thirteen point four, ESX expects threat claims to carry owners and dates.

Section thirteen point four treats common problems step by as testable only when evidence and ticket IDs are recorded.

For section thirteen point four, Ashgrove College will not accept threat work without a written trail.

### 13.5 Prevention

After each fix, add a check: alert if imports are zero; alert on unknown labels; compare exported and loaded counts.

Section thirteen point five develops threat intelligence and osint troubleshooting with a Ashgrove College note Tomás Reyes can demo offline.

Under section thirteen point five, ESX expects threat claims to carry owners and dates.

Section thirteen point five treats common problems step by as testable only when evidence and ticket IDs are recorded.

For section thirteen point five, Ashgrove College will not accept threat work without a written trail.

### 13.6 Keep changes small

Change one thing at a time while troubleshooting; otherwise you cannot tell which change helped.

Section thirteen point six develops threat intelligence and osint troubleshooting with a Ashgrove College note Tomás Reyes can demo offline.

Under section thirteen point six, ESX expects threat claims to carry owners and dates.

Section thirteen point six treats common problems step by as testable only when evidence and ticket IDs are recorded.

For section thirteen point six, Ashgrove College will not accept threat work without a written trail.

### 13.7 Escalation

When the problem lies in another team's system, give them evidence: the step where counts stop, timestamps and error messages.

Section thirteen point seven develops threat intelligence and osint troubleshooting with a Ashgrove College note Tomás Reyes can demo offline.

Under section thirteen point seven, ESX expects threat claims to carry owners and dates.

Section thirteen point seven treats common problems step by as testable only when evidence and ticket IDs are recorded.

For section thirteen point seven, Ashgrove College will not accept threat work without a written trail.

### 13.8 Recording

A fault log with symptom, cause, fix and prevention builds team memory.

Section thirteen point eight develops threat intelligence and osint troubleshooting with a Ashgrove College note Tomás Reyes can demo offline.

Under section thirteen point eight, ESX expects threat claims to carry owners and dates.

Section thirteen point eight treats common problems step by as testable only when evidence and ticket IDs are recorded.

For section thirteen point eight, Ashgrove College will not accept threat work without a written trail.

### 13.9 Calm under pressure

Pipeline faults during an incident feel urgent. Follow the same steps; skipping them usually costs more time.

Section thirteen point nine develops threat intelligence and osint troubleshooting with a Ashgrove College note Tomás Reyes can demo offline.

Under section thirteen point nine, ESX expects threat claims to carry owners and dates.

Section thirteen point nine treats common problems step by as testable only when evidence and ticket IDs are recorded.

For section thirteen point nine, Ashgrove College will not accept threat work without a written trail.

### Test data for the parser

Keep a small file of sample log lines in each known format, including the new one. Running the parser against it after every change proves old and new formats both still work.

### Worked example

Matches fall to zero on Tuesday. Counts show DNS logs arrived but the matcher read none. The log format gained a new first column after a resolver update, shifting fields. Tomás updates the parser to read fields by name, reruns Tuesday's data — finding three matches — and adds a check that warns when a day's parse count is zero.

> **Synthetic case.** The update is invented.

### Errors and limits

Some faults are intermittent; keep logs long enough to see patterns.

### Exercises

- **EX049 — Zero matches.** What caused the zero matches, and what was the lasting fix? *Rubric:* 3 = new first column shifted fields; parse by name + zero-count check; 2 = one; 1 = vague; 0 = none.
- **EX050 — One change rule.** Why change one thing at a time? *Rubric:* 3 = know which change worked; 2 = partial; 1 = faster to change all; 0 = none.
- **EX051 — Own logs.** What should scripts record in their own logs? *Rubric:* 3 = start time, inputs, counts, errors; 2 = two; 1 = one; 0 = none.
- **EX052 — Rerun.** Why rerun Tuesday's data after the fix? *Rubric:* 3 = find missed matches during the fault; 2 = partial; 1 = unnecessary; 0 = none.

### Synthesis

Troubleshoot stage by stage with counts and tool logs, communicate lapses, rerun missed data and add checks.

### Continue studying — chapter 13 of 18

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Threat intelligence and OSINT: automation

### Learning outcomes

You will (1) select CTI tasks suitable for automation; (2) keep human approval for high-impact actions; (3) schedule and monitor jobs; (4) document automated behaviour.

### 14.1 Suitable tasks

Daily import, validation, deduplication, matching, expiry flags, weekly counts. These follow rules and repeat.

Section fourteen point one develops threat intelligence and osint automation with a Ashgrove College note Tomás Reyes can demo offline.

Under section fourteen point one, ESX expects threat claims to carry owners and dates.

Section fourteen point one treats suitable tasks unsuitable tasks as testable only when evidence and ticket IDs are recorded.

For section fourteen point one, Ashgrove College will not accept threat work without a written trail.

### 14.2 Unsuitable tasks

Deciding relevance of new reports, grading new sources, blocking services that students depend on, sharing restricted data outward.

Section fourteen point two develops threat intelligence and osint automation with a Ashgrove College note Tomás Reyes can demo offline.

Under section fourteen point two, ESX expects threat claims to carry owners and dates.

Section fourteen point two treats suitable tasks unsuitable tasks as testable only when evidence and ticket IDs are recorded.

For section fourteen point two, Ashgrove College will not accept threat work without a written trail.

### 14.3 Approval gates

Automation prepares a block list; a person approves additions for the DNS filter. Low-risk categories — ESX GREEN domains graded B or better — may be auto-approved after a trial period agreed with the network team.

Section fourteen point three develops threat intelligence and osint automation with a Ashgrove College note Tomás Reyes can demo offline.

Under section fourteen point three, ESX expects threat claims to carry owners and dates.

Section fourteen point three treats suitable tasks unsuitable tasks as testable only when evidence and ticket IDs are recorded.

### 14.4 Scheduling and alerts

Jobs run at fixed times; failure sends an alert to a shared mailbox, not one person.

Section fourteen point four develops threat intelligence and osint automation with a Ashgrove College note Tomás Reyes can demo offline.

Under section fourteen point four, ESX expects threat claims to carry owners and dates.

Section fourteen point four treats suitable tasks unsuitable tasks as testable only when evidence and ticket IDs are recorded.

For section fourteen point four, Ashgrove College will not accept threat work without a written trail.

### 14.5 Documentation

Each job: purpose, schedule, inputs, outputs, owner, alert recipient, how to disable it.

Section fourteen point five develops threat intelligence and osint automation with a Ashgrove College note Tomás Reyes can demo offline.

Under section fourteen point five, ESX expects threat claims to carry owners and dates.

Section fourteen point five treats suitable tasks unsuitable tasks as testable only when evidence and ticket IDs are recorded.

For section fourteen point five, Ashgrove College will not accept threat work without a written trail.

### 14.6 Never automated

Contact with suspicious sites, scanning, downloading samples, posting to public channels.

Section fourteen point six develops threat intelligence and osint automation with a Ashgrove College note Tomás Reyes can demo offline.

Under section fourteen point six, ESX expects threat claims to carry owners and dates.

Section fourteen point six treats suitable tasks unsuitable tasks as testable only when evidence and ticket IDs are recorded.

For section fourteen point six, Ashgrove College will not accept threat work without a written trail.

Section fourteen point six fails closed if threat evidence is missing rather than guessing.

### 14.7 Trial periods

New automation runs alongside manual work for two weeks; results are compared before switching.

Section fourteen point seven develops threat intelligence and osint automation with a Ashgrove College note Tomás Reyes can demo offline.

Under section fourteen point seven, ESX expects threat claims to carry owners and dates.

Section fourteen point seven treats suitable tasks unsuitable tasks as testable only when evidence and ticket IDs are recorded.

For section fourteen point seven, Ashgrove College will not accept threat work without a written trail.

### 14.8 Kill switch

Every job can be disabled quickly by the on-call person without editing code.

Section fourteen point eight develops threat intelligence and osint automation with a Ashgrove College note Tomás Reyes can demo offline.

Under section fourteen point eight, ESX expects threat claims to carry owners and dates.

Section fourteen point eight treats suitable tasks unsuitable tasks as testable only when evidence and ticket IDs are recorded.

For section fourteen point eight, Ashgrove College will not accept threat work without a written trail.

### 14.9 Review

Twice a year, jobs no longer serving a requirement are retired.

Section fourteen point nine develops threat intelligence and osint automation with a Ashgrove College note Tomás Reyes can demo offline.

Under section fourteen point nine, ESX expects threat claims to carry owners and dates.

Section fourteen point nine treats suitable tasks unsuitable tasks as testable only when evidence and ticket IDs are recorded.

For section fourteen point nine, Ashgrove College will not accept threat work without a written trail.

Section fourteen point nine fails closed if threat evidence is missing rather than guessing.

### Logging automated decisions

Every automated action writes what it received, which rule it applied and what it produced. When a lecturer asks why a site was blocked, the log answers in seconds. Logs also let the team measure how often each rule fires, which helps retire rules that never trigger and tune those that fire too often. Keep these logs for at least as long as the blocks they explain, and store them where the network and help-desk teams can read them during out-of-hours calls.

### Worked example

Tomás automates weekly counts by technique. During the two-week trial his script counts one item twice because ESX re-sent it with a new identifier. He adds deduplication by indicator value and the counts match his manual tally.

> **Synthetic case.** The duplicate is invented.

### Errors and limits

Automation repeats mistakes quickly; test with tricky cases.

### Exercises

- **EX053 — Auto-approval.** Which category may be auto-approved after a trial? *Rubric:* 3 = ESX GREEN domains graded B+; 2 = partial; 1 = all; 0 = none.
- **EX054 — Kill switch.** Why must every job have a quick disable method? *Rubric:* 3 = stop harm fast without code edits; 2 = partial; 1 = unnecessary; 0 = none.
- **EX055 — Trial catch.** What did the trial reveal about the weekly counts? *Rubric:* 3 = duplicate from re-sent item; dedupe by value; 2 = one; 1 = nothing; 0 = none.
- **EX056 — Job document.** List five fields documenting a job. *Rubric:* 3 = five of purpose, schedule, inputs, outputs, owner, alerts, disable; 2 = three; 1 = one; 0 = none.

### Synthesis

Automate rules, keep humans on judgment and high impact, monitor jobs, document them and keep a kill switch.

### Continue studying — chapter 14 of 18

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Threat intelligence and OSINT: integration and dependencies

### Learning outcomes

You will (1) connect CTI to help desk, network, email and incident teams; (2) agree service levels; (3) map dependencies on suppliers and partners; (4) plan for dependency failure.

### 15.1 Consumers

Help desk: current scams and what to tell callers. Network and email teams: block lists. Incident response: context during incidents. Management: monthly summary.

Section fifteen point one develops threat intelligence and osint integration with a Ashgrove College note Tomás Reyes can demo offline.

Under section fifteen point one, ESX expects threat claims to carry owners and dates.

Section fifteen point one treats consumers service levels dependencies as testable only when evidence and ticket IDs are recorded.

For section fifteen point one, Ashgrove College will not accept threat work without a written trail.

### 15.2 Service levels

Urgent items reviewed within four working hours; routine within two days; scam list each Monday in term time.

Section fifteen point two develops threat intelligence and osint integration with a Ashgrove College note Tomás Reyes can demo offline.

Under section fifteen point two, ESX expects threat claims to carry owners and dates.

Section fifteen point two treats consumers service levels dependencies as testable only when evidence and ticket IDs are recorded.

For section fifteen point two, Ashgrove College will not accept threat work without a written trail.

### 15.3 Dependencies

ESX membership and its TAXII server; the platform's hosting; the cloud email supplier's logs; the network team's DNS filter. Each can fail.

Section fifteen point three develops threat intelligence and osint integration with a Ashgrove College note Tomás Reyes can demo offline.

Under section fifteen point three, ESX expects threat claims to carry owners and dates.

Section fifteen point three treats consumers service levels dependencies as testable only when evidence and ticket IDs are recorded.

For section fifteen point three, Ashgrove College will not accept threat work without a written trail.

### 15.4 Failure plans

If ESX is unavailable, use national education advisories; if the platform fails, scripts can read ESX email alerts directly; if the DNS filter fails, the proxy carries urgent domain blocks.

Section fifteen point four develops threat intelligence and osint integration with a Ashgrove College note Tomás Reyes can demo offline.

Under section fifteen point four, ESX expects threat claims to carry owners and dates.

Section fifteen point four treats consumers service levels dependencies as testable only when evidence and ticket IDs are recorded.

### 15.5 Feedback loop

Help desk forwards suspicious messages reported by students and staff to the CTI queue; this is often the earliest warning.

Section fifteen point five develops threat intelligence and osint integration with a Ashgrove College note Tomás Reyes can demo offline.

Under section fifteen point five, ESX expects threat claims to carry owners and dates.

Section fifteen point five treats consumers service levels dependencies as testable only when evidence and ticket IDs are recorded.

For section fifteen point five, Ashgrove College will not accept threat work without a written trail.

### 15.6 Incident support

During incidents, Tomás follows the incident lead's priorities, as NIST SP 800-61r3 places intelligence within response.

Section fifteen point six develops threat intelligence and osint integration with a Ashgrove College note Tomás Reyes can demo offline.

Under section fifteen point six, ESX expects threat claims to carry owners and dates.

Section fifteen point six treats consumers service levels dependencies as testable only when evidence and ticket IDs are recorded.

For section fifteen point six, Ashgrove College will not accept threat work without a written trail.

### 15.7 Supplier intelligence

Advisories about the learning-platform supplier or the email supplier go to contract managers too, who can ask the supplier for assurance.

Section fifteen point seven develops threat intelligence and osint integration with a Ashgrove College note Tomás Reyes can demo offline.

Under section fifteen point seven, ESX expects threat claims to carry owners and dates.

Section fifteen point seven treats consumers service levels dependencies as testable only when evidence and ticket IDs are recorded.

For section fifteen point seven, Ashgrove College will not accept threat work without a written trail.

### 15.8 Calendar

Term starts, exam periods and enrolment bring scam peaks; the team plans extra monitoring then.

Section fifteen point eight develops threat intelligence and osint integration with a Ashgrove College note Tomás Reyes can demo offline.

Under section fifteen point eight, ESX expects threat claims to carry owners and dates.

Section fifteen point eight treats consumers service levels dependencies as testable only when evidence and ticket IDs are recorded.

For section fifteen point eight, Ashgrove College will not accept threat work without a written trail.

### Measuring integration

Count how often each consumer acted on CTI each month: blocks applied, help-desk scripts used, incident questions answered. Falling numbers may mean products no longer fit, prompting a conversation with that team.

### Worked example

During enrolment week, the help desk forwards forty reports of fake "fee payment" emails. Tomás identifies two sender domains, requests blocks, gives the help desk a script for callers and sends ESX a GREEN item. Two other colleges block the domains the same day.

> **Synthetic case.** The campaign is invented.

### Errors and limits

Fallbacks need testing; an untested plan may fail when needed.

### Exercises

- **EX057 — Fallback list.** Give the fallback for an ESX outage and for a platform failure. *Rubric:* 3 = national advisories; scripts read email alerts; 2 = one; 1 = none; 0 = none.
- **EX058 — Earliest warning.** Which consumer is often also the earliest source? *Rubric:* 3 = help desk reports; 2 = partial; 1 = management; 0 = none.
- **EX059 — Enrolment outputs.** List the four outputs from the enrolment-week case. *Rubric:* 3 = blocks, help desk script, ESX item, (identification of domains); 2 = two; 1 = one; 0 = none.
- **EX060 — Supplier advisory.** Who besides technical owners should receive supplier advisories? *Rubric:* 3 = contract managers; 2 = partial; 1 = students; 0 = none.

### Synthesis

Serve each consumer, set service levels, map dependencies with fallbacks and use the help desk as an early-warning source.

### Continue studying — chapter 15 of 18

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Technical documentation and safety

### Learning outcomes

You will (1) write runbooks for CTI tasks; (2) document safety and handling rules; (3) keep documentation current; (4) write so others can act without you.

### 16.1 Runbooks

A runbook describes a routine task step by step: "Importing the ESX daily collection", "Requesting a DNS block", "Handling a credential-exposure notice". Each has purpose, prerequisites, steps, checks and what to do if something fails.

Section sixteen point one develops technical documentation and safety with a Ashgrove College note Tomás Reyes can demo offline.

Under section sixteen point one, ESX expects technical claims to carry owners and dates.

Section sixteen point one treats runbooks safety rules handling as testable only when evidence and ticket IDs are recorded.

### 16.2 Safety rules

A one-page rule sheet: no contact with suspicious infrastructure; no testing of exposed passwords; TLP respected; personal data minimised; suspicious files handed to qualified staff; RFC 5737 addresses and .example domains in training material.

Section sixteen point two develops technical documentation and safety with a Ashgrove College note Tomás Reyes can demo offline.

Under section sixteen point two, ESX expects technical claims to carry owners and dates.

Section sixteen point two treats runbooks safety rules handling as testable only when evidence and ticket IDs are recorded.

### 16.3 Handling labels in documents

Runbooks themselves are usually internal (TLP:AMBER) because they reveal how defences work. Examples inside them use synthetic values.

Section sixteen point three develops technical documentation and safety with a Ashgrove College note Tomás Reyes can demo offline.

Under section sixteen point three, ESX expects technical claims to carry owners and dates.

Section sixteen point three treats runbooks safety rules handling as testable only when evidence and ticket IDs are recorded.

For section sixteen point three, Ashgrove College will not accept technical work without a written trail.

### 16.4 Currency

Each document shows owner, last review date and next review. Changes in tools trigger reviews.

Section sixteen point four develops technical documentation and safety with a Ashgrove College note Tomás Reyes can demo offline.

Under section sixteen point four, ESX expects technical claims to carry owners and dates.

Section sixteen point four treats runbooks safety rules handling as testable only when evidence and ticket IDs are recorded.

For section sixteen point four, Ashgrove College will not accept technical work without a written trail.

### 16.5 Writing style

Short numbered steps, one action each; screenshots only where needed; commands in code blocks; expected results stated after each step.

Section sixteen point five develops technical documentation and safety with a Ashgrove College note Tomás Reyes can demo offline.

Under section sixteen point five, ESX expects technical claims to carry owners and dates.

Section sixteen point five treats runbooks safety rules handling as testable only when evidence and ticket IDs are recorded.

For section sixteen point five, Ashgrove College will not accept technical work without a written trail.

### 16.6 Testing documentation

A colleague follows the runbook without help. Wherever they hesitate, the text is unclear.

Section sixteen point six develops technical documentation and safety with a Ashgrove College note Tomás Reyes can demo offline.

Under section sixteen point six, ESX expects technical claims to carry owners and dates.

Section sixteen point six treats runbooks safety rules handling as testable only when evidence and ticket IDs are recorded.

For section sixteen point six, Ashgrove College will not accept technical work without a written trail.

### 16.7 Version history

Keep documents in the team's repository so changes are tracked and reversible.

Section sixteen point seven develops technical documentation and safety with a Ashgrove College note Tomás Reyes can demo offline.

Under section sixteen point seven, ESX expects technical claims to carry owners and dates.

Section sixteen point seven treats runbooks safety rules handling as testable only when evidence and ticket IDs are recorded.

For section sixteen point seven, Ashgrove College will not accept technical work without a written trail.

Section sixteen point seven fails closed if technical evidence is missing rather than guessing.

### 16.8 Incident notes

During incidents, write timestamped notes in a shared document; they later become the basis for review.

Section sixteen point eight develops technical documentation and safety with a Ashgrove College note Tomás Reyes can demo offline.

Under section sixteen point eight, ESX expects technical claims to carry owners and dates.

Section sixteen point eight treats runbooks safety rules handling as testable only when evidence and ticket IDs are recorded.

For section sixteen point eight, Ashgrove College will not accept technical work without a written trail.

### 16.9 Accessibility

Plain language helps colleagues whose first language differs and newcomers alike.

Section sixteen point nine develops technical documentation and safety with a Ashgrove College note Tomás Reyes can demo offline.

Under section sixteen point nine, ESX expects technical claims to carry owners and dates.

Section sixteen point nine treats runbooks safety rules handling as testable only when evidence and ticket IDs are recorded.

For section sixteen point nine, Ashgrove College will not accept technical work without a written trail.

Section sixteen point nine fails closed if technical evidence is missing rather than guessing.

### Glossary

A short glossary defines TLP, ATT&CK, STIX, indicator and runbook terms once, so documents stay brief and consistent for every reader.

### Worked example

Tomás writes the runbook for credential-exposure notices. His colleague tests it and stops at "notify the identity team" — which channel? Tomás adds: "open a restricted ticket in the Identity queue; never paste passwords; attach the list as an encrypted file". The next test runs without questions.

> **Synthetic case.** The runbook test is invented.

### Errors and limits

Documentation cannot replace judgment; runbooks state when to escalate.

### Exercises

- **EX061 — Runbook parts.** List five parts of a runbook. *Rubric:* 3 = purpose, prerequisites, steps, checks, failure actions; 2 = three; 1 = one; 0 = none.
- **EX062 — Runbook label.** Why are runbooks usually internal? *Rubric:* 3 = reveal defensive workings; 2 = partial; 1 = public; 0 = none.
- **EX063 — Hesitation test.** How was the credential runbook improved? *Rubric:* 3 = specified restricted ticket, no passwords, encrypted attachment; 2 = partial; 1 = none; 0 = none.
- **EX064 — Safety sheet.** Name four rules on the safety sheet. *Rubric:* 3 = four valid; 2 = three; 1 = one; 0 = none.

### Synthesis

Write tested, current, plain runbooks; keep safety rules visible; label documents appropriately.

### Continue studying — chapter 16 of 18

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Contained laboratory II

### Learning outcomes

You will (1) produce an internal and a community weekly summary from the same data; (2) filter by TLP correctly; (3) explain withheld items without revealing them; (4) check summaries before release.

### 17.1 Lab rules

Offline, synthetic, standard library. Students work in pairs and submit both summaries and a short check record.

Section seventeen point one develops contained laboratory ii with a Ashgrove College note Tomás Reyes can demo offline.

Under section seventeen point one, ESX expects contained claims to carry owners and dates.

Section seventeen point one treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

For section seventeen point one, Ashgrove College will not accept contained work without a written trail.

### Lab — two summaries

```python
"""Lab (ch 17): weekly summary by technique with a TLP filter for the community version (synthetic)."""
from collections import Counter
items = [("T1566", "TLP:GREEN"), ("T1566", "TLP:CLEAR"), ("T1078", "TLP:AMBER"), ("T1566", "TLP:AMBER"),
         ("T1190", "TLP:GREEN"), ("T1078", "TLP:GREEN"), ("T1486", "TLP:RED")]
internal = Counter(t for t, _ in items)
community = Counter(t for t, l in items if l in ("TLP:CLEAR", "TLP:GREEN"))
print("internal", dict(sorted(internal.items())))
print("community", dict(sorted(community.items())))
print("withheld from community:", len(items) - sum(community.values()))
```

Run with `python3 lab_weekly.py`. Verified output:

```text
internal {'T1078': 2, 'T1190': 1, 'T1486': 1, 'T1566': 3}
community {'T1078': 1, 'T1190': 1, 'T1566': 2}
withheld from community: 3
```

### 17.2 Reading the result

The internal summary counts all seven items: Phishing (T1566) 3, Valid Accounts (T1078) 2, Exploit Public-Facing Application (T1190) 1, Data Encrypted for Impact (T1486) 1. The community version counts only CLEAR and GREEN items: T1566 2, T1078 1, T1190 1. Three items are withheld — two AMBER and one RED.

Section seventeen point two develops contained laboratory ii with a Ashgrove College note Tomás Reyes can demo offline.

Under section seventeen point two, ESX expects contained claims to carry owners and dates.

Section seventeen point two treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

### 17.3 Mentioning withheld items

The community summary may say "some items were withheld under their handling labels" but must not describe them. Even "a ransomware item was received under RED" could reveal too much.

Section seventeen point three develops contained laboratory ii with a Ashgrove College note Tomás Reyes can demo offline.

Under section seventeen point three, ESX expects contained claims to carry owners and dates.

Section seventeen point three treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

### 17.4 Checking before release

The partner student checks: every included item is CLEAR or GREEN; no personal data; counts match the script; wording reveals nothing about withheld items.

Section seventeen point four develops contained laboratory ii with a Ashgrove College note Tomás Reyes can demo offline.

Under section seventeen point four, ESX expects contained claims to carry owners and dates.

Section seventeen point four treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

For section seventeen point four, Ashgrove College will not accept contained work without a written trail.

### 17.5 Internal value

The internal summary helps management see that phishing dominates and that one ransomware-related item arrived, prompting a backup check.

Section seventeen point five develops contained laboratory ii with a Ashgrove College note Tomás Reyes can demo offline.

Under section seventeen point five, ESX expects contained claims to carry owners and dates.

Section seventeen point five treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

For section seventeen point five, Ashgrove College will not accept contained work without a written trail.

### 17.6 Format

Each summary: period, counts by technique, top actions taken, requests to readers.

Section seventeen point six develops contained laboratory ii with a Ashgrove College note Tomás Reyes can demo offline.

Under section seventeen point six, ESX expects contained claims to carry owners and dates.

Section seventeen point six treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

For section seventeen point six, Ashgrove College will not accept contained work without a written trail.

Section seventeen point six fails closed if contained evidence is missing rather than guessing.

### 17.7 Common mistakes

Forgetting AMBER+STRICT; including technique counts that could only come from a RED item; copying internal notes into the community version.

Section seventeen point seven develops contained laboratory ii with a Ashgrove College note Tomás Reyes can demo offline.

Under section seventeen point seven, ESX expects contained claims to carry owners and dates.

Section seventeen point seven treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

For section seventeen point seven, Ashgrove College will not accept contained work without a written trail.

### 17.8 Reflection

Students note how the two audiences changed what they wrote.

Section seventeen point eight develops contained laboratory ii with a Ashgrove College note Tomás Reyes can demo offline.

Under section seventeen point eight, ESX expects contained claims to carry owners and dates.

Section seventeen point eight treats lab rules reading the as testable only when evidence and ticket IDs are recorded.

For section seventeen point eight, Ashgrove College will not accept contained work without a written trail.

Section seventeen point eight fails closed if contained evidence is missing rather than guessing.

### Time for checking

Allow at least fifteen minutes for the partner check; rushing it is how leaks happen.

### Worked example

Tomás's first community draft includes the phrase "plus one encryption-related item under RED". His partner flags it. He removes it; the summary now says only "items under restricted labels were not included".

> **Synthetic case.** The lab data is invented teaching material.

### Errors and limits

Filtering by label assumes labels are right; check suspicious labels with the source.

### Exercises

- **EX065 — Lab counts.** Give the internal and community counts for T1566. *Rubric:* 3 = internal 3, community 2; 2 = one; 1 = wrong; 0 = none.
- **EX066 — Withheld count.** How many items were withheld and why? *Rubric:* 3 = 3: two AMBER, one RED; 2 = number; 1 = wrong; 0 = none.
- **EX067 — Leaky phrase.** Why was "one encryption-related item under RED" removed? *Rubric:* 3 = reveals RED content; 2 = partial; 1 = harmless; 0 = none.
- **EX068 — Release checks.** List four checks before releasing the community summary. *Rubric:* 3 = labels, no personal data, counts match, nothing about withheld; 2 = three; 1 = one; 0 = none.

### Synthesis

Build both summaries from one dataset, filter strictly, reveal nothing about withheld items and check before release.

### Continue studying — chapter 17 of 18

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Supervised technical project

### Learning outcomes

You will (1) deliver a small CTI improvement under supervision; (2) plan, build, test and hand over; (3) measure the result; (4) present it to the team.

### 18.1 Choosing the project

Tomás proposes automating the Monday scam list for the help desk: collect the week's confirmed scam reports from the CTI queue, group by theme, add sample subject lines with personal data removed and advice for callers.

Section eighteen point one develops supervised technical project with a Ashgrove College note Tomás Reyes can demo offline.

Under section eighteen point one, ESX expects supervised claims to carry owners and dates.

Section eighteen point one treats choosing the project plan as testable only when evidence and ticket IDs are recorded.

### 18.2 Plan

Week 1: requirements with the help-desk lead. Week 2: build on synthetic data. Week 3: test with past weeks' data on the college server. Week 4: report-only run. Week 5: handover.

Section eighteen point two develops supervised technical project with a Ashgrove College note Tomás Reyes can demo offline.

Under section eighteen point two, ESX expects supervised claims to carry owners and dates.

Section eighteen point two treats choosing the project plan as testable only when evidence and ticket IDs are recorded.

For section eighteen point two, Ashgrove College will not accept supervised work without a written trail.

### 18.3 Safety and privacy

Reports contain names and email addresses of students and staff. The script strips them; a person checks each list before release. Only the help desk receives it.

Section eighteen point three develops supervised technical project with a Ashgrove College note Tomás Reyes can demo offline.

Under section eighteen point three, ESX expects supervised claims to carry owners and dates.

Section eighteen point three treats choosing the project plan as testable only when evidence and ticket IDs are recorded.

For section eighteen point three, Ashgrove College will not accept supervised work without a written trail.

### 18.4 Measures

Time to produce the list (before: two hours; target: thirty minutes); help-desk satisfaction; accuracy of grouping checked by the supervisor.

Section eighteen point four develops supervised technical project with a Ashgrove College note Tomás Reyes can demo offline.

Under section eighteen point four, ESX expects supervised claims to carry owners and dates.

Section eighteen point four treats choosing the project plan as testable only when evidence and ticket IDs are recorded.

For section eighteen point four, Ashgrove College will not accept supervised work without a written trail.

### 18.5 Handover

Runbook, job documentation, owner (the CTI team), kill switch and a short training session for the help-desk lead.

Section eighteen point five develops supervised technical project with a Ashgrove College note Tomás Reyes can demo offline.

Under section eighteen point five, ESX expects supervised claims to carry owners and dates.

Section eighteen point five treats choosing the project plan as testable only when evidence and ticket IDs are recorded.

For section eighteen point five, Ashgrove College will not accept supervised work without a written trail.

### 18.6 Presentation

Ten minutes: problem, solution, results, limits, next steps.

Section eighteen point six develops supervised technical project with a Ashgrove College note Tomás Reyes can demo offline.

Under section eighteen point six, ESX expects supervised claims to carry owners and dates.

Section eighteen point six treats choosing the project plan as testable only when evidence and ticket IDs are recorded.

For section eighteen point six, Ashgrove College will not accept supervised work without a written trail.

Section eighteen point six fails closed if supervised evidence is missing rather than guessing.

### 18.7 Supervision

Weekly meetings with the supervisor review progress and risks. Decisions are recorded.

Section eighteen point seven develops supervised technical project with a Ashgrove College note Tomás Reyes can demo offline.

Under section eighteen point seven, ESX expects supervised claims to carry owners and dates.

Section eighteen point seven treats choosing the project plan as testable only when evidence and ticket IDs are recorded.

For section eighteen point seven, Ashgrove College will not accept supervised work without a written trail.

Section eighteen point seven fails closed if supervised evidence is missing rather than guessing.

### 18.8 Limits

The tool groups by keywords; new scam themes may need manual grouping.

Section eighteen point eight develops supervised technical project with a Ashgrove College note Tomás Reyes can demo offline.

Under section eighteen point eight, ESX expects supervised claims to carry owners and dates.

Section eighteen point eight treats choosing the project plan as testable only when evidence and ticket IDs are recorded.

For section eighteen point eight, Ashgrove College will not accept supervised work without a written trail.

Section eighteen point eight fails closed if supervised evidence is missing rather than guessing.

### 18.9 Reflection

What worked, what he would change, what he learned about users.

Section eighteen point nine develops supervised technical project with a Ashgrove College note Tomás Reyes can demo offline.

Under section eighteen point nine, ESX expects supervised claims to carry owners and dates.

Section eighteen point nine treats choosing the project plan as testable only when evidence and ticket IDs are recorded.

For section eighteen point nine, Ashgrove College will not accept supervised work without a written trail.

Section eighteen point nine fails closed if supervised evidence is missing rather than guessing.

### Stakeholder sign-off

At the end, the help-desk lead signs a short acceptance note stating that the list meets their needs, and the CTI supervisor confirms ownership. Without both signatures, a student project often stops working when the student leaves.

### Worked example

In the report-only run, the tool groups "library fine" and "parking fine" scams together. The help-desk lead says callers need them separate. Tomás adds a rule, and the next run's grouping matches the supervisor's manual check. Production time falls to twenty-five minutes.

> **Synthetic case.** The project and figures are invented.

### Errors and limits

Small projects show value but need continued ownership to last.

### Exercises

- **EX069 — Project plan.** Summarise the five-week plan. *Rubric:* 3 = requirements, build synthetic, test past data, report-only, handover; 2 = three; 1 = one; 0 = none.
- **EX070 — Privacy step.** How does the scam list protect personal data? *Rubric:* 3 = script strips names/emails; human check; help desk only; 2 = two; 1 = one; 0 = none.
- **EX071 — Grouping fix.** What grouping problem appeared and how was it fixed? *Rubric:* 3 = library/parking fines merged; rule added after help-desk feedback; 2 = partial; 1 = none; 0 = none.
- **EX072 — Time result.** Did the project meet its time target? *Rubric:* 3 = yes, 25 min vs 30 target (from 2 h); 2 = yes; 1 = no; 0 = none.

### Synthesis

Plan with users, build safely, test with real past data under control, measure, hand over and reflect.

### Continue studying — chapter 18 of 18

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX072. Ashgrove College, Tomás Reyes, the Education Security Exchange and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Exploit Public-Facing Application (T1190), because the platform and gateway are internet-reachable, and Phishing (T1566), because email reaches every user.

**EX002.** The supplier contract keeps sign-in logs for only 30 days, so older records no longer exist.

**EX003.** Every service that relies on the directory for logins becomes reachable with the stolen credentials.

**EX004.** Network-level controls such as Wi-Fi segmentation and DNS filtering, plus advice to students, because the college cannot manage their devices.

**EX005.** Students' devices use the campus resolvers when on Wi-Fi, so their lookups are logged even without agents.

**EX006.** He converted the firewall timestamps to UTC and used the Wi-Fi translation log to find which device held that mapping at that time.

**EX007.** Attackers carrying command traffic inside normal web, DNS or mail protocols; regular connections to a rarely visited domain are one clue.

**EX008.** It is the student's own device; the college has no authority to inspect it, so it blocked network access and gave advice instead.

**EX009.** Many students reuse passwords from other sites, so leaked credentials often work on college accounts.

**EX010.** Separate administrator accounts with strong multi-factor authentication, and no mailbox on those accounts.

**EX011.** Each search is linked to a specific intelligence item and logged, and analysts do not browse individual students' activity.

**EX012.** Passwords were reset, sessions revoked and accessed resources checked; student multi-factor authentication was also prioritised.

**EX013.** M2, from the lookalike ashgrove-payments.example, failed DMARC; M3 claimed ashgrove.example but failed SPF, DKIM and DMARC, suggesting spoofing.

**EX014.** It proves the sender is authorised for partner-uni.example; it does not prove the content is safe, since a hijacked partner mailbox would pass too.

**EX015.** Only headers added by Ashgrove's own gateway; earlier headers could have been written by the sender.

**EX016.** Output "unparsed" with the raw header for a human to check, without crashing the run.

**EX017.** No. Visiting it contacts adversary infrastructure from a college device, which policy forbids.

**EX018.** Handle it as TLP:AMBER until the sender states the intended label.

**EX019.** Tell his supervisor and the recipient at once so the material can be deleted and the error recorded.

**EX020.** No. Vendor terms usually forbid that; he should summarise briefly with attribution and link to the original.

**EX021.** The network team owns the DNS filter; the email team owns the gateway.

**EX022.** ESX alerts reached only the supervisor's inbox; a shared mailbox with two readers removed that single point of failure.

**EX023.** Delivery — they stop malicious messages before users receive them.

**EX024.** Reconnaissance; no output addresses it, so the team should decide whether that gap matters.

**EX025.** The proxy keeps logs for only 30 days, so any visits 40 days ago had already been deleted.

**EX026.** Only the lines that match the indicator, with the fields needed such as time, host and indicator.

**EX027.** DNS resolver logs cover every campus device; endpoint events cover only college-managed machines.

**EX028.** Techniques for which no available log source could show the behaviour — blind spots to fix or accept.

**EX029.** A false positive caused by a stale indicator: the cloud address had been reassigned to the revision website.

**EX030.** Differences in normalisation such as trailing dots, and logs that are missing or already deleted by retention.

**EX031.** A process weakness — for example, unclear rules or tools that strip labels — rather than individual carelessness.

**EX032.** The expiry period for address indicators was shortened to 30 days.

**EX033.** Only the domain registration has been observed — resource development (T1583); no phishing messages have been seen yet.

**EX034.** B because certificate-transparency logs are usually reliable; 2 because impersonation is probable but not confirmed.

**EX035.** The platform contains only what sources sent; unshared or unseen threats will be missing.

**EX036.** Whether the domain belongs to a legitimate group connected to the college, such as a student society.

**EX037.** Addresses 30 days and domains 90 days, because addresses are reassigned to new users much faster than domains change owner.

**EX038.** It stopped the export from blocking a file-sharing domain that lecturers rely on.

**EX039.** Quarantining macro-enabled documents arriving from external senders at the email gateway.

**EX040.** A mistaken block during exams could stop students reaching essential services when disruption hurts most.

**EX041.** It sat on a large content-delivery service with a long legitimate history, had a certificate from a reputable owner, and no college device had looked it up.

**EX042.** That the machine may be infected and repeatedly trying to reach the blocked domain, so it should be investigated.

**EX043.** He should ask what observation each report is based on.

**EX044.** Visiting the suspicious site, downloading files from it or scanning its servers from college systems.

**EX045.** ws-fin-11 → service desk plus Finance; srv-lms-01 → incident response (server); ws-lab-99 → unknown asset, ask the network team.

**EX046.** A server contacting a command address may be compromised and affects many users, so it needs immediate incident handling.

**EX047.** A gap in the asset inventory; the network team identifies the device and it is added to the owner list.

**EX048.** Real names would expose college systems outside the lab; coursework uses only synthetic values.

**EX049.** A resolver update added a first column, shifting fields; parsing by field name and a zero-parse warning fixed it for good.

**EX050.** Changing one thing at a time shows which change solved the problem and avoids new faults.

**EX051.** Start time, inputs read, counts at each stage and any errors.

**EX052.** To catch matches missed while the parser was broken — three were found.

**EX053.** Domains from ESX labelled TLP:GREEN with a source grade of B or better, once the trial is agreed with the network team.

**EX054.** So a misbehaving job can be stopped immediately by on-call staff without waiting for someone to change code.

**EX055.** An item ESX re-sent with a new identifier was counted twice; deduplicating by indicator value fixed it.

**EX056.** Purpose, schedule, inputs, outputs and owner (also alert recipient and how to disable it).

**EX057.** National education advisories replace ESX; scripts reading ESX email alerts replace the platform.

**EX058.** The help desk, because students and staff report suspicious messages there first.

**EX059.** Block requests for the two sender domains, a script for help desk callers and a GREEN item shared with ESX, after identifying the domains.

**EX060.** Contract managers, who can ask the supplier for assurance.

**EX061.** Purpose, prerequisites, numbered steps, checks after steps, and what to do if a step fails.

**EX062.** They describe how the college's defences operate, which would help an attacker.

**EX063.** The step now says to open a restricted ticket in the Identity queue, never paste passwords and attach the list as an encrypted file.

**EX064.** No contact with suspicious infrastructure, no testing exposed passwords, respect TLP, and hand suspicious files to qualified staff.

**EX065.** Internal: 3; community: 2.

**EX066.** Three items: two labelled TLP:AMBER and one TLP:RED, none allowed in a community product.

**EX067.** It disclosed the topic of a RED item to people who are not its named recipients.

**EX068.** Every item is CLEAR or GREEN, no personal data remains, counts match the script, and nothing describes withheld items.

**EX069.** Requirements in week 1, build on synthetic data in week 2, test on past data in week 3, report-only run in week 4, handover in week 5.

**EX070.** The script removes names and email addresses, a person checks every list before release, and only the help desk receives it.

**EX071.** Library-fine and parking-fine scams were merged; a separation rule was added after the help-desk lead explained callers need them apart.

**EX072.** Yes. Production fell from two hours to twenty-five minutes, inside the thirty-minute target.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing.

- Bianco, D. (2013). The Pyramid of Pain. <https://detect-respond.blogspot.com/2013/03/the-pyramid-of-pain.html>
- Caltagirone, S., Pendergast, A. and Betz, C. (2013). The Diamond Model of Intrusion Analysis. Technical Report ADA586960, Center for Cyber Intelligence Analysis and Threat Research. <https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf>
- European Union. Regulation (EU) 2016/679 (General Data Protection Regulation). <https://eur-lex.europa.eu/eli/reg/2016/679/oj>
- FIRST. Traffic Light Protocol (TLP) version 2.0. <https://www.first.org/tlp/>
- Heuer, R. J. (1999). Psychology of Intelligence Analysis. CIA Center for the Study of Intelligence. <https://www.cia.gov/resources/csi/books-monographs/psychology-of-intelligence-analysis-2/>
- Hutchins, E. M., Cloppert, M. J. and Amin, R. M. (2011). Intelligence-Driven Computer Network Defense Informed by Analysis of Adversary Campaigns and Intrusion Kill Chains. Lockheed Martin. <https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf>
- Kent, S. (1964). Words of Estimative Probability. CIA Studies in Intelligence. <https://www.cia.gov/resources/csi/static/Words-of-Estimative-Probability.pdf>
- MITRE ATT&CK Enterprise matrix, groups, software and technique pages. <https://attack.mitre.org/>
- NIST SP 800-150 (2016). Guide to Cyber Threat Information Sharing. <https://doi.org/10.6028/NIST.SP.800-150>
- NIST SP 800-61 Rev. 3 (2025). Incident Response Recommendations and Considerations for Cybersecurity Risk Management. <https://doi.org/10.6028/NIST.SP.800-61r3>
- OASIS. STIX Version 2.1 (Committee Specification / OASIS Standard). <https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html>
- OASIS. TAXII Version 2.1. <https://docs.oasis-open.org/cti/taxii/v2.1/taxii-v2.1.html>
- ODNI. Intelligence Community Directive 203: Analytic Standards (2015, amended 2022). <https://www.odni.gov/files/documents/ICD/ICD-203.pdf>
