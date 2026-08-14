"""Manuscript figures (Phase 4 of MANUSCRIPT_PLAN.md).

Writes, at 600 dpi, into this directory:
  fig1_flow.png            sample construction and role structure   (new, hand-coded)
  fig2_substances.png      substances across ceremonies attended    (revised)
  fig3_ceremony_good.png   satisfaction distribution / ceiling      (revised)
  fig4_prep_outcome.png    satisfaction by preparation status       (revised)
  graphical_abstract.png   repo-policy asset, NOT part of the JPD submission

Every count is read from the analysis pipeline (`analysis/data_prep.py`), never
typed in: the flow diagram, bar labels, and bases all recompute if the data or
the role rules change. In-figure titles are omitted — the LaTeX caption carries
the title, per journal convention.

Disclosure convention (Phase 5, peer-review item P1-7): exact counts are printed
throughout. The earlier "<5" masking was decorative — every masked cell was
recoverable from the percentage of a stated base printed beside it, Figure 2 drew
the masked bar to its true length against a numbered axis, and Figures 3 and 4
already printed sub-floor counts. The protection is aggregate-only reporting of a
survey that collected no direct identifiers, not cell masking, and the manuscript
now says so.

Usage:
    PYTHONIOENCODING=utf-8 C:/Users/jeanv/miniforge3/python.exe manuscript/figures/make_figures.py
"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent.parent
sys.path.insert(0, str(ROOT / "analysis"))

from data_prep import load, choices_map            # noqa: E402

DPI = 600

# ── Shared style (matches analysis/report.py and figures/example.py) ──────────
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "DejaVu Sans", "Liberation Sans"],
    "font.size": 9,
    "axes.spines.right": False,
    "axes.spines.top": False,
    "axes.linewidth": 0.8,
    "axes.grid": False,
    "axes.axisbelow": True,
    "xtick.major.width": 0.8,
    "ytick.major.width": 0.8,
    "legend.frameon": False,
    "svg.fonttype": "none",
})

PALETTE = {
    "blue_main": "#0F4D92",
    "blue_secondary": "#3775BA",
    "red_strong": "#B64342",
    "neutral_light": "#CFCECE",
    "neutral_dark": "#4D4D4D",
    "band": "#EDF1FA",      # light blue band, as in figures/example.py
    "navy_text": "#162040",
    "excl_fill": "#F2F2F2",
    "excl_edge": "#9A9A9A",
}


def _save(fig, name):
    p = HERE / name
    fig.savefig(p, dpi=DPI, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"wrote {p.relative_to(ROOT)}")
    return p


# ── Figure 1: sample construction and role structure ─────────────────────────

def _box(ax, cx, cy, w, h, text, *, fill="white", edge=PALETTE["blue_main"],
         lw=1.0, fontsize=8.6, weight="normal", color="black", style="normal"):
    ax.add_patch(FancyBboxPatch(
        (cx - w / 2, cy - h / 2), w, h,
        boxstyle="round,pad=0,rounding_size=1.2",
        linewidth=lw, edgecolor=edge, facecolor=fill, zorder=2))
    ax.text(cx, cy, text, ha="center", va="center", fontsize=fontsize,
            fontweight=weight, color=color, fontstyle=style, zorder=3,
            linespacing=1.45)


def _arrow(ax, xy_from, xy_to, color=PALETTE["neutral_dark"], lw=0.9, ls="-"):
    ax.add_patch(FancyArrowPatch(
        xy_from, xy_to, arrowstyle="-|>", mutation_scale=9,
        linewidth=lw, linestyle=ls, color=color,
        shrinkA=0, shrinkB=0, zorder=1))


def fig_flow(df):
    """Sample construction: submissions -> role fork -> analytic sample -> roles
    -> the two unlinked analysis branches. All counts recomputed from `role`."""
    rc = df["role"].value_counts()
    n_total = len(df)
    n_abandoned = int(rc.get("abandoned_blank", 0))
    n_fork = int(df["in_role_fork"].sum())
    n_screenout = int(rc.get("screenout_no_no", 0))
    n_ana = int(df["in_analytic"].sum())
    n_part_only = int(rc.get("participant_only", 0))
    n_dual = int(rc.get("dual", 0))
    n_fac_only = int(rc.get("facilitator_only", 0))
    ana = df[df.in_analytic]
    n_part_branch = int(ana["analytic_participant"].sum())
    n_fac_branch = int(ana["analytic_facilitator"].sum())
    # Continuation gate (P1-4): the XLSForm shows the participant block to a
    # dual-role respondent only if they also answered pause_facil = 'si'. Those
    # who did not were never shown a single participant item, so the routed
    # participant base is smaller than the self-identified one.
    dual_rows = ana[ana.role == "dual"]
    n_dual_stop = int(dual_rows["pause_facil"].eq("no").sum())
    n_part_routed = n_part_branch - n_dual_stop

    fig, ax = plt.subplots(figsize=(7.2, 8.0))
    ax.set_xlim(0, 100)
    ax.set_ylim(-10, 100)
    ax.axis("off")

    cx, bw, bh = 34, 42, 8.5          # main chain
    ex_cx, ex_w, ex_h = 79, 40, 9.5   # exclusion boxes at right
    y_a, y_b, y_c = 92, 76, 60

    _box(ax, cx, y_a, bw, bh, f"Survey submissions received\nN = {n_total}")
    _box(ax, cx, y_b, bw, bh, f"Reached the role fork\nn = {n_fork}")
    _box(ax, cx, y_c, bw, bh + 0.5,
         f"Analytic sample\nN = {n_ana}",
         fill=PALETTE["band"], lw=1.6, weight="bold",
         color=PALETTE["navy_text"], fontsize=9.6)

    # exclusions
    for y_mid, txt in ((84, f"Excluded: abandoned before the role fork\n"
                            f"(both role items left blank)   n = {n_abandoned}"),
                       (68, f"Excluded: screened out — answered \u201cno\u201d to\n"
                            f"both role items   n = {n_screenout} "
                            f"({100 * n_screenout / n_fork:.0f}% of {n_fork})")):
        _box(ax, ex_cx, y_mid, ex_w, ex_h, txt, fill=PALETTE["excl_fill"],
             edge=PALETTE["excl_edge"], fontsize=7.9,
             color=PALETTE["neutral_dark"], style="italic")
        _arrow(ax, (cx, y_mid), (ex_cx - ex_w / 2, y_mid))

    _arrow(ax, (cx, y_a - bh / 2), (cx, y_b + bh / 2))
    _arrow(ax, (cx, y_b - bh / 2), (cx, y_c + bh / 2))

    # role fork
    y_role, rw, rh = 41, 27, 9.0
    roles = [(16, f"Participant only\nn = {n_part_only}"),
             (46, f"Both roles\nn = {n_dual}"),
             (76, f"Facilitator only\nn = {n_fac_only}")]
    ax.text(2, 52, "Self-reported role", ha="left", va="center", fontsize=8.2,
            fontstyle="italic", color=PALETTE["neutral_dark"])
    for rx, txt in roles:
        _box(ax, rx, y_role, rw, rh, txt, edge=PALETTE["blue_secondary"])
        _arrow(ax, (cx, y_c - bh / 2 - 0.5), (rx, y_role + rh / 2))

    # analysis branches
    y_br, brh = 20, 9.5
    part_cx, part_w = 29, 44
    fac_cx, fac_w = 78, 30
    _box(ax, part_cx, y_br, part_w, brh + 1.5,
         f"Participant-side analyses\nn = {n_part_branch} self-identified; "
         f"{n_part_routed} routed to the items",
         fill=PALETTE["band"], weight="bold", color=PALETTE["navy_text"],
         fontsize=8.2)
    _box(ax, fac_cx, y_br, fac_w, brh + 1.5,
         f"Facilitator-side analyses\nn = {n_fac_branch}",
         fill=PALETTE["band"], weight="bold", color=PALETTE["navy_text"])

    _arrow(ax, (16, y_role - rh / 2), (part_cx - 8, y_br + brh / 2))
    _arrow(ax, (76, y_role - rh / 2), (fac_cx + 6, y_br + brh / 2))
    # dual-role respondents enter both branches (arrows leave the box corners so
    # the label between them stays clear)
    for x0, target in ((34.5, (part_cx + 10, y_br + brh / 2)),
                       (57.5, (fac_cx - 8, y_br + brh / 2))):
        _arrow(ax, (x0, y_role - rh / 2), target, color=PALETTE["red_strong"],
               lw=1.1, ls=(0, (4, 2)))
    ax.text(49, 31.4, f"dual-role (n = {n_dual})\nenter both branches",
            ha="center", va="center", fontsize=7.6, fontstyle="italic",
            color=PALETTE["red_strong"], linespacing=1.4)
    # continuation gate: dual-role respondents who answered 'no' were never shown
    # a participant item (structural skip, not item nonresponse)
    ax.text(part_cx, y_br - brh / 2 - 3.2,
            f"{n_dual_stop} of the {n_dual} dual-role respondents answered “no” at the "
            f"participant\ncontinuation gate and were shown no participant item "
            f"(structural skip).",
            ha="center", va="center", fontsize=7.4, fontstyle="italic",
            color=PALETTE["neutral_dark"], linespacing=1.5)

    # the unlinked-branch constraint
    y_link = y_br - brh / 2 - 9.0
    ax.plot([part_cx - part_w / 2, fac_cx + fac_w / 2], [y_link, y_link],
            linestyle=(0, (3, 3)), color=PALETTE["red_strong"], lw=1.0)
    for x_end in (part_cx - part_w / 2, fac_cx + fac_w / 2):
        ax.plot([x_end, x_end], [y_link, y_link + 1.6],
                color=PALETTE["red_strong"], lw=1.0)
    ax.text(53.5, y_link, "\u00d7", ha="center", va="center", fontsize=13,
            color=PALETTE["red_strong"], zorder=4,
            bbox=dict(boxstyle="circle,pad=0.18", facecolor="white",
                      edgecolor=PALETTE["red_strong"], linewidth=1.0))
    ax.text(50, y_link - 6.4,
            "Branches are unlinked \u2014 at the ceremony level, not the respondent level. No identifier\n"
            "connects a participant to the facilitator who ran their ceremony, and the ceremonies a\n"
            "dual-role respondent led are different events from the ones they attended, so no\n"
            "participant\u2013facilitator comparison is possible.",
            ha="center", va="center", fontsize=7.9, color=PALETTE["neutral_dark"],
            linespacing=1.55)

    fig.tight_layout()
    return _save(fig, "fig1_flow.png")


# ── Figure 2: substances across ceremonies attended ──────────────────────────

def fig_substances(df, ch):
    """`drug_used_part` (participant, select-multiple, ceremonies attended).
    Not the facilitator-led variable and not the most-recent-ceremony variable."""
    labs = choices_map(ch, "drugs_used", "label_en")
    # "other" is the fourth-most-endorsed option and was omitted from the v2
    # figure (peer-review item P1-9); it is restored here and flagged as
    # uninterpretable because its free-text follow-up was rarely completed.
    subs = ["tabaco", "cacao", "lsd", "dmt", "ayahuasca", "hongos_magic",
            "ketamina", "mdma", "other"]
    ana_part = df[df.in_analytic & df.analytic_participant]
    base_n = int(ana_part["drug_used_part"].notna().sum())
    n_other_text = int(ana_part["drugs_used_part_other"].notna().sum())

    counts = {}
    for s in subs:
        col = f"drug_used_part/{s}"
        if col in ana_part:
            name = "Other (unspecified)" if s == "other" else labs.get(s, s).split(". ")[-1]
            counts[name] = int(
                pd.to_numeric(ana_part[col], errors="coerce").fillna(0).sum())
    ser = pd.Series(counts).sort_values()

    fig, ax = plt.subplots(figsize=(6.6, 3.9))
    colors = [PALETTE["neutral_dark"] if i == "Other (unspecified)"
              else PALETTE["blue_main"] for i in ser.index]
    ax.barh(ser.index, ser.values, color=colors, edgecolor="none",
            height=0.66, zorder=3)
    xmax = int(ser.max())
    for y, v in enumerate(ser.values):
        ax.text(v + xmax * 0.017, y, f"{v}  ({100 * v / base_n:.0f}%)",
                va="center", fontsize=8, color=PALETTE["neutral_dark"])
    ax.set_xlabel(f"Participants reporting use (base n = {base_n})")
    ax.set_xlim(0, xmax * 1.26)
    ax.xaxis.grid(True, alpha=.25, linewidth=.6, zorder=0)
    ax.tick_params(axis="y", length=0)
    ax.spines["left"].set_visible(False)
    ax.text(0.0, -0.28,
            "Select-multiple item: percentages are of the base and do not sum to 100%.\n"
            f"“Other” is shown in grey because its free-text follow-up was completed by only\n"
            f"{n_other_text} respondents, so the category cannot be interpreted.",
            transform=ax.transAxes, ha="left", va="top", fontsize=7.2,
            fontstyle="italic", color=PALETTE["neutral_dark"], linespacing=1.5)
    fig.tight_layout()
    return _save(fig, "fig2_substances.png")


# ── Figure 3: satisfaction distribution (ceiling) ────────────────────────────

def fig_ceremony_good(pp):
    x = pp["ceremony_good_num"].dropna().astype(int)
    counts = x.value_counts().reindex(range(7), fill_value=0)
    n, med = len(x), int(x.median())
    n_top = int(counts.loc[[5, 6]].sum())
    # The 9-person remainder is three separate categories, not one (P3-1):
    n_self = len(pp)
    n_pna = int(pp["ceremony_good"].eq("pna").sum())
    n_struct = int(pp["pause_facil"].eq("no").sum())
    n_item = n_self - n - n_pna - n_struct

    fig, ax = plt.subplots(figsize=(6.2, 3.8))
    colors = [PALETTE["blue_secondary"]] * 5 + [PALETTE["blue_main"]] * 2
    ax.bar(counts.index, counts.values, color=colors, edgecolor="none",
           width=0.72, zorder=3)
    for i, v in enumerate(counts.values):
        ax.text(i, v + max(counts.values) * 0.02, str(v), ha="center",
                va="bottom", fontsize=8, color=PALETTE["neutral_dark"])

    ax.set_xlabel("Reported satisfaction with the most recent ceremony\n"
                  "(0 = very unpleasant … 6 = very pleasant)")
    ax.set_ylabel(f"Participants (base n = {n})")
    ax.set_xticks(range(7))
    ax.set_ylim(0, max(counts.values) * 1.30)
    ax.yaxis.grid(True, alpha=.25, linewidth=.6, zorder=0)

    # ceiling bracket over the top two categories
    y_br = max(counts.values) * 1.13
    ax.plot([4.68, 4.68, 6.32, 6.32],
            [y_br - max(counts.values) * 0.035, y_br, y_br,
             y_br - max(counts.values) * 0.035],
            lw=0.9, color=PALETTE["neutral_dark"], zorder=4)
    ax.text(5.5, y_br + max(counts.values) * 0.02,
            f"{n_top} of {n} ({100 * n_top / n:.0f}%) rated 5–6",
            ha="center", va="bottom", fontsize=8, color=PALETTE["neutral_dark"])
    ax.text(-0.35, max(counts.values) * 1.16, f"Median = {med}", ha="left",
            va="center", fontsize=8.6, fontweight="bold",
            color=PALETTE["red_strong"])
    ax.text(0.0, -0.30,
            f"Of the {n_self} respondents who identified as participants, {n} gave a numeric score; "
            f"{n_pna} chose “prefer not\nto answer”, {n_struct} were never routed to the participant "
            f"section (structural skip), and {n_item} did not answer.",
            transform=ax.transAxes, ha="left", va="top", fontsize=7.2,
            fontstyle="italic", color=PALETTE["neutral_dark"], linespacing=1.5)
    fig.tight_layout()
    return _save(fig, "fig3_ceremony_good.png")


# ── Figure 4: satisfaction by preparation status ─────────────────────────────

def fig_prep_outcome(pp):
    groups = [("No preparation", "none"), ("Any preparation", "prep")]
    data, labels = [], []
    for lab, key in groups:
        d = pp.loc[pp.prep_any == key, "ceremony_good_num"].dropna().astype(float)
        data.append(d)
        labels.append(f"{lab}\n(n = {len(d)})")

    fig, ax = plt.subplots(figsize=(5.4, 3.9))
    # Only the any-preparation group gets a box. A box-and-whisker over five
    # observations conveys distributional precision those five points do not
    # have (peer-review minor point), so the no-preparation group is drawn as
    # its raw points with a median tick and nothing else.
    # fliers are suppressed: every observation is already drawn as a raw point
    bp = ax.boxplot([data[1]], positions=[2], tick_labels=[labels[1]], widths=.46,
                    patch_artist=True, showfliers=False,
                    medianprops=dict(color=PALETTE["red_strong"], linewidth=1.8),
                    boxprops=dict(facecolor=PALETTE["neutral_light"],
                                  edgecolor=PALETTE["neutral_dark"], linewidth=0.8),
                    whiskerprops=dict(color=PALETTE["neutral_dark"], linewidth=0.8),
                    capprops=dict(color=PALETTE["neutral_dark"], linewidth=0.8))
    for patch in bp["boxes"]:
        patch.set_zorder(2)
    ax.set_xlim(0.4, 2.6)
    ax.set_xticks([1, 2])
    ax.set_xticklabels(labels)
    # median tick for the unboxed group
    ax.plot([1 - 0.14, 1 + 0.14], [data[0].median()] * 2,
            color=PALETTE["red_strong"], linewidth=1.8, zorder=4)

    # One marker per distinct score, area proportional to how many respondents
    # gave it — jittered raw points are unreadable on a 7-point scale where 35
    # of 58 observations tie at the ceiling.
    for i, d in enumerate(data, 1):
        vals, cnts = np.unique(d.values, return_counts=True)
        ax.scatter(np.full(len(vals), i), vals, s=26 + 9 * cnts,
                   color=PALETTE["blue_secondary"], alpha=.75, zorder=3,
                   edgecolor="white", linewidth=.5)
        ax.text(i + 0.30, d.median(), f"Mdn {d.median():.0f}", ha="left",
                va="center", fontsize=8, color=PALETTE["red_strong"])

    ax.set_ylabel("Reported satisfaction (0–6)")
    ax.set_ylim(-0.5, 6.6)
    ax.set_yticks(range(7))
    ax.yaxis.grid(True, alpha=.25, linewidth=.6, zorder=0)
    ax.text(0.02, 0.98, "EXPLORATORY", transform=ax.transAxes, ha="left",
            va="top", fontsize=7.6, fontweight="bold", color=PALETTE["red_strong"],
            bbox=dict(boxstyle="round,pad=0.32", facecolor="white",
                      edgecolor=PALETTE["red_strong"], linewidth=0.8))
    ax.text(0.0, -0.24,
            "Marker area is proportional to the number of respondents giving that score. The\n"
            f"no-preparation group (n = {len(data[0])}) is drawn as its raw points and median tick only:\n"
            "a box would imply distributional precision five observations cannot support.",
            transform=ax.transAxes, ha="left", va="top", fontsize=7.4,
            fontstyle="italic", color=PALETTE["neutral_dark"], linespacing=1.5)
    fig.tight_layout()
    return _save(fig, "fig4_prep_outcome.png")


# ── Graphical abstract (repo-policy asset; not a JPD submission element) ──────

def fig_graphical_abstract(df, pp, ch):
    ana = df[df.in_analytic]
    n_ana = len(ana)
    n_part = int(ana["analytic_participant"].sum())
    n_fac = int(ana["analytic_facilitator"].sum())

    cg = pp["ceremony_good_num"].dropna().astype(int)
    counts = cg.value_counts().reindex(range(7), fill_value=0)
    n_cg, med = len(cg), int(cg.median())

    labs = choices_map(ch, "drugs_used", "label_en")
    subs = ["tabaco", "cacao", "lsd", "dmt", "ayahuasca", "hongos_magic",
            "ketamina", "mdma"]
    base_n = int(pp["drug_used_part"].notna().sum())
    counts_s = {labs.get(s, s).split(". ")[-1]:
                int(pd.to_numeric(pp.get(f"drug_used_part/{s}"),
                                  errors="coerce").fillna(0).sum())
                for s in subs if f"drug_used_part/{s}" in pp}
    top3 = pd.Series(counts_s).sort_values(ascending=False).head(3).iloc[::-1]

    ncc = pp["non_con_contact"].dropna()
    ncc_base = int(len(ncc))
    ncc_yes = int((ncc == "si").sum())

    fig = plt.figure(figsize=(12, 6.2))
    fig.patch.set_facecolor("white")
    gs = fig.add_gridspec(2, 3, height_ratios=[0.48, 1.0],
                          hspace=0.30, wspace=0.30,
                          left=0.045, right=0.965, top=0.94, bottom=0.15)

    # header band
    head = fig.add_subplot(gs[0, :])
    head.axis("off")
    head.add_patch(FancyBboxPatch((0, 0.06), 1, 0.88,
                                  boxstyle="round,pad=0,rounding_size=0.02",
                                  transform=head.transAxes, linewidth=0,
                                  facecolor=PALETTE["band"], zorder=0))
    head.text(0.025, 0.72, "Ceremonial entheogen use in Puerto Rico",
              fontsize=17, fontweight="bold", color=PALETTE["navy_text"],
              va="center", ha="left", transform=head.transAxes)
    head.text(0.025, 0.36,
              f"First descriptive characterization \u2022 anonymous online convenience survey of "
              f"adults 21+ \u2022 analytic sample N = {n_ana}\n"
              f"{n_part} participant-side reports and {n_fac} facilitator-side reports; "
              f"branches unlinked \u2022 unweighted, no prevalence claims",
              fontsize=9.6, color=PALETTE["neutral_dark"], va="center", ha="left",
              transform=head.transAxes, linespacing=1.6)

    # panel 1 — substances
    ax1 = fig.add_subplot(gs[1, 0])
    ax1.barh(top3.index, top3.values, color=PALETTE["blue_main"],
             edgecolor="none", height=0.6, zorder=3)
    for y, v in enumerate(top3.values):
        ax1.text(v + top3.max() * 0.02, y, f"{v} ({100 * v / base_n:.0f}%)",
                 va="center", fontsize=8.5, color=PALETTE["neutral_dark"])
    ax1.set_xlim(0, top3.max() * 1.34)
    ax1.set_ylim(-0.8, 2.8)
    ax1.set_title("What is used", fontsize=11, fontweight="bold",
                  color=PALETTE["navy_text"], loc="left", pad=8)
    ax1.set_xlabel(f"Participants, ceremonies attended (base n = {base_n})",
                   fontsize=8.2)
    ax1.tick_params(axis="y", length=0, labelsize=9)
    ax1.spines["left"].set_visible(False)
    ax1.xaxis.grid(True, alpha=.25, linewidth=.6, zorder=0)

    # panel 2 — satisfaction ceiling
    ax2 = fig.add_subplot(gs[1, 1])
    ax2.bar(counts.index, counts.values,
            color=[PALETTE["blue_secondary"]] * 5 + [PALETTE["blue_main"]] * 2,
            edgecolor="none", width=0.74, zorder=3)
    ax2.set_xticks(range(7))
    ax2.set_ylim(0, max(counts.values) * 1.24)
    ax2.set_title("How it was rated", fontsize=11, fontweight="bold",
                  color=PALETTE["navy_text"], loc="left", pad=8)
    ax2.set_xlabel(f"Satisfaction 0\u20136 (base n = {n_cg})", fontsize=8.2)
    ax2.set_ylabel("Participants", fontsize=8.2)
    ax2.yaxis.grid(True, alpha=.25, linewidth=.6, zorder=0)
    n_top = int(counts.loc[[5, 6]].sum())
    ax2.text(0.5, max(counts.values) * 1.06,
             f"median {med} \u2014 {n_top}/{n_cg} ({100 * n_top / n_cg:.0f}%) rated 5\u20136",
             fontsize=8.8, color=PALETTE["red_strong"], fontweight="bold",
             ha="left", va="center")

    # panel 3 — safety
    ax3 = fig.add_subplot(gs[1, 2])
    ax3.axis("off")
    ax3.set_title("What was reported about safety", fontsize=11,
                  fontweight="bold", color=PALETTE["navy_text"], loc="left", pad=8)
    ax3.text(0.0, 0.80, f"{ncc_yes} of {ncc_base}", fontsize=30, fontweight="bold",
             color=PALETTE["red_strong"], va="center", ha="left",
             transform=ax3.transAxes)
    ax3.text(0.0, 0.56,
             "participants reported non-consensual\nphysical contact during a ceremony\n"
             f"({100 * ncc_yes / ncc_base:.0f}% of those answering)",
             fontsize=9.4, color=PALETTE["neutral_dark"], va="center", ha="left",
             transform=ax3.transAxes, linespacing=1.6)
    ax3.plot([0.0, 0.92], [0.40, 0.40], lw=0.8, color=PALETTE["neutral_light"],
             transform=ax3.transAxes)
    ax3.text(0.0, 0.24,
             "Protective practice was common but not\nuniversal, and facilitator-side reports\n"
             "cannot be linked to participant reports.",
             fontsize=9.0, color=PALETTE["neutral_dark"], va="center", ha="left",
             transform=ax3.transAxes, linespacing=1.6)

    fig.text(0.045, 0.04,
             "Descriptive, unweighted, non-probability sample \u2014 estimates describe respondents, "
             "not the Puerto Rican population.",
             fontsize=8.4, fontstyle="italic", color=PALETTE["neutral_dark"])
    return _save(fig, "graphical_abstract.png")


def main():
    df, ch, _sv = load()
    pp = df[df.in_analytic & df.analytic_participant]
    fig_flow(df)
    fig_substances(df, ch)
    fig_ceremony_good(pp)
    fig_prep_outcome(pp)
    fig_graphical_abstract(df, pp, ch)


if __name__ == "__main__":
    main()
