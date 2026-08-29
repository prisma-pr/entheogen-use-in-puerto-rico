# Peer review, round 3 — 2026-08-25

**Input:** `manuscript/drafts/v5_draft_human_reviewed.md` (Julián + Jean's manual revision of
`v4_draft.tex`).
**Output:** `manuscript/drafts/v6_draft.md`, `manuscript/drafts/v6_draft.tex` →
`v6_draft.pdf`, updated `manuscript/drafts/supplement.tex` → `supplement.pdf`, regenerated
`manuscript/figures/fig1_flow.png` and `fig3_ceremony_good.png`.

Every number below was recomputed from `data/results_7_15_2026.xlsx` through
`analysis/data_prep.load()`. Nothing was carried forward on trust.

---

## The four review comments

### C1 — "Any mention of a limitation in the data or design that's getting mentioned everywhere should just be mentioned in the Limitations section"

Applied at the moderate setting you chose: a fragile number keeps a bare statement where it first
appears, the *reasoning about* that fragility moves to Limitations, and Methods keeps design facts
(no pretesting, no back-translation) because those are what happened, not caveats about it.

| Where | Was | Now |
|---|---|---|
| Methods → Measurement | "The two differ in referent (…) **so the primary analysis relates a single-ceremony outcome to a habitual exposure.**" | "The two differ in referent: the outcome asks about one event, the exposure about a general practice." |
| Results → ceremonial context | "…specified via free text, **leaving it uninterpretable**, and then DMT…" | clause cut; the judgement now sits in Limitations |
| Results → preparation index | α reported, then three clauses explaining what low α means | trimmed to one clause — then removed outright, see "Follow-up: practice index removed" |
| Results → perceived safety | "That bears directly on what follows, because the facilitator-practice measures crossed against the lifetime item all describe the most recent ceremony…" | sentence cut entirely; Limitations carries it |
| Results → prep vs satisfaction | "The structural weakness of this comparison precedes its result: the no-preparation group contains five respondents." | cut — the same sentence already opens the paragraph with "5 reported none" |
| Discussion → informal landscape | "…**but this sample cannot establish whether it holds, and eight facilitators cannot characterize screening practice.**" | "…which this sample cannot establish." |
| Discussion → safety | "The cross-tabulations … **pair a lifetime outcome with single-ceremony exposures**, are powered neither to…" | referent clause cut; Limitations carries it |

Limitations absorbed what was removed and gained two specifics it did not have: which 3
respondents the referent mismatch actually affects, and the two response categories that are
uninterpretable as collected. (A third, on the practice index's low α, was added here and then
removed with the index — see "Follow-up: practice index removed".)

**Deliberately not moved.** The ceiling discussion (Discussion §2) stays in Discussion. It is not a
generic limitation — it is the interpretation of why the corrected families came back null, and
moving it would leave those nulls unexplained. The Abstract keeps its closing scope sentence.

### C2 — "Data on no-prep group is inaccurate. Non-prep group only answered 6 or NaN."

**Not reproduced. The manuscript is correct and was left unchanged.**

`prep_part` (the exposure the analysis actually uses, `si` / `a_veces` / `no` / `pna`) crossed with
`ceremony_good`:

```
ceremony_good  NaN  _0  _1  _2  _3  _4  _5  _6  pna
prep_part
si               2   1   1   3   0   2  15  30    1
a_veces          0   0   0   0   2   0   0   4    0
no               1   1   0   0   1   1   1   1    0
```

The six `prep_part = 'no'` respondents are rows 3, 8, 13, 17, 18, 42. Their satisfaction scores are
0, NaN, 5, 3, 6, 4 — five numeric answers spanning the full scale, median 4, IQR 3–5. That is
exactly what the text, Table 3, and Figure 4 report, and Figure 4 plots those five points
individually.

I also scanned every categorical column in the dataset for a "no"-type group whose `ceremony_good`
values are confined to `_6` and NaN. No preparation variable matches: `self_prep = 'no'` spans 0–6
(n=26), `prep_guide = 'no'` spans 0–6 (n=11), `followed_prep = 'none'` has n=2 at 5 and 6,
`prep_med = 'no'` has n=2 both NaN, and `how_prep_part/no_prep` was selected by nobody.

