# JPD figure/table count limit — verification

**Date:** 2026-08-25
**Question:** Does the Journal of Psychoactive Drugs impose a hard limit on the number of figures or
tables? Asked because v6 now carries 5 tables + 4 figures after the supplement was folded in.

**Method:** `PARALLEL_API_KEY` still not configured, so WebSearch/WebFetch fallback per CLAUDE.md
policy. Direct `WebFetch` of `tandfonline.com` returned HTTP 403 on both the legacy
`action/authorSubmission` path and the newer `journals/ujpd20/for-authors` path; routed through the
`r.jina.ai` read-proxy, the same method the 2026-08-13 guidelines fetch used.

---

## Answer: no count limit exists

Two independent fetches of the live instructions page
(`https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=ujpd20`), on
2026-08-13 and again today, both report **no maximum number of tables or figures anywhere on the
page**, and no page-extent limit on display items. Today's fetch, asked the question directly:

> "No maximum number of tables or figures is specified anywhere on this page."

The page states only *specifications* for display items, not counts: 1200 dpi line art / 600 dpi
grayscale / 300 dpi colour; tables must present new information rather than duplicate the text, be
editable, and be independently interpretable.

## A near-miss worth recording

A WebSearch for this question surfaced, as its top result, an "Instructions to Authors" page carrying
exactly the rule being looked for:

> "Tables and figures should comprise no more than a total of 5 double-spaced manuscript pages."
> "Word limits exclude the abstract, references, tables and figures."

**That page is not JPD.** Fetching it (`https://pmc.ncbi.nlm.nih.gov/articles/PMC6691792/`) identifies
it as the *Journal of the Canadian Academy of Child and Adolescent Psychiatry*, published by the
Canadian Academy of Child and Adolescent Psychiatry. The search engine conflated two journals'
author instructions. Had this been taken at face value it would have imposed a hard limit JPD does
not have — and one the current manuscript would violate. Verify the journal identity on any
instructions page reached through search, not just the quoted rule.

## Word limit: what it does and does not say

Verbatim, confirmed identically on both fetch dates:

> "A typical paper for this journal should be no more than 4,000 words for Original Research
> (Introduction, Methods, Results, Discussion) and for Review Articles, 4,500 words"

Asked explicitly whether the page states what the count includes or excludes, today's fetch returned:

> "The page does **not** specify what the word count includes or excludes. It provides no
> clarification regarding whether abstracts, references, tables, figures, or other elements are
> counted toward these limits."

So the working assumption that table content sits outside the 4,000 words rests entirely on the
parenthetical scoping the limit to four named prose sections. That is a reasonable reading and the
only one available, but it is an inference, not a stated rule. Note also the softening verb —
"a typical paper *should be* no more than" — which is guidance, not a hard cap.

## Empirical check: what published JPD papers actually carry

Three recent JPD original-research articles, counted from PMC full text:

| Article | Tables | Figures | Total | Supplementary? |
|---|---|---|---|---|
| PMC13053045 — naturalistic psychedelic use among gender/sexual minorities | 3 | 1 | 4 | no |
| PMC12092733 — adult-use legalization and medical cannabis patients (mixed methods) | 5 | 0 | 5 | yes (survey instrument, via OSF) |
| PMC13220840 — lifetime hallucinogen use and valvular heart disease | 3 | 1 | 4 | yes (Supplemental Table S1) |

Typical load is **4–5 display items**. The current manuscript's **9** is roughly double the norm.

Two of the three use supplementary material, so eliminating it is not a JPD convention either —
supplemental files are published via Figshare and the instructions actively encourage them
("Supplemental material can be videos, filesets, audio files, or anything that supports (and is
pertinent to) your paper").

## Bottom line

- No hard limit exists. Nine display items cannot be rejected on a stated rule.
- Nine is still about twice what JPD papers typically run, so it is a plausible desk-edit or reviewer
  comment, not a compliance failure.
- The word-count exclusion for tables is an inference from a parenthetical, not a stated rule. If
  precision matters before submission, one email to the editorial office settles both this and the
  display-item question at once.

## Sources

- [JPD instructions for authors](https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=ujpd20) (via r.jina.ai read-proxy; direct fetch 403)
- [PMC6691792 — J. Can. Acad. Child Adolesc. Psychiatry instructions](https://pmc.ncbi.nlm.nih.gov/articles/PMC6691792/) (the misattributed result)
- [PMC13053045](https://pmc.ncbi.nlm.nih.gov/articles/PMC13053045/), [PMC12092733](https://pmc.ncbi.nlm.nih.gov/articles/PMC12092733/), [PMC13220840](https://pmc.ncbi.nlm.nih.gov/articles/PMC13220840/)
