# Threat Intelligence and OSINT: A Technologist Book

- Language: English (`en`); technologist course, three years.
- Editorial state: **draft**. Chapters 1–30 of 30 have hand-written teaching text; exercises EX001–EX090 have matching worked results with 0–3 rubrics; five offline labs use only the Python 3 standard library on synthetic data, with outputs embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technologist students preparing for hands-on cyber threat intelligence (CTI) support roles in security teams.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical boundary: no collection on real private individuals, no terms-of-service evasion, no deanonymisation, no contact with adversary infrastructure. Organisations, people and indicators are **synthetic** unless a sentence cites a public source; addresses use RFC 5737 ranges and domains use `.example`.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Chapters 1–9 build computing, network, programming, data, security, identity, architecture and evidence foundations through intelligence examples (labs on refanging indicators and reading STIX). Chapters 10–23 teach CTI orientation, context, data flows, risk scenarios, methods, a guided lab, tooling, controls, monitoring, troubleshooting, integration, automation and evaluation (labs on deduplication, log matching and indicator expiry). Chapters 24–30 cover research methods, a team studio, handoff, deployment, field practice and the capstone. Each chapter has outcomes, teaching, a worked example, a labelled synthetic case, errors and limits, three exercises scored 0–3, a synthesis and a **Continue studying** block.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Corvale Municipal Services (CMS)** — a city's IT for council offices, libraries, permits and payments portals | Organisation served by CTI | Invented |
| **Lena Park** | Technologist student on a work-study post in the CMS security team | Invented |
| **Municipal Cyber Exchange (MCX)** | Regional community of local governments sharing intelligence under TLP 2.0 | Invented |

### Core sources

