# Manuscript Plan — Ceremonial Entheogen Use in Puerto Rico

Companion to [`ANALYSIS_PLAN.md`](ANALYSIS_PLAN.md). Covers the path from the current early draft
([`ceremonial_entheogen_pr_manuscript.md`](ceremonial_entheogen_pr_manuscript.md)) to a submission-ready
manuscript.

## Locked decisions

| Decision | Choice |
|---|---|
| Target journal | **Journal of Psychoactive Drugs** (Taylor & Francis) |
| Primary claim | **First-of-kind descriptive characterization** of ceremonial entheogen use in PR |
| Blockers | **Resolve by re-running `analysis/`** against the raw data — not flagged for authors |
| Format | **LaTeX + BibTeX → PDF**, English |

Safety and instrument/psychometric findings are supporting sections, not the headline. Everything the
analysis established stands: descriptive only, unweighted, no prevalence or causal claims, n<5 suppression.

## Directory convention

Manuscript work lives in `manuscript/` inside this project, parallel to `analysis/` and `outputs/`:

```
manuscript/
├── drafts/          v1_draft.tex, v2_draft.tex, revision_notes.md
├── references/      references.bib
├── figures/         manuscript figures (symlink/copy from outputs/figures where reused)
├── sources/         ALL literature-search and web-research output (-o flag, mandatory)
├── review/          page images for PDF formatting QA (deleted after)
└── final/           manuscript.tex, manuscript.pdf, STROBE_checklist.md, cover_letter.md
```

This deviates from the parent repo's `writing_outputs/<timestamp>_<desc>/` convention, deliberately: this
project already has an established `analysis/` + `outputs/` layout and the manuscript must sit beside the
analysis it reports.

---

## Phase 0 — Scaffolding and journal requirements

**Skills:** `venue-templates`, `parallel-web`

1. Create `manuscript/` tree above.
2. `venue-templates` → pull the Taylor & Francis / JPD template and author guidelines.
3. **Verify, do not assume**, via `parallel_web.py search` (saved to `manuscript/sources/`):
   word limit, abstract format (structured vs. unstructured) and word cap, reference style and cap,
   figure/table limits, whether STROBE is required, data-availability and ethics-statement requirements,
   APC/open-access options.
4. Record verified requirements in `manuscript/JOURNAL_REQUIREMENTS.md`. Every downstream length and
   formatting decision cites this file.

**Gate:** structure of the manuscript is not fixed until this file exists. The current draft's 249-word
structured abstract and section layout are provisional.

---

## Phase 1 — Resolve the open analysis items

**Tools:** existing `analysis/` pipeline. `PYTHONIOENCODING=utf-8 C:/Users/jeanv/miniforge3/python.exe`

This phase runs **before** drafting, because three of its outputs are numbers that appear in the abstract.

### 1a. Duplicate adjudication + sensitivity re-run — *the submission blocker*
`outputs/tables/data_quality_flags.csv` flags 2 rows sharing an identical nickname+password, 9 repeated
nicknames, 12 repeated passwords, and 2 rows with >1 failed attention item. Per protocol these were flagged,
never dropped.

- Adjudicate: inspect flagged rows side by side on timestamp, sociodemographics, and free-text style to
  classify each as true duplicate vs. coincidence (common nickname/password strings).
- Re-run the full pipeline excluding adjudicated true duplicates; produce a **sensitivity table** comparing
  primary and safety results before/after.
- Manuscript reports the primary analysis on the full retained sample with the sensitivity re-run as a
  Methods-declared robustness check. If conclusions flip, that reverses — the adjudicated sample becomes primary.
- **Author decision required:** adjudication criteria are a judgment call. I will propose explicit rules and
  the classification table for sign-off before the re-run is treated as final.

### 1b. Reporting gaps to close from the data
- **Per-substance counts and base n** for the substances-used figure (currently rank-order only — a headline
  descriptive result reported ordinally). Add numeric labels to `fig_substances.png`.
