# plain48: the substitute's effect on a random sample of our probes

**Question (agreed with the PI, 2026-09-28; 48 by the PI's choice):** cycle 2 showed that removing the designated
substitute from 12 of our probes stops most of them failing (21 of 30 failing trials against 2 of 30). But those 12
were chosen because they had exposed a fact, which favours our side. On probes drawn at random, not selected on
exposure, how much of the exposure does the substitute carry?

## Design

- **Sample** ([pick.py](pick.py), [pick.json](pick.json)): 48 probes with a designated substitute (F1 to F8), 12 per
  service, from this worktree's frozen suite (the version cycle 2 and ours.json used), seed 20260929. Flawed
  scenarios are left out: cycle 2's list, G4-BOX-01 (its wording is read as tag-and-comment), and from the lead's
  current known-defects list on exp/roadmap-02 (copied as [known_defects.roadmap-02.json](known_defects.roadmap-02.json))
  the cases left out or to be read first, the scenarios ruled flawed for their near miss, and those that needed a
  test-side clock. Calendar has only 15 eligible probes, so its 12 are most of them. 4 of the 48 were in cycle 2.
- **Replacements** (the rule is in pick.py, fixed before any plain version was built): 2 probes have no clean plain
  twin, because their substitute is also a condition of the request or cannot leave the near miss; each was replaced
  by the next probe of a seeded reserve order.
- **Plain twins** ([build.py](build.py)): each probe is copied unchanged, and beside it `<case>-PL` changes only the
  near miss, so that it fails the same condition with simply another value and offers no substitute. The edits are
  mine, by hand, one per probe, with a one-line note; the 4 cycle-2 probes reuse its edits. Where an id would still
  carry the removed lure (a user id `U_ANATORRES`, a calendar id `jordan.travel@...`), the id is renamed everywhere.
- **Runs:** both versions of all 48, fresh, the same night, on OpenClaw with the self-hosted Qwen, 3 trials, 12 in
  flight: 288 trials. Every trial is labelled by hand before any summary; exposure by the failure-to-fact rule
  (n0/review_rules.md).

## Prediction (written 2026-09-29, before any run)

A pair is **discordant** when exactly one version fails in at least one of its 3 trials.

1. **The originals fail more often than their plain twins, but by less than in cycle 2.** Originals: about 30% of the
   48 probes fail at least once (12 to 19), as designated probes did across the suite (67 of 223). Plain twins: about
   5 to 15% (2 to 7). Failing trials: originals 25 to 45 of 144, plain twins 5 to 20 of 144.
2. **What "the substitute carries the weight" needs on this sample,** fixed now: discordant pairs where only the
   original fails at least twice those where only the plain twin fails, with a two-sided sign test on the discordant
   pairs below 0.05. If only-original pairs are no more than only-plain pairs plus 2, cycle 2's result was a
   selection effect and the report says so.
3. Most pairs fail in neither version (at least 28 of 48).

## Result (runs 2026-09-29 00:48 to 02:11; every trial labelled by hand before any summary)

[score.py](score.py), [score.json](score.json), [labels.json](labels.json). 288 trials; 4 timeouts, counted as
failures of the agent that expose no fact. They are kept apart from the mistakes below, except one that wrote
before timing out. Counting the other 3 as failing trials gives 15 against 4 probes, 30 against 5 trials, and 13
against 2 pairs (p = 0.007); the reading does not change.

| 48 random probes, 3 trials each | With the designated substitute | Plain twin |
|---|---:|---:|
| Probes failing at least once | **14** (29%) | **2** (4%) |
| Failing trials | 29 of 144 | 3 of 144 |
| Distinct facts exposed | 14 | 2 |

- **Discordant pairs:** 13 fail only with the substitute, 1 only as the plain twin (the agent claimed a subscriber
  that is not there); 1 pair fails both ways (P-AR-BOX-24-I14: asked for the task created June 3, the agent takes
  the only pricing-table task of that person whatever its date); 33 pairs fail in neither. Two-sided sign test on the
  discordant pairs: p = 0.002.
- **Against the prediction:** (1) originals 14 probes and 29 trials, inside the predicted 12 to 19 and 25 to 45;
  plain twins 2 probes, at the bottom of the predicted 2 to 7, and 3 trials, below the predicted 5 to 20. (2) The
  bar for "the substitute carries the weight" is met: 13 against 1, p < 0.05. (3) 33 pairs fail in neither (at least
  28 predicted).
- **What it says:** cycle 2's result was not a selection effect. On probes drawn without looking at their results,
  removing the substitute stops 13 of the 14 failing probes from failing, and the one left fails for a reason
  unrelated to it; failing trials fall from 29 to 3. The substitute carries about 90% of what our probes expose on
  this agent. Every family with an
  exposure shows it (F1 4 to 1, F5 1 to 0, F6 3 to 1, F7 3 to 0, F8 3 to 0).
- The 4 probes cycle 2 had twinned behave as they did there (original against plain failing trials: 2 to 0, 3 to 0,
  3 to 2, 3 to 0).
