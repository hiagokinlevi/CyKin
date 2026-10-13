# CyKin web application

The public site runs as one Cloudflare Python Worker: Astro builds the frontend, FastAPI serves the API and MCP endpoint, and Workers Static Assets serves the built pages. The public [CyKin repository](https://github.com/hiagokinlevi/CyKin) is the source of teaching content. Course metadata is generated at build time; a selected manuscript and its plan are read from `main` on GitHub when a visitor opens a course. A new chapter is therefore visible without a site rebuild, while new course folders or changed course metadata require a deployment.

## Local development

From this directory:
