# attribution_01: which component owns a failure? (report)

*Roadmap step 5, first investigation. Plan: [plan.md](plan.md), pre-registered 2026-09-27 22:40 EDT, with dated
amendments. Written 2026-09-27.*

## The answer in brief

- **The judge is right for one class and blind to two.**
  - It attributes a failure to the mock when the replica notes it reads name the gap. Judge v2 made no false alarm
    on 403 agent-owned failures.
  - It never flagged a test-wording defect: 0 of 31 trial verdicts across three judge versions.
  - It flagged a test-construction defect only when a write was rejected with a clear error (3 of 30 trials).

  The judge takes the test as given, so this is what it can do.
- **Test construction is caught before any run.** The kit's write-feasibility pre-check rejects both
  test-construction scenarios in the development set (SLK-21 v1, LIN-25 v1). All 30 of their trials were
  preventable, and the repaired reruns pass the same check.
- **A trace scan finds replica gaps on the failure path.** It needs no model calls. It flags 10 of 11 mock-owned
  trials and 17 of 30 test-construction trials; the latter cover every test-construction scenario.
  - Its 5 flags on agent-owned failures are all contested (C1, C2).
  - These numbers are in-sample: the rules were refined on this set.
- **Test wording remains a job for people.**
  - No mechanical source flags any of the 7 test-wording tests.
  - A Muse reader of the solver's reading flags 4 of 7 (7 of 19 trials), with 3 false alarms in 39 hard negatives.
  - Most of its misses it reads as natural ambiguity: the standard the PI ruled after those labels were written. The
    labels themselves may need re-ruling (C4 below).
- **Where attribution belongs:** a separate step after the judge that combines the evidence per class, with human
  review for the classes no source settles. The judge keeps its mock calls as one input. The proposal is under
  "Recommendation".

## The development set

- **722 hand-labelled trials:** autogen_02 Phases 1, 3 and 4, plus fact_coverage_02. Owners are assigned by rule
  and by reading the notes. They were committed before any scoring ([devset.json](devset.json),
  [build_devset.py](build_devset.py)).
- **Owners, by trials (distinct tests):**
  - agent 545 (262);
  - none 115 (88);
  - test-construction 30 (10, from 2 scenarios);
  - test-wording 19 (7);
  - mock 11 (8, 5 mechanisms);
  - harness 2 (2).
- **Two levels of ground truth.** Each trial has an owner. Each test also has a flaw status, from roadmap_01's
  `known_defects.json` and the labels.
- **Five doubtful owners** are marked; the scores change by at most one trial without them.

## Results

Each cell gives flags / owned trials (tests with at least one flag / tests). "False alarms" counts flags on
agent-owned failures.

| Source | test-wording | test-construction | mock | harness | False alarms |
|---|---|---|---|---|---|
| Judge v2 `artifact` (autogen_02 and 24 fact_coverage_02 panel trials) | 0/13 (0/5) | not judged | 2/2 (2/2)¹ | 0/2² | 0/403 |
| Judge v1 on Muse (Phase 1; fact_coverage_02 dev split) | 0/12 (0/4) | not judged | 5/8 (3/5) | – | 3/329³ |
| Judge v1 on Sonnet (fact_coverage_02 dev and held-out test splits) | 0/6 (0/2) | 3/30 (1/10) | 7/9 (5/6) | – | 3/166³ |
| Pre-run checks (write feasibility, observability, witness)⁴ | – | 30/30 (10/10) | 0/1 (0/1) | – | 0 of 2 controls |
| Trace scan, naive (any documented gap in the trial) | 4/19 (2/7) | 20/30 (7/10) | 11/11 (8/8) | 2/2 | 80/545 |
| Trace scan, counterfactual (the gap decided the outcome)⁵ | 0/19 (0/7) | 17/30 (7/10) | 10/11 (7/8) | 2/2 | 5/545³ |
| Muse objection reader (source 4; 58 trials) | 7/19 (4/7) | – | – | – | 3/39 |

