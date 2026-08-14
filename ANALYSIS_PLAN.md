# Analysis Plan — Ceremonial Entheogen Use in Puerto Rico

**Prepared as a statistical/analytic consultation.** Status: descriptive study (reframed from epidemiological — see §0). Data: `results_7_15_2026.xlsx`, N=100 × 354 columns, real collected data. Instrument: `koboxls.xlsx` (`survey` = skip logic, authoritative; `choices` = value sets).

All counts below were verified by direct inspection of the data and the XLSForm `survey`/`choices` sheets. Where a number cannot be confirmed it is marked **[unconfirmed]**.

---

## Implementation status (as of build)

Legend: ✅ implemented & verified · 🟡 partial · ⬜ pending. Pipeline: `analysis/` → `outputs/report.md`.

| Area | Status | Where |
|------|--------|-------|
| §2.1 Project layout | ✅ | `analysis/{config,data_prep,quality,stats_helpers,report}.py` |
| §2.2 Import & encoding (UTF-8, choices/survey decode) | ✅ | `data_prep.load()` |
| §2.3 Cleaning & derived vars (roles, `ceremony_good` decode, 3 drug vars kept distinct, pna/not_sure policy) | ✅ | `data_prep.py` |
| §2.3 Full Likert decode of *all* scales | 🟡 (4 scales encoded; rest decoded on demand) | `config.ORDINAL_SCALES` |
| §2.4 Univariate — sociodemographics, residency, substances, roles | ✅ | `report.section_univariate` |
| §2.4 Univariate — full ceremony practice/context battery (frequency, env, format, duration, training tables) | ✅ | `report.section_univariate` §3.5–3.6 |
| §2.5 Bivariate — preparation → outcome (Mann–Whitney + Kruskal–Wallis, effect sizes) | ✅ | `report.section_bivariate` |
| §2.5 Bivariate — perceived safety by facilitator training/protocol | ✅ | `report.section_bivariate` §4.4–4.5 |
| §2.5 Integration proxy 2×2 | ❌ dropped per client (no clean item → prep-only analysis) | — |
| §2.6 Qualitative — open-text extraction + coding scaffold | ✅ | `analysis/qualitative.py`, `report.section_qualitative` §6 |
| §3.1 Safety — `non_con_contact` prevalence (Wilson CI) + `exp_crisis` aggregate | ✅ | `report.section_safety` |
| §3.1 Safety — association with training/screening/protocol | ✅ | `report.section_safety` §5.3–5.4 |
| §3.2 Data-quality flags (attention per branch + duplicates) | ✅ | `quality.py`, `outputs/tables/data_quality_flags.csv` |
| §3.2 Sensitivity re-run excluding adjudicated flags | ✅ | — |
| §3.3 Role-structure description | ✅ | `report.section_univariate` §3.1 |
| §3.9 Residency / diaspora description | ✅ | `report.section_univariate` §3.3 |
| §3.4 Multivariable ordinal model | ✅ | `report.section_bivariate` §4.8 |
| §3.5 Harm-reduction practice index | ✅ | `report.section_bivariate` §4.6 (participant), §4.5 (facilitator, descriptive) · `report.section_safety` §5.3.3 |
| §3.6 Substance-stratified satisfaction/safety | ✅ | `report.section_bivariate` §4.9 |
| §3.7 Psychometric / reliability check | ✅ | `report.section_psychometrics` §8 |
| §3.8 Legal knowledge/worry correlates | ✅ | `report.section_legal` §9 |
| §4 Rendered report (Markdown + LaTeX math, n<5 suppression) | ✅ | `outputs/report.md` |

Everything marked ✅ runs clean end-to-end via `PYTHONIOENCODING=utf-8 python analysis/report.py`.

---

## §0. Decisions locked in (from client answers)

