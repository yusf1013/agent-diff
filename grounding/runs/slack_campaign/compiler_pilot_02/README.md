# W02–W10 compilation and execution pilot

The user authorized retaining the existing writer outputs and attempting the full
compiler → review → native preflight → solver → evaluator pipeline. W01's earlier
result stays in [compiler_pilot_01](../compiler_pilot_01/execution_review.md).
The source is the final reflected sketch for each case in writer_pilot_04.

Nine workflows run concurrently after W02 warms the compiler/reviewer prefixes.
Each workflow makes model calls sequentially, keeping simultaneous calls at nine
or fewer. The compiler has at most three turns, with native conversational repairs.
The evaluator has its existing single mechanical-validation repair. Solvers are
not repeated for a better outcome. Quality issues do not independently block a
valid test; source/selector conflicts and failed validity/preflight checks stop the
case. No access-review model is called. Failed cases and costs remain recorded.

The W01 annotation definitions are already in the shared compiler contract. No
case-specific manual diagnoses or expected solver verdicts enter model prompts.
Manual audits live separately under `manual_reviews/` and are never model inputs.
Compilation/review status is not itself a manual validity judgment.

For evaluator comparisons, **positive means a grounding failure was detected**.
A manually confirmed failure flagged by the evaluator is a true positive; a flag
without a failure is a false positive; an unflagged actual failure is a false
negative; correct behavior accepted by the evaluator is a true negative. Missing
or unresolved assessments are reported separately, not silently treated as passes.
Invalid or unresolved test constructions are excluded from these classifications.
Other task errors remain visible separately from grounding errors.

The [first-pass batch summary](batch_summary.json) records the original outcomes.
Recorded development continuations have separate `continuation_statuses/` files;
the latest combined snapshot is [progress.json](progress.json). The
[plan](plan.json) fixes source hashes and limits. `usage_summary.json` and
`usage_ledger.json` update as cases finish; individual invocations record usage
immediately. A current total may omit solver turns still in flight; it is not a
final bill. Dollar conversions use recorded historical rates, not native invoices.

Launch command (already started; do not repeat into this directory):

```sh
python -m grounding.slack_campaign.concept_batch \
  --folder experiments/slack_campaign/compiler_pilot_02 --run --concurrency 9
```

The local backend serves port 18000 against the existing campaign PostgreSQL on
15432. Backend and batch processes were detached so subsequent cases can continue
while W02 is discussed. Runtime logs/process IDs for this session are under
`/tmp/ad-concept-batch-02*`. The runtime cleans each case's owned templates/clones.
No prior writer, compiler, solver or assessment output is overwritten.

## Development corrections during this pilot

W02 revealed an overstrict route-length check. Preserving the full assigned route
does not forbid an extra join needed for a condition already in the story. The
checker was corrected, with tests for allowed extensions and forbidden truncation;
W02's original compiled seed and selector were rechecked unchanged. The erroneous
rejection and its paid follow-ups remain recorded. [W02's independent review](manual_reviews/W02.md)
includes the completed solver/evaluator comparison and trajectory summary.

The compiler also initially rejected W03/W07's intended ambiguity as a design
conflict. Shared instructions now explicitly explain the assigned modes. Those
cases receive the same [generic clarification](mode_clarification.txt) as a native
continuation, without changing the source sketches or giving desired solver
verdicts. `concept_continue.py` records these development interventions separately
and keeps the total compiler-turn limit at three. These fixes are not retroactively
treated as automatic first-pass success. Other compilation, reviewer and preflight
failures remain preserved for case-by-case discussion.

## Current outcome

The launched attempts and recorded continuations have finished. W02, W03 and W07
reached solver and evaluator completion; only W02 has had its independent run
review so far. W04/W08 exhausted a reviewer output limit; W05 exhausted the compiler
output limit; W06 stopped at native preflight; W09's reviewer call returned a read
timeout without usage; W10 stopped at construction checks. These are pipeline
outcomes, not solver failures. They remain available for the subsequent individual
reviews and any explicitly recorded repair. No failed construction is counted as a
grounding false negative or silently removed from the attempt count.

Current native-usage estimate: **$3.30317 for calls with known usage**, including
all recorded development continuations. W09's timed-out review has unknown usage
and is not assumed free. The completed W02 subset cost **$0.64780**, including the
checker-induced compiler follow-ups. The owned HTTP backend has been stopped;
the existing PostgreSQL container remains available. See [cleanup record](runtime_cleanup.json).
