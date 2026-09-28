# several_match_01: does the agent find every match, and only the matches? (report)

*Roadmap step 5, second investigation. Plan: [plan.md](plan.md), pre-registered 2026-09-27 23:05 EDT. Written
2026-09-28. Solver: the self-hosted Qwen3.8-27B (`SOLVER_BACKEND=selfhost`), 3 trials per test, the agent clock.*

## The answer in brief

- **Plural requests are not a weakness for this agent in these scenarios.**
  - 22 of 24 trials acted on exactly the target set.
  - No near miss was acted on in 72 chances (3 near misses × 24 trials), including the sibling-role near misses
    (creator for owner, creator for assignee) that Qwen often accepts in singular probes.
- **The one real miss was pagination.**
  - In one of three SM-LIN-01 trials, the agent listed Linear issues without a filter at the default page size
    (50). It acted on the two targets on that page and never saw the two on the next.
  - It then stated that no other matching issue existed.
  - In every other trial it avoided paging, by asking for large pages (`limit=1000`, `limit=999`) or by
    filtering on the server (search, or Linear's team and assignee filters).
- **One trial did nothing, for a harness reason.**
  - In SM-CAL-01 t3 the agent wrote Python scripts that call curl through `subprocess`.
  - The executor rewrites API URLs only in its bash-level `curl` function, so those calls bypassed the proxy and
    returned nothing.
  - The agent's own time budget ran out after 5 steps.
  - This is the only trial, out of about 2,360 recorded trials in this and the earlier studies, whose agent called
    the API from a script.

## Results ([grades.json](grades.json), [grade.py](grade.py))

| Placement class | Targets acted on |
|---|---|
| V, visible on the natural first query | 52/54 (52/52 without the harness trial) |
| C, another container in scope (subfolders, other owned calendars, sub-teams) | 22/24 (22/22) |
| P, beyond the first page of the natural listing | 16/18 |

| Scenario | t1 | t2 | t3 |
|---|---|---|---|
| SM-BOX-01 (subfolders) | exact | exact | exact |
| SM-BOX-02 (116-file folder) | exact | exact | exact |
| SM-CAL-01 (owned calendars) | exact | exact | nothing (harness) |
| SM-CAL-02 (required attendee, owned calendars) | exact | exact | exact |
| SM-LIN-01 (70-issue team) | incomplete (pagination) | exact | exact |
| SM-LIN-02 (sub-teams) | exact | exact | exact |
| SM-SLK-01 (140-message history) | exact | exact | exact |
| SM-SLK-02 (channels by name prefix) | exact | exact | exact |

**Against the plan's criteria:**
- **Recall on C or P 20 points or more below V:** not met. P is 11 points below V (16/18 against 52/52), all from
  one trial.
- **Exact sets in most trials:** met (22 of 24).
- **Near misses acted on more often than in singular covers:** not met; none was acted on.

## What this suggests (hypotheses, not findings)

- **A plural request may make the agent check every candidate.** The sibling-role near misses were read correctly
  every time here. Qwen accepts such near misses in singular probes. A matched test, the same near miss under a
  singular and a plural request, would tell whether the framing matters.
- **The form discriminates only where the retrieval route can hide a match.**
  - Here that is the default page with no filter.
  - Qwen usually defeats it with large pages, so the placement class should be judged against the route the agent
    actually took (as `hiding.py` does), not the seed alone.
  - A harder form needs matches that no single query returns. Examples: a condition only a per-record detail read
    shows, across more candidates than one listing holds; or more than about 10 matches.
- **A false completeness claim follows a miss.** In the LIN-01 miss, the answer names what it did and asserts that
  nothing else matches. A plural test catches this without the judge: the diff shows the missing targets.

## Validity

- All 8 scenarios pass the kit's `scenario.build` checks and `preflight.check` ([checks/](checks/)):
  - reads, observability, and write feasibility on one target;
  - each near miss fails exactly one condition (the claim check).
- **Placement holds on the seed.**
  - SM-BOX-02's default listing returns 100 of 116 files, without the two late targets.
  - Slack history is newest first, so SM-SLK-01's two oldest targets are beyond the first 100.
  - SM-LIN-01's targets sit at both ends of creation order, so two are off the first 50 whichever way the listing
    runs.
- **The F class (a condition search cannot see) was dropped** before building. In these replicas every such
  condition (comments, tags) is one the real service can search; the replica ignores the filter. So it would be a
  replica gap, which the plan's validity rule excludes.
- **SM-SLK-02 has no non-visible target.** Slack lists channels whole and its search spans every channel
  (fact_coverage_02 §12.3: "Slack had no layout that passes"). It tests completeness across three containers, all
  visible.

## Files

- [scenarios.py](scenarios.py) → scenarios/ and [placements.json](placements.json).
- [build.py](build.py) → cases/ and checks/.
- runs/smoke (1 trial) and runs/main (24 trials), with the run log runs/main.log.
- [grade.py](grade.py) → [grades.json](grades.json).

## Cost

- The self-host only: 24 trials plus 1 smoke trial; no Purdue and no Muse.
- The replica checks ran locally.