- **Base n for the residency table** (currently 82/95% with no stated denominator).
- **`exp_crisis` base** — report.md gives it variously as 7, 7–8, and ≈8 across four sections. Pin to one number.
- **Descriptive count** of participants reporting neither preparation, screening, nor prior facilitator
  knowledge (the n=54 index currently masks whether such respondents exist).
- **Exact-test p-value** for the primary preparation comparison alongside the asymptotic one, given n₂=5.
- **ε² sign convention** — negative values (−0.00, −0.02, −0.04) reproduced from the bias-corrected formula
  read oddly to reviewers. Truncate at zero with a footnote, applied uniformly.

### 1c. Instrument documentation from `koboxls.xlsx`
- Verbatim item wording and scale anchors for `ceremony_good`, `comfort_safe`, `trust_level`, `prep_part`,
  `non_con_contact` — reviewers will ask, and `prep_part` anchors the primary analysis.
- Confirm bilingual fielding: whether Spanish and English versions were both deployed by design, and how
  translation equivalence was handled.
- Produce a supplementary instrument table (item → construct → scale → base n).

### 1d. Methods facts recovered from the proposal
The draft marks recruitment/sampling as `[not reported in source]` because it was written from `report.md`
alone. [`data/Narrativa de propuesta uso ceremonial de enteogenos.md`](data/Narrativa%20de%20propuesta%20uso%20ceremonial%20de%20enteogenos.md)
supplies: social-media recruitment (Facebook, Instagram, Twitter, WhatsApp) plus UPR Río Piedras and RCM
bulletin boards; convenience sampling via snowball/chain-referral; explicit inclusion criteria; target N=100.
Extract these verbatim into Methods.

**Still needed from the authors (not in any file):** fielding dates, IRB/CIPSHI approval number and date,
consent procedure as implemented, and whether the study was preregistered.

**Deliverable:** `outputs/report_v2.md` + `manuscript/sources/analysis_resolutions.md` recording every number
that changed and why.

---

## Phase 2 — Literature review

**Skills:** `literature-review` (primary), `research-lookup`, `parallel-web`, `citation-management`

All output saved to `manuscript/sources/` with the `-o` flag. Zero placeholder citations — every reference
verified to exist with complete metadata (volume, pages, DOI) before it enters `references.bib`.

### 2a. Novelty check — run first, because it can change the framing
Systematic search for **any prior Puerto Rico– or Caribbean-specific survey of ceremonial/naturalistic
entheogen use**. Spanish- and English-language, including regional journals (PRHSJ, Salud Pública de México,
Revista Panamericana), theses, and grey literature. Search in both languages.

If prior local work exists, the "first-of-kind" framing must be revised before drafting begins — this is a
gate, not a formality.

### 2b. Six citation gaps in the current Introduction
Each `[CITATION NEEDED]` marker maps to a targeted search:

1. Growth of non-clinical ceremonial and retreat-based psychedelic use in the Americas
2. Asymmetry between clinical-trial and naturalistic/ethnographic psychedelic literatures
3. Puerto Rico's legal status and controlled-substance framework (US federal drug law in a territory)
4. Traditional plant-based and spiritually framed healing practice in Puerto Rico / the Hispanic Caribbean
5. Absence of prior PR-specific survey evidence → satisfied by 2a
6. Harm-reduction, preparation, and screening frameworks in psychedelic settings

### 2c. Comparator literature for the Discussion
- Naturalistic/community psychedelic surveys with comparable descriptive profiles (Global Drug Survey
  psychedelic modules, ayahuasca retreat cohorts, psilocybin naturalistic-use surveys) — for benchmarking
  demographics, settings, and satisfaction ceilings.
- Adverse events and boundary violations in ceremonial and guided settings — the evidence base against which
  5/67 non-consensual contact is contextualized.
- Facilitator training, credentialing, and screening practice in non-clinical settings.
- Ceiling effects in self-reported psychedelic experience measures — supports §4.2's measurement argument.

### 2d. Bibliography build
`citation-management` → `manuscript/references/references.bib`. Metadata completeness pass before any
compile: every `@article` carries volume, pages, and DOI, or a `note` field explaining why not.

