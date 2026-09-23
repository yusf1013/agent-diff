# W01-single

Add 🚀 to the messages Priya reacted to with 🙌.

Resolution mode: **single**. [Fixed seed, card and specification](../dataset/cases/W01-single.json).

## Qwen 3.6 27B

Grounding: **correct**. Remaining failures: **none demonstrated**.

T1 resolves Priya Shah; T2 lists the single channel; T3 reads all five messages; T4-8 fetch each message's reactions and find Priya raised_hands only on M2. T9 adds rocket to M2; T10 verifies rocket/eyes/raised_hands; T11 reports completion.

**Response:** Accurately reports the sole matching message and successful rocket addition.

**Net diff:** One U_ACTOR rocket insert on M2 (1735808520.000001); no other changes.

Sources: [full trajectory](../runs/qwen36/W01-single/attempt-01/solver/W01-single.json), [final answer](../runs/qwen36/W01-single/attempt-01/solver/final_response.md), [native diff](../runs/qwen36/W01-single/attempt-01/environment/diff_run.json), [initial state](../runs/qwen36/W01-single/attempt-01/environment/initial_state.json), [final state](../runs/qwen36/W01-single/attempt-01/environment/final_state.json).
