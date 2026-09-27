# Plan (draft): how to automate fact-discrimination tests

**Status: a draft for review, 2026-09-26. It is not yet pre-registered.** It becomes the pre-registered plan once
the decisions at the end are settled. After that, changes go in dated amendments, as in
[autogen_01](../autogen_01/plan.md).

## Question

autogen_01 asked *whether* Claude Code Sonnet agents, inside fixed scaffolding, can generate and judge
fact-discrimination tests at the exemplars' standard. The answer was "not yet" ([report](../autogen_01/report.md)):
- validity was about equal to the exemplars';
- yield was below them;
- the judge missed its outcome bar, and caught none of the replica artifacts its profile does not describe.

This study asks **how**:
- which components of the pipeline are needed to reach the standard;
- what each one contributes to validity, to yield and to cost;
- which manual inputs remain, and why they resist automation.

**The deliverable is a recipe table.** Its columns are fixed now:

| Component | Stage | Automated or manual | Effect on valid decoys (paired) | Effect on probe failure rate (paired) | Cost | Evidence | Verdict |
|---|---|---|---|---|---|---|---|

The verdict is keep, drop or optional. The table comes with a list of the manual steps that remain, and what each
would take to automate.

## What autogen_01 leaves

**The baseline (M0)** is the autogen_01 kit with method v2 and its post-run fixes:
- the reader renders full records;
- every derived test is re-checked;
- replacement values get an observability check.

**Data for calibration.** I labelled all of it, so it can calibrate components but cannot validate them.
- **About 364 single-decoy probes with Qwen outcomes,** 3 trials each (6 for the 58 exemplar probes run twice):
  - fact_coverage_02's probes on the pilot facts (121) and on the new facts (58);
  - autogen_01's three arms (185).
- **Decoy validity labels:** 185 verdicts in 49 generated scenarios
  ([validity.json](../autogen_01/eval/validity.json)), 13 of them contestable or invalid, and the exemplars' known
  problems.
- **Verdict labels:** 167 adjudicated verdicts on the generated runs
  ([judge_review.json](../autogen_01/eval/judge_review.json)), and fact_coverage_02's 267 manual labels.
- **A list of replica gaps:**
  - those in the profiles;
  - the three that autogen_01 found;
  - the failing nested Linear connections ([check_nested.py](../autogen_01/kit/check_nested.py)).

**Two noise estimates.** A probe's failure rate is its failing trials over its established trials.
- **Run to run:** the same 58 exemplar probes, run on two days (3 trials each). The SD of the per-probe difference is
  0.26.
- **Generation to generation:** two generations (v1, v2) of the same 16 Arm P briefs, over 42 facts. The SD of the
  per-fact difference is 0.43.

Most of the variance between two suites is therefore the scenario design, not the solver. That shapes the design
below.

## Design principles, fixed now

1. **Hold fixed whatever can be held fixed.**
   - What makes a decoy tempting is answered within a scenario: two probes that differ only in the factor under test
     (Phase 1a).
   - Which generation mechanism works is answered within a brief: every mechanism generates the same briefs, and
     comparisons are paired by fact (Phase 1b).
2. **A continuous primary endpoint:** the probe failure rate over 5 fresh trials. detect@3 and facts per test stay
   as secondary endpoints, for comparison with the exemplars.
3. **Offline first.** A component goes online only if its signal clears a bar fixed now, on data we already have
   (Phase 0).
4. **Held-out evaluation.** No trial used to select or repair a test counts in that test's evaluation. Every arm that
   uses a solver during generation is evaluated on fresh Qwen trials, and on a transfer solver it never saw.
5. **Blind manual review.** I review the pre-registered samples of scenarios and trials before seeing any agent's
   output. The review can then test the automated reviewers, which autogen_01's review, made while reading the
   judge's verdicts, could not.
6. **The same accounting as autogen_01.** Work done by Sonnet or Opus inside the pipeline is automated; mine is
   manual. Every call's usage is logged.
7. **A new folder with new frozen inputs.** autogen_01 stays untouched. Completing the replica profiles is a
   decision (at the end), not a silent fix.

## Phase 0: offline, on existing data

Phase 0 runs no solver, except the smoke test in 0.6. Each component has a bar. A component that misses its bar
does not go online, and that is itself a recipe finding.