| # | Decision |
|---|----------|
| Population | Analytic sample = eligible respondents who reached the role fork. Keep the 14 explicit `no/no` rows *only* to describe screen-outs; exclude the 13 abandoned-early (both role items blank) from substantive analysis. No authoritative completion field exists. |
| Dual-role (n=7) | Included in **both** facilitator-side and participant-side analyses. |
| `pna` / `not_sure` | Retained as a **substantive category**, uniformly across all items. Never silently recoded to NA or dropped. |
| `ceremony_good` | **Ordinal**; nonparametric methods primary. |
| Safety domain | `non_con_contact` + `exp_crisis` are a formal outcome set. No disclosure/reporting constraints. |
| Duplicates | Flag via `nickname` + `password` combination; `ev_dup` unusable (empty ×100), `_submitted_by` empty. |
| Attention checks | **Do not drop** failing rows — flag for reviewer. Facilitator judged on `atencion_1/2/3`; participant on `atencion_3_2/4/5/6`. |
| Framing | **Unweighted descriptive study.** No population weighting; drop incidence/prevalence-to-population language. |
| Residency | `municipality`/`country`/`hispanic` = descriptive covariate, not an inclusion filter. |
| Suppression | Subgroup cells with **n < 5** suppressed in all reported output. |
| Deliverable | **Python** scripts + rendered **PDF/HTML** report. Client writes manuscript separately. |
| Safety-domain cross-tabs (2026-07-15) | For the §3 item 1 association analysis (`non_con_contact`/`exp_crisis` × training/screening/protocol), the team decided to publish cross-tabs under the **same standard n<5 masking convention** used elsewhere in the report, rather than withholding them entirely per §4.4's stronger "no cross-tab" rule for these two items. Even masked, several cells are close to case-level (`non_con_contact` affirmative+not-sure totals n=6; `exp_crisis` facilitator base n≈8) — every result is flagged hypothesis-generating only. See `report.section_safety` §5.3. |

---

## §1. Critical review of the proposal as written

### 1.1 The structural mismatch: "facilitators and participants" is not a partition
Objectives 1–2 and the analytic plan treat facilitators and participants as two clean, exhaustive groups. The fielded data contradict this:

- **7** respondents are *both* facilitator and participant (`is_facilitator='si'` & `is_participant='si'`).
- **1** facilitator-only, **65** participant-only.
- **27** are neither "sí": **14** explicit `no/no` screen-outs + **13** who left both role items blank (abandoned before/at the fork).

Consequence: every facilitator-vs-participant contrast in the proposal is really a comparison of **overlapping** sets, and ~27% of the sample is unclassified. The instrument compounds this — the role fork (`is_facilitator`/`is_participant`) is itself gated on `ans_prev='no'`, and dual-role respondents only reach the participant block if they pass an extra `pause_facil='si'` continuation gate. The proposal's objectives need rewording around three analytic groups (facilitator-only, participant-only, dual-role) rather than a binary.

### 1.2 The headline hypothesis test (H3/H4) is largely infeasible as specified
Hypotheses 3–4 and Objectives 3–4 propose comparing `ceremony_good` across four arms: **prep+integration / prep-only / integration-only / neither**, via t-test or ANOVA. Two problems:

1. **No clean participant "received integration support" variable exists.** The instrument has a clean participant *preparation* item (`prep_part`: 55 sí / 6 no / 6 a_veces among the 67 answering) but **no** matching single item for *received post-ceremony integration support*. Post-ceremony content on the participant side is `self_care` (a select-multiple of self-directed behaviors) and `med_asist` (sought professional help; 13 sí / 53 no). Integration-*offered* items (`support_protocol`, `support_type`) live in the **facilitator** block (n≈7). So the 2×2 prep×integration design cannot be built from a symmetric pair of items — it must be *operationalized by proxy* (see §2.5), and that choice should be pre-registered, not silent.
2. **The cells are empty where the hypothesis needs them.** With `prep_part` = 55 sí vs. only 6 no and 6 a_veces, any "no preparation" arm is ~6 people *before* crossing with integration. Under the n<5 suppression rule, the "no-prep" cells of the 2×2 are unreportable. The proposal's central comparison is therefore **underpowered to the point of being descriptive-only**: nearly everyone prepared, so there is almost no contrast to test. This should be stated plainly rather than run as a formal ANOVA implying inferential weight.

