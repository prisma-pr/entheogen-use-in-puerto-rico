# Journal of Psychoactive Drugs — live requirements re-verification (2026-09-08)

Method: Parallel Web `search` worked (`manuscript/sources/search_20260908_*.md`); Parallel `extract` failed
in this environment with `Error: 'BetaResource' object has no attribute 'extract'` (a version mismatch
between the installed `parallel-web` 1.3.3 SDK and the script's call signature — reinstalling the package
did not fix it). Direct `WebFetch` of `tandfonline.com` and `authorservices.taylorandfrancis.com` returned
HTTP 403 (bot-blocked) on every attempt, as it did in the 2026-08-13 pass. Fell back to `WebFetch` through
the `r.jina.ai` read-proxy for the two page-level fetches below, per the project CLAUDE.md's fallback
instruction — noting this explicitly since it departs from "Parallel for all web work."

Primary source re-fetched: `https://r.jina.ai/https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=ujpd20`
(same live JPD "Instructions for Authors" page checked 2026-08-13), fetched twice with different
extraction prompts to cover all fields. Secondary source: Parallel `search` (model=base) for the
generative-AI disclosure wording and cover-letter/reviewer/title-page questions the primary page does not
address explicitly.

## Diff-style table

| Requirement | Previously recorded (`JOURNAL_REQUIREMENTS.md`) | Live value (2026-09-08) | Changed? | Source |
|---|---|---|---|---|
| Word limit (Intro–Methods–Results–Discussion) | 4,000 words, verbatim | Same, verbatim: "no more than 4,000 words for Original Research (Introduction, Methods, Results, Discussion)" | No | JPD instructions page (jina proxy) |
| Abstract | Unstructured, ≤200 words, verbatim | Same, verbatim: "unstructured abstract of 200 words" | No | JPD instructions page |
| Reference style | Chicago Manual of Style, Author-Date | Same — page still links the Chicago author-date reference guide; no APA/Vancouver/MLA mentioned | No | JPD instructions page |
| **Peer review model** | **Not previously determined** — `JOURNAL_REQUIREMENTS.md` is silent on this | **Single-anonymized.** Verbatim from the JPD page: "single anonymous peer reviewed by two independent, anonymous expert" reviewers. No mention of double-blind review or author-identity masking anywhere on the page. Corroborated independently by a Parallel search of Taylor & Francis's general editorial-policies page, which also states T&F journals in this class default to single-anonymous review. | **New finding** — was an open question | JPD instructions page (fetched twice, consistent both times); Parallel search of `authorservices.taylorandfrancis.com/editorial-policies/` |
| Title page / author masking | Not addressed | The JPD page states only "All authors of a manuscript should include their full name and affiliation on the cover page" — no instruction to omit author identity from the main file. Consistent with single-anonymized review: no masking is required. | New finding (consistent with peer-review finding) | JPD instructions page |
| Keywords | 4–6 | Not re-confirmed this pass (not covered by either fetch); no reason to believe it changed | Unconfirmed, carried over | — |
| Figures | 1200 dpi line art / 600 dpi grayscale / 300 dpi color; PS, JPEG, TIFF, or Word | Same, verbatim confirmed again: "PS, JPEG, TIFF, or Microsoft Word formats," figures "saved separately from the text" | No | JPD instructions page |
| Tables | Must add new information, editable, independently interpretable | Not re-confirmed this pass; no reason to believe changed | Unconfirmed, carried over | — |
| Reporting guideline (STROBE) | Not mandated | Not re-confirmed this pass; no mention found in either fetch | Unconfirmed, carried over | — |
| Ethics statement | Mandatory | Not re-confirmed this pass | Unconfirmed, carried over | — |
| **Cover letter** | Not previously recorded | The JPD-specific instructions page does not mention cover-letter content requirements. A Parallel search (lower-confidence "base" model, sources returned were partly off-target — a Wiley journal and an unrelated soil-science PDF, not JPD-specific) suggests the general T&F/ScholarOne pattern: cover letter uploaded as its own file, visible only to the editor, used to state submission type and any special declarations. Treated as **T&F house convention, not confirmed JPD-specific text** — flagged accordingly in the cover letter I drafted. | New, low-confidence | Parallel search (see caveat) |
| **Suggested reviewers** | Not previously recorded | Not mentioned on the JPD instructions page itself. ScholarOne's standard submission workflow (used by essentially all T&F ScholarOne journals) prompts for suggested-reviewer name/affiliation/email at the "Reviewers" step; JPD's page does not state it is mandatory or optional specifically. Treated as **likely present in the ScholarOne workflow but not confirmed as a JPD-specific requirement** from the page itself. | New, low-confidence | Parallel search + general ScholarOne convention |
| **Running head** | Not previously recorded | No character/word limit stated on the JPD instructions page. Only requirement found: full author name and affiliation on the cover page. | New (negative finding — no limit found) | JPD instructions page |
| **ORCID** | Not previously recorded | Optional: "Where available, please also include ORCiDs." | New | JPD instructions page |
| **Data availability statement** | Listed as a required disclosure, not detailed | Confirmed and detailed: JPD applies a "Basic Data Sharing Policy," authors are asked at submission whether a dataset is associated with the paper and encouraged to cite it | Detail added | JPD instructions page |
| **Supplementary material** | Not previously recorded | JPD accepts supplementary material ("videos, filesets, audio files, or anything that supports... your paper") published via Figshare — text-only supplementary tables/sections were not explicitly addressed, but nothing excludes them | New | JPD instructions page |
| **Generative-AI declaration wording/placement** | Listed only as "required," no wording given | T&F's general AI policy (not JPD-specific — no JPD-specific override found) requires the declaration to name the **specific tool and version**, describe **how** and **why** it was used, placed in the **Methods or Acknowledgments** section (or a dedicated AI-use statement section, as the journal specifies — JPD's own page does not name a specific section). If AI was *not* used, suggested wording is "The authors report generative AI was not used in their research or preparation of this manuscript." AI tools must not be listed as authors. | Detail added | Parallel search of `taylorandfrancis.com/our-policies/ai-policy` and related T&F pages |
| Open access / APC | Hybrid (Open Select), APC finder | Not re-confirmed this pass | Unconfirmed, carried over | — |
| Submission format | Word or LaTeX; LaTeX as compiled PDF + separate source zip | Reconfirmed, with more detail: LaTeX files must be "converted to PDF beforehand" for the manuscript upload, source files uploaded separately as a zip | Detail added, otherwise unchanged | JPD instructions page |
| Submission platform | ScholarOne Manuscripts | Same | No | JPD instructions page |
| Required disclosures | CRediT, funding, competing interests, AI-use, data availability | Same, with CRediT detail added: "Submitting authors should be prepared to submit CRediT roles for themselves and their co-authors" | Detail added | JPD instructions page + Parallel search |

