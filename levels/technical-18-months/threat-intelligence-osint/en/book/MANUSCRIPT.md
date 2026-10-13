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

For intelligence work the list matters because each service attracts different attacks and keeps different records. The learning platform serves 6,000 users and is a frequent target of plugin advisories, while the finance system handles payments and attracts invoice fraud. Tomás notes for every service whether it runs on campus servers or with a cloud supplier, since that decides who can search its logs.

### 1.2 Exposure

The learning platform, email, website and remote-access gateway are reachable from the internet. Exploit Public-Facing Application (T1190) and Phishing (T1566) are therefore the first ATT&CK techniques Tomás reads about. The finance system is internal only, but reachable from staff desktops.

Internet exposure decides which advisories need action within hours and which can wait for routine review. An advisory about a learning-platform plugin matters at once, because anyone on the internet can reach the platform. An advisory about the finance system matters less urgently, but staff desktops that read email can still be used as a path to it.

### 1.3 Logs and owners

Each service has an owner and logs: the email gateway logs messages; the remote-access gateway logs connections; the learning platform logs logins. Tomás builds a table with service, owner, log location, retention and who can search it.

Without this table, a matched indicator sits in a ticket while Tomás asks around for the person who can search the right log. The retention column also tells him in advance whether an old indicator can still be checked at all. The table is reviewed with each owner once a term, alongside the service diagram.

### 1.4 Dependencies

The learning platform depends on the directory for logins. If attackers steal directory credentials, they reach every service that trusts it.

Tomás records this dependency in the service table, so an advisory about stolen directory credentials goes to every owner whose service trusts the directory, not only to the identity team. The learning platform, email and remote-access gateway all sit behind the same logins. A single reused student password can therefore open more than one service, which is why credential notices are handled urgently.

### 1.5 Supplier-hosted services

Cloud email logs sit with the supplier. Ashgrove's contract allows downloading sign-in logs for 30 days; older ones are gone. Tomás notes that limit, because intelligence about last quarter's attacks cannot be checked there.

The thirty-day limit is a contract term, not a technical choice that Ashgrove can change on the day. When an ESX report describes attacks from two months ago, Tomás writes that cloud email sign-ins could not be checked and gives the reason. He also records the limit in the service table so the gap is visible during contract renewal.

### 1.6 Students as users

Students use personal devices on campus Wi-Fi. The college cannot install agents on them, so intelligence about malware on student laptops leads to network controls and advice, not endpoint rules.

Because the college cannot see inside student laptops, the campus resolvers and Wi-Fi translation logs are its main view of them. An indicator matched from a student device ends with a network block and advice from the help desk, as in the Wi-Fi case. Tomás never asks a student to hand over a personal laptop for checking.

### 1.7 A service diagram

A one-page diagram showing services, users, internet exposure and log locations helps everyone place an advisory quickly.

Tomás keeps the diagram to one page so it can be printed and checked in a meeting with service owners. Each box shows the service, its owner, whether it faces the internet and where its logs are kept. When the ESX plugin advisory arrived, the diagram and the service table together let him reach the e-learning owner within the hour. A printed copy hangs beside the team's desk, so visitors from other teams can find their service on it quickly.

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

For CTI, the resolver log is often the first place a domain from ESX can be matched against college activity. Each line ties a client address to a name at a given time, which is enough to show that a device asked for a suspicious domain. It does not show whether a connection followed, so Tomás states that limit in his notes.

### 2.2 HTTPS and the proxy

Staff web traffic goes through a proxy that records destination name, bytes and category. With encryption, the proxy sees the server name but not page content, unless inspection is enabled — which Ashgrove has not done for privacy and legal reasons.

Without inspection, Tomás can match domains and byte counts from intelligence but cannot see which page was fetched or what was downloaded. The category field helps him spot a rare or newly seen destination among ordinary staff browsing. Students are not covered, because only staff web traffic goes through the proxy, so their activity is checked through DNS instead.

### 2.3 SMTP

Mail servers exchange messages over SMTP. The gateway records sender, recipient, subject, attachment names and authentication results.

These gateway fields let Tomás match sender domains and attachment names from ESX advisories against messages that actually reached Ashgrove. The authentication results show whether a message claiming to come from the college passed SPF, DKIM and DMARC. Message bodies are not part of his searches, which keeps staff and student correspondence out of intelligence work. Attachment names from the gateway are often the quickest way to match an ESX advisory about a malicious document campaign.

### 2.4 Firewall logs

Firewall entries show source, destination, port, action and time. They are useful for checking addresses from intelligence feeds.

A firewall match shows only that a college address talked to an address from a feed, not what was sent. Tomás checks whether the feed address belongs to shared hosting before treating the match as meaningful. When the source is a public Wi-Fi address, he must also use the translation log, because the firewall alone cannot name the device. Tomás also notes the action field, since a blocked connection and an allowed one lead to very different follow-up work.

### 2.5 Address translation

Campus Wi-Fi translates many student devices to a few public addresses. Externally, one address represents thousands of people; internally, the translation log maps back to a device for a given time.

Address translation matters in both directions of sharing with ESX. When Tomás reports an Ashgrove address to ESX, he explains that it is shared Wi-Fi, so other members do not block thousands of students. When he investigates a match, the translation log must be read for the exact time, since the same public address belongs to another device minutes later.

### 2.6 Protocol abuse

Application Layer Protocol (T1071) describes attackers hiding command traffic in web, DNS or mail protocols so it blends in. Unusual regular connections to a rare domain are a clue worth checking.

At Ashgrove, the DNS and proxy logs are where such regular connections would appear, as repeated lookups or requests at similar intervals. Tomás treats regularity as a reason to look closer, not as proof, because update services also check in on a schedule. He asks the owning team whether the destination is expected before raising an incident ticket.

### 2.7 Time zones

Logs from cloud suppliers use UTC; campus devices use local time. Convert before correlating.

In the Wi-Fi case, the firewall times had to be converted to UTC before they could be compared with the translation log. A one-hour error during summer time would have pointed to a different laptop, and the wrong student would have been blocked. Tomás writes the zone beside every time in his notes, so reviewers can repeat the conversion. Campus devices change to and from local summer time, so the offset to UTC changes twice a year and must be checked for each date.

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

For CTI, this means credential leaks and spraying reports are among the most relevant items ESX shares with the college. A student password stolen from another website can unlock the learning platform and email through the directory. Contractor and service accounts deserve the same attention, because they are reviewed less often and their owners may have left.

### 3.2 Sign-in records

The directory logs user, time, source address, application and result. Tomás searches for successful sign-ins from addresses shared by ESX as attack sources.

A failed attempt from an ESX attack address confirms that Ashgrove was targeted, but a successful sign-in is what needs action. Tomás searches by the shared addresses and the time window in the advisory, not by browsing individual users. In the spraying case this search found 300 failed and two successful sign-ins, which he handed to the identity team.

### 3.3 Privileged accounts

IT administrators hold accounts that can change any system. Intelligence about attackers targeting administrators justifies separate admin accounts, stronger authentication and no email on admin accounts.

Intelligence about attackers seeking administrator access gives the IT team concrete reasons to keep these controls in place when they are inconvenient. An administrator who reads email on the same account can be phished into handing over control of every system. Tomás passes such advisories to the IT manager with the specific controls they support at Ashgrove.

### 3.4 Processes

On staff machines, endpoint agents log process starts. Reports about attackers running scripts (T1059) are checked against these logs by the endpoint team.

Tomás cannot search endpoint logs himself; he sends the endpoint team the script names, paths or hashes from the report. Their search covers only college-managed staff machines, so a negative result says nothing about student devices. He records that coverage beside the answer, as he does for every source, so the negative result is not read too widely.

### 3.5 Credential notices

When ESX reports Ashgrove addresses in a password dump, Tomás never tries the passwords. He sends the list to the identity team in a restricted ticket; they reset and notify users.

Trying a leaked password, even to check whether it still works, would be unauthorised access to the user's account. The restricted ticket limits who can read the list, and Tomás does not paste the passwords into ordinary email. Only the identity team can reset accounts and contact the students and staff affected, so his role ends at a clear handover.

### 3.6 Student privacy

Sign-in data about students is personal data. Searches are tied to a specific intelligence item and recorded; no browsing of individual students' activity.

Each search is logged against the ESX item or ticket that justified it, so a reviewer can see why a student's sign-ins were looked at. Tomás searches by indicator, such as an attack address, rather than by student name. Results are shared only with the team that must act on them, and extracts leave out unrelated fields.

