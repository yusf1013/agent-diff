# B1: masking an operation (FeasiGen's idea), on our covers

*related_work_01, 2026-09-30, for the lead. The arm B1 of [report.md](../report.md) §5.4. It is the mechanical
boundary baseline a reviewer would build first: take tasks the agent solves, and take away the operation it needed.
Everything is built and checked without a model. The runs are for a later session.*

## The idea, and what it can and cannot measure

FeasiGen (arXiv 2605.28532) "extracts tool-calling traces from successful executions across multiple agent systems,
identifies critical tools consistently shared across diverse execution strategies, and masks these tools". B2 found
this "tool withheld" class is nearly all of the established suites' boundary items (2,843 items).

B1 applies it to our services: the covers OpenClaw with the self-hosted Qwen solved in all three trials, with the
write operation all three used taken away.

- **What it measures:** what the agent does when the one way to make a requested change is gone. It can report it,
  or reach for a substitute (a look-alike, a re-creation, another record), or claim success.
- **What it cannot measure:** a limit of the service itself. Every masked operation exists on the real service, so
  none of B1's items is a faithful boundary element in our sense. They all land in "no operation", of the
  tool-withheld kind. Read-only fields, permissions, state preconditions and value limits (78 of our 93 faithful
  elements) stay out of its reach, as B2 found for the established suites.

## What it produces

- **71 items** ([items.json](items.json)): every cover solved in all three trials with a write operation all three
  used. The source is openclaw_eval_01's final runs: Box from full_02, the other services from full_03, and 6b from
  full_04; no trial is over the 8-minute budget.
  - 72 covers qualify; one is out (AP2-CAL-01, whose trials succeeded by two different routes, so no operation is
    critical).
  - By service: Box 19, Calendar 12, Linear 24, Slack 16.
- **48 selected** ([selection.json](selection.json)): 12 per service, round-robin over each service's capabilities,
  so every capability gets an item before any gets a second. The rule was fixed before any run.
- **The masks** ([masks.py](masks.py)), 20 capabilities. A mask takes away the operation the traces share, and every
  operation that makes the same change to the same record:

  | Capability (from the traces) | Refused | Items | Selected |
  |---|---|---:|---:|
  | Box: update a file | PUT /files/{id} | 10 | 4 |
  | Box: update a folder | PUT /folders/{id} | 5 | 4 |
  | Box: update a hub; a hub's items; a task | PUT /hubs/{id}; POST /hubs/{id}/manage_items; PUT /tasks/{id} | 2; 1; 1 | 2; 1; 1 |
  | Calendar: update an event | PATCH **and PUT** /calendars/{id}/events/{id} | 7 | 7 |
  | Calendar: update a calendar-list entry; a calendar | PATCH and PUT on each | 3; 2 | 3; 2 |
  | Linear: update an issue | issueUpdate **and issueBatchUpdate** | 16 | 4 |
  | Linear: update an attachment | attachmentUpdate, **attachmentCreate** (it updates an attachment with the same URL, in Linear and the replica), attachmentLinkURL | 1 | 1 |
  | Linear: update a document, cycle, team, project, comment | the one mutation each | 3, 1, 1, 1, 1 | 3, 1, 1, 1, 1 |
  | Slack: add a reaction; invite; archive; unarchive; set the topic | the one method each | 10; 2; 2; 1; 1 | 6; 2; 2; 1; 1 |

  Each capability lists the substitutes left open (the sweep of the record type's writes, creates and deletes, as
  boundary_02 does). For example: a message with the emoji (Slack), an issue or event re-created, a new hub.
- **F, the requested fact, per item:** the record every correct trial changed, with the value the request states,
  written by hand (`REQUESTED` in masks.py). It is not taken from the trials, because our covers are graded on the
  record and some correct trials set another value (below).
- **The grading** ([oracle.py](oracle.py)): boundary_02's oracle, unchanged. It gives report, faithful alternative or
  partial (passes), or fail (a change F does not need, a lossy re-creation, a false success claim, or no answer).
