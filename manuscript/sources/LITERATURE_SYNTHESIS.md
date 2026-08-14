# Literature Synthesis — Phase 2

Thematic synthesis mapping every finding gathered in Phase 2 to the manuscript claim it supports, plus the
populated `manuscript/references/references.bib` (26 entries, all verified real papers/primary legal
sources with complete metadata or an explicit note on any missing field). Search logs:
[`sources/search_20260813_novelty_check_pr_caribbean.md`](search_20260813_novelty_check_pr_caribbean.md),
[`sources/search_20260813_citation_gaps_2b.md`](search_20260813_citation_gaps_2b.md),
[`sources/search_20260813_comparator_literature_2c.md`](search_20260813_comparator_literature_2c.md).

**Tool note:** `PARALLEL_API_KEY` and a Perplexity key are both absent from the repo `.env`, so the
`parallel-web`/`research-lookup` skills mandated by the root `CLAUDE.md` were unavailable for this
session. Per that file's own fallback policy, all searches used WebSearch/WebFetch plus direct, keyless
calls to NCBI E-utilities (PubMed), the Semantic Scholar Graph API, and the CrossRef API — every citation
below was independently cross-checked against at least two of these sources before entering
`references.bib`.

---

## 1. Novelty framing (hard gate — resolved with author 2026-08-13)

**Finding:** No prior published survey of *ceremonial/facilitated, multi-substance* entheogen use
practice in Puerto Rico exists. Two narrower PR-specific items do exist:

- `velezrodriguez2026psilocybin` — a companion output from this study's own research team (author-
  confirmed), single-substance (psilocybin), use-pattern/personality-correlate focus, no ceremonial or
  safety content.
- `doeltermorales2020hongos` — an unpublished 2020 UPR Río Piedras M.A. thesis on university-community
  *perceptions* of psilocybin mushrooms, not a use-practice survey.

**Manuscript consequence:** the Introduction's novelty claim narrows from "first survey of entheogen use
in Puerto Rico" to **"first survey specifically characterizing ceremonial/facilitated entheogen use
practices (preparation, screening, facilitator role, safety) in Puerto Rico."** The Introduction should
cite `velezrodriguez2026psilocybin` explicitly with a scope-distinguishing sentence (not leave the overlap
implicit), and cite `doeltermorales2020hongos` as supporting evidence of prior, narrower PR-specific
research interest in this space.

---

## 2. Introduction citation gaps (§1, all six markers)

| # | Gap | Citations | How it's used |
|---|---|---|---|
| 1 | Growth of non-clinical ceremonial/retreat-based use in the Americas | `golden2022effects`, `carvalho2025scoping` | Supports the claim that ceremonial practice has expanded largely outside clinical-trial infrastructure; academic sources chosen over trade-press/marketing sources that dominate general search results on this topic. |
| 2 | Asymmetry between clinical-trial and naturalistic/ethnographic literatures | `carvalho2025scoping`, `hughes2024ethnoracial`, `marcus2026psychedelics` | `carvalho2025scoping` is a scoping review in the target journal itself, published on exactly this asymmetry; the other two document narrower clinical-trial samples and call for more survey-level naturalistic evidence. |
| 3 | Puerto Rico's legal status and controlled-substance framework | `uscongress1970csa`, `pr1971csa`, `siegel2023psychedelic` | The two are primary legal sources (federal and territorial statutes) establishing the Schedule I framework Puerto Rico operates under; `siegel2023psychedelic` (JAMA Psychiatry) is the peer-reviewed review contextualizing that framework within the broader 2020s legislative-reform landscape. |
| 4 | Traditional plant-based/spiritually framed healing practice in PR | `koss1980therapist`, `comasdiaz1981puertorican`, `bird1981sociopsychiatry`, `zerrate2022espiritismo` | Four peer-reviewed sources spanning 1980–2022 documenting espiritismo/curanderismo as an actively practiced, clinically documented PR healing tradition — establishes the cultural context the Introduction claims without over-claiming continuity with ceremonial entheogen use specifically (the two practices are related context, not equated). |
| 5 | Absence of prior PR-specific survey evidence | See §1 above | Resolved as a literature-search obligation, not a citation lookup, per the plan's own framing. |
| 6 | Harm-reduction, preparation, and screening frameworks | `gorman2021psychedelic`, `pilecki2021ethical`, `dutton2025harm`, `kruger2023preferences` | `gorman2021psychedelic` is the field's standard harm-reduction/integration model; the other three establish the ethical/legal grounding and current state of screening/preparation practice this study's `prep_part`, `screening_quest`, and `emergency_plan` items can be read against. |