### 3.7 Lockout and spraying

Password spraying tries a few common passwords across many accounts. Lockout settings and multi-factor authentication blunt it; intelligence about spraying against colleges supports tighter settings.

Spraying shows up in sign-in logs as one source trying many different accounts with only a few attempts each. The spraying case at Ashgrove matched this pattern: 300 failures from four ESX addresses and two successful logins. Because both successful accounts belonged to students, the case supported moving multi-factor authentication for students earlier in the college plan.

### Contractor accounts

Contractors maintaining campus systems often keep accounts long after their work ends. A quarterly review with each contract manager disables accounts no longer needed and shortens the list of credentials attackers could use.

### Worked example

ESX shares four addresses used in spraying against colleges. Tomás finds 300 failed and two successful sign-ins at Ashgrove, both student accounts. The identity team resets both, revokes sessions and checks what was accessed: course materials only. Multi-factor authentication for students is moved up the plan.

> **Synthetic case.** The addresses and accounts are invented.

### Errors and limits

Address-based searches miss attackers using residential proxies.

### Exercises

- **EX009 — Why education.** Why is T1078 common in education? *Rubric:* 3 = student password reuse/many accounts; 2 = partial; 1 = no reason; 0 = none.
- **EX010 — Admin separation.** Give two controls for administrator accounts supported by intelligence. *Rubric:* 3 = separate admin accounts, strong MFA, no email; 2 = one; 1 = vague; 0 = none.
- **EX011 — Search discipline.** How is student privacy protected during sign-in searches? *Rubric:* 3 = tied to intelligence item, recorded, no browsing; 2 = partial; 1 = vague; 0 = none.
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

Tomás reads each format with the matching module and prints a few records before trusting any value in a script. CSV lists from vendors may rename columns without warning, so he reads them by header name. STIX bundles are JSON, so the same json module handles both ESX bundles and ordinary JSON exports from college tools.

### 4.2 Authentication results

Mail gateways add an Authentication-Results header with SPF, DKIM and DMARC outcomes. DMARC passes only when the visible From domain aligns with an SPF or DKIM pass. A message failing DMARC that claims to come from the college deserves attention.

SPF checks the sending server and DKIM checks a signature, but DMARC also requires the domain to match the visible From address. That alignment rule is why a lookalike domain can pass SPF for itself and still fail DMARC. Tomás reads these results from Ashgrove's own gateway header, which the lab simulates with four synthetic messages.

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

M2 shows why one passing check is not enough: SPF passed only because the lookalike domain's owner published records for it. M3 is the more direct impersonation of the college, failing all three checks while claiming ashgrove.example as its domain. Both are flagged in the output, and the script prints the parsed results so the reasons for each verdict are visible.

### 4.4 Passing is not trust

M4 passes because partner-uni.example's records are correct; it shows the sender controls that domain, not that the message is safe. A compromised partner mailbox would also pass.

A passing result therefore tells Tomás where the message came from, not whether its contents are honest. If ESX warns that a partner university's mailboxes have been taken over, messages like M4 need the same suspicion as a failing one. He would then look at sender behaviour and content reports from staff, not at authentication results alone.

### 4.5 Clear output

Each line shows message, domain, parsed results and verdict. Anyone can check it without reading code.

In the lab output, each line carries the message identifier, the sender domain, the three parsed results and the verdict. The email team can read those lines and agree or disagree with each verdict without opening the script. Tomás pastes the output into tickets unchanged, so the reasoning behind each flag travels with it to whoever acts. If a verdict looks wrong, the email team can point to the exact line and parsed result in their reply.

### 4.6 Bad input

Malformed headers should produce "unparsed" with the raw text, not a crash.

A header that cannot be split into key=value pairs would raise an error in the lab's dict call and stop the whole run. Tomás's version catches that case, prints 'unparsed' with the raw text and carries on with the remaining messages. A person then reads the raw header, so an odd or forged result is examined rather than lost. The count of unparsed headers is printed at the end of each run, even when it is zero, so readers know the check happened.

### 4.7 STIX basics

A STIX indicator object holds a pattern, a valid_from time and an id. Tomás reads bundles with `json.load` and prints each object's type and id before using any value.

Printing the type and id first shows Tomás what the bundle contains before any pattern reaches a block list. A bundle may mix indicators with reports and relationships, and only indicator patterns are candidates for controls. The valid_from time tells him how old the indicator is, which matters for the expiry rules applied later.

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

The line between these lists is drawn by who carries the risk of each action. Matching and drafting change nothing on college systems, while blocking and contact can disrupt services or alert attackers. When an action falls outside the list, Tomás writes a request to the owning team and waits for their decision.

### 5.2 TLP 2.0

CLEAR — public. GREEN — community, not public. AMBER — Ashgrove and its clients on a need-to-know basis. AMBER+STRICT — Ashgrove only. RED — named people only. Unlabelled material is treated as AMBER until the sender confirms.

Tomás reads the label before forwarding anything, because the label limits who may receive it. In the vendor case, an unlabelled report was treated as AMBER until the vendor confirmed AMBER+STRICT, which kept it inside Ashgrove. ESX items marked GREEN may go to other member colleges, but never to a public page or social media.

### 5.3 Evidence and provenance

Every item records source, date received, TLP, what the source based it on, and Tomás's checks. Exported log extracts used as evidence are saved with the ticket.

When Tomás later explains a block or a match, the provenance record shows exactly which report it came from and what was checked. A note that says only 'from ESX' cannot be tested by anyone else. Log extracts saved with the ticket let a reviewer repeat his match without searching the live logs again.

### 5.4 Personal data

Logs include student and staff identities. Extracts contain only what the question needs; names are removed before sharing with ESX.

When Tomás shares a finding with ESX, such as the lookalike invoice domain, he includes the sender domain and dates but not the name of the staff member who received it. Inside Ashgrove, extracts keep usernames only when the receiving team must act on a specific account. Every other field is left out of the extract at export time. Removing names before sharing does not weaken the indicator, because other colleges need the domain and dates, not the recipient.

### 5.5 Authorisation

The placement agreement and IT security policy define what Tomás may do. When unsure, he asks his supervisor and records the answer.

The placement agreement names his supervisor as the person who decides unclear cases. Recording each answer means the same question does not need asking twice, and it protects Tomás if his action is later questioned. Several of those recorded answers have since become rules on the team's one-page safety sheet. The supervisor's answers are kept in a shared note that later placement students can read before asking the same question.

### 5.6 Public sources

Government advisories and vendor blogs are useful, but their terms vary. Quoting short parts with attribution is usually fine; republishing whole reports is not.

Tomás records the terms of each public source he uses, alongside its grade in the platform. A government advisory may allow free reuse, while a vendor blog may forbid copying beyond short quotations. When unsure, he summarises the source in his own words, attributes it and links to the original instead of copying text. The source terms are noted in the platform record, so they travel with each item.

### 5.7 Mistakes

If he shares something wrongly, he reports it at once so the recipient can delete it. Hiding mistakes breaks trust far more.

A wrong share caught quickly can be contained: the recipient deletes the material and the error is logged. Tomás tells his supervisor first, then the recipient, and records the event in the failure log for review. The review asks why the error happened, which is how process problems such as missing labels come to light. Tomás's own early mistakes are in that log too, which shows newer students that reporting is expected.

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

Each source is listed with its owner, its format and how often it arrives. ESX's TAXII collection supplies STIX objects automatically, while its email alerts arrive in a mailbox someone must read. Help-desk reports and college logs are internal sources, and they often show whether an external item matters to Ashgrove at all. Tomás records each source's TLP habits too, since ESX labels every item while the national advisory page publishes only CLEAR material.

### 6.2 Processing

Tomás's scripts validate and normalise indicators; his supervisor reviews relevance and grades sources; requests go to system owners.

Splitting the work this way keeps judgment with the person accountable for it. Scripts catch malformed or duplicate indicators quickly, but they cannot decide whether a report on another college applies to Ashgrove. The supervisor's grade and relevance call are recorded in the platform, so later readers can see who decided what, and why. When the supervisor is away, routine relevance calls wait for her return, while urgent items go to the IT security manager instead.

### 6.3 Storage

A small threat intelligence platform stores STIX 2.1 objects: indicators, attack patterns, reports and relationships, each with a TLP marking definition.

Storing objects in STIX keeps relationships visible, such as which indicators belong to which report or attack pattern. The TLP marking travels with each object, so an export to ESX can be filtered by label automatically. Tomás checks that imported objects keep their markings, because a lost label could lead to a wrong share. Indicators also carry their valid_from time from the source, which the expiry rules later use to decide when an entry should leave the block lists.

