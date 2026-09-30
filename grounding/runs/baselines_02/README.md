# baselines_02: the naive baselines written by a stronger coding agent (Sonnet 5.5)

Session "values" (second assignment of the day from the lead session "RoadMap specialist"), brief
[baselines_sonnet.md](../../protocols/briefs/baselines_sonnet.md). Branch `exp/values-01`.

## Status

- **2026-09-30, 02:20 EDT.** Set up. Nothing has run yet.

## The question

How can we tell whether the naive baselines' result (no catalog fact exposed in 169 valid tests; the wrong records
they catch come from requests that presuppose a missing record) is a property of the naive approach or of the coding
agent that wrote them? We regenerate the two arms that matter, N0M and N1M
([baselines_01](../baselines_01/report.md) §8), with a stronger coding agent, Sonnet 5.5 through Claude Code, at the
same 48-test budget, and measure them the same way.

## Setup (stated defaults)

- **Writer:** Sonnet 5.5 (`claude-sonnet-5-5`) through Claude Code 2.1.285 (`claude -p`, on the PI's plan), with the
  generation kit's settings (`autogen_01/kit/agent.py`, the Claude Code backend): a clean workspace outside the
  repository, restricted mode, the file tools only (Read, Write, Edit, Glob, Grep; no shell, no web), no MCP servers,
  user and project settings ignored. Effort `high`, the Muse arms' setting (`MUSE_EFFORT=high`).
- **Inputs:** baselines_01's, unchanged: `twin2/n0m/inputs/<domain>/` (N0M) and `twin2/n1m/inputs/<domain>/` (N1M).
  The prompts are not tuned.
- **Sessions:** one session per service writes its 12 tests, one session at a time (the plan's window is shared).
- **Load feedback:** the loader's errors go back in the same session until the tests load, at most three repair
  turns (baselines_01's rule for the full comparison). Every round is snapshotted.
- **Refusals:** a refused or failed call is kept (`*.failed.json`); the domain is run again later under a new run
  name, and both are recorded.
- **Review:** by hand, under baselines_01's rules ([n0/review_rules.md](../baselines_01/n0/review_rules.md)), in one
  shuffled pool with anonymous ids and about 20 of our Muse tests (5 per service, a seeded draw). The review is blind
  to the arm; it cannot be blind to ours against theirs, since our probes' wording gives them away. It adds each
  test's intended target and effect, the answer key for grading.
- **Runs:** every valid test on OpenClaw with the self-hosted Qwen3.8-27B, 3 trials, the 10-minute budget, at most
  24 in flight. Timeouts are the agent's failures; only infrastructure errors are re-run.
- **Grading:** the tests' own AgentDiff assertions (`baselines_01/assertions.py --twin`), and our triage plus judge
  v2 with the review's answer key. A blind sample of 30 trials per arm, drawn before the runs and labelled by hand
  before any assertion result or verdict. Muse cap $5 billed.

## Layout

| Path | What |
|---|---|
| [generate.py](generate.py) | One Claude Code session per service writes 12 tests from baselines_01's inputs, with load feedback |
| `runs/` | Generation runs (`gen_<arm>_NN/<domain>/`: prompts, transcripts, results, workspace per round, `load.json`, `cases/`), and later the solver runs |
| [log.md](log.md) | The cycle log |
