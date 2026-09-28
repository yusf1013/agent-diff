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

## Layout

| Path | What |
|---|---|
| [log.md](log.md) | The cycle log: what changed, what ran, what was learned |
| `q4/` | Question 4: why the judge baselines came out close |

Further folders are added per cycle and listed here.
