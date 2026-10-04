# Logins for the harnesses under test

The PI's own Claude Code and Codex sessions stay signed in through `~/.claude` and `~/.codex`. The harnesses under
test sign in separately, in homes under `~/.agentdiff-auth` (mode 700, outside the repository):

| Home | What | Used by (planned) |
|---|---|---|
| `~/.agentdiff-auth/claude` | `CLAUDE_CONFIG_DIR` of a separate Claude subscription login | harnesses that drive the official Claude CLI as their model client: Hermes's `claude-subscription-directsdk` plugin (`CLAUDE_SUBSCRIPTION_DIRECTSDK_CONFIG_DIR`), the Codex plugin for Claude models, OpenClaw's Claude CLI transport |
| `~/.agentdiff-auth/claude-oauth-token` | a one-year token from `claude setup-token` (mode 600) | Claude Code runs: `CLAUDE_CODE_OAUTH_TOKEN` with a fresh `CLAUDE_CONFIG_DIR` per run, as in [claudecode_pilot_01](../../runs/claudecode_pilot_01/README.md) |
| `~/.agentdiff-auth/codex` | `CODEX_HOME` of a separate ChatGPT login (file store) | Codex runs |
| `~/.agentdiff-auth/openhands` | `OH_PERSISTENCE_DIR`: OpenHands keeps its own ChatGPT login in `auth/` | OpenHands runs with GPT-6 Sol and 6.1 Sol |
| `~/.agentdiff-auth/openclaw` | `OPENCLAW_STATE_DIR` holding OpenClaw's own ChatGPT login | OpenClaw runs with GPT-6 Sol and 6.1 Sol (copied per attempt, as the Sol round copied `~/.openclaw`'s) |
| `~/.agentdiff-auth/anthropic-api-key` | an Anthropic API key (mode 600), only if the PI chooses it | Sonnet in OpenClaw's and OpenHands's own loops (neither runs Sonnet on the Claude plan in its own loop) |

The PI signs in once per home with [login.sh](login.sh) (`status`, `claude`, `claude-token`, `save-claude-token`,
`codex`, `openhands`, `openclaw`, `anthropic-key`).

The harness installs used for runs live in `~/.agentdiff-harness` (OpenHands SDK 1.51.0 in a Python 3.12
environment); OpenClaw stays at the installed 2026.7.1-2, the version the Qwen and Sol rounds ran on.

## Why two logins can coexist

- **Claude Code** keeps `.credentials.json` under `CLAUDE_CONFIG_DIR` when it is set ("Log in with multiple
  accounts", [authentication](https://code.claude.com/docs/en/authentication)): each directory has its own login.
  `claude setup-token` saves nothing; it prints a token.
- **Codex** keeps `auth.json` under `CODEX_HOME` with `cli_auth_credentials_store = "file"`
  ([auth](https://learn.chatgpt.com/docs/auth)).
- A login in an isolated home is a grant of its own. Checked on 2026-10-03: the helper's status checks left
  `~/.claude/.credentials.json` and `~/.codex/auth.json` byte-identical.

## Rules

- Never copy `~/.claude/.credentials.json` or `~/.codex/auth.json`, or an isolated home's credential file. Both tools
  rotate the refresh token when they refresh; the holder of a stale copy is signed out, or signs the other out.
- Never run a login or logout without the isolated home set (`login.sh` sets it and runs the CLIs in a clean
  environment).
- Never print a token where a transcript can keep it (`save-claude-token` reads it unechoed).
- Per-run isolation passes credentials, never shares state: a fresh config directory per run, authenticated by an
  environment variable.

## Accounts

- This machine's main Claude login reports a Pro plan; sign the isolated login in with the account on the Max plan.
- The ChatGPT plan lapses around 2026-10-06; the ChatGPT logins stop working with it.
