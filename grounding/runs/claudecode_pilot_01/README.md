# claudecode_pilot_01: Claude Code as a backend of our runner, and a Sonnet 5.5 pilot

Session "harness", second assignment from the lead session "RoadMap specialist" (2026-09-30), after
[harness_scout_01](../harness_scout_01/report.md) recommended Claude Code as the second harness.

## Status

- **2026-09-30, 01:31 EDT.** The backend ([backend.py](backend.py)) and runner ([run.py](run.py)) work: a two-test
  smoke (`runs/smoke_01`) ran end to end. The pilot is next.

## The question

How can a Sonnet 5.5 round run on Claude Code through our runner, with the cases, trials and evidence of the
OpenClaw rounds, so it could start on the PI's word, and what would a full round take from the Claude plan?

Parts (the lead's assignment):
1. an adapter with the contract of OpenClaw's (per-run isolation with its own configuration directory, the clock
   shim, the curl shim and skills, the 10-minute budget, the transcript as judge steps in the judge layout, usage
   from the transcript, infrastructure rules for provider errors), driven by openclaw_eval_01's selection;
2. the Sol round's 32-test pilot (`sol_pilot_01/pilot_cases.txt`, one trial each) with Sonnet 5.5 on the plan,
   judged with Muse judge v2 (cap $3 billed), with timings, tokens and the plan's windows before and after;
3. what the PI must decide, and the estimated plan cost of a full round.

## Files

| Path | What |
|---|---|
| [backend.py](backend.py) | One attempt through `claude -p`, with OpenClaw's `run_attempt` contract |
| [run.py](run.py) | The runner: openclaw_eval_01's selection, trials and output layout, with this backend |
| [clock/fakeclock.c](clock/fakeclock.c) | The LD_PRELOAD wall-clock shift (from harness_scout_01) |
| [eval/blind_pilot_01.json](eval/blind_pilot_01.json) | The pilot's blind list: all 32 trials, fixed before the run |
| `runs/<run>/t<k>/<case>/attempt-XX/` | Evidence in the judge layout (hidden from ripgrep by `.ignore`) |

## Log

### Cycle 1 (2026-09-30, 01:21-01:31): the backend

- **Authentication without touching the login.** A fresh `CLAUDE_CONFIG_DIR` per run, authenticated by
  `CLAUDE_CODE_OAUTH_TOKEN`: either a `claude setup-token` token from a file the PI makes once (`token-file`), or,
  until then, the login's current access token read from `~/.claude/.credentials.json` at launch (`login`). The
  refresh token is never read, so no run can refresh or rotate the login; a run starts only with more than 20
  minutes left on the token (rule R4). Checked on a trivial prompt: it runs, and the run's context holds no account
  email (the shared-login smoke of harness_scout_01 had it), no MCP server and none of the account's synced skills.
- **Smoke** (`runs/smoke_01`, two tests outside the pilot, one trial each): AR-SLK-21 (Slack, test clock
  2026-09-25) and G4-CAL-06 (Calendar, 2018-06-17 in Los Angeles). Both completed in 12-13 s, 5 tool calls,
  $0.06-0.07 each at list price; the context's date matched each test's clock; tools `Bash, Read, Skill`,
  `mcp_servers: []`, no leak, no email. Raw files (stream, session, context, debug log) are bundled into
  `solver/claude.tar.xz`.
- Fixed after the smoke: the plan-window readings skip rate-limit events that carry no windows, and Claude Code's
  `latest` symlink to its debug log is not bundled.