### 1.3 Statistical-plan weaknesses
- **Parametric test choice.** t-test/ANOVA on `ceremony_good` assume an interval outcome; it is a 0–6 ordinal with a severe ceiling (51 of 64 answered 5–6). Means are misleading; nonparametric/ordinal methods are required.
- **Multiple comparisons.** The plan implies many bivariate tests (prep, integration, facilitator training, protocol, perceived safety…) with no correction and no primary/secondary hierarchy. At N≈72 participants this is a false-positive engine.
- **No multivariable analysis.** Rich covariates were collected (sociodemographics, context, trust, screening) yet the plan stops at pairwise bivariate comparisons — no adjustment, no confounder control.
- **No missing-data strategy.** The proposal offers a "Prefiero no contestar" option everywhere but never says how `pna`/`not_sure`/skip are handled. (Now resolved: retained as a category — but this must be documented as it changes denominators.)
- **No psychometrics.** A newly developed, non-validated instrument with multiple Likert scales, yet no reliability/internal-consistency check is planned.
- **Attention checks ignored.** Six/seven `atencion_*` items were fielded but never mentioned in the analytic plan; no data-quality rule.
- **Safety outcome absent.** `non_con_contact` (5 sí / 1 not_sure / 61 no) and `exp_crisis` (incl. suicidal-ideation and panic-attack sub-items) are serious adverse-event measures that appear nowhere in the stated variables or plan.
- **Weighting claim unsupported.** Limitations promise results "ponderado para representar la población general de PR" with no benchmark, frame, or method — incompatible with a convenience/snowball sample. (Now resolved: dropped; study reframed descriptive.)

### 1.4 Design/sampling (appropriate, with caveats)
Cross-sectional convenience/snowball via social media is defensible for a hidden, hard-to-reach population and an exploratory first-look — the design matches the (revised) descriptive aim. Genuine limits to state up front: self-selection and social-media coverage bias, recall bias on self-report, no causal or prevalence inference, likely diaspora contamination of "PR" claims (residency must be checked, §3.9), and duplicate-responder risk from snowball recruitment that the platform's `ev_dup` flag never screened.

---

## §2. Implementation plan for the analysis AS PROPOSED (univariate → bivariate → qualitative)

Language: **Python**. Core stack: `pandas`, `numpy`, `scipy.stats`, `statsmodels`, `pingouin` (nonparametric + effect sizes + reliability), `matplotlib`/`seaborn`, `great_tables` or `tabulate` for tables, `jupyter`/`quarto` (or `nbconvert`) to render HTML/PDF. Rendering fallback if Quarto/LaTeX unavailable: HTML via `nbconvert`, PDF via `weasyprint`.

### 2.1 Project layout — ✅ implemented
```
analysis/
  00_config.py          # paths, value maps, suppression threshold, ordinal scales
  01_load_clean.py      # import, encoding fix, decode, derive role/analytic flags
  02_quality_flags.py   # attention-check + duplicate flags (no row dropping)
  03_univariate.py      # frequencies, central tendency
  04_bivariate.py       # the proposed comparisons (nonparametric)
  05_qualitative.py     # open-text extraction + coding scaffold
  06_report.qmd/.ipynb  # assembles rendered PDF/HTML
outputs/
  tables/  figures/  report.html  report.pdf
  data_quality_flags.csv          # for client review (attention/dup)
```

### 2.2 Import & encoding — ✅ implemented
- Read `results_7_15_2026.xlsx` with `pandas.read_excel`; force UTF-8 handling (`PYTHONIOENCODING=utf-8`) — Spanish glyphs corrupt under cp1252.
- Load `koboxls.xlsx` `choices` sheet into a `{list_name: {name: label_es/en}}` dictionary for value decoding; load `survey` sheet for type + `relevant` (skip logic) metadata. **All recoding maps derive from these sheets, never hard-coded guesses.**

### 2.3 Cleaning & derived variables — ✅ implemented (full Likert battery 🟡 partial)
1. **Role / analytic flags** (from `is_facilitator`, `is_participant`):
   - `role ∈ {facilitator_only, participant_only, dual, screenout_no_no, abandoned_blank}`.
   - `analytic_participant = is_participant=='si'` (72), `analytic_facilitator = is_facilitator=='si'` (8); dual-role in both.
   - Exclude `abandoned_blank` (13) from substantive analysis; retain `screenout_no_no` (14) for a screen-out description table only.