**Target:** 45–65 verified references, pending the JPD reference cap from Phase 0.

**Deliverable:** `manuscript/sources/LITERATURE_SYNTHESIS.md` — thematic synthesis mapping every finding in
the paper to the literature it speaks to, plus the populated `.bib`.

---

## Phase 3 — Manuscript drafting

**Skills:** `scientific-writing` (two-stage: outline with key points → flowing prose), `venue-templates`

Flowing prose throughout, no bullet points in the manuscript body. IMRaD. Abstract written last.

The existing draft is a strong Results/Limitations skeleton sourced faithfully from `report.md` — it is
**reused, not rewritten**, for §2.3–§2.6, §3, §5. The work concentrates on Introduction, Discussion, and the
Methods facts recovered in Phase 1. 

### Section-by-section

| Section | Action | Source |
|---|---|---|
| Introduction | **Rewrite.** Six citations resolved, novelty claim grounded in 2a, PR context substantiated | Phase 2 |
| Methods §2.1 Design | Light edit | draft + proposal |
| §2.2 Recruitment/sample | **Rewrite** — remove `[not reported in source]`, insert proposal facts, add IRB/dates once supplied | Phase 1d |
| §2.3 Instrument | **Expand** — verbatim item wording, scale anchors, bilingual fielding | Phase 1c |
| §2.4 Missing data/suppression | Keep; add duplicate-adjudication rule | draft + Phase 1a |
| §2.5 Statistical approach | Keep; add exact test, ε² convention | draft + Phase 1b |
| §2.6 Protocol deviations | Keep — this section is a strength, it is what makes the design constraints visible | draft |
| Results §3.1–3.6 | Keep structure; patch every resolved number; add substance counts | draft + Phase 1 |
| Discussion | **Substantially expand** — currently sourced only from the report, needs the comparator literature to say how this sample compares to naturalistic cohorts elsewhere | Phase 2c |
| Limitations | Keep; update duplicate paragraph to report the adjudicated sensitivity result | draft + Phase 1a |
| Conclusion | Light edit for consistency with resolved numbers | draft |
| Abstract | **Write last**, to the JPD-verified format and word cap | — |

### Reporting compliance
STROBE checklist for cross-sectional studies, completed and saved to `manuscript/final/STROBE_checklist.md`,
regardless of whether JPD mandates it. Reviewers of a non-probability survey will look for it.

### Supplementary materials
Instrument table, full BH-corrected test family tables (current Table 10), duplicate-adjudication sensitivity
table, qualitative open-text coding scaffold, and the reproducibility statement pointing at `analysis/`.
Moving these to supplement keeps the main text inside the word limit while preserving the audit trail.

---

## Phase 4 — Figures

**Skills:** `scientific-schematics` (primary), `nature-figure` (data figures), `generate-image` (sparingly)

Three publication figures already exist in `outputs/figures/`, but should be replaced as they are not publication ready. Target 5–6 total, pending JPD's figure cap.

| Figure | Status | Tool |
|---|---|---|
| Graphical abstract | **New** — mandatory per repo policy | `scientific-schematics` |
| Sample-construction flow (100 → 87 → role fork, participant/facilitator/dual, unlinked branches) | **New** — the single most important figure; the unlinked-branch structure governs every limitation in the paper | `scientific-schematics` |
| Substances used across ceremonies attended | **Revise** — add numeric labels and base n | `nature-figure` |
| `ceremony_good` distribution (ceiling) | **Revise** to journal spec | `nature-figure` |
| Satisfaction by preparation status | **Revise** — mark exploratory in-figure | `nature-figure` |
| Facilitator practice profile (n=8) | **Optional** — only if suppression leaves anything plottable; likely stays a table | `nature-figure` |

Every figure carries its own base n in the caption. No denominator carried across figures. Figures should follow the aesthetic in figures/example.png and figures/example.py.

---

## Phase 5 — Peer review

