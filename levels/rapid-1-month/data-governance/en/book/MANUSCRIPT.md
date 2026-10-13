# Data Governance: Rapid Course

- Language: English (`en`); course 003, Rapid course (1 month).
- Editorial state: **draft**. Chapters 1–4 of 4 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; one offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: beginners who need a fast, practical start in data governance for a small business.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the lab checks a twelve-row synthetic café sign-up list for blank emails, malformed addresses, duplicates and consent ticks. Law is cited by edition and paraphrased; nothing here is legal advice. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The four chapters follow one shift supervisor through a one-month course: foundations and first decisions, ownership and safe practice, quality, systems and suppliers, and a guided lab that becomes a short action plan. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Kwame Boateng** | Rapid course student, café shift supervisor | Invented |
| **Ms. Lena Fischer** | Mentor, council data manager | Invented |
| **Riverside Adult Learning Centre** | Fictional learning centre | Invented |
| **Copperleaf Café** | Fictional business, two cafés and twelve staff | Invented |

### Core sources

GDPR. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Data governance: foundations and first decisions

### Learning outcomes

You will (1) explain data governance in plain words; (2) list the data a small café holds; (3) make three first decisions about responsibility and rules.

### 1.1 The learner and the café

Kwame Boateng works as a shift supervisor at Copperleaf Café, a fictional business with two cafés, twelve staff and a newsletter for regular customers. The owner, Mrs. Adeyemi, asks him to sort out how the café looks after its data. He joins a one-month rapid course at the fictional Riverside Adult Learning Centre, guided by mentor Ms. Lena Fischer, who works as a data manager for a local council. Every exercise uses synthetic data invented for teaching, never real customer details.

### 1.2 What data governance means

Ms. Fischer explains data governance in one sentence: agreeing who is responsible for each kind of data, what rules it must follow and how everyone checks that the rules work. Kwame notes that this is about decisions and habits, not expensive software. A small café can govern its data with a short list of owners, a page of rules and a few regular checks. The aim is data that are accurate enough to use, safe and kept only as long as needed.

### 1.3 Copperleaf's data

Kwame lists Copperleaf's data: the newsletter sign-up sheet with customer emails, staff names, contact numbers and rotas, supplier contacts and invoices, card payment reports from the till provider, allergy notes for a few regular customers and photos from a recent event. He marks which contain personal data about identifiable people. Most do. He notes that allergy notes are health information, which the GDPR treats as special category data needing extra care. He writes each item on a list with where it is kept, so nothing is forgotten later.

### 1.4 Why it matters

Ms. Fischer asks Kwame what could go wrong. He lists: emailing customers who never agreed, losing the allergy notes and serving the wrong food, sharing staff phone numbers with the wrong person, keeping old rotas forever and paying a supplier twice because two invoice copies exist. Each problem affects customers, staff or money. He sees that governance protects people and the business at the same time, and that small businesses face the same kinds of risk as large ones. Mrs. Adeyemi agrees.

### 1.5 Three first decisions

Ms. Fischer asks Kwame to make three decisions this week. First, Mrs. Adeyemi is accountable for all data, and Kwame looks after it day to day. Second, each kind of data gets a named person: Kwame for the newsletter and allergy notes, the assistant manager for rotas and Mrs. Adeyemi for supplier and payment records. Third, no customer or staff data leave the café's approved systems. Mrs. Adeyemi agrees all three, and Kwame writes them on one page. Staff are told that week.

### Worked example

Kwame defines governance as responsibility, rules and checks, lists Copperleaf's data including allergy notes as health information, identifies risks to people and money and records three first decisions approved by Mrs. Adeyemi.

> **Synthetic case.** Copperleaf, Riverside and all people are synthetic; the GDPR is real.

### Errors and limits

Thinking governance needs expensive tools delays simple decisions that help immediately.

### Exercises

