# several_match_02: where do we place the extra matches so that a lazy agent cannot pass?

*Started 2026-09-28 11:18 EDT. A manual investigation: hand-built tests, hand analysis, the self-hosted solver, no
Muse. It runs in cycles of build, run, analyze and iterate; [log.md](log.md) records each cycle. This plan states the
question and the method. Findings go in the log, and the report at the end.*

## The question

The PI: "how do we pack or where do we pack the other matches so that a lazy agent cannot pass them."

A plural request asks the agent to act on every record that meets its conditions. A lazy agent takes a shortcut
route and passes if the shortcut happens to return every match. The design question has three parts:
1. **Which shortcuts exist, per service?**
2. **Where can a match be placed so that a given shortcut misses it,** while the match stays within the request's
   scope and is reachable through an API path that behaves like the real service?
3. **How many tests** does it take to defeat every shortcut in a service? One test can hide matches in several places.

Agent runs come last. They show which placements catch real agents, and they feed back into the list of shortcuts.

## Terms

- **Strategy:** an ordered list of API calls that retrieves candidates for the request. A strategy "finds" a record
  if the record's id appears in one of its responses.
- **Lazy strategy:** a strategy that covers only part of the request's scope. The candidates come from the API's
  shortcuts and from the routes agents actually took (the pilot's 24 plural trajectories, and the ~2,360 earlier
  trajectories):
  - the default first page;
  - only the container the request names;
  - only a text search;
  - only the first query ("stops after the first batch");
  - the defaults that hide records (hidden calendars, private channels, archived records).
- **Generous variant:** the same query with larger quantity parameters (`limit=1000`, `first: 250`, `count=100`). The
  pilot's agent used these almost every time.
  - A placement defeats a quantity shortcut only if it survives the generous variant too.
  - Visibility flags (`showHidden`, `types=…private_channel`, `includeArchived`) are not generosity. Setting them is
    the thorough behaviour under test.
- **Thorough strategy:** the careful route that covers the whole scope. It must find every match; a test where it
  does not is invalid.
- **Lazy-proof placement (against a strategy):** the strategy misses at least one match.

## Validity rules (fixed before building)

- **Scope wording.** The request states scope as a user would. The reference query encodes the careful reading.
  - For each wording, record whether a careful reader includes the hidden place. For example, "every PDF under the
    Finance folder" includes subfolders; "every channel whose name starts with incident-" includes private ones.
  - Contestable wordings are not used. Wordings that hand the scope to the agent are recorded as such (for example,
    "including the ones in its subfolders"), since they test less.
- **No replica gaps.** Every retrieval path used, and every condition's field, must behave like the real service.
  - Known traps: Box folder listings return the short form whatever `fields` asks for (real Box honours `fields`);
    Box search ignores `content_types`; Linear ignores the `parent` and `subscribers` filters.
  - A placement that depends on a gap is invalid. A gap that only makes the agent's job easier (for example, Slack
    search usable by a bot) cannot invalidate a test, but it can make a placement fail to hide.
- **The seed must make the thorough route a different query.** A small seed lets "list everything" pass
  (fact_coverage_02 §12.3: hiding failed in the small Linear workspace).

## Method, per cycle

1. **Mechanical first (no model calls).** [strategies.py](strategies.py) runs every strategy against the replica on
   each seed and records which matches it misses: a strategies × placements matrix per service.
2. **Design** tests that combine placements so that every lazy strategy misses at least one match, while the
   thorough strategy finds them all. The matrix gives the minimum number of tests per service.
3. **Run** on the self-host: 3 trials per test, at most 12 in flight.
4. **Analyze** each trial's route ([routes.py](routes.py)). Which strategy did the agent follow, where did it stop,
   and which placements caught it? Update the list of strategies and placements, then iterate.

## What would answer the question

- A table per service of shortcut → the placements that defeat it (checked mechanically) → how often each caught
  the agent.
- The minimum number of tests per service that defeats every shortcut, and whether that is "a few" or needs many.
- **A valid result:** some services may have almost no valid hiding place. For example, Slack lists channels whole
  and its search spans every channel. Saying so, with the evidence, answers the question for that service.
