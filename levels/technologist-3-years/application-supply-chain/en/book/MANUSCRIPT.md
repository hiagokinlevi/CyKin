# Application and Software Supply Chain Security: Technologist Course

- Language: English (`en`); course 083, Technologist course (3 years).
- Editorial state: **draft**. Chapters 1–30 of 30 have hand-written teaching text; exercises EX001–EX090 have matching worked results with 0–3 rubrics; Seven offline labs use only the Python 3 standard library on synthetic evidence, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
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

Each client site has a browser front end, an application server, a database and file storage, running on a cloud hosting account managed by Brightwave. Code lives in repositories; a build service turns code into deployable packages.

Section one point two develops computing systems with a Brightwave Digital note Diego Ramos can demo offline.

Under section one point two, Aiko Mori expects computing claims to carry owners and dates.

Section one point two treats the case parts of as testable only when evidence and ticket IDs are recorded.

### 1.3 Shared components

Brightwave reuses libraries across clients: the same upload library, forms library and date utilities appear in many projects. Reuse saves time but means one flaw affects many clients at once.

Section one point three develops computing systems with a Brightwave Digital note Diego Ramos can demo offline.

Under section one point three, Aiko Mori expects computing claims to carry owners and dates.

Section one point three treats the case parts of as testable only when evidence and ticket IDs are recorded.

For section one point three, Brightwave Digital will not accept computing work without a written trail.

### 1.4 Third-party code

Most code in each project comes from open-source packages. Zimmermann et al. (2019) showed that a small number of packages and maintainers can reach a large share of an ecosystem; agencies concentrate this risk further by reusing the same packages across clients.

Section one point four develops computing systems with a Brightwave Digital note Diego Ramos can demo offline.

Under section one point four, Aiko Mori expects computing claims to carry owners and dates.

Section one point four treats the case parts of as testable only when evidence and ticket IDs are recorded.

### 1.5 Responsibility

Brightwave is responsible to each client for keeping their site secure, including the libraries it chose. Contracts say so.

Section one point five develops computing systems with a Brightwave Digital note Diego Ramos can demo offline.

Under section one point five, Aiko Mori expects computing claims to carry owners and dates.

Section one point five treats the case parts of as testable only when evidence and ticket IDs are recorded.

For section one point five, Brightwave Digital will not accept computing work without a written trail.

### 1.6 What was missing

Brightwave had no central list of which client used which library version. Each project's manifest held the answer, but nobody had combined them.

Section one point six develops computing systems with a Brightwave Digital note Diego Ramos can demo offline.

Under section one point six, Aiko Mori expects computing claims to carry owners and dates.

Section one point six treats the case parts of as testable only when evidence and ticket IDs are recorded.

For section one point six, Brightwave Digital will not accept computing work without a written trail.

### Worked example

Diego's first task is to draw one client system end to end: the Greenleaf booking site. His diagram shows the browser, server, database, file storage, payment link and nine direct libraries. Aiko asks him to add arrows showing where uploaded files go, which reveals that uploads are stored in the same storage bucket as the site's images.

> **Synthetic case.** Southport Polytechnic, Brightwave Digital, Greenleaf Veterinary Group, their staff, projects and all events are synthetic.

### Errors and limits

Diagrams show intended design; real configuration can differ and must be checked.

### Exercises

- **EX001 — January problem.** What made the January advisory hard to handle? *Rubric:* 3 = no central list; 3 days manual search; 2 = partial; 1 = none; 0 = none.
- **EX002 — Reuse trade-off.** What is the trade-off of reusing libraries across clients? *Rubric:* 3 = saves time; one flaw affects many; 2 = partial; 1 = none; 0 = none.
- **EX003 — Upload storage.** What did the arrows reveal? *Rubric:* 3 = uploads stored with site images; 2 = partial; 1 = none; 0 = none.

### Synthesis

Know the parts of each system, the shared components and where third-party code runs.

### Continue studying — chapter 01 of 30

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Networks and internet services

### Learning outcomes

You will (1) explain how browsers reach hosted apps; (2) describe DNS, HTTPS and content delivery; (3) explain how build services download packages; (4) identify network controls for apps and builds.

### 2.1 Reaching a site

A visitor types the Greenleaf booking address. DNS translates the name to an address; the browser connects over HTTPS, checking the certificate; a content delivery network may serve images; the request reaches the app server.

Section two point one develops networks and internet services with a Brightwave Digital note Diego Ramos can demo offline.

Under section two point one, Aiko Mori expects networks claims to carry owners and dates.

Section two point one treats reaching site https dns as testable only when evidence and ticket IDs are recorded.

### 2.2 HTTPS

HTTPS encrypts traffic and lets the browser confirm it reaches the real site. Brightwave renews certificates automatically and monitors expiry.

Section two point two develops networks and internet services with a Brightwave Digital note Diego Ramos can demo offline.

Under section two point two, Aiko Mori expects networks claims to carry owners and dates.

Section two point two treats reaching site https dns as testable only when evidence and ticket IDs are recorded.

For section two point two, Brightwave Digital will not accept networks work without a written trail.

### 2.3 DNS control

Client domains are managed in Brightwave's DNS account with two-person approval and multi-factor sign-in, since a changed DNS record could send visitors to a fake site.

Section two point three develops networks and internet services with a Brightwave Digital note Diego Ramos can demo offline.

Under section two point three, Aiko Mori expects networks claims to carry owners and dates.

Section two point three treats reaching site https dns as testable only when evidence and ticket IDs are recorded.

For section two point three, Brightwave Digital will not accept networks work without a written trail.

### 2.4 Package downloads

Build services download packages from public registries over HTTPS. Lockfile hashes let the build check that what arrives is what was recorded.

Section two point four develops networks and internet services with a Brightwave Digital note Diego Ramos can demo offline.

Under section two point four, Aiko Mori expects networks claims to carry owners and dates.

Section two point four treats reaching site https dns as testable only when evidence and ticket IDs are recorded.

For section two point four, Brightwave Digital will not accept networks work without a written trail.

### 2.5 Network controls

App servers accept web traffic only through the hosting platform's load balancer; databases are not reachable from the internet; build machines can reach only package registries and code hosts.

Section two point five develops networks and internet services with a Brightwave Digital note Diego Ramos can demo offline.

Under section two point five, Aiko Mori expects networks claims to carry owners and dates.

Section two point five treats reaching site https dns as testable only when evidence and ticket IDs are recorded.

### 2.6 Outbound calls

Some apps call external services (payments, email). Each allowed destination is listed, which limits server-side request forgery (OWASP Top 10:2021 A10).

Section two point six develops networks and internet services with a Brightwave Digital note Diego Ramos can demo offline.

Under section two point six, Aiko Mori expects networks claims to carry owners and dates.

Section two point six treats reaching site https dns as testable only when evidence and ticket IDs are recorded.

For section two point six, Brightwave Digital will not accept networks work without a written trail.

### Email security

Client sites send booking confirmations by email. Brightwave configures each sending domain with standard email authentication records so receiving servers can check messages really come from the clinic, which makes it harder for others to send convincing fake booking emails in the clinic's name. Diego checks the records for all clients and finds two missing.

### Worked example

Diego checks Greenleaf's outbound rules and finds the app can connect anywhere. He lists the three services it actually uses and Aiko restricts outbound traffic to them; the app works normally afterwards.

> **Synthetic case.** Network settings are synthetic.

### Errors and limits

Network controls limit damage but cannot fix flaws in the application itself.

### Exercises

- **EX004 — DNS protection.** How are client DNS records protected? *Rubric:* 3 = two-person approval; MFA; 2 = partial; 1 = none; 0 = none.
- **EX005 — Build downloads.** How do builds check downloaded packages? *Rubric:* 3 = HTTPS plus lockfile hashes; 2 = partial; 1 = none; 0 = none.
- **EX006 — Outbound fix.** What did Diego change for Greenleaf? *Rubric:* 3 = restricted outbound to three services; 2 = partial; 1 = none; 0 = none.

### Synthesis

Control names, connections and downloads; list allowed destinations.

### Continue studying — chapter 02 of 30

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Programming foundations

### Learning outcomes

You will (1) write small, clear functions; (2) validate input; (3) keep secrets out of code; (4) use version control and review.

### 3.1 Clear code

Diego writes small functions with one job each and names that say what they do. Clear code is easier to review, and reviewers catch more problems in short changes.

Section three point one develops programming foundations with a Brightwave Digital note Diego Ramos can demo offline.

Under section three point one, Aiko Mori expects programming claims to carry owners and dates.

Section three point one treats clear code input validation as testable only when evidence and ticket IDs are recorded.

For section three point one, Brightwave Digital will not accept programming work without a written trail.

### 3.2 Input validation

The booking form accepts a pet name, a date and a time slot. Each field is checked on the server against what is allowed: a name of 1–40 letters, spaces or hyphens; a date within the next 60 days; a slot from the clinic's list. OWASP ASVS input-validation requirements describe this allowlist approach.

Section three point two develops programming foundations with a Brightwave Digital note Diego Ramos can demo offline.

Under section three point two, Aiko Mori expects programming claims to carry owners and dates.

### 3.3 Secrets

API keys for email and payments are read from environment variables set in the hosting platform, never written in code. A pre-commit check warns if anything key-like is added.

Section three point three develops programming foundations with a Brightwave Digital note Diego Ramos can demo offline.

Under section three point three, Aiko Mori expects programming claims to carry owners and dates.

Section three point three treats clear code input validation as testable only when evidence and ticket IDs are recorded.

For section three point three, Brightwave Digital will not accept programming work without a written trail.

### 3.4 Version control

Every change is a commit with a message explaining why. Pull requests are reviewed by another developer before merging.

Section three point four develops programming foundations with a Brightwave Digital note Diego Ramos can demo offline.

Under section three point four, Aiko Mori expects programming claims to carry owners and dates.

Section three point four treats clear code input validation as testable only when evidence and ticket IDs are recorded.

For section three point four, Brightwave Digital will not accept programming work without a written trail.

### 3.5 Tests

Each validation rule has tests for valid values, edge values and invalid values.

Section three point five develops programming foundations with a Brightwave Digital note Diego Ramos can demo offline.

Under section three point five, Aiko Mori expects programming claims to carry owners and dates.

Section three point five treats clear code input validation as testable only when evidence and ticket IDs are recorded.

For section three point five, Brightwave Digital will not accept programming work without a written trail.

Section three point five fails closed if programming evidence is missing rather than guessing.

### 3.6 Error messages

Errors tell the user which field is wrong without repeating unsafe input back into the page.

Section three point six develops programming foundations with a Brightwave Digital note Diego Ramos can demo offline.

Under section three point six, Aiko Mori expects programming claims to carry owners and dates.

Section three point six treats clear code input validation as testable only when evidence and ticket IDs are recorded.

For section three point six, Brightwave Digital will not accept programming work without a written trail.

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

- **EX007 — Name rule.** What is the pet-name rule? *Rubric:* 3 = 1–40 letters, spaces or hyphens; 2 = partial; 1 = none; 0 = none.
- **EX008 — Secret storage.** Where are API keys kept? *Rubric:* 3 = environment variables in hosting platform; 2 = partial; 1 = none; 0 = none.
- **EX009 — Review catch.** What did Aiko catch? *Rubric:* 3 = past dates accepted; 2 = partial; 1 = none; 0 = none.

### Synthesis

Clear, validated, reviewed code with secrets kept out of the repository.

### Continue studying — chapter 03 of 30

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Data models

### Learning outcomes

You will (1) model project dependencies as structured data; (2) query manifests across projects; (3) answer "who uses this version?"; (4) keep the data current.

### 4.1 Manifests as data

Each project has a manifest listing its libraries and versions. Treated as data, manifests from all projects can be combined into one inventory.

Section four point one develops data models with a Brightwave Digital note Diego Ramos can demo offline.

Under section four point one, Aiko Mori expects data claims to carry owners and dates.

Section four point one treats manifests as data version as testable only when evidence and ticket IDs are recorded.

For section four point one, Brightwave Digital will not accept data work without a written trail.

### 4.2 Version ranges

Advisories state affected ranges, such as "at least 2.0.0 and below 3.2.0". Versions must be compared as numbers, part by part, not as text.

Section four point two develops data models with a Brightwave Digital note Diego Ramos can demo offline.

Under section four point two, Aiko Mori expects data claims to carry owners and dates.

Section four point two treats manifests as data version as testable only when evidence and ticket IDs are recorded.

For section four point two, Brightwave Digital will not accept data work without a written trail.

### Lab — Lab — who is affected?

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

Three projects use upload-kit. greenleaf-booking (3.1.0) and museum-tickets (2.9.8) fall in the affected range; kiteschool-site (3.4.2) is above it and safe. harbour-cafe does not use upload-kit. In January this took three days by hand; the script answers in under a second.

Section four point three develops data models with a Brightwave Digital note Diego Ramos can demo offline.

Under section four point three, Aiko Mori expects data claims to carry owners and dates.

Section four point three treats manifests as data version as testable only when evidence and ticket IDs are recorded.

### 4.4 Keeping current

