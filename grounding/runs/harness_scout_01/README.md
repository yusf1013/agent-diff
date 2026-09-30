# harness_scout_01: a second real-world agent harness

Session "harness", started by the lead session "RoadMap specialist" on 2026-09-29 from the brief
[grounding/protocols/briefs/harness.md](../../protocols/briefs/harness.md). Rules: [briefs/README.md](../../protocols/briefs/README.md).

## Status

- **Date:** 2026-09-29 (evening, EDT).
- **Done:** reading (AGENTS.md, the PI's notes, the roadmap, the OpenClaw adapter, the toy harness); local inventory
  of installed harnesses; the lead's answers on the budgets (below).
- **Running:** the desk survey (candidates, providers' terms).
- **Blocked:** nothing.
- **Deliverable:** [report.md](report.md) (not written yet).

## The question

How can we run the frozen suite on a second real-world agent harness, one that runs all three solver models within
each provider's terms, and what would connecting it to our runner take? The models:

- the self-hosted Qwen3.8-27B (an OpenAI-compatible endpoint);
- GPT-6.1 Sol on the PI's OpenAI plan;
- Sonnet 5.5 on the PI's Claude plan.

A sub-question from the PI's notes (section E): should Claude's and Codex's own agents (Claude Code, Codex CLI) count
as solvers themselves, and is that the same question as the second harness?

What would answer it: for each candidate, evidence (terms pages with dates, the harness's own documentation, and
for the two best candidates, smoke runs on three of our tests through the curl shim) on which models it can run and
how, whether the plans may be used in it, and what our adapter needs from it: a shell tool, transcripts we can turn
into judge steps, clock control, per-run isolation, a turn time limit, usage reporting.

## Limits for this session (the brief and the lead)

- **Codex on the OpenAI plan:** at most 4 `codex exec` runs in total (3 tests and one retry), whatever their request
  count (the lead, 2026-09-29). Try `gpt-6.1-sol` first; if Codex refuses it, `gpt-6-sol`, and say so.
- **Claude Code with Sonnet 5.5 on the Claude plan:** smoke tests are fine.
- **The self-hosted Qwen:** up for this session (the lead, 2026-09-29), at concurrency 1, directly at the endpoint
  (a harness that talks to it directly bypasses our client-side shared limiter; fine at concurrency 1). Never
  `qwen up` or `qwen down`. Purdue is not used.
- **Muse:** not needed for this study.

## Log

One entry per cycle: what changed, what ran, what was learned.

### Cycle 0 (2026-09-29, 23:30-00:00): orientation

- Read the required documents and the OpenClaw adapter (`grounding/integrations/openclaw/runtime.py`, the curl shim,
  the fake clock, the skills).
- **Installed on this machine:** Claude Code 2.1.285 (a native ELF binary under the npm package, so the Node clock
  shift OpenClaw uses cannot load into it); OpenClaw 2026.7.1-2; Codex CLI in two copies: the system-wide
  `/usr/local/bin/codex` (npm 0.125.0) is broken ("Missing optional dependency @openai/codex-linux-x64"), and the
  working one is bundled with the VS Code extension
  (`~/.vscode-server/extensions/openai.chatgpt-26.917.62051-linux-x64/bin/linux-x86_64/codex`, 0.155.0-alpha.16.3,
  a static musl binary). Not installed: OpenCode, Goose, Aider, Cline/Roo CLIs, Qwen Code, Crush, OpenHands.
- **Codex's transcript** (`~/.codex/sessions/.../rollout-*.jsonl`) records every response item (messages,
  reasoning, tool calls and outputs), per-request token usage (input, cached, output, reasoning) and the plan's
  rate-limit state (`used_percent` of the weekly window, plan type). Its environment context tells the model
  `<current_date>` and `<timezone>`.
- **Model ids:** Codex's model cache (fetched tonight) lists `gpt-6-sol` but not `gpt-6.1-sol`; OpenClaw's refreshed
  catalog lists both.
- **The lead's answers** (2026-09-29): Codex at most 4 runs; try `gpt-6.1-sol` first; the self-host is up for this
  session at concurrency 1.
