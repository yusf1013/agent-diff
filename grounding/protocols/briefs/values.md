# Brief: failures beyond fact discrimination (session "values")

Rules for every session: [README.md](README.md). Study folder: `grounding/runs/values_01/`. No solver runs; the
data is on disk. If you want an LLM to classify text, cap it at $5 billed on Muse through the existing client code.

## The question

Beyond choosing the right record, what else goes wrong in the final 3,018 executions: wrong values written, wrong
or false statements in the final reply, unrequested side effects? Which of these can be checked mechanically, with
what precision, and what should a "value layer" beside the grounding verdict look like? The PI's worry: "are we
missing a lot of valuable information that's right in front of us?"

## Materials

- What exists: the concise report's RQ7; `grounding/runs/report_01/kit/beyond.py` and `numbers/beyond.json`
  (literal-value checks: Linear priority and estimate, Box tags, Slack reactions, archive state, Calendar hidden
  state; the classification of additional writes); several_match_auto_01's finding that 31 of 39 passed Linear
  trials wrote the wrong priority (Qwen reads 4 as urgent).
- The executions: `grounding/runs/report_01/numbers/concise.json` → `final_execution_keys`, under
  `grounding/runs/openclaw_eval_01/runs/`. Each attempt has the request (`case.json`), the state diff
  (`environment/diff_run.json`), the transcript and the final reply (`solver/`), and, for 2,139 of them, the Muse
  judge's verdict and notes.
- The blind labels (openclaw_eval_01's and blind_review_01's) record wrong values and side effects separately from
  grounding; use them as a check on your classifiers.

## Steps

1. Define each check precisely before running it: interpreted dates and times (including time zones); free text
   written (titles, names, descriptions, messages: exact, paraphrased, wrong); booleans and states; and the final
   reply against the diff (success claimed with no matching write; absence claimed with a match present; a value
   stated that differs from what was written). Say what each check cannot see.
2. Run them on all 3,018 executions. Report counts with denominators, by service, form and outcome.
3. Read about 60 flagged executions by hand, stratified over the checks, and estimate each check's precision. Read
   the "wrote, then restored" cases with their trajectories; a diff alone cannot tell restoration from a no-op.
4. Propose the value layer: which checks are mechanical, which need a judge, how the results are reported apart
   from fact-discrimination exposure, and what the checks cost.

## Deliverable

`grounding/runs/values_01/report.md`: status; the check definitions; the counts; the hand-read sample and the
precision estimates; examples of each error kind; the proposal. Message the lead when the counts exist and at the
end.
