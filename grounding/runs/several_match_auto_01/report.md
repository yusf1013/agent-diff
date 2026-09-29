# several_match_auto_01: automating the several-match method (phases 2 and 3)

*2026-09-28, overnight. The method is [../several_match_02/method.md](../several_match_02/method.md) (version 1.1),
made by hand in the manual investigation. Here Muse (`muse-spark-1.3-contributor`) does the creative steps, code does
the rest, and the self-hosted Qwen is the instrument. Numbers marked [pending] are filled as the runs finish.*

## The pipeline

| Step | Who | What |
|---|---|---|
| Population | code | 91 single-target covers: fact_coverage_02's hand-built covers, autogen_01's 49 generated scenarios, autogen_02's 28 ([population.py](population.py)) |
| Plural request | Muse writer (one call per service) | plural-worthy or not, with the reason; the plural wording; the words a user would search with; three texts for the extra matches ([writer.py](writer.py)) |
| Wording check | code | no hiding place the original did not name |
| Easy tier | code | the target plus two copies in plain view ([build.py](build.py), [seedkit.py](seedkit.py)) |
| Hard tier | code | one trap per laziness behaviour that applies. Whether the request pins its container (a channel, calendar, folder or team) comes from the reference query |
| Checks | code | the reference query selects exactly the targets and every near-miss claim still holds (fdc); no container over 200 records; every target's date the same in UTC and Los Angeles |
| Cold reader | Muse, a fresh session per case | reads the request and every record of the kind, with containers and visibility, and must pick exactly the targets ([reader.py](reader.py)) |
| Shortcut check | code, on the replica | every shortcut of the request's kind run on the hard seed; the thorough route must find every target ([checks.py](checks.py)) |
| Runs | self-hosted Qwen, 3 trials | [runs/p3](runs/p3) |
| Judge | code | acted-on set against the targets; misses by placement; near misses acted on by fact ([grade.py](grade.py)) |

## Phase 2: does the automation meet the manual standard?

On the four covers of the manual cycle 8, the automated hard cases defeat the same shortcuts:

| Cover | Automated | Manual (cycle 8) |
|---|---:|---:|
| CAL-23 | 4 of 4 | 4 of 4 |
| BOX-23 | 4 of 5 | 4 of 5 |
| LIN-21 | 1 of 6 | 1 of 6 |
| SLK-21 | 3 of 8 | 3 of 8 |

The writer's plural wordings of those four are the manual ones in substance ("Delete all of Friday's architecture
reviews that Kenji Sato … attends as an optional guest"). The cold reader's verdicts on them: [pending].

## Phase 3: the numbers

[pending: coverage space; tests generated; coverage reached; valid tests; distinct failures exposed; judge true and
false positives (false negatives from a sample); tokens and costs]

## Files

- [population.py](population.py) → `population.json`; [writer.py](writer.py) → `writer.json`;
  [build.py](build.py) → `cases/`, `build.json`, `placements.json`; [reader.py](reader.py) → `reader.json`;
  [checks.py](checks.py) → `checks.json`; [grade.py](grade.py) → `grades.json`.
- Muse calls: `runs/calls.jsonl` and `runs/writer/`, `runs/reader/` (prompts, transcripts, usage).
- Solver runs: `runs/p3` (and `runs/smoke`, the first end-to-end trial).