- **EX001 — Café size.** How many cafés does Copperleaf run? *Rubric:* 3 = two;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX002 — Mentor job.** What is Ms. Fischer's job? *Rubric:* 3 = data manager for a local council;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX003 — One-sentence definition.** How does Ms. Fischer define governance? *Rubric:* 3 = who is responsible, what rules, how rules are checked;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX004 — Software need.** Does a small café need expensive software to govern data? *Rubric:* 3 = no;; 2 = partly correct;; 1 = yes;; 0 = none.
- **EX005 — Allergy status.** Why do allergy notes need extra care? *Rubric:* 3 = they are health information, special category data;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX006 — Staff data example.** Name one kind of staff data Copperleaf holds. *Rubric:* 3 = names, contact numbers or rotas;; 2 = one;; 1 = vague;; 0 = none.
- **EX007 — Supplier risk.** What money risk did Kwame list? *Rubric:* 3 = paying a supplier twice from duplicate invoices;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX008 — Allergy risk.** What could losing allergy notes cause? *Rubric:* 3 = serving the wrong food;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX009 — Accountable person.** Who is accountable for all Copperleaf data? *Rubric:* 3 = Mrs. Adeyemi;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX010 — Newsletter person.** Who looks after the newsletter list? *Rubric:* 3 = Kwame;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX011 — Rota person.** Who looks after rotas? *Rubric:* 3 = the assistant manager;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX012 — Approved systems rule.** What is the third decision? *Rubric:* 3 = no customer or staff data leave approved systems;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX013 — Decision record.** Where are the three decisions written? *Rubric:* 3 = on one page;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-02"></a>

## Chapter 2 — Ownership, rules and safe practice

### Learning outcomes

You will (1) write simple rules for each kind of data; (2) apply basic security habits; (3) decide how long to keep records.

### 2.1 Simple rules

Kwame writes a page of rules with Ms. Fischer's help. Newsletter emails are used only for the newsletter. Allergy notes are kept in a locked folder behind the counter and shown only to staff preparing that customer's order. Rotas are shared through the staff messaging group the café pays for, not personal social media. Invoices are filed by supplier and date in one shared folder. Each rule names the person responsible, so staff know whom to ask. The page fits on one side.

### 2.2 Asking only for what is needed

The old sign-up sheet asked for name, email, phone, birthday and home address. Kwame asks why. Mrs. Adeyemi says only the email is needed for the newsletter, and a first name makes emails friendlier. Kwame removes phone, birthday and address from the new sheet. Ms. Fischer explains that collecting less data means less to protect, less to lose and fewer questions from customers about why the café wants their details. The new sheet is quicker to fill in, and Kwame notices that more customers sign up in the first week than before.

### 2.3 Security habits

Kwame lists habits for staff: lock the till computer screen when stepping away, use separate logins for the till system rather than one shared code, keep the sign-up sheet out of customers' reach, never photograph customer details on personal phones and report lost papers or devices to Kwame the same day. He explains each habit at the next staff meeting with a real example of what could happen, such as a customer reading the sign-up sheet on the counter. Staff agree readily.

### 2.4 Keeping and deleting

Kwame sets keeping periods. Newsletter emails are kept while the customer stays subscribed and deleted soon after they unsubscribe. Old rotas are kept for the period employment rules require, then deleted. Invoices are kept for the period tax rules require. Allergy notes are reviewed every six months with the customer. Photos from events are deleted after a year unless people agreed to longer use. He writes each period beside the matching rule. Mrs. Adeyemi checks the tax and employment periods with her accountant.

### 2.5 Getting agreement

Kwame shows the rules to Mrs. Adeyemi and the assistant manager. The assistant manager asks whether staff may still swap shifts by text. They agree that shift swaps go through the paid messaging group, which keeps numbers private. Mrs. Adeyemi signs the page and asks Kwame to pin it in the staff room. Ms. Fischer reminds him that rules work when people understand them, so he should explain changes rather than just announce them. Kwame explains each change at the next staff meeting.

### Worked example

Kwame writes rules naming who is responsible, cuts the sign-up sheet to first name and email, lists security habits explained with examples, sets keeping periods and gets the rules signed and pinned in the staff room.

> **Synthetic case.** Rules are synthetic.

### Errors and limits

Copying a large company's long policy into a café produces rules nobody reads.

### Exercises