### 6.4 Outputs

DNS filter and email gateway block lists, notes to owners, monthly summaries for management and feedback to ESX.

Each of these outputs has a different reader and a different timing. Block lists go to the network and email teams as configuration requests; notes go to individual owners; the monthly summary goes to management. Feedback to ESX closes the loop, telling the community which items matched, which were wrong and which were withdrawn. Each output is listed in the configuration register or the reporting calendar, so a missing one is noticed quickly. Feedback to ESX is sent at least monthly, even when nothing matched.

### 6.5 Owners

The network team owns the DNS filter; the email team the gateway; the supervisor the platform; Tomás the scripts.

Writing the owners on the diagram shows where Tomás must send a request rather than act himself. It also shows that Tomás owns only the scripts, so their documentation and testing are his responsibility. When an owner changes jobs, the diagram and the configuration register are both updated in the same week. The supervisor owns the platform, so platform upgrades and user accounts are her decisions, not Tomás's.

### 6.6 Weak points

Single-person knowledge of scripts; email alerts arriving in a personal inbox; no check that block lists actually loaded.

Each weak point on the list has a matching fix. Script knowledge is shared through runbooks and code review; the alert inbox became a shared mailbox with two readers; loaded lists are tested with a lookup after each change. The diagram is redrawn after each fix, so the next review starts from the current design. The loaded-list check is now part of every block request, through the test lookup required after each change.

### 6.7 Kill chain view

Mapping outputs to the Hutchins et al. phases shows coverage: email blocks act at delivery; DNS blocks at command and control; account resets after exploitation. No output addresses reconnaissance — a gap to discuss.

Laying the kill chain over the diagram is how Tomás found that no output addresses reconnaissance. Lookalike-domain searches in certificate transparency logs could move some coverage earlier, before phishing messages are sent. Whether that is worth the effort is a decision for the supervisor, so Tomás presents the gap rather than a solution.

### 6.8 Diagram

One page, boxes and arrows, names of owners on each box.

The diagram for Ashgrove shows five source boxes, the scripts, the platform and four kinds of output, with arrows between them. Owners' names sit inside each box, so readers can see who to call. Tomás keeps the editable file in the team repository, so each change is recorded with its date. Arrows show direction of flow, from sources through the scripts and the platform to each output and back to ESX as feedback. A dashed arrow marks the help-desk reports, which arrive by forwarded email rather than through any automated feed.

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

Tomás keeps the list as a table with the questions each source can answer. DNS shows which devices asked for a domain; the proxy shows staff web visits; email logs show delivery; sign-ins show account use. Endpoint events show what ran on staff machines, and learning-platform logs show logins and administrator changes. Tomás adds the retention period and the owning team to each row of the table.

### 7.2 Coverage

DNS covers all campus devices; endpoint events cover only college-managed machines; the proxy covers staff only. Tomás writes coverage beside each source so negative results are honest.

A clean DNS search means no campus device asked for the domain within the retention period, which is a strong statement. A clean proxy search says nothing about students, because they never pass through it. Writing coverage beside each result stops readers treating a narrow negative as proof that the whole college is safe.

### 7.3 Retention

DNS 90 days, proxy 30 days, cloud sign-ins 30 days, endpoint 60 days. An indicator from 45 days ago can still be checked in DNS but not in the proxy.

Tomás checks an indicator's age against these periods before searching, so he knows which logs can still answer. An ESX report about activity 40 days ago can be tested in DNS and endpoint logs, but not in the proxy or cloud sign-ins. He states which logs were too short, rather than reporting a plain negative.

### 7.4 Access

Tomás has read-only access to DNS and email logs. Others are searched on request by owning teams. Access requests are justified in writing.

Read-only access lets Tomás match indicators without any risk of changing records. For other sources, a written request names the indicator, the time range and the fields needed, and the owning team runs the search. Their answer goes into the ticket, so the evidence trail shows who searched what and when. Each written request also states how long the requested extract will be kept and who will read it.

### 7.5 Minimal extracts

When evidence is needed, export only matching lines with needed fields — time, host, indicator — not full logs with every user's browsing.

In the DNS case from the library, the extract held two lines with time, device and domain, which was enough to show the lookups. Full logs would have included every other lookup by library users that morning. Keeping extracts small reduces the personal data stored in tickets and makes the evidence easier to review. The ticket records which fields were exported, so nobody has to guess what was left out of the extract.

### 7.6 Clock accuracy

All servers synchronise time. A server with drifting time makes correlation unreliable; Tomás reports such drift.

Correlation depends on comparing times across sources, such as DNS lookups and firewall connections. A resolver that drifted by a few minutes could make a lookup appear after the connection it caused. Tomás reports drift to the owning team and notes it beside any affected result, so readers allow for it. Endpoint agents on staff machines take their time from the same servers, which keeps endpoint process events comparable with DNS and proxy records.

### 7.7 Quality checks

Daily volume per source shows gaps: a resolver that logged nothing overnight probably failed.

Tomás compares each day's line count with the usual range for that source and weekday. A sudden drop to zero is usually a logging fault, not a quiet night, and it means searches covering that period are incomplete. He reports the gap to the owner and records it, so later negative results are qualified. Weekend and holiday volumes are lower, so the usual ranges are kept separately for term-time weekdays, weekends and college holidays.

### 7.8 Telemetry for techniques

Technique intelligence needs behavioural data. Phishing needs email logs; valid-account abuse needs sign-ins; command channels need DNS and proxy. A matrix of techniques against sources shows blind spots.

The matrix lists techniques from ATT&CK down one side and Ashgrove's log sources across the top. A technique with no source marked is a blind spot, such as scripts running on student laptops. Tomás shares the matrix with his supervisor, who decides which blind spots to accept and which to close.

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
- **EX028 — Technique matrix.** What does a technique-by-source matrix reveal? *Rubric:* 3 = blind spots where no telemetry covers a technique; 2 = partial; 1 = vague; 0 = none.

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

Naming the stage tells the team where to look for the fix. A missed alert points to how sources are monitored, while a wrong recipient points to dissemination rules. At Ashgrove, the unread ESX alerts during the supervisor's illness were a collection failure, fixed by the shared mailbox with two readers. Recording the stage in the failure log makes patterns across a term visible, such as repeated dissemination errors.

### 8.2 False positives

Blocking a legitimate site because an indicator was stale or shared. Typical causes: old cloud addresses, popular file-sharing domains in feeds, typing errors.

The revision website is the Ashgrove example: a six-month-old address that had since been reassigned to a legitimate service. Students noticed the block before the team did, which shows how false positives reach users first. Expiry dates and the allow list are the two controls that reduce them, and both are checked before each export. Popular file-sharing domains in vendor feeds are a second common source, as the allow-list catch showed.

### 8.3 False negatives

Missing a real match because of normalisation differences (trailing dot, capital letters), missing logs or retention expiry.

A domain written with a trailing dot in a feed will not match the same domain in DNS logs unless both are normalised. Capital letters cause the same matching problem in some college tools. Tomás's validation script lowercases names and strips trailing dots before matching, and the failure log records any new normalisation fault. Missing logs and retention expiry produce false negatives that look exactly like real negatives, so the note must name both.

### 8.4 Label failures

Sharing AMBER material with ESX at large. Causes: missing label in source, copy-paste stripping labels, unclear rules.

A label failure can harm the college's standing in ESX, because members share AMBER material on trust. Copy-paste from one tool to another is the commonest cause, since labels often sit in metadata rather than text. The pre-share checklist asks Tomás to confirm the label on the source before anything leaves Ashgrove. Unclear rules are the third cause, which is why the safety sheet spells out what each TLP label allows. A review that finds a label failure checks the source item, the tool used and the rule the person followed.

### 8.5 Overload

Too many low-value alerts mean owners stop reading. Cause: no triage before dissemination.

When owners receive alerts that rarely apply to their systems, they begin to skip them, and a relevant one is then missed. Triage using the four questions removes items that are not relevant or not actionable before they reach owners. The weekly triage with his supervisor keeps that filter consistent between them. Grouping several minor items into the Monday list or the monthly summary also reduces the number of separate messages owners receive. Owners then read each urgent alert because they know it is rare.

### 8.6 Learning

Each failure gets a short blameless review: what happened, why, what changed. Patterns guide improvement.