MITRE [ATT&CK](https://attack.mitre.org/); OASIS [STIX 2.1](https://docs.oasis-open.org/cti/stix/v2.1/stix-v2.1.html) and [TAXII 2.1](https://docs.oasis-open.org/cti/taxii/v2.1/taxii-v2.1.html); [Diamond Model](https://www.activeresponse.org/wp-content/uploads/2013/07/diamond.pdf); Hutchins et al. [kill chain](https://www.lockheedmartin.com/content/dam/lockheed-martin/rms/documents/cyber/LM-White-Paper-Intel-Driven-Defense.pdf); NIST [SP 800-150](https://doi.org/10.6028/NIST.SP.800-150); FIRST [TLP 2.0](https://www.first.org/tlp/); [ICD 203](https://www.odni.gov/files/documents/ICD/ICD-203.pdf). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) |
| [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) |
| [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Computing systems

### Learning outcomes

You will (1) map the computing estate of a municipal IT service; (2) identify which systems hold evidence useful to CTI; (3) explain why public-facing services attract attackers; (4) keep an asset list good enough for intelligence matching.

### 1.1 A city's estate

Corvale Municipal Services runs desktops for council staff, library public-access computers, a permits portal, a payments portal, email, a directory, file servers and a backup system. Each serves residents or staff and each can be the target or the evidence source in an intrusion.

Section one point one develops computing systems with a Corvale Municipal Services note Lena Park can demo offline.

Under section one point one, MCX expects computing claims to carry owners and dates.

Section one point one treats city's estate public-facing systems as testable only when evidence and ticket IDs are recorded.

### 1.2 Public-facing systems

The permits and payments portals are reachable from the internet. Exploit Public-Facing Application (T1190) in MITRE ATT&CK describes attackers abusing weaknesses in such services. Intelligence about vulnerabilities in the portal software therefore has direct value to CMS.

Section one point two develops computing systems with a Corvale Municipal Services note Lena Park can demo offline.

Under section one point two, MCX expects computing claims to carry owners and dates.

Section one point two treats city's estate public-facing systems as testable only when evidence and ticket IDs are recorded.

### 1.3 Library computers

Public-access machines are used by anyone. They are reset daily, have no staff accounts and sit on a separate network. Intelligence about malware spreading by USB matters here; intelligence about executive phishing does not.

Section one point three develops computing systems with a Corvale Municipal Services note Lena Park can demo offline.

Under section one point three, MCX expects computing claims to carry owners and dates.

Section one point three treats city's estate public-facing systems as testable only when evidence and ticket IDs are recorded.

### 1.4 Evidence holders

Email gateway, web proxy, DNS resolver, directory and endpoint agents keep logs. Lena lists each, its retention period and who can query it, because an indicator nobody can search for is useless.

Section one point four develops computing systems with a Corvale Municipal Services note Lena Park can demo offline.

Under section one point four, MCX expects computing claims to carry owners and dates.

Section one point four treats city's estate public-facing systems as testable only when evidence and ticket IDs are recorded.

### 1.5 The asset list

A spreadsheet of product, version, owner and exposure (internet, internal, public-access) is enough to start. When MCX shares an advisory, Lena checks the product column first.

Section one point five develops computing systems with a Corvale Municipal Services note Lena Park can demo offline.

Under section one point five, MCX expects computing claims to carry owners and dates.

Section one point five treats city's estate public-facing systems as testable only when evidence and ticket IDs are recorded.

For section one point five, Corvale Municipal Services will not accept computing work without a written trail.

### 1.6 Keeping it current

Every change ticket that adds or removes a system updates the list. Lena checks the list against the network team's scan results each quarter and flags differences to owners.

Section one point six develops computing systems with a Corvale Municipal Services note Lena Park can demo offline.

Under section one point six, MCX expects computing claims to carry owners and dates.

Section one point six treats city's estate public-facing systems as testable only when evidence and ticket IDs are recorded.

For section one point six, Corvale Municipal Services will not accept computing work without a written trail.

### Worked example

MCX warns about a flaw in a document-management product. Lena searches the asset list: CMS runs it internally for planning records, version 7.2, not internet-facing. She sends the advisory to the owner marked "internal exposure, patch in normal cycle unless exploitation is reported", rather than raising an emergency.

> **Synthetic case.** CMS, the product and the advisory are invented.

### Errors and limits

Shadow IT — systems departments bought without telling IT — will be missing from the list. Ask departments directly.

### Exercises

- **EX001 — Portal technique.** Which ATT&CK technique describes abuse of the payments portal's software flaws? *Rubric:* 3 = T1190 Exploit Public-Facing Application with reason; 2 = name; 1 = T1566; 0 = none.
- **EX002 — Library relevance.** Why is executive-phishing intelligence low priority for library computers? *Rubric:* 3 = no staff accounts/email, reset daily, separate network; 2 = one; 1 = high priority; 0 = none.
- **EX003 — Exposure call.** How did exposure change Lena's handling of the document-management advisory? *Rubric:* 3 = internal-only → normal patch cycle unless exploited; 2 = partial; 1 = emergency; 0 = none.

### Synthesis

Know the estate, its exposure and its logs; keep a simple, current asset list so intelligence can be matched quickly.

### Continue studying — chapter 01 of 30

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Networks and internet services

### Learning outcomes

You will (1) explain how DNS, web and email services expose indicators; (2) read a resolver log line; (3) use public DNS data passively; (4) understand the role of address ranges reserved for documentation.

### 2.1 Services residents use

Residents reach CMS through the website, the permits portal and email. Each depends on DNS records that CMS publishes. Attackers imitate these names with lookalike domains to trick residents into paying fake fees.

Section two point one develops networks and internet services with a Corvale Municipal Services note Lena Park can demo offline.

Under section two point one, MCX expects networks claims to carry owners and dates.

Section two point one treats services residents use resolver as testable only when evidence and ticket IDs are recorded.

### 2.2 Resolver logs

A resolver log line typically records time, client, queried name and answer. Lena reads lines such as "08:03 ws-114 pay-portal.example". The client tells her which machine asked; the name tells her whether it matches an indicator.

Section two point two develops networks and internet services with a Corvale Municipal Services note Lena Park can demo offline.

Under section two point two, MCX expects networks claims to carry owners and dates.

Section two point two treats services residents use resolver as testable only when evidence and ticket IDs are recorded.

### 2.3 Passive DNS data

Some services publish historical DNS resolutions collected from many resolvers. Looking up a name there is passive: CMS does not contact the suspicious server. Lena may use services CMS has approved and whose terms allow this use.

Section two point three develops networks and internet services with a Corvale Municipal Services note Lena Park can demo offline.

Under section two point three, MCX expects networks claims to carry owners and dates.

Section two point three treats services residents use resolver as testable only when evidence and ticket IDs are recorded.

### 2.4 Mail flow

Email enters through CMS's gateway, which logs sender, recipient, subject and attachment names. Phishing (T1566) indicators — sender domains, subjects, attachment hashes — are checked here.

Section two point four develops networks and internet services with a Corvale Municipal Services note Lena Park can demo offline.

Under section two point four, MCX expects networks claims to carry owners and dates.

Section two point four treats services residents use resolver as testable only when evidence and ticket IDs are recorded.

For section two point four, Corvale Municipal Services will not accept networks work without a written trail.

### 2.5 Documentation addresses

This course uses the ranges 192.0.2.0/24, 198.51.100.0/24 and 203.0.113.0/24, which RFC 5737 reserves for documentation, and the .example domain. Real addresses never appear in teaching material, so nobody blocks or investigates an innocent party by copying an example.

Section two point five develops networks and internet services with a Corvale Municipal Services note Lena Park can demo offline.

Under section two point five, MCX expects networks claims to carry owners and dates.

Section two point five treats services residents use resolver as testable only when evidence and ticket IDs are recorded.

### 2.6 Ports and protocols

Web services use 443 (HTTPS); mail uses 25 between servers. Traffic from office desktops to unusual ports is worth noting, but council applications sometimes use odd ports legitimately — check with owners before treating it as suspicious.

Section two point six develops networks and internet services with a Corvale Municipal Services note Lena Park can demo offline.

Under section two point six, MCX expects networks claims to carry owners and dates.

Section two point six treats services residents use resolver as testable only when evidence and ticket IDs are recorded.

### Worked example

Residents report a text message linking to "corvale-permits-pay.example". Lena checks passive DNS through the approved service: the name first resolved three days ago. The resolver log shows two staff machines also looked it up after receiving the same text on work phones. She reports both findings to her supervisor.

> **Synthetic case.** The message and domain are invented.

### Errors and limits

Passive DNS coverage is incomplete; absence of records does not prove a name is unused.

### Exercises

- **EX004 — Log reading.** In "08:03 ws-114 pay-portal.example", what are the three fields? *Rubric:* 3 = time, client host, queried name; 2 = two; 1 = one; 0 = none.
- **EX005 — Passive meaning.** Why is a passive DNS lookup acceptable when visiting the site is not? *Rubric:* 3 = no contact with suspect server; approved service/terms; 2 = partial; 1 = both fine; 0 = none.
- **EX006 — Reserved ranges.** Why does teaching material use RFC 5737 addresses? *Rubric:* 3 = reserved for documentation; avoids harming real parties; 2 = partial; 1 = random; 0 = none.

### Synthesis

DNS, web and mail logs reveal indicator contact; use passive data through approved services and teach only with reserved examples.

### Continue studying — chapter 02 of 30

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming foundations

### Learning outcomes

You will (1) write small Python scripts that handle indicators as text; (2) refang defanged values safely; (3) validate addresses with the standard library; (4) keep scripts free of network activity.

### 3.1 Defanging

Analysts write "pay-portal[.]example" or "hxxps://" so that links in reports cannot be clicked by accident. Scripts must convert these back to normal form — refang — before matching against logs, but only as text.

Section three point one develops programming foundations with a Corvale Municipal Services note Lena Park can demo offline.

Under section three point one, MCX expects programming claims to carry owners and dates.

Section three point one treats defanging reading the result as testable only when evidence and ticket IDs are recorded.

### Lab — refang and classify

```python
"""Lab (ch 03): refang defanged indicators safely as text and classify them (synthetic; no network)."""
import ipaddress
raw = ["hxxps://pay-portal[.]example/login", "198.51.100[.]23", "update-svc[.]example", "203.0.113.300", "notes"]
for r in raw:
    v = r.replace("[.]", ".").replace("hxxp", "http")
    host = v.split("//")[-1].split("/")[0]
    try:
        ipaddress.ip_address(host); kind = "ipv4"
    except ValueError:
        kind = "domain" if "." in host and not host.replace(".", "").isdigit() else "invalid"
    print(f"{r} -> {host} [{kind}]")
```

Run with `python3 lab_defang.py`. Verified output:

```text
hxxps://pay-portal[.]example/login -> pay-portal.example [domain]
198.51.100[.]23 -> 198.51.100.23 [ipv4]
update-svc[.]example -> update-svc.example [domain]
203.0.113.300 -> 203.0.113.300 [invalid]
notes -> notes [invalid]
```

### 3.2 Reading the result

The defanged URL becomes host pay-portal.example, classified as a domain. 198.51.100[.]23 becomes a valid IPv4 address. update-svc[.]example is a domain. 203.0.113.300 is invalid because 300 exceeds the maximum octet value of 255; the `ipaddress` module rejects it. "notes" is a stray word and is marked invalid rather than guessed.

Section three point two develops programming foundations with a Corvale Municipal Services note Lena Park can demo offline.

Under section three point two, MCX expects programming claims to carry owners and dates.

Section three point two treats defanging reading the result as testable only when evidence and ticket IDs are recorded.

### 3.3 Text only

The script never opens a connection. Refanging for matching is safe; refanging for clicking is not. Keep defanged forms in documents and refanged forms only inside matching code.

Section three point three develops programming foundations with a Corvale Municipal Services note Lena Park can demo offline.

Under section three point three, MCX expects programming claims to carry owners and dates.

Section three point three treats defanging reading the result as testable only when evidence and ticket IDs are recorded.

For section three point three, Corvale Municipal Services will not accept programming work without a written trail.

### 3.4 Structure

Small functions — refang, extract host, classify — are easier to test than one long block. Each has one job.

Section three point four develops programming foundations with a Corvale Municipal Services note Lena Park can demo offline.

Under section three point four, MCX expects programming claims to carry owners and dates.

Section three point four treats defanging reading the result as testable only when evidence and ticket IDs are recorded.

For section three point four, Corvale Municipal Services will not accept programming work without a written trail.

### 3.5 Testing edges

Test with values like trailing dots, capital letters and ports ("host.example:8443"). Each edge case either passes cleanly or produces a clear "invalid" so a human can look.

Section three point five develops programming foundations with a Corvale Municipal Services note Lena Park can demo offline.

Under section three point five, MCX expects programming claims to carry owners and dates.

Section three point five treats defanging reading the result as testable only when evidence and ticket IDs are recorded.

For section three point five, Corvale Municipal Services will not accept programming work without a written trail.

### 3.6 Comments and names

Name variables for what they hold — `host`, `kind` — not `x` and `y`. A one-line docstring at the top states the script's purpose and that it uses synthetic data, which helps reviewers and future maintainers.

Section three point six develops programming foundations with a Corvale Municipal Services note Lena Park can demo offline.

Under section three point six, MCX expects programming claims to carry owners and dates.

Section three point six treats defanging reading the result as testable only when evidence and ticket IDs are recorded.

### Version control

Keep scripts in the team's repository with short commit messages. When a script's output changes, the history shows which edit caused it, and colleagues can review changes before they affect daily matching.

### Worked example

Lena pastes 30 values from an MCX email. Her script classifies 27 and marks three invalid: two had octets above 255, typos introduced when the sender typed them. She asks MCX for corrections instead of guessing which digit was wrong.

> **Synthetic case.** The values are invented.

### Errors and limits

Simple host extraction fails for unusual URL forms; keep a manual review queue.

### Exercises

- **EX007 — Invalid octet.** Why was 203.0.113.300 marked invalid? *Rubric:* 3 = octet above 255; ipaddress rejects; 2 = partial; 1 = range reserved; 0 = none.
- **EX008 — Why defang.** What risk does defanging reduce in reports? *Rubric:* 3 = accidental clicks/auto-linking to malicious sites; 2 = partial; 1 = none; 0 = none.
- **EX009 — Typo handling.** What should Lena do with indicators containing typos? *Rubric:* 3 = mark invalid, ask sender; do not guess; 2 = discard; 1 = guess; 0 = none.

### Synthesis

Refang only as text for matching, validate with the standard library, flag rather than guess, and test edge cases.

### Continue studying — chapter 03 of 30

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Data models

### Learning outcomes

You will (1) explain the structure of STIX 2.1 objects; (2) read a bundle with Python's `json` module; (3) check relationships for missing targets; (4) choose fields worth storing locally.

### 4.1 Objects and relationships

STIX 2.1 represents intelligence as typed JSON objects — indicator, attack-pattern, malware, threat-actor, report — each with an `id` made from its type and a unique identifier. Relationship objects connect them with a `source_ref`, a `target_ref` and a `relationship_type` such as "indicates" or "uses".

Section four point one develops data models with a Corvale Municipal Services note Lena Park can demo offline.

Under section four point one, MCX expects data claims to carry owners and dates.

Section four point one treats objects and relationships reading as testable only when evidence and ticket IDs are recorded.

### Lab — reading a bundle

```python
"""Lab (ch 04): read a small synthetic STIX 2.1-style bundle with json and list objects and links."""
import json
bundle = json.loads('''{"type":"bundle","id":"bundle--1","objects":[
 {"type":"indicator","id":"indicator--a","name":"pay-portal domain","pattern":"[domain-name:value = 'pay-portal.example']","valid_from":"2026-09-01T00:00:00Z"},
 {"type":"attack-pattern","id":"attack-pattern--b","name":"Phishing","external_references":[{"source_name":"mitre-attack","external_id":"T1566"}]},
 {"type":"relationship","id":"relationship--c","relationship_type":"indicates","source_ref":"indicator--a","target_ref":"attack-pattern--b"},
 {"type":"relationship","id":"relationship--d","relationship_type":"indicates","source_ref":"indicator--a","target_ref":"malware--z"}]}''')
ids = {o["id"]: o for o in bundle["objects"]}
from collections import Counter
print(dict(Counter(o["type"] for o in bundle["objects"])))
for o in bundle["objects"]:
    if o["type"] == "relationship":
        ok = o["source_ref"] in ids and o["target_ref"] in ids
        print(o["id"], o["relationship_type"], "OK" if ok else "DANGLING target " + o["target_ref"])
```

Run with `python3 lab_stix.py`. Verified output:

```text
{'indicator': 1, 'attack-pattern': 1, 'relationship': 2}
relationship--c indicates OK
relationship--d indicates DANGLING target malware--z
```

### 4.2 Reading the result

The bundle holds one indicator, one attack-pattern (Phishing, external identifier T1566) and two relationships. The first links the indicator to the attack pattern correctly. The second points to malware--z, which is not in the bundle — a dangling reference. It may exist in the sender's database, but CMS cannot use it without the object.

Section four point two develops data models with a Corvale Municipal Services note Lena Park can demo offline.

Under section four point two, MCX expects data claims to carry owners and dates.

### 4.3 Patterns

An indicator's `pattern` field uses STIX patterning, such as matching a domain-name value. Lena extracts the value for matching but keeps the full pattern for reference.

Section four point three develops data models with a Corvale Municipal Services note Lena Park can demo offline.

Under section four point three, MCX expects data claims to carry owners and dates.

Section four point three treats objects and relationships reading as testable only when evidence and ticket IDs are recorded.

For section four point three, Corvale Municipal Services will not accept data work without a written trail.

### 4.4 What to keep locally

CMS's simple store keeps: indicator value, type, source, TLP marking, valid_from, and linked ATT&CK identifiers. Other fields are stored in the original JSON for reference.

Section four point four develops data models with a Corvale Municipal Services note Lena Park can demo offline.

Under section four point four, MCX expects data claims to carry owners and dates.

Section four point four treats objects and relationships reading as testable only when evidence and ticket IDs are recorded.

For section four point four, Corvale Municipal Services will not accept data work without a written trail.

### 4.5 Other formats

Partners also send CSV and email lists. Mapping each to the same local fields lets all sources be searched together.

Section four point five develops data models with a Corvale Municipal Services note Lena Park can demo offline.

Under section four point five, MCX expects data claims to carry owners and dates.

Section four point five treats objects and relationships reading as testable only when evidence and ticket IDs are recorded.

For section four point five, Corvale Municipal Services will not accept data work without a written trail.

### 4.6 Timestamps

STIX timestamps are in UTC with a trailing "Z". Keep them in UTC in storage and convert only when displaying to staff, so comparisons across sources stay correct.

Section four point six develops data models with a Corvale Municipal Services note Lena Park can demo offline.

Under section four point six, MCX expects data claims to carry owners and dates.

Section four point six treats objects and relationships reading as testable only when evidence and ticket IDs are recorded.

For section four point six, Corvale Municipal Services will not accept data work without a written trail.

### Worked example

Lena reports the dangling reference to MCX. The sender explains that the malware object is TLP:AMBER and was filtered out before the GREEN bundle was published, leaving the relationship behind. MCX fixes its export to drop relationships whose targets are filtered.

> **Synthetic case.** The bundle and exchange are invented.

### Errors and limits

Valid JSON can still be poor intelligence; structure checks are the first step only.

### Exercises

- **EX010 — Object count.** What object types and counts did the lab bundle contain? *Rubric:* 3 = indicator 1, attack-pattern 1, relationship 2; 2 = partial; 1 = wrong; 0 = none.
- **EX011 — Dangling cause.** What caused the dangling reference in the worked example? *Rubric:* 3 = AMBER target filtered out of GREEN export, relationship left; 2 = partial; 1 = typo; 0 = none.
- **EX012 — UTC rule.** Why keep timestamps in UTC in storage? *Rubric:* 3 = consistent comparison across sources; convert only for display; 2 = partial; 1 = no reason; 0 = none.

### Synthesis

Read STIX as typed objects and relationships, check references, keep useful fields and store times in UTC.

### Continue studying — chapter 04 of 30

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) describe common threats to local government; (2) explain the CTI cycle in a small team; (3) use TLP 2.0 labels correctly; (4) separate information from intelligence.

### 5.1 Threats to councils

Local governments face payment fraud through lookalike portals, ransomware that disrupts services (Data Encrypted for Impact, T1486), credential phishing against staff, and defacement of public websites. Residents' trust makes even minor incidents newsworthy.

Section five point one develops security literacy with a Corvale Municipal Services note Lena Park can demo offline.

Under section five point one, MCX expects security claims to carry owners and dates.

Section five point one treats threats to councils the as testable only when evidence and ticket IDs are recorded.

### 5.2 The cycle in a small team

Direction from the security manager, collection from MCX and public advisories, processing in Lena's scripts, analysis with her supervisor, dissemination to owners and feedback at a weekly meeting. In a team of three, the cycle is informal but each stage still happens.

Section five point two develops security literacy with a Corvale Municipal Services note Lena Park can demo offline.

Under section five point two, MCX expects security claims to carry owners and dates.

Section five point two treats threats to councils the as testable only when evidence and ticket IDs are recorded.

### 5.3 TLP 2.0

TLP:CLEAR — no limit. TLP:GREEN — the community, not public. TLP:AMBER — the organisation and its clients, need to know. TLP:AMBER+STRICT — the organisation only. TLP:RED — named recipients only. FIRST's definitions are short; Lena keeps a copy beside her desk.

Section five point three develops security literacy with a Corvale Municipal Services note Lena Park can demo offline.

Under section five point three, MCX expects security claims to carry owners and dates.

Section five point three treats threats to councils the as testable only when evidence and ticket IDs are recorded.

### 5.4 Information versus intelligence

A list of fraud domains is information. A note saying "residents are being targeted with fake permit-payment sites this month; we have asked the hosting provider to take two down and posted a warning on the council site" is intelligence: assessed and tied to action.

Section five point four develops security literacy with a Corvale Municipal Services note Lena Park can demo offline.

Under section five point four, MCX expects security claims to carry owners and dates.

Section five point four treats threats to councils the as testable only when evidence and ticket IDs are recorded.

### 5.5 Who acts

Lena informs; owners act. The web team posts warnings; the network team blocks; the communications team speaks to residents.

Section five point five develops security literacy with a Corvale Municipal Services note Lena Park can demo offline.

Under section five point five, MCX expects security claims to carry owners and dates.

Section five point five treats threats to councils the as testable only when evidence and ticket IDs are recorded.

For section five point five, Corvale Municipal Services will not accept security work without a written trail.

### 5.6 Proportion

Not every advisory is urgent. Lena labels each item as act now, act this week, or note only, so owners can plan.

Section five point six develops security literacy with a Corvale Municipal Services note Lena Park can demo offline.

Under section five point six, MCX expects security claims to carry owners and dates.

Section five point six treats threats to councils the as testable only when evidence and ticket IDs are recorded.

For section five point six, Corvale Municipal Services will not accept security work without a written trail.

### Worked example

An MCX item marked TLP:AMBER describes fraud domains targeting a neighbouring city. Lena may share it with CMS staff who need it, but not post it publicly. The communications team asks for a public warning; Lena asks MCX for a CLEAR version, which arrives the next day.

> **Synthetic case.** The item is invented.

### Errors and limits

TLP labels only work if everyone knows them; brief new staff.

### Exercises

- **EX013 — Council threats.** Name three threats typical for local government. *Rubric:* 3 = three of lookalike payment fraud, ransomware, credential phishing, defacement; 2 = two; 1 = one; 0 = none.
- **EX014 — Public warning.** How did Lena get a publishable version of the AMBER item? *Rubric:* 3 = asked MCX for CLEAR version; 2 = partial; 1 = posted AMBER; 0 = none.
- **EX015 — Item labels.** What three urgency labels does Lena use, and why? *Rubric:* 3 = act now/this week/note only; helps owners plan; 2 = labels only; 1 = one; 0 = none.

### Synthesis

Know the threats, run the cycle even in a small team, apply TLP precisely and turn information into actionable intelligence.

### Continue studying — chapter 05 of 30

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Operating systems and virtualization

### Learning outcomes

You will (1) relate operating-system activity to ATT&CK techniques; (2) use virtual machines safely for analysis tasks; (3) understand snapshots and isolation; (4) know what not to do with suspicious files.

### 6.1 Operating-system activity

Processes, services, scheduled tasks and accounts are where intrusions become visible. ATT&CK techniques such as Command and Scripting Interpreter (T1059) and Scheduled Task/Job (T1053) describe common behaviours. Endpoint logs recording process starts with command lines help confirm or rule out reported behaviour.

Section six point one develops operating systems and virtualization with a Corvale Municipal Services note Lena Park can demo offline.

Under section six point one, MCX expects operating claims to carry owners and dates.

Section six point one treats operating-system activity virtual machines as testable only when evidence and ticket IDs are recorded.

### 6.2 Virtual machines

A virtual machine runs a separate operating system on shared hardware. Analysts use them to read reports, run scripts on synthetic data and open documents in an environment that can be reset. Snapshots capture a known-good state to return to.

Section six point two develops operating systems and virtualization with a Corvale Municipal Services note Lena Park can demo offline.

Under section six point two, MCX expects operating claims to carry owners and dates.

Section six point two treats operating-system activity virtual machines as testable only when evidence and ticket IDs are recorded.

### 6.3 Isolation limits

Virtual machines reduce risk but are not perfect barriers. Network settings matter: a machine with internet access can still contact adversary servers. CMS's analysis VM has no network route except to the internal update server.

Section six point three develops operating systems and virtualization with a Corvale Municipal Services note Lena Park can demo offline.

Under section six point three, MCX expects operating claims to carry owners and dates.

Section six point three treats operating-system activity virtual machines as testable only when evidence and ticket IDs are recorded.

### 6.4 Suspicious files

Technologist-level analysts do not run malware. If a suspicious attachment arrives, Lena records its hash and metadata, submits it through CMS's approved sandbox service if policy allows, and leaves deeper analysis to qualified staff.

Section six point four develops operating systems and virtualization with a Corvale Municipal Services note Lena Park can demo offline.

Under section six point four, MCX expects operating claims to carry owners and dates.

Section six point four treats operating-system activity virtual machines as testable only when evidence and ticket IDs are recorded.

### 6.5 Containers

Containers share the host kernel and isolate less than virtual machines. They suit packaging scripts, not handling hostile files.

Section six point five develops operating systems and virtualization with a Corvale Municipal Services note Lena Park can demo offline.

Under section six point five, MCX expects operating claims to carry owners and dates.

Section six point five treats operating-system activity virtual machines as testable only when evidence and ticket IDs are recorded.

For section six point five, Corvale Municipal Services will not accept operating work without a written trail.

### 6.6 Patching the analysis environment

Analysis machines need updates too; an outdated VM is an easy target. Lena refreshes the base image monthly and re-creates her snapshot afterwards.

Section six point six develops operating systems and virtualization with a Corvale Municipal Services note Lena Park can demo offline.

Under section six point six, MCX expects operating claims to carry owners and dates.

Section six point six treats operating-system activity virtual machines as testable only when evidence and ticket IDs are recorded.

For section six point six, Corvale Municipal Services will not accept operating work without a written trail.

### Worked example

An MCX report says attackers created a scheduled task named "CivicUpdate" on council servers. Lena asks the endpoint team to search for scheduled tasks with that name across CMS servers in the past 60 days. None appear. She records the query, period and data source, and notes that two servers lack endpoint agents — a coverage gap she reports.

> **Synthetic case.** The task name and report are invented.

### Errors and limits

A clean search covers only machines with logging; report gaps alongside results.

### Exercises

- **EX016 — Task technique.** Which ATT&CK technique fits a malicious scheduled task? *Rubric:* 3 = Scheduled Task/Job T1053; 2 = name; 1 = T1190; 0 = none.
- **EX017 — VM network.** Why does CMS's analysis VM lack internet access? *Rubric:* 3 = prevents contact with adversary infrastructure/leaks; 2 = partial; 1 = speed; 0 = none.
- **EX018 — Coverage gap.** What gap did Lena report alongside her clean search? *Rubric:* 3 = two servers without endpoint agents; 2 = vague gap; 1 = none; 0 = none.

### Synthesis

Map OS behaviours to techniques, analyse in isolated, patched VMs, leave malware to qualified staff and report coverage gaps.

### Continue studying — chapter 06 of 30

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Identity and access foundations

### Learning outcomes

You will (1) explain why stolen credentials are central to many intrusions; (2) read sign-in logs for intelligence matches; (3) support identity controls with intelligence; (4) handle exposed-credential notices safely.

### 7.1 Credentials as targets

Phishing pages that imitate the council's single sign-on page collect staff passwords. Attackers then log in normally — Valid Accounts (T1078). Many intrusions involve no malware at all.

Section seven point one develops identity and access foundations with a Corvale Municipal Services note Lena Park can demo offline.

Under section seven point one, MCX expects identity claims to carry owners and dates.

Section seven point one treats credentials as targets sign-in as testable only when evidence and ticket IDs are recorded.

For section seven point one, Corvale Municipal Services will not accept identity work without a written trail.

### 7.2 Sign-in logs

The identity provider logs user, time, source address, application and result. When MCX shares addresses used in credential attacks against councils, Lena searches sign-in logs for successful logins from them.

Section seven point two develops identity and access foundations with a Corvale Municipal Services note Lena Park can demo offline.

Under section seven point two, MCX expects identity claims to carry owners and dates.

Section seven point two treats credentials as targets sign-in as testable only when evidence and ticket IDs are recorded.

### 7.3 Supporting controls

Intelligence that councils face password-spraying justifies lockout thresholds and multi-factor authentication for all staff, including part-time library workers who were previously exempt.

Section seven point three develops identity and access foundations with a Corvale Municipal Services note Lena Park can demo offline.

Under section seven point three, MCX expects identity claims to carry owners and dates.

Section seven point three treats credentials as targets sign-in as testable only when evidence and ticket IDs are recorded.

For section seven point three, Corvale Municipal Services will not accept identity work without a written trail.

### 7.4 Exposure notices

Sometimes a partner reports CMS addresses found in a public credential dump. Lena never tests the passwords. She passes the list to the identity team through a restricted ticket; they force resets.

Section seven point four develops identity and access foundations with a Corvale Municipal Services note Lena Park can demo offline.

Under section seven point four, MCX expects identity claims to carry owners and dates.

Section seven point four treats credentials as targets sign-in as testable only when evidence and ticket IDs are recorded.

### 7.5 Shared accounts

Shared logins on library staff desks make it impossible to tell who did what. Intelligence about account abuse strengthens the case for individual accounts.

Section seven point five develops identity and access foundations with a Corvale Municipal Services note Lena Park can demo offline.

Under section seven point five, MCX expects identity claims to carry owners and dates.

Section seven point five treats credentials as targets sign-in as testable only when evidence and ticket IDs are recorded.

For section seven point five, Corvale Municipal Services will not accept identity work without a written trail.

### 7.6 Service accounts

Accounts used by applications often have broad rights and passwords that never change. When intelligence describes attackers seeking such accounts, the identity team reviews their rights and rotates credentials first.

Section seven point six develops identity and access foundations with a Corvale Municipal Services note Lena Park can demo offline.

Under section seven point six, MCX expects identity claims to carry owners and dates.

Section seven point six treats credentials as targets sign-in as testable only when evidence and ticket IDs are recorded.

### Leavers and dormant accounts

Accounts of staff who have left are attractive to attackers because nobody notices their use. A monthly report of accounts with no sign-in for 60 days, checked against human-resources leaver lists, closes many quiet entry points.

### Worked example

MCX shares five addresses used in password-spraying against councils. Lena's search finds 40 failed logins and one success from one address against a parks-department account. The identity team resets the password, revokes sessions and reviews the account's recent actions. The user had reused a password from a breached shopping site.

> **Synthetic case.** The addresses and account are invented.

### Errors and limits

Attackers rotate addresses quickly; address matches are useful for days, not months.

### Exercises

- **EX019 — No malware.** Explain how an intrusion can succeed without malware. *Rubric:* 3 = stolen credentials, valid-account login (T1078); 2 = partial; 1 = impossible; 0 = none.
- **EX020 — Testing passwords.** Why must Lena never test passwords from a dump? *Rubric:* 3 = unauthorised access/legal and policy breach; identity team resets instead; 2 = partial; 1 = acceptable; 0 = none.
- **EX021 — Spraying response.** List the identity team's three actions after the successful spray login. *Rubric:* 3 = reset password, revoke sessions, review actions; 2 = two; 1 = one; 0 = none.

### Synthesis

Credentials are prime targets; match intelligence against sign-in logs, support identity controls and handle exposure notices without touching passwords.

### Continue studying — chapter 07 of 30

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Security architecture basics

### Learning outcomes

You will (1) describe layered defences in a municipal network; (2) choose the right layer for each indicator type; (3) explain segmentation of public-access networks; (4) recognise collateral damage from blocking.

### 8.1 Layers

Email gateway, DNS filter, web proxy, endpoint protection, identity provider, network segmentation and backups. Each layer can use some intelligence; none uses all of it.

Section eight point one develops security architecture basics with a Corvale Municipal Services note Lena Park can demo offline.

Under section eight point one, MCX expects security claims to carry owners and dates.

Section eight point one treats layers matching indicators to as testable only when evidence and ticket IDs are recorded.

For section eight point one, Corvale Municipal Services will not accept security work without a written trail.

### 8.2 Matching indicators to layers

Sender domains go to the email gateway; malicious domains to DNS and proxy; file hashes to endpoint protection; addresses used in password attacks to identity-provider conditional access; ransomware technique intelligence to backup design.

Section eight point two develops security architecture basics with a Corvale Municipal Services note Lena Park can demo offline.

Under section eight point two, MCX expects security claims to carry owners and dates.

Section eight point two treats layers matching indicators to as testable only when evidence and ticket IDs are recorded.

### 8.3 Segmentation

Library public computers, staff desktops, servers and payment systems sit in separate zones. Intelligence about attackers moving between systems via remote services (T1021) supports keeping those zones strictly separated.

Section eight point three develops security architecture basics with a Corvale Municipal Services note Lena Park can demo offline.

Under section eight point three, MCX expects security claims to carry owners and dates.

Section eight point three treats layers matching indicators to as testable only when evidence and ticket IDs are recorded.

For section eight point three, Corvale Municipal Services will not accept security work without a written trail.

### 8.4 Collateral damage

Blocking a shared hosting address can cut off a legitimate supplier. Blocking a popular file-sharing domain stops staff from receiving planning documents. Before blocking, Lena checks whether the indicator is shared or popular and asks the owner.

Section eight point four develops security architecture basics with a Corvale Municipal Services note Lena Park can demo offline.

Under section eight point four, MCX expects security claims to carry owners and dates.

Section eight point four treats layers matching indicators to as testable only when evidence and ticket IDs are recorded.

### 8.5 Payment card systems

The payments portal falls under card-industry rules. Changes there go through its own approval process; intelligence is passed to its owner, not applied directly.

Section eight point five develops security architecture basics with a Corvale Municipal Services note Lena Park can demo offline.

Under section eight point five, MCX expects security claims to carry owners and dates.

Section eight point five treats layers matching indicators to as testable only when evidence and ticket IDs are recorded.

For section eight point five, Corvale Municipal Services will not accept security work without a written trail.

### 8.6 Recording blocks

Every block is recorded with its source, reason, date and review date. When a resident complains that a site is unreachable, the service desk can check the record and lift a mistaken block quickly.

Section eight point six develops security architecture basics with a Corvale Municipal Services note Lena Park can demo offline.

Under section eight point six, MCX expects security claims to carry owners and dates.

Section eight point six treats layers matching indicators to as testable only when evidence and ticket IDs are recorded.

### Backups and recovery

Ransomware intelligence often reports attackers deleting backups before encrypting. CMS keeps an offline copy and tests restores every quarter, so a council service can be rebuilt even if online copies are destroyed.

### Worked example

MCX lists an address hosting a fraud page. Lena checks it: a large cloud provider address used by thousands of sites. She recommends blocking the specific domain at DNS instead of the address at the firewall, and reporting the page to the provider's abuse team through the supervisor.

> **Synthetic case.** The address and page are invented.

### Errors and limits

Layer choices depend on what each tool supports; check product capabilities.

### Exercises

- **EX022 — Hash layer.** Where should a malicious attachment hash be enforced? *Rubric:* 3 = endpoint protection/mail attachment scanning; 2 = one; 1 = firewall; 0 = none.
- **EX023 — Cloud address choice.** Why block the domain at DNS rather than the address at the firewall? *Rubric:* 3 = address shared by many sites; collateral; domain precise; 2 = partial; 1 = no difference; 0 = none.
- **EX024 — Block record.** What should each block record contain? *Rubric:* 3 = source, reason, date, review date; 2 = two; 1 = one; 0 = none.

### Synthesis

Send each indicator to the layer that can use it, segment zones, avoid collateral damage and record every block.

### Continue studying — chapter 08 of 30

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Evidence and measurement

### Learning outcomes

You will (1) record the provenance of each intelligence item; (2) separate what was observed from what was concluded; (3) count outcomes rather than activity; (4) report negative results with their coverage.

### 9.1 Provenance

For every item Lena records who sent it, when, how, under which TLP, and what the sender based it on. Without provenance, the same indicator copied by three newsletters looks like three confirmations.

Section nine point one develops evidence and measurement with a Corvale Municipal Services note Lena Park can demo offline.

Under section nine point one, MCX expects evidence claims to carry owners and dates.

Section nine point one treats provenance observation and conclusion as testable only when evidence and ticket IDs are recorded.

### 9.2 Observation and conclusion

"The proxy logged ws-114 contacting pay-portal.example at 08:03" is an observation. "A staff member probably entered credentials" is a conclusion. Reports keep them in separate sentences so readers can judge each.

Section nine point two develops evidence and measurement with a Corvale Municipal Services note Lena Park can demo offline.

Under section nine point two, MCX expects evidence claims to carry owners and dates.

Section nine point two treats provenance observation and conclusion as testable only when evidence and ticket IDs are recorded.

### 9.3 Outcome counting

"500 indicators imported" counts activity. "Two staff were stopped from reaching the fraud page by the DNS block" counts an outcome. Lena reports both but leads with outcomes in the monthly summary.

Section nine point three develops evidence and measurement with a Corvale Municipal Services note Lena Park can demo offline.

Under section nine point three, MCX expects evidence claims to carry owners and dates.

Section nine point three treats provenance observation and conclusion as testable only when evidence and ticket IDs are recorded.

### 9.4 Negative results

"No matches" is useful only with its query, time range, data source and coverage. "No DNS lookups of the three domains in the last 30 days across all staff resolvers; library resolvers not included" lets the reader see what was and was not checked.

Section nine point four develops evidence and measurement with a Corvale Municipal Services note Lena Park can demo offline.

Under section nine point four, MCX expects evidence claims to carry owners and dates.

Section nine point four treats provenance observation and conclusion as testable only when evidence and ticket IDs are recorded.

### 9.5 Timeliness

Record when intelligence arrived and when it was acted on. Long gaps point to process problems.

Section nine point five develops evidence and measurement with a Corvale Municipal Services note Lena Park can demo offline.

Under section nine point five, MCX expects evidence claims to carry owners and dates.

Section nine point five treats provenance observation and conclusion as testable only when evidence and ticket IDs are recorded.

For section nine point five, Corvale Municipal Services will not accept evidence work without a written trail.

### 9.6 Keeping evidence

Exported log extracts used in a finding are saved with the ticket, hashed, and kept under the retention rule. If the finding is challenged, the evidence can be shown exactly as it was.

Section nine point six develops evidence and measurement with a Corvale Municipal Services note Lena Park can demo offline.

Under section nine point six, MCX expects evidence claims to carry owners and dates.

Section nine point six treats provenance observation and conclusion as testable only when evidence and ticket IDs are recorded.

### 9.7 Simple dashboards

A one-page monthly table — items received, items acted on, blocks that stopped connections, median time to action — gives the manager a view of value without overwhelming detail.

Section nine point seven develops evidence and measurement with a Corvale Municipal Services note Lena Park can demo offline.

Under section nine point seven, MCX expects evidence claims to carry owners and dates.

Section nine point seven treats provenance observation and conclusion as testable only when evidence and ticket IDs are recorded.

For section nine point seven, Corvale Municipal Services will not accept evidence work without a written trail.

### Worked example

Three newsletters list the same fraud domain. Lena traces them: all cite one MCX post. She records one independent source. Her DNS search shows one lookup by a library computer, outside the staff resolver she usually checks — so her report notes that she widened the search to library resolvers after a colleague's question.

> **Synthetic case.** The sources and lookup are invented.

### Errors and limits

Outcomes rarely prove intelligence alone made the difference; describe contribution.

### Exercises

- **EX025 — Three newsletters.** How many independent sources did Lena record, and why? *Rubric:* 3 = one; all cite same MCX post; 2 = number only; 1 = three; 0 = none.
- **EX026 — Split the sentence.** Separate observation from conclusion in "ws-114 hit the fraud site so the user gave away their password". *Rubric:* 3 = observation: contact logged; conclusion: probable credential entry; 2 = partial; 1 = merged; 0 = none.
- **EX027 — Negative result.** Write a complete "no match" statement. *Rubric:* 3 = query, range, source, coverage gaps; 2 = three; 1 = verdict only; 0 = none.

### Synthesis

Record provenance, separate observation from conclusion, lead with outcomes and give coverage with every negative result.

### Continue studying — chapter 09 of 30

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Threat intelligence and OSINT: orientation

### Learning outcomes

You will (1) define CTI and OSINT for a technologist role; (2) place the role within a security team; (3) name the core models and standards; (4) state the ethical rules for OSINT.

### 10.1 Definitions

Cyber threat intelligence is analysed information about threats that supports defensive decisions. Open-source intelligence is intelligence derived from publicly available information collected lawfully. NIST SP 800-150 describes how organisations share threat information to strengthen defences.

Section ten point one develops threat intelligence and osint orientation with a Corvale Municipal Services note Lena Park can demo offline.

Under section ten point one, MCX expects threat claims to carry owners and dates.

Section ten point one treats definitions the technologist's role as testable only when evidence and ticket IDs are recorded.

### 10.2 The technologist's role

Lena's tasks: collect from approved sources, validate and normalise indicators, match them against logs, maintain the indicator store, draft short notes and support analysts. She does not decide blocks on critical systems or publish attribution.

Section ten point two develops threat intelligence and osint orientation with a Corvale Municipal Services note Lena Park can demo offline.

Under section ten point two, MCX expects threat claims to carry owners and dates.

Section ten point two treats definitions the technologist's role as testable only when evidence and ticket IDs are recorded.

### 10.3 Models

The intrusion kill chain (Hutchins, Cloppert and Amin, 2011) splits intrusions into phases, showing where defenders can act. The Diamond Model (Caltagirone, Pendergast and Betz, 2013) describes each event by adversary, capability, infrastructure and victim. MITRE ATT&CK catalogues observed techniques.

Section ten point three develops threat intelligence and osint orientation with a Corvale Municipal Services note Lena Park can demo offline.

Under section ten point three, MCX expects threat claims to carry owners and dates.

Section ten point three treats definitions the technologist's role as testable only when evidence and ticket IDs are recorded.

### 10.4 Standards

STIX 2.1 is the data format; TAXII 2.1 the exchange protocol; FIRST TLP 2.0 the sharing labels.

Section ten point four develops threat intelligence and osint orientation with a Corvale Municipal Services note Lena Park can demo offline.

Under section ten point four, MCX expects threat claims to carry owners and dates.

Section ten point four treats definitions the technologist's role as testable only when evidence and ticket IDs are recorded.

For section ten point four, Corvale Municipal Services will not accept threat work without a written trail.

### 10.5 OSINT rules

Use only approved sources and methods. Follow each site's terms of service. Do not create fake accounts, join closed groups, or collect personal data beyond the need. Data-protection law applies to public personal data.

Section ten point five develops threat intelligence and osint orientation with a Corvale Municipal Services note Lena Park can demo offline.

Under section ten point five, MCX expects threat claims to carry owners and dates.

Section ten point five treats definitions the technologist's role as testable only when evidence and ticket IDs are recorded.

### 10.6 Where OSINT helps CMS

Certificate-transparency logs for lookalike domains, public vulnerability advisories, official government alerts, and passive DNS through approved services. These answer CMS questions without touching adversaries.

Section ten point six develops threat intelligence and osint orientation with a Corvale Municipal Services note Lena Park can demo offline.

Under section ten point six, MCX expects threat claims to carry owners and dates.

Section ten point six treats definitions the technologist's role as testable only when evidence and ticket IDs are recorded.

For section ten point six, Corvale Municipal Services will not accept threat work without a written trail.

### Career path

Technologists often move into analyst roles after building strong data-handling habits. Writing clear notes, asking good questions and respecting handling rules matter as much as scripting skill in that progression.

### Worked example

A colleague suggests searching social media for the names of people who complained about fraud texts to "see who was targeted". Lena points out that CMS needs the fraud domains, not residents' identities; she collects the domains from CMS's own complaint form instead, where residents agreed to share details.

> **Synthetic case.** The suggestion is invented.

### Errors and limits

Public information can be wrong or planted; validate before use.

### Exercises

- **EX028 — Role boundary.** Name two tasks outside a technologist's authority at CMS. *Rubric:* 3 = deciding blocks on critical systems, publishing attribution; 2 = one; 1 = matching logs; 0 = none.
- **EX029 — Social media idea.** Why did Lena reject searching residents' social media? *Rubric:* 3 = unnecessary personal data; complaint form gives what's needed lawfully; 2 = partial; 1 = acceptable; 0 = none.
- **EX030 — Useful OSINT.** List three OSINT sources that help CMS without touching adversaries. *Rubric:* 3 = three of CT logs, advisories, government alerts, passive DNS; 2 = two; 1 = one; 0 = none.

### Synthesis

Know the definitions, your role, the models and standards, and the ethical limits of OSINT.

### Continue studying — chapter 10 of 30

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Threat intelligence and OSINT: assets and context

### Learning outcomes

You will (1) build a threat-relevance view of CMS assets; (2) link asset types to likely techniques; (3) prioritise intelligence by business impact; (4) keep context current with owners.

### 11.1 Relevance view

Lena adds two columns to the asset list: "services residents depend on" and "techniques of concern". The payments portal: fraud lookalikes and T1190. Staff email: T1566. File servers: T1486. This view lets her sort incoming intelligence quickly.

Section eleven point one develops threat intelligence and osint assets with a Corvale Municipal Services note Lena Park can demo offline.

Under section eleven point one, MCX expects threat claims to carry owners and dates.

Section eleven point one treats relevance view business impact as testable only when evidence and ticket IDs are recorded.

### 11.2 Business impact

Payments and permits affect residents directly and bring revenue; the intranet affects only staff. When two advisories arrive together, the one touching resident-facing services goes first.

Section eleven point two develops threat intelligence and osint assets with a Corvale Municipal Services note Lena Park can demo offline.

Under section eleven point two, MCX expects threat claims to carry owners and dates.

Section eleven point two treats relevance view business impact as testable only when evidence and ticket IDs are recorded.

For section eleven point two, Corvale Municipal Services will not accept threat work without a written trail.

### 11.3 Seasonal context

Council tax deadlines and elections bring spikes in fraud and attention. Lena marks those dates on the team calendar so monitoring increases beforehand.

Section eleven point three develops threat intelligence and osint assets with a Corvale Municipal Services note Lena Park can demo offline.

Under section eleven point three, MCX expects threat claims to carry owners and dates.

Section eleven point three treats relevance view business impact as testable only when evidence and ticket IDs are recorded.

For section eleven point three, Corvale Municipal Services will not accept threat work without a written trail.

### 11.4 Owner conversations

Owners know what spreadsheets say nothing about: that the permits portal will be replaced in spring, or that a supplier connects every night. Quarterly chats keep context fresh.

Section eleven point four develops threat intelligence and osint assets with a Corvale Municipal Services note Lena Park can demo offline.

Under section eleven point four, MCX expects threat claims to carry owners and dates.

Section eleven point four treats relevance view business impact as testable only when evidence and ticket IDs are recorded.

### 11.5 Dependencies

The payments portal depends on an external payment provider. Intelligence about that provider matters to CMS even though CMS does not run it.

Section eleven point five develops threat intelligence and osint assets with a Corvale Municipal Services note Lena Park can demo offline.

Under section eleven point five, MCX expects threat claims to carry owners and dates.

Section eleven point five treats relevance view business impact as testable only when evidence and ticket IDs are recorded.

For section eleven point five, Corvale Municipal Services will not accept threat work without a written trail.

### 11.6 Writing context into notes

Each intelligence note names the affected asset, its owner, its exposure and the relevant date context, so the reader understands why the item matters to CMS today.

Section eleven point six develops threat intelligence and osint assets with a Corvale Municipal Services note Lena Park can demo offline.

Under section eleven point six, MCX expects threat claims to carry owners and dates.

Section eleven point six treats relevance view business impact as testable only when evidence and ticket IDs are recorded.

For section eleven point six, Corvale Municipal Services will not accept threat work without a written trail.

### Crown jewels

Ask leadership which three services would cause the most harm if lost for a week. For CMS the answer was payments, permits and the emergency-notification system. Intelligence touching these always receives same-day review, whatever its source or apparent severity.

### Worked example

Two weeks before the council-tax deadline, MCX reports fraud texts imitating tax-payment pages in another city. Lena's relevance view marks payments as top priority and the calendar shows the deadline. She drafts an early warning for the communications team and asks the network team to watch DNS for "tax" lookalikes.

> **Synthetic case.** The report and dates are invented.

### Errors and limits

Relevance views encode assumptions; revisit them when services change.

### Exercises

- **EX031 — Asset technique.** Which technique of concern did Lena assign to file servers, and why? *Rubric:* 3 = T1486 ransomware encryption; holds shared data; 2 = name; 1 = T1566; 0 = none.
- **EX032 — Seasonal spike.** Why mark council-tax deadlines on the calendar? *Rubric:* 3 = fraud spikes; raise monitoring in advance; 2 = partial; 1 = no reason; 0 = none.
- **EX033 — Provider dependency.** Why does intelligence about the payment provider matter to CMS? *Rubric:* 3 = portal depends on it; its compromise affects residents; 2 = partial; 1 = doesn't; 0 = none.

### Synthesis

Tie assets to techniques and impact, watch seasons and dependencies, and keep context fresh with owners.

### Continue studying — chapter 11 of 30

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Threat intelligence and OSINT: data flows

### Learning outcomes

You will (1) trace intelligence from source to enforcement; (2) normalise and deduplicate indicators while keeping provenance; (3) identify points where data is lost or altered; (4) document the flow.

### 12.1 The flow at CMS

MCX TAXII collection and email, a vendor list and public advisories arrive; Lena's scripts normalise and deduplicate them; the indicator store holds results; exports feed the DNS filter, proxy and endpoint tool; feedback returns via tickets.

Section twelve point one develops threat intelligence and osint data with a Corvale Municipal Services note Lena Park can demo offline.

Under section twelve point one, MCX expects threat claims to carry owners and dates.

Section twelve point one treats the flow at cms as testable only when evidence and ticket IDs are recorded.

### Lab — normalise and deduplicate

```python
"""Lab (ch 12): normalise and deduplicate indicators from three synthetic sources, keeping provenance."""
rows = [("MCX", "Pay-Portal.example."), ("vendor", "pay-portal.example"), ("public", "198.51.100.23"),
        ("MCX", "198.51.100.23"), ("vendor", "update-svc.example"), ("public", "PAY-PORTAL.EXAMPLE")]
seen = {}
for src, v in rows:
    k = v.strip().lower().rstrip(".")
    seen.setdefault(k, set()).add(src)
print("raw", len(rows), "unique", len(seen))
for k in sorted(seen):
    print(k, sorted(seen[k]))
```

Run with `python3 lab_dedupe.py`. Verified output:

```text
raw 6 unique 3
198.51.100.23 ['MCX', 'public']
pay-portal.example ['MCX', 'public', 'vendor']
update-svc.example ['vendor']
```

### 12.2 Reading the result

Six raw rows collapse to three unique indicators after lower-casing and removing trailing dots. pay-portal.example was reported by MCX, the vendor and a public source; 198.51.100.23 by MCX and a public source; update-svc.example only by the vendor. The script keeps every source for each value.

Section twelve point two develops threat intelligence and osint data with a Corvale Municipal Services note Lena Park can demo offline.

Under section twelve point two, MCX expects threat claims to carry owners and dates.

Section twelve point two treats the flow at cms as testable only when evidence and ticket IDs are recorded.

### 12.3 Why keep provenance

When the vendor later withdraws update-svc.example as a false positive, Lena can remove it confidently because no other source reported it. If she had discarded sources during deduplication, she could not tell.

Section twelve point three develops threat intelligence and osint data with a Corvale Municipal Services note Lena Park can demo offline.

Under section twelve point three, MCX expects threat claims to carry owners and dates.

Section twelve point three treats the flow at cms as testable only when evidence and ticket IDs are recorded.

### 12.4 Loss points

Data is lost when spreadsheets reformat values, when exports truncate long fields, or when TLP labels are not carried into enforcement tools. Lena checks each hand-off.

Section twelve point four develops threat intelligence and osint data with a Corvale Municipal Services note Lena Park can demo offline.

Under section twelve point four, MCX expects threat claims to carry owners and dates.

Section twelve point four treats the flow at cms as testable only when evidence and ticket IDs are recorded.

For section twelve point four, Corvale Municipal Services will not accept threat work without a written trail.

### 12.5 Documentation

A one-page diagram shows each source, script, store and export with owners and schedules. New staff learn the flow in minutes.

Section twelve point five develops threat intelligence and osint data with a Corvale Municipal Services note Lena Park can demo offline.

Under section twelve point five, MCX expects threat claims to carry owners and dates.

Section twelve point five treats the flow at cms as testable only when evidence and ticket IDs are recorded.

For section twelve point five, Corvale Municipal Services will not accept threat work without a written trail.

### 12.6 Normalisation rules

Rules are written down: lower-case domains, strip trailing dots, keep addresses as written after validation, never alter hashes except to lower-case them. Unwritten rules drift between scripts.

Section twelve point six develops threat intelligence and osint data with a Corvale Municipal Services note Lena Park can demo offline.

Under section twelve point six, MCX expects threat claims to carry owners and dates.

Section twelve point six treats the flow at cms as testable only when evidence and ticket IDs are recorded.

For section twelve point six, Corvale Municipal Services will not accept threat work without a written trail.

### Worked example

The DNS filter shows fewer entries than the store. Lena traces the export: the filter accepts at most 255 characters per entry, and two long lookalike domains were silently cut. She shortens nothing; instead she sends those two to the proxy, which accepts them, and notes the limit on the diagram.

> **Synthetic case.** The limits and domains are invented.

### Errors and limits

Normalisation can merge values that are actually different, such as internationalised domains; review edge cases.

### Exercises

- **EX034 — Lab counts.** How many raw and unique indicators did the lab report, and who reported pay-portal.example? *Rubric:* 3 = 6 raw, 3 unique; MCX, public, vendor; 2 = counts only; 1 = wrong; 0 = none.
- **EX035 — Withdrawal confidence.** Why could Lena remove update-svc.example confidently? *Rubric:* 3 = only vendor reported it; provenance kept; 2 = partial; 1 = guessed; 0 = none.
- **EX036 — Silent truncation.** What did Lena do about the filter's length limit? *Rubric:* 3 = routed long domains to proxy; documented limit; 2 = one; 1 = truncated; 0 = none.

### Synthesis

Trace the flow end to end, deduplicate with provenance, find loss points and document the path.

### Continue studying — chapter 12 of 30

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Threat intelligence and OSINT: risk scenarios

### Learning outcomes

You will (1) write threat scenarios grounded in intelligence; (2) map scenarios to ATT&CK techniques and kill-chain phases; (3) estimate likelihood and impact in bands; (4) link scenarios to controls.

### 13.1 Scenario structure

A scenario names the actor type, goal, entry route, key techniques, affected service and impact. Example: "Fraud group registers lookalike payment domains, sends texts to residents, collects card details; residents lose money and trust in CMS falls."

Section thirteen point one develops threat intelligence and osint risk with a Corvale Municipal Services note Lena Park can demo offline.

Under section thirteen point one, MCX expects threat claims to carry owners and dates.

Section thirteen point one treats scenario structure grounding mapping as testable only when evidence and ticket IDs are recorded.

### 13.2 Grounding

Each scenario cites intelligence: MCX reports from other councils, public advisories, CMS incidents. Scenarios without evidence are speculation.

Section thirteen point two develops threat intelligence and osint risk with a Corvale Municipal Services note Lena Park can demo offline.

Under section thirteen point two, MCX expects threat claims to carry owners and dates.

Section thirteen point two treats scenario structure grounding mapping as testable only when evidence and ticket IDs are recorded.

For section thirteen point two, Corvale Municipal Services will not accept threat work without a written trail.

### 13.3 Mapping

The ransomware scenario: phishing (T1566) for entry, valid accounts (T1078), remote services (T1021) to spread, encryption (T1486) for impact. Mapped to kill-chain phases: delivery, exploitation via credentials, actions on objectives.

Section thirteen point three develops threat intelligence and osint risk with a Corvale Municipal Services note Lena Park can demo offline.

Under section thirteen point three, MCX expects threat claims to carry owners and dates.

Section thirteen point three treats scenario structure grounding mapping as testable only when evidence and ticket IDs are recorded.

### 13.4 Bands

Likelihood: likely, roughly even, unlikely. Impact: minor, moderate, severe. Bands keep discussion honest when data is thin.

Section thirteen point four develops threat intelligence and osint risk with a Corvale Municipal Services note Lena Park can demo offline.

Under section thirteen point four, MCX expects threat claims to carry owners and dates.

Section thirteen point four treats scenario structure grounding mapping as testable only when evidence and ticket IDs are recorded.

For section thirteen point four, Corvale Municipal Services will not accept threat work without a written trail.

### 13.5 Controls

Each scenario lists existing controls and gaps. The fraud scenario: CT-log monitoring exists; resident warnings exist; takedown process is slow — a gap.

Section thirteen point five develops threat intelligence and osint risk with a Corvale Municipal Services note Lena Park can demo offline.

Under section thirteen point five, MCX expects threat claims to carry owners and dates.

Section thirteen point five treats scenario structure grounding mapping as testable only when evidence and ticket IDs are recorded.

For section thirteen point five, Corvale Municipal Services will not accept threat work without a written trail.

### 13.6 Review rhythm

Scenarios are reviewed every six months, or sooner if MCX reports a new pattern. Retired scenarios are archived, not deleted.

Section thirteen point six develops threat intelligence and osint risk with a Corvale Municipal Services note Lena Park can demo offline.

Under section thirteen point six, MCX expects threat claims to carry owners and dates.

Section thirteen point six treats scenario structure grounding mapping as testable only when evidence and ticket IDs are recorded.

For section thirteen point six, Corvale Municipal Services will not accept threat work without a written trail.

### 13.7 Audience

Managers read scenarios to set priorities; engineers read them to choose detections. A short summary line and a technical table serve both.

Section thirteen point seven develops threat intelligence and osint risk with a Corvale Municipal Services note Lena Park can demo offline.

Under section thirteen point seven, MCX expects threat claims to carry owners and dates.

Section thirteen point seven treats scenario structure grounding mapping as testable only when evidence and ticket IDs are recorded.

For section thirteen point seven, Corvale Municipal Services will not accept threat work without a written trail.

### Using the Diamond Model

For each scenario, fill the four Diamond vertices: adversary (a fraud group), capability (lookalike pages and text messages), infrastructure (newly registered domains and bulk-text services) and victim (residents paying fees). Gaps in any vertex show where intelligence is missing, and the infrastructure vertex shows which monitoring — such as certificate-transparency checks — can detect the scenario early.

### Worked example

Lena drafts three scenarios: payment fraud, ransomware and website defacement. With her supervisor she rates fraud likely/moderate, ransomware roughly even/severe, defacement likely/minor. The manager funds faster takedown support for fraud and an offline backup test for ransomware.

> **Synthetic case.** The ratings are invented.

### Errors and limits

Scenarios can anchor thinking; add a "surprise" scenario each review.

### Exercises

- **EX037 — Scenario parts.** List six parts of a threat scenario. *Rubric:* 3 = actor, goal, entry, techniques, service, impact; 2 = four; 1 = two; 0 = none.
- **EX038 — Ransomware mapping.** Map the ransomware scenario to four ATT&CK techniques. *Rubric:* 3 = T1566, T1078, T1021, T1486; 2 = three; 1 = one; 0 = none.
- **EX039 — Funding link.** Which two decisions did the scenarios inform? *Rubric:* 3 = takedown support; offline backup test; 2 = one; 1 = vague; 0 = none.

### Synthesis

Write evidence-based scenarios, map them to techniques and phases, rate in bands and tie them to control decisions.

### Continue studying — chapter 13 of 30

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Threat intelligence and OSINT: methods I

### Learning outcomes

You will (1) triage incoming items consistently; (2) grade sources and information; (3) tag items with ATT&CK techniques; (4) write a three-line intelligence note.

### 14.1 Triage questions

Is it relevant to CMS assets? Is it timely? Is it actionable? Is the source known? Items failing relevance are logged and closed.

Section fourteen point one develops threat intelligence and osint methods with a Corvale Municipal Services note Lena Park can demo offline.

Under section fourteen point one, MCX expects threat claims to carry owners and dates.

Section fourteen point one treats triage questions grading tagging as testable only when evidence and ticket IDs are recorded.

For section fourteen point one, Corvale Municipal Services will not accept threat work without a written trail.

### 14.2 Grading

The Admiralty scale grades source reliability A–F and information credibility 1–6. MCX, with a long accurate record, is usually B; an anonymous forum post is F. Information confirmed by CMS's own logs is 1.

Section fourteen point two develops threat intelligence and osint methods with a Corvale Municipal Services note Lena Park can demo offline.

Under section fourteen point two, MCX expects threat claims to carry owners and dates.

Section fourteen point two treats triage questions grading tagging as testable only when evidence and ticket IDs are recorded.

### 14.3 Tagging

Lena tags each relevant item with ATT&CK identifiers supported by the text. "Attackers sent invoice emails with links" supports T1566; it does not support T1059 unless the text mentions scripts.

Section fourteen point three develops threat intelligence and osint methods with a Corvale Municipal Services note Lena Park can demo offline.

Under section fourteen point three, MCX expects threat claims to carry owners and dates.

Section fourteen point three treats triage questions grading tagging as testable only when evidence and ticket IDs are recorded.

### 14.4 The three-line note

Line one: what happened and where. Line two: relevance to CMS with confidence. Line three: recommended action and owner. Busy owners read three lines.

Section fourteen point four develops threat intelligence and osint methods with a Corvale Municipal Services note Lena Park can demo offline.

Under section fourteen point four, MCX expects threat claims to carry owners and dates.

Section fourteen point four treats triage questions grading tagging as testable only when evidence and ticket IDs are recorded.

For section fourteen point four, Corvale Municipal Services will not accept threat work without a written trail.

### 14.5 Consistency

Lena and her supervisor triage the same ten items monthly and compare decisions, discussing differences.

Section fourteen point five develops threat intelligence and osint methods with a Corvale Municipal Services note Lena Park can demo offline.

Under section fourteen point five, MCX expects threat claims to carry owners and dates.

Section fourteen point five treats triage questions grading tagging as testable only when evidence and ticket IDs are recorded.

For section fourteen point five, Corvale Municipal Services will not accept threat work without a written trail.

### 14.6 Time budget

Triage takes minutes per item. If an item needs more, it moves to analysis with a note explaining why.

Section fourteen point six develops threat intelligence and osint methods with a Corvale Municipal Services note Lena Park can demo offline.

Under section fourteen point six, MCX expects threat claims to carry owners and dates.

Section fourteen point six treats triage questions grading tagging as testable only when evidence and ticket IDs are recorded.

For section fourteen point six, Corvale Municipal Services will not accept threat work without a written trail.

### 14.7 Logging

Every item, including closed ones, is logged with date, source, decision and reason, so patterns in irrelevant traffic can be spotted and sources tuned.

Section fourteen point seven develops threat intelligence and osint methods with a Corvale Municipal Services note Lena Park can demo offline.

Under section fourteen point seven, MCX expects threat claims to carry owners and dates.

Section fourteen point seven treats triage questions grading tagging as testable only when evidence and ticket IDs are recorded.

For section fourteen point seven, Corvale Municipal Services will not accept threat work without a written trail.

### Calibrating with peers

At MCX meetings, analysts from different councils grade the same anonymised item and compare. Differences reveal local habits: one city rates vendor blogs C, another B. Agreeing shared guidance makes grades on shared items mean the same thing to every member, which increases trust in the exchange.

### Worked example

Note: "MCX (B2) reports invoice-themed phishing (T1566) against two councils' finance teams this week. Relevant: CMS finance uses the same invoicing supplier; moderate confidence. Action: email team to add sender domains; finance manager to brief staff."

> **Synthetic case.** The report is invented.

### Errors and limits

Grades and tags are judgments; record reasons.

### Exercises

- **EX040 — Triage quartet.** List the four triage questions. *Rubric:* 3 = relevance, timeliness, actionability, source known; 2 = three; 1 = one; 0 = none.
- **EX041 — Tag support.** Does "attackers sent invoice emails with links" support T1059? Explain. *Rubric:* 3 = no; no scripts mentioned; supports T1566; 2 = no; 1 = yes; 0 = none.
- **EX042 — Three-line note.** Write a three-line note for a fictional advisory. *Rubric:* 3 = what/where, relevance+confidence, action+owner; 2 = two; 1 = one; 0 = none.

### Synthesis

Triage consistently, grade and tag with reasons, and write short notes owners can act on.

### Continue studying — chapter 14 of 30

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Threat intelligence and OSINT: guided lab

### Learning outcomes

You will (1) match indicators against a synthetic DNS log; (2) summarise hits per host with first-seen times; (3) avoid false matches from partial strings; (4) turn results into a hand-off for responders.

### 15.1 Lab setup

The lab uses a synthetic resolver log and two indicators. It runs offline in the course virtual machine with the standard library. Students must not paste real CMS logs into lab files.

Section fifteen point one develops threat intelligence and osint guided with a Corvale Municipal Services note Lena Park can demo offline.

Under section fifteen point one, MCX expects threat claims to carry owners and dates.

Section fifteen point one treats lab setup reading the as testable only when evidence and ticket IDs are recorded.

### Lab — matching a log

```python
"""Lab (ch 15): match a synthetic DNS log against an indicator list and report hits per host."""
iocs = {"pay-portal.example", "update-svc.example"}
log = ["2026-09-04T08:01Z ws-114 intranet.example", "2026-09-04T08:03Z ws-114 pay-portal.example",
       "2026-09-04T08:05Z ws-207 news.example", "2026-09-04T09:12Z ws-207 update-svc.example",
       "2026-09-04T09:13Z ws-207 update-svc.example", "2026-09-04T10:40Z ws-031 pay-portal.example.org"]
hits = {}
for line in log:
    t, host, q = line.split()
    if q in iocs:
        hits.setdefault(host, []).append((t, q))
for h, v in sorted(hits.items()):
    print(h, len(v), "first", v[0][0], v[0][1])
print("non-match kept for review: pay-portal.example.org (suffix differs)")
```

Run with `python3 lab_match.py`. Verified output:

```text
ws-114 1 first 2026-09-04T08:03Z pay-portal.example
ws-207 2 first 2026-09-04T09:12Z update-svc.example
non-match kept for review: pay-portal.example.org (suffix differs)
```

### 15.2 Reading the result

ws-114 looked up pay-portal.example once, first at 08:03 UTC. ws-207 looked up update-svc.example twice, first at 09:12. A lookup of pay-portal.example.org was not matched: it contains the indicator as a substring but is a different domain. The script prints it for review rather than ignoring it silently.

Section fifteen point two develops threat intelligence and osint guided with a Corvale Municipal Services note Lena Park can demo offline.

Under section fifteen point two, MCX expects threat claims to carry owners and dates.

### 15.3 Exact versus substring

Substring matching would flag pay-portal.example.org and perhaps legitimate names. Exact matching on the full name, after normalisation, avoids false alarms. Separate rules can watch for lookalikes deliberately.

Section fifteen point three develops threat intelligence and osint guided with a Corvale Municipal Services note Lena Park can demo offline.

Under section fifteen point three, MCX expects threat claims to carry owners and dates.

Section fifteen point three treats lab setup reading the as testable only when evidence and ticket IDs are recorded.

### 15.4 Hand-off

Responders need host, indicator, first and last time, count and source of the indicator with its TLP. They do not need the script.

Section fifteen point four develops threat intelligence and osint guided with a Corvale Municipal Services note Lena Park can demo offline.

Under section fifteen point four, MCX expects threat claims to carry owners and dates.

Section fifteen point four treats lab setup reading the as testable only when evidence and ticket IDs are recorded.

For section fifteen point four, Corvale Municipal Services will not accept threat work without a written trail.

### 15.5 What a hit means

A DNS lookup shows that a machine asked for a name. It does not prove a connection succeeded or a user entered data. Proxy logs and user contact follow.

Section fifteen point five develops threat intelligence and osint guided with a Corvale Municipal Services note Lena Park can demo offline.

Under section fifteen point five, MCX expects threat claims to carry owners and dates.

Section fifteen point five treats lab setup reading the as testable only when evidence and ticket IDs are recorded.

### 15.6 Repeat lookups

ws-207's two lookups a minute apart may be one browser retry or software checking repeatedly. Repeated automatic lookups over hours would suggest installed software rather than a single click.

Section fifteen point six develops threat intelligence and osint guided with a Corvale Municipal Services note Lena Park can demo offline.

Under section fifteen point six, MCX expects threat claims to carry owners and dates.

Section fifteen point six treats lab setup reading the as testable only when evidence and ticket IDs are recorded.

### 15.7 Lab report

Students record inputs, the command run, the output, interpretation and one improvement they would make, such as reading last-seen times as well as first-seen.

Section fifteen point seven develops threat intelligence and osint guided with a Corvale Municipal Services note Lena Park can demo offline.

Under section fifteen point seven, MCX expects threat claims to carry owners and dates.

Section fifteen point seven treats lab setup reading the as testable only when evidence and ticket IDs are recorded.

For section fifteen point seven, Corvale Municipal Services will not accept threat work without a written trail.

### Worked example

Lena's hand-off: "ws-114 — pay-portal.example (MCX, TLP:GREEN) — 1 lookup at 08:03 UTC. ws-207 — update-svc.example (vendor, TLP:AMBER) — 2 lookups from 09:12 UTC. Please check proxy logs and contact users. One near-miss name (pay-portal.example.org) listed for analyst review."

> **Synthetic case.** The hosts and log are invented teaching material.

### Errors and limits

Logs without client identity (shared resolvers, NAT) cannot pinpoint machines.

### Exercises

- **EX043 — Lab hits.** Report hits per host from the lab with first-seen times. *Rubric:* 3 = ws-114 1 at 08:03 pay-portal; ws-207 2 from 09:12 update-svc; 2 = one host; 1 = wrong; 0 = none.
- **EX044 — Substring trap.** Why was pay-portal.example.org not matched? *Rubric:* 3 = different domain; exact match avoids false alarms; 2 = partial; 1 = bug; 0 = none.
- **EX045 — Lookup meaning.** What does a DNS hit not prove? *Rubric:* 3 = connection success or data entry; needs proxy/user follow-up; 2 = partial; 1 = proves compromise; 0 = none.

### Synthesis

Match exactly, summarise per host, flag near misses for review and hand off what responders need.

### Continue studying — chapter 15 of 30

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Threat intelligence and OSINT: methods II

### Learning outcomes

You will (1) pivot carefully from one indicator to related infrastructure using passive sources; (2) avoid pivoting through shared services; (3) monitor certificate transparency for lookalikes; (4) write findings with confidence levels.

### 16.1 Pivoting

From a fraud domain, an analyst may look at passive DNS (what addresses it used), certificate records (which other names shared the certificate), and registration timing. Each pivot can reveal related infrastructure — or mislead.

Section sixteen point one develops threat intelligence and osint methods with a Corvale Municipal Services note Lena Park can demo offline.

Under section sixteen point one, MCX expects threat claims to carry owners and dates.

Section sixteen point one treats pivoting shared services certificate as testable only when evidence and ticket IDs are recorded.

### 16.2 Shared services

Cloud hosting, content-delivery networks and privacy-protected registrations are shared by thousands of unrelated customers. Pivoting through them links innocent sites. Lena stops a pivot when the shared item serves many unrelated names.

Section sixteen point two develops threat intelligence and osint methods with a Corvale Municipal Services note Lena Park can demo offline.

Under section sixteen point two, MCX expects threat claims to carry owners and dates.

Section sixteen point two treats pivoting shared services certificate as testable only when evidence and ticket IDs are recorded.

### 16.3 Certificate transparency

Publicly trusted certificates appear in public logs. Searching for names containing "corvale" with payment words finds lookalikes early. This is passive and lawful through approved search services.

Section sixteen point three develops threat intelligence and osint methods with a Corvale Municipal Services note Lena Park can demo offline.

Under section sixteen point three, MCX expects threat claims to carry owners and dates.

Section sixteen point three treats pivoting shared services certificate as testable only when evidence and ticket IDs are recorded.

For section sixteen point three, Corvale Municipal Services will not accept threat work without a written trail.

### 16.4 Confidence

Write "likely related" only when two independent pivots agree, such as shared certificate and registration minutes apart. One weak link is "possibly related".

Section sixteen point four develops threat intelligence and osint methods with a Corvale Municipal Services note Lena Park can demo offline.

Under section sixteen point four, MCX expects threat claims to carry owners and dates.

Section sixteen point four treats pivoting shared services certificate as testable only when evidence and ticket IDs are recorded.

For section sixteen point four, Corvale Municipal Services will not accept threat work without a written trail.

### 16.5 Recording pivots

Each pivot step is logged: source, query, result and decision. Others can repeat or challenge it.

Section sixteen point five develops threat intelligence and osint methods with a Corvale Municipal Services note Lena Park can demo offline.

Under section sixteen point five, MCX expects threat claims to carry owners and dates.

Section sixteen point five treats pivoting shared services certificate as testable only when evidence and ticket IDs are recorded.

For section sixteen point five, Corvale Municipal Services will not accept threat work without a written trail.

### 16.6 Stopping rules

Set a limit — three pivots or 30 minutes — unless the supervisor extends it. Endless pivoting wastes time and drifts from CMS's question.

Section sixteen point six develops threat intelligence and osint methods with a Corvale Municipal Services note Lena Park can demo offline.

Under section sixteen point six, MCX expects threat claims to carry owners and dates.

Section sixteen point six treats pivoting shared services certificate as testable only when evidence and ticket IDs are recorded.

For section sixteen point six, Corvale Municipal Services will not accept threat work without a written trail.

### 16.7 Registration data

Public registration records are often redacted for privacy. Analysts do not try to uncover redacted registrant identities; the domain and its timing are enough for defence.

Section sixteen point seven develops threat intelligence and osint methods with a Corvale Municipal Services note Lena Park can demo offline.

Under section sixteen point seven, MCX expects threat claims to carry owners and dates.

Section sixteen point seven treats pivoting shared services certificate as testable only when evidence and ticket IDs are recorded.

For section sixteen point seven, Corvale Municipal Services will not accept threat work without a written trail.

### Takedown requests

Takedowns go through CMS's supervisor or a contracted service, citing the impersonation and evidence. Lena prepares the evidence package — screenshots from approved services, certificate records, resident reports — but does not contact hosting providers herself.

### Worked example

From corvale-permits-pay.example, Lena finds the certificate also covers corvale-tax-pay.example, issued the same minute. Passive DNS shows both on a large cloud provider address shared by thousands of sites, so she does not pivot further through the address. She reports both domains as "likely related, moderate confidence" for blocking and takedown requests.

> **Synthetic case.** The domains are invented.

### Errors and limits

Passive datasets are incomplete and sometimes outdated.

### Exercises

- **EX046 — Stop the pivot.** When should Lena stop pivoting through an address? *Rubric:* 3 = shared by many unrelated sites (cloud/CDN); 2 = partial; 1 = never; 0 = none.
- **EX047 — Likely wording.** What evidence justified "likely related" for the two domains? *Rubric:* 3 = same certificate, issued same minute (two links); 2 = one; 1 = address; 0 = none.
- **EX048 — Redacted registrants.** Should Lena try to uncover redacted registrant identities? *Rubric:* 3 = no; privacy; unnecessary for defence; 2 = no; 1 = yes; 0 = none.

### Synthesis

Pivot passively and briefly, stop at shared services, use certificate transparency and calibrate confidence to independent links.

### Continue studying — chapter 16 of 30

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Threat intelligence and OSINT: tooling

### Learning outcomes

You will (1) describe the tools in a small CTI stack; (2) choose between scripts and platforms; (3) secure the tools themselves; (4) maintain tools sustainably.

### 17.1 The CMS stack

Lena's stack: standard-library Python scripts for parsing and matching, a small open-source threat intelligence platform that stores STIX 2.1 and pulls MCX's TAXII 2.1 collection, the log search tool owned by operations, and a shared ticket queue.

Section seventeen point one develops threat intelligence and osint tooling with a Corvale Municipal Services note Lena Park can demo offline.

Under section seventeen point one, MCX expects threat claims to carry owners and dates.

Section seventeen point one treats the cms stack scripts as testable only when evidence and ticket IDs are recorded.

### 17.2 Scripts or platform

Scripts are flexible and transparent but depend on their author. A platform offers storage, sharing, TLP marking and a web interface but needs maintenance. CMS uses the platform for storage and sharing and scripts for local checks.

Section seventeen point two develops threat intelligence and osint tooling with a Corvale Municipal Services note Lena Park can demo offline.

Under section seventeen point two, MCX expects threat claims to carry owners and dates.

Section seventeen point two treats the cms stack scripts as testable only when evidence and ticket IDs are recorded.

### 17.3 Securing tools

The platform holds TLP:AMBER partner data, so it needs strong authentication, restricted access, updates and backups. A compromised CTI platform would leak partner trust.

Section seventeen point three develops threat intelligence and osint tooling with a Corvale Municipal Services note Lena Park can demo offline.

Under section seventeen point three, MCX expects threat claims to carry owners and dates.

Section seventeen point three treats the cms stack scripts as testable only when evidence and ticket IDs are recorded.

For section seventeen point three, Corvale Municipal Services will not accept threat work without a written trail.

### 17.4 API keys

Keys for MCX's TAXII server live in the platform's secret store, not in scripts or tickets. Rotating them is a scheduled task.

Section seventeen point four develops threat intelligence and osint tooling with a Corvale Municipal Services note Lena Park can demo offline.

Under section seventeen point four, MCX expects threat claims to carry owners and dates.

Section seventeen point four treats the cms stack scripts as testable only when evidence and ticket IDs are recorded.

For section seventeen point four, Corvale Municipal Services will not accept threat work without a written trail.

### 17.5 Maintenance

Each tool has an owner, an update schedule and documentation. Lena writes a README for every script: purpose, inputs, outputs, example run.

Section seventeen point five develops threat intelligence and osint tooling with a Corvale Municipal Services note Lena Park can demo offline.

Under section seventeen point five, MCX expects threat claims to carry owners and dates.

Section seventeen point five treats the cms stack scripts as testable only when evidence and ticket IDs are recorded.

For section seventeen point five, Corvale Municipal Services will not accept threat work without a written trail.

### 17.6 Choosing new tools

Before adding a tool, ask what requirement it serves, who maintains it, what data it touches and how it will be retired. Many small teams accumulate tools nobody uses.

Section seventeen point six develops threat intelligence and osint tooling with a Corvale Municipal Services note Lena Park can demo offline.

Under section seventeen point six, MCX expects threat claims to carry owners and dates.

Section seventeen point six treats the cms stack scripts as testable only when evidence and ticket IDs are recorded.

### 17.7 Licences

Open-source licences and commercial terms both apply. Check before redistributing tool outputs or modifying code for partners.

Section seventeen point seven develops threat intelligence and osint tooling with a Corvale Municipal Services note Lena Park can demo offline.

Under section seventeen point seven, MCX expects threat claims to carry owners and dates.

Section seventeen point seven treats the cms stack scripts as testable only when evidence and ticket IDs are recorded.

For section seventeen point seven, Corvale Municipal Services will not accept threat work without a written trail.

### Testing tool changes

Before upgrading the platform, the team restores last night's backup to a test machine and upgrades that first. If imports or exports break, they find out without losing partner data or interrupting the daily feed to defensive tools.

### Worked example

A colleague finds a browser extension that "auto-checks indicators against 20 online services". Lena reviews it: it sends every highlighted value to external sites, including TLP:AMBER material. She declines it and documents why in the tool register.

> **Synthetic case.** The extension is invented.

### Errors and limits

Tools encode assumptions; read their documentation before trusting outputs.

### Exercises

- **EX049 — Extension risk.** Why was the browser extension declined? *Rubric:* 3 = sends restricted data to external services; TLP breach; 2 = partial; 1 = slow; 0 = none.
- **EX050 — Key storage.** Where should TAXII keys be stored, and where not? *Rubric:* 3 = secret store; not scripts/tickets; 2 = one; 1 = in script; 0 = none.
- **EX051 — Script README.** List the four parts of Lena's script README. *Rubric:* 3 = purpose, inputs, outputs, example run; 2 = three; 1 = one; 0 = none.

### Synthesis

Keep the stack small, secure and documented; choose tools by requirement and protect partner data inside them.

### Continue studying — chapter 17 of 30

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Threat intelligence and OSINT: controls

### Learning outcomes

You will (1) convert intelligence into control changes through owners; (2) write a change request with evidence; (3) verify controls after change; (4) plan rollback.

### 18.1 From note to change

Intelligence becomes protection only when a control changes: a DNS block, an email rule, an endpoint rule, a configuration fix. Lena drafts; owners decide and implement through change management.

Section eighteen point one develops threat intelligence and osint controls with a Corvale Municipal Services note Lena Park can demo offline.

Under section eighteen point one, MCX expects threat claims to carry owners and dates.

Section eighteen point one treats from note to change as testable only when evidence and ticket IDs are recorded.

### 18.2 Change request contents

Intelligence summary with source and TLP, affected asset, proposed change, expected effect, possible side effects, verification method, rollback plan and review date.

Section eighteen point two develops threat intelligence and osint controls with a Corvale Municipal Services note Lena Park can demo offline.

Under section eighteen point two, MCX expects threat claims to carry owners and dates.

Section eighteen point two treats from note to change as testable only when evidence and ticket IDs are recorded.

For section eighteen point two, Corvale Municipal Services will not accept threat work without a written trail.

### 18.3 Verification

After a DNS block, a test lookup from an approved test machine should fail. After an email rule, a harmless test message matching the rule should be quarantined. Results are attached to the change.

Section eighteen point three develops threat intelligence and osint controls with a Corvale Municipal Services note Lena Park can demo offline.

Under section eighteen point three, MCX expects threat claims to carry owners and dates.

Section eighteen point three treats from note to change as testable only when evidence and ticket IDs are recorded.

### 18.4 Rollback

If a block breaks a service, the owner removes it quickly. The plan says how and who approves.

Section eighteen point four develops threat intelligence and osint controls with a Corvale Municipal Services note Lena Park can demo offline.

Under section eighteen point four, MCX expects threat claims to carry owners and dates.

Section eighteen point four treats from note to change as testable only when evidence and ticket IDs are recorded.

For section eighteen point four, Corvale Municipal Services will not accept threat work without a written trail.

### 18.5 Review dates

Domain and address blocks are reviewed after a set period; techniques-based rules are reviewed when ATT&CK or the threat changes.

Section eighteen point five develops threat intelligence and osint controls with a Corvale Municipal Services note Lena Park can demo offline.

Under section eighteen point five, MCX expects threat claims to carry owners and dates.

Section eighteen point five treats from note to change as testable only when evidence and ticket IDs are recorded.

For section eighteen point five, Corvale Municipal Services will not accept threat work without a written trail.

### 18.6 Avoiding overload

Owners receive many requests. Lena bundles low-urgency indicator blocks into a weekly change and keeps single urgent changes for genuine emergencies.

Section eighteen point six develops threat intelligence and osint controls with a Corvale Municipal Services note Lena Park can demo offline.

Under section eighteen point six, MCX expects threat claims to carry owners and dates.

Section eighteen point six treats from note to change as testable only when evidence and ticket IDs are recorded.

For section eighteen point six, Corvale Municipal Services will not accept threat work without a written trail.

### 18.7 Mitigation ideas from ATT&CK

Technique pages list mitigations. For T1566, filtering and user training; for T1078, multi-factor authentication. These guide proposals but must be adapted to CMS tools.

Section eighteen point seven develops threat intelligence and osint controls with a Corvale Municipal Services note Lena Park can demo offline.

Under section eighteen point seven, MCX expects threat claims to carry owners and dates.

Section eighteen point seven treats from note to change as testable only when evidence and ticket IDs are recorded.

For section eighteen point seven, Corvale Municipal Services will not accept threat work without a written trail.

### Measuring effect

After a month, check whether the control did anything: blocked lookups counted by the DNS filter, quarantined messages counted by the gateway. A control with zero hits may still be worthwhile, but the count informs the review decision.

### Worked example

Lena requests a DNS block for the two fraud domains, with an MCX source at TLP:GREEN, verification by test lookup and rollback by removing the entries. The network team applies it in the evening change window. Her test lookup fails as expected; she attaches the result.

> **Synthetic case.** The change is invented.

### Errors and limits

Verification proves the control is active, not that it stops every variant.

### Exercises

- **EX052 — Change contents.** List six items in Lena's change request. *Rubric:* 3 = six of summary/source/TLP, asset, change, effect, side effects, verification, rollback, review; 2 = four; 1 = two; 0 = none.
- **EX053 — Verify email rule.** How can an email rule be verified safely? *Rubric:* 3 = harmless test message matching rule quarantined; 2 = partial; 1 = real phish; 0 = none.
- **EX054 — Bundling.** Why bundle low-urgency blocks weekly? *Rubric:* 3 = reduce owner overload; reserve urgent path; 2 = partial; 1 = no reason; 0 = none.

### Synthesis

Turn intelligence into owner-approved changes with evidence, verify them, plan rollback and review over time.

### Continue studying — chapter 18 of 30

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Threat intelligence and OSINT: monitoring

### Learning outcomes

You will (1) monitor indicator matches over time; (2) apply type-specific expiry rules; (3) watch for lookalike registrations continuously; (4) report monitoring health.

### 19.1 Continuous matching

Matching runs daily against new logs, not just once. A domain from last month can appear today when a staff member opens an old message.

Section nineteen point one develops threat intelligence and osint monitoring with a Corvale Municipal Services note Lena Park can demo offline.

Under section nineteen point one, MCX expects threat claims to carry owners and dates.

Section nineteen point one treats continuous matching reading the as testable only when evidence and ticket IDs are recorded.

For section nineteen point one, Corvale Municipal Services will not accept threat work without a written trail.

### Lab — expiry review

```python
"""Lab (ch 19): flag indicators for review by type-specific age limits (synthetic)."""
from datetime import date
LIMIT = {"ipv4": 30, "domain": 90, "sha256": 365}
today = date(2026, 10, 1)
items = [("198.51.100.23", "ipv4", date(2026, 8, 20)), ("pay-portal.example", "domain", date(2026, 8, 20)),
         ("update-svc.example", "domain", date(2026, 6, 10)), ("ab12" * 16, "sha256", date(2026, 1, 5))]
for v, t, last in items:
    age = (today - last).days
    print(v[:20], t, age, "REVIEW" if age > LIMIT[t] else "keep")
```

Run with `python3 lab_expiry.py`. Verified output:

```text
198.51.100.23 ipv4 42 REVIEW
pay-portal.example domain 42 keep
update-svc.example domain 113 REVIEW
ab12ab12ab12ab12ab12 sha256 269 keep
```

### 19.2 Reading the result

With a reference date of 1 October 2026, the address last seen 42 days ago exceeds its 30-day limit and is flagged for review. The fraud domain at 42 days is within its 90-day limit and kept. update-svc.example at 113 days exceeds 90 and is flagged. The hash at 269 days is within its 365-day limit.

Section nineteen point two develops threat intelligence and osint monitoring with a Corvale Municipal Services note Lena Park can demo offline.

Under section nineteen point two, MCX expects threat claims to carry owners and dates.

### 19.3 Why limits differ

Addresses are reassigned quickly, especially in cloud services, so stale address blocks hit innocent parties. Domains last longer; hashes identify exact files indefinitely, though the file may stop circulating. Bianco's Pyramid of Pain explains this ordering.

Section nineteen point three develops threat intelligence and osint monitoring with a Corvale Municipal Services note Lena Park can demo offline.

Under section nineteen point three, MCX expects threat claims to carry owners and dates.

Section nineteen point three treats continuous matching reading the as testable only when evidence and ticket IDs are recorded.

### 19.4 Review, not delete

Flagged items go to review: check fresh sightings and source updates. Expired items are marked inactive with a date, keeping history.

Section nineteen point four develops threat intelligence and osint monitoring with a Corvale Municipal Services note Lena Park can demo offline.

Under section nineteen point four, MCX expects threat claims to carry owners and dates.

Section nineteen point four treats continuous matching reading the as testable only when evidence and ticket IDs are recorded.

For section nineteen point four, Corvale Municipal Services will not accept threat work without a written trail.

### 19.5 Monitoring health

Lena reports weekly: logs received from each source, matches, flagged expiries and any source that stopped sending. A silent log source is itself an alert.

Section nineteen point five develops threat intelligence and osint monitoring with a Corvale Municipal Services note Lena Park can demo offline.

Under section nineteen point five, MCX expects threat claims to carry owners and dates.

Section nineteen point five treats continuous matching reading the as testable only when evidence and ticket IDs are recorded.

For section nineteen point five, Corvale Municipal Services will not accept threat work without a written trail.

### 19.6 Lookalike watch

A daily certificate-transparency query for CMS-like names runs automatically and lists new matches for triage.

Section nineteen point six develops threat intelligence and osint monitoring with a Corvale Municipal Services note Lena Park can demo offline.

Under section nineteen point six, MCX expects threat claims to carry owners and dates.

Section nineteen point six treats continuous matching reading the as testable only when evidence and ticket IDs are recorded.

For section nineteen point six, Corvale Municipal Services will not accept threat work without a written trail.

### 19.7 Thresholds

Limits are set with owners and written down. Changing them is a recorded decision, not a script edit.

Section nineteen point seven develops threat intelligence and osint monitoring with a Corvale Municipal Services note Lena Park can demo offline.

Under section nineteen point seven, MCX expects threat claims to carry owners and dates.

Section nineteen point seven treats continuous matching reading the as testable only when evidence and ticket IDs are recorded.

For section nineteen point seven, Corvale Municipal Services will not accept threat work without a written trail.

### Alert fatigue

If monitoring produces dozens of low-value matches daily, people stop reading. Tune by removing stale indicators and grouping repeat matches per host, so each alert represents something worth a look.

### Worked example

The weekly health report shows the library resolver sent no logs for three days. The network team finds a full disk on the log forwarder. Matching for those days is rerun after repair, and the gap is noted in the report.

> **Synthetic case.** The outage is invented.

### Errors and limits

Fixed limits are crude; a still-active campaign may justify keeping an old indicator.

### Exercises

- **EX055 — Lab expiry.** Which items did the lab flag for review, and why? *Rubric:* 3 = address 42>30; update-svc 113>90; 2 = one; 1 = wrong; 0 = none.
- **EX056 — Address ageing.** Why do addresses get the shortest limit? *Rubric:* 3 = reassigned quickly, esp. cloud; innocent parties; 2 = partial; 1 = random; 0 = none.
- **EX057 — Silent source.** What did the weekly health report catch, and what followed? *Rubric:* 3 = library resolver silent 3 days; disk full fixed; rerun; gap noted; 2 = partial; 1 = nothing; 0 = none.

### Synthesis

Monitor continuously, expire by type with review, watch for lookalikes and report the health of the monitoring itself.

### Continue studying — chapter 19 of 30

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Threat intelligence and OSINT: troubleshooting

### Learning outcomes

You will (1) diagnose failures in the intelligence pipeline methodically; (2) distinguish data, code and configuration faults; (3) communicate incidents in the pipeline; (4) prevent recurrence.

### 20.1 Symptoms

Typical symptoms: no new indicators today; a spike of false-positive blocks; exports rejected by a tool; matches missing that should exist. Each starts a structured check rather than random fixes.

Section twenty point one develops threat intelligence and osint troubleshooting with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty point one, MCX expects threat claims to carry owners and dates.

Section twenty point one treats symptoms method fault types as testable only when evidence and ticket IDs are recorded.

### 20.2 Method

Work from the source forward: did data arrive? Did parsing accept it? Did the store hold it? Did export send it? Did the tool load it? Check one hand-off at a time and record each result.

Section twenty point two develops threat intelligence and osint troubleshooting with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty point two, MCX expects threat claims to carry owners and dates.

Section twenty point two treats symptoms method fault types as testable only when evidence and ticket IDs are recorded.

### 20.3 Fault types

Data faults: a partner changed a column name or label spelling. Code faults: a script assumed lower-case labels. Configuration faults: an expired API key, a firewall rule blocking TAXII, a full disk.

Section twenty point three develops threat intelligence and osint troubleshooting with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty point three, MCX expects threat claims to carry owners and dates.

Section twenty point three treats symptoms method fault types as testable only when evidence and ticket IDs are recorded.

### 20.4 Communicating

If indicators stopped flowing, tell consumers: "Since 06:00 no new MCX indicators have reached the DNS filter; existing blocks remain; fix expected by noon." Silence makes people assume protection that is not there.

Section twenty point four develops threat intelligence and osint troubleshooting with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty point four, MCX expects threat claims to carry owners and dates.

Section twenty point four treats symptoms method fault types as testable only when evidence and ticket IDs are recorded.

### 20.5 Preventing recurrence

After the fix, add a check: a test that alerts when daily imports fall to zero, or when a new label value appears.

Section twenty point five develops threat intelligence and osint troubleshooting with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty point five, MCX expects threat claims to carry owners and dates.

Section twenty point five treats symptoms method fault types as testable only when evidence and ticket IDs are recorded.

For section twenty point five, Corvale Municipal Services will not accept threat work without a written trail.

### 20.6 Keeping a fault log

Each fault gets an entry: symptom, cause, fix, prevention, time lost. Patterns appear over months — for example, most faults follow partner format changes.

Section twenty point six develops threat intelligence and osint troubleshooting with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty point six, MCX expects threat claims to carry owners and dates.

Section twenty point six treats symptoms method fault types as testable only when evidence and ticket IDs are recorded.

For section twenty point six, Corvale Municipal Services will not accept threat work without a written trail.

### 20.7 Asking for help

Escalate when the fault sits in another team's system. Bring evidence of where the flow stops so they can act quickly.

Section twenty point seven develops threat intelligence and osint troubleshooting with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty point seven, MCX expects threat claims to carry owners and dates.

Section twenty point seven treats symptoms method fault types as testable only when evidence and ticket IDs are recorded.

For section twenty point seven, Corvale Municipal Services will not accept threat work without a written trail.

### Partner format changes

Ask MCX to announce format changes in advance and keep a test file of the new format. Running it through the parser before the change date prevents a Monday morning outage.

### Worked example

On Monday the platform shows zero MCX imports. Lena checks: TAXII requests return "unauthorised". The API key expired over the weekend. She informs consumers, the supervisor renews the key, imports resume, and Lena adds an alert for authentication failures and a calendar reminder 30 days before expiry.

> **Synthetic case.** The outage is invented.

### Errors and limits

Root causes can be multiple; do not stop at the first plausible one if symptoms remain.

### Exercises

- **EX058 — Key fault type.** Classify the expired API key fault and name the prevention added. *Rubric:* 3 = configuration; auth-failure alert + expiry reminder; 2 = one; 1 = data fault; 0 = none.
- **EX059 — Forward check.** In what order should Lena check pipeline hand-offs? *Rubric:* 3 = source→parse→store→export→tool, one at a time; 2 = partial; 1 = random; 0 = none.
- **EX060 — Outage message.** Why must consumers be told when indicators stop flowing? *Rubric:* 3 = avoid false assumption of protection; plan around gap; 2 = partial; 1 = unnecessary; 0 = none.

### Synthesis

Troubleshoot hand-off by hand-off, classify faults, communicate gaps and add checks so the same fault is caught earlier.

### Continue studying — chapter 20 of 30

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Threat intelligence and OSINT: service integration

### Learning outcomes

You will (1) integrate CTI outputs with the service desk, operations and incident response; (2) define simple service levels; (3) route items to the right team; (4) gather feedback systematically.

### 21.1 Consumers

The service desk receives resident and staff reports of suspicious messages. Operations runs monitoring tools. Incident response handles confirmed incidents. Communications warns the public. Each needs a different product.

Section twenty-one point one develops threat intelligence and osint service with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-one point one, MCX expects threat claims to carry owners and dates.

Section twenty-one point one treats consumers service desk operations as testable only when evidence and ticket IDs are recorded.

### 21.2 Service desk

Lena gives the service desk a short weekly list of current scams with sample subject lines and what to tell callers. When reports come in, the desk forwards samples to the CTI queue, closing the loop.

Section twenty-one point two develops threat intelligence and osint service with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-one point two, MCX expects threat claims to carry owners and dates.

Section twenty-one point two treats consumers service desk operations as testable only when evidence and ticket IDs are recorded.

### 21.3 Operations

Operations receives indicators through the platform's export and technique notes for tuning alerts. Urgent items come by phone.

Section twenty-one point three develops threat intelligence and osint service with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-one point three, MCX expects threat claims to carry owners and dates.

Section twenty-one point three treats consumers service desk operations as testable only when evidence and ticket IDs are recorded.

For section twenty-one point three, Corvale Municipal Services will not accept threat work without a written trail.

### 21.4 Incident response

During incidents, Lena searches for related indicators and checks MCX for similar cases, following the incident lead's priorities. NIST SP 800-61r3 places such intelligence support within incident response.

Section twenty-one point four develops threat intelligence and osint service with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-one point four, MCX expects threat claims to carry owners and dates.

Section twenty-one point four treats consumers service desk operations as testable only when evidence and ticket IDs are recorded.

### 21.5 Service levels

Urgent items reviewed within four hours in working time; routine items within two days; weekly scam list every Monday.

Section twenty-one point five develops threat intelligence and osint service with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-one point five, MCX expects threat claims to carry owners and dates.

Section twenty-one point five treats consumers service desk operations as testable only when evidence and ticket IDs are recorded.

For section twenty-one point five, Corvale Municipal Services will not accept threat work without a written trail.

### 21.6 Feedback

A two-question monthly form: what helped, what was noise. Answers adjust content.

Section twenty-one point six develops threat intelligence and osint service with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-one point six, MCX expects threat claims to carry owners and dates.

Section twenty-one point six treats consumers service desk operations as testable only when evidence and ticket IDs are recorded.

For section twenty-one point six, Corvale Municipal Services will not accept threat work without a written trail.

### 21.7 Routing table

A table maps item types to teams: fraud against residents to communications and web; staff phishing to email and service desk; vulnerabilities to system owners; partner compromise to supervisor.

Section twenty-one point seven develops threat intelligence and osint service with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-one point seven, MCX expects threat claims to carry owners and dates.

Section twenty-one point seven treats consumers service desk operations as testable only when evidence and ticket IDs are recorded.

### Communications partnership

Public warnings must be accurate and calm. Lena gives communications a plain description — what the scam looks like, what the council will never ask for, how to report it — and leaves wording and timing to them. Agreeing a template in advance makes the next warning faster.

### Worked example

The service desk reports twenty calls about a fake parking-fine text. Lena checks: the domain is new and absent from MCX. She adds it to the block request, sends a CLEAR description to communications for a public warning and shares a GREEN item with MCX so neighbouring councils can prepare.

> **Synthetic case.** The text and calls are invented.

### Errors and limits

Service levels slip during staff absence; plan cover.

### Exercises

- **EX061 — Desk loop.** How does the service desk close the intelligence loop? *Rubric:* 3 = forwards reported samples to CTI queue; 2 = partial; 1 = none; 0 = none.
- **EX062 — Parking text routing.** Which three teams or bodies received outputs from the parking-fine case? *Rubric:* 3 = network block, communications, MCX; 2 = two; 1 = one; 0 = none.
- **EX063 — Routing table.** Where should a vulnerability advisory be routed? *Rubric:* 3 = system owner (via asset list); 2 = IT generally; 1 = communications; 0 = none.

### Synthesis

Serve each consumer with the product it needs, set service levels, route by type and collect feedback.

### Continue studying — chapter 21 of 30

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Threat intelligence and OSINT: automation

### Learning outcomes

You will (1) choose which CTI tasks to automate; (2) design automation with human checkpoints; (3) log automated decisions; (4) avoid automating unsafe actions.

### 22.1 Good candidates

Repetitive, rule-based tasks: importing feeds, normalising, deduplicating, matching logs, flagging expiries, producing weekly counts.

Section twenty-two point one develops threat intelligence and osint automation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-two point one, MCX expects threat claims to carry owners and dates.

Section twenty-two point one treats good candidates poor candidates as testable only when evidence and ticket IDs are recorded.

For section twenty-two point one, Corvale Municipal Services will not accept threat work without a written trail.

### 22.2 Poor candidates

Judgment tasks: deciding relevance of a novel report, grading new sources, writing assessments, blocking on critical systems.

Section twenty-two point two develops threat intelligence and osint automation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-two point two, MCX expects threat claims to carry owners and dates.

Section twenty-two point two treats good candidates poor candidates as testable only when evidence and ticket IDs are recorded.

For section twenty-two point two, Corvale Municipal Services will not accept threat work without a written trail.

### 22.3 Human checkpoints

Automation proposes; humans approve where impact is high. Lena's pipeline auto-exports indicators to the DNS filter only from MCX at TLP:GREEN or CLEAR with grade B or better; others wait for review.

Section twenty-two point three develops threat intelligence and osint automation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-two point three, MCX expects threat claims to carry owners and dates.

Section twenty-two point three treats good candidates poor candidates as testable only when evidence and ticket IDs are recorded.

### 22.4 Logging

Every automated action logs input, rule applied and output. When a block causes complaints, the log shows exactly why it happened.

Section twenty-two point four develops threat intelligence and osint automation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-two point four, MCX expects threat claims to carry owners and dates.

Section twenty-two point four treats good candidates poor candidates as testable only when evidence and ticket IDs are recorded.

For section twenty-two point four, Corvale Municipal Services will not accept threat work without a written trail.

### 22.5 Unsafe automation

Never automate contact with adversary infrastructure — automated visits, downloads or scans of suspicious sites. Never automate sharing of AMBER or RED data outward.

Section twenty-two point five develops threat intelligence and osint automation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-two point five, MCX expects threat claims to carry owners and dates.

Section twenty-two point five treats good candidates poor candidates as testable only when evidence and ticket IDs are recorded.

For section twenty-two point five, Corvale Municipal Services will not accept threat work without a written trail.

### 22.6 Scheduling

Jobs run at fixed times with alerts on failure. A job that fails silently is worse than none.

Section twenty-two point six develops threat intelligence and osint automation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-two point six, MCX expects threat claims to carry owners and dates.

Section twenty-two point six treats good candidates poor candidates as testable only when evidence and ticket IDs are recorded.

For section twenty-two point six, Corvale Municipal Services will not accept threat work without a written trail.

### 22.7 Small steps

Automate one task, run it alongside manual work for two weeks, compare results, then switch.

Section twenty-two point seven develops threat intelligence and osint automation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-two point seven, MCX expects threat claims to carry owners and dates.

Section twenty-two point seven treats good candidates poor candidates as testable only when evidence and ticket IDs are recorded.

For section twenty-two point seven, Corvale Municipal Services will not accept threat work without a written trail.

### Maintaining automated jobs

Each job has an owner, a short description, its schedule and its failure alert recipient. When a job's owner changes role, ownership transfers explicitly; orphaned jobs are a frequent cause of silent pipeline decay. Twice a year Lena reviews every job and retires those that no longer serve a requirement, because each running job is code that must be maintained and secured. A job inventory makes this review quick, and it also helps auditors see exactly which decisions are taken by machines and which by people.

### Worked example

Lena automates weekly expiry flagging. For two weeks she compares the script's list with her manual list: the script catches two items she missed and misses none. She switches to the script, keeping a monthly manual spot-check.

> **Synthetic case.** The comparison is invented.

### Errors and limits

Automation multiplies mistakes as fast as successes; test thoroughly.

### Exercises

- **EX064 — Auto-export rule.** Which items does Lena's pipeline auto-export to DNS? *Rubric:* 3 = MCX, GREEN/CLEAR, grade B or better; 2 = two conditions; 1 = all; 0 = none.
- **EX065 — Never automate.** Name two things that must never be automated. *Rubric:* 3 = contact with adversary infra; outward AMBER/RED sharing; 2 = one; 1 = imports; 0 = none.
- **EX066 — Parallel run.** Why run automation alongside manual work first? *Rubric:* 3 = compare results; catch errors before relying; 2 = partial; 1 = unnecessary; 0 = none.

### Synthesis

Automate repetitive rules, keep humans on judgment and high impact, log everything and never automate unsafe contact or sharing.

### Continue studying — chapter 22 of 30

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Threat intelligence and OSINT: evaluation

### Learning outcomes

You will (1) evaluate sources and products against requirements; (2) compute simple usefulness measures; (3) gather consumer judgments; (4) recommend keeping, changing or dropping a source.

### 23.1 What to evaluate

Sources (MCX, vendor list, public advisories) and products (weekly scam list, three-line notes, block requests). Each should serve a requirement.

Section twenty-three point one develops threat intelligence and osint evaluation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-three point one, MCX expects threat claims to carry owners and dates.

Section twenty-three point one treats what to evaluate source as testable only when evidence and ticket IDs are recorded.

For section twenty-three point one, Corvale Municipal Services will not accept threat work without a written trail.

### 23.2 Source measures

For each source over a quarter: items received, items relevant to CMS, items leading to action, false positives reported, median delay from first public appearance. A ratio of actionable to received gives a rough usefulness figure.

Section twenty-three point two develops threat intelligence and osint evaluation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-three point two, MCX expects threat claims to carry owners and dates.

Section twenty-three point two treats what to evaluate source as testable only when evidence and ticket IDs are recorded.

### 23.3 Product measures

For products: did consumers read them, act on them, find them clear? The monthly feedback form and service-desk call reasons answer these.

Section twenty-three point three develops threat intelligence and osint evaluation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-three point three, MCX expects threat claims to carry owners and dates.

Section twenty-three point three treats what to evaluate source as testable only when evidence and ticket IDs are recorded.

For section twenty-three point three, Corvale Municipal Services will not accept threat work without a written trail.

### 23.4 Comparing fairly

Compare sources over the same period and against the same requirements. A source covering a different threat may look worse but fill a gap.

Section twenty-three point four develops threat intelligence and osint evaluation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-three point four, MCX expects threat claims to carry owners and dates.

Section twenty-three point four treats what to evaluate source as testable only when evidence and ticket IDs are recorded.

For section twenty-three point four, Corvale Municipal Services will not accept threat work without a written trail.

### 23.5 Recommendations

Keep, change (for example, filter by type) or drop. Each recommendation states evidence and cost.

Section twenty-three point five develops threat intelligence and osint evaluation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-three point five, MCX expects threat claims to carry owners and dates.

Section twenty-three point five treats what to evaluate source as testable only when evidence and ticket IDs are recorded.

For section twenty-three point five, Corvale Municipal Services will not accept threat work without a written trail.

### 23.6 Small numbers

A quarter may hold few actionable items; avoid strong claims from tiny counts and repeat next quarter.

Section twenty-three point six develops threat intelligence and osint evaluation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-three point six, MCX expects threat claims to carry owners and dates.

Section twenty-three point six treats what to evaluate source as testable only when evidence and ticket IDs are recorded.

For section twenty-three point six, Corvale Municipal Services will not accept threat work without a written trail.

### 23.7 Writing the evaluation

One page: question, method, table, interpretation, recommendation, limits. Managers read the recommendation first.

Section twenty-three point seven develops threat intelligence and osint evaluation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-three point seven, MCX expects threat claims to carry owners and dates.

Section twenty-three point seven treats what to evaluate source as testable only when evidence and ticket IDs are recorded.

For section twenty-three point seven, Corvale Municipal Services will not accept threat work without a written trail.

### Cost per useful item

Include cost: the vendor list's licence and the analyst hours spent triaging its matches. Dividing total cost by actionable items gives a rough price per useful item. MCX membership costs little, while the vendor list's price per action was high until filtering cut wasted triage. Present this figure carefully, since some value — such as context that shaped a decision — never appears as an action count.

### Worked example

Over a quarter MCX delivered 120 items, 30 relevant and 12 actionable; the vendor list delivered 2,000 indicators, 40 matched CMS logs and 6 led to action, with 9 false-positive complaints. Lena recommends keeping MCX, and filtering the vendor list to domains only, where its false-positive rate was lowest.

> **Synthetic case.** The figures are invented.

### Errors and limits

Actions are not the only value; context that prevented a wrong decision is hard to count.

### Exercises

- **EX067 — Actionable ratio.** Compute the actionable-to-received ratio for MCX. *Rubric:* 3 = 12/120 = 10%; 2 = number; 1 = wrong; 0 = none.
- **EX068 — Vendor change.** What change did Lena recommend for the vendor list, and why? *Rubric:* 3 = filter to domains; lowest false-positive rate; 2 = change only; 1 = drop; 0 = none.
- **EX069 — Gap source.** Why might a low-scoring source still be worth keeping? *Rubric:* 3 = covers a different threat/fills gap; 2 = partial; 1 = never; 0 = none.

### Synthesis

Evaluate sources and products against requirements with simple measures, compare fairly and recommend with evidence.

### Continue studying — chapter 23 of 30

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Applied research methods

### Learning outcomes

You will (1) frame a practical research question for a CTI improvement; (2) collect and code data systematically; (3) analyse results simply and honestly; (4) respect research ethics in the workplace.

### 24.1 Practical questions

"Does the weekly scam list reduce service-desk calls that need escalation?" is answerable with existing data. "Are councils safer with CTI?" is too broad.

Section twenty-four point one develops applied research methods with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-four point one, MCX expects applied claims to carry owners and dates.

Section twenty-four point one treats practical questions data collection as testable only when evidence and ticket IDs are recorded.

For section twenty-four point one, Corvale Municipal Services will not accept applied work without a written trail.

### 24.2 Data collection

Use existing records — tickets, logs, feedback forms — where policy allows. Define what counts before collecting: an escalated call means one forwarded to the CTI queue.

Section twenty-four point two develops applied research methods with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-four point two, MCX expects applied claims to carry owners and dates.

Section twenty-four point two treats practical questions data collection as testable only when evidence and ticket IDs are recorded.

For section twenty-four point two, Corvale Municipal Services will not accept applied work without a written trail.

### 24.3 Coding

When reading free-text tickets, use a small set of categories with examples. Code a sample twice, a week apart, to check your own consistency.

Section twenty-four point three develops applied research methods with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-four point three, MCX expects applied claims to carry owners and dates.

Section twenty-four point three treats practical questions data collection as testable only when evidence and ticket IDs are recorded.

For section twenty-four point three, Corvale Municipal Services will not accept applied work without a written trail.

### 24.4 Simple analysis

Counts before and after, by week, with a chart. Note other changes in the same period, such as a news story about scams, that could explain differences.

Section twenty-four point four develops applied research methods with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-four point four, MCX expects applied claims to carry owners and dates.

Section twenty-four point four treats practical questions data collection as testable only when evidence and ticket IDs are recorded.

For section twenty-four point four, Corvale Municipal Services will not accept applied work without a written trail.

### 24.5 Ethics

Tickets contain residents' and staff's personal data. Use only what the question needs, remove names, store results securely and get the manager's and data-protection officer's approval.

Section twenty-four point five develops applied research methods with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-four point five, MCX expects applied claims to carry owners and dates.

Section twenty-four point five treats practical questions data collection as testable only when evidence and ticket IDs are recorded.

For section twenty-four point five, Corvale Municipal Services will not accept applied work without a written trail.

### 24.6 Reporting honestly

State what changed, what else might explain it and how confident you are. A small improvement with honest caveats is more useful than an inflated claim.

Section twenty-four point six develops applied research methods with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-four point six, MCX expects applied claims to carry owners and dates.

Section twenty-four point six treats practical questions data collection as testable only when evidence and ticket IDs are recorded.

For section twenty-four point six, Corvale Municipal Services will not accept applied work without a written trail.

### 24.7 Literature

Look for published guidance and studies on security awareness and CTI sharing; cite sources you actually read.

Section twenty-four point seven develops applied research methods with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-four point seven, MCX expects applied claims to carry owners and dates.

Section twenty-four point seven treats practical questions data collection as testable only when evidence and ticket IDs are recorded.

For section twenty-four point seven, Corvale Municipal Services will not accept applied work without a written trail.

### Choosing a time window

Pick equal periods before and after the change and avoid holidays or known campaign peaks that would distort counts. Eight weeks each side gave Lena enough calls to see a pattern without waiting a whole year. Write the window down before looking at results, so it cannot be adjusted to make the change look better.

### Worked example

Lena compares eight weeks before and after starting the scam list. Escalated calls fell from 34 to 21, while total scam-related calls stayed similar. She notes that a regional news story about scams ran during the "after" period, which might have helped callers recognise scams themselves.

> **Synthetic case.** The numbers are invented.

### Errors and limits

Before/after comparisons cannot prove causation; they suggest.

### Exercises

- **EX070 — Define the measure.** Define "escalated call" for Lena's study. *Rubric:* 3 = call forwarded to CTI queue, defined before collection; 2 = vague definition; 1 = none; 0 = none.
- **EX071 — Confounder.** What else might explain the fall in escalations? *Rubric:* 3 = regional news story/other awareness; 2 = vague; 1 = none; 0 = none.
- **EX072 — Ticket ethics.** List three ethical steps when using tickets as data. *Rubric:* 3 = minimise, remove names, secure storage, approvals; 2 = two; 1 = one; 0 = none.

### Synthesis

Ask practical questions, define measures first, code consistently, analyse simply and report with honest caveats.

### Continue studying — chapter 24 of 30

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Team project studio

### Learning outcomes

You will (1) plan and deliver a small CTI tool or process as a team; (2) divide roles and review each other's work; (3) manage scope and deadlines; (4) present results to a client.

### 25.1 The brief

Teams of three build a "lookalike watch" for a fictional client council: generate candidate names, check them against a provided synthetic certificate-log extract, triage matches and produce a weekly report template.

Section twenty-five point one develops team project studio with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-five point one, MCX expects team claims to carry owners and dates.

Section twenty-five point one treats the brief roles planning as testable only when evidence and ticket IDs are recorded.

### 25.2 Roles

One student owns the generator, one the matcher, one triage and reporting. Each reviews another's work. Roles rotate at mid-point so everyone learns all parts.

Section twenty-five point two develops team project studio with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-five point two, MCX expects team claims to carry owners and dates.

Section twenty-five point two treats the brief roles planning as testable only when evidence and ticket IDs are recorded.

For section twenty-five point two, Corvale Municipal Services will not accept team work without a written trail.

### 25.3 Planning

A simple board with to-do, doing and done columns. Weekly stand-ups: what I did, what I will do, what blocks me.

Section twenty-five point three develops team project studio with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-five point three, MCX expects team claims to carry owners and dates.

Section twenty-five point three treats the brief roles planning as testable only when evidence and ticket IDs are recorded.

For section twenty-five point three, Corvale Municipal Services will not accept team work without a written trail.

### 25.4 Scope

The client asks midway for SMS-scam monitoring. The team records it, estimates effort and agrees with the tutor to note it as future work.

Section twenty-five point four develops team project studio with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-five point four, MCX expects team claims to carry owners and dates.

Section twenty-five point four treats the brief roles planning as testable only when evidence and ticket IDs are recorded.

For section twenty-five point four, Corvale Municipal Services will not accept team work without a written trail.

### 25.5 Quality

Each component has tests on synthetic inputs. The final report includes a table of planted lookalikes found and missed.

Section twenty-five point five develops team project studio with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-five point five, MCX expects team claims to carry owners and dates.

Section twenty-five point five treats the brief roles planning as testable only when evidence and ticket IDs are recorded.

For section twenty-five point five, Corvale Municipal Services will not accept team work without a written trail.

### 25.6 Ethics in the studio

All data is synthetic. The team must not run the generator against live certificate services during the studio unless the tutor approves and terms allow.

Section twenty-five point six develops team project studio with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-five point six, MCX expects team claims to carry owners and dates.

Section twenty-five point six treats the brief roles planning as testable only when evidence and ticket IDs are recorded.

For section twenty-five point six, Corvale Municipal Services will not accept team work without a written trail.

### 25.7 Presentation

Ten minutes to the client panel: problem, demo on synthetic data, results, limits, next steps.

Section twenty-five point seven develops team project studio with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-five point seven, MCX expects team claims to carry owners and dates.

Section twenty-five point seven treats the brief roles planning as testable only when evidence and ticket IDs are recorded.

For section twenty-five point seven, Corvale Municipal Services will not accept team work without a written trail.

### Handling disagreement

Teams disagree about design. Agree a rule early: the component owner decides after hearing the reviewer, and unresolved issues go to the tutor with both views written down. Disagreement handled openly improves the design; disagreement left unspoken delays it.

### Worked example

Lena's team finds their generator misses names that replace "o" with "0". The reviewer catches it with a planted test case. They add the rule; the next run finds all twelve planted lookalikes and flags three harmless names, which triage dismisses.

> **Synthetic case.** The client and data are invented teaching material.

### Errors and limits

Team projects reward visible work; make sure reviewing and testing are credited too.

### Exercises

- **EX073 — Role rotation.** Why rotate roles at mid-point? *Rubric:* 3 = everyone learns all parts; reduces dependency; 2 = partial; 1 = no reason; 0 = none.
- **EX074 — SMS request.** How was the client's mid-project SMS request handled? *Rubric:* 3 = recorded, estimated, agreed as future work; 2 = partial; 1 = added immediately; 0 = none.
- **EX075 — Planted cases.** How did planted test cases improve the generator? *Rubric:* 3 = revealed missing 0-for-o rule; after fix all 12 found; 2 = partial; 1 = none; 0 = none.

### Synthesis

Plan with clear roles, review each other, control scope, test with planted cases and present honestly.

### Continue studying — chapter 25 of 30

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Threat intelligence and OSINT: operational handoff

### Learning outcomes

You will (1) hand over CTI duties between shifts or staff; (2) write a handover note; (3) transfer open items and their handling labels; (4) keep continuity during absence.

### 26.1 Why handover matters

Intelligence work spans days: an advisory awaits a patch, a takedown request awaits a reply, a fraud wave continues. Without handover, items stall when someone is away.

Section twenty-six point one develops threat intelligence and osint operational with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-six point one, MCX expects threat claims to carry owners and dates.

Section twenty-six point one treats why handover matters handover as testable only when evidence and ticket IDs are recorded.

For section twenty-six point one, Corvale Municipal Services will not accept threat work without a written trail.

### 26.2 Handover note

Open items with status, owner and next step; scheduled jobs and their health; partner commitments such as promised MCX feedback; anything unusual seen this week. Each item keeps its TLP label.

Section twenty-six point two develops threat intelligence and osint operational with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-six point two, MCX expects threat claims to carry owners and dates.

Section twenty-six point two treats why handover matters handover as testable only when evidence and ticket IDs are recorded.

### 26.3 Access

The cover person needs platform access, the ticket queue and MCX portal access approved in advance. Sharing passwords is not handover; individual accounts are.

Section twenty-six point three develops threat intelligence and osint operational with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-six point three, MCX expects threat claims to carry owners and dates.

Section twenty-six point three treats why handover matters handover as testable only when evidence and ticket IDs are recorded.

For section twenty-six point three, Corvale Municipal Services will not accept threat work without a written trail.

### 26.4 Restricted items

TLP:RED items go only to named recipients. If the cover person is not named, the item is noted as "restricted item pending; supervisor holds details".

Section twenty-six point four develops threat intelligence and osint operational with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-six point four, MCX expects threat claims to carry owners and dates.

Section twenty-six point four treats why handover matters handover as testable only when evidence and ticket IDs are recorded.

For section twenty-six point four, Corvale Municipal Services will not accept threat work without a written trail.

### 26.5 Verbal briefing

A fifteen-minute conversation alongside the written note catches nuance: "the parks owner prefers phone calls".

Section twenty-six point five develops threat intelligence and osint operational with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-six point five, MCX expects threat claims to carry owners and dates.

Section twenty-six point five treats why handover matters handover as testable only when evidence and ticket IDs are recorded.

For section twenty-six point five, Corvale Municipal Services will not accept threat work without a written trail.

### 26.6 Return

On return, the person reads the cover log and confirms each item's state before resuming.

Section twenty-six point six develops threat intelligence and osint operational with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-six point six, MCX expects threat claims to carry owners and dates.

Section twenty-six point six treats why handover matters handover as testable only when evidence and ticket IDs are recorded.

For section twenty-six point six, Corvale Municipal Services will not accept threat work without a written trail.

### 26.7 Templates

A fixed template with the same headings every time speeds writing and reading. Missing sections are visible at a glance.

Section twenty-six point seven develops threat intelligence and osint operational with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-six point seven, MCX expects threat claims to carry owners and dates.

Section twenty-six point seven treats why handover matters handover as testable only when evidence and ticket IDs are recorded.

For section twenty-six point seven, Corvale Municipal Services will not accept threat work without a written trail.

### 26.8 Long absence

For absences over two weeks, the supervisor reassigns items formally rather than leaving them with temporary cover.

Section twenty-six point eight develops threat intelligence and osint operational with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-six point eight, MCX expects threat claims to carry owners and dates.

Section twenty-six point eight treats why handover matters handover as testable only when evidence and ticket IDs are recorded.

For section twenty-six point eight, Corvale Municipal Services will not accept threat work without a written trail.

### Handover in incidents

During a live incident, handover happens at shift change with the incident lead present. The outgoing person states current hypotheses, pending searches and promised updates, so the incoming person does not repeat work or contradict earlier messages.

### Worked example

Before a week's leave, Lena hands over to a colleague: four open items, one awaiting the hosting provider's takedown reply, the weekly scam list due Monday, an MCX feedback form due Friday, and one TLP:RED item noted only as "held by supervisor". On return everything has moved except the takedown, which is chased.

> **Synthetic case.** The items are invented.

### Errors and limits

Notes cannot hold everything; the verbal briefing fills gaps.

### Exercises

- **EX076 — Handover parts.** List four sections of a handover note. *Rubric:* 3 = open items, jobs health, partner commitments, unusual observations; 2 = three; 1 = one; 0 = none.
- **EX077 — RED in handover.** How should a TLP:RED item appear in a handover to someone not named? *Rubric:* 3 = noted only as pending, details held by supervisor; 2 = partial; 1 = full details; 0 = none.
- **EX078 — Access, not passwords.** Why must cover use individual accounts? *Rubric:* 3 = accountability/audit; password sharing breaches policy; 2 = partial; 1 = sharing fine; 0 = none.

### Synthesis

Write structured handovers, keep labels, arrange access properly, brief verbally and check items on return.

### Continue studying — chapter 26 of 30

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Deployment and validation

### Learning outcomes

You will (1) deploy a CTI script or process into production safely; (2) validate outputs against known cases; (3) plan monitoring after deployment; (4) document acceptance.

### 27.1 From lab to production

A script that worked on synthetic data now meets real feeds and logs. Deployment moves it to a managed server, under a service account with minimum rights, scheduled and monitored.

Section twenty-seven point one develops deployment and validation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-seven point one, MCX expects deployment claims to carry owners and dates.

Section twenty-seven point one treats from lab to production as testable only when evidence and ticket IDs are recorded.

### 27.2 Validation set

Before go-live, run the script on a validation set: a sample of real past indicators and logs where results are already known — matches that were confirmed, near misses that were not. Outputs must agree.

Section twenty-seven point two develops deployment and validation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-seven point two, MCX expects deployment claims to carry owners and dates.

Section twenty-seven point two treats from lab to production as testable only when evidence and ticket IDs are recorded.

### 27.3 Acceptance criteria

Written beforehand: no missed known matches; false-positive rate no worse than the manual process; runtime under ten minutes; failure alerts reach the team.

Section twenty-seven point three develops deployment and validation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-seven point three, MCX expects deployment claims to carry owners and dates.

Section twenty-seven point three treats from lab to production as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point three, Corvale Municipal Services will not accept deployment work without a written trail.

### 27.4 Staged rollout

Run in report-only mode for two weeks, producing outputs humans check but no automatic exports. Then enable exports.

Section twenty-seven point four develops deployment and validation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-seven point four, MCX expects deployment claims to carry owners and dates.

Section twenty-seven point four treats from lab to production as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point four, Corvale Municipal Services will not accept deployment work without a written trail.

### 27.5 Rights

The service account can read logs and write to the store; it cannot change firewall rules. Least privilege limits damage if the script misbehaves.

Section twenty-seven point five develops deployment and validation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-seven point five, MCX expects deployment claims to carry owners and dates.

Section twenty-seven point five treats from lab to production as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point five, Corvale Municipal Services will not accept deployment work without a written trail.

### 27.6 Documentation

A deployment record: version, date, configuration, validation results, approver.

Section twenty-seven point six develops deployment and validation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-seven point six, MCX expects deployment claims to carry owners and dates.

Section twenty-seven point six treats from lab to production as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point six, Corvale Municipal Services will not accept deployment work without a written trail.

Section twenty-seven point six fails closed if deployment evidence is missing rather than guessing.

### 27.7 Rollback

Keep the previous version ready; if outputs go wrong, switch back and investigate.

Section twenty-seven point seven develops deployment and validation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-seven point seven, MCX expects deployment claims to carry owners and dates.

Section twenty-seven point seven treats from lab to production as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point seven, Corvale Municipal Services will not accept deployment work without a written trail.

### 27.8 Privacy in validation

Validation data comes from real logs, so it contains personal data. Keep it on the managed server, use only what is needed and delete the extract after acceptance.

Section twenty-seven point eight develops deployment and validation with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-seven point eight, MCX expects deployment claims to carry owners and dates.

Section twenty-seven point eight treats from lab to production as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point eight, Corvale Municipal Services will not accept deployment work without a written trail.

### Change approval

Deployment goes through the normal change process: description, risk, test evidence, rollback and approver. Treating CTI scripts as production software, rather than personal tools, means operations knows they exist and can support them out of hours. It also ensures someone other than the author can restart or disable the job safely.

### Worked example

Lena's matching script runs report-only for two weeks. It finds every match the manual process found plus one extra, confirmed real by the supervisor. Runtime is four minutes. The manager signs acceptance and exports are enabled.

> **Synthetic case.** The results are invented.

### Errors and limits

Validation sets age; refresh them when data formats change.

### Exercises

- **EX079 — Acceptance list.** List four acceptance criteria for the matching script. *Rubric:* 3 = no missed known matches, FP ≤ manual, runtime, alerts; 2 = three; 1 = one; 0 = none.
- **EX080 — Report-only mode.** What is report-only mode and why use it? *Rubric:* 3 = outputs checked by humans, no automatic action; catch errors safely; 2 = partial; 1 = none; 0 = none.
- **EX081 — Service account rights.** What rights should the script's account lack, and why? *Rubric:* 3 = no firewall/control changes; limits damage; 2 = partial; 1 = admin fine; 0 = none.

### Synthesis

Deploy with least privilege, validate against known cases, roll out in stages, document acceptance and keep rollback ready.

### Continue studying — chapter 27 of 30

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Field practice

### Learning outcomes

You will (1) work under supervision in a real CTI environment; (2) apply confidentiality agreements; (3) keep a practice journal; (4) receive and act on feedback.

### 28.1 Placement

Lena spends six weeks with MCX's coordination desk under a confidentiality agreement. She sees how members' submissions are checked, labelled and redistributed.

Section twenty-eight point one develops field practice with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-eight point one, MCX expects field claims to carry owners and dates.

Section twenty-eight point one treats placement confidentiality tasks journal as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point one, Corvale Municipal Services will not accept field work without a written trail.

### 28.2 Confidentiality

Everything seen on placement stays there unless released. Her coursework uses synthetic examples inspired by patterns, never real member details.

Section twenty-eight point two develops field practice with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-eight point two, MCX expects field claims to carry owners and dates.

Section twenty-eight point two treats placement confidentiality tasks journal as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point two, Corvale Municipal Services will not accept field work without a written trail.

### 28.3 Tasks

Normalising submissions, checking labels, drafting summaries for review, answering members' format questions. She does not approve releases.

Section twenty-eight point three develops field practice with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-eight point three, MCX expects field claims to carry owners and dates.

Section twenty-eight point three treats placement confidentiality tasks journal as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point three, Corvale Municipal Services will not accept field work without a written trail.

### 28.4 Journal

Daily notes: what I did, what I learned, what I would ask. Notes contain no restricted details; they record lessons, not data.

Section twenty-eight point four develops field practice with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-eight point four, MCX expects field claims to carry owners and dates.

Section twenty-eight point four treats placement confidentiality tasks journal as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point four, Corvale Municipal Services will not accept field work without a written trail.

### 28.5 Feedback

Her mentor reviews every draft. Early feedback: "Your summaries bury the action at the end." Lena moves actions to the first line.

Section twenty-eight point five develops field practice with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-eight point five, MCX expects field claims to carry owners and dates.

Section twenty-eight point five treats placement confidentiality tasks journal as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point five, Corvale Municipal Services will not accept field work without a written trail.

### 28.6 Professional conduct

Arrive prepared, ask questions, admit mistakes immediately. A wrong label caught early is a lesson; one hidden is a breach.

Section twenty-eight point six develops field practice with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-eight point six, MCX expects field claims to carry owners and dates.

Section twenty-eight point six treats placement confidentiality tasks journal as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point six, Corvale Municipal Services will not accept field work without a written trail.

### 28.7 Assessment

The placement supervisor rates reliability, handling discipline, communication and learning; the journal shows reflection.

Section twenty-eight point seven develops field practice with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-eight point seven, MCX expects field claims to carry owners and dates.

Section twenty-eight point seven treats placement confidentiality tasks journal as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point seven, Corvale Municipal Services will not accept field work without a written trail.

### 28.8 After placement

Contacts made are professional; requests to them go through proper channels, not personal favours for restricted data.

Section twenty-eight point eight develops field practice with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-eight point eight, MCX expects field claims to carry owners and dates.

Section twenty-eight point eight treats placement confidentiality tasks journal as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point eight, Corvale Municipal Services will not accept field work without a written trail.

### Learning from the desk

Lena observes how the desk handles a surge: twenty submissions on one fraud wave in an hour. The coordinator merges them into one item, credits each member and publishes once. Watching triage under pressure teaches more than any slide; Lena notes the merge procedure and later proposes a similar approach for CMS's own service-desk reports during campaigns.

### Worked example

Lena notices a member submission labelled TLP:CLEAR containing a staff email address. She flags it to her mentor rather than editing it herself. The mentor contacts the member, who confirms the address should be removed; the corrected version is released.

> **Synthetic case.** The submission is invented.

### Errors and limits

Placements show one organisation's habits; compare them with standards.

### Exercises

- **EX082 — Journal content.** What should the placement journal contain and avoid? *Rubric:* 3 = lessons/actions/questions; no restricted details; 2 = one; 1 = data copies; 0 = none.
- **EX083 — CLEAR with email.** Why did Lena flag rather than edit the submission? *Rubric:* 3 = not her authority; member/mentor decide; 2 = partial; 1 = should edit; 0 = none.
- **EX084 — Summary feedback.** What feedback changed Lena's summaries? *Rubric:* 3 = put action first; 2 = partial; 1 = none; 0 = none.

### Synthesis

Work within supervision and confidentiality, journal lessons not data, welcome feedback and act professionally.

### Continue studying — chapter 28 of 30

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Capstone build

### Learning outcomes

You will (1) build a capstone CTI pipeline end to end on synthetic data; (2) integrate earlier labs into one tested system; (3) keep a build log; (4) meet a fixed scope by a deadline.

### 29.1 The capstone

Lena's capstone: an "MCX-to-CMS pipeline" that imports a synthetic STIX bundle, refangs and validates values, deduplicates with provenance, stores them with TLP labels, matches a synthetic DNS log, flags expiries and produces the weekly note and a TLP-filtered export for MCX feedback.

Section twenty-nine point one develops capstone build with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-nine point one, MCX expects capstone claims to carry owners and dates.

Section twenty-nine point one treats the capstone integration tests as testable only when evidence and ticket IDs are recorded.

### 29.2 Integration

Each earlier lab becomes a module with clear inputs and outputs. A single runner calls them in order and stops with a clear message if any stage fails.

Section twenty-nine point two develops capstone build with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-nine point two, MCX expects capstone claims to carry owners and dates.

Section twenty-nine point two treats the capstone integration tests as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point two, Corvale Municipal Services will not accept capstone work without a written trail.

### 29.3 Tests

Each module keeps its lab test cases; an end-to-end test checks the whole run against expected outputs: three unique indicators, two hosts with hits, two expiry flags, one dangling relationship reported.

Section twenty-nine point three develops capstone build with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-nine point three, MCX expects capstone claims to carry owners and dates.

Section twenty-nine point three treats the capstone integration tests as testable only when evidence and ticket IDs are recorded.

### 29.4 Build log

Daily entries: what was built, decisions and reasons, problems. The log becomes an appendix.

Section twenty-nine point four develops capstone build with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-nine point four, MCX expects capstone claims to carry owners and dates.

Section twenty-nine point four treats the capstone integration tests as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point four, Corvale Municipal Services will not accept capstone work without a written trail.

### 29.5 Scope discipline

Features beyond the brief — a web dashboard, a chat bot — go to a "later" list. The deadline holds.

Section twenty-nine point five develops capstone build with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-nine point five, MCX expects capstone claims to carry owners and dates.

Section twenty-nine point five treats the capstone integration tests as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point five, Corvale Municipal Services will not accept capstone work without a written trail.

### 29.6 Safety rules

No network calls, no real data, standard library only. The export filter refuses anything not CLEAR or GREEN and any unknown label.

Section twenty-nine point six develops capstone build with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-nine point six, MCX expects capstone claims to carry owners and dates.

Section twenty-nine point six treats the capstone integration tests as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point six, Corvale Municipal Services will not accept capstone work without a written trail.

### 29.7 Code review

The tutor and one peer review the code before submission, focusing on clarity, error handling and the export filter.

Section twenty-nine point seven develops capstone build with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-nine point seven, MCX expects capstone claims to carry owners and dates.

Section twenty-nine point seven treats the capstone integration tests as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point seven, Corvale Municipal Services will not accept capstone work without a written trail.

### 29.8 Packaging

A README explains how to run the pipeline and tests in one command each, so assessors can reproduce results.

Section twenty-nine point eight develops capstone build with a Corvale Municipal Services note Lena Park can demo offline.

Under section twenty-nine point eight, MCX expects capstone claims to carry owners and dates.

Section twenty-nine point eight treats the capstone integration tests as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point eight, Corvale Municipal Services will not accept capstone work without a written trail.

### Error messages

When a stage fails, the message names the stage, the input file and the offending line, so the operator can act without reading code.

### Worked example

The end-to-end test fails: two hosts expected, three reported. Lena traces it to the matcher reading a new log column. She fixes the parser, reruns, and records the cause in the build log.

> **Synthetic case.** The pipeline and data are invented teaching material.

### Errors and limits

A capstone proves design on synthetic inputs; production needs validation on real data.

### Exercises

- **EX085 — Module chain.** List the pipeline stages in order. *Rubric:* 3 = import, refang/validate, dedupe, store, match, expiry, report/export; 2 = most; 1 = few; 0 = none.
- **EX086 — Export filter.** What does the export filter refuse? *Rubric:* 3 = anything not CLEAR/GREEN and unknown labels; 2 = one; 1 = nothing; 0 = none.
- **EX087 — Failing test.** What caused the end-to-end test failure and how was it recorded? *Rubric:* 3 = new log column misread; parser fixed; logged; 2 = partial; 1 = ignored; 0 = none.

### Synthesis

Integrate tested modules, log decisions, hold scope, keep safety rules and make results reproducible.

### Continue studying — chapter 29 of 30

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Capstone assessment

### Learning outcomes

You will (1) evaluate the capstone against its brief; (2) present results to assessors and a client panel; (3) reflect on limits and next steps; (4) document a transition plan to real use.

### 30.1 Against the brief

Each requirement is checked: imports work, labels are preserved, matching is exact, expiries are flagged, export filter refuses restricted items, tests pass in one command.

Section thirty point one develops capstone assessment with a Corvale Municipal Services note Lena Park can demo offline.

Under section thirty point one, MCX expects capstone claims to carry owners and dates.

Section thirty point one treats against the brief evidence as testable only when evidence and ticket IDs are recorded.

For section thirty point one, Corvale Municipal Services will not accept capstone work without a written trail.

### 30.2 Evidence

Assessors see test outputs, the build log, code review comments and a short demonstration on synthetic data.

Section thirty point two develops capstone assessment with a Corvale Municipal Services note Lena Park can demo offline.

Under section thirty point two, MCX expects capstone claims to carry owners and dates.

Section thirty point two treats against the brief evidence as testable only when evidence and ticket IDs are recorded.

For section thirty point two, Corvale Municipal Services will not accept capstone work without a written trail.

### 30.3 Presentation

Ten minutes: purpose, design diagram, demonstration, results, limits, next steps. A panel member from MCX asks about handling; Lena explains the fail-closed export.

Section thirty point three develops capstone assessment with a Corvale Municipal Services note Lena Park can demo offline.

Under section thirty point three, MCX expects capstone claims to carry owners and dates.

Section thirty point three treats against the brief evidence as testable only when evidence and ticket IDs are recorded.

For section thirty point three, Corvale Municipal Services will not accept capstone work without a written trail.

### 30.4 Reflection

What went well (modular design, tests); what was hard (format changes); what she would do differently (write the end-to-end test first).

Section thirty point four develops capstone assessment with a Corvale Municipal Services note Lena Park can demo offline.

Under section thirty point four, MCX expects capstone claims to carry owners and dates.

Section thirty point four treats against the brief evidence as testable only when evidence and ticket IDs are recorded.

For section thirty point four, Corvale Municipal Services will not accept capstone work without a written trail.

### 30.5 Limits

Synthetic data is cleaner than reality; the pipeline has not met real feeds; performance at scale is untested.

Section thirty point five develops capstone assessment with a Corvale Municipal Services note Lena Park can demo offline.

Under section thirty point five, MCX expects capstone claims to carry owners and dates.

Section thirty point five treats against the brief evidence as testable only when evidence and ticket IDs are recorded.

For section thirty point five, Corvale Municipal Services will not accept capstone work without a written trail.

### 30.6 Transition plan

To use it at CMS: validation on real past data, report-only run, change approval, service account, monitoring, owner and documentation — as in chapter 27.

Section thirty point six develops capstone assessment with a Corvale Municipal Services note Lena Park can demo offline.

Under section thirty point six, MCX expects capstone claims to carry owners and dates.

Section thirty point six treats against the brief evidence as testable only when evidence and ticket IDs are recorded.

For section thirty point six, Corvale Municipal Services will not accept capstone work without a written trail.

### 30.7 Assessment criteria

Correctness, safety, code quality, documentation, reflection and presentation, each scored with the published rubric.

Section thirty point seven develops capstone assessment with a Corvale Municipal Services note Lena Park can demo offline.

Under section thirty point seven, MCX expects capstone claims to carry owners and dates.

Section thirty point seven treats against the brief evidence as testable only when evidence and ticket IDs are recorded.

For section thirty point seven, Corvale Municipal Services will not accept capstone work without a written trail.

### 30.8 Continuing

Graduates move toward analyst roles; the next courses build analysis and leadership skills on these foundations.

Section thirty point eight develops capstone assessment with a Corvale Municipal Services note Lena Park can demo offline.

Under section thirty point eight, MCX expects capstone claims to carry owners and dates.

Section thirty point eight treats against the brief evidence as testable only when evidence and ticket IDs are recorded.

For section thirty point eight, Corvale Municipal Services will not accept capstone work without a written trail.

### Feedback from the client panel

The panel asks for two changes before any real use: weekly notes in the council's house style, and an extra column showing which resident-facing service each match affects. Lena records both as transition requirements rather than rushing them into the assessed version, keeping the submitted work stable while the client's needs are captured for the next phase.

### Worked example

A panel member asks whether the pipeline could share AMBER items with partner councils automatically. Lena answers no: AMBER restricts sharing to CMS and its clients, and outward sharing needs human approval. The panel notes the answer as evidence of handling discipline.

> **Synthetic case.** The panel is invented.

### Errors and limits

Assessment captures one moment; skills grow with practice.

### Exercises

- **EX088 — Brief check.** List four brief requirements assessed. *Rubric:* 3 = four of imports, labels, exact matching, expiry, export filter, one-command tests; 2 = three; 1 = one; 0 = none.
- **EX089 — AMBER to partners.** How did Lena answer the AMBER-sharing question? *Rubric:* 3 = no; AMBER limited; human approval for outward sharing; 2 = no; 1 = yes; 0 = none.
- **EX090 — Transition steps.** List five steps to move the capstone into real use. *Rubric:* 3 = five of validation, report-only, change approval, service account, monitoring, owner, docs; 2 = three; 1 = one; 0 = none.

### Synthesis

Assess against the brief with evidence, present clearly, reflect honestly and plan a careful transition.

### Continue studying — chapter 30 of 30

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX090. Corvale Municipal Services, Lena Park, the Municipal Cyber Exchange and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Exploit Public-Facing Application (T1190), because the portal is internet-reachable software that attackers can target directly.

**EX002.** Library machines have no staff mailboxes or accounts, are wiped daily and sit on their own network, so executive phishing does not reach them.

**EX003.** Because the product was internal only, she routed it for patching in the normal cycle, with escalation only if exploitation were reported.

**EX004.** The time of the query, the client machine that asked, and the domain name it asked for.

**EX005.** A passive lookup queries a third-party dataset under approved terms and never touches the suspect server; visiting the site contacts adversary infrastructure.

**EX006.** Those ranges are reserved for documentation, so copied examples cannot accidentally point at or accuse a real network.

**EX007.** Its last octet is 300, above the 255 maximum, so the standard library's ipaddress module rejects it.

**EX008.** It stops readers or mail clients from turning indicators into live links that someone might click by accident.

**EX009.** Mark them invalid, keep them out of matching, and ask the sender for the correct values.

**EX010.** One indicator, one attack-pattern and two relationship objects.

**EX011.** The malware object was TLP:AMBER and filtered from the GREEN export, but the relationship pointing to it was not removed.

**EX012.** Storing every time in UTC keeps comparisons correct across sources in different zones; local times are only for display.

**EX013.** Lookalike payment-portal fraud, ransomware disrupting services, and credential phishing against staff.

**EX014.** She asked MCX to release a TLP:CLEAR version, which could then be used in the public warning.

**EX015.** "Act now", "act this week" and "note only" — so owners can schedule work by urgency instead of treating every item as an emergency.

**EX016.** Scheduled Task/Job (T1053), which covers adversaries using task schedulers to run code.

**EX017.** Without internet access the VM cannot accidentally reach adversary servers or leak data while analysts work.

**EX018.** Two servers had no endpoint agent, so the search could not see scheduled tasks on them.

**EX019.** An attacker phishes or buys a password and logs in as the user (Valid Accounts, T1078), so no malicious code is needed.

**EX020.** Trying the passwords would be unauthorised account access and breach policy and law; the identity team forces resets instead.

**EX021.** They reset the password, revoked active sessions and reviewed the account's recent activity.

**EX022.** In endpoint protection and the mail gateway's attachment scanning, which inspect files.

**EX023.** The address serves thousands of sites; blocking it would cut off legitimate services, while the domain block targets only the fraud page.

**EX024.** The intelligence source, the reason, the date applied and the date for review.

**EX025.** One; each newsletter repeated the same MCX post, so they are not independent.

**EX026.** Observation: the proxy logged ws-114 contacting the fraud site. Conclusion: the user may have entered a password — not yet confirmed.

**EX027.** "Searched staff DNS resolver logs for the three domains from 1 to 30 September; no lookups found; library resolvers and mobile devices not covered."

**EX028.** Deciding blocks on critical systems such as the payments portal, and publishing attribution of attacks.

**EX029.** CMS needs fraud domains, not residents' identities; the complaint form already provides those details with consent, so searching profiles would collect personal data needlessly.

**EX030.** Certificate-transparency logs, public vulnerability advisories and official government alerts (also approved passive DNS).

**EX031.** Data Encrypted for Impact (T1486), because file servers hold shared data whose encryption would halt many services.

**EX032.** Fraud campaigns cluster around payment deadlines, so monitoring and warnings should increase beforehand.

**EX033.** The payments portal relies on the provider; a compromise there could expose residents' payments even though CMS does not run the system.

**EX034.** Six raw rows, three unique values; pay-portal.example came from MCX, the public source and the vendor.

**EX035.** Provenance showed the vendor was its only source, so withdrawing it removed the sole support.

**EX036.** She sent the two long domains to the proxy, which accepts them, and recorded the filter's limit on the flow diagram.

**EX037.** Actor type, goal, entry route, key techniques, affected service and impact.

**EX038.** Phishing (T1566), Valid Accounts (T1078), Remote Services (T1021) and Data Encrypted for Impact (T1486).

**EX039.** Funding faster takedown support for payment fraud and an offline backup restore test for ransomware.

**EX040.** Is it relevant, is it timely, is it actionable, and is the source known?

**EX041.** No. The text describes emails with links (T1566) and says nothing about scripts or interpreters.

**EX042.** Example: "Public advisory reports exploitation of a permits-software flaw at two cities. Relevant: CMS runs the same version on its portal; high confidence. Action: portal owner to apply the vendor fix by Friday."

**EX043.** ws-114: one lookup of pay-portal.example, first at 2026-09-04T08:03Z. ws-207: two lookups of update-svc.example, first at 2026-09-04T09:12Z.

**EX044.** It is a different domain that merely contains the indicator text; exact matching prevents that false alarm.

**EX045.** That the machine connected successfully or that a user typed anything; proxy logs and contacting the user are needed.

**EX046.** When the address belongs to a shared service hosting many unrelated sites, because further links would be meaningless.

**EX047.** Both names appeared on the same certificate, issued in the same minute — two pieces of linking evidence.

**EX048.** No. Redaction protects privacy, and defensive action needs only the domains and timing.

**EX049.** It forwards highlighted values, including TLP:AMBER partner data, to external websites, breaking sharing rules.

**EX050.** In the platform's secret store; never inside scripts or tickets.

**EX051.** Purpose, inputs, outputs and an example run.

**EX052.** Intelligence summary with source and TLP, affected asset, proposed change, expected effect, side effects and verification method (also rollback and review date).

**EX053.** Send a harmless test message that matches the rule and confirm it is quarantined.

**EX054.** Owners face many requests; bundling routine blocks reduces disruption and keeps the urgent route meaningful.

**EX055.** The address (42 days, limit 30) and update-svc.example (113 days, limit 90).

**EX056.** Addresses change hands quickly, particularly in cloud hosting, so an old address block can hit an innocent new user.

**EX057.** The library resolver had sent no logs for three days; a full disk was fixed, matching was rerun and the gap recorded.

**EX058.** A configuration fault; she added an alert on authentication failures and a reminder 30 days before key expiry.

**EX059.** From the source forward: arrival, parsing, storage, export, then loading in the tool — one hand-off at a time.

**EX060.** Otherwise they assume new threats are being blocked when they are not, and cannot compensate during the gap.

**EX061.** It forwards suspicious samples reported by residents and staff to the CTI queue, giving new evidence back to Lena.

**EX062.** The network team (block request), communications (public warning) and MCX (shared GREEN item).

**EX063.** To the owner of the affected system, identified through the asset list.

**EX064.** Indicators from MCX labelled TLP:GREEN or CLEAR with a source grade of B or better.

**EX065.** Visiting, downloading from or scanning adversary infrastructure, and sharing AMBER or RED data outward.

**EX066.** Running both side by side shows whether the script matches or beats manual work before people depend on it.

**EX067.** 12 actionable out of 120 received, which is 10%.

**EX068.** Keep only its domain indicators, because that type had the lowest false-positive rate among its feeds.

**EX069.** It may cover a threat or service that other sources miss, so its value lies in filling that gap.

**EX070.** A call the service desk forwarded to the CTI queue for analysis, defined before data collection began.

**EX071.** A regional news story about scams during the same period may have helped people recognise them without escalation.

**EX072.** Use only needed fields, remove names, store results securely and obtain manager and data-protection officer approval.

**EX073.** So every member understands every component and the team does not depend on one person.

**EX074.** The team recorded it, estimated effort and agreed with the tutor to list it as future work.

**EX075.** A planted name using "0" for "o" exposed a missing rule; after adding it, all twelve planted lookalikes were found.

**EX076.** Open items with status and next step, scheduled jobs and their health, partner commitments and anything unusual observed.

**EX077.** As a restricted item pending, with the details held by the supervisor, who is a named recipient.

**EX078.** Individual accounts keep actions attributable and auditable; sharing passwords breaks policy and accountability.

**EX079.** No known matches missed, false positives no worse than manual work, runtime under ten minutes, and failure alerts reaching the team.

**EX080.** The script produces outputs for people to check but triggers no exports; it reveals errors before they affect defences.

**EX081.** Rights to change firewall or filter rules, so a fault in the script cannot alter defences directly.

**EX082.** Daily lessons, tasks done and questions to ask; never restricted details from members.

**EX083.** Changing a member's submission is for the member and mentor to decide; her role was to spot and report the problem.

**EX084.** Her mentor said actions were buried at the end, so she moved the recommended action to the first line.

**EX085.** Import the bundle, refang and validate, deduplicate with provenance, store with labels, match the DNS log, flag expiries, then produce the note and filtered export.

**EX086.** Any item not labelled TLP:CLEAR or TLP:GREEN, and any item with an unrecognised label.

**EX087.** The matcher misread a new log column; Lena fixed the parser, reran the test and recorded the cause in the build log.

**EX088.** Imports work, TLP labels are preserved, matching is exact, and the export filter refuses restricted or unknown labels.

**EX089.** No. TLP:AMBER limits sharing to CMS and its clients on a need-to-know basis, and any outward sharing requires human approval.

**EX090.** Validate on real past data, run report-only, obtain change approval, use a least-privilege service account and set up monitoring (also name an owner and document).

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
