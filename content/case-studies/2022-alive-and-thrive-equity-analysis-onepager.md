---
title: "One-pager: Alive & Thrive MCHN equity analysis"
format: pdf-one-pager
status: draft
date_created: "2026-02-27"
notes: "Export to PDF via Canva or Google Docs. Keep to one page."
---

# Uncovering Who Is Furthest Behind
### A Multi-Country MCHN Equity Analysis

**Client:** Alive & Thrive (FHI Solutions) | **Sector:** Maternal & child health and nutrition
**Countries:** Cambodia, Lao PDR, Viet Nam | **Duration:** April–December 2022

---

### Challenge

Alive & Thrive needed to understand whether two decades of progress in maternal and child health and nutrition was reaching the most vulnerable populations across three Southeast Asian countries. The evidence existed in 15+ nationally representative survey rounds, but it was scattered across dozens of files with inconsistent variable names, coding schemes, and questionnaire structures.

### Approach

A3DI built a **configuration-driven Python pipeline** to harmonize MICS and DHS survey data across all three countries and 20+ years. The pipeline:

- Standardised variables via **JSON config files** (new country = new config, not new code)
- Merged household and individual records with unique mother-child identifiers
- Computed MCHN indicators for both **health service delivery** (ANC, institutional delivery, postnatal care) and **infant feeding practices** (exclusive breastfeeding, dietary diversity, minimum acceptable diet)
- Applied **survey weights** for nationally representative estimates
- Produced **disaggregated tabulations and logistic regression models** by wealth, ethnicity, geography, education, and urban/rural residence

### Result

- Overall MCHN indicators improved, but **progress was deeply uneven**
- Wealth-driven disparities persisted; poorest households catching up slowly from a very low base
- **Ethnic and regional gaps exceeded 35 percentage points** in Lao PDR
- Health service **access** expanded, but **quality of care** lagged behind
- A&T used findings for **country strategies, donor advocacy, and regional knowledge products**
- Pipeline designed as a **reusable asset**, extensible to new countries and survey rounds

---

**A3DI** | www.a3di.dev | aaron@a3di.dev
Data analysis, pipelines, and visualisation for development & humanitarian organisations
