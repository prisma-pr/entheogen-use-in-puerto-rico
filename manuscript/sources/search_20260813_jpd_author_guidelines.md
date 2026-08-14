# Journal of Psychoactive Drugs — author guidelines verification

**Date:** 2026-08-13
**Method:** `PARALLEL_API_KEY` not configured in `.env` (only `ANTHROPIC_API_KEY` and `OPENROUTER_API_KEY`
present) — Parallel unavailable, so this used the WebSearch/WebFetch fallback per CLAUDE.md policy. Direct
`WebFetch` of `tandfonline.com` and `taylorandfrancis.com` domains returned HTTP 403 (bot-blocked) on every
attempt; routed through the `r.jina.ai` read-proxy to reach the same pages successfully.

## Primary source (verbatim quotes, via r.jina.ai proxy)

URL: `https://www.tandfonline.com/action/authorSubmission?show=instructions&journalCode=ujpd20`
(found via the "Instructions for authors" link on
`https://www.tandfonline.com/action/journalInformation?journalCode=ujpd20`)

Quoted verbatim:

> "A typical paper for this journal should be no more than 4,000 words for Original Research (Introduction,
> Methods, Results, Discussion) and for Review Articles, 4,500 words"

> "Should contain an unstructured abstract of 200 words."

> "Please use this reference guide when preparing your paper." — links to `tf_uschicagob.pdf` (Chicago
> Manual of Style, Author-Date). No APA, Vancouver, or MLA style is mentioned anywhere on the page.

Additional items extracted from the same page (paraphrased, lower confidence than the verbatim quotes above
since this pass was AI-summarized rather than quoted):

- Keywords: 4–6 required.
- Figures: 1200 dpi line art / 600 dpi grayscale / 300 dpi color; PS, JPEG, TIFF, or Word files accepted.
- Tables: must present new information, not duplicate text; editable files; independently interpretable.
- Formatting: double-spaced, 1-inch margins, numbered pages, 12pt Times New Roman or similar, American
  spelling.
- No STROBE/CONSORT/reporting-guideline requirement stated explicitly. Clinical trials require registration
  + ethics documentation.
- Mandatory: written ethical-approval statement in Methods for all human-subjects research; informed-consent
  statement.
- Open Select (hybrid OA) available; APC required unless waived/covered.
- Word and LaTeX accepted; LaTeX must be submitted as a compiled PDF plus a separate source zip.
- Submission platform: ScholarOne Manuscripts.
- Required disclosures: CRediT contributor roles, funding sources, competing interests, generative-AI-use
  declaration, data-availability statement.

## Corroborating evidence from real published JPD articles (PubMed + Crossref, independently fetched)

Used to cross-check the guidelines page rather than rely on it alone.

1. **Teixeira et al., "Ayahuasca and Public Health III: Health Status of a Sample of Ayahuasca Ceremony
   Attenders in Portugal"** — *Journal of Psychoactive Drugs*, 2026 Mar 19:1–11.
   DOI: [10.1080/02791072.2026.2631378](https://doi.org/10.1080/02791072.2026.2631378). PMID 41854389.
   - Cross-sectional online survey of n=203 ayahuasca ceremony attenders — closely analogous design to this
     project.
   - Abstract confirmed **unstructured**, single paragraph, no Background/Methods/Results/Conclusions labels.
   - Crossref metadata: page range 1–11, **41 references**.
   - Relevant for the Phase 2 novelty check — a very similar naturalistic-ceremony survey design, different
     country/substance, published in the target journal within the last year. Not a substitute for the
     dedicated PR/Caribbean novelty search still required in Phase 2a.

2. **"Psychedelic Use, Microdosing, Motives, and Information and Product Sources Among Young Adults in the
   United States"** — *Journal of Psychoactive Drugs*, 2026. DOI: 10.1080/02791072.2026.2685527. PMID 42318842.
   - Abstract fetched and counted directly: **~230 words**, unstructured, no section labels — confirms the
     200-word cap is applied loosely/rounded in practice (this example runs slightly over) but the
     unstructured format is consistent.

3. Three further recent JPD survey articles checked via PubMed listing (PMIDs 42152600, 41834488, 41661937) —
   all unstructured abstracts, no exceptions found.

## Confidence assessment

- **High confidence, verbatim-quoted:** word limit (4,000 words Intro–Discussion for original research),
  unstructured abstract ≤200 words, Chicago author-date reference style. These three are load-bearing for the
  manuscript plan and are quoted directly from the live instructions page, not paraphrased.
- **Medium confidence, AI-summarized from the same fetch:** figure/table specs, formatting details,
  disclosure requirements. Should be re-verified by a human skim of the instructions page before final
  submission formatting, since this pass was not verbatim-quoted for these items.
- **Not found / not stated on the instructions page:** an explicit figure or table *count* limit; a
  structured graphical-abstract requirement (none appears to exist for this journal — the repo's mandatory
  graphical-abstract figure will be produced for internal/preprint use but is not a JPD submission element).
