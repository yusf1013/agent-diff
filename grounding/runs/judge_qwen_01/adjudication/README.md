# Manual adjudication of the Qwen-Muse disagreements

Step 4 of the brief: for every execution where Qwen's verdict and Muse's disagree, I read the execution and decide
who is right. These labels are manual work (an Opus agent's, under the PI's rule), kept apart from everything the
judges read, and never given to a judge.

## What counts as a disagreement

[compare.py](../compare.py) lists an execution when the two verdicts differ in
- the outcome group (failure: incorrect, presented; nonfailure: correct, correct_absent, false_absence,
  incomplete; void: artifact, not_established);
- or, within a group, the exact outcome;
- or, when both are failures, the exposed facts.

## How I label, blind

1. `queue_<set>.json` holds the keys only, shuffled. Its order says nothing about the verdicts.
2. For each key I read the evidence only: `python grounding/runs/judge_qwen_01/view.py KEY` (request, test form,
   the construction's targets and decoys as hypotheses, the solver's steps, its final answer, the state diff). It
   shows no verdict, no reference label, and not the bundle's mechanical attribution. I use the judge prompt's
   outcome definitions and the domain's replica notes, and the PI's rulings on individual tests
   (`roadmap_01/known_defects.json`, blind_review_01's README), and look at each case as it is.
3. I write the label into `labels_<set>.json` before opening either verdict or the reference label: outcome, ids
   acted on, exposed facts, mechanism, artifact reason, the decisive steps, the reason, and my confidence.
4. `adjudicate.py lock <set>` records the file's SHA-256 and the time. Only then does `adjudicate.py unblind <set>`
   set each label beside Qwen's verdict, Muse's and the reference label, and say who was right.
5. Where my label and a reference label differ, both stay: I report the difference and never revise a reference
   label. A label I would change after unblinding goes to a separate corrections list, with the reason; the locked
   file stays as it was.