**0.1 A temptation predictor.** Can we tell in advance which decoys Qwen takes?
- **Mechanical features,** computed from each case and the replica:
  - whether the substitute sits in a field a listing or search shows (a name, title or login), or only in a detail
    field;
  - whether the decoy's value contains the requested value (a superstring), or the reverse;
  - natural-query visibility: whether the decoy comes back from the query a solver would run first for the
    requested value (a search, or a filter on it), executed on the replica;
  - the request's length and number of conditions, and the family.
- **A rater** (Sonnet, no tools): given the request and the records, how likely is an agent that skips one check to
  take each decoy?
- **Data:** the ~364 probes, split by scenario. fact_coverage_02 and Arm R are for development; Arm P and v2 are for
  the test.
- **Bar:** on the test half, AUC ≥ 0.70 for "failed in at least one trial", by either predictor.

**0.2 Discovering replica gaps.** Can the gaps be found without a person?
- **A schema-driven prober** (code). For each filter and nested connection the API offers:
  - install a minimal seed;
  - run the query;
  - check the response against the seed.

  The API surface comes from introspection for Linear, the method list for Slack, and the documented routes for Box
  and Calendar.
- **A trial-side detector** (code). When a solver's query carried a filter and the response itself shows records
  that violate it, the step is flagged as a candidate artifact.
- **Bar:** the prober finds at least 80% of the known list. I check every new flag in the replica code, and at least
  half must be real.

**0.3 Observability through the actor's own reads.** For each decoy, read its deciding field the way the actor
would, with the actor's permissions, and compare the result with the seed.
- **Bar:** it flags both known cases, AR-SLK-23's group DM and AP-CAL-02's sharing rules, with at most one false
  flag in the 49 scenarios.

**0.4 An automated validity reviewer.** Can the second validity pass be automated?
- **Input:** a fresh reviewer (no tools) gets the scenario, every record in full, and the replica profile.
- **Output, per decoy:** valid, contestable or invalid, with a reason.
- **Output, per scenario:** contrived wording, or a domain-semantics error.
- **Models:** Sonnet and Opus, with the same prompt, to see whether capacity matters here.
- **Data:** the 49 reviewed scenarios, and the exemplars' known problems (BOX-22's contestable decoy, BOX-31's
  wording).
- **Bar:** recall ≥ 0.70 of contestable or invalid decoys, at precision ≥ 0.50.

**0.5 Judge v2.** Three changes:
- a decoy-validity flag and a test-validity flag next to the outcome;
- the trial-side filter-violation flags from 0.2, in its bundle;
- the completed replica profile.

It is developed on fact_coverage_02's dev split and autogen_01's reviewed verdicts. Both have been inspected, so they
serve for development only. Its test is the blind review of Phase 2; there is no clean test set before that.

**0.6 A solver smoke test.** Purdue serves other families besides Qwen, among them gpt-oss 20B and 120B, gemma3 27B,
llama3.3 70B and qwen3 14B. Each candidate runs 20 exemplar covers, 1 trial each.
- **The proxy solver** is used during generation, by M3. It should differ from Qwen and be cheap to run.
- **The transfer solver** is used only for evaluation. It should be a third, strong model.
- **Both must complete** at least 16 of the 20 covers correctly, in the same harness.

**Gate 0 to 1.** The arms of Phase 1b are those whose components cleared their bars. The result is recorded as an
amendment before any Phase 1 generation.

## Phase 1a: what makes a decoy tempting (a controlled experiment)

Method v2 assumed the autopsy's explanation (salience) without testing it, and then did not raise yield. Here the
explanation is tested directly, with the scenario held fixed.

**Pairs.** Two variants of one decoy in a valid scenario from autogen_01 or the exemplars, differing in one factor:
- **Field:** the substitute in a listed field (a name, title or login) vs in a detail field (a description, comment
  or location).
- **Direction:** a partial identity that contains the requested value vs one that the requested value contains, or
  merely resembles.
- **Request length:** the terse request vs the same request plus qualifiers that are true of every candidate.

**Construction.** The writer makes each variant under a specific instruction. The code checks each variant (fdc,
observability, derived tests), and checks that the two seeds differ only in the manipulated fields.