If the comment came from a specific table or figure I haven't identified, send it and I'll re-check
against that. As it stands there is nothing to correct.

### C3 — "The first time KoboToolbox is mentioned, cite Kobo"

Citation added at the first mention (Methods → Design, ethics, and consent):

> …fielded on KoboToolbox (KoboToolbox 2026) between 24 February and 9 June 2026.

New BibTeX entry `kobotoolbox2026` in `manuscript/references/references.bib`, using the vendor's own
recommended citation form from
<https://community.kobotoolbox.org/t/citing-kobo-and-kobo-toolbox/76214>. KoboToolbox is a hosted
service with no versioned release or DOI, so the fielding window is recorded in the `note` field
instead of a version number.

### C4 — "Add S7 (Missing data distribution and attention checks) to the manuscript in the data quality section"

Two parts, both done.

**New analysis.** `analysis/missingness.py` decomposes every reported item over the analytic sample
into four mutually exclusive states — substantive answer, retained non-response
(`pna`/`not_sure`), blank while routed, never routed — using the group-level `relevant` expressions
transcribed from the XLSForm rather than inferred from which cells are empty. The four states
partition N=73 on every row, and the script asserts that they do. Output:
`outputs/tables/missingness_by_item.csv`, rendered as **Supplementary Table S10**.

**Manuscript.** The Methods data-quality subsection was one sentence. It is now two paragraphs
carrying the substance inline rather than deferring to the supplement, since you said most
supplementary sections are being cut: the structural-vs-genuine split, the peak nonresponse rate,
where retained non-response concentrates, the attention-check tallies per branch, and the duplicate
adjudication. Supplement §S7 was retitled "Missing-data distribution, attention checks, and
duplicate adjudication" and gained the decomposition prose plus Table S10.

Headline numbers now in the manuscript: item nonresponse among routed participants peaks at
**3 of 67 (4.5%)** on the satisfaction outcome and is zero on six of the fifteen participant items;
retained non-response concentrates on one item, **12 of 67** unsure or declining on whether the
facilitator screened them. Facilitators answered **21 of 21** attention items correctly;
participants answered 241 with 3 incorrect, in 2 respondents, both flagged and retained.

---

## Three errors found while doing the above

These were not in the comment list. All three are corrected in v6.

### E1 — The routed-participant base is 67, not 69 (structural skips are 5, not 3)

The XLSForm routes the participant section on

```
(is_participant='si' and pause_facil='si' and is_facilitator='si')
or (is_participant='si' and is_facilitator='no')
```

Every draft since v3 assumed the only structural skips were the 3 dual-role respondents who answered
`no` at the continuation gate. But **2 further participants answered `pna` to the facilitator role
item**, matching neither arm of that condition. Verified directly: rows 70 and 73 have every
participant item blank — `prep_part`, `ceremony_good`, `screening_quest`, `non_con_contact`,
`drug_used_part`, `trust_level`, all NaN.

So 5 participants were never routed, not 3, and every published per-item split overstated genuine
item nonresponse by exactly 2.

**Per-item bases were all correct** — n=67, 66, 65 and so on are unchanged, and **no statistic, test,
or effect size changes.** What changes is the skip/nonresponse attribution:

| Item | Was (skip / nonresponse) | Now |
|---|---|---|
| Time since last ceremony | 3 / 3 | 5 / 1 |
| Place | 3 / 2 | 5 / 0 |
| Format | 3 / 4 | 5 / 2 |
| Duration | 3 / 4 | 5 / 2 |
| Self-directed preparation | 3 / 2 | 5 / 0 |
| Knew facilitator's background | 3 / 2 | 5 / 0 |
| Facilitator asked screening questions | 3 / 3 | 5 / 1 |
| Spoke to a health professional | 3 / 4 | 5 / 2 |
| Non-consensual contact, ever | 3 / 2 | 5 / 0 |
| Non-consensual contact, most recent | 3 / 4 | 5 / 2 |
| Satisfaction (Figure 3 caption) | 3 skips / 5 nonresponse | 5 skips / 3 nonresponse |

