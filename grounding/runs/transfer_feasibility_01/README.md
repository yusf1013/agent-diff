# transfer_feasibility_01: which tests can be rerun on the real services?

Desk study for the lead ("RoadMap specialist"), started 2026-09-30 in the judge_qwen session (message of
2026-09-30, about 03:00 EDT). No model calls and no host: the services' public API documentation, fetched and cited
with dates, and the suite's recorded seeds.

## Status

- **2026-09-30 03:15 EDT.** Started: the question and the plan below. Nothing classified yet.

## The question

How can we rerun a sample of the suite's tests against the real services (Slack, Linear, Box, Google Calendar),
to see whether the failures the mock exposes also happen there? Concretely:
- which of the suite's tests (the 565 regular tests and the 441 policy units) could be set up on the real services
  with ordinary accounts, or a small team of test accounts, through the public APIs, which only with a stated change
  (a date shifted, a second account, a paid plan), and which not at all, and why;
- and what a case study of about 40 tests would need: which tests, which accounts, what seeding scripts, how the
  agent reaches the real endpoints, and what it costs in time and money.

The mock was chosen because seeding is easy there (a message from someone two days ago is one row). The study
asks which of the suite's seed constructs the real services let a tester create.

## Plan

1. List the seed constructs the suite uses, per service, from the recorded seeds and the catalog's facts
   (backdated timestamps, other users' records, ownership and creator fields, shared links, collaborations,
   reactions, hidden calendars, sub-teams, cycles, …).
2. For each construct, decide from the services' API documentation whether one account or a small team of test
   accounts can create it, on which plan, and cite the page (URL, date read).
3. Classify every regular test and policy unit mechanically from its seed and its facts: realizable as is, with a
   stated change, or not; with the reasons.
4. Propose the case study: a sample of about 40 tests, the accounts, the seeding scripts' shape, the mapping from the
   replica's curl shim to the real endpoints, and a cost and time estimate.