A blameless review asks what in the process allowed the failure, not who is at fault. In the revision-site case, the review found that address entries kept too long, and the expiry was shortened to 30 days. People report their own mistakes faster when they know the review looks at the process. The review is written up in the failure log within a week, while the people involved still remember the details. Changes that come out of it are given an owner and a date.

### 8.7 Recording failures

A shared failure log with date, stage, cause and fix shows recurring issues. Three label failures in a term indicate a process problem, not three careless people.

The failure log at Ashgrove is a shared spreadsheet that the supervisor reviews each month. Recurring causes, such as stale addresses or stripped labels, become process changes rather than reminders. Each entry links to its ticket, so the original evidence can be reread if the pattern later needs a closer look. The term's count of each cause is reported to the supervisor at the end of term.

### 8.8 Bias

Assuming every issue is an attack leads to over-blocking; assuming none is leads to missing real ones. Check evidence each time.

Tomás guards against both errors by writing down what the evidence shows before deciding. In the revision-site case, checking the feed's age showed a stale address, not an attack. In the spraying case, two successful logins from ESX addresses were treated as real compromise and acted on at once. Writing the evidence down first also lets the supervisor check his reasoning when she reviews the case.

### Dissemination failures

An advisory sent to a general IT mailbox that nobody owns will wait for days. Each item type has a named recipient, and the sender asks for acknowledgement so silence is noticed. When no acknowledgement arrives within the agreed time, the item is escalated to the supervisor rather than left waiting.

### Worked example

Students complain that a revision website is blocked. Tomás finds the address came from a feed six months old; the site moved to that cloud address last month. He requests removal, the network team unblocks it within an hour, and the expiry rule for addresses is shortened to 30 days.

> **Synthetic case.** The site and feed are invented.

### Errors and limits

Fixing one failure can create another; test changes.

### Exercises

- **EX029 — Revision site.** Classify the revision-site block and its cause. *Rubric:* 3 = false positive; stale cloud address; 2 = one; 1 = attack; 0 = none.
- **EX030 — Missed match.** Give two causes of false negatives. *Rubric:* 3 = normalisation, missing logs, retention; 2 = one; 1 = vague; 0 = none.
- **EX031 — Pattern meaning.** What do three label failures in one term suggest? *Rubric:* 3 = process problem; fix process; 2 = partial; 1 = careless people; 0 = none.
- **EX032 — Fix applied.** What process change followed the revision-site case? *Rubric:* 3 = address expiry shortened to 30 days; 2 = partial; 1 = vague; 0 = none.

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

Keeping storage in the platform and checks in scripts lets Tomás test his code on synthetic data without touching the stored objects. The platform's TLP markings are what make filtered exports to ESX possible. Exports for the DNS filter and email gateway are validated by his scripts and the allow list before they become configuration requests.

### 9.2 Triage

Four questions: relevant to Ashgrove? timely? actionable? source known? Items failing the first are logged and closed.

Relevance comes first because an item about software Ashgrove does not run can be closed without further work. Timeliness matters next, since an indicator from last year may have been reassigned. An item that passes all four questions moves on to grading and a note, while failures are logged with a one-line reason. Source known is the last question because an anonymous claim may still be relevant and timely, but it needs more checking before any action. Tomás asks ESX about such items rather than discarding them.

### 9.3 Grading

The Admiralty scale: source reliability A–F, information credibility 1–6. ESX is usually B; an unverified social-media claim F6.

Reliability grades the source's record over time, while credibility grades this particular claim. Keeping the two apart means a reliable source can still send an item that is only possible, such as B3. Tomás records both letters and the reason in the platform, and the supervisor reviews new or unusual grades during their weekly triage. The worked example's B2 grade shows how the two letters combine: a usually reliable log source and a claim that is probably true. The supervisor checks new F-graded sources, since they are rarely worth action without corroboration.

### 9.4 Tagging

Tag only what the text supports: "students received fake grade notices with links" supports T1566.

If a report only says that a domain was registered, tagging it T1566 would claim that phishing happened when nobody has seen it. Over-tagging also distorts the weekly counts by technique, which management reads. Tomás quotes the sentence that supports each tag in the platform note, so a reviewer can check the link. Tags are reviewed in the weekly triage, alongside the grades and relevance decisions.

### 9.5 OSINT tools

Certificate-transparency search for lookalike college domains; approved passive DNS; public vulnerability databases. All used within their terms; nothing that contacts suspicious sites.

Certificate-transparency logs are public records of issued certificates, so searching them never contacts the lookalike site itself. Passive DNS shows past resolutions from data collected by others, again without touching the domain. Tomás records the tool, the query and the date with each finding, as provenance for the note. Approved tools are listed on the safety sheet, so students know which searches are allowed. New tools are added only after the supervisor checks their terms and confirms they stay passive.

### 9.6 Notes

Three lines: what, why it matters here with confidence, action and owner.

For the lookalike domain, the three lines were: a new lookalike registered yesterday; likely phishing preparation with moderate confidence; email team to block and supervisor to request takedown. Owners can act on a note of that length without reading the source. The full source stays linked in the platform for anyone who needs it. The three-line format is the same in tickets, emails to owners and platform notes, so readers learn where to find the action. Confidence is stated in words such as moderate or high, with the reason after it.

### 9.7 Tool limits

A platform shows what it was given. If ESX did not share an object, it is absent; absence in the platform is not absence in the world.

Tomás writes the scope of every platform search in his notes, such as 'no object in ESX's shared collection'. That wording keeps readers from treating an empty search as a statement about the world. Where the question matters, he also searches approved public sources or asks ESX directly whether other members have seen the item.

### 9.8 Practice

Tomás triages twenty items each week with his supervisor and compares decisions to build consistency.

Comparing decisions shows where their judgments differ, such as relevance of advisories about supplier software. Each difference is discussed and the agreed reason is written down, so the next similar item is handled the same way. Over the term, the comparison shows whether Tomás can triage alone on routine items. The twenty items are chosen by the supervisor to include easy, difficult and borderline cases. Disagreements found in the weekly practice are recorded with the agreed outcome, which later helps new students.

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
- **EX036 — Innocent lookalike.** What should be checked before requesting takedown? *Rubric:* 3 = whether legitimate (e.g. student society); 2 = partial; 1 = vague; 0 = none.

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

Validation catches entries that would fail to load or block too much, such as a domain with a space or a whole top-level domain. Each control needs its own format, so one platform export becomes three separate lists. Tomás checks the line count of each list against the platform export before attaching it to the request.

### 10.2 Choosing points

Domains to DNS; sender domains to email; hashes to email attachment scanning and endpoint; addresses only when not shared hosting. Techniques inform configuration too: intelligence on macro-laden attachments (User Execution, T1204) supports quarantining macro documents from outside.

Addresses on shared hosting can serve hundreds of unrelated sites, so blocking one would cut off legitimate services, as the revision-site case showed. Domains and hashes are more specific and sit better at DNS and email. The macro example shows how technique intelligence can support a broad rule rather than one indicator at a time.

### 10.3 Expiry

Every entry carries an expiry date: 30 days for addresses, 90 for domains, longer for hashes. Lists without expiry grow until they break things.

The periods follow how quickly each type of indicator changes hands: addresses are reassigned fastest, domains less often and file hashes never. When an entry expires, the platform flags it for review rather than renewing it automatically. Tomás renews only entries that ESX or another source has reported again since the original item. The expiry date is set from the indicator's valid_from time, not from the date it reached Ashgrove.

### 10.4 Requests

Tomás drafts; the owning team configures. The request includes list, source, TLP, reason, expiry and verification plan.

Including the verification plan means the owning team knows in advance how success will be tested. The TLP marking tells them whether the list can be shared with suppliers who manage the control. Tomás attaches the validated list to the request rather than pasting entries into the ticket text, so nothing is mistyped. The source and reason let the owning team check the request against the original intelligence if they wish. The owning team replies in the same ticket once the change is loaded.

### 10.5 Allow lists

Some domains must never be blocked: the learning platform, examination boards, the student loan service. An allow list checked before every export prevents accidents.

These services are ones students and staff cannot work without, and some sit on shared cloud platforms that also appear in feeds. Tomás's export script compares every entry against the allow list and removes matches before the request is drafted. The file-sharing domain caught in the worked example shows the check working on a real export.

### 10.6 Testing

After loading, a test lookup of one blocked domain from a test machine must fail; a test of an allowed domain must succeed.

The test lookup proves that the list loaded and that the control acts on it. Testing an allowed domain at the same time shows that the change did not break ordinary access. Tomás records both results with the time and the test machine used, and attaches them to the configuration request. If either test fails, the change is rolled back and the request reopened with the test result attached.

