# Revision notes — early draft → v1_draft.tex (Phase 3) → v2_draft.tex (Phase 4)

Source of the early draft: [`ceremonial_entheogen_pr_manuscript.md`](../../ceremonial_entheogen_pr_manuscript.md)
(written from `outputs/report.md` alone, before Phases 0–2).
Every number in v1 traces to [`outputs/report_v2.md`](../../outputs/report_v2.md) or to a direct
recomputation from `data/results_7_15_2026.xlsx` (noted below where that applies).

## Author decisions applied in this phase

| Decision | Applied as |
|---|---|
| Fielding window: report the data-derived range | Methods states 24 Feb – 9 Jun 2026. The plan's stated 12 May close is contradicted by the data: one submission arrived 9 Jun 2026 |
| Disclosures: draft standard text for review | Author contributions, funding, competing interests, data availability, and generative-AI statements are drafted and marked `UNCONFIRMED` in the `.tex` source |
| Word budget: strict ≤4,000 | Introduction–Discussion measures **4,000 words** (Intro 453, Methods 1,201, Results 1,251, Discussion 1,095). Achieved by moving five result domains to the supplement, not by cutting caveats. Abstract 180/200 |
| Output: LaTeX + local TeX toolchain | TinyTeX installed; `v1_draft.pdf` (26 pp.) and `supplement.pdf` (9 pp.) compile locally with `chicago.bst` |

## Structural changes

- **Analytic sample N = 87 → N = 73.** The 14 explicit screen-outs are dropped from the analytic sample and
  reported only as a 16% screening yield in Methods, per the locked author decision. Every affected
  denominator, the abstract, and the conclusion were repatched.
- **Abstract rewritten**: structured (249 words) → unstructured (180 words), per the verified JPD
  requirement. The four Background/Methods/Results/Conclusions headers are gone.
- **Limitations folded into Discussion** as §4.5, with the Conclusion as §4.6, so the whole
  Introduction-through-Discussion block sits inside the 4,000-word cap without an ambiguous section
  boundary.
- **Reference style**: Chicago author-date via `natbib` + `chicago.bst`, not APA.
- **Five domains moved to `supplement.tex`**: facilitator self-report detail, all four BH-corrected test
  families, the exploratory proportional-odds model, the legal-knowledge results, the psychometric
  evidence, the instrument skip-logic errors, the duplicate adjudication, and the qualitative scaffold.

## Numbers corrected

Three corrections beyond the N=87→73 cascade. The first two matter because the early draft reported
**test-table subgroup counts as if they were item-level distributions** — those tables count respondents
who answered *the outcome* within each predictor group, not everyone who answered the predictor. Recomputed
directly from the raw data:

| Item | Early draft | v1 (correct) |
|---|---|---|
| Self-directed preparation | "52 prepared, 6 sometimes, 5 not" (implied base 63) | Base **67**: 55 yes (82%), 6 sometimes (9%), 6 no (9%) |
| Spoke to a health professional | "7 to 8 … against 47 to 50" | Base **65**: 8 yes (12%), 54 no (83%) |
| Screening questions asked | 39 / 15 / 7, base unstated | Base **66**: 39 (59%), 15 (23%), 7 (11%), plus 5 "prefer not to answer" |

The primary comparison is unaffected — it correctly uses the outcome-answering base (58 vs. 5). v1 now
states explicitly why that 5 differs from the 6 in Table 3 (one no-preparation respondent did not answer
the satisfaction item), which the early draft left as an unexplained discrepancy.

Also patched from Phase 1: substance counts and base n (magic mushrooms 50/75% … ketamine <5, base 67),
residency base n = 72, `exp_crisis` base pinned to 7 of 8, the zero-of-54 no-practices count, the tie-aware
permutation p = 0.024 alongside the asymptotic p = 0.041, and ε² truncation at zero.

## Gaps closed

- **`[not reported in source]` markers: all removed.** Recruitment channels, sampling strategy, inclusion
  and exclusion criteria, anonymity procedure, and instrument development come from the proposal narrative;
  IRB number and date, fielding window, and the consent procedure come from the author decisions and
  `data/Hoja Informativa uso ceremonial de enteogenos Final.md`.
- **All six `[CITATION NEEDED]` markers resolved** from `references.bib` (26 verified entries).
- **Novelty claim narrowed** to first characterization of *ceremonial/facilitated* entheogen use practices
  in Puerto Rico, with the team's companion psilocybin survey cited explicitly in the Introduction rather
  than left to surface in Discussion.
- **Duplicate adjudication** moved from an open submission blocker in Limitations to a closed Methods step
  (zero exclusions required), with the full reasoning in the supplement.

