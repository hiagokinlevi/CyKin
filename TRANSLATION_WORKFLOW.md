# Translation production and release workflow

This workflow turns reviewed English teaching into complete language editions without treating a chapter count as proof of translation quality. English remains the authoring reference. Portuguese is the active translation language; planned Spanish production follows completion and review of the Portuguese collection. The other six languages remain outside planned production until the [three-language gate](BOOK_STANDARD.md#sequential-production-order) passes. Existing public translations remain readable and may receive maintenance corrections.

## Two scopes that must remain separate

| Measure | Denominator | What it says |
|---|---|---|
| Translation coverage of a pinned reference | All instructional units and shared material in a named English commit | The target edition has corresponding published teaching, examples, labs, figures, exercises and worked answers. |
| Reviewed translation parity | The same pinned scope | Source and target were compared, technical and linguistic checks were recorded, and the exact published revisions still match that review. |
| Full curriculum completion | The course's intended weekly and daily curriculum | Every required lesson has passed the [book publication gate](BOOK_STANDARD.md#publication-gate-for-each-volume). |

A translation may cover all English teaching available at one commit while both books remain incomplete against the curriculum. Report chapter or lesson counts and source volume alongside percentages. A new English lesson changes the *current* scope; it does not rewrite the historical measurement for an earlier pinned commit. Never call structural anchor presence “reviewed parity.” The [multilingual shelf](WRITING_PROGRESS.md) remains a separate structural indicator.

## Release a coherent English unit

1. Choose a full public commit SHA and a course. Inventory the English `book/MANUSCRIPT.md` at that SHA. The working unit is a chapter, including its nested lessons and the matching worked-answer entries. Include book-wide preface, glossary, references, rights notes and navigation in a separate whole-book review; chapter units alone cannot certify a whole book.
2. Review the unit's factual sources, terminology, mechanisms, assumptions, limits, privacy and safety conditions, executable examples, figures, exercises and answers. Include dependent material when one changed claim affects another chapter or answer. Record reviewer, date, exact unit hash and evidence. A named editor must actually perform the review; an AI comparison is supporting evidence, not an independent human review.
3. Correct a defect in the English public manuscript first. Pin the resulting new SHA and recheck affected units. Do not work around a reference defect silently in Portuguese.
4. Release only reviewed units to the translation queue. An outline, an unexamined unit and an unavailable file stay pending. The operational queue does not infer approval from the manuscript's “published” label.

## Process a released translation unit

1. Read the current Portuguese `book/MANUSCRIPT.md` and any local manual changes before accepting work. Preserve valid existing translation. If the destination is being edited manually, hold the overlapping unit rather than assigning it again.
2. Translate the full instructional package: prose, tables, captions and diagram labels, laboratory instructions and interpretations, exercise prompts and rubrics, worked answers, source explanations and navigation. Preserve stable exercise IDs, exact fixture data, literal code output, API fields and constraints. Maintain a contextual glossary; never reuse a phrase solely because the English words match.
3. Use isolated branches or worktrees for nonoverlapping units. Four translation workers are an experimental starting limit, subject to measured cost, review load and defect rate. Workers submit candidates in public repository branches; they do not write concurrently to one principal manuscript. The private Engine may hold task metadata and test records, never a duplicate teaching manuscript.
4. Compare source and target for omissions, negation, strength of claims, formulas, scope, chronology, uncertainty, citations, rights, visual meaning, exercise demands and answer reasoning. Run the relevant offline labs, link and navigation checks, language-leak scan and rendered reading check. An unchanged code/data/environment/test signature may justify reusing an earlier run record if the reviewer confirms that the result remains applicable; the final integrated edition still needs a readback check.
5. One integrator reconciles accepted candidate units into the target edition's single `book/MANUSCRIPT.md`, updates `SUBJECTS.md` and relevant indexes, and publishes with a normal fast-forward commit. Check the remote SHA and the actual public book. Site deployment and MCP readback are separate checks. Do not use GitHub Actions or force push.
6. Record the source and target hashes, comparison evidence, editor and date. A changed English unit or translated answer invalidates that unit's previous parity approval until reconciled. Preserve unaffected approved units. A source change can also invalidate dependent examples and answers in another unit.

The website's five-choice exercise is a separate authored assessment artifact. If a source lesson lacks five reviewed options, record that as a separate content gap; a translated free-response prompt and worked answer do not magically create a reviewed choice set.

## Operational inventory and queue

The authorized local private Engine contains `scripts/translation_queue.py`. It reads a clean public checkout at an immutable commit and can inspect a separate manual checkout without changing either. Its output classifies units as `absent`, `local_unpublished`, `present_unreviewed`, `stale` or `reviewed`. “Reviewed” means the supplied review ledger names an editor, date and evidence for the exact source and target package hashes and no structural issue was detected; the script does not itself judge translation quality or authenticate an editor's assertion.

Example from the private Engine checkout:

~~~sh
python3 scripts/translation_queue.py inventory \
  --repo /path/to/clean/OpenCyberAcademy \
  --source-ref FULL_PUBLIC_COMMIT_SHA \
  --course rapid-1-month/human-factors-policy --language pt \
  --working-repo /path/to/manual/OpenCyberAcademy \
  --ledger /path/to/editorial-review-ledger.json
~~~

The ledger has `source_reviews` and `translation_reviews` arrays. A source entry names `course`, `unit`, `source_sha256`, `reviewer`, `reviewed_on` and `evidence`. A translation entry additionally names `language` and `target_sha256`. The source hash covers chapter teaching and its matching worked answers. The ledger must contain actual review evidence; filling a field with a claim is not a substitute for review. The operator verifies that the chosen clean checkout reflects the current public `main` before queue synchronization.

After an English unit is reviewed, `sync` inserts only eligible nonoverlapping jobs into an SQLite queue in the private Engine. `claim` uses an atomic lease so two workers cannot take the same job; `submit` records a public candidate branch or commit for the single integrator. No command generates or publishes translation automatically. An unreviewed source, missing source answer or local manual destination change blocks queue insertion. Queue data are operational records, not reader-facing lessons.

## Pilot and acceptance

Start with one book whose remaining units have actually been released. Inventory and review the source; then compare against the current public Portuguese edition *and* any local manuscript changes. Do not repeat translation already present in a manual checkout. Publish a coherent batch only when its corresponding exercises and answers, links, labs and navigation are validated. Measure units accepted and published per hour, cost per accepted unit, defect and rework rate, and the review queue. Increase parallelism only when the single integrator and reviewers can keep up.

The earlier suggestion to translate rapid Human Factors chapters 11–20 is a candidate, not a permanent assignment: check the real checkout first. Its English source and Portuguese destination may have changed since the suggestion was written. No queue entry or coverage claim is earned by this document itself.
