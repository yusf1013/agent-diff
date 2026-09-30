# sol_eval_01: GPT-6.1 Sol on OpenClaw, the Muse-written half of the suite

## Status

- **2026-09-30 00:00 (started):** the regular tests of the Muse-written half are running (`runs/regular_p4`, then
  `runs/regular_6b`), 3 trials each, 10 in flight; the policy units follow automatically (`runs/run_policy.sh`).
  Judging, the blind sample and the scores come after the runs.
- The pilot (32 regular tests, one trial each) is in `../sol_pilot_01/runs/pilot_01`: 31 completed, 1 failed on
  the clock problem below; median 37 s per run, about 45k input tokens (mostly cached) and 350 output tokens.
- **Judging and scoring (session `sol_score`, branch `exp/sol_score-01`), 2026-09-30 01:05:**
  - **Done:** the question below; one finding reported to the lead and fixed by the lead (provider stalls, in the
    log).
  - **Running:** nothing of mine. The runs are the lead's: `regular_p4` is about 80% done.
  - **Next:** the kit copies with regression tests on Qwen's records (no model calls); then `regular_p4` gets its
    blind labels, judge and score.
  - **Blocked:** nothing.

## The questions (session sol_score)

How can we measure, under the Qwen round's judge (v2 on Muse), rulings and 10-minute budget, what GPT-6.1 Sol shows
on the Muse-written half of the suite, and set it beside Qwen's results on the same tests?

1. **Exposure:** which tests expose a fact, and how many facts at detect@3 and detect@1, per service and form? How
   do the failures happen?
2. **Judge accuracy:** how accurate is judge v2 on Sol's runs, against 180 blind trials labelled by hand before any
   verdict?
3. **Policy:** what does the fixed rule (`policy.pooled_decision`) decide in the eight policy cells over the
   Muse-parent units, and what does the per-fact view show?
4. **Everything else:** awareness remarks, timings, tokens (input, cached, output, reasoning), infrastructure errors
   and surprises.

Test validity, test difficulty, solver failures and judge errors are kept apart; every rate has its denominator.

## What runs

The second agent of the roadmap's final evaluation (goal 1: "more models and harnesses"): **GPT-6.1 Sol** on the
PI's OpenAI plan, in the same OpenClaw harness as the Qwen round of [openclaw_eval_01](../openclaw_eval_01/README.md),
on the tests written by Muse. The Sonnet-written half is being regenerated with Muse (the `regen` session,
[brief](../../protocols/briefs/regen.md)); its Sol runs follow once that suite exists.

| Set | Cases | Where the cases come from | Runs |
|---|---:|---|---:|
| Regular, Phase 4 (autogen_02) | 148 | `openclaw_eval_01/suite_opaque/cases`, the final manifest's `full_02`/`full_03` cases with `G4-` ids | 444 |
| Regular, 6b (completion_01) | 136 | `completion_01/suite/cases`, the manifest's `full_04` cases | 408 |
| Absence units | 125 | the final manifest's policy units with `G4-` parents and all of 6b's, copied to `cases/policy_absence` | 375 |
| Underspecified units | 96 | the same, `cases/policy_underspecified` | 288 |

`cases/selection.json` and `cases/policy_selection.json` record the selection. The final manifest is
`report_01/numbers/concise.json` → `final_execution_keys`.

**Left out: the ten G4-LIN-08 tests and its six policy units.** They run under a test-side clock of 2026-10-16,
and the OpenAI login token expires on 2026-10-10: under the fake clock OpenClaw's auth code sees an expired login
and the run fails before the first model call ("Unknown model"). Options for later: shift that scenario's seed
dates back instead of its clock, or run those 16 with an API key.

## The harness, and what differs from the Qwen round

The adapter's `openai` backend (`grounding/integrations/openclaw/runtime.py`, `BACKENDS["openai"]`):

- **OpenClaw's own agent loop** (`agentRuntime.id: "openclaw"`). OpenClaw's default would hand `openai/*` turns
  to a bundled Codex engine, a different harness.
- **Authentication:** the ChatGPT login profile (`openclaw models auth login --provider openai --device-code`,
  done by the PI on 2026-09-29) is copied from `~/.openclaw`'s main agent store into each attempt's agent store,
  together with a refreshed model catalog (`~/.openclaw-runs/openai-catalog.json`). The token lasts until
  2026-10-10 and nothing in a run refreshes it. No proxy: OpenClaw talks to OpenAI itself.
- **Thinking level "medium", set explicitly.** The Qwen round ran at OpenClaw's "medium" (its fallback for a
  reasoning model on a custom provider). For GPT models OpenClaw's fallback label is "off", which sends no
  reasoning setting and leaves the model at OpenAI's default effort (it still reasons: 126 reasoning tokens on a
  one-line arithmetic prompt, against 116 at explicit medium). Setting medium explicitly keeps one label for both
  rounds. Each run records its reasoning tokens.
