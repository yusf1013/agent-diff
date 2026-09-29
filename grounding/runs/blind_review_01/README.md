# Additional blind reference review: 200 final OpenClaw executions

Started 2026-09-29 at the PI's request. Reviewer: Codex, with PI adjudication where necessary.
These are independently authored AI reference labels, not labels from a second human annotator.
The reviewer has seen aggregate results and study design in the prior conversation, but must not read the
selected executions' judge verdicts, mechanical classifications or earlier reference labels before locking labels.

## Scope and sampling fixed before labeling

- Population: the final 3,018 executions of the 1,006 methodology cases, as listed in
  [the final manifest](../report_01/numbers/concise.json), `final_execution_keys` only.
- Include both LLM-judged and mechanically scored executions. The PI explicitly selected this scope.
- Exclude executions with previous reference labels. Also exclude AP-BOX-01: its final result was displayed
  while investigating the earlier report. Do not sample by outcome or by whether an LLM verdict exists.
- Stratify by domain (Box, Calendar, Linear, Slack) × form (cover, probe, fact probe, absence, underspecified).
  Allocate 200 proportionally to eligible execution counts, using largest remainders. Sample without replacement
  within strata using seed 2026092902, then shuffle the review order. Different executions of one case may occur;
  report their overlap and account for case clustering when estimating uncertainty.
- Save exact source paths and SHA-256 hashes before reviewing. The draw is immutable; uncertain, missing-evidence
  and artifact cases remain in the sample rather than being replaced.
- New-sample estimates describe the eligible, previously unlabelled execution pool. They are not automatically
  representative of all 3,018 executions after the previous-label exclusions.

## Blind evidence and labels

Use `python grounding/runs/blind_review_01/view.py BR001` from the repository root for an evidence-only view.
It displays the prompt, construction references, seed, solver commands/reasoning/observations, final response and
state diff. Construction targets and decoy claims are hypotheses to check against evidence, not execution labels.
`--brief` omits read responses and abbreviates reasoning; inspect decisive original responses with `--steps`.
Raw evidence is retained at its original source paths and is never executed. Avoid the older `review.py`, which
prints provisional outcomes and would break blinding.

Use the existing [judge-v2 outcome definitions](../autogen_02/kit/prompts/judge_v2.md) and domain replica notes,
with the [reference-labeling protocol](../../protocols/ground_truth_evaluation.md) for evidence and provenance.
The applicable output schema is this study's existing trial-verdict schema, not a new card assessment.
For every sampled execution record an outcome, acted-on IDs, exposed facts, mechanism, artifact reason,
decisive evidence pointers and a concise independent explanation. Record wrong values and side effects separately
from grounding. Time-budget treatment is a separate scoring layer, not an excuse to copy a judge's outcome.

When evidence is ambiguous, record the competing interpretations and ask the PI without showing any judge label.
Retain the initial label and any PI adjudication separately. Do not call unresolved cases finalized to reach 200.
Once all 200 are resolved, validate the labels and evidence pointers and write a SHA-256 lock before unblinding.
After unblinding, preserve initial labels and record subsequent corrections separately.

## Planned comparison

Report exact outcome agreement; failure/nonfailure agreement and confusion counts; false positives and false
negatives; void disagreements; and exposed-fact agreement. Keep LLM-verdict agreement separate from pipeline
agreement, including the mechanically scored subset. Report by domain and form and distinguish raw sample
summaries from stratification-weighted estimates. Failure means `incorrect` or `presented`; `false_absence` and
`incomplete` are separate outcomes, not automatically successful task completion. Report budget-adjusted agent
failure separately. Missing LLM verdicts must not be treated as missing pipeline scores or invented LLM outputs.

## Existing human-validated bugs

The PI reports manually validating the [16-bug Qwen pilot review](../fact_coverage_01/bugs.md). It counts distinct
violated catalog requirements in earlier pilot executions, not 16 final OpenClaw execution labels. Its source
execution paths belong to another study and do not overlap the final manifest. Keep this historical validation
separate from the new sample. The review notes that two requirements share one run/cause and one error was
reverted with a lasting side effect; it is useful context, not a substitute for reading a new execution.

No report files or historical evidence are edited by this review. No solver or paid judge calls are required.

## Pre-unblinding clarification and reproducibility

All 200 initial records are in `labels.jsonl`. `human_adjudications.jsonl` retains the PI's replies and their
application separately; `review_revisions.jsonl`, if present, retains pre-lock reviewer corrections. The effective
reference applies those amendments without overwriting the initial records. PI-elected uncertainty remains in the
draw and is excluded from agreement denominators; it does not block finalization or cause a replacement draw.
Open questions in `pending_adjudications.json` do block finalization. `finalize.py` validates the evidence, applies
the amendments, and creates `effective_labels.json` plus `labels.sha256` before any score comparison.

The PI allows descendants for ordinary folder-containment wording and accepts the unquoted shortened name
Seaport Archive for Seaport Archive 2024 when the other conditions match. A supplied construction's exact-name
predicate does not override that semantic decision. PI rules also require the cycle's number for Cycle 4, evidence
of budget-review intent rather than an unsupported budget-sync substitution, and clarification among the three
matching pricing-table tasks despite only one having a due date. The Slack decision is conditional on a real
structured-card distinction: [Block Kit](https://docs.slack.dev/block-kit/) documents structured message blocks
(checked 2026-09-29), and the fixtures distinguish section-block cards from plain text. No particular native
card-block type is required. The PI rule is applied by Codex; it is not represented as an unconditional human
inspection of the whole execution.

Comparison will retain three outcome groups: failure (`incorrect`, `presented`), nonfailure (`correct`,
`correct_absent`, `false_absence`, `incomplete`), and void (`artifact`, `not_established`). Nonfailure denotes
absence of an established grounding failure, not successful task completion. Binary agreement uses only rows
where both labels are nonvoid; also report the full three-way matrix so void disagreements cannot disappear.
Exact-outcome and fact-set comparisons include all resolved references with the respective comparison label.
Report fact-set agreement separately among jointly failing executions to avoid inflation by empty sets.

Stratification weights are eligible stratum size divided by sampled stratum size. Weighted estimates target the
2,705 eligible executions, with unresolved references excluded from the applicable weighted denominator. If
intervals are reported, use an explicitly approximate case-cluster bootstrap, retaining all sampled repeats of
one case together. The same 200 draw is used for all comparisons; no outcome-driven substitutions are allowed.
Any interpretation reconsidered after opening scores must be reported separately, never silently substituted
into the locked primary reference. Saved budget adjustments are a separate layer from the judge's raw verdict.