### 10.7 Change windows

Large list changes happen outside exam periods, when disruption would hurt most.

During exams, a wrong block could stop students reaching an examination board or the learning platform at the worst moment. Urgent single entries can still be added in those weeks after the owning team agrees. Tomás checks the college calendar before scheduling any large update and notes the chosen window in the request. Exam periods are taken from the college calendar each term, because they differ between courses and campuses. Tomás asks the network team to confirm the window in writing before he schedules anything.

### 10.8 Documentation

The configuration register lists every list, owner, last change and expiry policy.

When a block causes a complaint, the register shows at once which list holds the entry, who owns it and when it last changed. It also shows the expiry rules for each list, so reviewers can check that old entries are being removed. Tomás updates the register in the same ticket as each change. The register is kept in the team repository with the runbooks, so every edit is tracked and reversible. The network and email teams can read it at any time, including during out-of-hours calls.

### 10.9 Size limits

Some tools cap list size. When near the cap, remove expired entries first rather than raising the cap blindly.

Expired entries are the safest to remove because their sources no longer support them. Raising the cap without that cleanup only delays the problem and keeps stale indicators that can block legitimate services. Tomás reports the list size to the owning team each month, so the cap is never reached by surprise. The monthly size report shows the number of entries per list, how many expire within thirty days and the product's cap.

### Worked example

Tomás's export includes a file-sharing domain from a vendor feed. The allow-list check stops it: lecturers use that service to share materials. He removes it from the request and reports the feed's error to the vendor through his supervisor.

> **Synthetic case.** The domain and feed are invented.

### Errors and limits

Controls vary by product; read their documentation before formatting.

### Exercises

- **EX037 — Expiry periods.** State expiry periods for addresses and domains and why they differ. *Rubric:* 3 = 30 vs 90 days; addresses reassigned faster; 2 = numbers; 1 = same; 0 = none.
- **EX038 — Allow-list catch.** What did the allow-list check prevent? *Rubric:* 3 = blocking lecturer file-sharing service; 2 = partial; 1 = vague; 0 = none.
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

In the withdrawn-domain case, these checks showed a long legitimate history and hosting on a large content-delivery service. Form checks catch indicators that cannot be right, such as malformed domains or private addresses. Passive sources mean the checks never alert the owner of a suspicious domain that the college is looking at it. Each check and its result goes into the ticket before any block is requested.

### 11.2 Internal corroboration

Did college logs see it? Internal sightings both confirm relevance and show urgency.

An ESX indicator seen in Ashgrove's DNS logs is more urgent than one that only matched at another college. A match also shows which device or account needs attention. When no internal sighting is found, Tomás records which sources were searched and their retention, so the negative result is read correctly. In the DNS case, two library lookups of a 40-day-old domain showed that the item was relevant to Ashgrove. Tomás passed the library device names to the team that manages those machines, with the times of both lookups.

### 11.3 Independence

Two reports citing the same original are one source. Ask what each is based on.

A vendor blog and a news story that both cite the same ESX item add no extra weight to it. Tomás traces each report back to its original observation before counting sources. When the original cannot be found, he notes that the reports may not be independent, and the confidence stays lower in the note. This question also applies to sources inside ESX, where several members may repeat one original report. A count of reports is therefore never used as the confidence figure on its own.

### 11.4 Verify the control

After blocking, test from an approved machine. After an email rule, send a harmless test message. Record results.

The test machine is approved for this purpose, so its lookups are expected in the logs and not mistaken for an incident. A harmless test message checks an email rule without sending anything malicious through the gateway. Recording results gives the owning team evidence that the change worked, attached to the original request. If a test fails, the owning team is told the same day with the result, so the control can be fixed quickly.

### 11.5 Verify the outcome

A week later, check whether matches dropped. If blocked lookups continue from one machine, that machine may be infected and needs attention.

The outcome check asks whether the change made any difference to what college devices actually do. A drop in matches suggests the block is working, while continued blocked lookups from one device point to something still running there. That device is handed to the team that manages it, and Tomás records the referral. The one-week check is booked in the ticket when the block is made, so it is not forgotten.

### 11.6 Record

Checks, results, time and person. Others can repeat them.

A record names the check, its result, the time and who performed it, in the ticket for the item. Another member of the team should be able to repeat it from the record alone. Tomás uses the same format for intelligence checks, control tests and outcome checks, so reviewers know where to look. Records are kept with the item for as long as the item stays in the platform. When ESX later withdraws an item, the records show which checks were done before it was used, and which controls it reached.

### 11.7 Time limits

Urgent items get quick checks; strategic claims can wait for fuller verification. Report what was and was not verified.

An urgent phishing domain might be checked for form, age and internal sightings within minutes and blocked the same morning. A claim about a group targeting colleges can wait for fuller corroboration. In both cases, Tomás's note states which checks were done and which were not, so readers know how far to trust it. Quick checks still cover form, age and internal sightings at a minimum.

### 11.8 Disagreement

If verification contradicts the source, tell the source politely with evidence. Communities improve through such feedback.

In the withdrawn-domain case, Tomás gave ESX the hosting details, history and certificate owner rather than simply saying the item was wrong. ESX could then check its own records and found the typing error. Polite, evidence-based feedback keeps Ashgrove trusted in the community and improves the shared data for every member. Tomás sends feedback through ESX's agreed channel, with the item's identifier and label, so the right member receives it. A withdrawal by ESX is recorded in the platform, and any related block is removed.

### 11.9 Never active

Verification never includes visiting suspicious pages, downloading files from them or scanning their servers from college systems.

These actions could alert attackers, trigger downloads of malicious code or break the college's acceptable-use rules. Passive sources and college logs give enough information for the decisions Tomás supports. If a page really must be examined, the request goes to qualified staff with suitable tools, as the safety sheet says. The rule applies to every college device, including the approved test machine used for control checks. Tomás repeats it in the lab rules, so students practise only passive methods.

### Verifying with owners

System owners know whether a connection is expected. Before escalating a match on the library server, Tomás asks the library systems officer whether the server legitimately talks to that supplier. A two-minute call often settles what hours of log reading cannot, and owners appreciate being asked rather than surprised by an incident ticket.

### Worked example

ESX shares a domain as a phishing site. Tomás finds it on a large content-delivery service, with a long legitimate history and no college lookups. Certificate records show a reputable owner. He tells ESX the domain appears legitimate; ESX checks and withdraws it — the original report had a typing error.

> **Synthetic case.** The domain is invented.

### Errors and limits

Verification reduces errors but cannot remove them.

### Exercises

- **EX041 — Withdrawn domain.** What evidence suggested the ESX domain was legitimate? *Rubric:* 3 = CDN, long history, no lookups, reputable certificate owner; 2 = two; 1 = one; 0 = none.
- **EX042 — Ongoing lookups.** What do continued blocked lookups from one machine suggest? *Rubric:* 3 = machine may be infected; investigate; 2 = partial; 1 = vague; 0 = none.
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

Running offline means the lab cannot contact any real host, even by mistake, and synthetic data means no college or student information is involved. The standard-library rule keeps the scripts readable and avoids installing unknown packages on the course virtual machine. The same rules apply to Contained laboratory II, later in the course. Lab files and outputs stay inside the course virtual machine throughout.

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

The script decides only the route; it does not decide whether a match is serious. That judgment stays with the receiving team, who know their systems. Printing the host, indicator and technique beside each route lets Tomás check every line before acting on it.

### 12.3 Why route by asset

A staff machine contacting a phishing domain may need a password reset and a conversation; a server talking to a command address may be compromised and needs incident response immediately.

The difference lies in what each machine does and who relies on it. A Finance staff machine affects one user, and the service desk can reset passwords and speak to them. The learning-platform server serves 6,000 users, so a possible compromise there needs incident response without delay. Routing by asset type therefore sends each match to the team best placed to act quickly.

### 12.4 Unknown assets

Unknown hosts are common: new machines, lab equipment, devices named differently. Each is a gap in the inventory to close.

In the lab, ws-lab-99 is such a gap, and guessing an owner could send a match to the wrong team. Asking the network team identifies the device and adds it to the owner list for next time. Tomás counts unknown hosts in each lab run, so the size of the inventory gap is visible. Each unknown host is also logged as a ticket for the network team, with the lab's synthetic name and match.

### 12.5 Lab report

Aim, method, results with exact outputs, interpretation, problems and one improvement.

