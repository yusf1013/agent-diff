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
