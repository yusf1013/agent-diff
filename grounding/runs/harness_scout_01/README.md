# harness_scout_01: a second real-world agent harness

Session "harness", started by the lead session "RoadMap specialist" on 2026-09-29 from the brief
[grounding/protocols/briefs/harness.md](../../protocols/briefs/harness.md). Rules: [briefs/README.md](../../protocols/briefs/README.md).

## Status

- **Date:** 2026-09-30, 01:20 EDT.
- **Done:** the desk survey (report sections 1-3, sent to the lead); the smoke adapter ([adapter.py](adapter.py),
  [smoke.py](smoke.py), [clock/fakeclock.c](clock/fakeclock.c)); 15 smoke attempts on three tests: Claude Code with
  Sonnet 5.5 (plan) and with the self-hosted Qwen, Codex with Sol (plan: all 4 runs spent; `gpt-6.1-sol` refused, so
  `gpt-6-sol`) and with Qwen; the integration estimates and the recommendation (report sections 4-6).
- **Running:** nothing.
- **Blocked:** nothing. Waiting for the lead's next assignment.
- **Deliverable:** [report.md](report.md).

## Files

| Path | What |
|---|---|
| [report.md](report.md) | The deliverable |
| [adapter.py](adapter.py) | One case through `claude -p` or `codex exec`, on OpenClaw's environment and judge-step helpers |
| [smoke.py](smoke.py) | Runs listed cases (from openclaw_eval_01's `full_03_cases`) through the adapter |
| [clock/fakeclock.c](clock/fakeclock.c) | The LD_PRELOAD wall-clock shift used for Claude Code |
| [summarize.py](summarize.py), [smoke_table.json](smoke_table.json) | The smoke runs as a table |
| `runs/<run>/<case>/attempt-XX/` | Evidence, OpenClaw's judge layout (hidden from ripgrep by `.ignore`) |

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

### Cycle 1 (2026-09-30, 00:00-00:40): the desk survey

- Fetched the providers' pages (Anthropic's Claude Code legal page, the Agent SDK plan article with its June 15
  pause, the consumer terms; OpenAI's Sign in with ChatGPT docs from DevDay 2026-09-29) and the harnesses' own docs
  (OpenCode, Goose, Hermes, Pi via search, Cline, Qwen Code, OpenClaw's installed docs). Report sections 1-3.
- Learned: Sonnet on the Claude plan is only within the terms in Claude Code's own loop; OpenClaw's plan path is
  `claude -p` with OpenClaw's prompt appended. Sol on the plan is allowed in Codex and in the named partners
  (OpenClaw, OpenCode, Pi, Hermes, …). No third-party loop runs all three on the plans.
- A web summarizer echoed my prompt's examples as if they were the page's rules (developers.openai.com/siwc); from
  then on every terms quote was read from the raw page (Markdown twins, curl), not from a summary.
- Sent to the lead. The lead's reply (2026-09-30): proceed with the Sonnet smoke on the shared login with a neutral
  cwd, `--strict-mcp-config`, `--setting-sources` without the user's, `--tools` limited to what a run needs (no web),
  and the init event's tool and server lists in the report; make explicit for the PI (a) the Pro login and (b) the
  choice for the Sonnet round.

### Cycle 2 (00:10-00:40): Claude Code plumbing

- A trivial `claude -p` in a neutral directory with the guardrails: the init event lists tools `Bash, Read, Skill`,
  `mcp_servers: []`, our four skills plus Claude Code's bundled ones, none of the account's synced skills. The shim
  was first on the Bash tool's PATH.
- The session transcript holds the full system prompt (`prompt_snapshot`) and the context attachments. They include
  the login's email address ("The user's email address is …") and "Today's date is …". The adapter flags the email
  and redacts it from stored evidence.
- The clock: Claude Code 2.1.285 is a dynamically linked Bun binary. An LD_PRELOAD shim that also used `setenv`
  deadlocked Bun's allocator at start-up (no output, killed at 180 s); an allocation-free rewrite starts. Shifting all
  three time functions breaks the API ("SSL certificate is not yet valid"); shifting only `clock_gettime` moves
  Claude Code's date (context "Today's date is 2018-06-17") and the shell's `date`, while TLS keeps the real time.
- Hazard found: on the shared login a shifted process thinks the access token is valid for years; a refresh forced by
  a real expiry mid-run would write a 2018-based expiry into the credentials every session shares. The adapter
  starts a shifted run only with more than 20 minutes left on the token. A setup-token login avoids it.

### Cycle 3 (00:30-00:55): Sonnet 5.5 smoke, three tests

- Tests (opaque ids, from openclaw_eval_01's `full_03_cases`, all failed 3 of 3 by OpenClaw's Qwen): AR-LIN-24
  (cover, fact `Cycle.number`), G4-CAL-06 (cover, `Calendar.data_owner`, clock 2018-06-17), P-G4-SLK-04-I11
  (absence probe, `Message.blocks`).
- All three ran end to end: 7-16 s, 2-5 tool calls, $0.03-0.09 each at list (Claude Code's own estimate).
- Sonnet asked on both covers (it listed the target and the decoy and asked which), and on the probe reacted to the
  plain-text message while saying it was "a plain text message rather than a card with blocks".

### Cycle 4 (00:45-01:10): Codex and Qwen

- Codex with Qwen through the self-host's Responses API worked on the first try (AR-LIN-24: 483 s, 23 requests).
  Codex warned it had no metadata for the model; the adapter now sets `model_context_window = 131072`.
- `codex debug models` (no inference) showed the account's catalog without `gpt-6.1-sol`. Plan run 1 with
  `gpt-6.1-sol`: refused, HTTP 400 "The 'gpt-6.1-sol' model is not supported when using Codex with a ChatGPT
  account." Plan runs 2-4 used `gpt-6-sol` (the lead's fallback): 22-45 s each. The copied login was unchanged after
  every run (checked by hash).
- Codex's context carried `current_date 2026-09-29` for the Calendar test: its static binary cannot be shifted.
- Claude Code with Qwen: the first attempt got 401 (Claude Code sends `ANTHROPIC_API_KEY` as `x-api-key`; the
  self-host checks `Authorization: Bearer`); fixed with `ANTHROPIC_AUTH_TOKEN`, relabelled as an infrastructure
  error. Then all three ran (109-270 s), with the shifted clock on Calendar.

### Cycle 5 (01:00-01:14): Codex with Qwen again, and the write-up

- With `model_context_window = 131072` Codex still warns that it has no metadata for the model (the other defaults
  stay generic). The three Codex-Qwen runs took 118-130 s.
- All 11 completed attempts, read against judge v2's notes on OpenClaw's trials: Sol and Qwen took the decoys
  OpenClaw's Qwen took; Sonnet asked on both covers and reacted to the absence probe's plain message with a
  disclosure. Qwen wrote a wrong priority value in all three of its Linear writes. Not judged; plumbing evidence.
- A flag for Codex runs with a test clock records the date Codex showed (`context_date`); added to the two recorded
  Codex Calendar runs afterwards.
- Report sections 4-6 written; the table of attempts comes from [summarize.py](summarize.py).

### Cycle 6 (01:14-01:20): review

- The advisor's review. The three Anthropic quotes the reading rests on were checked on the raw pages (curl, not a
  summarizer): the Agent SDK article (dated 2026-06-16, the June 15 pause banner verbatim), the consumer terms
  (effective 2025-10-08, the automated-access clause), the Claude Code legal page (the developer and end-user
  sentences).
- The current Codex release is 0.159.2 (npm); the smoke used the VS Code extension's 0.155.0-alpha. Installed 0.159.2
  in the scratch folder and listed the account's catalog without inference: it includes `gpt-6.1-sol`. The alpha's
  refusal was most likely a client-version gate; a run on 0.159.2 would confirm it (not spent). 0.159.2 is also a
  static binary, so the clock finding stands.
- The relabelled `claude_qwen_01` attempt 01 now carries a `relabelled_after_run` note, as the backfilled Codex
  clock flags carry theirs.
- Report: the recommendation's first sentence names one harness (Claude Code), with Codex as a conditional add-on for
  Sol and OpenCode as the alternative; the plan's no-overage setting is stated.
