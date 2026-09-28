# Ceremonial Entheogen Use in Puerto Rico — Descriptive Analysis Report

*Descriptive study (unweighted); no causal or population-prevalence claims. Subgroup cells with $n<5$ are suppressed.*

## 1. Sample and framing

- Rows collected: **100** (target N=100 met).
- Participants (`is_participant='si'`): **72**; facilitators (`is_facilitator='si'`): **8**; dual-role: **7**.
- Outcome `ceremony_good` decoded `_0`…`_6` $\to 0$–$6$, treated as **ordinal**.

## 2. Methods (summary)

Nonparametric throughout (Mann–Whitney $U$, Kruskal–Wallis $H$) with rank-biserial $r_{rb}$ / epsilon-squared $\varepsilon^2$ effect sizes; `pna`/`not_sure` retained as categories; $n<5$ suppression; Wilson 95% CIs for prevalences. Full rationale in `ANALYSIS_PLAN.md`. $\varepsilon^2$ uses the standard bias-corrected formula, which can return small negative values when the effect is at or indistinguishable from zero; these are displayed truncated to 0.00 (marked $^\dagger$) rather than reported as negative, applied uniformly to every $\varepsilon^2$ in this report.

## 3. Univariate description (Objectives 1–2)

Descriptive sample: **N = 73** adults who identified a role (participant, facilitator, or both). Of the 13 abandoned-blank submissions excluded, none reached the role fork. Of the 87 respondents who reached the role fork, 14 (16%) answered "no" to both role questions and are reported as a screening-yield rate rather than a described subgroup; they are excluded from the analytic sample. Role-specific analyses in §4–§5 restrict to participants/facilitators as noted.

### 3.1 Role composition

| role | n | % of 100 |
| --- | --- | --- |
| participant_only | 65 | 65% |
| screenout_no_no | 14 | 14% |
| abandoned_blank | 13 | 13% |
| dual | 7 | 7% |
| facilitator_only | <5 | 1% |

Facilitator and participant roles **overlap** (7 dual-role); they are not a partition. Dual-role respondents appear in both role-specific analyses below, per protocol.

### 3.2 Sociodemographics (analytic sample)

- **Age** (n=72): mean $\bar{x}=42.4$, median $\tilde{x}=41$, SD $s=11.9$, range 21–71, IQR 34–50.


**Gender identity** (answered base n=71):

| category | n | % answered |
| --- | --- | --- |
| Woman | 35 | 49% |
| Man | 30 | 42% |
| Non-binary | <5 | 6% |
| I'd prefer not to answer | <5 | 3% |
| (structural skip) | <5 |  |


**Education** (answered base n=72):

| category | n | % answered |
| --- | --- | --- |
| Bachelor's | 34 | 47% |
| Masters | 19 | 26% |
| Associate's Degree | 7 | 10% |
| High school Diploma/GED | 6 | 8% |
| I'd prefer not to answer | <5 | 4% |
| Doctorate | <5 | 4% |
| (structural skip) | <5 |  |


**Economic situation** (answered base n=72):

| category | n | % answered |
| --- | --- | --- |
| Comfortable: I can cover my needs and some extras | 44 | 61% |
| b. Tight: I can cover basic needs with some difficulty | 20 | 28% |
| c. Difficult: I often cannot cover my basic needs | 6 | 8% |
| d. Prefer not to answer | <5 | 3% |
| (structural skip) | <5 |  |

### 3.3 Residency / diaspora check


**Country of residence** (answered base n=72):

| country of residence | n | % answered |
| --- | --- | --- |
| Puerto Rico | 68 | 94% |
| United States | <5 | 4% |
| Spain | <5 | 1% |
| (structural skip) | <5 |  |

Residency is treated as a **descriptive covariate**, not an inclusion filter, per protocol. Non-PR respondents temper any PR-population read of the sample.

### 3.4 Substances (participant-reported)

![Substances](figures/fig_substances.png)


**Substances used across ceremonies attended** (select-multiple; answered base n=67 participants; percentages need not sum to 100%):

| substance | n | % of base |
| --- | --- | --- |
| Magic mushrooms (“shrooms”) | 50 | 75% |
| Ayahuasca | 43 | 64% |
| Tobacco | 38 | 57% |
| Cacao | 23 | 34% |
| DMT (dimethyltryptamine) | 17 | 25% |
| LSD (lysergic acid diethylamide) | 13 | 19% |
| MDMA (“molly”) | 10 | 15% |
| Ketamine | <5 | 6% |

The three drug variables are kept distinct: `drugs_used_facil` (facilitator-led), `drug_used_part` (participant, ceremonies attended, shown above), `drugs_used_part` (participant, most-recent ceremony).

### 3.5 Facilitator practice context

**Facilitator-reported only** (`is_facilitator='si'`, base n=8) — do not conflate with the participant-side context in §3.6. At this base, most category cells fall at or below the $n<5$ suppression floor; tables are reported for completeness with cells masked, and should be read as **descriptive only**.


**Training / experience preparing to facilitate** (`training_facilitator`, select multiple; % of facilitator base):

| training/experience | n | % of base |
| --- | --- | --- |
| Personal experience and self-study | 6 | 75% |
| Mentorship or apprenticeship learning | <5 | 50% |
| Family or ancestral tradition | <5 | 38% |
| Formal Certifications | 0 | 0% |
| Academic courses or workshops | 0 | 0% |
| Other | 0 | 0% |
| None of the above | 0 | 0% |
| Prefer not to answer | 0 | 0% |
(base n=8)


**Gives participants preparation instructions (`inst_ceremonia`)** (answered base n=7):

| response | n | % answered |
| --- | --- | --- |
| Yes | 6 | 86% |
| Prefer not to answer | <5 | 14% |
| (structural skip) | <5 |  |


**How dose is decided per participant** (`dosis_choice`, answered base n=7):

| dosing approach | n | % answered |
| --- | --- | --- |
| I allow participants to decide their dose | <5 | 43% |
| Other | <5 | 29% |
| A conservative initial dose followed by stronger additional doses | <5 | 14% |
| A single dose for everyone | <5 | 14% |
| (structural skip) | <5 |  |


**Typical ceremony environment** (`ceremony_env`, answered base n=7):

