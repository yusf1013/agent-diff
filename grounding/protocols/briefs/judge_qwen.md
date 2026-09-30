# Brief: the judge on Qwen (session "judge")

Rules for every session: [README.md](README.md). Study folder: `grounding/runs/judge_qwen_01/`.

## The question

Does our judge keep its accuracy when the model behind it is the self-hosted Qwen3.8-27B instead of Muse, with the
same prompt and the same inputs? Where the two disagree, which one is right?

The PI's expectation: most verdicts will match, so the manual work is reading the disagreements. If Qwen holds up,
the whole pipeline runs on an open model, and the paper gets a "does the judge need a strong model" result.

## Materials

- The judge: `grounding/runs/autogen_02/kit/` (judge v2; its prompt is `kit/prompts/judge_v2.md`), and how
  openclaw_eval_01 runs it on OpenClaw trials (`grounding/runs/openclaw_eval_01/README.md`, "How to run").
- The runs and their Muse verdicts: openclaw_eval_01's `judged_*` folders and the policy populations. The final
  selection of 3,018 executions is `grounding/runs/report_01/numbers/concise.json` → `final_execution_keys`;
  the 2,139 with an LLM verdict are the ones to replay.
- Reference labels, all made blind before any verdict:
  - the lead's 310 retained labels on final executions: `concise.json` → `blind_label_keys` and the label files
    openclaw_eval_01's README points to;
  - blind_review_01's 200 (`grounding/runs/blind_review_01/effective_labels.json`, with `README.md` for the
    outcome vocabulary and the comparison rules).
  - Together about 500 executions, with about 190 labelled failures.
- How report_01 computed judge accuracy: `grounding/runs/report_01/kit/` (the judge-accuracy script) and the
  concise report's RQ5.

## Steps

1. Find how judge v2 chooses its model backend. Add a backend for an OpenAI-compatible endpoint without changing the
   prompt, the inputs or the output schema. Two endpoints:
   - **Purdue's Qwen** (`qwen3.8:27b`, key `PURDUE_GENAI_STUDIO_API_KEY` in `grounding/.env`, about 20 requests a
     minute, streams cut short: go through `grounding/integrations/openclaw/purdue_proxy.py` or the toy harness's
     Purdue client, which handle both). Use this first.
   - **The self-hosted Qwen** (`http://127.0.0.1:18000/v1`, model `qwen3.8-27b`, key in
     `~/qwen-selfhost/secrets/api_key`; never print it), only after the lead says it is up. Repeat the replay there
     if it comes up; report which host produced which numbers.
   Record every call as the pipeline does (request, response, usage, cost of zero).
2. Replay on the ~500 labelled executions first. Then, as time allows, on all 2,139.
3. Compare, per execution: Qwen's verdict against Muse's (exact outcome; failure or not; exposed facts), and each
   against the reference label. Confusion matrices with denominators. Void handling as in blind_review_01.
4. For every disagreement between Qwen and Muse, read the execution (an evidence-only view, as
   `blind_review_01/view.py` gives; never the verdicts first) and decide who is right, with the reason. This is
   manual labelling; keep it in its own file.
5. Bar, fixed now: Qwen can replace Muse only if, on the labelled executions, it misses at most 2 of the labelled
   failures and its precision is within 3 points of Muse's. Report against this bar; the decision is the lead's.

## Deliverable

`grounding/runs/judge_qwen_01/README.md`: status; the question; the setup (backend, host, prompt unchanged);
the numbers; the disagreements with your adjudications; costs (Muse: none; Qwen: none); what is not covered; and a
recommendation against the bar. Message the lead when the labelled replay is done, and again at the end.