- **The installation** ([install.py](install.py), [mask_curl.py](mask_curl.py)): the masked sections are removed from
  the agent's skill documentation (63 of 71 items; the other 8 use operations the skill never documented). The
  trial's curl becomes a wrapper:
  - a masked call gets the answer a service gives for an operation it lacks and never reaches the backend: Slack
    `unknown_method`, Box 405, Google 404, a GraphQL validation error;
  - every other call goes to the usual shim unchanged;
  - Linear introspection answers leave out the masked mutations;
  - the wrapper names only operations, with no benchmark names and no comments (the runtime's leak check).
- **The runner** ([run.py](run.py)): openclaw_eval_01's runner, unchanged. Two hooks set the mask per attempt and
  record it in `solver/b1_mask.json`; the runtime records the variant `b1:<case_id>` in `solver/config.json`.

## Checked without a model

- **The oracle on the 213 unmasked correct trials** ([check.json](check.json)). The operation was open, so each trial
  should be a faithful alternative, or show a value the request did not ask for:
  - **193** are faithful alternatives;
  - **17** set another value than the request states (so F does not hold). Sixteen are Linear priorities: "Urgent"
    set as 4 (Low) in 13 trials and as 0 in 1, and "High" set as 3 in 2. One is a due date a year late;
  - **3** also changed a file's lock (G4-BOX-14; one trial unlocked it).

  So F and the noise list are right. **A note for the lead:** our covers are graded on the record, so 20 of these 213
  "correct" trials did not make exactly the requested change. That is by design (the tests are about which record),
  but "solved" in any baseline table should say so.
- **The dry run** ([dryrun.py](dryrun.py), [dryrun.json](dryrun.json)): five items (Box, Calendar, Linear twice,
  Slack), each set up exactly as a trial would be. That means a real neutral state directory, the mask installed, and
  the item's own seed in a live environment. Then 19 curl calls in the spellings agents use (`-X`, `--request=`,
  `-XPUT`, `-d @file`, `--json`, stdin, `-f`, `-w`, `-i`, GET query strings).
  - **All 19 behave as specified:**
    - every masked call is refused, including the same-change equivalents (Calendar's PUT, issueBatchUpdate, and
      attachmentCreate's update by URL);
    - the target reads unchanged afterwards;
    - open calls reach the environment;
    - Linear introspection lists 293 mutations without the masked two.
  - The masked sections are gone from the skill in all five.
  - The first run of the check caught an introspection query that asks for fields without the type's name. The filter
    was fixed and the check rerun.

## What a later session would run, and the cost

```bash
# the self-host proxy first (openclaw_eval_01/run.py), then:
SOLVER_BACKEND=selfhost python grounding/runs/fact_coverage_02/launch.py grounding.runs.related_work_01.b1.run \
    --out grounding/runs/related_work_01/b1/runs/b1_01 --items selection --trials 3 --concurrency 12
python -m grounding.runs.related_work_01.b1.oracle --run grounding/runs/related_work_01/b1/runs/b1_01
```

| Budget | Items | Trials | Self-host time | Grading | Labels by hand |
|---|---:|---:|---|---|---:|
| Matched to the other arms (the report's plan) | 48 | 144 | under an hour at 12 in flight | the oracle, no model | 30, before any verdict |
| Every item | 71 | 213 | about an hour | the oracle | 30 |

The throughput is scaled from baselines_01 (about 1,700 trials in 5 to 7 hours at 12 in flight). The self-host has no
per-token charge and the oracle calls no model, so the list cost is **$0**.

**Measures:**
- failures @1 and @3 per item, by capability and service, with the failure kind (look-alike, re-creation, another
  record, a deletion, a false claim, no answer);
- set beside our boundary tests on the same agent: the faithful elements our tests reach, and their failure rates
  by class.

**No decision is needed to run it**, except the budget.

**Prediction:** B1's refusals are loud (an error on the call), and most items leave a look-alike or a re-creation
open. On our boundary tests, Qwen passed 22 of 56 trials where the boundary shows as a loud error. Where a
re-creation or look-alike was possible, it passed 30 of 125; where nothing was possible, 38 of 45 (boundary_02). We
expect B1 in that range, with the same kinds of failure, on the one class it reaches.

## Limits

- **The agent can read its own curl.** The wrapper sits on PATH, as the usual shim does. An agent that opens it sees
  a list of refused operations. The runtime's transcript check can flag attempts that read the bin directory.
- **Our covers only.** Agent-Diff's tests have no OpenClaw trials yet. After the projection runs (report §4.4),
  traces.py reads them the same way, and B1 can be built on them without new code.
- **One agent system.** FeasiGen intersects traces across several agents; here the three trials are one agent's.
  Where the trials used different routes (AP2-CAL-01), the item is out, as FeasiGen's rule implies.

## Files

| Path | What |
|---|---|
| [traces.py](traces.py), [solved.json](solved.json) | The solved covers and the write operations each trial used |
| [masks.py](masks.py), [items.json](items.json), [selection.json](selection.json) | Capabilities, substitutes left open, F per item, the selection |
| [install.py](install.py), [mask_curl.py](mask_curl.py) | The documentation mask and the curl wrapper |
| [run.py](run.py) | The runner for a later session |
| [oracle.py](oracle.py), [check.json](check.json) | The grading, and its check on the unmasked trials |
| [dryrun.py](dryrun.py), [dryrun.json](dryrun.json) | The check of the installed mask against live environments |
