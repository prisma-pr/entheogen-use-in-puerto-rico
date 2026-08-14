# Comparator-cohort demographics for Discussion §4.1 (peer-review item R8)

Collected 2026-08-13 during the Phase-5 revision. `PARALLEL_API_KEY` is still unset in the repo `.env`, so
this used the WebSearch/WebFetch fallback plus direct keyless CrossRef and PubMed E-utilities calls (the
approach that worked in Phase 2). Taylor & Francis full text was reached through the `r.jina.ai` proxy,
which bypasses the 403 that blocks direct fetches.

**Purpose.** Reviewer point R8: the Discussion asserted that this sample's demographic profile "resembles
that of ceremony-attender cohorts described elsewhere" while giving no comparator numbers. These are the
numbers, taken from the comparators already cited in the manuscript.

## Comparators used in the revision

| Cohort | Source | n | Age | Women | Bachelor's degree or above |
|---|---|---|---|---|---|
| This sample | own data | 73 | mean 42.4, SD 11.9 | 49% (35 of 71) | 78% (56 of 72: bachelor's 34, master's 19, doctorate 3) |
| Neo-shamanic ayahuasca ceremony attenders, US | Pagni et al. 2025, *J Psychoactive Drugs* | 66 | mean 37.56, SD 10.16, range 19–64 | 61% (40 of 66; 26 men) | "almost half (49.9%)" — bachelor's 30.3%, master's/professional 12.1%, doctoral 6.1% |
| Ceremonial ayahuasca retreat attenders, Peruvian Amazon | Ruffell et al. 2021, *Front Psychiatry* | 63 | mean 37.0, SD 9.7, range 19–63 | 44.4% (25 women, 35 men) | not reported |
| Naturalistic psilocybin users, international online cohort | Nayak et al. 2023, *Front Psychiatry* | 2,833 | mean 40, SD 13.1, range 18–89 | 46% | 58.5% (bachelor's 31.7% + master's 18.8% + advanced professional 8.0%) |

Notes on the numbers:

- **Pagni 2025** — the paper states 49.9% for "bachelor's degree or above" while its own components sum to
  48.5%. The paper's stated figure (49%) is used, and the discrepancy is the source's, not ours.
- **Ruffell 2021** reports no education distribution, so the education comparison rests on Pagni and Nayak.
- **Teixeira et al. 2026** (the Portuguese ayahuasca attender cohort, n = 203) was the reviewer's first
  suggested comparator, but its demographic table sits behind the Taylor & Francis paywall and neither the
  abstract, the ICEERS project page, nor the PANO/FMH Lisbon project pages report age, gender, or education
  for that sample. Only n = 203 could be verified. **It is therefore not used for numeric comparison** and
  remains cited for design analogy only. Same for Kopra et al. 2023 (Global Drug Survey 2020): the abstract
  reports 3,364 respondents (1,996 LSD, 1,368 psilocybin) but no age/gender/education breakdown, and the
  full text is not open access.

## Sources

- Pagni et al. 2025 — https://www.tandfonline.com/doi/full/10.1080/02791072.2025.2465800 (via r.jina.ai);
  PubMed record https://pubmed.ncbi.nlm.nih.gov/39980134/
- Ruffell et al. 2021 — https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2021.687615/full
- Nayak et al. 2023 — https://www.frontiersin.org/journals/psychiatry/articles/10.3389/fpsyt.2023.1199642/full
- Teixeira et al. 2026 — https://www.tandfonline.com/doi/full/10.1080/02791072.2026.2631378 (paywalled);
  https://www.iceers.org/en/studies/ayahuasca-and-health-in-portugal/
- Kopra et al. 2023 — https://pubmed.ncbi.nlm.nih.gov/36876583/

---

# New references added for R8 / R-refs (all CrossRef-verified)

Queried against `api.crossref.org/works`; author lists, journal, year, volume, issue, and pagination are
the publisher-deposited values.

| Key | Work | Verified metadata |
|---|---|---|
| `bouso2022adverse` | Bouso, Andión, Sarris, Scheidegger, Tófoli, Opaleye, Schubert, Perkins. "Adverse effects of ayahuasca: Results from the Global Ayahuasca Survey" | *PLOS Global Public Health* 2(11): e0000438, 2022. DOI 10.1371/journal.pgph.0000438 |
| `carbonaro2016survey` | Carbonaro, Bradstreet, Barrett, MacLean, Jesse, Johnson, Griffiths. "Survey study of challenging experiences after ingesting psilocybin mushrooms" | *Journal of Psychopharmacology* 30(12): 1268–1278, 2016. DOI 10.1177/0269881116662634 |
| `hartogsohn2017constructing` | Hartogsohn. "Constructing drug effects: A history of set and setting" | *Drug Science, Policy and Law* 3: 2050324516683325, 2017. DOI 10.1177/2050324516683325 |
| `mcnamee2023studying` | McNamee, Devenot, Buisson. "Studying Harms Is Key to Improving Psychedelic-Assisted Therapy" | *JAMA Psychiatry* 80(5): 411, 2023. DOI 10.1001/jamapsychiatry.2023.0099 |
| `bethlehem2010selection` | Bethlehem. "Selection Bias in Web Surveys" | *International Statistical Review* 78(2): 161–188, 2010. DOI 10.1111/j.1751-5823.2010.00112.x |

# Metadata defects corrected in `references.bib`

Peer-review item P3-5, plus two further defects found while re-querying CrossRef that the review had not
flagged:

| Key | Was | CrossRef / PubMed |
|---|---|---|
| `koss1980therapist` | *Social Science & Medicine. Medical Anthropology*, vol. 14B | *Social Science & Medicine. Part B: Medical Anthropology*, vol. **14**, no. 4 |
| `hughes2024ethnoracial` | `EClinicalMedicine`; author "Hughes, Matthew E." | `{eClinicalMedicine}` (brace-protected); CrossRef gives **"Hughes, Marcus E."** (PubMed: "Hughes ME") |
| `bouso2016measuring` | journal "Human Psychopharmacology" | full title *Human Psychopharmacology: Clinical and Experimental* |
| `golden2022effects` | `@article`; authors "Golden, Thea L.", "Sandu, Cristina C.", "Lin, Shiqi", "Shi, Kevin M." | `@incollection` in the *Current Topics in Behavioral Neurosciences* book series; CrossRef gives **Golden, Tasha L.**; **Sandu, Clara C.**; **Lin, Shuyang**; **Shi, Kathy M.**; **Roebuck, Grace Marie** (PubMed initials TL, CC, S, KM, GM all consistent) |
| `marcus2026psychedelics` | year 2026 | print issue 2026-01, 47(1):279–296; online-first 2025-07-27 recorded in a `note` |
