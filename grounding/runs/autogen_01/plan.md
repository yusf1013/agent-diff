# Plan: automated test generation and evaluation with Claude Code Sonnet agents

Written on 2026-09-25, before any generation or judging run. Changes after the first run are added as dated
amendments at the end; nothing above them is edited.

## Question

Can Claude Code Sonnet agents, inside fixed scaffolding, do the two jobs done by hand in
[fact_coverage_01](../fact_coverage_01/README.md) and [fact_coverage_02](../fact_coverage_02/README.md), at the same
standard?
1. **Generation:** from a domain model and its fact catalog, write fact-discrimination scenarios: a natural request, a
   seed with one target, and one decoy per (fact, substitute), with mechanically checked claims.
2. **Evaluation:** judge each solver trial (outcome, exposed facts, mechanism), as the manual labels do.

The standard is the hand-built exemplars: the pilot's 31 scenarios, the 18 new scenarios of fact_coverage_02 with
their probes, fact probes and hidden-target tests, and the 267 manual labels. The G3 runs are not a reference.

## What counts as automated

| Part | Who | Counts as |
|---|---|---|
| Writing a scenario (request, seed, reference query, decoy claims, probe and write calls) and repairing it | Sonnet (writer agent) | automated |
| Reading a scenario cold: which records match, and why each near miss fails | Sonnet (reader agent) | automated |
| Judging a trial | Sonnet (judge agent) | automated |
| Choosing facts per brief, expanding seed operations, validators, replica pre-checks, deriving the suite, running Qwen, triage, scoring | code (the kit) | scaffolding, written by hand before the main runs |
| Domain inputs: the four additions, the seed vocabulary, two worked examples | my drafts | manual domain input |
| Validity review of accepted scenarios, and the comparison | me | manual evaluation |

Agents are Claude Code sessions run headless (`claude -p --model sonnet`, which resolves to `claude-sonnet-5`) on
the user's subscription. Each runs in a clean workspace outside the repository, in restricted mode, with no MCP servers:
- **The writer** gets file tools inside its workspace only: Read, Write, Edit, Glob, Grep. No Bash.
- **The reader and the judge** get no tools; their input is in the prompt, and their output follows a JSON schema.

No agent sees the manual labels, the exemplar scenarios of its assigned facts, or this repository. **Agents never
certify their own work.** The orchestrator runs every check and sends failures back by resuming the same session.
Every call's usage (input, output, cache-creation and cache-read tokens, list-price cost estimate) and its
transcript are saved.

## Pipeline

1. **Brief** (code): domain, scenario id, and 2 to 4 primary facts. Facts whose natural check depends on a filter the
   replica ignores, or on a field it cannot return, are excluded and reported as capability boundaries.
2. **Writer:** reads the method notes, the domain package and two worked examples. It writes `scenario.json`:
   - request;
   - seed operations;
   - target;
   - the conditions of the request, each mapped to its facts;
   - reference query;
   - decoys with fact, family, mutation and explanation;
   - effect locator;
   - write call;
   - probe calls.
3. **Checks** (code). Failures go back to the writer, up to 4 rounds:
   - format;
   - the seed expands and its references resolve;
   - `fdc.check_reference`: the reference selects exactly the target, and every claim is killed by its witness;
   - every primary fact has a decoy;
   - anchors survive in every derived probe;
   - replica-profile rules;
   - request lint (no ids, no fact names, no escape clause).
4. **Replica pre-checks** (code). Failures go back to the writer:
   - install the seed and run the probe calls;
   - **observability:** every decoy's deciding value appears in a recorded response;
   - **write feasibility:** the scenario's write, applied to the target in a throwaway environment, succeeds and
     changes the target in the effect table.
5. **Reader**, two turns in one session:
   - request only: its own reading, and any phrase that can be read two ways;
   - then the seed and the writer's condition list: the records that match, and the conditions each other record
     of the target's kind fails.

   Code accepts the scenario when:
   - the reader's matches equal the target;
   - every decoy fails exactly the conditions mapped to its fact.

   Disagreements go back to the writer, up to 2 rounds.
