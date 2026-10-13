# Network and Communications Security: Rapid Course

- Language: English (`en`); course 011, Rapid course (1 month).
- Editorial state: **draft**. Chapters 1–4 of 4 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; Two offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: newcomers and small-business staff who need safe, practical network security basics in one month.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: review and test only networks and devices you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic configurations, flow records, logs and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one office worker helping a small bakery, from what network security protects and how to choose first steps, through written scope and safe practice, to listing devices and dependencies, and finally checking the router against a checklist, making agreed changes and writing a short report. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Leo Hart** | Rapid-course learner | Invented |
| **Nadia Petrov** | Coach | Invented |
| **Quayside Skills Centre** | Fictional training centre | Invented |
| **Bramble Street Bakery** | Fictional partner (one shop) | Invented |

### Core sources

NIST [SP 800-41r1](https://doi.org/10.6028/NIST.SP.800-41r1), [SP 800-77r1](https://doi.org/10.6028/NIST.SP.800-77r1), [SP 800-94](https://doi.org/10.6028/NIST.SP.800-94), [SP 800-207](https://doi.org/10.6028/NIST.SP.800-207), [SP 800-153](https://doi.org/10.6028/NIST.SP.800-153) and [SP 800-53r5](https://doi.org/10.6028/NIST.SP.800-53r5); [CIS Controls v8](https://www.cisecurity.org/controls/v8); IETF [RFC 8446](https://www.rfc-editor.org/rfc/rfc8446), [RFC 4301](https://www.rfc-editor.org/rfc/rfc4301) and [RFC 2827](https://www.rfc-editor.org/rfc/rfc2827). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Network and communications security: foundations and decisions

### Learning outcomes

You will (1) explain what network security protects; (2) describe a small business network; (3) make first decisions with limited time.

### 1.1 Why this course

Leo Hart works in the office of a small business and joins a one-month rapid course at the fictional Quayside Skills Centre to learn the basics of network security. His coach is Nadia Petrov. The course uses one running example: the fictional Bramble Street Bakery, a single shop with a café, card payments, an office computer, two tills, online orders and free Wi-Fi for customers. The owner, Ellen, asked Leo to help because nobody at the bakery knows much about networks. Every lab uses synthetic data, and any change to the bakery's equipment is made only with Ellen's agreement.

### 1.2 What network security protects

Network security protects the information that travels between devices and the devices that send and receive it. At the bakery, that includes card payments between the reader and the bank, orders arriving from the website, the owner's email and accounts on the office computer, and the café Wi-Fi that customers use. The three goals are confidentiality, so customer and payment details stay private; integrity, so orders and accounts are not changed; and availability, so tills and card payments work during opening hours. Leo learns to judge every decision against these three goals.

### 1.3 How a small network works

The bakery has one router supplied by its internet provider. The router connects to the internet, gives out addresses to devices using DHCP, provides Wi-Fi and protects the shop from unrequested traffic from outside. All devices share one local network: tills, card reader, office computer, the owner's phone and every customer phone on the café Wi-Fi. Leo draws this on one page. The drawing shows the main weakness straight away: customers' phones share a network with the tills and the office computer, so nothing stops them reaching each other.

### 1.4 Threats to a small business

Small businesses face common threats. A customer's infected phone might try to reach other devices on the same network. Someone might guess the router's administrator password if it is still the factory default. A phishing email might trick the owner into entering a password on a fake page. Old router firmware might have known weaknesses. Leo notes that small businesses are rarely targeted individually; most harm comes from automated attacks and opportunistic misuse, which simple controls stop. This shapes his priorities towards basic, cheap, effective steps.

### 1.5 Making decisions with limited time

Ellen has little time and a small budget, so Leo learns to make decisions in order of value. He asks three questions for each possible step: how much harm does it prevent, how much does it cost in money and time, and could it disrupt the shop? Separating customer Wi-Fi from business devices prevents a lot of harm, costs nothing on most routers and can be done after closing. Buying a new firewall costs more and takes longer. Starting with high-value, low-cost steps delivers most of the benefit quickly.

### 1.6 Guidance worth knowing

Leo learns that good guidance exists even for small organisations. The CIS Controls list prioritised safeguards, starting with knowing which devices you have. NIST SP 800-153 explains how to secure wireless networks, including keeping guest networks separate. NIST SP 800-41r1 explains firewall policy, including the idea of denying traffic by default. Leo does not need to read them in full during the course, but he learns to cite them when explaining to Ellen why a step matters, which makes his advice more convincing than personal opinion.

### 1.7 The plan for the month

Nadia and Leo agree a plan: in week one, understand the network and decide priorities; in week two, agree scope and permission with Ellen; in week three, list devices and dependencies; in week four, check the router against a checklist, make agreed changes and write a short report. Each week ends with a short review. Writing the plan down keeps the work focused and gives Ellen a clear idea of what will happen and when she needs to be involved.

### Worked example

Leo's one-page drawing shows tills, card reader, office computer and customer phones on one network, and his first priority is separating customer Wi-Fi.

> **Synthetic case.** The bakery and all data are synthetic.

### Errors and limits

Spending the first week researching expensive products delays cheap steps that would remove most risk.

### Exercises

- **EX001 — Bakery assets.** Name three things network security protects at the bakery. *Rubric:* 3 = card payments, orders, accounts or Wi-Fi;; 2 = two;; 1 = one;; 0 = none.
- **EX002 — Main weakness.** What weakness does the one-page drawing reveal? *Rubric:* 3 = customer phones share network with tills and office PC;; 2 = shared network;; 1 = vague;; 0 = none.
- **EX003 — Goal for tills.** Which security goal matters most for tills during opening hours? *Rubric:* 3 = availability, so sales and payments keep working;; 2 = availability, without explanation;; 1 = confidentiality;; 0 = none.
- **EX004 — Opportunistic threats.** Why are basic controls effective for small businesses? *Rubric:* 3 = most harm from automated, opportunistic attacks;; 2 = automated;; 1 = not targeted;; 0 = none.
- **EX005 — Decision questions.** List Leo's three questions for each step. *Rubric:* 3 = harm prevented, cost, disruption;; 2 = two;; 1 = one;; 0 = none.
- **EX006 — First step choice.** Why separate customer Wi-Fi first? *Rubric:* 3 = high value, low cost, low disruption;; 2 = cheap and effective;; 1 = required;; 0 = none.
- **EX007 — Default password threat.** Why is a factory-default router password dangerous? *Rubric:* 3 = easily guessed, gives control of router;; 2 = guessable;; 1 = vague;; 0 = none.
- **EX008 — Firewall guidance.** Which publication explains default-deny firewall policy? *Rubric:* 3 = NIST SP 800-41r1;; 2 = 800-41r1;; 1 = other;; 0 = none.
- **EX009 — Wireless guidance.** Which publication covers securing wireless networks? *Rubric:* 3 = NIST SP 800-153;; 2 = 800-153;; 1 = other;; 0 = none.
- **EX010 — Inventory first.** What do the CIS Controls start with? *Rubric:* 3 = knowing which devices you have;; 2 = inventory;; 1 = passwords;; 0 = none.
- **EX011 — Week two task.** What happens in week two of the plan? *Rubric:* 3 = agree scope and permission with Ellen;; 2 = permission;; 1 = changes;; 0 = none.
- **EX012 — Router roles.** Name three jobs the bakery router performs. *Rubric:* 3 = internet connection, DHCP, Wi-Fi or blocking outside traffic;; 2 = two;; 1 = one;; 0 = none.
- **EX013 — Integrity example.** Give an integrity concern at the bakery. *Rubric:* 3 = orders or accounts changed;; 2 = changed data;; 1 = generic;; 0 = none.

### Synthesis

Understanding what the network protects and choosing high-value, low-cost steps first is the foundation of practical security.

### Continue studying — chapter 01 of 04

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Scope, permission and safe practice

### Learning outcomes

You will (1) agree written scope and permission; (2) work safely on a live business; (3) handle information responsibly.

### 2.1 Why permission matters

Even helpful security work needs permission. Changing router settings, looking at device lists or reading logs can disrupt a business or reveal private information. Without the owner's permission, such actions may also break the law. Nadia makes this the first practical lesson: before touching anything at the bakery, Leo agrees in writing with Ellen what he will do, when and how. Permission is not a formality; it protects Ellen's business, her customers and Leo himself, and it is expected of anyone doing security work.

### 2.2 Writing a simple scope

Leo's scope is one page. It lists what he may do: view the router's settings with Ellen present, export the list of connected devices, check settings against a checklist and, with Ellen's approval of each change, adjust Wi-Fi and router settings. It lists what he may not do: access the card reader's internal settings, which belong to the payment provider; open business files on the office computer; or make changes during opening hours. Both sign it. A short, clear scope prevents misunderstandings and makes it easy to check whether a task is allowed.

### 2.3 Third-party equipment

Some equipment at the bakery belongs to others. The card reader is provided and managed by a payment company under its own security rules; changing its settings could break payments and the contract. The router belongs to the internet provider, though Ellen can change its settings. Leo checks each device's owner and any contract terms before suggesting changes. Where a change affects a third party's equipment, he recommends Ellen contact the provider rather than doing it himself. Respecting ownership avoids accidental breaches of contracts and service.

### 2.4 Working safely on a live business

The bakery cannot afford downtime during opening hours. Leo plans every change for after closing, keeps a note of the original settings so he can put them back, and tests that tills and card payments work afterwards. He changes one thing at a time so that if something breaks, the cause is obvious. He also keeps Ellen's phone number handy and stops if anything unexpected happens. These habits are simple, but they are what separate safe practice from well-meant disruption.

### 2.5 Handling information

During the work, Leo sees information such as device names, customer Wi-Fi usage and possibly the Wi-Fi password. He writes down only what he needs, stores notes on the skills centre's secure storage rather than his personal phone, and never shares passwords by message. If he changes the Wi-Fi password, he gives it to Ellen in person or on paper. When the course ends, he deletes his notes as agreed. Careful handling of information is part of trustworthiness, and small businesses rely heavily on trust.

### 2.6 Stopping and asking

Sometimes a task reveals something outside scope, such as an unknown device or an odd message in the router's log. Leo's rule is to stop, write down what he saw and ask Ellen before going further. He does not investigate the unknown device's contents or try to connect to it. In week three, this rule matters when he finds two unknown devices. Stopping and asking may feel slow, but it keeps the work within agreed limits and lets the owner decide what happens next.

### 2.7 Recording what was done

Every action is recorded: date, time, what was changed, original value, new value and who approved it. Leo uses a simple table in a notebook and copies it into his final report. The record helps if something goes wrong later, because anyone can see exactly what changed and when. It also shows Ellen the value of the work and gives her a reference for the future. Recording actions is a habit worth starting from the very first task, even in a small shop.

### Worked example

Leo and Ellen sign a one-page scope listing four permitted activities, three exclusions and a rule to make changes only after closing.

> **Synthetic case.** The scope is synthetic.

### Errors and limits

Changing a payment provider's device without permission can break payments and contracts.

### Exercises

- **EX014 — Permission reasons.** Give two reasons security work needs permission. *Rubric:* 3 = disruption, privacy, legality or protection;; 2 = two;; 1 = one;; 0 = none.
- **EX015 — Card reader exclusion.** Why is the card reader outside Leo's scope? *Rubric:* 3 = owned and managed by payment company;; 2 = third party;; 1 = broken;; 0 = none.
- **EX016 — Change timing.** When does Leo make changes, and why? *Rubric:* 3 = after closing to avoid disrupting sales;; 2 = after closing;; 1 = anytime;; 0 = none.
- **EX017 — Original settings.** Why record original settings before changing them? *Rubric:* 3 = to restore them if something breaks;; 2 = rollback;; 1 = audit;; 0 = none.
- **EX018 — One change at a time.** Why change one thing at a time? *Rubric:* 3 = cause of any problem is obvious;; 2 = clarity;; 1 = speed;; 0 = none.
- **EX019 — Password sharing.** How should a new Wi-Fi password be given to Ellen? *Rubric:* 3 = in person or on paper, not by message;; 2 = in person;; 1 = text;; 0 = none.
- **EX020 — Unknown device rule.** What does Leo do when he finds an unknown device? *Rubric:* 3 = stop, note it, ask Ellen;; 2 = ask;; 1 = investigate;; 0 = none.
- **EX021 — Action record fields.** List four fields in the action record. *Rubric:* 3 = date, change, original, new or approver;; 2 = three;; 1 = fewer;; 0 = none.
- **EX022 — Notes storage.** Where are Leo's notes kept? *Rubric:* 3 = skills centre secure storage, not personal phone;; 2 = secure storage;; 1 = phone;; 0 = none.
- **EX023 — End of course data.** What happens to Leo's notes when the course ends? *Rubric:* 3 = deleted as agreed;; 2 = deleted;; 1 = kept;; 0 = none.
- **EX024 — Third-party change route.** How should changes to a provider's equipment be handled? *Rubric:* 3 = Ellen contacts the provider;; 2 = provider;; 1 = Leo changes it;; 0 = none.
- **EX025 — Scope benefit.** What does a written scope make easy? *Rubric:* 3 = checking whether a task is allowed;; 2 = clarity;; 1 = vague;; 0 = none.
- **EX026 — Safe practice test.** What should Leo test after each change? *Rubric:* 3 = tills and card payments work;; 2 = payments;; 1 = vague;; 0 = none.

### Synthesis

Written scope, respect for ownership, safe timing and careful records make security help trustworthy.

### Continue studying — chapter 02 of 04

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Network and communications security: systems, data and dependencies

### Learning outcomes

You will (1) list devices and dependencies; (2) find unknown devices; (3) understand which services the business relies on.

### 3.1 Knowing your devices

You cannot protect devices you do not know about. Leo's first technical task is a device list for the bakery: each device's name, purpose, owner, how it connects and its hardware address. He starts with what Ellen knows: two tills, the card reader, the office computer and her phone. Then he compares this with what the router sees. The CIS Controls put inventory of devices first for this reason; every later step, such as deciding what may connect where, depends on it.

### 3.2 What the router knows

The router keeps a list of devices it has given addresses to, called DHCP leases. Each lease shows a hardware address and the address given. With Ellen's permission, Leo exports this list after closing, when customer phones have left. Comparing the leases with the known list shows any devices nobody accounted for. Leo uses synthetic data in the lab exercise below to practise the comparison before doing it with the real export, so mistakes in his method do not affect the real check.

### Lab — Unknown devices

```python
"""Compare a synthetic device list with synthetic router DHCP leases to find unknown devices (stdlib only)."""
known = {"aa:01": "till-1", "aa:02": "till-2", "aa:03": "office-pc", "aa:04": "card-reader", "aa:05": "owner-phone"}
leases = [("aa:01", "192.168.1.10"), ("aa:02", "192.168.1.11"), ("aa:03", "192.168.1.20"), ("aa:05", "192.168.1.30"),
          ("bb:77", "192.168.1.41"), ("aa:04", "192.168.1.12"), ("cc:19", "192.168.1.42")]
seen = {m for m, _ in leases}
for m, ip in leases: print(f"{m}  {ip:14}{known.get(m, 'UNKNOWN')}")
print("unknown:", sorted(seen - set(known)), " known but not seen:", sorted(set(known) - seen))
```

Run with `python3 lab_leases.py`. Verified output:

```text
aa:01  192.168.1.10  till-1
aa:02  192.168.1.11  till-2
aa:03  192.168.1.20  office-pc
aa:05  192.168.1.30  owner-phone
bb:77  192.168.1.41  UNKNOWN
aa:04  192.168.1.12  card-reader
cc:19  192.168.1.42  UNKNOWN
unknown: ['bb:77', 'cc:19']  known but not seen: []
```

### 3.3 Reading the result

In the synthetic data, all five known devices appear, and two unknown devices hold addresses even after closing. Leo writes them down and asks Ellen, following his stop-and-ask rule. One turns out to be a smart speaker a staff member connected to play music; the other is a delivery company's handheld scanner left on charge. Neither is harmful in itself, but both share the network with the tills. Leo recommends moving them to a separate network for non-business devices, such as the guest network once it is isolated.

### 3.4 Dependencies

Leo lists what the bakery depends on to trade: the internet connection for card payments and online orders, the router for Wi-Fi and addresses, the payment provider's service, the website and order platform hosted by a supplier, and email for supplier orders. For each, he notes what happens if it fails. If the internet fails, the card reader may still take some payments offline, depending on the provider, but online orders stop. Knowing dependencies helps Ellen plan, such as keeping a mobile data backup for the card reader.

### 3.5 Where data goes

Leo also notes where important data travels. Card payment data goes from the reader straight to the payment provider, encrypted, and never touches the office computer. Online orders arrive by email and through the order platform's website, which uses HTTPS. Accounts stay on the office computer and a cloud backup. Understanding data flows shows what needs most protection: the office computer, the email account and the order platform login, because they hold or control business and customer information. Leo marks these three on his drawing in a different colour.

### 3.6 Keeping the list current

A device list goes stale quickly as phones are replaced and staff change. Leo suggests Ellen checks the router's device list once a month after closing, comparing it with the known list, and asks about anything new. He leaves a simple printed table for this. The check takes five minutes. Keeping the list current is the cheapest way to notice unexpected devices, and it keeps the foundation for every other control accurate over time. Ellen adds the date and her initials each time she completes the check.

### Worked example

The synthetic lease check finds two unknown devices, later identified as a smart speaker and a delivery scanner, both recommended for a separate network.

> **Synthetic case.** Devices and leases are synthetic.

### Errors and limits

Assuming every connected device is known misses equipment added by staff or visitors.

### Exercises

- **EX027 — Unknown count.** How many unknown devices does the lab find? *Rubric:* 3 = two, bb:77 and cc:19;; 2 = two;; 1 = vague;; 0 = none.
- **EX028 — Lease meaning.** What does a DHCP lease show? *Rubric:* 3 = hardware address and address given;; 2 = device and address;; 1 = password;; 0 = none.
- **EX029 — Export timing.** Why export leases after closing? *Rubric:* 3 = customer phones gone, fewer unknowns to sort;; 2 = clarity;; 1 = speed;; 0 = none.
- **EX030 — Unknown device outcome.** What were the two unknown devices? *Rubric:* 3 = smart speaker and delivery scanner;; 2 = identified;; 1 = malware;; 0 = none.
- **EX031 — Separate network reason.** Why move the speaker and scanner off the business network? *Rubric:* 3 = share network with tills, non-business;; 2 = separation;; 1 = speed;; 0 = none.
- **EX032 — Internet failure effect.** What stops if the internet fails? *Rubric:* 3 = online orders, possibly some card payments;; 2 = orders;; 1 = vague;; 0 = none.
- **EX033 — Card data path.** Where does card payment data go? *Rubric:* 3 = reader straight to payment provider, encrypted;; 2 = provider;; 1 = office PC;; 0 = none.
- **EX034 — Most protected items.** Which three items need most protection? *Rubric:* 3 = office computer, email account, order platform login;; 2 = two;; 1 = one;; 0 = none.
- **EX035 — Monthly check.** How often should Ellen check the device list? *Rubric:* 3 = monthly after closing;; 2 = monthly;; 1 = yearly;; 0 = none.
- **EX036 — Lab practice reason.** Why practise the comparison on synthetic data first? *Rubric:* 3 = avoid mistakes affecting real check;; 2 = safety;; 1 = required;; 0 = none.
- **EX037 — Mobile backup.** What backup does Leo suggest for card payments? *Rubric:* 3 = mobile data backup for card reader;; 2 = mobile;; 1 = vague;; 0 = none.
- **EX038 — Inventory dependency.** Why does every later step depend on the device list? *Rubric:* 3 = decisions about where devices connect need it;; 2 = foundation;; 1 = vague;; 0 = none.

### Synthesis

A current device list, known dependencies and understood data flows show what to protect and what to separate.

### Continue studying — chapter 03 of 04

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Network and communications security: guided lab and applied synthesis

### Learning outcomes

You will (1) check router settings against a checklist; (2) make agreed changes safely; (3) write a short report.

### 4.1 The router checklist

Leo builds a short checklist for the bakery router based on common guidance: the administrator password changed from the factory default; Wi-Fi using WPA2 or WPA3 with a strong passphrase; a guest network for customers that is isolated from business devices; remote administration from the internet turned off; firmware updated recently; and UPnP turned off unless needed, because it lets devices open ports on the router automatically. Each item is easy to check in the router's settings pages and addresses a common weakness in small business networks.

### Lab — Router checklist

```python
"""Check a synthetic small-office router settings summary against a basic checklist (stdlib only)."""
settings = {"admin_password_changed": False, "wifi_security": "WPA2-Personal", "guest_network": True,
            "guest_isolated_from_lan": False, "remote_admin": True, "firmware_age_days": 540, "upnp": True}
checks = [("admin password changed from default", settings["admin_password_changed"]),
          ("Wi-Fi uses WPA2 or WPA3", settings["wifi_security"] in ("WPA2-Personal", "WPA3-Personal")),
          ("guest network enabled", settings["guest_network"]),
          ("guest isolated from business devices", settings["guest_isolated_from_lan"]),
          ("remote administration off", not settings["remote_admin"]),
          ("firmware updated within 180 days", settings["firmware_age_days"] <= 180),
          ("UPnP off", not settings["upnp"])]
for name, ok in checks: print(f"{'PASS' if ok else 'FIX '}  {name}")
print(f"{sum(ok for _, ok in checks)} of {len(checks)} pass")
```

Run with `python3 lab_router.py`. Verified output:

```text
FIX   admin password changed from default
PASS  Wi-Fi uses WPA2 or WPA3
PASS  guest network enabled
FIX   guest isolated from business devices
FIX   remote administration off
FIX   firmware updated within 180 days
FIX   UPnP off
2 of 7 pass
```

### 4.2 Reading the checklist

The synthetic settings pass only two of seven checks: Wi-Fi security and the existence of a guest network. The administrator password is still the default, the guest network is not isolated from business devices, remote administration is on, firmware is about eighteen months old and UPnP is on. Leo orders the fixes by value: change the administrator password first, because anyone who guesses it can change everything else; then isolate the guest network and turn off remote administration; then update firmware and turn off UPnP.

### 4.3 Making the changes

After closing, with Ellen present and approving each step, Leo changes the administrator password to a long passphrase that Ellen stores in a password manager. He turns on guest isolation and moves the smart speaker and scanner to the guest network. He turns off remote administration and UPnP. He updates the firmware using the router's built-in update function. After each change, he checks that tills, the card reader and the office computer still connect and that a test card payment works. He records every change with the original value.

### 4.4 Checking the result

Leo reruns the checklist against the new settings: seven of seven pass. He also tests guest isolation by connecting his own phone to the guest network and confirming it can reach the internet but not the office computer, with Ellen's permission and without trying anything beyond a simple connection check. The next morning, he calls Ellen to confirm opening went smoothly. Verifying results, not just making changes, is what shows the work actually achieved its goal. He saves the after-change checklist output with the date as evidence for the report.

### 4.5 Habits for the future

Leo leaves Ellen with a short list of habits: check the router's device list monthly; check for firmware updates every three months; change the guest Wi-Fi passphrase every few months and after staff leave; use a password manager and multi-factor authentication for email and the order platform; and call the internet provider or the payment company for problems with their equipment. These habits take little time but keep the improvements in place long after the course ends. He prints the list and pins it beside the office computer.

### 4.6 The short report

Leo's final report is two pages. It covers what he found, what was changed and why, the before and after checklist results, the remaining recommendations and the monthly habits. It uses plain language, avoids jargon and includes the record of changes. Nadia reviews it before Leo gives it to Ellen. A short, clear report lets Ellen understand her network, explain it to an adviser or insurer and pick up where Leo left off. Ellen keeps a printed copy with the router's documentation, and a digital copy in her cloud storage.

### 4.7 Reflection

Leo reflects that the biggest improvements came from simple steps: a changed password, guest isolation and turning off unneeded features. The most important skills were not technical: agreeing permission, working after hours, recording changes and stopping to ask about unknown devices. Nadia points out that these habits apply at any scale, from a bakery to a large organisation, and that the rest of the curriculum builds on exactly these foundations. He plans to take the technical course next, building on what he practised at the bakery.

### Worked example

The router passes two of seven checks before changes and seven of seven after; Ellen receives a two-page report and five habits.

> **Synthetic case.** Router settings are synthetic.

### Errors and limits

Making several router changes at once during opening hours risks stopping card payments with no clear cause.

### Exercises

- **EX039 — Initial checklist result.** How many checks pass before changes? *Rubric:* 3 = 2 of 7, Wi-Fi security and guest network exists;; 2 = two;; 1 = seven;; 0 = none.
- **EX040 — First fix.** Which fix comes first, and why? *Rubric:* 3 = admin password; controls everything else;; 2 = password;; 1 = firmware;; 0 = none.
- **EX041 — UPnP reason.** Why turn off UPnP? *Rubric:* 3 = lets devices open ports automatically;; 2 = ports;; 1 = speed;; 0 = none.
- **EX042 — Guest isolation test.** How is guest isolation tested? *Rubric:* 3 = phone on guest reaches internet not office PC, with permission;; 2 = test;; 1 = vague;; 0 = none.
- **EX043 — Password storage.** Where is the new router password stored? *Rubric:* 3 = Ellen's password manager;; 2 = manager;; 1 = note;; 0 = none.
- **EX044 — After-change test.** What is tested after each change? *Rubric:* 3 = tills, card reader, office PC and test payment;; 2 = payments;; 1 = vague;; 0 = none.
- **EX045 — Final checklist.** How many checks pass after changes? *Rubric:* 3 = 7 of 7;; 2 = all;; 1 = six;; 0 = none.
- **EX046 — Firmware habit.** How often should Ellen check for firmware updates? *Rubric:* 3 = every three months;; 2 = quarterly;; 1 = never;; 0 = none.
- **EX047 — Guest passphrase habit.** When should the guest passphrase change? *Rubric:* 3 = every few months and after staff leave;; 2 = periodically;; 1 = never;; 0 = none.
- **EX048 — Report contents.** List four parts of Leo's report. *Rubric:* 3 = findings, changes, before/after, recommendations or habits;; 2 = three;; 1 = fewer;; 0 = none.
- **EX049 — Morning check.** Why call Ellen the next morning? *Rubric:* 3 = confirm opening went smoothly;; 2 = verify;; 1 = courtesy;; 0 = none.
- **EX050 — Key reflection.** What did Leo find mattered most besides technical steps? *Rubric:* 3 = permission, timing, records, stopping to ask;; 2 = habits;; 1 = vague;; 0 = none.

### Synthesis

A simple checklist, careful agreed changes, verification and clear habits secure a small business network quickly.

### Continue studying — chapter 04 of 04

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Leo Hart, Nadia Petrov, Quayside Skills Centre, Bramble Street Bakery and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Card payments, online orders and the office computer's accounts.

**EX002.** Customer phones share a network with the tills and office computer.

**EX003.** Availability, so sales and payments keep working.

**EX004.** Most harm comes from automated and opportunistic attacks that basic controls stop.

**EX005.** How much harm it prevents, what it costs and whether it could disrupt the shop.

**EX006.** It prevents much harm at little cost and can be done after closing.

**EX007.** It is easily guessed and would give someone control of the router.

**EX008.** NIST SP 800-41r1.

**EX009.** NIST SP 800-153.

**EX010.** Knowing which devices you have.

**EX011.** Agreeing scope and permission with Ellen.

**EX012.** It connects to the internet, gives out addresses and provides Wi-Fi.

**EX013.** Online orders or the accounts being changed without permission.

**EX014.** It can disrupt the business and reveal private information.

**EX015.** The payment company owns and manages it under its own rules.

**EX016.** After closing, so sales and payments are not disrupted.

**EX017.** So they can be restored if something breaks.

**EX018.** So the cause of any problem is obvious.

**EX019.** In person or on paper, not by message.

**EX020.** Stop, write down what he saw and ask Ellen.

**EX021.** Date, what changed, original value and who approved it.

**EX022.** On the skills centre's secure storage, not his personal phone.

**EX023.** They are deleted as agreed.

**EX024.** Ellen contacts the provider rather than Leo changing it.

**EX025.** Checking whether a particular task is allowed.

**EX026.** That tills and card payments still work.

**EX027.** Two: bb:77 and cc:19.

**EX028.** A device's hardware address and the address it was given.

**EX029.** Customer phones have left, so remaining devices are easier to identify.

**EX030.** A staff smart speaker and a delivery company's scanner.

**EX031.** They are non-business devices sharing a network with the tills.

**EX032.** Online orders stop, and card payments may be limited.

**EX033.** From the reader directly to the payment provider, encrypted.

**EX034.** The office computer, the email account and the order platform login.

**EX035.** Once a month after closing.

**EX036.** So mistakes in the method do not affect the real check.

**EX037.** A mobile data backup for the card reader.

**EX038.** Deciding what may connect where requires knowing every device.

**EX039.** Two of seven.

**EX040.** Changing the administrator password, because it controls every other setting.

**EX041.** It lets devices open ports on the router automatically.

**EX042.** A phone on the guest network reaches the internet but not the office computer.

**EX043.** In Ellen's password manager.

**EX044.** That tills, card reader and office computer connect and a test payment works.

**EX045.** All seven.

**EX046.** Every three months.

**EX047.** Every few months and after staff leave.

**EX048.** Findings, changes made, before and after results and habits.

**EX049.** To confirm the shop opened without problems.

**EX050.** Agreeing permission, working after hours, recording changes and stopping to ask.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, code and data in this book are synthetic unless a sentence cites a public source.

- Axelsson, S. (2000). The base-rate fallacy and the difficulty of intrusion detection. *ACM Transactions on Information and System Security*, 3(3), 186–205. <https://doi.org/10.1145/357830.357849>
- Barker, E., Dang, Q., Frankel, S., Scarfone, K., & Wouters, P. (2020). *Guide to IPsec VPNs* (NIST SP 800-77 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-77r1>
- Center for Internet Security. (2021). *CIS Critical Security Controls v8*. <https://www.cisecurity.org/controls/v8>
- Chandramouli, R., & Rose, S. (2013). *Secure Domain Name System (DNS) deployment guide* (NIST SP 800-81-2). NIST. <https://doi.org/10.6028/NIST.SP.800-81-2>
- Claise, B., Trammell, B., & Aitken, P. (2013). *Specification of the IP Flow Information Export (IPFIX) protocol* (RFC 7011). IETF. <https://www.rfc-editor.org/rfc/rfc7011>
- Ferguson, P., & Senie, D. (2000). *Network ingress filtering* (RFC 2827, BCP 38). IETF. <https://www.rfc-editor.org/rfc/rfc2827>
- Gerhards, R. (2009). *The Syslog protocol* (RFC 5424). IETF. <https://www.rfc-editor.org/rfc/rfc5424>
- Joint Task Force. (2020). *Security and privacy controls for information systems and organizations* (NIST SP 800-53 Rev. 5). NIST. <https://doi.org/10.6028/NIST.SP.800-53r5>
- Kaufman, C., Hoffman, P., Nir, Y., Eronen, P., & Kivinen, T. (2014). *Internet Key Exchange Protocol Version 2 (IKEv2)* (RFC 7296). IETF. <https://www.rfc-editor.org/rfc/rfc7296>
- Kent, S., & Seo, K. (2005). *Security architecture for the Internet Protocol* (RFC 4301). IETF. <https://www.rfc-editor.org/rfc/rfc4301>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- Lepinski, M., & Kent, S. (2012). *An infrastructure to support secure Internet routing* (RFC 6480). IETF. <https://www.rfc-editor.org/rfc/rfc6480>
- McKay, K., & Cooper, D. (2019). *Guidelines for the selection, configuration, and use of Transport Layer Security (TLS) implementations* (NIST SP 800-52 Rev. 2). NIST. <https://doi.org/10.6028/NIST.SP.800-52r2>
- Paxson, V. (1999). Bro: A system for detecting network intruders in real-time. *Computer Networks*, 31(23–24), 2435–2463. <https://doi.org/10.1016/S1389-1286(99)00112-7>
- Rescorla, E. (2018). *The Transport Layer Security (TLS) protocol version 1.3* (RFC 8446). IETF. <https://www.rfc-editor.org/rfc/rfc8446>
- Rose, S., Borchert, O., Mitchell, S., & Connelly, S. (2020). *Zero trust architecture* (NIST SP 800-207). NIST. <https://doi.org/10.6028/NIST.SP.800-207>
- Saltzer, J. H., & Schroeder, M. D. (1975). The protection of information in computer systems. *Proceedings of the IEEE*, 63(9), 1278–1308. <https://doi.org/10.1109/PROC.1975.9939>
- Scarfone, K., & Hoffman, P. (2009). *Guidelines on firewalls and firewall policy* (NIST SP 800-41 Rev. 1). NIST. <https://doi.org/10.6028/NIST.SP.800-41r1>
- Scarfone, K., & Mell, P. (2007). *Guide to intrusion detection and prevention systems (IDPS)* (NIST SP 800-94). NIST. <https://doi.org/10.6028/NIST.SP.800-94>
- Sommer, R., & Paxson, V. (2010). Outside the closed world: On using machine learning for network intrusion detection. *2010 IEEE Symposium on Security and Privacy*, 305–316. <https://doi.org/10.1109/SP.2010.25>
- Souppaya, M., & Scarfone, K. (2012). *Guidelines for securing wireless local area networks (WLANs)* (NIST SP 800-153). NIST. <https://doi.org/10.6028/NIST.SP.800-153>
- Sriram, K., & Montgomery, D. (2019). *Resilient interdomain traffic exchange: BGP security and DDoS mitigation* (NIST SP 800-189). NIST. <https://doi.org/10.6028/NIST.SP.800-189>
- Wool, A. (2004). A quantitative study of firewall configuration errors. *Computer*, 37(6), 62–67. <https://doi.org/10.1109/MC.2004.2>