1. **Circular:** both labels were revised to `artifact` after v2 said so (Phase 1, 00:40). v2 has never been scored
   on a mock-owned trial it did not help label.
2. v2 judged the labelled first attempts as `not_established` and `correct_absent`: no failure, but no artifact call
   either.
3. The false alarms are the contested cases below, not clear errors: P-LIN-10 ×3 for v1 and the scan (C1), and
   AT-BOX-23-I11 t3 and P-SLK-23-I13 t3 for the scan (C2).
4. **Pre-run checks** work at the test level, before any trial ([precheck.json](precheck.json)).
   - Write feasibility rejects SLK-21 v1's `:white_check_mark:` (`invalid_name`) and LIN-25 v1's non-UUID label ids,
     and passes both repaired reruns.
   - Observability misses P-LIN-03-I12's unreadable project lead, because the lead's name appears in the user
     listing. The check tests whether the value appears anywhere, not in the right place.
   - The witness check flags P-G4-LIN-01-I13, a probe without its trap. Its one labelled trial "passed" without
     testing anything.
5. The counterfactual rule was refined on this set (plan.md amendments), so its scores are in-sample.

**Where each source's reason names the component:**
- the judges' mock calls name the ignored filter or the unreadable field correctly;
- v1 on Sonnet names the seed's non-UUID ids in 2 of its 3 LIN-25 calls;
- the counterfactual scan names the gap and the step in every flag.

## What each source can and cannot see

- **The judge** reads one trajectory under the test's assumptions.
  - It sees a replica gap when the replica notes describe it and the trajectory shows the call.
  - It cannot see that a request admits another reading, or that the seed is unrealistic, unless the replica
    rejects something.
  - v2 and v1 were never scored on the same trials. The only held-out split (v1 on Sonnet) has no v2 verdicts.
- **The pre-run checks** see what the replica would do with the intended write and reads.
  - They prevent test-construction flaws of the write kind at no model cost.
  - They cannot see gaps that depend on the agent's route, such as ignored filters.
  - They cannot see wording.
- **The trace scan** sees every documented gap the agent's own calls hit. Its counterfactual asks whether the real
  service, honouring the filter, would have returned the item the agent acted on.
  - It cannot tell an agent that relied on the filter from one that noticed the mismatch and acted anyway (C2).
  - It sees a test-construction flaw only in the trials where the flaw bites. So it should flag tests, not trials:
    one flagged trial excludes the test.
- **The objection reader** reads the request against what the solver did. It is the only source that flags any
  wording defect.
  - Its three false alarms repeat known agent failure families. In two, it accepted "in my Favorites" for a folder
    inside a favourite folder (containment taken as membership).
  - In one, it accepted acting on all matches of a singular request.

## Contested cases, for the PI ([contested.json](contested.json))

- **C1. P-LIN-10 ×3: an ignored filter whose response betrays it.**
  - For the mock: the replica ignored `parent`, and real Linear would not have returned the item. The Phase 1 rule
    from 00:40 ("an ignored filter decided the outcome") applies. Both v1 judges and the scan agree.
  - For the agent: the response listed the epic itself as its own sub-issue. In one trial the agent remarked on this
    and still trusted the rest.
  - The labels predate the documentation of this gap.
- **C2. Reliance versus noticing.** The labels call a failure the mock's only if the agent relied on the ignored
  filter. Noticing the mismatch and acting anyway makes it the agent's (AT-BOX-23-I11 t1 versus t3; AT-SLK-23-I13
  t1 versus P-SLK-23-I13 t3). The counterfactual rule would make all four the mock's.
- **C3. "Linear has no documents" (3 trials).**
  - The benchmark's own system prompt lists 19 Linear operations and none for documents or projects. My override
    had said the prompt names no endpoints, which was wrong; it is corrected, and the owner is unchanged.
  - Is this the agent's error, or a harness or test issue?