- **EX014 — Newsletter use.** What may newsletter emails be used for? *Rubric:* 3 = only the newsletter;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX015 — Allergy access.** Who may see allergy notes? *Rubric:* 3 = staff preparing that customer's order;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX016 — Rota channel.** How are rotas shared? *Rubric:* 3 = the paid staff messaging group;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX017 — Kept sign-up fields.** Which fields stay on the new sign-up sheet? *Rubric:* 3 = first name and email;; 2 = both;; 1 = one;; 0 = none.
- **EX018 — Collect-less benefit.** Why collect less data? *Rubric:* 3 = less to protect, lose or explain;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX019 — Till login habit.** What replaces the shared till code? *Rubric:* 3 = separate logins;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX020 — Loss reporting.** When should lost papers be reported? *Rubric:* 3 = the same day;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX021 — Unsubscribe action.** What happens to emails after unsubscribing? *Rubric:* 3 = deleted soon after;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX022 — Allergy review.** How often are allergy notes reviewed? *Rubric:* 3 = every six months;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX023 — Photo period.** How long are event photos kept by default? *Rubric:* 3 = one year;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX024 — Shift swap answer.** How do staff swap shifts now? *Rubric:* 3 = through the paid messaging group;; 2 = partly correct;; 1 = text;; 0 = none.
- **EX025 — Rules location.** Where are the signed rules displayed? *Rubric:* 3 = the staff room;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX026 — Explaining changes.** What does Ms. Fischer say makes rules work? *Rubric:* 3 = people understanding them;; 2 = partly correct;; 1 = vague;; 0 = none.

<a id="ch-03"></a>

## Chapter 3 — Quality, systems and suppliers

### Learning outcomes

You will (1) check data quality in a small business; (2) map where data are stored; (3) check suppliers who handle the café's data.

### 3.1 Quality in plain words

Ms. Fischer explains quality with three questions: is the data complete, is it valid and is it accurate? For the newsletter list, complete means every row has an email, valid means each email looks like a real address and accurate means it belongs to the person who signed up. Kwame adds a fourth question for duplicates: does the same person appear twice? He notes that poor quality wastes effort and annoys customers who receive two copies of every email. Kwame writes all four down.

### 3.2 Where data live

Kwame draws a simple map of where Copperleaf's data are stored: the paper sign-up sheet, the newsletter service, the till provider's system, the staff messaging group, a shared folder for invoices and the locked allergy folder. For each place he notes who can see it and whether it is protected. He finds an old spreadsheet of customer emails on the café laptop that nobody uses. Mrs. Adeyemi agrees he should delete it after checking it holds nothing needed. He keeps the map with the rules.

### 3.3 Suppliers

Three suppliers handle Copperleaf's data: the newsletter service, the till and card payment provider and the messaging app. Kwame checks each one's terms for data protection commitments, such as keeping data secure, using it only for Copperleaf and deleting it when the contract ends. The newsletter service and till provider include these terms. The messaging app is a free personal version without business terms, so Mrs. Adeyemi switches to its paid business version. Kwame keeps a copy of each supplier's terms in the shared folder.

### 3.4 Payments and invoices

Kwame looks at invoices and finds two copies of the same supplier invoice, one emailed and one paper, with slightly different dates. The café nearly paid twice. He suggests that invoices be entered once, from the emailed copy, with the paper copy marked as received. Mrs. Adeyemi agrees. Ms. Fischer notes that duplicate records are a quality problem in money data too, and that a single entry point prevents most of them. The accountant also welcomes the change, because it makes the monthly records easier to check.

### 3.5 Simple checks

Kwame sets three monthly checks: look for duplicate or malformed emails in the newsletter list, confirm that only current staff are in the messaging group and compare invoices entered with payments made. Each check takes a few minutes. He records the date and anything found in a notebook kept with the rules. Ms. Fischer explains that short, regular checks catch problems early and show that the rules are being followed. After the first month, the notebook already shows one duplicate email removed and one former staff member taken out of the group.

### Worked example

Kwame defines quality with completeness, validity, accuracy and duplicates, maps where data live and deletes an unused email spreadsheet, moves staff messaging to a business version, stops duplicate invoices at entry and sets three monthly checks.

> **Synthetic case.** Systems and suppliers are synthetic.

### Errors and limits

Free personal apps used for business data often lack the terms a business needs.

### Exercises

- **EX027 — Quality questions.** What three quality questions does Ms. Fischer use? *Rubric:* 3 = complete, valid, accurate;; 2 = all;; 1 = some;; 0 = none.
- **EX028 — Added question.** What fourth question did Kwame add? *Rubric:* 3 = whether the same person appears twice;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX029 — Forgotten spreadsheet.** What forgotten file was on the café laptop? *Rubric:* 3 = an old spreadsheet of customer emails;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX030 — Deletion condition.** What was checked before deleting it? *Rubric:* 3 = that it held nothing needed;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX031 — Supplier count.** How many suppliers handle Copperleaf's data? *Rubric:* 3 = three;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX032 — Supplier terms.** What should supplier terms commit to? *Rubric:* 3 = security, use only for Copperleaf, deletion at end;; 2 = most;; 1 = few;; 0 = none.
- **EX033 — Messaging fix.** What changed for the messaging app? *Rubric:* 3 = switched to the paid business version;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX034 — Invoice duplicate.** Why did the café nearly pay twice? *Rubric:* 3 = emailed and paper copies of one invoice;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX035 — Invoice entry rule.** Which invoice copy is entered? *Rubric:* 3 = the emailed copy;; 2 = partly correct;; 1 = paper;; 0 = none.
- **EX036 — Messaging check.** What does the messaging group check confirm? *Rubric:* 3 = only current staff are members;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX037 — Check record.** Where are check results recorded? *Rubric:* 3 = a notebook kept with the rules;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX038 — Check time.** How long does each monthly check take? *Rubric:* 3 = a few minutes;; 2 = partly correct;; 1 = wrong;; 0 = none.

