# A3DI Marketing Operations

Code-first marketing management for [A3DI](https://www.a3di.dev) — Advanced Analytics for Actionable Development Insights.

## Quick Start

```bash
# Clone and setup
git clone https://github.com/<your-username>/a3di-marketing.git
cd a3di-marketing
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp config/config.example.yaml config/config.yaml  # Add your API keys
```

## Project Structure

```
a3di-marketing/
├── content/                    # All marketing content
│   ├── posts/
│   │   ├── drafts/            # WIP posts (YYYY-MM-DD-slug.md)
│   │   ├── published/         # Posted content (moved here after publishing)
│   │   └── templates/         # Reusable post templates
│   ├── case-studies/          # Formalized case study docs
│   ├── webinars/              # Webinar outlines, slides, follow-up sequences
│   └── lead-magnets/          # PDFs, checklists, etc.
│
├── scripts/                   # Automation scripts
│   ├── content_gen.py         # AI-assisted content generation from bullet points
│   ├── schedule_post.py       # Push drafts to Buffer/LinkedIn API
│   ├── analytics_pull.py      # Pull LinkedIn analytics into data/
│   ├── lead_tracker.py        # Simple CRM / lead tracking utilities
│   └── utils/
│       └── helpers.py
│
├── pipelines/                 # Automated workflows
│   └── weekly_review.py       # Weekly KPI snapshot + content calendar check
│
├── config/
│   ├── config.example.yaml    # Template (committed)
│   ├── config.yaml            # Actual secrets (gitignored)
│   ├── brand_voice.md         # Tone/style guidelines for AI content gen
│   └── content_calendar.yaml  # Planned content schedule
│
├── data/                      # Local data (gitignored except schemas)
│   ├── contacts/              # Partner/lead contact lists
│   ├── analytics/             # LinkedIn metrics, website stats
│   └── leads/                 # Inbound lead tracking
│
├── assets/                    # Images, logos, PDFs for posts
│   ├── images/
│   ├── logos/
│   └── pdfs/
│
├── docs/                      # Strategy docs & plans
│   └── marketing_plan_2026.md
│
├── .github/
│   └── workflows/
│       └── weekly_digest.yml  # GitHub Action: weekly KPI email
│
├── .gitignore
├── requirements.txt
├── Makefile                   # Common commands as make targets
└── CLAUDE.md                  # Instructions for Claude Code
```

## Core Workflows

### 1. Generate a LinkedIn post from project notes
```bash
# Jot bullet points into a draft, then let AI flesh it out
make draft slug=survey-design-tips
# Edit the generated draft in VS Code, then schedule
make schedule file=content/posts/drafts/2026-03-01-survey-design-tips.md
```

### 2. Weekly review
```bash
make weekly-review
# Outputs: KPI snapshot, upcoming content calendar items, overdue drafts
```

### 3. Track a new lead
```bash
python scripts/lead_tracker.py add --name "Jane Doe" --org "UNICEF" --source "linkedin" --notes "Interested in data pipeline training"
```

### 4. Pull analytics
```bash
make analytics
# Pulls LinkedIn post performance into data/analytics/
```

## Content Naming Convention

All content files follow: `YYYY-MM-DD-slug.md`

Example: `2026-03-15-five-survey-mistakes.md`

Each file has YAML frontmatter for metadata (see templates).

## Key Make Targets

| Command | Description |
|---------|-------------|
| `make draft slug=<name>` | Create a new draft from template |
| `make generate file=<path>` | AI-generate content from bullet points in a draft |
| `make schedule file=<path>` | Schedule a post via Buffer API |
| `make analytics` | Pull latest LinkedIn analytics |
| `make weekly-review` | Run weekly KPI + calendar review |
| `make leads` | Show current lead pipeline |