Exact outputs matter because a reviewer compares them with a rerun of the same script. Interpretation explains why each route is right, such as servers going to incident response. Problems and an improvement show that the student tested the script's limits, not just ran it once and copied the output. The lab report is about one page long for each pair. Tomás's report included the unknown-asset count and the Finance server rule his pair added. Tutors mark it against these six headings, so a missing heading costs marks even when the script itself works.

### 12.6 Improvement ideas

Add last-seen times; add severity by technique; read the owner list from a file maintained by the network team.

Last-seen times help the receiving team judge whether the match is current or historic. Severity by technique could put T1071 command traffic ahead of a single phishing visit. Reading owners from the network team's file would keep the list current without editing the script, which removes one cause of stale routing. Each idea is tested on the lab data before it is written up as an improvement. Reading owners from a file also means a missing owner can be fixed by editing data, without changing and retesting the code. Students record which idea they tried and what changed in the output.

### 12.7 Pair work

One student runs, the other checks outputs against expectations, then swap.

The partner compares each printed route with what they expect from the owner list before the pair agrees on the result. Swapping roles means both students practise running the script and checking its output. The pair notes any disagreement in their lab report, together with how they resolved it. Tomás's pair found the missing Finance server rule during this checking step, before submitting. Pairs are assigned by the tutor, so students work with someone new in each lab. The check is done line by line against the owner list, not by glancing at the output. Each student signs the report's check record before it is submitted.

### 12.8 Safety

No real hostnames or addresses in submitted reports; use the lab's synthetic values.

Lab reports leave the virtual machine and may be read by other students or tutors. Using only the synthetic hostnames and RFC 5737 addresses means nothing about college systems is exposed. The partner check includes a scan of the report for any value that does not come from the lab data. The same rule applies to screenshots and pasted output in the report. The partner rejects any report containing a value that is not in the lab data. Reports that fail the scan are corrected and resubmitted before marking.

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

Each of these problems appears first as a change in counts or an error in a log. A renamed CSV column can make a vendor list load as empty without any error at all. An unknown label value, such as a misspelt TLP marking, must stop the item rather than default to sharing. Each is listed in the fault log with its usual symptom.

### 13.2 Step by step

Check input arrived, parsing succeeded, storage updated, export produced, control loaded. At each step compare counts with yesterday.

Following the pipeline in order finds the first step where counts differ from the day before. In the Tuesday case, DNS logs had arrived but the matcher read none, which placed the fault in parsing. Checking all five steps each time avoids blaming a control when the fault lies earlier. Comparing with yesterday works only if counts are logged each day, which is why the scripts record them. Counts from the same weekday are better references during term, because volumes follow the timetable.

### 13.3 Tool logs

Scripts write their own logs: start time, inputs, counts, errors. Without them, troubleshooting is guesswork.

Tomás's scripts write one line per run with the start time, input file, number of records read, number matched and any errors. The zero count that revealed Tuesday's fault came from these run logs. They are kept in the team repository's log folder, where the supervisor can read them when Tomás is away. Errors are written with the line number or record that caused them. Logs older than the DNS retention period are archived, since no rerun could use the data anyway.

### 13.4 Communicating

If protection lapsed, tell owners plainly: what stopped, since when, what still works, when a fix is expected.

Owners need to know whether they are exposed and for how long. A message that says DNS matching stopped on Tuesday morning, while email blocking still works, lets them judge the risk. Giving an expected fix time, even a rough one, saves them chasing for updates while the fault is being repaired. Messages about lapses go to the owners' shared mailboxes, never to one person. A second message confirms when protection is restored, with the time the rerun finished.

### 13.5 Prevention

After each fix, add a check: alert if imports are zero; alert on unknown labels; compare exported and loaded counts.

Each check turns a fault that once went unnoticed into an alert. The zero-parse warning added after the Tuesday case would show the same problem the first day it happened. Comparing exported and loaded counts catches lists that failed to load into the DNS filter or gateway. Each new check is listed in the fault log entry that prompted it. Tomás tests each new check on synthetic data before it goes live, to confirm it fires when it should.

### 13.6 Keep changes small

Change one thing at a time while troubleshooting; otherwise you cannot tell which change helped.

In the Tuesday case, Tomás changed only the parser to read fields by name, then reran the data. If he had also changed the matching rules, he could not have said which change restored the three matches. Each change is committed separately in the repository with a short note. Small changes also make rollback simple, because only one commit has to be reverted. After each change, Tomás reruns the sample file of log lines to confirm nothing else broke.

### 13.7 Escalation

When the problem lies in another team's system, give them evidence: the step where counts stop, timestamps and error messages.

The resolver belongs to the network team, so a format change there is theirs to explain and to announce in future. Showing them the step where counts stopped, with times and the parser's error lines, saves them repeating the diagnosis. Tomás asks to be told before future updates that change log formats. The evidence is attached to a ticket in the other team's queue, not sent in a private message. Tomás follows up if the ticket has no reply within the agreed service time.

### 13.8 Recording

A fault log with symptom, cause, fix and prevention builds team memory.

The fault log uses the same fields for every entry, so similar faults can be found quickly. The Tuesday entry records the resolver update as cause, parsing by name as fix and the zero-count warning as prevention. New team members read the log to learn how the pipeline usually breaks. Entries are written as soon as the fix is confirmed, while details are fresh. Each entry links to the commit that fixed the fault and the ticket that reported it.

### 13.9 Calm under pressure

Pipeline faults during an incident feel urgent. Follow the same steps; skipping them usually costs more time.

During an incident, the temptation is to change several things at once to restore matching quickly. Following the steps in order usually finds the fault faster than guessing. Tomás keeps notes as he works, so the incident lead can see what has been checked and what remains. Tomás tells the incident lead how long the next step will take, so they can plan around the gap. If the fault cannot be fixed quickly, he says which fallback from the dependency plan applies.

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

These tasks give the same result whoever performs them, so a script does them faster and without tiredness. Daily import and validation catch malformed items before they reach the platform. Weekly counts by technique feed the management summary, and the trial in the worked example showed why deduplication must be part of them. Each automated task still writes its decisions to the log, so a person can check what it did. Expiry flags only mark entries; the decision to remove or renew stays with a person.

### 14.2 Unsuitable tasks

Deciding relevance of new reports, grading new sources, blocking services that students depend on, sharing restricted data outward.

Each of these needs judgment about context that a rule cannot capture. Blocking a service students depend on, such as an examination board, could stop work across the college. Sharing restricted data outward cannot be undone once sent, so a person must check the label and recipient every time. Grading new sources needs knowledge of their history, which a script does not have. Relevance of new reports depends on Ashgrove's services and calendar, which change each term.

### 14.3 Approval gates

Automation prepares a block list; a person approves additions for the DNS filter. Low-risk categories — ESX GREEN domains graded B or better — may be auto-approved after a trial period agreed with the network team.

The approval step lets the network team see every new entry before it reaches the DNS filter. Auto-approval is limited to ESX GREEN domains graded B or better because those have the lowest risk of blocking something important. The trial period gives evidence that the category behaves as expected before anyone stops checking it.

### 14.4 Scheduling and alerts

Jobs run at fixed times; failure sends an alert to a shared mailbox, not one person.

Fixed times make it easy to notice when a job has not run. Sending failure alerts to a shared mailbox avoids the problem found in the system model, when ESX alerts sat unread in one person's inbox. Each alert names the job, the step that failed and where its log is stored. The shared mailbox is the one created after the ESX alert problem, read by two people. Alerts also go to the on-call person outside working hours.

### 14.5 Documentation

Each job: purpose, schedule, inputs, outputs, owner, alert recipient, how to disable it.

With this documentation, the on-call person can understand a job and stop it without reading the code. Inputs and outputs show what else would be affected if the job fails. Tomás keeps one document per job in the team repository, beside the job's code and tests. Tomás reviews each job document when the job changes, and the supervisor approves the update. A job without a current document is not allowed to run in production. The same template is used for every job, so readers know where to find each field.

### 14.6 Never automated

Contact with suspicious sites, scanning, downloading samples, posting to public channels.

These actions could alert attackers, bring malicious files onto college systems or publish restricted material, and they are forbidden even when done by hand. Automating them would also remove the human check that might catch a mistake. The rule is written on the safety sheet and in each job's documentation. The rule is checked during code review of every new job. Any code that would make network requests to indicators, rather than to ESX or college systems, is rejected. Tomás's scripts read only exported college files and ESX's TAXII collection.

### 14.7 Trial periods

New automation runs alongside manual work for two weeks; results are compared before switching.

