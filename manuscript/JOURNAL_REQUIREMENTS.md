# Journal of Psychoactive Drugs — verified requirements

Source: [`sources/search_20260813_jpd_author_guidelines.md`](sources/search_20260813_jpd_author_guidelines.md).
Every number below with "verbatim" next to it is quoted directly from the live instructions page; everything
else is AI-summarized from the same fetch and should get a human skim before final formatting.

## The two findings that change the plan

**1. Abstract must be rewritten — unstructured, not structured.**
JPD requires an **unstructured abstract, 200 words maximum** (verbatim). The current draft's abstract is
structured (Background/Methods/Results/Conclusions headers) and runs 249 words. Both the format and the
length change. Real JPD abstracts checked directly (PMID 42318842, ~230 words) suggest reviewers tolerate
modest overage, but the structured-header format has no exceptions in five recent JPD survey articles
checked — that part is firm.

**2. The manuscript body is already over the word limit before Phase 1 additions.**
JPD caps original-research articles at **4,000 words for Introduction–Methods–Results–Discussion combined**
(verbatim). The current draft's Introduction through Discussion is **4,674 words** (measured directly from
[`ceremonial_entheogen_pr_manuscript.md`](../ceremonial_entheogen_pr_manuscript.md) — script below), already
674 words over, before:
- Introduction citations are filled in (Phase 2 — adds length)
- Discussion is expanded with comparator literature (Phase 2c/3 — adds length)
- Methods gains recruitment/instrument detail (Phase 1 — adds length)

Net effect: something has to move to supplementary material or be cut, on top of what Phase 3 already
planned to move there. Candidates, in order of how little they cost the main narrative:
- Table 10 (full BH-correction-by-family detail) → supplement, keep only the headline q-values in text
- §3.5 facilitator self-report detail (n=8, already flagged as barely interpretable) → condense to one
  paragraph in text, full table in supplement
- §6-equivalent qualitative/psychometric material already slated for Limitations → trim further
- Table 6 (facilitator practice) and Table 9 (ordinal model) → supplement, reference from text

This is a **flag for the user**, not a decision made unilaterally: cutting ~700–1000+ words from a draft
that is already tight on necessary caveats (suppression floors, unlinked branches, exploratory framing)
risks losing exactly the qualifying language that keeps every claim honest. I'll propose specific cuts at
the start of Phase 3 for sign-off before applying them.

```python
# Reproducible word count check
text = open('ceremonial_entheogen_pr_manuscript.md', encoding='utf-8').read()
start = text.index('## 1. Introduction')
end = text.index('## 5. Limitations')
print(len(text[start:end].split()))  # -> 4674
```

## Full requirements table

| Requirement | Value | Confidence |
|---|---|---|
| Article type | Original Research | — |
| Word limit (Intro–Methods–Results–Discussion) | **4,000 words** | Verbatim |
| Abstract | **Unstructured, ≤200 words** | Verbatim |
| Reference style | **Chicago Manual of Style, Author-Date** (`tf_uschicagob.pdf`) — not APA, not Vancouver | Verbatim |
| Keywords | 4–6 | Summarized |
| Figures | 1200 dpi line art / 600 dpi grayscale / 300 dpi color; PS, JPEG, TIFF, or Word | Summarized |
| Figure/table count limit | Not stated | — |
| Tables | Must add new information, not duplicate text; editable, independently interpretable | Summarized |
| Page formatting | Double-spaced, 1-inch margins, numbered pages, 12pt Times New Roman or similar, American spelling | Summarized |
| Reporting guideline (STROBE etc.) | **Not mandated.** Keep the STROBE checklist as supplement anyway — reviewer-facing best practice for a cross-sectional survey, per plan Phase 3 | Summarized |
| Ethics statement | Mandatory written ethical-approval statement in Methods + informed-consent statement | Summarized |
| Graphical abstract | Not a JPD submission element | Inferred (not found) |
| Open access | Hybrid (Open Select), APC via APC finder tool | Summarized |
| Submission format | Word or LaTeX (LaTeX submitted as compiled PDF + separate source zip) | Summarized |
| Submission platform | ScholarOne Manuscripts | Summarized |
| Required disclosures | CRediT roles, funding, competing interests, generative-AI-use declaration, data-availability statement | Summarized |

## Consequence for Phase 3 section allocations (supersedes the table in MANUSCRIPT_PLAN.md)

- Abstract: rewrite unstructured, target 180–200 words, written last as planned.
- Everything currently itemized for supplementary material in the plan is now **required**, not optional,
  to have any room for the Phase 2 citations and expanded Discussion within 4,000 words.
- `references.bib` and in-text citations must render in **Chicago author-date**, not APA. This changes the
  `citation-management` skill's output format and the LaTeX bibliography package choice (see template note
  below).

## LaTeX toolchain note

No `pdflatex`/`latexmk`/`kpsewhich` found on PATH in either the Bash or PowerShell environment during this
check. Compilation approach (Phase 6) needs verification before that phase starts — whatever mechanism the
other skills in this repo normally use to produce `outputs/report.pdf` should be reused rather than assuming
a local TeX install exists. Not a Phase 0 blocker.

For the reference style itself: `natbib` + `chicago.bst` (the classic "Chicago" BibTeX style, author-date)
is the more portable choice if a full TeX Live install is available wherever compilation happens;
`biblatex-chicago` (`style=authordate`) is the modern equivalent if `biber` is available. The template below
defaults to `natbib`+`chicago.bst` with the `biblatex-chicago` alternative commented out, since it has fewer
moving parts. This should be confirmed against whatever the compile step actually has installed before
Phase 6.
