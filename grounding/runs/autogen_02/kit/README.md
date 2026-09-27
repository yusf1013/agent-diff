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

`--source phase4` takes Phase 4's accepted scenarios instead of autogen_01's 49 (`population.phase4_scenarios`;
`population --survey --phase4` runs the code-only derivations on them first).

## 3. Sampling the policy tests (code)

Per cell (domain x mode), a random order fixed once by a seed, stratified by substitute family; units ruled out by
the manual validity review are skipped; looks after 11, 18 and 25 units ([../plan.md](../plan.md), amendment 2).

```bash
$L grounding.runs.autogen_02.kit.sampler plan absence --seed 20260926 --out $S/runs/phase3
$L grounding.runs.autogen_02.kit.sampler look absence 1 --out $S/runs/phase3        # cases of look 1
$L grounding.runs.autogen_02.kit.sampler decide absence --out $S/runs/phase3 --verdicts $S/runs/judge2_phase3
```

New scenarios join the cells after the fixed order (amendment 5), once and before any verdict is read; the plan
before the extension is kept as `plan_<mode>.v1.json`. A look completed by the new units takes only the units no
earlier look folder holds:

```bash
$L grounding.runs.autogen_02.kit.sampler extend absence --seed 2026092702 --out $S/runs/phase3
$L grounding.runs.autogen_02.kit.sampler look underspecified 1 --cells calendar/underspecified --dest NAME --out $S/runs/phase3
```

`decide` then reports each writer's units apart beside the combined decision.

## 4. Solver runs (Qwen on Purdue, 3 trials)

```bash
$L grounding.runs.autogen_02.kit.solve --cases-dir $S/runs/phase3/absence_look1 --out $S/runs/phase3/solve_absence_look1
```

A main pass, then a retry pass for infrastructure errors and timeouts. A run waits while another solver run is in
progress.

**The Purdue queue** runs solve runs one after another from a file that can grow while it runs; a gate lets a
higher-priority run be put ahead of a queued one without leaving Purdue idle (`gate_timeout`). It stops if a run
completes no trial (for instance without the key):

```bash
GROUNDING_ENV=/path/to/grounding/.env $L grounding.runs.autogen_02.kit.purdue_queue $S/runs/purdue_queue.jsonl
```

## 5. Judging (Muse, judge v2)

```bash
$L grounding.runs.autogen_02.kit.judge2 select --runs RUN_DIR > trials.json
AUTOGEN_BACKEND=muse $L grounding.runs.autogen_02.kit.judge2 run --trials trials.json --out JUDGED_DIR
```

For generated suites (Phase 4), the trials to judge are autogen_01's selection (every trial that is not
mechanically clean, plus 20% of the clean ones) and the blind sample; `phase4 score` then scores the run:

```bash
$L grounding.runs.autogen_02.kit.phase4 select RUN_DIR SUITE --blind $S/eval/blind_RUN.json > trials.json
$L grounding.runs.autogen_02.kit.phase4 score RUN_DIR SUITE JUDGED_DIR --json RUN.score.json
```

**Blind samples** for evaluating the judge are drawn from a run's cases folder before the run
(`blind_sample.py CASES_DIR RUN_NAME N SEED`) and labelled by hand before any verdict on them is read.

Judge v2 = autogen_01's judge with explicit rules for the policy tests ([prompts/judge_v2.md](prompts/judge_v2.md)),
the test form named by case prefix (`AT-` absence twin, `U-`/`UC-` underspecified), every full match listed as
TARGET, and this study's replica notes.

## Aids for the manual work
- `review.py RUN_DIR [--brief] [--cases ...] [--full t1/CASE] [--keys BLIND.json] [--unlabelled LABEL_DIR]`: trials,
  compactly, for labelling by hand; it flags any use of a filter the replica ignores.
- `show_variants.py DIR [--manual]` and `calibration.py dropf|clone DIR`: automated variants against my hand-made
  ones.
- `policy_analysis.py`: Phase 1 per fact (the pair reading with the probes) and per cell; `--actions RUN_DIR ...`
  says what each policy trial did to the record asked about (from the state diff).
- `tables.py`: every table of the report, from the run data.
- `check_derivable.py`, `population.py --survey`, `recheck_a1.py`: construction checks.
