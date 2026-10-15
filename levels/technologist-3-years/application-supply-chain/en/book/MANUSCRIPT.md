# Application and Software Supply Chain Security: Technologist Course

- Language: English (`en`); course 083, Technologist course (3 years).
- Editorial state: **published**. Chapters 1–30 of 30 have hand-written teaching text; exercises EX001–EX090 have matching worked results with 0–3 rubrics; seven offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: technologist students learning to build, run and improve practical application and software supply chain security in a small development organisation.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Ethical and legal boundary: test and review only software you are authorised to assess; no exploit code, no payloads, no attack procedures and no instructions for bypassing controls. Weaknesses are taught from the defender's side using synthetic code and data. All evidence, people and organisations are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order: the chapters follow one student on placement at a web agency, from a slow manual search for clients affected by a library advisory, through foundations, inventory, checks, pipeline controls, monitoring, automation and evaluation, to a handoff, a field response and a capstone. Run each lab where it appears, attempt the three exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Diego Ramos** | Technologist student on placement | Invented |
| **Aiko Mori** | Placement mentor | Invented |
| **Brightwave Digital** | Fictional web agency | Invented |
| **Southport Polytechnic** | Fictional polytechnic | Invented |
| **Greenleaf Veterinary Group** | Fictional client | Invented |

### Core sources

[OWASP Top 10:2021](https://owasp.org/Top10/); OWASP [ASVS](https://owasp.org/www-project-application-security-verification-standard/) 4.0.3 and 5.0.0; OWASP [WSTG](https://owasp.org/www-project-web-security-testing-guide/) and [SAMM](https://owaspsamm.org/); NIST [SP 800-218 (SSDF)](https://doi.org/10.6028/NIST.SP.800-218); [CWE Top 25](https://cwe.mitre.org/top25/); [SLSA v1.0](https://slsa.dev/spec/v1.0/); Shostack, *Threat Modeling: Designing for Security* (Wiley, 2014). Full list in [References](#references).

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

You will (1) describe the parts of a hosted web application; (2) explain how client projects share components; (3) identify where third-party code runs; (4) introduce the course case.

### 1.1 The case

Diego Ramos is a technologist student at the fictional Southport Polytechnic. His three-year course includes a long placement at the fictional Brightwave Digital, a small agency that builds and hosts websites and web apps for local organisations. His mentor is Aiko Mori, Brightwave's lead developer. In January, a penetration tester hired by Brightwave's client, the fictional Greenleaf Veterinary Group, reported that the booking site's pet-record upload feature used upload-kit 3.1.0, a library with a published high-severity advisory. Brightwave fixed Greenleaf within a day, but then needed three days of manual searching to find which other client projects used the same library. One more, museum-tickets, was affected. Diego's course follows how Brightwave makes such questions answerable in minutes.

### 1.2 Parts of a web app

Each client site has a browser front end, an application server, a database and file storage, running on a cloud hosting account managed by Brightwave. Code lives in repositories; a build service turns code into deployable packages. For Greenleaf these parts map onto the January problem directly. The pet-record upload runs in the application server, the uploaded files land in file storage, and upload-kit is one of the libraries packaged into the server by the build service. Diego learns to ask, for each part, who at Brightwave configures it and which client data passes through it.

### 1.3 Shared components

Brightwave reuses libraries across clients: the same upload library, forms library and date utilities appear in many projects. Reuse saves time but means one flaw affects many clients at once. The January advisory showed the real cost of this sharing for Brightwave's clients. Because upload-kit sat in a common starting template, the same flaw could have been present in any project built from it, and nobody could say which ones without opening every repository. Later in the placement Diego counts how many clients each library serves, because the widest-shared libraries are where one advisory creates the most work.

### 1.4 Third-party code

Most code in each project comes from open-source packages. Zimmermann et al. (2019) showed that a small number of packages and maintainers can reach a large share of an ecosystem; agencies concentrate this risk further by reusing the same packages across clients. For Greenleaf, the nine direct libraries on Diego's diagram pull in further libraries of their own, so the code actually installed is much larger than the list the developers chose. A flaw can arrive through any of them, which is why later chapters track transitive dependencies as well as direct ones.

### 1.5 Responsibility

Brightwave is responsible to each client for keeping their site secure, including the libraries it chose. Contracts say so. That responsibility is why the Greenleaf report reached Brightwave rather than the library's authors: the clinic paid Brightwave to run a safe booking site and expects the agency to notice and fix flawed components. Brightwave cannot fix upload-kit itself, but it chooses which version each client runs and how quickly an update reaches production. In January it could not even tell the clinic, or its other clients, which sites ran the flawed version. Diego's placement work therefore treats every client contract as a promise that depends on knowing the agency's own components.

### 1.6 What was missing

Brightwave had no central list of which client used which library version. Each project's manifest held the answer, but nobody had combined them. The pieces of the answer already existed in January, spread across separate repositories. Every one of the 23 client repositories declared its libraries, yet the search took three days because each repository had to be opened, its manifest read and the upload-kit version compared by hand. Nothing joined those manifests into a single view that could be queried when an advisory arrived. Building that missing view becomes Diego's first real task and the base for almost everything later in the course.

### Worked example

Diego's first task is to draw one client system end to end: the Greenleaf booking site. His diagram shows the browser, server, database, file storage, payment link and nine direct libraries. Aiko asks him to add arrows showing where uploaded files go, which reveals that uploads are stored in the same storage bucket as the site's images.

> **Synthetic case.** Southport Polytechnic, Brightwave Digital, Greenleaf Veterinary Group, their staff, projects and all events are synthetic.

### Errors and limits

Diagrams show intended design; real configuration can differ and must be checked.

### Exercises

- **EX001 — January problem.** What made the January advisory hard to handle? *Rubric:* 3 = no central list; 3 days manual search; 2 = partial; 1 = vague; 0 = none.
- **EX002 — Reuse trade-off.** What is the trade-off of reusing libraries across clients? *Rubric:* 3 = saves time; one flaw affects many; 2 = partial; 1 = vague; 0 = none.
- **EX003 — Upload storage.** What did the arrows reveal? *Rubric:* 3 = uploads stored with site images; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Know the parts of each system, the shared components and where third-party code runs.

### Continue studying — chapter 01 of 30

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Networks and internet services

### Learning outcomes

You will (1) explain how browsers reach hosted apps; (2) describe DNS, HTTPS and content delivery; (3) explain how build services download packages; (4) identify network controls for apps and builds.

### 2.1 Reaching a site

A visitor types the Greenleaf booking address. DNS translates the name to an address; the browser connects over HTTPS, checking the certificate; a content delivery network may serve images; the request reaches the app server. Each step is a place where something can go wrong for the clinic's visitors. A wrong DNS answer sends them elsewhere, a broken certificate makes the browser warn them away, and a slow app server delays bookings. Diego traces this path once for Greenleaf so he knows which Brightwave account controls each step.

### 2.2 HTTPS

HTTPS encrypts traffic and lets the browser confirm it reaches the real site. Brightwave renews certificates automatically and monitors expiry. For the Greenleaf booking site this matters because visitors type owners' phone numbers and upload pet records into the page. Without HTTPS, those details would cross networks readable and changeable by anyone on the path. Automatic renewal removes the old risk of a forgotten certificate expiring on a busy clinic morning, and expiry monitoring catches the rare case where renewal itself fails.

### 2.3 DNS control

Client domains are managed in Brightwave's DNS account with two-person approval and multi-factor sign-in, since a changed DNS record could send visitors to a fake site. One wrong record in this account could redirect the Greenleaf booking page, including its upload form, to a copy run by someone else. Visitors would see the clinic's address in their browser and have no reason to doubt it. That is why changes need a second person's approval rather than resting on a single developer's sign-in, even for small routine edits.

### 2.4 Package downloads

Build services download packages from public registries over HTTPS. Lockfile hashes let the build check that what arrives is what was recorded. This is where upload-kit entered every affected project: the build fetched it from the public registry exactly as the lockfile recorded. The hash check protects against a changed download, but it does not judge whether the recorded version is safe. A flawed version such as upload-kit 3.1.0 matches its hash perfectly, so integrity checks and advisory checks solve different problems.

### 2.5 Network controls

App servers accept web traffic only through the hosting platform's load balancer; databases are not reachable from the internet; build machines can reach only package registries and code hosts. Each rule limits what an attacker could reach from one foothold. If a flaw in the Greenleaf app were misused, the database would still accept connections only from the app, and the build machines could not be used to browse arbitrary sites. Diego writes down each rule's purpose so later changes keep it.

### 2.6 Outbound calls

Some apps call external services (payments, email). Each allowed destination is listed, which limits server-side request forgery (OWASP Top 10:2021 A10). Before Diego's check, Greenleaf's app could connect to any address on the internet, so a flaw that let someone steer its requests would have had no limit. After the change it may reach only the three services it really uses, and anything else is refused. A new external service now needs an explicit list change, which also creates a record of when each destination was added.

### Email security

Client sites send booking confirmations by email. Brightwave configures each sending domain with standard email authentication records so receiving servers can check messages really come from the clinic, which makes it harder for others to send convincing fake booking emails in the clinic's name. Diego checks the records for all clients and finds two missing.

### Worked example

Diego checks Greenleaf's outbound rules and finds the app can connect anywhere. He lists the three services it actually uses and Aiko restricts outbound traffic to them; the app works normally afterwards.

> **Synthetic case.** Network settings are synthetic.

### Errors and limits

Network controls limit damage but cannot fix flaws in the application itself.

### Exercises

- **EX004 — DNS protection.** How are client DNS records protected? *Rubric:* 3 = two-person approval; MFA; 2 = partial; 1 = vague; 0 = none.
- **EX005 — Build downloads.** How do builds check downloaded packages? *Rubric:* 3 = HTTPS plus lockfile hashes; 2 = partial; 1 = vague; 0 = none.
- **EX006 — Outbound fix.** What did Diego change for Greenleaf? *Rubric:* 3 = restricted outbound to three services; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Control names, connections and downloads; list allowed destinations.

### Continue studying — chapter 02 of 30

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming foundations

### Learning outcomes

You will (1) write small, clear functions; (2) validate input; (3) keep secrets out of code; (4) use version control and review.

### 3.1 Clear code

Diego writes small functions with one job each and names that say what they do. Clear code is easier to review, and reviewers catch more problems in short changes. In Diego's booking code this means one function checks the pet name, another checks the date and a third checks the time slot. When Aiko later finds the past-date bug, she finds it quickly because the date logic sits in one short function with an obvious name. Short functions also make the tests in this chapter easier to write, because each rule can be tested on its own.

### 3.2 Input validation

The booking form accepts a pet name, a date and a time slot. Each field is checked on the server against what is allowed: a name of 1–40 letters, spaces or hyphens; a date within the next 60 days; a slot from the clinic's list. OWASP ASVS input-validation requirements describe this allowlist approach. Each rule is checked again on the server even though the browser form shows hints, because a request can be sent without the form at all. Anything outside these rules is rejected before the booking reaches the database, so later code can rely on clean values.

### 3.3 Secrets

API keys for email and payments are read from environment variables set in the hosting platform, never written in code. A pre-commit check warns if anything key-like is added. Before this rule, a key pasted into a test file would have stayed in the repository history even after deletion. The hosting platform keeps Greenleaf's email and payment keys separate from other clients' keys. The pre-commit check is a safety net rather than the main control, since it only recognises key-like patterns it was written to find.

### 3.4 Version control

Every change is a commit with a message explaining why. Pull requests are reviewed by another developer before merging. For security work, this commit and review history is useful evidence as well. When the January advisory arrived, commit messages showed when upload-kit had been added to the Greenleaf project and by whom, and the pull request review shows that the version had not been questioned at the time. Diego writes messages that a future reader could use the same way, naming the library and the reason for every version change.

### 3.5 Tests

Each validation rule has tests for valid values, edge values and invalid values. For the pet-name rule, valid tests include a short name, edge tests include one letter and exactly forty, and invalid tests include forty-one characters and digits. For the date rule, the tests Diego adds after review reject yesterday and accept today. The tests run on every pull request, so a later change that loosens a rule fails before it reaches a client. A test that fails names the rule and the value, so the developer can see at once which change broke it.

### 3.6 Error messages

Errors tell the user which field is wrong without repeating unsafe input back into the page. On the Greenleaf form, a rejected pet name produces a message saying the name may contain only letters, spaces and hyphens, without echoing what was typed. Echoing raw input into the page is how harmful script can end up running in a visitor's browser. The message stays useful to the clinic's customers while giving nothing extra to someone probing the form. Server logs keep the full detail of each rejection, so developers can still investigate problems without exposing it to visitors.

### Dependencies in code

When adding a library, Diego checks whether a few lines of his own code would do instead. Every library added is code someone else maintains, which Brightwave must then track and update for every client using it. Aiko's rule: add a library only when it saves real work and is actively maintained.

### Commit hygiene

Each commit should contain one logical change, making review and rollback easier.

### Worked example

In review, Aiko spots that Diego's date check accepts dates in the past. He adds the rule and two tests (yesterday rejected, today accepted).

> **Synthetic case.** Code and reviews are synthetic.

### Errors and limits

Validation reduces bad input but does not replace output encoding and parameterised queries.

### Exercises

- **EX007 — Name rule.** What is the pet-name rule? *Rubric:* 3 = 1–40 letters, spaces or hyphens; 2 = partial; 1 = vague; 0 = none.
- **EX008 — Secret storage.** Where are API keys kept? *Rubric:* 3 = environment variables in hosting platform; 2 = partial; 1 = vague; 0 = none.
- **EX009 — Review catch.** What did Aiko catch? *Rubric:* 3 = past dates accepted; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Clear, validated, reviewed code with secrets kept out of the repository.

### Continue studying — chapter 03 of 30

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Data models

### Learning outcomes

You will (1) model project dependencies as structured data; (2) query manifests across projects; (3) answer "who uses this version?"; (4) keep the data current.

### 4.1 Manifests as data

Each project has a manifest listing its libraries and versions. Treated as data, manifests from all projects can be combined into one inventory. In Brightwave's case each manifest is already a small structured file listing names and versions, so the work is mainly collecting them in one place. The lab does exactly that with four synthetic projects and asks one question of the combined data. Scaling the same idea to all 23 client projects is what the nightly inventory does. Each row in the combined data names the project, the library and the installed version.

### 4.2 Version ranges

Advisories state affected ranges, such as "at least 2.0.0 and below 3.2.0". Versions must be compared as numbers, part by part, not as text. Comparing as text gives wrong answers: "3.10.0" sorts before "3.2.0" because the character 1 comes before 2. The lab splits each version at the dots and compares the parts as integers, so 2.9.8 correctly falls inside the range and 3.4.2 falls outside it. The same comparison runs in the audit lab later, so getting it right once protects every later check. A version string with letters, such as a hotfix label, would break this simple parser, which is why the drift lab treats such labels separately.

### Lab — who is affected?

```python
"""Find which client projects use an affected library version (synthetic manifests)."""
import json
manifests = json.loads('''{"greenleaf-booking": {"upload-kit": "3.1.0", "forms": "2.2.0"},
 "harbour-cafe": {"forms": "2.4.1"}, "kiteschool-site": {"upload-kit": "3.4.2"},
 "museum-tickets": {"upload-kit": "2.9.8", "forms": "2.4.1"}}''')
def v(s): return tuple(map(int, s.split(".")))
affected = (v("2.0.0"), v("3.2.0"))  # >=2.0.0, <3.2.0
for proj, deps in sorted(manifests.items()):
    ver = deps.get("upload-kit")
    if ver:
        hit = affected[0] <= v(ver) < affected[1]
        print(f"{proj:18} upload-kit {ver:6} {'AFFECTED' if hit else 'ok'}")
```

Run with `python3 lab_inventory.py`. Verified output:

```text
greenleaf-booking  upload-kit 3.1.0  AFFECTED
kiteschool-site    upload-kit 3.4.2  ok
museum-tickets     upload-kit 2.9.8  AFFECTED
```

### 4.3 Lab result

Three projects use upload-kit. greenleaf-booking (3.1.0) and museum-tickets (2.9.8) fall in the affected range; kiteschool-site (3.4.2) is above it and safe. harbour-cafe does not use upload-kit. In January this took three days by hand; the script answers in under a second. The lab also shows its own limits, which Diego notes beside the result. It checks only upload-kit and only the four synthetic projects written into it, so a project missing from the data would be missed silently. The answer is only as good as the manifests: an outdated copy of a project's file would give a confident but wrong result. That is why the full inventory reads lockfiles fresh every night.

### 4.4 Keeping current

The inventory is rebuilt nightly from every repository's lockfile, so it reflects exactly what each project installs. Rebuilding from lockfiles rather than manifests matters because a manifest may allow a range of versions while the lockfile records the one actually installed. The nightly run also catches change: when a project updates upload-kit, the next morning's inventory shows the new version without anyone editing a spreadsheet. A run that fails is reported, so a stale inventory is never mistaken for a current one.

### 4.5 Data quality

Projects without lockfiles show as "unknown" and are fixed first, since their real versions cannot be known. Diego's full run finds two such projects among the 23, and Aiko adds lockfiles to both that week. Until then their rows are treated as possibly affected by every advisory for their declared libraries, which is the safe assumption. An inventory with unexplained gaps would repeat January's problem in a quieter form, because nobody would know which answers to trust. Each unknown row also names the project owner who must add the missing lockfile.

### The inventory schema

Each inventory row has: project, client, library, installed version, direct or transitive, and date checked. Transitive dependencies matter because many flaws arrive through libraries that other libraries bring in. Diego adds a column for the owner of each project, so alerts reach the right developer quickly. He also adds a query that lists every library used by more than five clients, because a flaw in one of those would be the most disruptive.

### Answering quickly

With the inventory, Diego can answer three questions for any advisory: which clients, which versions, and who owns each project. Aiko times it on a test advisory: four minutes from advisory to a list of owners notified.

### Worked example

Diego runs the full inventory: 23 client projects, 412 distinct library versions. Two projects lack lockfiles; Aiko adds them that week.

> **Synthetic case.** Projects and versions are synthetic.

### Errors and limits

Manifests list declared dependencies; code copied directly into projects will not appear.

### Exercises

- **EX010 — Lab result.** Which projects were affected? *Rubric:* 3 = greenleaf-booking, museum-tickets; 2 = one; 1 = vague; 0 = none.
- **EX011 — Text comparison.** Why not compare versions as text? *Rubric:* 3 = wrong ordering e.g. 3.10 vs 3.2; 2 = partial; 1 = vague; 0 = none.
- **EX012 — Missing lockfiles.** Why fix projects without lockfiles first? *Rubric:* 3 = real versions unknown; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Treat manifests as data so "who is affected?" takes seconds.

### Continue studying — chapter 04 of 30

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) explain core application security concepts; (2) use the OWASP Top 10:2021 categories; (3) read advisories and CWE names; (4) explain supply-chain risk to clients.

