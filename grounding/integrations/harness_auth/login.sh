#!/usr/bin/env bash
# Logins for the harnesses under test, each kept in its own home under ~/.agentdiff-auth, never in ~/.claude or
# ~/.codex, so the PI's own Claude Code and Codex sessions stay signed in.
#
#   bash grounding/integrations/harness_auth/login.sh status             # what is signed in where (reads only)
#   bash grounding/integrations/harness_auth/login.sh claude             # Claude subscription login (browser)
#   bash grounding/integrations/harness_auth/login.sh claude-token       # a one-year token for per-run Claude Code
#   bash grounding/integrations/harness_auth/login.sh save-claude-token  # paste that token into its file, unechoed
#   bash grounding/integrations/harness_auth/login.sh codex              # ChatGPT subscription login (device code)
#   bash grounding/integrations/harness_auth/login.sh openhands          # ChatGPT login for OpenHands (device code)
#   bash grounding/integrations/harness_auth/login.sh openclaw           # ChatGPT login for OpenClaw (device code)
#   bash grounding/integrations/harness_auth/login.sh anthropic-key      # an Anthropic API key, pasted unechoed
#
# Rules (README.md): never copy ~/.claude/.credentials.json or ~/.codex/auth.json (a copy that refreshes rotates the
# refresh token and signs the other holder out); never run a login or logout without the isolated home set; never
# print a token where a transcript can keep it.
set -euo pipefail

ROOT="${AGENTDIFF_AUTH_ROOT:-$HOME/.agentdiff-auth}"
CLAUDE_HOME_ISO="$ROOT/claude"                 # CLAUDE_CONFIG_DIR of the isolated Claude login
CLAUDE_TOKEN_FILE="$ROOT/claude-oauth-token"   # CLAUDE_CODE_OAUTH_TOKEN for per-run Claude Code isolation
CODEX_HOME_ISO="$ROOT/codex"                   # CODEX_HOME of the isolated ChatGPT login
OPENHANDS_ISO="$ROOT/openhands"                # OH_PERSISTENCE_DIR: OpenHands keeps its ChatGPT login in auth/ here
OPENCLAW_ISO="$ROOT/openclaw"                  # OPENCLAW_STATE_DIR of OpenClaw's own ChatGPT login
ANTHROPIC_KEY_FILE="$ROOT/anthropic-api-key"   # an API key, only if the PI chooses that route for Sonnet
OPENHANDS_PY="${OPENHANDS_PY:-$HOME/.agentdiff-harness/openhands/bin/python}"
OPENCLAW_BIN="${OPENCLAW_BIN:-$(command -v openclaw)}"   # the installed 2026.7.1-2, the version Qwen and Sol ran on
CLAUDE_BIN="${CLAUDE_BIN:-$(command -v claude)}"
newest_codex() {   # the installed Codex with the highest version (VS Code's bundled copies; /usr/local's is broken)
  for c in "$HOME"/.vscode-server/extensions/openai.chatgpt-*-linux-x64/bin/linux-x86_64/codex \
           "$HOME"/.vscode/extensions/openai.chatgpt-*-linux-x64/bin/linux-x86_64/codex; do
    [ -x "$c" ] && printf '%s %s\n' "$("$c" --version 2>/dev/null | awk '{print $2}')" "$c"
  done | sort -V | tail -1 | cut -d' ' -f2-
}
CODEX_BIN="${CODEX_BIN:-$(newest_codex)}"
MAIN_FILES=("$HOME/.claude/.credentials.json" "$HOME/.codex/auth.json")

case "$ROOT" in
  "$HOME/.claude"* | "$HOME/.codex"*) echo "refusing: $ROOT is inside a main login home" >&2; exit 2 ;;
esac

# A clean environment: only what the CLIs need, plus the one variable that selects the isolated home.
clean() { env -i HOME="$HOME" PATH="$PATH" TERM="${TERM:-xterm-256color}" LANG="${LANG:-C.UTF-8}" \
              ${DISPLAY:+DISPLAY="$DISPLAY"} ${BROWSER:+BROWSER="$BROWSER"} "$@"; }

fingerprints() {
  for f in "${MAIN_FILES[@]}"; do
    if [ -f "$f" ]; then printf '%s  %s\n' "$(sha256sum "$f" | cut -c1-12)" "$f"; else printf 'absent  %s\n' "$f"; fi
  done
}

check_main_untouched() {   # $1: the fingerprints taken before
  local after; after="$(fingerprints)"
  if [ "$1" = "$after" ]; then
    echo "main logins untouched: ~/.claude/.credentials.json and ~/.codex/auth.json are byte-identical"
  else
    echo "note: a main credentials file changed meanwhile (normally your own sessions refreshing a token):"
    diff <(echo "$1") <(echo "$after") || true
  fi
  printf 'main Claude login: '
  login_line "$(clean "$CLAUDE_BIN" auth status --json 2>/dev/null || true)"
}

login_line() {   # one line from `claude auth status --json` (it exits non-zero when signed out)
  python3 -c 'import json,sys
try: d = json.loads(sys.argv[1])
except Exception: print("unknown"); sys.exit()
print("signed in |", d.get("subscriptionType"), "|", d.get("orgName")) if d.get("loggedIn") else print("not signed in")' "$1"
}