Corrected in: Table 2 caption and rows, Table 3 caption and rows, Figure 1 caption, Figure 3
caption, the supplement preamble, and **the figures themselves** — `make_figures.py` gained a
`participant_routed()` helper implementing the real relevance condition, replacing the
`pause_facil == 'no'` shortcut that Figures 1 and 3 both used. Both PNGs regenerated.

This makes the data-quality story stronger, not weaker: more of the missingness is structural than
the paper previously claimed.

### E2 — Table 1's age row in v5 was computed over the wrong base

v5 changed the age row to "Mean 42.5 (SD 12.2); median 41.0 (IQR 32.8–50.0); range 21–75" while
still labelling it `n=72`. Those statistics are the **96 respondents who gave an age across all 100
submissions**, not the analytic sample:

```
all 100        n=96 mean=42.5 sd=12.2 med=41.0 iqr=32.8-50.0 range=21-75   <- what v5 printed
role_fork 87   n=86 mean=42.4 sd=12.2 med=41.0 iqr=34.0-50.0 range=21-75
analytic 73    n=72 mean=42.4 sd=11.9 med=41.0 iqr=34.0-50.0 range=21-71   <- correct
```

It also contradicted the Abstract and Results, which both say 42.4. Restored to the analytic-sample
values (v4 had these right). The rest of Table 1 was re-verified category by category and is
correct.

### E3 — Two dangling cross-references in v5

- The Results text says the practice index "was constructed for the 54 with complete data on all
  three (Table 3)", but v5's Table 3 no longer had the index rows. Restored at the time — then
  **superseded**: the author subsequently asked for the index to be removed entirely. See
  "Follow-up: practice index removed" below.
- Golden et al. 2022 remained in the reference list but v5's Introduction rewrite dropped the only
  citation to it. **Removed from the reference list** — flagging in case the intent was to keep the
  citation instead, in which case say so and I'll put it back in the Introduction.

---

## Conversion artifacts repaired

The `.docx` → `.md` round trip silently dropped mathematical symbols. All restored:

| Was | Now |
|---|---|
| "permutation 2 with 10,000 label permutations" | permutation χ² |
| "rank-biserial rrb … epsilon-squared 2" | rank-biserial *r*ᵣᵇ … epsilon-squared ε² |
| "tie-aware permutation p=0.010, 2=0.10" | ε²=0.10 |
| "permutation 2=18.90 … permutation 2=13.64" | permutation χ²=18.90 … χ²=13.64 |
| "returned U=218.0, p=0.041, rrb=0.50" | *U*=218.0, p=0.041, *r*ᵣᵇ=0.50 |
| "(= 0.14, 95% CI 0.36–0.47)" | (α = 0.14, 95% CI **−**0.36–0.47) — the minus sign was lost, turning a CI that crosses zero into one that doesn't |
| "four-arm preparation  integration design" | four-arm preparation × integration design |

---

## Open items for you

