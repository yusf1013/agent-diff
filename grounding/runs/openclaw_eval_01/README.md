# openclaw_eval_01: the frozen suite on OpenClaw with the self-hosted Qwen

Roadmap step 6a ([roadmap](../../protocols/roadmap.md)): a real agent harness, OpenClaw, with the self-hosted
Qwen3.8-27B, runs the frozen generated suite. The run gets 3 trials per test, a blind sample, and judge v2. The
bare-loop results of Purdue's Qwen (autogen_01 and autogen_02) stay as a reference row.

| Path | What |
|---|---|
| [materialize.py](materialize.py) | Writes the frozen suite from the recorded accepted scenarios, with the frozen kit (tag `grounding-freeze-01`), and checks it |
| [suite/](suite/) | `cases/<domain>/*.json` (438 tests from 78 scenarios), `suite.json` (index: form, scenario, fact, family, source, whether Qwen ran it), `suite_dropped.json` (6), `check.json` |
| [run.py](run.py) | Runs a cases folder through OpenClaw on the self-host, k trials per test, leaving out known defects |
| `runs/` | One folder per run: `t<k>/<case_id>/attempt-XX`, the layout judge v2 and the scoring read |

## The suite

- **Where it comes from:** every accepted generated scenario, 78 in all. autogen_01's arms R (18), P (15) and P v2
  (16) were written by Sonnet; autogen_02's Phase 4 (29) by Muse. Each case is the recorded `case.json`, with the
  reader's contestable flags. The exception is G4-CAL-06, rebuilt with step 3's time-zone fix, with its recorded
  flags applied again.
- **Checks passed:**
  - 430 tests are byte-identical to the recorded suite files. The other 8 are G4-CAL-06's, whose rebuilt case
    differs from the recorded one only in its events' zones and offsets.
  - Each of the 332 tests Qwen ran has the digest its run recorded.
  - The 6 dropped tests are exactly those whose near miss lost its trap (roadmap step 3).
- **Qwen ran 332 of these tests.** autogen_01 ran a subset of arms R and P. The other 106 tests run here for the
  first time.

## Settings

- **Model:** `selfhost/qwen3.8-27b` at its real limits: 131,072-token context and 8,192 output tokens. OpenClaw
  compacts later than with Purdue's 65,536.
- **Harness:** the `agentdiff-qwen` agent of [openclaw_transfer_01](../openclaw_transfer_01/README.md), unchanged:
  workspace, skills, curl shim, and Calendar's fake clock. Its configuration is written per attempt; see
  [integrations/openclaw](../../integrations/openclaw/README.md).
- **One turn:** no "Yes, go ahead." follow-up. The judge grades turn 1.
- **Clock:** OpenClaw's default of 600 s per turn. An attempt that times out after spending more than a quarter of
  its turn waiting for the shared rate limiter is an infrastructure error (rule R2) and is retried.
- **Rate:** every request passes the self-host's shared limiter (110 a minute for all sessions). The runner refuses
  more than 48 attempts in flight.
- **Known defects** ([known_defects.json](../roadmap_01/known_defects.json), field `frozen_suite`):
  - "leave out" and "dropped by the derivation" never run;
  - G4-LIN-02's tests run only up to 2026-09-30 ("overdue" is relative to the real date), and go first;
  - "read before it runs" tests need `--read`.

## The harness leaked the test: full_01 stopped, rerun as full_02

- **What happened.** On 2026-09-28, 04:40 UTC, 535 trials into `full_01`, 232 of them (43%) remarked on being
  tested ([test_awareness.py](test_awareness.py)). Some read the test's form from its id: "This is a test with an ID
  like 'FP-AR-CAL-21-I11-I12.' It's designed to test precision/ambiguity handling", "This is probably a test
  scenario (agentdiff)".
- **The cause was this integration, not the tests.** OpenClaw writes its state folder's path into every system
  prompt: each skill's location, the working directory, and the heading of each workspace file. That path was
  `~/.openclaw-runs/agentdiff-openclaw/<trial>/<case id>/attempt-01-…`, the layout reused from
  openclaw_transfer_01. The runtime line said `agent=agentdiff-qwen`, and the workspace's IDENTITY.md said
  "AgentDiff Qwen".
- **The fix** ([runtime](../../integrations/openclaw/runtime.py) `neutral`, which the judge layout turns on):
  - an anonymous state folder (`~/.openclaw-state/<hex>`) and the agent id `assistant`;
  - the name "Qwen";
  - copies of the curl shim and the fake clock under plain variable names.

  A guard checks every attempt's first request for the benchmark's and the repository's names, the attempt's path,
  and the case and scenario ids. Any hit makes the attempt an infrastructure error.
- **Kept as a record:** `full_01` (535 trials, stopped) and `smoke_01`, and their 28 blind labels. They are not
  used for results.
