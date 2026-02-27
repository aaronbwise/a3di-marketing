# GitHub Profile Update Spec

> Goal: Position your GitHub as the **technical complement** to a3di.dev (the consultancy)
> and aaronbwise.com (the CV). This page should answer: "What does Aaron actually build?"
> Focus on Python, data engineering, and the tools/systems behind the humanitarian work.

---

## 1. Profile Settings (the sidebar)

Update these in GitHub → Settings → Profile:

| Field | Current | Updated |
|-------|---------|---------|
| **Bio** | "Data Analyst. Proficient in ETL operations and survey data analysis with python and R." | "Python developer building data pipelines and analysis tools for humanitarian organisations. ETL, survey data, food security monitoring." |
| **Location** | Rome, Italy | Gainesville, FL |
| **Website** | *(not set?)* | https://www.a3di.dev |
| **Company** | *(not set?)* | A3DI |

**Why this bio works:** It leads with "Python developer" (not "Data Analyst"), which is
the technical identity you want to project on GitHub. Then it contextualises *what kind*
of Python work — pipelines and tools for humanitarian orgs. The keywords (ETL, survey data,
food security monitoring) are both accurate and searchable.

---

## 2. Pinned Repositories

You get 6 pins. Choose repos that showcase **technical skill** and **domain relevance**.

### Current pins:
1. Pacific-ETL-pipeline ✅ Keep — this is your strongest showcase
2. AT_Equity_KHM ✅ Keep — shows analytical depth with real data
3. NHIES_analysis ✅ Keep — Namibia micronutrient work, Python scripts
4. Chess-Variant ❌ Remove — OSU coursework, doesn't align with brand
5. a3di_website ❌ Remove — it's just a static site, not a technical showcase

### Recommended pins (in display order):
1. **Pacific-ETL-pipeline** — your flagship technical project
2. **AT_Equity_KHM** — multi-country nutrition analysis
3. **NHIES_analysis** — Python-based survey analysis
4. **a3di-marketing** — *(once you push it)* shows you run your ops as code
5. *(Future)* A new repo showcasing a reusable tool, e.g., a survey data cleaning library, an mVAM pipeline template, or a Tableau/dashboard data prep script
6. *(Future)* Another project from consulting work or OSU that demonstrates software engineering (Flask app, REST API, database design)

**If you don't have 6 strong repos yet**, 3-4 well-chosen pins are better than 6
mediocre ones. Remove Chess-Variant and a3di_website now, add the marketing repo,
and fill the remaining slots as you build more.

### Improve existing repo READMEs

Your pinned repos need strong READMEs to make an impression. For each, ensure:
- **One-line description** at the top (what it does, in plain English)
- **Tech stack** listed clearly
- **Context** — who it was built for and why (anonymised if needed)
- **How to run it** (even a basic `pip install -r requirements.txt && python main.py`)

Example for Pacific-ETL-pipeline:
```markdown
# Pacific ETL Pipeline

Automated data pipeline for processing food security monitoring data across
WFP's Pacific Island operations. Extracts survey data, cleans and validates
responses, and loads structured outputs for downstream analysis and reporting.

**Tech:** Python, pandas, PostgreSQL
**Context:** Built for WFP's Regional Bureau for Asia and the Pacific
```

---

## 3. Profile README (aaronbwise/aaronbwise/README.md)

Replace the current README with the version below. The key differences from your
current version:

- **Leads with what you build**, not who you are
- **Shows technical stack** in a structured, scannable way
- **Links the three properties** (GitHub → A3DI → CV) with clear purpose for each
- **No generic tool icons** — uses text-based badges instead, which look cleaner and
  are more informative
- **Doesn't rehash** the CV or the consultancy pitch — this is the *builder's* page

---

### Proposed README.md

```markdown
## Hey, I'm Aaron 👋

I build **data pipelines and analysis tools** for humanitarian and development
organisations — mostly in Python, mostly for food security and nutrition programmes.

By day I work at a university; on the side I consult through
[**A3DI**](https://www.a3di.dev), helping UN agencies and NGOs turn messy programme
data into something they can actually use.

---

### What I work with

**Languages & Frameworks**

`Python` · `R` · `SQL` · `Flask` · `HTML/CSS` · `Bash`

**Data & Databases**

`pandas` · `NumPy` · `PostgreSQL` · `SQLite` · `ODK/KoboToolbox` · `Jupyter`

**Analysis & Viz**

`Tableau` · `Stata` · `SPSS` · `matplotlib` · `seaborn`

**Infrastructure & Tools**

`Git` · `GitHub Actions` · `REST APIs` · `Linux` · `VS Code`

---

### What I build

Most of my repos fall into two categories:

🔧 **ETL & pipeline tools** — automated workflows for extracting, cleaning, and
loading humanitarian survey data (see:
[Pacific-ETL-pipeline](https://github.com/aaronbwise/Pacific-ETL-pipeline))

📊 **Analytical projects** — food security and nutrition analyses using DHS, MICS,
and custom survey datasets across multiple countries (see:
[AT_Equity_KHM](https://github.com/aaronbwise/AT_Equity_KHM),
[NHIES_analysis](https://github.com/aaronbwise/NHIES_analysis))

I'm also pursuing a **BS in Computer Science at Oregon State**, which keeps the
software engineering fundamentals sharp alongside the domain work.

---

### Links

| | |
|---|---|
| 🌐 **Consulting** | [a3di.dev](https://www.a3di.dev) — data services for humanitarian & development orgs |
| 📄 **Full CV** | [aaronbwise.com](https://www.aaronbwise.com) |
| 💼 **LinkedIn** | [linkedin.com/in/aaronbwise](https://www.linkedin.com/in/aaronbwise/) |
```

---

## 4. What this README does differently

| Aspect | Current | Updated |
|--------|---------|---------|
| **Opening line** | "Hi! I'm Aaron — a data analyst trained in public health" | "I build data pipelines and analysis tools for humanitarian orgs" |
| **Emphasis** | CS degree pursuit | What you actually build (pipelines, analysis tools) |
| **Technical showcase** | Generic devicons (visual icons for Python, Flask, etc.) | Structured text badges grouped by function |
| **Repo context** | No guidance on what to look at | Categorises repos into ETL tools vs analytical projects with direct links |
| **Brand alignment** | Mentions A3DI as an afterthought in links | A3DI woven naturally into the intro |
| **Tone** | Student/career-switcher | Practitioner who also happens to be studying CS |
| **Differentiation from other sites** | Overlaps with CV | Focuses on *what you build*, not career history |

---

## 5. The three-site ecosystem

Here's how the three properties now complement each other without overlap:

| Site | Purpose | Audience | Leads with |
|------|---------|----------|------------|
| **a3di.dev** | Sell consulting services | M&E officers, programme managers | Services, sectors, credibility |
| **aaronbwise.com** | Professional CV / career history | Anyone evaluating your background | Profile, consolidated experience, education |
| **github.com/aaronbwise** | Technical portfolio | Technical peers, potential collaborators, employers | What you build, tech stack, code |

No duplication. Each site serves a distinct purpose with clear cross-links.

---

## 6. Quick action checklist

- [ ] Update GitHub bio, location, website, company in Settings
- [ ] Replace README.md in `aaronbwise/aaronbwise` repo with new version
- [ ] Unpin Chess-Variant and a3di_website
- [ ] Pin a3di-marketing repo (once pushed)
- [ ] Improve READMEs for Pacific-ETL-pipeline, AT_Equity_KHM, NHIES_analysis
- [ ] (Future) Create and pin 1-2 more repos that showcase reusable tools
