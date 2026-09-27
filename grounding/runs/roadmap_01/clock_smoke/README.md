# The agent clock on Purdue: smoke run

**The change** (commit 0c7503bf3; `grounding/solver/slack/agent_clock.py`). Each Qwen trial's 480-second budget now
counts only the agent's own time: successful model calls and tool calls. The Purdue client pushes the deadline back
by every second it waits:
- the shared rate limiter's queue;
- the pauses after rate-limit and transient errors;
- failed attempts.

A 1,800-second wall ceiling guards against hangs.
- **A cut by the budget** (`timeout`) is the agent's, and is graded.
- **A cut by the ceiling** (`ceiling`) is an infrastructure error, and the retry pass reruns it.
- **Bedrock runs** keep their plain wall-clock budget.
- **Each attempt's `execution_summary.json`** now records the clock: elapsed, waited and agent seconds.

**The run (approved by the PI; 2026-09-27, 16:00:41–16:08:19).**
- **What ran:** 6 Linear tests whose first attempts had timed out in autogen_02 (on 2 or 3 of their 3 trials),
  1 trial each, on qwen3.8:27b through `autogen_02/kit/solve.py`, all 6 at once ([cases/](cases/),
  [run_clock_smoke.sh](run_clock_smoke.sh), [solve/](solve/)).
- **Results:**

| Test | Earlier first attempts timed out | Termination now | Turns | Elapsed s | Waiting s | Agent s |
|---|---:|---|---:|---:|---:|---:|
| G4-LIN-01 | 1 of 3 | done | 27 | 334 | 232 | 102 |
| G4-LIN-04 | 2 of 3 | done | 8 | 136 | 107 | 30 |
| U-G4-LIN-01-ProjectMilestone_projectId | 2 of 3 | done | 19 | 276 | 186 | 90 |
| U-G4-LIN-04-Attachment_creatorId | 3 of 3 | turn limit | 40 | 433 | 251 | 182 |
| U-G4-LIN-04-Attachment_sourceType | 3 of 3 | done | 11 | 141 | 104 | 36 |
| UC-G4-LIN-01 | 3 of 3 | done | 26 | 379 | 222 | 158 |

- **What it shows:**
  - Every trial finished on its first attempt: no timeout, no ceiling cut, nothing for the retry pass.
  - Waiting was 65% of the wall time, as the clock records it.
  - The most any trial used of its own budget was 182 of 480 seconds, at 40 turns. So the 40-turn limit, not the
    clock, is now the binding budget.
- **What it does not show:** the saving under load. With only 6 trials running, the longest took 433 s of wall time,
  so these would have finished under the old wall clock too. The batches that timed out ran 6 at a time among many
  queued trials. The first full batch on the new clock will show how many retries it saves.
