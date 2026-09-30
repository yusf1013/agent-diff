# claudecode_pilot_01: Claude Code as a backend of our runner, and a Sonnet 5.5 pilot

Session "harness", second assignment from the lead session "RoadMap specialist" (2026-09-30), after
[harness_scout_01](../harness_scout_01/report.md) recommended Claude Code as the second harness.

## Status

- **2026-09-30, 01:50 EDT. Done.** The backend works through the runner; the 32-test pilot ran (32 of 32
  completed, no infrastructure error); my blind labels were written before any verdict; judge v2 on Muse agrees with
  all 32 ($0.05 billed). A full Sonnet round could start on the PI's word once the two decisions below are made.
- **Running:** nothing. **Blocked:** nothing.

## Summary

- **The backend** ([backend.py](backend.py), [run.py](run.py)): Claude Code 2.1.285 headless (`claude -p`), with
  OpenClaw's `run_attempt` contract and openclaw_eval_01's selection, trials and output layout. Each run has its own
  configuration directory; tools `Bash, Read, Skill`; no MCP server and the claude.ai connectors off; the test clock
  through an LD_PRELOAD shift; the 10-minute limit; judge steps, usage and the plan's windows from the transcript;
  infrastructure rules R1-R5 (below). No account email reaches the model or the evidence.
- **The pilot** (the Sol pilot's 32 regular tests, one trial each, Sonnet 5.5 at effort medium): 7 correct,
  23 correct_absent, **2 incorrect** by my blind labels, the same by judge v2:
  - **G4-LIN-04** (`R:Attachment.creatorId`): the replica's nested `issue { attachments }` query errors (a known gap;
    the top-level `attachments` query works). Sonnet never tried the working query and set the estimate on the issue
    Maya Chen *created* instead of the one whose link she *uploaded*, saying it could not confirm the link.
  - **FP-G4-LIN-06-I11-I12** (`R:issue_label_issue_association`): Sonnet read label names but not their teams and
    set the estimate on an issue whose Bug label is the Mobile team's, presenting it as the match.
- **Judge v2 on Muse**: 32 of 32 agree with my labels; both failures found, with the same facts; $0.048 billed
  ($0.69 at Muse Spark 1.3's list price).
- **Against the Sol pilot** (OpenClaw, GPT-6.1 Sol, the same 32 tests): Sonnet on Claude Code is faster (median
  13 s against 37 s per run) with a similar number of calls (median 4 tool calls, 5 model requests), more input
  (54k against 46k, mostly cached) and twice the output (726 against 349 tokens).
- **The same 32 tests, both judged by judge v2 on Muse** (the Sol pilot judged afterwards at the lead's request,
  2026-09-30; its verdicts in `runs/judged_sol_pilot_01`, 34 calls with 2 retried errors, $0.058 billed, $0.82 list;
  no blind labels on the Sol trials):

  | Pilot (one trial per test) | correct | correct_absent | incorrect | not established |
  |---|---:|---:|---:|---:|
  | Claude Code × Sonnet 5.5 (plan) | 7 | 23 | 2 | 0 |
  | OpenClaw × GPT-6.1 Sol (plan) | 8 | 23 | 0 | 1 (FP-G4-LIN-08: the clock problem, an infrastructure error) |

  Sol passed both tests Sonnet failed: on G4-LIN-04 it listed the attachments with their source and creator
  through the top-level query and acted on the target; on FP-G4-LIN-06 it filtered the Bug label by team and found
  nothing. One trial per test: an observation, not a comparison of the models.
- **The G4-LIN-08 tests run here.** The Sol round left them out because OpenClaw's login check fails under their
  2026-10-16 clock; with a token passed to Claude Code nothing checks an expiry, and FP-G4-LIN-08-I13-I14 ran with
  "Today's date is 2026-10-16" in its context.

## What the PI must decide

1. **A `claude setup-token` login for the runs.** A full round waits for it:
   - The pilot borrowed the machine login's current access token (read at launch, passed only to the run, never
     written, the refresh token never read; the lead approved this for the pilot). That token lasts about eight
     hours, and only the PI's interactive Claude Code sessions refresh it. A round of 1,500 to 3,000 runs spans
     hours; runs are refused within 20 minutes of the token's expiry (R4) and wait until some session refreshes it,
     which overnight may never happen.
   - A setup-token is made for automation: long-lived, separate from the PI's sessions, revocable on its own. It
     removes the dependence on the live login and its email.
   - How: the PI runs `claude setup-token` once in a terminal (it opens a browser to sign in) and saves the printed
     token to `~/.config/claude-solver/oauth_token` (mode 600). The backend then uses it (`--auth token-file`, the
     default when the file exists); each run still gets its own configuration directory.
2. **Pro or Max.** `claude auth status` on this machine says "Login method: Claude Pro account" (the credentials
   record `subscriptionType: pro`). If the PI is on Max, the setup-token should be made from the Max account (or
   the login refreshed first), since the plan's limits set the pace of a round.
