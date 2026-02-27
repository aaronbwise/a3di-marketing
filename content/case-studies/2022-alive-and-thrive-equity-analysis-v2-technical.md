---
title: "Harmonizing 20 years of nutrition survey data across three countries"
slug: alive-and-thrive-equity-analysis
client_type: ingo
sector: nutrition
region: southeast-asia
services_used: [data-analysis, data-pipelines, visualisation]
status: draft
date_created: "2026-02-27"
date_completed: "2022-12-10"
publish_to:
  - website
  - linkedin
  - pdf
hook_angle: "technical-first"
---

# Harmonizing 20 Years of Nutrition Survey Data Across Three Countries

## At a Glance

- **Client:** Alive & Thrive (managed by FHI Solutions)
- **Sector:** Maternal, infant, and young child nutrition (MIYCN)
- **Countries:** Cambodia, Lao PDR, Viet Nam
- **Data:** 15+ nationally representative survey rounds (MICS, DHS) spanning 2000–2023
- **Services:** Data harmonization, secondary data analysis, statistical modelling, data visualisation
- **Duration:** April–December 2022

## Challenge

Alive & Thrive wanted to understand how nutrition equity had changed across Cambodia, Lao PDR, and Viet Nam over two decades — who was improving, who was falling behind, and where the gaps were widest. The raw material existed: more than 15 rounds of nationally representative household surveys (MICS and DHS) spanning 2000 to 2023. But these surveys used different variable names, different coding schemes, and different questionnaire structures across countries and years. Turning this patchwork of SPSS files into a coherent, comparable dataset — one that could support trend analysis disaggregated by wealth, ethnicity, geography, and education — was a substantial data engineering challenge before any analysis could begin.

## Approach

A3DI built a configuration-driven Python pipeline that separated data logic from data structure. Instead of writing country-specific or year-specific cleaning scripts, the pipeline used JSON configuration files to map each survey's raw variable names and value labels to a standardised set of indicators. Adding a new country or survey round meant writing a new config file, not new code.

The pipeline processed the full workflow end to end: ingesting raw SPSS files via `pyreadstat`, merging household-level and individual-level records, generating unique identifiers to link mothers and children across datasets, and computing composite MIYCN indicators — exclusive breastfeeding, minimum dietary diversity, minimum meal frequency, minimum acceptable diet, ANC components, institutional delivery, and others. All calculations applied survey weights to produce nationally representative estimates, and the modular design meant each step could be validated independently.

With harmonized datasets for each country, A3DI ran weighted frequency tabulations disaggregated by wealth quintile, geographic region, urban/rural residence, ethnicity of household head, and mother's education — for every indicator, across every available survey year. Bivariate logistic regression models quantified the strength of associations between equity dimensions and nutrition outcomes, comparing the earliest and most recent survey rounds to measure how disparities had shifted over time.

## Result

The analysis revealed that while national-level nutrition indicators had improved across all three countries, progress was uneven. Wealth-driven gaps persisted in most indicators, with some evidence of the poorest households catching up — but slowly and from a very low starting point. In Lao PDR, ethnic and regional disparities in breastfeeding and dietary diversity exceeded 35 percentage points. Access to health services (ANC visits, institutional delivery) had improved substantially, but the quality of care within those services showed far less progress.

A&T used the findings for country-level programming, donor advocacy, and knowledge products shared across the region. Because the pipeline was configuration-driven rather than hardcoded, it could be reused for additional countries or updated when new survey data became available — delivering a reusable analytical asset, not just a set of slides.

## Key Takeaway

Standardising messy, multi-source survey data is often the hardest and most time-consuming part of secondary analysis — investing in a reproducible pipeline upfront pays off every time the analysis needs to be extended or updated.
