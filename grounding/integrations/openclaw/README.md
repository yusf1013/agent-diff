# OpenClaw adapter: AgentDiff cases on a real agent harness

Runs our AgentDiff grounding cases through a real OpenClaw agent (`agentdiff-qwen`, Purdue `qwen3.8:27b`) instead of
the toy ReAct loop, with the same backend, the same API documentation and the same raw JSON.

| Piece | What it does |
|---|---|
| Agent `agentdiff-qwen` in `~/.openclaw/openclaw.json` | Strict model `purdue/qwen3.8:27b` (no fallbacks); own workspace `~/.openclaw/workspace-agentdiff-qwen`; skills limited to `slack`, `box`, `google-calendar`, `linear` (the bundled `gog` skill is excluded); irrelevant tools denied (browser, canvas, media generation, TTS, nodes and node file tools, cron, gateway, message, sessions and sub-agents, skill workshop). Web search and fetch stay on. First-run ritual removed; `USER.md` left as the empty template. |
| Provider `purdue` | OpenAI-compatible, `contextWindow` 65,536 and `maxTokens` 8,192 (Purdue's real limits), key from `PURDUE_GENAI_STUDIO_API_KEY` in `~/.openclaw/.env` (a SecretRef; never written to config). Points at the local proxy. |
| [purdue_proxy.py](purdue_proxy.py) | Local pass-through on `127.0.0.1:18777`. Purdue ends every stream without the final chunk, which Node reports as "terminated" and OpenClaw fails the turn; the proxy re-sends the stream properly. It draws each request from the shared limiter file (cap set with `PURDUE_RATE_LIMIT_PER_MINUTE`; Purdue refuses beyond ~20 requests/minute, answering HTTP 400 "Rate limit exceeded"), retries those refusals, and records full request/response pairs for registered test runs. |
| [build_skills.py](build_skills.py), [skills/](skills/) | One skill per service carrying, verbatim, the toy prompt's service block and API documentation. Google Calendar's docs (38,923 characters) exceed what OpenClaw's `read` returns in one call (~15,900), so its `SKILL.md` holds an endpoint index and the same text split into `references/*.md`. |
| [bin/curl](bin/curl) | Put first on the exec `PATH` for test runs; rewrites the real API base URLs to the run's AgentDiff environment exactly as the toy harness's curl wrapper did. |
| [fake_clock.cjs](fake_clock.cjs) | Calendar runs only: shifts Node's clock so OpenClaw's `session_status` and message timestamps say Sunday 2018-06-17 00:01 Los Angeles, the moment the toy prompt stated. Non-Node processes keep the real clock; the runner flags any Calendar trajectory that could have seen it. |
| [runtime.py](runtime.py) | One attempt: install the case seed, open a fresh environment, build a fresh OpenClaw state directory with only this agent (no channels, no `.env`, empty memory), send the prefixed prompt with `openclaw agent --local --json`, snapshot the state, send "Yes, go ahead." if turn 1 changed nothing and asked a question, record diff, transcript, requests and settings, then delete the environment and template. An attempt whose last model stream Purdue cut (R1) or that timed out after more than a quarter of its turn waiting for the shared rate limiter (R2) is recorded as `infrastructure_error`, so `run.py --retry-infrastructure` reruns it. |

## Start the proxy

```bash
cd /home/yusf/PyProj/agent-diff-coverage-claude
set -a; . /home/yusf/PyProj/agent-diff/grounding/.env; set +a        # provides PURDUE_GENAI_STUDIO_API_KEY
PURDUE_RATE_LIMIT_PER_MINUTE=20 PYTHONPATH=$PWD setsid nohup \
  /home/yusf/PyProj/agent-diff/backend/.venv/bin/python -m grounding.integrations.openclaw.purdue_proxy \
  >> ~/.local/state/agentdiff-openclaw-proxy/proxy.log 2>&1 < /dev/null &
```

The agent then also works interactively, e.g. `openclaw agent --agent agentdiff-qwen --local -m "hello"`
(it needs the proxy running; its API skills need a run's environment variables to reach AgentDiff).

## The self-hosted Qwen (since 2026-09-27)

`runtime.run_attempt(..., backend="selfhost")` points the attempt at the self-hosted Qwen (`qwen3.8-27b`, see
[grounding/solver/README.md](../../solver/README.md)). It writes a `selfhost` provider into the attempt's own
configuration, made from the `purdue` entry, with the model's real limits (131,072-token context, 8,192 output). The
user's `~/.openclaw/openclaw.json` is not changed. Requests go through a second proxy on port 18778, started through
the launcher, which supplies the self-host's key, endpoint and the rate limiter every session shares:

```bash
SOLVER_BACKEND=selfhost python grounding/runs/fact_coverage_02/launch.py \
  grounding.integrations.openclaw.purdue_proxy --backend selfhost
```

`layout="judge"` writes what judge v2 and the scoring read: OpenClaw's raw turn files under `solver/openclaw/`, and
the record's steps in the toy harness's format (`judge_steps`). [openclaw_eval_01](../../runs/openclaw_eval_01/README.md)
runs both.

## Differences from the toy harness that are part of the treatment

- OpenClaw's own system prompt, workspace files (`AGENTS.md`: "When in doubt, ask", "Ask first: … anything that
  leaves the machine") and native tool calling replace the toy ReAct prompt and XML protocol.
- Documentation is read on demand from the skill instead of sitting in the system prompt.
- The prompt carries a domain prefix ("In Box: …"), because OpenClaw does not guess which service is meant.
- OpenClaw compacts the conversation when it nears the 65,536-token window (the toy loop never needed to).
- Each turn may run up to 600 s (OpenClaw's default; the toy loop allowed 480 s and 40 turns).
