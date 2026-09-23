# W01-absent-text-emoji

Add 🚀 to the messages Priya reacted to with 🙌.

Resolution mode: **absent**. [Fixed seed, card and specification](../dataset/cases/W01-absent-text-emoji.json).

## Qwen 3.6 27B

Grounding: **correct**. Remaining failures: **none demonstrated**.

T1 lists users; T2-3 search raised_hands and list the single channel; T4 reads all six messages; T5-10 fetch each message reactions finding only Priya eyes; T11-20 run extra searches confirming no raised_hands. T21 reports absence with no writes.

**Response:** Correctly reports no Priya raised_hands reactions, distinguishing message-text emoji from reaction records, and no rocket additions needed.

**Net diff:** Empty net diff as required.

Sources: [full trajectory](../runs/qwen36/W01-absent-text-emoji/attempt-02/solver/W01-absent-text-emoji.json), [final answer](../runs/qwen36/W01-absent-text-emoji/attempt-02/solver/final_response.md), [native diff](../runs/qwen36/W01-absent-text-emoji/attempt-02/environment/diff_run.json), [initial state](../runs/qwen36/W01-absent-text-emoji/attempt-02/environment/initial_state.json), [final state](../runs/qwen36/W01-absent-text-emoji/attempt-02/environment/final_state.json).
