# Phase 1 analysis resolutions

Records every number that changed from the early draft (`ceremonial_entheogen_pr_manuscript.md`) and why,
plus the reasoning behind each Phase 1 decision. This is the audit trail `outputs/report_v2.md` and the
manuscript both trace back to.

## 1a. Duplicate adjudication — resolved, no exclusions needed

**Finding: zero true duplicate pairs exist within the analytic sample, at N=87 or N=73.**

`outputs/tables/data_quality_flags.csv` flags 20 rows across three signals: exact nickname+password match
(`dup_combo_flag`), nickname-only repeat, password-only repeat. Inspected each:

**Combo match (nickname AND password both identical) — the only signal that indicates a true duplicate
submission — flags exactly one pair:**

| row | role | nickname | password | submitted |
|---|---|---|---|---|
| 61 | participant_only | Riki | Aktharak | 2026-02-28 14:13:22 |
| 77 | abandoned_blank | Riki | Aktharak | 2026-02-26 02:22:43 |

Row 77 is an abandoned blank submission two days before row 61's completed one — the same respondent trying
twice, abandoning the first attempt, completing the second. Row 77 is **already excluded** from every
analytic sample by the pre-existing `abandoned_blank` rule (`data_prep.py::derive_roles`, `in_analytic`
definition). This pair requires no new exclusion — the existing pipeline logic already handles it correctly.
No second combo-match pair exists anywhere in the 100 rows.

**Nickname-only repeats (9 rows) and password-only repeats (12 rows) — inspected individually, all coincidental:**

The repeated strings are common Spanish words a respondent pool in this thematic context would plausibly
pick independently, not evidence of the same person submitting twice under different aliases:
- `Amor` (love) — 4 different nicknames (Luz, Rafa, mc, Seli) share it as a password
- `Si` (yes), `Secreta` (secret), `Hongos` (mushrooms — the substance itself) — 2 rows each, different
  nicknames/roles/dates
- `Luna` (moon) — a generic pseudonym, 2 rows, different passwords, different dates
- `Luigi`/`LuiGi` — 3 rows, different passwords, different dates — but **all three are already
  `screenout_no_no` or `abandoned_blank`**, so even in the unlikely case all three are the same person
  retrying, none of the rows enter any analytic sample (N=87 old or N=73 new)
- `Enid` — 2 rows, different passwords, both `abandoned_blank`, same reasoning

No nickname-only or password-only pair has **both** members inside an analytic sample with a plausible
same-person signal strong enough to justify exclusion.

**Attention-check flags (rows 63, 65):** both `participant_only`, both remain in the analytic sample per the
existing flag-never-drop protocol. 2 of 4 branch items failed (row 63) and 1 of 4 (row 65) — reported as a
data-quality note, not grounds for exclusion, consistent with the locked policy.

**Conclusion for the manuscript:** the draft's Limitations paragraph currently frames duplicate adjudication
as an open, submission-blocking question ("results reported here precede that adjudication"). That framing
is now out of date. Replace with a short paragraph stating the adjudication was performed, its method, and
its finding (no exclusions required) — turning a caveat into a closed methods step. No sensitivity re-run
table is needed since there is nothing to compare against (zero rows would be excluded either way).

## 1a′. Screen-out sample decision (author-confirmed 2026-08-13)

Per author decision: the 14 `screenout_no_no` respondents are **dropped from the analytic sample**. New
analytic sample: **N = 73** (was 87). Reported instead as a screening-yield statistic in Methods: 14 of the
87 respondents who reached the role fork (100 collected − 13 abandoned blank) screened out by answering "no"
to both role questions — a 16% screen-out rate. No further description of the screen-out subgroup is
produced (the alternative option — comparing their sociodemographics — was not selected).

Implementation: `data_prep.py::derive_roles` now sets two flags instead of one — `in_role_fork` (N=87, the
old `in_analytic`) and `in_analytic` (N=73, excludes `screenout_no_no` too). Every downstream table/section
in `report.py` reads `df.in_analytic`, so this single change propagates the new N through the entire report
without hardcoded numbers to hunt down (verified: no bare `87` literal existed anywhere in `report.py`).

