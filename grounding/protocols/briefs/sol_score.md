# Brief: judge and score the Sol round (session "sol_score")

Rules for every session: [README.md](README.md). Study folder: `grounding/runs/sol_eval_01/` (it exists; read its
README first: the design, the case sets, what differs from the Qwen round). Muse cap for this session: **$10
billed** (judging about 1,500 runs costs about $3–4).

## The questions

1. What does GPT-6.1 Sol expose on the Muse-written half of the suite, under the same judge, rulings and 10-minute
   budget as the Qwen round: tests exposing a fact, facts at detect@3 and detect@1, per service and form, and the
   failure mechanisms? Side by side with Qwen's numbers on the same tests.
2. How accurate is the judge on Sol's runs? 180 blind trials were drawn before any verdict
   (`sol_eval_01/eval/blind_*.json`, 45 per set); you label them before reading any verdict on them.
3. The eight policy cells for Sol, on the Muse-parent units, under the fixed rule (`policy.pooled_decision`), and
   the per-fact view. Side by side with Qwen's.
4. What else the runs show: awareness remarks (`openclaw_eval_01/test_awareness.py`), timings, tokens (input,
   cached, output, reasoning), infrastructure errors, and anything surprising. The PI welcomes observations.

## Materials

- The runs: `sol_eval_01/runs/regular_p4`, `regular_6b`, `policy_absence`, `policy_underspecified` (t1–t3 each).
  They may still be running when you start: build and test your scripts on the finished sets first.
- The Qwen round's machinery, to reuse unchanged where it fits and to adapt by copying into `sol_eval_01/kit/`
  where paths are hard-wired: `openclaw_eval_01/README.md` ("Commands"), `autogen_02/kit/phase4.py` (`select`,
  `score`), `autogen_02/kit/judge2.py` (`run` with `AUTOGEN_BACKEND=muse`, `compare`, `select --runs` for policy
  units), `openclaw_eval_01/adjudicate.py` and `rulings.py` (the rulings and the budget), `openclaw_eval_01/policy.py`
  (`population_outcomes`, `pooled_decision`, `decide_population`), `openclaw_eval_01/combine.py`.
- Suite indexes for `select` and `score`: `sol_eval_01/cases/<set>/suite.json`.
- Labelling: the evidence-only view and the outcome vocabulary of `blind_review_01` (`view.py`, `README.md`) and
  the judge's outcome definitions (`autogen_02/kit/prompts/judge_v2.md`). Keep initial labels, adjudications and any
  later corrections in separate files, as blind_review_01 does.
- Qwen's numbers on the same tests: `openclaw_eval_01/runs/*.adjudicated.json` (restricted to the Muse-written
  cases), `runs/policy/decisions_population_*.json` (the `phase4_only` and `6b_only` parts), and
  `report_01/numbers/`.

## Steps

1. For each regular set: `select` with `--blind`, judge on Muse, label the blind sample first, `compare`, `score`,
   adjudicate under the rulings and the budget. Report per set and combined.
2. For each policy set: select every trial, judge, label the blind sample first, compare; then decide per cell over
   the Muse-parent units with the fixed rule, and the per-fact counts.
3. The side-by-side with Qwen, with denominators; note the 16 G4-LIN-08 tests and units that could not run.
4. Awareness, timings, tokens, infrastructure errors; a short "how it fails" section from the blind labels.

## Deliverable

The **Results** section of `sol_eval_01/README.md`, `eval/` (verdicts, labels, comparisons, scores, decisions), and
`kit/` (your scripts, each with a docstring saying what it copies from where). Message the lead when the first
regular set is scored, and at the end. Do not edit openclaw_eval_01 or report_01.
