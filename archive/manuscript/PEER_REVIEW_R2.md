# Peer review — Phase 5, round 2

**Manuscript reviewed:** [`drafts/v3_draft.tex`](drafts/v3_draft.tex) (30 pp.) + [`drafts/supplement.tex`](drafts/supplement.tex),
with [`references/references.bib`](references/references.bib) (31 entries), the four figures in
[`figures/`](figures/), and [`final/STROBE_checklist.md`](final/STROBE_checklist.md). This is the manuscript
that closed [`PEER_REVIEW.md`](PEER_REVIEW.md) (round 1) — every round-1 finding was applied to produce v3.

**Status: closed — every finding applied in [`drafts/v4_draft.tex`](drafts/v4_draft.tex) (29 pp.) and the
revised [`drafts/supplement.tex`](drafts/supplement.tex) (9 pp.).** Word count measured 3,947 (citations
excluded), down from 4,295, comfortably under the 4,000-word cap. All 21 reference corrections applied and
independently re-confirmed in the compiled bibliography (Antonio Inserra and Heather Jackson both now render
correctly). Both `.tex` files compile clean (`pdflatex` \(\times\)3 + `bibtex`) and were visually inspected
page-by-page for formatting defects; none found. The disposition table at the bottom records what was done
for each item, and [`drafts/revision_notes.md`](drafts/revision_notes.md) carries the full change log.

## How this review was conducted

Three passes, as specified in `MANUSCRIPT_PLAN.md` Phase 5, all run fresh against v3 (round 1's findings are
not re-litigated except where re-checking them surfaced something round 1 missed):

1. **Methodological rigor** — close read against what a non-probability, unweighted, N=73 descriptive design
   supports, plus a specific hunt for places where the manuscript's own stated conventions (family
   independence, suppression policy, permutation-testing use) don't match what the tables actually do.
2. **Journal peer-review simulation** — treating v3 as a resubmission and asking whether it would now clear
   *Journal of Psychoactive Drugs* review, including a hard re-check of the verbatim word-count requirement.