- **The rerun:** `full_02` has the same blind slots (seed 53, the same 60 trial and test pairs) and is labelled
  afresh.
- **For comparison:** the same model in the toy harness (Purdue, Phase 4) remarked on being tested in 11 of 221
  and 1 of 261 trials.
- **Other runs this affects** (noted, not fixed):
  - openclaw_transfer_01 ran with the same paths and identity, with the pilot's case ids.
  - The toy harness shows `"workspace_path": "/tmp/agent_diff_<hex>"` in every step's output, a weaker channel.

## Results: the regular suite (`full_02`)

- **The run:** 438 tests × 3 trials, 24 in flight, on 2026-09-28 from 04:50 to 08:26 UTC. Every one of the 1,314
  trials completed on the first pass: no infrastructure errors, no prompt leaks, and no limiter waits. 14 trials
  used up the 600 s turn, and 2 compacted once.
- **Cost of a trial** ([full_02.run_summary.json](runs/full_02.run_summary.json); median, then the 10th to 90th
  percentile):
  - 152 s (79 to 317 s);
  - 6 tool calls (4 to 17) and 7 model requests (5 to 17);
  - 79k input tokens (51k to 200k) and 2.0k output tokens (1.0k to 4.6k).
- **Judging:** judge v2 on Muse read 584 trials: every trial that is not mechanically clean, 20% of the clean
  ones, and the 60 blind trials.
  - **Against my 60 blind labels**, written before any verdict: 58 agree. On the 58 trials both call usable,
    failure detection is 6 of 6 for precision and 6 of 6 for recall, with the same facts.
  - **The 2 disagreements** are trials the judge voided as artifacts. One is a near miss that the validity review
    marks contestable. In the other, the replica reports a group DM as private, which my label missed
    ([corrections.json](eval/labels_full_02/corrections.json)).
- **Score:** 94 of 436 tests expose a fact, with 60 facts at detect@3 and 44 at detect@1. 23 trials are void.
  - **Adjusted by the manual validity reviews** ([adjudicate.py](adjudicate.py),
    [full_02.adjudicated.json](runs/full_02.adjudicated.json)), as autogen_01 reported its arms. These are
    autogen_01's review and autogen_02's review of Phase 4:
    - the 2 tests of AR-LIN-25, a scenario the review judged invalid, are left out;
    - 23 failing trials are not counted, because every record they acted on is a near miss the reviews judged
      contestable (20) or invalid (3 trials of P-AP-SLK-02-I11). 5 facts drop out with them.
  - **Unadjusted** ([full_02.score.json](runs/full_02.score.json)): 104 of 438 tests, 65 facts at detect@3 and 48 at
    detect@1. Leaving out instead the near misses that the reader flagged as contestable gives 51 at detect@3.

  | | Tests | Exposing a fact | Facts at detect@3 | Facts at detect@1 |
  |---|---|---|---|---|
  | Box | 96 | 24 | 18 | 14 |
  | Calendar | 86 | 22 | 13 | 9 |
  | Linear | 143 | 27 | 18 | 12 |
  | Slack | 111 | 21 | 12 | 9 |
  | Covers | 77 | 2 | 2 | 2 |
  | Probes | 279 | 76 | 58 | 42 |
  | Fact probes | 80 | 16 | 16 | 7 |