Running both side by side shows any difference between the script and the manual result before the script is trusted. In the weekly counts trial, the duplicate ESX item appeared as a difference in the T1566 tally. Tomás switched to the script only after its counts matched his manual tally. The comparison is recorded day by day, so any difference can be traced. If a difference cannot be explained, the trial is extended rather than ended.

### 14.8 Kill switch

Every job can be disabled quickly by the on-call person without editing code.

A job that sends a wrong block list to the DNS filter must be stopped within minutes. Editing code under pressure out of hours risks further mistakes. Each job therefore has a documented switch, such as a flag in its configuration file, that the on-call person can change. The switch is tested at the end of each trial period, by the on-call person following the documented steps. Stopping a job does not remove lists already loaded, so the runbook also explains how to roll back the last change.

### 14.9 Review

Twice a year, jobs no longer serving a requirement are retired.

A requirement may end, for example when a supplier is replaced or ESX changes how it shares. Jobs left running after that still consume attention when they fail and may feed stale data into controls. The review checks each job against a current requirement and its rule logs before deciding to keep it. The rule logs show which rules fired and how often in the past six months. A retired job's code stays in the repository with a note explaining why it stopped.

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
- **EX055 — Trial catch.** What did the trial reveal about the weekly counts? *Rubric:* 3 = duplicate from re-sent item; dedupe by value; 2 = one; 1 = vague; 0 = none.
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

Each consumer needs a different product in a different form. The help desk needs plain advice it can read to callers, while the network team needs a validated list. Tomás asks each consumer once a term whether the product still fits their work, so the outputs change when their needs do. Incident response also receives a short standing note of current campaigns aimed at colleges.

### 15.2 Service levels

Urgent items reviewed within four working hours; routine within two days; scam list each Monday in term time.

Urgent items include confirmed phishing aimed at Ashgrove and credential exposures, where hours matter. Routine items can wait up to two working days without causing harm. The Monday scam list in term time gives the help desk a predictable briefing before the busiest day of the week. Service levels are agreed with each consumer team and written in the CTI runbook. During college holidays the scam list pauses, while urgent items keep the four-hour review. Missed service times are recorded in the failure log with their cause.

### 15.3 Dependencies

ESX membership and its TAXII server; the platform's hosting; the cloud email supplier's logs; the network team's DNS filter. Each can fail.

Tomás lists each dependency with its owner and what stops if it fails. The cloud email supplier's thirty-day log retention is itself a dependency limit, because it decides which past events can be checked. The list is reviewed with the supervisor each term alongside the system diagram. For each dependency, the list also records how a failure would be noticed, such as a zero import count. ESX membership is renewed each year, and its renewal date is on the list.

### 15.4 Failure plans

If ESX is unavailable, use national education advisories; if the platform fails, scripts can read ESX email alerts directly; if the DNS filter fails, the proxy carries urgent domain blocks.

Each fallback is slower or narrower than the normal path, so the plan states what is lost. National advisories cover education broadly but lack ESX members' specific indicators. The proxy covers staff only, so urgent domain blocks through it would leave student devices on Wi-Fi unprotected until DNS filtering returns. The fallbacks are tested once a term, outside exam periods. Each test is recorded in the dependency list with its date and result.

### 15.5 Feedback loop

Help desk forwards suspicious messages reported by students and staff to the CTI queue; this is often the earliest warning.

Students and staff often see a scam before any feed reports it, as the forty enrolment-week reports showed. The help desk forwards the original message with headers, which lets Tomás run his authentication parser on it. Each forwarded report is acknowledged, so the help desk knows the queue is being read. Tomás also tells the help desk what came of their reports, so they see the value of forwarding them.

### 15.6 Incident support

During incidents, Tomás follows the incident lead's priorities, as NIST SP 800-61r3 places intelligence within response.

The incident lead decides what matters most, such as which systems to contain first. Tomás answers their questions with what is known about the indicators and techniques involved. He keeps his own notes timestamped in the shared incident document, as the documentation rules require. Requests from the incident lead take priority over routine triage during the incident. Tomás tells his supervisor which routine items will be delayed, so consumers can be warned. His intelligence notes in the incident follow the same three-line format.

### 15.7 Supplier intelligence

Advisories about the learning-platform supplier or the email supplier go to contract managers too, who can ask the supplier for assurance.

A supplier advisory may require action that only the supplier can take, such as patching the learning platform they host. Contract managers can ask the supplier for written assurance or a timeline. Tomás sends them a short summary with the advisory's label, so they know what they may forward. The summary also states whether Ashgrove uses the affected product version, which the service table shows.

### 15.8 Calendar

Term starts, exam periods and enrolment bring scam peaks; the team plans extra monitoring then.

During enrolment week, the help desk received forty reports of fake fee payment emails in a short period. Planning ahead means extra triage time is booked and the help desk is briefed before term begins. Tomás marks these weeks in the team calendar at the start of each year. Exam periods bring a different risk: changes are avoided, so monitoring matters more than new blocks. Tomás reviews each peak afterwards, noting the scam themes seen.

### Measuring integration

Count how often each consumer acted on CTI each month: blocks applied, help-desk scripts used, incident questions answered. Falling numbers may mean products no longer fit, prompting a conversation with that team.

### Worked example

During enrolment week, the help desk forwards forty reports of fake "fee payment" emails. Tomás identifies two sender domains, requests blocks, gives the help desk a script for callers and sends ESX a GREEN item. Two other colleges block the domains the same day.

> **Synthetic case.** The campaign is invented.

### Errors and limits

Fallbacks need testing; an untested plan may fail when needed.

### Exercises

- **EX057 — Fallback list.** Give the fallback for an ESX outage and for a platform failure. *Rubric:* 3 = national advisories; scripts read email alerts; 2 = one; 1 = vague; 0 = none.
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

Runbooks let someone other than Tomás perform a task the same way when he is away. The credential-exposure runbook is the one tested in the worked example, which showed that one unclear step can stop a colleague. Each runbook links to the job documentation for any automated parts it relies on.

### 16.2 Safety rules

A one-page rule sheet: no contact with suspicious infrastructure; no testing of exposed passwords; TLP respected; personal data minimised; suspicious files handed to qualified staff; RFC 5737 addresses and .example domains in training material.

The sheet gathers rules that appear across the book into one page that new students can read on their first day. Each rule links to the runbook step where it applies, such as never pasting passwords into a ticket. The sheet is reviewed whenever a failure review shows a rule was unclear.

### 16.3 Handling labels in documents

Runbooks themselves are usually internal (TLP:AMBER) because they reveal how defences work. Examples inside them use synthetic values.

A runbook explains which logs are searched and how block lists are loaded, which would help an attacker plan around them. Labelling it AMBER keeps it within Ashgrove and the clients who need it. Synthetic examples mean the runbook can be used for training without exposing real indicators or hostnames. Some runbooks, such as credential-exposure handling, also contain personal-data steps, which is another reason to keep them internal. The label is printed at the top of every page.

### 16.4 Currency

Each document shows owner, last review date and next review. Changes in tools trigger reviews.

A runbook that still describes an old parser or a retired tool will mislead whoever follows it. The resolver format change in the Tuesday case triggered a review of the DNS import runbook. Owners receive a reminder when the next review date arrives, and the review result is recorded in the document. An overdue review is flagged in the team's monthly meeting. The owner either confirms the document still matches the tools or updates it the same week.

### 16.5 Writing style

Short numbered steps, one action each; screenshots only where needed; commands in code blocks; expected results stated after each step.

One action per step lets a reader check each result before moving on. Stating the expected result tells them at once when something has gone wrong. Commands in code blocks can be copied exactly, which avoids typing errors in hostnames and file paths. Screenshots go out of date quickly when tools change, so text is preferred. Each runbook starts with a single sentence saying when it should be used. Warnings, such as never pasting passwords, appear just before the step they apply to.

### 16.6 Testing documentation

A colleague follows the runbook without help. Wherever they hesitate, the text is unclear.

The colleague's hesitation in the worked example came at 'notify the identity team', where the channel was not named. Tomás watched the test without helping and noted each pause in the runbook. After the step was rewritten, the next test ran without questions, which is the test's pass condition. The colleague chosen is someone who has not done the task before, so gaps in the text are not filled from memory. Tests are repeated with a new colleague after every substantial change. The tester's name and date are recorded in the runbook's history.

### 16.7 Version history

Keep documents in the team's repository so changes are tracked and reversible.

