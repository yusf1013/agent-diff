# roadmap_02: step 3's fixes and the frozen version

Roadmap step 3 ([roadmap](../../protocols/roadmap.md)): the fixes agreed with the PI on 2026-09-27, checked by
rebuilding every generated suite, then frozen as git tag `grounding-freeze-01`. The final evaluation (step 6) runs
this version.

## What changed

| Fix | Where | Effect |
|---|---|---|
| **Probe-trap check at derivation** | [derive.py](../autogen_01/kit/derive.py) `suite_with_dropped`; [orchestrate.py](../autogen_01/kit/orchestrate.py) | A probe or fact probe whose near miss no longer fails exactly its fact once the target is gone is dropped, and recorded in the run's `suite_dropped.json`. The check always ran; its result was ignored. The writer still hears about every probe's missing anchors, dropped or not ([scenario.py](../autogen_01/kit/scenario.py)). |
| **The seed builders own their helpers** | [seed_linear.py](../autogen_01/kit/seed_linear.py), [seed_slack.py](../autogen_01/kit/seed_slack.py), [seedops.py](../autogen_01/kit/seedops.py) | The Linear and Slack `Seed` classes are copied verbatim from the pilot studies, so the kit imports no study's hand-made cases. |
| **Calendar time zones** | [seedops.py](../autogen_01/kit/seedops.py) `local_offset`, `CalendarSeed.op_event` | A timed event takes its calendar's time zone, with that zone's offset on its date. Before, every event got Los Angeles at −07:00. |
| **A date check** | [scenario.py](../autogen_01/kit/scenario.py) `_relative_dates` | Outside Calendar, a request with words relative to today ("overdue", "next week", ...) goes back to the writer. It applies to new generation. |
| **Known defects** | [loose_ends.py](../roadmap_01/loose_ends.py) → [known_defects.json](../roadmap_01/known_defects.json) | G4-BOX-05 kept (the PI's ruling). "Flawed but usable" is now "weak but valid". G4-CAL-06 is fixed in the rebuilt suite. The probes without a trap are dropped by the derivation. G4-LIN-02 is kept for runs up to 2026-09-30. The actions follow the decision "flawed is flawed". |
| **Documentation** | [kit README](../autogen_01/kit/README.md) | Notes for maintainers, which no agent reads: where "make the near miss tempting" came from, Slack's replica line about agents, the default near-miss people, the 9 scenarios that copied the examples, and Slack's bot in every channel. |
| **Tests** | [test_roadmap02_step3.py](../../tests/test_roadmap02_step3.py) | Offsets, the date check, a dropped probe, and G4-CAL-06's zones. |

No prompt, method note, example or domain input changed.

## The check before freezing

[rebuild_suites.py](rebuild_suites.py) rebuilds every accepted generated scenario from its last recorded version.
That covers 78 scenarios: autogen_01's arms R (18), P (15) and P v2 (16), and autogen_02's Phase 4 (29). It records
digests of each built case, seed and derived test, the dropped tests, and the build's problems. There are no model or
replica calls. Each fix was checked on its own against the snapshot before it:

| Fix | Differences from the snapshot before it |
|---|---|
| Helpers copied | none: 78 of 78 scenarios identical |
| Time zones | G4-CAL-06 only: its seed and its 8 tests. Its events now carry New York (−04:00), Chicago (−05:00) and Los Angeles (−07:00), following their calendars. |
| Probe-trap drop | exactly the 6 tests the [witness check](../roadmap_01/witness_check.json) had flagged: FP-AP-SLK-03-I12-I13, P-AP-SLK-03-I13, P-AP-SLK-05-I12 (arm P); FP-AP2-SLK-03-I13-I14, P-AP2-SLK-03-I14 (arm P v2); P-G4-LIN-01-I13 (Phase 4). The build's problems are unchanged. |
| Date check | new build problems for 2 accepted scenarios only. G4-LIN-02 ("overdue") is the known case. AR-SLK-22 ("tonight", in quoted message text) is a false positive. The check matters only for new generation. |

- **All fixes together:** 71 of 78 scenarios identical to before step 3. The 7 differences are exactly those above.
  [rebuild_before.json](rebuild_before.json) and [rebuild_frozen.json](rebuild_frozen.json) hold the snapshots.
- **The before-snapshot is verified.** Rebuilt from a copy of the committed kit before step 3 (commit 78dda24bf), it
  is byte-identical.
- **Suite sizes:** 444 regular tests before, 438 after (6 dropped).
- **The rebuilt G4-CAL-06 passes the replica pre-checks:** it installs, the deciding value of each of its 5 decoys
  can be observed, and the write acts on the target, which the replica returns at New York time.
- **One build problem predates step 3.** AP-SLK-05 (arm P) was accepted before derived tests were re-checked for a
  match. Its probe P-AP-SLK-05-I12 is the one the derivation now drops.

## What the freeze covers

- **Frozen:** the generation kit (prompts, method notes, examples, domain inputs, checks, seed builders, derivation)
  and judge v2, as of tag `grounding-freeze-01`.
- **Growing:** the known-defects list. By "flawed is flawed", a defect found later is added whenever it is found.
  Since the tag, each entry also says what the frozen suite does with it (`frozen_suite`).
- **Added on top for step 6:** integration code, such as the OpenClaw runner and its trajectory conversion. It changes
  how an agent is run, not how tests are made or judged.

Reproduce the check:

```bash
L="python grounding/runs/fact_coverage_02/launch.py"
$L grounding.runs.roadmap_02.rebuild_suites snapshot /tmp/rebuild_now.json
$L grounding.runs.roadmap_02.rebuild_suites compare grounding/runs/roadmap_02/rebuild_frozen.json /tmp/rebuild_now.json
```