The inventory is rebuilt nightly from every repository's lockfile, so it reflects exactly what each project installs.

Section four point four develops data models with a Brightwave Digital note Diego Ramos can demo offline.

Under section four point four, Aiko Mori expects data claims to carry owners and dates.

Section four point four treats manifests as data version as testable only when evidence and ticket IDs are recorded.

For section four point four, Brightwave Digital will not accept data work without a written trail.

### 4.5 Data quality

Projects without lockfiles show as "unknown" and are fixed first, since their real versions cannot be known.

Section four point five develops data models with a Brightwave Digital note Diego Ramos can demo offline.

Under section four point five, Aiko Mori expects data claims to carry owners and dates.

Section four point five treats manifests as data version as testable only when evidence and ticket IDs are recorded.

For section four point five, Brightwave Digital will not accept data work without a written trail.

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

- **EX010 — Lab result.** Which projects were affected? *Rubric:* 3 = greenleaf-booking, museum-tickets; 2 = one; 1 = none; 0 = none.
- **EX011 — Text comparison.** Why not compare versions as text? *Rubric:* 3 = wrong ordering e.g. 3.10 vs 3.2; 2 = partial; 1 = none; 0 = none.
- **EX012 — Missing lockfiles.** Why fix projects without lockfiles first? *Rubric:* 3 = real versions unknown; 2 = partial; 1 = none; 0 = none.

### Synthesis

Treat manifests as data so "who is affected?" takes seconds.

### Continue studying — chapter 04 of 30

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Security literacy

### Learning outcomes

You will (1) explain core application security concepts; (2) use the OWASP Top 10:2021 categories; (3) read advisories and CWE names; (4) explain supply-chain risk to clients.

### 5.1 Core ideas