## v1 → v2_draft.tex (Phase 4, figures)

The only body change is the figure block; no result, number, or sentence of the manuscript text moved.

| Figure | v1 | v2 |
|---|---|---|
| 1 Sample-construction flow | Placeholder `\fbox` | Generated diagram: 100 → 13 abandoned → 87 → 14 screen-outs → N=73, the three role boxes, the two branches (72 / 8), and the unlinked-branch constraint marked in-figure |
| 2 Substances | `outputs/figures` version, count labels only | Count **and** percentage of base per bar, base n on the axis, `<5` masking stated in-figure |
| 3 `ceremony_good` | Same, with in-figure title | Title dropped, per-bar counts, median called out, and the 51/63 (81%) ceiling bracketed |
| 4 Preparation vs. satisfaction | Boxplot + jittered points | Jitter replaced by one marker per score with area proportional to tie count (35 of 58 tie at 6, so jitter was unreadable); `EXPLORATORY` badge and the n=5 caveat carried in-figure |

- All four are generated by [`manuscript/figures/make_figures.py`](../figures/make_figures.py) from
  `analysis/data_prep.py`, so every count in every figure recomputes from the raw data rather than being
  typed in. 600 dpi PNG, above the JPD 300 dpi colour minimum.
- In-figure titles are dropped throughout — the LaTeX caption carries the title (author decision).
- Figures are set at `\textwidth`, one per page; the draft is 28 pp. (was 26).
- Captions now state base n, the masking rule, and the marker convention where it applies.
- **`graphical_abstract.png` is deliberately not in the `.tex`.** JPD does not list a graphical abstract as a
  submission element (`JOURNAL_REQUIREMENTS.md`), so it is built to satisfy repo policy and to have a
  shareable summary asset, without spending a figure slot in the submission.
- The optional facilitator-practice figure (n=8) was **not** built: with 7–8 answering and `n<5` masking,
  most cells are suppressed or single-case, and plotting it would imply more resolution than the data has.
  It stays as supplement Tables 6–7.

## v2 → v3_draft.tex (Phase 5, peer review)

Every finding in [`manuscript/PEER_REVIEW.md`](../PEER_REVIEW.md) was applied, together with the four
author decisions taken this session. Where the review offered a choice, its stated recommendation was
followed. The disposition table in `PEER_REVIEW.md` is marked accordingly.

### Author decisions taken this session (2026-08-13)

| Question | Decision | Applied as |
|---|---|---|
| R9 — consent-documentation waiver | The consent sheet was embedded in the questionnaire; reading it and proceeding constituted consent, and the IRB approved that procedure as submitted | Methods §2.1 now states the procedure and that it was approved as described, so no signed document was required |
| R10 — competing interests | Disclose the organizational affiliations | Competing-interests statement now names the Puerto Rico Institute for Psychedelic Science and the Colectivo Psicodélico as potential non-financial competing interests and declares no financial interests; still needs per-author confirmation |
| P1-10 — "pre-declared" | "Specified before testing, not before seeing data" | Abstract, §2.5, §3.6 now say the comparison was *designated in the analysis plan as the primary comparison before any test was run*, plus an explicit "the study was not preregistered, and the analysis plan was written after data collection" in §2.5. `ANALYSIS_PLAN.md` quotes the outcome distribution, so the stronger "before the outcome was examined" wording would have been false |
| R2 — title | Qualify the facilitator arm | Title is now *"…: A Descriptive Survey of Participants and a Small Facilitator Subsample"* (main text and supplement) |
| IRB body | OPPHI, Medical Sciences Campus | Methods §2.1: "the Institutional Review Board of the University of Puerto Rico, Medical Sciences Campus" |
| Corresponding-author email | `jean.velez5@upr.edu` | Title block |
| Funding | Unfunded, confirmed | `UNCONFIRMED` marker removed |
| Data availability | Commit to a repository deposit | Statement now promises a public deposit of de-identified data and code on publication, with a DOI placeholder |

### Peer-review findings applied

