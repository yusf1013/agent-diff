# Run index

The run folders are hidden from default searches by [../.ignore](../.ignore). Name a folder to search it.

**To find an episode:**
- **Verdicts:** [../manual_labels.json](../manual_labels.json), keyed `run/trial/case`.
- **Summaries:** [../tables.md](../tables.md).
- **Raw files:** `<run>/<trial>/<case>/attempt-NN/`. The last attempt counts.

Each episode holds:
- `case.json`: the request, seed and references;
- `solver/<case>.json`: every turn's command and observation;
- `solver/final_response.md`: the final answer;
- `environment/diff_run.json`: the state changes;
- `execution_summary.json`: status and usage.

| Run | What | Cases | Trials | Episodes |
|---|---|---:|---:|---:|
| b1 | Baseline 1: the pilot's cover cases at 3 trials | 31 | 3 | 100 |
| method_pilot | Method v1 on the pilot's facts | 139 | 3 | 434 |
| method_pilot_panel | Policy panel, pilot domains | 5 | 3 | 15 |
| method_new | Method v1 on the new scenarios (controls, probes, Slack panel) | 79 | 3 | 237 |
| method_new_lin25, method_new_slk21 | Reruns of two fixed scenarios | 3, 7 | 3 | 9, 22 |
| factprobe, factprobe_extra | All of a fact's decoys in one probe (§12.2), plus equal-run extras | 19 | 3, 9 | 57, 75 |
| wording_check | Hidden-target covers plus "just tell me" (§12.3) | 3 | 3 | 9 |
| hidden_pilot | Hidden-target pilot and probe twins (§12.3) | 7 | 3 | 21 |
| prepare_* | Preflights without the model (`prepare_hidden` is the replica check) | | 1 | |
| smoke_slack | One exploration episode | 1 | 1 | 1 |
