# Submission checklist — Journal of Psychoactive Drugs (ScholarOne)

Manuscript: *Ceremonial Entheogen Use in Puerto Rico: A Descriptive Survey of Participants and a Small
Facilitator Subsample*. Package assembled 2026-09-08. Peer-review model confirmed live: **single-anonymized**
(reviewers see author identity; authors do not see reviewer identity) — see
`manuscript/JOURNAL_REQUIREMENTS_VERIFIED.md`. **No masking was applied to any file** as a result.

## File manifest and ScholarOne upload mapping

| # | File | Path | ScholarOne file type / field | Notes |
|---|---|---|---|---|
| 1 | Cover letter | `manuscript/final/cover_letter.md` / `.pdf` | "Cover Letter" | Editor name verified live (Dr. Caravella McCuistian) — reconfirm immediately before submission |
| 2 | Main manuscript, compiled PDF | `manuscript/final/manuscript_v7_compiled.pdf` | "Main Document" (PDF) | Freshly compiled this session from `v7_draft.tex` via TinyTeX `pdflatex`+`bibtex`; 0 errors, 0 undefined refs/citations, 0 overfull hboxes |
| 3 | Main manuscript, LaTeX source | `manuscript/drafts/v7_draft.tex` (unedited — the approved file) | Included in source zip, not uploaded standalone | Body text untouched throughout this task |
| 4 | LaTeX source bundle | `manuscript/final/submission_source.zip` | "LaTeX Source Files" (zip) | Contains `v7_draft.tex`, `v7_draft.bbl`, `references.bib`, and the 4 main-text figures (PNG; see row 7 for the TIFF submission copies) |
| 5 | Title page | `manuscript/final/title_page.tex` / (compile to PDF, or use `manuscript/final/title_page.pdf`) | "Title Page" (if ScholarOne wants a separate file) or transcribe into Step-1 metadata fields | Not required for anonymization (single-anon review) — produced because JPD's instructions separately ask for full name/affiliation "on the cover page." **See Blocked section: ORCIDs, phone, mailing address, and every co-author's email are placeholders** |
| 6 | STROBE checklist | `manuscript/final/STROBE_checklist.md` / `.pdf` | "Supplementary Material" or "Other" (JPD does not mandate STROBE; include as reviewer-facing good practice) | References corrected to v7's actual section/table numbers this session; two items downgraded from earlier drafts because supplement content was dropped — see the file's "Open items" |
| 7 | Figures, TIFF, 600 dpi | `manuscript/final/figures/Figure1.tif` … `Figure4.tif` | "Figure" (one per upload slot) | Converted from the 600 dpi source PNGs — a format conversion, not an upscale; 600 dpi exceeds JPD's 300 dpi color minimum for all four |
| 8 | Figure captions | `manuscript/final/figure_captions.md` | Captions typically entered directly in ScholarOne's per-figure caption field, or bundled at the end of the main document per JPD's own template convention | Copied verbatim from `v7_draft.tex`; also notes `graphical_abstract.png` exists in the repo but is **not** part of the approved manuscript (no `\includegraphics`/caption in v7) and is excluded here |
| 9 | Generative-AI-use declaration | `manuscript/final/ai_use_declaration.md` | Belongs in the manuscript body (Methods/Acknowledgments, or a dedicated AI-statement section) per general T&F policy — v7 already has a "Generative AI use declaration" section; this file's fuller wording is a drop-in replacement candidate, not yet applied to `v7_draft.tex` (body is not to be edited per the task brief) | Use this wording at the point of final submission-file assembly, or paste into ScholarOne's AI-declaration metadata field if the platform has one |
| 10 | References | `manuscript/references/references.bib` | Bundled in the source zip (row 4); not uploaded separately | Chicago author-date via `natbib`+`chicago.bst`, confirmed still the required style |
| 11 | Suggested reviewers | `manuscript/final/suggested_reviewers.md` | ScholarOne's "Reviewers" submission step (if prompted) | 6 candidates; **every email needs independent verification before entry** — see Blocked section |
| 12 | Supplement audit (internal, not for upload) | `manuscript/final/supplement_audit.md` | N/A — working document for the author | Confirms no supplement ships by default; documents what was dropped and why |
| 13 | Supplement, trimmed candidate (NOT part of default package) | `manuscript/final/supplement_submission.tex` / `.pdf` | "Supplementary Material" — **only if the author approves reinstating it** | Contains the 4 BH-correction family tables, the exploratory proportional-odds model, and the full psychometric reliability table. Compiles cleanly (0 errors) but is not wired into the checklist above by default |
| 14 | Data availability statement | Already in `v7_draft.tex` (unnumbered section after Discussion) | Answered in ScholarOne's data-availability prompt at submission | States data/code will be deposited on publication and are available from the corresponding author until then; **no DOI exists yet** — see Blocked |
| 15 | Journal-requirements re-verification record | `manuscript/JOURNAL_REQUIREMENTS_VERIFIED.md` | N/A — internal record | Diff table vs. the prior `JOURNAL_REQUIREMENTS.md`; single-anonymized finding is the headline change |
| 16 | Word-count check | `manuscript/wordcount.py` (script) + this report | N/A | 3,842/4,000 words Intro–Discussion; 199/200 abstract. **Compliant. No cuts applied or needed** |

