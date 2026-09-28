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

---

# Phase 5, round 3 (2026-08-25) — v5 human review → v6

Input was `v5_draft_human_reviewed.md`, Julián and Jean's manual revision of v4 (new author order and
affiliations, rewritten Introduction, restructured Methods, ~300 fewer words). This round applied their four
outstanding comments to it. Full disposition in `manuscript/PEER_REVIEW_R3.md`; only the mechanics are here.

**Applied.** (1) Scattered limitation caveats consolidated into Limitations at the moderate setting the
author chose — seven passages trimmed in Methods, Results, and Discussion, Limitations expanded to absorb
them; the ceiling discussion deliberately left in Discussion because it explains the corrected-family nulls.
(3) KoboToolbox cited at first mention; new `kobotoolbox2026` `@misc` entry using the vendor's own
recommended citation form. (4) New `analysis/missingness.py` produces a four-state per-item decomposition
(`outputs/tables/missingness_by_item.csv` → Supplementary Table S10); the Methods data-quality subsection
grew from one sentence to two self-contained paragraphs, and supplement §S7 was retitled and expanded.

**Not applied.** (2) The "non-prep group only answered 6 or NaN" comment does not reproduce. `prep_part='no'`
has six respondents scoring 0, NaN, 5, 3, 6, 4 — the manuscript, Table 3, and Figure 4 are all correct. Every
categorical column was scanned for a "no"-type group confined to `_6`/NaN; no preparation variable matches.
Left unchanged, documented rather than silently ignored.

**Errors found while doing the above, all corrected.**
- The participant-routed base is **67, not 69**; structural skips are **5, not 3**. The XLSForm relevance is
  `(is_participant='si' and pause_facil='si' and is_facilitator='si') or (is_participant='si' and
  is_facilitator='no')`, and 2 participants answered `pna` to the facilitator role item, matching neither arm
  (rows 70 and 73 — every participant item blank). Drafts since v3 counted only the 3 continuation-gate
  refusals. Per-item bases and every statistic are unaffected; the skip/nonresponse attribution shifts by 2 on
  each participant item. Fixed in Tables 2–3, Figure 1 and 3 captions, the supplement preamble, and in
  `make_figures.py` itself, which gained a `participant_routed()` helper replacing the `pause_facil == 'no'`
  shortcut Figures 1 and 3 both used. Both PNGs regenerated.
- v5's Table 1 age row was computed over all 96 age-answering submissions while labelled `n=72`, and
  contradicted the Abstract. Restored to the analytic-sample values (mean 42.4, SD 11.9, IQR 34.0–50.0,
  range 21–71).
- Two dangling cross-references in v5: the practice-index rows were missing from Table 3 though the Results
  text cites them (restored), and Golden et al. 2022 was left in the reference list with no remaining citation
  (removed — flagged in case the intent was to keep the citation).

