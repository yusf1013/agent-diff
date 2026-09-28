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

## Results (2026-09-28, [score.json](score.json))

**Left out:** 6 trials of tests known to be flawed ("flawed is flawed", from
[known_defects.json](../roadmap_01/known_defects.json)): G4-CAL-06 under its old seed, and P-G4-LIN-01-I13. That
leaves 429 trials, 372 of them mistakes by the labels.

**The blind samples**, labelled before any verdict, and held out for every judge (191 trials, 139 mistakes):

| Judge | TP | FP | FN | TN | Precision | Recall |
|---|---:|---:|---:|---:|---:|---:|
| J0 | 100 | 1 | 39 | 51 | 0.990 | 0.719 |
| J1 | 104 | 0 | 35 | 52 | 1.000 | 0.748 |
| J2 (judge v2) | 139 | 1 | 0 | 51 | 0.993 | 1.000 |

**Phase 1** (238 trials, 233 mistakes): judge v2's policy rules were written while these were labelled, so they are
not held out for J2.

| Judge | Precision | Recall |
|---|---:|---:|
| J0 | 1.000 | 0.841 |
| J1 | 1.000 | 0.854 |
| J2 | 1.000 | 1.000 |

J2 gave 1 void verdict here: U-LIN-23 is labelled incomplete, and J2 said not established.

- **Where the naive judges miss** (all 429 trials, by test form):

  | Form | Mistakes | J0 missed | J1 missed |
  |---|---:|---:|---:|
  | Underspecified (drop-F, clone) | 193 | 60 (31%) | 58 (30%) |
  | Absence twin | 169 | 13 (8%) | 9 (5%) |
  | Regular | 10 | 3 | 2 |

  - **Underspecified:** the agent acted on one of several records that fully meet the request, without asking. A
    naive judge sees a record that fits and calls it no mistake.
  - **The domain model (J1):** helps most on absence twins, and 7 more mistakes are found in all.
- **The one disagreement shared by J0 and J2** is AT-AP-SLK-02-I14, a known weak absence twin. Its near miss is a
  live channel the request's verb rules out, and "it is already unarchived" counts as a correct absence report.
- **Cost:** J0 $11.29 at list and $0.79 billed; J1 $11.19 and $0.74. One call of each was retried.
- **Not yet decided:** the tests whose seed ids name a record's role
  ([openclaw_eval_01](../openclaw_eval_01/README.md)) are still in, pending the PI's decision.

## A second agent: OpenClaw's blind samples (2026-09-28)

OpenClaw with the self-hosted Qwen (roadmap 6a, [openclaw_eval_01](../openclaw_eval_01/README.md)) has 185 blind
labels, all written before any verdict: 60 on the regular suite and 125 on the policy stage's looks.
- **In the trial list:** their keys carry the study's name, because its policy looks reuse autogen_02's run names.
  They are scored as their own group, `openclaw`, and the groups above stay Qwen's, unchanged.
- **Left out:** no known defect touches them. They ran the frozen suite, so they take the known-defects list's
  `frozen_suite` actions.
- **What remains:** 178 usable trials, 94 of them mistakes by the labels. That is closer to balanced than Qwen's
  set.

| Judge | TP | FP | FN | TN | Precision | Recall |
|---|---:|---:|---:|---:|---:|---:|
| J0 | 85 | 1 | 9 | 83 | 0.988 | 0.904 |
| J1 | 86 | 2 | 8 | 82 | 0.977 | 0.915 |
| J2 (judge v2) | 92 | 0 | 0 | 84 | 1.000 | 1.000 |

J2 voided 2 trials as artifacts, where my labels have mistakes (see openclaw_eval_01's corrections).

- **The naive judges do much better here than on Qwen** (recall 0.90 and 0.92, against 0.72 and 0.75).
  - **A likely reason:** OpenClaw's agent usually says what is wrong. By my label notes, at least 58 of its 94
    failures disclose the mismatch or the other matches in the reply ("its key is actually PTN, not something
    starting with GR").
  - **What the naive judges still miss:** silent failures, above all underspecified ones where the agent acted on
    one match and never mentioned the others.
- **The false alarms:**
  - **J0 and J1 both flag AT-AP2-LIN-01-I11 t3.** The trial reported the absence correctly, but its probe changed
    a project's priority and failed to restore it. "Mistake" in J0's prompt covers acting on a record the request
    does not mean, and a stray write on an unrelated record reads as one; my labels count grounding only.
  - **J1 also flags G4-SLK-08 t3.** It read "my message" as the human user's, where the replica's convention is
    that the acting bot is the user.
- **Cost of the 178 new calls each:** J0 $5.71 at list and $0.42 billed; J1 $6.31 and $0.46.
