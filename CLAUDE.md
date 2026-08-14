# AGENTS.md

Drop-in operating instructions for coding agents. Read this file before every task.

**Working code only. Finish the job. Plausibility is not correctness.**

This file follows the [AGENTS.md](https://agents.md) open standard (Linux Foundation / Agentic AI Foundation). Claude Code, Codex, Cursor, Windsurf, Copilot, Aider, Devin, Amp read it natively. For tools that look elsewhere, symlink:

```bash
ln -s AGENTS.md CLAUDE.md
ln -s AGENTS.md GEMINI.md
```

---

## 0. Non-negotiables

These rules override everything else in this file when in conflict:

1. **No flattery, no filler.** Skip openers like "Great question", "You're absolutely right", "Excellent idea", "I'd be happy to". Start with the answer or the action.
2. **Disagree when you disagree.** If the user's premise is wrong, say so before doing the work. Agreeing with false premises to be polite is the single worst failure mode in coding agents.
3. **Never fabricate.** Not file paths, not commit hashes, not API names, not test results, not library functions. If you don't know, read the file, run the command, or say "I don't know, let me check."
4. **Stop when confused.** If the task has two plausible interpretations, ask. Do not pick silently and proceed.
5. **Touch only what you must.** Every changed line must trace directly to the user's request. No drive-by refactors, reformatting, or "while I was in there" cleanups.

---

## 1. Before writing code

**Goal: understand the problem and the codebase before producing a diff.**

- State your plan in one or two sentences before editing. For anything non-trivial, produce a numbered list of steps with a verification check for each.
- Read the files you will touch. Read the files that call the files you will touch. Claude Code: use subagents for exploration so the main context stays clean.
- Match existing patterns in the codebase. If the project uses pattern X, use pattern X, even if you'd do it differently in a greenfield repo.
- Surface assumptions out loud: "I'm assuming you want X, Y, Z. If that's wrong, say so." Do not bury assumptions inside the implementation.
- If two approaches exist, present both with tradeoffs. Do not pick one silently. Exception: trivial tasks (typo, rename, log line) where the diff fits in one sentence.

---

## 2. Writing code: simplicity first

**Goal: the minimum code that solves the stated problem. Nothing speculative.**

- No features beyond what was asked.
- No abstractions for single-use code. No configurability, flexibility, or hooks that were not requested.
- No error handling for impossible scenarios. Handle the failures that can actually happen.
- If the solution runs 200 lines and could be 50, rewrite it before showing it.
- If you find yourself adding "for future extensibility", stop. Future extensibility is a future decision.
- Bias toward deleting code over adding code. Shipping less is almost always better.

The test: would a senior engineer reading the diff call this overcomplicated? If yes, simplify.

---

## 3. Surgical changes

**Goal: clean, reviewable diffs. Change only what the request requires.**

- Do not "improve" adjacent code, comments, formatting, or imports that are not part of the task.
- Do not refactor code that works just because you are in the file.
- Do not delete pre-existing dead code unless asked. If you notice it, mention it in the summary.
- Do clean up orphans created by your own changes (unused imports, variables, functions your edit made obsolete).
- Match the project's existing style exactly: indentation, quotes, naming, file layout.

The test: every changed line traces directly to the user's request. If a line fails that test, revert it.

---

## 4. Goal-driven execution

**Goal: define success as something you can verify, then loop until verified.**

Rewrite vague asks into verifiable goals before starting:

- "Add validation" becomes "Write tests for invalid inputs (empty, malformed, oversized), then make them pass."
- "Fix the bug" becomes "Write a failing test that reproduces the reported symptom, then make it pass."
- "Refactor X" becomes "Ensure the existing test suite passes before and after, and no public API changes."
- "Make it faster" becomes "Benchmark the current hot path, identify the bottleneck with profiling, change it, show the benchmark is faster."

For every task:

1. State the success criteria before writing code.
2. Write the verification (test, script, benchmark, screenshot diff) where practical.
3. Run the verification. Read the output. Do not claim success without checking.
4. If the verification fails, fix the cause, not the test.

---

## 5. Tool use and verification

- Prefer running the code to guessing about the code. If a test suite exists, run it. If a linter exists, run it. If a type checker exists, run it.
- Never report "done" based on a plausible-looking diff alone. Plausibility is not correctness.
- When debugging, address root causes, not symptoms. Suppressing the error is not fixing the error.
- For UI changes, verify visually: screenshot before, screenshot after, describe the diff.
- Use CLI tools (gh, aws, gcloud, kubectl) when they exist. They are more context-efficient than reading docs or hitting APIs unauthenticated.
- When reading logs, errors, or stack traces, read the whole thing. Half-read traces produce wrong fixes.

---

## 6. Session hygiene

- Context is the constraint. Long sessions with accumulated failed attempts perform worse than fresh sessions with a better prompt.
- After two failed corrections on the same issue, stop. Summarize what you learned and ask the user to reset the session with a sharper prompt.
- Use subagents (Claude Code: "use subagents to investigate X") for exploration tasks that would otherwise pollute the main context with dozens of file reads.
- When committing, write descriptive commit messages (subject under 72 chars, body explains the why). No "update file" or "fix bug" commits. No "Co-Authored-By: Claude" attribution unless the project explicitly wants it.

---

## 7. Communication style

- Direct, not diplomatic. "This won't scale because X" beats "That's an interesting approach, but have you considered...".
- Concise by default. Two or three short paragraphs unless the user asks for depth. No padding, no restating the question, no ceremonial closings.
- When a question has a clear answer, give it. When it does not, say so and give your best read on the tradeoffs.
- Celebrate only what matters: shipping, solving genuinely hard problems, metrics that moved. Not feature ideas, not scope creep, not "wouldn't it be cool if".
- No excessive bullet points, no unprompted headers, no emoji. Prose is usually clearer than structure for short answers.

---

## 8. When to ask, when to proceed

**Ask before proceeding when:**
- The request has two plausible interpretations and the choice materially affects the output.
- The change touches something you've been told is load-bearing, versioned, or has a migration path.
- You need a credential, a secret, or a production resource you don't have access to.
- The user's stated goal and the literal request appear to conflict.

**Proceed without asking when:**
- The task is trivial and reversible (typo, rename a local variable, add a log line).
- The ambiguity can be resolved by reading the code or running a command.
- The user has already answered the question once in this session.

---

## 9. Self-improvement loop

**This file is living. Keep it short by keeping it honest.**

After every session where the agent did something wrong:

1. Ask: was the mistake because this file lacks a rule, or because the agent ignored a rule?
2. If lacking: add the rule under "Project Learnings" below, written as concretely as possible ("Always use X for Y" not "be careful with Y").
3. If ignored: the rule may be too long, too vague, or buried. Tighten it or move it up.
4. Every few weeks, prune. For each line, ask: "Would removing this cause the agent to make a mistake?" If no, delete. Bloated AGENTS.md files get ignored wholesale.

Boris Cherny (creator of Claude Code) keeps his team's file around 100 lines. Under 300 is a good ceiling. Over 500 and you are fighting your own config.

---

## 10. Project context

**Study.** Ceremonial entheogen use among adults 21+ in Puerto Rico. Originally framed as a cross-sectional *epidemiological* survey (PI: Yamil O. Ortiz Ortiz; UPR Río Piedras CIS, UPR RCM, PR Institute for Psychedelic Science, Colectivo Psicodélico de PR). **Reframed to a descriptive study** — no weighting, no incidence/prevalence-to-population claims (see decision E10 below). Instrument is team-developed (no validated PR instrument exists), online, anonymous, convenience/snowball sample. Target N=100, achieved N=100.

**Data files (`data/`).**
- `Narrativa de propuesta uso ceremonial de enteogenos.md` — Spanish IRB-style proposal narrative.
- `koboxls.xlsx` — the KoboToolbox XLSForm. **`survey` sheet = full skip/relevance logic (authoritative); `choices` sheet = value sets.** Always resolve variable meaning and skip logic here, not from column names.
- `questionnaire_choices.xlsx` — standalone copy of the choices sheet (~60 `list_name` value sets).
- `results_7_15_2026.xlsx` — real collected data, **100 rows × 354 columns**, one sheet. This is ground truth; inspect directly.

**Encoding.** Files contain Spanish characters (ñ, á). Always run Python with `PYTHONIOENCODING=utf-8` or reads/prints crash under cp1252.

**Structure / skip logic (verified against survey sheet + data).**
- Consent/eligibility gate: sociodemographics shown only when `vol_part='si' AND over_21='si'`.
- Role fork: `is_facilitator` and `is_participant` (both `si_no_pna`), asked only when `ans_prev='no'`. **Not mutually exclusive.** Counts: 7 both, 65 participant-only, 1 facilitator-only, 27 neither "sí" (13 both-role-items-blank = abandoned early; 14 explicit no/no = screen-outs).
- Facilitator block (`seccion_facilitatores`): shown when `is_facilitator='si'` (~8 people).
- Participant block (`Secci_n_4_Participantes`, incl. `ceremony_good`, `non_con_contact`): shown when `is_participant='si'`; dual-role respondents reach it only if they also pass a `pause_facil='si'` continuation gate — this is why some dual-role cases have missing participant items.

**Key variables.**
- Primary satisfaction outcome: `ceremony_good`, ODK-encoded `_0`…`_6` (strip underscore → 0–6) + `pna`. Missing in 36/100 overall, but only **8/72 (11%) missing within `is_participant='si'`** — the rest is structural (non-participants never asked). Treat as **ordinal / nonparametric** (heavy ceiling: 51/64 answered 5–6).
- Safety domain (in scope, absent from proposal): `non_con_contact` (`si_no_unsure`: 61 no / 5 si / 1 not_sure / 33 missing), `non_con_contact_recent`, and `exp_crisis` (select-multiple; includes `suicide_idea`, `panic_atk`). Associate with `training_facilitator`, `screening_quest`, `protocol_bad_exp`, `emergency_plan`, `safe_ceremony`.
- **Three distinct drug variables** — do not conflate: `drugs_used_facil` (facilitator, substances across ceremonies led, select-multiple, ~7 non-null); `drug_used_part` (participant, substances across ceremonies attended, select-multiple, 67 non-null); `drugs_used_part` (participant, substance in *most recent* ceremony, select-one). The review-prompt brief mislabeled `drug_used_part` as facilitator-reported — it is participant-side; corrected here.
- Attention checks are **branch-specific, not 6 uniform items**: facilitator judged on `atencion_1/2/3` (~7 responses each); participant judged on `atencion_3_2/4/5/6` (~64–67 each). 7 columns total.
- Select-multiple items appear both as a space-separated string column and as one-hot `name/option` columns in results.

**Confirmed analysis decisions (this session).**
1. Population: keep the 14 explicit no/no rows for describing screen-outs; no authoritative completion-status field exists.
2. Dual-role (7): include in **both** facilitator-side and participant-side analyses.
3. `pna` and `not_sure`: retain as a **substantive category**, applied **uniformly** across all items (not dropped, not NA).
4. `ceremony_good`: ordinal / nonparametric primary.
5. Safety domain (`non_con_contact` + `exp_crisis`): formal outcome set, no disclosure/reporting constraints imposed.
6. Duplicate screening: flag via **`nickname` + `password` combination** (repeats exist; `_submitted_by` empty, no IP). `ev_dup`/`ev_dup_note` are empty for all 100 — platform never populated them.
7. Attention checks: **do not drop** rows — mark for reviewer, judged per branch as above.
8. **Reframe as unweighted descriptive study** (no weighting to PR Census/ACS; drop epidemiological framing).
9. Residency (`municipality`, `country`, `hispanic`): descriptive covariate, not an inclusion filter.
10. Cell-size suppression: suppress subgroup cells with **n < 5**.

**Deliverables & tooling.** Analysis code in **Python** (not R, despite the proposal's stated R/RStudio plan). Output = executable Python scripts + a rendered **PDF/HTML** statistical report. The user writes the manuscript separately in this same repo from these results. Analysis plan document: `ANALYSIS_PLAN.md`.

---

## 11. Project Learnings

**Accumulated corrections. This section is for the agent to maintain, not just the human.**

When the user corrects your approach, append a one-line rule here before ending the session. Write it concretely ("Always use X for Y"), never abstractly ("be careful with Y"). If an existing line already covers the correction, tighten it instead of adding a new one. Remove lines when the underlying issue goes away (model upgrades, refactors, process changes).

- Always invoke Python as `C:/Users/jeanv/miniforge3/python.exe`; the `python` and `py` shims resolve to the Microsoft Store stub and do nothing.

---
