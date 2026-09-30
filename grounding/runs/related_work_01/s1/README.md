# S1: our several-match shortcut check, on Agent-Diff's own plural requests

*related_work_01, 2026-09-30, for the lead. The arm S1 of [report.md](../report.md) §5.3: the status quo's seeds, as
they are, put through the shortcut check our automation runs, plus a check of whether Agent-Diff's assertions notice a
target left out. No model calls. Run from the repository root with the backend interpreter
(`grounding/runs/fact_coverage_02/launch.py`).*

## What it produces

- [checks.json](checks.json): for each plural request, every route of its kind's route table (the lazy shortcuts
  and the complete routes of [several_match_02/strategies.py](../../several_match_02/strategies.py)), run as API calls
  on a fresh environment of Agent-Diff's shared seed (slack_bench_v2, box_default, linear_expanded). A route that
  misses a target is **defeated**. Each route carries its behaviour from
  [route_table.py](../../several_match_02/route_table.py): scope, pages, visibility, filter or selection.
- [omissions.json](omissions.json): for each target, whether the test's own assertions would fail a trial that left
  it out, reviewed by hand against the assertion engine's count rules.
- [summary.json](summary.json): both, set beside our automation's numbers
  ([several_match_auto_01](../../several_match_auto_01/report.md)).

## Which requests: all 60 plural obligations, accounted for

The report's plan used the suite's "multi-entity" label as a proxy. The obligation cards name the plural obligations
directly: **60** resolved obligations in Slack, Box and Linear have two or more targets. Calendar is out: its tests
have no cards yet.

| Bucket | Obligations | Why |
|---|---:|---|
| **Probed** | **23**, plus **3** with the same targets, words and kind (slack_77, slack_113, box_163) | The request needs every target, and its kind has a route table |
| Run, not counted | 2 (slack_107 O4, slack_109 O6) | Permissive by their cards ("whatever you can dig up"): missing some is not a failure |
| Left out | 6 | Pick one (box_118 "the first file found", slack_112 O3, linear_54 O5); a delegated judgment (slack_100); a permissive source (slack_108 O8); a card that counts a whole channel's history as the targets (slack_92) |
| No route table | 26 | Sets of people (17), teams (2), hubs (2), tasks (1), a thread's replies (1), comments and issues found through them (2), issues reached through a relation (1) |

The parameters of each probe follow stated rules ([probes.py](probes.py)): search words are the request's own words,
punctuation is not a word, and alternatives the request names are each searched and combined. Linear's "all
conditions" filter carries every condition the request states. When no team is named, the team routes guess the first
target's team, as the Box "anywhere" routes guess its folder.

## Result 1: which shortcuts the seeds defeat

**Agent-Diff's seeds defeat 3 of the 15 practical lazy shortcuts our automation defeats on these three services.**
The automation defeats all 19, including Calendar's four. The comparable measure is the one the automation reports:
a shortcut counts when some request's seed defeats it.

| Request kind | Practical shortcuts | Defeated on Agent-Diff's seeds | Where |
|---|---:|---:|---|
| Box, files in a named folder | 4 | **1**: list the named folder, first page | 5 requests whose files sit in subfolders (below) |
| Box, files anywhere | 5 | 0 | (box_129, box_158) |
| Linear, issues | 1 | 0 | The whole workspace is 44 issues, under the default page of 50 |
| Slack, messages in a named channel | 3 | **2**: both word searches | slack_67: "lunch" is in 2 of the 4 lunch questions |
| Slack, channels | 2 | 0 | Every target channel is public |
| Calendar | 4 | – | No cards |
| **Total (checkable)** | **15** | **3** | |

- **By behaviour:** defeats come from scope (Box, 5 requests; the named folder holds the targets only in its
  subfolders) and filter (Slack, 1 request). **Pages and visibility never:** no target is past a default page, and none
  is behind a default visibility.
- **Two of the five Box scope defeats are explicit in the request:** box_143 ("from all subfolders") and box_151 ("and
  its subfolders"). The other three (box_127, box_139, box_150) rest on the card's recursive reading of "in the
  folder" or "in the area". Our automation treats a copy one folder down as contestable (its check 8: the cold reader
  left it out in 2 of 2 probes).
- **One more, outside the 19:** linear_32 ("Reassign all of John's urgent issues") names no team. Guessing the first
  target's team (Engineering) misses PROD-2 on all four team routes. The automation's requests all name the team, so it
  counts these routes as not lazy.
- **The complete route found every target in every counted probe**, except box_158's search route (below).

## Result 2: rows the replica cannot decide (void)

