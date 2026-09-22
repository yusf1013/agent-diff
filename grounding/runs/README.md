# Experiment evidence

All tracked historical experiments moved here intact internally:

- [slack_campaign](slack_campaign/): original campaign, writer pilots, compilation/solver/evaluator runs and human reviews. Start with [writer pilot 04](slack_campaign/writer_pilot_04/review.md), [W01 compilation review](slack_campaign/compiler_pilot_01/review.md), or the later compiler-batch reviews in this directory.
- [oracle_evaluation](oracle_evaluation/): evaluator variants, repeats, comparisons and archived trials.
- [slack_baseline](slack_baseline/): original saved Bedrock solver runs.

The [manual Slack comparison](manual_comparison_01/report.md) runs all 57 [manual exemplars](manual_exemplars_01/story3.md) on Sonnet 5 and Haiku 4.5, with per-case manual judgments, full trajectories/state evidence, and cache/cost accounting.

Historical paths inside JSON and provider transcripts were not rewritten. Human review links were updated where their targets moved. Use `python -m grounding.paths OLD_PATH` to locate recorded paths. A folder name or a recorded `review_pass` is not a new validity claim; retain the associated manual review and failed attempts.

New writer and compilation batches use:

```text
<run>/
  assignments.json or plan.json
  usage_ledger.json, usage_summary.json
  cases/<case>/
    assignment.json
    generation/
      input.md, writer/turn-01/, writer/turn-02/  # writer run
      input.json, story.md                     # compilation run
      compiler/turn-01/, compiler/compiled-1.json
      validation/checks-1.json
      reviewer/attempt-1/turn-01/
      case.json, summary.json
    environment/
      preflight/
      initial_state.json, final_state.json, diff_run.json
    solver/
      system_prompt.txt, config.json, <case>.json, final_response.md
    evaluation/
      inputs/
      assessment/, assessment-repair-1/        # repair only when needed
      command.json, run.log
    manual_review/                            # reserved for human judgments
    execution_summary.json
```

Writer and compilation batches may be separate runs. The compiler copies the source sketch and records its path and hash; it does not duplicate the writer's full conversation. The generated case contains its fresh seed; `environment/initial_state.json` records what was actually installed. The solver's native run JSON can still embed its diff as part of its original record; dedicated state/diff files are owned by `environment/`.

Do not edit requests, responses, thinking or original outcomes to make historical runs match newer policies. New repairs, interventions and model runs need distinct records. Manual judgments do not belong in model input bundles.
