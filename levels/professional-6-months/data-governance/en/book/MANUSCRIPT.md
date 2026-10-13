# Data Governance: Professional Course

- Language: English (`en`); course 026, Professional course (6 months).
- Editorial state: **draft**. Chapters 1–12 of 12 have hand-written teaching text; exercises EX001–EX060 have matching worked results with 0–3 rubrics; two offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: working professionals who have been asked to take responsibility for data governance in a small organisation.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs normalise synthetic donor emails to reveal duplicates and classify synthetic marketing consent records by whether they show when consent was given. Standards and law are cited by edition and paraphrased; nothing here is legal advice. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one professional from mapping a small charity's data and risks through roles, an inventory, policy, data quality, consent, security, suppliers, retention and rights to incident handling, trustee reporting and a one-year plan. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Grace Mwangi** | Operations manager and course participant | Invented |
| **Mr. Tomasz Nowak** | Course tutor | Invented |
| **Kingsford Professional Academy** | Fictional academy | Invented |
| **Northbank Food Bank Network** | Fictional charity, six food banks, about 400 volunteers and 4,000 donors | Invented |

### Core sources

DAMA-DMBOK2 (2017); GDPR. Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — The role and the organisation

### Learning outcomes

You will (1) describe the professional course and its case; (2) outline the data a small charity holds; (3) set goals for a governance lead role.

### 1.1 The learner

Grace Mwangi is the new operations manager at Northbank Food Bank Network, a fictional charity running six food banks with about four hundred volunteers, four thousand donors and referral records for families who receive food parcels. Her trustees have asked her to take responsibility for data governance. She enrols on a six-month professional course at the fictional Kingsford Professional Academy, taught by Mr. Tomasz Nowak, which meets one evening a week and uses synthetic data for every exercise. Grace is eager to start.

### 1.2 Northbank's data

Grace lists the charity's data: donor names, addresses, emails and gift histories; volunteer contact details, availability and safeguarding checks; client referrals from social workers and doctors, including household size, reasons for need and sometimes health details; stock records of food received and distributed; and financial records. She notes that client referral data are the most sensitive, because they reveal hardship and sometimes health conditions, which the GDPR treats as special category data needing extra protection. She records each kind of data with the team that uses it.

### 1.3 Current state

Grace finds data spread across a donor database, spreadsheets kept by each food bank, paper referral forms in filing cabinets, a shared email inbox and volunteers' personal phones. Nobody has written rules on who may see referral data or how long it is kept. A trustee recently asked how many families were helped last year, and three food banks gave figures using different definitions of a family. Mr. Nowak notes that this is a typical starting point for a small organisation. Grace records this.

### 1.4 Goals

Grace sets goals for the course: know what data Northbank holds and where, agree who is responsible for each kind, protect client data properly, improve donor data for fundraising and report reliable figures to trustees. Mr. Nowak asks her to make each goal measurable, such as all six food banks using one definition of a household by the end of the course. She writes the goals in her course notebook and shares them with the chair of trustees. The chair welcomes the goals.

### Worked example

Grace, a new operations manager at Northbank, lists donor, volunteer, client, stock and financial data, finds scattered records and inconsistent family counts and sets measurable governance goals shared with the chair.

> **Synthetic case.** Northbank, Kingsford and all people are synthetic; the GDPR is real.

### Errors and limits

Treating a small organisation's data as too simple to govern leaves sensitive records unprotected.

### Exercises

