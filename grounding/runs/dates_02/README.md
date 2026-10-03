# dates_02: dates belong to the test

*The PI's request of 2026-10-03, in three parts: (1) record in the documentation that shifting the agent's clock is
discontinued as a severe anti-pattern; (2) find which tests in the denominator tables the dates affected (the 2018
tests, tests run under a "now" other than the one they were written for, tests made too easy or impossible, tests that
could not run); (3) fix it: first by deterministic checks applied retrospectively to the generated tests, turning
every date, weekday and similar phrase into a template that is filled in with the real date when the test runs; only
as the last resort, minimal instructions to the writer to use templates, with the writer given the current date.
Follows [dates_01](../dates_01/README.md).*

## Status

- **2026-10-03:** part 1 done ([grounding/AGENTS.md](../../AGENTS.md), "Dates: never change the agent's clock"; the
  roadmap's step 8; the shims' docs). Parts 2 and 3 in progress. Nothing is run and no suite is changed in place.
