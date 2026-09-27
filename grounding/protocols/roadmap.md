# Roadmap after autogen_02

Agreed with the PI on 2026-09-27, after [autogen_02](../runs/autogen_02/overview.md). The work is done in steps,
and the PI steps in where a step needs a decision. Progress is recorded in the status table at the end.

## The goal

The end point is a final evaluation of the automated grounding-test system:
- **Harnesses:** 1–2 real agent harnesses, such as OpenClaw.
- **Models:** a few models of different strengths.
- **Baselines:** two alternative ways to produce tests, compared on what their tests expose across the same agents.
  One is a coding agent with no help; the other is a coding agent given only our domain model. (This reading is
  pending the PI's confirmation.)

The suite should give every catalog fact a test, on the supported side (regular and policy tests) or on the
unsupported side (capability-boundary tests).

## The order: freeze the system before the final runs

The audits and several loose ends can change prompts or code. Every such change is discussed with the PI first, and
any change made after the final generation would force re-validation. So the audits come first, and everything final
runs on one tagged version.

1. **Quick unblockers:**
   - **The trial clock:** only the agent's own time counts toward the 8-minute trial limit. Waiting for Purdue (the
     shared rate limiter's queue, the pauses after rate-limit errors, and attempts that fail) is excluded. A wall
     ceiling guards against hangs. A trial cut by the agent clock is graded; one cut by the ceiling is retried.
   - **Muse's verify-reminder off** for the judge and the reader. It never changed a judge or reader call, and it
     cost about a fifth of the Muse bill.
   - **Loose ends that need only a list or an existing check:**
     - a list of known defective tests to leave out for new agents;
     - the witness check over every existing probe;
     - a flag for facts that depend on today's date.
2. **Two audits, reported and then discussed:**
   - **Overfitting and leaks in every prompt, before they are open-sourced.** Each prompt is read as a whole, and a
     mechanical scan matches its names and phrases against the tests and labels. Few-shot examples are fine; leaked
     answers are not. Fixes are made only after discussion.
   - **Domain knowledge hidden in deterministic code.** Every per-domain touchpoint the generator relies on is
     classified: derived from the mock, the domain model given as input, or hand-written knowledge. Then the
     question: what would we write for a new domain added to the mock?
3. **The PI steps in:** we discuss the audit findings and the pending loose-end fixes, apply what we agree, and tag
   a frozen version.
4. **Complete the suite on the frozen version:**
   - 26 remaining briefs: 19 never generated, 3 that failed, and about 4 new ones for 12 facts that autogen_01's
     scenarios did not realize.
   - Qwen runs them as a byproduct, in 3–4 Purdue hours.
5. **Investigations, manual first, then automated:**
   - **Failure attribution:** deciding which component a failure belongs to: the agent, the test, the mock, the
     harness or the judge. This is not about why the agent failed; mechanisms are fine for manual analysis. Bad tests
     cannot be prevented completely, so the aim is to detect or filter them with a valid reason. Whether that belongs
     in the judge or elsewhere is open.
     - The judge takes the test as given, so evidence about the test and the mock has to come from outside the one
       trajectory: a solver told the intended answer, patterns across agents, the mock's traces, and the agent's own
       objections.
     - The known defects of autogen_01 and autogen_02 form a labelled development set for scoring any method.
   - **Several-match requests:** can the agent find all of the matches and only them? Use at least 3 matches,
     because an agent may take "several" to mean two. Reuse what we know about where matches get missed: a search
     that cannot see message cards, reading only the primary calendar, thread replies, a second page. The judge needs
     a set-level mode with its own blind sample.
   - **The capability boundary:**
     - Tests close to the boundary, with tempting decoys (a nearby action that is possible and looks like it
       satisfies the request). The coverage space is a set of equivalence classes: a missing operation, a read-only
       field, a missing permission, a state precondition, a limit.
     - The 42 catalog facts the mock cannot serve could supply the unsupported side. A fact qualifies only where the
       agent's documentation says the feature is unsupported; a documented feature that the mock fails to serve is a
       mock bug, not a boundary.
6. **Final evaluation:** harnesses × models × baselines. Each agent's first run gets a blind sample to validate the
   judge on it.

## Open decisions for the PI

- **The final evaluation's size.** A full suite is about 2,000–2,400 trials per agent, or 12–22 Purdue hours per
  model. A lean suite (one probe per fact first) takes 2–6 hours. Models on paid APIs cost money instead of hours.
- **The baselines,** as read above.

## Standing rules

- Changes to existing prompts or functionality are discussed with the PI first ("if it ain't broke, don't fix it").
- Every Muse-written policy variant gets a manual read before it runs, now with one more question: "can the
  action be done to each intended match?"

## Status

| Step | Item | Status | Where |
|---|---|---|---|
| 1 | Trial clock excludes Purdue waiting | done (2026-09-27) | [roadmap_01/clock_smoke](../runs/roadmap_01/clock_smoke/README.md) |
| 1 | Muse verify-reminder off for judge and reader | done (2026-09-27) | [roadmap_01/muse_reminder_check](../runs/roadmap_01/muse_reminder_check/README.md) |
| 1 | List-level loose ends | done (2026-09-27) | [roadmap_01](../runs/roadmap_01/README.md) |
| 2 | Prompt overfitting and leak audit | reported (2026-09-27) | [overfit_audit.md](../runs/roadmap_01/overfit_audit.md) |
| 2 | Domain knowledge in deterministic code | reported (2026-09-27) | [domain_code_audit.md](../runs/roadmap_01/domain_code_audit.md) |
| 3 | Discussion, fixes, frozen version | ready: 13 proposed changes listed | [roadmap_01](../runs/roadmap_01/README.md#for-step-3-proposed-changes-none-made) |
| 4–6 | Suite, investigations, final evaluation | not started | – |
