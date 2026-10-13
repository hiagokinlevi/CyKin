# Application and Software Supply Chain Security: Rapid Course

- Language: English (`en`); course 014, Rapid course (1 month).
- Editorial state: **draft**. Chapters 1–4 of 4 have hand-written teaching text; exercises EX001–EX050 have matching worked results with 0–3 rubrics; two offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: people who look after a small organisation's website and need practical, proportionate application and software supply chain security in one month.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: test and review only software you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic code and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow the only IT person at a small charity from a donation-page error caused by an outdated component, through foundations and decisions, permission and safe practice, and components, data and dependencies, to a guided release lab and lasting routines. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Owen Clarke** | Rapid course student and charity IT lead | Invented |
| **Nadia Haddad** | Course tutor | Invented |
| **Riverside Food Network** | Fictional charity | Invented |
| **Kestrel Skills Centre** | Fictional training centre | Invented |

### Core sources

[OWASP Top 10:2021](https://owasp.org/Top10/); OWASP [ASVS](https://owasp.org/www-project-application-security-verification-standard/) 4.0.3 and 5.0.0; OWASP [WSTG](https://owasp.org/www-project-web-security-testing-guide/) and [SAMM](https://owaspsamm.org/); NIST [SP 800-218 (SSDF)](https://doi.org/10.6028/NIST.SP.800-218); [CWE Top 25](https://cwe.mitre.org/top25/); [SLSA v1.0](https://slsa.dev/spec/v1.0/); Shostack, *Threat Modeling: Designing for Security* (Wiley, 2014). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Application and software supply chain security: foundations and decisions

### Learning outcomes

You will (1) explain what application and software supply chain security means for a small organisation's website; (2) recognise the main risks; (3) make simple, proportionate decisions; (4) set priorities for a month of work.

### 1.1 The opening case

Owen Clarke is the only IT person at the fictional charity Riverside Food Network. He is taking a one-month rapid course at the fictional Kestrel Skills Centre with tutor Nadia Haddad. The charity's donation website runs on a common website platform with a handful of plugins. A volunteer installed most of them years ago. Last month a donor reported that the donation page briefly showed an error mentioning an outdated form component, and Owen realised nobody knew which components the site used or who kept them updated.

### 1.2 What the subject covers

Application security protects the website's own code and settings. Software supply chain security protects everything the site is built from: the platform, its plugins, themes and the services they call, and the path by which each arrives and is updated. For a small charity, the supply chain is most of the website.

Owen's site shows the split. The charity wrote almost nothing itself: its settings and a few page templates are its own code. The donation form, the event calendar, the photo gallery, the newsletter plugin, the theme and the platform all came from other people, and the error message a donor saw last month came from one of them.

### 1.3 Main risks

Outdated components with known flaws (OWASP Top 10:2021 A06); components that are no longer maintained; components from unofficial sources; weak administrator sign-in (A07); and integrity failures, where an update or file is changed before it arrives (A08).

Each risk has a face on Owen's site. The donation form was out of date and had a published advisory (A06). The event calendar had not been released for over four years. A component downloaded from an unofficial page could be anything. Three administrator accounts had no multi-factor sign-in (A07). And an update file changed on its way to him is what the hash check guards against (A08).

### 1.4 Proportionate decisions

Owen has a few hours a week. He decides by asking three questions for each risk: how likely is it, how much harm would it cause to donors and the charity, and how cheap is the fix? Cheap fixes for likely, harmful risks go first.

Turning on multi-factor sign-in for the three administrator accounts is the clearest example: an attack on a password is likely, an administrator account could change everything on the site, and the fix costs minutes. Replacing the event calendar is harmful to leave but takes longer, so it comes later in the month.

### 1.5 Frameworks as guides

NIST SP 800-218 (SSDF) and OWASP SAMM v2 are written for software producers and larger organisations, but their ideas scale down: know your components, keep them updated, check what you install, and have a plan for problems.

Owen's month uses each idea at his scale. "Know your components" is the plugin list he exports in week 3. "Keep them updated" is the donate-form update and the weekly routine. "Check what you install" is the hash comparison in the release checklist. "Have a plan" is his rule to stop and call the host and Nadia if he finds signs of misuse.

### 1.6 The month's plan

Week 1 foundations and decisions; week 2 scope and safe practice; week 3 components, data and dependencies; week 4 guided lab and putting it together.

The order matters. Owen cannot decide what to update until he knows what the site uses, and he should not change anything until he has permission, a backup and a staging copy. So the inventory comes in week 3, after the scope, and the donate-form update in week 4, after both. The first week's quick win, multi-factor sign-in, needs no inventory and starts at once.

### Worked example

Owen lists his first decisions: turn on multi-factor sign-in for the three administrator accounts (cheap, high value), list every plugin and its version (cheap, needed for everything else), and ask the platform host whether automatic security updates are available. Nadia agrees these are the right first steps.

> **Synthetic case.** Riverside Food Network and all people and events are synthetic.

### Errors and limits

Proportionate does not mean minimal; some risks need more effort than they first seem to.

### Exercises

- **EX001 — Opening problem.** What did Owen realise after the donor's report? *Rubric:* 3 = nobody knew components or owners; 2 = partial; 1 = vague; 0 = none.
- **EX002 — Supply chain scope.** What does the charity's software supply chain include? *Rubric:* 3 = platform, plugins, themes, services, update path; 2 = three; 1 = one; 0 = none.
- **EX003 — Top 10 links.** Which Top 10:2021 categories match the main risks? *Rubric:* 3 = A06, A07, A08; 2 = two; 1 = one; 0 = none.
- **EX004 — Deciding questions.** What three questions guide Owen's decisions? *Rubric:* 3 = likelihood, harm, cost of fix; 2 = two; 1 = one; 0 = none.
- **EX005 — First decisions.** Name Owen's first three decisions. *Rubric:* 3 = MFA, component list, ask about auto-updates; 2 = two; 1 = one; 0 = none.
- **EX006 — Framework scaling.** How do SSDF and SAMM ideas scale down? *Rubric:* 3 = know, update, check, plan; 2 = three; 1 = one; 0 = none.
- **EX007 — Week three.** What does week 3 cover? *Rubric:* 3 = components, data and dependencies; 2 = partial; 1 = vague; 0 = none.
- **EX008 — Most of the site.** Why is the supply chain "most of the website" here? *Rubric:* 3 = built from others' components; 2 = partial; 1 = vague; 0 = none.
- **EX009 — Unmaintained risk.** Why is an unmaintained component a risk? *Rubric:* 3 = future flaws never fixed; 2 = partial; 1 = vague; 0 = none.
- **EX010 — Integrity failure.** Give an example of an integrity failure. *Rubric:* 3 = update changed before arrival; 2 = partial; 1 = vague; 0 = none.
- **EX011 — MFA value.** Why is multi-factor sign-in a good first step? *Rubric:* 3 = cheap and high value; 2 = partial; 1 = vague; 0 = none.
- **EX012 — Proportionate limit.** What warning comes with proportionate decisions? *Rubric:* 3 = some risks need more effort; 2 = partial; 1 = vague; 0 = none.
- **EX013 — Nadia's role.** What did Nadia do with Owen's list? *Rubric:* 3 = agreed they were right first steps; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Know the components, fix cheap high-value risks first and plan the month.

### Continue studying — chapter 01 of 04

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Scope, permission and safe practice

### Learning outcomes

You will (1) confirm permission before checking or changing the website; (2) set clear scope; (3) work safely with backups and staging; (4) protect donor data.

### 2.1 Permission

Owen is employed by the charity, but changes to the website still need the director's agreement, recorded in an email that names what he will check and change. The website host's terms also say what customers may test. Owen checks only the charity's own site and accounts; he does not probe the host's systems or other sites.

The director's reply adds a condition: she wants to be told before any change that donors could notice. Owen treats the donate-form update as such a change and tells her before releasing it. Keeping the permission in an email means that, if something goes wrong, there is a record of what was agreed and by whom.

### 2.2 Scope

The scope for the month: the donation website, its administrator accounts, its plugins and theme, and the charity's account with the website host. Out of scope: the payment provider's systems, which belong to the provider, and volunteers' personal devices.

Leaving out the payment provider is a limit, not an oversight: card details go straight to the provider's page, and Owen has no right to test its systems. He checks only the hand-off, that the donation form sends donors to the provider's real page. In his final presentation he names this as one of the things he cannot check himself.

### 2.3 Safe practice

Before any change, Owen takes a full backup and confirms it can be restored. He tests updates on a staging copy, a private copy of the site with donor data removed or replaced by synthetic records. He makes one change at a time and notes it in a simple change log.

Owen proves the backup works before relying on it: he restores it once to staging in the first weeks. That restore also gives him the staging copy where he later tests the donate-form update with synthetic donations. Each line in the change log says what changed, when, and how to undo it, which is what the director needs if donors report a problem.

### 2.4 Donor data

The site stores donor names, emails and donation amounts; card details stay with the payment provider. Owen never copies donor data to his own devices and uses synthetic records for testing.

This rule also shapes the staging copy: it holds synthetic donors, so testing the donation form there cannot leak a real person's details. When event-calendar turned out to store volunteers' phone numbers, the same thinking applied: those numbers moved to the charity's volunteer system and were deleted from the website.

### 2.5 Defensive only

The course teaches checking and fixing, not attacking. Owen does not run tools that try to break into the site; he reviews versions, settings and logs.

His checks are all of this kind: the plugin list from the administration page, version numbers compared with published advisories, the hash of a download compared with the vendor's, and the list of administrator accounts. None of them sends unusual requests to the site, so none can break it or upset the host. If he wanted a deeper test, it would need the host's permission and a professional tester.

### 2.6 When to ask for help

If he sees signs that the site has already been misused, such as unknown administrator accounts, Owen stops, preserves evidence and contacts the host's support and Nadia.

Preserving evidence means not deleting the unknown account straight away: Owen notes its name and creation date, takes a screenshot, and asks the host for the access logs before anything changes. Deleting first might stop the attacker, but it would also remove the clues to how they got in and what else they touched. In Owen's month, the monthly account review found no unknown accounts.

### Worked example

Owen's permission email to the director lists the scope and says he will take backups, test on staging and keep a change log. The director replies with approval and asks to be told before any change that donors could notice. Owen restores a backup to staging once to prove it works before relying on it.

> **Synthetic case.** Emails and systems are synthetic.

### Errors and limits

Backups that have never been restored may not work.

### Exercises

- **EX014 — Permission form.** How is Owen's permission recorded? *Rubric:* 3 = email naming checks and changes; 2 = partial; 1 = vague; 0 = none.
- **EX015 — In scope.** List the in-scope items. *Rubric:* 3 = site, admin accounts, plugins and theme, host account; 2 = three; 1 = one; 0 = none.
- **EX016 — Out of scope.** Name two out-of-scope items. *Rubric:* 3 = payment provider systems; volunteers' devices; 2 = one; 1 = vague; 0 = none.
- **EX017 — Staging copy.** What is a staging copy? *Rubric:* 3 = private copy with synthetic data; 2 = partial; 1 = vague; 0 = none.
- **EX018 — Backup proof.** How did Owen prove the backup works? *Rubric:* 3 = restored it to staging; 2 = partial; 1 = vague; 0 = none.
- **EX019 — Card details.** Where are card details stored? *Rubric:* 3 = with the payment provider; 2 = partial; 1 = vague; 0 = none.
- **EX020 — Change log.** Why keep a change log? *Rubric:* 3 = track one change at a time; undo; 2 = partial; 1 = vague; 0 = none.
- **EX021 — Misuse signs.** What should Owen do if he sees misuse? *Rubric:* 3 = stop, preserve evidence, contact host and tutor; 2 = two; 1 = one; 0 = none.
- **EX022 — Defensive scope.** What kind of tools does Owen avoid? *Rubric:* 3 = tools that try to break in; 2 = partial; 1 = vague; 0 = none.
- **EX023 — Director request.** What did the director ask for? *Rubric:* 3 = notice before donor-visible changes; 2 = partial; 1 = vague; 0 = none.
- **EX024 — Donor data rule.** How is donor data protected during testing? *Rubric:* 3 = never copied; synthetic records; 2 = partial; 1 = vague; 0 = none.
- **EX025 — Host terms.** Why read the host's terms? *Rubric:* 3 = they say what customers may test; 2 = partial; 1 = vague; 0 = none.
- **EX026 — One change.** Why make one change at a time? *Rubric:* 3 = easy to find what caused a problem; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Permission, scope, backups and staging make changes safe.

### Continue studying — chapter 02 of 04

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Application and software supply chain security: systems, data and dependencies

### Learning outcomes

You will (1) list the website's components and versions; (2) check advisories, maintenance and use; (3) map where donor data flows; (4) decide to update, replace or remove each component.

### 3.1 Listing components

Owen exports the plugin list from the site's administration page: name, version and whether each is active. He adds the theme, the platform version and the outside services the site calls: the payment provider and the newsletter service. This list is the charity's inventory, the base for every other check.

Writing down which plugins are active matters: photo-gallery appears in the list but is not in use, and an unused plugin still has code on the server that an attacker could reach. Adding the payment provider and the newsletter service shows where donor data leaves the site, which is needed for the data-flow check later in the week.

### Lab — component review

```python
"""Review a synthetic list of website components: advisories, maintenance and use (stdlib only)."""
from datetime import date
today = date(2026, 10, 1)
components = [  # name, version, fixed_version_or_None, last_release, in_use
    ("donate-form", "3.2.0", "3.2.4", date(2026, 8, 2), True),
    ("event-calendar", "1.4.1", None, date(2022, 5, 9), True),
    ("photo-gallery", "2.0.0", None, date(2026, 6, 20), False),
    ("newsletter", "5.1.3", None, date(2026, 9, 1), True),
]
def v(s): return tuple(map(int, s.split(".")))
for name, ver, fixed, last, used in components:
    notes = []
    if fixed and v(ver) < v(fixed):
        notes.append(f"UPDATE to {fixed}")
    if (today - last).days > 730:
        notes.append(f"UNMAINTAINED ({(today - last).days} days since release)")
    if not used:
        notes.append("REMOVE (not in use)")
    print(f"{name:15} {ver:6} {'; '.join(notes) or 'ok'}")
```

Run with `python3 lab_deps.py`. Verified output:

```text
donate-form     3.2.0  UPDATE to 3.2.4
event-calendar  1.4.1  UNMAINTAINED (1606 days since release)
photo-gallery   2.0.0  REMOVE (not in use)
newsletter      5.1.3  ok
```

### 3.2 Lab result

donate-form 3.2.0 must be updated to 3.2.4, the version that fixes a published advisory. event-calendar 1.4.1 is flagged UNMAINTAINED: its last release was 1,606 days ago. photo-gallery 2.0.0 is flagged REMOVE because it is not in use. newsletter 5.1.3 is ok. Each flag leads to a different action: update, replace or remove.

The lab's rules are simple enough to check by hand. A component is UNMAINTAINED if its last release is more than 730 days, about two years, before the review date of 1 October 2026; event-calendar's last release was 9 May 2022. The script compares versions as numbers, so it would correctly flag a version like 3.10 as newer than 3.9.

### 3.3 Why maintenance matters

A component with no releases for years will not receive fixes for future flaws. Kula et al. (2018) found that outdated dependencies are common because updating takes effort; Zimmermann et al. (2019) showed that a few maintainers can affect very many users. Small sites benefit from choosing popular, actively maintained components.

Owen's event-calendar shows the risk: 1,606 days without a release means that any flaw found in it now will probably never be fixed. When he chooses a replacement, he checks the release history and how many sites use it, so that the new calendar is less likely to be abandoned too.

### 3.4 Data flows

Donor details move from the donation form to the site's database, the card details go directly to the payment provider's page, and email addresses go to the newsletter service if the donor opts in. Each flow is a place to check: the form component, database access, the payment hand-off and the newsletter connection.

The newsletter flow depends on the donor's choice: only donors who tick the box are sent to the newsletter service, so Owen checks that the box is unticked by default. The payment hand-off is the most sensitive point: if the form were changed to collect card numbers itself, they would pass through the charity's site, which is exactly what the current design avoids.

### 3.5 Deciding

Update donate-form now (it handles donor data and has an advisory). Replace event-calendar with a maintained alternative within the month. Remove photo-gallery after confirming nobody needs it. Keep newsletter and turn on automatic security updates where the host supports them.

Owen's later discovery changed one priority: event-calendar also stored volunteers' phone numbers for shift sign-ups, which nobody remembered. That moved its replacement up to week 3, with the phone numbers moved to the charity's existing volunteer system and deleted from the website. A decision list is a plan, not a promise; it changes when new facts appear.

### Worked example

Owen reruns the three priority questions for event-calendar after the discovery. Likelihood is unchanged: with no release for 1,606 days, any future flaw stays unfixed. Harm is higher, because the plugin also holds volunteers' phone numbers. The fix cost is unchanged: a maintained alternative. Higher harm alone is enough to move the replacement up to week 3.

> **Synthetic case.** Components, dates and data are synthetic.

### Errors and limits

A component list from the admin page may miss files added by hand; ask the host if unsure.

### Exercises

- **EX027 — Inventory fields.** What does Owen's inventory record? *Rubric:* 3 = name, version, active, plus theme, platform, services; 2 = three; 1 = one; 0 = none.
- **EX028 — donate-form action.** What does the lab say about donate-form? *Rubric:* 3 = update 3.2.0 to 3.2.4; 2 = partial; 1 = vague; 0 = none.
- **EX029 — event-calendar flag.** Why is event-calendar flagged? *Rubric:* 3 = 1,606 days without a release; 2 = partial; 1 = vague; 0 = none.
- **EX030 — photo-gallery flag.** What should happen to photo-gallery? *Rubric:* 3 = remove; not in use; 2 = partial; 1 = vague; 0 = none.
- **EX031 — Card flow.** Where do card details go? *Rubric:* 3 = directly to payment provider; 2 = partial; 1 = vague; 0 = none.
- **EX032 — Newsletter flow.** When does an email reach the newsletter service? *Rubric:* 3 = if donor opts in; 2 = partial; 1 = vague; 0 = none.
- **EX033 — Maintenance research.** What did Kula et al. find? *Rubric:* 3 = outdated dependencies common; 2 = partial; 1 = vague; 0 = none.
- **EX034 — Choosing components.** What kind of components suit small sites? *Rubric:* 3 = popular, actively maintained; 2 = partial; 1 = vague; 0 = none.
- **EX035 — Hidden data.** What did Owen discover about event-calendar? *Rubric:* 3 = stored volunteers' phone numbers; 2 = partial; 1 = vague; 0 = none.
- **EX036 — Phone numbers.** What happened to the phone numbers? *Rubric:* 3 = moved to volunteer system; deleted; 2 = partial; 1 = vague; 0 = none.
- **EX037 — Three actions.** Name the three possible actions. *Rubric:* 3 = update, replace, remove; 2 = two; 1 = one; 0 = none.
- **EX038 — Admin page gap.** What might the admin page list miss? *Rubric:* 3 = files added by hand; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Inventory, check and decide for each component.

### Continue studying — chapter 03 of 04

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Application and software supply chain security: guided lab and applied synthesis

### Learning outcomes

You will (1) prepare a safe update with a pre-release checklist; (2) verify downloads; (3) complete the month's improvements; (4) set routines to keep the site safe.

### 4.1 The update

Owen prepares the donate-form update to 3.2.4. He downloads it from the plugin's official page, compares its SHA-256 hash with the one published by the vendor, takes a backup and tests it on staging with synthetic donations.

The hash comparison protects against a changed download: even if the official page were tampered with or the file damaged on the way, a different file gives a different hash. The test on staging with synthetic donations checks that the updated form still sends donors to the payment provider and records the donation correctly.

### Lab — release checklist

```python
"""Pre-release checklist for a synthetic site update (stdlib only)."""
import hashlib
download = b"synthetic donate-form 3.2.4 release"
vendor_hash = hashlib.sha256(b"synthetic donate-form 3.2.4 release").hexdigest()
checks = {
    "official source used": True,
    "hash matches vendor": hashlib.sha256(download).hexdigest() == vendor_hash,
    "backup taken": True,
    "tested on staging copy": True,
    "admin accounts use MFA": False,
}
for item, ok in checks.items():
    print(f"[{'x' if ok else ' '}] {item}")
missing = [k for k, ok in checks.items() if not ok]
print("READY" if not missing else f"NOT READY: {', '.join(missing)}")
```

Run with `python3 lab_release.py`. Verified output:

```text
[x] official source used
[x] hash matches vendor
[x] backup taken
[x] tested on staging copy
[ ] admin accounts use MFA
NOT READY: admin accounts use MFA
```

### 4.2 Lab result

Four items pass: official source used, hash matches vendor, backup taken and tested on staging copy. One fails: admin accounts use MFA, because one volunteer administrator has not finished setting up multi-factor sign-in. The lab prints NOT READY: admin accounts use MFA. Owen holds the release until the volunteer completes setup the next morning, then reruns the checklist and releases.

The failed item is outside the update itself, which is why it belongs on the list. A newly updated form on a site where one administrator account still has only a password leaves the most powerful account as the easiest way in. Holding the release for one night costs little; the director had already been told the update was coming.

### 4.3 Why a checklist

A checklist makes sure nothing is skipped under time pressure. Each item links to an earlier lesson: sources and hashes protect integrity, backups and staging protect availability, multi-factor sign-in protects the administrator accounts that could change everything else. SLSA v1.0 and Sigstore (Newman et al., 2022) show how larger projects automate similar integrity checks.

For Owen, the list also replaces memory. He runs this release once, but the weekly routine will repeat the same steps for every update, sometimes in a hurry when an advisory is published. A written checklist means a second volunteer, who the director has asked to learn the routines, can follow the same steps without Owen there.

### 4.4 Routines

Weekly: check for plugin updates and apply security updates after staging. Monthly: review the component list and administrator accounts. Yearly: review maintenance of each component and the restore test. All are noted in the change log.

Each routine has an owner and a note. The weekly update check is Owen's, with the second volunteer as backup. The monthly account review would have caught the volunteer administrator who had not finished setting up multi-factor sign-in. The yearly maintenance review is where a component like event-calendar, quiet for years, would be spotted early.

### 4.5 Putting it together

By the end of the month: multi-factor sign-in for all administrators, a component inventory, donate-form updated, event-calendar replaced, photo-gallery removed, automatic security updates on, and written routines.

Each item has evidence in the change log or the inventory, which is what Owen showed the director and Nadia. The limits are written down too: he cannot check the payment provider's security, he relies on vendors publishing advisories, and he is one person. A second volunteer learning the routines is the answer to the last of these.

### Worked example

Owen presents the month's work to the director and Nadia, opening the change-log entry or inventory row behind each result and reading out the three limits. The director agrees to ask a second volunteer to learn the routines so they continue if Owen is away.

> **Synthetic case.** Components, checklists and outcomes are synthetic.

### Errors and limits

A passed checklist means the known steps were done, not that the site is perfectly safe.

### Exercises

- **EX039 — Download source.** Where did Owen download the update? *Rubric:* 3 = official plugin page; 2 = partial; 1 = vague; 0 = none.
- **EX040 — Hash check.** How did Owen check the download? *Rubric:* 3 = compare SHA-256 with vendor's; 2 = partial; 1 = vague; 0 = none.
- **EX041 — Lab outcome.** What did the checklist report? *Rubric:* 3 = NOT READY: admin MFA; 2 = partial; 1 = vague; 0 = none.
- **EX042 — Holding release.** What did Owen do about the failed item? *Rubric:* 3 = waited for volunteer setup; reran; 2 = partial; 1 = vague; 0 = none.
- **EX043 — Checklist purpose.** Why use a checklist? *Rubric:* 3 = nothing skipped under pressure; 2 = partial; 1 = vague; 0 = none.
- **EX044 — Weekly routine.** What is the weekly routine? *Rubric:* 3 = check and apply security updates after staging; 2 = partial; 1 = vague; 0 = none.
- **EX045 — Monthly routine.** What happens monthly? *Rubric:* 3 = review components and admin accounts; 2 = partial; 1 = vague; 0 = none.
- **EX046 — Month results.** Name four results of the month. *Rubric:* 3 = MFA, inventory, update, replace, remove, auto-updates, routines; 2 = three; 1 = one; 0 = none.
- **EX047 — Limits named.** Name two limits Owen gave. *Rubric:* 3 = payment provider; vendor advisories; one person; 2 = one; 1 = vague; 0 = none.
- **EX048 — Continuity.** How will routines continue if Owen is away? *Rubric:* 3 = second volunteer learns them; 2 = partial; 1 = vague; 0 = none.
- **EX049 — What passing means.** What does a passed checklist mean? *Rubric:* 3 = known steps done, not perfect safety; 2 = partial; 1 = vague; 0 = none.
- **EX050 — Larger projects.** Which tools automate integrity checks for larger projects? *Rubric:* 3 = SLSA, Sigstore; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Check before each release and keep simple routines going.

### Continue studying — chapter 04 of 04

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX050. Owen Clarke, Nadia Haddad, Riverside Food Network, Kestrel Skills Centre and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Nobody knew which components the site used or who updated them.

**EX002.** The platform, plugins, themes, services and how each arrives and updates.

**EX003.** A06 outdated components, A07 authentication failures, A08 integrity failures.

**EX004.** How likely, how much harm, and how cheap the fix is.

**EX005.** Enable multi-factor sign-in, list plugins and versions, ask about automatic updates.

**EX006.** Know components, keep them updated, check what is installed, plan for problems.

**EX007.** Components, data and dependencies.

**EX008.** The site is built almost entirely from other people's components.

**EX009.** Future flaws will never be fixed.

**EX010.** An update or file changed before it arrives.

**EX011.** It is cheap and protects administrator accounts strongly.

**EX012.** Some risks need more effort than they first seem to.

**EX013.** She agreed they were the right first steps.

**EX014.** An email from the director naming what he will check and change.

**EX015.** The website, administrator accounts, plugins and theme, and the host account.

**EX016.** The payment provider's systems and volunteers' personal devices.

**EX017.** A private copy of the site with donor data replaced by synthetic records.

**EX018.** He restored it to staging.

**EX019.** With the payment provider, not on the site.

**EX020.** To track each change so problems can be traced and undone.

**EX021.** Stop, preserve evidence and contact the host and his tutor.

**EX022.** Tools that try to break into the site.

**EX023.** To be told before changes donors could notice.

**EX024.** It is never copied to personal devices; tests use synthetic records.

**EX025.** They state what customers are allowed to test.

**EX026.** So any problem can be traced to a single change.

**EX027.** Name, version and active state for plugins, plus theme, platform version and outside services.

**EX028.** Update from 3.2.0 to 3.2.4.

**EX029.** It has had no release for 1,606 days.

**EX030.** Remove it, since it is not in use.

**EX031.** Directly to the payment provider's page.

**EX032.** Only if the donor opts in.

**EX033.** Outdated dependencies are common because updating takes effort.

**EX034.** Popular, actively maintained ones.

**EX035.** It stored volunteers' phone numbers.

**EX036.** Moved to the volunteer system and deleted from the website.

**EX037.** Update, replace or remove.

**EX038.** Files added by hand.

**EX039.** From the plugin's official page.

**EX040.** By comparing its SHA-256 hash with the vendor's published hash.

**EX041.** NOT READY because admin accounts did not all use MFA.

**EX042.** Held the release until setup was finished, then reran the checklist.

**EX043.** So nothing is skipped under time pressure.

**EX044.** Check for updates and apply security updates after staging.

**EX045.** Review the component list and administrator accounts.

**EX046.** MFA for admins, inventory, donate-form updated, calendar replaced, gallery removed, auto-updates, routines.

**EX047.** He cannot check the payment provider, relies on vendor advisories, and is one person.

**EX048.** A second volunteer will learn the routines.

**EX049.** The known steps were done, not that the site is perfectly safe.

**EX050.** Approaches like SLSA and Sigstore.

<a id="references"></a>

## References

Links checked 12 October 2026; re-verify editions before citing. Organisations, people, systems, code and data in this book are synthetic unless a sentence cites a public source.

- Decan, A., Mens, T., & Constantinou, E. (2018). On the impact of security vulnerabilities in the npm package dependency network. *Proceedings of the 15th International Conference on Mining Software Repositories (MSR '18)*, 181–191. <https://doi.org/10.1145/3196398.3196401>
- Jacobs, J., Romanosky, S., Edwards, B., Adjerid, I., & Roytman, M. (2021). Exploit Prediction Scoring System (EPSS). *Digital Threats: Research and Practice*, 2(3), 1–17. <https://doi.org/10.1145/3436242>
- Johnson, B., Song, Y., Murphy-Hill, E., & Bowdidge, R. (2013). Why don't software developers use static analysis tools to find bugs? *35th International Conference on Software Engineering (ICSE)*, 672–681. <https://doi.org/10.1109/ICSE.2013.6606613>
- Kula, R. G., German, D. M., Ouni, A., Ishio, T., & Inoue, K. (2018). Do developers update their library dependencies? *Empirical Software Engineering*, 23(1), 384–417. <https://doi.org/10.1007/s10664-017-9521-5>
- Ladisa, P., Plate, H., Martinez, M., & Barais, O. (2023). SoK: Taxonomy of attacks on open-source software supply chains. *IEEE Symposium on Security and Privacy*, 1509–1526. <https://doi.org/10.1109/SP46215.2023.10179304>
- Lamb, C., & Zacchiroli, S. (2022). Reproducible builds: Increasing the integrity of software supply chains. *IEEE Software*, 39(2), 62–70. <https://doi.org/10.1109/MS.2021.3073045>
- Landis, J. R., & Koch, G. G. (1977). The measurement of observer agreement for categorical data. *Biometrics*, 33(1), 159–174. <https://doi.org/10.2307/2529310>
- MITRE. (2024). *CWE Top 25 Most Dangerous Software Weaknesses*. <https://cwe.mitre.org/top25/>
- Newman, Z., Meyers, J. S., & Torres-Arias, S. (2022). Sigstore: Software signing for everybody. *ACM SIGSAC Conference on Computer and Communications Security (CCS '22)*, 2353–2367. <https://doi.org/10.1145/3548606.3560596>
- NTIA. (2021). *The minimum elements for a software bill of materials (SBOM)*. U.S. Department of Commerce. <https://www.ntia.gov/report/2021/minimum-elements-software-bill-materials-sbom>
- Ohm, M., Plate, H., Sykosch, A., & Meier, M. (2020). Backstabber's knife collection: A review of open source software supply chain attacks. *DIMVA 2020*, LNCS 12223, 23–43. <https://doi.org/10.1007/978-3-030-52683-2_2>
- OpenSSF. (2023). *SLSA: Supply-chain Levels for Software Artifacts, version 1.0*. <https://slsa.dev/spec/v1.0/>
- OWASP Foundation. (2020). *Software Assurance Maturity Model (SAMM) v2.0*. <https://owaspsamm.org/model/>
- OWASP Foundation. (2020). *Web Security Testing Guide v4.2*. <https://owasp.org/www-project-web-security-testing-guide/>
- OWASP Foundation. (2021). *Application Security Verification Standard 4.0.3*. <https://owasp.org/www-project-application-security-verification-standard/>
- OWASP Foundation. (2021). *OWASP Top 10:2021*. <https://owasp.org/Top10/>
- OWASP Foundation. (2025). *Application Security Verification Standard 5.0.0*. <https://owasp.org/www-project-application-security-verification-standard/>
- Shostack, A. (2014). *Threat modeling: Designing for security*. Wiley. ISBN 978-1-118-80999-0.
- Souppaya, M., Scarfone, K., & Dodson, D. (2022). *Secure Software Development Framework (SSDF) version 1.1* (NIST SP 800-218). NIST. <https://doi.org/10.6028/NIST.SP.800-218>
- Thompson, K. (1984). Reflections on trusting trust. *Communications of the ACM*, 27(8), 761–763. <https://doi.org/10.1145/358198.358210>
- Torres-Arias, S., Afzali, H., Kuppusamy, T. K., Curtmola, R., & Cappos, J. (2019). in-toto: Providing farm-to-table guarantees for bits and bytes. *28th USENIX Security Symposium*, 1393–1410. <https://www.usenix.org/conference/usenixsecurity19/presentation/torres-arias>
- Wermke, D., Wöhler, N., Klemmer, J. H., Fourné, M., Acar, Y., & Fahl, S. (2022). Committed to trust: A qualitative study on security & trust in open source software projects. *IEEE Symposium on Security and Privacy*, 1880–1896. <https://doi.org/10.1109/SP46214.2022.9833686>
- Zimmermann, M., Staicu, C.-A., Tenny, C., & Pradel, M. (2019). Small world with high risks: A study of security threats in the npm ecosystem. *28th USENIX Security Symposium*, 995–1010. <https://www.usenix.org/conference/usenixsecurity19/presentation/zimmerman>
