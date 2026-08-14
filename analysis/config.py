"""Shared configuration: paths, decoding maps, ordinal scales, reporting rules.

All value decodes derive from the KoboToolbox XLSForm (`koboxls.xlsx`):
`survey` sheet = skip/relevance logic, `choices` sheet = value sets.
Nothing here is guessed; ordered scales use the choices-sheet order.
"""
from pathlib import Path

# ---- paths ----
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
OUT = ROOT / "outputs"
FIG = OUT / "figures"
TAB = OUT / "tables"

RESULTS_XLSX = DATA / "results_7_15_2026.xlsx"
KOBO_XLSX = DATA / "koboxls.xlsx"

for d in (OUT, FIG, TAB):
    d.mkdir(parents=True, exist_ok=True)

# ---- reporting rules ----
SUPPRESS_N = 5          # subgroup cells with n < SUPPRESS_N are masked
RANDOM_SEED = 20260715  # bootstrap reproducibility

# ---- ordered ordinal scales (choices-sheet order, low -> high) ----
# `pna`/`not_sure` are retained as substantive categories elsewhere but are
# NOT part of the numeric order; they are held out of ordinal encodings.
ORDINAL_SCALES = {
    "ceremony_good": ["_0", "_1", "_2", "_3", "_4", "_5", "_6"],  # -> 0..6
    "trust_level":   ["none", "some", "mid", "a_lot", "fully"],
    "comfort_safe":  ["very_uncomf", "some_uncomf", "mostly_comf", "fully_comf"],
    "followed_prep": ["none", "some", "mostf", "all"],
    # legal_worry_scale, most-recent-ceremony item (§3 item 8 / §9)
    "est_legal_worry_part": ["no_worry", "some_worry", "indif", "very_worry", "extr_worry"],
}

# non-response tokens retained as their own category (uniform policy)
NONRESPONSE = {"pna", "not_sure"}

# ---- §9 psychometric check: harmonized legal-knowledge ordinal code ----
# `info_est_legal_part` (general, list_name legal_know_scale) and
# `legal_know_part` (most-recent-ceremony, list_name legal_know_scale_2) ask
# the same participant-side construct but use two different `list_name`
# option sets that can't go through the per-list_name ORDINAL_SCALES
# pipeline: legal_know_scale_2 is missing the bottom "not aware at all"
# category that legal_know_scale has (no_know/no_know_2). The remaining four
# option codes are identical strings across both lists, so they're mapped to
# one shared 0-4 ordinal code by content match, not list_name. `pna` (both
# lists) is excluded, same as every other ordinal numeric encoding here.
LEGAL_KNOW_HARMONIZED = {
    "no_know": 0, "no_know_2": 0,
    "heard_ilegal": 1,
    "idea_gen": 2,
    "good_know": 3,
    "clear_know": 4,
}

# ---- §4.7 multivariable model: collapsed ceremony_good outcome ----
# Not a choices-sheet scale — a model-only collapse of ceremony_good_num
# (0-6) to 3 ordered levels. The raw 7-level scale has cells as thin as
# n=1-3 at the low end (severe ceiling: 51/64 answered 5-6), which risks
# quasi-complete separation in an ordinal logit at N~62; collapsing keeps
# every level well above the suppression floor while preserving order.
CEREMONY_GOOD_3LVL_LABELS = {0: "low/mixed (0–3)", 1: "mostly positive (4–5)",
                              2: "very positive (6)"}

# ---- role fork ----
ROLE_FAC = "is_facilitator"
ROLE_PART = "is_participant"

# ---- attention checks, per branch (verified: branch-specific, not uniform) ----
ATTN_FACILITATOR = ["atencion_1", "atencion_2", "atencion_3"]
ATTN_PARTICIPANT = ["atencion_3_2", "atencion_4", "atencion_5", "atencion_6"]
# correct answers recovered from the survey-sheet item wording
ATTN_KEY = {
    "atencion_1": "disagree",   # "select Disagree"
    "atencion_2": "_7",          # 3+4
    "atencion_3": "falso",       # humans can breathe underwater -> FALSE
    "atencion_3_2": "disagree",  # "select Disagree"
    "atencion_4": "_4",          # 2x2
    "atencion_5": "si",          # "answer with Yes"
    "atencion_6": "cierto",      # 12 > 2 -> TRUE
}

# ---- duplicate-screening fields (ev_dup empty x100; _submitted_by empty) ----
DUP_FIELDS = ["nickname", "password"]

# ---- the three distinct drug variables (never conflate) ----
DRUG_VARS = {
    "drugs_used_facil": "facilitator: substances across ceremonies LED (select-multiple)",
    "drug_used_part":   "participant: substances across ceremonies ATTENDED (select-multiple)",
    "drugs_used_part":  "participant: substance in MOST RECENT ceremony (select-one)",
}

# ---- §3 item 1 / §5.3: safety-domain association predictors ----
# Facilitator-side select-multiple predictors, valid to cross with
# facilitator-witnessed `exp_crisis` (same <=8 respondents on both sides, no
# participant-linkage gap). Each collapsed to a binary "any substantive
# response" indicator; the excluded option-suffixes below are non-substantive
# placeholders (no training / never had this experience / prefer not to
# answer) and don't count toward the positive indicator, but the respondent
# is still counted as having answered.
SAFETY_FACILITATOR_ONEHOT_PREDICTORS = {
    "training_facilitator": {"train_facil_na", "train_facil_pna"},
    "safe_ceremony": {"pna"},
    "protocol_bad_exp": {"no_protocol", "no_exp", "pna"},
}
# exp_crisis outcome: exclude these non-substantive sub-items (uncertainty /
# non-response markers, not an actual crisis sign) from the "any crisis sign
# reported" aggregate.
EXP_CRISIS_EXCLUDE = {"not_sure", "pna"}

# ---- open-text (qualitative) fields ----
# The authoritative field list is `survey[survey.type == 'text'].name`, not the
# plan's prose list — that prose mislabeled `add_share` as free text; it is
# actually a `select_one si_no_pna` gate for `additional_info`, the real
# free-text item. Exclude respondent identifiers (not analytic content).
TEXT_FIELD_EXCLUDE = {"nickname", "password"}

# seed keyword categories to bootstrap a codebook (client-specified themes;
# substring match, case-insensitive, ES+EN stems)
SEED_KEYWORD_CATEGORIES = {
    "legality":            ["legal", "ilegal", "ley", "leyes", "regulaci", "regulation",
                             "law", "legislat", "legaliza", "descriminaliza"],
    "education":           ["educaci", "education", "informed", "capacitaci", "training",
                             "aprendiz", "conocimiento", "awareness"],
    "facilitator_vetting": ["facilitador", "facilitator", "vetting", "certificaci",
                             "credential", "profesional", "screening", "entrenamiento"],
    # NB: bare "medic" also matches "medicina"/"medicamento" (the substance
    # itself, a very common word in this corpus) - stems below require a
    # médico/médica-shaped ending so the substance sense isn't counted here.
    "medical_presence":    [r"médic[oa]", r"medic[oa]s?\b", "doctor", "enfermer",
                             "nurse", "clinical", "clínic", "salud"],
    "consent":             ["consent", "consentimiento", "permiso", "autoriza"],
}
N_CODE_COLUMNS = 3  # code_1..code_3 in the manual-coding scaffold