2. **Decode `ceremony_good`**: strip leading underscore on `_0`…`_6` → integer 0–6, ordered categorical; keep `pna` as its own labeled level (not NA). Flag structural vs. item missingness: among `analytic_participant`, 8/72 (11%) are true item nonresponse; the other 28 overall-missing are non-participants (never asked) and are *structurally* NA.
3. **Three drug variables kept separate** with explicit provenance in variable labels:
   - `drugs_used_facil` — facilitator, ceremonies led (select-multiple string + one-hot).
   - `drug_used_part` — participant, ceremonies attended (select-multiple string + `drug_used_part/*` one-hot).
   - `drugs_used_part` — participant, most-recent ceremony (select-one).
   Parse space-separated select-multiple strings into indicator matrices; verify parsed indicators match the platform's `col/option` one-hot columns (cross-check, don't trust one alone).
4. **`pna`/`not_sure` policy**: a single helper applies the retain-as-category rule uniformly; denominators in every table explicitly show `n answered`, `n pna`, `n not_sure`, `n structural-skip`.
5. **Likert decodes** tied to `list_name`: `agreement_scale`, `agreement_scale_2`, `frequency_scale`, `legal_know_scale(_2)`, `legal_worry_scale`, `trust_level`, `comfort_safe`, `phys_comfort`, etc. — each mapped to an ordered categorical with the choices-sheet order.

### 2.4 Univariate (Objectives 1–2) — ✅ implemented
- **Sociodemographics** (`age`, `gender_idt`, `academic`, `civil`, `work`, `econ`, `health_insurance`, religion/spirituality, `municipality`/`country`/`hispanic`): frequency + %, and for `age` mean/median/SD/range/IQR. Report separately for participant-only, facilitator, and dual where cell sizes allow (else pooled, with n<5 suppression).
- **Ceremony practice/context**: substances (all three drug vars, clearly labeled), `frequency`/`amount_cer`, `ceremony_env`, `ceremony_format`, `ceremony_duration`, `last_ceremony_time/place`, facilitator training (`training_facilitator` one-hot), `inst_ceremonia`, `dosis_choice`. Split into **§3.5 facilitator practice context** (facilitator branch only, n≈8 — most cells at/below suppression floor, descriptive only) and **§3.6 participant ceremony frequency / most-recent-ceremony context** (participant branch, n≈65–72), per the project rule against conflating facilitator- and participant-reported items.
- Every table carries its own denominator and missingness breakdown.
- **Data-quality fixes surfaced during implementation**: `ceremony_duration` codes `4_6`/`7_12` lost their underscore on export and arrived as the ints `46`/`712` (only these two — codes with a letter suffix were unaffected); remapped in `data_prep.fix_ceremony_duration` with the collision checked against the choices sheet, not guessed. One respondent's `amount_cer_year` was recorded as `-3` (impossible for a count); corrected to `3` (client-confirmed sign-entry error) in `data_prep.fix_amount_cer_year`. Note: this respondent's `amount_cer` (lifetime, =2) is now *less* than `amount_cer_year` (past 12 months, =3) — a residual internal inconsistency in that row worth a source-data check, separate from the sign fix.

### 2.5 Bivariate (Objectives 3–4) — nonparametric, with the infeasibility stated — ✅ prep→outcome; integration proxy ❌ dropped per client; ✅ perceived-safety-by-training
Because `ceremony_good` is ordinal and cells are thin, replace the proposed t-test/ANOVA with:

