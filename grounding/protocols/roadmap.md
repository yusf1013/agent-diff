# Roadmap after autogen_02

Agreed with the PI on 2026-09-27 after [autogen_02](../runs/autogen_02/overview.md), and re-agreed later that day
once steps 1 and 2 were done. The work is done in steps. The PI steps in where a step needs a decision. Progress is
recorded in the status table at the end.

## The goal

A final evaluation of the automated grounding-test system, from three angles:
1. **What the system finds in real agents:**
   - **Agents:** real harnesses only, for every model (the PI, 2026-10-01). Done on OpenClaw: the self-hosted
     Qwen3.8-27B and GPT-6.1 Sol. Being set up (2026-10-03): Claude Code and Codex, each with the Claude and the
     ChatGPT subscription, in isolated logins; further harnesses (Hermes, Goose, Pi) at the PI's decision.
   - **Per agent:** the facts the regular tests expose, the eight policy decisions, and how the failures happen
     (analysed by hand).
   - **No bare-loop rows:** the bare loop (the toy harness, Purdue's or the self-hosted Qwen's) is outdated and is
     not used in any analysis, comparison or report, not even as a reference row (the PI, 2026-10-01).
2. **The system itself, reported in two phases:**
   - **Generation:** briefs, then scenarios, then valid tests, then tests run.
   - **Judging:** the judge's accuracy per agent, against a blind sample labelled by hand before any verdict.
3. **Baselines**, each run on Muse like our own agents:
   - **G0**, a generator: a coding agent with no domain model.
   - **G1**, a generator: the same agent given our facts, without the substitute menus.
   - **J0**, a judge: a naive judge.
   - **J1**, a judge: the naive judge given the domain model.

The suite should give every catalog fact a test: on the supported side, with regular and policy tests, or on the
unsupported side, with capability-boundary tests (step 5).

## The order

The audits and the loose ends could change prompts or code. Every such change is discussed with the PI first. So
the final runs use one frozen version.

1. **Quick unblockers (done).** A trial clock that leaves out Purdue waiting; Muse's verify-reminder off for judge and
   reader; the lists of known defects, probes without a trap, and requests that depend on today's date.
2. **Two audits (done and discussed).** Overfitting and leaks in the prompts; domain knowledge in the deterministic
   code.
3. **The agreed fixes, then a frozen version:**
   - **The probe-trap check at derivation.** The check that each near miss still fails exactly its fact now runs on
     every probe and fact probe when a suite is derived. A probe that fails it is dropped and recorded.
   - **The seed builders own their helpers.** The Linear and Slack seed builders' helper classes are copied into the
     kit, unchanged, so the generator no longer imports the pilot studies' files.
   - **Calendar time zones.** Events take their calendar's time zone and the right offset for their date.
   - **A date check.** New scenarios whose requests depend on today's date outside Calendar go back to the writer.
     G4-LIN-02 is left out of runs after 2026-09-30.
   - **Known defects.** G4-BOX-05 is kept. Its ambiguity is natural language, and a misreading counts against the
     agent.
   - **Documentation.** A note in the kit's README, which no agent reads: where the method's "tempting near miss"
     advice came from, one line of Slack's replica notes about agents, the default near-miss people, and the 9
     scenarios that copied the worked examples.
   - **Check before freezing.** Rebuild the existing suites. Only the intended differences may appear.
4. **Complete the suite:** folded into 6b.
5. **Investigations**, in a separate session on branch `exp/investigations-01`, which sends its status here.
   - **Failure attribution:** which component a failure belongs to.
   - **Several-match requests.**
   - **The capability boundary.**
   - The known-defects list is the development set for attribution.
   - **Policy-level: the definition and the sampling rule** (added 2026-09-28, from 6a).
     - **The question:** what should "policy-level" mean for an agent whose runs of one test disagree, and when
       can a sample of policy tests stand in for all of them?
     - **Why it came up:** OpenClaw's Qwen fails many policy tests in one or two of three runs. The decisions change
       with how the runs are read: the first run only (the rule so far), any of the three, or all of them pooled.
     - **Candidate definitions:**
       - with 90% confidence, one run of a policy test on a new fact fails with probability above 0.8;
       - the same for a test with its three runs;
       - the failure rate is about the same across 80% of the facts.
     - **The ground truth:** the full set of policy tests on OpenClaw, which runs regardless of the sampled
       decisions. Each definition and sampling rule is judged against it: does it reach the same decision, and
       with how few tests?
     - **The working rule until then:** all runs are used, with tests (not runs) as the independent units.