<a id="ch-04"></a>

## Chapter 4 — Guided lab and action plan

### Learning outcomes

You will (1) check a synthetic sign-up list with a short script; (2) decide who may receive the newsletter; (3) write a one-month action plan.

### 4.1 The sign-up list

Copperleaf's newsletter list was typed from paper sheets by different staff. Some rows have blank emails, some have the same address typed twice with different capitals or spaces and some have no tick in the consent box. Kwame wants to know how many addresses the café may actually email. Ms. Fischer helps him write a short Python script using only the standard library, run on a synthetic list of twelve rows that copies these problems without using any real customer details. Kwame runs it.

### Lab — Checking a synthetic café sign-up list for blanks, malformed addresses, duplicates and consent ticks

```python
"""Check a synthetic cafe newsletter sign-up list: blanks, duplicates and consent ticks (stdlib only)."""
rows = [("ana@example.org", "yes"), ("Ana@Example.org ", "yes"), ("", "yes"), ("ben@example.org", ""),
        ("cai@example.org", "yes"), ("dee@example", "yes"), ("eli@example.org", "no"), ("fay@example.org", "yes"),
        ("cai@example.org", "yes"), ("gus@example.org", "yes"), ("", ""), ("hal@example.org", "yes")]
clean = [(e.strip().lower(), c) for e, c in rows]
blank = sum(1 for e, _ in clean if not e)
bad = sum(1 for e, _ in clean if e and ("@" not in e or "." not in e.split("@")[-1]))
seen, dup = set(), 0
for e, _ in clean:
    if e and e in seen: dup += 1
    seen.add(e)
ok = {e for e, c in clean if e and c == "yes" and "." in e.split("@")[-1]}
print(f"rows {len(rows)}; blank email {blank}; malformed {bad}; duplicates {dup}")
print(f"unique valid addresses with a yes tick: {len(ok)}")
```

Run with `python3 lab_signups.py`. Verified output:

```text
rows 12; blank email 2; malformed 1; duplicates 2
unique valid addresses with a yes tick: 5
```

### 4.2 What the lab finds

The script trims spaces and lowercases each address before checking it. Of twelve rows, two have a blank email, one address is malformed because it has no proper ending after the at sign and two rows are duplicates of addresses already listed. After removing problems, only five unique, valid addresses have a yes tick in the consent box. Kwame is surprised: twelve rows on paper become five people the café can confidently email. He shows the result to Mrs. Adeyemi, who had expected a much larger list.

### 4.3 Deciding who to email

Ms. Fischer explains that marketing emails need the customer's consent, and the café must be able to show it. Rows with a blank tick or a no tick are not emailed. The malformed address cannot be used anyway. Kwame and Mrs. Adeyemi decide to email the five confirmed addresses and to ask other customers in person to sign the new sheet if they want the newsletter. He records the decision and the date in the notebook. Mrs. Adeyemi agrees with the decision.

### 4.4 The action plan

Kwame writes a one-month plan with five actions: replace the sign-up sheet with the shorter version including a clear consent box and the date; run the lab check each month on the typed list; delete the forgotten spreadsheet; finish switching to the paid messaging app; and explain the rules at the next staff meeting. Each action has a person and a date. Mrs. Adeyemi approves it, and Kwame pins it beside the rules. He keeps the plan short so that it can actually be finished in a month.

### 4.5 After the course

At the end of the month, Kwame reviews progress. Four actions are done; the staff meeting moved to the following week. He reflects that small, clear decisions changed more than he expected, and that checking data with a short script made the problem visible to everyone. Ms. Fischer suggests he continue with privacy and data protection, since customer and staff details are central to the café. The next course in this area does exactly that. Kwame thanks Ms. Fischer and enrols the following month.

### Worked example

