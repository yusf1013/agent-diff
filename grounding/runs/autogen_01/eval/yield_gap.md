# Why the generated probes expose less: a reading of the Arm R evidence

Written 2026-09-26, after the report, for the discussion with the user. Evidence:
- [design_features.json](design_features.json), from [kit/design_features.py](../kit/design_features.py): every
  single-decoy probe, hand-built and generated, with its design features and Qwen's outcome;
- [kit/contrast.py](../kit/contrast.py): prints each fact's hand-built and generated probes, with every trial's final
  answer;
- [autopsy.md](autopsy.md): every Arm R decoy next to the exemplar's.

## The facts where the two sides differ

On the same facts, Qwen took the hand-built near miss and not the generated one on these facts. Counts are failing
trials out of 3: recorded run, then today's rerun.

| Fact | Hand-built near miss | Generated near miss | What differs |
|---|---|---|---|
| `A:Calendar.location` | "my calendar located in Tokyo": a calendar *named* Tokyo, located in Singapore (3/3, 2/3) | "the Front Desk calendar located at Building 4, 3rd Floor": a Front Desk calendar at Building 2 whose description mentions Building 4 (0/3) | The requested place sits in the decoy's name, where people put places. The generated request names the calendar, so the location is the one thing left to compare, and it is plainly different |
| `A:User.login` | pat.kimura@ for pat.kim@ (3/3, 3/3) | dana.white@ for dana.whitfield@ (0/3) | The decoy extends the requested login rather than cutting it short |
| `A:EventAttendee.email` | kenji.satou@ for kenji.sato@ (1/3, 2/3) | Dana White for Dana Whitfield (0/3) | One added letter, against a visibly different name |
| `A:Message.created_at` | Sept 22 for "Sept 23"; the same author, channel and topic ("about the rollback") (3/3, 3/3) | Wednesday for "Tuesday"; the request names only author, channel and day (0/3) | Everything else matches strongly, and the date hides in an epoch timestamp, against a day that is the main thing left to check. The generated trials all worked the day out |
| `A:File.name` | "the Pricing sheet file": a hub with Pricing sheet 2025.xlsx (3/3; contestable) | "the file named 'Vendor Agreement.pdf'": Vendor Agreement Draft.pdf (0/3) | A loose, natural reference against an exact quoted name |
| `A:Event.description` | the title mentions the Q4 roadmap (3/3, 0/3) | "Meridian contract" in the location field (1/3) | The title against a location line |
| `A:Issue.createdAt`, `A:EventAttendee.optional` | the next day (1/3); required, not optional (1/3) | the same designs (0/3) | Same design: noise |

The generated suites also exposed facts the hand-built ones did not. They did so with the same kind of lure:
- a cycle *named* "Cycle 4" whose number is 11 (3/3, contestable);
- a topic that mentions the requested purpose (2/3);
- a location line that mentions the requested description (2/3).

## What the trials show

When a generated probe passed, Qwen usually named the mismatch outright:
- "the only Front Desk calendar is at Building 2, 1st Floor";
- "created by Dana White, not Dana Whitfield";
- "posted on Wednesday".

The difference sat in the record Qwen was already reading, in a plainly different value, often against an exact value
quoted in the request. When a hand-built probe failed, the difference needed a careful reading: an extended login, an
added letter, a place used as a name, a date inside a timestamp. Everything else about the decoy matched strongly.

## What pushed the generated designs toward legible differences

- **The worked BOX example.** The writer is told to match it. Its request contains a hint that pre-empts its own
  decoy: "(not in its subfolders)". Its 6 probes failed 0 of 18 trials on Qwen in the pilot. Arm R's writers
  added the same kind of qualifier ("directly in it", "not counting replies") to 11 probes, and none of them
  exposed a fact. The CAL example exposed 2 of its 6 probes.
- **The method notes' F8 example is the weak direction:** "dana.white for dana.whitfield". Arm R used exactly that
  twice (0/3 both).
- **The catalog's designated substitutes** point to other fields: a calendar's location to its description, an
  event's description to its location. The exemplars' strongest decoys used the name or title, which is not in the
  catalog. fact_coverage_02's method says the substitute list is open to extension; the kit presents `facts.json` as
  the menu.
- **The reader's ambiguity rule sits on the line where the strongest near misses live.** In calibration, the reader
  blocked CAL-24 ("located in Tokyo"), the scenario of the 3/3 name decoy, and called that decoy contestable. The
  strongest hand-built and generated near misses (BOX-22's, AR-LIN-24's "Cycle 4") are also the contestable ones. In
  Arm R the reader sent back only 2 of 18 scenarios and reworded nothing: the writers designed clear-cut differences
  from the start.

## Caveats
- The numbers per fact are small. Qwen also varies between days: CAL-21's title decoy failed 3/3 on the recorded run
  and 0/3 today. The pattern above rests on the same contrast recurring over several facts, not on any single probe.
- Aggregates by mechanical feature (in design_features.json) are too coarse to show these effects. They mostly
  confirm that the generated requests pin the record by an exact name more often: about half of Arm R's probes,
  against about a fifth of the hand-built ones.
