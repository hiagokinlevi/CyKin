# CyKin web application

The public site runs as one Cloudflare Python Worker: Astro builds the frontend, FastAPI serves the API and MCP endpoint, and Workers Static Assets serves the built pages. The public [CyKin repository](https://github.com/hiagokinlevi/CyKin) is the source of teaching content. Course metadata is generated at build time; a selected manuscript and its plan are read from `main` on GitHub when a visitor opens a course. A new chapter is therefore visible without a site rebuild, while new course folders or changed course metadata require a deployment.

## Daily study migration — deployment must be verified separately

The [daily-study policy](../DAILY_STUDY_STANDARD.md) is a public Markdown contract for all nine levels and languages. The new `/daily/?level=...&area=...&lang=...` reader separates daily portions from the existing whole-chapter reader. Its optional `start=YYYY-MM-DD` calendar counts actual Monday–Friday dates, shows the calendar-month boundary and fixed-sequence end, and flags alignment differences. No holiday or vacation is silently excluded. Every mapped view presents teaching, example, exercises and separately disclosed worked answers from the **same manuscript**, not a second content store.

The read-only endpoints are `GET /api/daily/{level}/{area}/{language}` and `GET /api/daily/{level}/{area}/{language}/{day}`. They reuse the existing catalog and public source loader. An edition-specific `DAILY_PLAN.md` binds exact heading ranges and exercise-answer pairs to the manuscript's Git blob. Missing maps remain planned; changed or invalid sources are blocked; upstream errors are not reported as proof of absent teaching. There is no English content substitution and no daily progress write endpoint in this version. Existing chapter URLs, account records and private Access boundaries are preserved. Existing `/api/lessons` and MCP lesson resources remain **chapter-based compatibility interfaces**, not the new daily positions.

The first rapid IR English map proposes 22 readings and retains 50 exercises. The nine-code edition selector and daily controls do not establish translated books. Mapped readings are distinct from native or reviewed daily lessons; see [migration status](../DAILY_STUDY_PROGRESS.md). Complete the prerequisite, workload, actual-source and browser review before presenting a fully paced edition. Longer future books may need a revision-indexed extraction/cache implementation beyond current upstream reader size limits; do not compress editorial content to fit an implementation limit.

Run `uv run pytest -q tests/test_daily_study.py` from `web` for the isolated contract suite, then run the existing complete tests and `npm run build`. The reported 171 daily tests use synthetic source fixtures and metadata checks, not an end-to-end live-book extraction or a Cloudflare acceptance test. TypeScript transpilation and strict isolated checking are not an Astro build. Inspect daily and planned views, all language selection paths, RTL reading, answer disclosures, previous/next and full-book links, stale-source behavior and mobile layout before deployment. Use the local script below only from the authorized maintainer checkout; no GitHub Actions. **Publishing these source files does not demonstrate that the new page or API is live.**

## Local development

From this directory:
