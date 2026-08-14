"""Generate the descriptive-study analysis report (Markdown + LaTeX math).

Run:  PYTHONIOENCODING=utf-8 python report.py
Writes: outputs/report.md, outputs/figures/*.png, outputs/tables/*.csv
"""
import warnings
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from config import (OUT, FIG, TAB, SUPPRESS_N, DRUG_VARS, RANDOM_SEED,
                    SAFETY_FACILITATOR_ONEHOT_PREDICTORS, EXP_CRISIS_EXCLUDE,
                    CEREMONY_GOOD_3LVL_LABELS)
from data_prep import load, choices_map
from quality import build as build_quality
from qualitative import build as build_qualitative, get_text_fields, keyword_hits, top_tokens
from stats_helpers import (mask, fmt_eps2, freq_table, onehot_freq, desc_numeric,
                           desc_ordinal, mann_whitney, mann_whitney_perm, kruskal,
                           prevalence, md_table, bh_fdr, fisher_or, chi2_perm,
                           ordinal_logit, cronbach, spearman_pair)

warnings.simplefilter("ignore")
plt.rcParams.update({
    "figure.dpi": 130,
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "DejaVu Sans", "Liberation Sans"],
    "svg.fonttype": "none",
    "font.size": 9,
    "axes.spines.right": False,
    "axes.spines.top": False,
    "axes.linewidth": 0.8,
    "axes.grid": False,
    "axes.axisbelow": True,
    "legend.frameon": False,
})
PALETTE = {
    "blue_main": "#0F4D92",
    "blue_secondary": "#3775BA",
    "red_strong": "#B64342",
    "neutral_light": "#CFCECE",
    "neutral_dark": "#4D4D4D",
}


def fig_ceremony_good(pp):
    x = pp["ceremony_good_num"].dropna().astype(int)
    fig, ax = plt.subplots(figsize=(6, 3.2))
    counts = x.value_counts().reindex(range(7), fill_value=0)
    ax.bar(counts.index, counts.values, color=PALETTE["blue_main"],
           edgecolor=PALETTE["neutral_dark"], linewidth=0.6, width=0.7, zorder=3)
    ax.set_xlabel("ceremony_good  (0 = very unpleasant … 6 = very pleasant)")
    ax.set_ylabel("participants")
    ax.set_title(f"Satisfaction with ceremony (n={len(x)} answered)")
    ax.set_xticks(range(7))
    ax.yaxis.grid(True, alpha=.25, linewidth=.6, zorder=0)
    fig.tight_layout()
    p = FIG / "fig_ceremony_good.png"
    fig.savefig(p, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return p


def fig_prep_outcome(pp):
    g = {"No preparation": pp.loc[pp.prep_any == "none", "ceremony_good_num"].dropna(),
         "Any preparation": pp.loc[pp.prep_any == "prep", "ceremony_good_num"].dropna()}
    fig, ax = plt.subplots(figsize=(6, 3.4))
    data = [g["No preparation"].astype(float), g["Any preparation"].astype(float)]
    ax.boxplot(data, vert=True, tick_labels=[f"No prep\n(n={len(data[0])})",
               f"Any prep\n(n={len(data[1])})"], widths=.5, patch_artist=True,
               medianprops=dict(color=PALETTE["red_strong"], linewidth=1.6),
               boxprops=dict(facecolor=PALETTE["neutral_light"],
                             edgecolor=PALETTE["neutral_dark"], linewidth=0.8),
               whiskerprops=dict(color=PALETTE["neutral_dark"], linewidth=0.8),
               capprops=dict(color=PALETTE["neutral_dark"], linewidth=0.8),
               flierprops=dict(markeredgecolor=PALETTE["neutral_dark"], markersize=4))
    rng = np.random.default_rng(1)
    for i, d in enumerate(data, 1):
        ax.scatter(np.full(len(d), i) + rng.uniform(-.08, .08, len(d)), d,
                   color=PALETTE["blue_secondary"], alpha=.65, s=18, zorder=3,
                   edgecolor="white", linewidth=.3)
    ax.set_ylabel("ceremony_good (0–6)")
    ax.set_title("Preparation vs. satisfaction")
    ax.yaxis.grid(True, alpha=.25, linewidth=.6, zorder=0)
    fig.tight_layout()
    p = FIG / "fig_prep_outcome.png"
    fig.savefig(p, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return p


def fig_substances(df, ch):
    """Participant-reported substances across ceremonies attended
    (`drug_used_part`, select-multiple). Base = participants in the analytic
    sample with a non-missing response on this item (verified: summing over
    this base vs. the full 100-row df gives identical per-substance counts,
    since the item is skip-gated to participants — see
    manuscript/sources/analysis_resolutions.md §1b). Bars carry numeric count
    labels; cells n<SUPPRESS_N are masked as "<5" per the report's standard
    suppression convention (closes the "counts not reported" gap flagged in
    the early manuscript draft's Open Items)."""
    labs = choices_map(ch, "drugs_used", "label_en")
    subs = ["tabaco", "cacao", "lsd", "dmt", "ayahuasca", "hongos_magic",
            "ketamina", "mdma"]
    ana_part = df[df.in_analytic & df.analytic_participant]
    base_n = int(ana_part["drug_used_part"].notna().sum())
    counts = {}
    for s in subs:
        col = f"drug_used_part/{s}"
        if col in ana_part:
            counts[labs.get(s, s).split(". ")[-1]] = int(
                pd.to_numeric(ana_part[col], errors="coerce").fillna(0).sum())
    ser = pd.Series(counts).sort_values()
    fig, ax = plt.subplots(figsize=(6.5, 3.4))
    ax.barh(ser.index, ser.values, color=PALETTE["blue_main"],
            edgecolor=PALETTE["neutral_dark"], linewidth=0.6, height=0.65, zorder=3)
    for y, v in enumerate(ser.values):
        label = mask(v)
        ax.text(v + max(ser.values) * 0.015, y, label, va="center",
                fontsize=8, color=PALETTE["neutral_dark"])
    ax.set_xlabel(f"participants reporting use, ceremonies attended (base n={base_n})")
    ax.set_title("Substances used, participant-reported")
    ax.xaxis.grid(True, alpha=.25, linewidth=.6, zorder=0)
    ax.set_xlim(0, max(ser.values) * 1.12)
    fig.tight_layout()
    p = FIG / "fig_substances.png"
    fig.savefig(p, dpi=300, bbox_inches="tight")
    plt.close(fig)
    return p, base_n, ser


def section_univariate(df, ch, W):
    W("## 3. Univariate description (Objectives 1–2)\n")
    ana = df[df.in_analytic]
    role_fork = df[df.in_role_fork]
    n_screenout = int((df.role == "screenout_no_no").sum())
    W(f"Descriptive sample: **N = {len(ana)}** adults who identified a role "
      f"(participant, facilitator, or both). Of the "
      f"{int((df.role=='abandoned_blank').sum())} abandoned-blank submissions "
      f"excluded, none reached the role fork. Of the {len(role_fork)} "
      f"respondents who reached the role fork, {n_screenout} "
      f"({100*n_screenout/len(role_fork):.0f}%) answered \"no\" to both role "
      f"questions and are reported as a screening-yield rate rather than a "
      f"described subgroup; they are excluded from the analytic sample. "
      f"Role-specific analyses in §4–§5 restrict to participants/facilitators "
      f"as noted.\n")

    # role composition
    W("### 3.1 Role composition\n")
    rc = df["role"].value_counts()
    rows = [(r, mask(n), f"{100*n/len(df):.0f}%") for r, n in rc.items()]
    W(md_table(["role", "n", "% of 100"], rows) + "\n")
    W("Facilitator and participant roles **overlap** (7 dual-role); they are "
      "not a partition. Dual-role respondents appear in both role-specific "
      "analyses below, per protocol.\n")

    # age
    W("### 3.2 Sociodemographics (analytic sample)\n")
    age = pd.to_numeric(ana["age"], errors="coerce").dropna()
    W(f"- **Age** (n={len(age)}): mean $\\bar{{x}}={age.mean():.1f}$, "
      f"median $\\tilde{{x}}={age.median():.0f}$, SD $s={age.std():.1f}$, "
      f"range {int(age.min())}–{int(age.max())}, "
      f"IQR {age.quantile(.25):.0f}–{age.quantile(.75):.0f}.\n")

    for var, lst, title in [("gender_idt", "gender_idt", "Gender identity"),
                            ("academic", "niv_acad", "Education"),
                            ("econ", "sit_econ", "Economic situation")]:
        labs = choices_map(ch, lst, "label_en")
        rows_, base = freq_table(ana[var], labs)
        rows_ = [(c, mask(n), "" if p is None else f"{p:.0f}%") for c, n, p in rows_]
        W(f"\n**{title}** (answered base n={base}):\n")
        W(md_table(["category", "n", "% answered"], rows_) + "\n")

    # residency / diaspora
    W("### 3.3 Residency / diaspora check\n")
    labs = choices_map(ch, "pais_res", "label_en")
    rows_, base = freq_table(ana["country"], labs)
    rows_ = [(c, mask(n), "" if p is None else f"{p:.0f}%") for c, n, p in rows_]
    W(f"\n**Country of residence** (answered base n={base}):\n")
    W(md_table(["country of residence", "n", "% answered"], rows_) + "\n")
    W("Residency is treated as a **descriptive covariate**, not an inclusion "
      "filter, per protocol. Non-PR respondents temper any PR-population "
      "read of the sample.\n")

    # substances
    W("### 3.4 Substances (participant-reported)\n")
    p, subs_base, subs_ser = fig_substances(df, ch)
    W(f"![Substances]({p.relative_to(OUT).as_posix()})\n")
    W(f"\n**Substances used across ceremonies attended** (select-multiple; "
      f"answered base n={subs_base} participants; percentages need not sum "
      f"to 100%):\n")
    subs_rows = [(c, mask(n), f"{100*n/subs_base:.0f}%")
                 for c, n in subs_ser.sort_values(ascending=False).items()]
    W(md_table(["substance", "n", "% of base"], subs_rows) + "\n")
    W("The three drug variables are kept distinct: `drugs_used_facil` "
      "(facilitator-led), `drug_used_part` (participant, ceremonies attended, "
      "shown above), `drugs_used_part` (participant, most-recent ceremony).\n")

    # 3.5 facilitator practice context (facilitator branch only, tiny n)
    W("### 3.5 Facilitator practice context\n")
    W("**Facilitator-reported only** (`is_facilitator='si'`, base "
      f"n={int(df.analytic_facilitator.sum())}) — do not conflate with the "
      "participant-side context in §3.6. At this base, most category cells "
      f"fall at or below the $n<{SUPPRESS_N}$ suppression floor; tables are "
      "reported for completeness with cells masked, and should be read as "
      "**descriptive only**.\n")
    fac_mask = df["analytic_facilitator"]

    W("\n**Training / experience preparing to facilitate** "
      "(`training_facilitator`, select multiple; % of facilitator base):\n")
    labs = choices_map(ch, "training_facilitator", "label_en")
    rows_, base = onehot_freq(df, "training_facilitator", labs, fac_mask)
    rows_ = [(c, mask(n), f"{p:.0f}%") for c, n, p in rows_]
    W(md_table(["training/experience", "n", "% of base"], rows_) + f"\n(base n={base})\n")

    labs_av = choices_map(ch, "si_no_av_pna", "label_en")
    for var, title in [("inst_ceremonia",
                         "Gives participants preparation instructions (`inst_ceremonia`)")]:
        rows_, base = freq_table(df.loc[fac_mask, var], labs_av)
        rows_ = [(c, mask(n), "" if p is None else f"{p:.0f}%") for c, n, p in rows_]
        W(f"\n**{title}** (answered base n={base}):\n")
        W(md_table(["response", "n", "% answered"], rows_) + "\n")

    labs = choices_map(ch, "dosis_choice", "label_en")
    rows_, base = freq_table(df.loc[fac_mask, "dosis_choice"], labs)
    rows_ = [(c, mask(n), "" if p is None else f"{p:.0f}%") for c, n, p in rows_]
    W("\n**How dose is decided per participant** (`dosis_choice`, answered "
      f"base n={base}):\n")
    W(md_table(["dosing approach", "n", "% answered"], rows_) + "\n")

    labs = choices_map(ch, "ceremony_env", "label_en")
    rows_, base = freq_table(df.loc[fac_mask, "ceremony_env"], labs)
    rows_ = [(c, mask(n), "" if p is None else f"{p:.0f}%") for c, n, p in rows_]
    W("\n**Typical ceremony environment** (`ceremony_env`, answered "
      f"base n={base}):\n")
    W(md_table(["environment", "n", "% answered"], rows_) + "\n")

    # 3.6 participant ceremony frequency & most-recent-ceremony context
    W("### 3.6 Participant ceremony frequency and most-recent-ceremony context\n")
    W("**Participant-reported only** (`is_participant='si'`, base "
      f"n={int(df.analytic_participant.sum())}).\n")
    part_mask = df["analytic_participant"]
    pana = df.loc[part_mask]

    W("\n**Ceremony frequency**\n")
    W(desc_numeric(pana["amount_cer"], "Lifetime ceremonies attended (`amount_cer`)"))
    W(desc_numeric(pana["amount_cer_year"],
                    "Ceremonies attended in the past 12 months (`amount_cer_year`)"))
    n_neg = int((pd.to_numeric(pana["amount_cer_year"], errors="coerce") < 0).sum())
    if n_neg:
        W(f"> **Data-quality note.** {n_neg} respondent{'s' if n_neg != 1 else ''} "
          f"reported a negative `amount_cer_year` (impossible for a count); "
          "retained as entered per protocol (flagged rather than silently "
          "dropped or recoded) but included in the range/mean above, so treat "
          "the mean and minimum as unreliable for this variable — prefer the "
          "median.\n")

    W("\n**Most-recent-ceremony context**\n")
    for var, lst, title in [
        ("last_ceremony_time", "last_ceremony_time", "Time since last ceremony (`last_ceremony_time`)"),
        ("last_ceremony_place", "last_ceremony_place", "Place of last ceremony (`last_ceremony_place`)"),
        ("ceremony_format", "ceremony_format", "Retreat/series vs. single ceremony (`ceremony_format`)"),
        ("ceremony_duration", "ceremony_duration", "Total duration (`ceremony_duration`)"),
    ]:
        labs = choices_map(ch, lst, "label_en")
        rows_, base = freq_table(pana[var], labs)
        rows_ = [(c, mask(n), "" if p is None else f"{p:.0f}%") for c, n, p in rows_]
        W(f"\n**{title}** (answered base n={base}):\n")
        W(md_table(["category", "n", "% answered"], rows_) + "\n")


def section_bivariate(df, ch, W):
    W("## 4. Bivariate analyses (Objectives 3–4, revised)\n")
    W("The original study proposal specified a four-arm preparation×integration "
      "design; this is **not estimable** from the collected data, as the "
      "instrument contains no clean participant *integration-received* item and "
      "the preparation split is badly unbalanced. Per protocol, we analyze "
      "**preparation → outcome** directly. The outcome `ceremony_good` is "
      "treated as **ordinal** (heavy ceiling), so tests are nonparametric.\n")
    pp = df[df.analytic_participant]

    # descriptive medians by prep_any
    W("### 4.1 Distribution and group medians\n")
    p1 = fig_ceremony_good(pp)
    W(f"![ceremony_good distribution]({p1.relative_to(OUT).as_posix()})\n")
    W(f"Among participants, {int(pp['ceremony_good_num'].notna().sum())}/72 "
      f"answered `ceremony_good`; the remaining are item nonresponse "
      f"(structural skips affect non-participants, excluded here). Distribution "
      f"is strongly ceiling-weighted (median $\\tilde{{x}}=6$).\n")

    rows = []
    for lab, key in [("Any preparation", "prep"), ("No preparation", "none")]:
        d = desc_ordinal(pp.loc[pp.prep_any == key, "ceremony_good_num"])
        med = "n/a" if d["n"] == 0 else f'{d["median"]:.0f}'
        iqr = "n/a" if d["n"] == 0 else f'{d["q1"]:.0f}–{d["q3"]:.0f}'
        rows.append((lab, mask(d["n"]), med, iqr))
    W(md_table(["group", "n (answered outcome)", "median", "IQR"], rows) + "\n")
    p2 = fig_prep_outcome(pp)
    W(f"![Preparation vs outcome]({p2.relative_to(OUT).as_posix()})\n")

    # Mann-Whitney prep vs none
    W("### 4.2 Primary comparison — Mann–Whitney $U$\n")
    mw = mann_whitney(pp.loc[pp.prep_any == "prep", "ceremony_good_num"],
                      pp.loc[pp.prep_any == "none", "ceremony_good_num"])
    if mw:
        W(f"Any-preparation ($n_1={mw['n1']}$) vs. no-preparation "
          f"($n_2={mw['n2']}$): $U={mw['U']:.1f}$, $p={mw['p']:.3f}$ "
          f"(asymptotic, tie-corrected normal approximation), "
          f"rank-biserial $r_{{rb}}={mw['rbc']:.2f}$, "
          f"common-language effect size $\\mathrm{{CLES}}={mw['cles']:.2f}$.\n")
        mwp = mann_whitney_perm(pp.loc[pp.prep_any == "prep", "ceremony_good_num"],
                                pp.loc[pp.prep_any == "none", "ceremony_good_num"],
                                n_perm=10000, seed=RANDOM_SEED)
        if mwp:
            W(f"**Robustness check — exact/permutation test.** scipy's own "
              f"`method='exact'` for Mann–Whitney applies *no* tie correction "
              f"to the null distribution, which is invalid given how heavily "
              f"tied `ceremony_good` is at this ceiling; a 10,000-resample "
              f"label-permutation test (seed {RANDOM_SEED}, same convention "
              f"as the permutation $\\chi^2$ tests elsewhere in this report) "
              f"resamples the tied ranks directly and stays valid: "
              f"$p={mwp['p']:.3f}$. This is *more* significant than the "
              f"asymptotic result above, not less — the asymptotic "
              f"approximation is not the more conservative of the two at "
              f"this $n_2=5$.\n")
        W(f"> **Interpretation.** The no-preparation group is $n_2={mw['n2']}$ "
          f"(at the $n<{SUPPRESS_N}$ suppression floor). Even a sizable effect "
          f"here is statistically fragile; report as **suggestive, exploratory**, "
          f"not confirmatory. Direction: preparation is associated with higher "
          f"reported satisfaction.\n")

    # Kruskal 3-level
    W("### 4.3 Sensitivity — 3-level preparation (Kruskal–Wallis $H$)\n")
    groups = {lv: pp.loc[pp.prep_3lvl == lv, "ceremony_good_num"]
              for lv in ["si", "a_veces", "no"]}
    kw = kruskal(groups)
    secondary_tests = []  # (label, raw p) — the BH-FDR family for this section
    if kw:
        ns = ", ".join(f"{k}: {v}" for k, v in kw["ns"].items())
        W(f"Across `prep_part` levels ({ns}): $H={kw['H']:.2f}$, "
          f"$p={kw['p']:.3f}$, $\\varepsilon^2={fmt_eps2(kw['eps2'])}$. "
          f"The `no` and `a_veces` cells are below $n<{SUPPRESS_N}$ once the "
          f"outcome is non-missing — interpret as descriptive only.\n")
        secondary_tests.append(("Preparation (3-level) → `ceremony_good` (KW)", kw["p"]))
    W("`pna`/`not_sure` are retained as substantive categories in all "
      "frequency tables but are excluded from the ordinal numeric tests "
      "(they carry no rank position).\n")

    # ---- 4.4 Perceived safety by facilitator training/protocol -----------
    W("### 4.4 Perceived safety by facilitator training/protocol "
      "(participant-perceived proxy; secondary, exploratory)\n")
    W("The `training_facilitator`/`safe_ceremony`/`emergency_plan`/"
      "`protocol_bad_exp` items as specified in the original proposal are "
      "**facilitator self-report** ($n=8$), a different, unlinked set of "
      "respondents from the participants who report perceived safety — there "
      "is no ceremony/facilitator ID connecting a given participant to the "
      "facilitator who ran their ceremony, so those items cannot be crossed "
      "with participant-reported safety without falsely pairing unrelated "
      "respondents (the same unlinked-respondent limitation that ruled out "
      "the integration-proxy comparison in §4). This analysis instead uses "
      "the two **participant-side proxies** for facilitator training/"
      "protocol: "
      "`facil_background` (did the participant know about the facilitator's "
      "background/training beforehand) and `screening_quest` (did the "
      "facilitator ask screening questions before the ceremony). "
      "Facilitator self-report is presented separately, descriptively, in "
      "§4.5.\n")

    fb_labels = choices_map(ch, "facil_background", "label_en")
    sq_labels = choices_map(ch, "si_no_unsure", "label_en")
    comparisons = [
        ("comfort_safe_num", "In-ceremony comfort/safety (`comfort_safe`)",
         "facil_background", ["si", "some", "no"], fb_labels, "4.4.1"),
        ("comfort_safe_num", "In-ceremony comfort/safety (`comfort_safe`)",
         "screening_quest", ["si", "no", "not_sure"], sq_labels, "4.4.2"),
        ("trust_level_num", "Trust in facilitator (`trust_level`)",
         "facil_background", ["si", "some", "no"], fb_labels, "4.4.3"),
        ("trust_level_num", "Trust in facilitator (`trust_level`)",
         "screening_quest", ["si", "no", "not_sure"], sq_labels, "4.4.4"),
    ]
    for outcome_col, outcome_lab, exp_col, levels, elabels, tag in comparisons:
        W(f"**{tag}. {outcome_lab} by `{exp_col}`**\n")
        groups = {lv: pp.loc[pp[exp_col] == lv, outcome_col] for lv in levels}
        kw_st = kruskal(groups)
        rows = []
        for lv in levels:
            d = desc_ordinal(groups[lv])
            med = "n/a" if d["n"] == 0 else f'{d["median"]:.0f}'
            iqr = "n/a" if d["n"] == 0 else f'{d["q1"]:.0f}–{d["q3"]:.0f}'
            rows.append((str(elabels.get(lv, lv)), mask(d["n"]), med, iqr))
        W(md_table(["group", "n (answered outcome)", "median", "IQR"], rows) + "\n")
        if kw_st:
            thin = [lv for lv in levels if kw_st["ns"].get(lv, 0) < SUPPRESS_N]
            thin_note = (f" Cells below $n<{SUPPRESS_N}$ ({', '.join(thin)}) make "
                         f"this descriptive/exploratory only." if thin else "")
            W(f"$H={kw_st['H']:.2f}$, $p={kw_st['p']:.3f}$, "
              f"$\\varepsilon^2={fmt_eps2(kw_st['eps2'])}$.{thin_note}\n")
            secondary_tests.append((f"{outcome_lab} by `{exp_col}`", kw_st["p"]))
        else:
            W("Insufficient non-missing data for a test.\n")

    # ---- 4.5 Facilitator self-report — descriptive only ------------------
    W("### 4.5 Facilitator self-reported training/protocol "
      "(context, descriptive only, $n=8$)\n")
    W("Reported for context; **not** crossed with any safety outcome (see "
      "§4.4 for why). Every subgroup here is at or below the "
      f"$n<{SUPPRESS_N}$ suppression floor, so no group comparison is "
      "meaningful — counts are shown against the full facilitator base.\n")
    fac_mask = df.analytic_facilitator
    tf_labels = choices_map(ch, "training_facilitator", "label_en")
    sc_labels = choices_map(ch, "safe_ceremony", "label_en")
    pb_labels = choices_map(ch, "met_calm", "label_en")
    ep_labels = choices_map(ch, "emergency_plan", "label_en")

    W("**Training/experience (`training_facilitator`, select-multiple):**\n")
    rows_, base = onehot_freq(df, "training_facilitator", tf_labels, fac_mask)
    W(md_table(["form of training", "n", "% of facilitators"],
               [(c, mask(n), f"{p:.0f}%") for c, n, p in rows_ if n > 0]) + f"\n(base $n={base}$)\n")

    W("**Screening/safety approach (`safe_ceremony`, select-multiple):**\n")
    rows_, base = onehot_freq(df, "safe_ceremony", sc_labels, fac_mask)
    W(md_table(["approach", "n", "% of facilitators"],
               [(c, mask(n), f"{p:.0f}%") for c, n, p in rows_ if n > 0]) + f"\n(base $n={base}$)\n")

    W("**Response to a difficult experience (`protocol_bad_exp`, "
      "select-multiple):**\n")
    rows_, base = onehot_freq(df, "protocol_bad_exp", pb_labels, fac_mask)
    W(md_table(["response", "n", "% of facilitators"],
               [(c, mask(n), f"{p:.0f}%") for c, n, p in rows_ if n > 0]) + f"\n(base $n={base}$)\n")

    W("**Emergency plan (`emergency_plan`):**\n")
    rows_, base = freq_table(df.loc[fac_mask, "emergency_plan"], ep_labels)
    W(md_table(["response", "n", "% answered"],
               [(c, mask(n), "" if p is None else f"{p:.0f}%") for c, n, p in rows_]) + "\n")

    W("**Composite harm-reduction/readiness score** (training + "
      "safety-screening approach + distress-response protocol + emergency "
      "plan, each 0/1, `emergency_plan` informal/depende given 0.5 partial "
      "credit; range 0–4, complete cases only):\n")
    fac_items = _facilitator_hr_items(df, fac_mask)
    fac_cc = fac_items.dropna()
    fac_score = fac_cc.sum(axis=1)
    fac_rows, _ = freq_table(fac_score.round(1))
    W(md_table(["score", "n", "% answered"],
               [(c, mask(n), "" if p is None else f"{p:.0f}%") for c, n, p in fac_rows])
      + f"\n(complete-case $n={len(fac_cc)}$)\n")
    W(f"`training_facilitator` and `safe_ceremony` (any substantive response) "
      f"are answered \"yes\" by every facilitator who answered them (no "
      f"variance), and no facilitator selected the formal (`sí`) "
      f"`emergency_plan` option (all informal/conditional) — so this branch "
      f"is close to a constant. With that little variance and "
      f"$n={len(fac_cc)}$, neither a reliability statistic nor an "
      f"association test with `exp_crisis` is meaningful here; reported for "
      f"completeness only, for the same reason given in §5.3.2. The "
      f"participant-side version of this index (§4.6) carries the actual "
      f"inferential weight for this recommendation.\n")

    # ---- 4.6 Harm-reduction practice index --------------------------------
    W("### 4.6 Harm-reduction practice index — participant-side score vs. "
      "`ceremony_good`\n")
    W("The composite specified in the original proposal (\"prep + "
      "`emergency_plan` + `facil_background` + `safe_ceremony`\") mixes "
      "**facilitator self-report** items (`emergency_plan`, `safe_ceremony`, "
      "$n=8$) with **participant self-report** items (`prep_part`, "
      "`facil_background`) — the same unlinked-respondent limitation noted "
      "for the integration proxy and the perceived-safety comparisons "
      "(§4.4): these are two different, unlinked sets of respondents, so "
      "one mixed score cannot be validly built. As in §4.4, the composite "
      "is instead built "
      "in two branch-specific versions: a **participant-side index** here "
      "(`prep_any` + `facil_background` + `screening_quest`, the three "
      "participant-answerable protective-practice items — `screening_quest` "
      "substitutes for the facilitator-side `safe_ceremony`/`emergency_plan` "
      "items as the participant-observable analog), and a **facilitator-side "
      "descriptive composite** reported for completeness at the end of "
      "§4.5. `pna`/`not_sure` are item-missing here (not scored 0), "
      "matching the convention already used to build `prep_any`.\n")

    hr_items = _participant_hr_items(pp)
    hr_cc = hr_items.dropna()
    hr_score = hr_cc.sum(axis=1)
    W(f"**Score distribution** (0–3, complete-case $n={len(hr_cc)}$ of "
      f"{len(pp)} participants answering all three items):\n")
    hr_rows, _ = freq_table(hr_score)
    W(md_table(["score", "n", "% answered"],
               [(c, mask(n), "" if p is None else f"{p:.0f}%") for c, n, p in hr_rows]) + "\n")
    n_zero = int((hr_score == 0).sum())
    W(f"**Zero of {len(hr_cc)}** complete-case participants reported none of "
      f"the three practices (no preparation, no prior knowledge of the "
      f"facilitator's background, and no screening) — every respondent with "
      f"complete data on all three items reported at least one. This closes "
      f"the descriptive gap the earlier draft flagged: the index's floor is "
      f"empty at this base, not merely thin.\n" if n_zero == 0 else
      f"**{mask(n_zero)}** of {len(hr_cc)} complete-case participants "
      f"reported none of the three practices.\n")

    cr = cronbach(hr_items)
    if cr:
        W(f"**Internal consistency.** Cronbach's $\\alpha={cr['alpha']:.2f}$ "
          f"(95% CI {cr['lo']:.2f}–{cr['hi']:.2f}, $n={cr['n']}$, "
          f"{cr['k']} items). This is low — the three items likely capture "
          "**distinct** protective practices (preparation, facilitator "
          "vetting, being screened) rather than one shared latent "
          "construct, so the composite score below should be read as a "
          "simple count of practices present, not a validated scale.\n")
    else:
        W("Insufficient complete cases for a reliability estimate.\n")

    W("**Association with `ceremony_good`** (Kruskal–Wallis across score "
      "levels):\n")
    outcome_by_score = {int(s): pp.loc[hr_score.index[hr_score == s], "ceremony_good_num"]
                        for s in sorted(hr_score.unique())}
    kw_hr = kruskal(outcome_by_score)
    rows = []
    for s in sorted(outcome_by_score):
        d = desc_ordinal(outcome_by_score[s])
        med = "n/a" if d["n"] == 0 else f'{d["median"]:.0f}'
        iqr = "n/a" if d["n"] == 0 else f'{d["q1"]:.0f}–{d["q3"]:.0f}'
        rows.append((str(s), mask(d["n"]), med, iqr))
    W(md_table(["score", "n (answered outcome)", "median", "IQR"], rows) + "\n")
    if kw_hr:
        thin = [s for s, n in kw_hr["ns"].items() if n < SUPPRESS_N]
        thin_note = (f" Score {', '.join(map(str, thin))} is below "
                     f"$n<{SUPPRESS_N}$ once the outcome is non-missing — "
                     "interpret as descriptive only." if thin else "")
        W(f"$H={kw_hr['H']:.2f}$, $p={kw_hr['p']:.3f}$, "
          f"$\\varepsilon^2={fmt_eps2(kw_hr['eps2'])}$.{thin_note}\n")
        secondary_tests.append(("Harm-reduction practice score → `ceremony_good` (KW)", kw_hr["p"]))
    else:
        W("Insufficient non-missing data for a test.\n")

    # ---- 4.7 Multiplicity — BH-FDR across the secondary family -----------
    W("### 4.7 Multiplicity correction — secondary/exploratory family "
      "(Benjamini–Hochberg FDR)\n")
    W("The primary comparison (§4.2, preparation vs. `ceremony_good`, "
      "pre-declared) is reported uncorrected. Every other bivariate test run "
      "so far — the 3-level preparation sensitivity (§4.3), the four "
      "perceived-safety-by-training comparisons (§4.4), and the "
      "harm-reduction practice index (§4.6) — forms one secondary/"
      "exploratory family, corrected jointly here.\n")
    if secondary_tests:
        qs = bh_fdr([p for _, p in secondary_tests])
        rows = [(lab, f"{p:.3f}", f"{q:.3f}", "yes" if rej else "no")
                for (lab, p), (q, rej) in zip(secondary_tests, qs)]
        W(md_table(["test", "raw $p$", "BH $q$", "significant at $q<.05$"], rows) + "\n")
    else:
        W("No secondary tests were estimable.\n")

    # ---- 4.8 Multivariable ordinal model -----------------------------------
    W("### 4.8 Multivariable ordinal model for `ceremony_good` "
      "(exploratory, hypothesis-generating)\n")
    W("§4.2–§4.7 are unadjusted pairwise tests; this model adjusts "
      "preparation for age and facilitator trust simultaneously. The full "
      "covariate set specified in the original proposal (age, gender, prep, "
      "trust, screening) is not estimable here: `gender_idt` has cells too "
      "thin for a 4-level categorical predictor (non-binary $n=4$, `pna` "
      "$n=1$), and `screening_quest` overlaps substantively with "
      "`trust_level`/`facil_background` already in the model (§4.4) — "
      "adding both risks collinearity without enough $N$ to resolve it. Per "
      "the analysis plan's prespecified fallback, we fit a **parsimonious "
      "3-predictor** proportional-odds model instead: `age` (years), "
      "`prep_any` (any preparation vs. none), and `trust_level_num` (trust "
      "in the "
      "facilitator, 0–4) — the two exposures already flagged as relevant in "
      "§4.2/§4.4, adjusted for baseline age.\n")
    W("The raw 7-level `ceremony_good` has cells as thin as $n=1$–$3$ at the "
      "low end (severe ceiling — see §4.1), which risks quasi-complete "
      "separation in an ordinal logit at this $N$. The outcome is therefore "
      "**collapsed to 3 ordered levels** for this model only "
      "(`ceremony_good_3lvl`; order preserved, all univariate tables "
      "elsewhere in this report keep the full 0–6 scale).\n")

    pp["prep_bin"] = (pp["prep_any"] == "prep").astype(float)
    model_cols = ["ceremony_good_3lvl", "age", "prep_bin", "trust_level_num"]
    sub = pp.dropna(subset=model_cols).copy()
    y = sub["ceremony_good_3lvl"].astype(int)
    X = sub[["age", "prep_bin", "trust_level_num"]].astype(float)
    X.columns = ["age", "prep_any (any vs. none)", "trust_level"]

    ylab_rows = [(lab, mask(int((y == k).sum())))
                 for k, lab in CEREMONY_GOOD_3LVL_LABELS.items()]
    W(f"Complete-case model sample: $n={len(sub)}$ of "
      f"{int(pp['ceremony_good_num'].notna().sum())} participants with a "
      f"non-missing outcome (dropped for missing `age`, `trust_level`, or "
      f"`prep_part`). Outcome distribution in the model sample: " +
      ", ".join(f"{lab} ({n})" for lab, n in ylab_rows) + ".\n")

    fit = ordinal_logit(y, X)
    if fit is None or len(sub) < 20:
        W("> **Model not reported.** Fit failed to converge or the "
          "complete-case sample is too small for a stable estimate; treat "
          "the adjustment question as open pending more data.\n")
    else:
        rows = [(r["predictor"], f'{r["OR"]:.2f}', f'{r["lo"]:.2f}–{r["hi"]:.2f}',
                 f'{r["p"]:.3f}') for r in fit["rows"]]
        W(md_table(["predictor", "OR", "95% CI", "$p$"], rows) + "\n")
        W(f"Omnibus likelihood-ratio test vs. an intercept/cutpoint-only "
          f"model: $\\chi^2({fit['llr_df']})={fit['llr']:.2f}$, "
          f"$p={fit['llr_p']:.3f}$; "
          f"McFadden pseudo-$R^2={fit['prsquared']:.2f}$.\n")
        W(f"> **Power caveat.** $n={fit['n']}$ complete cases for "
          f"{fit['k_params']} estimated parameters "
          f"(3 slopes + 2 cutpoints) — roughly "
          f"{fit['n'] / fit['k_params']:.0f} cases per parameter, below "
          "conventional rules of thumb for stable ordinal-regression "
          "estimates. The proportional-odds (parallel-lines) assumption is "
          "**not formally tested** here (sample too small to support it "
          "reliably) and is simply assumed. Treat every estimate in this "
          "table as **exploratory / hypothesis-generating**, not "
          "confirmatory, and do not present standalone in the manuscript "
          "without this caveat.\n")

    # ---- 4.9 Substance-stratified satisfaction and safety -----------------
    W("### 4.9 Substance-stratified satisfaction and safety\n")
    W("Stratifies by the participant's most-recent-ceremony substance "
      "(`drugs_used_part`; full multi-ceremony substance frequencies are in "
      "§3.4). Individually reportable groups: **ayahuasca** ($n=23$) and "
      "**magic mushrooms** ($n=31$); every other substance — cacao, DMT, "
      "tobacco, LSD, \"other\" — is individually below "
      f"$n<{SUPPRESS_N}$ and is pooled into one **other/rare substances** "
      "group ($n=11$), per the analysis plan's prespecified rule to combine "
      "rare substances. `pna` ($n=1$) and non-response are excluded from this "
      "grouping variable as missing exposure (same convention as "
      "`prep_3lvl`). Both tests below join one small secondary/exploratory "
      "family (§4.9.3), corrected separately from §4.7/§5.4 because the "
      "exposure (substance) cuts across both outcome domains.\n")

    grp = _substance_group(pp)
    grp_order = ["ayahuasca", "hongos_magic", "other_rare"]
    grp_labels = {"ayahuasca": "Ayahuasca", "hongos_magic": "Magic mushrooms",
                  "other_rare": "Other/rare (combined)"}
    substance_secondary_tests = []

    W("#### 4.9.1 Satisfaction (`ceremony_good`) by substance\n")
    groups = {lv: pp.loc[grp == lv, "ceremony_good_num"] for lv in grp_order}
    kw_sub = kruskal(groups)
    rows = []
    for lv in grp_order:
        d = desc_ordinal(groups[lv])
        med = "n/a" if d["n"] == 0 else f'{d["median"]:.0f}'
        iqr = "n/a" if d["n"] == 0 else f'{d["q1"]:.0f}–{d["q3"]:.0f}'
        rows.append((grp_labels[lv], mask(d["n"]), med, iqr))
    W(md_table(["substance group", "n (answered outcome)", "median", "IQR"], rows) + "\n")
    if kw_sub:
        W(f"$H={kw_sub['H']:.2f}$, $p={kw_sub['p']:.3f}$, "
          f"$\\varepsilon^2={fmt_eps2(kw_sub['eps2'])}$.\n")
        substance_secondary_tests.append(("ceremony_good by substance group (KW)", kw_sub["p"]))
    else:
        W("Insufficient non-missing data for a test.\n")

    W("#### 4.9.2 Safety (`non_con_contact`) by substance\n")
    res_sub = chi2_perm(pp["non_con_contact"], grp, seed=RANDOM_SEED)
    ncc_labels_sub = choices_map(ch, "si_no_unsure", "label_en")
    if res_sub is None:
        W("Insufficient non-missing data for a test.\n")
    else:
        tbl = _reorder(res_sub["table"], ["si", "no", "not_sure"], grp_order)
        W(_crosstab_md(tbl, ncc_labels_sub, grp_labels) +
          f"\n(pairwise-complete $n={res_sub['n']}$)\n")
        W(f"Permutation $\\chi^2={res_sub['chi2']:.2f}$, $p={res_sub['p']:.3f}$ "
          f"(10,000 label permutations, seed {RANDOM_SEED}), "
          f"Cramér's $V={res_sub['cramers_v']:.2f}$.\n")
        substance_secondary_tests.append(("non_con_contact by substance group (perm. χ²)", res_sub["p"]))
        W("Affirmative (`sí`) cells are thin at this base (§5.1 already "
          "reports the pooled prevalence); read this cross-tab as "
          "**hypothesis-generating only**, same caveat as §5.3.\n")

    W("#### 4.9.3 Multiplicity correction (substance-stratified family)\n")
    if substance_secondary_tests:
        qs = bh_fdr([p for _, p in substance_secondary_tests])
        rows = [(lab, f"{p:.3f}", f"{q:.3f}", "yes" if rej else "no")
                for (lab, p), (q, rej) in zip(substance_secondary_tests, qs)]
        W(md_table(["test", "raw $p$", "BH $q$", "significant at $q<.05$"], rows) + "\n")
    else:
        W("No secondary tests were estimable.\n")


def _any_true(df, prefix, exclude, base_mask):
    """Binary 'any substantive option selected' indicator for a
    select-multiple field (one-hot `prefix/option` columns), restricted to
    respondents in base_mask who answered the field. Excluded
    option-suffixes are non-substantive placeholders (§config) and don't
    count toward the positive indicator, but the row still counts as
    answered. Returns a 'yes'/'no'/<NA> Series aligned to df.index."""
    cols = [c for c in df.columns if c.startswith(prefix + "/")
            and c.split("/", 1)[1] not in exclude]
    answered = base_mask & df[prefix].notna()
    any_sub = df[cols].apply(pd.to_numeric, errors="coerce").fillna(0).sum(axis=1) > 0
    out = pd.Series(pd.NA, index=df.index, dtype="object")
    out.loc[answered] = any_sub.loc[answered].map({True: "yes", False: "no"})
    return out


def _participant_hr_items(pp):
    """Participant-side harm-reduction/protective-practice components for the
    §3 item 5 composite index: `prep_any` (prepared beforehand),
    `facil_background` (knew the facilitator's background/training
    beforehand; `si`/`some` scored 1), `screening_quest` (facilitator asked
    screening questions; `si` scored 1). `pna`/`not_sure` are item-missing
    here (not scored 0) — same convention already used to build `prep_any`,
    not the "retain as category" policy used for descriptive frequency
    tables. Returns a 3-column 0/1 DataFrame aligned to pp.index (NaN where
    the source item is unanswered/pna/not_sure)."""
    return pd.DataFrame({
        "prep": pp["prep_any"].map({"prep": 1, "none": 0}),
        "facil_background": pp["facil_background"].map({"si": 1, "some": 1, "no": 0}),
        "screening_quest": pp["screening_quest"].map({"si": 1, "no": 0}),
    })


def _substance_group(pp):
    """Participant most-recent-ceremony substance (`drugs_used_part`),
    collapsed to 3 groups for the §3 item 6 stratified satisfaction/safety
    analysis (§4.9): the two substances with an individually reportable base
    (ayahuasca n=23, hongos_magic n=31) stand alone; every other substance
    (cacao, dmt, tabaco, lsd, "other" — each n<5 individually) is pooled
    into one 'other/rare substances' group (n=11, >=SUPPRESS_N combined),
    per the plan's explicit "combine rare substances" rule. `pna` (n=1) and
    non-response are excluded from this grouping variable as missing
    exposure — same convention already used for `prep_3lvl` (drops
    pna/skip) — while remaining visible in the full §3.4 frequency table.
    Returns a Series aligned to pp.index."""
    def f(v):
        if v in ("ayahuasca", "hongos_magic"):
            return v
        if pd.isna(v) or v == "pna":
            return pd.NA
        return "other_rare"
    return pp["drugs_used_part"].map(f)


def _facilitator_hr_items(df, fac_mask):
    """Facilitator-side counterpart (descriptive only, n~7-8): any
    substantive `training_facilitator`/`safe_ceremony`/`protocol_bad_exp`
    response (1/0), plus `emergency_plan` (`si`=1, informal/depende=0.5
    partial credit, `no`=0). Kept separate from the participant-side index
    (§4.6) — mixing facilitator and participant self-report into one score
    would repeat the structural gap already flagged in §2.5 item 2/§4.4."""
    training = _any_true(df, "training_facilitator",
                          SAFETY_FACILITATOR_ONEHOT_PREDICTORS["training_facilitator"],
                          fac_mask).map({"yes": 1, "no": 0})
    safe = _any_true(df, "safe_ceremony",
                      SAFETY_FACILITATOR_ONEHOT_PREDICTORS["safe_ceremony"],
                      fac_mask).map({"yes": 1, "no": 0})
    protocol = _any_true(df, "protocol_bad_exp",
                          SAFETY_FACILITATOR_ONEHOT_PREDICTORS["protocol_bad_exp"],
                          fac_mask).map({"yes": 1, "no": 0})
    emergency = df["emergency_plan"].map({"si": 1, "informal": 0.5, "depende": 0.5, "no": 0})
    return pd.DataFrame({"training": training, "safe_ceremony_approach": safe,
                          "protocol_bad_exp": protocol, "emergency_plan": emergency})


def _reorder(table, row_order=None, col_order=None):
    """Reindex a contingency table to a canonical (choices-sheet) category
    order for display; chi2_perm/fisher_or don't depend on row/column
    order, so this is purely presentational. Categories absent from the
    data are dropped, never invented."""
    if row_order:
        table = table.reindex([r for r in row_order if r in table.index])
    if col_order:
        table = table.reindex(columns=[c for c in col_order if c in table.columns])
    return table


def _crosstab_md(table, row_labels=None, col_labels=None):
    """Render a contingency table (rows=outcome, cols=predictor) as a
    markdown table with n<5 per-cell suppression (row/column totals shown,
    also masked; same convention as every other table in this report)."""
    cols = list(table.columns)
    header = ["", *[str((col_labels or {}).get(c, c)) for c in cols], "total"]
    rows = []
    for r in table.index:
        vals = [mask(int(table.loc[r, c])) for c in cols]
        rows.append([str((row_labels or {}).get(r, r)), *vals,
                     mask(int(table.loc[r].sum()))])
    rows.append(["**total**", *[mask(int(table[c].sum())) for c in cols],
                 mask(int(table.to_numpy().sum()))])
    return md_table(header, rows)


def section_safety(df, ch, W):
    W("## 5. Safety / adverse-event domain (recommended; absent from proposal)\n")
    W("Two distinct reporters — do not merge:\n\n"
      "- `non_con_contact`: **participant-reported** non-consensual physical "
      "contact (answered base ≈67).\n"
      "- `exp_crisis`: **facilitator-reported** crisis signs *witnessed* while "
      "leading ceremonies (answered base $n=7$ of 8 facilitators) — almost "
      f"entirely below the $n<{SUPPRESS_N}$ floor, so reported in aggregate "
      "only.\n")

    W("### 5.1 Non-consensual contact (participant-reported)\n")
    pp = df[df.analytic_participant]
    pr = prevalence(pp["non_con_contact"], positive="si")
    labs = choices_map(ch, "si_no_unsure", "label_en")
    rows_, base = freq_table(pp["non_con_contact"], labs)
    rows_ = [(c, mask(n), "" if p is None else f"{p:.0f}%") for c, n, p in rows_]
    W(md_table(["response", "n", "% answered"], rows_) + "\n")
    if pr["k"] < SUPPRESS_N:
        W(f"Affirmative reports are suppressed at the cell level "
          f"($k<{SUPPRESS_N}$); the answered base is $n={pr['base']}$. "
          f"Even suppressed, this is a **non-zero safety signal** that the "
          f"proposal did not plan to measure and that warrants qualitative "
          f"follow-up and protocol attention. Prevalence point/CI withheld to "
          f"avoid re-identification given the small cell.\n")
    else:
        W(f"Prevalence $= {pr['pct']:.1f}\\%$ "
          f"(95% CI {pr['lo']:.1f}–{pr['hi']:.1f}; $k={pr['k']}$, $n={pr['base']}$).\n")

    W("### 5.2 Facilitator-witnessed crisis signs (`exp_crisis`)\n")
    fac = df[df.analytic_facilitator]
    sub = [c for c in df.columns if c.startswith("exp_crisis/")]
    total = int(pd.to_numeric(fac["exp_crisis"].notna(), errors="coerce").sum())
    any_sig = 0
    for c in sub:
        any_sig += int(pd.to_numeric(fac[c], errors="coerce").fillna(0).sum())
    W(f"Facilitator base $n={total}$ answered `exp_crisis`. Individual crisis "
      f"sub-items (including `suicide_idea`, `panic_atk`) are each below "
      f"$n<{SUPPRESS_N}$ and are **suppressed**; they are flagged here only to "
      f"establish that serious crisis events were witnessed and are within "
      f"scope. With $n\\approx{total}$ facilitators, no stable rate is "
      f"estimable — this motivates targeted recruitment of facilitators in "
      f"future waves.\n")

    # ---- 5.3 Association with facilitator training / screening / protocol
    W("### 5.3 Association with facilitator training / screening / protocol "
      "(secondary, exploratory)\n")
    W("**Disclosure note.** Under the general reporting policy for this "
      "study, sensitive items such as `non_con_contact` and `exp_crisis` "
      "are otherwise reported aggregate-only, with no cross-tabulation that "
      "could re-identify a respondent. For this specific association "
      "question, the research team elected to publish cross-tabs here under "
      "the **same standard $n<5$ cell-masking convention used for every "
      "other thin-cell table in this report** (§4.4/§4.5), rather than "
      "withholding them entirely. Even masked, several cells below are "
      "close to case-level given how few affirmative/uncertain reports "
      "exist (`non_con_contact` 'sí'+'no estoy seguro(a)' totals $n=6$ of "
      f"67 answered; the `exp_crisis` facilitator base is $n={total}$ of 8 "
      "facilitators). **Rationale for this judgment call** (author decision, "
      "2026-08-13): withholding these cross-tabs entirely would remove the "
      "only evidence this study can offer on whether non-consensual contact "
      "clusters with any measured facilitator-practice proxy — a question "
      "directly relevant to what a harm-reduction intervention should "
      "target. The research team judged that reporting under the same "
      "n<5 masking convention already applied to every other thin-cell "
      "table in this report gives readers that evidence without disclosing "
      "any cell small enough to plausibly re-identify a respondent, and "
      "that this transparency outweighs the residual risk at this sample "
      "size. Treat every result in this subsection as "
      "**hypothesis-generating "
      "only** — not adequately powered to confirm or rule out an "
      "association.\n")

    W("#### 5.3.1 Participant-reported non-consensual contact vs. "
      "participant-side training/screening proxies\n")
    W("Same structural-gap rationale as §4.4: facilitator self-report items "
      "are unlinked to a specific participant's ceremony, so only the "
      "participant-answered proxies (`facil_background`, `screening_quest`) "
      "can be validly crossed with a participant's own reported safety "
      "outcome. `not_sure`/`pna` are kept as their own row/column (uniform "
      "policy), not merged into `si`/`no`.\n")

    ncc_labels = choices_map(ch, "si_no_unsure", "label_en")
    fb_labels = choices_map(ch, "facil_background", "label_en")
    sq_labels = choices_map(ch, "si_no_unsure", "label_en")
    safety_secondary_tests = []  # (label, raw p) for this section's BH-FDR family

    ncc_order = ["si", "no", "not_sure"]
    pred_orders = {
        "facil_background": ["si", "some", "no", "pna"],
        "screening_quest": ["si", "no", "not_sure", "pna"],
    }
    for pred_col, pred_labels, tag in [
        ("facil_background", fb_labels, "5.3.1a"),
        ("screening_quest", sq_labels, "5.3.1b"),
    ]:
        res = chi2_perm(pp["non_con_contact"], pp[pred_col], seed=RANDOM_SEED)
        W(f"**{tag}. `non_con_contact` × `{pred_col}`**\n")
        if res is None:
            W("Insufficient non-missing data for a test.\n")
            continue
        tbl = _reorder(res["table"], ncc_order, pred_orders[pred_col])
        W(_crosstab_md(tbl, ncc_labels, pred_labels) +
          f"\n(pairwise-complete $n={res['n']}$)\n")
        W(f"Permutation $\\chi^2={res['chi2']:.2f}$, $p={res['p']:.3f}$ "
          f"(10,000 label permutations, seed {RANDOM_SEED}), "
          f"Cramér's $V={res['cramers_v']:.2f}$.\n")
        safety_secondary_tests.append((f"non_con_contact × {pred_col}", res["p"]))

    W("#### 5.3.2 Facilitator-witnessed crisis signs vs. facilitator-reported "
      "training/protocol (same respondents: facilitator branch $n=8$; "
      "`exp_crisis` answered $n=7$)\n")
    W("These items sit on the same side of the survey (facilitator "
      "self-report), so — unlike §5.3.1 — there is no participant-linkage "
      "gap here; the limiting factor is purely statistical power. "
      "Select-multiple predictors are collapsed to a binary **any "
      "substantive response** indicator; `emergency_plan` is used at its "
      "observed categories directly.\n")

    fac_mask = df.analytic_facilitator
    any_crisis = _any_true(df, "exp_crisis", EXP_CRISIS_EXCLUDE, fac_mask)
    crisis_labels = {"yes": "≥1 crisis sign reported", "no": "no crisis sign reported"}
    binary_labels = {"yes": "yes", "no": "no"}
    binary_order = ["yes", "no"]

    for prefix, exclude in SAFETY_FACILITATOR_ONEHOT_PREDICTORS.items():
        pred = _any_true(df, prefix, exclude, fac_mask)
        res = fisher_or(any_crisis, pred)
        W(f"**`exp_crisis` (any) × `{prefix}` (any substantive response)**\n")
        if res is None:
            W("Insufficient non-missing / non-degenerate data for a test.\n")
            continue
        tbl = _reorder(res["table"], binary_order, binary_order)
        W(_crosstab_md(tbl, crisis_labels, binary_labels) +
          f"\n($n={res['n']}$)\n")
        or_str = "$\\infty$" if np.isinf(res["odds_ratio"]) else f"${res['odds_ratio']:.2f}$"
        W(f"Fisher's exact test: odds ratio = {or_str}, $p={res['p']:.3f}$.\n")
        safety_secondary_tests.append((f"exp_crisis × {prefix} (any)", res["p"]))

    ep_labels = choices_map(ch, "emergency_plan", "label_en")
    ep_order = ["si", "no", "informal", "depende", "pna"]
    res = fisher_or(any_crisis, df.loc[fac_mask, "emergency_plan"])
    W("**`exp_crisis` (any) × `emergency_plan`**\n")
    if res is None:
        W("Insufficient non-missing / non-degenerate data for a test "
          "(fewer than 2 `emergency_plan` categories observed against both "
          "`exp_crisis` levels in this branch).\n")
    else:
        tbl = _reorder(res["table"], binary_order, ep_order)
        W(_crosstab_md(tbl, crisis_labels, ep_labels) +
          f"\n($n={res['n']}$)\n")
        or_str = "$\\infty$" if np.isinf(res["odds_ratio"]) else f"${res['odds_ratio']:.2f}$"
        W(f"Fisher's exact test: odds ratio = {or_str}, $p={res['p']:.3f}$.\n")
        safety_secondary_tests.append(("exp_crisis × emergency_plan", res["p"]))

    W("> **Interpretation.** With a facilitator base of $n\\approx8$, every "
      "2×2 table above has at least one margin $\\le2$; Fisher's exact test "
      "is mathematically valid at any $n$, but statistical power is "
      "essentially nil. These results are reported for completeness and to "
      "establish the analytic approach for a future, larger facilitator "
      "sample — they should not be read as evidence for or against an "
      "association.\n")

    W("#### 5.3.3 Harm-reduction practice index (§4.6) vs. "
      "`non_con_contact`\n")
    W("Same participant-side index built in §4.6 (`prep_any` + "
      "`facil_background` + `screening_quest`, 0–3). The facilitator-side "
      "composite (§4.5) is not tested against `exp_crisis` here — as noted "
      "there, it is close to constant at $n\\approx7$, so an association "
      "test would be statistically vacuous. The participant-side score is "
      "binarized (all three practices present vs. one or two) because the "
      "middle score cell is thin (§4.6) and non_con_contact's affirmative "
      "cell is already small; a 4×3 table would leave almost every cell "
      "below $n<5$.\n")

    hr_items_s = _participant_hr_items(pp)
    hr_score_s = hr_items_s.dropna().sum(axis=1)
    hr_bin = hr_score_s.map(lambda s: "all 3 practices" if s == 3 else "1–2 practices")
    res = chi2_perm(pp["non_con_contact"], hr_bin, seed=RANDOM_SEED)
    if res is None:
        W("Insufficient non-missing data for a test.\n")
    else:
        tbl = _reorder(res["table"], ncc_order, ["all 3 practices", "1–2 practices"])
        W(_crosstab_md(tbl, ncc_labels) + f"\n(pairwise-complete $n={res['n']}$)\n")
        W(f"Permutation $\\chi^2={res['chi2']:.2f}$, $p={res['p']:.3f}$ "
          f"(10,000 label permutations, seed {RANDOM_SEED}), "
          f"Cramér's $V={res['cramers_v']:.2f}$.\n")
        safety_secondary_tests.append(("Harm-reduction score (binary) × non_con_contact", res["p"]))

    # ---- 5.4 Multiplicity — safety-domain secondary family ---------------
    W("### 5.4 Multiplicity correction — safety-domain secondary family "
      "(Benjamini–Hochberg FDR)\n")
    W("The tests in §5.3 (3 participant-side + up to 4 facilitator-side) "
      "form their own secondary/exploratory family, distinct from the "
      "bivariate family in §4.7 (different outcome domain, same correction "
      "principle).\n")
    if safety_secondary_tests:
        qs = bh_fdr([p for _, p in safety_secondary_tests])
        rows = [(lab, f"{p:.3f}", f"{q:.3f}", "yes" if rej else "no")
                for (lab, p), (q, rej) in zip(safety_secondary_tests, qs)]
        W(md_table(["test", "raw $p$", "BH $q$", "significant at $q<.05$"], rows) + "\n")
    else:
        W("No secondary tests were estimable.\n")


def section_qualitative(df, sv, W):
    W("## 6. Qualitative — open-text extraction and coding scaffold\n")
    fields = get_text_fields(sv)
    corpus = build_qualitative(df, sv)
    W(f"**{len(fields)}** open-text fields (authoritative list: "
      "`survey[type=='text']`, excluding the `nickname`/`password` "
      f"identifiers) yield **{len(corpus)}** non-empty answers, mixed "
      "Spanish/English. This is a coding scaffold to support the research "
      "team's manual thematic analysis — it does not automate "
      "interpretation.\n")
    W("> **Correction to the original field list.** The proposal's prose "
      "names `add_share` as an open-text item. It is actually a "
      "`select_one si_no_pna` gate (\"is there anything else you'd like to "
      "share?\") for the real free-text field, `additional_info`. `add_share` "
      "is excluded here as categorical, not free text.\n")

    W("### 6.1 Answers per field\n")
    vc = corpus["field"].value_counts()
    rows = [(f, mask(int(n))) for f, n in vc.items()]
    W(md_table(["field", "n answered"], rows) + "\n")
    n_zero = len(fields) - len(vc)
    if n_zero:
        W(f"\n{n_zero} field(s) with zero non-empty answers are omitted from "
          "the table above. Notably `no_comfort_safe` (\"why did you feel "
          "uncomfortable/unsafe?\") has **0** responses because its skip-logic "
          "condition (`comfort_safe='some_uncomf' AND comfort_safe='very_uncomf'`) "
          "requires one variable to equal two different values simultaneously — "
          "an instrument bug that makes the item structurally unreachable, not "
          "a low-response item.\n")

    W("\n### 6.2 Language mix\n")
    lv = corpus["language_guess"].value_counts()
    rows = [(l, mask(int(n)), f"{100*n/len(corpus):.0f}%") for l, n in lv.items()]
    W(md_table(["language_guess", "n", "% of answers"], rows) + "\n")
    W("`language_guess` is a rough heuristic (diacritics/marker-words for "
      "short strings, `langdetect` for longer ones) to characterize the "
      "corpus, not a validated per-item classification.\n")

    W("\n### 6.3 Seed keyword categories (codebook bootstrap)\n")
    kh = keyword_hits(corpus)
    rows = [(c, mask(n)) for c, n in kh]
    W(md_table(["theme", "answers with ≥1 keyword hit"], rows) + "\n")
    W("Categories are prespecified by the research team (legality, education, "
      "facilitator vetting, medical presence, consent), matched by ES/EN "
      "keyword stems. "
      "`opinion_safe` in particular shows a dominant "
      "legalization/regulation + facilitator-training/education cluster on "
      "inspection — a natural first code family for the team's codebook.\n")

    W("\n### 6.4 Word-frequency view\n")
    tt = [(w, n) for w, n in top_tokens(corpus) if n >= SUPPRESS_N]
    rows = [(w, n) for w, n in tt[:15]]
    W(md_table(["token", "n answers"], rows) + "\n")
    W("Stopwords removed (ES+EN); tokens below the "
      f"$n<{SUPPRESS_N}$ floor are not listed. This is a seed view for "
      "codebook development, not a substitute for reading the corpus.\n")

    W("\n### 6.5 Deliverables for the research team\n")
    W("- `outputs/tables/opentext_corpus.csv` — long format "
      "(`respondent_id`, `field`, `text`, `language_guess`), one row per "
      "non-empty answer, all fields.\n"
      "- `outputs/tables/opentext_manual_coding.csv` — same rows plus empty "
      "`code_1`, `code_2`, `code_3` columns for manual coding by the team. "
      "This scaffold supports the team's thematic analysis; it does not "
      "replace it.\n")


def section_quality(df, flags, W):
    W("## 7. Data quality (flag, not drop)\n")
    W("### 7.1 Attention checks (per branch)\n")
    W("Facilitators judged on `atencion_1/2/3`; participants on "
      "`atencion_3_2/4/5/6` (checks are branch-specific). Rows are **flagged, "
      "never dropped**, per protocol.\n")
    nf = int(flags["attn_fail_flag"].sum())
    W(f"- Respondents with $\\geq 1$ answered-but-incorrect attention item: "
      f"**{nf}**.\n")
    W("### 7.2 Duplicate-responder screening\n")
    W(f"`ev_dup` was never populated (empty ×100) and `_submitted_by` is empty "
      f"(no IP/device), so duplicates are screened manually via "
      f"`nickname`+`password`, per protocol.\n")
    W(f"- Rows sharing an identical nickname+password combination: "
      f"**{int(flags['dup_combo_flag'].sum())}**.\n"
      f"- Rows with a repeated nickname: **{int(flags['dup_nickname_flag'].sum())}**; "
      f"repeated password: **{int(flags['dup_password_flag'].sum())}**.\n")
    W("All flagged rows are exported to "
      "`outputs/tables/data_quality_flags.csv` for audit.\n")
    combo_rows = df.index[flags["dup_combo_flag"]]
    combo_in_analytic = [i for i in combo_rows if bool(df.loc[i, "in_analytic"])]
    n_combo_pairs = len(combo_rows) // 2 if len(combo_rows) else 0
    if len(combo_in_analytic) <= 1:
        W(f"**Adjudication (completed).** The only signal that indicates a "
          f"true duplicate *submission* — not merely a coincidentally shared "
          f"nickname or password — is an exact nickname+password match "
          f"(`dup_combo_flag`): {n_combo_pairs} such "
          f"{'pair' if n_combo_pairs == 1 else 'pairs'} exist in the 100 "
          f"rows collected. Inspection shows the matching row(s) outside the "
          f"analytic sample (already excluded as `abandoned_blank` or "
          f"`screenout_no_no`) rather than a genuine double-count within it: "
          f"**zero rows require exclusion from the analytic sample on "
          f"duplicate grounds.** Nickname-only and password-only repeats "
          f"(without a matching second field) were inspected individually "
          f"and are consistent with coincidental reuse of common words "
          f"(e.g. \"Amor\", \"Si\", \"Hongos\") rather than same-respondent "
          f"duplication; full reasoning in "
          f"`manuscript/sources/analysis_resolutions.md` §1a. No sensitivity "
          f"re-run is needed, since no rows would be excluded either way.\n")
    else:
        W(f"**Adjudication incomplete.** {len(combo_in_analytic)} rows in the "
          f"analytic sample share an exact nickname+password match — this "
          f"requires manual review before results are finalized; do not "
          f"treat this report as final until resolved.\n")


def section_psychometrics(df, ch, W):
    W("## 8. Psychometric / reliability check\n")
    W("The instrument was purpose-built for this study (no validated PR "
      "entheogen-use instrument exists), so this is the first reliability "
      "evidence for it. The original proposal's language (\"agreement "
      "scales, legal-knowledge, legal-worry, trust/comfort\") implies "
      "multi-item Likert batteries, but inspecting `koboxls.xlsx` shows the "
      "instrument does not actually contain any: every Likert-shaped "
      "`list_name` maps to at most 2 items, and most 2-item pairs split "
      "across the facilitator/participant branches — unlinked respondents, "
      "the same limitation noted for the integration proxy (§4) and the "
      "harm-reduction index (§4.6). Two genuine same-respondent pairs are "
      "testable; the rest are reported below as **not testable**, with the "
      "reason.\n")

    pp = df[df.analytic_participant]

    W("### 8.1 Trust in facilitator + in-ceremony comfort/safety\n")
    W("`trust_level` (5-level) and `comfort_safe` (4-level) are both "
      "participant-side, single-item measures of subjective in-ceremony "
      "experience, already treated as related outcomes in §4.4. With only "
      "**2 items**, Cronbach's $\\alpha$ is a direct, monotonic transform of "
      "their pairwise correlation ($\\alpha = 2r/(1+r)$), and the "
      "item-total (item-rest) correlation for each item is identical to "
      "that pairwise correlation — not an independent number.\n")
    items = pp[["trust_level_num", "comfort_safe_num"]]
    sp = spearman_pair(items["trust_level_num"], items["comfort_safe_num"])
    cr = cronbach(items.rename(columns={"trust_level_num": "trust_level",
                                         "comfort_safe_num": "comfort_safe"}))
    if sp:
        W(f"Spearman correlation: $\\rho={sp['rho']:.2f}$, $p={sp['p']:.3f}$ "
          f"($n={sp['n']}$ pairwise-complete).\n")
    if cr:
        W(f"Cronbach's $\\alpha={cr['alpha']:.2f}$ (95% CI {cr['lo']:.2f}–"
          f"{cr['hi']:.2f}, complete-case $n={cr['n']}$). This reflects a "
          "positive association between reported trust and perceived "
          "safety, consistent with both tracking one underlying \"the "
          "ceremony felt held/safe\" experience — but with only 2 items "
          "this is suggestive, not a validated scale.\n")
    else:
        W("Insufficient complete-case data for a reliability estimate.\n")

    W("### 8.2 Perceived legal knowledge — general vs. most-recent ceremony\n")
    W("`info_est_legal_part` (general legal understanding, `list_name` "
      "`legal_know_scale`) and `legal_know_part` (most-recent-ceremony "
      "legal understanding, `list_name` `legal_know_scale_2`) are both "
      "participant-side items on the same construct, but use two different "
      "`list_name` option sets — the recent-ceremony version is **missing "
      "the bottom \"not aware at all\" category** the general version has. "
      "They cannot be run through the standard per-scale ordinal decode "
      "used elsewhere, so they are harmonized by matching option content "
      "into one shared 0–4 ordinal code; `pna` is excluded (same policy as "
      "every other ordinal numeric encoding in this report).\n")
    items2 = pp[["info_est_legal_part_num", "legal_know_part_num"]]
    sp2 = spearman_pair(items2["info_est_legal_part_num"], items2["legal_know_part_num"])
    cr2 = cronbach(items2.rename(columns={"info_est_legal_part_num": "general",
                                           "legal_know_part_num": "recent"}))
    if sp2:
        W(f"Spearman correlation: $\\rho={sp2['rho']:.2f}$, $p={sp2['p']:.3f}$ "
          f"($n={sp2['n']}$ pairwise-complete).\n")
    if cr2:
        W(f"Cronbach's $\\alpha={cr2['alpha']:.2f}$ (95% CI {cr2['lo']:.2f}–"
          f"{cr2['hi']:.2f}, complete-case $n={cr2['n']}$). Reported for "
          "the same reason as §8.1: a real, if provisional, reliability "
          "signal rather than a placeholder result.\n")
    else:
        W("Insufficient complete-case data for a reliability estimate.\n")

    W("### 8.3 Candidates not testable, and why\n")
    n_pos = int(df["impact_positive"].notna().sum())
    pos_vc = df["impact_positive"].value_counts(dropna=True)
    n_worry_gen = int(df["est_legal_worry"].notna().sum())
    n_worry_rec = int(df["est_legal_worry_part"].notna().sum())
    n_fac_legal = int(df["entheogen_legal_know"].notna().sum())
    rows = [
        ("`impact_positive` / `impact_negative` (perceived life impact, "
         "`agreement_scale_2`)",
         f"`impact_positive` has **zero variance**: all {n_pos} respondents "
         f"who answered selected \"{pos_vc.index[0]}\" ({int(pos_vc.iloc[0])}"
         f"/{n_pos}). A constant item cannot correlate with anything and "
         "alpha is undefined. Reported as a data-quality finding, not a "
         "scale."),
        ("`est_legal_worry` / `est_legal_worry_part` (`legal_worry_scale`)",
         f"Asymmetric skip logic: `est_legal_worry` is gated on "
         f"`info_est_legal_part='pna'` — the opposite of what a parallel "
         f"item would need — so only $n={n_worry_gen}$ ever reach it "
         "(near-constant response). `est_legal_worry_part` is asked broadly "
         f"($n={n_worry_rec}$). Not comparable/parallel items; likely an "
         "instrument logic bug, same category as the `no_comfort_safe` "
         "unreachable-item finding in §6."),
        ("`entheogen_legal_know` (facilitator legal-knowledge item)",
         f"Facilitator-branch item ($n={n_fac_legal}$), unlinked to any "
         "participant respondent — the same limitation noted for the "
         "integration proxy (§4) and perceived-safety analysis (§4.4). No "
         "matching facilitator-side item exists to pair it with."),
    ]
    W(md_table(["candidate set", "why not testable"], rows) + "\n")


def section_legal(df, ch, W):
    W("## 9. Legal knowledge/worry correlates\n")
    W("The analysis plan lists `entheogen_legal_know`, `legal_know_part`, and "
      "`est_legal_worry(_part)` as candidate predictors against "
      "\"disclosure/screening participation and safety behavior.\" §8.3 "
      "already found two of those four legal-domain items unusable for any "
      "cross-tabulation: `est_legal_worry` (general) is gated on "
      "`info_est_legal_part='pna'`, reaching only a handful of respondents; "
      "`entheogen_legal_know` is a facilitator-branch item ($n\\approx8$), "
      "unlinked to any participant respondent (§9.5 repeats the exact "
      "counts). This section instead uses the three well-populated "
      "**participant-side** legal items — `info_est_legal_part_num` "
      "(general legal knowledge, harmonized 0–4, §8.2), `legal_know_part_num` "
      "(most-recent-ceremony legal knowledge, harmonized 0–4, §8.2), and "
      "`est_legal_worry_part` (most-recent-ceremony legal worry, 5-level "
      "`legal_worry_scale`, decoded 0–4) — against three participant-side "
      "outcomes: **disclosure** (`med_couns_part`: talked to a doctor/"
      "therapist/health professional about ceremony participation "
      "beforehand), **screening participation** (`screening_quest`: "
      "facilitator asked screening questions beforehand), and **safety** "
      "(`non_con_contact`: unwanted physical contact — the same primary "
      "safety outcome as §5.1/§5.3, tested here against a different "
      "predictor set). Each outcome is `si_no_unsure`; `pna` is excluded "
      "from the grouping (retained elsewhere as a category per policy) "
      "because it carries no group identity to compare against, the same "
      "convention used for every other ordinal group comparison in this "
      "report.\n")

    pp = df[df.analytic_participant]
    predictors = [
        ("info_est_legal_part_num", "General legal knowledge (`info_est_legal_part`)"),
        ("legal_know_part_num", "Most-recent-ceremony legal knowledge (`legal_know_part`)"),
        ("est_legal_worry_part_num", "Most-recent-ceremony legal worry (`est_legal_worry_part`)"),
    ]
    outcomes = [
        ("med_couns_part", "9.1 Disclosure to a health professional (`med_couns_part`)"),
        ("screening_quest", "9.2 Screened by facilitator (`screening_quest`)"),
        ("non_con_contact", "9.3 Unwanted contact (`non_con_contact`)"),
    ]
    levels = ["si", "no", "not_sure"]
    labels = choices_map(ch, "si_no_unsure", "label_en")

    secondary_tests = []
    for out_col, out_lab in outcomes:
        W(f"### {out_lab}\n")
        for pred_col, pred_lab in predictors:
            groups = {lv: pp.loc[pp[out_col] == lv, pred_col] for lv in levels}
            kw = kruskal(groups)
            rows = []
            for lv in levels:
                d = desc_ordinal(groups[lv])
                med = "n/a" if d["n"] == 0 else f'{d["median"]:.0f}'
                iqr = "n/a" if d["n"] == 0 else f'{d["q1"]:.0f}–{d["q3"]:.0f}'
                rows.append((str(labels.get(lv, lv)), mask(d["n"]), med, iqr))
            W(f"**{pred_lab} by `{out_col}`**\n")
            W(md_table(["group", "n (answered predictor)", "median", "IQR"], rows) + "\n")
            if kw:
                thin = [lv for lv in levels if kw["ns"].get(lv, 0) < SUPPRESS_N]
                thin_note = (f" Cells below $n<{SUPPRESS_N}$ ({', '.join(thin)}) make "
                             "this descriptive/exploratory only." if thin else "")
                W(f"$H={kw['H']:.2f}$, $p={kw['p']:.3f}$, "
                  f"$\\varepsilon^2={fmt_eps2(kw['eps2'])}$.{thin_note}\n")
                secondary_tests.append((f"{pred_lab} by `{out_col}` (KW)", kw["p"]))
            else:
                W("Insufficient non-missing data for a test.\n")

    W("### 9.4 Multiplicity correction (legal-knowledge/worry family)\n")
    W("All nine comparisons above (3 legal predictors × 3 outcomes) form one "
      "secondary/exploratory family, corrected jointly here — separate from "
      "§4.7/§4.9.3/§5.4 because the exposure (legal knowledge/worry) and "
      "these outcomes are not shared with those other families.\n")
    if secondary_tests:
        qs = bh_fdr([p for _, p in secondary_tests])
        rows = [(lab, f"{p:.3f}", f"{q:.3f}", "yes" if rej else "no")
                for (lab, p), (q, rej) in zip(secondary_tests, qs)]
        W(md_table(["test", "raw $p$", "BH $q$", "significant at $q<.05$"], rows) + "\n")
    else:
        W("No secondary tests were estimable.\n")

    W("### 9.5 Not tested\n")
    n_worry_gen = int(df["est_legal_worry"].notna().sum())
    n_fac_legal = int(df["entheogen_legal_know"].notna().sum())
    rows = [
        ("`est_legal_worry` (general legal worry)",
         f"Gated on `info_est_legal_part='pna'` — only $n={n_worry_gen}$ ever "
         "reach it (§8.3); too sparse for a group comparison."),
        ("`entheogen_legal_know` (facilitator legal knowledge)",
         f"Facilitator-branch item ($n={n_fac_legal}$), unlinked to any "
         "participant respondent — same limitation as §4/§4.4/§8.3."),
    ]
    W(md_table(["candidate", "why not tested"], rows) + "\n")


def main():
    df, ch, sv = load()
    flags = build_quality(df)
    buf = []
    W = lambda s: buf.append(s)

    W("# Ceremonial Entheogen Use in Puerto Rico — Descriptive Analysis Report\n")
    W("*Descriptive study (unweighted); no causal or population-prevalence "
      f"claims. Subgroup cells with $n<{SUPPRESS_N}$ are suppressed.*\n")
    W("## 1. Sample and framing\n")
    W(f"- Rows collected: **{len(df)}** (target N=100 met).\n"
      f"- Participants (`is_participant='si'`): **{int(df.analytic_participant.sum())}**; "
      f"facilitators (`is_facilitator='si'`): **{int(df.analytic_facilitator.sum())}**; "
      f"dual-role: **{int((df.role=='dual').sum())}**.\n"
      "- Outcome `ceremony_good` decoded `_0`…`_6` $\\to 0$–$6$, treated as "
      "**ordinal**.\n")
    W("## 2. Methods (summary)\n")
    W("Nonparametric throughout (Mann–Whitney $U$, Kruskal–Wallis $H$) with "
      "rank-biserial $r_{rb}$ / epsilon-squared $\\varepsilon^2$ effect sizes; "
      "`pna`/`not_sure` retained as categories; $n<5$ suppression; Wilson "
      "95% CIs for prevalences. Full rationale in `ANALYSIS_PLAN.md`. "
      "$\\varepsilon^2$ uses the standard bias-corrected formula, which can "
      "return small negative values when the effect is at or indistinguishable "
      "from zero; these are displayed truncated to 0.00 (marked $^\\dagger$) "
      "rather than reported as negative, applied uniformly to every "
      "$\\varepsilon^2$ in this report.\n")

    section_univariate(df, ch, W)
    section_bivariate(df, ch, W)
    section_safety(df, ch, W)
    section_qualitative(df, sv, W)
    section_quality(df, flags, W)
    section_psychometrics(df, ch, W)
    section_legal(df, ch, W)

    W("## 10. Reproducibility\n")
    W("Regenerate: `PYTHONIOENCODING=utf-8 python analysis/report.py`. "
      "Pipeline: `config.py` → `data_prep.py` → `quality.py` → "
      "`qualitative.py` → `stats_helpers.py` → `report.py`. All decodes derive from "
      "`koboxls.xlsx`.\n")

    (OUT / "report.md").write_text("\n".join(buf), encoding="utf-8")
    print("wrote", OUT / "report.md")
    print("figures in", FIG)


if __name__ == "__main__":
    main()