1. **Preparation vs. `ceremony_good`** (the only arm with usable n): `prep_part` (sí / a_veces / no) → **Kruskal–Wallis**; if the "no"+"a_veces" arms are < 5 after listwise handling, collapse to `prep_part ∈ {any prep, none}` and use **Mann–Whitney U** with rank-biserial effect size + bootstrap CI. Report medians and full distributions, not means.
2. **Integration proxy** — ❌ **dropped per client decision.** No clean participant "received integration support" item exists, so rather than construct a proxy composite the analysis focuses on **preparation → outcome** directly (item 1 above). The `med_asist`/`self_care` items remain available for descriptive reporting but are not used to synthesize an integration exposure. *(Original proposal: define `integration_any` from `med_asist='si'` or structured `self_care`; retired.)*
3. **Perceived safety by facilitator training / protocol** — ✅ **implemented** (`report.section_bivariate` §4.4–4.5). The proposal's literal facilitator-side items (`training_facilitator`, `safe_ceremony`, `emergency_plan`, `protocol_bad_exp`) live on the facilitator self-report branch (n=8), unlinked to any specific participant — the same structural gap as the retired integration proxy (item 2), so they cannot be validly crossed with a participant's perceived safety. Operationalized instead via two **participant-side proxies**: `facil_background` (participant's pre-ceremony knowledge of the facilitator's background/training) and `screening_quest` (whether the facilitator asked screening questions), crossed against `comfort_safe` and `trust_level` via Kruskal–Wallis (n≈65–72, usable). Facilitator self-report items are reported separately as descriptive context only (§4.5; all subgroups ≤ suppression floor). `opinion_safe` is free text, already covered under §2.6 qualitative, not part of this quantitative bivariate.
4. **Assumption checks & fallbacks**: for any comparison where a parametric test is even considered, run Shapiro–Wilk (normality) and Levene (variance homogeneity); default to the nonparametric result. Report exact p, effect size (rank-biserial / epsilon-squared), and CI.
5. **Multiplicity** — ✅ **implemented** (`report.section_bivariate` §4.7): the primary comparison (prep → `ceremony_good`) is pre-declared and reported uncorrected; the 3-level preparation sensitivity test, the four perceived-safety-by-training comparisons, and the harm-reduction practice index (§4.6, see §3 item 5) form one secondary/exploratory family, corrected jointly via Benjamini–Hochberg FDR (`stats_helpers.bh_fdr`).

### 2.6 Qualitative (open-text thematic analysis) — ✅ implemented (`analysis/qualitative.py`, report §6)
Open-text fields: the authoritative list is `survey[type=='text']` (37 fields after excluding the `nickname`/`password` identifiers) — **not** the plan's prose list, which mislabeled `add_share` as free text; it is actually a `select_one si_no_pna` gate for the real free-text field `additional_info`. Responses are **mixed Spanish/English** (285 non-empty answers: ~77% es, ~19% en, ~4% mixed/other by a lightweight heuristic).
- Extract all non-empty open-text into one long-format table (`respondent_id`, `field`, `text`, `language_guess`) written to `outputs/tables/opentext_corpus.csv`. ✅
- Operationalize applied thematic analysis *in Python as a coding scaffold*, not automated interpretation: normalize text, generate a frequency/keyword view (legality, education, facilitator vetting, medical presence, consent) to seed a codebook, and export `outputs/tables/opentext_manual_coding.csv` — one row per non-empty answer, empty `code_1..code_3` columns for the research team's manual coding. The pipeline supports the human analysis; it does not replace it. ✅ (`opinion_safe` shows a dominant "legalization/regulation + facilitator training/education" cluster on inspection — a natural first code family.)
- Data-quality finding surfaced during implementation: `no_comfort_safe` has 0 responses not from low uptake but because its `relevant` condition (`comfort_safe='some_uncomf' AND comfort_safe='very_uncomf'`) requires one variable to equal two values at once — the item is structurally unreachable (instrument bug, flagged for the team, not fixed retroactively).

---

## §3. Additional analyses recommended (fuller variable set)

Each item: rationale + priority. Priority reflects both scientific value and the fact that several surfaced directly from the data.