| environment | n | % answered |
| --- | --- | --- |
| 3. In an outdoor space or near nature | 6 | 86% |
| 1. In my home | <5 | 14% |
| (structural skip) | <5 |  |

### 3.6 Participant ceremony frequency and most-recent-ceremony context

**Participant-reported only** (`is_participant='si'`, base n=72).


**Ceremony frequency**

- **Lifetime ceremonies attended (`amount_cer`)** (n=67): median $\tilde{x}=6$, mean $\bar{x}=15.1$, SD $s=35.7$, range 1–250, IQR 3–12.

- **Ceremonies attended in the past 12 months (`amount_cer_year`)** (n=67): median $\tilde{x}=1$, mean $\bar{x}=1.3$, SD $s=1.7$, range 0–8, IQR 0–2.


**Most-recent-ceremony context**


**Time since last ceremony (`last_ceremony_time`)** (answered base n=66):

| category | n | % answered |
| --- | --- | --- |
| 4. More than 12 months ago | 30 | 45% |
| 2. 2 to 6 months ago | 20 | 30% |
| 3. 7 to 12 months ago | 11 | 17% |
| 1. During the past month | <5 | 6% |
| 5. Prefer not to answer | <5 | 2% |
| (structural skip) | 6 |  |


**Place of last ceremony (`last_ceremony_place`)** (answered base n=67):

| category | n | % answered |
| --- | --- | --- |
| 3. A natural setting (e.g., forest, beach, mountain) | 37 | 55% |
| 5. A private home (mine or someone else’s) | 15 | 22% |
| 2. A retreat center or wellness facility | 9 | 13% |
| 6. Other | <5 | 4% |
| 4. An urban or residential space used informally (e.g., house, apartment, studio, clinic) | <5 | 3% |
| 7. Prefer not to answer | <5 | 1% |
| (structural skip) | 5 |  |


**Retreat/series vs. single ceremony (`ceremony_format`)** (answered base n=65):

| category | n | % answered |
| --- | --- | --- |
| 2. No, a single ceremony | 48 | 74% |
| 1. Yes, a retreat or a series of ceremonies | 13 | 20% |
| 4. Prefer not to answer | <5 | 5% |
| 3. I’m not sure | <5 | 2% |
| (structural skip) | 7 |  |


**Total duration (`ceremony_duration`)** (answered base n=65):

| category | n | % answered |
| --- | --- | --- |
| 3. 4 to 6 hours | 19 | 29% |
| 5. Overnight (~12+ hours) | 19 | 29% |
| 4. 7 to 12 hours | 14 | 22% |
| 2. 1 to 3 hours | 7 | 11% |
| 6. 2 to 3 days | <5 | 6% |
| 7. 4 to 6 days | <5 | 2% |
| 1. Less than 1 hour | <5 | 2% |
| (structural skip) | 7 |  |

## 4. Bivariate analyses (Objectives 3–4, revised)

The original study proposal specified a four-arm preparation×integration design; this is **not estimable** from the collected data, as the instrument contains no clean participant *integration-received* item and the preparation split is badly unbalanced. Per protocol, we analyze **preparation → outcome** directly. The outcome `ceremony_good` is treated as **ordinal** (heavy ceiling), so tests are nonparametric.

### 4.1 Distribution and group medians

![ceremony_good distribution](figures/fig_ceremony_good.png)

Among participants, 63/72 answered `ceremony_good`; the remaining are item nonresponse (structural skips affect non-participants, excluded here). Distribution is strongly ceiling-weighted (median $\tilde{x}=6$).

| group | n (answered outcome) | median | IQR |
| --- | --- | --- | --- |
| Any preparation | 58 | 6 | 5–6 |
| No preparation | 5 | 4 | 3–5 |

![Preparation vs outcome](figures/fig_prep_outcome.png)

### 4.2 Primary comparison — Mann–Whitney $U$

Any-preparation ($n_1=58$) vs. no-preparation ($n_2=5$): $U=218.0$, $p=0.041$ (asymptotic, tie-corrected normal approximation), rank-biserial $r_{rb}=0.50$, common-language effect size $\mathrm{CLES}=0.75$.

**Robustness check — exact/permutation test.** scipy's own `method='exact'` for Mann–Whitney applies *no* tie correction to the null distribution, which is invalid given how heavily tied `ceremony_good` is at this ceiling; a 10,000-resample label-permutation test (seed 20260715, same convention as the permutation $\chi^2$ tests elsewhere in this report) resamples the tied ranks directly and stays valid: $p=0.024$. This is *more* significant than the asymptotic result above, not less — the asymptotic approximation is not the more conservative of the two at this $n_2=5$.

> **Interpretation.** The no-preparation group is $n_2=5$ (at the $n<5$ suppression floor). Even a sizable effect here is statistically fragile; report as **suggestive, exploratory**, not confirmatory. Direction: preparation is associated with higher reported satisfaction.

### 4.3 Sensitivity — 3-level preparation (Kruskal–Wallis $H$)

Across `prep_part` levels (si: 52, a_veces: 6, no: 5): $H=4.24$, $p=0.120$, $\varepsilon^2=0.04$. The `no` and `a_veces` cells are below $n<5$ once the outcome is non-missing — interpret as descriptive only.

`pna`/`not_sure` are retained as substantive categories in all frequency tables but are excluded from the ordinal numeric tests (they carry no rank position).

### 4.4 Perceived safety by facilitator training/protocol (participant-perceived proxy; secondary, exploratory)

