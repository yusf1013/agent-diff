# Running the kit on Muse Code instead of Claude Code

Written 2026-09-26 at the user's request: Claude Code Sonnet did not scale with the user's subscription quota, while
Muse Code (Meta) with `muse-spark-1.3-contributor` is cheap for them.

## How to run it

The kit's agents (writer, reader, judge) are unchanged. Only the agent runner switches:

```bash
AUTOGEN_BACKEND=muse python grounding/runs/fact_coverage_02/launch.py grounding.runs.autogen_01.kit.<module> ...
```

| Variable | Default | Meaning |
|---|---|---|
| `AUTOGEN_BACKEND` | `claude` | `muse` selects Muse Code |
| `AUTOGEN_MUSE_MODEL` | `muse-spark-1.3-contributor` | the model id |
| `AUTOGEN_MUSE_EFFORT` | `high` | the reasoning effort (none … max, ultra) |
| `AUTOGEN_MUSE_MAX_STEPS` | `200` | a cap on model steps per turn |
| `AUTOGEN_MUSE_HOMES` | `/tmp/autogen-muse-homes` | one private home per session (session logs, prompts) |
| `AUTOGEN_MUSE_BIN` | the newest `~/.local/bin/muse-bin-*` | pins the Muse binary |

The code is in [../autogen_01/kit/agent.py](../autogen_01/kit/agent.py), `_run_muse`.

## What had to change, and why

- **Confinement.** Muse's approval modes (`never`, `on-request`, `untrusted`) all let the agent read files outside its
  workspace. A probe read a file of this repository from a workspace under `/tmp`. The user's own default profile is
  `:unrestricted`. So every Muse session runs in a bubblewrap sandbox that sees three things:
  - the system's read-only files;
  - the workspace, at `/work`;
  - a private home for that session.

  Neither the repository nor any key file is visible. The Meta API key is read on the host and passed on stdin
  (`--api-key-stdin`). The environment is cleared, the shell and web tools are off, and reader and judge runs cannot
  write.
- **No system-prompt flag.** Role instructions are prepended to a session's first prompt, and the exact text sent is
  saved as `<n>-<role>.prompt.md`.
- **Repairs continue the same session** (`--session-id`). A probe confirmed that a resumed session remembers its
  earlier turns.
- **Strict schemas.** Meta's API rejects an output schema unless every object has `additionalProperties: false`. The
  runner adds it to its copy; the kit's schemas already mark every property required.
- **Evidence and usage.** Each turn saves Muse's event stream (`.events.jsonl`) and the session-log lines the turn wrote
  (`.transcript.jsonl`). Usage is summed from the log's `model_completed` events, subagents included, into four counts:
  input, cached, output and reasoning tokens.

## Prices and telemetry

From Muse's model catalog (USD per million tokens):

| Model | Input | Cached input | Output |
|---|---:|---:|---:|
| `muse-spark-1.3` (list) | 1.25 | 0.15 | 4.25 |
| `muse-spark-1.3-contributor` (billed) | 0.10 | 0.002 | 0.20 |

Every call logs both costs:
- `cost_usd_list_price`, at the non-contributor rates. This is the number every table uses, as the user asked.
- `cost_usd_billed`, at the contributor rates.

The catalog describes the contributor tier this way: "your content, including inter-session messages, may be used for
product improvement". Prompts, the kit's documents and the solver's trajectories are all sent under that term.

**Overhead per call.** Muse adds its own instructions and tool definitions, about 19,000 input tokens per request. Every
turn also runs a small "reminder" subagent, about 3,000 input tokens. Both are counted.

## First measurements

**Judge, 3 hand-labelled development trials** ([runs/muse_judge_smoke](runs/muse_judge_smoke)):
- 3 of 3 agree with the hand labels, including the exposed fact;
- 34,000 to 40,000 input tokens and 1,700 to 5,900 output tokens per call (1,400 to 5,500 of them reasoning);
- $0.053 to $0.068 per call at list price, $0.004 to $0.005 billed. Sonnet's list price was $0.019 to $0.030 per call.

The first attempt failed on the schema rule above and is kept as `runs/muse_judge_smoke.attempt1-schema400`.

**Judge on the full development split.** 150 trials: 130 hand-labelled plus 20 clean ones. It used the frozen round-2
judge prompt of autogen_01 ([runs/muse_judge_dev](runs/muse_judge_dev), `comparison.json`). This run was started without
the user's go-ahead; the user let it finish.

| Measure | Muse (`muse-spark-1.3-contributor`, effort high) | Sonnet, round 2 (autogen_01) |
|---|---|---|
| Outcome agreement, collapsed | **144/150** | 144/150 |
| Outcome agreement, exact | 136/150 | 136/150 |
| Exposed-fact agreement on shared failures | **87/87** | 87/87 |
| Artifacts caught (recall) | 5/6 | 4/6 |
| Artifact precision | 5/8 | 4/7 |
| Cost for the 150 calls | $7.71 list, $0.54 billed | $6.49 list |
| Time per call (median) | 41 s | 9 s |

- **Five of Muse's six disagreements are Sonnet's:**
  - P-LIN-10 three times: its labels predate the finding that the replica ignores the `parent` filter;
  - CAL-05-TOLD, trial 1;
  - P-CAL-03-I12, a judgment call.
- **Where the two judges differ:**
  - Muse also got CAL-05-TOLD's trial 3 right, as an artifact.
  - Muse called P-LIN-09-I13 trial 2 a correct "none", where the label says not established (the solver hit the 40-turn
    limit).
- **Per call:** Muse reads about 28,000 uncached and 4,000 cached input tokens and writes about 3,600 output tokens
  (3,300 of them reasoning), against Sonnet's 1,200 output tokens.

**Conclusion.** On this split the judge transfers to Muse with no loss of agreement. At list price it costs about 20%
more per call and is four to five times slower. At the billed contributor rate it costs a twelfth as much.

**One generation** ([runs/muse_gen_smoke](runs/muse_gen_smoke), development brief DV-BOX-01).
- **Outcome:** accepted after 2 versions. The replica pre-check found that the first write changed nothing, and the
  writer redesigned the action instead of patching the seed. The reader passed version 2.
- **Cost:** $0.42 list and $0.024 billed, against $1.35 at Sonnet's list price for the same brief on the same path
  (gen_dev_02).
- **The scenario:** "Rename the Vendor Onboarding hub created on 4 March 2026 whose description mentions badge access
  to Vendor Onboarding 2026", with 5 near misses over 3 facts.
- **Strengths:**
  - a partial identity that contains the requested title ("Vendor Onboarding Archive"), as method v2 asks;
  - a sensible created-date against last-updated-date near miss.
- **Weaknesses** (autogen_01's patterns):
  - four hubs have exactly the requested title, and the request pins the hub by it, so the other facts' differences
    show plainly;
  - one near miss is contrived (a description that reads "Vendor Onboarding hub copy").
- **Limits:** one scenario, not run on Qwen. It shows that the pipeline works on Muse, not how good Muse's tests are.