3. **Citation and reporting integrity** — full external re-verification of all 31 references (going beyond
   round 1's DOI/journal/volume check to a name-by-name author audit against CrossRef), plus independent
   recomputation of every number in both `.tex` files from the raw data.

Two things were run rather than read, as in round 1:

- **Independent recomputation from raw data.** A background agent rebuilt every count, base, test statistic,
  p-value, q-value, and effect size directly from `data/results_7_15_2026.xlsx` via
  `analysis/data_prep.load()` and the project's own `stats_helpers.py` primitives, without copying the
  manuscript-specific aggregation code in `report.py`. I independently re-ran its two flagged discrepancies
  by hand to confirm them before including them here.
- **External reference verification.** A background agent re-checked all 31 references against CrossRef/
  PubMed. Its report showed enough gaps under my own spot-checking (it missed real errors in two entries)
  that I re-ran the check myself directly against the CrossRef REST API for every DOI-bearing entry — the
  citation section below is my own direct-fetch results, credited to the agent's report where it matches and
  corrected where it undercounted.

Neither environment has `PARALLEL_API_KEY` set, so citation verification used the WebFetch/WebSearch fallback
and direct CrossRef API calls rather than the `parallel-web` skill.

---

# Pass 1 — Methodological rigor

Overall: v3 is materially more disciplined than v2 was — round 1's fixes held up under a fresh, independent
recomputation of essentially every number in both files, with only two small transcription errors surviving
(below). The problems found this round are narrower and more mechanical than round 1's: one compliance gap
that was already flagged and never closed, one place where the manuscript's own methodological
self-description is factually wrong, and two prose numbers that don't match their own tables.

### R2-1 (Major) — The manuscript still exceeds the JPD's 4,000-word cap; the trim flagged after v3 was never done

`drafts/revision_notes.md` already knew this: *"Expect to need a final ~50–100-word trim at submission... the
counting convention matters: v2 was declared compliant at 3,870 by a count this script reproduces as 4,123."*
That trim was never applied to `v3_draft.tex`. Measuring Introduction–Discussion the same way (comments
stripped, `\citep`/`\cite` contents excluded, LaTeX commands stripped) gives **4,295 words**, not the ~50–100
words over budget the note anticipated but **~295 words over** the verbatim 4,000-word cap
(`JOURNAL_REQUIREMENTS.md`: *"Word limit (Intro–Methods–Results–Discussion): 4,000 words | Verbatim"*). By
section: Introduction 438, Methods 1,319 (grew the most since v2 — the P1-1/P1-2/P1-4/P1-8 disclosures round 1
added all landed here), Results 1,374, Discussion 1,224.

The count above is also the *generous* convention: it drops citation text entirely. A real word processor
count of the compiled PDF would count the rendered `(Author et al. YEAR)` text, which adds roughly another
100+ words across the 39 citation instances in the body — meaning the true overage against however JPD
actually counts is probably closer to 300–400 words, not the ~300 the generous convention already shows.

**Proposed disposition:** trim ~300–350 words from Methods and Results specifically (Introduction and
Discussion are already lean relative to their content). Candidates, in order of how little narrative they
cost: (a) Methods §2.3–2.4 restate several exact figures that Tables 2–3 already carry in full (e.g., the
per-item n's spelled out in prose); tighten to reference the table rather than repeat every number; (b) the
protocol-deviations paragraph (§2.6) and the facilitator-practice paragraph (§3.5) can each lose one clause
without losing a caveat; (c) do **not** cut anything from the disclosure sentences round 1 added (P1-1
through P1-9) — those are exactly the qualifying language `JOURNAL_REQUIREMENTS.md` warned against cutting.
This is mechanical tightening, not a new judgment call, so I'll apply it directly in `v4_draft.tex` unless
you'd rather review the specific cuts first.

### R2-2 (Moderate) — Methods §2.5's claim that the four BH-correction families "share neither exposures nor outcome domains" is false for two variables

Verbatim: *"All other bivariate tests were assigned to four prespecified families... corrected jointly within
family by the Benjamini–Hochberg procedure and kept separate because they share neither exposures nor outcome
domains."*

Traced every test in Supplementary Tables S4–S7 by the variable it uses:

| Variable | Appears in | Count |
|---|---|---|
| `non_con_contact` (non-consensual contact) | Safety-domain family ×3 (background, screening, HR-index); Substance family ×1; Legal-knowledge family ×3 | **7 tests across 3 of the 4 families** |
| `screening_quest` (screening received) | Bivariate family ×2 (comfort, trust); Safety-domain family ×1; Legal-knowledge family ×3 | **6 tests across 3 of the 4 families** |

Both variables recur as predictor or outcome across three of the four supposedly independent families. This
doesn't change any substantive conclusion — every q-value in every family is already >0.05, and correcting
across the union of tests that share either variable would only push q-values higher, reinforcing the
existing "nothing survives correction" conclusion, not reversing it. But the Methods sentence describing *why*
the families are separate is incorrect as written.

**Proposed disposition (two options, as round 1 offered for comparable choices):**
- **(a) Correct the claim.** Replace "share neither exposures nor outcome domains" with an accurate
  description — the families are organized by substantive theme (general bivariate, substance-stratified,
  safety, legal-knowledge), not by variable exclusivity, and two variables (`non_con_contact`,
  `screening_quest`) recur across families; add one sentence noting that family-wise correction therefore
  does not bound the error rate specific to conclusions drawn about either variable across all the tests it
  appears in. Cheap, no q-values change, no table changes.
- **(b) Restructure the families** so no variable appears in more than one, recomputing BH within the merged
  sets. More faithful to the original claim, but touches four supplementary tables for a fix that cannot
  change any conclusion (all q's are already non-significant and would only get larger).

**My recommendation is (a)**, for the same reason round 1 recommended the lower-cost, no-conclusion-changing
option where one was available: it fixes the actual defect (an inaccurate methodological claim) without
manufacturing motion in numbers that are already unambiguous.

### R2-3 (Minor) — Two prose numbers don't match their own tables

Independent recomputation from the raw data caught two descriptive-statistic transcription errors (everything
else — every count, base, test statistic, p-value, q-value, and effect size in both files — reproduced
exactly):

1. **§3.4** claims perceived comfort/safety returned "a median of 3 in every subgroup tested" when compared
   by facilitator-background knowledge. The `facil_background="no"` subgroup has only **2** non-missing
   values (`[1, 3]`), median **2.0**, not 3. The two larger subgroups (`si`, n=54; `some`, n=8) do have median
   3, and the Kruskal–Wallis statistic itself is correct and unaffected (H=2.24, p=0.326, matching
   Supplementary Table S4 exactly) — this is a prose-summary error, not a test error, but "every subgroup" is
   also an overclaim on its own terms: a 2-person median is too unstable to fold into a uniformity claim.
2. **Supplement §S3** (prose after Table S7) states the legal-worry median among the 8 respondents reporting
   disclosure to a health professional is "median 2 (IQR 0–2)." The 8 values are `[0,0,0,1,2,2,2,4]`,
   **median 1.5**, not 2. IQR 0–2 is correct. The test statistics (H=6.92, p=0.031, ε²=0.09, q=0.283) are
   correct and unaffected.

**Proposed disposition:** fix both numbers in place; for (1), also soften "every subgroup" to something that
doesn't fold a 2-person cell into a general pattern (e.g., "median 3 in the two larger subgroups; the
`facil_background`-unknown-or-no subgroup (n=2) is too small to characterize").

### R2-4 (Minor) — The one nominally-significant bivariate result doesn't get the same robustness check the paper applies elsewhere

The trust-by-facilitator-background Kruskal–Wallis test (H=8.15, p=0.017, ε²=0.10) is the single test in the
bivariate family (Table S4) that reaches uncorrected significance — it doesn't survive BH correction
(q=0.102), but it's still the one result in that family a reader's eye goes to. One of its three groups
(`facil_background="no"`) contributes only 3 non-missing trust values (Table 3 lists 4 respondents in that
category, but one has a missing trust score). The paper already knows how to stress-test a thin-sample
comparison — it ran a tie-aware permutation test as a named robustness check for the primary preparation
comparison (§3.6) — but doesn't extend the same treatment here, where the asymptotic KW chi-square
approximation is arguably least reliable in the whole bivariate family.

**Proposed disposition:** add a permutation-based KW p-value for this one test alongside the asymptotic one,
the same way §3.6 reports both for the primary comparison. Computed directly (10,000 label permutations,
seed 20260715, matching the study's existing permutation convention): **permutation $p=0.010$**, slightly
*stronger* than the asymptotic $p=0.017$, not weaker — it does not survive BH correction either way
($q=0.102$ was computed from the asymptotic $p$; recomputing $q$ from the permutation $p$ would only lower
it further, not raise it above 0.05). Low cost, and it reinforces rather than undercuts the one number in
this table a careful reader will focus on.

### R2-5 (Minor) — "De-identified" vs. "anonymous" in the Data availability statement

The statement's first sentence commits to depositing "de-identified survey data," while its second sentence
and Methods §2.1 both say the data are anonymous by design — no identifiers were ever collected, so there is
nothing to *de-identify*. "De-identified" implies a removal step that didn't happen; "anonymous" is the term
the rest of the manuscript uses correctly and consistently.

**Proposed disposition:** change "de-identified survey data" to "anonymous survey data" in the Data
availability statement. One word, no policy content changes — this doesn't touch the repository-choice/DOI
question you asked to leave as-is.

---

# Pass 2 — Journal peer-review simulation

*Written as a reviewer reassessing the resubmission that closed round 1's major-revision request.*

Round 1 correctly identified this as a competent, unusually self-critical descriptive paper and recommended
major revision on disclosure and precision grounds, not new analysis. Having independently re-verified nearly
every number and every reference, I'd characterize v3 the same way round 1 characterized v2's intent: the
substantive concerns (branch overlap, referent mismatches, suppression policy, ethics/competing-interests
disclosure, comparator numbers) are now handled well and I would not reopen any of them.

What would stop this specific manuscript at this specific journal today is narrower and procedural:

**A verbatim, quantified requirement is still violated.** Editorial offices that check word counts
mechanically before sending a manuscript to reviewers will flag this regardless of content quality — R2-1 is
not a stylistic nicety, it's the one requirement in `JOURNAL_REQUIREMENTS.md` marked "Verbatim" that the
manuscript does not currently meet. I would not let this manuscript go out for review in its current word
count.

**Author-identity accuracy in the reference list is a real, if quiet, problem.** Two citations
(`ruffell2021ceremonial`, `nayak2023naturalistic`) currently omit a real co-author of the cited work, and six
more have a co-author's given name wrong (`carvalho2025scoping`, `siegel2023psychedelic` — two errors in one
entry, `gorman2021psychedelic`, `pilecki2021ethical`, `dutton2025harm`, `teixeira2026ayahuasca` — three errors
in one entry). None of this reflects on the *manuscript's* science, but a reviewer or editorial office that
spot-checks references (increasingly common practice given citation-fabrication concerns in the field) would
find a wrong or incomplete author list on 8 of 31 references, which reads carelessly even though nothing here
was invented — every cited work exists and is correctly matched to its DOI, title, journal, and findings.
This should be fixed before submission regardless of whether a reviewer would ever check.

Everything else I looked for — the facilitator-branch framing, the safety cross-tab referent mismatches, the
suppression-policy consistency, the ethics/competing-interests completeness, the comparator numbers in
§4.1 — held up. I did not find a new substantive objection of the kind round 1's R1–R10 raised.

**Recommendation: minor revision.** Unlike round 1, nothing here requires new author judgment calls beyond
confirming the disposition choices above — R2-1 through R2-5 are precision and compliance fixes with a single
clearly-better option each, not policy questions.

---

# Pass 3 — Citation and reporting integrity

## 3a. Reference verification — direct CrossRef re-check of all 31 entries

A background agent's first pass found 6 author-name errors across 6 entries and correctly identified the
"Online First" pagination status of all 5 unpaginated entries. Spot-checking three of its "confirmed correct"
entries directly against the CrossRef REST API surfaced two more errors it had missed (a second wrong name
within an entry it had already flagged once, and a wrong name in an entry it hadn't flagged at all), so I
re-ran the full check myself directly against `api.crossref.org` for all 28 DOI-bearing entries rather than
rely on the agent's pass. The table below is my own direct-fetch result.

**Result: every DOI resolves to a real work correctly matched by title, journal, year, and general content —
no fabricated or mismatched citations, as round 1 also found. But 8 of 31 entries have author-name errors:
21 individual field-level corrections, including two entries that omit a real co-author entirely.**

| Key | Field | Bib currently has | CrossRef record | Note |
|---|---|---|---|---|
| `carvalho2025scoping` | author 1 | Carvalho, Louise C. | **Carvalho, Laura C.** | |
| `siegel2023psychedelic` | author 1 | Siegel, Jacob S. | **Siegel, Joshua S.** | |
| `siegel2023psychedelic` | author 2 | Daily, Julia E. | **Daily, James E.** | agent's pass missed this one |
| `gorman2021psychedelic` | author 4 | Cassidy, Kellianne | **Cassidy, Ksenia** | |
| `pilecki2021ethical` | author 4 | Rhea, Jason | **Rhea, Joseph** | |
| `dutton2025harm` | author 1 | Dutton, Charlotte | **Dutton, Carissa** | |
| `dutton2025harm` | author 4 | Oliva, Jamie | **Oliva, Jessica** | |
| `teixeira2026ayahuasca` | author 3 | Amaro, Hugo D. | **Amaro, Helena D.** | |
| `teixeira2026ayahuasca` | author 5 | Carvalho, Louise C. | **Carvalho, Laura C.** | same person as above; agent's pass missed this occurrence |
| `teixeira2026ayahuasca` | author 10 | Kohek, Mauricio | **Kohek, Maja** | |
| `ruffell2021ceremonial` | author 3 | Tsang, Wesley | **Tsang, WaiFung** | |
| `ruffell2021ceremonial` | author 4 | Davies, Molly | **Davies, Merlin** | |
| `ruffell2021ceremonial` | — | *(absent)* | **insert "Inserra, Antonio" between Davies and Butler** | co-author omitted entirely |
| `ruffell2021ceremonial` | author (was 5) | Butler, Marilyn | **Butler, Matthew** | |
| `nayak2023naturalistic` | author 5 | So, Suzanne | **So, Sara** | |
| `nayak2023naturalistic` | author 6 | Yaffe, Alyssa | **Yaffe, Abigail** | |
| `nayak2023naturalistic` | author 7 | Zaki, Hanaan | **Zaki, Hadi** | |
| `nayak2023naturalistic` | author 8 | Brasher, Theodore J. | **Brasher, Trey J.** | |
| `nayak2023naturalistic` | author 9 | Lowe, Manoj X. | **Lowe, Matthew X.** | agent's pass missed this one |
| `nayak2023naturalistic` | author 10 | Jolly, Deborah R. P. | **Jolly, Del R. P.** | agent's pass missed this one |
| `nayak2023naturalistic` | — | *(absent)* | **insert "Jackson, Heather" between Johnson and Garcia-Romeu** | co-author omitted entirely (distinct from "Jackson, Hillary," the 2nd author, already correct) |

The remaining 23 entries are confirmed correct as-is, including every journal name, volume, issue, page range,
and year (round 1's non-author-name fixes all hold up), and both non-DOI legal-statute entries and the
master's-thesis entry (re-checked against their primary sources).

**Pattern worth naming:** every defective entry is a recent (2020–2026), multi-author, non-Puerto-Rico-specific
paper. The four older Puerto Rico–specific entries (Koss, Comas-Díaz, Bird & Canino, Zerrate et al.) and the
two legal statutes are all still fully correct, as they were in round 1. The specific errors — Ksenia→Kellianne,
Joshua→Jacob, Laura→Louise, Sara→Suzanne, Hadi→Hanaan — read as plausible-sounding substitutions rather than
random corruption, consistent with round 1's Pass 3 finding of a similar pattern in the 6 defects it caught.
This suggests whatever process populated these particular entries did not read every author name off a
verified source, and a fully independent field-by-field check (as done here) is worth repeating for any future
references added the same way.

**Proposed disposition:** apply all 21 corrections above directly to `references.bib`. Mechanical, no judgment
calls.

### 3a-ii. Orphan bibliography entry

`teixeira2026ayahuasca` is defined in `references.bib` but **never cited** in `v3_draft.tex` or
`supplement.tex`. `sources/search_20260813_comparator_demographics_R8.md` documents that it was deliberately
kept "for design analogy" after its demographic data proved unusable for the numeric comparator table — but
that intent was never carried through to an actual `\citep{teixeira2026ayahuasca}` in the text. This also
means round 1's Pass 3 claim ("all 26 keys are both defined and cited") was true for the 26 it checked but was
never re-verified after the 5 references added later in round 1 (R-refs), one of which turned out to be
orphaned.

**Proposed disposition:** add a citation to `teixeira2026ayahuasca` in Discussion §4.1, alongside the existing
comparator-cohort sentence (`kopra2023investigation`, `robinson2026field`), since it is itself a closely
analogous naturalistic ayahuasca-ceremony-attender survey published in the same target journal — exactly the
kind of company round 1's Pass 2 (R1) said this paper should be keeping. One clause, no new word-count pressure
beyond a single citation key.

### 3a-iii. Online-First pagination recheck

Re-checked all 5 flagged entries directly against CrossRef as of 2026-08-14 (one day after round 1's check).
**All 5 remain unpaginated** — no volume, issue, or page assignment for any of them yet. No `.bib` changes
needed; existing `note` fields stating "Online First... not yet assigned as of 2026-08-13" remain accurate to
within a day and don't need re-dating. This still needs a final recheck immediately before actual submission,
as round 1 already flagged.

## 3b. Number tracing — independent recomputation from raw data

A background agent rebuilt essentially the entire manuscript's numeric content from
`data/results_7_15_2026.xlsx` using the project's own low-level statistical primitives (not the
manuscript-specific report-generation code, to keep the check independent) and reported that **every count,
base, test statistic, p-value, q-value, effect size, and confidence interval reproduced exactly** except the
two median transcription errors reported as R2-3 above (which I independently re-derived by hand and
confirmed). This includes a full re-derivation of all four BH-corrected test families, the proportional-odds
model (including tracing the n=63→n=62 complete-case drop to a single respondent missing both age and trust),
both reliability coefficients, the duplicate-adjudication and attention-check counts, and the qualitative
corpus counts.

This is a stronger result than round 1's Pass 3b, which found four discrepancies in v2; v3 has two, both
minor and already isolated to prose sentences rather than tables. It's a reasonable signal that the
`make_figures.py`/table-generation pipeline itself is solid, and that remaining errors are concentrated in
hand-written summarizing prose rather than in the analysis.

## 3c. Journal-requirements compliance

Re-checked against `JOURNAL_REQUIREMENTS.md`:

| Requirement | Status |
|---|---|
| Abstract unstructured, ≤200 words | **199 words** (naive word-split; corrects a rougher LaTeX-token count that suggested 201), unstructured ✅ |
| Introduction–Discussion ≤ 4,000 words | **~4,295** (citations excluded, the generous convention) — ❌ **not compliant**, see R2-1 |
| Keywords 4–6 | 6 ✅ |
| Chicago author-date | `natbib` + `chicago.bst`, compiles clean (30 pp., verified by a fresh `pdflatex` run this session) ✅ |
| 12 pt, double-spaced, 1-inch margins, numbered pages, line numbers | ✅ |
| Figures ≥ 300 dpi colour | 600 dpi ✅; visually inspected all four this session — no overlap, mislabeling, or layout defects ✅ |
| American spelling | ✅ no British-spelling instances found (round 1's "labelled" fix holds; re-swept both `.tex` files and the STROBE checklist) |
| Bibliography integrity | ❌ 8/31 author-name errors (3a), 1 orphan entry (3a-ii) — see above |
| BibTeX build | Clean except the 4 expected "no number and no volume" Online-First warnings (a 5th, `teixeira2026ayahuasca`, throws no warning because it is never cited — a symptom of 3a-ii, not a separate defect) |

---

# Consolidated disposition table

All rows applied in `v4_draft.tex` / `supplement.tex` / `references.bib` on 2026-08-14. None required new
author policy judgment (unlike round 1) — each had one clearly lower-risk option.

| # | Severity | Finding | Disposition |
|---|---|---|---|
| R2-1 | Major | Body still ~295–400 words over the JPD's verbatim 4,000-word cap | ☑ Applied. Trimmed Methods, Results, and (lightly) Introduction/Discussion by referencing tables/figures instead of repeating their numbers in prose, tightening the Conclusion (which largely restated the Abstract), and compressing several non-caveat clauses. Measured **3,947 words** (citations excluded), down from 4,295. Every round-1 disclosure sentence is intact — nothing was cut for content, only for redundant restatement |
| 3a | Major | 8/31 references have author-name errors (21 fields), incl. 2 entries missing a co-author entirely | ☑ Applied. All 21 corrections made to `references.bib`; recompiled and visually confirmed both Antonio Inserra (`ruffell2021ceremonial`) and Heather Jackson (`nayak2023naturalistic`) now render correctly in the bibliography |
| R2-2 | Moderate | Methods §2.5 incorrectly claims the four BH-correction families share no variables; `non_con_contact` (×7) and `screening_quest` (×6) each recur across 3 families | ☑ Applied (option a). Corrected in both `v4_draft.tex` §2.5 **and** `supplement.tex` §S3, which repeated the same incorrect claim in its own preamble — caught during the PDF visual-formatting pass, not in the original three-pass review; both now state the two variables recur across families and that this doesn't bound their error rate, with no q-value affected |
| 3a-ii | Moderate | `teixeira2026ayahuasca` defined but never cited | ☑ Applied. Cited in the Introduction alongside `carvalho2025scoping` as one of the few existing survey-level descriptions of ceremonial practice elsewhere, rather than in §4.1's numeric comparator sentence (its demographics were never verified for numeric use — see `sources/search_20260813_comparator_demographics_R8.md`) |
| R2-3 | Minor | Two prose numbers don't match their own tables (comfort/safety median claimed 3 for an n=2 subgroup that's actually 2.0; legal-worry median claimed 2, actually 1.5) | ☑ Applied. §3.4 now attributes median 3 only to the two characterizable subgroups (n=54, n=8) and states the n=2 subgroup is too small to characterize; Supplement §S3 now states median 1.5 |
| R2-4 | Minor | The one nominally-significant bivariate result (trust × facilitator background) lacks the permutation-based check applied elsewhere; its thinnest group is n=3, not n=4 as Table 3's category count would suggest (one of the 4 has a missing trust score) | ☑ Applied. Computed directly (10,000 permutations, seed 20260715): $p=0.010$, slightly reinforcing the asymptotic $p=0.017$. Added to §3.4 and Supplementary Table S4 with a $\ddagger$ marker |
| R2-5 | Minor | "De-identified" (Data availability) vs. "anonymous" (Methods) terminology inconsistency | ☑ Applied. Changed to "anonymous survey data"; does not touch the repository/DOI choice, left as-is per your instruction |
| 3a-iii | — | Online-First pagination recheck | ☐ No `.bib` change needed — all 5 still unpaginated as of 2026-08-14. Re-check immediately before submission, as round 1 also flagged |