6. **Suite** (code, decisions D6 and D7):
   - one probe per decoy (the decoy alone, no target, "If there isn't one, just tell me.");
   - one fact probe per fact with two or more decoys;
   - one target-present test: the plain cover, which set answers keep too. Hidden-target layouts are not generated
     in this version (see Scope).
7. **Solver runs:** Qwen `qwen3.8:27b`, 3 trials, with the settings, limiter and retry rule of fact_coverage_02
   ([run.py](../fact_coverage_02/run.py)).
8. **Judging:**
   - code triage with `score.classify`;
   - the judge on every trial that is not mechanically clean;
   - a random sample of clean trials.

   The scoring rules are fact_coverage_02's: a trial exposes a fact when it acts on that fact's decoy or presents it
   as the match. An artifact is not established.

## Evaluation, fixed now

**E1. The judge against the manual labels.**
- **Dev split, used for prompt changes:** the labels of runs `b1`, `method_pilot` and `method_pilot_panel` (130).
- **Test split, held out and run once with the frozen judge:** `method_new`, `method_new_lin25`, `method_new_slk21`,
  `factprobe`, `factprobe_extra`, `wording_check` and `hidden_pilot` (137). It also includes 40 clean trials sampled
  from the same runs with seed 7; the manual process accepted these without a label.
- **Metrics:**
  - outcome agreement on collapsed classes: fail, pass, false absence, not established or artifact, incomplete;
  - exposed-fact agreement on failures;
  - artifact recall and precision;
  - mechanism agreement where a manual tag exists;
  - the distinct facts each run set exposes under judge labels vs manual labels.
- **Bar:** at least 90% outcome agreement and 90% exposed-fact agreement on the test split. The same distinct-fact
  set is the target.

**E2. Generation.** Prompts are frozen after the dev round, and each main brief is then generated once.

| Set | Briefs | Use |
|---|---|---|
| Dev | 4, one per domain, from untested facts | Prompt and scaffolding iteration; reported but not counted |
| Arm R (reproduction) | the 18 fact_coverage_02 new scenarios' fact sets (BOX-21..24, CAL-21..24, LIN-21..26, SLK-21..24) | Compare with my scenarios on the same facts; the writer never sees them |
| Arm P (prospective) | 16 briefs from facts no exemplar tested: Linear 7, Slack 5, Box 2, Calendar 2 | Generalization |

The worked examples come from the pilot (fact_coverage_01), whose facts do not overlap Arm R except
`A:File.extension`.

**Reported, per arm:**
- **Acceptance:** briefs to accepted scenarios, check and reader rounds, and the reason for each rejection;
- **Manual validity:** my verdict per accepted scenario and per test (valid, contestable or invalid, with a
  reason), against the exemplars. Of fact_coverage_02's 21 new scenarios (the 18 plus the 3 hidden-target ones), 2
  had to be fixed after running, 1 decoy is contestable, and 1 test is invalid;
- **Runtime validity:** trials judged artifact or not established;
- **Yield:** distinct facts exposed per test, detect@1 and detect@3, by family;
- **Reproduction** (Arm R, fact by fact): the exemplars exposed 13 of these 36 facts (12 uncontested). I report
  which of them the automated suite exposes, and the facts it exposes that the exemplars did not;
- **Request size** against decision D9: conditions, facts tested, decoys;
- **Tokens:** per accepted scenario and per judged trial.

**The bar**, against the exemplars on comparable facts:
- manual validity at least theirs;
- yield per test within their range (about 0.2 facts per test at 3 trials).

**Overfitting check.** The prompts are generic and hold no fact- or scenario-specific hint. For the Arm R facts, I
compare the families and substitutes the writer chose against mine, as a check, not a gate.

## Scope and limits, fixed now
- **No hidden-target generation in this version.** Hidden layouts were scarce in these replicas (Box and one Calendar
  layout). If time allows after the main runs, a later amendment may add them.
- **No policy panel and no presupposing twins** (D3, D4). They are per domain, not per fact, and derived by code.
- **No packed plain tests** (§11).
- **Written values** are checked only where the scorer already does (the Linear priority scale).
- **Budget:** none. The user asked for token telemetry only.

## Amendment 1 (2026-09-25, after the dev split, before the test split)