### 5.1 Core ideas

Confidentiality (pet owners' details), integrity (bookings, prices and the code itself) and availability (clinics need bookings to work). Each of the three ideas maps onto a concrete harm for Greenleaf. A leak of owners' phone numbers or pet medical notes breaks confidentiality. A changed price, a booking moved to another day, or a library altered before it reached the build breaks integrity. A booking page that stops working during a busy morning breaks availability and sends clients to phone the clinic instead. Diego uses these three words when he explains to clients why a library update matters to them.

### 5.2 OWASP Top 10:2021

Categories include Broken Access Control (A01), Injection (A03), Insecure Design (A04), Security Misconfiguration (A05), Vulnerable and Outdated Components (A06) and Software and Data Integrity Failures (A08). The January upload-kit case is an A06 problem. Naming the category helps Diego find the right guidance quickly instead of treating each advisory as a new kind of problem. When Diego meets a new finding, he names its category before deciding what to do, because each category's page lists typical causes and defences. The CSV export found later in the course, which any staff account could reach, is a Broken Access Control problem (A01), while the unsigned payment callback relates to Software and Data Integrity Failures (A08).

### 5.3 Advisories

An advisory lists the package, affected and fixed versions, severity and a description. Diego learns to read the fixed version first: it tells you what to upgrade to. For upload-kit, the January advisory gave the affected range as at least 2.0.0 and below 3.2.0, which made 3.2.0 the fixed version to install. Diego also notes the publication date, because it starts the remediation clock that Brightwave later measures for every client. He reads the description last and only to judge whether the affected feature is used by a given client. A severity score alone does not tell him whether that feature is used.

### 5.4 CWE

The CWE Top 25 names weaknesses such as unrestricted upload of dangerous file types (CWE-434), relevant to Greenleaf's upload feature. Advisories often name a CWE, so the identifier links a specific library flaw to a general class of weakness and its documented defences. CWE-434 points Diego towards checking type, content and storage for every upload, not only for the upload-kit version that was flagged. That is the thinking behind the upload checks built later in the course. Diego notes the CWE identifier in each task, so similar findings can later be grouped.

### 5.5 Supply chain risk

Ohm et al. (2020) and Ladisa et al. (2023) describe how attackers target packages, build systems and distribution, not just applications. Defenders respond with inventories, updates, integrity checks and provenance. For Brightwave, the January case was the simplest kind of supply chain problem: an honest library with a published flaw. The literature also describes deliberately harmful versions and compromised build systems, which an inventory alone would not stop. That is why Brightwave adds pinning, review of dependency changes and recorded builds alongside the inventory.

### 5.6 Talking to clients

Clients want to know: are we affected, what did you do, do we need to do anything? Diego practises answering these in three sentences. For Greenleaf the three answers were yes, the library was updated on 14 January, and no action was needed. The note Diego later drafts for Greenleaf follows exactly that order of answers. For harbour-cafe, which never used upload-kit, the honest answer to the first question was simply no. Each answer is a plain sentence without jargon, and none promises more than the record shows. If Brightwave does not yet know whether a client is affected, the answer says so and gives a time for the follow-up.

### Severity in context

An advisory's severity is general. For a given client, Diego asks whether the affected feature is used and whether it is reachable from the internet. upload-kit's flaw mattered for Greenleaf because uploads were open to any visitor booking an appointment.

### Learning sources

Diego follows the advisory feeds for the ecosystems Brightwave uses and reads the OWASP Top 10 pages for each category he meets in practice.

### Worked example

Diego drafts the note to Greenleaf: "A library used in your booking site's upload feature had a published security flaw. We updated it on 14 January and checked that uploads still work. You do not need to take any action." Aiko approves it unchanged.

> **Synthetic case.** The note is synthetic.

### Errors and limits

The Top 10 is an awareness list; use ASVS for detailed requirements.

### Exercises

- **EX013 — Category.** Which Top 10 category is the upload-kit case? *Rubric:* 3 = A06; 2 = partial; 1 = vague; 0 = none.
- **EX014 — CWE-434.** What is CWE-434? *Rubric:* 3 = unrestricted upload of dangerous file types; 2 = partial; 1 = vague; 0 = none.
- **EX015 — Client questions.** What three questions do clients ask? *Rubric:* 3 = affected? what done? action needed?; 2 = two; 1 = one; 0 = none.

### Synthesis

Shared vocabulary lets you read advisories and explain risk to clients.

### Continue studying — chapter 05 of 30

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Operating systems and virtualization

### Learning outcomes

You will (1) explain processes, permissions and containers for hosted apps; (2) apply least privilege; (3) isolate builds and client workloads; (4) keep base images patched.

### 6.1 Processes and permissions

Each client app runs as a process under its own user with limited permissions. It can read its code and write only to its upload and log folders. If a flaw is misused, the damage stays within these rights. Diego checks this for the Greenleaf app by listing what its user may change. For Greenleaf, that user can write uploaded X-rays and reports to the upload folder and append to its log folder, but cannot change its own code or configuration. A misused flaw in upload handling would therefore be unable to rewrite the application or plant files elsewhere on the host. Diego confirms this by checking the folder permissions rather than relying on the deployment notes.

### 6.2 Containers

Brightwave packages each app as a container image built from a small base image. Containers isolate client apps from each other on shared hosts, so a problem in one client's app does not reach another's files. Each image includes only the app, its libraries and a small operating system base, so fewer packages need updating than on a full server installation. Each image is recorded by digest, so Brightwave can later tell exactly which base and libraries each client release used. When an image needs updating, the whole container is replaced rather than patched in place, which keeps every running copy identical to what the build produced.

### 6.3 Virtual machines

The hosting platform runs containers on virtual machines; the cloud provider is responsible for isolating machines between customers, Brightwave for everything inside its account. Diego uses this split when clients ask who handles hosting security. Anything below the virtual machine belongs to the provider; the containers, images, network rules and accounts are Brightwave's to configure and check. The split also decides who answers which question when a client asks about hosting. Questions about the physical hardware go to the provider's published documentation, while questions about Greenleaf's containers, network rules and accounts are Brightwave's to answer from its own records.

### 6.4 Build isolation

Builds run in fresh containers that are deleted afterwards, so nothing left by one build affects the next. SLSA v1.0 build requirements describe isolated, hosted builds as a foundation for trustworthy artifacts. For Brightwave, fresh build containers also protect clients' projects from each other. A build for one client's project starts from an empty container, so a file or setting left by a previous build of another project cannot slip into it. Isolated builds are also the first step towards the recorded, verified builds that become one of Diego's three placement goals.

### 6.5 Patching

Base images are rebuilt weekly with operating system updates, and each image is recorded by digest so Brightwave knows which image every release used. Recording the digest matters when an operating system advisory appears: Brightwave can see which releases used an affected base image and rebuild exactly those. Weekly rebuilds also keep each update small, so a breaking change is easier to spot. A weekly rebuild also means an image never goes more than about a week without the latest operating system fixes. If a rebuilt image breaks a client app, the previous digest is still recorded and can be redeployed while the problem is fixed.

### 6.6 Upload handling

Uploaded files are stored outside the app's code folder and are never executed. The storage bucket for uploads is separated from site images after Diego's chapter 1 finding. Before the split, a harmful upload sat beside the files the site serves to every visitor. Greenleaf's X-rays and reports now live in a bucket that holds nothing else and is never served as part of the site. Stored files also receive new random names, so an uploaded file cannot choose its own path or overwrite another one. Serving them only as downloads means the browser never treats an upload as part of the site.

### Image checks

Besides the administrator check, the build also rejects images based on unsupported operating system versions, so no client stays on a base that no longer receives updates.

### Worked example

Diego finds that one older client app runs as the administrator user inside its container. He changes it to a dedicated user, fixes the two folders whose permissions then need adjusting, and adds a build check that fails if any image runs as administrator.

> **Synthetic case.** Systems and findings are synthetic.

### Errors and limits

Containers share the host's kernel; they reduce risk but are not perfect isolation.

### Exercises

- **EX016 — App permissions.** What can each app process write to? *Rubric:* 3 = upload and log folders only; 2 = partial; 1 = vague; 0 = none.
- **EX017 — Isolation purpose.** Why use containers for client apps? *Rubric:* 3 = isolate clients from each other; 2 = partial; 1 = vague; 0 = none.
- **EX018 — Admin finding.** What did Diego change in the older app? *Rubric:* 3 = run as dedicated user; build check; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Least privilege, isolation and patched images limit damage.

### Continue studying — chapter 06 of 30

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Identity and access foundations

### Learning outcomes

You will (1) manage developer and client access to systems; (2) apply multi-factor authentication; (3) use roles and least privilege; (4) review access regularly.

### 7.1 Developer access

Developers sign in to code hosting, the build service and the hosting platform with multi-factor authentication. Each has only the roles needed: most can deploy to test environments; only two can deploy to production. Limiting production deployment to two developers means a stolen test-environment account cannot change a live client site. When the former contractor's access is found in the first review, this split is why the exposure was limited to deploy rights on three projects rather than every client.

### 7.2 Client access

Clinic staff log into their booking admin pages with their own accounts; shared logins are not allowed. OWASP Top 10:2021 A07 covers identification and authentication failures. Personal accounts mean Greenleaf's log shows which receptionist changed a booking. A shared login would hide that, and nobody could remove one leaver's access without changing everyone's password. When a receptionist leaves a clinic, the manager disables that one account without disturbing anyone else's work. OWASP's description of A07 lists shared and weak credentials among common causes, which is why Brightwave refuses shared clinic logins even when a client asks for one to save time.

### 7.3 Service accounts

The build service uses a dedicated identity with permission to push images, not a developer's personal token. Before this change, an image push from the build ran under whichever developer had set the pipeline up. If that developer left, the pipeline either broke or kept a leaver's credential alive. A dedicated build identity can be given exactly the rights to push images and nothing more, and its use appears separately in the platform's logs. If the build identity were ever misused, its permissions would limit the damage to pushing images, which the approved-image rule later checks as well.

### 7.4 Tokens

Long-lived tokens are replaced with short-lived ones where the platform allows, reducing harm if a token leaks. A short-lived token copied into a log or a chat message by mistake stops working within hours rather than staying valid for months. Diego lists which of Brightwave's platforms still require long-lived tokens so they can be rotated on a schedule instead. A long-lived token found in an old repository would remain dangerous long after anyone remembered creating it. Short-lived tokens make the build identity's access expire on its own unless the pipeline requests a new one for the next run.

### 7.5 Access reviews

Every quarter Diego lists who has which access and asks owners to confirm. Leavers' access is removed on their last day. The first review is the one that finds the former contractor still able to deploy to three client projects. Diego's list goes to each platform owner, who confirms every name individually. Owners are asked to confirm each person and role, not to approve the whole list at once. Leavers are checked against the leaver checklist, so a missing tick shows which platform still needs attention. The review record is kept, so the next quarter's review can compare names and show what changed in between.

### 7.6 Role design

Roles for clinic staff: receptionist (manage bookings), vet (view records), manager (settings and staff). Checks happen on the server. Greenleaf's roles also decide who could reach the old CSV export that Diego's data-flow diagram later uncovers. Because the export checked only that a user was logged in, receptionists could download every booking, which their role never needed. Checks on the server, not hidden buttons in the page, are what stop a receptionist's account from reaching manager functions. Diego tests each of the three roles with a synthetic account before release.

### Leaver checklist

The leaver checklist now lists every place access might exist: code hosting, the build service, the hosting platform, the image registry, client admin pages used for support, and shared password vaults. Each line is ticked by a named person on the leaver's last day, and the record is kept with the access review. Diego also asks the platform owners to send a monthly list of accounts with no sign-in in 60 days, since unused accounts are often forgotten accounts. The first such list finds four, all removed after confirming with their owners.

### Worked example

The first access review finds a former contractor still able to deploy to three client projects. Access is removed the same day, and the leaver checklist gets a line for build and hosting access.

> **Synthetic case.** Accounts and findings are synthetic.

### Errors and limits

Access reviews only help if owners check carefully; ask them to confirm each name, not approve the list in bulk.

### Exercises

- **EX019 — Production deploy.** Who can deploy to production? *Rubric:* 3 = only two developers; 2 = partial; 1 = vague; 0 = none.
- **EX020 — Build identity.** What identity does the build service use? *Rubric:* 3 = dedicated identity, not personal token; 2 = partial; 1 = vague; 0 = none.
- **EX021 — Review finding.** What did the first review find? *Rubric:* 3 = former contractor with deploy access; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Strong sign-in, least privilege and regular reviews keep access under control.

### Continue studying — chapter 07 of 30

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Security architecture basics

### Learning outcomes

You will (1) apply layered defences to client apps; (2) place trust boundaries; (3) separate environments and clients; (4) document a standard architecture.

### 8.1 Layers

Edge protections (HTTPS, rate limiting), application controls (validation, authorisation, encoding), data protection (encryption, least-privilege database accounts) and pipeline controls (reviews, dependency checks, isolated builds). For the Greenleaf upload feature, each layer adds a separate obstacle. The edge limits request rates, the application checks file type and size, the data layer keeps uploads in their own bucket, and the pipeline flags an outdated upload library. If one layer misses a problem, another still has a chance to catch it. Diego lists each layer's controls per client, so gaps in any layer are visible.

### 8.2 Trust boundaries

Boundaries exist between visitor and app, app and database, app and external services, build and production, and between clients. Each boundary gets a check. The January flaw crossed the visitor-to-app boundary, because any visitor could upload a file. The library itself crossed the boundary from the public registry into Brightwave's build. Diego marks both on his diagrams so each gets a named check. Other boundaries matter as much: between build and production, the approved-image rule decides what may run, and between clients, separate databases and buckets stop one site reading another's data. A boundary without a named check is treated as a gap to fix.

### 8.3 Separating clients

Each client has its own database, storage bucket and secrets. A flaw in one client's app cannot read another client's data. This is exactly what was missing for the two small clients Diego finds sharing one database with separate tables. A flaw in either site could have read the other's records. Splitting them into separate databases restores the rule and removes an exception nobody had recorded. Separate secrets mean a leaked key for one client cannot send email or take payments for another. Separate buckets mean an upload flaw in one site cannot list or read another client's files.

### 8.4 Environments

Test and production are separate, with separate secrets and data; test uses synthetic data only. Keeping test data synthetic matters for Greenleaf, whose real data includes pet medical notes. A developer debugging a booking bug in test never sees a real owner's details, and a leaked test database exposes nothing real. Separate secrets also mean a test key cannot send real confirmation emails or take real payments by mistake. Production deployment rights are also limited to two developers, which keeps the environments separate in practice and not only on paper.

### 8.5 Standard architecture

Brightwave writes a one-page standard for new projects, so security decisions are made once and reused. The standard covers the decisions that came up repeatedly in client projects: separate database, bucket and secrets, least-privilege database accounts, HTTPS and rate limits at the edge, server-side authorisation, and a pinned and reviewed pipeline. Writing these down once means a new project inherits them rather than relying on each developer to remember. Each line of the standard points to the ASVS requirement it comes from, so a developer who wants the reasoning can follow it. Aiko reviews the checklist before a new project's first production deployment.

### 8.6 Exceptions

Projects that differ from the standard record why. An exception records what differs, why, which extra checks compensate and who approved it. A client needing an external payment provider is a typical example that Brightwave accepts. The shared database Diego found was different: an unrecorded exception that nobody had decided on, which is why it was fixed rather than written down. Recorded exceptions are reviewed with the standard so that temporary ones do not quietly become permanent. Each recorded exception also names a review date when it is checked again.

### Applying the standard

For each new project, the lead developer fills in a short checklist against the standard: separate database, bucket and secrets; least-privilege database account; HTTPS and rate limits at the edge; server-side authorisation; reviewed and pinned pipeline. Aiko reviews the checklist before the project's first production deployment. Where a client needs something different, such as an external payment provider, the difference and its extra checks are written down. Over the year, the checklists also serve as evidence when clients ask how their site is protected, which saves the team time answering security questionnaires.

### Why one page

A one-page standard is short enough that developers actually read it. Longer guidance lives in linked notes, and each line of the standard points to the ASVS requirement it comes from.

### Worked example

Applying the standard to existing clients, Diego finds that two small clients share one database with separate tables. They are split into separate databases during the next maintenance window.

> **Synthetic case.** The architecture is synthetic.

### Errors and limits

A standard helps only if followed; check new projects against it.

### Exercises

- **EX022 — Four layers.** List the four layers. *Rubric:* 3 = edge, application, data, pipeline; 2 = three; 1 = one; 0 = none.
- **EX023 — Client separation.** How are clients separated? *Rubric:* 3 = own database, bucket, secrets; 2 = two; 1 = one; 0 = none.
- **EX024 — Shared database.** What was found and fixed? *Rubric:* 3 = two clients sharing a database; split; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Layer controls, guard boundaries and separate clients by default.

### Continue studying — chapter 08 of 30

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Evidence and measurement

### Learning outcomes

You will (1) measure dependency freshness and remediation; (2) choose measures that drive the right behaviour; (3) collect evidence automatically; (4) present trends.

### 9.1 Freshness

How old is each installed library version? Old versions miss fixes and are more likely to be affected by advisories. Kula et al. (2018) found developers often leave dependencies outdated. The lab measures this for Greenleaf on 1 March 2026. upload-kit's installed version was released on 2 June 2024, 637 days earlier, which places it among the oldest libraries in the booking site. Age is easy to measure from the inventory and release dates, which makes it a practical first signal for a small agency. Diego treats it as a prompt to look closer, not as proof that a library is unsafe, because some old versions have no known flaws. The 365-day threshold the team agreed marks where that closer look becomes routine.

### Lab — version age

```python
"""Days since each dependency's installed version was released, flagging versions older than 365 days (synthetic)."""
from datetime import date
today = date(2026, 3, 1)
deps = {"upload-kit": date(2024, 6, 2), "forms": date(2025, 11, 20), "date-utils": date(2023, 1, 15), "mailer": date(2026, 2, 3)}
for name, released in sorted(deps.items(), key=lambda d: d[1]):
    age = (today - released).days
    print(f"{name:11} {age:4} days {'STALE' if age > 365 else ''}")
```

Run with `python3 lab_age.py`. Verified output:

```text
date-utils  1141 days STALE
upload-kit   637 days STALE
forms        101 days 
mailer        26 days
```

### 9.2 Lab result

For Greenleaf, date-utils is 1,141 days old and upload-kit 637 days; both are flagged stale (over 365 days). forms is 101 days old and mailer 26 days. upload-kit's age explains why the January advisory found it vulnerable. The lab calculates each age by subtracting the release date from 1 March 2026, so date-utils, released on 15 January 2023, is the oldest by a wide margin. The stale flag uses a strict comparison, so an age of exactly 365 days would not be marked stale. Under the stricter 180-day threshold Diego uses for upload, authentication and payment libraries, upload-kit's 637 days would be flagged even more clearly. forms at 101 days and mailer at 26 days pass either threshold. The lab hard-codes the release dates, so Diego checks each against the registry before trusting the result.

### 9.3 Remediation time

Days from an advisory's publication to the fix being deployed, per severity. For Brightwave the clock starts when an advisory is published and stops when the fixed version is deployed to a client, not when the pull request is merged. Measured this way, January's upload-kit case shows the gap clearly: the Greenleaf fix took a day, but finding museum-tickets took three more. Reporting the measure per severity lets the team check it against the target of seven days for high advisories.

### 9.4 Behaviour

Measures can drive the wrong behaviour: counting "libraries updated" could encourage risky bulk updates without tests. Brightwave measures outcomes: stale count and remediation time. Stale count rewards keeping libraries current, and remediation time rewards fixing what advisories actually flag. Neither rewards touching many libraries at once without tests, which is the behaviour a raw update count would encourage. Before choosing measures, the team asks what a developer would do to improve each number quickly. If the quick route is unsafe, the measure is rejected or paired with one that would catch it.

### 9.5 Automatic evidence

Measures come from the nightly inventory and deployment records, not manual reports. Because the figures come from the same nightly inventory and deployment records used for daily work, nobody has to compile them by hand, and nobody can make a month look better by choosing what to report. If the inventory misses a project, the measures miss it too, which is why the missing-project count matters later in the course. The records also carry dates, so each figure can be traced back to its source.

### 9.6 Presenting

A monthly chart shows stale libraries and remediation times across clients. The chart covers all 23 client projects and shows stale counts falling from 64 towards 18 over six months, alongside remediation times by severity. Aiko uses it in the monthly team meeting to show which projects need attention, and the two legacy projects stand out because most of the remaining stale versions sit there. Each chart shows the threshold and the date of the data, so readers can compare months fairly. Showing both figures together stops one improving while the other quietly worsens.

### Choosing thresholds

The 365-day stale threshold is a starting point that the team agreed together. For libraries handling uploads, authentication or payments, Diego uses a stricter threshold of 180 days, because flaws there matter more. Thresholds are reviewed each quarter against what the advisories actually show: if many advisories hit versions younger than the threshold, it is too loose. The lab's docstring states the 365-day threshold it applies, so anyone reading the code knows which rule produced the STALE flags.

### Reading the lab

The lab compares each installed version's release date with today's date and prints the age in days and a status. Diego checks that the dates are correct before trusting the result.

### Worked example

After six months of weekly updates, the number of stale library versions across all clients falls from 64 to 18. The remaining 18 are mostly in two legacy projects scheduled for rebuild.

> **Synthetic case.** Ages and counts are synthetic.

### Errors and limits

Age is a rough proxy; a new version can still have flaws, an old one may be fine.

### Exercises

- **EX025 — Lab stale.** Which libraries were stale? *Rubric:* 3 = date-utils 1,141; upload-kit 637; 2 = one; 1 = vague; 0 = none.
- **EX026 — Bad measure.** Why not count libraries updated? *Rubric:* 3 = encourages risky bulk updates; 2 = partial; 1 = vague; 0 = none.
- **EX027 — Six-month result.** What did six months of updates achieve? *Rubric:* 3 = stale 64 to 18; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Measure freshness and remediation from automatic evidence.

### Continue studying — chapter 09 of 30

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Application and software supply chain security: orientation

### Learning outcomes

You will (1) define application and software supply chain security; (2) map the stages from code to client site; (3) place frameworks on the map; (4) see Brightwave's gaps.

### 10.1 Definitions

Application security protects the software's design and code. Supply chain security protects everything that goes into it and how it reaches users: source, dependencies, build, artifacts, deployment and updates. The January case needed both views, application security and supply chain security together. Greenleaf's upload feature was application code, while upload-kit arrived through dependencies and was built and deployed without anyone recording it. A team focused only on its own code would have missed the library entirely. Both views use the same evidence about Brightwave's projects, but they ask different questions of it. Application security asks whether the booking form handles uploads safely, while supply chain security asks where upload-kit came from and which clients received it.

### 10.2 The stages

For Brightwave: developers write code; libraries are fetched; the build service builds images; images go to a registry; deployment puts them on hosting; updates repeat the cycle. upload-kit passed through every stage: a developer added it, the build fetched it, images carried it, and deployments placed it on Greenleaf and museum-tickets. At no stage was the version recorded where anyone could query it across clients. Each stage also needs evidence that can be checked later: lockfiles for libraries, digests for images and deployment records for hosting. Missing evidence at any stage leaves a gap that the January search had to fill by hand.

### 10.3 Frameworks

NIST SP 800-218 (SSDF) groups practices into Prepare the Organization, Protect the Software, Produce Well-Secured Software and Respond to Vulnerabilities. SLSA v1.0 focuses on build integrity and provenance. OWASP SAMM v2 assesses maturity. OWASP ASVS defines application requirements. Each framework answers a different question for Brightwave, so Diego uses them together rather than choosing one. Diego uses the SSDF to find gaps, SLSA to set build goals, SAMM to judge maturity and ASVS to write application checks. Each framework supplies one piece, and none of them alone would cover the whole January case. He keeps a short table linking each placement goal to the framework that informed it.

### 10.4 Brightwave's gaps

Mapping to the SSDF shows strengths in producing software (reviews, tests) but gaps in responding: no inventory before January, no target times for fixes. The upload-kit search is the clearest evidence of the responding gap: three days to find affected clients, and no agreed deadline for fixing them once found. The strengths in producing software were real, but code reviews and tests had never been asked to question a library's version or its advisories. Mapping also showed which existing strengths, such as reviews and tests, to keep.

### 10.5 Trust

Thompson (1984) reminded developers that you cannot fully trust code you did not create; evidence such as hashes and provenance is how trust is earned. For Brightwave this means trusting a library because a hash matches what was recorded, and trusting a deployed image because its digest matches a pipeline build, rather than trusting either because it carries a familiar name. Thompson's point applies even to Brightwave's own tools, since the build service and its actions are code the agency did not write. That is why pipeline actions are later pinned and reviewed like libraries.

### 10.6 The course plan

The next chapters build Brightwave's inventory, checks, controls and monitoring. The order follows the January lesson: an inventory comes first because no audit, fix target or monitor can work without knowing which client runs which version. Checks and pipeline controls follow, then monitoring and automation, and the final chapters test whether the whole arrangement survives a real-style advisory, a handoff and an assessment. Each chapter adds one control and tests it on the same client projects, so later chapters can measure what earlier ones changed. The three placement goals agreed in this chapter are the yardstick used again when the field event and the capstone are assessed.

### Where the case fits

The upload-kit incident touches several stages: an outdated library was fetched, built into images and deployed without anyone recording which clients had it. The fix therefore needs work at several stages, not just one patch. That is why the course moves through inventory, checks, build controls and monitoring in order.

### Worked example

Diego and Aiko agree three goals for the placement year: an inventory answering "who is affected" in minutes, fixes for high advisories within 7 days across all clients, and verified, recorded builds for every deployment.

> **Synthetic case.** Goals are synthetic.

### Errors and limits

Frameworks describe what good looks like; small agencies must choose what is proportionate.

### Exercises

- **EX028 — Stages.** List the stages for Brightwave. *Rubric:* 3 = code, libraries, build, registry, deploy, update; 2 = four; 1 = two; 0 = none.
- **EX029 — SSDF gap.** Where were Brightwave's SSDF gaps? *Rubric:* 3 = Respond: no inventory, no fix targets; 2 = partial; 1 = vague; 0 = none.
- **EX030 — Three goals.** State the three placement goals. *Rubric:* 3 = inventory minutes; highs in 7 days; verified builds; 2 = two; 1 = one; 0 = none.

### Synthesis

Map the chain and frameworks, then set goals for the gaps.

### Continue studying — chapter 10 of 30

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Application and software supply chain security: assets and context

### Learning outcomes

You will (1) list the assets in client apps and the supply chain; (2) rate their importance; (3) record owners and context; (4) use context to prioritise work.

### 11.1 Data assets

Greenleaf's booking site holds owners' names, phone numbers and emails, pet medical notes, uploaded X-rays and reports, and appointment histories. Medical notes and uploads are the most sensitive because they are private and hard to replace. The harbour-cafe site, by contrast, holds only table bookings with a name and phone number. The difference changes how Diego treats the same advisory in each project. A flaw in Greenleaf's upload feature could expose X-rays and medical notes that owners cannot easily replace, while the same flaw at harbour-cafe would expose names and phone numbers for table bookings. Both clients deserve a fix, but the Greenleaf fix comes first.

### 11.2 Supply chain assets

Code repositories, the library registry configuration, the build service, signing and deployment credentials, the image registry and the hosting accounts are all assets. A weakness in any of them could change every client's site at once, which makes them more important than any single client app. The build service alone touches all 23 client projects, so a change to its configuration reaches every site at the next deployment. Deployment credentials can put any image on any client's hosting. That reach is why these assets get Aiko's ownership and the strictest access rules in the agency.

### 11.3 Rating importance

Diego rates each asset high, medium or low using two questions: how much harm if it were exposed or changed, and how many clients depend on it. Deployment credentials score high on both; a single client's public image folder scores low. The two questions give a simple grid that every owner can apply consistently. Deployment credentials are high on harm and on client count. Greenleaf's upload bucket is high on harm but serves one client. A single client's public image folder is low on both, since its contents are already public and only one site uses it. Diego writes one line of reasoning beside each rating so others can challenge it.

### 11.4 Owners

Every asset has a named owner who decides about access and changes. The build service is owned by Aiko; each client app by its lead developer. Named owners are what made the four-minute test advisory possible: the inventory could say who should receive each alert. The build service's owner, Aiko, decides who may change pipeline settings, and each lead developer decides when a client's update is deployed. Where an owner leaves, the access review flags the gap and a new owner is named before the asset is left unwatched.

### 11.5 Context records

The inventory gains a short context note per project: data held, internet exposure, the client's contact for incidents, and any contract requirements such as response times. For Greenleaf the note records medical notes and uploads, a public booking form, the clinic manager as incident contact, and the contract's response time. For harbour-cafe it records only table bookings with a name and phone number. Diego keeps each note to a few lines so owners actually update it when a project changes.

### 11.6 Using context

When an advisory arrives, context decides the order of work: projects with sensitive data and public exposure come first. The order is applied even when every project will eventually be patched. During the form-library advisory, Greenleaf and museum-tickets were patched the same day, while three brochure sites with no forms in use waited for the weekly cycle. Writing the order down beforehand avoids arguing about priorities while an advisory is open. Exposure also counts: a site whose affected feature is not reachable from the internet can wait for the weekly cycle.

### Worked example

Context changes the order of work during the next advisory, which affects a form library used by eight clients. Greenleaf and museum-tickets, holding medical notes and payment references, are patched the same day; the three small brochure sites with no forms in use are patched in the weekly cycle.

> **Synthetic case.** Assets and ratings are synthetic.

### Errors and limits

Ratings are judgements; record the reasoning so others can challenge them.

### Exercises

- **EX031 — Most sensitive.** Which Greenleaf assets are most sensitive? *Rubric:* 3 = medical notes and uploads; 2 = one; 1 = vague; 0 = none.
- **EX032 — Supply chain importance.** Why do supply chain assets rate highly? *Rubric:* 3 = affect all clients at once; 2 = partial; 1 = vague; 0 = none.
- **EX033 — Context order.** How did context order the form-library patching? *Rubric:* 3 = sensitive same day; brochure sites weekly; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Know assets, owners and context so priorities follow real harm.

### Continue studying — chapter 11 of 30

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Application and software supply chain security: data flows

### Learning outcomes

You will (1) draw data flows for a client app and the build pipeline; (2) mark trust boundaries; (3) find where checks are needed; (4) keep diagrams current.

### 12.1 Application flow

For Greenleaf: the visitor's browser sends a booking form and an upload to the web app; the app checks it, stores the booking in the database and the file in the upload bucket; staff view bookings through the admin pages; the app sends a confirmation through the email service. Each arrow on the diagram names the data it carries: owner details and pet notes, uploaded files, bookings to the admin pages, and only email address and appointment time to the email service.

### 12.2 Pipeline flow

A developer pushes code; the build service fetches code and libraries, runs tests and checks, builds an image, pushes it to the registry, and the deployment step pulls the image onto hosting. Secrets are injected only at deployment. The flow shows where upload-kit entered: at the step where the build service fetched libraries. Secrets entering only at deployment means a build that runs tests on a pull request never holds a production key, so a mistaken or harmful change cannot read one during testing.

### 12.3 Trust boundaries

Marked boundaries: browser to app, app to database and bucket, app to email service, public library registry to build, build to registry, registry to hosting. Shostack (2014) recommends drawing such diagrams as the starting point for asking what can go wrong. Diego draws the two flows on one page so that the library registry, an outside party, appears as clearly as the visitor's browser. Each boundary is a place where one party hands data or code to another that should not simply trust it. The visitor may send a harmful file, the registry may serve a flawed library, and the registry-to-hosting step may receive an image nobody approved. Naming these handovers is what lets the next step assign a check to each.

### 12.4 Checks at boundaries

Each boundary needs a check: validation and size limits for uploads; least-privilege database accounts; pinned and verified libraries entering the build; recorded digests for images entering hosting. For Greenleaf, the upload boundary uses the type, content and size checks built later in the course. The registry-to-build boundary uses lockfile hashes and the audit against advisories. The registry-to-hosting boundary uses the approved-image rule, which refuses any digest that the main-branch build did not produce. A boundary without one of these checks is listed as a gap for the next review.

### 12.5 Keeping current

Diagrams live in each repository and are updated in the same pull request that changes a flow. Reviewers ask "does the diagram still match?" when a change adds a service. Keeping the diagram in the same pull request means reviewers see the change to the flow beside the change to the code. When Brightwave later adds the mapping service for kiteschool-site, the diagram gains an arrow and a boundary in the same review, along with a note of what data goes to the provider.

### 12.6 Common surprises

Drawing flows often reveals forgotten paths, such as an old export feature or a test webhook still enabled. At Greenleaf, the forgotten path was an old CSV export that any logged-in staff account could reach. It had worked for years without anyone thinking about who used it. Diego now asks owners, for every client diagram, to list features nobody has used recently, because those are the paths most likely to have been left without a check. Test webhooks left enabled after a launch are another common example the team now checks for.

### Worked example

Drawing the Greenleaf flow reveals a forgotten path: an old CSV export endpoint that lists all bookings, reachable by any logged-in staff account including receptionists. It is restricted to managers and its use logged.

> **Synthetic case.** Flows are synthetic.

### Errors and limits

A diagram is a model; walk through the running system to check it.

### Exercises

- **EX034 — Pipeline entry.** Where do libraries enter the pipeline? *Rubric:* 3 = public registry to build boundary; 2 = partial; 1 = vague; 0 = none.
- **EX035 — Upload check.** What check guards the upload boundary? *Rubric:* 3 = validation and size limits; 2 = partial; 1 = vague; 0 = none.
- **EX036 — Forgotten path.** What did the Greenleaf diagram reveal? *Rubric:* 3 = CSV export reachable by any staff; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Draw flows, mark boundaries and put a check on each.

### Continue studying — chapter 12 of 30

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Application and software supply chain security: risk scenarios

### Learning outcomes

You will (1) write risk scenarios for client apps and the supply chain; (2) estimate likelihood and impact; (3) link scenarios to controls; (4) review them.

### 13.1 Writing scenarios

A scenario says what could happen, through which weakness, and what harm follows: "An outdated upload library with a known flaw lets a visitor's upload affect the server, exposing medical records." Scenarios describe outcomes, not procedures. Diego keeps each scenario to one or two sentences and names Greenleaf's data where relevant, so readers can picture the harm without needing technical detail. Describing outcomes keeps the register safe to share with clients and students, because it records harm and weakness rather than any method of causing it. The January scenario names the outdated library, the public upload form and the medical records together, which is enough to decide which controls matter. A scenario that cannot name its harm is rewritten before it is rated.

### 13.2 Supply chain scenarios

Ladisa et al. (2023) catalogue attacks on open-source supply chains, such as a library maintainer's account being taken over and a harmful version published. Ohm et al. (2020) studied real malicious packages. Brightwave writes scenarios for these kinds of events at the level of "a harmful library version enters a build". These scenarios differ from the January case because the harmful version may have no advisory yet. An inventory alone would show which clients installed it, but only pinning, review and an adoption delay could stop it entering a build in the first place. Brightwave does not try to model the attacker's method; it records which of its own controls would apply.

### 13.3 Likelihood and impact

Each scenario gets low, medium or high for likelihood and impact, using evidence: advisories seen, exposure, data held, number of clients. For the outdated-library scenario, the January advisory, Greenleaf's public upload form, medical notes and 23 projects sharing libraries all point to high likelihood and high impact. A scenario about the internal status page scores lower on exposure, because only staff and client contacts can reach it. Each rating cites its evidence so the next review can test whether it still holds.

### 13.4 Linking controls

Each scenario lists its controls: for a harmful library version, pinned versions with hashes, a short delay before adopting brand-new versions, and review of dependency changes. Writing the controls beside each scenario shows quickly which ones are missing. Before this course, the harmful-version scenario had review of code changes but no review of lockfile changes and no adoption delay, so two of its three controls were gaps. Each control is also linked to the chapter of the course where it is built, so progress can be checked against the plan.

### 13.5 Review

Scenarios are reviewed every six months and after any incident. The six-month review asks whether each rating still matches the evidence, whether any control has been added or lost, and whether any new advisory or incident fits no existing scenario. After an incident the review happens within weeks rather than waiting, so lessons reach the register while the details are fresh. The review compares each rating with the evidence gathered since the last one. After the form-library advisory, for example, the scenario about shared libraries keeps its high rating because eight clients were affected at once. A control that has stopped working, such as a pipeline check someone disabled, moves its scenario back up the list.

### 13.6 Ranking

The top five scenarios get named owners and target dates for missing controls. Ranking keeps the register from becoming a list nobody acts on. With about fifteen rows, the top five are a manageable set for a small agency. Each owner reports progress at the monthly meeting, and a missed target date is discussed there rather than quietly moved. The top-ranked scenario, an outdated library with a known flaw in a public client app, is owned by Aiko, with Diego building its first controls. Ranking is revisited at each review, so a scenario whose controls are all in place can drop out of the top five and free attention for the next one.

### Scenario register

Scenarios are kept in a shared register with columns for the scenario, likelihood, impact, evidence, controls in place, missing controls, owner and review date. The register is short, about fifteen rows, so it is actually read. When a new advisory or incident does not fit any existing scenario, a new row is added, which shows where earlier thinking missed something.

### Worked example

The top-ranked scenario is "an outdated library with a known flaw in a public client app", rated high likelihood and high impact because of the January case. Its controls (inventory, audits, weekly updates) are the first built in this course.

> **Synthetic case.** Scenarios and ratings are synthetic.

### Errors and limits

Ratings are estimates; record the evidence behind each.

### Exercises

- **EX037 — Scenario parts.** What does a scenario state? *Rubric:* 3 = what, weakness, harm; 2 = two; 1 = one; 0 = none.
- **EX038 — Harmful version controls.** Name controls for a harmful library version. *Rubric:* 3 = pinning with hashes; adoption delay; review; 2 = two; 1 = one; 0 = none.
- **EX039 — Top scenario.** What was the top-ranked scenario? *Rubric:* 3 = outdated library with known flaw in public app; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Scenarios link evidence to controls and priorities.

### Continue studying — chapter 13 of 30

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Application and software supply chain security: methods I

### Learning outcomes

You will (1) validate file uploads safely; (2) check type, content and size; (3) store uploads safely; (4) test the checks with synthetic files.

### 14.1 Why uploads matter

The Greenleaf flaw was in upload handling. Even with a patched library, Brightwave wants its own checks so that a future library flaw is less likely to be reachable. OWASP ASVS 4.0.3 section V12 covers files and resources. The January flaw showed that Brightwave relied entirely on upload-kit to handle uploads safely. Adding its own checks means the next library flaw would have to get past Brightwave's rules as well, which makes the flaw less likely to be reachable from the public booking form.

### 14.2 The checks

Allow only listed types (PNG, JPEG, PDF); check that the file content matches the claimed type by its leading bytes; limit size to 5 MB; give stored files new random names; store them outside the web root and serve them with a safe download header. Each of these checks addresses a different problem with uploaded files. The type allowlist rejects files the clinic never needs, the content check rejects files whose leading bytes do not match their name, the size limit protects storage and processing, and random names stop an upload from choosing where it lands.

### Lab — upload checks

```python
"""Validate synthetic uploaded files: extension allowlist, size limit and content signature."""
SIG = {".png": b"\x89PNG", ".pdf": b"%PDF"}
files = [("xray.png", b"\x89PNG....", 120_000), ("report.pdf", b"%PDF-1.7", 900_000),
         ("notes.pdf", b"PK\x03\x04", 40_000), ("scan.png", b"\x89PNG....", 9_000_000), ("run.exe", b"MZ..", 10_000)]
for name, head, size in files:
    ext = name[name.rfind("."):]
    if ext not in SIG: verdict = "reject: type not allowed"
    elif size > 5_000_000: verdict = "reject: too large"
    elif not head.startswith(SIG[ext]): verdict = "reject: content does not match type"
    else: verdict = "accept"
    print(f"{name:11} {verdict}")
```

Run with `python3 lab_upload.py`. Verified output:

```text
xray.png    accept
report.pdf  accept
notes.pdf   reject: content does not match type
scan.png    reject: too large
run.exe     reject: type not allowed
```

### 14.3 Lab result

xray.png and report.pdf are accepted. notes.pdf is rejected because its content does not match a PDF. scan.png is rejected as too large. run.exe is rejected because the type is not allowed. Every rejection names its reason, which helps support staff explain it to clinic users. The order of checks matters: run.exe is rejected on type before its content is ever examined. The lab's signature table covers only PNG and PDF, so JPEG support would need its own entry before JPEG uploads could be accepted.

### 14.4 Testing

Synthetic test files cover each rule. Tests run in the build on every change. For each rule there is at least one file that should pass and one that should fail, mirroring the five lab files. A change that loosens a rule therefore fails the build, and the reviewer sees exactly which test broke. The synthetic files are tiny and contain no real patient data. Diego adds a test whenever a support case shows a file the rules handled wrongly.

### 14.5 Limits

Content checks reduce risk but cannot prove a file is harmless; storage and serving rules provide the second layer. A PDF with correct leading bytes can still contain unexpected content, so a passing check is not a guarantee. That is why accepted files are stored outside the web root with new names and served as downloads, so even a harmful file is never run by the server or rendered as part of the site. The second layer is what protects clinics if a future content check misses something new.

### Reviewing the rules

The allowed types and size limit are reviewed with each client, since clinics, museums and cafes need different files. Every change to the rules goes through review with updated tests.

### Shared module

The checks live in one shared module used by all client projects, so a fix reaches everyone at the next deployment.

### Worked example

After the checks go live, the Greenleaf support log shows clinic users occasionally uploading oversized phone photos. Brightwave adds a clear message suggesting how to reduce size instead of raising the limit.

> **Synthetic case.** Files are synthetic.

### Errors and limits

Keep the allowed list short; every added type adds risk.

### Exercises

- **EX040 — Lab rejections.** Why was each file rejected? *Rubric:* 3 = notes mismatch; scan too large; run.exe type; 2 = two; 1 = one; 0 = none.
- **EX041 — Second layer.** What protects if a checked file is still harmful? *Rubric:* 3 = storage outside web root; safe serving; random names; 2 = partial; 1 = vague; 0 = none.
- **EX042 — Oversize response.** How was oversized photo uploads handled? *Rubric:* 3 = clear message, not raised limit; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Validate uploads on type, content and size, and store them safely.

### Continue studying — chapter 14 of 30

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Application and software supply chain security: guided lab

### Learning outcomes

You will (1) run a dependency audit across clients; (2) read advisory matches; (3) total by severity; (4) turn results into tasks.

### 15.1 The audit

The audit compares each client's installed library versions with a synthetic advisory list, each advisory naming a library, affected versions and severity. Each advisory row gives the lowest affected version and the fixed version, the same form used in the inventory lab. Because the advisory list is synthetic, the lab shows the method without depending on any real feed. The audit is the step that turns the inventory into action. The inventory says which version each project runs; the audit says which of those versions an advisory names. Running it nightly means a newly published advisory is matched against every client by the next morning instead of after days of searching.

### Lab — dependency audit

```python
"""Audit all client projects against a synthetic advisory list and summarise by severity."""
projects = {"greenleaf-booking": {"upload-kit": "3.1.0", "forms": "2.2.0"}, "harbour-cafe": {"forms": "2.4.1"},
            "kiteschool-site": {"upload-kit": "3.4.2"}, "museum-tickets": {"upload-kit": "2.9.8", "forms": "2.4.1"}}
adv = [("ADV-7", "upload-kit", "2.0.0", "3.2.0", "high"), ("ADV-8", "forms", "2.0.0", "2.3.0", "medium")]
def v(s): return tuple(map(int, s.split(".")))
count = {}
for p, deps in sorted(projects.items()):
    for aid, pkg, lo, fix, sev in adv:
        if pkg in deps and v(lo) <= v(deps[pkg]) < v(fix):
            print(f"{p:18} {aid} {pkg} {deps[pkg]} -> {fix} ({sev})"); count[sev] = count.get(sev, 0) + 1
print("totals:", count)
```

Run with `python3 lab_audit.py`. Verified output:

```text
greenleaf-booking  ADV-7 upload-kit 3.1.0 -> 3.2.0 (high)
greenleaf-booking  ADV-8 forms 2.2.0 -> 2.3.0 (medium)
museum-tickets     ADV-7 upload-kit 2.9.8 -> 3.2.0 (high)
totals: {'high': 2, 'medium': 1}
```

### 15.2 Lab result

Greenleaf matches ADV-7 (high) and ADV-8 (medium); museum-tickets matches ADV-7. Totals: high 2, medium 1. The output lists project, library, version and advisory, which is exactly what a developer needs to start. museum-tickets also uses forms 2.4.1, which is above ADV-8's fixed version 2.3.0, so it does not match. harbour-cafe uses the same forms version and is likewise clear. kiteschool-site runs upload-kit 3.4.2, above ADV-7's fix. Each output line gives the fixed version after the arrow, so the developer knows the target without opening the advisory. The totals line tells Aiko how much high-severity work is open at a glance.

### 15.3 Turning results into tasks

Each match becomes a task with the owner from the inventory and a due date from the severity: high within 7 days, medium within 30. For the lab results, both ADV-7 matches would be due within 7 days and Greenleaf's ADV-8 match within 30. The owner named in the inventory receives the task, so nobody has to decide who should act. Due dates come from the severity in the advisory, adjusted only when context shows the affected feature is unused. Any such adjustment is written on the task with the reason.

### 15.4 Checking matches

Diego confirms each match by reading the advisory, since version ranges can be written ambiguously. Checking also confirms that the affected feature is actually used. Of the 11 matches in the full audit, one turned out false because the advisory's range excluded the installed patch version. Diego records the reason so the same wording does not mislead the next run. Ambiguity is common at range boundaries, for example whether a range ending at a version includes that version itself. Reading the advisory text settles it before work starts, so developers are not asked to fix projects that were never affected.

### 15.5 Prioritisation

Where many matches arrive at once, Brightwave may consider exploit likelihood scores such as EPSS (Jacobs et al., 2021) alongside severity and client context. Brightwave has not adopted such scores yet, because its match counts are small enough to handle by severity and context. Diego notes EPSS as an option if a single advisory ever matches many projects at once. Severity remains the starting point; any other score would only change the order within a severity group. Client context, such as Greenleaf's medical notes, still decides which project goes first.

### Recording the audit

Each audit run is saved with its date, the advisory list version used and the matches found. When a client asks whether they were affected by an advisory, Brightwave can answer from the record rather than from memory. The record also shows how long each match stayed open, which feeds the remediation-time measure from chapter 9. Diego notices that matches in projects with an active owner close in about four days, while those in projects with no recent work take nearly three weeks, and he raises this with Aiko as a staffing issue.

### Worked example

Running the audit across all 23 client projects returns 11 matches. Diego confirms 10; one is a false match because the advisory's range excludes the installed patch version. Corrected matches become tasks, and all highs are fixed within six days.

> **Synthetic case.** Advisories and matches are synthetic.

### Errors and limits

Audits only find known advisories; they say nothing about unknown flaws.

### Exercises

- **EX043 — Lab totals.** What totals did the lab give? *Rubric:* 3 = high 2, medium 1; 2 = partial; 1 = vague; 0 = none.
- **EX044 — Due dates.** What due dates apply? *Rubric:* 3 = high 7 days; medium 30; 2 = partial; 1 = vague; 0 = none.
- **EX045 — False match.** Why was one match false? *Rubric:* 3 = range excluded installed version; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Audit, confirm, assign and fix by severity.

### Continue studying — chapter 15 of 30

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Application and software supply chain security: methods II

### Learning outcomes

You will (1) pin dependency versions with hashes; (2) use lock files; (3) review dependency changes; (4) delay adoption of brand-new versions.

### 16.1 Lock files

A lock file records the exact version and hash of every direct and transitive library. Builds install exactly what the lock file says, so two builds of the same commit get the same libraries, and a changed file in the registry is detected because its hash no longer matches. For Brightwave, the lockfile is also the raw material for the nightly inventory: it records exactly which upload-kit version each project installed. A project without one was an unknown in the inventory until Aiko added it.

### 16.2 Reviewing changes

Changes to the lock file appear in pull requests. Reviewers look at which libraries changed, whether a new library was added, and whether a new maintainer or install script appeared. Large unexplained changes are questioned. A lockfile change of hundreds of lines for a one-library update deserves a question. Reviewers ask the author to explain what pulled in the extra libraries before approving the change. A new install script deserves particular attention, because it runs code during installation on the build machine. Diego's review of exactly such a change appears in the worked example below.

### 16.3 Adoption delay

Brightwave waits a few days before adopting brand-new library versions unless they fix a security advisory, since harmful versions are often discovered and removed quickly. Ohm et al. (2020) describe how malicious packages are spread. The delay applies to updates opened by the weekly bot, which waits until a new version has been public for a few days. A security fix skips the delay, because leaving a known flaw in place is the larger risk. The delay is a few days, short enough that ordinary updates are not held back for long.

### 16.4 Choosing libraries

Before adding a library, developers check maintenance activity, number of maintainers and how widely it is used. Zimmermann et al. (2019) showed how a few maintainer accounts can reach very large parts of an ecosystem, and Decan et al. (2018) compared dependency networks across ecosystems. Diego writes the answers into the pull request that adds the library, so the reasoning stays with the change. A library with one inactive maintainer and few users needs a stronger reason than one with several active maintainers. This matches Aiko's rule that a library should save real work and be actively maintained.

### 16.5 Removing libraries

Unused libraries are removed; each removal shrinks what must be tracked. Diego's first pass finds libraries that remained in manifests after features using them were removed. Each removal shortens the inventory, reduces advisory matches and makes later reviews faster. A removal still goes through review and tests, since an unused-looking library may be loaded indirectly. Fewer libraries also mean fewer weekly update pull requests to review. Diego asks owners to confirm that each library is unused before it is removed, and the build's tests confirm nothing broke. A removed library also stops appearing in future SBOMs, which keeps each client's component list shorter and easier to explain.

### 16.6 Automated update requests

A bot opens weekly update pull requests with tests run, so updates are small and regular rather than large and rare. Small weekly updates are also easier to review: a pull request changing one library is quick to check, while a yearly update changing dozens is hard to judge. Diego's later research compares projects with these weekly pull requests against projects still updated manually. The bot's pull requests run the full test suite and wait for a human review before merging. An update that fails tests stays open with its failure visible, which is how the date-library time-zone problem was caught before it reached any client.

### Lock file in builds

The build fails if the lock file and the dependency list disagree, so nobody can forget to update it.

### Worked example

Diego reviews an update pull request that adds a new transitive library with an install script. The team pauses, finds the parent library added it for an optional feature, and selects a configuration that avoids it.

> **Synthetic case.** Libraries and changes are synthetic.

### Errors and limits

Pinning stops surprise changes but also stops automatic fixes; pair it with regular updates.

### Exercises

- **EX046 — Lock file purpose.** What does a lock file record? *Rubric:* 3 = exact versions and hashes of all libraries; 2 = partial; 1 = vague; 0 = none.
- **EX047 — Adoption delay.** Why delay brand-new versions? *Rubric:* 3 = harmful versions often found quickly; 2 = partial; 1 = vague; 0 = none.
- **EX048 — Review finding.** What did Diego's review find? *Rubric:* 3 = new transitive library with install script; avoided; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Pin, review and update regularly.

### Continue studying — chapter 16 of 30

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Application and software supply chain security: tooling

### Learning outcomes

You will (1) review build pipeline configuration; (2) pin pipeline actions; (3) limit token permissions; (4) protect secrets from untrusted changes.

### 17.1 The pipeline as code

Each project's pipeline is a configuration file in the repository. It decides which external actions run, which permissions the build token has and which secrets are available. Mistakes here affect every build. Because the configuration sits in the repository, changes to it go through the same review as code changes. The file also decides which branch can deploy, which is why the template restricts deployment to the main branch after review. Because the configuration lives in the repository, a change to it is visible in history, and reviewers can see when a permission was widened or an action changed. Diego's lab reads one such file and reports risky settings in plain language.

### Lab — pipeline review

```python
"""Check a synthetic CI configuration for risky settings."""
ci = {"steps": [{"uses": "checkout@v4"}, {"uses": "setup-node@3f2a9c1e"}, {"uses": "deploy-helper@main"}],
      "secrets_on_pull_requests_from_forks": True, "token_permissions": "write-all"}
issues = []
for s in ci["steps"]:
    ref = s["uses"].split("@")[1]
    if not (len(ref) >= 8 and all(c in "0123456789abcdef" for c in ref)):
        issues.append(f"step {s['uses']} not pinned to a commit")
if ci["secrets_on_pull_requests_from_forks"]: issues.append("secrets exposed to fork pull requests")
if ci["token_permissions"] != "read": issues.append(f"token permissions {ci['token_permissions']} (use read by default)")
for i in issues: print("-", i)
print(len(issues), "issues")
```

Run with `python3 lab_ci.py`. Verified output:

```text
- step checkout@v4 not pinned to a commit
- step deploy-helper@main not pinned to a commit
- secrets exposed to fork pull requests
- token permissions write-all (use read by default)
4 issues
```

### 17.2 Lab result

The lab reports four issues in the synthetic pipeline: checkout@v4 and deploy-helper@main are not pinned to a commit, secrets are available to pull requests from forks, and the token has write-all permissions. Pinning to a full commit identifier means a changed action cannot silently enter the build. The lab treats any reference of at least eight hexadecimal characters as a commit, so setup-node@3f2a9c1e passes. That is looser than a full commit identifier, and Brightwave's template uses full identifiers.

### 17.3 Fixing permissions

The token gets read-only permission by default, with write only for the step that needs it. Write permission is granted only to the deployment step that pushes the image, after review on the main branch. The other steps can read the repository but cannot change it. Applying this across the nine pipelines that had write-all tokens is part of the three-week fix. Read-only by default means a mistaken or harmful step cannot push code or change settings in the repository.

### 17.4 Secrets and untrusted changes

Pull requests from outside contributors run without secrets. Deployment runs only from the main branch after review. Pull requests from forks are code written by people outside Brightwave, so running them with secrets would let an unknown change read deployment keys. Two pipelines exposed secrets this way, and both were fixed on the first day. Main-branch deployment means every change reaching a client has passed review. Contributors from outside still get test results on their pull requests, only without access to any secret.

### 17.5 Applying across projects

Diego runs the review across all 23 pipelines and opens fix pull requests in batches. Batching groups similar fixes, so reviewers see one kind of change at a time across several projects. The secret exposures are fixed first, unpinned actions and write-all tokens follow, and the template stops new projects repeating the same issues. The review script is the lab code extended to read every pipeline file in Brightwave's repositories. Across 23 pipelines it found 41 unpinned actions, 9 write-all tokens and 2 pipelines exposing secrets to forks. Each batch of fix pull requests is reviewed by the project owner.

### Keeping pins current

Pinned actions are updated by the same weekly bot that updates libraries. Each update shows the old and new commit, and reviewers check the action's release notes before approving. This keeps the protection of pinning without leaving old versions in place forever. Diego also writes a short template pipeline with safe defaults (pinned actions, read-only token, no secrets for forks) that new projects copy, so the same mistakes are not repeated. Within two months every new project starts from the template.

### Worked example

Across 23 pipelines, the review finds 41 unpinned actions, 9 write-all tokens and 2 pipelines exposing secrets to forks. All are fixed within three weeks, with the secret exposures fixed on the first day.

> **Synthetic case.** Pipelines and counts are synthetic.

### Errors and limits

Pinning needs updating too; a pinned old action can miss its own fixes.

### Exercises

- **EX049 — Lab issues.** List the four lab issues. *Rubric:* 3 = two unpinned; fork secrets; write-all; 2 = three; 1 = one; 0 = none.
- **EX050 — Token fix.** How were token permissions fixed? *Rubric:* 3 = read-only default, write only where needed; 2 = partial; 1 = vague; 0 = none.
- **EX051 — First fix.** Which issues were fixed first and why? *Rubric:* 3 = secret exposure; most direct harm; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Treat pipeline configuration as security-critical code.

### Continue studying — chapter 17 of 30

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Application and software supply chain security: controls

### Learning outcomes

You will (1) record image digests for every deployment; (2) record build provenance; (3) deploy only approved images; (4) describe SLSA build levels.

### 18.1 Recording digests

Each built image has a digest, a fingerprint of its contents. The deployment record stores the digest, the commit and the build run, so Brightwave can always say exactly what is running. The digest changes if even one byte of the image changes, so it identifies contents exactly. A tag such as a version name can be moved to a different image. Knowing exactly what is running makes the drift check and the monthly tracing possible. Diego's monthly tracing relies on these three fields being present for every deployment.

### 18.2 Provenance

Provenance is a signed statement of how an artifact was built: source, builder and steps. SLSA v1.0 defines build levels: L1 provenance exists, L2 a hosted build service signs it, L3 builds are hardened against tampering between runs. in-toto (Torres-Arias et al., 2019) and Sigstore (Newman et al., 2022) provide ways to create and verify such statements. Brightwave records the source commit, the build service and the build steps for each image. Provenance answers how an artifact was produced; it does not say whether the code inside is free of flaws.

### 18.3 Approved images

Hosting accepts only images whose digests appear in the approved list produced by the main-branch build. This rule is what refuses the locally built test image a developer tries to deploy. It also prevents a repeat of the museum-tickets weekend hotfix, which was built and deployed by hand before the rule existed. The approved list is produced automatically by the main-branch build, so no person edits it by hand. A digest not on the list is refused even if the image came from a trusted developer's laptop. That refusal is the expected outcome, and the developer rebuilds through the pipeline instead.

### 18.4 Brightwave's target

The agency targets SLSA build L2 for all client projects this year. Brightwave already uses a hosted build service and records digests, so the remaining work is to have that service produce signed provenance for every client project. L3, with builds hardened against tampering between runs, is left for after the placement. Reaching L2 for every client project would mean each deployment's provenance is signed by the hosted build service. Brightwave tracks progress in the monthly report, project by project, so laggards are visible.

### 18.5 Exceptions

Emergency changes still go through the build; there are no manual uploads to hosting. During an outage the pipeline may run with a shortened review, but the image is still built by the build service and recorded by digest. The museum-tickets weekend hotfix shows why: a manual upload left a build nobody could trace. After the emergency, the team reviews the change normally, so the shortened review is never the final one. Because nothing reaches hosting except through the build, the drift check and the approved list stay accurate even in an outage.

### 18.6 Evidence

Digest records give clients evidence of what changed and when. When a client asks what changed on their site last month, Brightwave can list each deployment with its date, commit and digest. The same records supported the monthly tracing checks that found one project recording tags instead of digests. Clients ask such questions after incidents or during their own audits. Brightwave can answer from the deployment records in minutes, without relying on anyone's memory. The records also show each change's commit, so a client can be told what the change was meant to do.

### Checking the records

Each month Diego picks three deployments at random and traces each from the running digest back through the registry to the build run and commit. If any link is missing, the gap is fixed in the pipeline. The first check finds one project whose deployment step recorded the image tag but not the digest; because tags can be moved to point at a different image, only the digest identifies the contents reliably. The step is corrected to record digests, and a test is added to the shared pipeline template.

### Worked example

After the approved-image rule is introduced, a developer's attempt to deploy a locally built test image to a client's production is refused. The developer rebuilds through the pipeline, and the event confirms the control works.

> **Synthetic case.** Builds and events are synthetic.

### Errors and limits

Provenance proves how something was built, not that the code is safe.

### Exercises

- **EX052 — Digest record.** What does the deployment record store? *Rubric:* 3 = digest, commit, build run; 2 = two; 1 = one; 0 = none.
- **EX053 — SLSA L2.** What does SLSA build L2 add over L1? *Rubric:* 3 = hosted build service signs provenance; 2 = partial; 1 = vague; 0 = none.
- **EX054 — Refused deploy.** What did the refused deploy show? *Rubric:* 3 = control works; local images blocked; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Record what runs and deploy only what the pipeline built.

### Continue studying — chapter 18 of 30

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Application and software supply chain security: monitoring

### Learning outcomes

You will (1) compare running versions with approved releases; (2) detect drift and unapproved builds; (3) alert owners; (4) investigate differences.

### 19.1 Drift

Drift is when what runs differs from what was approved: a client left behind on an old release, or something running that the pipeline never approved. Both kinds appear in the lab: harbour-cafe left behind on an older release, and museum-tickets running a build the pipeline never approved. Drift matters because every earlier control assumes that what runs is what was built and approved. A client left behind keeps old library versions after the audit says they were fixed, while an unapproved build bypasses review, pinning and digest records entirely.

### Lab — release drift

```python
"""Compare deployed versions with the latest approved release per client (synthetic)."""
approved = {"greenleaf-booking": "5.3.0", "harbour-cafe": "2.1.4", "kiteschool-site": "1.9.0", "museum-tickets": "4.0.2"}
deployed = {"greenleaf-booking": "5.3.0", "harbour-cafe": "2.0.9", "kiteschool-site": "1.9.0", "museum-tickets": "4.0.3-hotfix"}
for c in sorted(approved):
    d, a = deployed[c], approved[c]
    state = "ok" if d == a else ("UNAPPROVED BUILD" if "-" in d else "BEHIND")
    print(f"{c:18} deployed {d:13} approved {a:6} {state}")
```

Run with `python3 lab_drift.py`. Verified output:

```text
greenleaf-booking  deployed 5.3.0         approved 5.3.0  ok
harbour-cafe       deployed 2.0.9         approved 2.1.4  BEHIND
kiteschool-site    deployed 1.9.0         approved 1.9.0  ok
museum-tickets     deployed 4.0.3-hotfix  approved 4.0.2  UNAPPROVED BUILD
```

### 19.2 Lab result

harbour-cafe runs 2.0.9 while 2.1.4 is approved, so it is BEHIND. museum-tickets runs 4.0.3-hotfix, which is not in the approved list, so it is an UNAPPROVED BUILD. Other clients match. The lab treats any version containing a hyphen as an unapproved build, which works for these labels but is a simplification. A real check compares digests with the approved list rather than reading version strings. Reading the output, Diego starts with the unapproved build, because nobody yet knows what it contains. A real check would therefore not depend on how someone chose to name a build.

### 19.3 Investigating

BEHIND usually means a deployment failed or was skipped; UNAPPROVED BUILD needs urgent questions about where the build came from. For harbour-cafe, the cause was a failed database migration that stopped the deployment. For museum-tickets, the cause was a manual weekend build deployed during an outage before the approved-image rule. For a BEHIND client, the owner checks the deployment log and reruns the failed step. For an UNAPPROVED BUILD, Aiko asks who built it, from which code and why, before deciding whether to replace it.

### 19.4 Alerts

A daily check sends drift to the project owner and, for unapproved builds, to Aiko too. Alerts name the client, both versions and the status, so the owner can start without opening the full report. Holds agreed with a client and recorded with an end date stay quiet until that date passes. The daily timing means drift is found within a day of appearing rather than at the next manual check. Sending unapproved builds to Aiko as well reflects that their origin is unknown.

### 19.5 Closing the loop

Each finding is recorded with its cause and fix. Recording causes over time shows patterns, such as failed migrations, that point to fixes beyond the single case. Recording the cause matters because a fix without a cause can return. When harbour-cafe's deployment stalls on a failed migration, the record names the migration and the fix, so a similar stall elsewhere is recognised quickly. The museum-tickets record notes the manual weekend deployment and its replacement by a pipeline build of the same change. Over time the records show which causes recur and which earlier controls have stopped them.

### Tuning alerts

At first, the daily check alerts on every client behind the latest release, including those deliberately held back while a client tests a change. Diego adds an approved hold list with an end date, so expected differences stay quiet while unexpected ones still alert. Holds that pass their end date alert again. This keeps owners trusting the alerts, because almost every alert now needs action. Over the following month, the check raises nine alerts; eight lead to fixes and one to a hold being extended with the client's agreement.

### Reading the lab

The lab compares a list of running versions with the approved list and prints a status per client, quoting both versions.

### Worked example

The museum-tickets hotfix turns out to have been built and deployed manually during a weekend outage before the approved-image rule. It is replaced by a pipeline build of the same change, and the harbour-cafe deployment, stuck on a failed migration, is fixed.

> **Synthetic case.** Versions and causes are synthetic.

### Errors and limits

Monitoring shows differences; people must find the causes.

### Exercises

- **EX055 — Lab drift.** What did the lab report? *Rubric:* 3 = harbour-cafe BEHIND; museum UNAPPROVED BUILD; 2 = one; 1 = vague; 0 = none.
- **EX056 — Unapproved urgency.** Why is an unapproved build urgent? *Rubric:* 3 = unknown origin of what runs; 2 = partial; 1 = vague; 0 = none.
- **EX057 — Hotfix cause.** What caused the museum hotfix? *Rubric:* 3 = manual weekend deploy before rule; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Watch for drift and fix its causes.

### Continue studying — chapter 19 of 30

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Application and software supply chain security: troubleshooting

### Learning outcomes

You will (1) diagnose failing dependency updates and pipeline checks; (2) avoid disabling checks; (3) fix root causes; (4) record lessons.

### 20.1 Common failures

Update pull requests fail tests because of breaking changes; pinned actions break when their own dependencies change; content checks reject unusual but valid files; audit matches turn out false. Each failure has a tempting shortcut: skipping the update, unpinning the action, widening the upload rules or ignoring the audit. The troubleshooting work in this chapter is about finding the cause instead. Diego keeps a list of these failure types so new ones can be compared with what the team has already solved.

### 20.2 Diagnosing

Diego reads the failure, reproduces it locally with synthetic data, and changes one thing at a time. Reproducing with synthetic data keeps real client data out of debugging and lets the failure be run again on demand. Changing one thing at a time means that when the failure stops, Diego knows which change fixed it. Writing down each change and its effect helps if the problem returns later. If the failure cannot be reproduced locally, that difference is itself a clue, often pointing to configuration on the build machine.

### 20.3 Not disabling checks

A failing check is never switched off to make a deadline. If it must be bypassed, Aiko approves a time-limited exception with a ticket. The ticket records which check, which project, why it is bypassed and the expiry date. When the date passes, the exception ends automatically and the check runs again. Exceptions are listed in the monthly report, so expired or repeated ones are noticed. The rule exists because a disabled check rarely gets switched back on once the deadline has passed and attention moves elsewhere.

### 20.4 Breaking changes

For a major library update, the developer reads the change notes and updates code in a separate pull request. Keeping code changes separate from the version bump lets reviewers see which edits the new version required. If the update later causes trouble, the previous approved digest can be redeployed while the code change is investigated. The bot's minor updates stay small, while major ones get their own planned pull request. This keeps the weekly bot's small updates moving while bigger changes get the attention they need.

### 20.5 Recording lessons

Each solved problem gets a short note in the team's troubleshooting page. The date-library time-zone note is the clearest payoff: a month later it saved another developer an afternoon on the same failure. Each note uses the same four fields: symptom, cause, fix and date. Diego writes the note on the day the problem is solved, while the details are fresh, and links it to the pull request that fixed it. The quarterly review removes notes about replaced libraries, so search results stay relevant. Searching the page is the first step when a check fails, before anyone starts debugging from scratch.

### 20.6 Knowing when to ask

If a problem takes more than an hour, Diego asks for help. Asking early also spreads knowledge, because the person helping learns about the failure too. Pair debugging often finds the cause quickly, usually because one stated assumption turns out to be wrong. The one-hour rule protects deadlines and stops a student from spending a day stuck on a failure that a colleague has already seen. Diego brings what he has tried, the error and his current guess, so the person helping can start quickly. The answer usually becomes a troubleshooting note for the next developer.

### The troubleshooting page

Each note has the symptom, the cause, the fix and the date. Notes are searchable by library or check name. Diego reviews the page every quarter and removes notes that no longer apply, for example after a library is replaced. He notices that a third of the notes concern one legacy project, which strengthens the case to rebuild it.

### Pair debugging

For harder failures, Diego works with another developer: one describes the failure aloud while the other questions each assumption. Several stubborn problems were solved this way within minutes, usually because a stated assumption turned out wrong.

### Worked example

A weekly update fails because a date library changed its time-zone default, breaking booking times in tests. Diego sets the time zone explicitly, the tests pass, and the troubleshooting page saves another developer an afternoon a month later.

> **Synthetic case.** Failures are synthetic.

### Errors and limits

Exceptions must expire; permanent exceptions become hidden risk.

### Exercises

- **EX058 — No disabling.** What happens if a check must be bypassed? *Rubric:* 3 = time-limited approved exception; 2 = partial; 1 = vague; 0 = none.
- **EX059 — Diagnosis steps.** How does Diego diagnose? *Rubric:* 3 = read, reproduce, one change at a time; 2 = two; 1 = one; 0 = none.
- **EX060 — Date library fix.** What fixed the date library failure? *Rubric:* 3 = explicit time zone; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Fix root causes and keep checks on.

### Continue studying — chapter 20 of 30

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Application and software supply chain security: service integration

### Learning outcomes

You will (1) secure connections to external services; (2) manage service secrets; (3) validate data from services; (4) plan for service failures.

### 21.1 External services

Client apps use an email service, a payment provider for museum-tickets and a mapping service for the kiteschool site. Each is a trust boundary: Brightwave depends on it and sends data to it. Each service receives some client data and returns answers the apps act on, so a problem at the provider can become a problem for the client. The email service sees owners' email addresses, the payment provider handles museum ticket payments and the mapping service receives requests from kiteschool-site visitors.

### 21.2 Secrets for services

Service keys are kept in the hosting platform's secret store, scoped to one client and one environment, and rotated yearly or immediately if exposed. Keys never appear in code; a pre-commit scan catches mistakes. Scoping a key to one client and one environment means a leaked test key cannot reach production, and a leaked kiteschool key cannot touch museum-tickets. Yearly rotation limits how long a quietly copied key stays useful, and immediate rotation is the response whenever a key appears in a log, a chat or a repository. The date of each rotation is recorded in the service inventory for later review.

### 21.3 Validating responses

Data returned by services is checked like user input. Payment confirmations are verified with the provider's signature before marking a ticket as paid. Without the signature check, anyone who learned the callback address could have sent a message claiming a ticket was paid. Other responses get the same treatment as form input: mapping results are checked for expected fields, and unexpected values are logged and rejected rather than shown to visitors. A provider's good reputation does not change this rule for any Brightwave integration.

### 21.4 Least data

Only needed data is sent: the email service receives the owner's email and appointment time, not medical notes. Medical notes stay inside Greenleaf's database because the email only needs to confirm a time. If the email provider ever had a breach, Greenleaf's exposure would be limited to addresses and appointment times. Diego checks each integration's outgoing fields against this rule and removes two unneeded fields from a confirmation template. Each service's data list is recorded in the service inventory so later changes can be compared against it.

### 21.5 Failure planning

If the email service fails, bookings still save and emails retry later; if payment confirmation is missing, the ticket stays pending. These rules keep a provider's outage from becoming a booking outage. Greenleaf's clinic still receives every booking when the email service is down, and confirmations are sent once it recovers. A museum ticket without a confirmed payment is never marked paid by default, so a missing callback cannot give away free entry. Each failure path has a synthetic test so the behaviour is checked on every build.

### 21.6 Reviewing services

Before adding a service, Brightwave reviews its security information and data location. The review records what data the service would receive, where it stores that data, how keys are issued and rotated, and how the provider announces security incidents. The answers go into the service inventory before any client data is sent. A service that cannot answer these questions is not added until a safer alternative or arrangement is found. Diego applies the same review retroactively to the three existing services and records the answers in the service inventory.

### Service inventory

Diego adds external services to the inventory: which client uses which service, what data is sent, where the key is stored and when it was last rotated. When a provider announces a security incident, Brightwave can tell within minutes which clients are affected and which keys to rotate. During the year, the mapping provider announces a key-handling issue; the kiteschool key is rotated the same afternoon and the client informed.

### Timeouts

Every service call has a timeout so a slow provider cannot freeze the booking site.

### Worked example

Reviewing integrations, Diego finds the museum-tickets payment callback accepted confirmations without checking the provider's signature. Signature verification is added and tested with synthetic signed and unsigned messages.

> **Synthetic case.** Services and findings are synthetic.

### Errors and limits

A trusted provider can still send unexpected data; validate everything.

### Exercises

- **EX061 — Key storage.** Where are service keys kept? *Rubric:* 3 = secret store, scoped per client and environment; 2 = partial; 1 = vague; 0 = none.
- **EX062 — Least data.** What does the email service receive? *Rubric:* 3 = email and appointment time only; 2 = partial; 1 = vague; 0 = none.
- **EX063 — Callback finding.** What was wrong with the payment callback? *Rubric:* 3 = no signature check; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Treat every service as a boundary to check.

### Continue studying — chapter 21 of 30

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Application and software supply chain security: automation

### Learning outcomes

You will (1) automate inventory, audit and drift checks; (2) schedule them; (3) route results to owners; (4) keep automation reviewed and safe.

### 22.1 What to automate

The nightly job builds the inventory from lock files, runs the audit against the advisory list, checks drift and writes one report. These are the same steps Diego earlier ran by hand each week: build the inventory, compare it with advisories and compare running versions with approved ones. Combining them in one nightly job means the morning report reflects the state of every client as of last night, and a new advisory is matched across all 23 projects without anyone starting a search.

### 22.2 Routing

Each finding goes to the project owner in the team chat with a link to the task; highs also go to Aiko. Routing to the owner named in the inventory means nobody has to read the whole report to find their own work. The task link gives the advisory, the affected project, the fixed version and the due date. Highs going to Aiko as well means the 7-day target is watched by someone beyond the person doing the fix. The chat message is short; the task holds the details.

### 22.3 Safe automation

The job has read-only access to repositories and hosting status. It opens tasks and update pull requests but cannot merge or deploy. Read-only access means a bug in the job, or a misuse of its credentials, cannot change a client site or a repository. A human still reviews and merges every update pull request, and deployment still goes through the pipeline and the approved-image rule. The job's narrow rights were checked in the access review like any other identity. Its credential is scoped to these actions and nothing else.

### 22.4 Reviewing automation

The job's code is reviewed like any project, pinned and tested with synthetic data. The job is held to the same rules it enforces: its actions are pinned, its dependencies have a lockfile and its token is read-only. Its tests use synthetic manifests and advisories, including cases near version-range boundaries, so a change to the matching logic is checked before it runs against real projects. Changes to the job go through pull request review like any client project. Any change also reruns the synthetic tests in the pipeline before it can merge.

### 22.5 Watching the watcher

If the nightly report does not arrive, an alert fires, because silent failure would look like "no problems". An empty report and a missing report look the same to a busy reader, yet they mean very different things. The alert fires if no report arrives by the expected time each morning. The report also includes the number of projects checked, which is how the three skipped projects were noticed. Together these turn a silent failure into a visible one. The missing-report alert goes to Aiko and to the job's named owner.

### 22.6 Effort saved

The manual weekly checks that took Diego half a day now take ten minutes of reading. The saved time goes into fixing findings rather than finding them. Reading takes ten minutes because the report starts with counts by severity and lists only new findings with their owners. Diego still compares one day's report with a manual check now and then, using the same trust-by-comparison idea that guided the automation's first weeks. The ten minutes include confirming any new match against its advisory text.

### Starting small

The automation started as Diego's manual checklist turned into a script one step at a time: first the inventory, then the audit, then drift. Each step ran beside the manual process for two weeks, and results were compared before the manual step was dropped. This caught two differences, both bugs in the script, before anyone relied on it. Aiko calls this approach 'trust by comparison', and the team uses it for later automation as well.

### Report format

The nightly report starts with counts by severity, then lists each new finding with its owner.

### Worked example

Two months in, the nightly job silently skips three projects whose lock files moved during a restructure. The missing-project count added to the report reveals it the next day, and the job is fixed to fail loudly when an expected project has no lock file.

> **Synthetic case.** Automation and events are synthetic.

### Errors and limits

Automation repeats mistakes quickly; test it and watch its output.

### Exercises

- **EX064 — Job permissions.** What can the nightly job do? *Rubric:* 3 = read; open tasks and PRs; not merge or deploy; 2 = partial; 1 = vague; 0 = none.
- **EX065 — Silent failure.** Why alert when the report is missing? *Rubric:* 3 = absence looks like no problems; 2 = partial; 1 = vague; 0 = none.
- **EX066 — Skipped projects.** How were skipped projects found? *Rubric:* 3 = missing-project count; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Automate checks with least privilege and watch for silent failures.

### Continue studying — chapter 22 of 30

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Application and software supply chain security: evaluation

### Learning outcomes

You will (1) measure check quality with precision and recall; (2) label a sample; (3) compare checks; (4) improve noisy checks.

### 23.1 Precision and recall

Precision is the share of a check's alerts that are real; recall is the share of real problems the check finds. A noisy check wastes time; a check with low recall gives false comfort. For Brightwave, both kinds of failure have a real cost in time or risk. The outdated-component check raising many alerts that are not real teaches developers to skim them, and a credential check that misses real keys would leave secrets in repositories without anyone knowing. Measuring both figures shows which problem each check has and what kind of tuning would help.

### 23.2 Labelling

Diego and another developer independently label a sample of findings as real or not, then discuss disagreements. Labelling independently means neither person sees the other's choice until both are done, so agreement is measured honestly. Disagreements are discussed and the reasons written down, because they usually show that the definition of a real finding is unclear. The month of triaged findings for the two rules in the lab comes from this kind of labelling. The labelled sample is kept so later tuning can be measured on the same items.

### Lab — check quality

```python
"""Quality of two scanner rules over a month of triaged synthetic findings."""
rules = {"outdated-component": (48, 30, 2), "hardcoded-credential": (12, 3, 0)}
for r, (flags, real, missed) in rules.items():
    print(f"{r:21} flags={flags:3} real={real:2} precision={real / flags:.2f} recall={real / (real + missed):.2f}")
```

Run with `python3 lab_quality.py`. Verified output:

```text
outdated-component    flags= 48 real=30 precision=0.62 recall=0.94
hardcoded-credential  flags= 12 real= 3 precision=0.25 recall=1.00
```

### 23.3 Lab result

The outdated-component check has precision 0.62 and recall 0.94: it finds nearly everything but over a third of alerts are not real. The hardcoded-credential check has precision 0.25 and recall 1.00: it finds every real credential but three quarters of its alerts are test strings or examples. Recall depends on knowing what was missed, which comes from the labelled sample rather than from the check itself. For the outdated-component rule, the sample found two real problems the check missed, giving 30 of 32. These figures are estimates from one month's sample, and small samples move a lot with a few changed labels.

### 23.4 Improving

The credential check gets an allow list for clearly synthetic test values, reviewed by Aiko; the outdated check ignores libraries used only in development. Both changes target the false alerts without narrowing what counts as real. The allow list covers only values that are clearly synthetic, and Aiko reviews each entry so it cannot become a hiding place for a real key. Development-only libraries never reach a client's running site, which is why the outdated check can safely set them aside. Each change is recorded with its reason and the date.

### 23.5 Re-measuring

After changes, the same labelled sample is rerun to confirm recall did not fall. Rerunning on the same labelled items isolates the effect of the change, because nothing else about the sample differs. If recall falls, the change has hidden real problems and is reworked even if precision improved. After the credential check's tuning, a fresh sample is also labelled to check that the improvement holds on new data, giving precision 0.70 with recall still 1.00. Reporting the sample size with each figure keeps readers from trusting small changes too much.

### Labelling carefully

Two labellers working independently make it possible to see how often they agree. Where they disagree, the reason is written down, because disagreements often show that the definition of a real problem is unclear. For the credential check, the team agrees that a real credential is any value that would work against a live system, while expired or example values are not. Writing this definition down raised agreement in the next sample. The labelled samples are kept, so future changes to a check can be measured on the same items.

### Worked example

After tuning, the credential check's precision rises to 0.70 on a fresh sample with recall still 1.00, and developers stop ignoring its alerts.

> **Synthetic case.** Samples and figures are synthetic.

### Errors and limits

A small labelled sample gives rough estimates; report the sample size.

### Exercises

- **EX067 — Definitions.** Define precision and recall. *Rubric:* 3 = share of alerts real; share of problems found; 2 = one; 1 = vague; 0 = none.
- **EX068 — Lab figures.** What were the lab figures? *Rubric:* 3 = outdated 0.62/0.94; credential 0.25/1.00; 2 = one; 1 = vague; 0 = none.
- **EX069 — Re-measure.** Why re-run the sample after tuning? *Rubric:* 3 = check recall did not fall; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Measure checks and tune them without losing recall.

### Continue studying — chapter 23 of 30

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Applied research methods

### Learning outcomes

You will (1) ask a focused question; (2) collect evidence from Brightwave records; (3) analyse simply; (4) report honestly.

### 24.1 The question

Diego asks: "Do projects receiving weekly update pull requests fix high advisories faster than projects updated manually?" The question comes from Diego's own observation that some projects close high advisories much faster than others. It is narrow enough to answer from records Brightwave already has, and its answer would change a practical decision: whether to give every active project weekly update pull requests. Diego writes it down before looking at the data so the analysis cannot drift towards a convenient finding.

### 24.2 Evidence

Task records give advisory dates and fix dates for each project and update method over one year. The task tracker already holds these dates because every audit match becomes a task with an owner and due date. Using existing records means no new data collection and no extra work for developers. Diego keeps only high advisories, so the comparison is between similar kinds of work, and he checks twenty records by hand against the original advisories. The year of records covers projects with each update method, and each record gives its project's method at the time.

### 24.3 Analysis

He compares median fix times: weekly-update projects 3 days, manual projects 12 days. Medians suit this data better than averages, because a few long-running fixes in neglected projects would pull an average upward. With weekly-update projects at 3 days and manual projects at 12, both groups' medians sit inside the 7-day target for highs only for the weekly group. Diego reports the number of advisories in each group alongside the medians so readers can judge how solid each figure is. Only the weekly group's median sits inside the 7-day target for highs.

### 24.4 Limits

Projects were not randomly assigned; manual projects are older and less active, which could explain part of the difference. Wermke et al. (2022) interviewed open-source projects about supply chain practices and show how context shapes adoption. Diego states this limit in the report itself rather than in a footnote. Older, less active projects may fix slowly for reasons unrelated to how they receive updates, such as having no active owner or harder code to change. Diego's earlier observation that matches in projects with no recent work took nearly three weeks points the same way. The comparison therefore shows an association that supports the recommendation, not proof that weekly pull requests alone cause faster fixes.

### 24.5 Reporting

The report states the question, data, result, limits and a recommendation. The recommendation follows from the result but is worded no more strongly than the limits allow. Diego proposes weekly update pull requests for active projects and says the older projects should be reassessed after their rebuild. The data, script and cleaning decisions are attached, so Aiko or the tutor can rerun the analysis and check each step. The report fits on two pages, with the chart, the limits and the recommendation on the first, so the team can read it before the meeting.

### 24.6 Ethics

Records about developers' work are summarised by project, not used to judge individuals. Grouping by project keeps the research about the update method rather than about who was slow. A developer whose project sits in the manual group usually inherited that setup and is not at fault. Diego removes developer names from the exported records before analysis, and the report shows only project-level figures. Summaries by project also make the report safe to share with the tutor, since no individual developer can be identified from the figures shown.

### Collecting the data

Diego exports a year of task records from the tracker, keeps only high advisories, and checks twenty records by hand against the original advisories to make sure dates are correct. He finds two records with a fix date earlier than the advisory date, caused by fixes made before the advisory was published, and handles them separately rather than letting them distort the median. The data and the script are saved with the report so that Aiko can rerun them. A short appendix lists every decision made while cleaning the data, so readers can judge whether they agree with it.

### Presenting results

Diego presents the report in ten minutes at the team meeting, showing one chart, the limits and the recommendation, then takes questions about the cleaned records and the two unusual cases.

### Worked example

The report recommends weekly update pull requests for all active projects, with older projects included after their rebuild. Aiko accepts it, and the change is made the following month.

> **Synthetic case.** Data and results are synthetic.

### Errors and limits

A difference in records is not proof of cause.

### Exercises

- **EX070 — Question.** What was the question? *Rubric:* 3 = weekly PRs vs manual fix speed; 2 = partial; 1 = vague; 0 = none.
- **EX071 — Result.** What were the medians? *Rubric:* 3 = 3 vs 12 days; 2 = partial; 1 = vague; 0 = none.
- **EX072 — Limit.** Name a limit. *Rubric:* 3 = not random; older projects manual; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Ask focused questions and report limits honestly.

### Continue studying — chapter 24 of 30

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Team project studio

### Learning outcomes

You will (1) plan a team project; (2) divide work; (3) review each other's changes; (4) deliver in increments.

### 25.1 The project

Diego's team of three builds a shared "client security status" page showing inventory, open advisories and drift for each client. The page answers the questions clients and owners most often ask Brightwave: what each project uses, which advisories are open and whether the site runs the approved release. It reuses data the nightly job already produces, so the team builds a view rather than a new collection process. Clinic contacts can check their own status without emailing the agency. The page also gives Diego's team a real product with real risks to manage.

### 25.2 Planning

They write a short plan: users, data, risks and a first version in two weeks. Listing the page's risks early shapes its design from the very first version. The plan names the page's users, staff and client contacts, notes that inventory and advisory data could help an attacker choose targets, and therefore marks access control as the first risk. The two-week first version is small enough to finish and review properly. The plan also states that tests use synthetic client data only. Each item in the plan has a named owner and a target date.

### 25.3 Dividing work

One builds the data import, one the page, Diego the access checks and tests. Diego takes the access checks because the page shows sensitive information about clients' weaknesses. Splitting the work this way lets each person own one part while reviewing the others. The data import person also handles the case where the nightly job has not yet produced a report, so the page shows that gap instead of stale data. The split also matches each person's strengths, which the team discussed openly at the start.

### 25.4 Reviewing

Every change gets a review; reviewers check authorisation and data shown. Reviews within one working day keep work flowing, and nobody merges their own change. Each reviewer checks two things beyond the code itself: who can see each page, and whether the data shown is limited to what that viewer needs. The authorisation line added to the checklist came from a review that caught all clients being visible to any staff member. Reviewers leave written comments so the reasoning remains visible later.

### 25.5 Increments

The first version shows inventory only; advisories and drift come in later increments. Starting with inventory alone gives clients something useful early while the riskier advisory view is still being designed. When the second increment runs late, the team moves drift to the third increment instead of skipping reviews. Each increment goes through the same review and test steps, so the page grows without losing the controls built into the first version. Each increment ends with a short demonstration to Aiko before the next one starts.

### 25.6 Retrospective

After each increment, the team notes what went well and what to change. Retrospectives are kept short, about fifteen minutes, and the notes are written down. After the second increment, the team notes that reviewing within a day kept work moving, while one estimate was too optimistic because of the authorisation work. They adjust the plan for the third increment accordingly and keep the review agreement for later projects. The notes also help the next placement student understand why the page works as it does.

### Working agreements

The team agrees how to work before starting: daily ten-minute check-ins, reviews within one working day, and no merging of one's own changes. They also agree that tests use only synthetic client data. Having these written down helps when the second increment runs late: instead of skipping reviews, they move the drift feature to the third increment. The page's first version is shown to Aiko after two weeks as planned, and clinic contacts begin using it in the following month. Their feedback, mostly about wording, shapes the second increment. The retrospectives also show that reviews within a day kept work flowing, so the agreement is kept for later projects.

### Handover of the page

At the end of the project, the team writes a short note on how the page works, who owns it and how to add a client, so the page keeps working after the placement ends.

### Worked example

In review, a teammate notices the status page would show all clients to any staff member. Access is limited so client contacts see only their own projects, and the review checklist gains an explicit authorisation line.

> **Synthetic case.** The project is synthetic.

### Errors and limits

Small increments make reviews easier and problems smaller.

### Exercises

- **EX073 — Project.** What did the team build? *Rubric:* 3 = client security status page; 2 = partial; 1 = vague; 0 = none.
- **EX074 — Diego's part.** What did Diego build? *Rubric:* 3 = access checks and tests; 2 = partial; 1 = vague; 0 = none.
- **EX075 — Review catch.** What did review catch? *Rubric:* 3 = all clients visible to anyone; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Plan, divide, review and deliver in steps.

### Continue studying — chapter 25 of 30

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Application and software supply chain security: operational handoff

### Learning outcomes

You will (1) hand over security processes to the team that will run them; (2) write runbooks; (3) define responsibilities; (4) check the handoff works.

### 26.1 What is handed over

As the placement nears its end, Diego hands over the nightly job, the inventory, the upload checks module, the pipeline template and the drift check. Each needs an owner who will keep it running after he leaves; otherwise the controls will slowly decay as libraries and platforms change around them. Each item is something the agency now relies on daily, built during Diego's placement. For each item Diego lists where its code lives, what it depends on and who uses its output.

### 26.2 Runbooks

Each process gets a runbook: what it does, how to tell it is healthy, what common failures look like and how to fix them, and who to contact. Runbooks are written for a developer who has never seen the process, and tested by having one follow them. A developer who follows a runbook without help shows that the steps are complete. A runbook also states what not to do, such as never disabling a failing check to clear the nightly report. It links to the troubleshooting page entries that concern the process, so a new owner can see which failures have happened before and how they were solved.

### 26.3 Responsibilities

A simple table names who owns each process, who is the backup, and who approves changes. Advisory response is shared: the nightly job finds matches, project owners fix them, and Aiko watches the due dates each week. Naming a backup matters because a process with one person who understands it stops when that person is away. The table also records who approves changes, so the nightly job's matching logic or the pipeline template cannot be edited without a named reviewer. Weekly checking of due dates by Aiko keeps the 7-day target visible across all owners.

### 26.4 Checking the handoff

For two weeks the new owners run everything while Diego only watches. Any question they have to ask him becomes a runbook update. The watched fortnight tests the handoff under real conditions rather than in a meeting. Diego answers questions but does not run any step himself, so gaps in the runbooks become visible. Eleven questions came up, and each became a runbook update before he left. The new owners also handle one real advisory match during the fortnight, following the runbook from task to fix.

### 26.5 Client communication

Clients are told who their security contact is and how advisories affecting them will be reported. Each client's note names the Brightwave contact, explains that advisories affecting their site will be reported with what was done, and states the agreed response times from their contract. Greenleaf's clinic manager, the incident contact in the inventory's context note, receives the first of these. Clients who never had an affected library still learn how they would be told. Clients are also told that a quiet month means no affected advisories, not a missed report.

### 26.6 Keeping knowledge

Decisions and reasons are kept in the repositories next to the code, not in personal notes. Diego's reasons for decisions, such as the 180-day threshold for upload, authentication and payment libraries or the hold list in the drift check, are written into the repositories that use them. A new owner reading the code finds the explanation next to it. Personal notes would leave with Diego at the end of the placement, along with the reasons behind the controls. Repositories keep this knowledge reviewed alongside the code it explains, in the same pull requests.

### Worked example

During the watched fortnight, the new owner of the nightly job cannot find how to add a new client project to the inventory. Diego adds a step to the runbook; the next new project is added without help. By the end, the owners have asked eleven questions, all now answered in the runbooks.

> **Synthetic case.** Processes and events are synthetic.

### Errors and limits

A handoff is finished when others can run the process without you, not when the documents exist.

### Exercises

- **EX076 — Runbook contents.** What does a runbook include? *Rubric:* 3 = purpose, health, failures, fixes, contacts; 2 = three; 1 = one; 0 = none.
- **EX077 — Advisory roles.** Who does what in advisory response? *Rubric:* 3 = job finds; owners fix; Aiko watches dates; 2 = two; 1 = one; 0 = none.
- **EX078 — Handoff check.** How was the handoff checked? *Rubric:* 3 = two weeks owners run, Diego watches; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Hand over with runbooks, owners and a watched trial.

### Continue studying — chapter 26 of 30

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Deployment and validation

### Learning outcomes

You will (1) deploy the security controls to all client projects; (2) validate each works; (3) record results; (4) handle projects that cannot yet comply.

### 27.1 Rollout plan

Controls are rolled out project by project, starting with the most sensitive clients identified in chapter 11. Each project gets the shared upload module, the pipeline template, lock-file enforcement and digest recording. Starting with Greenleaf and museum-tickets, whose data is most sensitive, means the highest-risk sites gain the controls first if the rollout is interrupted. Each project receives the same four controls, so the validation checklist can be identical across projects. The two legacy projects come last because they need separate handling.

### 27.2 Validation tests

For each project, Diego runs a validation checklist with synthetic data: a disallowed upload is rejected with its reason; the pipeline uses pinned actions and a read-only token; a lock-file mismatch fails the build; the deployment record holds a digest; the drift check reports the project as matching. Each item on the checklist tests exactly one of the rolled-out controls. If any item fails, the project is not marked complete until the fix is deployed and the whole checklist is run again. Using the same synthetic files for every project means a result in one project can be compared directly with another, and a failure points to the project rather than the test data.

### 27.3 Recording results

Results are recorded per project with date and tester, forming evidence for clients and for Brightwave's own review. Recording the tester and date makes each validation result traceable to a person. When a client asks whether their site has the new upload checks, Brightwave answers from the record rather than from memory. The results also feed the capstone presentation, where Diego shows validation records for all 23 projects as evidence that the controls exist. Records also show when each project was last validated, so later changes can trigger a fresh run.

### 27.4 Projects that cannot comply

Two legacy projects cannot use the new upload module without a rewrite. They get compensating steps (tighter size limits and storage rules) and a rebuild date. The compensating steps reduce exposure until the rebuild without pretending the projects comply. A tighter size limit and stricter storage rules cover the most important gaps, and the rebuild date is tracked in the monthly report. These are the same two legacy projects that held most of the remaining stale libraries and the slowest fixes.

### 27.5 Rollback

Each rollout can be reversed by redeploying the previous approved digest if a client site breaks. Because every deployment records its digest, the previous version is known exactly and can be redeployed through the pipeline in minutes. Rollback does not bypass the approved-image rule, since the earlier digest is already on the approved list. The one rollback during the rollout used this path, and the corrected change was redeployed the next day. Owners are told how to roll back before each project's rollout begins.

### 27.6 Communicating

Clients receive a short note on what changed and any visible effects, such as new upload messages. Telling clients in advance prevents surprise when an upload is now rejected with a message. Greenleaf's note mentions the new upload messages and the 5 MB limit, so reception staff can explain them to pet owners. The note is short and avoids technical detail, following the same style as the January message. Clients with no visible change still receive a brief note confirming what was updated.

### Validation as a habit

The validation checklist becomes part of the release process for new projects, so each new client starts with every control in place and recorded. The checklist takes about twenty minutes per project with the synthetic test files ready.

### Worked example

Rollout across 23 projects takes five weeks. Twenty-one pass every validation item on the first attempt or after small fixes, including one that first needs a rollback when an upload change rejects a file format the client really uses; the format is added to its allowed list after review and redeployed the next day. The two legacy projects are validated against their compensating steps instead.

> **Synthetic case.** Projects and results are synthetic.

### Errors and limits

Validation proves the control is present; monitoring proves it stays present.

### Exercises

- **EX079 — Rollout order.** Which projects went first? *Rubric:* 3 = most sensitive clients; 2 = partial; 1 = vague; 0 = none.
- **EX080 — Legacy projects.** How were the two legacy projects handled? *Rubric:* 3 = compensating steps and rebuild date; 2 = partial; 1 = vague; 0 = none.
- **EX081 — Rollback case.** Why was one project rolled back? *Rubric:* 3 = rejected a format the client used; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Roll out in order, validate each project and plan for exceptions.

### Continue studying — chapter 27 of 30

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Field practice

### Learning outcomes

You will (1) apply the course in a real-style advisory response; (2) coordinate across clients; (3) communicate clearly; (4) reflect on what worked.

### 28.1 The event

In the final month, a synthetic high-severity advisory is published for a widely used form library. This time, the nightly job matches it to nine client projects within hours of publication. The contrast with January is the point of the event. Instead of three days of manual searching, the nightly job reads every project's lockfile, compares versions with the advisory and produces tasks with owners attached. Diego starts the day with a list of nine affected projects rather than a question nobody can yet answer.

### 28.2 Coordination

Owners receive tasks automatically. Diego coordinates: sensitive clients first, updates through the weekly bot pipeline, validation tests rerun before deployment. Ordering by sensitivity uses the context notes recorded earlier, so Greenleaf and other clients with personal data are updated first. Using the weekly bot pipeline means each fix is tested, reviewed and recorded by digest like any other change. Rerunning the validation tests before deployment confirms the update did not break uploads, pinning or digest recording. Diego tracks each project's status in the client security status page.

### 28.3 Communication

Affected clients get a short message: what the issue is in plain terms, whether their site was affected, what was done and when. Unaffected clients who ask get a clear "not affected" answer from the inventory record. Clients unaffected by the advisory and who ask get their answer from the inventory record, which lists every project's form-library version. Affected clients receive the message once the fix is deployed, so it can state what was done and when. The shortened template that came out of this event keeps each message to a few plain sentences.

### 28.4 Timeline

All nine projects are fixed within four days, well inside the 7-day target. Compared with January's three days just to find affected clients, the difference is clear. The comparison is not exact, since January's library and this event's library differ, but both were high-severity advisories affecting several clients. The four-day figure covers matching, fixing, validating and deploying for all nine projects. That margin left time to handle the legacy project's slower fix without missing the 7-day target. Each project's fix date is recorded, so the timeline can be checked against the tasks.

### 28.5 Reflection

The team notes that the slowest fix was in a legacy project, again pointing to the rebuild. The legacy project's slower fix came from its missing update automation and older code, the same causes noted in Diego's research. That pattern now appears in the research, the troubleshooting page and the field event, which together give the directors a clear case for the rebuild. The team also notes which steps went smoothly, so they are not changed unnecessarily. The rebuild decision is left to the directors, who receive the evidence in one place.

### 28.6 Lessons

Two runbook steps are improved and the client message template is shortened after feedback. One runbook step improved is how to add a temporary hold when a client asks to delay an update during the event. The other clarifies how to confirm an inventory match before tasks are opened. Client feedback says the message template was too long, so it is cut to the three answers clients want. Both runbook changes are reviewed and merged within the week, while the event is still fresh in everyone's memory.

### Compared with January

In January, three days went on manual searching before any fix began, and the full extent was unclear. In the field event, matching took hours, owners were known, fixes followed the update pipeline and validation, and every client received an accurate answer. The difference came from routine work done earlier: the inventory, the nightly job, the pipeline template and the runbooks. None of it was dramatic, but together it changed how the agency responded, and the directors agreed to keep funding the time owners spend on these processes.

### Worked example

Aiko presents the event to Brightwave's directors as evidence that the placement's three goals have been met: the inventory answered in minutes, highs were fixed within 7 days, and every deployment was a recorded pipeline build.

> **Synthetic case.** The event and results are synthetic.

### Errors and limits

One good event does not prove the process always works; keep measuring.

### Exercises

- **EX082 — Detection.** How quickly were affected projects found? *Rubric:* 3 = within hours via nightly job; 2 = partial; 1 = vague; 0 = none.
- **EX083 — Fix time.** How long did fixing take? *Rubric:* 3 = four days for all nine; 2 = partial; 1 = vague; 0 = none.
- **EX084 — Goals met.** Which goals were shown to be met? *Rubric:* 3 = inventory minutes; 7-day highs; recorded builds; 2 = two; 1 = one; 0 = none.

### Synthesis

The controls turn a three-day search into a four-day fix.

### Continue studying — chapter 28 of 30

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Capstone build

### Learning outcomes

You will (1) design and build a capstone improvement; (2) apply the course methods; (3) test with synthetic data; (4) document it.

### 29.1 Choosing the capstone

Diego's capstone is a software bill of materials (SBOM) for each client release, listing every component and version. NTIA (2021) describes the minimum elements: supplier, component name, version, unique identifier, dependency relationship, author of the data and timestamp. An SBOM extends the inventory from what runs now to what each release contained. Diego chooses it because clients have begun asking for component lists and because it closes a gap the inventory leaves. The NTIA minimum elements give a clear checklist for what each SBOM must contain, so the capstone can be tested against it.

### 29.2 Design

The build creates the SBOM from the lock file, attaches it to the release record next to the image digest, and stores it with the deployment record. Clients can request their SBOM. Generating the SBOM from the lockfile keeps it consistent with what the build actually installed. Storing it next to the image digest links each component list to an exact release. A client asking for their SBOM receives the one matching the release running on their site. The SBOM is regenerated only when a release is built, not on every test run.

### 29.3 Using SBOMs

With SBOMs per release, the inventory can answer not only "who uses this library now" but "which past release contained it", which helps when clients ask about past exposure. Without SBOMs, answering a question about past exposure means rebuilding old lockfiles from repository history, which is slow and easy to get wrong. With them, Brightwave can search stored component lists for any release. This matters when a client asks whether an older release they ran last year contained a library named in a new advisory.

### 29.4 Testing

Tests check that every library in the lock file appears in the SBOM and that the SBOM matches the deployed digest. Both tests run in the build, so a missing component or a mismatch fails the release before it is deployed. Diego also checks by hand that one small project's SBOM matches its lockfile. The hand check catches a formatting issue in version strings that the automated tests had not been written to detect. After that fix, the tests are trusted for the remaining projects, and a deliberately broken synthetic lockfile is used to show that a missing component really fails the build.

### 29.5 Documentation

A runbook explains how SBOMs are created, where they are stored and how to answer a client request. The runbook names the owner and explains how to find a past release's SBOM by date or digest. It also covers what to send a client and how to record that a request was answered. The runbook was followed once by another developer before the capstone was submitted, using a synthetic client request. It also lists the common failures seen while testing the SBOM build, with their fixes.

### 29.6 Scope limits

The capstone does not attempt signing SBOMs; that is noted as future work linked to the SLSA L3 goal. Keeping the scope small lets the capstone finish properly and be tested on real Brightwave projects. Signing would need the provenance and key handling planned for the SLSA L3 goal, which is not yet in place. Naming the limit openly lets the assessors judge the capstone for what it does rather than for what it might later become. The unsigned state is stated plainly in the runbook and in each client response.

### SBOM format

Diego chooses a widely supported standard SBOM format so clients' own tools can read it, and keeps one SBOM per release rather than per build attempt. Each SBOM records the generating tool and version, so later differences can be explained. He compares a generated SBOM with the lock file by hand for one small project before trusting the automated tests, which confirms the test logic and catches a formatting issue in version strings.

### Worked example

Diego tests the SBOM build on three client projects. One reveals a library bundled directly into code instead of through the lock file, invisible to the inventory until now. It is moved into the lock file so it is tracked like everything else.

> **Synthetic case.** The capstone is synthetic.

### Errors and limits

An SBOM lists components; it does not say whether they are safe.

### Exercises

- **EX085 — NTIA elements.** Name four NTIA minimum elements. *Rubric:* 3 = supplier, name, version, identifier, relationship, author, timestamp; 2 = two; 1 = one; 0 = none.
- **EX086 — New question.** What new question can SBOMs answer? *Rubric:* 3 = which past release had a library; 2 = partial; 1 = vague; 0 = none.
- **EX087 — Hidden library.** What did testing reveal? *Rubric:* 3 = library bundled outside lock file; 2 = partial; 1 = vague; 0 = none.

### Synthesis

SBOMs extend the inventory to every release.

### Continue studying — chapter 29 of 30

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Capstone assessment

### Learning outcomes

You will (1) present the capstone; (2) show evidence; (3) answer questions; (4) reflect on learning and next steps.

### 30.1 Presentation

Diego presents to Aiko and a Southport Polytechnic tutor: the January problem, the controls built, the evidence that they work, and the SBOM capstone. The presentation follows the course order: the problem first, then each control with its evidence, then the capstone and its limits. Diego keeps to synthetic records throughout, so no client data appears on the slides. The tutor and Aiko assess the presentation together, each using the course rubric, and compare their scores afterwards. Diego's talk lasts twenty minutes, leaving time for questions about evidence and limits.

### 30.2 Evidence

He shows the nightly reports, the validation records for 23 projects, the field-practice timeline and the SBOM tests, all from synthetic records. Each piece of evidence matches one of the three placement goals. Nightly reports and the field timeline show the inventory answering in minutes and highs fixed within seven days; validation records and digest records show deployments were recorded pipeline builds. Each piece of evidence is a record produced during normal work, not a document prepared for the assessment. He brings the raw records so any figure on a slide can be checked on request.

### 30.3 Questions

The tutor asks how the work fits the SSDF. Diego maps it: inventory and audits to Respond to Vulnerabilities; pipeline template and pinning to Protect the Software; upload checks and reviews to Produce Well-Secured Software; runbooks and roles to Prepare the Organization. The tutor follows up by asking which group was weakest at the start, and Diego names Respond, as the January search showed. The mapping shows that each group gained at least one concrete control during the placement. He adds that the map came from the SSDF table used to set the placement goals.

### 30.4 Limits

He names the limits honestly: two legacy projects remain, SBOMs are unsigned and unknown flaws are not found by audits. Naming limits shows the assessors what the evidence does not cover yet. The two legacy projects still rely on compensating steps until their rebuild, unsigned SBOMs could be altered without detection, and audits find only flaws that already have advisories. Diego also notes that the field event was a single event, so it shows the process can work rather than that it always will.

### 30.5 Reflection

Diego writes that the biggest lesson was that most security work is careful routine: keeping lists current, watching checks and fixing small problems before they grow. Diego's reflection links this lesson to specific moments: the four-minute test advisory, the missed lockfiles caught by the missing-project count, and the eleven handoff questions turned into runbook steps. None of these was dramatic, but each kept a control working. Diego also notes that the routine only worked because each control had a named owner.

### 30.6 Next steps

Brightwave will rebuild the legacy projects, aim for SLSA build L3 and add signed SBOMs. Each next step answers one named limit: the rebuild for the two legacy projects, SLSA L3 for build hardening, and signed SBOMs. Diego hands these to their owners with target dates in the monthly report, and the tutor's suggestion to count SBOM requests is added to the same report. The next placement student will start from these targets and the existing runbooks. Each next step names the limit it closes and the evidence that would show success.

### Feedback received

The tutor's feedback praises the evidence and the honest limits, and suggests that the next step should include measuring how often clients use their SBOMs, since an unused document adds work without value. Aiko adds that the handoff quality was the strongest part, because the processes kept running without Diego during the watched fortnight. Diego records both points in his learning log and adds an SBOM-request count to the monthly report. Looking back over the year, he notes how each chapter's small step depended on earlier ones: the inventory made audits possible, audits made fix targets measurable, and records made the capstone possible.

### Worked example

The capstone is assessed as complete with distinction, and Brightwave offers Diego a junior developer role starting after graduation, with security processes as part of his responsibilities.

> **Synthetic case.** People, results and outcomes are synthetic.

### Errors and limits

Assessment rewards honest limits as well as results.

### Exercises

- **EX088 — SSDF map.** Map the work to the SSDF groups. *Rubric:* 3 = four groups mapped; 2 = three; 1 = one; 0 = none.
- **EX089 — Limits.** Name two limits. *Rubric:* 3 = legacy projects; unsigned SBOMs; unknown flaws; 2 = one; 1 = vague; 0 = none.
- **EX090 — Lesson.** What was Diego's main lesson? *Rubric:* 3 = security is careful routine; 2 = partial; 1 = vague; 0 = none.

### Synthesis

Present evidence, map it to frameworks and name the limits.

### Continue studying — chapter 30 of 30

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX090. Diego Ramos, Aiko Mori, Brightwave Digital, Southport Polytechnic, Greenleaf Veterinary Group and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** Brightwave had no central list of which clients used which library, so finding affected projects took three days.

**EX002.** It saves time but one flaw affects many clients at once.

**EX003.** Uploaded files were stored in the same bucket as the site's images.

**EX004.** With two-person approval and multi-factor sign-in.

**EX005.** Over HTTPS, checking lockfile hashes.

**EX006.** Restricted outbound connections to the three services it uses.

**EX007.** One to forty letters, spaces or hyphens.

**EX008.** In environment variables set in the hosting platform.

**EX009.** The date check accepted dates in the past.

**EX010.** greenleaf-booking and museum-tickets.

**EX011.** Because text ordering is wrong, for example 3.10 would sort before 3.2.

**EX012.** Because their real installed versions cannot be known.

**EX013.** A06 Vulnerable and Outdated Components.

**EX014.** Unrestricted upload of file with dangerous type.

**EX015.** Are we affected, what did you do, and do we need to do anything?

**EX016.** Only its upload and log folders.

**EX017.** To isolate each client's app from others on shared hosts.

**EX018.** Made it run as a dedicated user and added a build check against administrator images.

**EX019.** Only two developers.

**EX020.** A dedicated identity with limited permission, not a personal token.

**EX021.** A former contractor could still deploy to three client projects.

**EX022.** Edge, application, data and pipeline.

**EX023.** Each has its own database, storage bucket and secrets.

**EX024.** Two clients shared a database; it was split.

**EX025.** date-utils (1,141 days) and upload-kit (637 days).

**EX026.** It could encourage risky bulk updates without tests.

**EX027.** Stale versions fell from 64 to 18.

**EX028.** Code, libraries, build, image registry, deployment and updates.

**EX029.** In responding to vulnerabilities: no inventory and no fix targets.

**EX030.** An inventory answering in minutes, highs fixed within 7 days, and verified recorded builds.

**EX031.** Pet medical notes and uploaded files.

**EX032.** A weakness in them could change every client's site at once.

**EX033.** Sensitive, exposed clients the same day; brochure sites in the weekly cycle.

**EX034.** From the public library registry into the build.

**EX035.** Validation of type and content plus size limits.

**EX036.** An old CSV export of all bookings reachable by any staff account.

**EX037.** What could happen, through which weakness, and what harm follows.

**EX038.** Pinned versions with hashes, a delay before adopting brand-new versions, and review of dependency changes.

**EX039.** An outdated library with a known flaw in a public client app.

**EX040.** notes.pdf content mismatch, scan.png too large, run.exe type not allowed.

**EX041.** Storing outside the web root with random names and serving with a safe download header.

**EX042.** A clear message on reducing size instead of raising the limit.

**EX043.** High 2, medium 1.

**EX044.** High within 7 days, medium within 30.

**EX045.** The advisory's range excluded the installed patch version.

**EX046.** The exact version and hash of every direct and transitive library.

**EX047.** Harmful versions are often discovered and removed within days.

**EX048.** A new transitive library with an install script, avoided by configuration.

**EX049.** checkout@v4 and deploy-helper@main unpinned, secrets on fork pull requests, write-all token.

**EX050.** Read-only by default, write only for steps that need it.

**EX051.** The secret exposures, because they could leak credentials directly.

**EX052.** The image digest, the commit and the build run.

**EX053.** Provenance signed by a hosted build service.

**EX054.** That only pipeline-built approved images can reach production.

**EX055.** harbour-cafe BEHIND (2.0.9 vs 2.1.4) and museum-tickets UNAPPROVED BUILD (4.0.3-hotfix).

**EX056.** Nobody can say how it was built or what it contains.

**EX057.** A manual weekend deployment made before the approved-image rule.

**EX058.** A time-limited exception approved by Aiko with a ticket.

**EX059.** Read the failure, reproduce with synthetic data, change one thing at a time.

**EX060.** Setting the time zone explicitly.

**EX061.** In the hosting secret store, scoped per client and environment.

**EX062.** Only the owner's email and appointment time.

**EX063.** It accepted confirmations without verifying the signature.

**EX064.** Read and open tasks or pull requests, but not merge or deploy.

**EX065.** A missing report would otherwise look like no problems.

**EX066.** Through the missing-project count in the report.

**EX067.** Precision: share of alerts that are real. Recall: share of real problems found.

**EX068.** Outdated 0.62 precision, 0.94 recall; credential 0.25 precision, 1.00 recall.

**EX069.** To confirm recall did not fall.

**EX070.** Whether weekly update pull requests lead to faster fixes of highs.

**EX071.** 3 days for weekly-update projects, 12 for manual.

**EX072.** Projects were not randomly assigned; manual ones were older and less active.

**EX073.** A client security status page.

**EX074.** The access checks and tests.

**EX075.** That all clients' data would be visible to any staff member.

**EX076.** What it does, how to tell it is healthy, common failures and fixes, and contacts.

**EX077.** The job finds matches, owners fix them, Aiko watches due dates.

**EX078.** New owners ran everything for two weeks while Diego only watched.

**EX079.** The most sensitive clients.

**EX080.** Compensating steps and a rebuild date.

**EX081.** The upload change rejected a file format the client really used.

**EX082.** Within hours, matched by the nightly job.

**EX083.** Four days for all nine projects.

**EX084.** Fast inventory answers, highs within 7 days, and recorded pipeline builds.

**EX085.** Supplier, component name, version, unique identifier, dependency relationship, data author and timestamp.

**EX086.** Which past releases contained a library.

**EX087.** A library bundled into code, invisible to the inventory.

**EX088.** Respond: inventory and audits; Protect: pipeline and pinning; Produce: uploads and reviews; Prepare: runbooks and roles.

**EX089.** Two legacy projects remain, SBOMs are unsigned, and audits miss unknown flaws.

**EX090.** That most security work is careful routine.

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