1. **[HIGH] Safety / adverse-event domain.** — ✅ **done:** prevalence of `non_con_contact` (Wilson CI) and aggregate `exp_crisis` (report §5.1–5.2), plus the association with facilitator `training_facilitator`, `screening_quest`, `protocol_bad_exp`, `emergency_plan`, `safe_ceremony` (report §5.3–5.4). The association analysis splits by structural gap (same rationale as §2.5 item 3): `non_con_contact` (participant-reported) is crossed with the **participant-side proxies** `facil_background`/`screening_quest` via a permutation chi-square (Fisher–Freeman–Halton substitute, `stats_helpers.chi2_perm`); `exp_crisis` (facilitator-reported) is crossed with the **facilitator's own** `training_facilitator`/`safe_ceremony`/`protocol_bad_exp`/`emergency_plan` (same n≈8 respondents, no linkage gap) via Fisher's exact test (`stats_helpers.fisher_or`). Both test families are BH-FDR corrected jointly (§5.4); none survive correction. Prevalence of `non_con_contact` (5 sí / 1 not_sure / 61 no / 33 skip → ~7.5% among 67 answering) and `non_con_contact_recent`; `exp_crisis` sub-item prevalence (incl. `suicide_idea`, `panic_atk`) reported as a distinct outcome domain from satisfaction. *Rationale:* serious, populated, and entirely absent from the proposal. Cross-tabs use standard n<5 masking (team decision, see §0), not full withholding.
2. **[HIGH] Data-quality sensitivity + duplicate handling.** — 🟡 **partial:** attention-check + duplicate flagging ✅ (`outputs/tables/data_quality_flags.csv`); ⬜ sensitivity re-run excluding adjudicated flags pending team adjudication. Score attention checks per branch (facilitator: `atencion_1/2/3`; participant: `atencion_3_2/4/5/6`); flag (not drop) failures. Flag candidate duplicates by `nickname`+`password` matches (repeats confirmed: password "Amor" ×4; nicknames ×2) plus `_submission_time` proximity, for client adjudication. *Rationale:* snowball + unpopulated `ev_dup` leave data integrity unscreened.
3. **[HIGH] Reframe role structure explicitly.** — ✅ **done:** role-composition table in report §3.1. Facilitator-only vs. participant-only vs. dual-role, now that overlap is confirmed. *Rationale:* corrects the proposal's false partition and is prerequisite to interpreting every other contrast.
4. **[MEDIUM] Multivariable ordinal model for `ceremony_good`.** — ✅ **done** (`report.section_bivariate` §4.8). The full covariate set (age, gender, prep, trust, screening) is not estimable: `gender_idt` has cells too thin for a 4-level categorical predictor (non-binary n=4, `pna` n=1), and `screening_quest` overlaps with `trust_level`/`facil_background` already used in §4.4 — added together they risk collinearity the N can't resolve. Per the plan's fallback, fit a **parsimonious 3-predictor** proportional-odds model (statsmodels `OrderedModel`, logit link): `age`, `prep_any` (any prep vs. none), `trust_level_num`. The outcome is additionally collapsed from the raw 7-level `ceremony_good` to 3 ordered levels (`ceremony_good_3lvl`, model-only) because the low end has cells as thin as n=1–3 — a separation risk in a 7-level ordinal logit at N≈62. Result (n=62 complete cases): `trust_level` OR=2.20 [1.06–4.53], p=.033; `prep_any` OR=5.21 [0.84–32.41], p=.077; `age` OR=0.99 [0.94–1.03], p=.527; omnibus LR χ²(3)=8.68, p=.034, McFadden R²=0.07. Reported with an explicit power caveat (~12 cases/parameter; proportional-odds assumption assumed, not formally tested) — **exploratory/hypothesis-generating only**. *Rationale:* moves beyond unadjusted pairwise tests without overfitting.
5. **[MEDIUM] Harm-reduction practice index.** — ✅ **done** (`report.section_bivariate` §4.6/§4.5, `report.section_safety` §5.3.3). The proposal's single composite ("prep + `emergency_plan` + `facil_background` + `safe_ceremony`") mixes facilitator self-report items (`emergency_plan`, `safe_ceremony`, n=8) with participant self-report items (`prep_part`, `facil_background`) — the same unlinked-respondents gap already resolved for the integration proxy (§2.5 item 2) and perceived safety (§2.5 item 3/§4.4). Split into two branch-specific composites instead: **participant-side** (`prep_any` + `facil_background` + `screening_quest`, 0–3, n=54 complete cases) — Cronbach's α=0.14 (95% CI −0.36–0.47), i.e. the three items don't cohere as one latent construct and the score is better read as a simple count of practices present; Kruskal–Wallis vs. `ceremony_good` is non-significant (H=2.09, p=.352) and vs. binarized `non_con_contact` is non-significant (χ²=0.56, p=.641; both included in the relevant BH-FDR families, §4.7/§5.4). **Facilitator-side** (training + `safe_ceremony` + `protocol_bad_exp` any-response + `emergency_plan`, 0–4, n=7) is reported descriptively only — two of four components are answered "yes"/no-variance by every facilitator, and no facilitator selected a formal (`sí`) `emergency_plan`, so the branch is close to constant; neither reliability nor an `exp_crisis` association test is meaningful at that n. *Rationale:* turns scattered protective-factor items into an interpretable exposure — result is a real (if null) hypothesis-generating finding, not just a pipeline placeholder.
6. **[MEDIUM] Substance-stratified description.** — ✅ **done:** substance frequencies (`drug_used_part`, ceremonies attended) charted in report §3.4; stratified satisfaction/safety by substance in `report.section_bivariate` §4.9. Stratifies by `drugs_used_part` (most-recent-ceremony substance, select-one) rather than the multi-ceremony `drug_used_part`, so each respondent contributes one substance exposure. Individually reportable groups: ayahuasca (n=23), hongos_mágicos (n=31); every other substance (cacao, DMT, tobacco, LSD, "other" — each n<5) pooled into one "other/rare substances" group (n=11), per the plan's rule; `pna` (n=1) and non-response excluded from the grouping variable as missing exposure (same convention as `prep_3lvl`). Two tests, one small secondary/exploratory family (BH-FDR, §4.9.3), distinct from §4.7/§5.4: **4.9.1** `ceremony_good` by substance group (Kruskal–Wallis): medians 5 (ayahuasca, n=22) / 6 (mushrooms, n=30) / 6 (other, n=11), H=4.98, p=.083 (q=.166, ns). **4.9.2** `non_con_contact` by substance group (permutation χ², masked cross-tab, n=65 pairwise-complete): χ²=3.70, p=.486 (q=.486, ns). Neither survives correction — reported as hypothesis-generating only, consistent with the rest of the report's small-cell caveats. *Rationale:* materially different risk/benefit profiles.
7. **[MEDIUM] Psychometric check.** — ✅ **done** (`report.section_psychometrics` §8). The instrument does not actually contain multi-item Likert batteries — every Likert-shaped `list_name` maps to ≤2 items, and most 2-item pairs split across the facilitator/participant branches (same unlinked-respondents gap as the integration proxy/harm-reduction index). Two genuine same-respondent pairs are testable: **trust/comfort** (`trust_level` + `comfort_safe`, both participant-side; Spearman $\rho=0.39$, $p=.002$, Cronbach's $\alpha=0.58$ [0.31–0.74], $n=64$) and **legal knowledge, general vs. most-recent-ceremony** (`info_est_legal_part` + `legal_know_part`, harmonized to a shared 0–4 ordinal code across their two different `list_name` option sets — `config.LEGAL_KNOW_HARMONIZED`; $\rho=0.79$, $p<.001$, $\alpha=0.86$ [0.75–0.92], $n=55$). Three other candidates implied by the proposal's wording are reported as **not testable**, with reasons (§8.3): `impact_positive`/`impact_negative` (`impact_positive` has zero variance — all 67 respondents answered "somewhat_agree"); `est_legal_worry`/`est_legal_worry_part` (asymmetric, apparently-broken skip logic — `est_legal_worry` gated on the *other* item equaling `pna`, reaching only $n=6$, same bug category as `no_comfort_safe`); `entheogen_legal_know` (facilitator-branch item, unlinked to any participant). *Rationale:* first reliability evidence for a novel, non-validated PR instrument; both alpha estimates are 2-item ($\alpha=2r/(1+r)$), reported as suggestive, not validated multi-item scales.
8. **[LOW–MED] Legal knowledge/worry correlates.** — ✅ **done** (`report.section_legal` §9). Per §8.3, `est_legal_worry` (general; gated on `info_est_legal_part='pna'`, $n=6$) and `entheogen_legal_know` (facilitator-branch, $n=7$, unlinked to participants) are excluded as not-testable (§9.5) — client-confirmed scope, same rationale as §8.3. Uses the three well-populated participant-side legal items — `info_est_legal_part_num`/`legal_know_part_num` (harmonized 0–4 legal knowledge, §8.2) and `est_legal_worry_part` (0–4 legal worry) — against three participant-side outcomes (client-confirmed set): disclosure (`med_couns_part`), screening participation (`screening_quest`), safety (`non_con_contact`), via Kruskal–Wallis (9 tests, one BH-FDR family, §9.4). One nominally significant raw result — legal worry is higher among those who disclosed participation to a health professional ($H=6.92$, $p=.031$, $n=8$ "sí") — does not survive correction ($q=.283$) and is thin ($n<5$ not-sure cell); reported as hypothesis-generating only. All other comparisons are null. *Rationale:* legality shapes help-seeking; `opinion_safe` free-text shows legality is the respondents' dominant concern.
9. **[MEDIUM] Geographic/residency description.** — ✅ **done:** country-of-residence table in report §3.3 (82 PR / ~4 non-PR). *(Municipality-level tabulation ⬜ still optional.)* *Rationale:* directly bears on the generalizability claims already in Limitations — must know whether "PR sample" is literally PR-resident.

---

## §4. Final deliverable — structured plan (data prep → confirmed analysis → additions → reporting)

### 4.1 Data preparation / cleaning rules (canonical) — ✅ implemented
- Import with UTF-8; decode every categorical via the `choices` sheet; attach skip logic from the `survey` sheet.
- Derive `role` and analytic-inclusion flags; exclude 13 abandoned-blank, retain 14 screen-outs for a screen-out table only; dual-role in both analytic sets.
- Decode `ceremony_good` `_N`→0–6 ordered; keep `pna` as a level; separate structural vs. item missingness.
- Keep `drugs_used_facil` / `drug_used_part` / `drugs_used_part` distinct; parse select-multiple strings to indicators and cross-check against one-hot columns.
- Apply `pna`/`not_sure`-as-category uniformly; every table shows answered / pna / not_sure / structural-skip counts.
- Generate quality flags (attention per branch, duplicate candidates) — **flag, never drop**.

### 4.2 Confirmed analytic plan (executable specifics) — 🟡 partial
- Univariate: §2.4 (✅). Bivariate: §2.5 (🟡 — prep→`ceremony_good` ✅). Qualitative: §2.6 (✅).

### 4.3 Recommended additions — 🟡 partial
- §3, prioritized. HIGH items: safety domain ✅, data-quality/duplicates 🟡, role-structure ✅ (folded into the main report); multivariable ordinal model ✅; harm-reduction practice index ✅; substance-stratified satisfaction/safety ✅; psychometric check ✅; legal knowledge/worry correlates ✅. Remaining: data-quality sensitivity re-run 🟡 pending team adjudication.

### 4.4 Reporting rules given small-N / anonymity / sensitive content — ✅ implemented
- **Suppression:** any reported cell with n<5 is suppressed (shown as "<5" / masked), including in cross-tabs and subgroup medians.
- **Denominators:** always explicit; never report a percentage without its base and its pna/not_sure/skip breakdown.
- **Inference discipline:** descriptive study — no causal, prevalence-to-population, or weighted-representativeness claims; effect sizes with CIs over bare p-values; primary vs. exploratory clearly separated.
- **Sensitive items** (`non_con_contact`, `exp_crisis/suicide_idea`): neutral clinical language, aggregate-only, suppressed below n<5. Present as prevalence within answered base with the skip/pna denominators shown. *Clarified 2026-07-15 (§0):* the §3 item 1 association analysis is the one exception where cross-tabs of these items are published, under standard n<5 masking rather than full withholding — see `report.section_safety` §5.3.
- **Reproducibility:** all outputs regenerate from `analysis/` scripts; quality-flag CSV handed to the team for adjudication before any figures are finalized.

---

### Open items for the client before implementation locks
- Confirm the **integration proxy** composition in §2.5(2) (which `self_care` options count as "integration support").
- Confirm treatment of the **8 dual-role who did/didn't pass `pause_facil`** — include their (often missing) participant items as structural-skip, agreed?
- Confirm **render target**: HTML always; PDF via Quarto+LaTeX if available, else WeasyPrint (affects environment setup only).
