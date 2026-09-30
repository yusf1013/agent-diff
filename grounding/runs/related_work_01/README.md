# related_work_01: related work, baselines and the projection of established suites

A reading, searching and analysis study for the lead session ("RoadMap specialist"), started 2026-09-30 from the
brief [related_work.md](../../protocols/briefs/related_work.md). Branch `exp/related_work-01`, worktree
`.claude/worktrees/related_work`. No model runs; no Muse spend. It does not edit the roadmap, the notes file,
report_01, other studies, the replicas or the frozen pipeline.

## Status

- **Date:** 2026-09-30.
- **Done:** orientation (the brief, the PI's notes, the roadmap, the concise report, the criterion, the AgentDiff
  obligation analysis, baselines_01, the step-5 spaces, the PI's earlier baseline audits in
  `~/PyProj/baseline_study/`, the PI's MCP-Bench runs in `~/PyProj/mcp-bench/`, the survey arXiv 2606.12191,
  EnvScaler).
- **Running:** the literature search and the cards.
- **Blocked:** nothing.

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