| # | What changed |
|---|---|
| P1-1 | §3.5, supplement §S2, Figure 1, and §4.5 now state that 7 of the 8 facilitators are also participants and that **every** facilitator who answered a substantive facilitator item is one of those 7. The unlinkage claim is restated at the correct level — *ceremony*, not respondent — everywhere it appears, and Limitations adds the non-independence sentence. No analytic decision changed |
| P1-2 | The lifetime-vs-most-recent referent mismatch is disclosed in Methods §2.3, at the point of report in §3.4, in the supplement's safety-family table caption, and in Limitations. Cross-tabs retained |
| P1-3 | `non_con_contact_recent` (2 yes / 62 no / 1 prefer-not-to-answer, base 65) is now reported in the abstract, §3.4, and Table 3, next to the lifetime item, with the 2-of-5 / 3-of-5 split that makes the mismatch concrete |
| P1-4 | The `pause_facil` continuation gate is documented in Methods §2.2, drawn in Figure 1 (3 of 7 dual-role respondents exit; 69 routed), and reflected in the Figure 3 caption and in Tables 2–3 |
| P1-5 | Tables 2 and 3 now carry explicit *structural skip* and *item nonresponse* rows, so Methods' promise is kept. Table 3 became a `longtable` to fit |
| P1-6 | Methods §2.3 states that the outcome is single-ceremony while the exposure is a general practice; §3.3 and supplement §S5 name referent heterogeneity alongside multidimensionality as explanations for α = 0.14 |
| P1-7 | **Option (a), as recommended.** All `<5` masking is gone from the tables, the figures, and `make_figures.py`; every count is exact. Methods §2.4 replaces the suppression sentence with the policy actually in force — anonymous design, aggregate-only reporting, no quoted free text — and says why masking would have been cosmetic |
| P1-8 | Methods §2.2 states that the eligibility criteria were self-assessed and advisory, with the four specific ways they were not enforced |
| P1-9 | "Other" (18, 27%) is restored to Figure 2 and to §3.2, drawn in grey and labelled uninterpretable because only 3 respondents completed its free-text follow-up |
| P1-10 | See the decisions table above |
| P1-11 | "screening yield" is gone; Methods and the STROBE checklist now say 16% of those reaching the role fork screened out |
| P1-12 | The truncation convention moved to the supplement preamble, and the ε² column added to Supplementary Tables S4 and S7 actually uses the † marker (six truncated values). Effect-size columns were added to the substance and safety families at the same time |
| R1 | Introduction ¶4 now states that the contribution does not depend on any test reaching significance |
| R2 | See the decisions table above |
| R5 | "Primary" no longer appears in the abstract or §4.4; the comparison is described as pre-specified |
| R8 | §4.1 now carries comparator numbers: mean age 42.4 and 78% degree-holding here against 37.6 years / 49% (Pagni et al. 2025), 37.0 years (Ruffell et al. 2021), and 40 years / 59% (Nayak et al. 2023), with the 49% women falling inside their 44–61%. Sources and the reason Teixeira et al. and Kopra et al. could **not** be used numerically are in [`sources/search_20260813_comparator_demographics_R8.md`](../sources/search_20260813_comparator_demographics_R8.md) |
| R7, R3, R4, R6 | No change required — the review endorsed the existing text |
| R-refs | Five CrossRef-verified references added (Bouso et al. 2022 ayahuasca adverse effects; Carbonaro et al. 2016 challenging experiences; McNamee et al. 2023 on studying harms; Hartogsohn 2017 set and setting; Bethlehem 2010 web-survey selection bias), taking the bibliography from 26 to 31 |
| P3-1 | Figure 3's caption and the figure itself now decompose the 9-person remainder into 1 "prefer not to answer", 3 structural skips, and 5 item nonresponses |
| P3-2 | Supplementary Tables S2 and S3 both use base 7 (the number who answered any facilitator item), with an explicit note explaining why the base of 8 is not used |
| P3-3 | Both `.tex` header comments now say what is actually true: numbers trace to `outputs/report_v2.md` **except** the distributions and effect sizes recomputed directly from the raw data |
| P3-4 | `final/STROBE_checklist.md` refreshed to v3; items 13a, 13c, and 22 closed; item 10 remains the only open row |
| P3-5 | Applied, plus two defects the review had not caught. `koss1980therapist`: journal is *Social Science & Medicine. Part B: Medical Anthropology*, vol. **14**. `hughes2024ethnoracial`: brace-protected `{eClinicalMedicine}`, and the first author is **Marcus** E. Hughes, not Matthew (CrossRef; PubMed gives "Hughes ME"). `bouso2016measuring`: full journal title. `golden2022effects`: retyped `@incollection`, and CrossRef gives **Tasha L.** Golden, **Clara C.** Sandu, **Shuyang** Lin, and **Kathy M.** Shi against the bib's Thea/Cristina/Shiqi/Kevin. `marcus2026psychedelics`: online-first date recorded in a `note` |
| P3-6 | Still open by design — the five Online First entries must be re-checked immediately before submission |
| P3-7 | Generic "(Supplementary Material)" pointers replaced with §S2, §S6, §S7, §S8 and Tables S1, S4–S9 |
| P3-8 | "labelled" → "labeled" in the Figure 2 caption |

