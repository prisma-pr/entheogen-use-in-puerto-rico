"""Qualitative pipeline (§2.6): open-text extraction + coding scaffold.

This supports human thematic analysis; it does not replace it. Outputs:
  outputs/tables/opentext_corpus.csv         long-format corpus (all fields)
  outputs/tables/opentext_manual_coding.csv  one row per answer + empty
                                              code_1..code_N columns for the
                                              research team to fill in by hand
"""
import re
import warnings
import pandas as pd
from config import TAB, TEXT_FIELD_EXCLUDE, SEED_KEYWORD_CATEGORIES, N_CODE_COLUMNS

warnings.simplefilter("ignore")

STOPWORDS_ES = set("""
de la que el en y a los del se las por un para con no una su al lo como mas
pero sus le ya o este si porque esta entre cuando muy sin sobre tambien me
hasta hay donde quien desde todo nos durante todos uno les ni contra otros
ese eso ante ellos esto mi antes algunos
""".split())
STOPWORDS_EN = set("""
the of to and a in is it you that he was for on are with as i his they be
at one have this from or had by but some what there we can out other were
all your when up use how said each she which do their time if will way
about many then them would like so these her make thing see look could go
""".split())
STOPWORDS = STOPWORDS_ES | STOPWORDS_EN

# short strings (<4 tokens) are unreliable for langdetect; use these
# Spanish-specific function words + diacritics/punctuation as a fallback signal
ES_SHORT_MARKERS = STOPWORDS_ES | {"si", "sí"}


def get_text_fields(sv):
    """Authoritative free-text field list from survey type=='text', minus
    respondent identifiers (nickname/password are not analytic content)."""
    names = sv.loc[sv["type"] == "text", "name"].tolist()
    return [n for n in names if n not in TEXT_FIELD_EXCLUDE]


def guess_language(text):
    """Rough es/en/mixed guess. langdetect is unreliable on very short
    strings, so short answers fall back to a Spanish marker-word/diacritic
    check instead."""
    t = text.strip()
    if not t:
        return "unknown"
    words = re.findall(r"[a-záéíóúñü]+", t.lower())
    if len(words) < 4:
        if re.search(r"[áéíóúñü¿¡]", t.lower()) or any(w in ES_SHORT_MARKERS for w in words):
            return "es"
        return "en" if words else "unknown"
    try:
        from langdetect import detect, DetectorFactory
        DetectorFactory.seed = 0
        lang = detect(t)
    except Exception:
        return "unknown"
    if lang == "es":
        return "es"
    if lang == "en":
        return "en"
    return "mixed/other"


def extract_corpus(df, sv):
    """Long-format: one row per non-empty open-text answer."""
    fields = get_text_fields(sv)
    rows = []
    for field in fields:
        if field not in df.columns:
            continue
        col = df[field]
        for rid, val in zip(df["_id"], col):
            if pd.isna(val):
                continue
            text = str(val).strip()
            if not text:
                continue
            rows.append({
                "respondent_id": rid,
                "field": field,
                "text": text,
                "language_guess": guess_language(text),
            })
    return pd.DataFrame(rows, columns=["respondent_id", "field", "text", "language_guess"])


def keyword_hits(corpus, categories=SEED_KEYWORD_CATEGORIES):
    """Per-category: number of distinct answers containing >=1 keyword stem.
    Stems are small regex fragments (see config.SEED_KEYWORD_CATEGORIES),
    not literal substrings, so they are joined as-is, not re.escape'd."""
    lower = corpus["text"].str.lower()
    out = []
    for cat, stems in categories.items():
        pattern = "|".join(stems)
        n = int(lower.str.contains(pattern, regex=True, na=False).sum())
        out.append((cat, n))
    return sorted(out, key=lambda r: -r[1])


def top_tokens(corpus, n=20):
    """Plain word-frequency view (stopwords removed) to seed the codebook,
    independent of the five named seed categories."""
    counts = {}
    for text in corpus["text"]:
        for w in re.findall(r"[a-záéíóúñü]{3,}", text.lower()):
            if w in STOPWORDS:
                continue
            counts[w] = counts.get(w, 0) + 1
    return sorted(counts.items(), key=lambda r: -r[1])[:n]


def build(df, sv):
    corpus = extract_corpus(df, sv)
    corpus.to_csv(TAB / "opentext_corpus.csv", index=False, encoding="utf-8-sig")

    coding = corpus.copy()
    for i in range(1, N_CODE_COLUMNS + 1):
        coding[f"code_{i}"] = ""
    coding.to_csv(TAB / "opentext_manual_coding.csv", index=False, encoding="utf-8-sig")

    return corpus


if __name__ == "__main__":
    from data_prep import load
    df, ch, sv = load()
    corpus = build(df, sv)
    print("fields:", len(get_text_fields(sv)))
    print("non-empty answers:", len(corpus))
    print("\nby field:\n", corpus["field"].value_counts().to_string())
    print("\nlanguage_guess:\n", corpus["language_guess"].value_counts().to_string())
    print("\nkeyword hits:\n", keyword_hits(corpus))
    print("\ntop tokens:\n", top_tokens(corpus))
    print("\nwrote outputs/tables/opentext_corpus.csv")
    print("wrote outputs/tables/opentext_manual_coding.csv")
