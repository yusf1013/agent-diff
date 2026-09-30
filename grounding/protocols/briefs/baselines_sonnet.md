# Brief: the naive baselines with a stronger coding agent (session "baselines_sonnet")

Rules for every session: [README.md](README.md). Study folder: `grounding/runs/baselines_02/`. Muse cap: **$5
billed** (judging only). The coding agent under test as a test writer is **Sonnet 5.5 through Claude Code**
(`claude -p`, on the PI's plan). Codex arms are not for tonight: the OpenAI plan is carrying the Sol round.

## The question

The PI has been told that reviewers will ask how a stronger coding agent does as a naive test writer. Do the
naive baselines' results (no fact exposed in 169 valid tests; the wrong records they do catch come from
presupposing requests) hold when the writer is Sonnet 5.5 instead of Muse, at the same 48-test budget?

## Materials

- `grounding/runs/baselines_01/report.md`: the arms (N0 "ask your coding agent", N1 with the fact list, N0M and N1M
  with the PI's reviewer paragraph and the corrected format document), the inputs under `n0/`, `n1/`, `twin2/`
  (`inputs/` per domain), the load-feedback rule (at most three repair turns), the structural review rules and
  labels (facts exercised properly, designated look-alikes, flaws), how the tests ran on OpenClaw with the
  self-hosted Qwen (`cycle2/solve_01`, `twin2/*`), how they were graded (their own AgentDiff assertions; our triage
  plus judge v2 with the review's intended target as the answer key), and the pilot's open decisions for the PI.
- The Sol round's and the Qwen round's numbers for the "ours" column: `report_01/numbers/concise.json` →
  `equal_budget_muse_final`.
- The self-hosted Qwen is up (endpoint `http://127.0.0.1:18000/v1`, model `qwen3.8-27b`, the key in
  `~/qwen-selfhost/secrets/api_key`, never printed; the OpenClaw-side proxy on port 18778). Solver runs go through
  `openclaw_eval_01/run.py` with `SOLVER_BACKEND=selfhost`, at most 24 in flight.

## Steps

1. Generate the two arms that matter, **N0M and N1M**, with Sonnet 5.5 through Claude Code, using baselines_01's
   exact inputs and its load-feedback rule. 48 tests per arm, 12 per service. Record every session transcript and
   the turns used. Do not tune the prompts.
2. The structural review, blind, in one shuffled pool with about 20 of our tests mixed in, under baselines_01's
   rules: validity, facts exercised properly, look-alike kind, flaws.
3. Run every valid test on OpenClaw with the self-hosted Qwen, 3 trials, the 10-minute budget; grade with their own
   assertions and with our triage plus judge v2 keyed to the review's intended target; draw a blind sample of 30
   trials per arm before any verdict and label it.
4. Report the table of baselines_01's Table 14 for the new arms beside the Muse arms and ours, with denominators;
   the review's findings on what a stronger writer does differently; costs (Claude usage, Muse, Qwen time).

## Deliverable

`grounding/runs/baselines_02/README.md` (status, the question, the setup, the numbers, what differs from the Muse
arms, open points), the inputs and transcripts, the review, the runs' evidence (hidden from ripgrep with `.ignore`).
Message the lead after generation and review (before the runs), and at the end.