The repository shows who changed a runbook, when and why, through each commit message. If a change makes a procedure worse, the earlier version can be restored. Tomás's scripts and their documentation sit in the same repository, so code and runbook changes can be reviewed together. Runbook commits are reviewed by a second team member before they are merged. Tomás writes commit messages that state which step changed and why. The repository's history then serves as a record for audits. Older versions remain readable for anyone checking how a past incident was handled.

### 16.8 Incident notes

During incidents, write timestamped notes in a shared document; they later become the basis for review.

Timestamped notes record decisions and checks while they are fresh, before memory changes them. They let the incident lead see what has been done without interrupting people. After the incident, the review uses them to rebuild the order of events, and gaps in them become lessons for the next incident. Each note starts with a UTC time and the author's initials. Tomás writes what was checked and what was found, not his opinions. The shared document is restricted to the incident team and the supervisor.

### 16.9 Accessibility

Plain language helps colleagues whose first language differs and newcomers alike.

Several help-desk staff speak English as a second language, and new placement students arrive each year. Short sentences and common words help both groups follow a runbook under pressure. Tomás avoids unexplained abbreviations and links each technical term to the team's short glossary. Tomás tests readability by asking a help-desk colleague to explain a runbook step back to him. Where the colleague's explanation differs from the intended meaning, he rewrites the step in simpler words. He avoids idioms, which can confuse readers whose first language is not English. The glossary gets new entries when a term causes confusion.

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
- **EX063 — Hesitation test.** How was the credential runbook improved? *Rubric:* 3 = specified restricted ticket, no passwords, encrypted attachment; 2 = partial; 1 = vague; 0 = none.
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

Pairs mirror the partner check that every community product must pass before release. The check record lists what the partner looked at and what they found. Submitting both summaries together lets the tutor confirm that they come from the same dataset and differ only where labels require. The lab script is the same for every pair, so tutors can compare summaries directly. Pairs keep the check record on the template provided, signed by both students.

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

The community counts are lower for T1566 and T1078 because their AMBER items are removed. T1486 disappears entirely from the community version, since its only item is RED. A reader of the community summary therefore cannot learn that a ransomware-related item exists, which is the purpose of the filter.

### 17.3 Mentioning withheld items

The community summary may say "some items were withheld under their handling labels" but must not describe them. Even "a ransomware item was received under RED" could reveal too much.

Mentioning that items were withheld tells community readers the summary is not complete. Describing them, even by topic, would share part of their content with people outside the label's audience. The approved sentence is kept in the summary template, so nobody has to improvise wording under time pressure. The template sentence is reviewed by the supervisor once a year.

### 17.4 Checking before release

The partner student checks: every included item is CLEAR or GREEN; no personal data; counts match the script; wording reveals nothing about withheld items.

Each check addresses a different way the community version could leak. Label checks catch AMBER items that slipped through, and the personal-data check catches names in sample subject lines. Matching counts with the script output shows nothing was added by hand, and the wording check catches hints such as the RED phrase. The partner signs the check record only when all four checks pass.

### 17.5 Internal value

The internal summary helps management see that phishing dominates and that one ransomware-related item arrived, prompting a backup check.

Management readers need to know what to act on, not only what arrived. The ransomware-related item prompts a check that backups can be restored, which is an internal action. The internal summary can say this because it stays within Ashgrove under the labels of its items. The internal summary also shows that valid-account abuse appears twice, supporting the multi-factor plan for students. Management reads the internal summary together in the monthly meeting.

### 17.6 Format

Each summary: period, counts by technique, top actions taken, requests to readers.

The same four headings in both versions make them easy to compare during the partner check. Counts by technique come straight from the lab script's output, never typed by hand. Requests to readers ask for specific help, such as reporting a scam theme to the help desk, so the summary leads to action. Each summary covers one calendar week, from Monday to Sunday inclusive. Top actions taken are listed with their owners, such as the email team blocking a domain. The community version lists only actions safe to share under GREEN.

### 17.7 Common mistakes

Forgetting AMBER+STRICT; including technique counts that could only come from a RED item; copying internal notes into the community version.

AMBER+STRICT items must stay inside Ashgrove, so they belong in neither the community nor a client version. A technique count that appears only because of a RED item reveals that item exists. Copying internal notes is the commonest cause, because notes are written for colleagues and may name systems or people. Tomás's own first draft showed the second mistake, through the phrase about an encryption-related item.

### 17.8 Reflection

Students note how the two audiences changed what they wrote.

Tomás noted that the internal summary could explain the backup check, while the community summary could only give counts. Writing for ESX members made him think about what another college could act on. These reflections go into the lab report beside both summaries and the check record. The reflection also asks what the partner check caught that the writer missed. Tomás's answer named the RED phrase and his assumption that one vague word was harmless. Students compare reflections with another pair in the next session.

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

The project meets a real need, because the help desk relies on the Monday list in term time and producing it takes two hours by hand. It also uses skills from the course: parsing, grouping, removing personal data and writing for a non-technical reader. The supervisor approved the scope before any code was written.

### 18.2 Plan

Week 1: requirements with the help-desk lead. Week 2: build on synthetic data. Week 3: test with past weeks' data on the college server. Week 4: report-only run. Week 5: handover.

Building on synthetic data first means no personal data is processed until the script is tested. Testing on past weeks' data on the college server keeps real reports inside Ashgrove's systems. The report-only run in week 4 produces lists for comparison but does not send them to the help desk. Each week ends with a meeting with the supervisor and a short written status.

### 18.3 Safety and privacy

Reports contain names and email addresses of students and staff. The script strips them; a person checks each list before release. Only the help desk receives it.

Stripping names and addresses happens before the list is grouped, so the grouping code never handles them. The human check catches anything the script missed, such as a name inside a subject line. Restricting the list to the help desk keeps samples of real scam messages away from wider circulation. Test output on the college server is deleted once the comparison is recorded.

### 18.4 Measures

Time to produce the list (before: two hours; target: thirty minutes); help-desk satisfaction; accuracy of grouping checked by the supervisor.

The time measure compares production before and after with the same steps counted. Accuracy is checked by the supervisor grouping the same week's reports by hand and comparing the result with the script. Satisfaction is asked of the help-desk lead, since they are the main user of the list. The two-hour figure comes from the help desk's own estimate of the manual process. Accuracy is checked by the supervisor on the report-only weeks.

### 18.5 Handover

Runbook, job documentation, owner (the CTI team), kill switch and a short training session for the help-desk lead.

Handover makes the CTI team, not Tomás, responsible for the tool once his placement ends. The runbook and job documentation follow the formats used for other jobs, so the team can maintain it. Training the help-desk lead lets them check that lists look right without needing to read the code. The kill switch is tested in front of the CTI team during handover. The training session is recorded in the project log with the date and attendees.

### 18.6 Presentation

Ten minutes: problem, solution, results, limits, next steps.

The ten minutes are given to the CTI team and the help-desk lead together. Tomás shows the before and after production times and the library and parking fine example. Limits and next steps are presented plainly, including the need for manual grouping of new themes. Tomás rehearsed the presentation with his supervisor beforehand to keep within the ten minutes. Questions from the team are answered after the talk, and any requested changes are listed in the handover notes. The slides are kept in the repository beside the runbook.

### 18.7 Supervision

Weekly meetings with the supervisor review progress and risks. Decisions are recorded.

Weekly meetings let the supervisor spot risks early, such as personal data appearing in test output. Recorded decisions show why the project changed, for example the separate fine categories added after help-desk feedback. The record also supports the assessment, because it shows how Tomás responded to advice. Risks raised in meetings are listed with an owner and the date they were closed. The supervisor signs off each stage of the five-week plan before the next begins.

### 18.8 Limits

The tool groups by keywords; new scam themes may need manual grouping.

A scam theme that uses new words will not match existing keyword rules and will appear ungrouped. The runbook tells the operator to group such items by hand and suggest a new rule. The human check before release catches grouping errors, as it did with the library and parking fines. The help-desk lead knows this limit from the training session. New themes and the rules added for them are recorded in the runbook, so the team can see how the keyword rules grow.

### 18.9 Reflection

What worked, what he would change, what he learned about users.

Tomás's reflection records that he had not expected callers to need the two fine scams separated. He would ask the help desk for sample calls earlier in requirements next time. He also notes that the report-only run was where the real users' needs became clear. The reflection is written after the presentation, so it can include the team's questions. It forms part of Tomás's course assessment together with the project log and the help-desk sign-off.

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
- **EX071 — Grouping fix.** What grouping problem appeared and how was it fixed? *Rubric:* 3 = library/parking fines merged; rule added after help-desk feedback; 2 = partial; 1 = vague; 0 = none.
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