1. **C2 stands unresolved** unless you can point me at the table or figure the comment came from.
2. **v5 dropped the cell-suppression paragraph.** v4's Methods carried a justification for reporting
   counts below five ("the disclosure protection this study relies on is its design rather than cell
   masking…"). v5 removed it, but every table caption still says "counts are exact". The analysis
   plan's decision E10 sets an n<5 suppression rule, so a reviewer may ask why nothing is suppressed.
   I did not restore the paragraph — tell me if you want it back.
3. **Word count is 3,451** (IMRaD, citations excluded) against the 4,000 cap — down 317 from v4 even
   with the expanded data-quality section, so there is room if anything needs to come back.
4. **`\S S6` / Table S9 references** in the manuscript assume the supplement keeps its current
   section and table numbering. If sections are cut for tidiness, those pointers need renumbering.

---

## Verification run

```
analysis/missingness.py          four-state decomposition asserts a partition of N=73 — passes
pdflatex v6_draft.tex (×3)       28 pages, 0 undefined citations, 0 undefined references,
                                 0 overfull hboxes
pdflatex supplement.tex (×2)     11 pages, 0 errors, 1 overfull hbox of 1.98pt (pre-existing,
                                 in the S5 reliability table, not this round's Table S10)
make_figures.py                  all 5 figures regenerated; Figures 1 and 3 visually confirmed
                                 to show 67 routed / 5 structural skips
word count                       3,451 IMRaD words (cap 4,000)
```

---

## Follow-up: practice index removed

Author instruction after the round-3 pass: *"Remove all practice-index references."* Applied across
the manuscript, the tables, and the supplement.

**Manuscript.**

- Results → *Preparation, screening, and prior knowledge*: the index paragraph is deleted. Its one
  non-statistical finding was kept, restated without index language, at the end of the preceding
  paragraph — "Among the 54 respondents who answered all three of preparation, prior knowledge of the
  facilitator's background, and screening, every one reported at least one of them."
- Methods → *Protocol deviations*: "two branch-specific composites replace the mixed one" was now
  false on the participant side. Reworded to "a facilitator-side readiness composite replaces the
  mixed one" — the facilitator readiness composite (supplement Table S3) is a separate measure and
  survives.
- Limitations: the practice-index sentence added earlier this round is removed.
- Limitations: "produced mixed first reliability evidence" → "produced only preliminary two-item
  reliability evidence". The "mixed" characterization was carried by the α = 0.14 index row; with
  that row gone, Table S9 holds only α = 0.58 and α = 0.86.
- Table 3: the four index rows are removed.

**Supplement.**

- Table S4 (bivariate family) and Table S6 (safety-domain family): the two index tests removed and
  both families re-corrected — see below.
- Table S9: the index row removed and the caption narrowed to "the two testable same-respondent item
  pairs".
- §S5: the paragraph explaining the index's low α is removed.

**Retained deliberately.** Limitations still says the ceremony-level unlinking "eliminated … its
mixed harm-reduction composite". That names the *protocol's* planned composite and records why it
could not be built; it is a protocol-deviation statement, not a reference to the index that was
constructed. Say the word if you want that gone too.

### Re-corrected Benjamini–Hochberg families

You chose to drop the index tests from their families and re-correct rather than leave them in.
Recomputed with `analysis/stats_helpers.bh_fdr`. **No q crosses 0.05 in either family, so no
conclusion changes.**

*Bivariate family, 6 tests → 5:*

| Test | raw p | q before | q now |
|---|---|---|---|
| Preparation (3-level) → satisfaction | 0.120 | 0.359 | **0.300** |
| Comfort/safety by prior knowledge of background | 0.326 | 0.422 | **0.407** |
| Comfort/safety by screening received | 0.301 | 0.422 | **0.407** |
| Trust in facilitator by prior knowledge of background | 0.017 | 0.102 | **0.085** |
| Trust in facilitator by screening received | 0.679 | 0.679 | 0.679 |
| ~~Harm-reduction practice score → satisfaction~~ | 0.352 | 0.422 | *removed* |

*Safety-domain family, 5 tests → 4:*

| Test | raw p | q before | q now |
|---|---|---|---|
| Non-consensual contact × prior knowledge of background | 0.047 | 0.236 | **0.188** |
| Non-consensual contact × screening received | 0.094 | 0.236 | **0.188** |
| Witnessed crisis signs × distress-response protocol | 0.143 | 0.238 | **0.191** |
| Witnessed crisis signs × emergency plan | 0.429 | 0.536 | **0.429** |
| ~~Harm-reduction score (binarized) × non-consensual contact~~ | 0.641 | 0.641 | *removed* |

Two q-values are quoted in the main text and both were updated: the trust comparison now reads
q=0.085 (was 0.102), and the two non-consensual contact cross-tabulations now read q=0.188 (was
0.236).

**One caveat worth carrying into submission.** Re-correcting a family after withdrawing a test from
it lowers the surviving q-values, which is the direction that favours the paper. Nothing here crosses
significance and the withdrawn tests were both null (p=0.352, p=0.641), so no result is created or
destroyed — but if a reviewer asks why the families contain five and four tests rather than six and
five, the honest answer is that the index analysis was withdrawn from the paper in full, not that it
was never run. Worth a sentence in the response-to-reviewers if it comes up.

### Verification after removal

```
grep for practice index / practice score / harm-reduction score   0 matches in .md, .tex, supplement
pdflatex v6_draft.tex (×3)     28 pages, 0 undefined citations/references, 0 overfull hboxes
pdflatex supplement.tex (×2)   10 pages (was 11), 0 errors, 0 overfull hboxes — the 1.98pt
                               overfull in the old S9 table went with the removed row
PDF text scan                  no residual index text on any page of either document
word count                     3,394 IMRaD words (was 3,451; cap 4,000)
```

---

## Follow-up: supplementary material eliminated

Author instruction: fold the worthwhile supplement content into the manuscript and drop the rest.
The manuscript now has **no supplementary material**. `manuscript/drafts/supplement.tex` carries a
RETIRED banner and stays in the repo as the analysis record only.

The enabling fact: JPD's cap is "Introduction–Methods–Results–Discussion combined," so tables and
captions sit outside it. Folding a table therefore costs almost nothing against the cap; folding
prose costs 1:1.

| # | Item | Decision | Landed as |
|---|---|---|---|
| 1 | Table S10, missing-data decomposition | fold | **Table 2**, cited from Methods; prose was already inline |
| 2 | Tables S4–S7, BH families | drop tables + pointers | procedure and all four q-values kept in the text |
| 3 | §S6, skip-logic errors | fold | Limitations, both errors described in full |
| 4 | Tables S2–S3, facilitator practice | drop tables, expand prose | Results §3.5, roughly doubled |
| 5 | Table S1, verbatim item wording | fold | **Table 1**, cited from Methods → Instrument |
| 6 | §S1 coding notes | drop | the reverse-coding warning survives in Table 1's caption |
| 7 | preamble conventions | drop | — |
| 8 | §S9, reproducibility | fold | Data availability (outside the cap, so free) |
| 9 | Table S9, reliability | drop table | both α values stated inline in Limitations |
| 10 | §S8, qualitative scaffold | drop | held for a separate manuscript; the free-text sentence stays in Results |
| — | STROBE checklist | drop file | Methods still states that reporting follows STROBE |

**Tables renumbered by order of first mention**, which moved every existing table: instrument
wording (1) and missing data (2) are cited in Methods, so sociodemographics → 3, ceremony context →
4, protective practices → 5. All five in-text references updated in both the `.tex` and the `.md`.

**Two layout fixes this required.** The protective-practices table is a `longtable`, which does not
float — it was typesetting as Table 5 on p22 while the deferred float tables landed on pp24–27.
Correct numbering, wrong physical order. Display items are now one per page with explicit page
breaks, which is the conventional submission layout anyway. Table 1's long caption also landed its
last line on the table's top rule; fixed with explicit spacing.

**What this cost.** IMRaD word count went 3,394 → **3,778 of 4,000**, leaving 222 words of headroom.
Display items went from 3 tables + 4 figures to **5 tables + 4 figures**. The manuscript PDF is 32
pages.

### Things to watch

- **The cap interpretation is load-bearing.** If JPD counts table content toward the 4,000 words,
  this plan breaks and Tables 1 and 2 are the first candidates to go back out. Worth confirming with
  the editor before submission.
- **Nine display items** for a 3,778-word paper is on the heavy side. If a reviewer pushes back, Table
  1 (instrument wording) is the most natural one to move to an appendix, since nothing in the Results
  depends on it.
- **The cell-suppression justification is still absent.** v5 dropped v4's explanation for reporting
  counts below five, item 7 was dropped this round, and every table caption still says "counts are
  exact." The analysis plan's decision E10 sets an n<5 suppression rule that the paper does not
  follow. This has now been flagged three times and remains open.

### Verification

```
grep for "Supplementar" in .md and .tex          0 matches
PDF full-text scan for supplement pointers       0 pages
table numbering vs order of first mention        Tables 1-5 cited in order; verified in the PDF
pdflatex v6_draft.tex (×3) + bibtex              32 pages, 0 undefined citations/references,
                                                 0 overfull hboxes
word count                                       3,778 IMRaD words (cap 4,000)
```
