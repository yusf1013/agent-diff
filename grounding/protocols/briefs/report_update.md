# Brief: bring the report texts to the current numbers (session "report_update")

Rules for every session: [README.md](README.md). Study folder: `grounding/runs/report_01/` (this brief is the one
exception to "do not edit report_01": you edit its two report texts and its README's change log, nothing under
`kit/` or `numbers/`). No model calls.

## The task

`report.md` and `report_concise.md` still show the numbers of the 8-minute budget and a few stale references.
The numbers in `numbers/` are current (rebuilt 2026-09-30). Bring the texts to them, change by change, and log
every change. The PI reads the concise report as the paper's stub, so precision matters more than speed.

## What changed, and where it shows

1. **The solver's budget is 10 minutes** (roadmap, "Decisions (2026-09-29)"; `report_01/README.md`, "Recount").
   Affected: §0.4's execution categories, RQ4 (Tables 7 and 8, the paragraph on executions: 104 over budget → 52,
   138 → 143 tests exposing, 87/60 → 88/61 facts), RQ6 (Table 11's rates and intervals; decisions unchanged),
   Table 12 if its counts moved, RQ7's denominators if they moved, RQ8's Muse expectation
   (`concise.json` → `equal_budget_muse_final`), the lessons' mechanism counts (`exposure.json` →
   `failing_trial_mechanisms_judge_v2`), and the limits section ("The eight-minute budget was applied after
   executions performed under a ten-minute limit" is no longer true).
2. **Duplicate policy units count once** (two pairs; `openclaw_eval_01/rulings.py`, `DUPLICATE_UNITS`): Table 11's
   unit counts for Linear underspecified (79 → 78) and Slack underspecified (32 → 31), Table 6 and Table 12 if
   they count units.
3. **The F0 rule** (roadmap): RQ2's paragraph on the 37 facts credited through plain near misses should say which
   have no lure in the domain model (4), which have a lure the rulings make flawed (2), and which one is being
   regenerated; RQ8's coverage row note should say the comparison uses one rule on both sides.
4. **Stale references:** RQ8 says the baseline evidence "remains on the existing baseline branch" and Table 15
   links into `.claude/worktrees/baselines-01/...`; the study is `grounding/runs/baselines_01/` on main.
5. **blind_review_01** (a second reference review: Codex labels on 200 final executions, locked before unblinding;
   `grounding/runs/blind_review_01/README.md`, `numbers.json`, `uncertainty.json`) is not in RQ5 yet. Add it as its
   own paragraph and table row: pipeline agreement 186 of 190 non-void (68 TP, 4 FP, 0 FN), the judge alone 119 of
   123, exposed facts equal on all 68 joint failures, mechanical triage 67 of 67, the case-cluster bootstrap
   intervals. Say plainly that these are AI reference labels, not a second human. The limits section's "one manual
   annotator" line changes accordingly.

## How

- Take every number from `numbers/*.json` or the named study files; never from memory. Where a number in the
  text has no source in `numbers/`, say so in the log and leave it.
- Keep the reports' style: short sentences, plain words, denominators.
- Log each change in `report_01/README.md` under "Text changes (2026-09-30)": section, old → new, source file.
- Commit the two texts and the README together, in small commits per section.

## Deliverable

The updated texts, the change log, and a message to the lead listing what you could not source.
