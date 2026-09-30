# harness_scout_01: which second harness, and how to connect it

Brief: [grounding/protocols/briefs/harness.md](../../protocols/briefs/harness.md). Log of every cycle: [README.md](README.md).

## Status

- **2026-09-30, 00:40 EDT.** Desk survey done (sections 1 to 3). Smoke tests, integration estimates and the
  recommendation are in progress (sections 4 to 6 are placeholders until then).

## The question

Which real-world agent harnesses, other than OpenClaw, can run all three solver models within each provider's terms,
and what would connecting each to our runner take? The models: the self-hosted Qwen3.8-27B (an OpenAI-compatible
endpoint), GPT-6.1 Sol on the PI's OpenAI plan, Sonnet 5.5 on the PI's Claude plan. And: should Claude's and Codex's
own agents count as solvers?

## 1. The providers' terms (fetched 2026-09-30)

### Anthropic: the Claude plan

| Source | What it says |
|---|---|
| [Claude Code, Legal and compliance](https://code.claude.com/docs/en/legal-and-compliance) (no date on the page) | "**OAuth authentication** is intended exclusively for purchasers of Claude Free, Pro, Max, Team, and Enterprise subscription plans and is designed to support ordinary use of Claude Code and other native Anthropic applications." "Anthropic does not permit third-party developers to offer Claude.ai login into their own applications, or to route requests through Free, Pro, or Max plan credentials on behalf of their users. Moreover, developers may not collect, store, or intermediate Claude.ai credentials or session tokens." It does not "prevent an end user from signing in to the unmodified Claude Code binary with their own Claude subscription." |
| [Use the Claude Agent SDK with your Claude plan](https://support.claude.com/en/articles/15036540-use-the-claude-agent-sdk-with-your-claude-plan) (updated 2026-06-16) | Banner: "Update June 15: We're pausing the changes to Claude Agent SDK usage described below. For now, nothing has changed: Claude Agent SDK, `claude -p`, and third-party app usage still draw from your subscription's usage limits." The paused plan would have moved `claude -p` and Agent SDK use to a monthly credit billed at API rates beyond it. |
| [Consumer Terms](https://www.anthropic.com/legal/consumer-terms) (effective 2025-10-08) | Prohibits accessing the Services "through automated or non-human means, whether through a bot, script, or otherwise", "except when you are accessing our Services via an Anthropic API Key or where we otherwise explicitly permit it." |
| [Using Claude Code with your Pro or Max plan](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan) (updated 2026-08-19) | Plan limits are shared between Claude and Claude Code. |
| Third-party harness docs: [Hermes Agent](https://github.com/NousResearch/hermes-agent/blob/main/website/docs/integrations/providers.md), Pi's `providers.md` (v0.86.1, via search), [OpenCode](https://opencode.ai/docs/providers/) | Hermes: its Claude OAuth path "routes as Claude Code" and "only works on a Claude Max plan with purchased extra usage credits"; the base allowance is never used. Pi: Claude Pro/Max login works, but since 2026-04-04 third-party harness use is billed per token as extra usage. OpenCode: "There are plugins that allow you to use your Claude Pro/Max models with OpenCode. Anthropic explicitly prohibits this." (removed from OpenCode as of 1.3.0). |

**Reading.** On the Claude plan, only Claude Code's own binary is plainly within the terms and draws on the plan's
allowance, including headless `claude -p` (the June 15 note names it). `claude -p` is the "explicit permission" for
scripted use that the consumer terms leave room for. A third-party harness running its own agent loop with Claude
plan credentials is either prohibited (the legal page) or billed per token as extra usage (Hermes, Pi), so it saves
nothing over an API key. OpenClaw's own docs say "Anthropic staff told us" Claude CLI reuse is allowed: hearsay, but
consistent with the above, because OpenClaw's plan path runs `claude -p` (section 3).

### OpenAI: the ChatGPT plan

| Source | What it says |
|---|---|
| [Sign in with ChatGPT, Quickstart](https://developers.openai.com/siwc/quickstart.md) (DevDay, 2026-09-29) | "Eligible ChatGPT Plus and Pro users can use their ChatGPT plan for AI requests in participating apps and manage app usage and access in ChatGPT settings." "ChatGPT plan usage is available to all open-source partners and selected private clients." For open-source developers, the flow "registers your client and issues OAuth credentials for eligible Responses API requests, without a client secret or partner API key." |
| [ChatGPT plan usage, Overview](https://developers.openai.com/siwc/token-sharing-open-source.md) and [Models and inference](https://developers.openai.com/siwc/token-sharing-open-source/models-and-inference.md) | Open-source and locally hosted apps; per-app settings and limits; the example request uses `"model": "gpt-6.1-sol"`. [Preview limitations](https://developers.openai.com/siwc/token-sharing-open-source/preview-limitations.md): Responses API only, `store: false`, `stream: true`, no `temperature`/`max_output_tokens`. |
| [Using your ChatGPT plan in other apps and sites](https://help.openai.com/en/articles/20001542-using-your-chatgpt-plan-in-other-apps-and-sites) (help center; blocked to automated fetch, content from the search index) | Plus or Pro users; open-source examples "OpenCode, OpenClaw, Pi by Earendil, and T3"; commercial tools "Hyperagent, Nous Research - Hermes Agent, Vorflux, Amp, Dactyl, Kilo Code, Warp, Conductor, Devin by Cognition, Notion, and Vercel"; a weekly usage limit can be set per app. |
| [Codex authentication](https://learn.chatgpt.com/docs/auth) | Codex CLI signs in with ChatGPT by default; "Use API key authentication for programmatic Codex CLI workflows, such as CI/CD jobs." (advice for CI, not a prohibition). |
| [DevDay 2026 live blog](https://simonwillison.net/2026/Sep/29/openai-devday-2026-live-blog/) (2026-09-29) | GPT-6.1 Sol announced; "Sign in with ChatGPT, which lets people sign into your app and use the tokens they are paying for already." |

**Reading.** On the ChatGPT plan, Codex CLI (OpenAI's own) is plainly allowed, and since 2026-09-29 so are the named
partner harnesses, OpenClaw and OpenCode among them. The PI's plan shows as `prolite` in Codex's rate-limit record;
whether "Pro Lite" counts as "Pro" for Sign in with ChatGPT is not stated. OpenClaw's GPT login already works (the
lead's Sol round).

### The self-hosted Qwen

Open weights on the PI's own hardware: no provider terms apply. Any harness that speaks the OpenAI Chat Completions
API can use it; vLLM 0.30 may also serve the Responses and Anthropic Messages APIs (checked in section 4).

## 2. The candidates

"Plan" means within the provider's terms and drawing on the plan's allowance. Installed means on this machine.

| Harness | Qwen (self-host) | Sol on the ChatGPT plan | Sonnet on the Claude plan | Headless run, transcript | Clock control | Notes |
|---|---|---|---|---|---|---|
| **OpenClaw** (2026.7.1-2, installed; the current harness) | yes (done) | yes, in its own loop (`agentRuntime: openclaw`); a named partner | only through its `claude-cli` backend, which runs `claude -p` (section 3) | `openclaw agent --local --json`; session JSONL | Node `--require` clock shift (bash keeps the real clock) | the reference |
| **Claude Code** (2.1.285, installed) | through `ANTHROPIC_BASE_URL` to an Anthropic-compatible endpoint (vLLM or a translating proxy); to test | no (only with an API key behind a translating gateway) | **yes**: the unmodified binary, `claude -p` | `claude -p --output-format stream-json --verbose`: every message, tool call, result and per-request usage; session JSONL | the date comes from `new Date()` in a dynamically linked binary: an LD_PRELOAD clock shim may work (to test; TLS may object) | native skills (`SKILL.md`), subagents; widely used |
| **Codex CLI** (0.155.0-alpha, bundled with the VS Code extension; the npm copy in /usr/local is broken) | through a custom `model_providers` entry (Responses API); to test | **yes**: OpenAI's own | no | `codex exec --json`; rollout JSONL with reasoning items, tool calls, per-request usage and the plan's `used_percent` | the date comes from the system clock in a static musl binary: no LD_PRELOAD; no override found | native skills; widely used |
| **OpenCode** (not installed) | yes (`@ai-sdk/openai-compatible`) | yes, native ChatGPT Plus/Pro login; a named partner | no: "Anthropic explicitly prohibits this"; API key only | `opencode run --format json`, `opencode export` (JSON), `opencode stats` | not checked | the most-starred open-source coding agent |
| **Goose** (not installed) | yes (custom OpenAI-compatible provider) | only through `codex-acp`, i.e. Codex's own loop | only through `claude-acp`, i.e. Claude Code's own loop | `goose run`; session export | not checked | its CLI providers "use their own built-in tools", not Goose's |
| **Hermes Agent** (Nous Research; not installed) | yes (custom endpoint) | yes (ChatGPT OAuth); a named partner | Max plus purchased extra usage only, billed as extra usage | not checked | not checked | a personal agent like OpenClaw |
| **Pi** (Earendil; not installed) | yes | yes; a named partner | login works, billed per token as extra usage | print and RPC modes (not checked) | not checked | OpenClaw embeds Pi's SDK, so it is not a distinct harness |
| **Cline CLI** (not installed) | yes | yes (`openai-codex` OAuth, since 2026-01-22; not in the partner list) | through a "Claude Code" provider (not checked) | headless mode (not checked) | not checked | |
| **Qwen Code** (not installed) | yes (`OPENAI_BASE_URL`) | no | no | `qwen -p --output-format json/stream-json` | not checked | |
| **Aider** (not installed) | yes (LiteLLM) | no | no | not an autonomous tool loop (edits files; shell commands on confirmation) | not checked | not a fit for API tasks |

**No third-party harness runs all three models within the terms in its own agent loop.** Sonnet on the plan always
means Claude Code's loop: directly, or wrapped by OpenClaw (`claude-cli`), Goose (`claude-acp`) or Cline. Sol on the
plan is open to Codex and to the named partners (OpenClaw, OpenCode, Pi, Hermes, Kilo Code, Amp).

## 3. What "Sonnet on OpenClaw" would be

From OpenClaw's installed docs (`docs/providers/anthropic.md`, `docs/gateway/cli-backends.md`):

- OpenClaw reaches the Claude plan only through its `claude-cli` backend: "OpenClaw's Claude CLI backend runs the
  installed Claude Code CLI in non-interactive print mode (`claude -p`)."
- The launch is `claude -p --output-format stream-json --include-partial-messages --verbose --setting-sources user
  --allowedTools mcp__openclaw__* --disallowedTools ScheduleWakeup,CronCreate,Bash(run_in_background:true),Monitor`,
  with OpenClaw's system prompt **appended** to Claude Code's (`--append-system-prompt-file`), skills passed as a
  temporary Claude Code plugin (`--plugin-dir`), and OpenClaw's tools offered through a loopback MCP bridge.
  Claude Code's own tools (Bash, Read, Edit, …) stay; Claude Code compacts its own context.
- OpenClaw's docs call CLI backends "a safety net for 'always works' text responses, not a primary path".
- The alternative that keeps OpenClaw's own loop is an Anthropic API key (list price; report_concise Table 18
  estimates about $263 per 1,006-case round for Sonnet 5 and 5.5 at Qwen's token profile).

So a Sonnet round "on OpenClaw" on the plan is Claude Code's agent loop with OpenClaw's prompt and tools added. If
the second harness is Claude Code, the two Sonnet rounds would share one loop. The same holds for OpenClaw's default
for `openai/*` models, which hands turns to the Codex app-server; the lead's adapter already sets
`agentRuntime: openclaw` to keep OpenClaw's own loop for Sol.

## 4. Smoke tests

In progress.

## 5. Integration estimates

In progress.

## 6. Recommendation

In progress.