The `training_facilitator`/`safe_ceremony`/`emergency_plan`/`protocol_bad_exp` items as specified in the original proposal are **facilitator self-report** ($n=8$), a different, unlinked set of respondents from the participants who report perceived safety — there is no ceremony/facilitator ID connecting a given participant to the facilitator who ran their ceremony, so those items cannot be crossed with participant-reported safety without falsely pairing unrelated respondents (the same unlinked-respondent limitation that ruled out the integration-proxy comparison in §4). This analysis instead uses the two **participant-side proxies** for facilitator training/protocol: `facil_background` (did the participant know about the facilitator's background/training beforehand) and `screening_quest` (did the facilitator ask screening questions before the ceremony). Facilitator self-report is presented separately, descriptively, in §4.5.

**4.4.1. In-ceremony comfort/safety (`comfort_safe`) by `facil_background`**

| group | n (answered outcome) | median | IQR |
| --- | --- | --- | --- |
| 1. Yes | 54 | 3 | 3–3 |
| 3. A little | 8 | 3 | 2–3 |
| 2. No | <5 | 2 | 2–2 |

$H=2.24$, $p=0.326$, $\varepsilon^2=0.00$. Cells below $n<5$ (no) make this descriptive/exploratory only.

**4.4.2. In-ceremony comfort/safety (`comfort_safe`) by `screening_quest`**

| group | n (answered outcome) | median | IQR |
| --- | --- | --- | --- |
| 1. Yes | 39 | 3 | 3–3 |
| 2. No | 15 | 3 | 2–3 |
| 3. I’m not sure | 7 | 3 | 3–3 |

$H=2.40$, $p=0.301$, $\varepsilon^2=0.01$.

**4.4.3. Trust in facilitator (`trust_level`) by `facil_background`**

| group | n (answered outcome) | median | IQR |
| --- | --- | --- | --- |
| 1. Yes | 54 | 4 | 3–4 |
| 3. A little | 8 | 3 | 2–3 |
| 2. No | <5 | 3 | 2–4 |

$H=8.15$, $p=0.017$, $\varepsilon^2=0.10$. Cells below $n<5$ (no) make this descriptive/exploratory only.

**4.4.4. Trust in facilitator (`trust_level`) by `screening_quest`**

| group | n (answered outcome) | median | IQR |
| --- | --- | --- | --- |
| 1. Yes | 39 | 4 | 3–4 |
| 2. No | 15 | 4 | 3–4 |
| 3. I’m not sure | 7 | 4 | 3–4 |

$H=0.77$, $p=0.679$, $\varepsilon^2=0.00^{\dagger}$.

### 4.5 Facilitator self-reported training/protocol (context, descriptive only, $n=8$)

Reported for context; **not** crossed with any safety outcome (see §4.4 for why). Every subgroup here is at or below the $n<5$ suppression floor, so no group comparison is meaningful — counts are shown against the full facilitator base.

**Training/experience (`training_facilitator`, select-multiple):**

| form of training | n | % of facilitators |
| --- | --- | --- |
| Personal experience and self-study | 6 | 75% |
| Mentorship or apprenticeship learning | <5 | 50% |
| Family or ancestral tradition | <5 | 38% |
(base $n=8$)

**Screening/safety approach (`safe_ceremony`, select-multiple):**

| approach | n | % of facilitators |
| --- | --- | --- |
| I have an initial conversation or interview with the person. | 6 | 75% |
| I ask about any relevant medical history or physical health condition. | <5 | 50% |
| I ask whether they are currently taking any medication. | <5 | 50% |
| I ask questions to identify any psychological or mental health challenges that could make the ceremony unsafe. | <5 | 38% |
| I welcome anyone who feels called to participate. | <5 | 25% |
| Other | <5 | 25% |
(base $n=8$)

**Response to a difficult experience (`protocol_bad_exp`, select-multiple):**

| response | n | % of facilitators |
| --- | --- | --- |
| Singing, playing music, or using sound to guide them | 5 | 62% |
| Use grounding exercises (e.g., breathing, sensory focus) | <5 | 50% |
| Offer calming or supportive words | <5 | 38% |
| Use physical touch (with prior consent or as culturally appropriate) | <5 | 25% |
| Other | <5 | 25% |
| Use a “trip killer” or something to stop the psychoactive effect (e.g., a benzodiazepine or an antipsychotic medication) | <5 | 12% |
| I have never been in this type of situation | <5 | 12% |
(base $n=8$)

**Emergency plan (`emergency_plan`):**

| response | n | % answered |
| --- | --- | --- |
| I have an informal or unwritten approach | <5 | 57% |
| Depends on the situation | <5 | 43% |
| (structural skip) | <5 |  |

**Composite harm-reduction/readiness score** (training + safety-screening approach + distress-response protocol + emergency plan, each 0/1, `emergency_plan` informal/depende given 0.5 partial credit; range 0–4, complete cases only):

| score | n | % answered |
| --- | --- | --- |
| 3.5 | 6 | 86% |
| 2.5 | <5 | 14% |
(complete-case $n=7$)

`training_facilitator` and `safe_ceremony` (any substantive response) are answered "yes" by every facilitator who answered them (no variance), and no facilitator selected the formal (`sí`) `emergency_plan` option (all informal/conditional) — so this branch is close to a constant. With that little variance and $n=7$, neither a reliability statistic nor an association test with `exp_crisis` is meaningful here; reported for completeness only, for the same reason given in §5.3.2. The participant-side version of this index (§4.6) carries the actual inferential weight for this recommendation.

### 4.6 Harm-reduction practice index — participant-side score vs. `ceremony_good`

The composite specified in the original proposal ("prep + `emergency_plan` + `facil_background` + `safe_ceremony`") mixes **facilitator self-report** items (`emergency_plan`, `safe_ceremony`, $n=8$) with **participant self-report** items (`prep_part`, `facil_background`) — the same unlinked-respondent limitation noted for the integration proxy and the perceived-safety comparisons (§4.4): these are two different, unlinked sets of respondents, so one mixed score cannot be validly built. As in §4.4, the composite is instead built in two branch-specific versions: a **participant-side index** here (`prep_any` + `facil_background` + `screening_quest`, the three participant-answerable protective-practice items — `screening_quest` substitutes for the facilitator-side `safe_ceremony`/`emergency_plan` items as the participant-observable analog), and a **facilitator-side descriptive composite** reported for completeness at the end of §4.5. `pna`/`not_sure` are item-missing here (not scored 0), matching the convention already used to build `prep_any`.

**Score distribution** (0–3, complete-case $n=54$ of 72 participants answering all three items):

| score | n | % answered |
| --- | --- | --- |
| 3.0 | 35 | 65% |
| 2.0 | 16 | 30% |
| 1.0 | <5 | 6% |

**Zero of 54** complete-case participants reported none of the three practices (no preparation, no prior knowledge of the facilitator's background, and no screening) — every respondent with complete data on all three items reported at least one. This closes the descriptive gap the earlier draft flagged: the index's floor is empty at this base, not merely thin.

**Internal consistency.** Cronbach's $\alpha=0.14$ (95% CI -0.36–0.47, $n=54$, 3 items). This is low — the three items likely capture **distinct** protective practices (preparation, facilitator vetting, being screened) rather than one shared latent construct, so the composite score below should be read as a simple count of practices present, not a validated scale.

**Association with `ceremony_good`** (Kruskal–Wallis across score levels):

| score | n (answered outcome) | median | IQR |
| --- | --- | --- | --- |
| 1 | <5 | 4 | 2–5 |
| 2 | 14 | 5 | 5–6 |
| 3 | 34 | 6 | 5–6 |

$H=2.09$, $p=0.352$, $\varepsilon^2=0.00$. Score 1 is below $n<5$ once the outcome is non-missing — interpret as descriptive only.

### 4.7 Multiplicity correction — secondary/exploratory family (Benjamini–Hochberg FDR)

The primary comparison (§4.2, preparation vs. `ceremony_good`, pre-declared) is reported uncorrected. Every other bivariate test run so far — the 3-level preparation sensitivity (§4.3), the four perceived-safety-by-training comparisons (§4.4), and the harm-reduction practice index (§4.6) — forms one secondary/exploratory family, corrected jointly here.

| test | raw $p$ | BH $q$ | significant at $q<.05$ |
| --- | --- | --- | --- |
| Preparation (3-level) → `ceremony_good` (KW) | 0.120 | 0.359 | no |
| In-ceremony comfort/safety (`comfort_safe`) by `facil_background` | 0.326 | 0.422 | no |
| In-ceremony comfort/safety (`comfort_safe`) by `screening_quest` | 0.301 | 0.422 | no |
| Trust in facilitator (`trust_level`) by `facil_background` | 0.017 | 0.102 | no |
| Trust in facilitator (`trust_level`) by `screening_quest` | 0.679 | 0.679 | no |
| Harm-reduction practice score → `ceremony_good` (KW) | 0.352 | 0.422 | no |

### 4.8 Multivariable ordinal model for `ceremony_good` (exploratory, hypothesis-generating)

§4.2–§4.7 are unadjusted pairwise tests; this model adjusts preparation for age and facilitator trust simultaneously. The full covariate set specified in the original proposal (age, gender, prep, trust, screening) is not estimable here: `gender_idt` has cells too thin for a 4-level categorical predictor (non-binary $n=4$, `pna` $n=1$), and `screening_quest` overlaps substantively with `trust_level`/`facil_background` already in the model (§4.4) — adding both risks collinearity without enough $N$ to resolve it. Per the analysis plan's prespecified fallback, we fit a **parsimonious 3-predictor** proportional-odds model instead: `age` (years), `prep_any` (any preparation vs. none), and `trust_level_num` (trust in the facilitator, 0–4) — the two exposures already flagged as relevant in §4.2/§4.4, adjusted for baseline age.

The raw 7-level `ceremony_good` has cells as thin as $n=1$–$3$ at the low end (severe ceiling — see §4.1), which risks quasi-complete separation in an ordinal logit at this $N$. The outcome is therefore **collapsed to 3 ordered levels** for this model only (`ceremony_good_3lvl`; order preserved, all univariate tables elsewhere in this report keep the full 0–6 scale).

Complete-case model sample: $n=62$ of 63 participants with a non-missing outcome (dropped for missing `age`, `trust_level`, or `prep_part`). Outcome distribution in the model sample: low/mixed (0–3) (9), mostly positive (4–5) (19), very positive (6) (34).

| predictor | OR | 95% CI | $p$ |
| --- | --- | --- | --- |
| age | 0.99 | 0.94–1.03 | 0.527 |
| prep_any (any vs. none) | 5.21 | 0.84–32.41 | 0.077 |
| trust_level | 2.20 | 1.06–4.53 | 0.033 |

Omnibus likelihood-ratio test vs. an intercept/cutpoint-only model: $\chi^2(3)=8.68$, $p=0.034$; McFadden pseudo-$R^2=0.07$.

> **Power caveat.** $n=62$ complete cases for 5 estimated parameters (3 slopes + 2 cutpoints) — roughly 12 cases per parameter, below conventional rules of thumb for stable ordinal-regression estimates. The proportional-odds (parallel-lines) assumption is **not formally tested** here (sample too small to support it reliably) and is simply assumed. Treat every estimate in this table as **exploratory / hypothesis-generating**, not confirmatory, and do not present standalone in the manuscript without this caveat.

### 4.9 Substance-stratified satisfaction and safety

Stratifies by the participant's most-recent-ceremony substance (`drugs_used_part`; full multi-ceremony substance frequencies are in §3.4). Individually reportable groups: **ayahuasca** ($n=23$) and **magic mushrooms** ($n=31$); every other substance — cacao, DMT, tobacco, LSD, "other" — is individually below $n<5$ and is pooled into one **other/rare substances** group ($n=11$), per the analysis plan's prespecified rule to combine rare substances. `pna` ($n=1$) and non-response are excluded from this grouping variable as missing exposure (same convention as `prep_3lvl`). Both tests below join one small secondary/exploratory family (§4.9.3), corrected separately from §4.7/§5.4 because the exposure (substance) cuts across both outcome domains.

#### 4.9.1 Satisfaction (`ceremony_good`) by substance

| substance group | n (answered outcome) | median | IQR |
| --- | --- | --- | --- |
| Ayahuasca | 22 | 5 | 4–6 |
| Magic mushrooms | 30 | 6 | 5–6 |
| Other/rare (combined) | 11 | 6 | 4–6 |

$H=4.98$, $p=0.083$, $\varepsilon^2=0.05$.

#### 4.9.2 Safety (`non_con_contact`) by substance

|  | Ayahuasca | Magic mushrooms | Other/rare (combined) | total |
| --- | --- | --- | --- | --- |
| 1. Yes | <5 | <5 | 0 | 5 |
| 2. No | 22 | 26 | 11 | 59 |
| 3. I’m not sure | 0 | <5 | 0 | <5 |
| **total** | 23 | 31 | 11 | 65 |
(pairwise-complete $n=65$)

Permutation $\chi^2=3.70$, $p=0.486$ (10,000 label permutations, seed 20260715), Cramér's $V=0.17$.

Affirmative (`sí`) cells are thin at this base (§5.1 already reports the pooled prevalence); read this cross-tab as **hypothesis-generating only**, same caveat as §5.3.

#### 4.9.3 Multiplicity correction (substance-stratified family)

| test | raw $p$ | BH $q$ | significant at $q<.05$ |
| --- | --- | --- | --- |
| ceremony_good by substance group (KW) | 0.083 | 0.166 | no |
| non_con_contact by substance group (perm. χ²) | 0.486 | 0.486 | no |

## 5. Safety / adverse-event domain (recommended; absent from proposal)

Two distinct reporters — do not merge:

- `non_con_contact`: **participant-reported** non-consensual physical contact (answered base ≈67).
- `exp_crisis`: **facilitator-reported** crisis signs *witnessed* while leading ceremonies (answered base $n=7$ of 8 facilitators) — almost entirely below the $n<5$ floor, so reported in aggregate only.

### 5.1 Non-consensual contact (participant-reported)

| response | n | % answered |
| --- | --- | --- |
| 2. No | 61 | 91% |
| 1. Yes | 5 | 7% |
| 3. I’m not sure | <5 | 1% |
| (structural skip) | 5 |  |

Prevalence $= 7.5\%$ (95% CI 3.2–16.3; $k=5$, $n=67$).

### 5.2 Facilitator-witnessed crisis signs (`exp_crisis`)

Facilitator base $n=7$ answered `exp_crisis`. Individual crisis sub-items (including `suicide_idea`, `panic_atk`) are each below $n<5$ and are **suppressed**; they are flagged here only to establish that serious crisis events were witnessed and are within scope. With $n\approx7$ facilitators, no stable rate is estimable — this motivates targeted recruitment of facilitators in future waves.

### 5.3 Association with facilitator training / screening / protocol (secondary, exploratory)

**Disclosure note.** Under the general reporting policy for this study, sensitive items such as `non_con_contact` and `exp_crisis` are otherwise reported aggregate-only, with no cross-tabulation that could re-identify a respondent. For this specific association question, the research team elected to publish cross-tabs here under the **same standard $n<5$ cell-masking convention used for every other thin-cell table in this report** (§4.4/§4.5), rather than withholding them entirely. Even masked, several cells below are close to case-level given how few affirmative/uncertain reports exist (`non_con_contact` 'sí'+'no estoy seguro(a)' totals $n=6$ of 67 answered; the `exp_crisis` facilitator base is $n=7$ of 8 facilitators). **Rationale for this judgment call** (author decision, 2026-08-13): withholding these cross-tabs entirely would remove the only evidence this study can offer on whether non-consensual contact clusters with any measured facilitator-practice proxy — a question directly relevant to what a harm-reduction intervention should target. The research team judged that reporting under the same n<5 masking convention already applied to every other thin-cell table in this report gives readers that evidence without disclosing any cell small enough to plausibly re-identify a respondent, and that this transparency outweighs the residual risk at this sample size. Treat every result in this subsection as **hypothesis-generating only** — not adequately powered to confirm or rule out an association.

#### 5.3.1 Participant-reported non-consensual contact vs. participant-side training/screening proxies

Same structural-gap rationale as §4.4: facilitator self-report items are unlinked to a specific participant's ceremony, so only the participant-answered proxies (`facil_background`, `screening_quest`) can be validly crossed with a participant's own reported safety outcome. `not_sure`/`pna` are kept as their own row/column (uniform policy), not merged into `si`/`no`.

**5.3.1a. `non_con_contact` × `facil_background`**

|  | 1. Yes | 3. A little | 2. No | 4. Prefer not to answer | total |
| --- | --- | --- | --- | --- | --- |
| 1. Yes | <5 | 0 | <5 | 0 | 5 |
| 2. No | 50 | 8 | <5 | <5 | 61 |
| 3. I’m not sure | 0 | 0 | <5 | 0 | <5 |
| **total** | 54 | 8 | <5 | <5 | 67 |
(pairwise-complete $n=67$)

Permutation $\chi^2=18.90$, $p=0.047$ (10,000 label permutations, seed 20260715), Cramér's $V=0.38$.

**5.3.1b. `non_con_contact` × `screening_quest`**

|  | 1. Yes | 2. No | 3. I’m not sure | 4. Prefer not to answer | total |
| --- | --- | --- | --- | --- | --- |
| 1. Yes | <5 | <5 | 0 | 0 | 5 |
| 2. No | 35 | 14 | 7 | <5 | 60 |
| 3. I’m not sure | 0 | 0 | 0 | <5 | <5 |
| **total** | 39 | 15 | 7 | 5 | 66 |
(pairwise-complete $n=66$)

Permutation $\chi^2=13.64$, $p=0.094$ (10,000 label permutations, seed 20260715), Cramér's $V=0.32$.

#### 5.3.2 Facilitator-witnessed crisis signs vs. facilitator-reported training/protocol (same respondents: facilitator branch $n=8$; `exp_crisis` answered $n=7$)

These items sit on the same side of the survey (facilitator self-report), so — unlike §5.3.1 — there is no participant-linkage gap here; the limiting factor is purely statistical power. Select-multiple predictors are collapsed to a binary **any substantive response** indicator; `emergency_plan` is used at its observed categories directly.

**`exp_crisis` (any) × `training_facilitator` (any substantive response)**

Insufficient non-missing / non-degenerate data for a test.

**`exp_crisis` (any) × `safe_ceremony` (any substantive response)**

Insufficient non-missing / non-degenerate data for a test.

**`exp_crisis` (any) × `protocol_bad_exp` (any substantive response)**

|  | yes | no | total |
| --- | --- | --- | --- |
| ≥1 crisis sign reported | 6 | 0 | 6 |
| no crisis sign reported | 0 | <5 | <5 |
| **total** | 6 | <5 | 7 |
($n=7$)

Fisher's exact test: odds ratio = $\infty$, $p=0.143$.

**`exp_crisis` (any) × `emergency_plan`**

|  | I have an informal or unwritten approach | Depends on the situation | total |
| --- | --- | --- | --- |
| ≥1 crisis sign reported | <5 | <5 | 6 |
| no crisis sign reported | 0 | <5 | <5 |
| **total** | <5 | <5 | 7 |
($n=7$)

Fisher's exact test: odds ratio = $\infty$, $p=0.429$.

> **Interpretation.** With a facilitator base of $n\approx8$, every 2×2 table above has at least one margin $\le2$; Fisher's exact test is mathematically valid at any $n$, but statistical power is essentially nil. These results are reported for completeness and to establish the analytic approach for a future, larger facilitator sample — they should not be read as evidence for or against an association.

#### 5.3.3 Harm-reduction practice index (§4.6) vs. `non_con_contact`

Same participant-side index built in §4.6 (`prep_any` + `facil_background` + `screening_quest`, 0–3). The facilitator-side composite (§4.5) is not tested against `exp_crisis` here — as noted there, it is close to constant at $n\approx7$, so an association test would be statistically vacuous. The participant-side score is binarized (all three practices present vs. one or two) because the middle score cell is thin (§4.6) and non_con_contact's affirmative cell is already small; a 4×3 table would leave almost every cell below $n<5$.

|  | all 3 practices | 1–2 practices | total |
| --- | --- | --- | --- |
| 1. Yes | <5 | <5 | 5 |
| 2. No | 31 | 18 | 49 |
| **total** | 35 | 19 | 54 |
(pairwise-complete $n=54$)

Permutation $\chi^2=0.56$, $p=0.641$ (10,000 label permutations, seed 20260715), Cramér's $V=0.10$.

### 5.4 Multiplicity correction — safety-domain secondary family (Benjamini–Hochberg FDR)

The tests in §5.3 (3 participant-side + up to 4 facilitator-side) form their own secondary/exploratory family, distinct from the bivariate family in §4.7 (different outcome domain, same correction principle).

| test | raw $p$ | BH $q$ | significant at $q<.05$ |
| --- | --- | --- | --- |
| non_con_contact × facil_background | 0.047 | 0.236 | no |
| non_con_contact × screening_quest | 0.094 | 0.236 | no |
| exp_crisis × protocol_bad_exp (any) | 0.143 | 0.238 | no |
| exp_crisis × emergency_plan | 0.429 | 0.536 | no |
| Harm-reduction score (binary) × non_con_contact | 0.641 | 0.641 | no |

## 6. Qualitative — open-text extraction and coding scaffold

**37** open-text fields (authoritative list: `survey[type=='text']`, excluding the `nickname`/`password` identifiers) yield **285** non-empty answers, mixed Spanish/English. This is a coding scaffold to support the research team's manual thematic analysis — it does not automate interpretation.

> **Correction to the original field list.** The proposal's prose names `add_share` as an open-text item. It is actually a `select_one si_no_pna` gate ("is there anything else you'd like to share?") for the real free-text field, `additional_info`. `add_share` is excluded here as categorical, not free text.

### 6.1 Answers per field

| field | n answered |
| --- | --- |
| exp_highlight | 58 |
| opinion_safe | 54 |
| prep_guidance_desc | 45 |
| screening_quest_type | 38 |
| self_prep_type | 30 |
| additional_info | 12 |
| fam_structure_other | 8 |
| tech_pos_exp | 7 |
| protocol_prep | 6 |
| barriers | 6 |
| imp_factors | 6 |
| drugs_used_part_other | <5 |
| motive_type_other | <5 |
| dosis_choice_other | <5 |
| protocol_other | <5 |
| safe_ceremony_other | <5 |
| exp_crisis_other | <5 |
| reason_part_cer_other | <5 |
| otro | <5 |
| org_type_part_other | <5 |
| last_ceremony_place_other | <5 |


16 field(s) with zero non-empty answers are omitted from the table above. Notably `no_comfort_safe` ("why did you feel uncomfortable/unsafe?") has **0** responses because its skip-logic condition (`comfort_safe='some_uncomf' AND comfort_safe='very_uncomf'`) requires one variable to equal two different values simultaneously — an instrument bug that makes the item structurally unreachable, not a low-response item.


### 6.2 Language mix

| language_guess | n | % of answers |
| --- | --- | --- |
| es | 220 | 77% |
| en | 54 | 19% |
| mixed/other | 11 | 4% |

`language_guess` is a rough heuristic (diacritics/marker-words for short strings, `langdetect` for longer ones) to characterize the corpus, not a validated per-item classification.


### 6.3 Seed keyword categories (codebook bootstrap)

| theme | answers with ≥1 keyword hit |
| --- | --- |
| legality | 19 |
| medical_presence | 19 |
| facilitator_vetting | 14 |
| education | 13 |
| consent | <5 |

Categories are prespecified by the research team (legality, education, facilitator vetting, medical presence, consent), matched by ES/EN keyword stems. `opinion_safe` in particular shows a dominant legalization/regulation + facilitator-training/education cluster on inspection — a natural first code family for the team's codebook.


### 6.4 Word-frequency view

| token | n answers |
| --- | --- |
| dieta | 31 |
| ceremonia | 19 |
| mental | 19 |
| salud | 17 |
| personas | 15 |
| más | 14 |
| medicina | 14 |
| experiencia | 13 |
| vida | 13 |
| espiritual | 12 |
| tener | 11 |
| educación | 11 |
| medicamentos | 10 |
| intención | 9 |
| estar | 9 |

Stopwords removed (ES+EN); tokens below the $n<5$ floor are not listed. This is a seed view for codebook development, not a substitute for reading the corpus.


### 6.5 Deliverables for the research team

- `outputs/tables/opentext_corpus.csv` — long format (`respondent_id`, `field`, `text`, `language_guess`), one row per non-empty answer, all fields.
- `outputs/tables/opentext_manual_coding.csv` — same rows plus empty `code_1`, `code_2`, `code_3` columns for manual coding by the team. This scaffold supports the team's thematic analysis; it does not replace it.

## 7. Data quality (flag, not drop)

### 7.1 Attention checks (per branch)

Facilitators judged on `atencion_1/2/3`; participants on `atencion_3_2/4/5/6` (checks are branch-specific). Rows are **flagged, never dropped**, per protocol.

- Respondents with $\geq 1$ answered-but-incorrect attention item: **2**.

### 7.2 Duplicate-responder screening

`ev_dup` was never populated (empty ×100) and `_submitted_by` is empty (no IP/device), so duplicates are screened manually via `nickname`+`password`, per protocol.

- Rows sharing an identical nickname+password combination: **2**.
- Rows with a repeated nickname: **9**; repeated password: **12**.

All flagged rows are exported to `outputs/tables/data_quality_flags.csv` for audit.

**Adjudication (completed).** The only signal that indicates a true duplicate *submission* — not merely a coincidentally shared nickname or password — is an exact nickname+password match (`dup_combo_flag`): 1 such pair exist in the 100 rows collected. Inspection shows the matching row(s) outside the analytic sample (already excluded as `abandoned_blank` or `screenout_no_no`) rather than a genuine double-count within it: **zero rows require exclusion from the analytic sample on duplicate grounds.** Nickname-only and password-only repeats (without a matching second field) were inspected individually and are consistent with coincidental reuse of common words (e.g. "Amor", "Si", "Hongos") rather than same-respondent duplication; full reasoning in `manuscript/sources/analysis_resolutions.md` §1a. No sensitivity re-run is needed, since no rows would be excluded either way.

## 8. Psychometric / reliability check

The instrument was purpose-built for this study (no validated PR entheogen-use instrument exists), so this is the first reliability evidence for it. The original proposal's language ("agreement scales, legal-knowledge, legal-worry, trust/comfort") implies multi-item Likert batteries, but inspecting `koboxls.xlsx` shows the instrument does not actually contain any: every Likert-shaped `list_name` maps to at most 2 items, and most 2-item pairs split across the facilitator/participant branches — unlinked respondents, the same limitation noted for the integration proxy (§4) and the harm-reduction index (§4.6). Two genuine same-respondent pairs are testable; the rest are reported below as **not testable**, with the reason.

### 8.1 Trust in facilitator + in-ceremony comfort/safety

`trust_level` (5-level) and `comfort_safe` (4-level) are both participant-side, single-item measures of subjective in-ceremony experience, already treated as related outcomes in §4.4. With only **2 items**, Cronbach's $\alpha$ is a direct, monotonic transform of their pairwise correlation ($\alpha = 2r/(1+r)$), and the item-total (item-rest) correlation for each item is identical to that pairwise correlation — not an independent number.

Spearman correlation: $\rho=0.39$, $p=0.002$ ($n=64$ pairwise-complete).

Cronbach's $\alpha=0.58$ (95% CI 0.31–0.74, complete-case $n=64$). This reflects a positive association between reported trust and perceived safety, consistent with both tracking one underlying "the ceremony felt held/safe" experience — but with only 2 items this is suggestive, not a validated scale.

### 8.2 Perceived legal knowledge — general vs. most-recent ceremony

`info_est_legal_part` (general legal understanding, `list_name` `legal_know_scale`) and `legal_know_part` (most-recent-ceremony legal understanding, `list_name` `legal_know_scale_2`) are both participant-side items on the same construct, but use two different `list_name` option sets — the recent-ceremony version is **missing the bottom "not aware at all" category** the general version has. They cannot be run through the standard per-scale ordinal decode used elsewhere, so they are harmonized by matching option content into one shared 0–4 ordinal code; `pna` is excluded (same policy as every other ordinal numeric encoding in this report).

Spearman correlation: $\rho=0.79$, $p=0.000$ ($n=55$ pairwise-complete).

Cronbach's $\alpha=0.86$ (95% CI 0.75–0.92, complete-case $n=55$). Reported for the same reason as §8.1: a real, if provisional, reliability signal rather than a placeholder result.

### 8.3 Candidates not testable, and why

| candidate set | why not testable |
| --- | --- |
| `impact_positive` / `impact_negative` (perceived life impact, `agreement_scale_2`) | `impact_positive` has **zero variance**: all 67 respondents who answered selected "somewhat_agree" (67/67). A constant item cannot correlate with anything and alpha is undefined. Reported as a data-quality finding, not a scale. |
| `est_legal_worry` / `est_legal_worry_part` (`legal_worry_scale`) | Asymmetric skip logic: `est_legal_worry` is gated on `info_est_legal_part='pna'` — the opposite of what a parallel item would need — so only $n=6$ ever reach it (near-constant response). `est_legal_worry_part` is asked broadly ($n=57$). Not comparable/parallel items; likely an instrument logic bug, same category as the `no_comfort_safe` unreachable-item finding in §6. |
| `entheogen_legal_know` (facilitator legal-knowledge item) | Facilitator-branch item ($n=7$), unlinked to any participant respondent — the same limitation noted for the integration proxy (§4) and perceived-safety analysis (§4.4). No matching facilitator-side item exists to pair it with. |

## 9. Legal knowledge/worry correlates

The analysis plan lists `entheogen_legal_know`, `legal_know_part`, and `est_legal_worry(_part)` as candidate predictors against "disclosure/screening participation and safety behavior." §8.3 already found two of those four legal-domain items unusable for any cross-tabulation: `est_legal_worry` (general) is gated on `info_est_legal_part='pna'`, reaching only a handful of respondents; `entheogen_legal_know` is a facilitator-branch item ($n\approx8$), unlinked to any participant respondent (§9.5 repeats the exact counts). This section instead uses the three well-populated **participant-side** legal items — `info_est_legal_part_num` (general legal knowledge, harmonized 0–4, §8.2), `legal_know_part_num` (most-recent-ceremony legal knowledge, harmonized 0–4, §8.2), and `est_legal_worry_part` (most-recent-ceremony legal worry, 5-level `legal_worry_scale`, decoded 0–4) — against three participant-side outcomes: **disclosure** (`med_couns_part`: talked to a doctor/therapist/health professional about ceremony participation beforehand), **screening participation** (`screening_quest`: facilitator asked screening questions beforehand), and **safety** (`non_con_contact`: unwanted physical contact — the same primary safety outcome as §5.1/§5.3, tested here against a different predictor set). Each outcome is `si_no_unsure`; `pna` is excluded from the grouping (retained elsewhere as a category per policy) because it carries no group identity to compare against, the same convention used for every other ordinal group comparison in this report.

### 9.1 Disclosure to a health professional (`med_couns_part`)

**General legal knowledge (`info_est_legal_part`) by `med_couns_part`**

| group | n (answered predictor) | median | IQR |
| --- | --- | --- | --- |
| 1. Yes | 7 | 2 | 2–4 |
| 2. No | 50 | 2 | 1–4 |
| 3. I’m not sure | <5 | 4 | 4–4 |

$H=2.71$, $p=0.258$, $\varepsilon^2=0.01$. Cells below $n<5$ (not_sure) make this descriptive/exploratory only.

**Most-recent-ceremony legal knowledge (`legal_know_part`) by `med_couns_part`**

| group | n (answered predictor) | median | IQR |
| --- | --- | --- | --- |
| 1. Yes | 8 | 4 | 3–4 |
| 2. No | 47 | 3 | 2–4 |
| 3. I’m not sure | <5 | 4 | 4–4 |

$H=3.61$, $p=0.164$, $\varepsilon^2=0.03$. Cells below $n<5$ (not_sure) make this descriptive/exploratory only.

**Most-recent-ceremony legal worry (`est_legal_worry_part`) by `med_couns_part`**

| group | n (answered predictor) | median | IQR |
| --- | --- | --- | --- |
| 1. Yes | 8 | 2 | 0–2 |
| 2. No | 47 | 0 | 0–0 |
| 3. I’m not sure | <5 | 0 | 0–0 |

$H=6.92$, $p=0.031$, $\varepsilon^2=0.09$. Cells below $n<5$ (not_sure) make this descriptive/exploratory only.

### 9.2 Screened by facilitator (`screening_quest`)

**General legal knowledge (`info_est_legal_part`) by `screening_quest`**

| group | n (answered predictor) | median | IQR |
| --- | --- | --- | --- |
| 1. Yes | 36 | 2 | 1–4 |
| 2. No | 12 | 3 | 2–4 |
| 3. I’m not sure | 7 | 2 | 1–4 |

$H=1.77$, $p=0.412$, $\varepsilon^2=0.00^{\dagger}$.

**Most-recent-ceremony legal knowledge (`legal_know_part`) by `screening_quest`**

| group | n (answered predictor) | median | IQR |
| --- | --- | --- | --- |
| 1. Yes | 35 | 3 | 2–4 |
| 2. No | 13 | 3 | 2–4 |
| 3. I’m not sure | 6 | 3 | 2–4 |

$H=0.83$, $p=0.659$, $\varepsilon^2=0.00^{\dagger}$.

**Most-recent-ceremony legal worry (`est_legal_worry_part`) by `screening_quest`**

| group | n (answered predictor) | median | IQR |
| --- | --- | --- | --- |
| 1. Yes | 35 | 0 | 0–0 |
| 2. No | 13 | 0 | 0–0 |
| 3. I’m not sure | 6 | 0 | 0–0 |

$H=0.18$, $p=0.914$, $\varepsilon^2=0.00^{\dagger}$.

### 9.3 Unwanted contact (`non_con_contact`)

**General legal knowledge (`info_est_legal_part`) by `non_con_contact`**

| group | n (answered predictor) | median | IQR |
| --- | --- | --- | --- |
| 1. Yes | 5 | 2 | 1–4 |
| 2. No | 54 | 2 | 1–4 |
| 3. I’m not sure | <5 | 1 | 1–1 |

$H=0.97$, $p=0.617$, $\varepsilon^2=0.00^{\dagger}$. Cells below $n<5$ (not_sure) make this descriptive/exploratory only.

**Most-recent-ceremony legal knowledge (`legal_know_part`) by `non_con_contact`**

| group | n (answered predictor) | median | IQR |
| --- | --- | --- | --- |
| 1. Yes | 5 | 4 | 3–4 |
| 2. No | 51 | 3 | 2–4 |
| 3. I’m not sure | <5 | 1 | 1–1 |

$H=3.61$, $p=0.165$, $\varepsilon^2=0.03$. Cells below $n<5$ (not_sure) make this descriptive/exploratory only.

**Most-recent-ceremony legal worry (`est_legal_worry_part`) by `non_con_contact`**

| group | n (answered predictor) | median | IQR |
| --- | --- | --- | --- |
| 1. Yes | 5 | 0 | 0–2 |
| 2. No | 51 | 0 | 0–0 |
| 3. I’m not sure | <5 | 0 | 0–0 |

$H=0.99$, $p=0.611$, $\varepsilon^2=0.00^{\dagger}$. Cells below $n<5$ (not_sure) make this descriptive/exploratory only.

### 9.4 Multiplicity correction (legal-knowledge/worry family)

All nine comparisons above (3 legal predictors × 3 outcomes) form one secondary/exploratory family, corrected jointly here — separate from §4.7/§4.9.3/§5.4 because the exposure (legal knowledge/worry) and these outcomes are not shared with those other families.

| test | raw $p$ | BH $q$ | significant at $q<.05$ |
| --- | --- | --- | --- |
| General legal knowledge (`info_est_legal_part`) by `med_couns_part` (KW) | 0.258 | 0.581 | no |
| Most-recent-ceremony legal knowledge (`legal_know_part`) by `med_couns_part` (KW) | 0.164 | 0.495 | no |
| Most-recent-ceremony legal worry (`est_legal_worry_part`) by `med_couns_part` (KW) | 0.031 | 0.283 | no |
| General legal knowledge (`info_est_legal_part`) by `screening_quest` (KW) | 0.412 | 0.741 | no |
| Most-recent-ceremony legal knowledge (`legal_know_part`) by `screening_quest` (KW) | 0.659 | 0.741 | no |
| Most-recent-ceremony legal worry (`est_legal_worry_part`) by `screening_quest` (KW) | 0.914 | 0.914 | no |
| General legal knowledge (`info_est_legal_part`) by `non_con_contact` (KW) | 0.617 | 0.741 | no |
| Most-recent-ceremony legal knowledge (`legal_know_part`) by `non_con_contact` (KW) | 0.165 | 0.495 | no |
| Most-recent-ceremony legal worry (`est_legal_worry_part`) by `non_con_contact` (KW) | 0.611 | 0.741 | no |

### 9.5 Not tested

| candidate | why not tested |
| --- | --- |
| `est_legal_worry` (general legal worry) | Gated on `info_est_legal_part='pna'` — only $n=6$ ever reach it (§8.3); too sparse for a group comparison. |
| `entheogen_legal_know` (facilitator legal knowledge) | Facilitator-branch item ($n=7$), unlinked to any participant respondent — same limitation as §4/§4.4/§8.3. |

## 10. Reproducibility

Regenerate: `PYTHONIOENCODING=utf-8 python analysis/report.py`. Pipeline: `config.py` → `data_prep.py` → `quality.py` → `qualitative.py` → `stats_helpers.py` → `report.py`. All decodes derive from `koboxls.xlsx`.