### Word budget

The accepted revisions added roughly 700 words of mandated disclosure to a manuscript that was already at
the 4,000-word cap, so the whole body was rewritten more tightly rather than allowed to grow: statistics
that Tables 1–3 and Supplementary Tables S4–S7 already carry were cut from the prose, the facilitator
results were condensed against the supplement, and the protocol-deviation and duplicate-screening
paragraphs were compressed. Measured with the same script used through Phase 3
(`Introduction`–`Discussion`, inline math and `\cite*` commands dropped), the body went from **4,872 words
before trimming to 4,318**, against **4,123 for v2** — that is, about 200 words above v2's measured length,
which the Phase-5 review scored at ~3,870. **Expect to need a final ~50–100-word trim at submission**, and
note that the counting convention matters: v2 was declared compliant at 3,870 by a count this script
reproduces as 4,123. The abstract is at 200 words against the 200-word cap.

### Figures

All four regenerate from `manuscript/figures/make_figures.py`, which no longer imports `SUPPRESS_N` or
`mask`. Figure 1 gained the continuation-gate exit and grew to 8 inches tall (set at `0.94\textwidth` so it
fits with its caption); Figure 2 gained the "other" bar and lost its masking note; Figure 3 gained a
missing-data decomposition line; Figure 4 no longer draws a box over the five no-preparation observations,
plotting them as raw points with a median tick instead, per the review's minor point.

## Open items after Phase 5, round 1

Items 1–3 of the Phase-4 list are closed: the IRB body is named (OPPHI, Medical Sciences Campus), the
corresponding-author email is `jean.velez5@upr.edu`, and funding, competing interests, and data
availability are settled. What remains:

1. **Two disclosure statements still marked `UNCONFIRMED`**: author contributions (CRediT roles drafted
   from the protocol, never confirmed by the co-authors) and the generative-AI use declaration (scope to be
   verified). The competing-interests statement is now written but needs each author to confirm the
   affiliations it discloses on their behalf.
2. **Data-availability DOI placeholder.** The statement now commits to a public repository deposit on
   publication; the repository and DOI must be chosen and filled in before submission.
3. **Five references are Online First** and need a pagination recheck immediately before submission
   (`carvalho2025scoping`, `pagni2025longterm`, `robinson2026field`, `teixeira2026ayahuasca`,
   `velezrodriguez2026psilocybin`; flagged in `references.bib` notes). BibTeX emits a "no number and no
   volume" warning for each on every build, which is the reminder.
4. **A final word-count trim of roughly 50–100 words** may be needed depending on how the journal counts;
   see the word-budget note above.
5. **No a priori power calculation exists.** The N=100 target came from the protocol. STROBE item 10 states
   this plainly rather than retrofitting a justification; a reviewer may raise it.

## v3 → v4_draft.tex (Phase 5, round 2 peer review)

Every finding in [`manuscript/PEER_REVIEW_R2.md`](../PEER_REVIEW_R2.md) was applied. Unlike round 1, none of
round 2's findings required a new author policy decision — each had one clearly lower-risk fix. Full
verification method: a background agent independently recomputed nearly every number in both `.tex` files
directly from the raw data (two small discrepancies found, both fixed); a second background agent's
reference re-check was itself independently re-verified and extended by direct calls to the CrossRef REST
API for all 28 DOI-bearing entries, which surfaced more errors than the agent's own pass caught.

### Findings applied

