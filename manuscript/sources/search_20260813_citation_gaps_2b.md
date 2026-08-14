# Phase 2b — Six Introduction citation-gap searches

**Date:** 2026-08-13. **Method:** Parallel/Perplexity unavailable (no API key in repo `.env`); used
NCBI E-utilities (PubMed esearch/esummary/efetch), Semantic Scholar Graph API, CrossRef API (all
keyless), and WebSearch as fallback per CLAUDE.md policy. All entries below cross-checked against at
least two sources (PubMed metadata + CrossRef DOI resolution) before entering `references.bib`.

## Gap 1 — Growth of non-clinical ceremonial and retreat-based psychedelic use in the Americas
Queries: WebSearch `"growth expansion ayahuasca retreat centers tourism Americas psychedelic ceremony
trend review"`; Semantic Scholar `growth non-clinical ceremonial retreat psychedelic use Americas`.
Resolved via `golden2022effects` (set/setting scoping review) and `carvalho2025scoping` (see Gap 2),
which both document the retreat/naturalistic-use expansion empirically rather than relying on trade-press
sources (psychedelic-retreat marketing sites, travel journalism) that surfaced heavily in general
WebSearch results but are not citable academic evidence.

## Gap 2 — Asymmetry between clinical-trial and naturalistic/ethnographic psychedelic literatures
Queries: WebSearch `"asymmetry clinical trial naturalistic ethnographic psychedelic research literature
gap"`; PubMed `psychedelic decriminalization policy United States` (cross-reference sweep).
Resolved via `carvalho2025scoping` (JPD 2025 — the target journal itself, directly on point: scoping
review documenting the naturalistic/clinical divide), `hughes2024ethnoracial` (systematic review showing
clinical-trial samples are narrower than real-world use populations), `marcus2026psychedelics`
(explicitly synthesizes population/survey/observational vs.\ clinical-trial evidence and calls for more
survey-level research).

## Gap 3 — Puerto Rico's legal status and controlled-substance framework
Queries: WebSearch `"Controlled Substances Act Puerto Rico territory federal drug law psychedelics
decriminalization"`; WebSearch `"legal status classic psychedelics United States Schedule I Controlled
Substances Act review policy territories"`; PubMed `psychedelic decriminalization policy United States`.
Resolved via the two primary legal sources (`uscongress1970csa` — 21 U.S.C. §812; `pr1971csa` — Ley
Núm. 4 de 1971, 24 L.P.R.A. §2101 et seq., confirmed via LexJuris/OGP Puerto Rico official statute text),
plus `siegel2023psychedelic` (JAMA Psychiatry 2023, peer-reviewed review of the federal/state legislative
landscape psychedelics sit within). PR statute citation cross-checked against two independent PR
government-adjacent sources (LexJuris, Oficina de Gerencia y Presupuesto virtual library) after
`law.justia.com` returned HTTP 403.

## Gap 4 — Traditional plant-based and spiritually framed healing practice in Puerto Rico / Hispanic Caribbean
Queries: WebSearch `"espiritismo curanderismo traditional plant-based spiritual healing Puerto Rico
Hispanic Caribbean"`; PubMed `espiritismo Puerto Rico spiritual healing`; PubMed `"Puerto Rico" AND
(curanderismo OR "folk healer" OR "traditional healer" OR espiritismo)`.
Resolved via four PubMed-indexed, peer-reviewed sources spanning 1980–2022: `koss1980therapist`
(the classic study of PR's therapist-spiritist public-health integration project), `comasdiaz1981puertorican`,
`bird1981sociopsychiatry` (child-psychiatric-population study of espiritismo in PR), and
`zerrate2022espiritismo` (contemporary follow-on study by an overlapping author, PMID 35016702, 41 years
later — demonstrates the practice's documented continuity into the present).

## Gap 5 — Absence of prior Puerto Rico–specific survey evidence
Satisfied by the dedicated Phase 2a novelty check
([`search_20260813_novelty_check_pr_caribbean.md`](search_20260813_novelty_check_pr_caribbean.md)), not
a citation lookup. Resolved with author sign-off 2026-08-13: narrow the novelty claim to ceremonial/
facilitated multi-substance practice, citing `velezrodriguez2026psilocybin` and
`doeltermorales2020hongos` explicitly as prior PR-specific but narrower-scope work.

## Gap 6 — Harm-reduction, preparation, and screening frameworks in psychedelic settings
Queries: WebSearch `"harm reduction screening preparation framework psychedelic ceremonial guided session
facilitator"`; PubMed `"Psychedelic Harm Reduction and Integration: A Transtheoretical Model"`; PubMed
`"Ethical and legal issues in psychedelic harm reduction and integration therapy"`; PubMed `"Harm
reduction practises for users of psychedelic drugs: a scoping review"`.
Resolved via `gorman2021psychedelic` (the field's standard harm-reduction/integration transtheoretical
model, Frontiers in Psychology, 1,000+ citations at time of search), `pilecki2021ethical` (ethics/legal
framework for harm-reduction practice), `dutton2025harm` (2025 scoping review, current state of the
field), and `kruger2023preferences` (JPD 2023 — what psychedelic users themselves report wanting from
screening/preparation practice, directly comparable to this study's `prep_part`/`screening_quest` items).
No PubMed-indexed paper specifically on facilitator *credentialing* in non-clinical settings was found
(search returned zero hits); this sub-topic is covered qualitatively by the three harm-reduction papers
above rather than a dedicated credentialing-specific citation — flagged here rather than forcing a weak
citation.
