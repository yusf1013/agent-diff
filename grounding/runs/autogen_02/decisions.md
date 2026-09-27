# Decisions log (autogen_02)

Decisions and observations from the discussions with the user after autogen_01. They are the source for the next
version of [plan.md](plan.md), which is still a draft.

## 2026-09-26

**N1. Generation effectiveness has two parts.** Settled.
- **Within the domain model,** and so something we can instruct on. Example: which sibling field carries a
  substitute. People name calendars after places and state topics in event titles.
- **Beyond the domain model:** how requests refer to records, and how identifiers get matched. Examples:
  - a near miss whose identifier extends the requested one (pat.kimura for pat.kim), not the reverse;
  - loose, natural references rather than quoted exact names;
  - strong matches on the other conditions;
  - values that need a conversion to check.

We acknowledge the second part but do not work on it now. Evidence:
[autogen_01/eval/yield_gap.md](../autogen_01/eval/yield_gap.md).

**N2. Tests come from the requirement space, not from a model's weaknesses.** Settled. Generation packs facts,
designs near misses from the domain model, and hides targets behind them. It is never tuned to a particular agent.
Qwen is only the measuring instrument. The draft plan's Qwen-specific parts are dropped:
- the predictor of which near misses fool Qwen (Phase 0.1);
- the solver in the loop (arm M3).

**N3. The reader has to be a very careful checker.** Noted for future work. Asking a model whether a scenario is
correct risks reproducing the deficiencies the tests are meant to catch. The reader blocked the exemplars' Tokyo
scenario, whose near miss was the most effective one.

**N4. Validity is accepted as meeting the bar; reduced effectiveness is accepted for now.** Settled, with autogen_01's
caveat that the validity reviewer (Claude) also built the kit.

**N5. The next focus is the evaluator.** Settled.
- **The goal:** valid tests evaluated correctly, at or above the manual standard.
- **Precision first.** A reported failure must be the agent's fault. Recall can be more lenient.
- **Why:** with fewer exposures from the generator, every real one matters, and none should be lost or diluted by the
  evaluator.