6. **Final evaluation:**
   - **6a. OpenClaw with the self-hosted Qwen, on the frozen generated suite.**
     - **Settings:** the model's real limits (131k context, 8k output); no "Yes, go ahead." follow-up turn.
     - **Size:** the full suite at 3 trials, plus the policy stage: its sequential looks first, then (after the
       discussion of 2026-09-28) every valid policy test, 3 trials each.
     - **Known defects** are left out.
     - **A blind sample** is drawn and labelled before any verdict.
     - **The integration code** from openclaw_transfer_01 is reused; its runs are not.
   - **6b. The 26 remaining briefs.** 19 were never generated, 3 failed, and about 4 are new for 12 facts. They are
     generated and run on OpenClaw, so it covers the whole servable space.
   - **6c. Judge baselines J0 and J1**, on the trials already labelled by hand. They are scored as confusion matrices
     on "did the agent make a mistake", against the labels reduced to yes/no. Only our judge attributes facts.
   - **6d. Generator baselines G0 and G1.**
     - **Which briefs:** drawn from the whole set, evenly by domain. Briefs generated after the method was tuned
       (Phase 4's and 6b's) are preferred.
     - **Budget:** equal numbers of tests: per brief for G1, per domain for G0.
     - **Review:** blind, over a shuffled pool: validity, and coverage credited by the credit rule. Anything the
       baselines test that we never defined gets noted.
     - **Runs:** on OpenClaw, compared under fact_coverage_02's decision D5.
   - **6e. Reports:** OpenClaw for first-time readers; the system (generation and judging); the baselines.