## What this changes for the submission package

Because JPD uses **single-anonymized** review (reviewers see author identity; authors do not see
reviewers), **no masking of the main manuscript file is required**. `v7_draft.tex` / `v7_draft.pdf` can be
submitted with author names, affiliations, acknowledgments, funding, and competing-interest text intact —
exactly as v7 already has them. I did not produce a masked version, since the live requirement does not
call for one; this is the "flag the decision" case named in the task brief, and the decision is: **do not
mask**, because the page states single-anonymous review twice, independently, in two separate fetches.

A separate title page is still worth producing (task 4) because JPD explicitly asks for full name and
affiliation "on the cover page" as a distinct concept from the manuscript body, and because ScholarOne's
metadata-entry step typically wants author/affiliation/corresponding-author data independent of the file
content — but it is a convenience/format-compliance page, not an anonymization requirement.

## Confidence caveats

- The cover-letter and suggested-reviewers rows rest on a Parallel `search` (not `extract`) call whose
  returned sources were partly mismatched to the query (a Wiley author-guidelines page and an unrelated
  agronomy-journal PDF appeared in the citation list rather than JPD- or T&F-specific pages). I am treating
  those two rows as **general T&F/ScholarOne convention, not a verified JPD-specific rule**, and said so in
  the cover letter and suggested-reviewers files.
- Parallel `extract` (URL-level extraction) is non-functional in this environment; every finding above that
  required page content came from `WebFetch` via the `r.jina.ai` proxy, not from Parallel. This should be
  flagged to whoever maintains the `parallel-web` skill — `pip install parallel-web` did not resolve the
  `'BetaResource' object has no attribute 'extract'` error.
