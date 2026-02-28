---
title: "Uncovering who is furthest behind: a multi-country MCHN equity analysis"
slug: alive-and-thrive-equity-analysis
client_type: ingo
sector: mchn
region: southeast-asia
services_used: [data-analysis, data-pipelines, visualisation]
status: draft
date_created: "2026-02-27"
date_completed: "2022-12-10"
publish_to:
  - website
  - linkedin
  - pdf
---

# Uncovering Who Is Furthest Behind: A Multi-Country MCHN Equity Analysis

## At a Glance

- **Client:** Alive & Thrive (managed by FHI Solutions)
- **Sector:** Maternal and child health and nutrition (MCHN)
- **Countries:** Cambodia, Lao PDR, Viet Nam
- **Data:** 15+ nationally representative survey rounds spanning 2000–2023
- **Services:** Data harmonization, secondary data analysis, statistical modelling, data visualisation
- **Duration:** April–December 2022

## Challenge

Alive & Thrive needed to understand how maternal and child health and nutrition outcomes had changed over two decades across Cambodia, Lao PDR, and Viet Nam, and critically, whether progress was reaching the most vulnerable populations. National averages can mask deep disparities: improvements in antenatal care, breastfeeding, or dietary diversity at the country level may not reflect the reality for ethnic minorities, rural communities, or the poorest households. With funding from the Government of Ireland, A&T wanted an evidence base to inform targeted programming, policy advocacy, and donor engagement across the Mekong Sub-Region. But the data sat in dozens of separate survey files, collected using different instruments and variable definitions over more than 20 years.

## Approach

A3DI designed and built a reproducible, configuration-driven analysis pipeline in Python to harmonize data from 15+ rounds of MICS and DHS surveys across the three countries. Each country-year combination required its own mapping of raw survey variables to standardised indicator definitions. These mappings were managed through JSON configuration files rather than hardcoded logic, so the same codebase could process Viet Nam's 2000 MICS and Cambodia's 2021 DHS without modification.

The pipeline handled the full analytical workflow: reading raw SPSS survey files, merging household and individual records, creating unique identifiers to link mothers and children across datasets, and computing standard MCHN indicators spanning both health service delivery (antenatal care, institutional delivery, postnatal care) and infant and young child feeding practices (exclusive breastfeeding, minimum dietary diversity, minimum acceptable diet, and others). All statistics were properly weighted to account for the complex survey designs.

With cleaned, combined datasets in hand, A3DI produced disaggregated frequency tabulations and weighted logistic regression models examining each indicator by wealth quintile, geographic region, urban/rural residence, ethnicity of household head, and mother's education level, across every available survey year. This revealed not just current gaps, but how those gaps had evolved over time.

## Result

The analysis produced a comprehensive equity profile for each country, revealing that while overall MCHN indicators had improved, progress was deeply uneven. Wealth-driven disparities persisted across most indicators, and in some cases the poorest households were beginning to catch up, but from a very low base. Access to health services like antenatal care and institutional delivery had expanded substantially, but the quality of care within those services showed far less improvement. Regional and ethnic disparities remained substantial, particularly in Lao PDR where gaps in breastfeeding and dietary diversity between ethnic groups exceeded 35 percentage points.

A&T used the findings to inform country-level strategies, advocacy with government partners and donors, and as inputs for knowledge products shared across the region. The configuration-driven approach meant the pipeline could be extended to additional countries or updated with new survey rounds without rebuilding the analysis from scratch. A reusable asset rather than a one-off deliverable.

## Key Takeaway

When national averages show progress, disaggregated analysis is the only way to know whether that progress is reaching the people who need it most. Building a reproducible pipeline to do that analysis is what turns a one-time project into a lasting capability.
