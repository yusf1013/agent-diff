# related_work_01: related work, baselines and the projection of established suites

A reading, searching and analysis study for the lead session ("RoadMap specialist"), started 2026-09-30 from the
brief [related_work.md](../../protocols/briefs/related_work.md). Branch `exp/related_work-01`, worktree
`.claude/worktrees/related_work`. No model runs; no Muse spend. It does not edit the roadmap, the notes file,
report_01, other studies, the replicas or the frozen pipeline.

## Status

- **Date:** 2026-09-30.
- **Done:** the deliverable, [report.md](report.md): the map (12 angles, 6 new), cards for 69 works in 35 blocks, the verdict table, two
  pilots on existing evidence (no model calls), the projection plan (Agent-Diff first; the ClawEnvKit arm sized), the
  proposals for the policy, several-match and boundary baselines. [claims.md](claims.md) quotes every claim about
  another work with its source and fetch date.
- **Phase 2 (the lead's assignment, no model calls): the four arms that need no decision.**
  - Done: [P1](p1/README.md), 350 runnable mutated variants; [B2](b2/README.md), the abstention suites projected;
    [S1](s1/README.md), the shortcut check and the omission review on Agent-Diff's seeds.
  - In progress: B1 (mask an operation).
- **Running:** nothing.
- **Blocked:** nothing. Running any arm waits for the PI's decision on budget.

## The investigation question

How can we place our fact-discrimination tests among the lines of work that test or benchmark tool-using agents, so
that every work a reviewer might take for a baseline at first glance is either run as one or explained away with a
stated reason? Three parts, from the brief:

1. **The map and the verdicts.** What lines of work exist, where do they overlap with ours, what do we do that they
   cannot, and which can serve as a baseline (and how)?
2. **The projection.** How can an established suite be projected onto our coverage space, the way the AgentDiff
   analysis was: how much of our space its tests cover; of the part they do not cover, how many failures our tests
   expose; of the part they do cover, how many failures their own assertions miss; and whether our generation
   exposes more in the same space?
3. **The missing baselines.** How can the policy tests, several-match tests and capability-boundary tests get fair
   baselines?

## Verdict vocabulary

Every card ends in exactly one verdict:

| Verdict | Meaning |
|---|---|
| **Run** | A generator we could run on our four services as a baseline arm, with a plan and a cost |
| **Project** | An established suite whose tests and checks we project onto our coverage space (a status-quo row) |
| **Adopt** | A judge or oracle design we compare our judge against |
| **Explain away** | Not a baseline, for a stated reason class: a different object under test; no seeded state; an oracle that cannot observe the fact; not released; a training reward, not test adequacy |

## Layout

| Path | What |
|---|---|
| [report.md](report.md) | The deliverable: the map, the cards, the verdict table, the projection plan, the baseline proposals |
| [bibliography.md](bibliography.md) | Every work cited, with links |
| [log.md](log.md) | The cycle log: what was read or checked, what was learned |
| [claims.md](claims.md) | Every claim about another work, quoted from its source, with the fetch date |
| [pilot/](pilot/) | The two pilots on existing evidence (scripts and outputs) and the claims builder |