- **C4. The test-wording labels predate the natural-ambiguity ruling.**
  - The reader reads 12 of the 19 test-wording trials as natural ambiguity (9) or solver error (3). Examples:
    - "Architecture review: storage" is still an architecture review;
    - "about travel costs" most naturally attaches to the comment.
  - Under the PI's ruling, some of the 7 tests may be valid and their failures the agent's. A ruling on the 7 tests
    would settle both the labels and source 4's recall.

## Also found

- **Passes through a replica error.** 17 of the 115 passing trials, about half of all passing Linear trials, hit a
  failing Linear query (`projects`, or a nested connection) on the way. 14 of them are correct "none" answers on
  no-target tests.
  - The replica notes say that "none" after such an error establishes nothing.
  - Whether each of these passes was earned needs reading. A probe's pass there may not certify that the near miss
    was rejected.
- **A harness mechanism the dev set lacks** (found in several_match_01). The executor rewrites API URLs only in its
  bash-level `curl` function. An agent that calls the API from a Python script (`subprocess`, `urllib`) reaches no
  service and gets empty responses.
  - It happened once in about 2,360 recorded trials (SM-CAL-01 t3); the agent's time budget ran out.
  - A trace scan can flag it mechanically: a script-level HTTP call followed by an empty response.
- **Label granularity.** The SLK-21 and LIN-25 labels mark every trial of the flawed scenario `artifact`, including
  trials where the flaw never came into play (for example a correct "none" that never tried the reaction). That
  matches the PI's rule that flawed is flawed, and it is why test-level scoring is the right view for
  test-construction.

## Recommendation: an attribution step after the judge

For each failing trial, in order:
1. **Harness:** under the agent clock, a `ceiling` termination or an infrastructure error is the harness's. The
   runner already retries it. Old-clock timeouts stay doubtful.
2. **Test (construction):**
   - a pre-run check failure excludes the test before any run;
   - a rejected write that the request itself asks for (in the trace scan) flags the test, and all its trials are
     excluded.
3. **Mock:**
   - the judge's `artifact` with a documented gap, and the counterfactual scan agreeing: the mock's;
   - only one of the two: contested, for review.
4. **Test (wording):** the objection reader's `test_wording` sends the test to human review with the reader's
   argument. It never excludes automatically, because of its false alarms and the open standard (C4).
5. **Otherwise:** the agent's.

This keeps the judge's prompt as it is ("if it ain't broke"). It adds only mechanical steps that already exist
(pre-checks, termination) or were built here (trace scan), plus one reader call per failing trial of a test with a
stated alternative reading. Nothing here changes the existing system; adopting any of it is the PI's call.

## Caveats

- **Denominators outside `agent` are small:** 7, 10, 8 and 2 tests.
- **The scan and the reader were built and run on this development set.** A fresh set, such as the step-2 OpenClaw
  labels, is the real test.
- **The labels and I share an author.** The contested cases are where that matters.
- **The reader read the judge's bundle,** which states the author's decision, so its question is not blind to the
  test's intent.

## Files

- [plan.md](plan.md): the plan and its amendments.
- [devset.json](devset.json) and [build_devset.py](build_devset.py): the development set.
- [contested.json](contested.json): the contested cases.
- Source 1: [score_judge.py](score_judge.py) → [source1_judge.json](source1_judge.json).
- Source 2: [precheck.py](precheck.py) → [precheck.json](precheck.json) and precheck/ (roadmap_01's
  `witness_check.json` for the witness check).
- Source 3: [scan_traces.py](scan_traces.py) → [source3_traces.json](source3_traces.json).
- Source 4:
  - [objection_reader.py](objection_reader.py) and
    [prompts/objection_reader.md](prompts/objection_reader.md);
  - the readings, requests and usage in objection_reader/;
  - the summary in [source4_objection.json](source4_objection.json).

## Cost

- Muse, source 4 only: 58 calls, $2.49 at list, $0.17 billed.
- Input: 1.35M tokens, of which 56k were cache reads (a fresh session per call).
- Output: 186k tokens.
- No agent runs. The pre-checks used the local replica only.