**Conversion artifacts repaired.** The `.docx` → `.md` round trip dropped χ², ε², *r*ᵣᵇ, α, the × in
"preparation × integration", and the minus sign on the α CI lower bound (−0.36, which had become 0.36 — a CI
that crosses zero rendered as one that doesn't). All restored.

**Build.** `v6_draft.tex` → 28 pages, `pdflatex` ×3 + `bibtex`, zero errors, zero undefined citations or
references, zero overfull hboxes; the 7 BibTeX warnings are the expected Online-First entries. `supplement.tex`
→ 11 pages, one pre-existing 1.98pt overfull hbox in the S5 table. IMRaD word count **3,451** (cap 4,000),
down from v4's 3,768. A `\texttt` introduced in the supplement this round hit a missing Courier TFM and was
replaced with `\emph` — this build has no Courier dependency anywhere, same as the `\urlstyle{same}` choice
in the main preamble.

## Follow-up to round 3: practice index removed (2026-08-25)

Author instruction after the round-3 pass: remove all harm-reduction practice-index references. This
reverses round 3's E3 restoration of the Table 3 index rows and goes further.

**Manuscript.** Results index paragraph deleted; its one non-statistical finding kept, restated
without index language, on the preceding paragraph ("Among the 54 respondents who answered all three
of preparation, prior knowledge of the facilitator's background, and screening, every one reported at
least one of them"). Protocol deviations reworded — "two branch-specific composites replace the mixed
one" was false on the participant side once the index went, now "a facilitator-side readiness
composite replaces the mixed one" (that composite, supplement Table S3, is a separate measure and
survives). Limitations lost the practice-index sentence, and "mixed first reliability evidence"
became "only preliminary two-item reliability evidence" — "mixed" was carried by the α = 0.14 index
row, and Table S9 now holds only α = 0.58 and α = 0.86. Table 3 lost its four index rows.

**Supplement.** Index rows dropped from Table S4 (bivariate) and Table S6 (safety-domain); Table S9
lost its index row and its caption narrowed; §S5's paragraph explaining the low α removed.

**BH families re-corrected** (author's choice: drop and re-correct rather than leave the withdrawn
tests in the family). Recomputed with `analysis/stats_helpers.bh_fdr`; no q crosses 0.05 either way,
so no conclusion changes.

- bivariate, 6 → 5 tests: prep 3-level 0.359→0.300, comfort by background 0.422→0.407, comfort by
  screening 0.422→0.407, **trust by background 0.102→0.085**, trust by screening 0.679 unchanged.
- safety-domain, 5 → 4 tests: **both non-consensual contact rows 0.236→0.188**, crisis × protocol
  0.238→0.191, crisis × emergency plan 0.536→0.429.

The two bolded values are quoted in the main text and were updated there.

**Kept deliberately.** Limitations still records that the ceremony-level unlinking "eliminated … its
mixed harm-reduction composite" — that names the *protocol's* planned composite and documents why it
could not be built, which is a protocol-deviation statement rather than a reference to the index that
was constructed.

**Build.** `v6_draft.tex` → 28 pages, 0 undefined citations or references, 0 overfull hboxes.
`supplement.tex` → 10 pages (was 11), 0 errors, 0 overfull hboxes — the pre-existing 1.98pt overfull
was in the S9 row that came out. Full-text scan of both PDFs finds no residual index text. IMRaD word
count **3,394** (was 3,451; cap 4,000).

## Follow-up to round 3: supplementary material eliminated (2026-08-25)

Author instruction: fold the worthwhile supplement content into the manuscript, drop the rest. The
manuscript now ships with no supplementary material; `supplement.tex` carries a RETIRED banner and
remains in the repo as the analysis record only. Item-by-item disposition in `../PEER_REVIEW_R3.md`.

Folded in: Table S1 verbatim item wording (now Table 1), Table S10 missing-data decomposition (now
Table 2), §S6 skip-logic errors (Limitations, both described in full), Tables S2–S3 facilitator
practice (dropped as tables, Results §3.5 expanded to carry the distributions), §S5 reliability (both
α values inline in Limitations), §S9 reproducibility (Data availability).

Dropped: Tables S4–S7 BH families (tables and pointers only — the BH procedure and all four reported
q-values stay in the text, per author decision), §S1 coding notes, the preamble conventions, §S4
proportional-odds model, §S8 qualitative scaffold (held for a separate manuscript). The STROBE
checklist file is not submitted; Methods still states that reporting follows STROBE.

Tables renumbered by order of first mention, which shifted all three existing tables: instrument
wording (1) and missing data (2) are cited from Methods, so sociodemographics → 3, ceremony context →
4, protective practices → 5. Both the `.tex` and the `.md` updated; the markdown keeps its Google-Docs
bookmark anchors bound to the tables they always pointed at and changes only the displayed number.

Two layout fixes this forced. The protective-practices table is a `longtable` and therefore does not
float, so it typeset as Table 5 on p22 while the deferred float tables landed on pp24–27 — right
numbering, wrong order. Display items are now one per page via explicit `\clearpage`, which is the
conventional submission layout regardless. Table 1's long caption also collided with the table's top
rule and needed explicit spacing.

Build: 32 pages, 0 undefined citations or references, 0 overfull hboxes. IMRaD word count **3,778**
of 4,000 (was 3,394). Display items: 5 tables + 4 figures.

Open: the 4,000-word cap is read as excluding table content ("Introduction–Methods–Results–Discussion
combined", verbatim from the JPD guidelines). If that reading is wrong the plan breaks and Tables 1–2
go back out first. Also still open after three flags — the cell-suppression justification v5 removed,
against analysis-plan decision E10 and captions that all say "counts are exact".

## v6 → v7_draft.tex (2026-09-08, human .docx revision)

Input was `v7_draft.docx.md`, a Word-exported markdown draft of Jean's manual revision, diffed against
`v6_draft.md` (the plain-markdown rendering of `v6_draft.tex`) to separate real content edits from the
`.docx` export's own formatting conventions (bold headers, numbered section labels, curly quotes, `*n*`
italics, comma-before-year citation punctuation) — none of the latter were carried into the `.tex`, since
LaTeX's own machinery (`\section`, `\citep`, `natbib`) already produces the equivalent output. Several
wording changes the diff surfaced (removal of "four-arm" before "preparation × integration", "common but
not uniform as 81%" phrasing, the "the psilocybin-specific Puerto Rico survey" edit, and the table's
"Overnight ($\sim$12+ hours)") turned out to already be present in `v6_draft.tex`, meaning the `.tex` had
drifted ahead of `v6_draft.md` at some point; no change was needed there.

**Author list and affiliations.** Paulina Rullán Farinacci → Paulina D. Rullán Farinacci (middle initial
added). A new affiliation, Sattva Clinic, was inserted as #6, pushing the Department of Psychology (UPR
Río Piedras) from #6 to #7 and Centro de Investigaciones Sociales from #7 to #8; Adriana I. Rodríguez
Massa's superscript updated 6→7 to track the renumbered Psychology affiliation, and Yamil O. Ortiz Ortiz's
superscripts updated 6,7→6,8 (he keeps affiliation 6, now Sattva Clinic, plus the renumbered CIS
affiliation 8). Affiliation #3 renamed from "Colectivo Psicodélico de Puerto Rico, Colectivo Psicodélico
Inc., and Within Psychological Services" to "Red Enteogénica de Puerto Rico, Colectivo Psicodélico de
Puerto Rico and Within Psychological Services".

