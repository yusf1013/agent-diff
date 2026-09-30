# Brief: regenerate the Sonnet-written half with Muse (session "regen")

Rules for every session: [README.md](README.md). Study folder: `grounding/runs/regen_01/`. Muse cap for this
session: **$10 billed** (generation is its job).

## The question

Can the frozen pipeline (tag `grounding-freeze-01`, as run by completion_01), with Muse as the writer, regenerate
valid tests for the briefs that autogen_01's Sonnet writer covered, so that the whole evaluated suite comes from one
pipeline version and one writer?

Why: 271 of the 565 regular tests (and their policy units) come from 49 scenarios Sonnet wrote in autogen_01,
while the method was still being tuned. The PI does not want a suite that mixes writers. The old Sonnet suite stays
as it is, as a historical record and a later writer comparison.

## Materials

- **The template:** `grounding/runs/completion_01/` (6b): 26 briefs through the frozen pipeline: Muse writer →
  code checks → cold reader → derivation of covers, probes and fact probes → policy variants (drop-F wording and
  clones, each read by hand before it runs) → opaque ids → review. Its README records every step, the acceptance
  rates and the costs. Reuse its scripts; do not change pipeline code.
- **The briefs to regenerate:** autogen_01's (`grounding/runs/autogen_01/`, arms R, P and P v2: 49 accepted
  scenarios covering 81 facts; the brief format may differ from the frozen pipeline's: map it, don't rewrite the
  facts). `grounding/runs/report_01/numbers/concise.json` → `writers.Sonnet.coverage` lists the facts.
- **Three facts need their designated near miss** (the lure), not a plain different value:
  - `A:Cycle.number` (Linear): a cycle whose *name* says "Cycle 4" but whose number isn't 4;
  - `A:Message.message_text` (Slack): the words appear only in the message's formatted blocks;
  - `R:IssueRelation.relatedIssueId` (Linear; Muse's own scenario had only a plain miss): the relation pointing the
    other way. This one needs a new brief of its own.
- The rulings that apply to every test: `grounding/runs/roadmap_01/known_defects.json` (near misses the PI ruled
  flawed, clocks), `autogen_01/kit/opaque_ids.py` (made-up ids become opaque; run it on every new scenario), the
  date rule (tests that depend on the day get a test-side clock).
- Validity criteria: the PI's rulings in the roadmap ("Decisions (2026-09-28)"): a near miss the agent cannot check,
  or that a natural reading of the request includes, is flawed; ambiguous ones case by case.

## Steps

1. Enumerate the 49 briefs and their facts; add the related-issue brief. Record the mapping.
2. Generate with Muse through the frozen pipeline, in batches, with every check and the cold reader. Log each
   batch: attempts, accepted, rejected and why, cost.
3. Review every accepted scenario yourself, as the manual reviews in autogen_02 and completion_01 did (valid; flawed
   but usable; invalid; with reasons). Review every policy variant with the one question "can the action be done to
   each intended match?".
4. Derive the tests, apply the opaque ids, and write the suite in the layout openclaw_eval_01's runner expects
   (see how completion_01's suite was materialized for `full_04`).
5. When the lead says the self-hosted Qwen is up: run every test at 3 trials on OpenClaw with the openclaw_eval_01
   runner (`SOLVER_BACKEND=selfhost`, concurrency at most 24, the 10-minute limit), judge with Muse judge v2 as
   before, draw a blind sample before any verdict (about 100 executions, stratified by service and form), label it
   yourself, then score with `adjudicate.py` and the policy scripts. Do not start the runs before the lead's word.
6. Report the funnel like report_01's Table 5, the coverage reached (facts, against the 81), the exposure, the judge
   check, and costs.

## Deliverable

`grounding/runs/regen_01/README.md`, kept current. Message the lead: when the suite is ready to run (with the
funnel numbers), and when the runs and scoring are done. Do not edit autogen_01, completion_01 or report_01.