8. **Dates that never go stale.** Asked for by the PI on 2026-10-01 and investigated the same day:
   [dates_01](../runs/dates_01/README.md). Finding: the agent-clock shift broke Sol's login (15 items not run), leaked the
   real clock in a few trials, and set a 2018 world against the model's prior in 40 Qwen Calendar trials (no fact's
   exposure rests on them); the writers were never told a current date. The proper fix, prototyped mechanically on all
   86 scenarios: render each test's dates to the run week at environment creation (whole-week shift of seed, query,
   witnesses and request phrases bound by the writer's conditions; Calendar's replica now follows), no agent clock.
   **Decided by the PI on 2026-10-03:** shifting the agent's clock is discontinued as a severe anti-pattern
   ([grounding/AGENTS.md](../AGENTS.md), "Dates: never change the agent's clock"). Dates belong to the test: every
   date is held as a template relative to the moment the test was written for and rendered against the real date
   when the environment is created. The PI asked for three things: the documentation (done the same day); which
   tests in the denominator tables the dates affected (made too easy, impossible, stale, or not run); and the fix,
   first by checks applied retrospectively to the generated tests, with minimal writer instructions only as the last
   resort, and with the writer given the current date. Study: [dates_02](../runs/dates_02/README.md).
   The PI's decision of 2026-10-01 had been pending.
   **Done 2026-10-03:** every one of the 937 tests behind the denominator tables has a verified template (identity
   937/937; the same derived tests on 61 run days over two years; month conditions kept on all 731; nothing from the
   future); the OpenClaw runtime and the Claude Code backend render templates when they create a test's environment
   and refuse a test made for a shifted clock; Slack is held at its written days until the scoring maps message ids.
   Affected on record: the 176 tests dated 2018 (no outcome rests on the 2018 setting); the overdue issue's 7 tests,
   run five days before their designed day (its sharpest near miss tested in an easier form); the October-15 issue's
   16 tests, never run by Sol (15 items). No writer change is needed for the tests on record; giving the writer the
   current date is proposed for new scenarios. Proposed runs, waiting for the PI: Sol on the October-15 issue (before
   the plan lapses), the overdue issue as designed, the Calendar rerun in the present.
   **2026-10-04, after the PI's answers:** the Calendar service in the backend keeps the real time (the PI's one-time
   exception to "report, don't fix"; the backend now runs from the repository); the writer and the cold reader are
   told the current date, and the Calendar notes no longer say 2018; self-hosted Qwen runs need no approval and
   validation on it is encouraged; eight converted tests ran live on Qwen, all as designed (dates_02, "The live
   check"). Waiting for the PI: Sol on the 15 items it never ran.
   **Deferred by the PI to the next generation (2026-10-04), to be raised with the PI before any new tests are
   generated:** replace the writer's relative-date word check with the moving checks (weeks, quarters and years
   added to months), and replace the suite builders' clock dates (which the runners now refuse) with templating
   from the scenario's `written_for` date. Details: grounding/AGENTS.md, "Before the next generation of tests". The earlier text of this step (2026-09-30, withdrawn as a decision):** The PI's question: *how can a test that depends on
   dates be right on any day it is run, without adding overhead to the LLMs in the pipeline?* Today every date in a
   scenario is absolute and the test runs the agent under a shifted clock (step 3's "dates are controlled on the
   test side"), which fails wherever the agent's process cannot be back- or forward-dated: the 16 G4-LIN-08 tests
   are clocked past the OpenAI login's expiry; Codex and Claude Code carry their own dates. The investigation
   compares the mechanical options: dates rendered from offsets against an anchor at environment creation (the
   writer keeps writing absolute dates; a pipeline step converts them to offsets from the scenario's clock, and the
   suite renders them against the real date, weekday preserved where a request names one, time zones and DST in the
   calendar's zone); the shifted clock kept only where rendering cannot reach; or both. It must cover seeds,
   prompts, expected outputs, the judge's inputs and the replica's "now", and be applied to every date-sensitive
   test in the suite, then verified by re-running the Calendar tests and the clocked tests on a day other than
   their original one. Owner: a session on a brief; the design is discussed with the PI before it is applied.

## Decisions (2026-10-01, the PI: the denominator comes first)

The methodology prescribes a fixed number of tests from the domain model alone; every report number is read
against that denominator, which is independent of any generation attempt or writer.

- **Facts: 255 in the catalog, 42 unservable on the replicas, 213 servable.** The one number known for sure.
- **Briefs (covers): the 89 as generated are kept, as a generation-side matter** (they are the vehicle by which the
  facts are covered, and the generation is done). Their shortcomings are on record:
  - two grouping rules: 38 briefs grouped by hand (the 18 reproduction briefs copy the earlier design study's
    hand-written scenarios, size free, as the PI approved; 16 prospective and 4 development briefs chosen by hand),
    51 by a script's rule (one entity's facts in catalog order, three per brief) whose fixed size was never put to
    the PI;
  - 22 briefs hold a single fact, so their requests meet the scope rule (a multi-condition request) only where the
    writer added conditions on its own;
  - 15 briefs were generated twice (method v1 and v2) and both scenarios sit in the suite; the regenerated half
    adds a third scenario to 34 briefs;
  - the writers claimed 12 facts beyond their briefs, so 8 facts earn credit in two or three briefs; one Slack
    fact (who posted a message) is in two briefs;
  - 3 briefs produced no accepted scenario and one scenario is invalid: 9 servable facts have no cover.
- **Probes: one per fact, holding all of the fact's decoys: 213.** The single-decoy probes of multi-decoy facts
  (212 in the current suite) are a separate set, reported apart, not part of the denominator.
- **Absence: 213. Underspecified: 213.** One test per fact in each mode. The scope rule, two facts sharing one
  condition, the writer declining a rewording, dropped probes and the rulings are generation-side matters and do
  not touch the denominator.
- **Production counts are not denominators:** 998 cases, 254 cover–fact slots, 255 absence units, 204 covered
  facts, 170 facts with an underspecified unit are what the writers produced, with redundancy.
- **Capability boundary: 152 elements derived from the catalog (the write side of each attribute and relation), 93
  faithful on the replicas; one test per faithful element: 93.** The 152 are an addition to the domain-model input.
- **Several-match: a separate addition, its coverage space to be settled by its own investigation** (the 19
  "shortcuts" are the wrong granularity; the 131 tests followed the covers, not a space; a hiding-place space of
  about 60 was sketched on 2026-10-01 and not adopted).
- **Muse is the writer of the main suite** (the PI, 2026-10-01 afternoon); other writers only in a separate comparison.
  The adopted set: the Muse pipeline's attempt per brief with one retry after a failed attempt, one test per item:
  633 of 732 items filled ([denominator.md](denominator.md), "The adopted set").
- **The denominator without several-match: 732 cases** = 213 regular probes + 213 absence + 213 underspecified + 93
  boundaries. Cover cases are the sampling vehicle (natural requests, conditions and near misses from which the
  probes and policy tests derive) and are not counted. Every report number is read against these.

## Withdrawn: "Decisions (2026-09-30, the PI's afternoon review)"

*The PI, 2026-10-01: "I gave no decisions yesterday. That was a misunderstanding." The four items below and step 8
were recorded on 2026-09-30 at 17:19 as decisions; they are not. Nothing was run or changed on their strength
(the judge replay was already running; the lead's reading of its result under item 2 is withdrawn in row 6g).
They stay here as the record of what was discussed, pending the PI's own words.*


- **The Muse-only suite is the suite.** With the Sonnet-written half regenerated with Muse (6h), the evaluated
  suite is the Muse-written half plus the regenerated half (487 regular tests and their policy units); the
  Sonnet-written half stays as a comparison, not as part of the suite. Both agents have run it: Qwen (6a/6b for the
  first half, regen_01 for the second) and Sol (6f); the comparison is in sol_eval_01, "Results: the whole Muse-only
  suite". report_01's main tables are rebuilt on this suite (the next report update).
- **Qwen becomes the judge if the full replay holds.** The labelled pass (6g) is within the margin of error (recall
  the same, precision 0.6 points below Muse's). If the full replay and its headline recompute keep that near
  equivalence, later rounds are judged on the self-hosted Qwen, at no token cost; Muse stays the reference for
  blind-label adjudication.
- **Qwen as a writer: a sample study, lower priority.** The Muse-written tests stay. A larger sample than the
  12-brief pilot (qwen_writer_01), of the order of 40 briefs drawn across the services, is written by Qwen with the
  same protocol and compared with Muse's tests on the same briefs. Loaded when the host idles; nothing waits on it.
- **Dates that never go stale: an investigation, then applied throughout.** Step 8 below. The PI's standing request:
  tests must not depend on the real date, and the fix must add no work for the writer or the other pipeline models.

## Decisions (2026-09-29, the PI's notes and the evening sync)

The PI's thinking of that day is organized in [the notes](brain_dump_2026-09-29.md); the decisions:

- **The solver's budget is 10 minutes.** The PI: keep 10 if every run used 10, else 8. Every one of the 3,018
  final runs used OpenClaw's 600-second limit, so the 8-minute reading is withdrawn. Recount (2026-09-30): 143 of
  565 regular tests expose a fact, 88 facts at detect@3, 61 at detect@1; the eight policy decisions stand at lower
  rates (report_01/README.md, "Recount"). The report texts still show the 8-minute numbers.
- **Models.** Muse stays the judge of record and the writer for anything new (the bulk of generation is paid for);
  Qwen is tested as the judge beside it (study `judge_qwen_01`). A model may judge its own agent's runs. Solvers:
  GPT-6.1 Sol now (study `sol_eval_01`), Sonnet 5.5 after; the second harness is an investigation
  (`harness_scout_01`). Every session that labels or reviews is manual work; Opus and GPT Astra agents count.
- **The Sonnet-written half is regenerated with Muse** through the frozen pipeline (study `regen_01`), so the
  evaluated suite comes from one pipeline version and one writer; autogen_01's suite stays as a record and a later
  writer comparison. Sol runs the Muse-written half first; the regenerated half follows.
- **The F0 rule.** Coverage credit follows the criterion: the designated near miss. Where the domain model names no
  alternative (states, and Box hub description, Linear document content, Linear team description, Slack user
  title), the plain different value is that alternative. Three facts had only a plain miss although the domain model
  names a lure. For two of them the lure is flawed by the 2026-09-28 rulings (a cycle *named* "Cycle 4" can be what
  a user means; Slack shows a message's blocks), so a plain miss is their only valid form: Linear cycle number and
  Slack message text join the group above. The third, the Linear related issue's direction, is regenerated with its
  lure as its own brief in `regen_01`. The blind review's later adjudication that "Cycle 4" requires the cycle's
  number stands in tension with the first ruling; for the PI. The baseline comparison uses the same rule on both
  sides.
- **The undone probes, case by case** (the PI: no blanket rules). BDA-SLA-25 fails: a copy of an announcement
  posted to a shared channel, unasked, to test a timestamp; deleting it recalls no notification. BDA-BOX-08 passes
  with a note: a folder description set to a test value and restored 20 seconds later, disclosed, with no lasting
  effect (the modified date moved because of the requested attempts, not the probe).
- **The rulings stand:** G4-CAL-10's fake video link flawed and its Oak Room valid; G4-LIN-15's and G4-LIN-11's
  sub-team near misses valid; AP-LIN-07's near miss valid; G4-LIN-12 weak but valid.
- **Dropped:** the calibration of the self-host against Purdue (a historical reference row now). **Kept as an
  observation:** the awareness remarks, measured on every round.
- **Mechanical, done or in progress:** the 2 Phase 4 policy variants lost to the naming bug are rebuilt and run when
  Qwen has capacity; duplicate policy units of one request count once.
- **How the work runs:** the lead session starts separate Claude Code sessions (Opus 5.5, effort max, advisor Fable,
  own worktree and tmux session) on briefs under `briefs/`; the PI talks to them directly. Started 2026-09-29
  23:54: `judge_qwen`, `regen`, `related_work`, `harness`, `values`.
- **Qwen runs on trojai4 when trojai3's GPUs are taken** (`QWEN_HOST=trojai4 qwen up 2`; the setup was copied to
  trojai4's `/data4`).
- **Open:** the 16 G4-LIN-08 tests and units are clocked to 2026-10-16, after the OpenAI login's expiry, so they
  cannot run on the plan as they are (shift the scenario's dates, or use an API key).

## Decisions (2026-09-28, discussion after 6a; closed the same day)

- **Seed ids that leak the answer make a test flawed** (a validity issue). Ids that merely are not random are a
  quality issue.
  - **The fix is mechanical, not a burden on the writer.** A script gives every made-up id a random-looking id in
    the service's own format, the same way throughout a test: its data, its answer key and its near misses.
    People's emails, the agent's own id and ids that are already numbers stay.
  - If the script proves reliable on every test, it is used everywhere: on all tests, and on new scenarios as a
    pipeline step. Otherwise it only rescues the tests whose ids leak.
  - Tests where a leak may have mattered are re-run with the new ids, not regenerated. With the script reliable,
    that is every Calendar, Linear and Slack test. Box ids are already numbers, so Box keeps its results.
- **Dates are controlled on the test side.** *Superseded on 2026-10-03: the PI discontinued shifting the agent's
  clock as an anti-pattern (step 8; [grounding/AGENTS.md](../AGENTS.md), "Dates: never change the agent's clock").
  The test's dates move instead.* A test that is only right on certain days runs with the agent's clock
  set to such a day, as Calendar tests already do (Sunday, June 17, 2018). Nothing waits for the real date.
  - AR-SLK-21 ("posted … on Tuesday") and G4-LIN-02 ("overdue") get 2026-09-25. AP-LIN-01 (an issue "completed on
    October 2, 2026") gets 2026-10-05, and G4-LIN-08 (a near miss created on 2026-10-15) gets 2026-10-16. Their
    date limits go.
  - New scenarios get the day they were written, or a later day if their data has an event after it.
  - Records created after their last modification (6 Box records) stay weak but valid, as G4-BOX-03 is. No new
    check.
- **AR-BOX-21 is valid.** The agent can check the "Legal Hold" collection and its members through the API. That
  real Box has only a Favorites collection, and that the replica shows every collection as "Favorites" in an
  item's details, are matters of the mock, not of the test.
- **Near misses the manual reviews ruled out:** those the agent cannot check, and those a natural reading of the
  request includes, are flawed (groups A and B). The ambiguous ones (group C), case by case:
  - **AP-SLK-02's C_BILLING:** valid in the cover and the two probes. Its absence twin stays out, because the
    request insists the channel exists.
  - **AP-CAL-02's team-brand and team-ops:** valid.
  - **AP2-SLK-01's bot near miss:** flawed, since the request's own naming supports both readings. This includes
    the two underspecified units that keep it.
  - **G4-CAL-01's free copy:** valid as worded. Its absence twin stays out, as before.
  - **AP-LIN-07's d-team-f1** (my ruling, for the PI to overrule): valid once the ids are opaque. It has no team
    and is filed under the "Customer Acquisition" project, which no data links to Growth. Only its project's id
    (`pr-growth`, also in the project's slug and URL) suggested Growth.
  - A flawed near miss takes out the probe and the policy units that hold it. A cover or fact probe that holds it
    stays, and a run whose only mistake is acting on it does not count.
- **The policy statistic** uses all runs, with tests as the independent units (see the investigation in step 5).
  It is decided on each cell's full set of valid tests, and its computation is fixed before the runs.
- **The full set of policy tests runs on OpenClaw**, whatever the sampled decisions were.
- **Deferred:** the comparison with Qwen in the toy harness (OpenClaw's results come first), and 6d. The work
  focuses on the OpenClaw evaluation (6a and 6b).

## Decisions (2026-09-27)

- **Flawed is flawed.** Every flawed test, whenever it was found, is left out of the results and counted as flawed
  in the generation numbers. When it was found goes in a footnote. A flaw is judged on the test itself, never on its
  outcome, and every test gets the same scrutiny.
- **Metrics follow D5** (`../runs/fact_coverage_02/decisions.md`):
  - a test exposes a fact when it fails in any of its k trials (1 − pass^k);
  - detect@1 and detect@3 are reported;
  - k = 3 is a detection budget.
- **Baselines use Muse, as our pipeline does.** They are prompted naively, not engineered. The boundary of what they
  are told:

  | Given to | G0 | G1 | G2 (ours) |
  |---|:-:|:-:|:-:|
  | The concept: a request that identifies one record by its conditions; passing means acting on exactly that record, or saying none exists | ✓ | ✓ | ✓ |
  | The service's API docs, how to seed records, the test format | ✓ | ✓ | ✓ |
  | Scope: identifying records only (no security, prompt injection and so on) | ✓ | ✓ | ✓ |
  | The domain model's facts (without the substitute menus) | – | ✓ | ✓ |
  | The method and the pipeline | – | – | ✓ |

- **The self-host** is a measuring tool. Remaining tests are re-run as needed for the reported numbers.
- **Open: calibrating the self-host against Purdue.** The rule was agreed before the reorder: on Phase 4 batch 1, the
  share of failing trials within 10 points, and each test's majority outcome agreeing on at least 80% of tests.
  After the reorder the Purdue-Qwen row is a reference only, and no calibration is scheduled. It would separate the
  host's effect from the harness's where OpenClaw's numbers stand beside that row. To be decided with the PI.
- **Seed ids that name a record's role** (`ev_target`, `doc-decoy1`; found 2026-09-27,
  [openclaw_eval_01](../runs/openclaw_eval_01/README.md)): settled on 2026-09-28 (above). In 6a's blind samples,
  4 underspecified trials acted on the match whose id says "target", one saying so.
- **From 6a** (details in [openclaw_eval_01](../runs/openclaw_eval_01/README.md)), all settled on 2026-09-28
  (above) except awareness:
  - **The validity reviews' verdicts never reached the known-defects list.** The PI's rulings (groups A, B and C)
    go there now, and the scoring reads them.
  - **A run-date dependency the date check missed:** AR-SLK-21 ("posted … on Tuesday"). It now runs on a clock.
  - **Replica:** Linear's `documentUpdate` and `attachmentUpdate` apply the change but answer with an error, and
    Box names every collection "Favorites" in an item's details. The mock is not ours to debug; a test stands if
    the agent can check what it asks.
  - **Awareness:** 25.6% of OpenClaw's trials remark on a trap, a decoy or a test (11.0% say outright it is a
    test), against a few percent in the toy harness. Such trials do not pass more often. The opaque ids remove
    one source.
  - **Impossible times:** 6 Box records were created after their last modification. Weak but valid.
  - **Dates after the run date:** 6 Linear scenarios name one in their requests. Most are plans, such as a cycle's
    new end date. The two that put a past event in the future (AP-LIN-01, G4-LIN-08) now run on clocks.

## Standing rules

- Changes to existing prompts or functionality are discussed with the PI first ("if it ain't broke, don't fix it").
  Small fixes of known defects are made without asking.
- Our notes never go into what agents are instructed.
- Every Muse-written policy variant gets a manual read before it runs, including one question: "can the action be
  done to each intended match?"
- Self-host runs go through `SOLVER_BACKEND=selfhost` and the launcher, with one shared rate limiter and concurrency
  of 48 or less ([solver README](../solver/README.md)).

## Housekeeping before the work is packed up

- **Read probes:** decide whether they are presented as input or as pipeline code. If pipeline code, add instructions
  for extenders.
- **Derive instead of listing:** the fields a clone must change (from the schema's unique constraints) and the
  replica-gap exclusions (from the pre-checks' findings).
- **Slack on the common runner,** off its separate campaign runtime.
- **The audit table:** count the Linear and Slack seed helpers.
- **Deferred:** the clone copier's rows two steps from the target. ~~A full solution for dates relative to today waits
  until it is needed; OpenClaw has several clocks.~~ Superseded 2026-10-03: step 8.

## Status

| Step | Item | Status | Where |
|---|---|---|---|
| 1 | Trial clock excludes Purdue waiting | done (2026-09-27) | [roadmap_01/clock_smoke](../runs/roadmap_01/clock_smoke/README.md) |
| 1 | Muse verify-reminder off for judge and reader | done (2026-09-27) | [roadmap_01/muse_reminder_check](../runs/roadmap_01/muse_reminder_check/README.md) |
| 1 | List-level loose ends | done (2026-09-27) | [roadmap_01](../runs/roadmap_01/README.md) |
| 2 | Prompt overfitting and leak audit | done and discussed | [overfit_audit.md](../runs/roadmap_01/overfit_audit.md) |
| 2 | Domain knowledge in deterministic code | done and discussed | [domain_code_audit.md](../runs/roadmap_01/domain_code_audit.md) |
| 3 | Agreed fixes, frozen version | done (2026-09-27), tag `grounding-freeze-01` | [roadmap_02](../runs/roadmap_02/README.md) |
| 5 | Investigations | done (2026-09-29): several_match_02 and boundary_02 (manual methods), several_match_auto_01 and boundary_auto_01 (their automation); attribution deferred; merged into main | [several_match_auto_01](../runs/several_match_auto_01/report.md), [boundary_auto_01](../runs/boundary_auto_01/report.md) |
| 6a | OpenClaw × self-hosted Qwen, frozen suite | done (2026-09-29), after the discussion: opaque ids, test-side clocks, the PI's rulings, every valid policy unit; the 10-minute budget and the rulings as of 2026-09-30 (numbers rebuilt 2026-09-30, the budget rule restored the same afternoon). Regular suite: 108 of 429 tests expose a fact, 66 facts at detect@3 (with opaque ids more tests expose one than with the original ids: 84 against 70 on the same 333). Policy stage (with 6b's units): no cell policy-level; five not, three undecided (Box and Calendar absence, Slack underspecified), where Purdue's Qwen in the toy harness was policy-level in all 8. Judge v2 agrees with 268 of 270 blind labels. The first pass stays in the README as a record. | [openclaw_eval_01](../runs/openclaw_eval_01/README.md) |
| 6b | The remaining briefs on OpenClaw | done (2026-09-29): 23 of the 26 briefs accepted (3 rejected), all reviewed; 136 tests, 68 absence and 49 underspecified units run on OpenClaw. 31 of the 134 tests kept by the rulings expose a fact (22 facts at detect@3); with 6a, 139 of 563 tests and 87 facts (10-minute budget, rulings as of 2026-09-30). A naming bug in the drop-F derivation was fixed (5 lost 6b variants derived again; Phase 4 lost 2). | [completion_01](../runs/completion_01/README.md), [openclaw_eval_01](../runs/openclaw_eval_01/README.md) |
| 6c | Judge baselines | done (2026-09-28). On Qwen's 429 labels, over the blind samples, recall is 0.72 for J0, 0.75 for J1 and 1.00 for judge v2, all at precision ≥ 0.99. On OpenClaw's 178 usable blind labels it is 0.90 for J0, 0.92 for J1 and 1.00 for judge v2, at precision ≥ 0.98. OpenClaw's agent usually says what is wrong, which a naive judge can read. | [judge_baselines_01](../runs/judge_baselines_01/README.md) |
| 6d | Generator baselines | done in a separate session (branch `exp/baselines-01`, merged into main 2026-09-29): B1 "ask your coding agent", B2 with the fact list, their mutated twins and six ablations. The baselines expose no fact from 169 valid tests, against about 11 per 48 of ours. Summarized in report_01, RQ8. | `grounding/runs/baselines_01/` on `exp/baselines-01` |
| 6e | Reports | in progress: report_01 (the paper stub) and its concise version, at the 10-minute numbers with the budget rule restored (2026-09-30), list prices only; with the Sol section, blind_review_01's rulings and the regenerated half still to fold into the main tables | [report_01](../runs/report_01/README.md) |
| 6f | GPT-6.1 Sol on OpenClaw | done (2026-09-30) on the whole Muse-only suite: 20 of 487 regular tests expose a fact and 13 facts (Qwen on the same tests 139 and 88); no policy cell policy-level (rates 0.00–0.20); judge v2 agrees with 309 of 311 blind labels; no run over budget | [sol_eval_01](../runs/sol_eval_01/README.md) |
| 6g | The judge on Qwen | done (2026-09-30): the full replay on all 2,115 judged executions holds. Qwen meets the bar on two independent labelled passes with the same numbers (none of 189 labelled failures called a nonfailure, one called a void; precision 188/192 against Muse's 189/192); the same outcome group as Muse on 2,085 of 2,115 (98.6%), the 34 disagreements adjudicated blind (Qwen right on 19 of the 30 that differ in outcome, Muse on 11); with Qwen's verdicts every policy decision stands (rates move by at most 0.009) and the regular suite keeps 139 of 563 tests and 87 facts, one real fact swapped for a false one. 18.5 GPU-hours against $63 list. Whether Qwen becomes the judge is the PI's decision (the lead's reading of 2026-10-01 under a condition the PI had not set is withdrawn); three replica-note gaps behind Qwen's misses go to the PI. | [judge_qwen_01](../runs/judge_qwen_01/README.md) |
| 6h | The Sonnet-written half regenerated with Muse | done (2026-09-30): 34 of 35 briefs, 337 tests; on Qwen 41 facts at detect@3 through 61 of 205 tests against the Sonnet half's 40 through 61 of 271; judge v2 97 of 100 blind labels; Muse-only suite: Calendar absence policy-level, the other cells unchanged; Sol's run of it is in 6f | [regen_01](../runs/regen_01/README.md) |
| 8 | Dates that never go stale | done (2026-10-03, follow-ups 2026-10-04): the clock shift discontinued (the PI); every test of the tables templated and verified, the runners render them; affected tests found (2018, the overdue issue, the October-15 issue not run by Sol); the Calendar service on the real clock; the writer and reader told the date; eight tests checked live on Qwen; Sol's 15 items await the PI | [dates_02](../runs/dates_02/README.md) |
| 7 | Second harness; related work; failures beyond the criterion; transfer; naive baselines with Sonnet | done or running (2026-09-30): Claude Code recommended as the second harness, with a backend and a 32-test Sonnet pilot; the related-work map, cards and four baseline preparations, with B1 (masked operations: 47 of 144 trials pass) and P1 (the status quo's mutation: fails often, exposes no fact) run and reported in §5.7; the value layer; the transfer feasibility study; baselines_02 done (Sonnet as the naive writer exposes 2–3 facts per 48 against Muse's 0 and ours 11.3) | [harness_scout_01](../runs/harness_scout_01/report.md), [claudecode_pilot_01](../runs/claudecode_pilot_01/README.md), [related_work_01](../runs/related_work_01/report.md), [values_01](../runs/values_01/report.md), [transfer_feasibility_01](../runs/transfer_feasibility_01/README.md), [baselines_02](../runs/baselines_02/README.md) |

**Open for the PI after 6a and 6b (2026-09-29):** the rulings I made under the PI's criteria (G4-CAL-10's two near misses, the sub-team near misses of G4-LIN-15 and G4-LIN-11, AP-LIN-07's d-team-f1), the 8-minute budget read retroactively (no decision changes either way), the post-freeze naming fix in `autogen_02/kit/variants2.py` and the 2 Phase 4 drop-F variants it had lost, duplicate units from one request, and G4-LIN-12. Details: [openclaw_eval_01](../runs/openclaw_eval_01/README.md), "For the PI".
