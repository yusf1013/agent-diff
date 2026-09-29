# several_match_auto_01: automating the several-match method (phases 2 and 3)

*2026-09-28/29, overnight. The method is [../several_match_02/method.md](../several_match_02/method.md) (version
1.1), made by hand in the manual investigation. Here Muse (`muse-spark-1.3-contributor`) does the creative steps,
code does the rest, and the self-hosted Qwen is the instrument. Numbers from [summary.py](summary.py) →
`summary.json`, after every batch was graded.*

## The numbers the PI asked for

| | |
|---|---|
| **The coverage space** | The method's requirement space: the laziness behaviours (stopping early, and falling short on scope, pages, visibility, filter or selection), instantiated as **shortcuts** on each service's route table per kind of request. The population's plural-worthy requests fall in **6 request kinds with a route table, 33 shortcuts** (the manual found 30 over its kinds; see below). Of the 33, **19 are lazy and practical to defeat**; 9 need more records than the replicas hold practically (a page of 250 to 1,000, a crowd over 200) and 5 are not lazy for these requests. Stopping early applies to every plural request. |
| **Covers** | 91 single-target cover scenarios (the fact method's hand covers and autogen_01/02's generated ones). The writer judged **65 plural-worthy**; 26 name one record by nature (an exact title, a superlative, a rename to one name). 16 of the 65 are record kinds with no route table (Box folders, calendars, Linear comments and projects, a Box task, a Slack user) or a pinned calendar (a page trap would need 250 events): they get the easy tier only. |
| **Tests generated automatically** | [pending] |
| **Coverage reached** | [pending] |
| **Valid** | [pending] |
| **Distinct failures exposed** | [pending] |
| **The judge** | [pending] |
| **Tokens and cost** | [pending] |

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
| Repair | code, then the reader again | a case the reader disagrees with is rebuilt with the original texts; if it still disagrees, without the traps it doubted |
| Shortcut check | code, on the replica | every shortcut of the request's kind run on the hard seed; the thorough route must find every target ([checks.py](checks.py)) |
| Runs | self-hosted Qwen, 3 trials | [runs/p3](runs/p3), repairs [runs/p3r](runs/p3r), iteration 2 [runs/p3c](runs/p3c) |
| Judge | code | the set acted on against the targets; misses by placement; near misses acted on by fact ([grade.py](grade.py)) |
| Review | code and me | every reported failure against its ground ([review_verdicts.py](review_verdicts.py)); every pass for changes outside the target table ([side_effects.py](side_effects.py)) and for the value written ([effects.py](effects.py)) |

**Two iterations.** The first round's coverage table showed two construction gaps: requests about Box files in a named
folder got only a search crowd (5 of 6 covers had no hard case), and Slack requests about channels got no trap.
Iteration 2 (`build.py --iterate2`) added a copy past the named folder's first 100 items, and a copy as a private
channel the actor belongs to. All 8 new cases passed the checks and the reader.

## Phase 2: does the automation meet the manual standard?

[pending]

## Phase 3: what the tests found

[pending]

## Files

- [population.py](population.py) → `population.json`; [writer.py](writer.py) → `writer.json`;
  [build.py](build.py) → `cases/`, `build.json`, `placements.json`; [reader.py](reader.py) → `reader.json`;
  [checks.py](checks.py) → `checks.json`; [grade.py](grade.py) → `grades.json`;
  [review_verdicts.py](review_verdicts.py) → `review.json`; [side_effects.py](side_effects.py),
  [effects.py](effects.py) → `effects.json`; [pace.py](pace.py); [summary.py](summary.py) → `summary.json`.
- [probe_subfolder.py](probe_subfolder.py): a reader-only probe (`probes/`), not a test.
- Muse calls: `runs/calls.jsonl` and `runs/writer/`, `runs/reader/` (prompts, transcripts, usage).
- Solver runs: `runs/p3` (the first builds), `runs/p3r` (repairs), `runs/p3c` (iteration 2), `runs/smoke`.
