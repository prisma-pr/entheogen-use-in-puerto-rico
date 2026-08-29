"""Per-item missing-data decomposition for the analytic sample (N=73).

Peer-review round 3 (2026-08-25): the manuscript's data-quality paragraph
asserted that most missingness on the participant items is structural rather
than nonresponse, but never showed the decomposition. This produces it.

Every item's routing condition is transcribed from the `survey` sheet of
`data/koboxls.xlsx` (group-level `relevant` expressions), not inferred from
which cells happen to be blank. Four mutually exclusive states per item,
summing to the analytic N=73:

  routed + substantive   answered with a real category
  routed + pna/not_sure  answered with a retained non-response category
                         (config.NONRESPONSE policy: kept, never dropped)
  routed + blank         genuine item nonresponse
  not routed             structural skip (the branch was never shown)

Run:  PYTHONIOENCODING=utf-8 python missingness.py
Writes: outputs/tables/missingness_by_item.csv
"""
import sys
import pandas as pd

from config import TAB, NONRESPONSE
from data_prep import load

# Group-level relevance, transcribed from koboxls.xlsx `survey`:
#   seccion_socio_dem       ${vol_part}='si' and ${over_21}='si'
#   seccion_facilitatores   ${is_facilitator}='si'
#   Secci_n_4_Participantes (${is_participant}='si' and ${pause_facil}='si'
#                            and ${is_facilitator}='si')
#                           or (${is_participant}='si' and ${is_facilitator}='no')
def routing(df):
    socio = df["vol_part"].eq("si") & df["over_21"].eq("si")
    facil = df["is_facilitator"].eq("si")
    dual_gate = (df["is_participant"].eq("si") & df["pause_facil"].eq("si")
                 & df["is_facilitator"].eq("si"))
    part_only = df["is_participant"].eq("si") & df["is_facilitator"].eq("no")
    part = dual_gate | part_only
    return {"socio": socio, "facilitator": facil, "participant": part}


# (column, branch, display label) in manuscript order.
ITEMS = [
    ("age",                    "socio",       "Age"),
    ("gender_idt",             "socio",       "Gender"),
    ("academic",               "socio",       "Education"),
    ("econ",                   "socio",       "Economic situation"),
    ("country",                "socio",       "Country of residence"),
    ("drug_used_part",         "participant", "Substances, all ceremonies attended"),
    ("drugs_used_part",        "participant", "Substance, most recent ceremony"),
    ("last_ceremony_time",     "participant", "Time since last ceremony"),
    ("last_ceremony_place",    "participant", "Place, most recent ceremony"),
    ("ceremony_format",        "participant", "Format, most recent ceremony"),
    ("ceremony_duration",      "participant", "Duration, most recent ceremony"),
    ("prep_part",              "participant", "Self-directed preparation"),
    ("facil_background",       "participant", "Knew facilitator's background"),
    ("screening_quest",        "participant", "Facilitator asked screening questions"),
    ("med_couns_part",         "participant", "Spoke to a health professional beforehand"),
    ("ceremony_good",          "participant", "Satisfaction, most recent ceremony"),
    ("trust_level",            "participant", "Trust in facilitator"),
    ("comfort_safe",           "participant", "In-ceremony comfort and safety"),
    ("non_con_contact",        "participant", "Non-consensual contact, ever"),
    ("non_con_contact_recent", "participant", "Non-consensual contact, most recent"),
    ("training_facilitator",   "facilitator", "Facilitator training background"),
    ("emergency_plan",         "facilitator", "Emergency plan"),
    ("exp_crisis",             "facilitator", "Crisis signs witnessed"),
]


def decompose(df, col, routed):
    """Four mutually exclusive counts over the analytic sample."""
    s = df[col]
    # select_multiple items export as a space-separated string; a respondent
    # who selected only 'pna' counts as non-response, same as select_one.
    tok = s.astype("string").str.strip()
    is_nonresp = tok.isin(NONRESPONSE)
    blank = s.isna()
    return {
        "n_routed": int(routed.sum()),
        "substantive": int((routed & ~blank & ~is_nonresp).sum()),
        "pna_notsure": int((routed & is_nonresp).sum()),
        "item_nonresponse": int((routed & blank).sum()),
        "structural_skip": int((~routed).sum()),
    }


def build(df):
    analytic = df[df["in_analytic"]].copy()
    routes = routing(analytic)
    rows = []
    for col, branch, label in ITEMS:
        if col not in analytic.columns:
            print(f"  !! column not found, skipped: {col}", file=sys.stderr)
            continue
        r = decompose(analytic, col, routes[branch])
        pct = 100 * r["item_nonresponse"] / r["n_routed"] if r["n_routed"] else float("nan")
        rows.append({"item": label, "variable": col, "branch": branch,
                     **r, "pct_nonresponse_of_routed": round(pct, 1)})
    out = pd.DataFrame(rows)
    assert (out[["substantive", "pna_notsure", "item_nonresponse",
                 "structural_skip"]].sum(axis=1) == len(analytic)).all(), \
        "decomposition must partition the analytic sample"
    return out


if __name__ == "__main__":
    df, _, _ = load()
    tbl = build(df)
    path = TAB / "missingness_by_item.csv"
    tbl.to_csv(path, index=False)
    pd.set_option("display.width", 200)
    print(tbl.to_string(index=False))
    print(f"\nanalytic N = {int(df['in_analytic'].sum())}")
    print("wrote", path)
