---
name: case-study
description: Scaffold a new case study for the a3di.dev website. Creates the content component, adds metadata, and wires it into the router.
argument-hint: [slug]
disable-model-invocation: true
---

# Scaffold a Case Study

You are creating a new case study page for the a3di.dev React website.
The React site lives at `../website/landing_page_react/` relative to this repo root.

## Inputs

- **Slug:** `$ARGUMENTS` (must be kebab-case, e.g. `wfp-dashboard`)

If `$ARGUMENTS` is empty, ask the user for a kebab-case slug before proceeding.

## Step 1 — Read brand voice

Read `config/brand_voice.md` and keep the tone guidance in mind for all content you write. Key points:
- Practitioner-first, grounded, clear, confident but humble
- Write like a senior colleague, not a consulting firm
- Use "programme" not "program"; avoid "synergy", "leverage", "unlock", "cutting-edge"

## Step 2 — Gather project details

Ask the user for the following details. Present this as a single structured prompt. The user can answer inline or say "skip" for optional fields:

| Field | Required | Example |
|-------|----------|---------|
| Title | yes | "Uncovering Who Is Furthest Behind" |
| Subtitle | yes | "Multi-country MCHN equity analysis for Alive & Thrive" |
| Client name | yes | "Alive & Thrive (FHI Solutions)" |
| Sector | yes | "Maternal & child health and nutrition" |
| Countries | yes | "Cambodia, Lao PDR, Viet Nam" |
| Duration | yes | "April–December 2022" |
| Tags (2–4) | yes | ["MCHN", "Southeast Asia", "Data Pipelines"] |
| Additional metaBar items | no | e.g. Data: "15+ survey rounds, 2000–2023" |
| Challenge narrative | yes | 2–3 paragraphs describing the problem |
| Approach narrative | yes | 2–4 paragraphs describing what A3DI did |
| Result narrative | yes | 2–3 paragraphs describing outcomes |
| Key takeaway | yes | 1–2 sentences for the TakeawayBox |
| Mermaid diagram | no | Flowchart or sequence diagram code |
| Code snippet | no | Config example with filename |
| Client logo filename | no | "client_logo.png" (must be placed in public/img/) |

## Step 3 — Create files

Read `.claude/skills/case-study/template.md` for the exact file patterns, then create/modify these three files. All paths below are relative to `../website/landing_page_react/`:

### 3a. Content component (NEW file)

Create `../website/landing_page_react/src/content/case-studies/$ARGUMENTS.jsx`

- Import only the components you need (`CaseStudySection` is always needed; `MermaidDiagram`, `CodeBlock`, `TakeawayBox` are conditional)
- Export a default function component named in PascalCase derived from the slug (e.g. `wfp-dashboard` → `WfpDashboardContent`)
- Use `&amp;` for ampersands, `&apos;` for apostrophes in JSX text
- All paragraph text uses className `text-[0.95rem] leading-[1.7]`
- TakeawayBox heading uses className `font-bold text-[1.3rem] mb-3`
- Only include `MermaidDiagram` or `CodeBlock` if the user provided that content

### 3b. Metadata entry (EDIT existing file)

Append a new object to the array in `../website/landing_page_react/src/content/caseStudies.js`. Follow the exact structure from the template. Set:
- `ogUrl` to `https://www.a3di.dev/case-studies/$ARGUMENTS`
- `ogImage` to `https://www.a3di.dev/img/optimized_logo.png`
- `clientLogo` and `clientLogoAlt` only if the user provided a logo filename

### 3c. Router wiring (EDIT existing file)

In `../website/landing_page_react/src/pages/CaseStudyDetailPage.jsx`:
- Add an import for the new content component, placed after existing imports
- Add the slug → component mapping to the `contentMap` object

## Step 4 — Remind about assets

After creating the files, remind the user:
- If they specified a client logo, it needs to be placed at `../website/landing_page_react/public/img/<filename>`
- To preview: run `npm run dev` from `../website/landing_page_react/` and navigate to `/case-studies/$ARGUMENTS`
- The case study will automatically appear on the homepage case studies section via the metadata array
