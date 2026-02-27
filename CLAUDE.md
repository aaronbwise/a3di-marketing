# CLAUDE.md — Instructions for Claude Code

## Project Context
This is the marketing operations repo for A3DI (www.a3di.dev), a data consultancy
serving humanitarian and development organizations. Aaron Wise is the sole operator.

## Key Facts
- **Sector:** International development / humanitarian (UN agencies, NGOs)
- **Services:** Survey design, data analysis & pipelines, dashboards, training
- **Expertise areas:** Food security, nutrition, social protection
- **Tone:** Professional but approachable, practitioner-to-practitioner, no jargon-heavy academic style
- **Target audience:** M&E officers, programme managers, data leads at UN/NGOs

## When generating content
- Always read `config/brand_voice.md` before drafting any content
- LinkedIn posts should be 150–300 words, conversational, with a clear takeaway
- Case studies follow the Challenge → Approach → Result structure
- Never fabricate project details — use placeholders like [COUNTRY] or [ORG] if unknown
- Avoid generic marketing language ("synergy", "leverage", "unlock")
- Include a call-to-action where appropriate

## When working with scripts
- Python 3.11+, use pathlib for file paths
- Config loaded from `config/config.yaml` (never hardcode API keys)
- All data outputs go to `data/` directory
- Content files use YAML frontmatter + Markdown body

## File conventions
- Content: `YYYY-MM-DD-slug.md`
- Scripts: snake_case.py
- Data: snake_case.csv or .json

## Related directories (same parent: `INTERNAL/`)
All paths are relative to this repo's root (`INTERNAL/marketing/`).

- **`../website/landing_page/`** — a3di.dev source (static HTML/CSS, deployed via Netlify)
  - Deployable files in `dist/` (no build step — edit directly)
  - CSS variables defined in `dist/css/style.css`:
    - `--primary-color: #3075ff` (blue — buttons, accents, about section background)
    - `--secondary-color: #0d1d3f` (dark navy — headings, body text, footer background)
    - `--dark-color: #002240` (darkest navy — footer, nav)
    - `--light-color: #f4f4f4` (light grey — backgrounds)
  - Bootstrap theme overrides in `dist/css/utilities.css`
  - Font: Montserrat (Google Fonts)
  - Sections: Navbar, Hero ("Better results through data"), Services (4 cards), About, Footer, Contact modal (Netlify Forms + reCAPTCHA)
  - No case studies section yet — adding this is a marketing plan priority
  - Has its own CLAUDE.md at `docs/CLAUDE.md` and update plan at `docs/UPDATE_PLAN.md`
- **`../branding/Fiverr/A3DI/`** — Logo files (PNG/JPG, plus `.ai` source), brand book PDF, mockups, source font zips (Montserrat, Lora)
- **`../data_viz_guide/`** — Chart and data style guides (PDFs: CHART style guide, Intelligence Data Styleguide)
- **`../website/website_text.txt`** — Original website copy (services descriptions, about text)

## Brand tokens
Canonical design tokens are in `config/brand_tokens.yaml`. Reference this file when generating any visual content, checking brand consistency, or working on the website.