| # | What changed |
|---|---|
| R2-1 | Word budget was still ~295–400 words over the JPD's verbatim 4,000-word cap — item 4 of round 1's open-items list, never actually done. Trimmed by referencing Tables 1–3/Figures 1–4 instead of repeating their exact counts in prose (Methods §2.2–2.4, Results §3.1–3.3, §3.5), tightening non-caveat clauses in Methods §2.1/2.6 and Discussion §4.1/4.2, and substantially compressing the Conclusion, which had come to restate the Abstract almost in full. No caveat, hedge, or disclosure sentence from round 1 was cut — only redundant restatement of numbers already in a table, a figure caption, or the abstract. Measured **3,947 words** (citations excluded, the convention used throughout this project), down from 4,295; by section, Introduction 419, Methods 1,173, Results 1,166, Discussion 1,189 |
| 3a | 8 of 31 references had author-name errors (21 individual fields), found by re-verifying every author array directly against CrossRef rather than trusting title/DOI/journal matching alone. Two entries were missing a real co-author outright: `ruffell2021ceremonial` (Antonio Inserra, added between Davies and Butler) and `nayak2023naturalistic` (Heather Jackson, added before Garcia-Romeu — distinct from Hillary Jackson, the 2nd author). The other 6: `carvalho2025scoping` (Louise→Laura Carvalho), `siegel2023psychedelic` (Jacob→Joshua Siegel, Julia→James Daily), `gorman2021psychedelic` (Kellianne→Ksenia Cassidy), `pilecki2021ethical` (Jason→Joseph Rhea), `dutton2025harm` (Charlotte→Carissa Dutton, Jamie→Jessica Oliva), `teixeira2026ayahuasca` (Hugo→Helena Amaro, Louise→Laura Carvalho, Mauricio→Maja Kohek). All corrected in `references.bib` and confirmed rendering correctly in the recompiled bibliography |
| 3a-ii | `teixeira2026ayahuasca` was defined in `references.bib` but never actually cited in either `.tex` file — the intent recorded in `sources/search_20260813_comparator_demographics_R8.md` to keep it "for design analogy" was never carried through. Cited in the Introduction alongside `carvalho2025scoping` |
| R2-2 | Methods §2.5 claimed the four BH-correction test families "share neither exposures nor outcome domains." False: `non_con_contact` recurs as an outcome across 3 of 4 families (7 tests total) and `screening_quest` recurs as predictor/outcome across 3 of 4 (6 tests total). Corrected in `v4_draft.tex` §2.5 **and**, caught only during the PDF visual-formatting pass, in `supplement.tex` §S3's own preamble, which repeated the identical incorrect sentence. No q-value is affected — every family already has all q's above 0.05 |
| R2-3 | Two prose numbers didn't match their own tables, both caught by independent recomputation: §3.4's claim of "median 3 in every subgroup" for comfort/safety by facilitator-background knowledge is wrong for the 2-person "no" subgroup (actually median 2.0) — now scoped to "both facilitator-background subgroups large enough to characterize." Supplement §S3's legal-worry median for the disclosure="si" group was stated as 2, actually 1.5 — corrected in place |
| R2-4 | The trust-by-facilitator-background test (the only nominally-significant result in the bivariate family) didn't get the tie-aware permutation robustness check the paper already applies to the primary comparison. Computed directly (10,000 permutations, seed 20260715): $p=0.010$, slightly *below* the asymptotic $p=0.017$, so the addition reinforces rather than undercuts the result. Also corrected: the "no"-background group has only 3 non-missing trust values, not 4 as Table 3's category count would suggest (one of the 4 has a missing trust score) |
| R2-5 | Data availability called the future deposit "de-identified survey data" while Methods says no identifiers were ever collected (anonymous by design, not de-identified after the fact). Changed to "anonymous survey data" |
| 3a-iii | Online-First pagination recheck: all 5 flagged entries (`carvalho2025scoping`, `pagni2025longterm`, `robinson2026field`, `teixeira2026ayahuasca`, `velezrodriguez2026psilocybin`) confirmed still unpaginated as of 2026-08-14, one day after round 1's check. No `.bib` change |

### Verification

Both `.tex` files compile clean: `pdflatex` (×3) + `bibtex`, zero errors, only the expected 5 "no number and
no volume" BibTeX warnings for the Online-First entries (previously 4 — `teixeira2026ayahuasca` now appears
because it's cited, confirming 3a-ii is fixed) and pre-existing cosmetic underfull-hbox warnings in table
cells unrelated to this revision. `v4_draft.pdf` is 29 pages (was 30), `supplement.pdf` is 9 pages (unchanged).
Every page of both PDFs was rendered to an image and visually inspected for overlap, truncation, or
misplacement; none found. Re-ran the citation-key consistency check (all 31 `.bib` keys defined and cited,
none orphaned) and the word-count script after every edit round rather than only at the end.

## Open items after Phase 5, round 2

Unchanged from round 1's open-items list above — none of round 2's findings touched author contributions,
the generative-AI declaration, the data-repository/DOI choice, or the power-analysis question, per the
author's explicit instruction to leave those flagged as before. Additionally:

6. **Citation pattern worth watching**: all 8 defective references from finding 3a were recent (2020–2026),
   multi-author, non-Puerto-Rico-specific papers with plausible-sounding name substitutions (Ksenia→Kellianne,
   Joshua→Jacob, etc.), not random corruption. If any further references are added before submission, verify
   every author name directly against CrossRef, not just the title/DOI/journal — that check is what caught
   these, and a lighter check (title/DOI only, which is what round 1's Pass 3a and this round's first
   background-agent pass both did) would have missed most of them.
