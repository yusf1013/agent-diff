# completion_01: the remaining briefs (roadmap 6b)

Roadmap step 6b ([roadmap](../../protocols/roadmap.md)): generate the scenarios the servable space still lacks, so
that OpenClaw's evaluation ([openclaw_eval_01](../openclaw_eval_01/README.md)) covers it whole.

| Path | What |
|---|---|
| [inputs/briefs_6b.json](inputs/briefs_6b.json) | 26 briefs, 74 facts: the servable facts no evaluated scenario covers (autogen_02's count: 54 + 8 + 12) |
| [generate.py](generate.py) | Phase 4's generator, unchanged, on these briefs |
| `runs/gen_01/` | The generation run |

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

## How the suite is built

As 6a's after the discussion of 2026-09-28: the generator is unchanged and the writer is asked about neither ids nor
dates. When the suite is built, every test gets opaque ids (`autogen_01/kit/opaque_ids.py`, with the same checks as
`openclaw_eval_01/opaque_suite.py`) and a test-side clock: the day its scenario was written, or a later day if its
data has an event after it (Calendar keeps its 2018 day). Every accepted scenario gets my validity review before any
run, and every Muse-written policy variant a manual read.
