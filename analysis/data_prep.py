"""Load, decode, and derive analytic variables.

Importable: `load()` returns (df, choices, survey) where df has derived columns:
  role, analytic_facilitator, analytic_participant, ceremony_good_num,
  ceremony_good_3lvl, prep_any, and per-branch attention/duplicate flags are
  added in quality.py.
"""
import warnings
import pandas as pd
import numpy as np
from config import (RESULTS_XLSX, KOBO_XLSX, ORDINAL_SCALES, ROLE_FAC, ROLE_PART,
                    LEGAL_KNOW_HARMONIZED)

warnings.simplefilter("ignore", pd.errors.PerformanceWarning)


def load_choices():
    ch = pd.read_excel(KOBO_XLSX, sheet_name="choices")
    ch.columns = ["list_name", "name", "label_es", "label_en"]
    return ch


def load_survey():
    return pd.read_excel(KOBO_XLSX, sheet_name="survey")


def choices_map(ch, list_name, lang="label_en"):
    sub = ch[ch.list_name == list_name]
    return dict(zip(sub["name"], sub[lang]))


def decode_ceremony_good(s):
    """'_0'..'_6' -> 0..6 (Int); 'pna' -> <NA> in the numeric view but kept
    as a labeled category in the raw column. Structural skips stay <NA>."""
    def f(v):
        if isinstance(v, str) and v.startswith("_") and v[1:].isdigit():
            return int(v[1:])
        return pd.NA
    return s.map(f).astype("Int64")


# Excel/Kobo export quirk: bare numeric-underscore choice codes with no
# letter suffix ("4_6", "7_12") lost their underscore on export and became
# the ints 46/712 in the results file; codes with a letter suffix ("1_3h",
# "2_3d", "2_6_month") were unaffected. Verified against the koboxls.xlsx
# `choices` sheet for `ceremony_duration` — no other code collides with
# these values, so the remap is unambiguous, not guessed.
CEREMONY_DURATION_FIX = {46: "4_6", 712: "7_12"}


def fix_ceremony_duration(df):
    df["ceremony_duration"] = df["ceremony_duration"].replace(CEREMONY_DURATION_FIX)
    return df


def fix_amount_cer_year(df):
    """One respondent's amount_cer_year was recorded as -3, impossible for a
    count. Client-confirmed correction: -3 -> 3 (sign-entry error)."""
    df["amount_cer_year"] = df["amount_cer_year"].replace(-3, 3)
    return df


def derive_roles(df):
    fac = df[ROLE_FAC]
    part = df[ROLE_PART]
    is_fac = fac.eq("si")
    is_part = part.eq("si")

    role = pd.Series("other", index=df.index, dtype="object")
    role[is_fac & is_part] = "dual"
    role[is_fac & ~is_part] = "facilitator_only"
    role[~is_fac & is_part] = "participant_only"
    # explicit screen-outs: both role items answered 'no'
    role[fac.eq("no") & part.eq("no")] = "screenout_no_no"
    # abandoned: both role items blank
    role[fac.isna() & part.isna()] = "abandoned_blank"

    df["role"] = role
    df["analytic_facilitator"] = is_fac
    df["analytic_participant"] = is_part
    # role-fork sample: reached the role fork (excludes abandoned-blank only).
    df["in_role_fork"] = ~role.isin(["abandoned_blank"])
    # primary analytic sample (author decision, 2026-08-13): also excludes the
    # 14 explicit no/no screen-outs, who answer no substantive items. Reported
    # instead as a screening-yield rate (screen-outs / in_role_fork) in Methods
    # rather than described as their own subgroup. See
    # manuscript/sources/analysis_resolutions.md §1a'.
    df["in_analytic"] = df["in_role_fork"] & ~role.isin(["screenout_no_no"])
    return df


def derive_ceremony_good_3lvl(df):
    """Collapse ceremony_good_num (0-6) to 3 ordered levels for the §4.7
    multivariable model — see config.CEREMONY_GOOD_3LVL_LABELS for rationale."""
    def f(v):
        if pd.isna(v):
            return pd.NA
        v = int(v)
        return 0 if v <= 3 else (1 if v <= 5 else 2)
    df["ceremony_good_3lvl"] = df["ceremony_good_num"].map(f).astype("Int64")
    return df


def derive_prep(df):
    """Participant preparation exposure (integration has no clean item, so the
    analysis focuses on preparation -> outcome, per client decision).

    prep_part (si_no_av_pna): si / a_veces / no / pna.
    prep_any: True if 'si' or 'a_veces'; False if 'no'; <NA> if pna/skip.
    """
    p = df["prep_part"]
    prep_any = pd.Series(pd.NA, index=df.index, dtype="object")
    prep_any[p.isin(["si", "a_veces"])] = "prep"
    prep_any[p.eq("no")] = "none"
    df["prep_any"] = prep_any
    df["prep_3lvl"] = p.where(p.isin(["si", "a_veces", "no"]))  # drops pna/skip
    return df


def add_ordinals(df):
    for col, order in ORDINAL_SCALES.items():
        if col == "ceremony_good":
            df["ceremony_good_num"] = decode_ceremony_good(df[col])
        else:
            code = {k: i for i, k in enumerate(order)}
            df[col + "_num"] = df[col].map(code).astype("Int64")
    return df


def derive_legal_know_harmonized(df):
    """§9.2: harmonized 0-4 ordinal code shared by `info_est_legal_part`
    (general) and `legal_know_part` (most-recent-ceremony) — see
    config.LEGAL_KNOW_HARMONIZED for why these can't use the per-list_name
    ORDINAL_SCALES pipeline."""
    df["info_est_legal_part_num"] = df["info_est_legal_part"].map(LEGAL_KNOW_HARMONIZED).astype("Int64")
    df["legal_know_part_num"] = df["legal_know_part"].map(LEGAL_KNOW_HARMONIZED).astype("Int64")
    return df


def load():
    df = pd.read_excel(RESULTS_XLSX)
    ch = load_choices()
    sv = load_survey()
    df = fix_ceremony_duration(df)
    df = fix_amount_cer_year(df)
    df = derive_roles(df)
    df = derive_prep(df)
    df = add_ordinals(df)
    df = derive_ceremony_good_3lvl(df)
    df = derive_legal_know_harmonized(df)
    df = df.copy()  # de-fragment after repeated inserts
    return df, ch, sv


if __name__ == "__main__":
    df, ch, sv = load()
    print("rows x cols:", df.shape)
    print("\nrole:\n", df["role"].value_counts(dropna=False).to_string())
    print("\nanalytic_participant:", int(df["analytic_participant"].sum()),
          "| analytic_facilitator:", int(df["analytic_facilitator"].sum()))
    print("\nceremony_good_num (participants only):")
    pp = df[df["analytic_participant"]]
    print(pp["ceremony_good_num"].value_counts(dropna=False).sort_index().to_string())
    print("median:", pp["ceremony_good_num"].median())
    print("\nprep_any x ceremony_good_num median:")
    print(pp.groupby("prep_any", dropna=False)["ceremony_good_num"].agg(["count", "median"]).to_string())