- **EX001 — Course length.** How long is Grace's course? *Rubric:* 3 = six months;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX002 — Most sensitive.** Which data are most sensitive at Northbank? *Rubric:* 3 = client referral data;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX003 — Special category.** Why can referrals be special category data? *Rubric:* 3 = they sometimes contain health details;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX004 — Family figures.** What went wrong when trustees asked about families helped? *Rubric:* 3 = food banks used different definitions;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX005 — Measurable goal.** Give the course's example of a measurable goal. *Rubric:* 3 = all six food banks use one household definition;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-01 -->
### Continue studying — lesson 01 (chapter 01 of 12)

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 →](#ch-02)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-02"></a>

## Chapter 2 — Why governance matters for a charity

### Learning outcomes

You will (1) explain the benefits of data governance to trustees; (2) link governance to the charity's mission; (3) describe the risks of doing nothing.

### 2.1 Mission and trust

Mr. Nowak explains that charities depend on trust from donors, clients, volunteers and funders. Donors give because they trust their money and details are handled well. Clients share personal hardship because they trust it will stay private. Grace writes that governance protects this trust by making sure data are accurate, used only as promised and kept safe. She notes that a data breach involving client referrals could stop families seeking help. Grace writes this point at the top of her briefing for trustees, because it connects data to the people the charity exists to help.

### 2.2 Better decisions

Good data help Northbank decide where to open a new distribution point, which foods to request and when volunteers are most needed. With inconsistent definitions, the charity cannot compare food banks or show funders its impact. Grace explains to trustees that agreed definitions and checks would let them see reliable trends. DAMA-DMBOK2 describes governance as giving authority and control over data so that it serves the organisation's goals. Grace gives trustees an example: with one household definition, they could compare demand across all six food banks for the first time.

### 2.3 Legal duties

Northbank must follow data protection law. The GDPR requires a lawful basis for each use of personal data, extra conditions for special category data, security, limits on keeping data and responses to people's requests. Fundraising emails need consent under electronic marketing rules. Grace lists the duties that apply and notes that failing them could lead to complaints, regulatory action and harm to the charity's reputation, which matters greatly for donations. She shares the list with the trustees and asks the chair to confirm who will check that each duty is met.

### 2.4 Risks of doing nothing

Grace lists risks: referral forms lost from an unlocked cabinet, a volunteer's phone with client numbers stolen, donors emailed after asking not to be, funders receiving inconsistent figures and records kept for years without reason. For each, she estimates likelihood and impact with Mr. Nowak's simple scale. The highest risks involve client data on paper and phones. She uses this list to explain to trustees why governance needs time and attention. The trustees agree to give Grace two days a month for governance work and to review progress quarterly.

### Worked example

Grace links governance to trust, better decisions and legal duties, lists risks of doing nothing and identifies client data on paper and phones as the highest risks for trustees.

> **Synthetic case.** Risks are synthetic; DAMA-DMBOK2 and the GDPR are real.

### Errors and limits

Presenting governance only as compliance misses its value for decisions and trust.

### Exercises

- **EX006 — Breach effect.** How could a referral breach affect clients? *Rubric:* 3 = families might stop seeking help;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX007 — Marketing rule.** What do fundraising emails need? *Rubric:* 3 = consent;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX008 — Decision example.** Name one decision good data support. *Rubric:* 3 = where to open a distribution point;; 2 = one;; 1 = vague;; 0 = none.
- **EX009 — Highest risks.** Which risks ranked highest? *Rubric:* 3 = client data on paper and phones;; 2 = partly correct;; 1 = partial;; 0 = none.
- **EX010 — Trustee case.** What did Grace use to explain the need for governance? *Rubric:* 3 = her ranked risk list;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-02 -->
### Continue studying — lesson 02 (chapter 02 of 12)

[← Chapter 01](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 →](#ch-03)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-03"></a>

## Chapter 3 — Roles and responsibilities

### Learning outcomes

You will (1) define governance roles for a small charity; (2) assign them realistically; (3) write simple role descriptions.

### 3.1 Keeping roles simple

Mr. Nowak explains that small organisations need simple roles. A trustee takes oversight of data on behalf of the board. A data lead, Grace, coordinates governance day to day. Owners are managers responsible for each kind of data: the fundraising manager for donors, the volunteer coordinator for volunteers and the food bank leads for client referrals. Volunteers and staff follow the rules. Grace notes that clear names matter more than impressive titles. Grace writes the roles in a short table with one line for each person and the data they look after.

### 3.2 Assigning roles

Grace proposes the roles to trustees. One trustee with legal experience agrees to oversee data. The fundraising manager accepts ownership of donor data. Food bank leads accept ownership of client referrals, with Grace setting common rules. Grace checks whether Northbank must appoint a data protection officer and finds that its large-scale processing of special category data may require one. She raises it with the trustee, who arranges external advice. The advice confirms that an external officer should be appointed, and the board agrees to arrange one on a part-time contract.

### 3.3 Role descriptions

Grace writes a short description for each role: what decisions it makes, what it must check and who it reports to. The food bank lead's description includes deciding which volunteers may see referrals, checking that paper forms are locked away and reporting problems to Grace within a day. She keeps each description to half a page. Mr. Nowak notes that short descriptions are more likely to be read and followed. Each owner reads and signs their description, and Grace keeps the signed copies with the data policy for reference.

### 3.4 Making it stick

Grace adds data responsibilities to volunteer induction, so new volunteers learn who to ask. She adds a standing data item to the monthly leads meeting. She also asks the trustee to report on data at each board meeting. Mr. Nowak explains that roles become real when they appear in routines such as inductions and meetings, rather than existing only in a document nobody revisits. After three months, Grace finds that leads raise data questions at most monthly meetings, which shows that the routine is working and that leads now see data as part of their job.

### Worked example

Grace defines trustee, data lead, owner and volunteer roles, assigns them with a legal trustee overseeing, raises the possible need for a data protection officer and embeds roles in inductions and meetings.

> **Synthetic case.** Roles are synthetic; the GDPR is real.

### Errors and limits

Copying large-company role structures into a small charity creates unfilled posts.

### Exercises

- **EX011 — Donor owner.** Who owns donor data? *Rubric:* 3 = the fundraising manager;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX012 — Oversight trustee.** Which trustee oversees data? *Rubric:* 3 = one with legal experience;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX013 — DPO question.** Why might Northbank need a data protection officer? *Rubric:* 3 = large-scale special category processing;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX014 — Lead reporting time.** How quickly must leads report problems? *Rubric:* 3 = within a day;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX015 — Embedding roles.** Name one routine that embeds roles. *Rubric:* 3 = volunteer induction or monthly meetings;; 2 = one;; 1 = vague;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-03 -->
### Continue studying — lesson 03 (chapter 03 of 12)

[← Chapter 02](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 →](#ch-04)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-04"></a>

## Chapter 4 — A data inventory

### Learning outcomes

You will (1) build a data inventory; (2) record purpose, location and access; (3) use the inventory to find gaps.

### 4.1 Building the inventory

Grace builds an inventory in a spreadsheet. Each row is a set of data, such as donor database or referral forms at the riverside food bank. Columns record what personal data it holds, purpose, lawful basis, where it is stored, who can access it, how long it is kept and the owner. She visits each food bank and asks leads to show her where data are kept, rather than relying on descriptions, and finds items nobody had mentioned. She visits all six food banks in two weeks.

### 4.2 Surprises

At two food banks, volunteers keep client phone numbers on personal phones to arrange collections. One food bank keeps referral forms from five years ago in a cupboard. The shared inbox contains referral emails from social workers with full case details. Grace records each in the inventory. Mr. Nowak notes that visiting in person reveals informal practices that people do not think to mention because they seem normal to them. Grace thanks the leads for showing her these practices openly and explains that the aim is to fix problems, not to blame anyone.

### 4.3 Finding gaps

With the inventory complete, Grace looks for gaps: data without a clear purpose, data without a lawful basis recorded, data kept too long and data accessible to too many people. She finds that the five-year-old forms have no purpose now, that volunteers' personal phones are uncontrolled and that the shared inbox is open to all staff. She lists actions with owners and dates for each gap. The trustee overseeing data reviews the action list and agrees the dates with each owner, so that the most serious gaps, involving client data, are addressed first.

### 4.4 Keeping it current

Grace asks owners to tell her when they start collecting new data or change how they store it. She schedules a review of the inventory every six months. She also uses the inventory to write Northbank's privacy notice, because it lists what data are held and why. Mr. Nowak explains that the GDPR expects organisations to keep records of processing, and that a good inventory serves this purpose and many others. Grace adds the inventory review to the governance calendar so that it is not forgotten during busy periods.

### Worked example

Grace builds an inventory by visiting each food bank, finds client numbers on personal phones, five-year-old forms and an open inbox, lists actions for gaps and keeps the inventory current for the privacy notice.

> **Synthetic case.** Findings are synthetic; the GDPR is real.

### Errors and limits

Building inventories from descriptions alone misses informal practices.

### Exercises

- **EX016 — Visiting reason.** Why did Grace visit food banks in person? *Rubric:* 3 = to find data people do not mention;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX017 — Old forms.** How old were the forgotten referral forms? *Rubric:* 3 = five years;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX018 — Inbox gap.** What was wrong with the shared inbox? *Rubric:* 3 = open to all staff with case details;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX019 — Review cycle.** How often is the inventory reviewed? *Rubric:* 3 = every six months;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX020 — Notice use.** What document does the inventory help write? *Rubric:* 3 = the privacy notice;; 2 = partly correct;; 1 = other;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-04 -->
### Continue studying — lesson 04 (chapter 04 of 12)

[← Chapter 03](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 →](#ch-05)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-05"></a>

## Chapter 5 — Policy essentials

### Learning outcomes

You will (1) write a short data policy; (2) turn it into practical rules for volunteers; (3) get approval and communicate it.

### 5.1 A short policy

Grace drafts a two-page data policy for Northbank: why data matter to the mission, roles, principles for handling personal data, rules for client data, security basics, retention and how to report problems. She avoids legal language where possible. The policy states that client referral data may be seen only by named volunteers at the relevant food bank and must never be stored on personal devices. Owners comment, and she revises the draft. The final version is clearer and shorter than the first draft.

### 5.2 Practical rules

Most volunteers will not read a policy. Grace turns it into a one-page guide called Looking after people's information, with ten simple rules, such as lock referral forms away at the end of each session, never take photos of forms and report lost papers or phones to your lead the same day. She tests the guide with five volunteers, who suggest simpler words for two rules. The final guide is printed for every food bank. Grace adds simple pictures to help volunteers.

### 5.3 Approval

The trustee overseeing data presents the policy to the board, explaining risks and benefits. The board approves it and asks for a progress report in three months. Grace notes that board approval gives the policy authority, which helps when leads or volunteers resist changes such as no longer using personal phones. Mr. Nowak explains that policies without senior backing are easily ignored. The trustee also asks Grace to bring examples of how the policy has changed practice at each food bank, so that the board can see real effects rather than only a document.

### 5.4 Communication

Grace introduces the guide at each food bank in a short talk during a session, explaining why each rule protects clients. She answers questions, such as how volunteers should arrange collections without personal phones. She arranges a shared charity phone at each food bank for that purpose. She notes that rules are followed more willingly when people understand the reason and have a practical alternative to their old habits. After the talks, Grace checks with each lead that the guide is displayed and that the charity phone is in use.

### Worked example

Grace drafts a two-page policy, turns it into a ten-rule volunteer guide tested with volunteers, gets board approval with a three-month progress check and introduces it with talks and charity phones.

> **Synthetic case.** Documents are synthetic.

### Errors and limits

Banning a practice without an alternative leads people to keep doing it quietly.

### Exercises

- **EX021 — Client data rule.** Who may see client referral data? *Rubric:* 3 = named volunteers at the relevant food bank;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX022 — Guide title.** What is the volunteer guide called? *Rubric:* 3 = Looking after people's information;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX023 — Rule count.** How many rules does the guide have? *Rubric:* 3 = ten;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX024 — Phone alternative.** What replaced personal phones for collections? *Rubric:* 3 = a shared charity phone at each food bank;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX025 — Board request.** What did the board ask for after approval? *Rubric:* 3 = a progress report in three months;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-05 -->
### Continue studying — lesson 05 (chapter 05 of 12)

[← Chapter 04](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 →](#ch-06)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-06"></a>

## Chapter 6 — Data quality in practice

### Learning outcomes

You will (1) find duplicate donor records; (2) normalise simple fields; (3) set up quality habits for a small team.

### 6.1 Duplicate donors

The fundraising manager reports that some donors receive two copies of each newsletter and complain. Grace suspects duplicate email addresses entered in different ways. She exports synthetic donor emails and checks how many are really the same address written differently, such as with capital letters or extra spaces. She explains that duplicates waste money, annoy donors and make it look as though Northbank has more supporters than it really does. The fundraising manager agrees to export the donor email list for checking with her help.

### Lab — Duplicate donor emails before and after normalising case and spaces

```python
"""Count duplicate synthetic donor emails before and after normalising case and spaces (stdlib only)."""
import random
random.seed(2)
base = [f"donor{i}@example.org" for i in range(1500)]
emails = []
for e in base:
    emails.append(e)
    if random.random() < 0.08: emails.append(e.upper())
    if random.random() < 0.05: emails.append(" " + e + " ")
print(f"records {len(emails)}; distinct as written {len(set(emails))}; distinct normalised {len({e.strip().lower() for e in emails})}")
print(f"duplicate records found by normalising {len(emails) - len({e.strip().lower() for e in emails})}")
```

Run with `python3 lab_emails.py`. Verified output:

```text
records 1684; distinct as written 1684; distinct normalised 1500
duplicate records found by normalising 184
```

### 6.2 Results

The lab checks 1,684 synthetic email records. As written, all 1,684 are distinct, so a simple duplicate check finds nothing. After converting to lowercase and removing spaces at the ends, only 1,500 distinct addresses remain. Normalising reveals 184 duplicate records. Grace notes that the duplicates were invisible until the data were normalised, which is why newsletters were going out twice without anyone understanding why. Grace explains the finding to the fundraising manager with three examples of the same address written in different ways, which makes the problem easy to understand without any technical knowledge.

### 6.3 Fixing and preventing

The fundraising manager merges duplicate donors in the database, keeping the full gift history on one record. Grace asks the database supplier whether emails can be stored in lowercase automatically, which it can. She also asks staff to search for a donor before adding a new one. Mr. Nowak notes that fixing existing duplicates and preventing new ones are both needed, or the problem returns. After the changes, newsletter complaints about duplicate copies stop, and the fundraising manager reports a more accurate count of supporters to the trustees.

### 6.4 Quality habits

Grace sets up simple habits: a monthly duplicate check, a quarterly check of missing postcodes and a yearly check that household definitions are used consistently. Each check has an owner and takes less than an hour. She records results in a short log. She notes that small, regular checks suit a charity with limited staff better than large clean-up projects that compete with daily work. The log is reviewed at each monthly leads meeting, so that problems are noticed early and owners can see that their checks make a difference.

### Worked example

Grace finds 184 duplicate donor emails that were invisible until 1,684 records were normalised to 1,500 addresses, merges them with gift history, adds lowercase storage and search-first entry and sets monthly checks.

> **Synthetic case.** Emails are synthetic; outputs come from lab_emails.py.

### Errors and limits

Exact-match duplicate checks miss differences in case and spacing.

### Exercises

- **EX026 — Distinct normalised.** How many distinct addresses remain after normalising? *Rubric:* 3 = 1,500;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX027 — Duplicates revealed.** How many duplicate records did normalising reveal? *Rubric:* 3 = 184;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX028 — Exact check result.** What did an exact duplicate check find? *Rubric:* 3 = nothing; all 1,684 distinct as written;; 2 = nothing, without the reason;; 1 = vague;; 0 = no answer.
- **EX029 — Supplier change.** What did the supplier enable? *Rubric:* 3 = storing emails in lowercase automatically;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX030 — Check duration.** How long should each check take? *Rubric:* 3 = less than an hour;; 2 = partly correct;; 1 = wrong;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-06 -->
### Continue studying — lesson 06 (chapter 06 of 12)

[← Chapter 05](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 →](#ch-07)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-07"></a>

## Chapter 7 — Consent and lawful basis

### Learning outcomes

You will (1) check whether consent records support marketing; (2) choose lawful bases for different uses; (3) fix weak consent records.

### 7.1 Why consent records matter

Northbank emails donors about appeals and events. Electronic marketing rules require consent for such emails, and the GDPR requires that the charity can show consent was given. Grace checks the donor database's consent field. Some records say yes with a date and source, some say yes without a date, some say no and some are blank. She explains that a yes without a date cannot show when or how consent was given, which makes it weak evidence if a donor complains. Grace counts each kind.

### Lab — Marketing consent records for 4,000 synthetic donors

```python
"""Check marketing consent records for 4,000 synthetic donors (stdlib only)."""
import random
random.seed(8)
rows = []
for _ in range(4000):
    r = random.random()
    rows.append("yes_dated" if r < 0.62 else "yes_undated" if r < 0.77 else "no" if r < 0.93 else "blank")
for k in ["yes_dated", "yes_undated", "no", "blank"]:
    n = rows.count(k); print(f"{k:<12} {n:5d} ({100*n/len(rows):.1f}%)")
print(f"safe to email: {rows.count('yes_dated')} of {len(rows)}")
```

Run with `python3 lab_consent.py`. Verified output:

```text
yes_dated     2507 (62.7%)
yes_undated    595 (14.9%)
no             615 (15.4%)
blank          283 (7.1%)
safe to email: 2507 of 4000
```

### 7.2 Results

The lab checks four thousand synthetic donor records. Records with a dated yes number 2,507, 62.7 percent. Undated yes records number 595, 14.9 percent. Records marked no number 615, 15.4 percent, and 283 are blank, 7.1 percent. Grace concludes that only the 2,507 donors with dated consent should receive marketing emails until the others are checked. The fundraising manager is surprised, having assumed that every yes was usable. Grace explains that the undated and blank records may well belong to supporters who are happy to hear from Northbank, but the charity cannot show it, so the safest choice is to ask them again rather than assume.

### 7.3 Lawful bases

Grace reviews lawful bases with Mr. Nowak. Marketing emails rely on consent. Processing donations and sending receipts rely on the charity's contract with the donor or legal obligations for tax relief. Client referrals rely on legitimate interests or public task considerations, plus a condition for special category data, which the external data protection officer helps confirm. She records each basis in the inventory so staff know which rules apply. The external officer reviews the list and confirms each basis, adding a short note on the condition used for health details in referrals.

### 7.4 Fixing weak records

For the 595 undated yes records, Grace and the fundraising manager plan a short preference form enclosed with printed gift receipts, so that donors can confirm their choices without Northbank sending marketing emails it cannot yet justify. Donors who confirm are recorded with the date and method. Blank records are treated as no. New sign-up forms record consent with date, wording shown and source automatically. Mr. Nowak notes that good records protect the charity and respect donors' choices. The fundraising manager agrees readily.

### Worked example

Grace finds 2,507 of 4,000 donors (62.7 percent) with dated consent, 595 undated, 615 no and 283 blank, limits emails to dated consent, records lawful bases for each use and plans reconfirmation through receipts.

> **Synthetic case.** Donors are synthetic; outputs come from lab_consent.py; the GDPR is real. This is not legal advice.

### Errors and limits

Treating any yes as valid consent ignores the need to show when and how it was given.

### Exercises

- **EX031 — Dated consent share.** What share of donors had dated consent? *Rubric:* 3 = 62.7% (2,507);; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX032 — Blank treatment.** How are blank consent records treated? *Rubric:* 3 = as no;; 2 = partly correct;; 1 = yes;; 0 = none.
- **EX033 — Undated weakness.** Why are undated yes records weak? *Rubric:* 3 = they cannot show when or how consent was given;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX034 — Receipt basis.** What basis supports sending receipts? *Rubric:* 3 = contract or legal obligation;; 2 = partly correct;; 1 = consent;; 0 = none.
- **EX035 — New form fields.** What do new forms record automatically? *Rubric:* 3 = date, wording shown and source;; 2 = all;; 1 = some;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-07 -->
### Continue studying — lesson 07 (chapter 07 of 12)

[← Chapter 06](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 →](#ch-08)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-08"></a>

## Chapter 8 — Security essentials

### Learning outcomes

You will (1) apply basic security controls in a small charity; (2) secure paper and devices; (3) control access to shared systems.

### 8.1 Paper records

Referral forms arrive on paper at food banks. Grace introduces lockable cabinets at each site, with keys held by leads. Forms are scanned into a secure case system within a week and the paper shredded. She checks each food bank a month later and finds two still storing forms in an open box. She discusses the reasons with the leads, who say the cabinet is in a different room, and arranges for a cabinet in the distribution room. The new cabinet arrives within a fortnight.

### 8.2 Devices

Volunteers had used personal phones for client contacts. Grace replaces this with charity phones that have screen locks, encryption and remote wipe enabled. Laptops used for referrals are encrypted and require passwords. She writes a short rule that client data must not be stored on personal devices, explained in the volunteer guide. Mr. Nowak notes that small organisations can achieve strong protection with basic settings that cost little. Grace sets up the phones herself with a short checklist, so that each one has the same protections and the settings can be confirmed during later checks.

### 8.3 Accounts and access

The shared inbox open to all staff is replaced with a referral mailbox accessible only to leads and Grace. Each person has their own login with multi-factor authentication. Grace reviews access every quarter and removes volunteers who have left. She finds three former volunteers still able to read the donor database and removes them. She explains that removing access promptly is one of the simplest and most effective security controls. She records each review with the date and the changes made, which the trustee overseeing data checks at the next board meeting.

### 8.4 Phishing and suppliers

Grace arranges a short phishing awareness session after a volunteer nearly entered a password into a fake login page. She also checks that the donor database supplier offers encryption, backups and access logs, and that its contract includes data protection terms. Mr. Nowak notes that charities are frequent targets of scams, and that combining staff awareness with checks on suppliers covers the most common threats. Grace writes a short note for volunteers on how to recognise fake login pages and who to tell, which is pinned beside each food bank's computer and repeated at induction.

### Worked example

Grace introduces locked cabinets, scanning and shredding, encrypted charity phones and laptops, a restricted referral mailbox with MFA, quarterly access reviews that remove three former volunteers and phishing awareness.

> **Synthetic case.** Controls are synthetic.

### Errors and limits

Leaving former volunteers' access in place exposes data long after they leave.

### Exercises

- **EX036 — Scan deadline.** How soon are referral forms scanned? *Rubric:* 3 = within a week;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX037 — Open box reason.** Why did two food banks still use open boxes? *Rubric:* 3 = the cabinet was in a different room;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX038 — Phone settings.** Which settings do charity phones have? *Rubric:* 3 = screen lock, encryption and remote wipe;; 2 = all;; 1 = some;; 0 = none.
- **EX039 — Former access.** How many former volunteers could still read the donor database? *Rubric:* 3 = three;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX040 — Supplier checks.** What did Grace check with the database supplier? *Rubric:* 3 = encryption, backups, logs and contract terms;; 2 = most;; 1 = few;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-08 -->
### Continue studying — lesson 08 (chapter 08 of 12)

[← Chapter 07](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 →](#ch-09)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-09"></a>

## Chapter 9 — Working with suppliers and volunteers

### Learning outcomes

You will (1) manage data with suppliers; (2) set expectations for volunteers; (3) handle data shared with referral partners.

### 9.1 Suppliers

Northbank uses a donor database supplier, an email newsletter service and a payroll provider for its few staff. Grace lists the personal data each receives and checks that contracts include processor terms required by the GDPR: acting only on Northbank's instructions, security, confidentiality and deleting data at the end. The newsletter service's standard terms include them; the payroll contract is old and lacks them, so she asks for an updated agreement. The payroll provider sends a new agreement within a month, and Grace files it with the other supplier contracts in one folder.

### 9.2 Volunteers

Volunteers handle client data during sessions. Grace adds a confidentiality agreement to volunteer sign-up, explaining that client details must stay private, and includes data rules in induction. She arranges that only volunteers who need client details see them, such as those preparing parcels for named collections. Volunteers sorting donated food do not need them. She notes that limiting who sees data reduces risk without slowing work. Leads decide which volunteers need client details for each session, and the rota shows this so that nobody has to guess whether they may see the referral list.

### 9.3 Referral partners

Social workers and doctors send referrals. Grace finds some send full case notes by ordinary email. She agrees with the main referral partners a short referral form asking only what Northbank needs: name, contact, household size, any dietary needs and the referrer's details. Health details are included only where relevant to food, such as allergies. Partners send forms through a secure portal. She records the agreement with each partner. Partners welcome the shorter form, which takes less time to complete, and the number of referrals containing unnecessary case notes falls sharply.

### 9.4 Ending relationships

When the old newsletter service is replaced, Grace asks it to confirm deletion of donor emails and records the confirmation. When volunteers leave, their access to systems and any keys are removed within a week. Mr. Nowak notes that ending relationships cleanly is often forgotten, and that a short leaving checklist for volunteers and suppliers prevents data remaining where it should not. Grace writes the checklist on a single page and asks leads to complete it whenever a volunteer leaves, returning it to her so that she can confirm that every account and key has been removed.

### Worked example

Grace checks processor terms and updates the payroll contract, adds volunteer confidentiality and limits client data to those who need it, agrees a minimal secure referral form with partners and confirms deletion when changing suppliers.

> **Synthetic case.** Suppliers and partners are synthetic; the GDPR is real.

### Errors and limits

Accepting full case notes when a short form would do collects more sensitive data than needed.

### Exercises

- **EX041 — Payroll contract.** What did the payroll contract lack? *Rubric:* 3 = processor terms;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX042 — Sorting volunteers.** Do food-sorting volunteers need client details? *Rubric:* 3 = no;; 2 = partly correct;; 1 = yes;; 0 = none.
- **EX043 — Health details rule.** When are health details included in referrals? *Rubric:* 3 = only when relevant to food, like allergies;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX044 — Referral channel.** How do partners send forms now? *Rubric:* 3 = through a secure portal;; 2 = partly correct;; 1 = email;; 0 = none.
- **EX045 — Leaver timing.** How soon is leaving volunteers' access removed? *Rubric:* 3 = within a week;; 2 = partly correct;; 1 = wrong;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-09 -->
### Continue studying — lesson 09 (chapter 09 of 12)

[← Chapter 08](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 →](#ch-10)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-10"></a>

## Chapter 10 — Retention and individual rights

### Learning outcomes

You will (1) set a simple retention schedule; (2) delete data safely; (3) respond to requests from individuals.

### 10.1 Retention schedule

Grace drafts a retention schedule with owners. Client referrals are kept for one year after the last parcel, long enough to handle repeat referrals and queries. Donor gift records are kept for the period tax rules require for gift aid claims. Volunteer records are kept for a short period after leaving, except safeguarding records, which follow sector guidance. Each entry has a reason. The trustee overseeing data approves the schedule. Grace shares the schedule with all owners and adds it to the inventory so that each set of data shows how long it will be kept.

### 10.2 Deletion in practice

Grace arranges a monthly routine: the case system lists referrals past one year since the last parcel, a lead checks them and deletes them, recording the count. The five-year-old paper forms found in the inventory are shredded securely with a record kept. She asks the donor database supplier to set automatic deletion for lapsed records after the tax period. Mr. Nowak notes that routine deletion is easier than occasional large clear-outs. The first monthly run deletes a large number of old referrals, and the lead records the count in the log.

### 10.3 Access requests

A former client asks what information Northbank holds about her. Grace checks the inventory to find all places: the case system, the referral mailbox and the charity phone at her food bank. She gathers the information, removes details about other people, such as the referrer's internal notes about other family members, and responds within a month. She records the request and response in a log. The former client thanks Northbank for the clear reply, and Grace notes that the inventory made the search take an afternoon instead of the days it might otherwise have taken.

### 10.4 Other rights

A donor asks to stop receiving appeals. Grace marks the record as no marketing rather than deleting it, so the donor is not added again from an old list. Another person asks for a wrong address to be corrected, and Grace corrects it in the database and the newsletter service. She notes that each right needs a clear process, and that the inventory makes it possible to find every copy of a person's data. She writes a one-page procedure for each type of request.

### Worked example

Grace sets retention including one year after the last parcel for referrals, runs monthly deletion and shreds old forms, answers a former client's access request within a month and handles marketing objections and corrections across systems.

> **Synthetic case.** The schedule and requests are synthetic; the GDPR is real.

### Errors and limits

Deleting a donor who objects to marketing risks re-adding them from old lists; suppress instead.

### Exercises

- **EX046 — Referral retention.** How long are referrals kept after the last parcel? *Rubric:* 3 = one year;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX047 — Deletion checker.** Who checks referrals before deletion? *Rubric:* 3 = a food bank lead;; 2 = partly correct;; 1 = other;; 0 = none.
- **EX048 — Access search.** Where did Grace search for the former client's data? *Rubric:* 3 = case system, referral mailbox and charity phone;; 2 = all;; 1 = some;; 0 = none.
- **EX049 — Objection handling.** How was the donor's objection handled? *Rubric:* 3 = marked no marketing, not deleted;; 2 = partly correct;; 1 = deleted;; 0 = none.
- **EX050 — Correction scope.** Where was the wrong address corrected? *Rubric:* 3 = database and newsletter service;; 2 = both;; 1 = one;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-10 -->
### Continue studying — lesson 10 (chapter 10 of 12)

[← Chapter 09](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 →](#ch-11)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-11"></a>

## Chapter 11 — Incidents and reporting to trustees

### Learning outcomes

You will (1) handle a data incident; (2) decide when to notify; (3) report governance progress to trustees.

### 11.1 An incident

A volunteer leaves a folder with five referral forms on a bus. She reports it to her lead within the hour, following the guide. Grace starts the incident procedure: record what happened, try to recover the folder, assess the risk and decide on notification. The bus company has no record of the folder. The forms contain names, addresses, household details and, on one form, a health condition. Grace writes down the contents of the forms from the lead's memory and the case system, so the risk can be assessed accurately.

### 11.2 Assessing and notifying

Grace and the external data protection officer assess the risk. The data are sensitive, involve vulnerable people and cannot be recovered. They decide the incident is likely to result in a risk to individuals and report it to the supervisory authority within seventy-two hours, as the GDPR requires. Because the risk to the families is high, they also inform them directly, explaining what happened and offering support. Each step is recorded. The supervisory authority acknowledges the report and asks a few questions, which Grace answers using her records.

### 11.3 Learning

The review finds that the volunteer took forms home to phone families because the charity phone was busy. Grace arranges a second charity phone at that food bank and reminds volunteers that forms never leave the premises. The review is blameless; the volunteer is thanked for reporting quickly. Mr. Nowak notes that fast reporting depends on people feeling safe to admit mistakes, so how the first incident is handled shapes future reporting. The volunteer agrees to help explain the new rules to others at her food bank.

### 11.4 Reporting to trustees

Grace prepares a quarterly report for trustees: progress on goals, the inventory status, consent improvement, quality checks, access reviews, requests handled and incidents with lessons. She uses a simple table with green, amber and red ratings and short explanations. The trustees ask about the bus incident and approve funding for more charity phones. Grace notes that honest reporting of incidents builds trustees' confidence that governance is working. She keeps the report to two pages, with a short paragraph on each red or amber item explaining what is being done and by whom.

### Worked example

Grace manages lost referral forms by recording, assessing with the external officer, reporting within seventy-two hours and informing families, adds a second phone after a blameless review and reports progress to trustees with ratings.

> **Synthetic case.** The incident is synthetic; the GDPR is real. This is not legal advice.

### Errors and limits

Blaming volunteers for reported mistakes discourages future reporting.

### Exercises

- **EX051 — Lost item.** What did the volunteer lose? *Rubric:* 3 = a folder with five referral forms;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX052 — Notification deadline.** Within what time was the authority notified? *Rubric:* 3 = seventy-two hours;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX053 — Families informed.** Why were families told directly? *Rubric:* 3 = the risk to them was high;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX054 — Root cause.** Why were the forms taken home? *Rubric:* 3 = the charity phone was busy;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX055 — Trustee decision.** What did trustees fund? *Rubric:* 3 = more charity phones;; 2 = partly correct;; 1 = other;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-11 -->
### Continue studying — lesson 11 (chapter 11 of 12)

[← Chapter 10](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 →](#ch-12)

Continue to the next authored lesson.
<!-- cyberabc:chapter-navigation:end -->

<a id="ch-12"></a>

## Chapter 12 — Action plan and next steps

### Learning outcomes

You will (1) review progress against goals; (2) write a one-year action plan; (3) sustain governance after the course.

### 12.1 Progress review

Grace reviews her goals. Northbank now knows what data it holds and where, roles are assigned, client data are better protected, donor duplicates and consent records are improved and trustees receive regular reports. One goal remains incomplete: all six food banks using one household definition. Four have adopted it; two still use their own. She records the evidence for each goal and the reasons for the gap. She shares the review with the trustee overseeing data before the board meeting, so the remaining gap is not a surprise to anyone.

### 12.2 The household definition

Grace visits the two food banks. Their leads explain that their referral partners count households differently, and changing forms is slow. Grace agrees a transition: both banks record the agreed definition alongside their old one for three months, then switch. She notes that some changes take longer because they depend on partners, and that a planned transition is better than forcing a sudden change that breaks partner relationships. Both leads agree to the transition, and Grace schedules a visit at the end of the three months to confirm the switch.

### 12.3 One-year plan

Grace writes a one-year plan: complete the household definition change, finish consent reconfirmation, automate referral deletion, run two inventory reviews, provide refresher training for volunteers and test the incident procedure with a practice exercise. Each action has an owner, a date and a measure. The trustees approve it. Mr. Nowak notes that plans with owners and measures are much more likely to be completed than general intentions. Grace adds the plan's actions to the governance calendar and reviews progress with the trustee each quarter.

### 12.4 Sustaining governance

Grace reflects that governance at Northbank depends on routines: monthly checks, quarterly access reviews and reports, inductions and leads meetings. She documents these in a calendar so they continue if she leaves. She plans to keep learning, starting with privacy, since client data are central to Northbank. The next course in this area turns to privacy and data protection, where governed data meet the rights of the people they describe. She thanks Mr. Nowak and her classmates, whose questions helped her see Northbank's data more clearly.

### Worked example

Grace reviews goals with one incomplete, agrees a three-month dual-recording transition for two food banks, writes an owned one-year plan approved by trustees and documents routines in a governance calendar.

> **Synthetic case.** The plan is synthetic.

### Errors and limits

Governance that depends on one person's memory stops when they leave.

### Exercises

- **EX056 — Incomplete goal.** Which goal remained incomplete? *Rubric:* 3 = one household definition at all six banks;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX057 — Banks adopted.** How many food banks adopted the definition? *Rubric:* 3 = four;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX058 — Transition length.** How long is the dual-recording transition? *Rubric:* 3 = three months;; 2 = partly correct;; 1 = wrong;; 0 = none.
- **EX059 — Plan test.** What exercise does the plan include? *Rubric:* 3 = a practice incident exercise;; 2 = partly correct;; 1 = vague;; 0 = none.
- **EX060 — Continuity tool.** Where are routines documented? *Rubric:* 3 = a governance calendar;; 2 = partly correct;; 1 = vague;; 0 = none.

<!-- cyberabc:chapter-navigation:start ch-12 -->
### Continue studying — lesson 12 (chapter 12 of 12)

[← Chapter 11](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Next course via chapter index →](../SUBJECTS.md)

The chapter index leads to the next course in the study path.
<!-- cyberabc:chapter-navigation:end -->

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX060. Grace Mwangi, Mr. Tomasz Nowak, Kingsford Professional Academy, Northbank Food Bank Network and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Six months.

**EX002.** Client referral data.

**EX003.** They sometimes include health details.

**EX004.** Food banks used different definitions of a family.

**EX005.** All six food banks using one household definition.

**EX006.** Families could stop seeking help.

**EX007.** Consent under electronic marketing rules.

**EX008.** Where to open a new distribution point.

**EX009.** Client data held on paper and phones.

**EX010.** Her list of ranked risks.

**EX011.** The fundraising manager.

**EX012.** A trustee with legal experience.

**EX013.** Its large-scale processing of special category data.

**EX014.** Within a day.

**EX015.** Volunteer induction.

**EX016.** To find informal practices people would not mention.

**EX017.** Five years.

**EX018.** It held case details and was open to all staff.

**EX019.** Every six months.

**EX020.** The privacy notice.

**EX021.** Only named volunteers at the relevant food bank.

**EX022.** Looking after people's information.

**EX023.** Ten.

**EX024.** A shared charity phone at each food bank.

**EX025.** A progress report in three months.

**EX026.** 1,500.

**EX027.** 184.

**EX028.** Nothing, because all 1,684 were distinct as written.

**EX029.** Automatic lowercase storage of emails.

**EX030.** Less than an hour.

**EX031.** 62.7 percent, 2,507 donors.

**EX032.** As no.

**EX033.** They cannot show when or how consent was given.

**EX034.** The contract with the donor or legal obligations.

**EX035.** The date, the wording shown and the source.

**EX036.** Within a week of arrival, then shredded.

**EX037.** The cabinet was in a different room.

**EX038.** Screen lock, encryption and remote wipe.

**EX039.** Three.

**EX040.** Encryption, backups, access logs and contract terms.

**EX041.** Processor terms required by the GDPR.

**EX042.** No.

**EX043.** Only where relevant to food, such as allergies.

**EX044.** Through a secure portal.

**EX045.** Within a week of the volunteer leaving.

**EX046.** One year.

**EX047.** A food bank lead.

**EX048.** The case system, referral mailbox and charity phone.

**EX049.** The record was marked no marketing rather than deleted.

**EX050.** In the database and the newsletter service.

**EX051.** A folder of five referral forms.

**EX052.** Within seventy-two hours.

**EX053.** Because the risk to them was high.

**EX054.** The charity phone was busy, so the volunteer phoned from home.

**EX055.** More charity phones.

**EX056.** The single household definition across all six food banks, still unfinished.

**EX057.** Four.

**EX058.** Three months.

**EX059.** A practice exercise testing the incident procedure.

**EX060.** In a governance calendar.

<a id="references"></a>
## References

Every DOI was resolved through doi.org on 12 October 2026, and standards were checked against their publisher pages. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- DAMA International. (2017). *DAMA-DMBOK: Data management body of knowledge* (2nd ed., D. Henderson & S. Earley, Eds.). Technics Publications. ISBN 978-1-63462-234-9.
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