Confidentiality (pet owners' details), integrity (bookings, prices and the code itself) and availability (clinics need bookings to work).

Section five point one develops security literacy with a Brightwave Digital note Diego Ramos can demo offline.

Under section five point one, Aiko Mori expects security claims to carry owners and dates.

Section five point one treats core ideas owasp top as testable only when evidence and ticket IDs are recorded.

For section five point one, Brightwave Digital will not accept security work without a written trail.

### 5.2 OWASP Top 10:2021

Categories include Broken Access Control (A01), Injection (A03), Insecure Design (A04), Security Misconfiguration (A05), Vulnerable and Outdated Components (A06) and Software and Data Integrity Failures (A08). The January upload-kit case is an A06 problem.

Section five point two develops security literacy with a Brightwave Digital note Diego Ramos can demo offline.

Under section five point two, Aiko Mori expects security claims to carry owners and dates.

Section five point two treats core ideas owasp top as testable only when evidence and ticket IDs are recorded.

### 5.3 Advisories

An advisory lists the package, affected and fixed versions, severity and a description. Diego learns to read the fixed version first: it tells you what to upgrade to.

Section five point three develops security literacy with a Brightwave Digital note Diego Ramos can demo offline.

Under section five point three, Aiko Mori expects security claims to carry owners and dates.

Section five point three treats core ideas owasp top as testable only when evidence and ticket IDs are recorded.

For section five point three, Brightwave Digital will not accept security work without a written trail.

### 5.4 CWE

The CWE Top 25 names weaknesses such as unrestricted upload of dangerous file types (CWE-434), relevant to Greenleaf's upload feature.

Section five point four develops security literacy with a Brightwave Digital note Diego Ramos can demo offline.

Under section five point four, Aiko Mori expects security claims to carry owners and dates.

Section five point four treats core ideas owasp top as testable only when evidence and ticket IDs are recorded.

For section five point four, Brightwave Digital will not accept security work without a written trail.

### 5.5 Supply chain risk

Ohm et al. (2020) and Ladisa et al. (2023) describe how attackers target packages, build systems and distribution, not just applications. Defenders respond with inventories, updates, integrity checks and provenance.

Section five point five develops security literacy with a Brightwave Digital note Diego Ramos can demo offline.

Under section five point five, Aiko Mori expects security claims to carry owners and dates.

Section five point five treats core ideas owasp top as testable only when evidence and ticket IDs are recorded.

For section five point five, Brightwave Digital will not accept security work without a written trail.

### 5.6 Talking to clients

Clients want to know: are we affected, what did you do, do we need to do anything? Diego practises answering these in three sentences.

Section five point six develops security literacy with a Brightwave Digital note Diego Ramos can demo offline.

Under section five point six, Aiko Mori expects security claims to carry owners and dates.

Section five point six treats core ideas owasp top as testable only when evidence and ticket IDs are recorded.

For section five point six, Brightwave Digital will not accept security work without a written trail.

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

- **EX013 — Category.** Which Top 10 category is the upload-kit case? *Rubric:* 3 = A06; 2 = partial; 1 = none; 0 = none.
- **EX014 — CWE-434.** What is CWE-434? *Rubric:* 3 = unrestricted upload of dangerous file types; 2 = partial; 1 = none; 0 = none.
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

Each client app runs as a process under its own user with limited permissions. It can read its code and write only to its upload and log folders. If a flaw is misused, the damage stays within these rights.

Section six point one develops operating systems and virtualization with a Brightwave Digital note Diego Ramos can demo offline.

Under section six point one, Aiko Mori expects operating claims to carry owners and dates.

Section six point one treats processes and permissions containers as testable only when evidence and ticket IDs are recorded.

### 6.2 Containers

Brightwave packages each app as a container image built from a small base image. Containers isolate client apps from each other on shared hosts, so a problem in one client's app does not reach another's files.

Section six point two develops operating systems and virtualization with a Brightwave Digital note Diego Ramos can demo offline.

Under section six point two, Aiko Mori expects operating claims to carry owners and dates.

Section six point two treats processes and permissions containers as testable only when evidence and ticket IDs are recorded.

### 6.3 Virtual machines

The hosting platform runs containers on virtual machines; the cloud provider is responsible for isolating machines between customers, Brightwave for everything inside its account.

Section six point three develops operating systems and virtualization with a Brightwave Digital note Diego Ramos can demo offline.

Under section six point three, Aiko Mori expects operating claims to carry owners and dates.

Section six point three treats processes and permissions containers as testable only when evidence and ticket IDs are recorded.

For section six point three, Brightwave Digital will not accept operating work without a written trail.

### 6.4 Build isolation

Builds run in fresh containers that are deleted afterwards, so nothing left by one build affects the next. SLSA v1.0 build requirements describe isolated, hosted builds as a foundation for trustworthy artifacts.

Section six point four develops operating systems and virtualization with a Brightwave Digital note Diego Ramos can demo offline.

Under section six point four, Aiko Mori expects operating claims to carry owners and dates.

Section six point four treats processes and permissions containers as testable only when evidence and ticket IDs are recorded.

### 6.5 Patching

Base images are rebuilt weekly with operating system updates, and each image is recorded by digest so Brightwave knows which image every release used.

Section six point five develops operating systems and virtualization with a Brightwave Digital note Diego Ramos can demo offline.

Under section six point five, Aiko Mori expects operating claims to carry owners and dates.

Section six point five treats processes and permissions containers as testable only when evidence and ticket IDs are recorded.

For section six point five, Brightwave Digital will not accept operating work without a written trail.

### 6.6 Upload handling

Uploaded files are stored outside the app's code folder and are never executed. The storage bucket for uploads is separated from site images after Diego's chapter 1 finding.

Section six point six develops operating systems and virtualization with a Brightwave Digital note Diego Ramos can demo offline.

Under section six point six, Aiko Mori expects operating claims to carry owners and dates.

Section six point six treats processes and permissions containers as testable only when evidence and ticket IDs are recorded.

For section six point six, Brightwave Digital will not accept operating work without a written trail.

### Image checks

Besides the administrator check, the build also rejects images based on unsupported operating system versions, so no client stays on a base that no longer receives updates.

### Worked example

Diego finds that one older client app runs as the administrator user inside its container. He changes it to a dedicated user, fixes the two folders whose permissions then need adjusting, and adds a build check that fails if any image runs as administrator.

> **Synthetic case.** Systems and findings are synthetic.

### Errors and limits

Containers share the host's kernel; they reduce risk but are not perfect isolation.

### Exercises

- **EX016 — App permissions.** What can each app process write to? *Rubric:* 3 = upload and log folders only; 2 = partial; 1 = none; 0 = none.
- **EX017 — Isolation purpose.** Why use containers for client apps? *Rubric:* 3 = isolate clients from each other; 2 = partial; 1 = none; 0 = none.
- **EX018 — Admin finding.** What did Diego change in the older app? *Rubric:* 3 = run as dedicated user; build check; 2 = partial; 1 = none; 0 = none.

### Synthesis

Least privilege, isolation and patched images limit damage.

### Continue studying — chapter 06 of 30

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Identity and access foundations

### Learning outcomes

You will (1) manage developer and client access to systems; (2) apply multi-factor authentication; (3) use roles and least privilege; (4) review access regularly.

### 7.1 Developer access

Developers sign in to code hosting, the build service and the hosting platform with multi-factor authentication. Each has only the roles needed: most can deploy to test environments; only two can deploy to production.

Section seven point one develops identity and access foundations with a Brightwave Digital note Diego Ramos can demo offline.

Under section seven point one, Aiko Mori expects identity claims to carry owners and dates.

Section seven point one treats developer access client access as testable only when evidence and ticket IDs are recorded.

### 7.2 Client access

Clinic staff log into their booking admin pages with their own accounts; shared logins are not allowed. OWASP Top 10:2021 A07 covers identification and authentication failures.

Section seven point two develops identity and access foundations with a Brightwave Digital note Diego Ramos can demo offline.

Under section seven point two, Aiko Mori expects identity claims to carry owners and dates.

Section seven point two treats developer access client access as testable only when evidence and ticket IDs are recorded.

For section seven point two, Brightwave Digital will not accept identity work without a written trail.

### 7.3 Service accounts

The build service uses a dedicated identity with permission to push images, not a developer's personal token.

Section seven point three develops identity and access foundations with a Brightwave Digital note Diego Ramos can demo offline.

Under section seven point three, Aiko Mori expects identity claims to carry owners and dates.

Section seven point three treats developer access client access as testable only when evidence and ticket IDs are recorded.

For section seven point three, Brightwave Digital will not accept identity work without a written trail.

### 7.4 Tokens

Long-lived tokens are replaced with short-lived ones where the platform allows, reducing harm if a token leaks.

Section seven point four develops identity and access foundations with a Brightwave Digital note Diego Ramos can demo offline.

Under section seven point four, Aiko Mori expects identity claims to carry owners and dates.

Section seven point four treats developer access client access as testable only when evidence and ticket IDs are recorded.

For section seven point four, Brightwave Digital will not accept identity work without a written trail.

### 7.5 Access reviews

Every quarter Diego lists who has which access and asks owners to confirm. Leavers' access is removed on their last day.

Section seven point five develops identity and access foundations with a Brightwave Digital note Diego Ramos can demo offline.

Under section seven point five, Aiko Mori expects identity claims to carry owners and dates.

Section seven point five treats developer access client access as testable only when evidence and ticket IDs are recorded.

For section seven point five, Brightwave Digital will not accept identity work without a written trail.

### 7.6 Role design

Roles for clinic staff: receptionist (manage bookings), vet (view records), manager (settings and staff). Checks happen on the server.

Section seven point six develops identity and access foundations with a Brightwave Digital note Diego Ramos can demo offline.

Under section seven point six, Aiko Mori expects identity claims to carry owners and dates.

Section seven point six treats developer access client access as testable only when evidence and ticket IDs are recorded.

For section seven point six, Brightwave Digital will not accept identity work without a written trail.

### Leaver checklist

The leaver checklist now lists every place access might exist: code hosting, the build service, the hosting platform, the image registry, client admin pages used for support, and shared password vaults. Each line is ticked by a named person on the leaver's last day, and the record is kept with the access review. Diego also asks the platform owners to send a monthly list of accounts with no sign-in in 60 days, since unused accounts are often forgotten accounts. The first such list finds four, all removed after confirming with their owners.

### Worked example

The first access review finds a former contractor still able to deploy to three client projects. Access is removed the same day, and the leaver checklist gets a line for build and hosting access.

> **Synthetic case.** Accounts and findings are synthetic.

### Errors and limits

Access reviews only help if owners check carefully; ask them to confirm each name, not approve the list in bulk.

### Exercises

- **EX019 — Production deploy.** Who can deploy to production? *Rubric:* 3 = only two developers; 2 = partial; 1 = none; 0 = none.
- **EX020 — Build identity.** What identity does the build service use? *Rubric:* 3 = dedicated identity, not personal token; 2 = partial; 1 = none; 0 = none.
- **EX021 — Review finding.** What did the first review find? *Rubric:* 3 = former contractor with deploy access; 2 = partial; 1 = none; 0 = none.

### Synthesis

Strong sign-in, least privilege and regular reviews keep access under control.

### Continue studying — chapter 07 of 30

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Security architecture basics

### Learning outcomes

You will (1) apply layered defences to client apps; (2) place trust boundaries; (3) separate environments and clients; (4) document a standard architecture.

### 8.1 Layers

Edge protections (HTTPS, rate limiting), application controls (validation, authorisation, encoding), data protection (encryption, least-privilege database accounts) and pipeline controls (reviews, dependency checks, isolated builds).

Section eight point one develops security architecture basics with a Brightwave Digital note Diego Ramos can demo offline.

Under section eight point one, Aiko Mori expects security claims to carry owners and dates.

Section eight point one treats layers trust boundaries separating as testable only when evidence and ticket IDs are recorded.

For section eight point one, Brightwave Digital will not accept security work without a written trail.

### 8.2 Trust boundaries

Boundaries exist between visitor and app, app and database, app and external services, build and production, and between clients. Each boundary gets a check.

Section eight point two develops security architecture basics with a Brightwave Digital note Diego Ramos can demo offline.

Under section eight point two, Aiko Mori expects security claims to carry owners and dates.

Section eight point two treats layers trust boundaries separating as testable only when evidence and ticket IDs are recorded.

For section eight point two, Brightwave Digital will not accept security work without a written trail.

### 8.3 Separating clients

Each client has its own database, storage bucket and secrets. A flaw in one client's app cannot read another client's data.

Section eight point three develops security architecture basics with a Brightwave Digital note Diego Ramos can demo offline.

Under section eight point three, Aiko Mori expects security claims to carry owners and dates.

Section eight point three treats layers trust boundaries separating as testable only when evidence and ticket IDs are recorded.

For section eight point three, Brightwave Digital will not accept security work without a written trail.

### 8.4 Environments

Test and production are separate, with separate secrets and data; test uses synthetic data only.

Section eight point four develops security architecture basics with a Brightwave Digital note Diego Ramos can demo offline.

Under section eight point four, Aiko Mori expects security claims to carry owners and dates.

Section eight point four treats layers trust boundaries separating as testable only when evidence and ticket IDs are recorded.

For section eight point four, Brightwave Digital will not accept security work without a written trail.

### 8.5 Standard architecture

Brightwave writes a one-page standard for new projects, so security decisions are made once and reused.

Section eight point five develops security architecture basics with a Brightwave Digital note Diego Ramos can demo offline.

Under section eight point five, Aiko Mori expects security claims to carry owners and dates.

Section eight point five treats layers trust boundaries separating as testable only when evidence and ticket IDs are recorded.

For section eight point five, Brightwave Digital will not accept security work without a written trail.

### 8.6 Exceptions

Projects that differ from the standard record why.

Section eight point six develops security architecture basics with a Brightwave Digital note Diego Ramos can demo offline.

Under section eight point six, Aiko Mori expects security claims to carry owners and dates.

Section eight point six treats layers trust boundaries separating as testable only when evidence and ticket IDs are recorded.

For section eight point six, Brightwave Digital will not accept security work without a written trail.

Section eight point six fails closed if security evidence is missing rather than guessing.

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
- **EX024 — Shared database.** What was found and fixed? *Rubric:* 3 = two clients sharing a database; split; 2 = partial; 1 = none; 0 = none.

### Synthesis

Layer controls, guard boundaries and separate clients by default.

### Continue studying — chapter 08 of 30

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Evidence and measurement

### Learning outcomes

You will (1) measure dependency freshness and remediation; (2) choose measures that drive the right behaviour; (3) collect evidence automatically; (4) present trends.

### 9.1 Freshness

How old is each installed library version? Old versions miss fixes and are more likely to be affected by advisories. Kula et al. (2018) found developers often leave dependencies outdated.

Section nine point one develops evidence and measurement with a Brightwave Digital note Diego Ramos can demo offline.

Under section nine point one, Aiko Mori expects evidence claims to carry owners and dates.

Section nine point one treats freshness lab result remediation as testable only when evidence and ticket IDs are recorded.

For section nine point one, Brightwave Digital will not accept evidence work without a written trail.

### Lab — Lab — version age

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

For Greenleaf, date-utils is 1,141 days old and upload-kit 637 days; both are flagged stale (over 365 days). forms is 101 days old and mailer 26 days. upload-kit's age explains why the January advisory found it vulnerable.

Section nine point two develops evidence and measurement with a Brightwave Digital note Diego Ramos can demo offline.

Under section nine point two, Aiko Mori expects evidence claims to carry owners and dates.

Section nine point two treats freshness lab result remediation as testable only when evidence and ticket IDs are recorded.

### 9.3 Remediation time

Days from an advisory's publication to the fix being deployed, per severity.

Section nine point three develops evidence and measurement with a Brightwave Digital note Diego Ramos can demo offline.

Under section nine point three, Aiko Mori expects evidence claims to carry owners and dates.

Section nine point three treats freshness lab result remediation as testable only when evidence and ticket IDs are recorded.

For section nine point three, Brightwave Digital will not accept evidence work without a written trail.

Section nine point three fails closed if evidence evidence is missing rather than guessing.

### 9.4 Behaviour

Measures can drive the wrong behaviour: counting "libraries updated" could encourage risky bulk updates without tests. Brightwave measures outcomes: stale count and remediation time.

Section nine point four develops evidence and measurement with a Brightwave Digital note Diego Ramos can demo offline.

Under section nine point four, Aiko Mori expects evidence claims to carry owners and dates.

Section nine point four treats freshness lab result remediation as testable only when evidence and ticket IDs are recorded.

For section nine point four, Brightwave Digital will not accept evidence work without a written trail.

### 9.5 Automatic evidence

Measures come from the nightly inventory and deployment records, not manual reports.

Section nine point five develops evidence and measurement with a Brightwave Digital note Diego Ramos can demo offline.

Under section nine point five, Aiko Mori expects evidence claims to carry owners and dates.

Section nine point five treats freshness lab result remediation as testable only when evidence and ticket IDs are recorded.

For section nine point five, Brightwave Digital will not accept evidence work without a written trail.

Section nine point five fails closed if evidence evidence is missing rather than guessing.

### 9.6 Presenting

A monthly chart shows stale libraries and remediation times across clients.

Section nine point six develops evidence and measurement with a Brightwave Digital note Diego Ramos can demo offline.

Under section nine point six, Aiko Mori expects evidence claims to carry owners and dates.

Section nine point six treats freshness lab result remediation as testable only when evidence and ticket IDs are recorded.

For section nine point six, Brightwave Digital will not accept evidence work without a written trail.

Section nine point six fails closed if evidence evidence is missing rather than guessing.

### Choosing thresholds

The 365-day stale threshold is a starting point that the team agreed together. For libraries handling uploads, authentication or payments, Diego uses a stricter threshold of 180 days, because flaws there matter more. Thresholds are reviewed each quarter against what the advisories actually show: if many advisories hit versions younger than the threshold, it is too loose. The lab prints the threshold it used, so anyone reading the output knows which rule applied.

### Reading the lab

The lab compares each installed version's release date with today's date and prints the age in days and a status. Diego checks that the dates are correct before trusting the result.

### Worked example

After six months of weekly updates, the number of stale library versions across all clients falls from 64 to 18. The remaining 18 are mostly in two legacy projects scheduled for rebuild.

> **Synthetic case.** Ages and counts are synthetic.

### Errors and limits

Age is a rough proxy; a new version can still have flaws, an old one may be fine.

### Exercises

- **EX025 — Lab stale.** Which libraries were stale? *Rubric:* 3 = date-utils 1,141; upload-kit 637; 2 = one; 1 = none; 0 = none.
- **EX026 — Bad measure.** Why not count libraries updated? *Rubric:* 3 = encourages risky bulk updates; 2 = partial; 1 = none; 0 = none.
- **EX027 — Six-month result.** What did six months of updates achieve? *Rubric:* 3 = stale 64 to 18; 2 = partial; 1 = none; 0 = none.

### Synthesis

Measure freshness and remediation from automatic evidence.

### Continue studying — chapter 09 of 30

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Application and software supply chain security: orientation

### Learning outcomes

You will (1) define application and software supply chain security; (2) map the stages from code to client site; (3) place frameworks on the map; (4) see Brightwave's gaps.

### 10.1 Definitions

Application security protects the software's design and code. Supply chain security protects everything that goes into it and how it reaches users: source, dependencies, build, artifacts, deployment and updates.

Section ten point one develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section ten point one, Aiko Mori expects application claims to carry owners and dates.

Section ten point one treats definitions the stages frameworks as testable only when evidence and ticket IDs are recorded.

### 10.2 The stages

For Brightwave: developers write code; libraries are fetched; the build service builds images; images go to a registry; deployment puts them on hosting; updates repeat the cycle.

Section ten point two develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section ten point two, Aiko Mori expects application claims to carry owners and dates.

Section ten point two treats definitions the stages frameworks as testable only when evidence and ticket IDs are recorded.

For section ten point two, Brightwave Digital will not accept application work without a written trail.

### 10.3 Frameworks

NIST SP 800-218 (SSDF) groups practices into Prepare the Organization, Protect the Software, Produce Well-Secured Software and Respond to Vulnerabilities. SLSA v1.0 focuses on build integrity and provenance. OWASP SAMM v2 assesses maturity. OWASP ASVS defines application requirements.

Section ten point three develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section ten point three, Aiko Mori expects application claims to carry owners and dates.

Section ten point three treats definitions the stages frameworks as testable only when evidence and ticket IDs are recorded.

### 10.4 Brightwave's gaps

Mapping to the SSDF shows strengths in producing software (reviews, tests) but gaps in responding: no inventory before January, no target times for fixes.

Section ten point four develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section ten point four, Aiko Mori expects application claims to carry owners and dates.

Section ten point four treats definitions the stages frameworks as testable only when evidence and ticket IDs are recorded.

For section ten point four, Brightwave Digital will not accept application work without a written trail.

### 10.5 Trust

Thompson (1984) reminded developers that you cannot fully trust code you did not create; evidence such as hashes and provenance is how trust is earned.

Section ten point five develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section ten point five, Aiko Mori expects application claims to carry owners and dates.

Section ten point five treats definitions the stages frameworks as testable only when evidence and ticket IDs are recorded.

For section ten point five, Brightwave Digital will not accept application work without a written trail.

### 10.6 The course plan

The next chapters build Brightwave's inventory, checks, controls and monitoring.

Section ten point six develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section ten point six, Aiko Mori expects application claims to carry owners and dates.

Section ten point six treats definitions the stages frameworks as testable only when evidence and ticket IDs are recorded.

For section ten point six, Brightwave Digital will not accept application work without a written trail.

Section ten point six fails closed if application evidence is missing rather than guessing.

### Where the case fits

The upload-kit incident touches several stages: an outdated library was fetched, built into images and deployed without anyone recording which clients had it. The fix therefore needs work at several stages, not just one patch. That is why the course moves through inventory, checks, build controls and monitoring in order.

### Worked example

Diego and Aiko agree three goals for the placement year: an inventory answering "who is affected" in minutes, fixes for high advisories within 7 days across all clients, and verified, recorded builds for every deployment.

> **Synthetic case.** Goals are synthetic.

### Errors and limits

Frameworks describe what good looks like; small agencies must choose what is proportionate.

### Exercises

- **EX028 — Stages.** List the stages for Brightwave. *Rubric:* 3 = code, libraries, build, registry, deploy, update; 2 = four; 1 = two; 0 = none.
- **EX029 — SSDF gap.** Where were Brightwave's SSDF gaps? *Rubric:* 3 = Respond: no inventory, no fix targets; 2 = partial; 1 = none; 0 = none.
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

Greenleaf's booking site holds owners' names, phone numbers and emails, pet medical notes, uploaded X-rays and reports, and appointment histories. Medical notes and uploads are the most sensitive because they are private and hard to replace. The harbour-cafe site, by contrast, holds only table bookings with a name and phone number.

Section eleven point one develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section eleven point one, Aiko Mori expects application claims to carry owners and dates.

### 11.2 Supply chain assets

Code repositories, the library registry configuration, the build service, signing and deployment credentials, the image registry and the hosting accounts are all assets. A weakness in any of them could change every client's site at once, which makes them more important than any single client app.

Section eleven point two develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section eleven point two, Aiko Mori expects application claims to carry owners and dates.

Section eleven point two treats data assets supply chain as testable only when evidence and ticket IDs are recorded.

### 11.3 Rating importance

Diego rates each asset high, medium or low using two questions: how much harm if it were exposed or changed, and how many clients depend on it. Deployment credentials score high on both; a single client's public image folder scores low.

Section eleven point three develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section eleven point three, Aiko Mori expects application claims to carry owners and dates.

Section eleven point three treats data assets supply chain as testable only when evidence and ticket IDs are recorded.

### 11.4 Owners

Every asset has a named owner who decides about access and changes. The build service is owned by Aiko; each client app by its lead developer.

Section eleven point four develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section eleven point four, Aiko Mori expects application claims to carry owners and dates.

Section eleven point four treats data assets supply chain as testable only when evidence and ticket IDs are recorded.

For section eleven point four, Brightwave Digital will not accept application work without a written trail.

### 11.5 Context records

The inventory gains a short context note per project: data held, internet exposure, the client's contact for incidents, and any contract requirements such as response times.

Section eleven point five develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section eleven point five, Aiko Mori expects application claims to carry owners and dates.

Section eleven point five treats data assets supply chain as testable only when evidence and ticket IDs are recorded.

For section eleven point five, Brightwave Digital will not accept application work without a written trail.

### 11.6 Using context

When an advisory arrives, context decides the order of work: projects with sensitive data and public exposure come first.

Section eleven point six develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section eleven point six, Aiko Mori expects application claims to carry owners and dates.

Section eleven point six treats data assets supply chain as testable only when evidence and ticket IDs are recorded.

For section eleven point six, Brightwave Digital will not accept application work without a written trail.

### Worked example

Context changes the order of work during the next advisory, which affects a form library used by eight clients. Greenleaf and museum-tickets, holding medical notes and payment references, are patched the same day; the three small brochure sites with no forms in use are patched in the weekly cycle.

> **Synthetic case.** Assets and ratings are synthetic.

### Errors and limits

Ratings are judgements; record the reasoning so others can challenge them.

### Exercises

- **EX031 — Most sensitive.** Which Greenleaf assets are most sensitive? *Rubric:* 3 = medical notes and uploads; 2 = one; 1 = none; 0 = none.
- **EX032 — Supply chain importance.** Why do supply chain assets rate highly? *Rubric:* 3 = affect all clients at once; 2 = partial; 1 = none; 0 = none.
- **EX033 — Context order.** How did context order the form-library patching? *Rubric:* 3 = sensitive same day; brochure sites weekly; 2 = partial; 1 = none; 0 = none.

### Synthesis

Know assets, owners and context so priorities follow real harm.

### Continue studying — chapter 11 of 30

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Application and software supply chain security: data flows

### Learning outcomes

You will (1) draw data flows for a client app and the build pipeline; (2) mark trust boundaries; (3) find where checks are needed; (4) keep diagrams current.

### 12.1 Application flow

For Greenleaf: the visitor's browser sends a booking form and an upload to the web app; the app checks it, stores the booking in the database and the file in the upload bucket; staff view bookings through the admin pages; the app sends a confirmation through the email service.

Section twelve point one develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twelve point one, Aiko Mori expects application claims to carry owners and dates.

### 12.2 Pipeline flow

A developer pushes code; the build service fetches code and libraries, runs tests and checks, builds an image, pushes it to the registry, and the deployment step pulls the image onto hosting. Secrets are injected only at deployment.

Section twelve point two develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twelve point two, Aiko Mori expects application claims to carry owners and dates.

Section twelve point two treats application flow pipeline flow as testable only when evidence and ticket IDs are recorded.

### 12.3 Trust boundaries

Marked boundaries: browser to app, app to database and bucket, app to email service, public library registry to build, build to registry, registry to hosting. Shostack (2014) recommends drawing such diagrams as the starting point for asking what can go wrong.

Section twelve point three develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twelve point three, Aiko Mori expects application claims to carry owners and dates.

Section twelve point three treats application flow pipeline flow as testable only when evidence and ticket IDs are recorded.

### 12.4 Checks at boundaries

Each boundary needs a check: validation and size limits for uploads; least-privilege database accounts; pinned and verified libraries entering the build; recorded digests for images entering hosting.

Section twelve point four develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twelve point four, Aiko Mori expects application claims to carry owners and dates.

Section twelve point four treats application flow pipeline flow as testable only when evidence and ticket IDs are recorded.

For section twelve point four, Brightwave Digital will not accept application work without a written trail.

### 12.5 Keeping current

Diagrams live in each repository and are updated in the same pull request that changes a flow. Reviewers ask "does the diagram still match?" when a change adds a service.

Section twelve point five develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twelve point five, Aiko Mori expects application claims to carry owners and dates.

Section twelve point five treats application flow pipeline flow as testable only when evidence and ticket IDs are recorded.

### 12.6 Common surprises

Drawing flows often reveals forgotten paths, such as an old export feature or a test webhook still enabled.

Section twelve point six develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twelve point six, Aiko Mori expects application claims to carry owners and dates.

Section twelve point six treats application flow pipeline flow as testable only when evidence and ticket IDs are recorded.

For section twelve point six, Brightwave Digital will not accept application work without a written trail.

### Worked example

Drawing the Greenleaf flow reveals a forgotten path: an old CSV export endpoint that lists all bookings, reachable by any logged-in staff account including receptionists. It is restricted to managers and its use logged.

> **Synthetic case.** Flows are synthetic.

### Errors and limits

A diagram is a model; walk through the running system to check it.

### Exercises

- **EX034 — Pipeline entry.** Where do libraries enter the pipeline? *Rubric:* 3 = public registry to build boundary; 2 = partial; 1 = none; 0 = none.
- **EX035 — Upload check.** What check guards the upload boundary? *Rubric:* 3 = validation and size limits; 2 = partial; 1 = none; 0 = none.
- **EX036 — Forgotten path.** What did the Greenleaf diagram reveal? *Rubric:* 3 = CSV export reachable by any staff; 2 = partial; 1 = none; 0 = none.

### Synthesis

Draw flows, mark boundaries and put a check on each.

### Continue studying — chapter 12 of 30

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Application and software supply chain security: risk scenarios

### Learning outcomes

You will (1) write risk scenarios for client apps and the supply chain; (2) estimate likelihood and impact; (3) link scenarios to controls; (4) review them.

### 13.1 Writing scenarios

A scenario says what could happen, through which weakness, and what harm follows: "An outdated upload library with a known flaw lets a visitor's upload affect the server, exposing medical records." Scenarios describe outcomes, not procedures.

Section thirteen point one develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section thirteen point one, Aiko Mori expects application claims to carry owners and dates.

Section thirteen point one treats writing scenarios supply chain as testable only when evidence and ticket IDs are recorded.

### 13.2 Supply chain scenarios

Ladisa et al. (2023) catalogue attacks on open-source supply chains, such as a library maintainer's account being taken over and a harmful version published. Ohm et al. (2020) studied real malicious packages. Brightwave writes scenarios for these kinds of events at the level of "a harmful library version enters a build".

Section thirteen point two develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section thirteen point two, Aiko Mori expects application claims to carry owners and dates.

### 13.3 Likelihood and impact

Each scenario gets low, medium or high for likelihood and impact, using evidence: advisories seen, exposure, data held, number of clients.

Section thirteen point three develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section thirteen point three, Aiko Mori expects application claims to carry owners and dates.

Section thirteen point three treats writing scenarios supply chain as testable only when evidence and ticket IDs are recorded.

For section thirteen point three, Brightwave Digital will not accept application work without a written trail.

### 13.4 Linking controls

Each scenario lists its controls: for a harmful library version, pinned versions with hashes, a short delay before adopting brand-new versions, and review of dependency changes.

Section thirteen point four develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section thirteen point four, Aiko Mori expects application claims to carry owners and dates.

Section thirteen point four treats writing scenarios supply chain as testable only when evidence and ticket IDs are recorded.

For section thirteen point four, Brightwave Digital will not accept application work without a written trail.

### 13.5 Review

Scenarios are reviewed every six months and after any incident.

Section thirteen point five develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section thirteen point five, Aiko Mori expects application claims to carry owners and dates.

Section thirteen point five treats writing scenarios supply chain as testable only when evidence and ticket IDs are recorded.

For section thirteen point five, Brightwave Digital will not accept application work without a written trail.

Section thirteen point five fails closed if application evidence is missing rather than guessing.

### 13.6 Ranking

The top five scenarios get named owners and target dates for missing controls.

Section thirteen point six develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section thirteen point six, Aiko Mori expects application claims to carry owners and dates.

Section thirteen point six treats writing scenarios supply chain as testable only when evidence and ticket IDs are recorded.

For section thirteen point six, Brightwave Digital will not accept application work without a written trail.

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
- **EX039 — Top scenario.** What was the top-ranked scenario? *Rubric:* 3 = outdated library with known flaw in public app; 2 = partial; 1 = none; 0 = none.

### Synthesis

Scenarios link evidence to controls and priorities.

### Continue studying — chapter 13 of 30

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Application and software supply chain security: methods I

### Learning outcomes

You will (1) validate file uploads safely; (2) check type, content and size; (3) store uploads safely; (4) test the checks with synthetic files.

### 14.1 Why uploads matter

The Greenleaf flaw was in upload handling. Even with a patched library, Brightwave wants its own checks so that a future library flaw is less likely to be reachable. OWASP ASVS 4.0.3 section V12 covers files and resources.

Section fourteen point one develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section fourteen point one, Aiko Mori expects application claims to carry owners and dates.

Section fourteen point one treats why uploads matter the as testable only when evidence and ticket IDs are recorded.

### 14.2 The checks

Allow only listed types (PNG, JPEG, PDF); check that the file content matches the claimed type by its leading bytes; limit size to 5 MB; give stored files new random names; store them outside the web root and serve them with a safe download header.

Section fourteen point two develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section fourteen point two, Aiko Mori expects application claims to carry owners and dates.

Section fourteen point two treats why uploads matter the as testable only when evidence and ticket IDs are recorded.

### Lab — Lab — upload checks

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

xray.png and report.pdf are accepted. notes.pdf is rejected because its content does not match a PDF. scan.png is rejected as too large. run.exe is rejected because the type is not allowed. Every rejection names its reason, which helps support staff explain it to clinic users.

Section fourteen point three develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section fourteen point three, Aiko Mori expects application claims to carry owners and dates.

### 14.4 Testing

Synthetic test files cover each rule. Tests run in the build on every change.

Section fourteen point four develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section fourteen point four, Aiko Mori expects application claims to carry owners and dates.

Section fourteen point four treats why uploads matter the as testable only when evidence and ticket IDs are recorded.

For section fourteen point four, Brightwave Digital will not accept application work without a written trail.

### 14.5 Limits

Content checks reduce risk but cannot prove a file is harmless; storage and serving rules provide the second layer.

Section fourteen point five develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section fourteen point five, Aiko Mori expects application claims to carry owners and dates.

Section fourteen point five treats why uploads matter the as testable only when evidence and ticket IDs are recorded.

For section fourteen point five, Brightwave Digital will not accept application work without a written trail.

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
- **EX041 — Second layer.** What protects if a checked file is still harmful? *Rubric:* 3 = storage outside web root; safe serving; random names; 2 = partial; 1 = none; 0 = none.
- **EX042 — Oversize response.** How was oversized photo uploads handled? *Rubric:* 3 = clear message, not raised limit; 2 = partial; 1 = none; 0 = none.

### Synthesis

Validate uploads on type, content and size, and store them safely.

### Continue studying — chapter 14 of 30

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Application and software supply chain security: guided lab

### Learning outcomes

You will (1) run a dependency audit across clients; (2) read advisory matches; (3) total by severity; (4) turn results into tasks.

### 15.1 The audit

The audit compares each client's installed library versions with a synthetic advisory list, each advisory naming a library, affected versions and severity.

Section fifteen point one develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section fifteen point one, Aiko Mori expects application claims to carry owners and dates.

Section fifteen point one treats the audit lab result as testable only when evidence and ticket IDs are recorded.

For section fifteen point one, Brightwave Digital will not accept application work without a written trail.

### Lab — Lab — dependency audit

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

Greenleaf matches ADV-7 (high) and ADV-8 (medium); museum-tickets matches ADV-7. Totals: high 2, medium 1. The output lists project, library, version and advisory, which is exactly what a developer needs to start.

Section fifteen point two develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section fifteen point two, Aiko Mori expects application claims to carry owners and dates.

Section fifteen point two treats the audit lab result as testable only when evidence and ticket IDs are recorded.

### 15.3 Turning results into tasks

Each match becomes a task with the owner from the inventory and a due date from the severity: high within 7 days, medium within 30.

Section fifteen point three develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section fifteen point three, Aiko Mori expects application claims to carry owners and dates.

Section fifteen point three treats the audit lab result as testable only when evidence and ticket IDs are recorded.

For section fifteen point three, Brightwave Digital will not accept application work without a written trail.

### 15.4 Checking matches

Diego confirms each match by reading the advisory, since version ranges can be written ambiguously.

Section fifteen point four develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section fifteen point four, Aiko Mori expects application claims to carry owners and dates.

Section fifteen point four treats the audit lab result as testable only when evidence and ticket IDs are recorded.

For section fifteen point four, Brightwave Digital will not accept application work without a written trail.

### 15.5 Prioritisation

Where many matches arrive at once, Brightwave may consider exploit likelihood scores such as EPSS (Jacobs et al., 2021) alongside severity and client context.

Section fifteen point five develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section fifteen point five, Aiko Mori expects application claims to carry owners and dates.

Section fifteen point five treats the audit lab result as testable only when evidence and ticket IDs are recorded.

For section fifteen point five, Brightwave Digital will not accept application work without a written trail.

### Recording the audit

Each audit run is saved with its date, the advisory list version used and the matches found. When a client asks whether they were affected by an advisory, Brightwave can answer from the record rather than from memory. The record also shows how long each match stayed open, which feeds the remediation-time measure from chapter 9. Diego notices that matches in projects with an active owner close in about four days, while those in projects with no recent work take nearly three weeks, and he raises this with Aiko as a staffing issue.

### Worked example

Running the audit across all 23 client projects returns 11 matches. Diego confirms 10; one is a false match because the advisory's range excludes the installed patch version. Corrected matches become tasks, and all highs are fixed within six days.

> **Synthetic case.** Advisories and matches are synthetic.

### Errors and limits

Audits only find known advisories; they say nothing about unknown flaws.

### Exercises

- **EX043 — Lab totals.** What totals did the lab give? *Rubric:* 3 = high 2, medium 1; 2 = partial; 1 = none; 0 = none.
- **EX044 — Due dates.** What due dates apply? *Rubric:* 3 = high 7 days; medium 30; 2 = partial; 1 = none; 0 = none.
- **EX045 — False match.** Why was one match false? *Rubric:* 3 = range excluded installed version; 2 = partial; 1 = none; 0 = none.

### Synthesis

Audit, confirm, assign and fix by severity.

### Continue studying — chapter 15 of 30

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Application and software supply chain security: methods II

### Learning outcomes

You will (1) pin dependency versions with hashes; (2) use lock files; (3) review dependency changes; (4) delay adoption of brand-new versions.

### 16.1 Lock files

A lock file records the exact version and hash of every direct and transitive library. Builds install exactly what the lock file says, so two builds of the same commit get the same libraries, and a changed file in the registry is detected because its hash no longer matches.

Section sixteen point one develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section sixteen point one, Aiko Mori expects application claims to carry owners and dates.

### 16.2 Reviewing changes

Changes to the lock file appear in pull requests. Reviewers look at which libraries changed, whether a new library was added, and whether a new maintainer or install script appeared. Large unexplained changes are questioned.

Section sixteen point two develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section sixteen point two, Aiko Mori expects application claims to carry owners and dates.

Section sixteen point two treats lock files reviewing changes as testable only when evidence and ticket IDs are recorded.

### 16.3 Adoption delay

Brightwave waits a few days before adopting brand-new library versions unless they fix a security advisory, since harmful versions are often discovered and removed quickly. Ohm et al. (2020) describe how malicious packages are spread.

Section sixteen point three develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section sixteen point three, Aiko Mori expects application claims to carry owners and dates.

Section sixteen point three treats lock files reviewing changes as testable only when evidence and ticket IDs are recorded.

### 16.4 Choosing libraries

Before adding a library, developers check maintenance activity, number of maintainers and how widely it is used. Zimmermann et al. (2019) showed how a few maintainer accounts can reach very large parts of an ecosystem, and Decan et al. (2018) compared dependency networks across ecosystems.

Section sixteen point four develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section sixteen point four, Aiko Mori expects application claims to carry owners and dates.

Section sixteen point four treats lock files reviewing changes as testable only when evidence and ticket IDs are recorded.

### 16.5 Removing libraries

Unused libraries are removed; each removal shrinks what must be tracked.

Section sixteen point five develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section sixteen point five, Aiko Mori expects application claims to carry owners and dates.

Section sixteen point five treats lock files reviewing changes as testable only when evidence and ticket IDs are recorded.

For section sixteen point five, Brightwave Digital will not accept application work without a written trail.

Section sixteen point five fails closed if application evidence is missing rather than guessing.

### 16.6 Automated update requests

A bot opens weekly update pull requests with tests run, so updates are small and regular rather than large and rare.

Section sixteen point six develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section sixteen point six, Aiko Mori expects application claims to carry owners and dates.

Section sixteen point six treats lock files reviewing changes as testable only when evidence and ticket IDs are recorded.

For section sixteen point six, Brightwave Digital will not accept application work without a written trail.

### Lock file in builds

The build fails if the lock file and the dependency list disagree, so nobody can forget to update it.

### Worked example

Diego reviews an update pull request that adds a new transitive library with an install script. The team pauses, finds the parent library added it for an optional feature, and selects a configuration that avoids it.

> **Synthetic case.** Libraries and changes are synthetic.

### Errors and limits

Pinning stops surprise changes but also stops automatic fixes; pair it with regular updates.

### Exercises

- **EX046 — Lock file purpose.** What does a lock file record? *Rubric:* 3 = exact versions and hashes of all libraries; 2 = partial; 1 = none; 0 = none.
- **EX047 — Adoption delay.** Why delay brand-new versions? *Rubric:* 3 = harmful versions often found quickly; 2 = partial; 1 = none; 0 = none.
- **EX048 — Review finding.** What did Diego's review find? *Rubric:* 3 = new transitive library with install script; avoided; 2 = partial; 1 = none; 0 = none.

### Synthesis

Pin, review and update regularly.

### Continue studying — chapter 16 of 30

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Application and software supply chain security: tooling

### Learning outcomes

You will (1) review build pipeline configuration; (2) pin pipeline actions; (3) limit token permissions; (4) protect secrets from untrusted changes.

### 17.1 The pipeline as code

Each project's pipeline is a configuration file in the repository. It decides which external actions run, which permissions the build token has and which secrets are available. Mistakes here affect every build.

Section seventeen point one develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section seventeen point one, Aiko Mori expects application claims to carry owners and dates.

Section seventeen point one treats the pipeline as code as testable only when evidence and ticket IDs are recorded.

### Lab — Lab — pipeline review

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

The lab reports four issues in the synthetic pipeline: checkout@v4 and deploy-helper@main are not pinned to a commit, secrets are available to pull requests from forks, and the token has write-all permissions. Pinning to a full commit identifier means a changed action cannot silently enter the build.

Section seventeen point two develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section seventeen point two, Aiko Mori expects application claims to carry owners and dates.

### 17.3 Fixing permissions

The token gets read-only permission by default, with write only for the step that needs it.

Section seventeen point three develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section seventeen point three, Aiko Mori expects application claims to carry owners and dates.

Section seventeen point three treats the pipeline as code as testable only when evidence and ticket IDs are recorded.

For section seventeen point three, Brightwave Digital will not accept application work without a written trail.

### 17.4 Secrets and untrusted changes

Pull requests from outside contributors run without secrets. Deployment runs only from the main branch after review.

Section seventeen point four develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section seventeen point four, Aiko Mori expects application claims to carry owners and dates.

Section seventeen point four treats the pipeline as code as testable only when evidence and ticket IDs are recorded.

For section seventeen point four, Brightwave Digital will not accept application work without a written trail.

### 17.5 Applying across projects

Diego runs the review across all 23 pipelines and opens fix pull requests in batches.

Section seventeen point five develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section seventeen point five, Aiko Mori expects application claims to carry owners and dates.

Section seventeen point five treats the pipeline as code as testable only when evidence and ticket IDs are recorded.

For section seventeen point five, Brightwave Digital will not accept application work without a written trail.

### Keeping pins current

Pinned actions are updated by the same weekly bot that updates libraries. Each update shows the old and new commit, and reviewers check the action's release notes before approving. This keeps the protection of pinning without leaving old versions in place forever. Diego also writes a short template pipeline with safe defaults (pinned actions, read-only token, no secrets for forks) that new projects copy, so the same mistakes are not repeated. Within two months every new project starts from the template.

### Worked example

Across 23 pipelines, the review finds 41 unpinned actions, 9 write-all tokens and 2 pipelines exposing secrets to forks. All are fixed within three weeks, with the secret exposures fixed on the first day.

> **Synthetic case.** Pipelines and counts are synthetic.

### Errors and limits

Pinning needs updating too; a pinned old action can miss its own fixes.

### Exercises

- **EX049 — Lab issues.** List the four lab issues. *Rubric:* 3 = two unpinned; fork secrets; write-all; 2 = three; 1 = one; 0 = none.
- **EX050 — Token fix.** How were token permissions fixed? *Rubric:* 3 = read-only default, write only where needed; 2 = partial; 1 = none; 0 = none.
- **EX051 — First fix.** Which issues were fixed first and why? *Rubric:* 3 = secret exposure; most direct harm; 2 = partial; 1 = none; 0 = none.

### Synthesis

Treat pipeline configuration as security-critical code.

### Continue studying — chapter 17 of 30

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Application and software supply chain security: controls

### Learning outcomes

You will (1) record image digests for every deployment; (2) record build provenance; (3) deploy only approved images; (4) describe SLSA build levels.

### 18.1 Recording digests

Each built image has a digest, a fingerprint of its contents. The deployment record stores the digest, the commit and the build run, so Brightwave can always say exactly what is running.

Section eighteen point one develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section eighteen point one, Aiko Mori expects application claims to carry owners and dates.

Section eighteen point one treats recording digests provenance approved as testable only when evidence and ticket IDs are recorded.

### 18.2 Provenance

Provenance is a signed statement of how an artifact was built: source, builder and steps. SLSA v1.0 defines build levels: L1 provenance exists, L2 a hosted build service signs it, L3 builds are hardened against tampering between runs. in-toto (Torres-Arias et al., 2019) and Sigstore (Newman et al., 2022) provide ways to create and verify such statements.

Section eighteen point two develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section eighteen point two, Aiko Mori expects application claims to carry owners and dates.

### 18.3 Approved images

Hosting accepts only images whose digests appear in the approved list produced by the main-branch build.

Section eighteen point three develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section eighteen point three, Aiko Mori expects application claims to carry owners and dates.

Section eighteen point three treats recording digests provenance approved as testable only when evidence and ticket IDs are recorded.

For section eighteen point three, Brightwave Digital will not accept application work without a written trail.

### 18.4 Brightwave's target

The agency targets SLSA build L2 for all client projects this year.

Section eighteen point four develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section eighteen point four, Aiko Mori expects application claims to carry owners and dates.

Section eighteen point four treats recording digests provenance approved as testable only when evidence and ticket IDs are recorded.

For section eighteen point four, Brightwave Digital will not accept application work without a written trail.

### 18.5 Exceptions

Emergency changes still go through the build; there are no manual uploads to hosting.

Section eighteen point five develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section eighteen point five, Aiko Mori expects application claims to carry owners and dates.

Section eighteen point five treats recording digests provenance approved as testable only when evidence and ticket IDs are recorded.

For section eighteen point five, Brightwave Digital will not accept application work without a written trail.

### 18.6 Evidence

Digest records give clients evidence of what changed and when.

Section eighteen point six develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section eighteen point six, Aiko Mori expects application claims to carry owners and dates.

Section eighteen point six treats recording digests provenance approved as testable only when evidence and ticket IDs are recorded.

For section eighteen point six, Brightwave Digital will not accept application work without a written trail.

Section eighteen point six fails closed if application evidence is missing rather than guessing.

### Checking the records

Each month Diego picks three deployments at random and traces each from the running digest back through the registry to the build run and commit. If any link is missing, the gap is fixed in the pipeline. The first check finds one project whose deployment step recorded the image tag but not the digest; because tags can be moved to point at a different image, only the digest identifies the contents reliably. The step is corrected to record digests, and a test is added to the shared pipeline template.

### Worked example

After the approved-image rule is introduced, a developer's attempt to deploy a locally built test image to a client's production is refused. The developer rebuilds through the pipeline, and the event confirms the control works.

> **Synthetic case.** Builds and events are synthetic.

### Errors and limits

Provenance proves how something was built, not that the code is safe.

### Exercises

- **EX052 — Digest record.** What does the deployment record store? *Rubric:* 3 = digest, commit, build run; 2 = two; 1 = one; 0 = none.
- **EX053 — SLSA L2.** What does SLSA build L2 add over L1? *Rubric:* 3 = hosted build service signs provenance; 2 = partial; 1 = none; 0 = none.
- **EX054 — Refused deploy.** What did the refused deploy show? *Rubric:* 3 = control works; local images blocked; 2 = partial; 1 = none; 0 = none.

### Synthesis

Record what runs and deploy only what the pipeline built.

### Continue studying — chapter 18 of 30

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Application and software supply chain security: monitoring

### Learning outcomes

You will (1) compare running versions with approved releases; (2) detect drift and unapproved builds; (3) alert owners; (4) investigate differences.

### 19.1 Drift

Drift is when what runs differs from what was approved: a client left behind on an old release, or something running that the pipeline never approved.

Section nineteen point one develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section nineteen point one, Aiko Mori expects application claims to carry owners and dates.

Section nineteen point one treats drift lab result investigating as testable only when evidence and ticket IDs are recorded.

For section nineteen point one, Brightwave Digital will not accept application work without a written trail.

### Lab — Lab — release drift

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

harbour-cafe runs 2.0.9 while 2.1.4 is approved, so it is BEHIND. museum-tickets runs 4.0.3-hotfix, which is not in the approved list, so it is an UNAPPROVED BUILD. Other clients match.

Section nineteen point two develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section nineteen point two, Aiko Mori expects application claims to carry owners and dates.

Section nineteen point two treats drift lab result investigating as testable only when evidence and ticket IDs are recorded.

### 19.3 Investigating

BEHIND usually means a deployment failed or was skipped; UNAPPROVED BUILD needs urgent questions about where the build came from.

Section nineteen point three develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section nineteen point three, Aiko Mori expects application claims to carry owners and dates.

Section nineteen point three treats drift lab result investigating as testable only when evidence and ticket IDs are recorded.

For section nineteen point three, Brightwave Digital will not accept application work without a written trail.

### 19.4 Alerts

A daily check sends drift to the project owner and, for unapproved builds, to Aiko too.

Section nineteen point four develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section nineteen point four, Aiko Mori expects application claims to carry owners and dates.

Section nineteen point four treats drift lab result investigating as testable only when evidence and ticket IDs are recorded.

For section nineteen point four, Brightwave Digital will not accept application work without a written trail.

### 19.5 Closing the loop

Each finding is recorded with its cause and fix.

Section nineteen point five develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section nineteen point five, Aiko Mori expects application claims to carry owners and dates.

Section nineteen point five treats drift lab result investigating as testable only when evidence and ticket IDs are recorded.

For section nineteen point five, Brightwave Digital will not accept application work without a written trail.

Section nineteen point five fails closed if application evidence is missing rather than guessing.

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

- **EX055 — Lab drift.** What did the lab report? *Rubric:* 3 = harbour-cafe BEHIND; museum UNAPPROVED BUILD; 2 = one; 1 = none; 0 = none.
- **EX056 — Unapproved urgency.** Why is an unapproved build urgent? *Rubric:* 3 = unknown origin of what runs; 2 = partial; 1 = none; 0 = none.
- **EX057 — Hotfix cause.** What caused the museum hotfix? *Rubric:* 3 = manual weekend deploy before rule; 2 = partial; 1 = none; 0 = none.

### Synthesis

Watch for drift and fix its causes.

### Continue studying — chapter 19 of 30

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Application and software supply chain security: troubleshooting

### Learning outcomes

You will (1) diagnose failing dependency updates and pipeline checks; (2) avoid disabling checks; (3) fix root causes; (4) record lessons.

### 20.1 Common failures

Update pull requests fail tests because of breaking changes; pinned actions break when their own dependencies change; content checks reject unusual but valid files; audit matches turn out false.

Section twenty point one develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty point one, Aiko Mori expects application claims to carry owners and dates.

Section twenty point one treats common failures diagnosing not as testable only when evidence and ticket IDs are recorded.

### 20.2 Diagnosing

Diego reads the failure, reproduces it locally with synthetic data, and changes one thing at a time.

Section twenty point two develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty point two, Aiko Mori expects application claims to carry owners and dates.

Section twenty point two treats common failures diagnosing not as testable only when evidence and ticket IDs are recorded.

For section twenty point two, Brightwave Digital will not accept application work without a written trail.

### 20.3 Not disabling checks

A failing check is never switched off to make a deadline. If it must be bypassed, Aiko approves a time-limited exception with a ticket.

Section twenty point three develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty point three, Aiko Mori expects application claims to carry owners and dates.

Section twenty point three treats common failures diagnosing not as testable only when evidence and ticket IDs are recorded.

For section twenty point three, Brightwave Digital will not accept application work without a written trail.

### 20.4 Breaking changes

For a major library update, the developer reads the change notes and updates code in a separate pull request.

Section twenty point four develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty point four, Aiko Mori expects application claims to carry owners and dates.

Section twenty point four treats common failures diagnosing not as testable only when evidence and ticket IDs are recorded.

For section twenty point four, Brightwave Digital will not accept application work without a written trail.

### 20.5 Recording lessons

Each solved problem gets a short note in the team's troubleshooting page.

Section twenty point five develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty point five, Aiko Mori expects application claims to carry owners and dates.

Section twenty point five treats common failures diagnosing not as testable only when evidence and ticket IDs are recorded.

For section twenty point five, Brightwave Digital will not accept application work without a written trail.

### 20.6 Knowing when to ask

If a problem takes more than an hour, Diego asks for help.

Section twenty point six develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty point six, Aiko Mori expects application claims to carry owners and dates.

Section twenty point six treats common failures diagnosing not as testable only when evidence and ticket IDs are recorded.

For section twenty point six, Brightwave Digital will not accept application work without a written trail.

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

- **EX058 — No disabling.** What happens if a check must be bypassed? *Rubric:* 3 = time-limited approved exception; 2 = partial; 1 = none; 0 = none.
- **EX059 — Diagnosis steps.** How does Diego diagnose? *Rubric:* 3 = read, reproduce, one change at a time; 2 = two; 1 = one; 0 = none.
- **EX060 — Date library fix.** What fixed the date library failure? *Rubric:* 3 = explicit time zone; 2 = partial; 1 = none; 0 = none.

### Synthesis

Fix root causes and keep checks on.

### Continue studying — chapter 20 of 30

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Application and software supply chain security: service integration

### Learning outcomes

You will (1) secure connections to external services; (2) manage service secrets; (3) validate data from services; (4) plan for service failures.

### 21.1 External services

Client apps use an email service, a payment provider for museum-tickets and a mapping service for the kiteschool site. Each is a trust boundary: Brightwave depends on it and sends data to it.

Section twenty-one point one develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-one point one, Aiko Mori expects application claims to carry owners and dates.

Section twenty-one point one treats external services secrets for as testable only when evidence and ticket IDs are recorded.

### 21.2 Secrets for services

Service keys are kept in the hosting platform's secret store, scoped to one client and one environment, and rotated yearly or immediately if exposed. Keys never appear in code; a pre-commit scan catches mistakes.

Section twenty-one point two develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-one point two, Aiko Mori expects application claims to carry owners and dates.

Section twenty-one point two treats external services secrets for as testable only when evidence and ticket IDs are recorded.

### 21.3 Validating responses

Data returned by services is checked like user input. Payment confirmations are verified with the provider's signature before marking a ticket as paid.

Section twenty-one point three develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-one point three, Aiko Mori expects application claims to carry owners and dates.

Section twenty-one point three treats external services secrets for as testable only when evidence and ticket IDs are recorded.

For section twenty-one point three, Brightwave Digital will not accept application work without a written trail.

### 21.4 Least data

Only needed data is sent: the email service receives the owner's email and appointment time, not medical notes.

Section twenty-one point four develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-one point four, Aiko Mori expects application claims to carry owners and dates.

Section twenty-one point four treats external services secrets for as testable only when evidence and ticket IDs are recorded.

For section twenty-one point four, Brightwave Digital will not accept application work without a written trail.

### 21.5 Failure planning

If the email service fails, bookings still save and emails retry later; if payment confirmation is missing, the ticket stays pending.

Section twenty-one point five develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-one point five, Aiko Mori expects application claims to carry owners and dates.

Section twenty-one point five treats external services secrets for as testable only when evidence and ticket IDs are recorded.

For section twenty-one point five, Brightwave Digital will not accept application work without a written trail.

### 21.6 Reviewing services

Before adding a service, Brightwave reviews its security information and data location.

Section twenty-one point six develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-one point six, Aiko Mori expects application claims to carry owners and dates.

Section twenty-one point six treats external services secrets for as testable only when evidence and ticket IDs are recorded.

For section twenty-one point six, Brightwave Digital will not accept application work without a written trail.

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

- **EX061 — Key storage.** Where are service keys kept? *Rubric:* 3 = secret store, scoped per client and environment; 2 = partial; 1 = none; 0 = none.
- **EX062 — Least data.** What does the email service receive? *Rubric:* 3 = email and appointment time only; 2 = partial; 1 = none; 0 = none.
- **EX063 — Callback finding.** What was wrong with the payment callback? *Rubric:* 3 = no signature check; 2 = partial; 1 = none; 0 = none.

### Synthesis

Treat every service as a boundary to check.

### Continue studying — chapter 21 of 30

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Application and software supply chain security: automation

### Learning outcomes

You will (1) automate inventory, audit and drift checks; (2) schedule them; (3) route results to owners; (4) keep automation reviewed and safe.

### 22.1 What to automate

The nightly job builds the inventory from lock files, runs the audit against the advisory list, checks drift and writes one report.

Section twenty-two point one develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-two point one, Aiko Mori expects application claims to carry owners and dates.

Section twenty-two point one treats what to automate routing as testable only when evidence and ticket IDs are recorded.

For section twenty-two point one, Brightwave Digital will not accept application work without a written trail.

### 22.2 Routing

Each finding goes to the project owner in the team chat with a link to the task; highs also go to Aiko.

Section twenty-two point two develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-two point two, Aiko Mori expects application claims to carry owners and dates.

Section twenty-two point two treats what to automate routing as testable only when evidence and ticket IDs are recorded.

For section twenty-two point two, Brightwave Digital will not accept application work without a written trail.

### 22.3 Safe automation

The job has read-only access to repositories and hosting status. It opens tasks and update pull requests but cannot merge or deploy.

Section twenty-two point three develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-two point three, Aiko Mori expects application claims to carry owners and dates.

Section twenty-two point three treats what to automate routing as testable only when evidence and ticket IDs are recorded.

For section twenty-two point three, Brightwave Digital will not accept application work without a written trail.

### 22.4 Reviewing automation

The job's code is reviewed like any project, pinned and tested with synthetic data.

Section twenty-two point four develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-two point four, Aiko Mori expects application claims to carry owners and dates.

Section twenty-two point four treats what to automate routing as testable only when evidence and ticket IDs are recorded.

For section twenty-two point four, Brightwave Digital will not accept application work without a written trail.

### 22.5 Watching the watcher

If the nightly report does not arrive, an alert fires, because silent failure would look like "no problems".

Section twenty-two point five develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-two point five, Aiko Mori expects application claims to carry owners and dates.

Section twenty-two point five treats what to automate routing as testable only when evidence and ticket IDs are recorded.

For section twenty-two point five, Brightwave Digital will not accept application work without a written trail.

### 22.6 Effort saved

The manual weekly checks that took Diego half a day now take ten minutes of reading.

Section twenty-two point six develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-two point six, Aiko Mori expects application claims to carry owners and dates.

Section twenty-two point six treats what to automate routing as testable only when evidence and ticket IDs are recorded.

For section twenty-two point six, Brightwave Digital will not accept application work without a written trail.

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

- **EX064 — Job permissions.** What can the nightly job do? *Rubric:* 3 = read; open tasks and PRs; not merge or deploy; 2 = partial; 1 = none; 0 = none.
- **EX065 — Silent failure.** Why alert when the report is missing? *Rubric:* 3 = absence looks like no problems; 2 = partial; 1 = none; 0 = none.
- **EX066 — Skipped projects.** How were skipped projects found? *Rubric:* 3 = missing-project count; 2 = partial; 1 = none; 0 = none.

### Synthesis

Automate checks with least privilege and watch for silent failures.

### Continue studying — chapter 22 of 30

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Application and software supply chain security: evaluation

### Learning outcomes

You will (1) measure check quality with precision and recall; (2) label a sample; (3) compare checks; (4) improve noisy checks.

### 23.1 Precision and recall

Precision is the share of a check's alerts that are real; recall is the share of real problems the check finds. A noisy check wastes time; a check with low recall gives false comfort.

Section twenty-three point one develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-three point one, Aiko Mori expects application claims to carry owners and dates.

Section twenty-three point one treats precision and recall labelling as testable only when evidence and ticket IDs are recorded.

### 23.2 Labelling

Diego and another developer independently label a sample of findings as real or not, then discuss disagreements.

Section twenty-three point two develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-three point two, Aiko Mori expects application claims to carry owners and dates.

Section twenty-three point two treats precision and recall labelling as testable only when evidence and ticket IDs are recorded.

For section twenty-three point two, Brightwave Digital will not accept application work without a written trail.

### Lab — Lab — check quality

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

The outdated-component check has precision 0.62 and recall 0.94: it finds nearly everything but over a third of alerts are not real. The hardcoded-credential check has precision 0.25 and recall 1.00: it finds every real credential but three quarters of its alerts are test strings or examples.

Section twenty-three point three develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-three point three, Aiko Mori expects application claims to carry owners and dates.

Section twenty-three point three treats precision and recall labelling as testable only when evidence and ticket IDs are recorded.

### 23.4 Improving

The credential check gets an allow list for clearly synthetic test values, reviewed by Aiko; the outdated check ignores libraries used only in development.

Section twenty-three point four develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-three point four, Aiko Mori expects application claims to carry owners and dates.

Section twenty-three point four treats precision and recall labelling as testable only when evidence and ticket IDs are recorded.

For section twenty-three point four, Brightwave Digital will not accept application work without a written trail.

### 23.5 Re-measuring

After changes, the same labelled sample is rerun to confirm recall did not fall.

Section twenty-three point five develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-three point five, Aiko Mori expects application claims to carry owners and dates.

Section twenty-three point five treats precision and recall labelling as testable only when evidence and ticket IDs are recorded.

For section twenty-three point five, Brightwave Digital will not accept application work without a written trail.

### Labelling carefully

Two labellers working independently make it possible to see how often they agree. Where they disagree, the reason is written down, because disagreements often show that the definition of a real problem is unclear. For the credential check, the team agrees that a real credential is any value that would work against a live system, while expired or example values are not. Writing this definition down raised agreement in the next sample. The labelled samples are kept, so future changes to a check can be measured on the same items.

### Worked example

After tuning, the credential check's precision rises to 0.70 on a fresh sample with recall still 1.00, and developers stop ignoring its alerts.

> **Synthetic case.** Samples and figures are synthetic.

### Errors and limits

A small labelled sample gives rough estimates; report the sample size.

### Exercises

- **EX067 — Definitions.** Define precision and recall. *Rubric:* 3 = share of alerts real; share of problems found; 2 = one; 1 = none; 0 = none.
- **EX068 — Lab figures.** What were the lab figures? *Rubric:* 3 = outdated 0.62/0.94; credential 0.25/1.00; 2 = one; 1 = none; 0 = none.
- **EX069 — Re-measure.** Why re-run the sample after tuning? *Rubric:* 3 = check recall did not fall; 2 = partial; 1 = none; 0 = none.

### Synthesis

Measure checks and tune them without losing recall.

### Continue studying — chapter 23 of 30

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Applied research methods

### Learning outcomes

You will (1) ask a focused question; (2) collect evidence from Brightwave records; (3) analyse simply; (4) report honestly.

### 24.1 The question

Diego asks: "Do projects receiving weekly update pull requests fix high advisories faster than projects updated manually?"

Section twenty-four point one develops applied research methods with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-four point one, Aiko Mori expects applied claims to carry owners and dates.

Section twenty-four point one treats the question evidence analysis as testable only when evidence and ticket IDs are recorded.

For section twenty-four point one, Brightwave Digital will not accept applied work without a written trail.

### 24.2 Evidence

Task records give advisory dates and fix dates for each project and update method over one year.

Section twenty-four point two develops applied research methods with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-four point two, Aiko Mori expects applied claims to carry owners and dates.

Section twenty-four point two treats the question evidence analysis as testable only when evidence and ticket IDs are recorded.

For section twenty-four point two, Brightwave Digital will not accept applied work without a written trail.

### 24.3 Analysis

He compares median fix times: weekly-update projects 3 days, manual projects 12 days.

Section twenty-four point three develops applied research methods with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-four point three, Aiko Mori expects applied claims to carry owners and dates.

Section twenty-four point three treats the question evidence analysis as testable only when evidence and ticket IDs are recorded.

For section twenty-four point three, Brightwave Digital will not accept applied work without a written trail.

Section twenty-four point three fails closed if applied evidence is missing rather than guessing.

### 24.4 Limits

Projects were not randomly assigned; manual projects are older and less active, which could explain part of the difference. Wermke et al. (2022) interviewed open-source projects about supply chain practices and show how context shapes adoption.

Section twenty-four point four develops applied research methods with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-four point four, Aiko Mori expects applied claims to carry owners and dates.

Section twenty-four point four treats the question evidence analysis as testable only when evidence and ticket IDs are recorded.

### 24.5 Reporting

The report states the question, data, result, limits and a recommendation.

Section twenty-four point five develops applied research methods with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-four point five, Aiko Mori expects applied claims to carry owners and dates.

Section twenty-four point five treats the question evidence analysis as testable only when evidence and ticket IDs are recorded.

For section twenty-four point five, Brightwave Digital will not accept applied work without a written trail.

Section twenty-four point five fails closed if applied evidence is missing rather than guessing.

### 24.6 Ethics

Records about developers' work are summarised by project, not used to judge individuals.

Section twenty-four point six develops applied research methods with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-four point six, Aiko Mori expects applied claims to carry owners and dates.

Section twenty-four point six treats the question evidence analysis as testable only when evidence and ticket IDs are recorded.

For section twenty-four point six, Brightwave Digital will not accept applied work without a written trail.

Section twenty-four point six fails closed if applied evidence is missing rather than guessing.

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

- **EX070 — Question.** What was the question? *Rubric:* 3 = weekly PRs vs manual fix speed; 2 = partial; 1 = none; 0 = none.
- **EX071 — Result.** What were the medians? *Rubric:* 3 = 3 vs 12 days; 2 = partial; 1 = none; 0 = none.
- **EX072 — Limit.** Name a limit. *Rubric:* 3 = not random; older projects manual; 2 = partial; 1 = none; 0 = none.

### Synthesis

Ask focused questions and report limits honestly.

### Continue studying — chapter 24 of 30

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Team project studio

### Learning outcomes

You will (1) plan a team project; (2) divide work; (3) review each other's changes; (4) deliver in increments.

### 25.1 The project

Diego's team of three builds a shared "client security status" page showing inventory, open advisories and drift for each client.

Section twenty-five point one develops team project studio with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-five point one, Aiko Mori expects team claims to carry owners and dates.

Section twenty-five point one treats the project planning dividing as testable only when evidence and ticket IDs are recorded.

For section twenty-five point one, Brightwave Digital will not accept team work without a written trail.

### 25.2 Planning

They write a short plan: users, data, risks and a first version in two weeks.

Section twenty-five point two develops team project studio with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-five point two, Aiko Mori expects team claims to carry owners and dates.

Section twenty-five point two treats the project planning dividing as testable only when evidence and ticket IDs are recorded.

For section twenty-five point two, Brightwave Digital will not accept team work without a written trail.

### 25.3 Dividing work

One builds the data import, one the page, Diego the access checks and tests.

Section twenty-five point three develops team project studio with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-five point three, Aiko Mori expects team claims to carry owners and dates.

Section twenty-five point three treats the project planning dividing as testable only when evidence and ticket IDs are recorded.

For section twenty-five point three, Brightwave Digital will not accept team work without a written trail.

### 25.4 Reviewing

Every change gets a review; reviewers check authorisation and data shown.

Section twenty-five point four develops team project studio with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-five point four, Aiko Mori expects team claims to carry owners and dates.

Section twenty-five point four treats the project planning dividing as testable only when evidence and ticket IDs are recorded.

For section twenty-five point four, Brightwave Digital will not accept team work without a written trail.

Section twenty-five point four fails closed if team evidence is missing rather than guessing.

### 25.5 Increments

The first version shows inventory only; advisories and drift come in later increments.

Section twenty-five point five develops team project studio with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-five point five, Aiko Mori expects team claims to carry owners and dates.

Section twenty-five point five treats the project planning dividing as testable only when evidence and ticket IDs are recorded.

For section twenty-five point five, Brightwave Digital will not accept team work without a written trail.

Section twenty-five point five fails closed if team evidence is missing rather than guessing.

### 25.6 Retrospective

After each increment, the team notes what went well and what to change.

Section twenty-five point six develops team project studio with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-five point six, Aiko Mori expects team claims to carry owners and dates.

Section twenty-five point six treats the project planning dividing as testable only when evidence and ticket IDs are recorded.

For section twenty-five point six, Brightwave Digital will not accept team work without a written trail.

Section twenty-five point six fails closed if team evidence is missing rather than guessing.

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

- **EX073 — Project.** What did the team build? *Rubric:* 3 = client security status page; 2 = partial; 1 = none; 0 = none.
- **EX074 — Diego's part.** What did Diego build? *Rubric:* 3 = access checks and tests; 2 = partial; 1 = none; 0 = none.
- **EX075 — Review catch.** What did review catch? *Rubric:* 3 = all clients visible to anyone; 2 = partial; 1 = none; 0 = none.

### Synthesis

Plan, divide, review and deliver in steps.

### Continue studying — chapter 25 of 30

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Application and software supply chain security: operational handoff

### Learning outcomes

You will (1) hand over security processes to the team that will run them; (2) write runbooks; (3) define responsibilities; (4) check the handoff works.

### 26.1 What is handed over

As the placement nears its end, Diego hands over the nightly job, the inventory, the upload checks module, the pipeline template and the drift check. Each needs an owner who will keep it running after he leaves; otherwise the controls will slowly decay as libraries and platforms change around them.

Section twenty-six point one develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-six point one, Aiko Mori expects application claims to carry owners and dates.

### 26.2 Runbooks

Each process gets a runbook: what it does, how to tell it is healthy, what common failures look like and how to fix them, and who to contact. Runbooks are written for a developer who has never seen the process, and tested by having one follow them.

Section twenty-six point two develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-six point two, Aiko Mori expects application claims to carry owners and dates.

### 26.3 Responsibilities

A simple table names who owns each process, who is the backup, and who approves changes. Advisory response is shared: the nightly job finds matches, project owners fix them, and Aiko watches the due dates each week.

Section twenty-six point three develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-six point three, Aiko Mori expects application claims to carry owners and dates.

Section twenty-six point three treats what is handed over as testable only when evidence and ticket IDs are recorded.

### 26.4 Checking the handoff

For two weeks the new owners run everything while Diego only watches. Any question they have to ask him becomes a runbook update.

Section twenty-six point four develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-six point four, Aiko Mori expects application claims to carry owners and dates.

Section twenty-six point four treats what is handed over as testable only when evidence and ticket IDs are recorded.

For section twenty-six point four, Brightwave Digital will not accept application work without a written trail.

### 26.5 Client communication

Clients are told who their security contact is and how advisories affecting them will be reported.

Section twenty-six point five develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-six point five, Aiko Mori expects application claims to carry owners and dates.

Section twenty-six point five treats what is handed over as testable only when evidence and ticket IDs are recorded.

For section twenty-six point five, Brightwave Digital will not accept application work without a written trail.

### 26.6 Keeping knowledge

Decisions and reasons are kept in the repositories next to the code, not in personal notes.

Section twenty-six point six develops application and software supply chain with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-six point six, Aiko Mori expects application claims to carry owners and dates.

Section twenty-six point six treats what is handed over as testable only when evidence and ticket IDs are recorded.

For section twenty-six point six, Brightwave Digital will not accept application work without a written trail.

### Worked example

During the watched fortnight, the new owner of the nightly job cannot find how to add a new client project to the inventory. Diego adds a step to the runbook; the next new project is added without help. By the end, the owners have asked eleven questions, all now answered in the runbooks.

> **Synthetic case.** Processes and events are synthetic.

### Errors and limits

A handoff is finished when others can run the process without you, not when the documents exist.

### Exercises

- **EX076 — Runbook contents.** What does a runbook include? *Rubric:* 3 = purpose, health, failures, fixes, contacts; 2 = three; 1 = one; 0 = none.
- **EX077 — Advisory roles.** Who does what in advisory response? *Rubric:* 3 = job finds; owners fix; Aiko watches dates; 2 = two; 1 = one; 0 = none.
- **EX078 — Handoff check.** How was the handoff checked? *Rubric:* 3 = two weeks owners run, Diego watches; 2 = partial; 1 = none; 0 = none.

### Synthesis

Hand over with runbooks, owners and a watched trial.

### Continue studying — chapter 26 of 30

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Deployment and validation

### Learning outcomes

You will (1) deploy the security controls to all client projects; (2) validate each works; (3) record results; (4) handle projects that cannot yet comply.

### 27.1 Rollout plan

Controls are rolled out project by project, starting with the most sensitive clients identified in chapter 11. Each project gets the shared upload module, the pipeline template, lock-file enforcement and digest recording.

Section twenty-seven point one develops deployment and validation with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-seven point one, Aiko Mori expects deployment claims to carry owners and dates.

Section twenty-seven point one treats rollout plan validation tests as testable only when evidence and ticket IDs are recorded.

### 27.2 Validation tests

For each project, Diego runs a validation checklist with synthetic data: a disallowed upload is rejected with its reason; the pipeline uses pinned actions and a read-only token; a lock-file mismatch fails the build; the deployment record holds a digest; the drift check reports the project as matching.

Section twenty-seven point two develops deployment and validation with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-seven point two, Aiko Mori expects deployment claims to carry owners and dates.

Section twenty-seven point two treats rollout plan validation tests as testable only when evidence and ticket IDs are recorded.

### 27.3 Recording results

Results are recorded per project with date and tester, forming evidence for clients and for Brightwave's own review.

Section twenty-seven point three develops deployment and validation with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-seven point three, Aiko Mori expects deployment claims to carry owners and dates.

Section twenty-seven point three treats rollout plan validation tests as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point three, Brightwave Digital will not accept deployment work without a written trail.

### 27.4 Projects that cannot comply

Two legacy projects cannot use the new upload module without a rewrite. They get compensating steps (tighter size limits and storage rules) and a rebuild date.

Section twenty-seven point four develops deployment and validation with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-seven point four, Aiko Mori expects deployment claims to carry owners and dates.

Section twenty-seven point four treats rollout plan validation tests as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point four, Brightwave Digital will not accept deployment work without a written trail.

### 27.5 Rollback

Each rollout can be reversed by redeploying the previous approved digest if a client site breaks.

Section twenty-seven point five develops deployment and validation with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-seven point five, Aiko Mori expects deployment claims to carry owners and dates.

Section twenty-seven point five treats rollout plan validation tests as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point five, Brightwave Digital will not accept deployment work without a written trail.

### 27.6 Communicating

Clients receive a short note on what changed and any visible effects, such as new upload messages.

Section twenty-seven point six develops deployment and validation with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-seven point six, Aiko Mori expects deployment claims to carry owners and dates.

Section twenty-seven point six treats rollout plan validation tests as testable only when evidence and ticket IDs are recorded.

For section twenty-seven point six, Brightwave Digital will not accept deployment work without a written trail.

### Validation as a habit

The validation checklist becomes part of the release process for new projects, so each new client starts with every control in place and recorded. The checklist takes about twenty minutes per project with the synthetic test files ready.

### Worked example

Rollout across 23 projects takes five weeks. Twenty-one pass every validation item on the first attempt or after small fixes; one needs a rollback when an upload change rejects a file format the client really uses, which is added to its allowed list after review and redeployed the next day.

> **Synthetic case.** Projects and results are synthetic.

### Errors and limits

Validation proves the control is present; monitoring proves it stays present.

### Exercises

- **EX079 — Rollout order.** Which projects went first? *Rubric:* 3 = most sensitive clients; 2 = partial; 1 = none; 0 = none.
- **EX080 — Legacy projects.** How were the two legacy projects handled? *Rubric:* 3 = compensating steps and rebuild date; 2 = partial; 1 = none; 0 = none.
- **EX081 — Rollback case.** Why was one project rolled back? *Rubric:* 3 = rejected a format the client used; 2 = partial; 1 = none; 0 = none.

### Synthesis

Roll out in order, validate each project and plan for exceptions.

### Continue studying — chapter 27 of 30

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Field practice

### Learning outcomes

You will (1) apply the course in a real-style advisory response; (2) coordinate across clients; (3) communicate clearly; (4) reflect on what worked.

### 28.1 The event

In the final month, a synthetic high-severity advisory is published for a widely used form library. This time, the nightly job matches it to nine client projects within hours of publication.

Section twenty-eight point one develops field practice with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-eight point one, Aiko Mori expects field claims to carry owners and dates.

Section twenty-eight point one treats the event coordination communication as testable only when evidence and ticket IDs are recorded.

### 28.2 Coordination

Owners receive tasks automatically. Diego coordinates: sensitive clients first, updates through the weekly bot pipeline, validation tests rerun before deployment.

Section twenty-eight point two develops field practice with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-eight point two, Aiko Mori expects field claims to carry owners and dates.

Section twenty-eight point two treats the event coordination communication as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point two, Brightwave Digital will not accept field work without a written trail.

### 28.3 Communication

Affected clients get a short message: what the issue is in plain terms, whether their site was affected, what was done and when. Unaffected clients who ask get a clear "not affected" answer from the inventory record.

Section twenty-eight point three develops field practice with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-eight point three, Aiko Mori expects field claims to carry owners and dates.

Section twenty-eight point three treats the event coordination communication as testable only when evidence and ticket IDs are recorded.

### 28.4 Timeline

All nine projects are fixed within four days, well inside the 7-day target. Compared with January's three days just to find affected clients, the difference is clear.

Section twenty-eight point four develops field practice with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-eight point four, Aiko Mori expects field claims to carry owners and dates.

Section twenty-eight point four treats the event coordination communication as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point four, Brightwave Digital will not accept field work without a written trail.

### 28.5 Reflection

The team notes that the slowest fix was in a legacy project, again pointing to the rebuild.

Section twenty-eight point five develops field practice with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-eight point five, Aiko Mori expects field claims to carry owners and dates.

Section twenty-eight point five treats the event coordination communication as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point five, Brightwave Digital will not accept field work without a written trail.

### 28.6 Lessons

Two runbook steps are improved and the client message template is shortened after feedback.

Section twenty-eight point six develops field practice with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-eight point six, Aiko Mori expects field claims to carry owners and dates.

Section twenty-eight point six treats the event coordination communication as testable only when evidence and ticket IDs are recorded.

For section twenty-eight point six, Brightwave Digital will not accept field work without a written trail.

Section twenty-eight point six fails closed if field evidence is missing rather than guessing.

### Compared with January

In January, three days went on manual searching before any fix began, and the full extent was unclear. In the field event, matching took hours, owners were known, fixes followed the update pipeline and validation, and every client received an accurate answer. The difference came from routine work done earlier: the inventory, the nightly job, the pipeline template and the runbooks. None of it was dramatic, but together it changed how the agency responded, and the directors agreed to keep funding the time owners spend on these processes.

### Worked example

Aiko presents the event to Brightwave's directors as evidence that the placement's three goals have been met: the inventory answered in minutes, highs were fixed within 7 days, and every deployment was a recorded pipeline build.

> **Synthetic case.** The event and results are synthetic.

### Errors and limits

One good event does not prove the process always works; keep measuring.

### Exercises

- **EX082 — Detection.** How quickly were affected projects found? *Rubric:* 3 = within hours via nightly job; 2 = partial; 1 = none; 0 = none.
- **EX083 — Fix time.** How long did fixing take? *Rubric:* 3 = four days for all nine; 2 = partial; 1 = none; 0 = none.
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

Diego's capstone is a software bill of materials (SBOM) for each client release, listing every component and version. NTIA (2021) describes the minimum elements: supplier, component name, version, unique identifier, dependency relationship, author of the data and timestamp.

Section twenty-nine point one develops capstone build with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-nine point one, Aiko Mori expects capstone claims to carry owners and dates.

Section twenty-nine point one treats choosing the capstone design as testable only when evidence and ticket IDs are recorded.

### 29.2 Design

The build creates the SBOM from the lock file, attaches it to the release record next to the image digest, and stores it with the deployment record. Clients can request their SBOM.

Section twenty-nine point two develops capstone build with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-nine point two, Aiko Mori expects capstone claims to carry owners and dates.

Section twenty-nine point two treats choosing the capstone design as testable only when evidence and ticket IDs are recorded.

### 29.3 Using SBOMs

With SBOMs per release, the inventory can answer not only "who uses this library now" but "which past release contained it", which helps when clients ask about past exposure.

Section twenty-nine point three develops capstone build with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-nine point three, Aiko Mori expects capstone claims to carry owners and dates.

Section twenty-nine point three treats choosing the capstone design as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point three, Brightwave Digital will not accept capstone work without a written trail.

### 29.4 Testing

Tests check that every library in the lock file appears in the SBOM and that the SBOM matches the deployed digest.

Section twenty-nine point four develops capstone build with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-nine point four, Aiko Mori expects capstone claims to carry owners and dates.

Section twenty-nine point four treats choosing the capstone design as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point four, Brightwave Digital will not accept capstone work without a written trail.

### 29.5 Documentation

A runbook explains how SBOMs are created, where they are stored and how to answer a client request.

Section twenty-nine point five develops capstone build with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-nine point five, Aiko Mori expects capstone claims to carry owners and dates.

Section twenty-nine point five treats choosing the capstone design as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point five, Brightwave Digital will not accept capstone work without a written trail.

### 29.6 Scope limits

The capstone does not attempt signing SBOMs; that is noted as future work linked to the SLSA L3 goal.

Section twenty-nine point six develops capstone build with a Brightwave Digital note Diego Ramos can demo offline.

Under section twenty-nine point six, Aiko Mori expects capstone claims to carry owners and dates.

Section twenty-nine point six treats choosing the capstone design as testable only when evidence and ticket IDs are recorded.

For section twenty-nine point six, Brightwave Digital will not accept capstone work without a written trail.

### SBOM format

Diego chooses a widely supported standard SBOM format so clients' own tools can read it, and keeps one SBOM per release rather than per build attempt. Each SBOM records the generating tool and version, so later differences can be explained. He compares a generated SBOM with the lock file by hand for one small project before trusting the automated tests, which confirms the test logic and catches a formatting issue in version strings.

### Worked example

Diego tests the SBOM build on three client projects. One reveals a library bundled directly into code instead of through the lock file, invisible to the inventory until now. It is moved into the lock file so it is tracked like everything else.

> **Synthetic case.** The capstone is synthetic.

### Errors and limits

An SBOM lists components; it does not say whether they are safe.

### Exercises

- **EX085 — NTIA elements.** Name four NTIA minimum elements. *Rubric:* 3 = supplier, name, version, identifier, relationship, author, timestamp; 2 = two; 1 = one; 0 = none.
- **EX086 — New question.** What new question can SBOMs answer? *Rubric:* 3 = which past release had a library; 2 = partial; 1 = none; 0 = none.
- **EX087 — Hidden library.** What did testing reveal? *Rubric:* 3 = library bundled outside lock file; 2 = partial; 1 = none; 0 = none.

### Synthesis

SBOMs extend the inventory to every release.

### Continue studying — chapter 29 of 30

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Capstone assessment

### Learning outcomes

You will (1) present the capstone; (2) show evidence; (3) answer questions; (4) reflect on learning and next steps.

### 30.1 Presentation

Diego presents to Aiko and a Southport Polytechnic tutor: the January problem, the controls built, the evidence that they work, and the SBOM capstone.

Section thirty point one develops capstone assessment with a Brightwave Digital note Diego Ramos can demo offline.

Under section thirty point one, Aiko Mori expects capstone claims to carry owners and dates.

Section thirty point one treats presentation evidence questions limits as testable only when evidence and ticket IDs are recorded.

For section thirty point one, Brightwave Digital will not accept capstone work without a written trail.

### 30.2 Evidence

He shows the nightly reports, the validation records for 23 projects, the field-practice timeline and the SBOM tests, all from synthetic records.

Section thirty point two develops capstone assessment with a Brightwave Digital note Diego Ramos can demo offline.

Under section thirty point two, Aiko Mori expects capstone claims to carry owners and dates.

Section thirty point two treats presentation evidence questions limits as testable only when evidence and ticket IDs are recorded.

For section thirty point two, Brightwave Digital will not accept capstone work without a written trail.

### 30.3 Questions

The tutor asks how the work fits the SSDF. Diego maps it: inventory and audits to Respond to Vulnerabilities; pipeline template and pinning to Protect the Software; upload checks and reviews to Produce Well-Secured Software; runbooks and roles to Prepare the Organization.

Section thirty point three develops capstone assessment with a Brightwave Digital note Diego Ramos can demo offline.

Under section thirty point three, Aiko Mori expects capstone claims to carry owners and dates.

Section thirty point three treats presentation evidence questions limits as testable only when evidence and ticket IDs are recorded.

### 30.4 Limits

He names the limits honestly: two legacy projects remain, SBOMs are unsigned and unknown flaws are not found by audits.

Section thirty point four develops capstone assessment with a Brightwave Digital note Diego Ramos can demo offline.

Under section thirty point four, Aiko Mori expects capstone claims to carry owners and dates.

Section thirty point four treats presentation evidence questions limits as testable only when evidence and ticket IDs are recorded.

For section thirty point four, Brightwave Digital will not accept capstone work without a written trail.

### 30.5 Reflection

Diego writes that the biggest lesson was that most security work is careful routine: keeping lists current, watching checks and fixing small problems before they grow.

Section thirty point five develops capstone assessment with a Brightwave Digital note Diego Ramos can demo offline.

Under section thirty point five, Aiko Mori expects capstone claims to carry owners and dates.

Section thirty point five treats presentation evidence questions limits as testable only when evidence and ticket IDs are recorded.

For section thirty point five, Brightwave Digital will not accept capstone work without a written trail.

### 30.6 Next steps

Brightwave will rebuild the legacy projects, aim for SLSA build L3 and add signed SBOMs.

Section thirty point six develops capstone assessment with a Brightwave Digital note Diego Ramos can demo offline.

Under section thirty point six, Aiko Mori expects capstone claims to carry owners and dates.

Section thirty point six treats presentation evidence questions limits as testable only when evidence and ticket IDs are recorded.

For section thirty point six, Brightwave Digital will not accept capstone work without a written trail.

### Feedback received

The tutor's feedback praises the evidence and the honest limits, and suggests that the next step should include measuring how often clients use their SBOMs, since an unused document adds work without value. Aiko adds that the handoff quality was the strongest part, because the processes kept running without Diego during the watched fortnight. Diego records both points in his learning log and adds an SBOM-request count to the monthly report. Looking back over the year, he notes how each chapter's small step depended on earlier ones: the inventory made audits possible, audits made fix targets measurable, and records made the capstone possible.

### Worked example

The capstone is assessed as complete with distinction, and Brightwave offers Diego a junior developer role starting after graduation, with security processes as part of his responsibilities.

> **Synthetic case.** People, results and outcomes are synthetic.

### Errors and limits

Assessment rewards honest limits as well as results.

### Exercises

- **EX088 — SSDF map.** Map the work to the SSDF groups. *Rubric:* 3 = four groups mapped; 2 = three; 1 = one; 0 = none.
- **EX089 — Limits.** Name two limits. *Rubric:* 3 = legacy projects; unsigned SBOMs; unknown flaws; 2 = one; 1 = none; 0 = none.
- **EX090 — Lesson.** What was Diego's main lesson? *Rubric:* 3 = security is careful routine; 2 = partial; 1 = none; 0 = none.

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
