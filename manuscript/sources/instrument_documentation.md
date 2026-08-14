# Instrument documentation — verbatim item wording and scale anchors

Source: `data/koboxls.xlsx`, `survey` and `choices` sheets (extracted directly, not paraphrased).
Closes the Phase 1c gap flagged in the early manuscript draft's Open Items: "the anchor wordings are not
given. Reviewers will ask."

## Bilingual fielding

`settings` sheet: `default_language = Español (es)`. Every survey item carries both a `label::Español (es)`
and a `label::English (en)` column in the same KoboToolbox form — this is a native bilingual XLSForm, not two
separate instruments or a post-hoc translation. Spanish is the default UI language; English is available via
KoboToolbox's built-in language switcher. This explains the mixed-language open-text corpus noted in Results
§3.1 (respondents could complete the survey in either language). Closes the "age of the instrument's
language versions" open item: the bilingual design was native to the form from the start, not an later
addition, and translation equivalence is a direct 1:1 per-item mapping within the same XLSForm rather than a
separately validated translation.

## Primary outcome: `ceremony_good`

- **Type:** `select_one ceremony_good`
- **Wording (EN):** "From 0 to 6, how pleasant was the ceremony?"
- **Wording (ES):** "Del 0 al 6, ¿qué tan agradable fue la ceremonia?"
- **Anchors (choices-sheet order, ascending, matches the numeric code used throughout the analysis):**

| code | label (EN) | label (ES) |
|---|---|---|
| 0 | Very unpleasant | Muy desagradable |
| 1 | Unpleasant | Desagradable |
| 2 | Somewhat unpleasant | Algo desagradable |
| 3 | Neither pleasant nor unpleasant | Ni agradable ni desagradable |
| 4 | Somewhat pleasant | Algo agradable |
| 5 | Pleasant | Agradable |
| 6 | Very pleasant | Muy agradable |
| — | Prefer not to answer | Prefiero no contestar |

## `comfort_safe`

- **Type:** `select_one comfort_safe`
- **Wording (EN):** "During the ceremony, how would you describe your overall sense of comfort and safety?"
- **Wording (ES):** "Durante la ceremonia, ¿cómo se sintió en cuanto a comodidad y seguridad?"
- **Anchors, ordered by the numeric code used in the analysis (0=worst, 3=best):**

| code used in analysis | label (EN) |
|---|---|
| 0 | I felt very uncomfortable or unsafe |
| 1 | At times I felt somewhat uncomfortable or unsafe |
| 2 | I felt mostly comfortable and safe |
| 3 | I felt completely comfortable and safe |
| — | Prefer not to answer |

**Methodological note (not a gap, but worth documenting explicitly):** the raw KoboToolbox choices-sheet row
order for this item is *best-first* (`fully_comf, mostly_comf, some_uncomf, very_uncomf, pna` — the reverse
of the table above). `analysis/config.py`'s `ORDINAL_SCALES["comfort_safe"]` deliberately re-orders these by
semantic content (reading the actual label text) into ascending low→high, so that — consistent with every
other ordinal scale in this analysis — higher numeric code always means a more positive response. This is
correct and intentional, not a bug: the numeric code assignment in `data_prep.py::add_ordinals()` is driven
entirely by `config.py`'s list order, not by the XLSForm's row position, so the raw sheet's UI-display order
(likely best-first for respondent-facing UX reasons) has no bearing on the analysis coding. Flagging this
here because a reviewer cross-referencing the raw `koboxls.xlsx` choices sheet against the analysis could
otherwise be confused by the apparent mismatch.

## `trust_level`

- **Type:** `select_one trust_level`
- **Wording (EN):** "How much did you trust the person who facilitated the ceremony?"
- **Wording (ES):** "¿Qué tanto confió en la persona que facilitó la ceremonia?"
- **Anchors (choices-sheet order, ascending, matches analysis coding 0–4):**

| code | label (EN) | label (ES) |
|---|---|---|
| 0 | Not at all | Nada |
| 1 | A little | Un poco |
| 2 | Moderately | Moderadamente |
| 3 | A lot | Mucho |
| 4 | Completely | Completamente |
| — | Prefer not to answer | Prefiero no contestar |

## Primary exposure: `prep_part`

- **Type:** `select_one si_no_av_pna`
- **Wording (EN):** "Aside from the facilitator's instructions or recommendations, do you personally engage
  in preparation for these ceremonies?"
- **Wording (ES):** "Aparte de las instrucciones o recomendaciones del facilitador, ¿usted personalmente se
  prepara para estas ceremonias?"
- **Anchors:** Yes (`si`) / No (`no`) / Sometimes (`a_veces`) / Prefer not to answer (`pna`)

Closes the "definition of preparation" open item in part: the item asks specifically about the respondent's
*own, self-directed* preparation, distinct from any preparation instructions the facilitator may have given
(captured separately). This is why the free-text `self_prep_type` field (30 answers) exists as a follow-up —
it asks respondents to describe what their self-directed preparation consisted of, since the closed item
only captures whether it happened, not what it was. The construct is genuinely heterogeneous by design, not
an instrument flaw: `prep_part` measures presence/frequency of self-directed preparation, and
`self_prep_type` (open-text, not separately coded in this analysis pass) captures its content.

## `non_con_contact`

- **Type:** `select_one si_no_unsure`
- **Wording (EN):** "Have you ever experienced physical touch during a ceremony that felt unexpected or that
  you did not clearly agree to beforehand? This could include moments where you were unsure, uncomfortable,
  or did not remember giving permission."
- **Wording (ES):** "¿Alguna vez ha experimentado contacto físico durante una ceremonia que le resultó
  inesperado o al que no dio su consentimiento claramente de antemano? Esto podría incluir momentos en los
  que no estaba seguro(a), se sintió incómodo(a) o no recordaba haber dado permiso."
- **Anchors:** Yes (`si`) / No (`no`) / I'm not sure (`not_sure`) / Prefer not to answer (`pna`)

Note the item wording is deliberately broad (unexpected/unclear-consent touch, including uncertainty and
memory gaps) — broader than a narrower "assault" framing would be. This matters for how the manuscript should
characterize the 7.5% prevalence figure: it measures experiences meeting this broad definition, not a
narrower legal or clinical standard. Worth a sentence in Methods §2.3 when describing this item.
