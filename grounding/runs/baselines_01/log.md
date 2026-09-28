# Cycle log

Times are US Eastern, from `date`.

## 2026-09-28 14:02: set-up

- The questions and constraints are in the [README](README.md).
- Plan, reviewed with the advisor:
  - **Q4 first**, from existing data only.
  - **N0, "ask your coding agent":** Muse Code, one sandboxed session per domain. It gets only the goal in plain
    words, the API docs the agent under test gets (`api.md`), how to seed data (`seed_ops.md`) and a neutral test
    format. It gets no domain model, facts, substitute menus, method, worked examples, replica profile, checks or
    feedback.
  - **Before any agent run:** review N0's tests by hand for facts exercised, the credit rule, validity (with the
    cause of each flaw) and the oracle. The mapping rules are written down before the review.
  - **Runs:** label every trial by hand before any verdict. Then grade with N0's own assertions, a plain LLM judge
    and J0.
  - **After N0:** decide the next cycle from what N0 shows. That is either N1 (N0 plus the facts, no menus) or
    hand-built ablations of our own tests.

## 2026-09-28 14:10–15:00: cycle 1, N0 ("ask your coding agent")

- **Q4 done** from existing data ([q4/README.md](q4/README.md)). A plain judge (told nothing about grounding) now
  runs on OpenClaw's 178 labelled trials, to measure what J0's prompt adds.
- **N0 generated** ([n0/](n0/)): four Muse Code sessions wrote 48 tests for $0.51 at list ($0.027 billed); all loaded
  at the first try, so no repair turn was needed.
- **My review, before any run** ([n0/review_gen_01.py](n0/review_gen_01.py)):
  - near misses: 39 plain (F0), 8 partial names (F8), 1 neighbouring value (F7); no F1 to F6;
  - forms: 36 target present, 9 absence presupposing a match, 3 sets; none permits absence, none underspecified;
  - facts exercised 49, exercised properly (credit rule) 8, against about 34 for 48 of our Phase 4 tests
    ([ours.py](ours.py));
  - invalid 3: two Slack deletes the service refuses (the bot is not the author), one Slack mention the API never
    shows; 2 oracles unsound (a Box delete expected as a removed row; one emoji name).
- **Runs:** N0's 48 tests × 3 trials on OpenClaw, 12 in flight (`n0/runs/gen_01/solve_01`). Labels are written as
  trials end (`labels.json`), before any assertion or judge verdict.

## Cycle 2, planned from cycle 1 (built while cycle 1 runs)

The two parts most likely to carry our exposure, both suggested by existing OpenClaw data (covers expose 2 of 77,
probes 76 of 279; F1-F8 probes 67/223, F0 probes 9/56):
- **Form ablation:** N0's own target-present tests turned into probes (target removed, "If there isn't one, just tell
  me."): 28 tests ([n0/probe_form.py](n0/probe_form.py)). Does the probe form alone make N0's plain near misses expose
  failures?
- **Content ablation:** plain twins of 12 of our probes that exposed a fact on OpenClaw, same request and seed, the
  substitute removed ([plain_twins.py](plain_twins.py), [plain_pick.json](plain_pick.json)), run beside the
  unchanged originals the same day. Of the facts our probes expose, how many would a plain near miss expose too?