## Suggested upload order (typical ScholarOne "Original Research" flow)

1. Cover letter (row 1)
2. Main manuscript PDF (row 2) — or the LaTeX zip if ScholarOne's Article Type accepts LaTeX-native
   upload; confirm at submission time which the portal expects as the primary file
3. Title page / metadata entry (row 5)
4. Figures, one per slot, in order (row 7), captions entered per JPD convention (row 8)
5. Supplementary material — STROBE checklist (row 6), and the trimmed supplement (row 13) only if approved
6. Source files (LaTeX zip, row 4) — usually a separate "source files" upload distinct from the reviewer-facing PDF
7. Any required metadata screens: CRediT roles, funding, competing interests, generative-AI declaration,
   data availability, suggested reviewers (rows 9, 11, 14)

## Blocked — needs Jean

Everything below is a placeholder, an unresolved verification, or something this pass could not complete.
Nothing in this list was fabricated to fill a gap.

### Placeholders in `title_page.tex`
- **Every author's ORCID iD** (`[ORCID: TBD]` × 8) — none found in any project file. ORCID is optional per
  JPD's live instructions, but locate and add for authors who have one.
- **Corresponding author's phone number and mailing address** — not present in any project source file.
- **Every co-author's email address** except `jean.velez5@upr.edu`. No other author's contact information
  exists anywhere in this repository.
- **Per-author CRediT taxonomy roles** (the 14-role formal taxonomy) — only the prose author-contributions
  statement exists; confirm whether ScholarOne requires the formal per-role breakdown and map it if so.
- **Acknowledgments text** — no acknowledgments beyond the funding/competing-interest/author-contribution
  statements were found in any file; add if the authors want specific acknowledgments recorded.

### Verification still needed
- **Editor name** (Dr. Caravella McCuistian) — verified live 2026-09-08 from the JPD journal-information
  page; reconfirm immediately before submission since editor terms can change.
- **Cover-letter and suggested-reviewer ScholarOne conventions** — the JPD-specific instructions page does
  not itself describe these; what I wrote follows general T&F/ScholarOne convention from a lower-confidence
  Parallel search whose returned sources were partly off-target (see `JOURNAL_REQUIREMENTS_VERIFIED.md`).
  Confirm against the live ScholarOne submission portal once a submission is actually opened.
- **All 6 suggested-reviewer email addresses** — none was confirmed by directly reading a page displaying
  it; see `suggested_reviewers.md` for the per-candidate confidence level. Verify each before entering into
  ScholarOne.
- **Running head, 48-character draft** (`title_page.tex`) — JPD's live instructions page states no
  character limit was found; the draft follows a common journal convention. Confirm against whatever limit
  ScholarOne's Step-1 metadata field actually enforces.
- **Keywords, table formatting rules, ethics-statement exact wording requirement, STROBE-mandate status** —
  carried over from the original `JOURNAL_REQUIREMENTS.md` without live re-confirmation this pass (not
  reached by either web fetch); low risk of having changed, but not independently re-verified 2026-09-08.

### Compilation and tooling caveats
- **Parallel `extract` (URL-level page reading) is non-functional** in this environment
  (`Error: 'BetaResource' object has no attribute 'extract'`, persists after `pip install parallel-web`).
  Every page-content finding in this pass came from `WebFetch` via the `r.jina.ai` proxy instead, per the
  project's stated fallback policy — flagged explicitly wherever it was used
  (`JOURNAL_REQUIREMENTS_VERIFIED.md`, cover letter, suggested reviewers).
- **LaTeX toolchain**: TinyTeX **is** installed and on PATH in this environment (`pdflatex`, `bibtex`,
  `xelatex`, `latexmk` all found under `AppData\Roaming\TinyTeX\bin\windows`), contrary to the prior
  `JOURNAL_REQUIREMENTS.md` note that none was found. `v7_draft.tex` was compiled this session
  (`pdflatex` → `bibtex` → `pdflatex` ×2) with **0 errors, 0 undefined citations/references, 0 overfull
  hboxes** — `manuscript/final/manuscript_v7_compiled.pdf` is a genuine fresh build, not a copy of the
  pre-existing `v7_draft.pdf` (both happen to be byte-identical in size, confirming reproducibility, not
  substituted). `title_page.tex` and `supplement_submission.tex` also compile cleanly after removing
  `\texttt{}` (the installed TinyTeX lacks the Courier/`pcr` font metrics needed for `\texttt` under the
  `times` package; `\textsf` was substituted — a purely mechanical fix, not a content change).
- **DOI for the data/code deposit** does not exist yet — `v7_draft.tex`'s Data Availability statement
  correctly says it will be recorded on publication; nothing to do before submission, but do not let this
  slip afterward.

### Not blocked (confirmed present, listed for completeness)
- IRB protocol number is present in `v7_draft.tex` Methods §2.1: OPPHIE 2509472552.
- No `UNCONFIRMED` markers remain anywhere in `v7_draft.tex` (author contributions, funding,
  competing interests, data availability, and generative-AI-use statements are all finalized text).
- Word count and abstract length are both compliant (3,842/4,000; 199/200) — no cuts were needed or applied.
