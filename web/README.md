# CyKin web application

The public site runs as one Cloudflare Python Worker: Astro builds the frontend, FastAPI serves the API and MCP endpoint, and Workers Static Assets serves the built pages. The public [CyKin repository](https://github.com/hiagokinlevi/CyKin) is the source of teaching content. Course metadata is generated at build time; a selected manuscript and its plan are read from `main` on GitHub when a visitor opens a course. A new chapter is therefore visible without a site rebuild, while new course folders or changed course metadata require a deployment.

## Daily study migration — deployment must be verified separately

The [daily-study policy](../DAILY_STUDY_STANDARD.md) is a public Markdown contract for all nine levels and languages. The new `/daily/?level=...&area=...&lang=...` reader separates daily portions from the existing whole-chapter reader. Its optional `start=YYYY-MM-DD` calendar counts actual Monday–Friday dates, shows the calendar-month boundary and fixed-sequence end, and flags alignment differences. No holiday or vacation is silently excluded. Every mapped view presents teaching, example, exercises and separately disclosed worked answers from the **same manuscript**, not a second content store.

The read-only endpoints are `GET /api/daily/{level}/{area}/{language}` and `GET /api/daily/{level}/{area}/{language}/{day}`. They reuse the existing catalog and public source loader. An edition-specific `DAILY_PLAN.md` binds exact heading ranges and exercise-answer pairs to the manuscript's Git blob. Missing maps remain planned; changed or invalid sources are blocked; upstream errors are not reported as proof of absent teaching. There is no English content substitution and no daily progress write endpoint in this version. Existing chapter URLs, account records and private Access boundaries are preserved. Existing `/api/lessons` and MCP lesson resources remain **chapter-based compatibility interfaces**, not the new daily positions.

The first rapid IR English map proposes 22 readings and retains 50 exercises. The nine-code edition selector and daily controls do not establish translated books. Mapped readings are distinct from native or reviewed daily lessons; see [migration status](../DAILY_STUDY_PROGRESS.md). Complete the prerequisite, workload, actual-source and browser review before presenting a fully paced edition. Longer future books may need a revision-indexed extraction/cache implementation beyond current upstream reader size limits; do not compress editorial content to fit an implementation limit.

Run `uv run pytest -q tests/test_daily_study.py` from `web` for the isolated contract suite, then run the existing complete tests and `npm run build`. The reported 171 daily tests use synthetic source fixtures and metadata checks, not an end-to-end live-book extraction or a Cloudflare acceptance test. TypeScript transpilation and strict isolated checking are not an Astro build. Inspect daily and planned views, all language selection paths, RTL reading, answer disclosures, previous/next and full-book links, stale-source behavior and mobile layout before deployment. Use the local script below only from the authorized maintainer checkout; no GitHub Actions. **Publishing these source files does not demonstrate that the new page or API is live.**

## Local development

From this directory:

```sh
npm ci
uv sync --frozen
npm run build
uv run pytest -q
uv run pywrangler dev --local --port 8787
```

Open `http://localhost:8787/`. The site and `/api/*` and `/mcp` are public. The protected progress endpoints require a Cloudflare Access token and are unavailable in local development without a matching Access session.

Readers use the separate **By level** and **By subject** menus. `/levels/` and `/subjects/` open distinct directories; `/levels/{level}/` lists the 23 separate courses at that level, and `/subjects/{area}/` lists the nine distinct levels of that subject. Each `/courses/{level}/{area}/?lang=...` page has its own lesson guide, lesson reader and navigation. `/book/?level=...&area=...&lang=...` displays the complete manuscript, and `/read/?path=...` displays course references and plans. Old `/learn/` links redirect to the corresponding course or directory. These pages render Markdown within CyKin and route book, chapter, index and reference links internally. The interface starts in English, follows a supported browser language (English, Portuguese or Spanish), and offers a persistent language switch. The selected course edition remains separate from the interface translation; an outline is never shown as a written lesson.

## Student sign-in and progress

Reading never requires an account. Only `/private/*` is protected by the Cloudflare Access self-hosted application **CyKin student progress** for `cykin.org/private/*`. Its **Allow** policy requires a verified one-time email PIN. FastAPI independently validates the signed Access JWT, its issuer, application audience, expiration, not-before time and user ID. The D1 `cykin-progress` database stores completed lessons and attempted exercises under that user ID. The optional `/account/` page and all books, lessons, catalog, OpenAPI and MCP routes remain public.

The Access application audience and team domain are non-secret Wrangler variables. The configured Access application uses an HTTP-only, path-scoped, SameSite=Lax cookie. Cloudflare Access Free currently has a 50-user seat limit; monitor usage before inviting more students. Audio and video are future features and are not claimed as available.

## Publish from an authorized local computer

The database is created once and `migrations/0001_progress.sql` is applied with `wrangler d1 execute cykin-progress --remote --file=migrations/0001_progress.sql`. Do not repeat setup against another account without checking the destination.

After committing and pushing the site to the public repository's `main` branch, run:

```sh
./scripts/deploy-local.sh
```

The script checks the GitHub remote, requires a clean checkout at the exact public `main` commit, checks the Cloudflare account, builds and tests locally, deploys with PyWrangler, and checks the live health and MCP endpoints. No GitHub Actions or cloud build pipeline is used.

For a content-only publication, push the Markdown to GitHub; the reader fetches the selected book from GitHub `main`. To update the static catalog after course structure changes, rebuild and deploy locally.

## Public AI interface

- `GET /api/catalog` lists 207 courses and build-time edition hints.
- `GET /api/courses/{level}/{area}/{language}` distinguishes authored chapters from outlines.
- `GET /api/lessons/{level}/{area}/{language}/{chapter}` returns a chapter, exercises, worked answers and its GitHub source URL.
- `GET /api/books/{level}/{area}/{language}` returns the current Markdown manuscript.
- `GET /api/source?path=...` returns a public Markdown course reference for internal reading routes.
- `GET /api/search/{level}/{area}/{language}?q=...` searches the current book.
- `POST /mcp` provides stateless MCP Streamable HTTP discovery, reading and search. `GET /mcp` returns 405 as required when no event stream is offered.
- `GET /llms.txt` gives AI clients a compact entry point.

Published text is not automatically an approved or completed book. The API and reader do not present plan-only chapters as finished lessons.
