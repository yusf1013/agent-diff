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
