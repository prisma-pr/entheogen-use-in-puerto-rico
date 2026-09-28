# Supplement audit — `supplement.tex` vs. `v7_draft.tex`

## Bottom line

`supplement.tex` carries an explicit `RETIRED 2026-08-25` banner: the author instructed that
supplementary material be eliminated entirely, folding what was worth keeping into the main text and
dropping the rest (full disposition in `manuscript/PEER_REVIEW_R3.md` and
`manuscript/drafts/revision_notes.md`, "Follow-up to round 3" section). I confirmed this is still true of
v7: **`v7_draft.tex` contains zero occurrences of the word "supplement"** (`grep -i supplement
v7_draft.tex` returns nothing), and no `\ref`/`\cite`/cross-reference anywhere in v7 points at anything in
`supplement.tex`. Every item below is therefore orphaned from the main text's point of view — the audit
question is not "is this still cited" (nothing is) but "was this content folded into the main text
in some other form, or genuinely dropped."

Nine content blocks in `supplement.tex`; six were folded into v7 in some form, three were dropped outright.

## Item-by-item table

| Supplement item | Folded into v7? | Where (if folded) | Recommendation |
|---|---|---|---|
| Instrument verbatim wording table (`\section{Instrument: verbatim wording and scale anchors}`, one table) | **Yes** | v7 Table 1 (`\label{tab:items}`), word-for-word match | **Drop from supplement.** Fully superseded — keeping it would create a duplicate the reader has to reconcile. |
| Facilitator practice, two tables (training/screening/response; environment/dosing/emergency/crisis signs/readiness composite) | **Partially** — folded as prose, not as tables | v7 Results §3.5 "Facilitator practice" (the full paragraph enumerating training sources, screening approach, difficult-experience response, dosing, emergency planning, crisis signs) | **Drop from supplement**, per the author's explicit choice to carry this branch as prose given its n=7-8 base. The supplement tables are strictly more granular (they show every category with % of the n=7 base) but the underlying counts are unchanged from what v7's prose states. Reviewer-facing case for keeping: a reviewer double-checking a specific percentage (e.g., "86% reported personal experience/self-study") has to recompute it from the prose rather than read it off a table. This is a real but minor cost — recommend **drop**, matching the author's decision, since the n is too small (7-8) for a table to add much beyond what the prose already says exactly. |
| Four Benjamini-Hochberg family tables (bivariate, substance-stratified, safety-domain, legal-knowledge — every raw p, q, and effect size for every test in all four families) | **Partially** — the BH procedure description and the headline q-values that are quoted in text survive; the complete per-test tables do not | v7 Methods §2.6 ("Statistical approach") describes the procedure; Results §3.3-3.6 and Discussion quote roughly half a dozen of the ~20 total test results by name (e.g. trust-by-background $q=0.085$, non-consensual contact $q=0.188$ both rows, satisfaction-by-substance $q=0.166$) | **Keep-but-uncited-and-here-is-why.** This is the one block I'd flag for reconsideration. Fourteen tests across the four families are in the supplement but never named individually anywhere in v7 (e.g., every legal-knowledge-family test except the one already quoted, several bivariate-family and safety-domain rows). The main text's claim "no test in any family was significant at q<0.05" is stated as a summary (Methods/Results, in narrower form each time it applies) without the complete table a skeptical reviewer would want to check that claim against directly. JPD imposes no figure/table count limit (`JOURNAL_REQUIREMENTS.md`, re-confirmed live 2026-09-08) and explicitly supports supplementary material via Figshare, so there is no format obstacle to reinstating these four tables. See `supplement_submission.tex` below — I built a trimmed candidate containing just these four tables, for the author's sign-off, not applied to the submission package by default. |
| Exploratory proportional-odds model (one table + prose, adjusting preparation for age and facilitator trust) | **No** | Not present anywhere in v7 — `grep -i "proportional"` and `grep -i "proportional-odds"` against `v7_draft.tex` return nothing | **Dropped by author decision, confirmed correctly.** `revision_notes.md`'s "Follow-up to round 3" section lists this explicitly among items dropped, not folded. It is a real result (adjusted OR estimates, likelihood-ratio test, McFadden pseudo-$R^2$) with an honest power caveat already written into its own text (62 complete cases / 5 parameters, ~12 cases/parameter). Recommend **keep-but-uncited-and-here-is-why**: a reviewer of a purely-bivariate results section may ask "did you try adjusting for anything?" and the honest answer, "yes, exploratory, here it is with the caveat," is stronger than no answer at all. Included in `supplement_submission.tex` candidate below. |
| Psychometric reliability table (both same-respondent item pairs, α, 95% CI, n) + Spearman ρ prose + the untestable third pair (zero-variance life-impact item) | **Partially** — both α point estimates only | v7 Limitations: "$\alpha=0.58$ for trust and in-ceremony comfort; $\alpha=0.86$ for the two legal-knowledge items" | **Keep-but-uncited-and-here-is-why.** The CIs (0.31-0.74 and 0.75-0.92 respectively — the first is wide enough to matter), the corresponding Spearman ρ values, and the note about the untestable zero-variance third pair are all dropped from v7 with no pointer. This is exactly the kind of detail a methods-focused reviewer asks for once a reliability number appears in the text without its interval. Included in `supplement_submission.tex` candidate below. |
| Instrument skip-logic errors (both errors, in full prose) | **Yes** | v7 Limitations, final paragraph — both errors described in essentially the same words (unreachable follow-up item; the legal-worry item's inverted gate reaching only 6 respondents) | **Drop from supplement.** Fully superseded, word-for-word equivalent content already in the main text. |
| Missing-data distribution, attention checks, duplicate adjudication (prose) + Table S10 (missingness decomposition, identical to v7 Table 2) | **Yes** | v7 Methods §2.5 ("Missing data and data quality") covers all three (structural-skip decomposition, branch-specific attention checks, nickname/password duplicate screening) in comparable or greater detail; v7 Table 2 is the same missingness table | **Drop from supplement.** Fully superseded. |
| Qualitative corpus and coding scaffold (37 open-text fields, 285 answers, keyword-category counts, coding template note) | **No** | Not present anywhere in v7 | **Drop — correctly, for a different reason than space.** `revision_notes.md` states this was "held for a separate manuscript," not cut for word budget. It is qualitative material the team intends to analyze and publish separately; including a keyword-count teaser here would pre-empt that paper and adds nothing to a quantitative descriptive report. Recommend leaving this out of any resubmitted supplement as well — this is the one item where I agree with dropping it entirely rather than flagging it as reviewer-useful. |
| Reproducibility statement | **Yes** | v7 "Data availability" section: "Every number reported here is generated by an executable Python pipeline that reads the raw survey export and the XLSForm directly..." | **Drop from supplement.** Fully superseded. |

## Recommendation summary

- **Drop (fully superseded, no residual value):** instrument-wording table, facilitator-practice tables,
  skip-logic-errors prose, missingness/attention-check/duplicate prose and table, reproducibility statement.
- **Drop (author's substantive reason, not space):** qualitative corpus and coding scaffold.
- **Keep-but-uncited-and-here-is-why (candidate for reinstatement as supplementary material):** the four
  BH-correction family tables, the exploratory proportional-odds model, and the full psychometric
  reliability table (with CIs and Spearman ρ). These three blocks are the only places where a reviewer
  could independently verify claims the main text makes only in summary form ("no test... significant at
  q<0.05"; two α point estimates with no interval). I built `manuscript/final/supplement_submission.tex`
  containing exactly these three blocks, trimmed from the full `supplement.tex`, as a candidate for the
  author's sign-off — **it is not wired into the submission package by default**, since re-adding
  supplementary material reverses an explicit 2026-08-25 author decision and that reversal is not mine to
  make unilaterally. If the author declines, the existing `SUBMISSION_CHECKLIST.md` treats "no supplement"
  as the default.

Nothing was deleted from `supplement.tex` itself — it is untouched and remains in the repository as the
analysis record, exactly as its own retirement banner says it should.
