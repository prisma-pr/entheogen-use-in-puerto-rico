# Peer review — Phase 5

**Manuscript reviewed:** [`drafts/v2_draft.tex`](drafts/v2_draft.tex) (28 pp.) + [`drafts/supplement.tex`](drafts/supplement.tex) (9 pp.),
with [`references/references.bib`](references/references.bib) (26 entries), the four figures in
[`figures/`](figures/), and [`final/STROBE_checklist.md`](final/STROBE_checklist.md).

**Status: closed — every finding applied in [`drafts/v3_draft.tex`](drafts/v3_draft.tex) (30 pp.) and the
revised [`drafts/supplement.tex`](drafts/supplement.tex) (9 pp.).** The author sign-off happened on
2026-08-13; where this review recommended one of two options, the recommendation was followed. The
disposition table at the bottom records what was done for each item, and
[`drafts/revision_notes.md`](drafts/revision_notes.md) carries the full change log, the four author
decisions, and the remaining open items.

## How this review was conducted

Three passes, as specified in `MANUSCRIPT_PLAN.md` Phase 5, all run against v2:

1. **Methodological rigor** — every claim tested against what a non-probability, unweighted, N=73 descriptive
   design supports; the unlinked-branch constraint checked against the data rather than taken on trust.
2. **Journal peer-review simulation** — a reviewer report as a *Journal of Psychoactive Drugs* reviewer would
   write it, with an editorial recommendation.
3. **Citation and reporting integrity** — full external re-verification of all 26 references, plus tracing every
   in-text number back to source.

Two things were run rather than read, because plausibility is not verification:

- **Independent recomputation of the manuscript's numbers from the raw data.** `analysis/data_prep.load()` was
  imported and every reported count, base, median, IQR, distribution, and subgroup was recomputed directly from
  `data/results_7_15_2026.xlsx` and `data/koboxls.xlsx`. Effect sizes were re-derived by hand from their own
  reported inputs. Item wording and skip logic were read from the XLSForm `survey` sheet.
- **CrossRef and PubMed verification of every DOI**, plus a live check of the thesis repository URL.

Both scripts are in the session scratchpad; they are re-runnable and neither writes to the project.

---

# Pass 1 — Methodological rigor