**The replica's Box search matches names and descriptions; Box's search also reads file content.** The gap is
already on record in [the Box model's source ledger](../../../domains/box/model_source_ledger.md), B-A10: "search does
not inspect file bytes". Five search rows in two requests are void:

- **box_158:** "Moog" is in all three targets' text and in none of their names. The complete search route missed all
  three. That is the check's own signal of a replica problem, and it is reported, not hidden.
- **box_139:** the replica finds 1 of 5 by name. "ethics" is in one more target's text, and the other three say
  "ethical". Whether Box matches those is not documented.

Box search rows whose words are in the file names stay (box_129, box_150, box_151, box_152, box_155). The replica
is not fixed (the standing rule). **For the lead:** Agent-Diff Box tests whose solvers rely on content search behave
differently on the replica than on Box.

## Result 3: what Agent-Diff's assertions notice when a target is left out

The question, per target: a trial does everything the test asks but leaves this one target out, and puts nothing in
its place. Does an assertion fail? The review applies the engine's count rules
(`evaluationEngine/assertion.py`): an integer count is exact, `min` is a lower bound, and no count means at least
one.

**Of 210 targets in the 26 counted obligations, 152 (72%) would go unnoticed.** Another 18 are noticed only by a
count, so a trial that substitutes a non-target passes. The remaining 40 are pinned by id or by text only they carry.
**17 of the 26 obligations have at least one unnoticed target.** Two large sets weigh heavily (box_127's 62 files,
box_143's 30). Without them, 60 of 118 targets go unnoticed.

| Obligation | Targets | Unnoticed | Cards' coverage | Why |
|---|---:|---:|---|---|
| slack_67 O1 | 4 | 2 | partial | Two of the lunch questions have no reaction check |
| slack_74 O1 | 8 | 4 | partial | Four keywords are checked, each in one question only |
| slack_75 O1, slack_76 O1, slack_77 O1 | 4, 6, 6 | 0 | partial | Each source message's fragment is checked |
| slack_106 O1 | 9 | 8 | partial | Only "general" is checked in the channel list |
| slack_108 O1 | 3 | 3 | no | Read-only: the answer is not checked |
| slack_110 O6 | 2 | 0 | partial | The count is checked, by a regex a stray "2" would also pass |
| slack_112 O1 | 11 | 11 | no | Read-only |
| slack_113 O1 | 11 | 2 | partial | The report's regex lists nine of the eleven channels |
| box_127 O2 | 62 | 62 | partial | Any non-empty description passes |
| box_129 O1, box_163 O2 | 4, 4 | 4, 4 | partial, no | At least one file moved; no check on the hub's items |
| box_139 O1 | 5 | 0 | yes | Each file's new name, by id |
| box_141 O1 | 8 | 0 | no | At least 8 hub items: noticed, but any eight files pass |
| box_143 O2 | 30 | 30 | no | No assertion on the moved files |
| box_150 O1 | 4 | 0 | partial | At least 4 hub items named fomc |
| box_151 O1, box_152 O1 | 5, 4 | 5, 4 | partial | At least one file changed, no count |
| box_155 O1 | 3 | 3 | no | At least two domain folders remain |
| box_158 O1 | 3 | 3 | no | Read-only |
| linear_32 O1 | 2 | 1 | partial | ENG-3 is checked, PROD-2 is not |
| linear_41 O1, O3, O5 | 4, 3, 2 | 0, 3, 0 | partial, partial, yes | Exact count of 4 labels; the rate's text is unchecked; SEED-7 and SEED-8 by identifier |
| linear_56 O2 | 3 | 3 | no | Read-only |

**How this differs from the cards' own coverage field:** the cards judge identity and fidelity too (a substitute, a
keyword-only summary). This audit asks only about omission. Six obligations the cards call partial notice every
omission (slack_75, slack_76, slack_77, slack_110, box_150, linear_41 O1). One the cards call uncovered notices it by a
count (box_141). The four read-only obligations are unchecked by construction, because Agent-Diff grades state, not
answers.

## What changed after the first run

The first run is committed as it was (2b4f3306a2). The review then made these changes, each by a rule stated in
[probes.py](probes.py) and not by a result:

- box_118 ("the first file found": pick one) was replaced by box_129, which has the same targets and asks for all.
- slack_107 O4 and slack_109 O6 are permissive, the criterion already used for slack_100: run, not counted.
- slack_74 searched "?"; punctuation is not a searchable word, so its search routes are not applicable.
- slack_108 searched "food"; the request names "food" or "eat", so both are searched and combined. Not defeated.
- box_143 searched one extension; the request names three, so all three are searched. An ordering fault in the check
  had also marked its extension route not applicable.
- Linear's "all conditions" filter carried only the team; it now carries each request's conditions.
- Three plural obligations the first selection missed were added: box_163 O2, linear_41 O3 and O5.
- The first run's omission count was mechanical (ids in `eq` or `in`, exact counts). It was wrong both ways: it
  missed text, regex, identifier and minimum-count pins, and counted ids that belong to other obligations. It said
  202 of 224. The hand review replaced it.

## What a later session would run, and the cost

**Nothing more for S1:** it needs no model and no decision, and the commands below rerun it in about an hour on the
backend.

The behavioural question is whether an agent takes these shortcuts on Agent-Diff's requests. That is part of the
projection runs (report §4.4, 672 trials), which include these tests. S1 tells those runs where a shortcut can show at
all: only in the 7 obligations with a faithful defeat (box_127, box_139, box_143, box_150, box_151, slack_67,
linear_32). Everywhere else, a lazy agent and a thorough one end with the same targets.

```bash
PY=/home/yusf/PyProj/agent-diff/backend/.venv/bin/python
$PY grounding/runs/fact_coverage_02/launch.py grounding.runs.related_work_01.s1.check     # [TEST ...]
$PY -m grounding.runs.related_work_01.s1.omissions
$PY grounding/runs/fact_coverage_02/launch.py grounding.runs.related_work_01.s1.summary
```

## Files

| Path | What |
|---|---|
| [probes.py](probes.py) | The 60 plural obligations in their buckets, each probe's parameters, the void rows and the changes after the first run |
| [check.py](check.py), [checks.json](checks.json) | The shortcut check and its results |
| [omissions.py](omissions.py), [omissions.json](omissions.json) | The omission review, by hand, per target |
| [summary.py](summary.py), [summary.json](summary.json) | The numbers above, beside the automation's |
| [routes.py](routes.py) | Prints the route tables |