**The judge is frozen.** Two rounds on the dev split:
- **Round 1** ([runs/judge_dev_01](runs/judge_dev_01)): 128/150 collapsed agreement.
- **Round 2** ([runs/judge_dev_02](runs/judge_dev_02)): 144/150 collapsed agreement, and 87/87 exposed-fact
  agreement on shared failures.

**What changed between the rounds.** The judge instructions now state five scoring rules of the method that version 1
left implicit:
- the policy panel's scoring;
- ignored filters count as artifacts;
- a rejected write on the target is correct grounding;
- a clarifying question in a no-target test is a correct "none";
- a record that is not a declared decoy is attributed by the condition it fails.

The policy-panel mapping to `policy:presupposed` or `policy:underspecified` is applied in code, not by the judge.

**Not pre-registered:** the dev run also judged 20 clean trials (seed 7).

**Dev disagreements that remain:**
- **Label older than the replica finding (3).** P-LIN-10 used the `parent` filter, which the replica ignores; this
  was found after those labels were written. The judge calls these artifacts.
- **Judgment calls (3).** In CAL-05-TOLD twice, Qwen noted the mismatch and deleted anyway. P-CAL-03-I12 had a
  "defensible reading" label.

## Amendment 2 (2026-09-26, before any main brief ran): what changed during dev, and the freeze

**E1, stated as pre-registered.** On the held-out test split ([runs/judge_test_01](runs/judge_test_01)):
- **Collapsed outcome agreement is 142/177 (80%). The 90% bar is missed.**
- **Exposed-fact agreement on shared failures is 64/64.**

The 35 disagreements break down as follows:
- **33 are trials of three tests that the manual review invalidated as whole tests.** SLK-21 v1 (21 trials) asked for
  a reaction the replica rejects. LIN-25 v1 (6) used non-UUID label ids. BOX-31 (6) has ambiguous wording. The
  judge scores grounding trial by trial, so it cannot see a test-level decision.
- **On the other 141 trials, agreement is 139/141 (98.6%).** Both remaining disagreements are judgment calls.
- **The judge caught all 3 trial-level artifacts** (LIN-26's ignored `subscribers` filter). This is optimistic:
  `replica.md` was drafted from report §9, which came out of the manual review of these same runs.
- **In the automated pipeline these three defects are caught before any run.** The replica rules reject unlisted
  reactions and non-UUID label ids, and the reader blocks BOX-31 (below).

**Dev generation** ([runs/gen_dev_01](runs/gen_dev_01), [runs/gen_dev_02](runs/gen_dev_02)):
- **Round 1 accepted 2 of 4.**
  - The reader treated loose readings of intended near misses as ambiguities. That made writers drop their best F1
    decoys, and in one case add a test-only hint ("simply").
  - A default query key broke Slack users.
- **Round 2 accepted 4 of 4, in 1 or 2 versions each.** Before it:
  - reader protocol v2: an ambiguity counts only if a careful reader would be unsure, and "contestable" is a
    non-blocking flag kept on the decoy, like the exemplars' asterisk;
  - the key fix.

**Reader calibration on the exemplars** ([runs/reader_calibration_01](runs/reader_calibration_01)). The 18 new
scenarios and 4 hidden-target tests were read with the reader's own conditions:
- 18 of 20 valid exemplars pass;
- BOX-23 and CAL-24 are blocked (false blocks; CAL-24's "located in Tokyo" is arguably debatable);
- H-BOX-31, the known-invalid test, is blocked for "about travel costs";
- BOX-22's "Pricing sheet 2025.xlsx", the known-contestable decoy, is flagged contestable.

**Changed after round 2, so the frozen set has not run as a whole on dev:**
- `format.md`: the Slack primary keys;
- `method.md`: when to label a decoy F7;
- the reader feedback: a writer may keep wording it judges clear and must say why; a fresh reader reads it again;
  no test-only hints;
- the derivation, from the end-to-end dev solver run ([runs/solve_dev_01](runs/solve_dev_01)):
  - removing a Slack user left its workspace memberships, so the probes did not install;
  - derived tests are now pruned by the replica's own foreign keys;
  - every derived test is checked for dangling keys.

**Frozen from this commit:** `kit/prompts`, `kit/docs`, `kit/examples` and `inputs/`. Arm R and Arm P run once on
this version.
