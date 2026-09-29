# several_match_01: does the agent find every match, and only the matches? (roadmap step 5, second investigation)

*Pre-registered 2026-09-27 23:05 EDT, before any scenario is built or run. Changes after this point are dated
amendments below.*

## The question

When a request asks to act on every record that meets its conditions, does the agent act on all of them and on
nothing else? The PI asked for at least three matches, and for reuse of what is already known about where matches
get missed.

## What is already known about misses

- **The agent stops at the first candidate in view.** The fact_coverage_02 hidden-target study (report §12.3) found
  this:
  - Qwen acted on a decoy in 5 of 12 trials when the decoy came back without the target, against 5 of 113 when the
    two came back together;
  - with an escape clause, it answered "none" without searching further (6 of 6).
- **Easy paths.** `fact_coverage_02/hiding.py` models the natural first queries from what a request names. A record
  off every easy path is reached only by a second query.
- **Retrieval paths that return a subset:**
  - a folder listing shows only direct children;
  - a calendar query covers one calendar;
  - search matches names and descriptions only;
  - listings are paged. The replicas page like the real services: Box search 30, Box listings 100, Slack 100,
    Linear issues 50, Calendar events 250.
- **Underspecified tests (autogen_02).** When several records fit a singular request, Qwen acted on one and asked
  "which one" once in 435 trials. A plural request asks it to act on all of them instead.

## Design

**Scenarios.** About 8 hand-written scenarios in the kit's format (`autogen_01/kit/docs/format.md`), with
`"answer": "all"`: 2 each for Box, Calendar, Linear and Slack.
- Each has 3 to 5 targets and 2 or 3 near misses.
- Each near miss fails exactly one condition, checked mechanically by the kit's claim check.
- Each request uses "every" or "all" and names its scope explicitly, so that a target outside the easy path is still
  in scope by the request's own words. A missed target must be a real mistake, and so must a near miss acted on.

**Placement of each target:**

| Class | Meaning | Example |
|---|---|---|
| V, visible | Returned by the natural first query from what the request names | a file in the named folder |
| C, another container in scope | In a container the request's scope includes, but not the one it names first | a subfolder of the named folder ("including its subfolders"); a secondary calendar ("on any of my calendars") |
| P, beyond the first page | Returned only after paging the natural listing | the 51st issue |
| F, a condition search cannot see | Its qualifying condition is readable only in a per-record detail read | a tag or comment count in Box; a reaction in Slack |

Every scenario has at least 2 V targets and at least 1 target of another class. Near misses are placed visibly.

**Validity and replica checks.** These run before any agent does:
- the kit's `scenario.build` (format, seed, reference query, claim witnesses, anchors, replica rules, lint);
- `preflight.check`: reads, observability, and write feasibility on one target;
- each non-V placement is reachable through a replica path that behaves like the real service. No replica gap may
  decide the placement: no ignored filter, failing query or unreadable field (`autogen_02/inputs/<domain>/replica.md`).

**Runs.** Cover tests only (all targets and near misses present), 3 trials each, on the self-hosted Qwen:
- `SOLVER_BACKEND=selfhost`;
- at most 12 in flight;
- the shared limiter;
- the agent clock.

The near-miss probes of these scenarios test rejection, which the main suites already measure; they are not run.

## Measures (graded by hand from the diff, the final answer and the trajectory)

- **Per trial:**
  - the acted-on set against the target set: exact, incomplete (a subset of the targets), over-inclusive (a near
    miss acted on), or both;
  - whether it asked instead of acting.
- **Per target class:** recall (acted-on targets / targets) for V, C, P and F.
- **Precision:** targets acted on / records acted on.
- **Per miss, the mechanism:**
  - never retrieved (the path was not taken);
  - retrieved but rejected (misread);
  - retrieved and overlooked.

  This is read from the first appearance of each id in what the agent saw (as in `hiding.py`'s `first_seen`).
- The judge is not used for grading. Judge v2 may be run afterwards to compare with the hand grades, reported
  separately.

## What would count as a finding

- **Recall on C, P or F well below recall on V** (for example, 20 points or more, pooled) would show that the agent's
  search depth, not its reading, decides completeness.
- **Exact sets in most trials** would show that plural requests are not a weakness for this agent. That is a valid
  outcome.
- **Near misses acted on more often than in the singular covers** would show that a plural request loosens its
  discrimination.

With about 24 trials, the results are descriptive; no significance test is planned.

## Cost

- The self-host only: no Purdue and no Muse.
- Judge v2 afterwards is optional, at about $0.04 per trial at list.
