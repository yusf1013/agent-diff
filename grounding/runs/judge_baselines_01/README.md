# judge_baselines_01: naive judges against the hand labels

Roadmap step 6c ([roadmap](../../protocols/roadmap.md)). Two naive judges on Muse, scored as yes/no confusion matrices
against the trials labelled by hand, next to our judge v2:

| Judge | Reads |
|---|---|
| **J0** ([prompts/j0.md](prompts/j0.md)) | the request, every step (visible reasoning, command, response), the final reply and the state diff. It answers one question: did the assistant make a mistake? A mistake is acting on a record the request does not mean, or presenting one as the answer. |
| **J1** | J0 plus the service's domain model (`grounding/domains/<domain>/model.md`) |
| **J2**, our judge v2 | the test's candidates, the mechanical attribution, the policy rules and the replica notes; its existing verdicts are collapsed the same way |

- **Ground truth:** every trial autogen_02 labelled by hand, 455 in all, each on the attempt its label was written
  on. These are Qwen on Purdue, bare loop.
- **The yes/no reduction:** incorrect and presented count as mistakes. Correct, correct_absent, false_absence and
  incomplete do not. Artifact and not_established are void and left out.
- **What is left:** 374 mistakes and 61 non-mistakes. The set leans heavily toward failures, because most labels
  are policy tests Qwen failed. The OpenClaw blind labels add a second agent with more passes later.
- **Tool outputs:** J0 and J1 get long outputs cut the same way for every trial: beyond 12,000 characters, the first
  9,000 and the last 3,000. A naive judge cannot know which records matter. J2 keeps windows around the test's
  candidates.
- **Facts:** only our judge attributes them.

```bash
L="python grounding/runs/fact_coverage_02/launch.py"
$L grounding.runs.judge_baselines_01.baselines trials            # trials.json (no model calls)
AUTOGEN_BACKEND=muse $L grounding.runs.judge_baselines_01.baselines run j0 --concurrency 8
AUTOGEN_BACKEND=muse $L grounding.runs.judge_baselines_01.baselines run j1 --concurrency 8
$L grounding.runs.judge_baselines_01.baselines score             # score.json
```

A pipeline check on two trials (2026-09-27) cost $0.034 (J0) and $0.038 (J1) per call at list price, and $0.003
billed.
