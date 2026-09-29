# Review rules for baseline tests (fixed 2026-09-28, before any baseline test was generated)

The same rules apply to every baseline's tests and to the sample of our own tests shuffled into the review pool.
They restate the credit rule ([criterion.md](../../fact_coverage_01/criterion.md)) and today's flaw rules
([roadmap](../../../protocols/roadmap.md), decisions of 2026-09-27 and 2026-09-28) for tests that carry no
annotations.

## Per test, by hand, before any agent run

1. **Conditions.** Split the request into the conditions that identify the record or records to act on.
2. **Facts exercised.** Map each condition to the catalog facts it rests on, as our writer's conditions do
   (`autogen_01/inputs/<domain>/facts.json`). A condition that maps to no catalog fact is recorded as outside the
   catalog. A test exercises the union of its conditions' facts.
3. **Competitors.** Every seeded record of the kind acted on, other than the intended ones, with the conditions it
   fails:
   - **near miss:** it fails exactly one condition;
   - **far:** it fails two or more.
4. **Kind of near miss.** For each near miss, the fact of the condition it fails, and whether it offers that fact's
   designated substitute from the catalog (families F1 to F8), or simply another value (F0, plain).
5. **Form.**
   - target present;
   - no target, with absence permitted ("if there isn't one, tell me");
   - no target, with the request presupposing a match;
   - several records that fully match a request for one (underspecified);
   - a request for a set.
6. **Exercised properly (the credit rule).** A fact is exercised properly when a test has a near miss through its
   designated substitute (4), in a fact-sensitive form: target present, or no target with absence permitted (5).
7. **Validity.** Every flaw gets a cause:
   - **(a) no single right outcome:** a natural reading of the request includes a competitor, or `expected` is
     wrong;
   - **(b) replica quirk:** the test would be valid on the real service, and the replica breaks it (counted apart);
   - **(c) does not load or install** (a funnel measure);
   - **(d) leaking ids:** an id names a record's role or the deciding difference;
   - **(e) the oracle does not check what `expected` says:** the assertions pass a wrong outcome or fail a right one;
   - **(f) the agent cannot tell:** the deciding field is not readable through the API;
   - **(g) depends on the run date,** or holds times the service never produces.
8. **Calibration.** About 10 of our own tests are shuffled into the pool and reviewed with the same rules. Their
   mechanically checked claims are compared with the hand review only afterwards.

## After the runs

- **Labels first.** Every trial is labelled by hand before any assertion result or judge verdict is read.
- **Failure to fact.** A failing trial exposes fact *f* when the record the agent acted on (or presented) is a near
  miss that fails exactly one condition, whose fact is *f*.
  - Acting on a far record is not attributable to one fact.
  - Acting when nothing matches and the request presupposes a match is the generic no-match policy, not fact credit.
  - Acting on one of several full matches without asking is the underspecified policy.
- **Oracles** are scored against the labels as yes/no confusion matrices: the test's own assertions, a plain LLM
  judge given the request and `expected`, and J0.

## Measures (question 3)

Per approach, at the same number of tests:
- tests written, tests that load, valid tests (with causes);
- facts exercised, and facts exercised properly;
- failures exposed: distinct facts at detect@1 and detect@3, failing tests, and failures that are one of the two
  policies;
- each oracle's agreement with the labels, and its false results;
- token cost: generation and judging, list and billed, per test, per valid test, per fact exercised properly and
  per fact exposed.
