# roadmap_01: the quick unblockers and the two audits

Steps 1 and 2 of the [roadmap](../../protocols/roadmap.md), done on 2026-09-27 on branch `exp/roadmap-01`. Nothing
here changes a result that autogen_01 or autogen_02 reported.

| Item | Status | Record |
|---|---|---|
| The trial clock leaves out Purdue waiting | done; the approved smoke run passed | [clock_smoke/](clock_smoke/README.md) |
| Muse's verify-reminder off for judge and reader | done; the approved check: 30/30 verdicts unchanged | [muse_reminder_check/](muse_reminder_check/README.md) |
| List-level loose ends | done | [loose_ends.py](loose_ends.py): [known_defects.json](known_defects.json), [witness_check.json](witness_check.json), [date_flags.json](date_flags.json) |
| Prompt overfitting and leak audit | report | [overfit_audit.md](overfit_audit.md) |
| Domain knowledge in deterministic code | report | [domain_code_audit.md](domain_code_audit.md) |

## Results in brief

- **The clock.** Waiting was 65% of the wall time in the smoke run. The 6 Linear tests that had timed out all
  finished on their first attempt: 5 answered and 1 reached the 40-turn limit. The most any used of its own budget
  was 182 of 480 seconds.
- **The reminder.** With it off, the judge gives the same verdict on all 30 labelled trials: the same outcome, exposed
  facts, records acted on and mechanism. It is 3 times faster, and 19% cheaper at list price in this run.
- **Loose ends.**
  - The witness check flags 6 of the 520 regular tests Qwen ran: five probes without their trap and one whose near
    miss becomes a match.
  - One scenario depends on the run date: G4-LIN-02, whose "overdue" turns wrong after 2026-09-30.
  - `known_defects.json` lists 21 known defective or doubtful tests and scenarios, each with what to do for a new
    agent. It is also the start of the failure-attribution development set.
- **Overfitting.**
  - No leak reaches the agent under test or the judge.
  - The Muse writer copied the worked examples into 9 of the 29 Phase 4 scenarios: "Room 5B" in 6 Calendar
    scenarios, and a near copy of the Box example.
- **Domain code.**
  - The machinery is generic. The domain knowledge sits in the seed builders, the pre-checks' read calls, and a few
    constants.
  - A new domain would need roughly 50–200 lines of our code plus two short notes; the domain model is the real cost.
  - Two findings to fix: the seed defaults encode decoy design, and the Linear and Slack seed builders import code
    from hand-made studies.

## For step 3: proposed changes, none made

From the loose ends (fixes found by autogen_02):
1. Run the witness check on every probe in the suite derivation, as the policy derivation already does.
2. Leave the tests in `known_defects.json` out of runs for new agents (in the sampler and the runner).
3. G4-LIN-02: pin the date, or leave its tests out.
4. The fixes that change prompts or code, pending from autogen_02:
   - state counts that the acting bot changes unambiguously;
   - have the reader check the seed's other fields (time zones) and requests that parse two ways;
   - let the clone copier copy rows two steps from the target.

From the overfit audit:

5. Tell the writer not to reuse the examples' names, values or phrasing; give the examples distinctive values.
6. Remove "(not in its subfolders)" from the Box example; it breaks the method's own rule 4.
7. State where the method's "make the near miss tempting" heuristics came from (the pilot runs).
8. Keep the 9 copied scenarios and disclose it, or regenerate G4-BOX-05.
9. Restate one line of Slack's replica notes as a fact about the mock.

From the code audit:

10. Make the default people neutral, or document their near-miss pairs.
11. Move the Linear and Slack seed classes into the kit, unchanged.
12. Derive the fields a clone must change from the schema's unique constraints.
13. Optional: derive the read probes from the API docs, and keep the replica-gap exclusions from the pre-checks'
    findings.
