# The complete system: how to run it

autogen_02 wraps autogen_01's generation, derivation, solver runs and judge into one system, and adds the two policy
tests (absent target and underspecified request) with sampled policy decisions. Every agent (writer, reader, judge)
runs on Muse (`AUTOGEN_BACKEND=muse`, [../muse_backend.md](../muse_backend.md)). The solver under test is Qwen
(`qwen3.8:27b`) on Purdue, through fact_coverage_02's runner and rate limiter.

All commands run from the repository root, through the launcher (it sets the Purdue key from `grounding/.env`, the
rate limiter, the database and `PYTHONPATH`):

```bash
L="python grounding/runs/fact_coverage_02/launch.py"
S=grounding/runs/autogen_02
```

## 1. Scenarios from briefs (automated: Muse writer and reader; code checks)

```bash
python3 -m grounding.runs.autogen_02.inputs.make_briefs4          # the briefs, by rule
AUTOGEN_BACKEND=muse $L grounding.runs.autogen_02.kit.generate --run $S/runs/phase4_gen --first 16 --concurrency 4
```

Each brief goes through autogen_01's orchestrator: the writer writes `scenario.json`; code checks it; the replica
pre-checks install it; a cold reader reads it; findings go back to the writer. An accepted scenario is expanded into
its suite (cover, one probe per near miss, fact probes) under `runs/phase4_gen/cases/`.

## 2. Policy variants (code, plus Muse for wording)

| Variant | Unit | Built by |
|---|---|---|
| Absence twin | (scenario, fact) | code: `policy.absence_twins` (the fact's probe or fact probe without "If there isn't one, just tell me") |
| Underspecified (drop-F) | distinct condition | code decides derivability and the match set (`policy.drop_f`, semantic construction); the Muse writer rewords (`variants2 dropf`); code checks the words; the Muse reader reads it cold and must find exactly the intended matches |
| Underspecified clone | scenario | the Muse writer describes a copy of the target (`variants2 clone`); code builds and checks it (`policy.clone`); the reader checks the match set |

```bash
AUTOGEN_BACKEND=muse $L grounding.runs.autogen_02.kit.variants2 dropf --source population --out $S/runs/phase3_dropf
AUTOGEN_BACKEND=muse $L grounding.runs.autogen_02.kit.variants2 clone --source population --out $S/runs/phase3_clone
```

## 3. Sampling the policy tests (code)

Per cell (domain x mode), a random order fixed once by a seed, stratified by substitute family; units ruled out by
the manual validity review are skipped; looks after 11, 18 and 25 units ([../plan.md](../plan.md), amendment 2).

```bash
$L grounding.runs.autogen_02.kit.sampler plan absence --seed 20260926 --out $S/runs/phase3
$L grounding.runs.autogen_02.kit.sampler look absence 1 --out $S/runs/phase3        # cases of look 1
$L grounding.runs.autogen_02.kit.sampler decide absence --out $S/runs/phase3 --verdicts $S/runs/judge2_phase3
```

## 4. Solver runs (Qwen on Purdue, 3 trials)

```bash
$L grounding.runs.autogen_02.kit.solve --cases-dir $S/runs/phase3/absence_look1 --out $S/runs/phase3/solve_absence_look1
```

A main pass, then a retry pass for infrastructure errors and timeouts. A run waits while another solver run is in
progress.

## 5. Judging (Muse, judge v2)

```bash
$L grounding.runs.autogen_02.kit.judge2 select --runs RUN_DIR > trials.json
AUTOGEN_BACKEND=muse $L grounding.runs.autogen_02.kit.judge2 run --trials trials.json --out JUDGED_DIR
```

Judge v2 = autogen_01's judge with explicit rules for the policy tests ([prompts/judge_v2.md](prompts/judge_v2.md)),
the test form named by case prefix (`AT-` absence twin, `U-`/`UC-` underspecified), every full match listed as
TARGET, and this study's replica notes.

## Aids for the manual work
- `review.py RUN_DIR [--brief] [--cases ...] [--full t1/CASE]`: trials, compactly, for labelling by hand.
- `show_variants.py DIR [--manual]` and `calibration.py dropf|clone DIR`: automated variants against my hand-made
  ones.
- `policy_analysis.py`: Phase 1 per fact (the pair reading with the probes) and per cell.
- `check_derivable.py`, `population.py --survey`, `recheck_a1.py`: construction checks.
