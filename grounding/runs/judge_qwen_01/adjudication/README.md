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

## Verdicts I saw before labelling

The run logs print each verdict's outcome and facts. Before I stopped reading them, I saw Qwen's outcome for
these executions (the smoke run's three, and log lines while checking progress). If one of them reaches a queue,
its label notes this. I saw no Muse verdict and no reference label for any execution.

- `full_03/t1/P-AP-SLK-01-I11`, `solve_absence_look4/t1/AT-G4-BOX-07-I13`,
  `solve_population_underspecified/t1/U-AP-SLK-04-Message_message_text` (smoke run, `runs/smoke_01`)
- `full_04/t1/P-G4-BOX-15-I13`, `solve_population_6b_absence/t3/AT-G4-LIN-09-I12`, `full_03/t2/P-AP-SLK-01-I13`,
  `solve_population_absence/t3/AT-G4-CAL-05-I12`, `full_03/t2/FP-G4-LIN-08-I11-I12`, `full_03/t2/P-G4-SLK-04-I11`,
  `solve_population_underspecified/t3/U-G4-CAL-03-primary`, `full_03/t3/P-G4-SLK-08-I13`,
  `full_03/t2/P-AP-LIN-02-I13`, `solve_population_6b_absence/t2/AT-G4-CAL-09-I11-I12`,
  `solve_population_underspecified/t3/U-AR-BOX-24-Task_created_at` (`runs/selfhost`, log lines)
- At the pause (06:39 UTC), the last three log lines showed Qwen's outcome for `full_03/t2/P-AR-SLK-24-I14`,
  `full_03/t2/P-AR-CAL-21-I14` and `solve_population_underspecified/t1/U-AR-LIN-21-Issue_createdAt`. None was in
  a queue.

## Rounds

| Round | Executions | Disagreements | Labels locked (UTC) | Unblinded |
|---|---|---|---|---|
| `labelled` | the 443 labelled | 3 | 2026-09-30 05:05:53 | `unblinded_labelled.json` |
| `rest` | the first 680 of the other 1,696 (the replay was paused there) | 15 | 2026-09-30 06:41:13 | `unblinded_rest.json` |
| `rest2` | the other 1,005 of the current manifest's 2,115 (resumed 20:48 UTC), less the keys labelled in the earlier rounds | 16 | 2026-09-30 22:57:45 | `unblinded_rest2.json` |

Labels of a later round are written after the earlier rounds were unblinded; each such label says so.

During the resumed replay I read only progress counts and the log's header line, never its verdict lines, until
the lock.

## Notes after unblinding

The locked files stay as they were. No label is corrected.

- **`solve_population_6b_underspecified/t3/U-G4-BOX-13-Comment_created_by_id` (round `rest2`): the label's reason
  misstates one step.** It says the solver "never read the files' comments". In fact its step 4 (`/steps/3`) listed
  the comments of all five PDFs, and its reasoning then noted that several carry the release phrase. It chose 8102
  from its description anyway. That makes the label's outcome (incorrect, `A:Comment.message`) firmer, not weaker, so
  the label stands. Both judges' notes describe the step correctly.
