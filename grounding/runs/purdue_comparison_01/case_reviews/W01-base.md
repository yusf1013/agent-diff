# W01-base

Add 🚀 to the messages Priya reacted to with 🙌.

Resolution mode: **multiple**. [Fixed seed, card and specification](../dataset/cases/W01-base.json).

## Qwen 3.6 27B

Grounding: **correct**. Remaining failures: **none demonstrated**.

T1 identifies Priya Shah; T2 lists the single channel; T3-4 read general history; T5-10 fetch reactions for all six messages and find Priya raised_hands on M1/M2 only. T11 add attempt fails invalid_name; T13-14 add rockets to M2 then M1; T15-16 verify both; T17 reports completion.

**Response:** Accurately names both matching messages and reports successful rocket additions.

**Net diff:** Exactly two U_ACTOR rocket inserts on M2 (1735808520.000001) and M1 (1735808460.000001); no other changes.

**Recovery notes:**

- T11 POST with query-string params fails invalid_name; T13 retries with form-encoded -d body and succeeds on both messages.
- T12 empty response is followed by the harness nudge and a successful retry; no invented observations persist.

Sources: [full trajectory](../runs/qwen36/W01-base/attempt-01/solver/W01-base.json), [final answer](../runs/qwen36/W01-base/attempt-01/solver/final_response.md), [native diff](../runs/qwen36/W01-base/attempt-01/environment/diff_run.json), [initial state](../runs/qwen36/W01-base/attempt-01/environment/initial_state.json), [final state](../runs/qwen36/W01-base/attempt-01/environment/final_state.json).
