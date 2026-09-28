# Ceremonial Entheogen Use in Puerto Rico

A descriptive, cross-sectional survey of participants and facilitators involved in ceremonial entheogen use (psilocybin mushrooms, ayahuasca, and related preparations) in Puerto Rico.

**Study title:** *Ceremonial Entheogen Use in Puerto Rico: A Descriptive Survey of Participants and a Small Facilitator Subsample*

**Investigators:** Yamil O. Ortiz Ortiz (PI) · Jean C. Vélez Rodríguez (corresponding author, jean.velez5@upr.edu) · Julián M. Hernández Torres

**Affiliations:** UPR Río Piedras Center for Interdisciplinary Studies (CIS) · UPR Medical Sciences Campus (RCM) · PR Institute for Psychedelic Science · Colectivo Psicodélico de PR

## Overview

No validated Spanish-language instrument for characterizing ceremonial entheogen use exists for Puerto Rico. This project fielded a purpose-built, anonymous, online, convenience/snowball survey of adults 21+ to describe — not to estimate population prevalence of — who takes part, what substances are used, where and how ceremonies occur, whether preparation/screening practices are followed, and what safety outcomes (including non-consensual contact and crisis experiences) are reported.

The design is unweighted and non-probability. No causal or population-level claims are made anywhere in the analysis or manuscript.

- **Sample:** 100 rows collected (target N = 100); 87 eligible adults reaching the role fork after excluding 13 abandoned blank submissions.
- **Roles:** 72 participants, 8 facilitators, 7 dual-role (not mutually exclusive); 14 explicit screen-outs retained for description.
- **Primary outcome:** `ceremony_good` (ceremony satisfaction, ordinal 0–6), analyzed with nonparametric methods.
- **Safety domain:** non-consensual contact and crisis experiences (e.g., suicidal ideation, panic), added on the analysis team's recommendation.

## Repository structure

```
data/           Survey instrument (KoboToolbox XLSForm) and raw results
analysis/       Python analysis pipeline (data prep, quality flags, statistics, report)
outputs/        Generated statistical report, figures, and tables
manuscript/
  drafts/       v7_draft.tex — approved manuscript source (+ .bbl, .pdf)
  final/        Submission package (compiled manuscript, title page, cover letter, TIFF figures,
                STROBE checklist, source zip); see final/SUBMISSION_CHECKLIST.md
  figures/      Main-text figures (fig1–fig4) and make_figures.py
  references/   references.bib
  sources/      Literature-search and verification audit trail
archive/        Superseded drafts, internal review rounds, and stale outputs (see archive/README.md)
ANALYSIS_PLAN.md      Full analysis rationale and locked methodological decisions
CLAUDE.md              Project operating notes (skip logic, variable definitions, decisions)
```

## Reproducing the analysis

```bash
cd analysis
PYTHONIOENCODING=utf-8 python report.py
```

`PYTHONIOENCODING=utf-8` is required — the data contains Spanish-language text (ñ, á) that crashes under the default Windows cp1252 codec. See [`analysis/README.md`](analysis/README.md) for the module breakdown and [`ANALYSIS_PLAN.md`](ANALYSIS_PLAN.md) for the full rationale behind every methodological decision (role handling, missingness, suppression threshold, correction for multiple comparisons).

## Data

`data/results_7_15_2026.xlsx` contains the raw, anonymized survey responses (100 rows × 354 columns). `data/koboxls.xlsx` is the KoboToolbox instrument definition — its `survey` sheet is the authoritative source for skip/relevance logic and its `choices` sheet defines all value sets. `data/questionnaire_choices.xlsx` is a standalone copy of the choices sheet.

Respondents are anonymous; no identifying information was collected beyond a self-chosen nickname and password used solely for duplicate-submission screening.

## Status

Submission package assembled for the *Journal of Psychoactive Drugs*; see [`manuscript/final/SUBMISSION_CHECKLIST.md`](manuscript/final/SUBMISSION_CHECKLIST.md) for the file manifest and outstanding items, and [`manuscript/JOURNAL_REQUIREMENTS_VERIFIED.md`](manuscript/JOURNAL_REQUIREMENTS_VERIFIED.md) for journal formatting constraints.
