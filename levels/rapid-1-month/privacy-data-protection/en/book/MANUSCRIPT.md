# Privacy and Data Protection: Rapid Course

- Language: English (`en`); course 004, Rapid course (1 month).
- Editorial state: **draft**. Chapters 1–4 of 4 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; one offline lab uses only the Python 3 standard library on synthetic data, and its output is embedded from a real run. Independent review and the 300-page A4 verification remain open.
- Audience: beginners who need a fast, practical start in privacy and data protection for a small business.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the lab compares fields a synthetic pharmacy loyalty app collects with the fields its stated purposes need. Legal analysis is teaching, not legal advice. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The four chapters follow one pharmacy assistant through a one-month course: foundations and first decisions, scope and safe practice, systems, data and vendors, and a guided lab that becomes a short action plan. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Sofia Mendes** | Rapid course student, pharmacy assistant | Invented |
| **Mr. Raj Patel** | Mentor, data protection officer | Invented |
| **Brightwater Community Learning Centre** | Fictional learning centre | Invented |
| **Juniper Pharmacy** | Fictional pharmacy, 3 shops, about 9,000 regular customers, loyalty app | Invented |

### Core sources

Regulation (EU) 2016/679 (GDPR) Articles 4(1), 5, 9 and 28; Lei 13.709/2018 (LGPD) Articles 5 and 6; NIST [Privacy Framework 1.0](https://doi.org/10.6028/NIST.CSWP.10); ISO/IEC 29100:2011. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Privacy and data protection: foundations and decisions

### Learning outcomes

You will (1) define personal data and special category data; (2) name the GDPR and LGPD principles; (3) make a first, reasoned privacy decision in a small business.

### 1.1 The course and the case

Sofia Mendes, a pharmacy assistant, joins a one-month rapid course at the fictional Brightwater Community Learning Centre. Her mentor, Mr. Raj Patel, works as a data protection officer for several small businesses. Sofia's workplace is the fictional Juniper Pharmacy, a family business with three shops, about 9,000 regular customers, a prescription service and a new loyalty app. Pharmacies handle information about medicines, which can reveal illnesses, so even a small business carries serious privacy responsibilities from its first customer interaction. Sofia starts with her own shop.

### 1.2 What counts as personal data

Mr. Patel explains that personal data means any information relating to an identified or identifiable living person, under Article 4(1) of the GDPR; the LGPD in Brazil uses a similar definition in Article 5. A customer's name and phone number are personal data, but so is a loyalty number, because Juniper can link it to a person. Sofia lists examples from her shop: prescriptions, loyalty points, CCTV images at the counter, delivery addresses and notes about a customer's preferred pharmacist. Identifiability, not names, is the test.

### 1.3 Special categories

Some data receive extra protection. Article 9 of the GDPR lists special categories, including data concerning health, and the LGPD calls them sensitive personal data in Article 5(II). A prescription for insulin reveals diabetes; a purchase of pregnancy tests may hint at a pregnancy. Sofia realises that the loyalty app's purchase history could therefore contain health information even though it was designed for points and vouchers, not care. Processing such data needs a specific condition, not just an ordinary lawful basis. Pharmacies meet these daily.

### 1.4 The principles

Mr. Patel gives Sofia a one-page summary of the principles in Article 5 of the GDPR: lawfulness, fairness and transparency; purpose limitation; data minimisation; accuracy; storage limitation; integrity and confidentiality; and accountability. The LGPD lists comparable principles in Article 6, including necessity and non-discrimination. For each principle, Sofia writes one sentence about Juniper. For minimisation she writes: the loyalty app should collect only what points and vouchers need. These sentences become her checklist for every later decision. Each sentence names one Juniper system, such as the loyalty app or CCTV.

### 1.5 A first decision

The owner asks Sofia whether staff may post a photo of the busy shop on social media, with customers visible at the counter. Sofia applies her checklist. The purpose is promotion, customers did not expect to appear online, and a pharmacy counter suggests health needs. She recommends taking photos only when no customers are present or with clear permission. Mr. Patel praises the reasoning: she identified the purpose, considered expectations and chose a simple alternative that still meets the business goal. The owner agrees.

### Worked example

Sofia defines personal and special category data with pharmacy examples, writes one sentence per principle for Juniper and advises against posting counter photos showing customers.

> **Synthetic case.** Brightwater, Juniper and all people are synthetic; GDPR Articles 4(1), 5 and 9 and LGPD Articles 5 and 6 are real.

### Errors and limits

Definitions are broad; when unsure whether data are personal, treat them as personal.

### Exercises

- **EX001 — Loyalty number.** Is a loyalty number personal data? *Rubric:* 3 = yes, it can be linked to a person;; 2 = yes;; 1 = no;; 0 = none.
- **EX002 — Insulin.** What can an insulin prescription reveal? *Rubric:* 3 = a health condition such as diabetes;; 2 = mentions health;; 1 = vague;; 0 = none.
- **EX003 — LGPD term.** What does the LGPD call special category data? *Rubric:* 3 = sensitive personal data;; 2 = correct;; 1 = other;; 0 = none.
- **EX004 — Purchase history.** Why might loyalty purchase history be health data? *Rubric:* 3 = purchases can reveal illnesses or conditions;; 2 = mentions health;; 1 = vague;; 0 = none.
- **EX005 — Count principles.** How many principles are in GDPR Article 5? *Rubric:* 3 = seven;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX006 — Necessity.** Which LGPD principle resembles minimisation? *Rubric:* 3 = necessity;; 2 = correct;; 1 = other;; 0 = none.
- **EX007 — Minimisation sentence.** What did Sofia write for minimisation? *Rubric:* 3 = the app should collect only what points and vouchers need;; 2 = mentions need;; 1 = vague;; 0 = none.
- **EX008 — Counter photo.** What did Sofia recommend for shop photos? *Rubric:* 3 = no customers visible or clear permission;; 2 = mentions permission;; 1 = allow;; 0 = none.
- **EX009 — Photo purpose.** What purpose did the counter photo serve? *Rubric:* 3 = promotion;; 2 = correct;; 1 = vague;; 0 = none.
- **EX010 — Expectation.** Did customers expect to appear online? *Rubric:* 3 = no;; 2 = correct;; 1 = yes;; 0 = none.
- **EX011 — Living persons.** Does the GDPR definition cover deceased people? *Rubric:* 3 = no, living persons;; 2 = correct;; 1 = yes;; 0 = none.
- **EX012 — Extra condition.** What does processing health data need beyond a lawful basis? *Rubric:* 3 = a specific Article 9 condition;; 2 = mentions condition;; 1 = vague;; 0 = none.
- **EX013 — Checklist use.** How will Sofia use her principle sentences? *Rubric:* 3 = as a checklist for later decisions;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-02"></a>

## Chapter 2 — Scope, permission and safe practice

### Learning outcomes

You will (1) work within agreed permission when reviewing privacy; (2) handle customer data safely during a review; (3) report problems through the right channel.

### 2.1 Agreeing the scope

Before Sofia reviews anything at Juniper, Mr. Patel asks her to agree a written scope with the owner. It lists what she may look at: the loyalty app settings, the privacy notice, the paper prescription filing, staff access to the dispensing system and the shop's CCTV signs. It excludes reading individual customer records, contacting customers and changing settings. The owner signs it. Mr. Patel explains that a scope protects customers, the business and Sofia, because it sets clear limits before curiosity or pressure can push them.

### 2.2 Safe handling during review

Sofia uses screenshots of settings, not customer screens. When she needs examples of records, she asks the pharmacist to create a test customer in the dispensing system with an invented name. She keeps her notes in a locked drawer and in an encrypted folder on the shop computer, not on her personal phone. Mr. Patel reminds her that a review can itself create a privacy risk if notes and screenshots spread, so the review must follow the same care it recommends. Notes are destroyed afterwards.

### 2.3 When asked to go further

A colleague asks Sofia to check whether a neighbour has collected a prescription. Sofia declines, explains that looking up a person without a work reason is a misuse of access, and records the request in her review log. Later, the owner asks her to look at the delivery driver's phone to see whether customer addresses are stored. Because this is outside the scope, she asks the owner to add it in writing first, and the owner agrees after speaking with the driver.

### 2.4 Reporting problems

During her review, Sofia finds a box of old prescription copies in an unlocked storeroom. She does not move or read them. She reports the finding to the owner and Mr. Patel the same day, with the location, time and what she saw. The owner locks the room and arranges secure shredding of copies past the retention period. Mr. Patel explains that quick, factual reporting allows the business to judge whether a breach occurred and whether notification is needed. Mr. Patel records the event.

### 2.5 Respecting staff

Sofia's review also touches on staff, such as their access to the dispensing system and CCTV images of the counter. She explains to her colleagues what she is checking and why, and she avoids recording opinions about individuals. Staff are data subjects too, with rights under the GDPR and LGPD. Mr. Patel notes that reviews go better when staff understand that the aim is to improve processes and protect customers, not to catch people out, and that openness encourages them to mention problems.

### Worked example

Sofia agrees a signed scope, uses a test customer and encrypted notes, declines a neighbour lookup, gets the delivery phone added in writing, reports unlocked prescription copies and explains her review to staff.

> **Synthetic case.** The scope and events are synthetic.

### Errors and limits

Verbal permission is easily disputed; get scope changes in writing.

### Exercises

- **EX014 — Scope exclusions.** Name two things excluded from Sofia's scope. *Rubric:* 3 = reading customer records, contacting customers, changing settings;; 2 = two;; 1 = one;; 0 = none.
- **EX015 — Test customer.** Why did Sofia use a test customer? *Rubric:* 3 = to avoid viewing real customer records;; 2 = mentions real data;; 1 = vague;; 0 = none.
- **EX016 — Note storage.** Where does Sofia keep her notes? *Rubric:* 3 = locked drawer and encrypted folder;; 2 = both;; 1 = phone;; 0 = none.
- **EX017 — Neighbour lookup.** Why did Sofia refuse the neighbour lookup? *Rubric:* 3 = no work reason; misuse of access;; 2 = mentions misuse;; 1 = vague;; 0 = none.
- **EX018 — Driver phone.** How was the driver's phone added to the review? *Rubric:* 3 = owner added it in writing after speaking with the driver;; 2 = mentions writing;; 1 = vague;; 0 = none.
- **EX019 — Storeroom find.** What did Sofia find in the storeroom? *Rubric:* 3 = old prescription copies unlocked;; 2 = correct;; 1 = vague;; 0 = none.
- **EX020 — Not touching.** Why did Sofia not move or read the copies? *Rubric:* 3 = to avoid further exposure and stay within scope;; 2 = mentions scope;; 1 = vague;; 0 = none.
- **EX021 — Report content.** What did her report include? *Rubric:* 3 = location, time and what she saw;; 2 = most;; 1 = one;; 0 = none.
- **EX022 — Owner response.** What did the owner do about the storeroom? *Rubric:* 3 = locked it and arranged shredding of expired copies;; 2 = both;; 1 = one;; 0 = none.
- **EX023 — Quick reporting.** Why does quick reporting matter? *Rubric:* 3 = to judge breach and notification;; 2 = mentions notification;; 1 = vague;; 0 = none.
- **EX024 — Staff as subjects.** Are staff data subjects too? *Rubric:* 3 = yes;; 2 = correct;; 1 = no;; 0 = none.
- **EX025 — Review risk.** How can a review itself create risk? *Rubric:* 3 = notes and screenshots can spread;; 2 = mentions notes;; 1 = vague;; 0 = none.
- **EX026 — Openness.** What encourages staff to mention problems? *Rubric:* 3 = understanding the aim is improvement, not blame;; 2 = mentions aim;; 1 = vague;; 0 = none.

<a id="ch-03"></a>

## Chapter 3 — Privacy and data protection: systems, data and dependencies

### Learning outcomes

You will (1) map Juniper's systems and data flows; (2) identify vendors and dependencies; (3) note lawful bases and retention.

### 3.1 Mapping the systems

Sofia draws Juniper's systems on one page: the dispensing system that holds prescriptions and medication histories, the till that records sales, the loyalty app run by a vendor, the email newsletter tool, the CCTV recorder, the delivery service and paper prescription files. For each box she writes the main data it holds. The drawing shows that the loyalty app receives purchase data from the till each night, a flow the owner had not realised included medicine purchases. The drawing takes one afternoon to complete.

### 3.2 Following the flows

Sofia traces where data go next. Prescriptions arrive electronically from doctors' surgeries and on paper. The dispensing system sends claims to the health service for payment. The delivery service receives names, addresses and a sealed bag description. The newsletter tool receives emails of customers who joined the mailing list. The loyalty vendor receives every till item, including pain relief and pregnancy tests. She marks each flow with an arrow, its contents and whether customers would expect it. Two flows surprise the owner.

### 3.3 Vendors and dependencies

Juniper relies on four vendors: the dispensing system supplier, the loyalty app company, the newsletter tool and the delivery firm. Each processes customer data for Juniper and needs a contract that meets Article 28 of the GDPR, setting out instructions, confidentiality, security and deletion. Sofia finds contracts for the dispensing supplier and newsletter tool, but the loyalty and delivery contracts are standard terms that do not mention data protection. She flags both as gaps for the owner and Mr. Patel. Mr. Patel drafts the missing clauses.

### 3.4 Lawful bases

With Mr. Patel, Sofia notes the lawful basis for each purpose. Dispensing relies on providing health care, with Article 9(2)(h) as the condition for health data. Keeping prescription records relies on legal obligations for pharmacies. The newsletter relies on consent. The loyalty scheme relies on contract with members, but using medicine purchases for personalised offers would need explicit consent because it uses health data. Mr. Patel explains that each purpose needs its own basis, chosen before processing starts. Sofia records each basis in a table.

### 3.5 Retention

Sofia asks how long each type of data is kept. Prescription records follow professional rules set for pharmacies. CCTV is overwritten after thirty days. Loyalty data have no limit, and delivery records are kept in the driver's phone indefinitely. She recommends that the owner set retention periods for loyalty data, delivery records and newsletter subscribers who never open emails, and record them in a simple schedule. Storage limitation, she notes, reduces both legal risk and the damage any breach could cause. The owner approves.

### Worked example

Sofia maps seven systems, traces flows including medicine purchases to the loyalty vendor, finds two vendor contracts without data protection terms, notes lawful bases and recommends retention periods.

> **Synthetic case.** Systems are synthetic; GDPR Articles 9(2)(h) and 28 are real.

### Errors and limits

A map drawn once becomes outdated; update it when systems change.

### Exercises

- **EX027 — Hidden flow.** Which flow had the owner not realised? *Rubric:* 3 = till sends medicine purchases to the loyalty app;; 2 = mentions loyalty;; 1 = vague;; 0 = none.
- **EX028 — Delivery data.** What does the delivery service receive? *Rubric:* 3 = names, addresses and bag description;; 2 = most;; 1 = one;; 0 = none.
- **EX029 — Vendor count.** How many vendors does Juniper rely on? *Rubric:* 3 = four;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX030 — Contract gaps.** Which contracts lacked data protection terms? *Rubric:* 3 = loyalty and delivery;; 2 = both;; 1 = one;; 0 = none.
- **EX031 — Article 28.** What must processor contracts cover? *Rubric:* 3 = instructions, confidentiality, security, deletion;; 2 = most;; 1 = one;; 0 = none.
- **EX032 — Dispensing condition.** Which condition covers dispensing health data? *Rubric:* 3 = Article 9(2)(h);; 2 = correct;; 1 = consent;; 0 = none.
- **EX033 — Personalised offers.** What would personalised offers from medicine purchases need? *Rubric:* 3 = explicit consent;; 2 = correct;; 1 = contract;; 0 = none.
- **EX034 — CCTV retention.** How long is CCTV kept? *Rubric:* 3 = thirty days;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX035 — Unlimited data.** Which data had no retention limit? *Rubric:* 3 = loyalty data and delivery records;; 2 = both;; 1 = one;; 0 = none.
- **EX036 — Retention benefit.** Why does storage limitation reduce breach damage? *Rubric:* 3 = less data held means less exposed;; 2 = mentions less data;; 1 = vague;; 0 = none.
- **EX037 — Basis timing.** When should a lawful basis be chosen? *Rubric:* 3 = before processing starts;; 2 = correct;; 1 = after;; 0 = none.
- **EX038 — Expectation marks.** What did Sofia mark on each flow besides contents? *Rubric:* 3 = whether customers would expect it;; 2 = correct;; 1 = vague;; 0 = none.

<a id="ch-04"></a>

## Chapter 4 — Privacy and data protection: guided lab and applied synthesis

### Learning outcomes

You will (1) run a guided minimisation lab; (2) combine findings into a short plan; (3) present recommendations to a business owner.

### 4.1 The guided lab

Mr. Patel guides Sofia through a lab using the loyalty app's synthetic sign-up form and the purposes Juniper states in its notice: earning and spending points, a birthday voucher and marketing emails for those who agree. The lab compares each field collected with the fields each purpose needs. It shows that the app collects ten fields and five of them, 50%, are not needed for any stated purpose: phone, postcode, prescription items, gender and a location trail recorded by the app in the background.

### 4.2 Interpreting the lab

Sofia considers each unneeded field. Prescription items are health data with no stated purpose in the scheme. The location trail tracks customers' movements, which is intrusive and unexpected. Gender, postcode and phone may have been added by the vendor's default template. Mr. Patel reminds her that collecting data for no stated purpose breaks the minimisation principle and the purpose limitation principle, and that health data in a loyalty scheme also lacks the Article 9 condition it would need. None of the five fields serves a stated purpose.

### 4.3 A short plan

Sofia combines her findings from the month into a one-page plan with five actions: remove the five unneeded fields and stop the till sending medicine items to the loyalty vendor; sign data protection contracts with the loyalty and delivery firms; set retention periods for loyalty, delivery and newsletter data; replace counter photos with customer-free images; and keep the storeroom locked with a shredding routine. Each action has an owner, a cost estimate and a target date within three months. The plan fits on one page.

### 4.4 Presenting to the owner

Sofia presents the plan to Juniper's owner in fifteen minutes. She starts with the most serious issue, medicine purchases reaching the loyalty vendor, and explains it in plain words: customers' health purchases are being shared with an app company without a reason or their knowledge. The owner asks whether removing fields will reduce the app's value. Sofia shows that points and vouchers work with the remaining fields. The owner approves all five actions and asks the vendor to make the changes. She answers calmly.

### 4.5 Checking and next steps

Two weeks later, Sofia and Mr. Patel check the loyalty app with a new synthetic sign-up. The form now asks for five fields, and the till export contains no medicine items, only total spend and non-medicine categories. The contracts are in negotiation. Mr. Patel explains that checking after a change confirms that the plan worked rather than assuming it did. Sofia plans her next course step, governance, risk and compliance, to learn how businesses keep such improvements in place over time. The course ends.

### Lab — Loyalty app fields versus stated purposes

```python
"""Compare fields collected by a synthetic pharmacy loyalty app with fields its purposes need (stdlib only)."""
collected = ["name", "email", "phone", "date_of_birth", "postcode", "purchase_history",
             "prescription_items", "gender", "location_trail", "marketing_choice"]
needs = {
    "earn and spend points": {"name", "email", "purchase_history"},
    "birthday voucher": {"email", "date_of_birth"},
    "marketing emails": {"email", "marketing_choice"},
}
used = set().union(*needs.values())
unneeded = [f for f in collected if f not in used]
for f in collected:
    print(f"{f:20s} {'needed' if f in used else 'NOT NEEDED'}")
print(f"fields collected {len(collected)}; not needed for any stated purpose {len(unneeded)} ({100*len(unneeded)/len(collected):.0f}%)")
```

Run with `python3 lab_loyalty.py`. Verified output:

```text
name                 needed
email                needed
phone                NOT NEEDED
date_of_birth        needed
postcode             NOT NEEDED
purchase_history     needed
prescription_items   NOT NEEDED
gender               NOT NEEDED
location_trail       NOT NEEDED
marketing_choice     needed
fields collected 10; not needed for any stated purpose 5 (50%)
```

### Worked example

Sofia finds five of ten loyalty fields (50%) unneeded, including prescription items and a location trail, combines the month's findings into a five-action plan, gains the owner's approval and confirms the app changes.

> **Synthetic case.** The app is synthetic; GDPR Articles 5 and 9 are real.

### Errors and limits

Purposes listed in a notice may be incomplete; ask the business whether any other purpose exists before deleting fields.

### Exercises

- **EX039 — Unneeded share.** What share of loyalty fields were unneeded? *Rubric:* 3 = 5 of 10, 50%;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX040 — Location trail.** Why is the location trail a concern? *Rubric:* 3 = intrusive and unexpected tracking;; 2 = mentions tracking;; 1 = vague;; 0 = none.
- **EX041 — Vendor defaults.** Where might gender, postcode and phone have come from? *Rubric:* 3 = the vendor's default template;; 2 = correct;; 1 = vague;; 0 = none.
- **EX042 — Principles broken.** Which two principles does unneeded collection break? *Rubric:* 3 = minimisation and purpose limitation;; 2 = both;; 1 = one;; 0 = none.
- **EX043 — Plan actions.** How many actions does Sofia's plan contain? *Rubric:* 3 = five;; 2 = correct;; 1 = wrong;; 0 = none.
- **EX044 — Plan details.** What does each action have? *Rubric:* 3 = owner, cost estimate, target date;; 2 = most;; 1 = one;; 0 = none.
- **EX045 — Lead issue.** Which issue did Sofia present first? *Rubric:* 3 = medicine purchases reaching the loyalty vendor;; 2 = correct;; 1 = other;; 0 = none.
- **EX046 — Owner concern.** What did the owner worry about? *Rubric:* 3 = removing fields reducing app value;; 2 = correct;; 1 = vague;; 0 = none.
- **EX047 — Remaining fields.** How many fields does the form ask for after the change? *Rubric:* 3 = five;; 2 = correct;; 1 = ten;; 0 = none.
- **EX048 — Till export.** What does the till export contain now? *Rubric:* 3 = total spend and non-medicine categories;; 2 = correct;; 1 = medicines;; 0 = none.
- **EX049 — Post-change check.** Why check after a change? *Rubric:* 3 = to confirm the plan worked;; 2 = mentions confirmation;; 1 = vague;; 0 = none.
- **EX050 — Next study.** What does Sofia plan to study next? *Rubric:* 3 = governance, risk and compliance;; 2 = correct;; 1 = vague;; 0 = none.

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Sofia Mendes, Mr. Raj Patel, Brightwater Community Learning Centre, Juniper Pharmacy and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Yes, because Juniper can link it to an identifiable customer.

**EX002.** That the customer probably has diabetes, a health condition.

**EX003.** Sensitive personal data.

**EX004.** Purchases such as tests or medicines can reveal health conditions.

**EX005.** Seven.

**EX006.** Necessity.

**EX007.** The loyalty app should collect only what points and vouchers need.

**EX008.** Take photos without customers present or with clear permission.

**EX009.** Promotion on social media.

**EX010.** No, they did not expect it.

**EX011.** No, it covers living persons.

**EX012.** A specific condition under Article 9.

**EX013.** As a checklist for every later decision.

**EX014.** Reading individual customer records and changing settings.

**EX015.** So she could see how records work without viewing real customers.

**EX016.** In a locked drawer and an encrypted folder on the shop computer.

**EX017.** Looking someone up without a work reason misuses access.

**EX018.** The owner added it to the scope in writing after speaking with the driver.

**EX019.** Old prescription copies in an unlocked room.

**EX020.** Handling them was outside her scope and could cause further exposure.

**EX021.** The location, time and what she saw.

**EX022.** Locked the room and arranged secure shredding of expired copies.

**EX023.** So the business can decide whether a breach occurred and must be notified.

**EX024.** Yes, staff have rights under the GDPR and LGPD.

**EX025.** Its notes and screenshots can spread personal data.

**EX026.** Knowing the review aims to improve processes, not catch people out.

**EX027.** The till sending medicine purchases to the loyalty app each night.

**EX028.** Names, addresses and a sealed bag description.

**EX029.** Four.

**EX030.** The loyalty app and delivery contracts.

**EX031.** Instructions, confidentiality, security and deletion.

**EX032.** Article 9(2)(h), the provision of health care.

**EX033.** Explicit consent, because they use health data.

**EX034.** Thirty days, then overwritten.

**EX035.** Loyalty data and delivery records on the driver's phone.

**EX036.** Less data held means less can be exposed.

**EX037.** Before processing starts.

**EX038.** Whether customers would expect the flow.

**EX039.** Five of ten (50%).

**EX040.** It tracks customers' movements in an intrusive, unexpected way.

**EX041.** The vendor's default sign-up template.

**EX042.** Data minimisation and purpose limitation.

**EX043.** Five.

**EX044.** An owner, a cost estimate and a target date.

**EX045.** Medicine purchases being sent to the loyalty vendor.

**EX046.** That removing fields would reduce the app's value.

**EX047.** Five fields.

**EX048.** Total spend and non-medicine categories only.

**EX049.** To confirm the plan worked rather than assume it.

**EX050.** Governance, risk and compliance.

<a id="references"></a>

## References

Every DOI was resolved through doi.org on 12 October 2026; laws and guidelines link to their official publishers. Re-verify editions before citing. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- ISO/IEC. (2011). *ISO/IEC 29100:2011 Information technology — Security techniques — Privacy framework*. <https://www.iso.org/standard/45123.html>
- National Institute of Standards and Technology. (2020). *NIST Privacy Framework: A tool for improving privacy through enterprise risk management, Version 1.0* (NIST CSWP 10). <https://doi.org/10.6028/NIST.CSWP.10>
- Article 29 Data Protection Working Party. (2017). *Guidelines on Data Protection Impact Assessment (DPIA) and determining whether processing is "likely to result in a high risk" for the purposes of Regulation 2016/679* (WP248 rev.01, as last revised 4 October 2017; endorsed by the EDPB). <https://ec.europa.eu/newsroom/article29/items/611236>
- European Data Protection Board. (2020). *Guidelines 05/2020 on consent under Regulation 2016/679* (Version 1.1, adopted 4 May 2020). <https://www.edpb.europa.eu/documents/guideline/guidelines-052020-on-consent-under-regulation-2016679_en>
