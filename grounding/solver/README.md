# Solver runners and Qwen handoff

The solver executes requests against isolated AgentDiff environments. These runners save evidence; their native assertion scores do not replace grounding judgments. Read [grounding/AGENTS.md](../AGENTS.md) before extending them.

## Entry points

| Use | Entry point |
| --- | --- |
| Original Slack tasks on Bedrock | [slack/run.py](slack/run.py), [Slack guide](slack/README.md) |
| Custom manual Slack suite on Sonnet/Haiku | [slack/compare_manual.py](slack/compare_manual.py) |
| Custom manual Slack suite on Purdue Qwen | [slack/compare_purdue.py](slack/compare_purdue.py) |
| Native Box, Calendar, Linear cases on Purdue Qwen | [box/smoke.py](box/smoke.py), [calendar/smoke.py](calendar/smoke.py), [linear/smoke.py](linear/smoke.py) |

All Qwen runners use [PurdueClient](slack/purdue_client.py) and its [shared rate limiter](slack/purdue_rate_limit.py). The non-Slack entry points share [smoke_runtime.py](../integrations/agentdiff/smoke_runtime.py). They were imported unchanged from commit `3a3ddb12` on `exp/coverage-campaign`; the ongoing campaign and its research conclusions remain on that branch. The corrected Slack integration and historical comparison were already merged in `d16f0e1d`.

The non-Slack CLI is a **native-case smoke runner**, not a compiler for arbitrary generated cases. It selects a numbered benchmark task and installs the domain's fixed seed (`box_default`, `calendar_default`, or `linear_expanded`). Check the task's seed compatibility before selecting another native case. Its read probes check basic environment access, not semantic validity or complete selector accessibility. New custom cases need an explicit seed-installation path and their own validation.

## Local setup

Run from the root of the chosen checkout/worktree. The existing Python environment and `bedrock_llm` checkout can be reused:

```bash
export PYTHONPATH="$PWD/sdk/agent-diff-python:$PWD:/home/yusf/PyProj/bedrock-llm/src"
export DATABASE_URL=postgresql://postgres@127.0.0.1:15432/agentdiff_campaign
export PURDUE_RATE_LIMIT_FILE=/tmp/purdue_genai_rate_limit.json
export PURDUE_RATE_LIMIT_PER_MINUTE=60
```

Export `GENAI_API_KEY` from the existing local credential store without printing it. This machine's gitignored `grounding/.env` uses the name `PURDUE_GENAI_STUDIO_API_KEY`; map that value to `GENAI_API_KEY` for these runners. Worktrees do not automatically inherit gitignored files. Neither credentials nor `.env` belong in commits or evidence.

The local AgentDiff backend must serve `http://127.0.0.1:18001` against the same database. Docker must have the `agent-diff-slack-executor` image; despite its name, the executor supports all four services. Calendar also requires `DATABASE_URL` at import time. Check an existing server before starting another; do not restart or clean up a server owned by another campaign.

## Commands

Offline adapter checks (no provider calls):

```bash
/home/yusf/PyProj/agent-diff/backend/.venv/bin/python -m unittest grounding.tests.test_purdue_client -v
```

One manual Slack case, with a **new** output directory:

```bash
/home/yusf/PyProj/agent-diff/backend/.venv/bin/python -m grounding.solver.slack.compare_purdue \
  --cases W01-single --concurrency 1 \
  --out grounding/runs/qwen_new_trial
```

The Slack runner defaults to the 57-case manual source suite. Its default output points at historical results, so always supply `--out` for a new experiment. Existing completed attempts are skipped; `--retry-infrastructure` retains earlier failed attempts and retries infrastructure failures only. This runner does not call an evaluator.

Non-Slack setup check (installs an isolated template, probes it, then cleans it up; no model calls):

```bash
/home/yusf/PyProj/agent-diff/backend/.venv/bin/python -m grounding.solver.box.smoke \
  --case box_116 --out grounding/runs/qwen_box_prepare --prepare-only
```

For a solver run, omit `--prepare-only` and use another new output directory. Equivalent verified entry points are `grounding.solver.calendar.smoke --case calendar_188` and `grounding.solver.linear.smoke --case linear_0`, each with its own `--out`. `--prepare-only` cleans up its template, so its saved `prepared.json` cannot subsequently be used with `--run-only`.

## Parallel campaigns and evidence

Keep the same absolute `PURDUE_RATE_LIMIT_FILE` and request budget across all local worktrees. Every HTTP attempt, including retries, acquires a shared slot. The limiter is local to this machine; another host or client that bypasses it needs separate coordination. Do not set `PURDUE_RATE_LIMIT_DISABLE=1` for real runs. Separate output directories and UUID-owned environments allow campaigns to coexist; cleanup must remain limited to the environments created by that run.

The defaults are Qwen `qwen3.6:27b`, 16,384 maximum output tokens per call, 40 turns, and a 480-second episode timeout. The client uses provider defaults for thinking and sampling and sends no explicit cache controls. These are the recorded comparison settings, not an assertion about the provider's current model inventory. Provider reasoning and raw responses are retained when supplied, but reasoning is excluded from subsequent conversation text. Requests are saved without authentication headers.

Review the trajectory, final answer, initial/final snapshots, and native diff together. Non-Slack runs also record native assertions; treat those as benchmark outputs, not ground truth. Box binary values in snapshots are represented by length and SHA-256. Calendar sync-token bookkeeping is excluded only from preflight state-stability comparison, not from saved snapshots. The notebook's Linear docs formatter omits argument details; this known baseline limitation is preserved.

Usage records contain provider-reported input/output counts and retry/failure counts. Thinking-token counts are unavailable; zero cache counters are not evidence that the provider did no internal caching. Cost is recorded as zero because this Purdue account has no per-token charge, not because of a provider invoice. Preserve failed attempts and report missing usage rather than silently excluding it.

The [historical Qwen comparison](../runs/purdue_comparison_01/report.md) and its [limitations](../runs/purdue_comparison_01/LIMITATIONS.md) describe the existing results. The earlier comparison predates the reasoning-preservation fix; that missing evidence cannot be reconstructed. The non-Slack import preserves the existing runner rather than changing solver prompts or regrading those results.
