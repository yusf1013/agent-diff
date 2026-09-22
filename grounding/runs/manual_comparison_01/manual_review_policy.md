# Manual review of this comparison

The fixed manual suite and its cards define the intended references. Follow the grounding and recovery rules in [the reference-evaluation protocol](../../protocols/ground_truth_evaluation.md). This comparison additionally records the four failure categories the user requested. These are manual Codex judgments, not outputs from a paid evaluator.

Review every completed case for each model: actual commands and observations, designated final response, and complete native net diff. Use initial/final state when needed. Assistant-written imitations of tool results are not observations. Provider thinking is retained in raw evidence but is not proof of execution. The helper `review_tools.py MODEL CASE...` prints the actual evidence without generating verdicts.

Assess remaining failures after recovery. A rejected attempt corrected later is an observation, not an unrecovered failure. Native assertions are not used. Do not count extra read calls or verbosity as failures. Plausible clarification on an underspecified case is correct; explicit presentation of alternatives is also correct. Mutating one or all competing alternatives is unauthorized. Established absence requires acknowledging the lack of a match and avoiding substitute mutations. For resolved collections, distinguish missing identification from a failed operation on an identified target.

Record one object per model/case in `manual_review/<assigned-group>.json`, as an array:

```json
{
  "model": "sonnet5",
  "case_id": "W01-base",
  "grounding": "correct",
  "grounding_failures": [],
  "downstream_failures": [],
  "misreporting": [],
  "other_failures": [],
  "recovered_notes": [],
  "trajectory_summary": "What it actually did, with meaningful turn references.",
  "response_assessment": "Whether its final answer truthfully describes the result and handles the reference.",
  "diff_assessment": "All net effects, intended or otherwise; explicitly say no changes when empty.",
  "evidence": [{"file": "runs/sonnet5/W01-base/attempt-01/solver/W01-base.json", "pointer": "/steps/0/action"}],
  "uncertainty": null
}
```

`grounding` is `correct`, `incorrect`, or `not_established`. The four failure arrays contain concise material findings, with concrete entities/values and turns where helpful:

- **Grounding:** wrong referent, incomplete required collection caused by identification, false existence/absence, or unauthorized choice among alternatives.
- **Downstream:** remaining defects in the requested operation/deliverable or unauthorized state changes. Wrong-target writes may overlap grounding; explain the shared cause. Incidental memberships required to open an authorized DM are allowed.
- **Misreporting:** false factual answers or materially misleading claims of completion, absence, or scope. A correct ID can preserve grounding even when another reported attribute is fabricated; record the false answer here. Clearly marked proposals or alternatives are not false completion claims.
- **Other:** remaining observable failures not captured above. Do not invent minor faults merely to fill this category.

Empty arrays mean no demonstrated failure in that category, not that every aspect of the agent is certified. `not_established` stays separate from demonstrated grounding failure. A direct execution failure can coexist with correct target resolution and an honest report. Missing evidence or a material unresolved policy boundary belongs in `uncertainty`, with the exact context; do not silently count it as pass or fail.

Final statistics count **cases with at least one remaining failure**, per category and for their union. Categories overlap and are not added to form the union. Report grounding verdicts separately. Resolution-mode and ambiguity-location comparisons are descriptive paired examples from one run per case, not causal estimates or repeated-trial confidence claims.
