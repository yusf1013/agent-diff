#!/bin/bash
# Start one Claude Code session on a brief, in its own git worktree and tmux session, as the PI asked on 2026-09-29:
# Opus 5.5, effort max, advisor Fable, no permission prompts, reachable through `tmux attach -t <name>`.
#
#   grounding/protocols/briefs/launch_session.sh <name> [extra note for the first prompt]
#
# <name> is the brief's file name without .md (judge_qwen, regen, related_work, harness, values). The worktree is
# .claude/worktrees/<name> on branch exp/<name>-01 (created from the current HEAD if missing).
set -euo pipefail
NAME=$1; NOTE=${2:-}
REPO=$(git -C "$(dirname "$0")" rev-parse --show-toplevel)
BRIEF=grounding/protocols/briefs/$NAME.md
[ -f "$REPO/$BRIEF" ] || { echo "no brief at $BRIEF"; exit 2; }
WT=$REPO/.claude/worktrees/$NAME
BRANCH=exp/$NAME-01
if [ ! -d "$WT" ]; then
  if git -C "$REPO" show-ref --verify --quiet "refs/heads/$BRANCH"; then
    git -C "$REPO" worktree add "$WT" "$BRANCH"
  else
    git -C "$REPO" worktree add -b "$BRANCH" "$WT"
  fi
fi
if tmux has-session -t "$NAME" 2>/dev/null; then
  echo "tmux session $NAME already exists; attach with: tmux attach -t $NAME"; exit 0
fi
PROMPT="You are the session \"$NAME\", started by the lead session \"RoadMap specialist\" on behalf of the PI. \
Read grounding/protocols/briefs/README.md first (the rules for every session), then your brief $BRIEF, and carry it \
out. You work in this worktree on branch $BRANCH; commit your own study folder as you go. $NOTE"
tmux new-session -d -s "$NAME" -c "$WT" \
  "claude --model opus --effort max --advisor fable --dangerously-skip-permissions -n \"$NAME\" \"$PROMPT\"; \
   echo; echo '[session ended; press enter to close]'; read -r"
echo "started tmux session $NAME in $WT ($BRANCH); attach with: tmux attach -t $NAME"
