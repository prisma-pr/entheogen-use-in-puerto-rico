# Analysis pipeline

Descriptive-study analysis for the ceremonial-entheogen survey. Python, output is a Markdown report with LaTeX math. Full rationale: [`../ANALYSIS_PLAN.md`](../ANALYSIS_PLAN.md).

## Run
```bash
cd analysis
PYTHONIOENCODING=utf-8 C:/Users/jeanv/miniforge3/python.exe report.py
```
(`PYTHONIOENCODING=utf-8` is required — Spanish glyphs crash under cp1252.)

## Modules
| file | role |
|------|------|
| `config.py` | paths, ordinal scales, attention-check key, suppression threshold (n<5) |
| `data_prep.py` | load + decode (from `koboxls.xlsx`), derive roles / prep exposure / ordinal `ceremony_good` |
| `quality.py` | attention-check + duplicate flags (flag, never drop) → `../outputs/tables/data_quality_flags.csv` |
| `stats_helpers.py` | Mann–Whitney, Kruskal–Wallis, Wilson-CI prevalence, suppression, markdown tables |
| `report.py` | orchestrates everything, writes `../outputs/report.md` + figures |

Each module runs standalone (`python <module>.py`) and prints a self-check.

## Outputs
- `outputs/report.md` — the report (Markdown + LaTeX math).
- `outputs/figures/*.png` — embedded figures.
- `outputs/tables/data_quality_flags.csv` — rows to adjudicate (attention/duplicates).

## Key modeling decisions (locked with client)
- `ceremony_good` = ordinal → nonparametric tests only.
- No clean participant integration item → analyze **preparation → outcome** directly.
- `pna`/`not_sure` retained as substantive categories, uniformly.
- Dual-role (7) in both role analyses; dual-role missing participant items = structural skip.
- Subgroup cells with n<5 suppressed. Descriptive study — no weighting, no population-prevalence claims.