Kwame checks twelve synthetic sign-up rows, finding two blanks, one malformed address and two duplicates, leaving five unique valid addresses with consent, decides to email only those and completes four of five actions in his one-month plan.

> **Synthetic case.** The list is synthetic; outputs come from lab_signups.py; the GDPR is real. This is not legal advice.

### Errors and limits

Counting rows instead of unique, valid, consented addresses overstates who may be emailed.

### Exercises

- **EX039 — Lab rows.** How many rows does the synthetic list have? *Rubric:* 3 = twelve;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX040 — Blank emails.** How many rows have a blank email? *Rubric:* 3 = two;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX041 — Malformed count.** How many addresses are malformed? *Rubric:* 3 = one;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX042 — Duplicate rows.** How many duplicate rows does the script find? *Rubric:* 3 = two;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX043 — Emailable total.** How many unique valid addresses have a yes tick? *Rubric:* 3 = five;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX044 — Normalising steps.** What does the script do before checking each address? *Rubric:* 3 = trims spaces and lowercases;; 2 = both;; 1 = one;; 0 = none.
- **EX045 — Blank tick decision.** Are rows with a blank tick emailed? *Rubric:* 3 = no;; 2 = partly correct;; 1 = yes;; 0 = none.
- **EX046 — Other customers.** How will other customers join the newsletter? *Rubric:* 3 = by signing the new sheet in person;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX047 — Plan actions.** How many actions are in the one-month plan? *Rubric:* 3 = five;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX048 — New sheet features.** What does the new sheet include? *Rubric:* 3 = a clear consent box and the date;; 2 = both;; 1 = one;; 0 = none.
- **EX049 — Late action.** Which action slipped? *Rubric:* 3 = the staff meeting explanation;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX050 — Next topic.** What does Ms. Fischer suggest next? *Rubric:* 3 = privacy and data protection;; 2 = partly correct;; 1 = other;; 0 = none.

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Kwame Boateng, Ms. Lena Fischer, Riverside Adult Learning Centre, Copperleaf Café and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Two.

**EX002.** A data manager for a local council.

**EX003.** Agreeing who is responsible, what rules apply and how they are checked.

**EX004.** No; owners, rules and checks are enough to start.

**EX005.** They are health information, a special category under the GDPR.

**EX006.** Staff rotas.

**EX007.** Paying a supplier twice because two invoice copies exist.

**EX008.** Serving a customer food they react to.

**EX009.** Mrs. Adeyemi, the owner.

**EX010.** Kwame.

**EX011.** The assistant manager.

**EX012.** Customer and staff data stay within approved systems.

**EX013.** On a single page agreed by Mrs. Adeyemi.

**EX014.** Only the newsletter.

**EX015.** Only staff preparing that customer's order.

**EX016.** Through the café's paid staff messaging group.

**EX017.** First name and email.

**EX018.** There is less to protect, lose or explain.

**EX019.** Separate logins for each person.

**EX020.** The same day, to Kwame.

**EX021.** They are deleted soon after.

**EX022.** Every six months, with the customer.

**EX023.** A year, unless people agreed to longer use.

**EX024.** Through the paid messaging group, keeping numbers private.

**EX025.** Pinned in the staff room.

**EX026.** People understanding why the rules exist.

**EX027.** Is it complete, valid and accurate?

**EX028.** Whether the same person appears twice.

**EX029.** An old spreadsheet of customer emails.

**EX030.** That it held nothing the café still needed.

**EX031.** Three.

**EX032.** Security, use only for Copperleaf and deletion at the end.

**EX033.** Copperleaf switched to its paid business version.

**EX034.** The same invoice existed as an emailed and a paper copy.

**EX035.** The emailed copy, with the paper marked as received.

**EX036.** That only current staff are in the group.

**EX037.** In a notebook kept with the rules.

**EX038.** A few minutes.

**EX039.** Twelve.

**EX040.** Two blank emails.

**EX041.** One malformed address.

**EX042.** Two duplicate rows.

**EX043.** Five.

**EX044.** It trims spaces and converts to lowercase.

**EX045.** No; blank ticks are not treated as consent.

**EX046.** By signing the new sheet in person if they wish.

**EX047.** Five actions.

**EX048.** A clear consent box and the date.

**EX049.** Explaining the rules at the staff meeting, moved a week.

**EX050.** Privacy and data protection.

<a id="references"></a>
## References

Every DOI was resolved through doi.org on 12 October 2026, and standards were checked against their publisher pages. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
