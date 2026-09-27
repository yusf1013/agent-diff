# Corrections to report.md (recorded 2026-09-24)

These corrections came up while the same cases were run on OpenClaw
([openclaw_transfer_01](../openclaw_transfer_01/report.md)). [report.md](report.md) and the run records are left as they
were; this file records what changes and why. **The failures are unaffected.** The 16 failing facts and the 16
requirement-level bugs (§7.8) stand. What changes is the evidence that some facts *held*: it comes from runs in which
the agent never saw the near-miss. Seven such runs also sit in one rate denominator (see [Rates](#rates)).

## 1. The Calendar replica hid the weekly series (CAL-02 family, CAL-11)

The replica's `events.list` gives `timeMin` a default: its fixed now, 2018-06-17 00:00 PDT
([methods.py](../../../backend/src/services/calendar/api/methods.py), `if not time_min`). It then filters every event by
its end time, and it treats a recurring series as ending when its *first* occurrence ends
([operations.py](../../../backend/src/services/calendar/database/operations.py), `list_events`). The pilot seeds start
these weekly series on 2018-05-01. So every list call without an explicit early `timeMin` returns neither the series nor
its occurrences. Only a call with `timeMin` before 1 May sees them.

| Run | What the agent saw | Effect on report.md |
|---|---|---|
| ALT-CAL-02-A-I12, trials 1 and 2 ([t1](pilot/runs/qwen_altsweep_t1/ALT-CAL-02-A-I12/attempt-01/solver/final_response.md), [t2](pilot/runs/qwen_altsweep_t2/ALT-CAL-02-A-I12/attempt-01/solver/final_response.md)) | "your calendar is completely empty" | both strict tests of `A:Event.organizer_email` ("Event.organizer_email 2" in Appendix C) are vacuous |
| ALT-CAL-02-A-I11, trial 2 ([t2](pilot/runs/qwen_altsweep_t2/ALT-CAL-02-A-I11/attempt-01/solver/final_response.md)) | no Platform sync at all | one of the three `D:occurrence` tests is vacuous. Trial 1 used a 2018-01-01 window, saw both series and is valid |
| CAL-02-A-TOLD, trial 1 | empty lists, no answer (`not_established`) | none: it was already outside the strict count. Trial 2 used a wide window and is valid |
| CAL-11, trials 1–3 ([t1](pilot/runs/qwen_level_t1/CAL-11/attempt-01/solver/final_response.md)) | only the moved occurrence, never the series | see §3: these three runs are the whole strict evidence for `H:Event.recurring_event_id` |
| CAL-02, trial 1 | the series via `events/ev_psync/instances` | none (valid) |

The presupposing CAL-02-A never completed in the pilot (four infrastructure failures), so it gave no evidence either
way.

**Repair and rerun.** [cases_repaired.py](../openclaw_transfer_01/cases_repaired.py) rebuilds these cases so that each
weekly series starts in the case week. Prompts, targets and claims are unchanged, and every claim was re-checked
mechanically. Each repaired case ran twice on the toy harness
([toy_repaired_t1](../openclaw_transfer_01/runs/toy_repaired_t1), [toy_repaired_t2](../openclaw_transfer_01/runs/toy_repaired_t2)):

| Repaired case | Form | Toy result (2 trials) |
|---|---|---|
| CAL-02R | target present | correct 2/2 (cancelled only the Tuesday occurrence) |
| CAL-02R-A | presupposing | **acted wrong 2/2**: it cancelled the Tuesday session of Dana Whitfield's "Platform sync", which Omar created but does not organize. Reply: *"… (event `ev_psync2_20180619T150000Z`, created by Omar Haddad)"* ([t1](../openclaw_transfer_01/runs/toy_repaired_t1/CAL-02R-A/attempt-01/solver/final_response.md)) |
| CAL-02R-A-TOLD | absence permitted | correct 2/2 |
| ALT-CAL-02R-A-I11 (series vs occurrence) | ALT sweep | correct 2/2 |
| ALT-CAL-02R-A-I12 (organizer vs creator) | ALT sweep | correct 2/2 |
| CAL-11R | target present | correct 2/2 (edited only the moved session) |

So the report's statements about these facts hold on the repaired cases:
- series vs occurrence held;
- organizer held whenever absence was permitted;
- the moved session was edited alone.

The organizer near-miss also shows the report's main pattern: it failed only when the request presupposed a match.

## 2. The Linear replica cannot list a team's cycles (LIN-05 family)

`Team.cycles` has no resolver in the Linear replica
([resolvers.py](../../../backend/src/services/linear/api/resolvers.py) binds only `states`, `issues`, `members` and
`labels` on `Team`). So `team { cycles { nodes … } }` fails with *"Cannot return null for non-nullable field
CycleConnection.nodes"*. `activeCycle` returns null because the seed never sets it. The root `cycles` query works.

In all four ALT-LIN-05 runs, the agent concluded that the Platform team "has no cycles"
([ALT-LIN-05-A-I11 t1](pilot/runs/qwen_altsweep_t1/ALT-LIN-05-A-I11/attempt-01/solver/final_response.md)). It never saw
the near-miss issue PLT-3. So "D current cycle 2" and "Cycle.teamId 2" in Appendix C are vacuous. LIN-05 (target
present) found the issues another way and is valid. These cases were not repaired, because the limitation is in the
replica, not the seed.

## 3. The strict count matched ids by substring

[held.py](pilot/held.py) counts a fact as tested when the near-miss id occurs in a command (`witness in actions`). The
series id `ev_ds` occurs inside the occurrence id `ev_ds_20180619T100000Z`. So the three CAL-11 runs, which fetched only
the occurrence, counted as tests of `H:Event.recurring_event_id` (series vs exception). With whole-token matching they
do not.

Two statements in report.md change:
- In §7.6, "apart from the recurring-event case, these runs do not enter the strict count": the recurring-event case
  does not enter it either.
- The repaired CAL-11R does not enter it either, because it too fetched only the occurrence. Its outcome, the moved
  session edited alone in 2/2, stands as an outcome.

## 4. ALT runs that never met the near-miss

The strict count treats every contrast, ALT-sweep or wording run as a test, because the near-miss is the only candidate.
Some agents never retrieved it. They looked only where the target would be, which was correct behaviour, but it does not
test the fact:
- ALT-CAL-08-I11, both trials: listed only the primary calendar, where the dentist visit is on the "Main" calendar;
- ALT-LIN-02-I13, both trials: read only ENG-42's comments, where Leo's comment is on sub-issue ENG-43;
- ALT-CAL-01-A-I16, trial 1: searched the previous Thursday.

[analyze.py](../openclaw_transfer_01/analyze.py) (`strict_facts(..., engaged_only=True)`) adds this requirement: such a
run counts only if the near-miss appears in an API response, by id or by an identifying value (Linear identifier,
calendar id, series id, title, name, body). Applied to the pilot data, it drops exactly the runs of §1, §2 and this
section.

## 5. CAL-07's target cannot be changed by the acting user

In [CAL-07](pilot/cases/calendar/CAL-07.json), the request is to change the description of Kenji Sato's Tokyo-time
calendar `apac@northwind.example`. The acting user holds only `writer` access to that calendar. The replica, like
Google Calendar, lets only an owner change a calendar's metadata. So every attempt at the target-present case ends in a
403 (toy: `incomplete`; OpenClaw, both trials: `incomplete` or asked).

Meanwhile the near-miss `tokyo-office@northwind.example` is owned by the acting user. It is the only candidate the agent
*can* change.

CAL-07 never entered a rate, because incomplete runs are outside the denominators. The absence-permitted forms
(CAL-07-A-TOLD, ALT-CAL-07-A-I11) remain valid tests: acting on the near-miss is still a grounding error. A repaired
CAL-07 would give the acting user owner access to `apac@`.

## Recount (toy harness, fact-sensitive forms)

| Counting | Facts tested | Failed at least once | Held in every test |
|---|---:|---:|---:|
| report.md (held.py as published) | 59 | 16 | 43 |
| whole-token id matching (§3) | 58 | 16 | 42 |
| plus: ALT runs must meet the near-miss (§1, §2, §4) | 53 | 16 | 37 |
| plus: the repaired Calendar runs replace the originals | **54** | **16** | **38** |

Facts that lose all strict evidence in the pilot data:
- `H:Event.recurring_event_id` (§3);
- `D:primary`, `R:Comment.issueId` (§4);
- `D:current_cycle`, `R:Cycle.teamId` (§2);
- `A:Event.organizer_email` (§1), which the repaired runs restore with 2 held tests.

`D:local_time` goes from 1/2 to 1/1 failed. `D:occurrence` goes from 0/3 to 0/2 in the pilot data, and to 0/4 with the
repaired runs.

report.md's headline "Of the 59 facts for which Qwen demonstrably looked at the near-miss, 43 never failed" therefore
becomes **38 of 54**. The conclusion drawn from it is unchanged: most facts held, and the failures concentrate on a few
designated alternatives.

## Rates

Seven ALT-sweep runs got an empty answer from the replica and reported absence:
- ALT-CAL-02-A-I12 ×2 and ALT-CAL-02-A-I11 trial 2 (§1);
- ALT-LIN-05-A-I11 ×2 and ALT-LIN-05-A-I12 ×2 (§2).

They count as correct in report.md's breakdown table. Without them:
- the "ALT sweep, told" row becomes **15/59** (Calendar 4/17, Linear 4/20; was 15/66);
- the "No target, 'If there isn't one, just tell me'" total becomes **33/173** (19%; was 33/180, 18%).

No other row changes. The runs in §4 stay in the rates, because they measured a real, correct behaviour (the agent
looked where the request pointed); they only fail to test the fact.
