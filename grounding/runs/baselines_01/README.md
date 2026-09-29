# baselines_01: which baseline comparisons show what our approach contributes

A manual investigation, started 2026-09-28 at the PI's request. Branch `exp/baselines-01`, worktree
`.claude/worktrees/baselines-01`, branched from `exp/roadmap-02` at 9b18a7b64. It does not edit the roadmap, the kit,
the known-defects list or the frozen suite.

## The questions (agreed with the PI, 2026-09-28)

**Main question:** what are the meaningful baseline comparisons, the ones that show the contributions that carry the
weight in our approach?

1. **Which contributions to highlight.** Which parts of our approach produce results that a naive approach would not?
2. **Which baselines.** For each of those contributions, what baseline shows it? It should be a realistic approach
   without that part, with no advantage taken from our system and not a straw man. Naively asking a coding agent to
   write the tests is a valid baseline, and the most intuitive one. The roadmap's G0, G1, J0 and J1 are candidates,
   not givens.
3. **Which measures.** Where does the difference show: facts exercised, facts exercised properly (the credit rule),
   failures exposed, failures the judge catches, false results, and token cost? In what unit?
4. **Why the judge result came out incremental.** Did J0 and J1 land close to our judge because of the wrong measure,
   an unfair advantage, or a part we never ablated? (Light analysis.)

**Deliverable:** a proposal for the full comparison, every choice backed by data from this investigation. Running
the full comparison is out of scope.

## Constraints

- **The coding agent** for the "ask your coding agent" baseline is Muse Code, the agent our writer, reader and judge
  run on (PI, 2026-09-28). Budget: $50 at list price for the whole investigation.
- **The agent under test** is OpenClaw with the self-hosted Qwen, through the shared proxy and rate limiter, at 12 or
  fewer attempts in flight.
- **Discipline:** hand labels before any verdict; failed attempts kept; every model call's usage recorded.

**Result:** [report.md](report.md), the answers to the four questions and the proposal for the full comparison.

## Layout

| Path | What |
|---|---|
| [report.md](report.md) | The answers and the proposal |
| [log.md](log.md) | The cycle log: what changed, what ran, what was learned |
| [q4/](q4/README.md) | Question 4: why the judge baselines came out close |
| [n0/](n0/) | N0, "ask your coding agent": inputs, generator, review rules and review, run, labels, oracles |
| [n1/](n1/) | N1, N0 plus our facts: inputs, review, run, labels, flaws found at run time |
| [cycle2/](cycle2/) | The form and content ablations: cases, run, labels |
| `ablation/`, [plain_twins.py](plain_twins.py) | The plain twins of our probes and the originals they pair with |
| [ours.py](ours.py), [machinery.py](machinery.py), [compare.py](compare.py) | Our side from existing records, the machinery's catches, the report's tables |

## Commands

Run from the repository root; `L="/home/yusf/PyProj/agent-diff/backend/.venv/bin/python grounding/runs/fact_coverage_02/launch.py"`.

```bash
$L grounding.runs.baselines_01.n0.make_inputs                         # N0's inputs (n1/make_inputs.py adds the facts)
AUTOGEN_BACKEND=muse $L grounding.runs.baselines_01.n0.generate --run NAME [--inputs DIR --generator N1]
SOLVER_BACKEND=selfhost $L grounding.runs.openclaw_eval_01.run --out RUN --cases-dir SUITE --trials 3 --concurrency 12
python3 grounding/runs/baselines_01/label_view.py RUN CASE --brief    # labelling, before any verdict
$L grounding.runs.baselines_01.assertions RUN --out GEN/assertions.json
python3 grounding/runs/baselines_01/trials_of.py RUN > GEN/trials.json
AUTOGEN_BACKEND=muse $L grounding.runs.baselines_01.judges run plain_expected|j0 --trials GEN/trials.json --out GEN/judged_<variant>
python3 grounding/runs/baselines_01/score_oracles.py GEN
python3 grounding/runs/baselines_01/compare.py
```

N1's two LLM oracles first failed with HTTP 402 (billing) at 16:13; the failed calls are kept in
`n1/runs/gen_01/judged_*.failed-402-billing`. The rerun on the 141 trials that ran finished at 21:30.

`assertions.py --faithful` (output `assertions.faithful.json`) evaluates the baselines' assertions as our format
document described them: the document listed an `"unchanged"` type the engine rejects and promised that bookkeeping
columns are ignored (log, 21:29–21:45).
