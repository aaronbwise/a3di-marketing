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
