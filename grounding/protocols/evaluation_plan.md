Below is a summary of chat with a coding agent. Here "you" refers to me, the user, as the coding agent was conversing with me.

**The evaluation has four goals: establish the baseline’s coverage gaps, show that those gaps matter, measure what generation adds, and validate your evaluator.** The primary failure measure is **confirmed grounding violations**. General downstream correctness checking remains outside this round.

| Goal                             | Main question                                                                                | Main results                                                                           |
| -------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| **G1: Baseline audit**           | What grounding requirements does the baseline exercise and check?                            | Grounding prevalence, native-oracle coverage, domain coverage                          |
| **G2: Consequences of the gaps** | Do existing oracles miss grounding failures, and do variations expose additional failures?   | Confirmed native-oracle false passes; original-correct → variant-incorrect transitions |
| **G3: Generation contribution**  | How much coverage and failure discovery does the campaign add?                               | Valid generation yield, coverage gains, confirmed failing runs                         |
| **G4: Evaluator reliability**    | Does your assessment method detect grounding failures reliably compared with a direct judge? | Precision, recall, false positives, false negatives, unresolved assessments            |

**The infrastructure you are implementing**

From each test, you extract grounding cards, structured task specifications, and links between them. Given a completed run, your evaluator produces:

* Grounding verdicts: `demonstrated_correct`, `demonstrated_incorrect`, `not_established`.
* Action applicability: active or inactive, including mixed batch portions.
* Execution status: `performed`, `partially_performed`, `execution_failed`, `deferred`, `skipped`, `omitted`, or `interrupted`.
* Supporting observations and evidence.

Only the grounding verdict directly supplies a failure judgment at this stage. Applicability and execution statuses support interpretation and descriptive analysis.

**G1 — Audit the existing baseline suite**

Report:

* Number and percentage of tasks containing grounding obligations.
* Number of grounding obligations.
* Obligations fully, partly, or not checked by native oracles.
* Distribution across resolution modes.
* Baseline coverage of your declared domain coverage space.

The coverage space is:

> **Referent entity × focal identifying attribute/path × resolution mode**

The modes are absent, single, multiple, and underspecified. Define meaningful, feasible identifying paths from the domain model before measuring coverage.

Your existing collaborative audit supplies this evidence, with a documented verification pass. Claims remain scoped to the audited suites. Broader relevance can be motivated by existing evidence about real assistant use; the benchmark audit alone does not establish real-world prevalence.

**G2 — Show observable consequences**

There are two experiments.

| Experiment                      | Procedure                                                                                                                                  | Report                                                                                                     |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------- |
| **Existing oracle blind spots** | Run the agent on unchanged baseline tests; compare native-oracle results with your evaluator; confirm reported grounding failures manually | Confirmed grounding violations in native-oracle-accepted runs, plus the number of affected runs            |
| **Sensitivity to variations**   | Run original/easy cases and controlled variants; assess both with your evaluator; confirm qualifying transitions                           | Valid pairs, original-correct pairs, correct → incorrect transitions, and distinct original tasks affected |

For transitions, “correct” means **correct grounding for the assessed obligations**, not necessarily perfect downstream task completion.

Environment-only variants preserve the original prompt. Adapted requests can also contribute: compare the same adapted wording in an easy environment and a strengthened environment, and report these separately.

Native-oracle reuse on mutants is optional. G2’s paired comparison does not require it. If reused, its actual assertions must remain valid; unchanged resolution mode alone is insufficient.

Reviewing evaluator flags establishes confirmed discoveries. It does not establish the total number of failures or the evaluator’s recall.

**G3 — One generation campaign, shared with G2**

Choose the coverage requirement first, then select how to realize it.

| Starting point                             | Construction approach                                                                               |
| ------------------------------------------ | --------------------------------------------------------------------------------------------------- |
| Existing single-criterion reference        | Vary resolution modes; enrich the reference and add focal negatives where needed                    |
| Existing compound reference                | Supply a negative that violates the focal criterion while satisfying auxiliary criteria; vary modes |
| Entity/path or other cells still uncovered | Clean generation                                                                                    |

For this round, mutation does not change the referent entity or replace the focal identifying path. Clean generation handles those missing families. Reference enrichment may introduce auxiliary criteria, with the working limit of three criteria total.

Compound generated references include validated near misses as a construction requirement. **There is no planned near-miss-versus-no-near-miss ablation.**

Selection is suite-wide; you need not exhaust every seed. Use a fixed generation budget and planned coverage targets rather than stopping at the first reported bug. A mode is covered only when a valid test realizes it—not merely because generation attempted it.

Report by construction stage:

* Candidates produced and valid tests retained.
* Newly covered cells.
* Existing coverage strengthened through focal negatives.
* Confirmed failing runs and affected source tasks.

Keep unsuccessful generation attempts in the accounting. Distinguish covered, attempted-but-unrealized, unattempted, and documented infeasible cells.

G3 includes gains from both mutation and clean generation. Clean generation fills the remaining gaps.

**G4 — Validate grounding-failure detection**

Select a manageable set of completed runs and manually assess all grounding obligations within them, including automated passes and uncertain judgments.

Compare:

| Method                    | Assessment approach                                                                  |
| ------------------------- | ------------------------------------------------------------------------------------ |
| **Your evaluator**        | Domain-guided cards, task specifications, links, and structured assessment procedure |
| **Direct judge baseline** | Finds reference-handling violations directly from the request, environment, and run  |

Both receive a concise shared definition of grounding violations and accepted behavior: no mandatory lookup sequence, acceptable confirmation, recovery, and separation of reference errors from unrelated answer errors.

The direct judge need not produce your cards or reproduce your obligation inventory. It reports localized violations with evidence; human review matches these against the reviewed violations.

Keep model, evidence access, and execution budget comparable where practical. Disclose whether your additional artifacts were automatically generated or manually curated.

Report:

* Failure-report precision and recall.
* False-positive and false-negative counts.
* Unresolved assessments.
* Your evaluator’s three-way confusion matrix as an additional diagnostic.

This evaluates the complete assessment approach. Component ablations can wait.

**Use the extra labels descriptively**

Examples include:

* Execution-status distributions among active and inactive actions.
* How often inactive portions were nevertheless performed.
* Deferral rates by resolution mode.
* Grounding failures in delivered reports, executed changes, and pending proposals.
* Circumstances associated with `not_established`.

Use separate denominators and portion-level records for mixed batches. These summaries do not certify downstream correctness or require a new bug-conversion policy.

**Keep the first round bounded**

Freeze the implementation and policies, select a manageable campaign, validate generated tests, execute it, and report the results before revising the system.

Across the campaign, confirm reported failures. Within the smaller G4 set, review unflagged cases too. Record uncertainty rather than forcing judgments.

Keep counting units explicit: **tasks, obligations, runs, pairs, and coverage cells**. Report failing runs rather than “distinct bugs” unless you add a deduplication rule. Poor or zero results remain valid results; the objective of this round is a defensible end-to-end measurement.

---

