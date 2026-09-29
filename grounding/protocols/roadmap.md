# Roadmap after autogen_02

Agreed with the PI on 2026-09-27 after [autogen_02](../runs/autogen_02/overview.md), and re-agreed later that day
once steps 1 and 2 were done. The work is done in steps. The PI steps in where a step needs a decision. Progress is
recorded in the status table at the end.

## The goal

A final evaluation of the automated grounding-test system, from three angles:
1. **What the system finds in real agents:**
   - **Agents:** OpenClaw with the self-hosted Qwen3.8-27B first; more models and harnesses later.
   - **Per agent:** the facts the regular tests expose, the eight policy decisions, and how the failures happen
     (analysed by hand).
   - **A reference row:** Purdue's Qwen on the bare solver loop (autogen_02).
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
- **Dates are controlled on the test side.** A test that is only right on certain days runs with the agent's clock
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
- **Deferred:** the clone copier's rows two steps from the target. A full solution for dates relative to today waits
  until it is needed; OpenClaw has several clocks.

## Status

| Step | Item | Status | Where |
|---|---|---|---|
| 1 | Trial clock excludes Purdue waiting | done (2026-09-27) | [roadmap_01/clock_smoke](../runs/roadmap_01/clock_smoke/README.md) |
| 1 | Muse verify-reminder off for judge and reader | done (2026-09-27) | [roadmap_01/muse_reminder_check](../runs/roadmap_01/muse_reminder_check/README.md) |
| 1 | List-level loose ends | done (2026-09-27) | [roadmap_01](../runs/roadmap_01/README.md) |
| 2 | Prompt overfitting and leak audit | done and discussed | [overfit_audit.md](../runs/roadmap_01/overfit_audit.md) |
| 2 | Domain knowledge in deterministic code | done and discussed | [domain_code_audit.md](../runs/roadmap_01/domain_code_audit.md) |
| 3 | Agreed fixes, frozen version | done (2026-09-27), tag `grounding-freeze-01` | [roadmap_02](../runs/roadmap_02/README.md) |
| 5 | Investigations | in progress (separate session, branch `exp/investigations-01`) | – |
| 6a | OpenClaw × self-hosted Qwen, frozen suite | done (2026-09-29), after the discussion: opaque ids, test-side clocks, the PI's rulings, every valid policy unit, the 8-minute budget. Regular suite: 104 of 429 tests expose a fact, 66 facts at detect@3 (with opaque ids more tests expose one than with the original ids: 80 against 65 on the same 333). Policy stage (with 6b's units): no cell policy-level; five not, three undecided (Box and Calendar absence, Slack underspecified), where Purdue's Qwen in the toy harness was policy-level in all 8. Judge v2 agrees with 268 of 270 blind labels. The first pass stays in the README as a record. | [openclaw_eval_01](../runs/openclaw_eval_01/README.md) |
| 6b | The remaining briefs on OpenClaw | done (2026-09-29): 23 of the 26 briefs accepted (3 rejected), all reviewed; 136 tests, 68 absence and 49 underspecified units run on OpenClaw. 34 of the 136 tests expose a fact (22 facts at detect@3); with 6a, 138 of 565 tests and 87 facts. A naming bug in the drop-F derivation was fixed (5 lost 6b variants derived again; Phase 4 lost 2). | [completion_01](../runs/completion_01/README.md), [openclaw_eval_01](../runs/openclaw_eval_01/README.md) |
| 6c | Judge baselines | done (2026-09-28). On Qwen's 429 labels, over the blind samples, recall is 0.72 for J0, 0.75 for J1 and 1.00 for judge v2, all at precision ≥ 0.99. On OpenClaw's 178 usable blind labels it is 0.90 for J0, 0.92 for J1 and 1.00 for judge v2, at precision ≥ 0.98. OpenClaw's agent usually says what is wrong, which a naive judge can read. | [judge_baselines_01](../runs/judge_baselines_01/README.md) |
| 6d | Generator baselines | not started | – |
| 6e | Reports | not started | – |

**Open for the PI after 6a and 6b (2026-09-29):** the rulings I made under the PI's criteria (G4-CAL-10's two near misses, the sub-team near misses of G4-LIN-15 and G4-LIN-11, AP-LIN-07's d-team-f1), the 8-minute budget read retroactively (no decision changes either way), the post-freeze naming fix in `autogen_02/kit/variants2.py` and the 2 Phase 4 drop-F variants it had lost, duplicate units from one request, and G4-LIN-12. Details: [openclaw_eval_01](../runs/openclaw_eval_01/README.md), "For the PI".