---

## 3. Discussion comparator literature (§4)

| Theme | Citations | How it's used |
|---|---|---|
| Naturalistic/community surveys with comparable descriptive profiles | `teixeira2026ayahuasca`, `pagni2025longterm`, `ruffell2021ceremonial`, `nayak2023naturalistic`, `kopra2023investigation`, `robinson2026field` | Benchmarks this sample's demographics, ceremony settings, and satisfaction ceiling against six naturalistic cohorts. `teixeira2026ayahuasca` (n=203 ayahuasca ceremony attenders, Portugal, JPD 2026) is the single closest design analog found in any database searched — same journal, same self-administered cross-sectional structure, published within the last year. |
| Adverse events and boundary violations in ceremonial/guided settings | `kruger2025psychedelic`, `peluso2020reflections` | Contextualizes the 5/67 non-consensual-contact finding against the only published survey-based evidence on psychedelic-facilitator sexual misconduct, plus the field's own harm-reduction response (the Chacruna ayahuasca sexual-abuse awareness guide). |
| Facilitator training, credentialing, and screening practice | `gorman2021psychedelic`, `pilecki2021ethical`, `dutton2025harm` (reused from §1 gap 6) | No dedicated credentialing-specific paper exists in the indexed literature (confirmed via a targeted PubMed search returning zero hits); covered instead by the harm-reduction sources, which treat facilitator training/screening as a harm-reduction-practice component. |
| Ceiling effects in self-reported psychedelic experience measures | `bouso2016measuring` | Supports §4.2's measurement argument about `ceremony_good`'s 51/64 (80%) concentration at scale points 5–6 — a known property of self-report hallucinogen-effect rating scales, not necessarily an artifact of this study's instrument alone. |

---

## 4. Reference count and scope note

Phase 2 (Introduction citation gaps + Discussion comparator literature) contributes **26 verified
references** to `references.bib`. `MANUSCRIPT_PLAN.md` sets a target of 45–65 references pending a JPD
reference cap; Phase 0 found no explicit cap, and the closest available real-world comparator (a very
similar JPD cross-sectional ceremony-attender survey, `teixeira2026ayahuasca`) used 41 references for the
*entire* paper. Given JPD's 4,000-word Introduction–Discussion cap (already 674 words over budget before
Phase 2 additions, per `JOURNAL_REQUIREMENTS.md`), padding the Introduction/Discussion bibliography
further would cost word budget without adding real support — every candidate paper considered and
excluded is logged in the two search-log files above with the reason for exclusion. Phase 3 will add a
smaller set of Methods/statistics citations (STROBE, the exact test and effect-size conventions already
decided in Phase 1) that were out of scope for Phase 2's literature-review mandate; those, combined with
this 26, should land the finished bibliography in a range consistent with `teixeira2026ayahuasca`'s
precedent rather than at the plan's upper bound.

## 5. Metadata completeness

Every `references.bib` entry has a DOI, or — for the four entries that structurally cannot have one — an
explicit `note` field stating why: `doeltermorales2020hongos` (unpublished thesis, repository URL given
instead), `uscongress1970csa` and `pr1971csa` (primary statutes, official citation given instead of a
DOI). Five entries (`carvalho2025scoping`, `teixeira2026ayahuasca`, `pagni2025longterm`,
`robinson2026field`, `velezrodriguez2026psilocybin`) are Online First as of 2026-08-13 and carry a `note`
stating that volume/issue/page assignment is pending — flagged for a recheck immediately before final PDF
compilation (Phase 6), since JPD and Contemporary Drug Problems typically assign final pagination within
months of Online First publication.