status() {
  echo "isolated root: $ROOT"
  printf 'isolated Claude login (%s): ' "$CLAUDE_HOME_ISO"
  if [ -d "$CLAUDE_HOME_ISO" ]; then
    login_line "$(clean CLAUDE_CONFIG_DIR="$CLAUDE_HOME_ISO" "$CLAUDE_BIN" auth status --json 2>/dev/null || true)"
  else
    echo "not created"
  fi
  printf 'Claude run token (%s): ' "$CLAUDE_TOKEN_FILE"
  if [ -s "$CLAUDE_TOKEN_FILE" ]; then echo "present, mode $(stat -c %a "$CLAUDE_TOKEN_FILE")"; else echo "absent"; fi
  printf 'isolated ChatGPT login (%s, %s): ' "$CODEX_HOME_ISO" "$("$CODEX_BIN" --version 2>/dev/null)"
  if [ -d "$CODEX_HOME_ISO" ]; then
    { clean CODEX_HOME="$CODEX_HOME_ISO" "$CODEX_BIN" login status 2>&1 || true; } | head -1
  else
    echo "not created"
  fi
  printf 'OpenHands ChatGPT login (%s): ' "$OPENHANDS_ISO"
  if ls "$OPENHANDS_ISO"/auth/*.json >/dev/null 2>&1; then echo "present"; else echo "absent"; fi
  printf 'OpenClaw ChatGPT login (%s): ' "$OPENCLAW_ISO"
  if [ -s "$OPENCLAW_ISO/agents/main/agent/openclaw-agent.sqlite" ]; then echo "store present"; else echo "absent"; fi
  printf 'Anthropic API key (%s): ' "$ANTHROPIC_KEY_FILE"
  if [ -s "$ANTHROPIC_KEY_FILE" ]; then echo "present, mode $(stat -c %a "$ANTHROPIC_KEY_FILE")"; else echo "absent"; fi
  echo "main logins (fingerprints only):"; fingerprints | sed 's/^/  /'
}

mkhome() { mkdir -p "$1"; chmod 700 "$ROOT" "$1"; }

cmd="${1:-status}"
case "$cmd" in
  status) status ;;
  claude)
    mkhome "$CLAUDE_HOME_ISO"; before="$(fingerprints)"
    echo "Signing in to the Claude subscription in $CLAUDE_HOME_ISO. Pick the account on the Max plan."
    clean CLAUDE_CONFIG_DIR="$CLAUDE_HOME_ISO" "$CLAUDE_BIN" auth login --claudeai
    check_main_untouched "$before"; status ;;
  claude-token)
    mkhome "$CLAUDE_HOME_ISO"; before="$(fingerprints)"
    echo "A one-year token prints at the end. Copy it, then run: bash $0 save-claude-token"
    clean CLAUDE_CONFIG_DIR="$CLAUDE_HOME_ISO" "$CLAUDE_BIN" setup-token
    check_main_untouched "$before" ;;
  save-claude-token)
    mkdir -p "$ROOT"; chmod 700 "$ROOT"
    read -rsp "Paste the token (not echoed), then Enter: " t; echo
    [ -n "$t" ] || { echo "empty; nothing saved" >&2; exit 1; }
    (umask 077; printf '%s' "$t" > "$CLAUDE_TOKEN_FILE"); unset t
    echo "saved to $CLAUDE_TOKEN_FILE (mode $(stat -c %a "$CLAUDE_TOKEN_FILE"))" ;;
  codex)
    mkhome "$CODEX_HOME_ISO"; before="$(fingerprints)"
    printf 'cli_auth_credentials_store = "file"\n' > "$CODEX_HOME_ISO/config.toml"
    echo "Signing in to ChatGPT in $CODEX_HOME_ISO with a device code: open the link it prints and enter the code."
    clean CODEX_HOME="$CODEX_HOME_ISO" "$CODEX_BIN" login --device-auth
    check_main_untouched "$before"; status ;;
  openhands)
    mkhome "$OPENHANDS_ISO"; before="$(fingerprints)"
    echo "Signing OpenHands in to ChatGPT in $OPENHANDS_ISO: answer y to its terms notice, then open the link and enter the code."
    clean OH_PERSISTENCE_DIR="$OPENHANDS_ISO" OPENHANDS_SUPPRESS_BANNER=1 "$OPENHANDS_PY" -c \
      'from openhands.sdk.llm.auth.openai import subscription_login as s; s(vendor="openai", model="gpt-5.5", auth_method="device_code", open_browser=False); print("OpenHands: signed in")'
    check_main_untouched "$before"; status ;;
  openclaw)
    mkhome "$OPENCLAW_ISO"; before="$(fingerprints)"
    echo "Signing OpenClaw in to ChatGPT in $OPENCLAW_ISO (not ~/.openclaw): open the link and enter the code."
    clean OPENCLAW_STATE_DIR="$OPENCLAW_ISO" "$OPENCLAW_BIN" models auth login --provider openai --device-code
    check_main_untouched "$before"; status ;;
  anthropic-key)
    mkdir -p "$ROOT"; chmod 700 "$ROOT"
    read -rsp "Paste the Anthropic API key (not echoed), then Enter: " k; echo
    [ -n "$k" ] || { echo "empty; nothing saved" >&2; exit 1; }
    (umask 077; printf '%s' "$k" > "$ANTHROPIC_KEY_FILE"); unset k
    echo "saved to $ANTHROPIC_KEY_FILE (mode $(stat -c %a "$ANTHROPIC_KEY_FILE"))" ;;
  *) echo "usage: $0 status|claude|claude-token|save-claude-token|codex|openhands|openclaw|anthropic-key" >&2; exit 2 ;;
esac
