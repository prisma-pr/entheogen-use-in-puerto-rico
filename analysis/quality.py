"""Data-quality flags: attention checks (per branch) and duplicate candidates.

Policy (client decision): FLAG, never drop. Writes outputs/tables/
data_quality_flags.csv for the research team to adjudicate.
"""
import pandas as pd
from config import (ATTN_FACILITATOR, ATTN_PARTICIPANT, ATTN_KEY, DUP_FIELDS,
                    TAB)


def attention_flags(df):
    """For each respondent, score attention items in THEIR branch.
    A 'fail' = item answered but incorrect (pna/blank are not counted as fails).
    Returns a frame with per-branch answered/correct counts and a fail flag.
    """
    rows = []
    for idx, r in df.iterrows():
        branch = ATTN_FACILITATOR if r["analytic_facilitator"] else (
            ATTN_PARTICIPANT if r["analytic_participant"] else [])
        answered = correct = failed = 0
        for item in branch:
            v = r.get(item)
            if pd.isna(v) or v == "pna":
                continue
            answered += 1
            if v == ATTN_KEY[item]:
                correct += 1
            else:
                failed += 1
        rows.append({
            "attn_branch": ("facilitator" if r["analytic_facilitator"]
                            else "participant" if r["analytic_participant"]
                            else "none"),
            "attn_answered": answered,
            "attn_correct": correct,
            "attn_failed": failed,
            "attn_fail_flag": failed > 0,
        })
    return pd.DataFrame(rows, index=df.index)


def duplicate_flags(df):
    """Flag candidate duplicate responders by (nickname, password) combination
    and by nickname-only / password-only repeats. _submission_time retained for
    manual adjudication. ev_dup unusable (empty x100)."""
    key = df[DUP_FIELDS].astype("string").apply(lambda c: c.str.strip().str.lower())
    combo = key["nickname"].fillna("") + " | " + key["password"].fillna("")
    combo_dup = combo.duplicated(keep=False) & (combo.str.strip() != "|")
    nick_dup = key["nickname"].duplicated(keep=False) & key["nickname"].notna()
    pass_dup = key["password"].duplicated(keep=False) & key["password"].notna()
    out = pd.DataFrame({
        "dup_combo_flag": combo_dup,
        "dup_nickname_flag": nick_dup,
        "dup_password_flag": pass_dup,
        "dup_key": combo,
    }, index=df.index)
    return out


def build(df):
    a = attention_flags(df)
    d = duplicate_flags(df)
    flags = pd.concat([a, d], axis=1)
    # export for reviewer
    review = df[["role", "nickname", "password", "_submission_time"]].join(flags)
    review = review[flags["attn_fail_flag"] | flags["dup_combo_flag"]
                    | flags["dup_nickname_flag"] | flags["dup_password_flag"]]
    review.to_csv(TAB / "data_quality_flags.csv", index=True,
                  index_label="row", encoding="utf-8-sig")
    return flags


if __name__ == "__main__":
    from data_prep import load
    df, ch, sv = load()
    flags = build(df)
    print("attention fails:", int(flags["attn_fail_flag"].sum()))
    print(flags[flags["attn_fail_flag"]][["attn_branch", "attn_answered",
          "attn_correct", "attn_failed"]].to_string())
    print("\nduplicate-combo flagged rows:", int(flags["dup_combo_flag"].sum()))
    print("nickname-repeat rows:", int(flags["dup_nickname_flag"].sum()),
          "| password-repeat rows:", int(flags["dup_password_flag"].sum()))
    print("\nwrote outputs/tables/data_quality_flags.csv")