**Cascading changes this produces** (to be filled in once `report.py` is re-run):
- Every "of N answering" denominator in Results shifts by the removal of 14 always-zero-response rows —
  in practice this changes very little numerically (the 14 screen-outs answered no participant/facilitator
  items in the first place), but the stated sample size, role-composition framing, and Methods §2.2 text all
  change from 87 to 73.
- Abstract's "87 eligible adults" becomes "73."

## 1b. Reporting gaps — all resolved

All fixes applied directly to `analysis/report.py` / `analysis/stats_helpers.py` and verified in the
regenerated `outputs/report.md` (snapshotted as `outputs/report_v2.md`):

- [x] **Per-substance counts + base n for the substances-used figure.** Root cause: `fig_substances()`
  drew from the full 100-row df with no denominator and no bar labels. Fixed to draw from the
  participant-analytic subset (numerically identical to the full-df sum — verified — since the item is
  skip-gated to participants, but now explicit and auditable), added numeric labels (masked `<5` for
  cells below the suppression floor, consistent with every other table), and added a companion frequency
  table. **Base n=67.** Counts: magic mushrooms 50 (75%), ayahuasca 43 (64%), tobacco 38 (57%), cacao 23
  (34%), DMT 17 (25%), LSD 13 (19%), MDMA 10 (15%), ketamine <5 (6%).
- [x] **Base n for the residency table.** Root cause: the table-building code never printed the caption
  line every other table gets. One-line fix. **Base n=72** (Puerto Rico 68/94%, US and Spain each <5).
- [x] **`exp_crisis` base pinned to one number.** Root cause: three separate hardcoded approximations
  ("≈8", "≈8", "n≈8" in a subsection heading) coexisted with one already-correctly-computed exact value.
  All three replaced with the live computed variable. **Pinned value: $n=7$ of 8 facilitators answered
  `exp_crisis`.**
- [x] **Descriptive count: participants reporting none of the three harm-reduction practices.** Computed
  directly: **zero of 54** complete-case participants scored 0 on the index (preparation + facilitator
  background knowledge + screening) — every respondent with complete data on all three items reported at
  least one. Added as an explicit sentence in §4.6.
- [x] **Exact-test p-value for the primary preparation comparison.** scipy's own `method='exact'` applies
  no tie correction, which is invalid given how heavily tied `ceremony_good` is — so a proper tie-aware
  permutation test was implemented (`stats_helpers.mann_whitney_perm()`, same 10,000-resample/seeded
  convention already used for `chi2_perm()` elsewhere in this project). Result: $p=0.024$, actually *more*
  significant than the asymptotic $p=0.041$ currently reported as primary — the normal approximation is
  not the conservative choice at this $n_2=5$. Reported as a robustness check alongside the primary result
  in §4.2, not a replacement for it.
- [x] **ε² sign convention.** Added `stats_helpers.fmt_eps2()`, applied at all 5 call sites: negative
  values (bias-corrected formula, near-null effect) now display as `0.00^{\dagger}$` with a footnote
  explaining the convention, defined once in §2 (Methods) before first use. (First implementation had a
  LaTeX bug — nested `$` delimiters broke math mode — caught by inspecting the rendered output and fixed.)

## 1c. Instrument documentation — complete

Full verbatim item wording, scale anchors, and bilingual-fielding confirmation extracted from
`koboxls.xlsx` (`survey`, `choices`, `settings` sheets) — see
[`instrument_documentation.md`](instrument_documentation.md). Headline findings:
- The instrument is a **native bilingual KoboToolbox form** (both `label::Español (es)` and
  `label::English (en)` on every item, Spanish default) — not a post-hoc translation. Closes that open item.
- `comfort_safe`'s raw choices-sheet row order is best-first, the reverse of the ascending 0–3 code used in
  the analysis; `config.py` deliberately re-orders by semantic content so higher code always means a more
  positive response, consistent with every other scale. Not a bug — documented so a reviewer cross-checking
  the raw XLSForm isn't confused.
- `prep_part` measures only presence/frequency of *self-directed* preparation (separate from any
  facilitator-given instructions, captured elsewhere) — explains why the construct reads as heterogeneous
  in free text (`self_prep_type`, 30 answers): the closed item deliberately doesn't capture preparation
  *content*, only whether it happened.
