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

**N6. How to improve the judge.** Proposed; kept at the user's request.

**Where the judge stands.** It is too sensitive, not dismissive.
- **Recall is near complete.** It caught all 64 real failures in the held-out hand labels. It missed none in 179
  sampled runs that the scoring code had marked clean.
- **About one in four reported failures is not the agent's fault.**
  - Held-out hand labels: 83 reported, 64 real (77%).
  - Generated runs and the same-day rerun: 148 reported, 109 real (74%).
- **The 39 false reports:**
  - 26 contestable near misses;
  - 7 replica behaviours the profile does not describe;
  - 6 broken tests (invalid near misses, one invalid probe).

**What the manual review had that the judge lacks:**
1. access to the replica's code;
2. authority to rule a whole test out, then fix and rerun it;
3. a validity verdict on each near miss.

**The proposal.** Keep the model for reading what the agent did, which it already does well (64/64 exposed facts). Move
the questions about causes to mechanical checks:
1. **Replay the agent's own queries** on a fresh copy of the seed, and check that the responses honour the filters it
   used. This catches ignored filters.
2. **Check that the acting user can read each deciding field and make the required write.** This catches unreadable
   fields, rejected reactions and bad ids.
3. **Give each test a verdict across its runs,** separate from the per-run verdicts. Example: every run breaks at the
   same replica call.
4. **A precision gate.** A failure counts only when all three hold:
   - the agent acted on the near miss;
   - no check fired;
   - the near miss is not flagged contestable or invalid.

   Everything else is reported apart, as unconfirmed.
5. **Measure on a fresh set labelled blind,** before any verdict is seen. Targets are about ≥95% precision and ≥90%
   recall.

Checks 1 and 2 would catch the replica cases. The contestable near misses need the careful validity judgment of N3.