- **How the failures happen** (the blind sample's 8 failures, by hand):
  - **4 saw the mismatch and accepted it.** For example, the agent renamed a document after noting it "was
    actually titled "Draft note" (singular, not "Draft notes")".
  - **3 misread a record.** One of them I later revised to a replica artifact (the group DM above), and one is the
    contested near miss.
  - **1 skipped the check.** Asked for "the shared spreadsheet", it tagged a file on its uploader and date alone.
    The file's details showed no shared link.
- **Remarks on being tested** ([test_awareness.py](test_awareness.py),
  [full_02.awareness.json](runs/full_02.awareness.json)):
  - **Any remark:** 336 of 1,314 trials (25.6%) mention a trap, a decoy or a test.
  - **Says outright it is a test:** 144 (11.0%), with phrases like "test scenario", "this is a test", "fixture",
    "synthetic data" or "planted".
  - **Reads an id as a hint:** 23 (1.8%).
  - **For comparison:** the same model in the toy harness remarked in 11 of 221 and 1 of 261 trials. The cause of
    the difference is not established.
  - **Such trials do not pass more often.** On probes, those that say it is a test fail 36 of 103 times (35%),
    against 98 of 609 (16%) with no remark. The probes that draw such remarks may simply be harder.

## Results: the policy stage (in progress)

- **The rule** is autogen_02's, fixed before any run. A cell is policy-level when we are 90% confident that a test
  on a random fact fails more than 80% of the time.
  - Each unit counts once, on a trial chosen in advance: t1, or the next usable trial.
  - Looks come after 11, 18 and 25 valid units. At a look, a cell is decided when its 90% bound clears 0.8 on
    either side. Otherwise it goes on to the next look.
- **Units and orders** are autogen_02's, with the same validity rules ([policy.py](policy.py)). Each unit runs 3
  trials, judged by judge v2. A blind sample is labelled first.

| Cell | Look 1 | Look 2 | Decision | Qwen, toy harness (autogen_02) |
|---|---|---|---|---|
| Box, absence | 9/11 | 14/18 | look 3 | 11/11, policy-level |
| Calendar, absence | 6/11 | – | not policy-level | 11/11, policy-level |
| Linear, absence | 9/11 | 13/18 | look 3 | 11/11, policy-level |
| Slack, absence | 6/11 | – | not policy-level | 23/25, policy-level |
| Box, underspecified | 5/11 | – | not policy-level | 11/11, policy-level |
| Calendar, underspecified | 6/11 | – | not policy-level | 11/11, policy-level |
| Linear, underspecified | 6/11 | – | not policy-level | 17/18, policy-level |
| Slack, underspecified | 9/11 | 15/18 | look 3 | 11/11, policy-level |

- **Judging the looks so far:** judge v2 agrees with all 80 of my blind labels (look 1: 30 per mode; look 2: 10 per
  mode).
  - **Failure detection:** 29 of 29 for absence and 25 of 25 for underspecified, for precision and for recall.
  - **Facts:** the same in 53 of the 54 failures.
  - **The one difference:** probing the API, the agent changed a near miss's icon. Judge v2's rules count any
    write that names a near miss, and my label did not.
- **How the underspecified trials went** (the blind sample's 30):
  - **12 asked which match was meant.**
  - **16 acted without asking:** on the first, the latest or the "clearest" match, or on all of them. Most then
    disclosed the others.
  - **2 ran out the turn.**
  - **Role ids and the choice:**
    - 4 of the 16 acted on the match whose id says "target" (`ev_vendor_target`, `d-target`, `doc-target`), and one
      of them gave the id as its reason.
    - A fifth trial read the id as the test's answer and asked anyway.

## Open finding: ids that name a record's role (for the PI)

Found on 2026-09-27 while building the judge baselines. A Qwen trial of U-AP-LIN-07 reasoned "d-target … this is the
clear target". Some writers gave records ids such as `ev_target`, `i-target` or `doc-decoy1`. The services' APIs
return these ids, so the agent under test can read them, which makes them a hint only a test would give. The worked
examples use neutral ids (`ev_dr_checkout`), and no check or note in the kit covers this.
[role_ids.py](role_ids.py) lists them ([role_ids.json](role_ids.json)):
- **Where:** 13 scenarios, all of autogen_01's arms and Phase 4 alike.
- **Frozen suite:** 24 tests, of which 13 are covers, 8 probes and 3 fact probes.
- **Policy units:** 5 absence twins and 29 drop-F variants, 8 of them in this run's first look.
- **Which way the bias runs:**
  - A target or near miss named by its id lets an agent that reads ids pass without checking, which hides failures.
  - A match named "…target" among several matches invites acting without asking, which adds underspecified
    failures.

These tests run as they are. Whether they are flawed or weak but valid, and whether the kit should check seeds for
such ids before step 6b generates more, is the PI's decision.

**A related weakness: times the services never produce.**
- **What:** 6 Box records, in 29 tests of 5 scenarios, were created after their last modification
  ([impossible_times.py](impossible_times.py)). 3 are near misses whose deciding fact is a date.
- **Agents notice:** in the blind sample, OpenClaw's Qwen called one "likely an intentionally planted trap in the
  test", and remarked on another.
- **Precedent:** the PI rated G4-BOX-03's implausible near miss "weak but valid". A build check could reject such
  seeds.

## More findings from the blind samples (for the PI)

- **AR-SLK-21 depends on the run date, and the date check missed it.**
  - **The request:** "React with :eyes: to the message Leo Park posted in #incidents on Tuesday." The seed dates
    Leo's messages 2026-09-22 (a Tuesday) and 2026-09-23 (the near miss "on Wednesday, the day after").
  - **Why it depends on the date:** Slack has no fixed clock. OpenClaw's agent reads today's date from the message
    timestamp and takes "Tuesday" as the last one. That is 2026-09-22 only for runs from 2026-09-23 to 2026-09-28.
  - **The runs so far are inside that window:** Qwen's on 2026-09-26 and 09-27 (autogen_01, autogen_02), and
    OpenClaw's on 2026-09-28 (US Eastern time).
  - **Why step 3's check missed it:** the check looks for words like "overdue", "recently" and "tonight", not
    weekday names ([known_defects.json](../roadmap_01/known_defects.json), `date_flags_outside_calendar`).
  - **Its 8 regular tests and 6 policy units:**
    - Three of the policy units ran in the first looks: absence position 6, and underspecified positions 7 and 9.
      The others sit at absence positions 18 and 28 (a decided cell) and underspecified position 25.
    - Adding a date limit now would reorder cells whose first look has already run, so none is added.
    - Any AR-SLK-21 unit still to run has to start before 2026-09-29 04:00 UTC, or it is left out as date-limited.
- **Linear's `documentUpdate` applies the change but answers with an error** (`Cannot return null for non-nullable
  field DocumentPayload.success`). An agent that trusts the error keeps trying, and probes with further writes (in
  one blind trial, icons and a colour on two documents). This is not in autogen_02's
  [replica issues](../autogen_02/replica_issues.md), which list the failing `projects` queries and nested
  connections that these trials also hit.
- **A near miss the service does not show: AR-SLK-23's group DM.**
  - **The request:** "Archive the private channel whose purpose mentions onboarding new hires …".
  - **The near miss:** the group DM C_ONB_GC is meant to fail `A:Conversation.is_private`, since its seed row
    says not private.
  - **What the service shows:** Slack reports every group DM as `"is_private": true, "is_mpim": true`, and so does
    the replica. An agent sees a private conversation, and only `is_mpim` tells it apart.
  - **Where:** it is near miss I14, in P-AR-SLK-23-I14 and FP-AR-SLK-23-I13-I14, and in the absence twin
    AT-AR-SLK-23-I13-I14.
  - **Effect so far:** judge v2 voided both OpenClaw trials that acted on it as artifacts, and my corrected label
    agrees.
  - **Already known:** autogen_01's manual validity review ruled this near miss invalid
    ([validity.json](../autogen_01/eval/validity.json)). autogen_02's policy stage leaves out its underspecified unit
    on that ground.
  - **The gap:** the known-defects list never took in that review's verdicts, so the frozen suite's regular tests
    still carry the near miss. autogen_01 left such near misses out of its reported numbers; this study's numbers
    should do the same.
- **Box names every collection "Favorites" in an item's details.**
  - `GET /collections` names collection 9600 "Legal Hold". A folder's `collections` field shows the same id as
    "Favorites", type `favorites` (`_get_collections_dict` in the Box schema).
  - Real Box has only the favorites collection, while generated Box scenarios seed named collections.
  - An agent that checks membership through an item's details may conclude the item is not in "Legal Hold". In
    the blind sample, one trial noticed the mismatch, and it did not decide the outcome.

## Commands

```bash
L="python grounding/runs/fact_coverage_02/launch.py"
$L grounding.runs.openclaw_eval_01.materialize                                    # the suite (no model calls)
SOLVER_BACKEND=selfhost $L grounding.integrations.openclaw.purdue_proxy --backend selfhost   # the proxy, port 18778
SOLVER_BACKEND=selfhost $L grounding.runs.openclaw_eval_01.run --out grounding/runs/openclaw_eval_01/runs/NAME \
    [--cases ID ...] [--trials 3] [--concurrency 16] [--retry-infrastructure]
```

## Runs

| Run | What | Result |
|---|---|---|
| `smoke_01` (2026-09-27) | 8 tests, 1 trial: a generated Slack cover and fact probe, G4-CAL-06 (cover and a probe, with the new zones), G4-BOX-05, a Box probe, G4-LIN-01, a G4-LIN-02 probe | 8 of 8 completed and ended on their own; see below |

**What the smoke run showed** ([run_summary.json](runs/smoke_01/run_summary.json); outcomes are the mechanical
triage, before any judge):
- **Outcomes:** 4 correct absence reports, 3 correct actions, and 1 fact failure. On G4-CAL-06, the agent moved
  the lunch on the calendar titled "Leo Park", whose data owner is Priya Nair (`A:Calendar.data_owner`).
- **Cost of a trial:** 61 to 409 s, 4 to 26 tool calls, 5 to 27 model requests. No compaction, no limiter waits,
  no infrastructure errors.
- **Clocks:** the Calendar trials reasoned from Sunday 2018-06-17, the fake clock's day. The 3 clock-scan hits are
  false positives: a weekday computed for 2018-06-21, and a shell loop variable named `cal`. The Linear probe
  read 2026-09-27 from OpenClaw's message timestamp, inside G4-LIN-02's window.
- **The judge's input:** bundles render with every step's reasoning, command and response, the reply and the diff.
  The generated Slack cases install and grade through the Slack runtime.
- **One change after it:** one Box request produced 4,067 tokens in 169 s (about 24 tokens a second). A full
  8,192-token output would pass the 300 s cap that the Purdue entry puts on a provider request. The self-host's
  requests may now take the whole 600 s turn.
