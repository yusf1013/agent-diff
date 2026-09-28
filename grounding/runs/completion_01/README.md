# completion_01: the remaining briefs (roadmap 6b)

Roadmap step 6b ([roadmap](../../protocols/roadmap.md)): generate the scenarios the servable space still lacks, so
that OpenClaw's evaluation ([openclaw_eval_01](../openclaw_eval_01/README.md)) covers it whole.

| Path | What |
|---|---|
| [inputs/briefs_6b.json](inputs/briefs_6b.json) | 26 briefs, 74 facts: the servable facts no evaluated scenario covers (autogen_02's count: 54 + 8 + 12) |
| [generate.py](generate.py) | Phase 4's generator, unchanged, on these briefs |
| `runs/gen_01/`, `runs/gen_02/` | The generation run and its retry of the briefs Muse's outage stopped |
| [eval/review.json](eval/review.json) | My validity review of every accepted scenario |
| [suite.py](suite.py), `suite/` | The suite: the accepted scenarios' tests with opaque ids and clocks |
| [policy_units.py](policy_units.py), `suite/units/` | The policy units (absence twins; drop-F variants once derived) |
| [variants.py](variants.py), `runs/dropf_01/` | autogen_02's drop-F derivation on these scenarios |

## The briefs

- **19 Phase 4 briefs never generated** (orders 33 to 51; the run was cut to 32 for time): Box 6, Calendar 1,
  Linear 12. 54 facts.
- **3 Phase 4 briefs with no accepted scenario,** generated again: G4-CAL-08 (the generation failed), G4-BOX-02 and
  G4-LIN-03 (rejected). 8 facts. Phase 4's records of the first attempts stay in autogen_02.
- **4 new briefs** (G4-BOX-15, G4-CAL-10, G4-LIN-21, G4-SLK-09) for the 12 facts of autogen_01's development briefs
  (DV-BOX-01, DV-CAL-01, DV-LIN-01, DV-SLK-01). Their scenarios were accepted in the second development round
  (`autogen_01/runs/gen_dev_02`), so the replicas serve these facts; they were used to develop the method and so
  never counted as coverage. Phase 4 drew only facts no autogen_01 brief had used, which left these 12 out.

## The generation run (`runs/gen_01`, 2026-09-28)

- **16 accepted:** G4-BOX-02, 09, 11, 12, 13, 14; G4-CAL-09; G4-LIN-09, 10, 11, 12, 13, 15, 16, 17, 19.
- **2 rejected** by the cold reader after 3 rounds: G4-BOX-10, G4-LIN-18.
- **8 not generated:** from about 19:14 UTC Muse refused every call with HTTP 402 (payment required), so the writer
  of G4-BOX-15, G4-CAL-08, G4-CAL-10, G4-LIN-03, G4-LIN-14, G4-LIN-20, G4-LIN-21 and G4-SLK-09 never ran to the end.
  These are infrastructure failures, to be generated once Muse answers again, not failed briefs.
- **Cost:** 127 Muse calls, $13.32 at list price, $0.75 billed.
- **My validity review** ([eval/review.json](eval/review.json)) of the 16 accepted scenarios: 14 valid, 2 weak but
  valid (contrived: G4-LIN-12's five users named Rae Ellison; G4-LIN-16's "the active human admin"). Two rulings
  are borderline and flagged for the PI: G4-LIN-15's two sub-team near misses (an issue of Platform Mobile, a
  sub-team of Platform, is not "in the Platform team", though Linear shows sub-team issues in the parent's views),
  ruled as G4-LIN-11's Delta near miss (owning the parent team is not owning its sub-team).

## The retry (`runs/gen_02`, 2026-09-28)

- **The 8 briefs Muse's outage stopped,** generated again by the same generator once Muse answered (`--run-name
  gen_02`): **7 accepted** (G4-BOX-15, G4-CAL-08, G4-CAL-10, G4-LIN-14, G4-LIN-20, G4-LIN-21, G4-SLK-09); G4-LIN-03
  **rejected** after 7 versions, as in Phase 4.
- **Cost:** 50 Muse calls, $5.51 at list price, $0.32 billed.
- **In all, 23 of the 26 briefs have an accepted scenario;** 3 were rejected (G4-BOX-10, G4-LIN-18, G4-LIN-03).
- **My validity review of the 7:** all valid, G4-LIN-21 on its clock ("next milestone" depends on today). One near
  miss is flawed: G4-CAL-10's `ev_sprint_fakelink` (group B: "the sprint review with a video link" naturally takes
  in an event whose description holds a Meet link), recorded in `roadmap_01/known_defects.json`; the test and the
  absence unit that hold it are left out. Flagged for the PI with it: G4-CAL-10's `ev_sprint_oak`, borderline and
  ruled valid (Oak Room is the booked room resource; Maple Room is only location text).

## How the suite is built

As 6a's after the discussion of 2026-09-28: the generator is unchanged and the writer is asked about neither ids nor
dates. When the suite is built, every test gets opaque ids (`autogen_01/kit/opaque_ids.py`, with the same checks as
`openclaw_eval_01/opaque_suite.py`) and a test-side clock: the day its scenario was written, or a later day if its
data has an event after it (Calendar keeps its 2018 day). Every accepted scenario gets my validity review before any
run, and every Muse-written policy variant a manual read.

## The suite and the units (2026-09-28)

- **137 tests from the 23 scenarios** (`suite/cases`); the derivation dropped P-G4-BOX-13-I12, whose witness does
  not change its probe's outcome. 463 ids were replaced by opaque ones.
- **69 absence units** (`suite/units.json`); AT-G4-BOX-13-I12 is excluded by the derivation for the same reason.
- **On OpenClaw** ([openclaw_eval_01](../openclaw_eval_01/README.md)), after 6a's re-run: the 136 tests the rulings
  keep (`runs/full_04_cases`) and the 68 absence units they keep (`runs/policy/population_6b_absence`), 3 trials
  each. The blind samples, 30 trials each (seeds 5308 and 5309), were drawn before the runs; they replace the first
  draws (seeds 5306 and 5307, over gen_01's 16 scenarios), which were never used.
- **Underspecified units** come from the drop-F derivation (`variants.py`, `runs/dropf_01`), each accepted variant
  read by me before it runs.