3. **Settings to confirm** (defaults used in the pilot): effort `medium` (the Qwen and Sol rounds' label); tools
   `Bash, Read, Skill` (OpenClaw's rounds also had web search and fetch); one turn, no follow-up.

## The estimated plan cost of a full round

| | Per run (pilot mean) | Muse-written half (1,515 runs) | Full suite (3,018 runs) |
|---|---:|---:|---:|
| API-equivalent at list price (Claude Code's own estimate, Sonnet 5.5 at $2/$10 per million) | $0.052 ($1.67 / 32) | about $79 | about $157 |
| Billed on the plan | $0 | $0 | $0 (overage is off: `overageStatus: rejected`) |
| Wall time at concurrency 6 (pilot: 32 runs in 10 min, with environment set-up, measured while the Sol round held the shared DDL lock; concurrency can go to 12) | | about 8 h | about 16 h |

The plan's windows, as the pilot's runs saw them (the account's other sessions used them at the same time):

| Window | Before (05:32 UTC) | After (05:42 UTC) | Resets |
|---|---:|---:|---|
| Five-hour | 41% | 45% | 07:10 UTC |
| Seven-day | 11% | 12% | 2026-10-07 02:00 UTC |

If all of the change were the pilot's (an upper bound: the lead's session and four other study sessions used the
account meanwhile), 32
runs cost 4 points of the five-hour window and 1 point of the seven-day window, so a full round (3,018 runs) would
need about 3.8 five-hour windows and about 94% of a week, and the Muse-written half about half of that. The true
share is smaller; a clean measurement is the first batch of the round run while nothing else uses the account,
reading the windows before and after.

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
| [eval/labels_pilot_01.json](eval/labels_pilot_01.json) | My labels, written before any verdict ([label_view.py](eval/label_view.py), [add_label.py](eval/add_label.py)) |
| [eval/judge_trials_pilot_01.json](eval/judge_trials_pilot_01.json) | Judge v2's selection (all 32) |
| [summarize.py](summarize.py), [pilot_summary.json](pilot_summary.json) | The pilot's numbers, with the Sol pilot's |
| `runs/smoke_01`, `runs/pilot_01`, `runs/pilot_01.log` | The runs, in the judge layout (hidden from ripgrep by `.ignore`) |
| `runs/judged_pilot_01/` | Judge v2's verdicts, calls log and `comparison.json` against my labels |
| `runs/judged_sol_pilot_01/` | Judge v2's verdicts on the Sol pilot's 32 trials (the same-test row) |
| [openai_store/](openai_store/README.md) | The fix of OpenClaw's openai backend login store (`AGENTDIFF_OPENAI_STORE=main`) and its evidence |

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

### Cycle 2 (01:31-01:43): the pilot and the blind labels

- `runs/pilot_01`: the 32 tests of `sol_pilot_01/pilot_cases.txt` from `openclaw_eval_01/suite_opaque/cases`, one
  trial each, concurrency 6, `--auth login`. Nothing was left out by the rulings. The first Box environments waited
  a few minutes on the shared DDL lock (the Sol round was running); all 32 runs completed (05:32-05:42 UTC).
- Labelled each trial by hand as it ended, from [eval/label_view.py](eval/label_view.py): the request, targets and
  decoys, steps, reply and diff, with no verdict and no mechanical attribution. One ruling came from the replica
  notes: G4-LIN-04's attachments error is the replica's known nested-connection gap, with a working top-level query,
  so the trial is the solver's failure (judge v2's rule: a solver that could not find the right query failed on its
  own), not an artifact.

### Cycle 3 (01:43-01:50): judge v2 and the numbers

- Judge v2 on Muse over all 32 (`runs/judged_pilot_01`): 32 of 32 agree with the labels, 2 of 2 failures with the
  same facts; 32 calls, $0.048 billed, $0.69 at list price, no error.
- [summarize.py](summarize.py): timings, tokens, list-price cost and the plan's windows, with the Sol pilot's
  numbers (read from the main checkout's `sol_pilot_01/runs/pilot_01`, which is not committed).

### Cycle 4 (01:51-02:04): the Sol pilot judged, and the openai backend's store

- At the lead's request, judge v2 on Muse over the Sol pilot's 32 trials (read only): the same-test table above.
- A development task from the lead: OpenClaw's openai backend copied the login store, owned by agent `main`, into
  the attempt agent's directory, so `memory_search` and the auth failover failed. `runtime.py` now has an opt-in
  layout (`AGENTDIFF_OPENAI_STORE=main`) with the login in the attempt state's main agent and a fresh store for the
  attempt agent; the default path is byte-for-byte unchanged. Three runs confirmed it
  ([openai_store/README.md](openai_store/README.md)).

## Infrastructure rules

A run that ends in one of these is re-run with `--retry-infrastructure`; it is never scored. A timeout (the
10-minute limit) is the agent's failure and is not re-run.

| Rule | When |
|---|---|
| R1 no result | `claude` exited without a result event, before the limit |
| R2 provider time | the run hit the limit after more than a quarter of it in failing, retried API requests (from Claude Code's debug log) |
| R3 provider error | the result is an API, authentication or plan-limit error |
| R4 login token | `--auth login` and less than the limit plus 10 minutes left on the login's token |
| R5 plan window | the plan refused a request (a rate-limit event with status `rejected`) |
| isolation | a leak token in the context, or tools or MCP servers other than expected in the init event |

## How to start a round (after the PI's decisions)

```bash
L="backend/.venv/bin/python grounding/runs/fact_coverage_02/launch.py"
$L grounding.runs.claudecode_pilot_01.run --trials 3 --concurrency 6 \
    --out grounding/runs/<study>/runs/regular_p4 --cases-dir grounding/runs/openclaw_eval_01/suite_opaque/cases \
    --cases $(cat grounding/runs/sol_eval_01/cases/regular_p4.txt)
```

Then judge v2 on Muse as for the other rounds (`autogen_02/kit/judge2 select`, `run`, `compare` against the blind
labels), with a blind sample drawn before the run (`openclaw_eval_01/blind_sample.py`).
