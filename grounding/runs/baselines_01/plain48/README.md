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