**Size and power.**
- 30 pairs per factor: 90 pairs, 180 probes, 5 trials each, 900 trials.
- With the run-to-run noise above, 30 pairs detect a difference of about 0.09 in failure rate (80% power, α = 0.10,
  two-sided).

The result tells Phase 1b which constraints are worth enforcing in code, whatever the generation mechanism.

## Phase 1b: generation mechanisms

**Briefs.** 32 briefs with about 90 facts:
- **the 16 Arm P briefs** (45 facts). Their two earlier generations feed the noise model only, not the arms.
- **16 fresh briefs,** from catalog facts that no study has tested, drawn by rule.
  - Facts whose deciding field lies on a known gap are excluded.
  - Slack has only 8 unused facts, so the fresh briefs lean to Linear, Box and Calendar.

The 18 Arm R briefs serve only for the comparison with the exemplars (Phase 2), because their facts shaped
method v2.

**Arms.** Each arm generates every brief once. Every arm uses the actor-read observability check (0.3) if it cleared
its bar, and the kit fixes.

| Arm | What it adds to M0 | What it tests |
|---|---|---|
| M0 | nothing (the autogen_01 kit, method v2) | the baseline |
| M1 | constraints enforced in code, chosen from Phase 1a and 0.1. Examples: a cap on request length; a natural-query visibility pre-check for name-like decoys | whether code succeeds where the prompt failed |
| M2 | M1, plus over-generate and select: the writer proposes 3 candidates per fact, and the predictor of 0.1 picks | a selection signal without a solver |
| M3 | M1, plus a solver in the loop: each probe runs twice on the proxy solver, and decoys it never takes go back to the writer, for up to 2 rounds | adaptive generation |
| M4 | M1, with an Opus writer | model capacity against scaffolding (diagnostic) |
| M5 (optional) | the inputs of one domain, drafted by an agent | irreducible manual input |

- **M4 is the cheapest informative arm.** If an Opus writer with the same scaffolding closes the gap, the "how" is
  capacity. If it does not, the "how" is scaffolding.
- **M5 measures how much of the manual domain input can be generated.**
  - A Sonnet agent drafts the `facts.json` substitutes, `replica.md` and the seed vocabulary for one domain. It works
    from the domain model and the replica code, without seeing mine.
  - The draft is scored against mine: entries found, and errors.
  - M1 then generates that domain's briefs on the drafted inputs.
- **Replicate generation.** 8 briefs are generated twice under M0 and under M1. This separates generation variance
  from the mechanism's effect.

## Phase 2: evaluation

**Runs:**
- every arm's probes on Qwen, 5 fresh trials each; covers at 3 trials, for M0 and the best arm;
- M0's probes a second time (a replicate run);
- the probes of M0, M1 and M3 on the transfer solver, 3 trials each;
- **the standard:** on the 18 Arm R briefs, the best arm's probes against the exemplars' 58 probes, both run on the
  same day, 5 trials.

**Judging.** Judge v1 (frozen) and judge v2 both judge every trial that is not mechanically clean, plus the same 20%
sample of the clean ones.

**Blind manual review.** This is the test set for everything automated.
- **Scenarios:** all of M0's and the best arm's, and a random quarter of the rest. I review them before I see the
  validity reviewer's output.
- **Trials:** every failing or void trial of M0 and the best arm, and 60 random clean trials. I review them from the
  evidence before I see any verdict.

## Evaluation, fixed now

**Primary endpoints:**
- **Yield (Phase 1b):** the per-fact difference in mean probe failure rate, each arm against M0, over the 32 briefs,
  with a 90% bootstrap interval over briefs.
- **Yield factors (Phase 1a):** the per-pair difference in failure rate for each factor, with a 90% bootstrap
  interval over pairs.
- **Validity:** the valid-decoy rate in the blind review, per arm.

**Secondary endpoints:**
- detect@3 and facts per test;
- acceptance and repair rounds;
- cost per accepted scenario and per exposed fact;
- transfer: each arm's failure rates on the transfer solver. This also tests whether a decoy that tempts one model
  tempts another.
- the automated reviewers against the blind review:
  - judge v1 and v2: outcome, exposed facts, artifacts, test-level calls;
  - the validity reviewer: recall and precision.

