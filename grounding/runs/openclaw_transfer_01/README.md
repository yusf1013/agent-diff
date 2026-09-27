# Do the fact-coverage findings transfer to a real agent harness? (OpenClaw)

Same cases, same backend, same API documentation and model as the toy-harness pilot
([fact_coverage_01](../fact_coverage_01/report.md)); the harness is a real OpenClaw agent instead of the toy ReAct loop.
Setup and harness differences: [integrations/openclaw](../../integrations/openclaw/README.md).

Start with [report.md](report.md): the answer, claim by claim, with evidence links.

| Path | Contents |
|---|---|
| [report.md](report.md) | The transfer report |
| [report_data.py](report_data.py) | Prints every number cited in the report from the run records and labels |
| [run.py](run.py) | Runs cases through OpenClaw (one isolated state directory and one AgentDiff environment per attempt); `--variant verify` adds one rule to the workspace's `AGENTS.md` |
| [toy_run.py](toy_run.py) | Runs cases through the toy harness with the pilot's own runner (baseline for new cases) |
| [cases_repaired.py](cases_repaired.py), [cases/](cases/) | CAL-02 and CAL-11 rebuilt so the Calendar replica lists their weekly series (the originals are invisible to most list calls in both harnesses) |
| [analyze.py](analyze.py) | Grades turn 1 with the pilot's attribution and compares every report claim with the toy results; Slack grading, follow-up outcomes, per-fact counts (strict and engaged), clock audit, variant comparison |
| [manual_labels.json](manual_labels.json), [disclosure_labels.json](disclosure_labels.json) | Manual corrections after reading replies and trajectories; how each wrong action's reply disclosed it |
| [review.py](review.py), [disclosure.py](disclosure.py) | What a reviewer reads per run; wrong actions with reply and mismatch-mentioning reasoning |
| [behaviors.py](behaviors.py) | Credential probing, web tools, file and memory writes, exec-failure notices, reverts |
| [streams.py](streams.py), [infra.py](infra.py) | Provider stream cuts and output-limit stops; the infrastructure rules (R1 provider hang, R2 rate-limit timeout) that mark attempts for rerun |
| [compact.py](compact.py), [cleanup.py](cleanup.py) | Remove duplicate evidence from finished attempts; remove environments/templates left by an interrupted run (only its own) |
| [runs/](runs/) | `t1` + `t1r`, `t2`: OpenClaw trials 1 and 2 (190 cases + 6 repaired Calendar cases each; `*_retry.log`: reruns of infrastructure failures); `verify1`: one trial with the `verify` rule; `noask2`: the 88 presupposing and told cases without the workspace's ask instructions (`noask1`: stopped after 4 cases because it had left `SOUL.md`'s ask line in place); `toy_repaired_t1`, `toy_repaired_t2`: the repaired Calendar cases on the toy harness; `smoke_*`: setup checks; `t0_pre_calendar_fix`: first 25 attempts, before the Calendar skill was split (not used) |

Each attempt keeps the toy layout (`case.json`, `execution_summary.json`, `environment/{initial,final}_state.json`,
`diff_run.json`, `solver/final_response.md`, `solver/<CASE>.json`) plus `environment/followup_state.json` and
`solver/followup_response.md` when "Yes, go ahead." was sent, `solver/openclaw_turn*.{json,stderr.txt}`,
`solver/config.json` (effective settings), `solver/requests.tar.xz` (every model request and response through the proxy)
and `solver/openclaw_sessions.tar.xz` (OpenClaw's own transcript and trajectory).

## Reproduce

```bash
cd /home/yusf/PyProj/agent-diff-coverage-claude
export PYTHONPATH=$PWD/sdk/agent-diff-python:$PWD:/home/yusf/PyProj/bedrock-llm/src
# start the proxy first (see integrations/openclaw/README.md), then:
/home/yusf/PyProj/agent-diff/backend/.venv/bin/python -m grounding.runs.openclaw_transfer_01.run \
    --out grounding/runs/openclaw_transfer_01/runs/<new dir> --cases BOX-01 CAL-01 --concurrency 4
python3 -m grounding.runs.openclaw_transfer_01.analyze grounding/runs/openclaw_transfer_01/runs/t1 [runs/t2 ...]
```