**Text edits applied.**
- Introduction: "psilocybin, DMT" → "psilocybin, N,N-dimethyltryptamine (DMT)" (acronym expanded on first
  use); "To the author's knowledge" → "To the authors' knowledge" (both instances, Introduction and
  Instrument).
- Results (ceremonial context): "DMT, LSD, MDMA, and ketamine" → "DMT, lysergic acid diethylamide (LSD),
  3,4-methylenedioxymethamphetamine (MDMA), and ketamine" (acronyms expanded on first use).
- Limitations: dropped the trailing clause "— the item on which retained non-response concentrated" after
  the "not sure"/"prefer not to answer" screening-item sentence.
- Competing interests: expanded the named-organization list from "the Puerto Rico Institute for Psychedelic
  Science, Medicine & Awareness and the Colectivo Psicodélico de Puerto Rico" to add Sattva Clinic, Pravan
  Foundation, and Within Psychological Services, consistent with the updated affiliation list.

**Not applied / flagged.** None — every substantive edit identified in the `.docx.md` diff mapped cleanly
onto an existing `.tex` passage or bibkey; no ambiguous rewording or unresolvable new citation was found.
The reference-list and in-text citation punctuation differences in the `.docx.md` export (numbered vs.
author-year, comma-before-year, DOI omission, added "Online First" notes) are pandoc/Word-export rendering
artifacts of a different `natbib` style setting on the human's end, not edits to the underlying `.bib`
data, and were left untouched.

Build not run this round per task instructions (no `pdflatex`/`bibtex`, no figure regeneration).

**Post-v7 correction (2026-09-08, same day).** The competing-interests paragraph inherited from v6
labeled all listed organizations, including Sattva Clinic and Within Psychological Services, as
"non-financial" and stated no author held a financial interest in any commercial entity. Confirmed with
the corresponding author that this was inaccurate for two co-authors: Juliana Millán-Torres owns Within
Psychological Services, and Paulina D. Rullán Farinacci is Chief Medical Officer of Sattva Clinic — both
are financial interests, not non-financial ones. Rewrote the paragraph to split PRIPSMA/Pravan
Foundation/Colectivo Psicodélico (non-financial) from the two named ownership/executive relationships
(financial), and narrowed the closing disclaimer to "No other author..." accordingly.