- `non_con_contact`'s wording is deliberately broad (unexpected/unclear-consent touch, including
  uncertainty and memory gaps) — broader than a narrower assault framing. Matters for how the 7.5%
  prevalence figure should be characterized in the manuscript.

## 1d. Methods facts recovered from the proposal — complete

From `data/Narrativa de propuesta uso ceremonial de enteogenos.md`, verbatim, closing the draft's
Methods §2.2 `[not reported in source]` gap:

- **Recruitment:** online promotion via social media (Facebook, Instagram, Twitter, WhatsApp) plus bulletin-board
  announcements at UPR Río Piedras and/or Ciencias Médicas.
- **Sampling:** convenience sampling via snowball/chain-referral, using digital promotion strategies "to
  maximize recruitment and facilitate inclusion of participants with the greatest variability and
  representativeness of potential participants in the population" (proposal's own framing — worth noting
  this aspirational language sits awkwardly next to the study's own decision to drop population-level
  claims; the manuscript should not repeat the proposal's representativeness language).
- **Target:** 100 participants (met).
- **Inclusion criteria (verbatim, translated):** 21 years or older; able to read and write in Spanish;
  access to an internet-connected device; has participated in a spiritual ceremony assisted by entheogens.
- **Exclusion:** under 21 / unable to consent.
- **Anonymity procedure:** fully anonymous — no names, birthdates, or other personal identifiers collected.
  Participants could optionally opt in to future-study contact via a separately-linked email address, with
  the proposal explicitly stating "questionnaires will be completely independent, guaranteeing no link
  between responses and contact information."
- **Voluntariness:** participation fully voluntary, withdrawal permitted at any time; "prefer not to answer"
  offered on every item (matches the `pna` category already retained throughout the analysis); no known
  risks stated, support resources offered in case of discomfort; no compensation.
- **Data retention:** identified data (there essentially is none, per the anonymity design) held on the PI's
  password-protected computer, de-identified data retained indefinitely for secondary analysis.
- **Instrument development:** built by the research team (described as experienced in psychedelic/entheogen
  ceremonial use in Puerto Rico), iteratively reviewed, then professionally translated (direct-translation
  technique) with a final team review pass for grammatical correctness and cross-language consistency —
  this is the citable source for "the instrument was purpose-built... professionally translated," a claim
  the current draft makes without this backing.

**Still not in any file** — searched the full proposal text for consent/IRB/committee/approval language;
zero matches. Genuinely needed from the study team, not derivable: IRB/CIPSHI approval number and date,
exact fielding start/end dates, consent procedure as actually implemented (the proposal describes the plan;
need what was actually run), preregistration status.

## Summary: every number that changed from the early draft

| Item | Early draft | Resolved value |
|---|---|---|
| Analytic sample | N=87 | **N=73** (screen-outs dropped per author decision; reported as 16% screening-yield rate instead) |
| Substances-used figure | rank order only, no counts, base n not reported | **Base n=67**; full counts table added (mushrooms 50…ketamine <5) |
| Residency table base n | not stated | **n=72** |
| `exp_crisis` base | stated variously as 7 / 7–8 / ≈8 | **Pinned: n=7 of 8** |
| Neither-practice count (harm-reduction index) | not computed | **Zero of 54** |
| Primary preparation test | asymptotic only, $p=0.041$ | **+ tie-aware exact/permutation check, $p=0.024$** (reported alongside, not replacing) |
| ε² sign convention | negative values shown as-is (−0.00, −0.02, −0.04) | **Truncated to 0.00 with footnote**, uniform |
| Duplicate adjudication | "results precede that adjudication," submission blocker | **Completed: zero exclusions required**, full reasoning documented |
| Recruitment/sampling/consent (Methods §2.2) | `[not reported in source]` | **Recruitment, sampling, inclusion/exclusion, anonymity, voluntariness — all resolved from the proposal.** IRB number, fielding dates, and implemented consent procedure still need the study team. |
| Instrument item wording/anchors | not given | **Full verbatim wording + anchors for all 5 key items**, plus bilingual-fielding confirmation |