**Decision rules:**
- **A mechanism enters the recipe** if its interval excludes zero and its valid-decoy rate is at most 5 points below
  M0's. An arm that uses a solver during generation must also improve on the transfer solver. If it does not, it
  enters only as "tuned to one solver".
- **The standard is met** if the recipe, on the Arm R briefs, reaches the exemplars' same-day failure rate within
  the replicate-run noise, with validity at least theirs.
- **Judge v2 passes** at ≥ 90% outcome agreement with the blind review, test-level calls included, and ≥ 90% on
  exposed facts.
- **The validity reviewer replaces my review** if it clears the bar of 0.4 again on the blind review.

**Power, stated plainly.**
- **Phase 1b:** between two generations of the same briefs, the per-fact SD of the difference was 0.43. With about
  90 facts, Phase 1b detects a difference of about 0.11 in mean failure rate (80% power, α = 0.10, two-sided). The
  baseline rate is 0.13 to 0.24, so only large effects are detectable, roughly a doubling. The replicate generations
  will refine this estimate.
- **Phase 1a,** with the scenario held fixed, detects about 0.09 per factor with 30 pairs.

## Budget

**Purdue.** At the limit of about 20 requests a minute, Qwen runs about 200 trials an hour. Proxy and transfer runs
share the key's limit.

| Part | Trials | Hours |
|---|---:|---:|
| Solver smoke test (0.6) | about 100 | 0.5 |
| Phase 1a pairs | 900 | 4.5 |
| M3's loop, on the proxy solver | about 500 | 2.5 |
| Five arms' probes (5 trials), and two arms' covers (3 trials) | about 3,400 | 17 |
| Replicate run of M0 | about 640 | 3 |
| Transfer solver, three arms | about 1,150 | 6 |
| The standard (Arm R) | about 620 | 3 |
| **Full plan** | **about 7,300** | **about 37** |
| **Lean plan:** three arms, a replicate run on half the probes, transfer on one arm | **about 4,900** | **about 25** |

**Sonnet and Opus,** at list price, billed to the subscription:
- about $15 to $30 for Phase 0;
- about $100 for the Phase 1a variants;
- about $100 to $150 per Sonnet arm in Phase 1b, and several times that for the Opus arm;
- about $70 of judging, with two judges.

That comes to roughly $800 to $1,300 in all. The Opus arm is the largest item.

**Timeline.** Phase 0 is about a day, mostly offline. Phase 1a and Phase 1b's generation can overlap. The solver runs
take two or three nights at the rate limit.

## Risks

- **A solver in the loop tunes the tests to that solver.** The proxy is not Qwen, and the evaluation uses fresh
  trials plus a transfer solver.
- **The candidate solvers may not operate the harness.** The smoke test decides; without a working proxy, M3 is
  dropped.
- **Purdue's instability** (unterminated streams, rate-limit errors, hangs). The proxy and the runner's retries
  handle these, as in autogen_01.
- **The subscription's session limit.** Every agent step can resume, and the verdict cache avoids judging twice.
- **My labels as ground truth.** The blind review, and the user's sample (decision 5), address this.
- **Too few fresh facts in Slack.** The fresh briefs lean to the other domains, and per-domain results are reported
  with their denominators.

## Decisions for the user

1. **A solver in the loop (M3): is it acceptable?** It tunes the tests to a solver. The plan uses a different model
   as the proxy, and evaluates on Qwen and on a transfer solver.
2. **Purdue hours: the full plan (about 37) or the lean plan (about 25)?** If Purdue's limit applies per model rather
   than per key, the proxy and transfer runs could overlap with Qwen's. That is a question for Purdue, not something
   to test.
3. **The Opus writer arm (M4): include it?** It is diagnostic, and the largest cost item.
4. **Agent-drafted domain inputs (M5): in this study, or in a later one?**
5. **An independent check of my labels.** Would you review a random sample of about 20 decoys and 20 trials (about an
   hour), blind to my verdicts? That would measure how far my labels can serve as ground truth.
6. **The replica profiles.** Should they be completed with the discovered gaps for every arm, keeping the old
   profile only for the judge comparison? I recommend it: it is what a user of the kit would do.