Overall: the manuscript is unusually disciplined about its own limits. Every inferential result is labelled
exploratory, the no-prevalence/no-causation statement appears in the abstract, Results, Discussion, and
Conclusion, and the protocol-deviations section is a genuine strength. I found **no creeping generalization in
the Discussion** — the two places where it starts ("If that asymmetry holds in a larger sample…", "The design
implication is…") are both hedged in the same sentence.

The problems are elsewhere: in three places the paper describes its own data structure incorrectly, and in two
places it analyses items whose referents do not match.

### P1-1 (Major) — The facilitator branch is not "a different set" from the participants; it is almost entirely a subset

§3.5 states: *"Eight respondents identified as facilitators. This is a different, unlinked set from the
participants above."* The supplement §S2 repeats it: *"Facilitator-branch respondents are a different, unlinked
set from the participants reported in the main text."*

This is backwards. Recomputed from the data:

- 7 of the 8 facilitators are **also** in the participant branch (the dual-role respondents).
- **All 7 facilitators who answered `training_facilitator` and `exp_crisis` are dual-role.** The single
  facilitator-only respondent answered neither. Every substantive facilitator-side number in this paper —
  the "no formal certification" finding, the emergency-planning finding, the crisis-signs finding — comes from
  people who are also participant-branch respondents.

Methods §2.2 and Figure 1 state the overlap correctly, so the manuscript contradicts itself. The *analytic*
constraint is real and survives: even for a dual-role respondent, the ceremonies they led are different events
from the ceremonies they attended, and no identifier links a participant to their facilitator. But that is a
**ceremony-level** unlinkage, not a respondent-level one, and the paper currently asserts the stronger, false
version.

Consequence beyond the wording: facilitator-side and participant-side descriptive statistics are not independent
samples, which is worth one sentence wherever they are read side by side.

**Proposed disposition:** rewrite §3.5 and supplement §S2 to state the overlap explicitly ("Eight respondents
identified as facilitators; seven of them also identified as participants and appear in both branches. The
branches remain unlinked *at the ceremony level*…"). Add one sentence to Limitations noting non-independence.
Keep every downstream analytic decision as is — none of them change.

*Fairness note:* the related claim in Discussion §4.3 — that the non-consensual-contact finding and the
crisis-signs finding "come from different, unlinked reporters" — **is true**, and I checked it: none of the five
respondents reporting non-consensual contact is a facilitator. That sentence can stand as written.

### P1-2 (Major) — The safety cross-tabulations pair a lifetime outcome with most-recent-ceremony exposures

Verbatim from the XLSForm:

| Variable | Wording | Referent |
|---|---|---|
| `non_con_contact` | "Have you **ever** experienced physical touch during a ceremony that felt unexpected…" | lifetime, any ceremony |
| `facil_background` | "**Before the ceremony**, did you know anything about the facilitator's background…" | most recent ceremony |
| `screening_quest` | "**Before the ceremony**, did the facilitator or a co-facilitator ask you any questions…" | most recent ceremony |
| `med_couns_part` | "**Before the ceremony**, did you talk to a doctor, therapist…" | most recent ceremony |

§3.4 reports `non_con_contact × facil_background` at permutation χ² = 18.90, *p* = 0.047 — the paper's most
attention-getting uncorrected result — and it crosses a lifetime event against a single-ceremony exposure.

The data show this is not hypothetical. `non_con_contact_recent` is in the dataset: of the 5 respondents
reporting the event ever, **2 reported it at the most recent ceremony and 3 did not**. For those 3, the
facilitator-practice exposure being cross-tabulated describes a *different ceremony* from the one where the event
occurred. The same mismatch applies to the screening cross-tab and to the harm-reduction-index cross-tab.

**Proposed disposition:** keep the cross-tabs (they are already labelled hypothesis-generating and there is no
better alternative at this n), but (a) state the referent mismatch explicitly in Methods §2.3 and in §3.4 where
the result is reported, (b) report `non_con_contact_recent` alongside — see P1-3 — and (c) add one sentence to
Limitations. This *strengthens* the paper's existing argument that the safety domain identifies a measurement
priority rather than an estimate.

### P1-3 (Major) — `non_con_contact_recent` is collected and reported nowhere

The instrument asks a most-recent-ceremony version of the safety item: *"During your most recent ceremony, did
you experience any physical touch that felt unexpected or that you didn't clearly agree to beforehand?"*
Distribution among participants: **2 yes, 62 no, 1 prefer-not-to-answer, base 65.**

It appears in neither the manuscript, the supplement, nor `report_v2.md`. This is the one measure in the safety
domain whose referent matches its exposures, and it is the measure most reviewers would ask for. Omitting it
while reporting the lifetime item is exactly the shape of selective outcome reporting that a careful reviewer
looks for, even though nothing here suggests it was deliberate.

**Proposed disposition:** report it in §3.4 and Table 3, with its base, next to the lifetime item. Two sentences.
Note that a count of 2 sits below the suppression floor — see P1-7 for how that interacts.

### P1-4 (Moderate) — An undocumented routing gate removes 3 of the 7 dual-role respondents from the participant section

The XLSForm gates the participant block as
`(is_participant='si' AND pause_facil='si' AND is_facilitator='si') OR (…)`. In the data, of the 7 dual-role
respondents, **4 answered `pause_facil='si'` and 3 answered `'no'`**. The 3 who answered "no" were never shown a
single participant item.

Three consequences:

1. The participant-side base of 72 includes 3 people who were structurally never asked anything. The number
   actually routed into the participant section is **69**.
2. Figure 1 shows all 7 dual-role respondents flowing into the participant branch. It should show 4, with 3
   exiting at the continuation gate. This is STROBE item 13a — numbers at each stage.
3. Figure 3's caption says *"Base: 63 of 72 participants answering; the remainder is item nonresponse."* The
   remainder of 9 is actually **3 structural skips + 5 item nonresponse + 1 "prefer not to answer"** — three
   categories the paper's own Methods insists on keeping separate ("structural skips arise from branch logic and
   are reported as their own row, while item nonresponse is the residual").

**Proposed disposition:** add the gate to Methods §2.2 (one sentence), add the 3-respondent exit to Figure 1,
and correct the Figure 3 caption. Consider reporting participant-item percentages against 69 rather than 72, or
state once that 72 is the self-identified base and 69 the routed base.

### P1-5 (Moderate) — Methods promises a structural-skip row that no table contains

Related to P1-4 but separable. Methods §2.4 and the Table 2 caption both promise that structural skips are
"reported as their own row" / "reported separately from item nonresponse." No table in the manuscript has such a
row; `report_v2.md` does. A reviewer who reads the convention and then looks for it will not find it.

**Proposed disposition:** either add the structural-skip row to Tables 2 and 3 (cheap — the numbers exist:
6, 5, 7, 7 for the most-recent-ceremony items) or soften the Methods claim to what the tables actually do
(report per-item answering bases). I recommend adding the row; it is the more defensible of the two and costs
almost no words.

### P1-6 (Moderate) — The primary exposure and the primary outcome have different referents

`prep_part` asks whether the respondent prepares for **"these ceremonies"** (general practice); `ceremony_good`
asks how pleasant **"the ceremony"** was (most recent). The primary analysis therefore regresses a single-event
outcome on a general-practice exposure. That is not fatal — it is a reasonable thing to do — but it is not
currently disclosed, and it is the kind of thing a methods-focused reviewer raises.

It also has an analytic payoff: the harm-reduction practice index mixes one general item (`prep_part`) with two
most-recent-ceremony items (`facil_background`, `screening_quest`). The manuscript attributes the index's low
α = 0.14 entirely to the items capturing "distinct protective practices." Referent heterogeneity is a second,
simpler explanation and should be named alongside the first.

**Proposed disposition:** one sentence in Methods §2.3, one clause added to the α = 0.14 interpretation in §3.3.

### P1-7 (Moderate) — The stated suppression rule is contradicted by the paper's own tables and figures

Methods §2.4: *"Subgroup cells containing fewer than five respondents are suppressed and are not
back-calculated."* In practice:

- **Every table publishes a percentage of a stated base for its suppressed cells**, so every masked count is
  recoverable by one multiplication. Non-binary: 6% of 71 → 4. "Not sure" on non-consensual contact: 1% of 67 →
  1. Doctorate: 4% of 72 → 3. The masking is decorative.
- **Figure 2** masks ketamine's label as "<5" but draws the bar to its true length against a numbered axis. The
  value reads off the chart as 4.
- **Figure 3** prints exact counts of 2, 1, 3, 3, 3 — five cells below the floor, unmasked.
- **Figure 4** plots all five no-preparation respondents as individual points at their exact scores.

Author decision #3 already says not to suppress at n = 5 and to report as completely as possible, so the
*direction* is clear; what is wrong is that the Methods asserts a protection the paper does not provide. Leaving
it as is invites a reviewer or editor to conclude the disclosure controls were not thought through, which is the
opposite of the truth.

**Proposed disposition (needs your call — two coherent options):**

- **(a) Report exact counts throughout** and replace the suppression sentence with the actual policy: aggregate
  reporting only, no free-text quotation, no cell small enough to identify anyone given that no direct
  identifiers were collected. Most consistent with decision #3, and it removes an entire class of internal
  inconsistency.
- **(b) Keep suppression but make it real**: restrict it to cross-tabulated cells (which is where re-identification
  risk actually lives), say so explicitly, and drop percentages for suppressed univariate cells. Costs the reader
  some information and requires changing Figures 2–4.

My recommendation is **(a)**, on the grounds that it matches the decision already made, is honest about what the
data disclose, and is easier to defend than a masking convention that does not mask.

### P1-8 (Moderate) — Eligibility criteria are presented as operative but were not enforced

Methods §2.2 lists inclusion criteria including prior participation in a ceremony in Puerto Rico and ability to
read and write in Spanish. The data contradict both as enforced criteria: 14 respondents answered "no" to both
role items and reached the fork anyway; the sole facilitator-only respondent need not have participated; 4
respondents reside outside Puerto Rico; and the instrument was fielded bilingually with 19% of free-text answers
in English, so Spanish literacy was plainly not required in practice.

**Proposed disposition:** state that criteria were self-assessed and advisory rather than enforced by
instrument logic — one clause. This is a strength when disclosed and a hole when not.

### P1-9 (Moderate) — "Other" is the fourth-most-endorsed substance and appears nowhere

Recomputed from `drug_used_part` (base 67): mushrooms 50 (75%), ayahuasca 43 (64%), tobacco 38 (57%), cacao 23
(34%), **"other" 18 (27%)**, DMT 17 (25%), LSD 13 (19%), MDMA 10 (15%), ketamine 4 (6%).

"Other" outranks DMT, LSD, MDMA, and ketamine, all of which are reported, and it is absent from Figure 2, from
Table-equivalent text in §3.2, and from `report_v2.md` §3.4. With 27% of participants selecting it, the substance
profile as published is incomplete. The companion free-text field `drugs_used_part_other` has fewer than 5
answers, so the content is largely unrecoverable — which is itself the finding worth reporting.

**Proposed disposition:** add "Other" to Figure 2 and to the §3.2 sentence, and note that the accompanying
free-text field was rarely completed, so the category is uninterpretable. Regenerating Figure 2 is a
`make_figures.py` change, not a redraw.

### P1-10 (Moderate) — "Pre-declared" will be read as "preregistered"

The phrase appears in the abstract ("A pre-declared comparison…"), §2.5, and §3.6. There is no preregistration —
this is confirmed in the author decisions. The original protocol specified a four-arm preparation × integration
design, *not* this comparison; the preparation-to-satisfaction comparison was specified in `ANALYSIS_PLAN.md`,
written after data collection. That is a legitimate and defensible provenance, and the paper is transparent about
the deviation elsewhere — but "pre-declared" claims more than that.

**Proposed disposition:** replace with "specified in the analysis plan before the outcome was examined" (if that
sequencing is accurate — please confirm) and add "the study was not preregistered" to Methods. Reviewers treat
volunteered non-preregistration far better than they treat language that implied otherwise.

### P1-11 (Minor) — "Screening yield" names the wrong quantity

Methods §2.2 reports the 14 screen-outs "as a screening yield" of 16%. A yield is what you keep: 73/87 = 84%.
16% is the screen-out rate. Same error in the STROBE checklist item 13b.

**Proposed disposition:** "16% of those reaching the role fork screened out."

### P1-12 (Minor) — The ε² truncation convention is stated but never used in the main text

§2.5 explains that negative bias-corrected ε² values are displayed as 0.00 and marked †. No † appears anywhere in
the main text; the only truncated values live in the supplement, which does not carry the marker either. The
convention statement is currently dangling.

**Proposed disposition:** either apply the † in the supplement tables where truncation occurred, or move the
convention sentence to the supplement.

---

# Pass 2 — Journal peer-review simulation

*Written as a reviewer report for* Journal of Psychoactive Drugs. *Recommendation stated at the end.*

## Summary of the submission

The authors report a cross-sectional, anonymous, bilingual online survey of adults involved in entheogen-assisted
ceremonies in Puerto Rico (N = 73 who identified a role; 72 participants, 8 facilitators, 7 both). They describe
demographics, ceremonial context, protective practices, a satisfaction outcome, and a safety domain including
non-consensual physical contact. The pre-declared preparation-to-satisfaction comparison is positive but rests on
five unprepared respondents; no test in any corrected family reaches q < 0.05.

This is a competent, admirably self-critical descriptive paper on a population with no published local evidence
base. It fits this journal, which has recently published closely analogous naturalistic survey work
(Carvalho et al. 2025; Teixeira et al. 2026; Pagni et al. 2025). My recommendation is **major revision** — the
required work is disclosure and precision, not new analysis.

## Major points

**R1. Does a descriptive paper with no significant corrected result clear the bar?**
In my view yes, and the authors should defend it more confidently than they currently do. The contribution is the
first characterization of ceremonial practice in this jurisdiction, plus an instrument-level diagnostic for the
successor study. But the manuscript should say that in the Introduction in one sentence rather than leaving the
reader to infer it from the Discussion's fourth subsection.

**R2. The title promises facilitators; the paper has eight of them, seven of whom are also participants.**
"A Descriptive Survey of Participants and Facilitators" sets an expectation the facilitator data cannot meet —
every facilitator cell is at or below the suppression floor, no rate is estimable, and (per Pass 1) the
facilitator respondents are almost entirely a subset of the participants. Either retitle to foreground the
participant sample, or add "with a small facilitator subsample" — but do not leave a title that implies two
comparable arms.

**R3. Self-selection, and what the demographic convergence actually shows.**
Handled well. §4.1's observation that the demographic profile "is best read as evidence about who responds to
online psychedelic surveys, not about who attends ceremonies" is the right reading and I would keep it verbatim.

**R4. The k = 5 safety cell.**
The prevalence is correctly presented with a Wilson interval (7.5%, 3.2–16.3) and correctly disclaimed. My
concern is not the estimate but the cross-tabulations against it — see Pass 1 P1-2 on the lifetime-versus-most-recent
mismatch, which I would want addressed before publication. I support the authors' decision to publish the
cross-tabs rather than withhold them; the reasoning given in §3.4 is sound.

**R5. The n = 5 no-preparation group.**
The manuscript already says the structural weakness "precedes its result," reports the three-level sensitivity
analysis as non-significant, and shows the adjusted OR spanning 0.84–32.41. That is the right handling. I would
go one step further and drop "primary" from how this comparison is described in the abstract — it is the
pre-specified comparison, but calling it primary invites readers to treat it as the paper's finding, which the
authors themselves do not believe.

**R6. The ceiling effect.**
Well argued and well supported by Bouso et al. (2016). The conclusion that satisfaction "is close to exhausted as
an outcome in this population" is the most useful sentence in the Discussion for future researchers.

**R7. Duplicate adjudication.**
Adequate. One exact nickname+password pair, its earlier member already excluded as abandoned, zero analytic
exclusions, full reasoning in the supplement. I would state in Methods that no IP or device metadata was
available *because the platform did not record it*, not as a design choice, so readers do not read it as a
deliberate omission. (The current text does say this — keep it.)

**R8. The Discussion benchmarks against comparator cohorts without numbers.**
§4.1 says the demographic profile "resembles that of ceremony-attender cohorts described elsewhere" and cites
five studies. No comparator figures are given. For a paper whose entire contribution is descriptive, this is the
place a reviewer wants a small comparison table: this sample's age, education, and gender split against the
Portuguese ayahuasca attender cohort and the Global Drug Survey samples. Without it the convergence claim is an
assertion.

**R9. Ethics statement is incomplete for this journal.**
The Methods state IRB approval, the protocol number, and that consent was indicated by clicking through with no
signed document. It does not state that the IRB **approved a waiver of documentation of informed consent**. For
an anonymous online survey that waiver almost certainly exists; if so, say so. Journals increasingly reject
manuscripts on this alone.

**R10. Competing interests.**
The draft declares none. Several authors are affiliated with psychedelic-focused organizations (the Puerto Rico
Institute for Psychedelic Science, Colectivo Psicodélico). Under Taylor & Francis policy those affiliations are
disclosable. As drafted, this statement is likely to be wrong.

## Minor points

- **26 references is thin** for a paper of this scope, and below the 45–65 the authors' own plan targeted. The
  Introduction is efficient; the Discussion is where the gap shows (see R8).
- **Data availability** — "available from the corresponding author on reasonable request" is the weakest form
  accepted. Given the data are anonymous by design, consider a repository deposit; it would also strengthen R1.
- **Supplementary material is never cited by table number.** The main text says "(Supplementary Material)" nine
  times. Point to Table S1, §S4, etc.
- **American spelling** is required; "labelled" appears in the Figure 2 caption.
- **Figure 4** draws a box-and-whisker for n = 5. The box conveys precision the five points do not have.
  Consider plotting the five points alone against the any-preparation box.
- The **zero-variance life-impact item** (all 67 answering chose the same option) is reported in one sentence in
  §3.4 and again in the supplement. It deserves slightly more prominence as an instrument finding — it is a
  concrete, actionable lesson for the successor instrument.

## Recommendation

**Major revision.** No additional data collection or reanalysis is required. The required changes are: correct
the branch-overlap description (P1-1), disclose and address the referent mismatch in the safety analysis and
report the most-recent-ceremony safety item (P1-2, P1-3), document the routing gate and fix the affected flow
figure and caption (P1-4), reconcile the suppression policy with what the tables and figures actually show
(P1-7), resolve "pre-declared" (P1-10), complete the ethics and competing-interests statements (R9, R10), and add
comparator numbers to the Discussion (R8).

---

# Pass 3 — Citation and reporting integrity

## 3a. Reference verification — all 26 entries, externally re-verified

Every DOI was resolved against the CrossRef API; author lists, journal, year, volume, issue, and pagination were
compared field by field. Non-DOI entries were verified against their primary source.

**Result: all 26 references are real and correctly attributed. 23 of 23 DOIs resolve to the cited work with
matching first author, title, journal, and year.** No fabricated, hallucinated, or misattributed citation.

Six metadata defects, none affecting whether the work exists:

| Key | Defect | Correct value | Severity |
|---|---|---|---|
| `koss1980therapist` | Journal name and volume | CrossRef: *Social Science & Medicine. Part B: Medical Anthropology*, vol. **14**, no. 4 (bib has "Social Science & Medicine. Medical Anthropology", vol. "14B") | Fix |
| `hughes2024ethnoracial` | `EClinicalMedicine` will render with a capital E | Brace-protect as `{eClinicalMedicine}` | Fix |
| `bouso2016measuring` | Journal short title | Full title is *Human Psychopharmacology: Clinical and Experimental* | Optional |
| `golden2022effects` | Typed `@article`; CrossRef type is `book-chapter` | *Current Topics in Behavioral Neurosciences* is a book series; `@incollection` is the accurate type. Volume 56 and pages 35–70 are correct | Optional |
| `marcus2026psychedelics` | Year | Online-first 2025-07-27, print issue **2026-01**, vol. 47(1):279–296. The bib's 2026 is defensible for the print issue; add a `note` recording the online-first date | Note only |
| `siegel2023psychedelic` | — | CrossRef lists first page only; PubMed (PMID 36477830) confirms **80(1):77–83** as in the bib. **No change needed** | Verified |

Other verifications:

- `doeltermorales2020hongos` — no DOI (unpublished thesis); repository URL `repositorio.upr.edu/handle/11721/2540`
  returns HTTP 200. Correctly typed `@mastersthesis` with a `note` explaining the absent DOI.
- `uscongress1970csa` — 21 U.S.C. § 812, Pub. L. No. 91-513, 84 Stat. 1242. Correct.
- `pr1971csa` — Ley Núm. 4 de 23 de junio de 1971, 24 L.P.R.A. § 2101 et seq. Correct.
- **Five entries remain Online First with no volume/pages**: `velezrodriguez2026psilocybin`, `carvalho2025scoping`,
  `teixeira2026ayahuasca`, `pagni2025longterm`, `robinson2026field`. Confirmed still unpaginated in CrossRef as of
  today. Each carries a `note`. **Re-check immediately before submission** — this is a live item, not a closed one.
- **All 26 keys are both defined and cited; no orphan entries, no undefined keys.**

## 3b. Number tracing — independent recomputation from the raw data

Rather than checking the manuscript against `report_v2.md`, I recomputed from the source data. **Everything below
reproduced exactly:**

- Sample construction: 100 → 13 abandoned → 87 at the fork → 14 screen-outs → N = 73; 72 participants,
  8 facilitators, 7 dual.
- Table 1 in full: age (n=72, mean 42.4, median 41, SD 11.9, range 21–71, IQR 34–50); gender 35/30/4/2 of 71;
  education 34/19/7/6/3/3 of 72; economic 44/20/6/2 of 72; residence 68/3/1 of 72.
- Table 2 in full: recency 30/20/11 of 66; place 37/15/9 of 67; format 48/13 of 65; duration 19/19/14/7 of 65.
- Table 3 in full: preparation 55/6/6 of 67; facilitator background 54/8/4/1 of 67; screening 39/15/7/5 of 66;
  health professional 54/8 of 65; non-consensual contact 61/5/1 of 67; practice index 35/16/3 of 54, floor empty.
- Substance counts (base 67) — **except the omitted "other" category, P1-9**.
- Most-recent substance: mushrooms 31, ayahuasca 23, pooled 11.
- Satisfaction: 63 numeric responses, median 6, 51 of 63 at 5–6; groups 58 vs 5 with medians 6 and 4.
- All facilitator counts, including the base-8 select-multiple percentages.
- Qualitative: 37 text fields, 285 non-empty answers. Attention-check flags: 2. Duplicate pairs: 1.
- The practice index reproduces exactly under the pipeline's documented coding (`facil_background` si/some = 1,
  `not_sure`/`pna` treated as item-missing), which caps the complete-case base at 54 via the screening item.

**Effect sizes independently re-derived and internally consistent:** CLES 0.75 = U/(n₁n₂) = 218/290; rank-biserial
0.50 = 2(CLES) − 1; Wilson 95% CI for 5/67 recomputes to 3.2–16.3; every Cramér's V reproduces from its own χ² and
n (0.38, 0.32, 0.17, 0.10); every ε² reproduces from its H and k.

**Discrepancies found in tracing:**

| # | Item | Finding |
|---|---|---|
| P3-1 | Satisfaction base | 64 respondents answered the item; 63 gave a numeric score and 1 chose "prefer not to answer." Figure 3's caption calls the whole 9-person remainder "item nonresponse," which conflicts with the paper's own policy of retaining "prefer not to answer" as substantive — and with the 3 structural skips identified in P1-4 |
| P3-2 | Facilitator denominators | Supplement Table S2 computes select-multiple percentages on base 8, while Table S3 uses base 7 answering, in adjacent tables with no note. Only 7 facilitators answered any of these items. Defensible convention, undocumented |
| P3-3 | Source-of-truth headers | Both `.tex` files state "Every number traces to `outputs/report_v2.md`." Several Table 3 distributions (preparation at base 67; health professional at base 65) exist only as direct recomputations — `revision_notes.md` documents this correctly, the file headers do not |
| P3-4 | STROBE checklist is stale | References `v1_draft.tex` throughout; items 13a and 13c still say "Figure 1 pending Phase 4" though Phase 4 is complete. Item 22 (funding) still open |

## 3c. Journal-requirements compliance

Checked against `JOURNAL_REQUIREMENTS.md`:

| Requirement | Status |
|---|---|
| Abstract unstructured, ≤ 200 words | **188 words**, unstructured ✅ |
| Introduction–Discussion ≤ 4,000 words | **~3,870** (Intro 439, Methods 1,191, Results 1,192, Discussion 1,046) ✅ — roughly 130 words of headroom, which is enough for the accepted revisions if the longer additions land in the supplement |
| Keywords 4–6 | 6 ✅ |
| Chicago author-date | `natbib` + `chicago.bst`, `.bbl` builds ✅ |
| 12 pt, double-spaced, 1-inch margins, numbered pages, line numbers | ✅ |
| Figures ≥ 300 dpi colour | 600 dpi ✅ |
| American spelling | ⚠️ "labelled" (Fig. 2 caption) |
| Ethics + consent statement in Methods | ⚠️ present but incomplete — no consent-documentation waiver (R9) |
| Required disclosures (CRediT, funding, competing interests, AI, data availability) | ⚠️ all five drafted, all five still `UNCONFIRMED` |
| STROBE | not mandated; checklist supplied ✅ but stale (P3-4) |

---

# Consolidated disposition table

All rows applied in `v3_draft.tex` / `supplement.tex` on 2026-08-13.

| # | Severity | Finding | Disposition |
|---|---|---|---|
| P1-1 | Major | Facilitator branch described as a different set; 7 of 8 are dual-role and all 7 substantive facilitator responses are dual-role | ☑ Applied. §3.5, Suppl. §S2, Fig. 1, and §4.5 state the overlap; unlinkage is now claimed at the ceremony level only; Limitations adds the non-independence sentence. No analytic decision changed |
| P1-2 | Major | Lifetime safety outcome crossed with most-recent-ceremony exposures | ☑ Applied. Disclosed in §2.3, at the point of report in §3.4, in the Suppl. safety-family caption, and in §4.5; cross-tabs retained |
| P1-3 | Major | `non_con_contact_recent` (2/65) never reported | ☑ Applied. Now in the abstract, §3.4, and Table 3, with the 2-of-5 / 3-of-5 split |
| P1-4 | Moderate | `pause_facil` gate removes 3 of 7 dual-role from the participant section; undocumented | ☑ Applied. Documented in §2.2, drawn in Fig. 1 (69 routed), corrected in the Fig. 3 caption, and carried into Tables 2–3 |
| P1-5 | Moderate | Promised structural-skip row absent from all tables | ☑ Applied as recommended. Tables 2 and 3 carry explicit structural-skip and item-nonresponse rows; Table 3 became a `longtable` to fit |
| P1-6 | Moderate | Primary exposure (general) vs. outcome (most recent) referent mismatch; also explains part of α = 0.14 | ☑ Applied. §2.3 states the mismatch; §3.3 and Suppl. §S5 name referent heterogeneity alongside multidimensionality |
| P1-7 | Moderate | Suppression rule contradicted by percentages, Fig. 2 bar length, Fig. 3 counts, Fig. 4 points | ☑ **Option (a), as recommended.** All masking removed from tables, figures, and `make_figures.py`; §2.4 states the real policy (anonymous design, aggregate-only, no quoted free text) and why masking would have been cosmetic |
| P1-8 | Moderate | Eligibility criteria presented as operative but not enforced | ☑ Applied. §2.2 lists the four specific ways they were not enforced |
| P1-9 | Moderate | "Other" substance (18/67, 27%) omitted from figure and text | ☑ Applied. In Fig. 2 (grey bar) and §3.2, with the 3-respondent free-text follow-up noted |
| P1-10 | Moderate | "Pre-declared" implies preregistration that does not exist | ☑ Applied, author-confirmed wording: "designated in the analysis plan as the primary comparison before any test was run", plus "the study was not preregistered, and the analysis plan was written after data collection". The stronger "before the outcome was examined" would have been false — `ANALYSIS_PLAN.md` quotes the outcome distribution |
| P1-11 | Minor | "Screening yield" names the wrong quantity | ☑ Applied in §2.2 and STROBE 13b |
| P1-12 | Minor | ε² truncation convention stated, never used in main text | ☑ Applied. Convention moved to the supplement preamble; ε² columns added to Suppl. Tables S4 and S7 carry six † markers; effect-size columns added to the substance and safety families too |
| R2 | Moderate | Title implies two comparable arms | ☑ Author decision: qualified — "…of Participants and a Small Facilitator Subsample" |
| R5 | Minor | "Primary" oversells the preparation comparison in the abstract | ☑ Applied. "Primary" removed from the abstract and §4.4 |
| R8 | Moderate | Comparator claims carry no comparator numbers | ☑ Applied. §4.1 gives age, education, and gender against Pagni 2025, Ruffell 2021, and Nayak 2023. Teixeira 2026 and Kopra 2023 could not be used numerically (paywalled tables, no demographics in the abstracts) — documented in `sources/search_20260813_comparator_demographics_R8.md` |
| R9 | Major | Ethics statement lacks the consent-documentation waiver | ☑ Author-confirmed: the information sheet sat inside the questionnaire and the IRB approved that procedure as submitted. §2.1 now says so, and that no signed document was collected or required |
| R10 | Major | Competing-interests statement likely incorrect | ☑ Author decision: disclose. The statement now names the affiliated organizations as potential non-financial competing interests and declares no financial interests. Per-author confirmation still needed |
| R-refs | Minor | 26 references, below the paper's own 45–65 target | ☑ Partially. Five CrossRef-verified comparator/harm references added (31 total). The 4,000-word cap is the binding constraint on adding more |
| P3-1 | Minor | Fig. 3 caption mislabels 9 non-responses as one category | ☑ Applied in both the caption and the figure itself |
| P3-2 | Minor | Two facilitator denominators in adjacent supplement tables | ☑ Applied. Both tables use base 7, with an explicit note |
| P3-3 | Minor | `.tex` headers claim full traceability to `report_v2.md` | ☑ Applied to both files |
| P3-4 | Minor | STROBE checklist stale (v1, Phase 4 "pending") | ☑ Refreshed to v3; 13a, 13c, and 22 closed; item 10 the only open row |
| P3-5 | Minor | `koss`, `hughes` metadata defects; `bouso`, `golden` optional | ☑ All four applied, **plus two author-name errors CrossRef surfaced that this review had not caught**: `hughes2024ethnoracial` is Marcus E. Hughes (not Matthew), and `golden2022effects` is Tasha L. Golden / Clara C. Sandu / Shuyang Lin / Kathy M. Shi (not Thea / Cristina / Shiqi / Kevin) |
| P3-6 | Minor | Five Online First entries unpaginated | ☐ **Open by design** — re-check immediately before submission. BibTeX warns on every build |
| P3-7 | Minor | Supplement never cited by table/section number | ☑ Applied throughout |
| P3-8 | Minor | "labelled" — British spelling | ☑ Applied |
