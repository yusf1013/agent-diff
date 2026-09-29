# Q4: why J0 and J1 came out close to judge v2

**Question:** did the naive judges land close to ours because of the wrong measure, an unfair advantage, or a part we
never ablated?

**Short answer:** mostly the last. 6c kept our tests fixed and changed only the judge. But our tests come with an
answer key: the target, every near miss, and the fact each one fails. From it, a mechanical check decides most
trials before any LLM reads them. The LLM judge is left with a small residue, and on that residue a naive judge does
nearly as well whenever the agent's own words give the mistake away. Two parts of the measure made this worse: the
scored set held only valid tests, and most of its failures were ones the agent narrates.

Numbers from [analysis.py](analysis.py) ([numbers.json](numbers.json)); no model calls.

## A. The answer key does most of the judging

OpenClaw's regular suite, `full_02` (1,314 trials). The mechanical triage reads the answer key and the state diff.
Judge v2 then reads every trial the triage cannot clear, plus a 20% sample of the cleared ones.

| | Trials |
|---|---:|
| Cleared by the triage as correct (never needs an LLM) | 957 (73%) |
| ... of which judge v2 checked, and changed | 227 checked, 2 changed |
| Failures after judge v2 | 189 |
| ... already flagged "incorrect" by the triage | 184 (97%) |
| Triage "incorrect" that judge v2 voided as artifacts | 11 |
| Triage "unsure" (mostly a probe's reply naming a near miss) that judge v2 cleared as correct | 143 |

So the triage alone finds 97% of the failures, from the answer key. The LLM's work is precision: it reads the
replies the triage cannot, voids artifacts, and adds 5 failures. J0 had none of the answer key and still reached
0.90 recall, because of B.

## B. J0 finds the failures the trajectory shows

Recall by how the failure happened (the mechanism in the hand labels):

| Mechanism | OpenClaw: J0 found | Qwen, toy harness: J0 found |
|---|---:|---:|
| Saw the mismatch and acted anyway | 43 / 43 | 58 / 61 |
| Misread a record | 4 / 8 | 72 / 77 |
| Skipped the check | 2 / 3 | 36 / 45 |
| No mechanism: acted on one of several full matches (underspecified) | 36 / 40 | 122 / 183 |
| All | 85 / 94 | 296 / 374 |

- **Where a mismatch is visible, J0 finds it.** The agent read the deciding field, or said it saw the mismatch. The
  test was built for exactly that: each near miss fails one condition that the normal reads show.
- **J0 misses what the trajectory does not show.** An underspecified failure acts on a record that fully matches.
  It is a failure only because other full matches exist. J0 knows that only if the agent listed or mentioned them.
  OpenClaw's agent usually does (36 of 40 found), and Qwen in the toy harness often does not (122 of 183). Judge v2
  knows it from the answer key.
- **So J0's recall measures the agent's narration as much as the judge.** It is 0.90 on OpenClaw and 0.79 on Qwen,
  on the same kind of tests.

## C. The scored set left out the trials where false results come from

- **27 trials were void** (18 artifacts, 9 not established). They are flawed tests and replica artifacts, and no
  naive judge read them.
- **On the 18 artifacts, judge v2 said "incorrect" 16 times.** It blames the agent for a flawed test, as the
  autogen_02 overview already notes.
- **So every judge's precision near 1.0 is a property of the scored set,** which people had cleaned. In a pipeline,
  false results come mostly from flawed tests. What protects ours there is the validity machinery (checks, reader,
  review), not the judge.

## What follows for the baseline design

- **Wrong comparison:** judge against judge with our tests held fixed. The comparison that shows the contribution is
  pipeline against pipeline: each pipeline's own tests, with each pipeline's own oracle. A naive pipeline has no
  answer key beyond what its test author wrote.
- **Unfair advantages J0 had:**
  - our tests, built so that a mistake shows in the reads;
  - our definition of a mistake in its prompt (acting on a record the request does not mean; asking and "none" are
    right);
  - a scored set without flawed tests;
  - on OpenClaw, an agent that narrates.
- **The missing ablation:** the answer key, which comes from generation. Judging without it is what a naive
  pipeline does.
- **Wrong measure:** mistake yes or no on valid trials. It leaves out false results on flawed tests and fact
  attribution, which only the answer key gives.

## D. What J0's prompt adds: a plain judge on the same 178 trials (2026-09-28)

A judge told nothing about grounding ([prompts/plain.md](../prompts/plain.md): "did the assistant do what the user
asked?"), on Muse, reading the same bundle as J0, scored against the same 178 OpenClaw labels
([score_plain.py](score_plain.py), [plain_openclaw.score.json](plain_openclaw.score.json)):

| Judge | Knows | Precision | Recall | Recall: regular | Recall: underspecified |
|---|---|---:|---:|---:|---:|
| plain | the request and the trajectory | 0.92 | 0.73 | 2 / 8 | 24 / 41 |
| J0 | + our definition of a mistake | 0.99 | 0.90 | 6 / 8 | 36 / 41 |
| J1 | + the domain model | 0.98 | 0.92 | – | – |
| J2 (judge v2) | + the answer key, policy rules, replica notes | 1.00 | 0.98 | 6 / 8 | 41 / 41 |

(J2's row is corrected on 2026-09-29; it first read recall 1.00 and 6 / 8 as 8 / 8. J2 gave no verdict on 2 of the
94 labelled mistakes, both on regular tests, because it voided them as artifacts. On one, the label missed a replica
response and the judge was right; the other is a contestable near miss
([corrections.json](../../openclaw_eval_01/eval/labels_full_02/corrections.json)). Scored against the original labels
like the other rows, the 2 are misses: recall 92 of 94. On the 176 trials it judged, J2 is 92 of 92.)

- **Absence twins are easy for every judge** (43 of 45 found by both plain and J0): acting on something when the
  request's record does not exist is visibly wrong.
- **J0's definition is worth 17 points of recall and 7 of precision** over the plain judge. Most of it is on the
  regular tests (a near miss that satisfies the plain reading) and on underspecified requests, where the plain judge
  calls acting on one of several matches a success (17 misses) and flags 5 correct trials.
- **So the 6c baselines were already given part of our work,** the definition of a grounding mistake, on top of
  our tests. A naive pipeline's judge would sit nearer the plain row.
