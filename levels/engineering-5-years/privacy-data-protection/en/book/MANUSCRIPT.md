# Privacy and Data Protection: Engineering Course

- Language: English (`en`); course 119, Engineering course (5 years).
- Editorial state: **published**. Chapters 1–50 of 50 have hand-written teaching text; exercises EX001–EX150 have matching worked results with 0–3 rubrics; nine offline labs use only the Python 3 standard library on synthetic data, and their outputs are embedded from real runs. Independent review and the 300-page A4 verification remain open.
- Audience: engineering students designing, verifying and operating privacy and data protection as properties of a real system.
- Author: [hiagokinlevi](https://github.com/hiagokinlevi). Original text [CC0 1.0](../../../../../LICENSE); cited works keep their rights.
- Boundary: the labs run randomised response, retention queries, data-flow checks, DPIA scoring, minimisation counts, erasure reliability, privacy budgets, a breach clock and evidence digests, all on synthetic data. Legal analysis is teaching, not legal advice. All people, organisations, systems and data are **synthetic** unless a sentence cites a public source.

[Course home](../../README.md) · [Chapter index](../SUBJECTS.md) · [Book plan](PLAN.md) · [Course skill](../../skill/SKILL.md) · [Worked results](#worked-results)

## How to use this draft

Read in order. The chapters follow one engineering student through a five-year course centred on a telemedicine provider: foundations read through privacy, systems and security, requirements and models, threats and DPIA, controls and implementation, measurement and verification, reliability, resilience and scale, operations and validation, the capstone research data service, the breach trial, the evidence dossier, the thesis and the defense. Run each lab where it appears, attempt the exercises before the worked results, and score yourself with the rubrics.

### Synthetic running case

| Element | Role | Boundary |
|---|---|---|
| **Zara Mbeki** | Engineering student | Invented |
| **Prof. Anders Holm** | Supervisor | Invented |
| **Corwen Polytechnic** | Fictional university | Invented |
| **Pellmore Telehealth** | Fictional telemedicine provider, 300 staff, patients in the EU and Brazil | Invented |

### Core sources

Regulation (EU) 2016/679 (GDPR); Lei 13.709/2018 (LGPD); EDPB Guidelines 4/2019, 05/2020, 07/2020, 01/2022 and 9/2022; WP248 rev.01 on DPIAs; NIST [Privacy Framework 1.0](https://doi.org/10.6028/NIST.CSWP.10), NISTIR 8053 and SP 800-188; ISO/IEC 29100:2011 and ISO/IEC 27701:2025; Sweeney (2002); Dwork et al. (2006) and Dwork and Roth (2014); Solove (2006); Nissenbaum (2004); Acquisti et al. (2015). Full list in [References](#references).

## Contents

| Chapters |
|---|
| [1](#ch-01) · [2](#ch-02) · [3](#ch-03) · [4](#ch-04) · [5](#ch-05) · [6](#ch-06) · [7](#ch-07) · [8](#ch-08) · [9](#ch-09) · [10](#ch-10) · [11](#ch-11) · [12](#ch-12) · [13](#ch-13) · [14](#ch-14) · [15](#ch-15) · [16](#ch-16) · [17](#ch-17) · [18](#ch-18) · [19](#ch-19) · [20](#ch-20) · [21](#ch-21) · [22](#ch-22) · [23](#ch-23) · [24](#ch-24) · [25](#ch-25) · [26](#ch-26) · [27](#ch-27) · [28](#ch-28) · [29](#ch-29) · [30](#ch-30) · [31](#ch-31) · [32](#ch-32) · [33](#ch-33) · [34](#ch-34) · [35](#ch-35) · [36](#ch-36) · [37](#ch-37) · [38](#ch-38) · [39](#ch-39) · [40](#ch-40) · [41](#ch-41) · [42](#ch-42) · [43](#ch-43) · [44](#ch-44) · [45](#ch-45) · [46](#ch-46) · [47](#ch-47) · [48](#ch-48) · [49](#ch-49) · [50](#ch-50) |

[Worked results](#worked-results) · [References](#references)

<a id="ch-01"></a>

## Chapter 1 — Calculus I

### Learning outcomes

You will (1) read rates of change in data growth; (2) use limits to reason about anonymity as groups shrink; (3) connect calculus to privacy engineering.

### 1.1 Why an engineer meets privacy early

Zara Mbeki begins a five-year engineering course at the fictional Corwen Polytechnic, supervised by Prof. Anders Holm. Her placement partner is the fictional Pellmore Telehealth, a telemedicine provider with 300 staff and patients in the European Union and Brazil. Pellmore's app books appointments, runs video consultations and stores records. Prof. Holm explains that privacy and data protection will be her main engineering domain, and that every foundation course will be read through it, starting with calculus, because privacy problems often involve quantities that grow or shrink over time.

### 1.2 Rates of change

Pellmore's stored video grows by roughly forty gigabytes a day. The derivative of storage with respect to time is that daily rate, and integrating it over a year gives the total. Zara sees a privacy consequence immediately: if recordings are never deleted, the amount of sensitive health data at risk grows linearly forever. A retention rule turns the growth curve into a plateau, because data enter and leave at the same rate. She sketches both curves and labels the gap between them as avoidable exposure that a breach could reveal.

### 1.3 Limits and small groups

A limit describes what happens as a quantity approaches a value. Zara applies the idea to published statistics. If Pellmore reports the average waiting time for a clinic, the average describes many patients; as the group size approaches one, the average becomes one person's exact waiting time. Privacy protection that works for large groups therefore fails in the limit of very small groups. This intuition, she learns, is behind rules that suppress small cells in published tables and behind the formal guarantees she will meet later in differential privacy.

### 1.4 Optimisation as trade-off

Calculus also finds maxima and minima. Prof. Holm sets an exercise: the usefulness of a dataset rises with detail while privacy risk also rises. If both are modelled as smooth curves, the best level of detail is where the marginal gain in usefulness equals the marginal increase in risk. Zara realises the model is simplistic, because risk to people is not freely exchangeable for usefulness and law sets hard limits, but the habit of asking about marginal effects will help her argue for proportionate designs throughout the course.

### Worked example

Zara models storage growth with and without retention, reasons about averages as group size shrinks, and frames detail versus risk as a marginal trade-off bounded by law.

> **Synthetic case.** Corwen, Pellmore and the figures are synthetic.

### Errors and limits

Smooth curves simplify discrete risks; legal limits are constraints, not terms in a trade-off.

### Exercises

- **EX001 — Retention plateau.** Why does a retention rule turn storage growth into a plateau? *Rubric:* 3 = data enter and leave at equal rates, so the total stops rising;; 2 = mentions deletion;; 1 = says storage stops;; 0 = none.
- **EX002 — Small-group limit.** What happens to an average as its group size approaches one? *Rubric:* 3 = it becomes one person's exact value, revealing it;; 2 = says it gets less accurate;; 1 = wrong;; 0 = none.
- **EX003 — Marginal trade-off limits.** Why is the marginal trade-off model simplistic for privacy? *Rubric:* 3 = harm to people is not freely exchangeable and law sets hard limits;; 2 = mentions law;; 1 = accepts the model;; 0 = none.

### Synthesis

Chapter 1 reads calculus through privacy. Chapter 2 uses discrete mathematics to count identities.

### Continue studying — chapter 01 of 50

[← Course home](../../README.md) · [Course chapter index](../SUBJECTS.md) · [Chapter 02 (draft) →](#ch-02)

<a id="ch-02"></a>

## Chapter 2 — Discrete mathematics

### Learning outcomes

You will (1) count combinations of attributes; (2) use sets to describe data categories; (3) reason about uniqueness with the pigeonhole principle.

### 2.1 Counting combinations

Zara counts how many distinct profiles Pellmore's booking form can produce. Birth date has about 36,500 values over a century, sex has two common values, and Pellmore serves around 3,000 postal areas. The product is over two hundred million possible combinations, far more than Pellmore's 150,000 patients. Most combinations are empty and many patients sit alone in their combination. This simple counting argument explains the finding of Sweeney (2002) that a few ordinary attributes can single out most people, which Zara will study in detail later in the course.

### 2.2 Sets and categories

Data protection law uses categories that behave like sets. The GDPR distinguishes personal data from special categories in Article 9, which include data concerning health. Zara draws a Venn diagram: all data Pellmore holds, the subset that is personal data, and inside it the subset that is health data. She notices that almost everything Pellmore holds falls in the innermost set, because even an appointment time at a telemedicine clinic reveals that someone sought care. Set thinking helps her see why classification decisions must be made carefully.

### 2.3 The pigeonhole principle

If more pigeons than holes exist, some hole contains at least two pigeons. Zara uses the converse: when there are far more holes than pigeons, most holes contain at most one. With two hundred million combinations and 150,000 patients, uniqueness is almost guaranteed unless attributes are coarsened. Prof. Holm asks her to compute how coarse the attributes must be before each combination holds at least five patients on average. Reducing birth date to birth year and postal area to region brings the number of combinations close to the needed scale.

### 2.4 Graphs of relationships

Discrete mathematics also covers graphs. Zara models Pellmore's systems as nodes and data flows as edges. A patient record moves from the app to the booking database, then to the video vendor, the records system and the laboratory partner. The graph shows where personal data travel and which nodes connect to outside organisations. She learns that such a graph is the starting point for a record of processing activities, which Article 30 of the GDPR requires, and that missing edges in the diagram usually mean undocumented and therefore unmanaged data flows.

### Worked example

Zara counts over two hundred million attribute combinations for 150,000 patients, classifies Pellmore's data with sets, applies the pigeonhole principle to uniqueness and draws a data-flow graph.

> **Synthetic case.** Patient numbers are synthetic; GDPR Articles 9 and 30 and Sweeney (2002) are real.

### Errors and limits

Uniform counting assumes values are equally likely; real attributes cluster.

### Exercises

- **EX004 — Combination count.** Why do many patients sit alone in their combination? *Rubric:* 3 = combinations vastly outnumber patients;; 2 = mentions numbers;; 1 = wrong;; 0 = none.
- **EX005 — Innermost set.** Why does most Pellmore data fall in the health-data subset? *Rubric:* 3 = even appointments reveal that someone sought medical care;; 2 = mentions health;; 1 = says only records;; 0 = none.
- **EX006 — Missing edges.** What does a missing edge in the data-flow graph usually mean? *Rubric:* 3 = an undocumented flow that is not managed;; 2 = mentions error;; 1 = vague;; 0 = none.

### Synthesis

Chapter 2 counts, classifies and maps. Chapter 3 looks at the physical side of data.

### Continue studying — chapter 02 of 50

[← Chapter 01 (draft)](#ch-01) · [Course chapter index](../SUBJECTS.md) · [Chapter 03 (draft) →](#ch-03)

<a id="ch-03"></a>

## Chapter 3 — Physics for computing

### Learning outcomes

You will (1) explain how data persist on physical media; (2) reason about deletion at the hardware level; (3) link physical facts to erasure obligations.

### 3.1 Bits are physical

In physics for computing Zara learns that stored bits are physical states: charge in flash cells, magnetised regions on disks. Deleting a file usually removes only a pointer, leaving the states intact until overwritten. For Pellmore this matters because the GDPR right to erasure in Article 17 requires that data be erased without undue delay in certain cases. If engineers equate deleting a database row with erasing data, copies may persist on disks, in logs and in backups, which is a gap between what the system reports and what is physically true.

### 3.2 Flash memory and wear levelling

Solid-state drives spread writes across cells to avoid wearing out any single area. A consequence is that overwriting a file may write to new cells and leave the old ones untouched. Zara reads that secure deletion on such media relies on built-in sanitisation commands or encryption. With encryption, data are stored only in encrypted form and destroying the key renders all copies unreadable. This approach, often called cryptographic erasure, is attractive for Pellmore's video archive, where physical overwriting of every copy would be impractical across many drives.

### 3.3 Energy and retention

Physics also teaches that storage consumes energy and space. Keeping years of video consultations has a cost in power and cooling as well as in risk. Zara writes a short note for Pellmore's facilities team linking retention to energy use. Shorter retention reduces both the environmental footprint and the amount of health data exposed in a breach. The argument is not decisive on its own, but it shows that privacy engineering often aligns with other engineering goals, which can make proposals easier to accept for managers.

### 3.4 Signals and side channels

Finally, Zara studies how physical signals leak information. Video calls send packets whose sizes and timing can reveal activity even when content is encrypted, and screens emit faint signals. For Pellmore the practical lesson is modest: encrypting video protects content, but metadata such as call duration and time still reveal that a patient consulted a doctor. She notes this as a theme to revisit when she studies networks and threat models, because protecting metadata often requires design choices rather than encryption alone.

### Worked example

Zara explains that row deletion leaves physical traces, proposes cryptographic erasure for the video archive, links retention to energy use and notes metadata leakage from encrypted calls.

> **Synthetic case.** Pellmore's archive is synthetic; GDPR Article 17 is real.

### Errors and limits

Cryptographic erasure depends on keys never being copied in plaintext; key management becomes the critical control.

### Exercises

- **EX007 — Pointer deletion.** Why does deleting a file often fail to erase the data? *Rubric:* 3 = only the pointer is removed; the physical states remain until overwritten;; 2 = mentions overwrite;; 1 = says it erases;; 0 = none.
- **EX008 — Cryptographic erasure.** How does cryptographic erasure work? *Rubric:* 3 = data stored encrypted; destroying the key makes every copy unreadable;; 2 = mentions keys;; 1 = describes overwriting;; 0 = none.
- **EX009 — Metadata leak.** What still leaks from an encrypted video call? *Rubric:* 3 = metadata such as time and duration reveal that a consultation happened;; 2 = mentions metadata;; 1 = vague;; 0 = none.

### Synthesis

Chapter 3 grounds erasure in physics. Chapter 4 starts programming for privacy.

### Continue studying — chapter 03 of 50

[← Chapter 02 (draft)](#ch-02) · [Course chapter index](../SUBJECTS.md) · [Chapter 04 (draft) →](#ch-04)

<a id="ch-04"></a>

## Chapter 4 — Programming I

### Learning outcomes

You will (1) write simple programs that handle personal data safely; (2) avoid logging identifiers; (3) validate input to reduce collection errors.

### 4.1 First programs with personal data

Zara's first programming course uses Python. Her first assignment, a booking script, asks for a patient's name and birth date and prints a confirmation. Prof. Holm points out that her debugging prints include the full birth date, which would end up in logs if the script ran on a server. Logs are often kept longer and protected less than databases. Zara replaces the print with a message that contains only a booking reference, a habit that the EDPB guidance on data protection by design would describe as protecting data by default.

### 4.2 Validating input

The booking form accepts free text for the reason for the visit. Zara notices that patients type far more than needed, including medications and family history. She changes the form to offer a short list of visit types and a limited free-text field with a clear note on what to include. Validating and limiting input is a programming technique, but it also applies the data minimisation principle in Article 5(1)(c) of the GDPR, which requires personal data to be adequate, relevant and limited to what is necessary.

### 4.3 Functions and responsibility

As her script grows, Zara splits it into functions: one to collect input, one to validate, one to store. She adds a function that pseudonymises a patient identifier with a keyed hash before it is passed to analytics. The key is kept separately, which matches the GDPR definition of pseudonymisation in Article 4(5). She learns that putting privacy logic in a single function makes it easier to test and harder to forget, and that a function name such as pseudonymise also documents intent for other developers.

### 4.4 Testing with fake data

Zara's tests use invented patients generated by the script, never real data copied from Pellmore. She writes a test that checks that no log line contains a birth date pattern. Prof. Holm calls this a privacy unit test and asks the class to add one to every assignment. The habit of testing privacy properties automatically will become important later in the verification laboratories, where Zara will test entire systems, but it begins with a few lines in a first-year programming exercise and a commitment never to use real records for development.

### Worked example

Zara removes birth dates from debug output, limits free text, isolates pseudonymisation in one function and adds a privacy unit test that scans logs for birth dates.

> **Synthetic case.** The script and patients are synthetic; GDPR Articles 4(5) and 5(1)(c) and EDPB Guidelines 4/2019 are real.

### Errors and limits

A keyed hash is pseudonymisation, not anonymisation; anyone with the key can re-link.

### Exercises

- **EX010 — Debug logging.** Why is printing birth dates in debug output risky? *Rubric:* 3 = logs are kept longer and protected less than databases;; 2 = mentions logs;; 1 = harmless;; 0 = none.
- **EX011 — Free text limits.** Which GDPR principle does limiting free-text input apply? *Rubric:* 3 = data minimisation in Article 5(1)(c);; 2 = mentions minimisation;; 1 = names another;; 0 = none.
- **EX012 — Privacy unit test.** What does Zara's privacy unit test check? *Rubric:* 3 = that no log line contains a birth-date pattern;; 2 = mentions logs;; 1 = omits;; 0 = none.

### Synthesis

Chapter 4 builds safe programming habits. Chapter 5 trains communication.

### Continue studying — chapter 04 of 50

[← Chapter 03 (draft)](#ch-03) · [Course chapter index](../SUBJECTS.md) · [Chapter 05 (draft) →](#ch-05)

<a id="ch-05"></a>

## Chapter 5 — Engineering communication

### Learning outcomes

You will (1) write privacy notices engineers and patients understand; (2) document design decisions; (3) explain risk without jargon.

### 5.1 Writing for patients

In engineering communication Zara rewrites Pellmore's privacy notice. The original is long and legalistic. Articles 12 to 14 of the GDPR require information to be given in a concise, transparent, intelligible and easily accessible form, using clear and plain language. Zara reorganises the notice around patients' questions: what is collected, why, who sees it, how long it is kept and how to exercise rights. She tests the draft with five classmates who are not engineers and rewrites every sentence they misread. The final notice is shorter and more accurate.

### 5.2 Layered information

Zara learns that one document cannot serve everyone. She designs a layered notice: a short summary at the point of booking, a full notice linked from it, and specific explanations at the moment a feature uses data, such as when the app asks for camera access. Acquisti, Brandimarte and Loewenstein (2015) describe how people's privacy decisions depend on context and framing, which supports giving information at the moment of decision rather than only in a long document read once, if at all, when an account is created.

### 5.3 Design decision records

Engineers also need to communicate with each other. Zara starts a decision log for her Pellmore work. Each entry states the decision, the alternatives considered, the privacy reasoning and who approved it. For example, she records the choice to store booking references rather than names in analytics. Prof. Holm explains that such records support the accountability principle in Article 5(2) of the GDPR, which requires a controller to be able to demonstrate compliance, and that they help future engineers understand why a system looks the way it does.

### 5.4 Explaining risk plainly

Zara practises explaining risk to managers. Instead of saying that a dataset has high re-identification risk, she says that someone who knows a patient's postcode and birth date could find that patient's consultation history in it. Concrete explanations lead to better decisions because managers can picture the harm. She also learns to state uncertainty honestly, for example that a risk estimate depends on what an attacker knows, without hiding behind it. Communication, she concludes, is an engineering skill that determines whether good designs are adopted at all.

### Worked example

Zara rewrites the privacy notice around patients' questions, layers it at decision points, starts a decision log for accountability and practises concrete risk explanations.

> **Synthetic case.** The notice and decision log are synthetic; GDPR Articles 5(2) and 12–14 and Acquisti et al. (2015) are real.

### Errors and limits

Plain language must stay accurate; simplification that misstates processing breaches transparency.

### Exercises

- **EX013 — Transparency standard.** What form must GDPR information take? *Rubric:* 3 = concise, transparent, intelligible, easily accessible, clear and plain language;; 2 = lists some;; 1 = says detailed;; 0 = none.
- **EX014 — Just-in-time notice.** Why give information when a feature uses data? *Rubric:* 3 = decisions depend on context, so information at that moment is more useful;; 2 = mentions timing;; 1 = says once is enough;; 0 = none.
- **EX015 — Decision log role.** Which principle does the decision log support? *Rubric:* 3 = accountability in Article 5(2);; 2 = mentions accountability;; 1 = names another;; 0 = none.

### Synthesis

Chapter 5 makes communication part of design. Chapter 6 returns to mathematics with accumulation.

### Continue studying — chapter 05 of 50

[← Chapter 04 (draft)](#ch-04) · [Course chapter index](../SUBJECTS.md) · [Chapter 06 (draft) →](#ch-06)

<a id="ch-06"></a>

## Chapter 6 — Calculus II

### Learning outcomes

You will (1) integrate exposure over time; (2) model exponential decay of risk; (3) use series to accumulate privacy loss.

### 6.1 Accumulated exposure

Zara models Pellmore's exposure as the number of patient records stored multiplied by the time they are stored. Integrating storage over a year gives patient-days of exposure. A retention period of thirty days instead of indefinite storage for video recordings reduces the integral dramatically, even though the daily inflow is unchanged. She shows the calculation to Pellmore's engineering lead as an area under two curves. The visual makes the effect of retention immediate, and it gives a single number that can be tracked as a key indicator.

### 6.2 Decay and staleness

Some risks decay. An old address is less useful to an attacker than a current one, and the usefulness of contact data might be modelled as decaying exponentially with time. Zara warns against over-using the model: health information does not lose sensitivity with age, and a diagnosis from ten years ago can still harm someone. She concludes that decay models can guide retention for low-sensitivity data, but special categories need explicit rules rather than an assumption that risk fades away naturally over time.

### 6.3 Series and accumulation

In later work Zara will publish repeated statistics. Calculus II introduces series, sums of many terms. If each release leaks a small amount of information, the total after many releases is the sum. Zara writes the sum for daily releases and sees that it grows without bound. This foreshadows the composition property of differential privacy described by Dwork and Roth (2014), where privacy loss adds up across queries, and it makes her sceptical of any claim that frequent releases are safe because each one is individually harmless.

### 6.4 Approximation

Taylor approximations let engineers replace a complex function with a simple one near a point. Zara uses the idea to estimate how a small change in retention affects exposure: near the current policy, exposure changes roughly in proportion to the retention period. She uses this to explain that halving retention roughly halves exposure for that category. Prof. Holm reminds her that approximations hold only near the point where they were made, which is a useful caution whenever engineers extrapolate from small changes to large redesigns.

### Worked example

Zara integrates storage to get patient-days of exposure, limits decay models to low-sensitivity data, sums repeated releases to foreshadow composition and uses a linear approximation for retention changes.

> **Synthetic case.** Exposure figures are synthetic; Dwork and Roth (2014) is real.

### Errors and limits

Patient-days ignores sensitivity differences between records; weight categories when needed.

### Exercises

- **EX016 — Patient-days.** What does integrating storage over time measure? *Rubric:* 3 = accumulated exposure in patient-days;; 2 = mentions area;; 1 = storage size;; 0 = none.
- **EX017 — Decay caution.** Why are decay models unsuitable for health data? *Rubric:* 3 = health information keeps its sensitivity over time;; 2 = mentions sensitivity;; 1 = accepts decay;; 0 = none.
- **EX018 — Summed releases.** What does summing daily leakage show? *Rubric:* 3 = total privacy loss grows without bound as releases continue;; 2 = mentions growth;; 1 = says it stays small;; 0 = none.

### Synthesis

Chapter 6 accumulates exposure and loss. Chapter 7 uses probability to collect sensitive data safely.

### Continue studying — chapter 06 of 50

[← Chapter 05 (draft)](#ch-05) · [Course chapter index](../SUBJECTS.md) · [Chapter 07 (draft) →](#ch-07)

<a id="ch-07"></a>

## Chapter 7 — Probability and statistics

### Learning outcomes

You will (1) apply randomised response to a sensitive survey; (2) estimate a proportion and its uncertainty; (3) explain the privacy-accuracy trade-off.

### 7.1 A sensitive question

Pellmore wants to know how many patients skip prescribed medication, but patients may not answer honestly if they fear their doctor will see. Zara proposes randomised response, a classic survey technique. Each patient privately flips a coin: on heads they answer truthfully, on tails they flip again and answer yes on heads and no on tails. Any single yes might be the coin, so no answer reveals the truth about any individual, yet the overall proportion can still be estimated from many answers because the coin's behaviour is known.

### 7.2 Estimating the share

The lab simulates 2,000 patients, of whom 17.9% truly skip medication. With the coin design, a quarter of all answers are random yeses, so the observed share of yes answers is 0.344. The estimate subtracts the random part and doubles the remainder, giving 0.189 with a 95% interval from 0.147 to 0.231. The interval contains the true value. Zara explains each step to Pellmore's clinical lead, emphasising that the estimate describes the group and that individual answers remain deniable even to the survey team. The clinical lead accepts the method for the pilot survey.

### 7.3 The cost of deniability

Privacy has a price in accuracy. A direct survey of 2,000 honest respondents would have a standard error of 0.009, but randomised response has 0.021, more than twice as large. Zara explains that the noise that protects individuals also blurs the estimate, so a larger sample is needed for the same precision. This is the same trade-off she will meet in differential privacy, where randomised response is often presented as an early example of a mechanism that gives each respondent plausible deniability. Noise widens the estimate's error.

### 7.4 Honest answers as the real gain

Zara also notes that the comparison with a direct survey assumes patients would answer honestly, which is exactly what Pellmore doubts. If fear makes many patients deny skipping medication, a direct survey would be precise but wrong. Randomised response trades precision for honesty. She recommends it for this question and writes a short consent explanation so that patients understand the coin mechanism. Prof. Holm adds that statistics is not only about calculating intervals but about understanding how data were generated and what could bias them.

### Lab — Randomised response survey on medication adherence

```python
# Randomised response: estimate how many of 2,000 synthetic patients skipped medication, without learning anyone's answer.
import random
r = random.Random(4)
true_p, n = 0.18, 2000
truth = [r.random() < true_p for _ in range(n)]
# each respondent flips a coin: heads answer truthfully, tails answer "yes" with probability 1/2
ans = [t if r.random() < 0.5 else (r.random() < 0.5) for t in truth]
y = sum(ans) / n
est = (y - 0.25) / 0.5
se = (y * (1 - y) / n) ** 0.5 / 0.5
print(f"true share {sum(truth)/n:.3f}; observed yes {y:.3f}; estimate {est:.3f} (95% CI {est-1.96*se:.3f} to {est+1.96*se:.3f})")
print(f"direct-survey standard error would be {(est*(1-est)/n)**0.5:.3f}; randomised response {se:.3f}")
```

Run with `python3 lab_rr.py`. Verified output:

```text
true share 0.179; observed yes 0.344; estimate 0.189 (95% CI 0.147 to 0.231)
direct-survey standard error would be 0.009; randomised response 0.021
```

### Worked example

Zara estimates medication skipping at 0.189 (95% interval 0.147 to 0.231) against a true 0.179, and shows the standard error rising from 0.009 to 0.021 as the price of deniability.

> **Synthetic case.** Patients and answers are synthetic and seeded.

### Errors and limits

The method protects against the survey holder only if patients trust the coin; poor explanation undermines it.

### Exercises

- **EX019 — Deniability.** Why does a single yes not reveal a patient's behaviour? *Rubric:* 3 = it may come from the coin rather than the truth;; 2 = mentions randomness;; 1 = says it reveals;; 0 = none.
- **EX020 — Estimate computation.** How is the estimate 0.189 derived from 0.344? *Rubric:* 3 = subtract the 0.25 random yeses and divide by 0.5;; 2 = describes partly;; 1 = wrong;; 0 = none.
- **EX021 — Error ratio.** How much larger is the randomised-response standard error? *Rubric:* 3 = 0.021 versus 0.009, more than twice;; 2 = mentions larger;; 1 = wrong;; 0 = none.

### Synthesis

Chapter 7 shows privacy-accuracy trade-offs in a survey. Chapter 8 looks at hardware where data live.

### Continue studying — chapter 07 of 50

[← Chapter 06 (draft)](#ch-06) · [Course chapter index](../SUBJECTS.md) · [Chapter 08 (draft) →](#ch-08)

<a id="ch-08"></a>

## Chapter 8 — Computer architecture

### Learning outcomes

You will (1) trace where data sit in memory and caches; (2) understand hardware isolation; (3) assess hardware features for protecting health data.

### 8.1 Data in many places

In computer architecture Zara follows a patient record through a server. It sits on disk, is copied into memory, passes through processor caches and may be written to swap space. Each copy is a place where data can persist or leak. She realises that an application that carefully deletes records may still leave fragments in memory dumps or swap files. For Pellmore she recommends encrypted swap and disabling crash dumps that include memory on production servers, unless a dump is explicitly requested and handled under a defined procedure.

### 8.2 Isolation

Architecture provides isolation: processes cannot normally read each other's memory, and virtual machines are separated by a hypervisor. Zara learns that hardware flaws have sometimes broken these boundaries, so cloud tenants share risk with neighbours. For Pellmore's records system she reads the cloud provider's documentation on dedicated hosts and confidential computing, which encrypts memory in use. She notes that such features reduce risk but add cost and complexity, and that the choice should follow a risk assessment rather than a vendor brochure.

### 8.3 Trusted hardware for keys

Hardware security modules and secure enclaves keep cryptographic keys away from ordinary memory. Zara links this to Chapter 3: if Pellmore uses cryptographic erasure for videos, the keys are the most valuable asset, and storing them in a hardware module makes accidental copying much harder. She sketches a design where each month of recordings has its own key, kept in the module, and deleting a month's key erases that month. The design turns retention enforcement into a simple, auditable key operation. Auditors can check key deletion logs.

### 8.4 Performance trade-offs

Encryption and isolation cost processor time. Zara measures that encrypting video at rest adds little load on modern processors with hardware acceleration. She records the measurement in her decision log, because the claim that privacy measures are too slow often blocks good designs without evidence. Prof. Holm reminds her that measurements should be repeated on Pellmore's actual workload, but her first figures are enough to move the conversation from opinion to data, which is a recurring goal in her engineering training. Encryption adds measurable latency.

### Worked example

Zara maps copies of a record from disk to cache, recommends encrypted swap, considers confidential computing and designs monthly keys in a hardware module for cryptographic erasure.

> **Synthetic case.** Pellmore's servers are synthetic.

### Errors and limits

Hardware features have their own flaws; defence in depth still matters.

### Exercises

- **EX022 — Hidden copies.** Name two places where a deleted record may persist in a server. *Rubric:* 3 = memory dumps and swap (also caches);; 2 = names one;; 1 = vague;; 0 = none.
- **EX023 — Monthly keys.** How do monthly keys make retention auditable? *Rubric:* 3 = deleting a month's key erases that month's recordings in one operation;; 2 = mentions keys;; 1 = omits;; 0 = none.
- **EX024 — Evidence over opinion.** Why measure encryption overhead? *Rubric:* 3 = to replace claims that privacy is too slow with data;; 2 = mentions speed;; 1 = skips it;; 0 = none.

### Synthesis

Chapter 8 places data in hardware. Chapter 9 advances programming.

### Continue studying — chapter 08 of 50

[← Chapter 07 (draft)](#ch-07) · [Course chapter index](../SUBJECTS.md) · [Chapter 09 (draft) →](#ch-09)

<a id="ch-09"></a>

## Chapter 9 — Programming II

### Learning outcomes

You will (1) design data structures that separate identifiers; (2) apply access checks in code; (3) write tests for privacy properties.

### 9.1 Separating identifiers

In Programming II Zara designs Pellmore's patient record as two linked structures: an identity table with name and contact details, and a clinical table keyed by an internal identifier. Most services need only the clinical part or only the identity part, rarely both. Separating them in code makes it easy to give each service only what it needs. She recognises this as an implementation of data protection by design, where the structure of the software itself limits exposure rather than relying on every developer to remember a rule.

### 9.2 Access checks in code

Zara writes a function that every service must call before reading a record. It checks the caller's role and the purpose of the request against a policy table. A receptionist can read appointment times but not clinical notes; a clinician can read notes only for patients booked with them. The function logs each access with the purpose. She tests that a call without a purpose fails. Prof. Holm points out that putting checks in one place prevents inconsistent rules, which are a common source of over-broad access in real systems.

### 9.3 Property-based testing

Zara learns property-based testing, where a tool generates many random inputs to test general rules. She writes properties such as no function returning a clinical record to a receptionist role, and no export function ever including the identity table. The tool finds one bug: an export written by a classmate joins both tables for convenience. Fixing it removes a path by which full records could leave the system. She realises that testing privacy properties generally is more powerful than checking a few hand-picked examples.

### 9.4 Error handling

Error messages can leak data. Zara finds that a failed booking returns an error containing the patient's full record for debugging. She changes errors to return a reference code and logs details internally under access control. She also ensures that exceptions do not print stack traces with variable values to users. These small changes reduce accidental disclosure, which often happens through ordinary software paths such as errors rather than through dramatic attacks, and they make the system more professional in the eyes of patients and auditors.

### Worked example

Zara separates identity from clinical data, centralises purpose-based access checks, finds an export bug with property-based tests and removes data from error messages.

> **Synthetic case.** The code and patients are synthetic.

### Errors and limits

Central checks become a single point of failure; they need their own tests and monitoring.

### Exercises

- **EX025 — Split record.** Why split identity and clinical data into two structures? *Rubric:* 3 = most services need only one part, so each gets only what it needs;; 2 = mentions separation;; 1 = no reason;; 0 = none.
- **EX026 — Purpose in access.** Why must callers state a purpose to read a record? *Rubric:* 3 = access is checked and logged against purpose, preventing over-broad use;; 2 = mentions logging;; 1 = says optional;; 0 = none.
- **EX027 — Property test finding.** What bug did property-based testing find? *Rubric:* 3 = an export joining identity and clinical tables;; 2 = mentions export;; 1 = vague;; 0 = none.

### Synthesis

Chapter 9 encodes privacy in programs. Chapter 10 considers ethics and safety.

### Continue studying — chapter 09 of 50

[← Chapter 08 (draft)](#ch-08) · [Course chapter index](../SUBJECTS.md) · [Chapter 10 (draft) →](#ch-10)

<a id="ch-10"></a>

## Chapter 10 — Engineering ethics and safety

### Learning outcomes

You will (1) apply engineering ethics to privacy decisions; (2) recognise harms beyond legal compliance; (3) decide when to escalate concerns.

### 10.1 Duties of an engineer

Engineering ethics asks professionals to hold public safety and welfare paramount. Zara applies this to Pellmore. Health data exposure can cause discrimination, embarrassment, loss of employment and distress. Warren and Brandeis (1890) wrote of injury to feelings; Solove (2006) lists harms such as disclosure, exposure and increased accessibility. Zara writes that her duty is not only to satisfy the law but to prevent foreseeable harm to patients, even when no regulator would notice, because patients cannot see or control how the system is built.

### 10.2 Beyond compliance

Zara finds a case where law and ethics diverge. Pellmore's analytics team wants to infer pregnancy from appointment patterns to send targeted health tips. The processing might be framed lawfully with consent, but many patients would find it intrusive and some could be harmed if a family member saw the messages. Nissenbaum's contextual integrity helps her articulate the problem: information shared for care is flowing into marketing, a different context with different norms. She recommends against the feature and records her reasoning in the decision log.

### 10.3 Safety of patients

Telemedicine adds safety concerns. If a video consultation fails silently, a patient may miss urgent care. Zara learns that privacy measures must not create safety risks: an over-strict session timeout could cut off a consultation. She works with clinicians to set timeouts that protect unattended devices without ending active calls. The exercise teaches her that safety and privacy are both duties toward the same patients, and that engineers must balance them openly rather than maximising one quietly at the expense of the other.

### 10.4 Escalation

Zara asks what she should do if a manager ignores a serious privacy concern. Prof. Holm explains that she should first document the concern and raise it with her supervisor and the data protection officer, whose role under GDPR Articles 38 and 39 includes advising the organisation and monitoring compliance independently. If the concern remains unaddressed and patients are at risk, professional codes and whistleblowing protections may apply. Zara writes a personal escalation plan, hoping never to use it, but feeling more confident that she knows the route.

### Worked example

Zara frames her duty around foreseeable harm, recommends against pregnancy inference using contextual integrity, balances timeouts with clinical safety and writes an escalation route through the data protection officer.

> **Synthetic case.** The analytics proposal is synthetic; Warren and Brandeis (1890), Solove (2006), Nissenbaum (2004) and GDPR Articles 38–39 are real.

### Errors and limits

Ethical judgement varies; recording reasoning lets others challenge it.

### Exercises

- **EX028 — Ethical duty.** What duty goes beyond legal compliance for Zara? *Rubric:* 3 = preventing foreseeable harm to patients even when unnoticed;; 2 = mentions harm;; 1 = only the law;; 0 = none.
- **EX029 — Pregnancy inference.** Why does Zara advise against the pregnancy inference feature? *Rubric:* 3 = care information flows into marketing, breaking contextual norms and risking harm;; 2 = mentions intrusion;; 1 = supports it;; 0 = none.
- **EX030 — DPO role.** Why escalate to the data protection officer? *Rubric:* 3 = the DPO advises and monitors compliance independently under Articles 38–39;; 2 = mentions DPO;; 1 = goes to press first;; 0 = none.

### Synthesis

Chapter 10 grounds the foundations in ethics. Chapter 11 begins the systems block with networks.

### Continue studying — chapter 10 of 50

[← Chapter 09 (draft)](#ch-09) · [Course chapter index](../SUBJECTS.md) · [Chapter 11 (draft) →](#ch-11)

<a id="ch-11"></a>

## Chapter 11 — Networks and protocols

### Learning outcomes

You will (1) identify personal data in network traffic; (2) apply encryption in transit; (3) limit metadata collection.

### 11.1 Personal data on the wire

In networks Zara captures traffic from a test copy of Pellmore's app on a lab network with synthetic accounts. She sees that the app sends the patient's email address to an analytics server in a URL parameter. URLs end up in server logs, proxies and browser history. Even with transport encryption, the receiving server logs the full address. Zara files a defect: identifiers must never travel in URLs. She explains to the app team that encryption protects data on the wire but not what the recipient does with it after arrival.

### 11.2 Transport encryption

Zara checks that all of Pellmore's endpoints use current transport layer security and reject old protocol versions. She explains to the class that Article 32 of the GDPR requires security appropriate to the risk, including encryption where appropriate, and that health data in transit is a clear case. She also verifies that internal traffic between services is encrypted, because attackers who reach the internal network often find unencrypted traffic there. The finding leads Pellmore to enable mutual authentication between its booking and records services.

### 11.3 Metadata minimisation

Network devices log IP addresses, which the Court of Justice of the European Union has treated as personal data in some circumstances, and which in any case can locate a patient. Zara reviews Pellmore's firewall and load balancer logs and finds full IP addresses kept for two years. She recommends truncating the last part of addresses after seven days, keeping full addresses only in a short security log. The change keeps enough for attack investigation while reducing a long-lived record of where patients connected from.

### 11.4 Third-party calls

The capture also shows calls to six third-party domains: fonts, analytics, crash reporting and advertising measurement. Zara lists each, what it receives and whether Pellmore has a contract with it. Two have no data processing agreement. Article 28 of the GDPR requires a binding contract with processors. She recommends removing the advertising script entirely, hosting fonts locally and signing agreements for the remaining processors. The exercise shows her that a network capture is also a compliance audit tool, revealing flows that documentation missed.

### Worked example

Zara finds an email address in an analytics URL, confirms transport and internal encryption, truncates stored IP addresses after seven days and removes or contracts six third-party calls.

> **Synthetic case.** The app and captures are synthetic; GDPR Articles 28 and 32 are real.

### Errors and limits

Captures on test builds may miss production behaviour; repeat on release builds.

### Exercises

- **EX031 — URL identifiers.** Why must identifiers not travel in URLs? *Rubric:* 3 = URLs are logged by servers, proxies and browsers despite encryption;; 2 = mentions logs;; 1 = fine if encrypted;; 0 = none.
- **EX032 — IP truncation.** What does truncating stored IP addresses achieve? *Rubric:* 3 = keeps attack investigation capacity while reducing long-lived location data;; 2 = mentions privacy;; 1 = deletes all logs;; 0 = none.
- **EX033 — Processor contracts.** What does Article 28 require for third-party processors? *Rubric:* 3 = a binding contract governing processing;; 2 = mentions contract;; 1 = vague;; 0 = none.

### Synthesis

Chapter 11 audits the network. Chapter 12 studies operating systems.

### Continue studying — chapter 11 of 50

[← Chapter 10 (draft)](#ch-10) · [Course chapter index](../SUBJECTS.md) · [Chapter 12 (draft) →](#ch-12)

<a id="ch-12"></a>

## Chapter 12 — Operating systems

### Learning outcomes

You will (1) apply file permissions to protect records; (2) control logging at the operating system level; (3) manage temporary files.

### 12.1 Permissions

Zara studies how operating systems enforce permissions. On Pellmore's records server she finds that export files are written to a shared directory readable by all users. Any account on the server, including monitoring tools, could read them. She changes the export process to write into a directory owned by a dedicated service account with no access for others. Least privilege at the operating system level is a basic control, she notes, but it is often overlooked because applications are tested on developer machines where everyone is an administrator.

### 12.2 System logs

Operating systems log events, and applications sometimes write sensitive data into system logs. Zara searches Pellmore's server logs for patterns resembling birth dates and email addresses and finds several. She configures log rotation with defined retention and adds a filter that masks identifiers before they are written. She also restricts who can read the logs. Logs are needed for security, she writes, but they must be designed with the same care as databases, because they often contain the most complete record of what happened to whom.

### 12.3 Temporary files

Report generation creates temporary files on disk, which are not always cleaned up after crashes. Zara finds hundreds of leftover temporary reports containing patient names. She changes the process to use the operating system's secure temporary file functions with restrictive permissions and to clean up on start, and she adds a scheduled job that deletes any temporary report older than one day. The finding shows her that data protection requires attention to the unglamorous parts of systems as well as their main databases.

### 12.4 Updates and patching

Finally, Zara checks patch levels. Unpatched operating systems are a frequent cause of breaches. She learns that Pellmore patches monthly but has no record of when critical patches were applied. She proposes tracking patch delay as a metric and agreeing a maximum delay for critical security updates. Prof. Holm reminds her that Article 32 asks for a process for regularly testing and evaluating the effectiveness of security measures, and patch metrics are one way to show that such a process actually exists. Her metric: days to patch.

### Worked example

Zara moves exports to a service-owned directory, masks identifiers in system logs, cleans leftover temporary reports and proposes tracking patch delay.

> **Synthetic case.** The server findings are synthetic; GDPR Article 32 is real.

### Errors and limits

Masking filters miss unusual formats; periodic searches remain necessary.

### Exercises

- **EX034 — Shared export directory.** What was wrong with the export directory? *Rubric:* 3 = it was readable by every account on the server;; 2 = mentions permissions;; 1 = vague;; 0 = none.
- **EX035 — Temporary reports.** How does Zara deal with leftover temporary reports? *Rubric:* 3 = secure temp functions, cleanup on start and a daily deletion job;; 2 = one measure;; 1 = ignores;; 0 = none.
- **EX036 — Patch metric.** Why track patch delay? *Rubric:* 3 = to show a regular process for testing and maintaining security, as Article 32 expects;; 2 = mentions patching;; 1 = vague;; 0 = none.

### Synthesis

Chapter 12 tightens the operating system. Chapter 13 enforces retention in databases.

### Continue studying — chapter 12 of 50

[← Chapter 11 (draft)](#ch-11) · [Course chapter index](../SUBJECTS.md) · [Chapter 13 (draft) →](#ch-13)

<a id="ch-13"></a>

## Chapter 13 — Data systems

### Learning outcomes

You will (1) express retention rules in a database; (2) query records past retention; (3) design deletion that is safe and verifiable.

### 13.1 Retention as data

Article 5(1)(e) of the GDPR requires storage limitation: personal data must be kept in identifiable form no longer than necessary. Pellmore has a retention policy on paper, but nothing in its databases enforces it. Zara proposes storing the policy as a table, with one row per data category and its retention period. Each record carries its category and creation date. With policy as data, a simple query can find records that should have been deleted, and changes to the policy are versioned like any other data.

### 13.2 The query

The lab builds 400 synthetic records in SQLite across four categories with retention periods of thirty days for video recordings, 180 days for marketing leads, 365 days for chat logs and 730 days for appointments. On 1 October 2026, 96 of 101 video recordings, 82 of 100 marketing leads, 72 of 101 chat logs and 12 of 98 appointments are past retention: 262 of 400 records in total. Zara presents the result as evidence that the paper policy has never been applied, with the video category the clearest gap. The query uses only stdlib sqlite3, so every classmate can rerun it.

### 13.3 Safe deletion

Deleting 262 records at once is risky. Some may be needed for legal claims or clinical safety. Zara designs a two-step process: records past retention are first marked and hidden from normal use, a weekly report lists them for review by a designated owner, and after fourteen days unflagged records are deleted. Records subject to a legal hold are excluded automatically. The design balances storage limitation with the need to avoid destroying evidence, and every step is logged for accountability so that deletions can be shown later.

### 13.4 Backups and replicas

Deleting from the main database does not delete from backups and replicas. Zara documents how backups expire on their own schedule and ensures that restored backups are re-checked against the retention table before use. She also checks that read replicas apply deletions promptly. Prof. Holm points out that regulators generally accept that backups cannot be edited record by record, provided they are protected, expire within a defined time and are not restored without reapplying deletions. Zara records this reasoning in the retention design document.

### Lab — Records past their retention period

```python
# SQLite: which synthetic records are past their retention period on 2026-10-01?
import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE policy(category TEXT PRIMARY KEY, keep_days INTEGER);
INSERT INTO policy VALUES ('video_recording',30),('chat_log',365),('appointment',730),('marketing_lead',180);
CREATE TABLE rec(id INTEGER, category TEXT, created TEXT);
""")
import random; r = random.Random(2)
cats = ['video_recording', 'chat_log', 'appointment', 'marketing_lead']
for i in range(400):
    db.execute("INSERT INTO rec VALUES (?,?,date('2026-10-01', ?))", (i, r.choice(cats), f"-{r.randint(0, 900)} days"))
q = """SELECT r.category, COUNT(*), SUM(julianday('2026-10-01') - julianday(r.created) > p.keep_days)
       FROM rec r JOIN policy p USING(category) GROUP BY r.category ORDER BY 3 DESC"""
tot = 0
for c, n, over in db.execute(q):
    tot += over; print(f"{c:16s} records {n:3d}  past retention {over:3d}")
print(f"total past retention: {tot} of 400")
```

Run with `python3 lab_retention.py`. Verified output:

```text
video_recording  records 101  past retention  96
marketing_lead   records 100  past retention  82
chat_log         records 101  past retention  72
appointment      records  98  past retention  12
total past retention: 262 of 400
```

### Worked example

Zara stores retention policy as a table, finds 262 of 400 synthetic records past retention (96 of 101 video recordings), and designs a mark-review-delete process with legal holds and backup handling.

> **Synthetic case.** Records are synthetic and seeded; GDPR Article 5(1)(e) is real.

### Errors and limits

Creation date may not be the right start for retention; some periods start at the end of a relationship.

### Exercises

- **EX037 — Storage limitation.** What does Article 5(1)(e) require? *Rubric:* 3 = data kept identifiable no longer than necessary;; 2 = mentions retention;; 1 = wrong;; 0 = none.
- **EX038 — Worst category.** Which category has the largest share past retention in the lab? *Rubric:* 3 = video recordings: 96 of 101;; 2 = names video;; 1 = names appointments;; 0 = none.
- **EX039 — Backup rule.** How are backups handled under the retention design? *Rubric:* 3 = protected, expire on schedule, deletions reapplied on restore;; 2 = two points;; 1 = ignores backups;; 0 = none.

### Synthesis

Chapter 13 turns policy into queries. Chapter 14 brings privacy into software engineering.

### Continue studying — chapter 13 of 50

[← Chapter 12 (draft)](#ch-12) · [Course chapter index](../SUBJECTS.md) · [Chapter 14 (draft) →](#ch-14)

<a id="ch-14"></a>

## Chapter 14 — Software engineering

### Learning outcomes

You will (1) write privacy requirements as user stories; (2) include privacy in code review; (3) manage personal data in test environments.

### 14.1 Privacy stories

In software engineering Zara learns to write requirements as user stories. She adds privacy stories to Pellmore's backlog: as a patient, I want to download my records so that I can check what is held; as a patient, I want my video recordings deleted after thirty days unless I ask otherwise. Each story has acceptance criteria that can be tested. Writing privacy as stories puts it in the same planning process as features, rather than leaving it to a separate document that developers rarely read.

### 14.2 Code review

Pellmore's code review checklist covers style and tests but not privacy. Zara adds five questions: does this change collect new personal data; is any new data logged; does it send data to a new recipient; does it change retention; and does it affect access checks. Reviewers must answer each question. In the first month the checklist catches a change that would have sent full patient names to a crash reporting service. The example convinces the team that a few targeted questions are worth the extra minute per review.

### 14.3 Test data

Developers at Pellmore sometimes copied production data into test environments to reproduce bugs. Zara explains that test environments are usually less protected and that copying health data there is a serious risk. She builds a generator that produces realistic synthetic patients with the same structure and edge cases, such as long names and unusual characters. Where production data are truly needed for a bug, a documented request with approval and automatic expiry replaces informal copying. NIST SP 800-188 discusses synthetic data as one de-identification approach.

### 14.4 Definition of done

Finally Zara proposes changes to the team's definition of done. A feature is done only when its privacy stories pass, the review checklist is completed, the record of processing is updated if data flows change, and the privacy notice is updated if patients would be surprised. The team debates whether this slows delivery. Zara argues that fixing privacy after release is slower and more expensive, and Pellmore's engineering lead agrees to try the definition for one quarter and review the effect on delivery times.

### Worked example

Zara writes privacy user stories, adds five privacy questions to code review, replaces production copies with a synthetic data generator and extends the definition of done.

> **Synthetic case.** The backlog and review are synthetic; NIST SP 800-188 is real.

### Errors and limits

Checklists become rote; rotate examples and audit samples of reviews.

### Exercises

- **EX040 — Privacy story.** Write one privacy user story from the chapter. *Rubric:* 3 = e.g. as a patient I want recordings deleted after thirty days unless I ask otherwise;; 2 = similar story;; 1 = vague;; 0 = none.
- **EX041 — Review catch.** What did the review checklist catch in its first month? *Rubric:* 3 = a change sending full names to a crash reporter;; 2 = mentions crash reporting;; 1 = vague;; 0 = none.
- **EX042 — Synthetic test data.** Why replace production copies with generated patients? *Rubric:* 3 = test environments are less protected; synthetic data avoids exposing health data;; 2 = mentions safety;; 1 = uses masking only;; 0 = none.

### Synthesis

Chapter 14 embeds privacy in delivery. Chapter 15 covers security fundamentals.

### Continue studying — chapter 14 of 50

[← Chapter 13 (draft)](#ch-13) · [Course chapter index](../SUBJECTS.md) · [Chapter 15 (draft) →](#ch-15)

<a id="ch-15"></a>

## Chapter 15 — Security fundamentals

### Learning outcomes

You will (1) relate confidentiality, integrity and availability to data protection; (2) apply authentication suited to health data; (3) understand security's role in GDPR Article 32.

### 15.1 Security serves privacy

Zara learns the classic security goals: confidentiality, integrity and availability. She relates them to data protection. Confidentiality prevents unauthorised disclosure of health records; integrity prevents wrong results reaching a patient; availability ensures clinicians can see records during a consultation. The GDPR lists integrity and confidentiality as a principle in Article 5(1)(f). But Zara notes that privacy is broader than security: a perfectly secure system can still collect too much or use data for unexpected purposes, so security is necessary but not sufficient.

### 15.2 Authentication

Pellmore patients log in with passwords. Zara reviews options and recommends adding a second factor for viewing records and for changing contact details, the actions most attractive to attackers. She avoids text-message codes as the only option, offering an authenticator app as well, and she ensures that recovery does not depend on knowledge questions whose answers are often public. Clinicians get stronger authentication because they can see many patients' records. She explains that authentication strength should follow the harm an account could do.

### 15.3 Article 32 measures

Article 32 lists examples of security measures: pseudonymisation and encryption, the ability to ensure ongoing confidentiality, integrity, availability and resilience, the ability to restore access after an incident, and regular testing. Zara maps Pellmore's controls to each example and finds gaps in restoring access and in testing. She explains that the article requires measures appropriate to the risk, taking into account the state of the art and costs, which makes risk assessment the starting point rather than a fixed list of controls. Encryption is named explicitly.

### 15.4 Integrity for patients

Zara studies an integrity failure: a test result attached to the wrong patient. This is both a safety and a data protection problem, because it discloses one patient's data to another and may harm both. She proposes checks: matching on two identifiers before attaching results, and alerts when names differ. She notes that errors like this are personal data breaches under the GDPR definition in Article 4(12), which includes accidental disclosure, not only attacks, and that they must be handled through the breach process.

### Worked example

Zara links security goals to data protection, adds step-up authentication, maps controls to Article 32 and treats misattached results as both a safety issue and a personal data breach.

> **Synthetic case.** Pellmore's controls are synthetic; GDPR Articles 4(12), 5(1)(f) and 32 are real.

### Errors and limits

Strong authentication can exclude patients with limited access to devices; offer alternatives.

### Exercises

- **EX043 — Not sufficient.** Why is security necessary but not sufficient for privacy? *Rubric:* 3 = a secure system can still over-collect or misuse data;; 2 = mentions purposes;; 1 = equates them;; 0 = none.
- **EX044 — Step-up actions.** Which patient actions get a second factor, and why? *Rubric:* 3 = viewing records and changing contacts, the most attractive to attackers;; 2 = names one;; 1 = all logins only;; 0 = none.
- **EX045 — Accidental breach.** Is a result attached to the wrong patient a personal data breach? *Rubric:* 3 = yes; Article 4(12) includes accidental disclosure;; 2 = yes without reason;; 1 = no;; 0 = none.

### Synthesis

Chapter 15 relates security to data protection. Chapter 16 takes a systems view.

### Continue studying — chapter 15 of 50

[← Chapter 14 (draft)](#ch-14) · [Course chapter index](../SUBJECTS.md) · [Chapter 16 (draft) →](#ch-16)

<a id="ch-16"></a>

## Chapter 16 — Systems engineering

### Learning outcomes

You will (1) describe Pellmore's platform as a system of systems; (2) trace privacy requirements across interfaces; (3) manage privacy through the life cycle.

### 16.1 System of systems

Systems engineering treats a product as interacting parts. Zara draws Pellmore's platform: mobile app, booking service, video service run by a vendor, records system, laboratory interface, analytics and support desk. Each has its own owner, data and failure modes. Privacy properties such as retention or access control must hold across all of them. A property enforced in one part and ignored in another is effectively absent. She calls this the weakest-interface problem and uses it to justify end-to-end requirements rather than component-by-component promises.

### 16.2 Requirement traceability

Zara creates a traceability matrix linking each privacy requirement to the components that implement it and the tests that verify it. For example, the thirty-day video retention requirement traces to the vendor contract, the archive key schedule and a monthly deletion test. Gaps appear immediately: the analytics system has no requirement for retention at all. ISO/IEC 27701:2025, the privacy information management system standard, emphasises documented controls and evidence, and Zara's matrix provides exactly that kind of documentation at the engineering level. Each row cites its source.

### 16.3 Life cycle

Systems pass through concept, development, operation and retirement. Privacy concerns differ at each stage: at concept, whether to collect data at all; in development, how to protect it; in operation, how to monitor; at retirement, how to delete or migrate. Zara notices that Pellmore has no plan for retiring its old booking system, which still holds data. She adds a decommissioning checklist with data inventory, migration or deletion, and certificate of destruction. Retirement, she writes, is when forgotten data most often escape.

### 16.4 Interfaces with vendors

Many of Pellmore's components are run by vendors. Zara learns that systems engineering must include contracts as interfaces. The video vendor's contract specifies retention, sub-processors and breach notification times. She checks that these match Pellmore's own requirements and finds that the vendor may keep recordings for ninety days, longer than Pellmore's thirty-day rule. She flags the mismatch for contract renegotiation. The example shows that legal documents are part of the technical system and must be engineered with the same care. Contracts carry technical promises.

### Worked example

Zara models Pellmore as a system of systems, builds a requirement traceability matrix, adds a decommissioning checklist and finds a ninety-day vendor retention clause that conflicts with the thirty-day rule.

> **Synthetic case.** The platform and vendor are synthetic; ISO/IEC 27701:2025 is real.

### Errors and limits

Traceability matrices go stale unless updated with each change.

### Exercises

- **EX046 — Weakest interface.** What is the weakest-interface problem? *Rubric:* 3 = a privacy property ignored in one component is effectively absent;; 2 = mentions components;; 1 = vague;; 0 = none.
- **EX047 — Analytics gap.** What gap did the traceability matrix reveal? *Rubric:* 3 = analytics had no retention requirement;; 2 = mentions analytics;; 1 = vague;; 0 = none.
- **EX048 — Contract mismatch.** What vendor mismatch did Zara find? *Rubric:* 3 = vendor may keep recordings 90 days versus Pellmore's 30;; 2 = mentions retention;; 1 = vague;; 0 = none.

### Synthesis

Chapter 16 engineers the whole system. Chapter 17 applies feedback control.

### Continue studying — chapter 16 of 50

[← Chapter 15 (draft)](#ch-15) · [Course chapter index](../SUBJECTS.md) · [Chapter 17 (draft) →](#ch-17)

<a id="ch-17"></a>

## Chapter 17 — Control and feedback basics

### Learning outcomes

You will (1) model privacy controls as feedback loops; (2) choose measurable signals; (3) avoid unstable or gamed control.

### 17.1 Feedback loops

Control engineering uses feedback: measure an output, compare with a target, adjust. Zara models Pellmore's retention process this way. The output is the number of records past retention; the target is zero; the controller is the deletion job. If the count rises, the job runs more often or a person investigates. Without measurement there is no feedback, which explains why Pellmore's paper policy failed. She draws the loop and labels each element, which helps managers see that monitoring is part of the control, not an extra.

### 17.2 Choosing signals

A feedback loop needs a signal that reflects the goal. For access control Zara considers the number of record views without a booked appointment. A rising count could indicate snooping by staff. For consent, the share of patients whose consent record is missing. She chooses signals that are cheap to compute, hard to fake and directly related to harm. She learns from Chapter 29 of her plan, which she reads ahead, that measurement design will become a full topic later, but even simple signals change behaviour.

### 17.3 Stability

Badly tuned loops oscillate. If the deletion job deletes aggressively whenever the count rises, it might remove records under legal hold or overload the database. Zara adds limits: deletion caps per run, an exclusion list and an alert if the count rises suddenly, which usually signals a fault rather than ordinary growth. She explains that in privacy, as in physical control, stability matters more than speed: a slow, predictable process is better than a fast one that occasionally destroys records it should keep.

### 17.4 Gaming

Any measured target can be gamed. If managers are judged on the number of overdue records, someone might change the category of records to one with a longer period. Zara adds a second signal that tracks category changes and requires approval for them. Prof. Holm reminds the class of the general warning that when a measure becomes a target it can cease to be a good measure. Combining signals and keeping a human review of anomalies reduces, though it never removes, the risk of gaming.

### Worked example

Zara models retention as a feedback loop, chooses signals for snooping and missing consent, adds limits for stability and a second signal to detect gaming.

> **Synthetic case.** Signals and thresholds are synthetic.

### Errors and limits

Signals can generate false alarms; review thresholds after the first months of data.

### Exercises

- **EX049 — Missing feedback.** Why did the paper retention policy fail in control terms? *Rubric:* 3 = there was no measurement, so no feedback adjusted the process;; 2 = mentions monitoring;; 1 = other cause;; 0 = none.
- **EX050 — Snooping signal.** What signal might reveal staff snooping? *Rubric:* 3 = record views without a booked appointment;; 2 = mentions views;; 1 = vague;; 0 = none.
- **EX051 — Gaming defence.** How does Zara guard against category gaming? *Rubric:* 3 = track and require approval for category changes;; 2 = mentions monitoring;; 1 = vague;; 0 = none.

### Synthesis

Chapter 17 frames privacy as control. Chapter 18 designs architecture.

### Continue studying — chapter 17 of 50

[← Chapter 16 (draft)](#ch-16) · [Course chapter index](../SUBJECTS.md) · [Chapter 18 (draft) →](#ch-18)

<a id="ch-18"></a>

## Chapter 18 — Security architecture

### Learning outcomes

You will (1) apply zones and segmentation to health data; (2) design for least privilege at scale; (3) evaluate architecture against data protection by design.

### 18.1 Zones

Zara divides Pellmore's architecture into zones: a public zone for the app front end, an application zone for booking and video, a restricted zone for clinical records and a management zone for administrators. Traffic between zones passes through controlled interfaces. Clinical records are reachable only from services that need them. Segmentation limits how far an attacker can move after compromising one service, and it also limits accidental access, since a misconfigured analytics job in the application zone cannot read the records zone directly.

### 18.2 Least privilege at scale

With dozens of services, manual permissions become unmanageable. Zara designs role templates for services and people, with permissions tied to purposes. A service account for appointment reminders can read names and appointment times but not clinical notes. Permissions are declared in configuration and reviewed automatically for changes. She explains that least privilege is not only about attackers: it also implements the purpose limitation principle in Article 5(1)(b), since each component can use data only for the purposes its role allows. Roles encode purposes.

### 18.3 Privacy patterns

Zara studies architectural patterns that support privacy: aggregation before data leave a zone, pseudonymisation at zone boundaries, and separate stores for identity and clinical data. She applies them to analytics: events leaving the application zone carry a pseudonymous identifier and coarse timestamps, and aggregation runs before data reach the analytics vendor. The EDPB guidelines on data protection by design describe such measures as ways to implement principles effectively, and Zara cites them when presenting her design to Pellmore's architecture board. The board approves the pattern list.

### 18.4 Evaluating the design

Zara evaluates the architecture with three questions: what personal data reach each zone, who can access them, and how would a failure in one zone affect others. She finds that support staff in the application zone can see full clinical notes through a support tool. She redesigns the tool to show notes only when a patient grants temporary access during a support call. The evaluation shows that architecture reviews must look at tools and people as well as servers, because many disclosures happen through legitimate interfaces used too broadly.

### Worked example

Zara segments Pellmore into four zones, templates purpose-based permissions, pseudonymises and aggregates at zone boundaries and redesigns a support tool to require patient-granted access.

> **Synthetic case.** The architecture is synthetic; GDPR Article 5(1)(b) and EDPB Guidelines 4/2019 are real.

### Errors and limits

Zones on diagrams can differ from deployed reality; verify with network tests.

### Exercises

- **EX052 — Segmentation benefit.** Name two benefits of zone segmentation. *Rubric:* 3 = limits attacker movement and accidental access;; 2 = names one;; 1 = vague;; 0 = none.
- **EX053 — Purpose via roles.** How does least privilege implement purpose limitation? *Rubric:* 3 = each component can only use data its role's purpose allows;; 2 = mentions purpose;; 1 = unrelated;; 0 = none.
- **EX054 — Support tool.** How was the support tool redesigned? *Rubric:* 3 = notes visible only with temporary patient-granted access;; 2 = mentions consent;; 1 = removes tool;; 0 = none.

### Synthesis

Chapter 18 designs zones and patterns. Chapter 19 covers identity and cryptography.

### Continue studying — chapter 18 of 50

[← Chapter 17 (draft)](#ch-17) · [Course chapter index](../SUBJECTS.md) · [Chapter 19 (draft) →](#ch-19)

<a id="ch-19"></a>

## Chapter 19 — Identity and cryptography

### Learning outcomes

You will (1) choose identifiers that limit linkage; (2) apply encryption and keyed hashing correctly; (3) understand the limits of pseudonymisation.

### 19.1 Identifiers and linkage

Zara notices that Pellmore uses the same patient number in every system, including analytics and the laboratory partner. A single identifier lets anyone with access to two datasets join them. She proposes domain-specific pseudonyms: each external recipient receives a different identifier derived from the internal one with a separate key. Linking datasets then requires the keys, which stay with Pellmore. This approach reduces linkage between recipients and fits the GDPR concept of pseudonymisation, in which additional information is kept separately. Each recipient gets a different pseudonym.

### 19.2 Keyed hashing

A plain hash of a patient number is not a pseudonym, because anyone can hash all possible numbers and compare. Zara uses a keyed hash with a secret key stored in Pellmore's hardware module. She explains that without the key, reversing the pseudonym is infeasible, but with it, re-linking is trivial. Therefore the key must be protected like the data itself. She documents key rotation: when a key changes, all pseudonyms for that recipient change, which can be used deliberately to break long-term linkage after a project ends.

### 19.3 Encryption choices

Zara reviews encryption at rest. Database encryption protects against stolen disks but not against an attacker using the application. Field-level encryption for especially sensitive fields, such as mental health notes, adds protection because only services holding the field key can decrypt. She weighs the extra complexity and decides to apply field-level encryption only to a small set of fields defined by clinicians. The decision illustrates the proportionality in Article 32, where measures follow risk rather than being applied everywhere. Low-risk fields stay unencrypted for searchability.

### 19.4 Limits of pseudonymisation

Zara reminds herself that pseudonymised data are still personal data under the GDPR. A pseudonymous record with a birth date and postcode can be re-identified through the attributes, as Sweeney (2002) showed, regardless of how well the identifier is protected. Garfinkel (NISTIR 8053, 2015) makes the same point: removing direct identifiers is only a first step. Pseudonymisation reduces risk and is encouraged by the GDPR, but it does not make data anonymous, and Pellmore's contracts must reflect that. Anyone holding the key table can reverse the pseudonyms, so the table is stored apart from the data.

### Worked example

Zara replaces one universal patient number with recipient-specific keyed pseudonyms, protects keys in hardware, applies field-level encryption to clinician-defined fields and documents why pseudonymised data remain personal data.

> **Synthetic case.** Identifiers and keys are synthetic; Sweeney (2002) and NISTIR 8053 are real.

### Errors and limits

Key rotation breaks legitimate longitudinal analysis; plan it with users.

### Exercises

- **EX055 — Plain hash weakness.** Why is a plain hash of a patient number not a pseudonym? *Rubric:* 3 = anyone can hash all possible numbers and match;; 2 = mentions reversal;; 1 = says it is secure;; 0 = none.
- **EX056 — Recipient pseudonyms.** What do recipient-specific pseudonyms prevent? *Rubric:* 3 = joining datasets across recipients without Pellmore's keys;; 2 = mentions linkage;; 1 = vague;; 0 = none.
- **EX057 — Still personal.** Why are pseudonymised records still personal data? *Rubric:* 3 = attributes and keys allow re-identification;; 2 = mentions keys;; 1 = says anonymous;; 0 = none.

### Synthesis

Chapter 19 completes the security foundations. Chapter 20 sets the engineering context of data protection.

### Continue studying — chapter 19 of 50

[← Chapter 18 (draft)](#ch-18) · [Course chapter index](../SUBJECTS.md) · [Chapter 20 (draft) →](#ch-20)

<a id="ch-20"></a>

## Chapter 20 — Privacy and data protection: engineering context

### Learning outcomes

You will (1) map the legal framework that shapes Pellmore's engineering; (2) identify roles of controller and processor; (3) relate standards and frameworks to engineering work.

### 20.1 Laws that apply

Pellmore serves patients in the EU and Brazil, so both the GDPR and the LGPD, Lei 13.709/2018, apply. Both define principles such as purpose limitation and necessity, rights for individuals and duties for organisations. Both treat health data as especially sensitive: GDPR Article 9 and LGPD Article 11 restrict processing to specific grounds. Zara builds a table comparing the two laws on legal bases, rights, breach notification and the role of a data protection officer, so that engineering requirements can be stated once and satisfy both.

### 20.2 Controllers and processors

Zara learns the difference between a controller, who decides why and how data are processed, and a processor, who acts on the controller's behalf. Pellmore is the controller for patient records; the video vendor is a processor. Laboratory partners may be separate controllers for their own testing. The roles determine who is responsible for what, including rights requests and breach notification. EDPB Guidelines 07/2020 explain the concepts in detail, and Zara uses them to label each node in her data-flow graph from Chapter 2.

### 20.3 Frameworks and standards

Beyond law, Zara studies frameworks. The NIST Privacy Framework 1.0 organises privacy risk management into functions such as Identify-P, Govern-P, Control-P, Communicate-P and Protect-P. ISO/IEC 29100 defines privacy principles and terms, and ISO/IEC 27701:2025 specifies a privacy information management system. She uses the NIST functions to group her engineering work: inventories under Identify-P, access controls under Protect-P and notices under Communicate-P. Frameworks, she notes, help organise work but do not replace legal analysis. Legal questions, such as which lawful basis applies to a new research use, still need counsel.

### 20.4 The engineer's role

Prof. Holm closes the first two years by asking what an engineer contributes to data protection. Zara answers that lawyers interpret obligations, but engineers decide how systems actually behave. A retention rule exists only if code deletes data; a right of access exists only if systems can find a person's data. Data protection by design, required by GDPR Article 25, places responsibility on the controller to build these capabilities into systems. Engineers are therefore central to whether data protection is real or only written down.

### Worked example

Zara compares GDPR and LGPD, labels controllers and processors on her flow graph, organises work with the NIST Privacy Framework functions and defines the engineer's role through Article 25.

> **Synthetic case.** Pellmore's roles are synthetic; the GDPR, LGPD, EDPB Guidelines 07/2020, NIST Privacy Framework 1.0, ISO/IEC 29100 and ISO/IEC 27701:2025 are real.

### Errors and limits

The comparison table simplifies; national laws and regulators add detail.

### Exercises

- **EX058 — Health data grounds.** Which articles restrict health data processing in GDPR and LGPD? *Rubric:* 3 = GDPR Article 9 and LGPD Article 11;; 2 = names one;; 1 = wrong;; 0 = none.
- **EX059 — Controller versus processor.** Is the video vendor a controller or a processor, and why? *Rubric:* 3 = processor; it acts on Pellmore's behalf;; 2 = says processor;; 1 = says controller;; 0 = none.
- **EX060 — Engineer centrality.** Why are engineers central to data protection? *Rubric:* 3 = systems' behaviour decides whether rights and retention are real;; 2 = mentions implementation;; 1 = says lawyers decide;; 0 = none.

### Synthesis

Chapter 20 frames the legal and standards context. Chapter 21 writes privacy requirements.

### Continue studying — chapter 20 of 50

[← Chapter 19 (draft)](#ch-19) · [Course chapter index](../SUBJECTS.md) · [Chapter 21 (draft) →](#ch-21)

<a id="ch-21"></a>

## Chapter 21 — Privacy and data protection: requirements

### Learning outcomes

You will (1) derive requirements from legal principles; (2) make requirements testable; (3) prioritise requirements by risk.

### 21.1 From principles to requirements

Zara starts the third year by deriving requirements from the principles in GDPR Article 5: lawfulness, fairness and transparency; purpose limitation; data minimisation; accuracy; storage limitation; integrity and confidentiality; and accountability. For each she writes at least one engineering requirement for Pellmore. Purpose limitation becomes: every data field shall be tagged with the purposes for which it may be used, and services shall read only fields tagged for their purpose. Turning principles into requirements forces precision that the legal text, written to apply everywhere, cannot provide.

### 21.2 Testable wording

A requirement that cannot be tested cannot be verified. Zara rewrites vague statements. "Data shall be kept secure" becomes "clinical notes shall be encrypted at rest with keys held in the hardware module, verified quarterly". "Patients shall be able to access their data" becomes "a patient shall be able to download all personal data held about them within one minute of request, in a machine-readable format". Each requirement now has a verification method. ISO/IEC 29100 provides consistent terms such as PII principal and PII controller, which Zara uses in the definitions section.

### 21.3 Rights as requirements

Zara writes requirements for each data subject right that applies to Pellmore: access, rectification, erasure, restriction, portability and objection. For erasure she specifies which stores must be covered and which exceptions apply, such as medical records that must be retained under health law. The LGPD Article 18 lists similar rights for Brazilian patients, including information about sharing with third parties. Writing the rights as system requirements reveals that portability needs a structured export format that Pellmore does not yet have. She adds a JSON export ticket.

### 21.4 Prioritising by risk

Not all requirements can be built at once. Zara ranks them by the harm their absence would cause and the likelihood that it would occur. Erasure of video recordings and access control for clinical notes come first; portability of appointment history comes later. She records the ranking and its reasoning in the decision log. Prof. Holm reminds her that risk-based prioritisation is supported by the GDPR, which repeatedly asks for measures appropriate to the risk, but legal duties still apply even when ranked lower.

### Worked example

Zara derives requirements from each Article 5 principle, rewrites them as testable statements, specifies rights requirements for GDPR and LGPD and ranks them by risk.

> **Synthetic case.** Requirements are synthetic; GDPR Article 5, LGPD Article 18 and ISO/IEC 29100 are real.

### Errors and limits

Ranking cannot postpone a legal duty indefinitely; lower-ranked items still need dates.

### Exercises

- **EX061 — Purpose tagging.** How does Zara turn purpose limitation into a requirement? *Rubric:* 3 = tag fields with permitted purposes; services read only fields tagged for their purpose;; 2 = mentions tags;; 1 = restates principle;; 0 = none.
- **EX062 — Testable access.** Rewrite "patients shall be able to access their data" testably. *Rubric:* 3 = download all data within one minute in machine-readable format;; 2 = partly measurable;; 1 = vague;; 0 = none.
- **EX063 — Portability gap.** Which gap did rights requirements reveal? *Rubric:* 3 = no structured export format for portability;; 2 = mentions export;; 1 = vague;; 0 = none.

### Synthesis

Chapter 21 writes requirements. Chapter 22 models systems and data flows.

### Continue studying — chapter 21 of 50

[← Chapter 20 (draft)](#ch-20) · [Course chapter index](../SUBJECTS.md) · [Chapter 22 (draft) →](#ch-22)

<a id="ch-22"></a>

## Chapter 22 — Privacy and data protection: system and data models

### Learning outcomes

You will (1) build a data-flow inventory; (2) check each flow for purpose, lawful basis and transfers; (3) connect the inventory to the record of processing.

### 22.1 The inventory

Zara converts her data-flow graph into an inventory with one row per flow: source, destination, purpose, lawful basis, region and transfer mechanism. Article 30 of the GDPR requires controllers to keep a record of processing activities, including purposes, categories of recipients and transfers to third countries. An inventory at flow level is more detailed than the legal minimum, but it is what engineers need to find problems. She checks seven flows from Pellmore's platform, chosen to cover internal systems, vendors and partners. Each flow has an owner.

### 22.2 Automated checks

The lab applies three rules to each flow: it must have a purpose, it must have a lawful basis, and if data leave the European Economic Area it must name a transfer mechanism. Four flows pass. The analytics SDK has no purpose, no lawful basis and no transfer mechanism for its United States destination. The offshore support team has no transfer mechanism. The research extract has no lawful basis. Three of seven flows need action. Zara notes that the analytics flow, added by the app team without review, fails every rule.

### 22.3 Transfers

Chapter V of the GDPR restricts transfers of personal data to countries outside the EEA. Transfers need an adequacy decision or appropriate safeguards such as standard contractual clauses. The marketing email platform has clauses recorded and passes. The offshore support team has none. Zara does not decide which mechanism to use, which is a legal question, but she flags the gap with the facts lawyers need: what data, how much, how often and why. She learns that engineers make transfers visible, while counsel decides how to make them lawful.

### 22.4 Research basis

The research extract sends records to an internal research team without a recorded basis. Health research may rely on specific grounds such as GDPR Article 9(2)(j) together with safeguards under Article 89, or on consent. Zara asks the data protection officer to determine the basis and recommends pseudonymising the extract in the meantime. She adds a rule to the inventory process: new flows cannot be deployed until all three fields are completed and reviewed, which turns the inventory from a document into a deployment gate.

### Lab — Checking data flows for purpose, basis and transfers

```python
# Check a synthetic data-flow inventory: every flow needs a purpose, a lawful basis and, if leaving the EEA, a transfer mechanism.
flows = [
 ("app -> booking DB", "appointments", "contract", "EEA", ""),
 ("booking DB -> video vendor", "consultation", "contract", "EEA", ""),
 ("app -> analytics SDK", "", "", "US", ""),
 ("records -> lab partner", "test orders", "health care (Art 9(2)(h))", "EEA", ""),
 ("support desk -> offshore team", "support", "contract", "non-EEA", ""),
 ("records -> research extract", "research", "", "EEA", ""),
 ("marketing list -> email platform", "newsletter", "consent", "US", "SCCs"),
]
bad = 0
for name, purpose, basis, region, mech in flows:
    issues = []
    if not purpose: issues.append("no purpose")
    if not basis: issues.append("no lawful basis")
    if region != "EEA" and not mech: issues.append("no transfer mechanism")
    bad += bool(issues)
    print(f"{name:34s} {'OK' if not issues else '; '.join(issues)}")
print(f"{bad} of {len(flows)} flows need action")
```

Run with `python3 lab_flow.py`. Verified output:

```text
app -> booking DB                  OK
booking DB -> video vendor         OK
app -> analytics SDK               no purpose; no lawful basis; no transfer mechanism
records -> lab partner             OK
support desk -> offshore team      no transfer mechanism
records -> research extract        no lawful basis
marketing list -> email platform   OK
3 of 7 flows need action
```

### Worked example

Zara builds a seven-flow inventory and finds three needing action: the analytics SDK (no purpose, basis or transfer mechanism), offshore support (no transfer mechanism) and the research extract (no basis).

> **Synthetic case.** Flows are synthetic; GDPR Articles 9(2)(j), 30 and 89 and Chapter V are real.

### Errors and limits

An inventory reflects what people report; network captures and code scans catch unreported flows.

### Exercises

- **EX064 — Failing flows.** How many flows need action, and which fails every rule? *Rubric:* 3 = three of seven; the analytics SDK;; 2 = count only;; 1 = wrong;; 0 = none.
- **EX065 — Transfer roles.** Who decides the transfer mechanism, and what does the engineer provide? *Rubric:* 3 = counsel decides; engineers provide facts on data, volume, frequency and purpose;; 2 = partial;; 1 = engineer decides;; 0 = none.
- **EX066 — Deployment gate.** How does the inventory become a deployment gate? *Rubric:* 3 = new flows cannot deploy until purpose, basis and transfer fields are reviewed;; 2 = mentions review;; 1 = stays a document;; 0 = none.

### Synthesis

Chapter 22 models and checks flows. Chapter 23 analyses threats and failures.

### Continue studying — chapter 22 of 50

[← Chapter 21 (draft)](#ch-21) · [Course chapter index](../SUBJECTS.md) · [Chapter 23 (draft) →](#ch-23)

<a id="ch-23"></a>

## Chapter 23 — Privacy and data protection: threat and failure analysis

### Learning outcomes

You will (1) apply a privacy threat model to the platform; (2) analyse failure modes that harm privacy; (3) include non-malicious threats.

### 23.1 Privacy threats

Security threat models focus on attackers. Zara adds privacy threats that can occur without any attacker: linkability, identifiability, non-repudiation, detectability, disclosure, unawareness and non-compliance. She applies them to the video consultation flow. Linkability arises because the same identifier appears in video logs and analytics; unawareness because patients are not told that the vendor records sessions. Solove's taxonomy supports the same analysis from a legal angle, naming harms such as aggregation and secondary use that a purely security-focused model would miss. Both views are recorded.

### 23.2 Failure modes

Zara performs a failure mode analysis on the erasure process. Possible failures include a deletion job that times out, a store that is not included in the job, a backup restored without reapplying deletions and a vendor that ignores the request. For each she estimates the effect on patients and how it would be detected. The vendor failure is hardest to detect because Pellmore cannot see the vendor's systems. She proposes contractual confirmation of deletion and periodic audit rights, which Article 28 of the GDPR allows controllers to require.

### 23.3 Insiders and errors

Many privacy incidents involve staff error or curiosity rather than outside attackers. Zara models a receptionist sending results to the wrong email address and a clinician looking up a neighbour's record. Controls include address confirmation, access logging with anomaly signals from Chapter 17 and training. She notes that monitoring staff is itself processing of personal data and must be proportionate and transparent to employees. The analysis shows that privacy threat models must include the organisation's own people, both as potential sources of harm and as people whose own privacy deserves respect.

### 23.4 Ranking threats

Zara ranks threats using a simple combination of likelihood and harm, and selects the top five for detailed treatment in the data protection impact assessment. Linkability through shared identifiers, vendor retention, misdirected results, staff snooping and analytics over-collection lead the list. She writes each threat as a short scenario that non-engineers can follow. Prof. Holm points out that scenarios make threats concrete for decision-makers, as she learned in communication, and that they also become test cases for the verification laboratory later in the year.

### Worked example

Zara applies privacy threat categories to video consultations, analyses erasure failure modes, models insider errors and ranks five threats for the DPIA.

> **Synthetic case.** Scenarios are synthetic; Solove (2006) and GDPR Article 28 are real.

### Errors and limits

Threat lists are never complete; revisit after incidents and design changes.

### Exercises

- **EX067 — Non-attacker threats.** Name two privacy threats that need no attacker. *Rubric:* 3 = e.g. unawareness and non-compliance (also linkability);; 2 = names one;; 1 = names hacking;; 0 = none.
- **EX068 — Vendor failure.** Why is vendor non-deletion hard to detect, and what helps? *Rubric:* 3 = Pellmore cannot see vendor systems; contractual confirmation and audit rights;; 2 = one part;; 1 = ignores;; 0 = none.
- **EX069 — Staff monitoring.** What constraint applies to monitoring staff access? *Rubric:* 3 = it must be proportionate and transparent because it processes employees' data;; 2 = mentions privacy;; 1 = unlimited;; 0 = none.

### Synthesis

Chapter 23 finds threats. Chapter 24 assesses them in a DPIA.

### Continue studying — chapter 23 of 50

[← Chapter 22 (draft)](#ch-22) · [Course chapter index](../SUBJECTS.md) · [Chapter 24 (draft) →](#ch-24)

<a id="ch-24"></a>

## Chapter 24 — Privacy and data protection: methods I

### Learning outcomes

You will (1) conduct a data protection impact assessment; (2) score risks before and after measures; (3) decide whether prior consultation is needed.

### 24.1 When a DPIA is needed

Article 35 of the GDPR requires a data protection impact assessment where processing is likely to result in a high risk to people's rights and freedoms, in particular for large-scale processing of special categories. The Article 29 Working Party guidelines (WP248 rev.01), endorsed by the EDPB, list criteria such as sensitive data, large scale and vulnerable data subjects; meeting two criteria usually indicates a DPIA is needed. Pellmore's telemedicine processing meets several. Zara prepares the DPIA with the data protection officer, whose advice Article 35(2) requires the controller to seek.

### 24.2 Scoring risks

Zara takes the five threats from Chapter 23 and scores each for likelihood and severity on a one-to-four scale, then multiplies them. Before measures, indefinite video retention scores 9, the analytics SDK sending health events scores 12, misdirected results 8, staff snooping 9 and a vendor breach of chat logs 6. Four risks are high or medium-high. She is careful to explain that the scores are an ordering aid, not measurements, and that the descriptions of harm matter more than the numbers when people decide what to do.

### 24.3 Measures and residual risk

For each risk Zara lists measures: thirty-day retention with monthly keys, removal of the analytics SDK, two-identifier matching for results, access logging with anomaly review and contractual limits on the vendor. After measures, scores fall to 3, 4, 4 and 4 for the first four risks, but the vendor breach stays at 6, because Pellmore cannot control the vendor's security directly. No risk remains high. The residual medium risk is accepted by Pellmore's management with a plan to review the vendor at contract renewal. Renewal is in eighteen months.

### 24.4 Prior consultation

Article 36 requires the controller to consult the supervisory authority before processing where a DPIA indicates high risk that the controller has not mitigated. Zara's register shows no residual high risk, so prior consultation is not triggered by this assessment. She writes this conclusion carefully, noting that it depends on the measures actually being implemented. If the analytics SDK were not removed, the risk would remain high. The DPIA therefore lists implementation of measures as conditions with owners and dates, and it is scheduled for review after the first quarter.

### Lab — DPIA risk scores before and after measures

```python
# DPIA risk scoring: likelihood x severity (1-4 each), before and after planned measures.
risks = [("video recordings kept indefinitely", 3, 3, 1, 3), ("analytics SDK sends health events", 3, 4, 1, 4),
         ("wrong patient receives results", 2, 4, 1, 4), ("staff browse records without need", 3, 3, 2, 2),
         ("vendor breach exposes chat logs", 2, 3, 2, 3)]
def band(s): return "high" if s >= 9 else "medium" if s >= 5 else "low"
for name, l, s, l2, s2 in risks:
    print(f"{name:38s} before {l*s:2d} ({band(l*s):6s}) after {l2*s2:2d} ({band(l2*s2)})")
hi = [n for n, l, s, l2, s2 in risks if l2 * s2 >= 9]
print("residual high risks:", hi if hi else "none; prior consultation under Art 36 not triggered by this register")
```

Run with `python3 lab_dpia.py`. Verified output:

```text
video recordings kept indefinitely     before  9 (high  ) after  3 (low)
analytics SDK sends health events      before 12 (high  ) after  4 (low)
wrong patient receives results         before  8 (medium) after  4 (low)
staff browse records without need      before  9 (high  ) after  4 (low)
vendor breach exposes chat logs        before  6 (medium) after  6 (medium)
residual high risks: none; prior consultation under Art 36 not triggered by this register
```

### Worked example

Zara scores five risks, reduces four from high or medium to low with measures, keeps the vendor breach at medium (6) and concludes that prior consultation is not triggered if the measures are implemented.

> **Synthetic case.** Risks and scores are synthetic; GDPR Articles 35 and 36 and WP248 rev.01 are real.

### Errors and limits

Multiplying ordinal scores is a convention, not arithmetic on real quantities.

### Exercises

- **EX070 — DPIA trigger.** Why does Pellmore need a DPIA? *Rubric:* 3 = large-scale special-category processing meets several WP248 criteria, indicating high risk;; 2 = mentions health data;; 1 = not needed;; 0 = none.
- **EX071 — Unchanged risk.** Which risk stays medium after measures, and why? *Rubric:* 3 = vendor breach of chat logs, because Pellmore cannot directly control vendor security;; 2 = names risk;; 1 = vague;; 0 = none.
- **EX072 — Conditional conclusion.** Why is the "no prior consultation" conclusion conditional? *Rubric:* 3 = it depends on the measures being implemented, e.g. removing the SDK;; 2 = mentions measures;; 1 = unconditional;; 0 = none.

### Synthesis

Chapter 24 assesses risk. Chapter 25 is the first design studio.

### Continue studying — chapter 24 of 50

[← Chapter 23 (draft)](#ch-23) · [Course chapter index](../SUBJECTS.md) · [Chapter 25 (draft) →](#ch-25)

<a id="ch-25"></a>

## Chapter 25 — Design studio I

### Learning outcomes

You will (1) design a privacy-preserving feature end to end; (2) present design alternatives; (3) respond to critique in a studio setting.

### 25.1 The brief

In the first design studio Zara's team receives a brief: design symptom triage for Pellmore's app that suggests whether a patient needs a video consultation, a pharmacist or emergency care. The feature needs symptoms, which are health data. The team must minimise data, explain the logic to patients and avoid storing more than needed. Prof. Holm adds a constraint: the design must work if the patient refuses analytics. The brief forces the team to treat privacy as a design input from the first sketch rather than a review at the end.

### 25.2 Alternatives

The team sketches three alternatives. In the first, symptoms are sent to a server that runs the triage model and stores answers for improvement. In the second, the model runs on the phone and nothing leaves the device unless the patient books. In the third, answers are sent but deleted after the result is shown. Zara evaluates each for data collected, transparency, accuracy and cost. On-device triage collects least, but updating the model is harder and some older phones may not run it.

### 25.3 Automated decisions

The triage suggests a course of action, which raises the question of automated decision-making. Article 22 of the GDPR gives people the right not to be subject to a decision based solely on automated processing that significantly affects them, with exceptions. Zara's team designs the triage as advice with a clear option to speak to a clinician, so that no patient is denied care by the algorithm alone. They also explain the main factors in plain language, which supports transparency even where Article 22 might not strictly apply.

### 25.4 Critique

Studio critics, including a clinician, challenge the on-device design: if answers are never stored, how will the team learn that triage is unsafe? Zara proposes an opt-in feedback route and a periodic clinical review using synthetic test cases. The critics accept the approach but ask for a safety monitoring plan. Zara learns that privacy and clinical safety must be designed together, and that critique in a studio is most useful when designers explain trade-offs openly rather than defending one option as perfect.

### Worked example

Zara's team designs symptom triage with three alternatives, prefers on-device processing, frames the result as advice with a clinician option and adds opt-in feedback and synthetic safety tests.

> **Synthetic case.** The studio and feature are synthetic; GDPR Article 22 is real.

### Errors and limits

On-device processing still needs a secure update channel and may leak through crash reports.

### Exercises

- **EX073 — Least-collecting option.** Which alternative collects least data, and what is its drawback? *Rubric:* 3 = on-device triage; model updates are harder and older phones may not cope;; 2 = one part;; 1 = server option;; 0 = none.
- **EX074 — Article 22 design.** How does the team avoid a solely automated decision? *Rubric:* 3 = triage is advice with a clear option to speak to a clinician;; 2 = mentions human;; 1 = ignores;; 0 = none.
- **EX075 — Learning without storage.** How can the team learn about unsafe triage without storing answers? *Rubric:* 3 = opt-in feedback and clinical review with synthetic cases;; 2 = one part;; 1 = store everything;; 0 = none.

### Synthesis

Chapter 25 designs a feature. Chapter 26 compares architecture alternatives.

### Continue studying — chapter 25 of 50

[← Chapter 24 (draft)](#ch-24) · [Course chapter index](../SUBJECTS.md) · [Chapter 26 (draft) →](#ch-26)

<a id="ch-26"></a>

## Chapter 26 — Privacy and data protection: architecture alternatives

### Learning outcomes

You will (1) compare centralised, federated and on-device architectures; (2) evaluate privacy-enhancing technologies; (3) choose with documented criteria.

### 26.1 Three architectures

Pellmore wants to analyse consultation outcomes across clinics to improve care. Zara compares three architectures. Centralised: copy all records to one analytics store. Federated: run analyses within each clinic's system and share only results. On-device or edge: compute statistics at the point of care. Centralisation is simplest but concentrates risk. Federation keeps raw data local but complicates analysis. She writes criteria before comparing: data exposure, analysis capability, cost, operational complexity and ability to honour erasure requests across the system. Each criterion is scored from one to three before any design discussion.

### 26.2 Privacy-enhancing technologies

Zara surveys privacy-enhancing technologies. Differential privacy adds calibrated noise to outputs, following Dwork and colleagues (2006). Secure multi-party computation lets parties compute joint results without revealing inputs. Synthetic data can replace real records for development. Each has limits: differential privacy reduces accuracy, especially for small groups; multi-party computation is complex and slow; synthetic data may leak if generated carelessly from real records. NIST SP 800-188 discusses several of these approaches for government data releases, which she finds transferable to health statistics. Synthetic data suit testing well.

### 26.3 Scoring

Zara scores each architecture on her criteria with the team. Federation with differentially private aggregated outputs scores best on exposure and erasure, adequate on analysis and worse on complexity. Centralisation scores best on analysis and worst on exposure. She presents the scores with their reasoning, stressing that the weights reflect Pellmore's priorities, which management must confirm. The EDPB guidelines on data protection by design list the state of the art and cost of implementation as factors, which supports making these trade-offs explicit.

### 26.4 Decision

Pellmore's architecture board chooses federation with aggregated outputs for clinic comparisons, and a small centralised, pseudonymised dataset for clinical safety audits that need record-level data under strict access. Zara records the decision, the alternatives rejected and the conditions for revisiting it. She notes that the hybrid answer is common in practice: no single architecture fits all purposes, and documenting which purpose uses which architecture helps auditors and future engineers understand the system and resist pressure to centralise everything for convenience. The decision record names owners.

### Worked example

Zara compares centralised, federated and edge architectures against pre-set criteria, surveys privacy-enhancing technologies and records a hybrid decision: federation for comparisons, a restricted pseudonymised set for safety audits.

> **Synthetic case.** The architectures and scores are synthetic; Dwork et al. (2006), NIST SP 800-188 and EDPB Guidelines 4/2019 are real.

### Errors and limits

Scores depend on weights; show sensitivity to different weights.

### Exercises

- **EX076 — Centralisation trade-off.** What is the main trade-off of centralisation? *Rubric:* 3 = easiest analysis but concentrated exposure;; 2 = mentions risk;; 1 = says best overall;; 0 = none.
- **EX077 — PET limits.** Name a limit of each of two privacy-enhancing technologies. *Rubric:* 3 = e.g. DP loses accuracy for small groups; MPC is complex and slow;; 2 = one;; 1 = vague;; 0 = none.
- **EX078 — Hybrid decision.** What did the architecture board decide? *Rubric:* 3 = federation for comparisons plus a restricted pseudonymised set for safety audits;; 2 = one part;; 1 = centralise;; 0 = none.

### Synthesis

Chapter 26 chooses architectures. Chapter 27 designs controls.

### Continue studying — chapter 26 of 50

[← Chapter 25 (draft)](#ch-25) · [Course chapter index](../SUBJECTS.md) · [Chapter 27 (draft) →](#ch-27)

<a id="ch-27"></a>

## Chapter 27 — Privacy and data protection: control design

### Learning outcomes

You will (1) design preventive, detective and corrective privacy controls; (2) design consent management; (3) link controls to requirements and risks.

### 27.1 Types of control

Zara classifies controls as preventive, detective or corrective. Preventive controls stop problems: purpose-based access checks, field minimisation in forms. Detective controls notice problems: anomaly signals on record access, retention monitoring. Corrective controls fix problems: deletion jobs, breach response. She ensures each high-ranked risk has at least one of each type. For staff snooping, access checks prevent, anomaly signals detect, and disciplinary and notification procedures correct. A risk with only preventive controls is fragile because failures go unnoticed until harm appears. Good designs mix all three.

### 27.2 Consent management

Some Pellmore processing relies on consent, such as the newsletter and optional research participation. EDPB Guidelines 05/2020 require consent to be freely given, specific, informed and unambiguous, and as easy to withdraw as to give. Zara designs a consent service that stores what each patient agreed to, when and through which wording version. Withdrawal is one tap and propagates to all systems within a day. She ensures that care is never conditional on consent to marketing, which would make consent not freely given.

### 27.3 Controls linked to requirements

Zara extends her traceability matrix: each control now links to the requirements it satisfies and the risks it reduces. Gaps show up as risks without controls or controls without purpose. She finds a legacy control, a nightly copy of the records database to an old reporting server, that no requirement justifies. Removing it reduces exposure at no cost. The exercise shows that control design includes pruning, because old controls and processes can themselves become privacy risks when nobody remembers why they exist.

### 27.4 Control owners

Every control needs an owner who maintains it and reports on it. Zara assigns owners: the engineering lead for access checks, the data protection officer for consent wording, the operations manager for retention jobs. She writes a one-page control description for each, covering purpose, operation, evidence and failure response. Prof. Holm reminds her that ISO/IEC 27701:2025 expects documented controls with evidence of operation, and that owners are what keep controls alive after the engineers who designed them move on to other projects.

### Worked example

Zara gives each high risk preventive, detective and corrective controls, designs a consent service meeting EDPB criteria, removes an unjustified nightly copy and assigns control owners.

> **Synthetic case.** Controls are synthetic; EDPB Guidelines 05/2020 and ISO/IEC 27701:2025 are real.

### Errors and limits

Too many controls create overhead and confusion; prune regularly.

### Exercises

- **EX079 — Control types for snooping.** Give a preventive, detective and corrective control for staff snooping. *Rubric:* 3 = access checks; anomaly signals; disciplinary and notification procedures;; 2 = two;; 1 = one;; 0 = none.
- **EX080 — Valid consent.** What makes consent valid under EDPB Guidelines 05/2020? *Rubric:* 3 = freely given, specific, informed, unambiguous, easy to withdraw;; 2 = lists some;; 1 = wrong;; 0 = none.
- **EX081 — Pruned control.** What control did Zara remove, and why? *Rubric:* 3 = a nightly database copy to an old reporting server, justified by no requirement;; 2 = mentions copy;; 1 = vague;; 0 = none.

### Synthesis

Chapter 27 designs controls. Chapter 28 implements them.

### Continue studying — chapter 27 of 50

[← Chapter 26 (draft)](#ch-26) · [Course chapter index](../SUBJECTS.md) · [Chapter 28 (draft) →](#ch-28)

<a id="ch-28"></a>

## Chapter 28 — Privacy and data protection: implementation I

### Learning outcomes

You will (1) implement purpose tags and access checks; (2) implement consent propagation; (3) deploy changes safely.

### 28.1 Purpose tags in the schema

Zara implements purpose tags in Pellmore's database schema. Each column carries metadata listing the purposes allowed to read it. The access library from Chapter 9 checks the caller's declared purpose against the tags before returning data. She migrates tags gradually, starting with clinical tables. During migration, any read of an untagged column is logged as a warning rather than blocked, so the team can find missing tags without breaking the service. After two weeks the warnings stop and the check is switched to blocking mode.

### 28.2 Consent propagation

The consent service publishes events when a patient gives or withdraws consent. Downstream systems, such as the email platform and the research extract, subscribe and update their records. Zara implements idempotent handlers, so repeated events do no harm, and a daily reconciliation that compares each system's consent state with the central record. The reconciliation finds that the email platform missed withdrawals during a network outage. She fixes the handler to retry and adds an alert, showing why event systems need a check that does not depend on the events themselves.

### 28.3 Safe deployment

Privacy changes can break services. Zara deploys behind feature flags, enabling the new checks for a small group of internal test accounts, then for one clinic, then for all. She monitors errors and access denials at each step. One clinic's reporting tool fails because it read a column without a purpose. The team adds the purpose and continues. She records the incident and the fix. Gradual deployment, she notes, lets privacy controls be strict without becoming the reason a clinic cannot work on a busy morning.

### 28.4 Documentation as code

Zara keeps purpose tags, retention periods and consent purposes in version-controlled configuration files. Changes go through code review with the privacy questions from Chapter 14. The record of processing is generated partly from these files, so it stays aligned with the system. She explains that documentation generated from configuration is more reliable than documents written separately, because it changes when the system changes. Pellmore's data protection officer welcomes the approach because it gives an up-to-date view of processing without asking engineers to write reports by hand.

### Worked example

Zara implements purpose tags with a warn-then-block migration, consent events with reconciliation that catches missed withdrawals, flag-based rollout and processing records generated from configuration.

> **Synthetic case.** Implementation details are synthetic.

### Errors and limits

Generated documentation covers only what is configured; manual processes still need description.

### Exercises

- **EX082 — Warn then block.** Why log warnings before blocking untagged reads? *Rubric:* 3 = to find missing tags without breaking the service;; 2 = mentions safety;; 1 = block immediately;; 0 = none.
- **EX083 — Reconciliation catch.** What did consent reconciliation find? *Rubric:* 3 = the email platform missed withdrawals during an outage;; 2 = mentions email;; 1 = vague;; 0 = none.
- **EX084 — Generated records.** Why generate the record of processing from configuration? *Rubric:* 3 = it stays aligned with the system as it changes;; 2 = mentions accuracy;; 1 = manual is better;; 0 = none.

### Synthesis

Chapter 28 implements controls. Chapter 29 measures them.

### Continue studying — chapter 28 of 50

[← Chapter 27 (draft)](#ch-27) · [Course chapter index](../SUBJECTS.md) · [Chapter 29 (draft) →](#ch-29)

<a id="ch-29"></a>

## Chapter 29 — Privacy and data protection: measurement

### Learning outcomes

You will (1) measure data minimisation; (2) define privacy metrics; (3) report metrics without creating new risks.

### 29.1 Measuring minimisation

Zara wants to measure whether Pellmore collects only what it needs. She lists, for each purpose, the fields collected and the fields actually needed, agreed with the owners of each process. The booking form collects eight fields but needs five; address, gender and occupation are not needed. Video consultations collect six fields but need four; contacts and location are not needed. The newsletter collects four fields but needs only email. Overall, 8 of 18 collected fields, 44%, are not needed for their purpose. Removing them cuts exposure directly.

### 29.2 Acting on the measure

The minimisation figure leads to changes. Zara removes the unnecessary booking fields, stops collecting phone contacts and location in the video app, and reduces the newsletter sign-up to an email address. She plans to re-measure after a release cycle. She also notes that the measure depends on owners' honest judgement of need: an owner who claims everything is needed would make the figure look good. A second reviewer, the data protection officer, checks each need claim against the purpose description before the figure is reported.

### 29.3 A metric set

Beyond minimisation, Zara defines a small set of privacy metrics: records past retention, flows without complete inventory fields, rights requests answered on time, consent reconciliation mismatches, and access anomalies reviewed within a week. Each has a definition, a data source, an owner and a target. The NIST Privacy Framework encourages organisations to monitor and review privacy risk, and the metric set gives Pellmore a way to do that regularly. She keeps the set small so that people actually read the monthly report.

### 29.4 Metrics without new risk

Measurement can create new privacy risks. A report listing staff with access anomalies could stigmatise innocent people if shared widely. Zara aggregates the report for management and gives named details only to the investigator. Similarly, rights request metrics show counts and timings, not who made requests. She writes a short rule: privacy metrics must themselves follow data minimisation. Prof. Holm calls this the recursive principle of privacy engineering, applying the same care to monitoring data as to the data being monitored. Monitoring logs expire quickly.

### Lab — Fields collected versus needed by purpose

```python
# Data minimisation: fields collected per purpose versus fields the purpose actually needs.
collected = {"booking": {"name", "dob", "phone", "email", "address", "insurer", "gender", "occupation"},
             "video consultation": {"name", "dob", "symptoms", "camera", "location", "contacts"},
             "newsletter": {"email", "name", "dob", "postcode"}}
needed = {"booking": {"name", "dob", "phone", "email", "insurer"},
          "video consultation": {"name", "dob", "symptoms", "camera"},
          "newsletter": {"email"}}
tc = tn = 0
for p in collected:
    extra = sorted(collected[p] - needed[p]); tc += len(collected[p]); tn += len(needed[p])
    print(f"{p:19s} collected {len(collected[p])} needed {len(needed[p])} excess {extra}")
print(f"overall: {tc - tn} of {tc} collected fields ({(tc - tn)/tc:.0%}) are not needed")
```

Run with `python3 lab_minimise.py`. Verified output:

```text
booking             collected 8 needed 5 excess ['address', 'gender', 'occupation']
video consultation  collected 6 needed 4 excess ['contacts', 'location']
newsletter          collected 4 needed 1 excess ['dob', 'name', 'postcode']
overall: 8 of 18 collected fields (44%) are not needed
```

### Worked example

Zara finds 8 of 18 collected fields (44%) are not needed, removes them, defines five privacy metrics with owners and targets, and aggregates metric reports to avoid creating new risks.

> **Synthetic case.** Fields and purposes are synthetic; the NIST Privacy Framework 1.0 is real.

### Errors and limits

Field counts ignore sensitivity; one unnecessary health field may matter more than three contact fields.

### Exercises

- **EX085 — Minimisation result.** What share of collected fields is unnecessary? *Rubric:* 3 = 8 of 18, 44%;; 2 = about four in ten;; 1 = wrong;; 0 = none.
- **EX086 — Need claims.** Why does a second reviewer check need claims? *Rubric:* 3 = owners may overstate need, making the measure look good;; 2 = mentions bias;; 1 = trusts owners;; 0 = none.
- **EX087 — Recursive principle.** What is the recursive principle of privacy engineering? *Rubric:* 3 = monitoring data must also follow privacy principles such as minimisation;; 2 = mentions metrics;; 1 = vague;; 0 = none.

### Synthesis

Chapter 29 measures privacy. Chapter 30 verifies controls in the first laboratory.

### Continue studying — chapter 29 of 50

[← Chapter 28 (draft)](#ch-28) · [Course chapter index](../SUBJECTS.md) · [Chapter 30 (draft) →](#ch-30)

<a id="ch-30"></a>

## Chapter 30 — Verification laboratory I

### Learning outcomes

You will (1) verify privacy controls with tests; (2) design tests from threats; (3) record evidence for accountability.

### 30.1 Tests from threats

In the first verification laboratory Zara turns the threat scenarios from Chapter 23 into tests. For linkability, she checks that analytics events carry recipient-specific pseudonyms and that no two recipients receive the same identifier. For misdirected results, she sends synthetic results with mismatched names and checks that the system blocks them. For staff snooping, she simulates record views without appointments and checks that the anomaly signal fires within a day. Each test has an expected result defined before running, which prevents interpreting results generously afterwards.

### 30.2 Rights tests

Zara tests data subject rights end to end. She creates a synthetic patient, uses the app for a week of fake appointments and messages, then requests access, rectification and erasure. The access export includes all data except chat logs, which are stored by a vendor and not yet integrated. The erasure request removes data from four of five stores, but the analytics store keeps events under the pseudonym. Both failures become defects with owners. She records that end-to-end tests with realistic synthetic patients find gaps that unit tests cannot see.

### 30.3 Evidence

Each test produces evidence: inputs, outputs, date and tester. Zara stores evidence in a versioned folder and summarises results in a table. The accountability principle requires that Pellmore can demonstrate compliance, and test evidence is one of the strongest forms of demonstration. She explains that a statement that erasure works is a claim, while a dated test log showing erasure across all stores is evidence. Prof. Holm asks her to include failing tests in the evidence, because hiding failures would make the folder misleading.

### 30.4 Retesting

After the defects are fixed, Zara repeats the tests. The access export now includes chat logs, and erasure reaches the analytics store. She records both runs, showing the failure and the fix. She also adds the tests to the continuous integration pipeline so that they run on every release. Verification, she concludes, is not a one-off certificate but a habit: privacy properties can break whenever the system changes, and only tests that run regularly catch regressions before they reach patients. Tests run on every release.

### Worked example

Zara turns threats into tests, finds gaps in access (chat logs missing) and erasure (analytics retained), records evidence including failures and adds retests to continuous integration.

> **Synthetic case.** Tests and the synthetic patient are synthetic.

### Errors and limits

Tests verify what they check; untested paths can still fail.

### Exercises

- **EX088 — Expected results.** Why define expected results before running tests? *Rubric:* 3 = to prevent generous interpretation after seeing results;; 2 = mentions bias;; 1 = not needed;; 0 = none.
- **EX089 — Erasure gap.** Which store kept data after erasure in the first run? *Rubric:* 3 = the analytics store, under the pseudonym;; 2 = names analytics;; 1 = vague;; 0 = none.
- **EX090 — Claim versus evidence.** Distinguish a claim from evidence about erasure. *Rubric:* 3 = a claim says it works; evidence is a dated test log across stores;; 2 = mentions logs;; 1 = equates them;; 0 = none.

### Synthesis

Chapter 30 verifies controls. Chapter 31 implements the next generation of features.

### Continue studying — chapter 30 of 50

[← Chapter 29 (draft)](#ch-29) · [Course chapter index](../SUBJECTS.md) · [Chapter 31 (draft) →](#ch-31)

<a id="ch-31"></a>

## Chapter 31 — Privacy and data protection: implementation II

### Learning outcomes

You will (1) implement data portability; (2) integrate a vendor's systems with rights handling; (3) implement privacy-preserving analytics.

### 31.1 Portability

Article 20 of the GDPR gives patients a right to receive data they provided, in a structured, commonly used and machine-readable format, where processing is based on consent or contract and carried out by automated means. Zara implements an export in a documented JSON format with a human-readable summary. She includes appointment history and patient-entered symptoms, and excludes clinicians' notes, which are covered by access rights but not portability. She documents the reasoning, because the boundary between portability and access is a common source of confusion for patients.

### 31.2 Vendor integration

The chat log gap found in the verification laboratory requires integration with the vendor. Zara designs an interface through which Pellmore can request a patient's chat logs and their deletion, with signed confirmations returned. The vendor agrees to the interface as part of its processor obligations under Article 28, which require assisting the controller with data subject rights. She tests the interface with synthetic patients and confirms that deletions are confirmed within the agreed two days, and that the confirmation is stored as evidence.

### 31.3 Analytics redesign

With the analytics SDK removed, Pellmore still needs to know how the app is used. Zara implements a server-side analytics pipeline that receives coarse events with recipient-specific pseudonyms, aggregates them daily and discards raw events after seven days. Dashboards show counts per feature and day, with counts below ten suppressed. She chooses not to collect device identifiers at all. The design gives product managers the information they need while removing the tracking that made the original SDK a high risk in the DPIA.

### 31.4 Code quality

Implementation work increases code size, and Zara reviews quality. She finds duplicated logic for pseudonymisation in three services and consolidates it into the shared library. She adds tests for edge cases such as patients with no appointments and very long chat histories. She also writes documentation for the export format so that patients and other providers can use it. Prof. Holm reminds her that maintainability affects privacy: duplicated logic drifts apart over time, and a forgotten copy can silently break a guarantee that everyone assumes still holds.

### Worked example

Zara implements a JSON portability export, a vendor interface with signed deletion confirmations, server-side analytics with suppression of small counts and consolidates pseudonymisation code.

> **Synthetic case.** Interfaces and data are synthetic; GDPR Articles 20 and 28 are real.

### Errors and limits

Portability formats evolve; version the schema and keep old readers working.

### Exercises

- **EX091 — Portability scope.** What does portability include and exclude in Zara's design? *Rubric:* 3 = includes patient-provided data such as appointments and symptoms; excludes clinicians' notes;; 2 = one part;; 1 = everything;; 0 = none.
- **EX092 — Processor assistance.** Which article obliges the vendor to help with rights requests? *Rubric:* 3 = Article 28;; 2 = mentions contract;; 1 = wrong;; 0 = none.
- **EX093 — Small-count suppression.** Why suppress dashboard counts below ten? *Rubric:* 3 = small counts can point to individuals;; 2 = mentions privacy;; 1 = no reason;; 0 = none.

### Synthesis

Chapter 31 implements more rights and analytics. Chapter 32 studies reliability of erasure.

### Continue studying — chapter 31 of 50

[← Chapter 30 (draft)](#ch-30) · [Course chapter index](../SUBJECTS.md) · [Chapter 32 (draft) →](#ch-32)

<a id="ch-32"></a>

## Chapter 32 — Privacy and data protection: reliability

### Learning outcomes

You will (1) compute the reliability of a multi-store erasure; (2) improve reliability with retries; (3) relate reliability to rights compliance.

### 32.1 Erasure as a series system

Erasure succeeds only if every store deletes the data. In reliability terms, the stores form a series system: the probability of complete erasure is the product of each store's success probability. Zara estimates first-attempt success rates from logs: booking database 0.995, records 0.99, video archive 0.95, analytics 0.90 and the backup deletion flag 0.98. Multiplying gives 0.825, so roughly one request in six would leave data somewhere on the first attempt. She presents this as a reliability problem, not a legal technicality. Each extra system multiplies the chance of a miss, so reducing copies improves reliability as much as fixing any one deletion.

### 32.2 Retries

Many failures are transient: timeouts, locks, temporary network errors. Zara adds one automatic retry per store. If failures are independent, the probability that a store fails twice is the square of its failure probability. With one retry the overall probability of complete erasure rises to 0.987. Expected incomplete erasures per thousand requests fall from 175 to 13. The lab confirms the calculation. She notes that the remaining failures are more likely to be persistent problems, which retries cannot fix and which require alerts. Persistent failures need human follow-up.

### 32.3 Persistent failures

For the remaining failures Zara adds a dead-letter queue: requests that fail after retry are routed to an operator with details of the failing store. The operator investigates and completes the deletion manually, recording the outcome. She sets a target of resolving all such cases within seven days, well inside the one-month response period in Article 12(3). The design turns a silent failure into a visible task, which matters because an erasure that silently fails is worse than a slow one: the patient believes the data are gone.

### 32.4 Independence assumption

The retry calculation assumes independent failures, but failures can be correlated: if the analytics store is down, every request fails there at once. Zara adds monitoring for store availability and pauses erasure for a store during an outage, resuming afterwards. She also tests the system under simulated outages. Prof. Holm explains that reliability engineering for privacy uses the same tools as for safety: series and parallel models, independence checks and fault injection, and that legal rights depend on these technical details. She tests shared dependencies.

### Lab — Reliability of erasure across five stores

```python
# Erasure must reach five stores; each deletion job succeeds with its own probability. Effect of one retry.
stores = {"booking DB": 0.995, "records": 0.99, "video archive": 0.95, "analytics": 0.90, "backups (flag)": 0.98}
p1 = p2 = 1.0
for s, p in stores.items():
    p1 *= p; p2 *= 1 - (1 - p) ** 2
print(f"all five complete on first attempt: {p1:.3f}")
print(f"with one automatic retry per store:  {p2:.3f}")
print(f"expected incomplete erasures per 1,000 requests: {1000*(1-p1):.0f} -> {1000*(1-p2):.0f}")
```

Run with `python3 lab_erasure.py`. Verified output:

```text
all five complete on first attempt: 0.825
with one automatic retry per store:  0.987
expected incomplete erasures per 1,000 requests: 175 -> 13
```

### Worked example

Zara models erasure as a series system with 0.825 first-attempt success, raises it to 0.987 with one retry (175 to 13 incomplete per 1,000), routes persistent failures to operators and guards against correlated outages.

> **Synthetic case.** Success rates are synthetic; GDPR Article 12(3) is real.

### Errors and limits

Logs may overstate success if confirmations are not checked; verify deletion by reading back.

### Exercises

- **EX094 — Series reliability.** Why is complete erasure a series system? *Rubric:* 3 = it succeeds only if every store deletes, so probabilities multiply;; 2 = mentions all stores;; 1 = parallel;; 0 = none.
- **EX095 — Retry effect.** How do expected incomplete erasures change with one retry? *Rubric:* 3 = from 175 to 13 per 1,000;; 2 = direction only;; 1 = wrong;; 0 = none.
- **EX096 — Silent failure.** Why is a silent erasure failure worse than a slow one? *Rubric:* 3 = the patient believes data are gone when they are not;; 2 = mentions trust;; 1 = equal;; 0 = none.

### Synthesis

Chapter 32 engineers reliable erasure. Chapter 33 addresses safety and resilience.

### Continue studying — chapter 32 of 50

[← Chapter 31 (draft)](#ch-31) · [Course chapter index](../SUBJECTS.md) · [Chapter 33 (draft) →](#ch-33)

<a id="ch-33"></a>

## Chapter 33 — Privacy and data protection: safety and resilience

### Learning outcomes

You will (1) plan for incidents that affect personal data; (2) design resilience that preserves privacy; (3) balance availability with confidentiality.

### 33.1 Resilience requirements

Article 32 requires the ability to restore availability and access to personal data in a timely manner after an incident. For telemedicine, unavailability of records during consultations can harm patients. Zara defines recovery objectives with clinicians: clinical records restored within four hours, video service within one hour. She designs backups and failover to meet them, and ensures backup copies are encrypted and access controlled. Resilience, she explains, is a privacy requirement as well as an operational one, because losing access to data harms patients just as disclosure does.

### 33.2 Breaches as incidents

The GDPR defines a personal data breach broadly, including loss of availability. If ransomware encrypts records and they cannot be restored quickly, that is a breach even if no data leave Pellmore. Zara works with the security team to align incident response with breach procedures: every security incident is assessed for personal data impact, and the data protection officer is involved early. EDPB Guidelines 9/2022 describe availability breaches and the assessment of risk, which she uses to train the incident team. Availability loss counts too.

### 33.3 Privacy during recovery

Recovery can create privacy risks. Restoring an old backup could reintroduce data that patients had erased or that were past retention. Zara's recovery runbook therefore reapplies the erasure log and retention table after any restore, before the system returns to service. She also limits who can access backups during recovery, since emergencies tempt teams to share access widely. She tests the runbook in a drill and finds that reapplying erasures takes forty minutes, which she includes in the recovery time objective. Restored backups need erasures replayed.

### 33.4 Graceful degradation

When parts of the platform fail, Zara wants the system to degrade safely. If the consent service is down, systems should treat consent as absent rather than assume it is present. If the access-check service is down, clinicians in a consultation get emergency access with enhanced logging and review afterwards, rather than no access. She documents these fail-safe and break-glass rules and agrees them with clinicians and the data protection officer. Designing failure behaviour in advance prevents improvised decisions during an outage.

### Worked example

Zara sets recovery objectives with clinicians, treats availability loss as a potential breach, reapplies erasures after restores (forty minutes) and defines fail-safe consent and break-glass access.

> **Synthetic case.** Objectives and drills are synthetic; GDPR Article 32 and EDPB Guidelines 9/2022 are real.

### Errors and limits

Break-glass access can be abused; review every use promptly.

### Exercises

- **EX097 — Availability breach.** Can ransomware without exfiltration be a personal data breach? *Rubric:* 3 = yes; loss of availability is a breach;; 2 = yes without reason;; 1 = no;; 0 = none.
- **EX098 — Restore risk.** What privacy risk does restoring a backup create, and how is it handled? *Rubric:* 3 = erased or expired data return; reapply erasure log and retention before service;; 2 = one part;; 1 = vague;; 0 = none.
- **EX099 — Fail-safe consent.** How should systems behave if the consent service is down? *Rubric:* 3 = treat consent as absent;; 2 = mentions caution;; 1 = assume present;; 0 = none.

### Synthesis

Chapter 33 builds resilience. Chapter 34 integrates the platform.

### Continue studying — chapter 33 of 50

[← Chapter 32 (draft)](#ch-32) · [Course chapter index](../SUBJECTS.md) · [Chapter 34 (draft) →](#ch-34)

<a id="ch-34"></a>

## Chapter 34 — Privacy and data protection: integration

### Learning outcomes

You will (1) integrate privacy controls across services; (2) handle partner integrations; (3) test integrated behaviour.

### 34.1 Shared services

By the fourth year Pellmore's privacy capabilities are spread across services: access checks, consent, retention, erasure and analytics. Zara integrates them through a shared privacy platform with clear interfaces. Each product service calls the platform rather than implementing its own logic. Integration reduces duplication and inconsistency, but it creates dependency: if the platform fails, many services are affected. She uses the fail-safe rules from Chapter 33 and runs the platform with high availability, treating it as critical infrastructure rather than a side project.

### 34.2 Laboratory partner

Pellmore's laboratory partner receives test orders and returns results. The partner is a separate controller for its own testing, as Zara determined using EDPB Guidelines 07/2020. Integration must respect both organisations' obligations. Zara designs the interface to send only the data needed for the test: a recipient-specific pseudonym, test type, sample identifier and clinically necessary details. Results return under the same pseudonym and are matched internally. She documents responsibilities in a data sharing agreement, including who answers which rights requests. The agreement is reviewed annually.

### 34.3 End-to-end tests

Zara builds end-to-end tests that cross services and partners using synthetic patients. A test patient books, consults, receives a test order, gets results, requests access and then erasure. The test checks that each step produces the expected data and that erasure reaches every Pellmore store and triggers notifications to the partner for its own handling. The first run reveals that the partner's results message includes the patient's full name in a free-text comment. Pellmore and the partner agree to remove names from comments.

### 34.4 Change control

Integrated systems change constantly. Zara sets a rule that any change to an interface carrying personal data needs a short privacy review and an update to the inventory. She automates detection: a schema comparison flags new fields in interface messages, and the review is triggered automatically. Prof. Holm points out that integration is where many privacy failures appear, because each team assumes another team handles a property, and that automated detection of interface changes reduces the reliance on people remembering to ask.

### Worked example

Zara centralises privacy capabilities in a shared platform, designs a minimal pseudonymised lab interface, finds names in partner comments through end-to-end tests and automates privacy review of interface changes.

> **Synthetic case.** The partner and tests are synthetic; EDPB Guidelines 07/2020 are real.

### Errors and limits

A shared platform concentrates failure; monitor and test its availability.

### Exercises

- **EX100 — Shared platform trade-off.** What is the trade-off of a shared privacy platform? *Rubric:* 3 = less duplication but dependency on one critical service;; 2 = one part;; 1 = no trade-off;; 0 = none.
- **EX101 — Partner role.** Why is the laboratory partner a separate controller? *Rubric:* 3 = it determines purposes and means for its own testing;; 2 = mentions independence;; 1 = processor;; 0 = none.
- **EX102 — Interface detection.** How are interface changes caught for review? *Rubric:* 3 = automated schema comparison flags new fields;; 2 = mentions automation;; 1 = manual only;; 0 = none.

### Synthesis

Chapter 34 integrates the platform. Chapter 35 is the second design studio.

### Continue studying — chapter 34 of 50

[← Chapter 33 (draft)](#ch-33) · [Course chapter index](../SUBJECTS.md) · [Chapter 35 (draft) →](#ch-35)

<a id="ch-35"></a>

## Chapter 35 — Design studio II

### Learning outcomes

You will (1) design a new data use with contextual integrity; (2) consider vulnerable groups; (3) present to a mixed panel.

### 35.1 The brief

The second studio brief asks Zara's team to design a feature that lets family carers help elderly patients manage appointments. Carers need some information but not all, and patients may have reasons to keep some consultations private from relatives. The team must design sharing that respects the patient's wishes. Nissenbaum's contextual integrity guides them: information shared with a clinician carries norms of confidentiality, and moving it to a family member requires the patient's informed choice about what moves and when. Patients choose per category.

### 35.2 Granular sharing

The team designs sharing by category: appointment times, medication reminders and test results can each be shared or not. Consultation notes are never shared by default. Patients choose categories at setup and can change them at any time. The carer sees a clear label of what has been shared. Zara ensures that a sharing setting cannot be changed by the carer, only by the patient or, where the patient lacks capacity, by a legally authorised representative, with that authority verified rather than merely claimed.

### 35.3 Vulnerable patients

The panel raises cases of coercion: a controlling relative might pressure a patient to share everything. The team adds a private review prompt: at random times, when the patient logs in alone, the app asks whether sharing settings still reflect their wishes, with a discreet option to change them. They also train clinicians to ask about sharing during consultations. Zara notes that WP248 lists vulnerable data subjects as a factor in assessing risk, and that design for vulnerable users often improves the experience for everyone.

### 35.4 Panel presentation

The team presents to a panel of a clinician, a carer, a patient representative and an engineer. The patient representative asks for simpler wording; the carer asks for notifications when sharing changes; the clinician asks how emergencies are handled. The team adds plain-language labels and notifications, and clarifies that emergencies follow clinical procedures outside the sharing feature. Zara reflects that a mixed panel catches problems that engineers alone would miss, and that privacy design is strongest when people affected by it help shape it.

### Worked example

Zara's team designs category-based carer sharing guided by contextual integrity, protects patient control, adds private prompts against coercion and refines the design with a mixed panel.

> **Synthetic case.** The feature and panel are synthetic; Nissenbaum (2004) and WP248 rev.01 are real.

### Errors and limits

Prompts can alert a controlling relative if seen; design their appearance carefully.

### Exercises

- **EX103 — Default notes.** Why are consultation notes never shared by default? *Rubric:* 3 = they carry confidentiality norms; moving them needs the patient's explicit choice;; 2 = mentions confidentiality;; 1 = share all;; 0 = none.
- **EX104 — Coercion defence.** What design responds to coercion by relatives? *Rubric:* 3 = private prompts when the patient is alone plus clinician questions;; 2 = one part;; 1 = vague;; 0 = none.
- **EX105 — Who changes settings.** Who may change sharing settings? *Rubric:* 3 = the patient, or a verified legal representative where the patient lacks capacity;; 2 = patient only;; 1 = carer;; 0 = none.

### Synthesis

Chapter 35 designs for relationships. Chapter 36 considers scale and differential privacy budgets.

### Continue studying — chapter 35 of 50

[← Chapter 34 (draft)](#ch-34) · [Course chapter index](../SUBJECTS.md) · [Chapter 36 (draft) →](#ch-36)

<a id="ch-36"></a>

## Chapter 36 — Privacy and data protection: performance and scale

### Learning outcomes

You will (1) plan a differential privacy budget for repeated releases; (2) understand accuracy at scale; (3) choose release frequency.

### 36.1 Publishing clinic statistics

Pellmore wants to publish clinic waiting-time and diagnosis statistics for public health partners. Zara proposes differential privacy for the published counts. Dwork and Roth (2014) explain that privacy loss accumulates across releases under composition, so a yearly budget must be shared among all releases. She sets an illustrative yearly epsilon of three for a family of counts and asks how frequently Pellmore can publish while keeping useful accuracy. The question links scale and performance to privacy: more releases mean more noise per release.

### 36.2 The budget lab

The lab divides the yearly budget equally among releases and computes the Laplace error for a count with sensitivity one. Monthly releases get epsilon 0.25 each and a mean absolute error of 4.0 per count. Weekly releases get epsilon 0.0577 and error 17.3. Daily releases get epsilon 0.0082 and error 121.7, which would swamp most clinic counts. Zara recommends monthly publication. She explains to partners that daily figures would look precise but mostly show noise, which would mislead rather than inform public health decisions. Weekly releases spend the budget more wisely.

### 36.3 Scale effects

Larger counts tolerate noise better. A national total of thousands is barely affected by an error of four, while a rural clinic's count of twenty changes visibly. Zara proposes publishing at regional level for rare diagnoses and clinic level for common ones. She also explains that the budget applies per person: if each person contributes to many counts, sensitivity rises. She limits each patient's contribution per release to one count, which keeps sensitivity at one and makes the error figures in the lab valid.

### 36.4 Engineering the pipeline

Zara implements a release pipeline that tracks budget spent, refuses releases that would exceed the yearly budget and logs each release with its epsilon. Post-processing rounds noisy counts and replaces negative values with zero, which does not weaken the guarantee. She writes a short public note explaining the method. Prof. Holm reminds the class that implementations of differential privacy can fail through subtle bugs, such as poor random number generation, so the pipeline uses a vetted library and independent review. Seeds are never fixed in production.

### Lab — Splitting a yearly privacy budget across releases

```python
# Differential privacy budget for daily clinic dashboards: per-release epsilon and Laplace error under a yearly budget.
yearly = 3.0
for releases in [12, 52, 365]:
    eps = yearly / releases
    print(f"{releases:3d} releases/year: epsilon per release {eps:.4f}; mean abs error per count {1/eps:7.1f}")
```

Run with `python3 lab_budget.py`. Verified output:

```text
 12 releases/year: epsilon per release 0.2500; mean abs error per count     4.0
 52 releases/year: epsilon per release 0.0577; mean abs error per count    17.3
365 releases/year: epsilon per release 0.0082; mean abs error per count   121.7
```

### Worked example

Zara splits a yearly epsilon of 3 across releases: monthly gives error 4.0 per count, weekly 17.3 and daily 121.7, so she recommends monthly publication with regional aggregation for rare diagnoses.

> **Synthetic case.** The budget and counts are illustrative; Dwork and Roth (2014) is real.

### Errors and limits

Simple composition is conservative; advanced accounting gives tighter bounds but needs expertise.

### Exercises

- **EX106 — Daily error.** What error would daily releases have? *Rubric:* 3 = 121.7 per count;; 2 = over a hundred;; 1 = wrong;; 0 = none.
- **EX107 — Contribution limit.** Why limit each patient to one count per release? *Rubric:* 3 = keeps sensitivity at one so error figures hold;; 2 = mentions sensitivity;; 1 = vague;; 0 = none.
- **EX108 — Safe post-processing.** Does rounding and clamping noisy counts weaken the guarantee? *Rubric:* 3 = no; post-processing does not weaken differential privacy;; 2 = no without reason;; 1 = yes;; 0 = none.

### Synthesis

Chapter 36 plans releases at scale. Chapter 37 runs privacy in operations.

### Continue studying — chapter 36 of 50

[← Chapter 35 (draft)](#ch-35) · [Course chapter index](../SUBJECTS.md) · [Chapter 37 (draft) →](#ch-37)

<a id="ch-37"></a>

## Chapter 37 — Privacy and data protection: operations

### Learning outcomes

You will (1) run privacy operations day to day; (2) handle rights requests at volume; (3) operate monitoring and response.

### 37.1 A privacy operations function

By now Pellmore's privacy controls need daily operation. Zara helps set up a small privacy operations function in the data protection officer's team. It handles rights requests, reviews access anomalies, monitors retention and consent reconciliation, and coordinates with security on incidents. She writes runbooks for each task with steps, tools and escalation routes. The function reports monthly using the metric set from Chapter 29. Operations, she notes, are where designs either work as intended or quietly decay over time. Its staff own every runbook.

### 37.2 Rights at volume

Pellmore now receives about two hundred rights requests a month. Zara automates identity checks through account login, data collection through the privacy platform and deadline tracking with alerts at twenty and twenty-five days. Complex requests, such as those involving several family members, go to a specialist. She measures on-time completion and finds that 97% of requests are answered within thirty days. EDPB Guidelines 01/2022 on access inform the process, including how to handle requests from third parties acting for a patient. Requests are logged with deadlines.

### 37.3 Monitoring

Anomaly signals for access are reviewed daily. In the first month the team reviews thirty alerts; twenty-six are legitimate, such as covering colleagues, and four lead to conversations about access need. One case is a clinician viewing a relative's record, which is handled under Pellmore's disciplinary policy and recorded as a potential breach for assessment. Zara adjusts thresholds to reduce false alarms without missing such cases. She learns that monitoring works only when reviews are prompt and fair to staff. Reviews happen within days.

### 37.4 Continuous improvement

Each quarter the privacy operations team reviews incidents, metrics and complaints and proposes improvements. Zara facilitates the first review. The team finds that postal rights requests are still slow and that a confusing notice causes many questions. They propose a scanning workflow and a rewritten notice section. ISO/IEC 27701:2025, structured as a management system standard, expects such cycles of monitoring, review and improvement. She notes that the cycle keeps privacy alive as an operating discipline rather than a project that ends. ISO/IEC 27701 builds on this cycle.

### Worked example

Zara sets up privacy operations with runbooks, automates rights requests to 97% on time, reviews thirty access alerts including one relative-snooping case and runs a quarterly improvement review.

> **Synthetic case.** Volumes and cases are synthetic; EDPB Guidelines 01/2022 and ISO/IEC 27701:2025 are real.

### Errors and limits

Automation can mis-identify requesters; keep a manual route for edge cases.

### Exercises

- **EX109 — On-time rate.** What share of rights requests was answered on time? *Rubric:* 3 = 97%;; 2 = nearly all;; 1 = wrong;; 0 = none.
- **EX110 — Relative's record.** How is a clinician viewing a relative's record handled? *Rubric:* 3 = disciplinary process and assessment as a potential breach;; 2 = one part;; 1 = ignored;; 0 = none.
- **EX111 — Management cycle.** What does the quarterly review provide? *Rubric:* 3 = a monitor-review-improve cycle expected of a management system;; 2 = mentions improvement;; 1 = vague;; 0 = none.

### Synthesis

Chapter 37 operates privacy. Chapter 38 validates that the system meets real needs.

### Continue studying — chapter 37 of 50

[← Chapter 36 (draft)](#ch-36) · [Course chapter index](../SUBJECTS.md) · [Chapter 38 (draft) →](#ch-38)

<a id="ch-38"></a>

## Chapter 38 — Privacy and data protection: validation

### Learning outcomes

You will (1) distinguish verification from validation; (2) validate privacy features with patients; (3) validate legal assumptions with experts.

### 38.1 Verification and validation

Verification asks whether the system meets its requirements; validation asks whether the requirements meet real needs. Zara's tests verified that erasure reaches every store. Validation asks whether patients understand erasure and get what they expect. She interviews twelve synthetic-scenario participants, volunteers who use test accounts. Several expect erasure to remove their medical record entirely, which health law does not allow. The validation reveals a gap in explanation, not in engineering, and leads to clearer wording in the erasure screen. Patients tested the new screen.

### 38.2 Usability of privacy

Zara runs usability tests of the privacy dashboard. Participants try to find who has seen their record, change sharing settings and download their data. Most succeed, but finding the access history takes too long. She moves it to the dashboard's first screen. She measures task time before and after and reports the improvement. Privacy controls that people cannot find or use, she explains, provide little real protection, and transparency obligations in Article 12 imply that people must actually be able to use what is offered.

### 38.3 Legal validation

Zara's designs rest on legal assumptions: that portability excludes clinicians' notes, that the laboratory partner is a separate controller, that retention of medical records overrides erasure. She asks Pellmore's counsel to validate each assumption and record the reasoning. Counsel confirms most but refines one: some patient-entered symptom notes are part of the medical record and must be retained, so erasure must exclude them. Zara updates the erasure requirements. She learns that legal assumptions should be validated explicitly, not inherited from earlier projects.

### 38.4 Validating with the supervisory context

Zara also reviews published decisions and guidance from supervisory authorities on telemedicine, to check that Pellmore's approach is consistent with how regulators interpret the law. She records relevant guidance in a short brief for the data protection officer. She does not treat any single decision as binding for Pellmore, but she uses them to identify risks the team had not considered, such as the treatment of video recordings. Validation, she concludes, looks outward to people, lawyers and regulators, while verification looks inward to requirements.

### Worked example

Zara validates erasure expectations with participants, improves access-history usability, has counsel validate legal assumptions (refining symptom-note retention) and briefs the DPO on regulatory guidance.

> **Synthetic case.** Participants and counsel are synthetic; GDPR Article 12 is real.

### Errors and limits

Small validation groups may not represent all patients; recruit diverse participants.

### Exercises

- **EX112 — V and V.** Distinguish verification from validation. *Rubric:* 3 = verification checks requirements are met; validation checks requirements meet real needs;; 2 = one;; 1 = confuses;; 0 = none.
- **EX113 — Erasure expectation.** What did validation reveal about erasure? *Rubric:* 3 = patients expected full medical record removal, which law prevents; explanation needed;; 2 = mentions expectation;; 1 = vague;; 0 = none.
- **EX114 — Refined assumption.** Which legal assumption did counsel refine? *Rubric:* 3 = some patient-entered symptom notes are part of the medical record and must be kept;; 2 = mentions notes;; 1 = vague;; 0 = none.

### Synthesis

Chapter 38 validates outward. Chapter 39 keeps the system maintainable.

### Continue studying — chapter 38 of 50

[← Chapter 37 (draft)](#ch-37) · [Course chapter index](../SUBJECTS.md) · [Chapter 39 (draft) →](#ch-39)

<a id="ch-39"></a>

## Chapter 39 — Privacy and data protection: maintainability

### Learning outcomes

You will (1) keep privacy controls maintainable; (2) manage technical debt with privacy impact; (3) document for future engineers.

### 39.1 Privacy debt

Technical debt accumulates when shortcuts are taken. Zara defines privacy debt as shortcuts that weaken privacy: temporary data copies, disabled checks, undocumented flows. She creates a register of privacy debt items with owners and repayment dates. The register reveals a temporary export created for a regulator's question two years earlier that was never removed. She deletes it. She explains that privacy debt is especially dangerous because, unlike performance debt, its costs appear only when harm occurs or an audit asks questions. She tracks it in the backlog.

### 39.2 Readable controls

Controls must be understandable to future engineers. Zara rewrites the access policy configuration with comments explaining each rule and its legal or clinical reason. She adds diagrams to the privacy platform documentation. She also writes architecture decision records for the major choices of the past two years, so that new engineers do not undo protections through misunderstanding. Prof. Holm notes that maintainability is a precondition for accountability, because an organisation that cannot explain its own controls cannot demonstrate compliance. Code comments cite the requirement each control satisfies.

### 39.3 Dependency updates

The privacy platform depends on libraries for cryptography, differential privacy and messaging. Zara sets up automated dependency checks and a policy for updating them. She tests updates against the privacy test suite before deployment. An update to the messaging library once changed retry behaviour, which would have affected erasure reliability. The test suite caught it. She records the event as evidence that the tests protect against regressions introduced by third-party code, not only by Pellmore's own engineers. A library upgrade had silently changed the default log level, and the privacy unit test failed on the first build.

### 39.4 Handover

As Zara's placement nears its end, she prepares a handover. Each control has an owner, documentation, tests and metrics. She runs walkthroughs with the engineers who will maintain the platform. She also lists open risks and the privacy debt register. Pellmore's engineering lead signs off the handover. Zara reflects that good maintainability is invisible when it works: nobody notices that a control still functions after two years, but they would notice quickly, and painfully, if it had silently decayed. Ownership must therefore be explicit.

### Worked example

Zara creates a privacy debt register (deleting a two-year-old temporary export), documents controls with reasons, catches a messaging library regression with tests and hands over with owners and open risks.

> **Synthetic case.** Debt items and the library change are synthetic.

### Errors and limits

Debt registers need regular review or they become lists nobody reads.

### Exercises

- **EX115 — Privacy debt.** Define privacy debt. *Rubric:* 3 = shortcuts that weaken privacy, such as temporary copies or disabled checks;; 2 = example only;; 1 = technical debt in general;; 0 = none.
- **EX116 — Library regression.** What did the test suite catch after a library update? *Rubric:* 3 = changed retry behaviour affecting erasure reliability;; 2 = mentions erasure;; 1 = vague;; 0 = none.
- **EX117 — Maintainability and accountability.** Why is maintainability a precondition for accountability? *Rubric:* 3 = an organisation that cannot explain its controls cannot demonstrate compliance;; 2 = mentions explanation;; 1 = unrelated;; 0 = none.

### Synthesis

Chapter 39 keeps controls healthy. Chapter 40 is the second verification laboratory.

### Continue studying — chapter 39 of 50

[← Chapter 38 (draft)](#ch-38) · [Course chapter index](../SUBJECTS.md) · [Chapter 40 (draft) →](#ch-40)

<a id="ch-40"></a>

## Chapter 40 — Verification laboratory II

### Learning outcomes

You will (1) verify privacy properties under adversarial testing; (2) commission independent testing; (3) report verification results to management.

### 40.1 Adversarial testing

In the second verification laboratory Zara's class acts as adversaries against a test copy of Pellmore's platform with synthetic data. They try to link analytics data back to patients, to obtain another patient's records through the carer feature and to infer diagnoses from published statistics. Linkage fails because recipient pseudonyms differ. The carer attack fails because settings require patient authentication. The statistics attack succeeds partly for one rural clinic, where small counts were published before the differential privacy pipeline was introduced. Older outputs were never reviewed.

### 40.2 Fixing the statistics leak

The rural clinic leak comes from old reports still on a public page. Zara removes them and checks that the new pipeline covers all published statistics. She also searches for other legacy publications and finds two more. The finding shows that new protections do not automatically fix old outputs. She adds a rule: when a new protection is introduced, the team must search for outputs produced under the old approach and decide whether to remove, replace or keep them with justification. Here, the old table is withdrawn.

### 40.3 Independent testing

Pellmore commissions an independent firm to test the platform. The firm receives the same synthetic environment and scope. It finds one issue the class missed: a support tool leaks patient email addresses in an autocomplete field. Pellmore fixes it. Zara notes that independent testers bring different habits and assumptions, which is why independent assessment is valuable even after strong internal testing. She records the finding and the fix in the evidence folder alongside the class's results. The support tool is restricted to masked addresses, and a regression test is added so the leak cannot quietly return.

### 40.4 Reporting to management

Zara writes a verification report for Pellmore's management: what was tested, what passed, what failed and what was fixed, with remaining risks. She avoids technical detail in the summary and attaches evidence for specialists. Management asks whether the platform is secure; she answers that it passed the tests described, that two issues were fixed and that testing will continue each year. She explains that verification reduces uncertainty but cannot prove the absence of all problems, and management accepts the framing. Testing is scheduled yearly.

### Worked example

Zara's class attacks the platform: linkage and carer attacks fail, a statistics attack exposes legacy rural clinic reports; an independent firm finds an autocomplete email leak; she reports results with remaining risks.

> **Synthetic case.** Attacks run only on synthetic test copies.

### Errors and limits

Passing tests do not prove absence of vulnerabilities.

### Exercises

- **EX118 — Partial success.** Which adversarial attack partly succeeded, and why? *Rubric:* 3 = statistics inference for a rural clinic via legacy small-count reports;; 2 = mentions rural clinic;; 1 = vague;; 0 = none.
- **EX119 — Legacy outputs rule.** What rule did Zara add after the statistics leak? *Rubric:* 3 = search for outputs from the old approach whenever a new protection is introduced;; 2 = mentions legacy;; 1 = vague;; 0 = none.
- **EX120 — Independent value.** Why commission independent testing after strong internal tests? *Rubric:* 3 = different habits find different issues, e.g. the autocomplete leak;; 2 = mentions independence;; 1 = unnecessary;; 0 = none.

### Synthesis

Chapter 40 closes the verification cycle. Chapter 41 optimises the system.

### Continue studying — chapter 40 of 50

[← Chapter 39 (draft)](#ch-39) · [Course chapter index](../SUBJECTS.md) · [Chapter 41 (draft) →](#ch-41)

<a id="ch-41"></a>

## Chapter 41 — Privacy and data protection: system optimization

### Learning outcomes

You will (1) optimise for privacy and utility together; (2) remove redundant processing; (3) measure the effect of optimisation.

### 41.1 Optimisation goals

In the final year Zara looks for ways to improve Pellmore's platform as a whole. She defines goals: reduce personal data held, reduce processing steps that touch identifiable data, and keep or improve service quality. She measures the current state: total identifiable records, number of services with access to clinical data and median time to answer rights requests. Defining measurable goals first prevents optimisation from becoming a vague clean-up, and it lets her report progress in numbers that managers and the data protection officer can check.

### 41.2 Removing redundancy

Zara traces processing paths and finds redundancy: three services each keep a cache of patient names for display. She replaces the caches with a single name service that returns names only to authorised callers. She also finds that video recordings are transcoded into two formats, both stored. Only one is used. Removing the second format halves video storage. Each change reduces exposure without harming service, which she presents as the easiest kind of privacy improvement, often hidden in systems that grew without a plan.

### 41.3 Trade-offs

Some optimisations involve trade-offs. Shortening chat log retention from a year to six months reduces exposure but may hinder clinical follow-up. Zara asks clinicians, who agree that six months is enough for most cases, with an option to keep specific logs in the medical record when clinically relevant. She documents the decision with the reasoning. She notes that optimisation in privacy is rarely a pure technical exercise, because the right setting often depends on clinical and legal judgement that engineers must seek rather than assume.

### 41.4 Measuring the effect

After three months Zara measures again. Identifiable records have fallen by about a third, services with clinical access have fallen from eleven to six and rights requests are answered faster because data are in fewer places. She reports the results with their uncertainty and notes which changes contributed most. Prof. Holm points out that improvements in privacy often improve other qualities too, such as cost and performance, which helps privacy engineers win support for further work across the organisation. Storage costs fell noticeably too.

### Worked example

Zara sets measurable optimisation goals, removes duplicate name caches and an unused video format, shortens chat retention with clinicians' agreement and measures a one-third fall in identifiable records.

> **Synthetic case.** Figures are synthetic.

### Errors and limits

Before-and-after comparisons can include unrelated changes; note other events in the period.

### Exercises

- **EX121 — Name caches.** How did Zara remove redundant name caches? *Rubric:* 3 = replaced three caches with one name service for authorised callers;; 2 = mentions caches;; 1 = vague;; 0 = none.
- **EX122 — Clinical trade-off.** How was chat log retention shortened safely? *Rubric:* 3 = clinicians agreed to six months with the option to keep logs in the record when relevant;; 2 = mentions clinicians;; 1 = vague;; 0 = none.
- **EX123 — Services with access.** How did the number of services with clinical access change? *Rubric:* 3 = from eleven to six;; 2 = direction only;; 1 = wrong;; 0 = none.

### Synthesis

Chapter 41 optimises the system. Chapter 42 turns to applied research.

### Continue studying — chapter 41 of 50

[← Chapter 40 (draft)](#ch-40) · [Course chapter index](../SUBJECTS.md) · [Chapter 42 (draft) →](#ch-42)

<a id="ch-42"></a>

## Chapter 42 — Privacy and data protection: applied research

### Learning outcomes

You will (1) frame an applied research question from engineering practice; (2) review evidence; (3) design a small study.

### 42.1 The question

Zara's applied research module asks her to investigate a question from practice. She chooses: do patients understand the carer sharing feature well enough to make informed choices? The question matters because consent and control depend on understanding. She frames it as a study of comprehension: after setting up sharing, can participants correctly state what their carer can see? She defines success as at least eighty per cent correct answers, set before collecting data, and explains her threshold choice in the study plan.

### 42.2 Evidence

Zara reviews research on privacy decision-making. Acquisti, Brandimarte and Loewenstein (2015) describe uncertainty, context dependence and malleability of privacy preferences. Research on privacy notices has found that people rarely read long policies. She notes that the evidence supports short, contextual explanations and testing comprehension directly rather than assuming it. She also looks for guidance on informed consent, using EDPB Guidelines 05/2020 to understand what informed means in law, and compares it with the practical comprehension measure she plans to use. Law and comprehension are compared side by side.

### 42.3 Study design

The study uses thirty volunteers with synthetic test accounts. Each sets up sharing for a scenario and then answers five questions about what the carer can see. Zara compares two versions of the setup screen: the current one and one with a preview showing exactly what the carer will see. Participants are assigned randomly. She keeps the study small and low-risk, with ethics approval from Corwen, no real health data and the right to withdraw. She pre-registers the analysis comparing comprehension between versions.

### 42.4 Results and use

Comprehension with the current screen is 71% correct; with the preview, 90%. The difference supports adopting the preview. Zara reports the result with caveats: a small sample, volunteers who may be more confident with apps than average patients, and scenarios rather than real relationships. Pellmore adopts the preview and plans to monitor sharing changes after setup as a real-world signal. She reflects that applied research can be small and still useful when it answers a specific design question with a pre-stated criterion. The criterion was set beforehand.

### Worked example

Zara asks whether patients understand carer sharing, randomises thirty volunteers between screens and finds 71% versus 90% comprehension, leading Pellmore to adopt a preview.

> **Synthetic case.** The study is synthetic; Acquisti et al. (2015) and EDPB Guidelines 05/2020 are real.

### Errors and limits

Volunteers may not represent patients with low digital confidence.

### Exercises

- **EX124 — Success criterion.** What criterion did Zara set before the study? *Rubric:* 3 = at least 80% correct comprehension;; 2 = mentions threshold;; 1 = vague;; 0 = none.
- **EX125 — Preview effect.** What comprehension did the two screens achieve? *Rubric:* 3 = 71% current, 90% preview;; 2 = one number;; 1 = wrong;; 0 = none.
- **EX126 — Study caveat.** Name one caveat on the comprehension result. *Rubric:* 3 = small sample, confident volunteers or scenarios not real relationships;; 2 = vague caveat;; 1 = minimal attempt;; 0 = none.

### Synthesis

Chapter 42 studies understanding. Chapter 43 reflects on practice.

### Continue studying — chapter 42 of 50

[← Chapter 41 (draft)](#ch-41) · [Course chapter index](../SUBJECTS.md) · [Chapter 43 (draft) →](#ch-43)

<a id="ch-43"></a>

## Chapter 43 — Industry or public-service practice

### Learning outcomes

You will (1) work within an organisation's privacy governance; (2) handle conflicting stakeholder demands; (3) reflect on professional practice.

### 43.1 Working in governance

Zara spends a term inside Pellmore's privacy team as a junior engineer. She attends the privacy steering group where the data protection officer, engineering, clinical and commercial leaders meet. She learns that decisions balance legal duties, patient trust, clinical needs and business goals. Her role is to explain technical options and their consequences clearly. She sees that engineers who present options with evidence and trade-offs are listened to more than those who only say what cannot be done, and she adjusts her own style accordingly.

### 43.2 Conflicting demands

The commercial team proposes sharing aggregated usage data with an insurer partner. The data protection officer worries about re-identification and purpose compatibility. Zara analyses the request: the insurer wants clinic-level usage by condition. She shows that small conditions in small clinics could identify patients, and proposes publishing only differentially private aggregates at regional level under the existing release budget. The insurer accepts the regional data. The steering group records the decision. She learns that technical alternatives can often resolve apparent conflicts. The insurer had wanted record-level data.

### 43.3 Professional conduct

During the term Zara is asked by a manager to quickly pull a patient's full history to answer a complaint. She checks the purpose and confirms that the complaints process allows access to the relevant records only. She retrieves only what is needed and records the access. The manager is initially impatient but accepts the process. She reflects that professional conduct in privacy often consists of small acts of discipline under time pressure, which together build an organisation's culture more than policies do.

### 43.4 Reflection

At the end of the term Zara writes a reflective report. She notes that she underestimated how much of privacy work is communication and negotiation, and overestimated how often purely technical problems arise. She also notes that the data protection officer's independence, protected by Article 38 of the GDPR, gave the steering group a voice that commercial pressure could not easily override. Prof. Holm encourages her to keep reflecting in her career, because practice changes faster than any course can predict. She keeps a reflective log.

### Worked example

Zara works in Pellmore's privacy governance, resolves an insurer data request with regional differentially private aggregates, retrieves only necessary records for a complaint and reflects on communication and the DPO's independence.

> **Synthetic case.** The steering group and requests are synthetic; GDPR Article 38 is real.

### Errors and limits

One placement shows one organisation's culture; others differ.

### Exercises

- **EX127 — Insurer request.** How was the insurer request resolved? *Rubric:* 3 = regional differentially private aggregates within the release budget;; 2 = mentions aggregates;; 1 = full sharing;; 0 = none.
- **EX128 — Complaint access.** How did Zara handle the request for a full patient history? *Rubric:* 3 = checked purpose, retrieved only relevant records and logged access;; 2 = mentions purpose;; 1 = gave all;; 0 = none.
- **EX129 — DPO independence.** Why did the DPO's independence matter in the steering group? *Rubric:* 3 = it gave a voice commercial pressure could not easily override;; 2 = mentions independence;; 1 = irrelevant;; 0 = none.

### Synthesis

Chapter 43 places Zara in practice. Chapter 44 starts the capstone.

### Continue studying — chapter 43 of 50

[← Chapter 42 (draft)](#ch-42) · [Course chapter index](../SUBJECTS.md) · [Chapter 44 (draft) →](#ch-44)

<a id="ch-44"></a>

## Chapter 44 — Engineering capstone I

### Learning outcomes

You will (1) scope an engineering capstone in privacy; (2) set requirements and acceptance criteria; (3) plan risk and verification.

### 44.1 Capstone scope

Zara's capstone project is to design and build a privacy-preserving research data service for Pellmore. Researchers should be able to analyse consultation outcomes without receiving identifiable records. The service must support approved studies, enforce purpose and time limits, and publish only safe outputs. She limits the scope to one type of analysis, outcome counts and rates by condition and region, so that the project can be completed and verified properly within the year rather than spread thinly across many features. Narrow scope allows deep verification.

### 44.2 Requirements

Zara writes requirements: analyses run inside the service, never on exported records; each study has an approved protocol with an expiry date; outputs pass automatic checks for small counts and are released with differential privacy where they will be published; every query is logged; and patients who opted out of research are excluded. She traces each requirement to GDPR provisions on research safeguards in Article 89 and to the LGPD's provisions on research bodies, recording which requirements are legal duties and which are design choices.

### 44.3 Risks

Zara lists capstone risks: researchers combining outputs to reconstruct individuals, implementation bugs in noise generation, opt-out lists not synchronised, and scope creep from researchers wanting record-level access. For each she defines controls and tests. For reconstruction she uses the release budget from Chapter 36 per study. For opt-outs she reuses the consent service. She also lists project risks, such as delays in approval, and schedules buffer time, because a capstone that runs late tends to cut verification first. The approval risk is mitigated by booking the ethics committee early.

### 44.4 Verification plan

Zara plans verification before building. Tests will check that no query returns records, that small counts are blocked, that budget limits stop excess queries, that opt-outs are excluded and that expired studies cannot run. An independent classmate will attempt reconstruction attacks. She sets acceptance criteria: all tests pass and the attack recovers no individual's data. Prof. Holm approves the plan, noting that defining verification first is the best protection against a capstone that works in demonstrations but fails under real use. Test cases precede code.

### Worked example

Zara scopes a research data service for outcome counts, writes requirements traced to GDPR Article 89 and LGPD, lists technical and project risks and plans verification with acceptance criteria.

> **Synthetic case.** The service is synthetic; GDPR Article 89 and the LGPD are real.

### Errors and limits

Narrow scope limits usefulness; plan extensions after verification.

### Exercises

- **EX130 — Capstone limit.** Why limit the capstone to outcome counts and rates? *Rubric:* 3 = to complete and verify properly within the year;; 2 = mentions time;; 1 = broad scope;; 0 = none.
- **EX131 — Reconstruction control.** How does the design limit reconstruction attacks? *Rubric:* 3 = a per-study differential privacy budget;; 2 = mentions noise;; 1 = vague;; 0 = none.
- **EX132 — Verification first.** Why plan verification before building? *Rubric:* 3 = it prevents a system that only works in demonstrations;; 2 = mentions quality;; 1 = after;; 0 = none.

### Synthesis

Chapter 44 plans the capstone. Chapter 45 holds an independent design review.

### Continue studying — chapter 44 of 50

[← Chapter 43 (draft)](#ch-43) · [Course chapter index](../SUBJECTS.md) · [Chapter 45 (draft) →](#ch-45)

<a id="ch-45"></a>

## Chapter 45 — Independent design review

### Learning outcomes

You will (1) prepare a design for independent review; (2) respond to findings; (3) record decisions after review.

### 45.1 Preparing the review

Before building, Zara submits her capstone design to an independent review panel: a privacy engineer from another company, a researcher and the data protection officer. She provides architecture diagrams, requirements, risk analysis and the verification plan. She also lists her own doubts, such as whether regional aggregation is enough for rare conditions. Prof. Holm explains that admitting doubts helps reviewers focus on real weaknesses rather than hunting for basic errors, and makes the review more useful to everyone involved. Her reviewers receive the code in advance.

### 45.2 Findings

The panel raises four findings. The researcher says that outcome rates for rare conditions will be too noisy to be useful at regional level. The privacy engineer says that the query log contains researchers' queries, which may reveal sensitive research interests and must be protected. The data protection officer asks how patients will be informed about research use. The engineer also notes that the opt-out check runs at query time, so a patient who opts out mid-study may still appear in cached intermediate results.

### 45.3 Responses

Zara responds to each finding. For rare conditions she allows national aggregation and a longer accumulation period, trading timeliness for accuracy. She restricts query log access to auditors. She adds a section to the privacy notice and a public register of approved studies. For opt-outs she removes caching of intermediate results and reruns studies from scratch at each release. She records which findings changed the design and which she accepted as residual risks with reasons, so that later reviewers can see the logic of every decision.

### 45.4 After review

The panel accepts the revised design. Zara notes that the opt-out finding was the most important, because it concerned a patient's right to object that her design would have quietly undermined. She also learns that reviewers with different backgrounds find different problems: the researcher focused on usefulness, the engineer on technical leaks and the data protection officer on transparency. She adds independent review as a standard step for any new data service at Pellmore and offers to serve on future panels. Panels meet quarterly.

### Worked example

Zara's design review raises rare-condition noise, sensitive query logs, transparency and cached opt-outs; she responds with national aggregation, restricted logs, a public study register and no caching.

> **Synthetic case.** The panel is synthetic.

### Errors and limits

Review panels can miss issues outside their expertise; combine with testing.

### Exercises

- **EX133 — Opt-out cache.** What was the cached opt-out problem? *Rubric:* 3 = patients opting out mid-study could remain in cached intermediate results;; 2 = mentions cache;; 1 = vague;; 0 = none.
- **EX134 — Query log sensitivity.** Why protect the query log? *Rubric:* 3 = queries reveal researchers' sensitive interests;; 2 = mentions privacy;; 1 = unnecessary;; 0 = none.
- **EX135 — Rare conditions.** How did Zara handle rare-condition noise? *Rubric:* 3 = national aggregation and longer accumulation periods;; 2 = one part;; 1 = ignore;; 0 = none.

### Synthesis

Chapter 45 strengthens the design. Chapter 46 builds and tests it.

### Continue studying — chapter 45 of 50

[← Chapter 44 (draft)](#ch-44) · [Course chapter index](../SUBJECTS.md) · [Chapter 46 (draft) →](#ch-46)

<a id="ch-46"></a>

## Chapter 46 — Engineering capstone II

### Learning outcomes

You will (1) build the research data service; (2) verify it against acceptance criteria; (3) evaluate it with researchers.

### 46.1 Building

Zara builds the service in three months. Analyses run as approved query templates inside an isolated environment. The output checker blocks counts below ten and applies differential privacy to published outputs using the study's budget. The consent service supplies opt-outs at each run. Study approvals carry expiry dates checked at query time. She implements the system with small, tested components and reuses the privacy platform where possible, which shortens development and means that improvements to shared components also benefit the research service.

### 46.2 Verification

Zara runs the planned tests. All pass except one: an expired study can still run if its expiry date was set in a different time zone format. She fixes the date handling and reruns. The independent classmate attempts reconstruction by issuing overlapping queries within the budget. The attack recovers no individual's data, because each output is noisy and the budget stops further queries. She records all results in the evidence folder, including the initial failure, so the record shows exactly how the acceptance criteria were met.

### 46.3 Evaluation with researchers

Three researchers use the service for a pilot study on follow-up consultations. They find the template approach restrictive but workable. They ask for one more template type, which Zara adds after review. The national figures for rare conditions are useful, though less timely than they wanted. She records their feedback. The evaluation confirms that the service supports real analysis without record-level access, which is the capstone's central claim, while also showing the limits that remain for exploratory research. Their feedback is recorded verbatim.

### 46.4 Reflection

Zara reflects on the capstone. The hardest problems were not algorithms but edge cases: time zones, caching and opt-out timing. Independent review and testing found them before they harmed anyone. She notes that the service will need monitoring for budget use, opt-out synchronisation and template changes. Prof. Holm comments that her capstone shows mature engineering because she chose a narrow scope, verified it thoroughly and was honest about the limits that remain for researchers who want more flexibility. She documents what the scope deliberately excluded.

### Worked example

Zara builds the service with templates, output checks and budgets, fixes an expiry time-zone bug, withstands a reconstruction attempt and evaluates it with three researchers.

> **Synthetic case.** The service, tests and researchers are synthetic.

### Errors and limits

Template systems can be extended unsafely; review each new template.

### Exercises

- **EX136 — Expiry bug.** What test failed in verification? *Rubric:* 3 = an expired study could run due to a time-zone date format;; 2 = mentions expiry;; 1 = vague;; 0 = none.
- **EX137 — Attack result.** What did the reconstruction attack recover? *Rubric:* 3 = nothing about any individual, because noise and the budget stopped it;; 2 = nothing, without the reason;; 1 = partial;; 0 = no answer.
- **EX138 — Researcher view.** How did researchers judge the template approach? *Rubric:* 3 = restrictive but workable; asked for one more template;; 2 = mentions restriction;; 1 = ideal;; 0 = none.

### Synthesis

Chapter 46 delivers the capstone. Chapter 47 tests failure and recovery.

### Continue studying — chapter 46 of 50

[← Chapter 45 (draft)](#ch-45) · [Course chapter index](../SUBJECTS.md) · [Chapter 47 (draft) →](#ch-47)

<a id="ch-47"></a>

## Chapter 47 — Failure and recovery trial

### Learning outcomes

You will (1) run a breach exercise against a legal clock; (2) assess vendor notification delays; (3) improve response based on the trial.

### 47.1 The scenario

Pellmore runs a breach exercise with Zara as an observer. In the synthetic scenario, the chat vendor detects an unusual export at 22:00 on 2 March. The vendor tells Pellmore at 09:30 on 4 March. Pellmore confirms that personal data are involved at 15:00 the same day. Article 33 of the GDPR requires notification to the supervisory authority without undue delay and, where feasible, within 72 hours of becoming aware, and Article 33(2) requires the processor to notify the controller without undue delay after becoming aware. The exercise uses synthetic records only.

### 47.2 The clock

The lab computes the timeline. Pellmore became aware at 15:00 on 4 March, so the 72-hour deadline is 15:00 on 7 March. Pellmore notified the authority at 11:00 on 6 March, 44 hours after awareness, on time. Patients were informed on 8 March. But the vendor took 35.5 hours to tell Pellmore after detecting the export. EDPB Guidelines 9/2022 explain when a controller becomes aware and emphasise prompt action. Zara notes that the vendor delay, not Pellmore's own process, is the weakest link in the timeline. The scenario's vendor reported after several days of delay.

### 47.3 Communicating with patients

Article 34 requires informing patients without undue delay where the breach is likely to result in a high risk to their rights and freedoms. The exercise team debates whether chat logs about symptoms meet that threshold and decides they do. The communication must describe the nature of the breach in clear language, the likely consequences, the measures taken and a contact point. Zara helps draft the message, avoiding jargon and giving practical steps, such as watching for phishing messages that refer to their consultations.

### 47.4 Improvements

After the exercise the team lists improvements: a contractual requirement for the vendor to notify within twelve hours of detection, a pre-approved patient message template, and a decision tree for assessing high risk. They also record that the internal process met the deadline comfortably. Zara adds the exercise results to the evidence dossier. She reflects that exercises reveal dependencies on others, such as vendors, that internal tests miss, and that recovery depends as much on contracts and communication as on technology. Contracts now set a twelve-hour clause.

### Lab — Breach timeline against the 72-hour clock

```python
# Breach timeline against the GDPR Article 33 72-hour clock, which starts when the controller becomes aware.
from datetime import datetime as D, timedelta
ev = [("vendor detects unusual export", D(2026, 3, 2, 22, 0)), ("vendor tells Pellmore", D(2026, 3, 4, 9, 30)),
      ("Pellmore confirms personal data involved (aware)", D(2026, 3, 4, 15, 0)),
      ("initial notification to supervisory authority", D(2026, 3, 6, 11, 0)),
      ("affected patients informed", D(2026, 3, 8, 10, 0))]
aware = ev[2][1]; deadline = aware + timedelta(hours=72)
for name, t in ev:
    print(f"{t:%d %b %H:%M}  {name}")
h = (ev[3][1] - aware).total_seconds() / 3600
print(f"deadline {deadline:%d %b %H:%M}; notified after {h:.0f} h -> {'on time' if h <= 72 else 'LATE'}")
print(f"vendor-to-controller delay {(ev[1][1]-ev[0][1]).total_seconds()/3600:.1f} h (Art 33(2): without undue delay)")
```

Run with `python3 lab_breach.py`. Verified output:

```text
02 Mar 22:00  vendor detects unusual export
04 Mar 09:30  vendor tells Pellmore
04 Mar 15:00  Pellmore confirms personal data involved (aware)
06 Mar 11:00  initial notification to supervisory authority
08 Mar 10:00  affected patients informed
deadline 07 Mar 15:00; notified after 44 h -> on time
vendor-to-controller delay 35.5 h (Art 33(2): without undue delay)
```

### Worked example

Zara's exercise shows Pellmore notifying 44 hours after awareness, inside the deadline of 15:00 on 7 March, but the vendor taking 35.5 hours to inform Pellmore, leading to a twelve-hour contractual target.

> **Synthetic case.** The breach is a synthetic exercise; GDPR Articles 33 and 34 and EDPB Guidelines 9/2022 are real.

### Errors and limits

Exercises run with known scenarios; real incidents are messier and slower to understand.

### Exercises

- **EX139 — Deadline.** When was the 72-hour deadline in the exercise? *Rubric:* 3 = 15:00 on 7 March;; 2 = right day;; 1 = wrong;; 0 = none.
- **EX140 — Weak link.** What was the weakest link in the timeline? *Rubric:* 3 = the vendor's 35.5-hour delay before telling Pellmore;; 2 = mentions vendor;; 1 = internal process;; 0 = none.
- **EX141 — Patient message.** What must the patient communication contain? *Rubric:* 3 = nature of breach, likely consequences, measures and contact point in clear language;; 2 = lists some;; 1 = vague;; 0 = none.

### Synthesis

Chapter 47 tests recovery. Chapter 48 assembles the evidence dossier.

### Continue studying — chapter 47 of 50

[← Chapter 46 (draft)](#ch-46) · [Course chapter index](../SUBJECTS.md) · [Chapter 48 (draft) →](#ch-48)

<a id="ch-48"></a>

## Chapter 48 — Evidence dossier

### Learning outcomes

You will (1) assemble evidence for accountability; (2) protect evidence integrity; (3) handle discrepancies honestly.

### 48.1 What goes in the dossier

Zara assembles an evidence dossier for her final assessment and for Pellmore's accountability. It contains the DPIA, the record of processing generated from configuration, erasure test logs, the breach exercise report and the retention monitoring report. Each item shows that a control exists and works. She organises the dossier by GDPR principle and requirement, so that an auditor can trace from a legal duty to the evidence that Pellmore meets it. Accountability under Article 5(2) depends on such evidence being complete and trustworthy.

### 48.2 Integrity

To show that evidence has not been altered, Zara records a SHA-256 digest of each file in a manifest when the dossier is approved. Later, the lab recomputes the digests. Four files match. The erasure test log does not: it now says four of five stores deleted, while the approved version said five of five. Someone edited the log after the manifest was signed. The mismatch does not tell Zara who changed the file or why, but it proves that the file differs from the approved evidence.

### 48.3 Investigating the mismatch

Zara investigates. The engineer responsible explains that a rerun after a vendor change showed one store failing, and he updated the log to reflect reality, without creating a new version. The new result is important: erasure is currently incomplete. Zara records both versions, opens a defect for the failing store and updates the manifest through the proper approval process. She notes that the integrity check did its job: it surfaced a silent change, which turned out to reveal a real problem rather than misconduct.

### 48.4 Lessons

Zara writes lessons. Evidence must be versioned, not overwritten; changes must create new entries with dates and reasons; and integrity checks should run regularly, not only at audits. She also notes that honesty about failing evidence is essential: a dossier that hid the failing store would mislead Pellmore and its patients. Prof. Holm adds that a dossier is not a showcase but a record, and that its value comes from being trustworthy, including when it shows problems. Problems found make the dossier credible.

### Lab — Verifying dossier evidence against its manifest

```python
# Evidence dossier: recompute SHA-256 digests and compare with the recorded manifest.
import hashlib
files = {"dpia_v3.md": b"DPIA v3 approved", "ropa.csv": b"flow,purpose,basis\n", "erasure_test.log": b"5/5 stores deleted",
         "breach_drill.md": b"drill 2026-03", "retention_report.txt": b"total past retention: 0"}
manifest = {n: hashlib.sha256(b).hexdigest() for n, b in files.items()}
files["erasure_test.log"] = b"4/5 stores deleted"  # edited after the manifest was signed
for n, b in files.items():
    ok = hashlib.sha256(b).hexdigest() == manifest[n]
    print(f"{n:22s} {'OK' if ok else 'MISMATCH'}")
```

Run with `python3 lab_dossier.py`. Verified output:

```text
dpia_v3.md             OK
ropa.csv               OK
erasure_test.log       MISMATCH
breach_drill.md        OK
retention_report.txt   OK
```

### Worked example

Zara's manifest check finds erasure_test.log changed from five to four stores deleted; she investigates, records both versions, opens a defect and fixes the evidence process.

> **Synthetic case.** Files and the edit are synthetic; GDPR Article 5(2) is real.

### Errors and limits

Digests detect change, not truth; a correct-looking file can still describe a wrong test.

### Exercises

- **EX142 — Mismatched file.** Which file failed the integrity check? *Rubric:* 3 = erasure_test.log;; 2 = names erasure log;; 1 = vague;; 0 = none.
- **EX143 — What the mismatch shows.** What does a digest mismatch prove and not prove? *Rubric:* 3 = the file changed since approval; not who changed it or why;; 2 = one part;; 1 = proves fraud;; 0 = none.
- **EX144 — Evidence lesson.** What process lesson follows from the mismatch? *Rubric:* 3 = version evidence instead of overwriting, with dates and reasons;; 2 = mentions versions;; 1 = vague;; 0 = none.

### Synthesis

Chapter 48 assembles trustworthy evidence. Chapter 49 writes the thesis.

### Continue studying — chapter 48 of 50

[← Chapter 47 (draft)](#ch-47) · [Course chapter index](../SUBJECTS.md) · [Chapter 49 (draft) →](#ch-49)

<a id="ch-49"></a>

## Chapter 49 — Engineering thesis

### Learning outcomes

You will (1) write an engineering thesis around a design claim; (2) present evidence and limits; (3) generalise lessons carefully.

### 49.1 The claim

Zara's thesis claims that a privacy-preserving research data service, built from templates, output checks and differential privacy budgets, can support useful outcome analysis for a telemedicine provider without record-level access, with verified protection against the reconstruction attacks tested. The claim is bounded: one organisation, one analysis type, synthetic verification data and a small researcher evaluation. She states the bounds in the abstract and the introduction so that no reader mistakes the claim for a general solution. Bounded claims are easier to defend under examination.

### 49.2 Evidence chapters

The thesis presents requirements traced to law, the design and its review, the implementation, verification results including failures and fixes, the reconstruction attack, the researcher evaluation and the evidence dossier. Each chapter answers part of the claim. Zara includes the expiry bug and the failing erasure store from the dossier, explaining how each was found and fixed. Examiners, she argues, should see that the verification process works because it found real problems, not because everything passed the first time. Each failure cites its fix and retest.

### 49.3 Limits

Zara writes limits clearly. Template systems restrict exploratory research. National aggregation reduces timeliness for rare conditions. Differential privacy budgets require careful management and expert implementation. Legal analysis relies on GDPR and LGPD texts and EDPB guidance, not case law. The service depends on the consent service and privacy platform, which must remain reliable. She also notes that real patient data might behave differently from synthetic test data, and that a real deployment would need its own DPIA. She also lists untested threats openly.

### 49.4 Generalisation

Zara discusses what other organisations could learn. The pattern of approved templates, output checks and per-study budgets could transfer to other health providers, but the parameters depend on population size, query types and risk appetite. She cites NIST SP 800-188 and Dwork and Roth (2014) for the general methods and Pellmore's results for one configuration. She avoids recommending specific epsilon values for others. Prof. Holm praises the restraint, noting that over-generalisation is a common weakness in engineering theses. She describes a method for choosing epsilon instead of recommending values.

### Worked example

Zara writes a bounded thesis claim, presents evidence including failures, lists limits from template restrictiveness to synthetic data and generalises the pattern without prescribing parameters.

> **Synthetic case.** The thesis is synthetic; NIST SP 800-188 and Dwork and Roth (2014) are real.

### Errors and limits

A bounded claim can still be misquoted; repeat the bounds in summaries.

### Exercises

- **EX145 — Thesis bounds.** List the bounds of Zara's claim. *Rubric:* 3 = one organisation, one analysis type, synthetic verification, small evaluation;; 2 = three;; 1 = one;; 0 = none.
- **EX146 — Failures in thesis.** Why include the expiry bug and failing store? *Rubric:* 3 = they show verification found and fixed real problems;; 2 = mentions honesty;; 1 = hide them;; 0 = none.
- **EX147 — No epsilon advice.** Why does Zara avoid recommending epsilon values for others? *Rubric:* 3 = parameters depend on each organisation's population, queries and risk appetite;; 2 = mentions context;; 1 = gives values;; 0 = none.

### Synthesis

Chapter 49 writes the thesis. Chapter 50 is the final defense.

### Continue studying — chapter 49 of 50

[← Chapter 48 (draft)](#ch-48) · [Course chapter index](../SUBJECTS.md) · [Chapter 50 (draft) →](#ch-50)

<a id="ch-50"></a>

## Chapter 50 — Final defense

### Learning outcomes

You will (1) defend an engineering thesis; (2) answer questions on law, design and verification; (3) plan professional development.

### 50.1 Preparing

Zara prepares for the final defense by listing likely questions in three groups: legal (why is the lawful basis for research appropriate?), design (why templates instead of a query language?) and verification (how do you know the noise generator is correct?). She rehearses concise answers with evidence references. Prof. Holm conducts a mock defense and pushes her on the limits of synthetic testing. She practises saying what she would do next to address each limit, rather than defending the limit itself. Rehearsals are recorded.

### 50.2 The defense

At the defense the examiners ask about the opt-out timing finding from the design review. Zara explains the cache problem and the decision to rerun studies without caching. They ask whether differential privacy guarantees hold if templates change. She explains that each new template needs sensitivity analysis and review, which the governance process requires. They ask about vendor dependence, and she cites the breach exercise and the new twelve-hour notification clause. The examiners pass the thesis and commend the evidence dossier. The examiners ask for no changes.

### 50.3 Professional development

After the defense Zara writes a development plan. She wants to deepen her knowledge of formal privacy accounting, gain experience with supervisory authority interactions and learn more about health law beyond the GDPR and LGPD. She notes that ISO/IEC 27701:2025 certification audits would give her practical experience with management systems. She also plans to mentor first-year students in privacy unit testing, completing the circle that began with her own first programming assignment five years earlier. Pellmore offers her a privacy engineering role, which she accepts after the defense.

### 50.4 Looking back

Zara looks back on five years. The foundations, from calculus to cryptography, each gave her tools for privacy problems. The middle years taught her to turn law into requirements and requirements into tested systems. The final years taught her to work with people, evidence and limits. She concludes that privacy engineering is not a specialism added at the end but a way of building systems responsibly from the start. Pellmore offers her a role in its privacy engineering team, which she accepts.

### Worked example

Zara defends opt-out timing, template sensitivity and vendor dependence, passes with commendation for the dossier and plans development in formal accounting, regulatory work and mentoring.

> **Synthetic case.** The defense and job offer are synthetic; ISO/IEC 27701:2025 is real.

### Errors and limits

A passed defense is not the end of learning; practice will expose new gaps.

### Exercises

- **EX148 — Template guarantee.** How are guarantees maintained when templates change? *Rubric:* 3 = each new template needs sensitivity analysis and review;; 2 = mentions review;; 1 = automatic;; 0 = none.
- **EX149 — Vendor answer.** What evidence did Zara cite on vendor dependence? *Rubric:* 3 = the breach exercise and the twelve-hour notification clause;; 2 = one;; 1 = vague;; 0 = none.
- **EX150 — Course conclusion.** What does Zara conclude about privacy engineering? *Rubric:* 3 = it is a way of building systems responsibly from the start, not an add-on;; 2 = mentions design;; 1 = specialism;; 0 = none.

### Synthesis

Chapter 50 completes the engineering route. The worked results follow, then the references.

### Continue studying — chapter 50 of 50

[← Chapter 49 (draft)](#ch-49) · [Course chapter index](../SUBJECTS.md) · [Worked results ↓](#worked-results) · [Next course via chapter index →](../SUBJECTS.md)

<a id="worked-results"></a>

## Worked results

Model answers for EX001–EX150. Zara Mbeki, Prof. Anders Holm, Corwen Polytechnic, Pellmore Telehealth and every figure are synthetic. Lab answers quote verified outputs. Any answer meeting the rubric scores equally.

**EX001.** With deletion after a fixed period, inflow equals outflow, so stored data level off.

**EX002.** It turns into a single person's value, so publishing it discloses that person's data.

**EX003.** Risk to individuals cannot be traded freely for usefulness, and legal requirements act as constraints.

**EX004.** There are far more possible combinations than patients, so most combinations hold at most one person.

**EX005.** At a telemedicine provider almost any personal data, even booking times, indicate health care.

**EX006.** An undocumented data flow that nobody is managing.

**EX007.** The file system drops its reference, but the stored states persist until overwritten.

**EX008.** All copies are encrypted under one key; destroying the key renders them unreadable.

**EX009.** Timing and duration reveal that a patient consulted a clinician, even if content is protected.

**EX010.** Logs often persist and are less protected, so identifiers in them create avoidable exposure.

**EX011.** Data minimisation: data must be adequate, relevant and limited to what is necessary.

**EX012.** It scans log output and fails if any line contains a birth date.

**EX013.** Concise, transparent, intelligible and easily accessible, in clear and plain language.

**EX014.** People decide in context, so explanations at the moment of use are more effective than a single long notice.

**EX015.** Accountability: being able to demonstrate compliance.

**EX016.** It measures accumulated exposure: how many patients' data were held for how long.

**EX017.** A past diagnosis can still cause harm, so sensitivity does not decay with age.

**EX018.** Small per-release losses add up, so repeated releases accumulate unbounded loss.

**EX019.** Any yes could be produced by the second coin, so it is plausibly deniable.

**EX020.** (0.344 − 0.25) / 0.5 ≈ 0.189.

**EX021.** About 0.021 versus 0.009, more than double.

**EX022.** Swap space and crash dumps; caches and memory can hold fragments too.

**EX023.** Each month's videos share a key; destroying it erases that month, and the key operation is easy to verify.

**EX024.** Measurements counter unsupported claims that protection is too costly.

**EX025.** It lets each service access only the part it needs, limiting exposure by design.

**EX026.** Purpose-based checks limit reading to legitimate uses and create an accountable log.

**EX027.** A convenience export that joined both tables, allowing full records to leave.

**EX028.** Preventing foreseeable harm to patients, regardless of whether a regulator would notice.

**EX029.** It moves care information into a marketing context, violating patients' expectations and risking harm.

**EX030.** The DPO's independent role includes advising and monitoring compliance, making it the right channel.

**EX031.** URLs are recorded in many logs, so identifiers in them leak even over encrypted connections.

**EX032.** It preserves short-term security use while limiting long-term tracking of where patients connected.

**EX033.** A binding data processing agreement with each processor.

**EX034.** Exports landed in a directory any account could read.

**EX035.** Use secure temporary files with restrictive permissions, clean up on start and delete anything older than a day.

**EX036.** It provides evidence that security measures are maintained and evaluated.

**EX037.** Personal data must not be kept in identifiable form longer than necessary for the purposes.

**EX038.** Video recordings, with 96 of 101 past the thirty-day limit.

**EX039.** Backups are protected, expire within a defined time and any restore reapplies the retention table before use.

**EX040.** As a patient, I want my video recordings deleted after thirty days unless I ask otherwise.

**EX041.** A change that would have sent patient names to a crash reporting service.

**EX042.** Test systems are weaker, so realistic synthetic data avoids placing real health data there.

**EX043.** Security protects data, but privacy also concerns how much is collected and for what purposes.

**EX044.** Viewing records and changing contact details, because they are high-value targets.

**EX045.** Yes; the definition covers accidental as well as unlawful disclosure.

**EX046.** If any component ignores a property such as retention, the system as a whole lacks it.

**EX047.** The analytics system had no retention requirement.

**EX048.** The video vendor's contract allowed ninety-day retention against Pellmore's thirty-day rule.

**EX049.** Without measuring overdue records, nothing triggered correction.

**EX050.** Views of records by staff with no appointment for that patient.

**EX051.** A second signal tracks category changes, which need approval.

**EX052.** It restricts lateral movement by attackers and prevents misconfigured jobs from reaching clinical data.

**EX053.** Permissions tied to purposes ensure data are used only for those purposes.

**EX054.** Clinical notes appear only when the patient grants temporary access during the call.

**EX055.** The number space is small, so hashing every value reverses it; a secret key is needed.

**EX056.** They stop different recipients linking their datasets.

**EX057.** Additional information or remaining attributes can re-identify people, so the GDPR treats them as personal data.

**EX058.** GDPR Article 9 and LGPD Article 11.

**EX059.** A processor, because it processes recordings on Pellmore's instructions.

**EX060.** Obligations become real only when systems implement them, and engineers build those systems.

**EX061.** Each field is tagged with allowed purposes, and services may read only fields tagged for their own purpose.

**EX062.** A patient can download all personal data held within one minute, in a machine-readable format.

**EX063.** Pellmore lacked a structured, machine-readable export needed for portability.

**EX064.** Three of seven; the analytics SDK fails all three rules.

**EX065.** Lawyers choose the mechanism; engineers supply what data move, how much, how often and why.

**EX066.** Deployment is blocked until a new flow has a reviewed purpose, basis and transfer mechanism.

**EX067.** Unawareness and non-compliance can arise from design alone, as can linkability.

**EX068.** The vendor's systems are invisible to Pellmore, so confirmations and audit rights are needed.

**EX069.** Monitoring is itself processing of employees' data and must be proportionate and transparent.

**EX070.** Telemedicine processes health data at scale for potentially vulnerable patients, meeting several criteria.

**EX071.** The vendor breach (6), since Pellmore can only influence, not control, the vendor's security.

**EX072.** Without the planned measures, such as removing the analytics SDK, high risk would remain.

**EX073.** On-device triage collects least, but updates and device support are harder.

**EX074.** The result is advisory and patients can always reach a clinician.

**EX075.** Through opt-in feedback and periodic clinical testing with synthetic cases.

**EX076.** It simplifies analysis but concentrates risk in one store.

**EX077.** Differential privacy reduces accuracy for small groups; multi-party computation is complex and slow.

**EX078.** Federated analysis with aggregated outputs, plus a small restricted pseudonymised dataset for safety audits.

**EX079.** Access checks prevent, anomaly signals detect, and disciplinary and notification procedures correct.

**EX080.** Freely given, specific, informed and unambiguous, with withdrawal as easy as giving.

**EX081.** A nightly copy to a legacy reporting server that no requirement justified.

**EX082.** Warnings reveal gaps without outages; blocking follows once gaps are fixed.

**EX083.** Withdrawals missed by the email platform during a network outage.

**EX084.** Generated records change when configuration changes, keeping documentation accurate.

**EX085.** 8 of 18 fields, 44%.

**EX086.** Owners might claim every field is needed, so an independent check keeps the measure honest.

**EX087.** Data collected to monitor privacy must be minimised and protected like any other personal data.

**EX088.** Fixing expectations beforehand stops results being interpreted to fit hopes.

**EX089.** The analytics store kept events under the pseudonym.

**EX090.** "Erasure works" is a claim; a dated log of a test deleting from all stores is evidence.

**EX091.** It includes data patients provided, such as appointment history and symptoms, but not clinicians' notes.

**EX092.** Article 28, which requires processors to assist the controller with data subject rights.

**EX093.** Very small counts may reveal individual patients' behaviour.

**EX094.** All stores must succeed, so the overall probability is the product of each store's.

**EX095.** From about 175 to 13 per 1,000 requests.

**EX096.** Because the patient wrongly believes their data were erased.

**EX097.** Yes, a personal data breach includes loss of availability of personal data.

**EX098.** Old backups can reintroduce erased data, so erasures and retention are reapplied before going live.

**EX099.** They should behave as if consent is absent.

**EX100.** It removes inconsistency but makes many services depend on it.

**EX101.** It decides why and how it processes data for its own testing.

**EX102.** A schema comparison flags new fields and triggers a privacy review.

**EX103.** Notes were shared in a confidential context, so they move only on the patient's explicit choice.

**EX104.** Discreet private prompts at login and clinicians asking about sharing.

**EX105.** Only the patient or a verified authorised representative.

**EX106.** A mean absolute error of about 121.7 per count.

**EX107.** It bounds sensitivity at one, matching the noise calibration.

**EX108.** No; post-processing of differentially private output keeps the guarantee.

**EX109.** 97% within thirty days.

**EX110.** Under the disciplinary policy, and recorded and assessed as a potential personal data breach.

**EX111.** A cycle of monitoring, review and improvement, as management system standards expect.

**EX112.** Verification: does the system meet requirements? Validation: do the requirements meet real needs?

**EX113.** Patients expected medical records to be erased; the screen needed clearer explanation of legal limits.

**EX114.** Patient-entered symptom notes forming part of the medical record must be retained.

**EX115.** Shortcuts that weaken privacy, like temporary copies, disabled checks or undocumented flows.

**EX116.** A messaging library change to retries that would have hurt erasure reliability.

**EX117.** Without understandable controls, the organisation cannot show it complies.

**EX118.** Diagnosis inference for a rural clinic, from old reports published before differential privacy.

**EX119.** When a protection is introduced, find and review outputs produced under the old approach.

**EX120.** Independent testers bring other assumptions and found the autocomplete leak the class missed.

**EX121.** She replaced the three caches with a single name service that only answers authorised callers.

**EX122.** After clinicians agreed, retention became six months, with relevant logs kept in the medical record.

**EX123.** It fell from eleven to six.

**EX124.** At least eighty per cent correct answers about what the carer can see.

**EX125.** 71% with the current screen and 90% with the preview.

**EX126.** The sample was small and volunteers may be more app-confident than typical patients.

**EX127.** By providing differentially private regional aggregates instead of clinic-level data.

**EX128.** She confirmed the complaint purpose, retrieved only relevant records and recorded the access.

**EX129.** Article 38 protects the DPO, so privacy concerns could not simply be overruled by commercial interests.

**EX130.** A narrow scope allows proper completion and verification.

**EX131.** Each study gets a fixed privacy budget, limiting how much can be learned by combining outputs.

**EX132.** Defining tests first guards against a system that looks fine but fails in real use.

**EX133.** Intermediate results cached before an opt-out could still include that patient.

**EX134.** Queries can reveal what researchers are investigating, which is sensitive.

**EX135.** By aggregating nationally and over longer periods.

**EX136.** Expired studies could still run because of a time-zone date-format error.

**EX137.** Nothing about any individual; noise and the budget stopped it.

**EX138.** Restrictive but workable, with a request for one additional template.

**EX139.** 15:00 on 7 March, 72 hours after awareness at 15:00 on 4 March.

**EX140.** The vendor took 35.5 hours to inform Pellmore after detection.

**EX141.** Clear description of the breach, likely consequences, measures taken and a contact point.

**EX142.** erasure_test.log.

**EX143.** It proves the file differs from the approved version, but not who changed it or why.

**EX144.** Evidence must be versioned with new dated entries rather than overwritten.

**EX145.** One organisation, one analysis type, synthetic test data and a small researcher evaluation.

**EX146.** They demonstrate that verification works by catching real issues.

**EX147.** Suitable values depend on local factors, so prescribing them would over-generalise.

**EX148.** Each new template requires sensitivity analysis and governance review.

**EX149.** The breach exercise and the new twelve-hour vendor notification requirement.

**EX150.** It is a way of building systems responsibly from the start rather than an add-on.

<a id="references"></a>

## References

Every DOI was resolved through doi.org on 12 October 2026; laws and guidelines link to their official publishers. Re-verify editions before citing. Organisations, people, systems and figures in the running cases are synthetic; only the works below are real.

- Acquisti, A., Brandimarte, L., & Loewenstein, G. (2015). Privacy and human behavior in the age of information. *Science, 347*(6221), 509–514. <https://doi.org/10.1126/science.aaa1465>
- Brasil. (2018). *Lei nº 13.709, de 14 de agosto de 2018 — Lei Geral de Proteção de Dados Pessoais (LGPD)*. <https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709.htm>
- Dwork, C., McSherry, F., Nissim, K., & Smith, A. (2006). Calibrating noise to sensitivity in private data analysis. *Theory of Cryptography (TCC 2006)*, 265–284. <https://doi.org/10.1007/11681878_14>
- Dwork, C., & Roth, A. (2014). The algorithmic foundations of differential privacy. *Foundations and Trends in Theoretical Computer Science, 9*(3–4), 211–407. <https://doi.org/10.1561/0400000042>
- European Data Protection Board. (2020). *Guidelines 4/2019 on Article 25 Data Protection by Design and by Default* (Version 2.0, adopted 20 October 2020). <https://www.edpb.europa.eu/documents/guideline/guidelines-42019-on-article-25-data-protection-by-design-and-by-default_en>
- European Data Protection Board. (2023). *Guidelines 9/2022 on personal data breach notification under GDPR* (Version 2.0, adopted 28 March 2023). <https://www.edpb.europa.eu/documents/guideline/guidelines-92022-on-personal-data-breach-notification-under-gdpr_en>
- European Union. (2016). Regulation (EU) 2016/679 (General Data Protection Regulation). *Official Journal of the European Union, L 119*, 1–88. <http://data.europa.eu/eli/reg/2016/679/oj>
- Garfinkel, S. L. (2015). *De-identification of personal information* (NISTIR 8053). NIST. <https://doi.org/10.6028/NIST.IR.8053>
- Garfinkel, S., Near, J., Dajani, A., Singer, P., & Guttman, B. (2023). *De-identifying government datasets: Techniques and governance* (NIST SP 800-188). NIST. <https://doi.org/10.6028/NIST.SP.800-188>
- ISO/IEC. (2011). *ISO/IEC 29100:2011 Information technology — Security techniques — Privacy framework*. <https://www.iso.org/standard/45123.html>
- ISO/IEC. (2025). *ISO/IEC 27701:2025 Information security, cybersecurity and privacy protection — Privacy information management systems — Requirements and guidance* (2nd ed., replaces the 2019 edition). <https://www.iso.org/standard/27701>
- National Institute of Standards and Technology. (2020). *NIST Privacy Framework: A tool for improving privacy through enterprise risk management, Version 1.0* (NIST CSWP 10). <https://doi.org/10.6028/NIST.CSWP.10>
- Nissenbaum, H. (2004). Privacy as contextual integrity. *Washington Law Review, 79*(1), 119–157.
- Solove, D. J. (2006). A taxonomy of privacy. *University of Pennsylvania Law Review, 154*(3), 477–564. <https://doi.org/10.2307/40041279>
- Sweeney, L. (2002). k-anonymity: A model for protecting privacy. *International Journal of Uncertainty, Fuzziness and Knowledge-Based Systems, 10*(5), 557–570. <https://doi.org/10.1142/S0218488502001648>
- Warren, S. D., & Brandeis, L. D. (1890). The right to privacy. *Harvard Law Review, 4*(5), 193–220. <https://doi.org/10.2307/1321160>
- European Data Protection Board. (2023). *Guidelines 01/2022 on data subject rights — Right of access* (Version 2.0 adopted 28 March 2023; Version 2.1 with minor corrections, 30 May 2024). <https://www.edpb.europa.eu/documents/guideline/guidelines-012022-on-data-subject-rights-right-of-access_en>
- European Data Protection Board. (2021). *Guidelines 07/2020 on the concepts of controller and processor in the GDPR* (Version 2.0 adopted 7 July 2021; Version 2.1, 20 September 2022). <https://www.edpb.europa.eu/documents/guideline/guidelines-072020-on-the-concepts-of-controller-and-processor-in-the-gdpr_en>
- Article 29 Data Protection Working Party. (2017). *Guidelines on Data Protection Impact Assessment (DPIA) and determining whether processing is "likely to result in a high risk" for the purposes of Regulation 2016/679* (WP248 rev.01, as last revised 4 October 2017; endorsed by the EDPB). <https://ec.europa.eu/newsroom/article29/items/611236>
- European Data Protection Board. (2020). *Guidelines 05/2020 on consent under Regulation 2016/679* (Version 1.1, adopted 4 May 2020). <https://www.edpb.europa.eu/documents/guideline/guidelines-052020-on-consent-under-regulation-2016679_en>