**Skills:** `peer-review` (primary), `scientific-critical-thinking`, `scholar-evaluation`

Three passes on the compiled PDF, each written to its own file, each producing a revision round with an
incremented draft version:

1. **Methodological rigor** (`scientific-critical-thinking`) — does every claim stay inside what a
   non-probability n=87 descriptive design supports? Hunt for creeping generalization, especially in the
   Discussion. Verify the unlinked-branch constraint is never violated.
2. **Journal peer review simulation** (`peer-review`) — full reviewer report as a JPD reviewer would write it.
   Anticipated attacks: self-selection, the k=5 safety cell, the n=5 no-preparation group, the ceiling effect,
   duplicate adjudication, facilitator n=8, and whether a descriptive paper with no significant corrected
   result clears the bar.
3. **Citation and reporting integrity** (`citation-management` + `scholar-evaluation`) — every reference
   verified real with complete metadata, every in-text number traced back to `report_v2.md`, STROBE
   completeness.

**Deliverable:** `manuscript/PEER_REVIEW.md` with a point-by-point response table, and the revisions applied.

---

## Phase 6 — Compile and QA

1. `pdflatex → bibtex → pdflatex × 2`
2. **PDF formatting review via images** — never read the PDF directly:
   `python scripts/pdf_to_images.py manuscript.pdf manuscript/review/page --dpi 150`, inspect each page for
   overlaps, float placement, margins, caption spacing, bibliography formatting. Fix and recompile, max 3
   iterations. Delete `manuscript/review/` after.
3. Cover letter drafted to JPD.
4. `manuscript/SUMMARY.md` — deliverables, file map, submission checklist.

---

## Decisions still needed from the authors

Flagged now so they do not block later. Phases 0–2 proceed without them.

1. **Ethics and fielding** — IRB/CIPSHI approval number:  2509472552 and date: November 4th, 2025, fielding dates: gathered data from February 24, 2026 to May 12th, 2026, consent procedure can be found at data\Hoja Informativa uso ceremonial de enteogenos Final.md, no preregistration.
2. **Authorship and affiliations** — The order is the one in data\Narrativa de propuesta uso ceremonial de enteogenos.md, Jean velez is the corresponding author. Pending: contributions statement, funding and
   conflict-of-interest disclosures.
3. **Disclosure floor for n = 5.** Three figures state exact n=5 counts (no-preparation group, affirmative
   non-consensual-contact cell, crisis-response cell) because the analysis reported them as exact. If study
   policy treats n=5 as suppressible, those three figures change and the 7.5% prevalence loses its k.
   *Affects the abstract — needed before Phase 3.*
   Answer: Do not suppress at n = 5. I would like to report the information as complete as possible. The people will not be identifiable by this information.
4. **Sensitive cross-tabs.** The research team elected to publish the non-consensual-contact cross-tabs under
   cell masking rather than withhold them, with some masked cells near case level.
5. **Qualitative corpus.** 285 open-text answers across 37 fields, with a coding scaffold already built. Keep
   as a brief descriptive paragraph in this paper.
6. **The 14 screen-outs.** Retained in N=87 "to describe who screens out," but no analysis describes them.
   Drop them from the analytic sample and report them as screen-outs only. They should only be accounted for in the narrative flow of how participants were screened. 

---

## Sequence and gates

```
Phase 0 (journal reqs) ──┐
Phase 1 (data resolution)─┼──> Phase 3 (drafting) ──> Phase 4 (figures) ──> Phase 5 (review) ──> Phase 6 (compile)
Phase 2 (literature) ────┘
```

Phases 0, 1, and 2 are independent and run concurrently. Phase 3 does not start until all three complete —
drafting against unresolved numbers or an unverified novelty claim means rewriting the Introduction and
abstract twice.

**Hard gates:**
- Phase 2a finds prior PR-specific work → framing revised before any drafting.
- Phase 1a duplicate adjudication reverses a conclusion → adjudicated sample becomes primary.
- Author decision #3 on the n=5 floor → resolved before the abstract is written.