- **Usage** comes from OpenClaw's session transcript (input, cached input, output, reasoning tokens per request),
  not from a proxy. There is no per-token charge on the plan.
- **The leak guard** reads the transcript's opening (working directory, model settings, stored skill prompts, first
  user message) instead of the first proxied request.
- **Infrastructure rule R3:** a turn that ends without an answer envelope, or with a provider rate-limit or quota
  message, is an infrastructure error and is re-run (`--retry-infrastructure`), never scored.
- **Time budget:** 10 minutes per turn, OpenClaw's own limit ([the PI's rule](../../protocols/roadmap.md)).
- Everything else is the Qwen round's: the neutral state directory and agent id, the curl shim, the skills, the
  Calendar fake clock, the prompt prefix, no follow-up turn, the judge layout.

## Commands

```bash
L="backend/.venv/bin/python grounding/runs/fact_coverage_02/launch.py"
$L grounding.runs.openclaw_eval_01.run --backend openai --trials 3 --concurrency 10 \
    --out grounding/runs/sol_eval_01/runs/regular_p4 --cases-dir grounding/runs/openclaw_eval_01/suite_opaque/cases \
    --cases $(cat grounding/runs/sol_eval_01/cases/regular_p4.txt)                     # runs/run_regular.sh
$L grounding.runs.openclaw_eval_01.run --backend openai --trials 3 --concurrency 10 \
    --out grounding/runs/sol_eval_01/runs/policy_absence --cases-dir grounding/runs/sol_eval_01/cases/policy_absence
```

Judging and scoring follow openclaw_eval_01's commands (judge v2 on Muse, the blind sample drawn before any
verdict and labelled by a coding agent, `adjudicate`, the policy decision per cell). The session sol_score ran them
through its kit, which reuses the pipeline code unchanged and copies only what has hard-wired paths:

```bash
L="backend/.venv/bin/python grounding/runs/fact_coverage_02/launch.py"
S=grounding/runs/sol_eval_01
$L grounding.runs.sol_eval_01.kit.score regress; $L grounding.runs.sol_eval_01.kit.policy regress  # copies = Qwen's files
$L grounding.runs.sol_eval_01.kit.view regular_p4/t1/G4-BOX-01 [--overview] [--steps 3,5]  # evidence only, for labels
$L grounding.runs.sol_eval_01.kit.label KEY OUTCOME [--exposed F] [--acted ID] [--mechanism M] --note "..."
$L grounding.runs.sol_eval_01.kit.judge_trials SET [--add-retried]             # eval/judge_SET.trials.json
AUTOGEN_BACKEND=muse $L grounding.runs.autogen_02.kit.judge2 run --trials $S/eval/judge_SET.trials.json \
    --out $S/eval/judged_SET --concurrency 6
$L grounding.runs.autogen_02.kit.judge2 compare --out $S/eval/judged_SET --labels $S/eval/labels_SET/SET_blind.json --name blind
$L grounding.runs.autogen_02.kit.phase4 score $S/runs/SET $S/cases/SET/suite.json $S/eval/judged_SET --json $S/eval/SET.score.json
$L grounding.runs.sol_eval_01.kit.score adjudicate SET; $L grounding.runs.sol_eval_01.kit.score combine
$L grounding.runs.sol_eval_01.kit.policy decide                                  # eval/policy_decisions.json
$L grounding.runs.sol_eval_01.kit.compare_qwen; $L grounding.runs.sol_eval_01.kit.observe; $L grounding.runs.sol_eval_01.kit.cost
```

## Results

*To be written by the sol_score session once the sets are judged and scored.*

## Log (session sol_score)

- **2026-09-30 00:40-01:05, orientation.** I read the brief, the PI's notes, the roadmap, the concise report and the
  Qwen round's README, and the machinery: phase4, judge2, adjudicate, rulings, policy and combine.
  - **Found: provider stalls were charged to Sol's budget.** Three `regular_p4` trials ended with termination
    "timeout" after 132-179 s. OpenClaw's stderr says "LLM idle timeout (120s): no response from model": a model
    request had been silent for 120 s.
    - The runner had recorded them as completed, and `rulings.over_budget` would have counted them as the solver's
      10-minute budget failures.
    - None of Qwen's 195 timeouts in the final runs is shorter than 590 s, so the Qwen round never hit this.
    - I reported it. The lead made it infrastructure rule R3 (commit fd38a82dec). `kit/reclassify_stalls.py`
      reclassifies the earlier stalls before the retry pass, which re-runs them.
    - Scoring treats a stall as an infrastructure void to be re-run, never as a budget failure, and reports the
      count per set.
  - **Sol's reasoning is not visible.** Its tool steps carry no thinking, and about a fifth have visible text.
    - The judge therefore sees Sol's commands, the responses, the final answer and the diff, but not its reasoning
      as it saw Qwen's.
    - Awareness remarks can only be measured on visible text.
    - Mechanisms that rest on reasoning (saw-mismatch-accepted against skipped-check) get less evidence.
