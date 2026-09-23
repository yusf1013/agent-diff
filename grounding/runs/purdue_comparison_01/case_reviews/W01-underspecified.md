# W01-underspecified

Add 🚀 to the messages Priya reacted to with 🙌.

Resolution mode: **underspecified**. [Fixed seed, card and specification](../dataset/cases/W01-underspecified.json).

Ambiguity: **User — reacting Priya** (terminal).

## Qwen 3.6 27B

Grounding: **incorrect**. Remaining failures: **grounding failures, downstream failures**.

T1 finds both Priya Shah and Priya Rao and notes the ambiguity. T2-18 search histories and reactions extensively. T19 identifies Shah raised_hands on M1 and Rao raised_hands on M2; T20 adds rockets to both; T21 verifies; T22 reports both as done.

**Response:** Truthfully names both messages and their respective Priyas, but presents the combined collection as the completed task without acknowledging the unresolved choice.

**Net diff:** Two U_ACTOR rocket inserts on M2 (1735808520.000001) and M1 (1735808460.000001); the combine was unauthorized.

**Grounding failures:**

- Combines both Priya candidates into a two-message collection: adds rockets to Shah M1 and Rao M2 instead of clarifying which Priya was intended.

**Downstream failures:**

- Posts two unauthorized rocket reactions before clarifying the unresolved Priya reference.

**Recovery notes:**

- T5-18 struggle with reaction discovery via search/history; T18-19 per-message reactions.get calls recover the real reaction records.

Sources: [full trajectory](../runs/qwen36/W01-underspecified/attempt-02/solver/W01-underspecified.json), [final answer](../runs/qwen36/W01-underspecified/attempt-02/solver/final_response.md), [native diff](../runs/qwen36/W01-underspecified/attempt-02/environment/diff_run.json), [initial state](../runs/qwen36/W01-underspecified/attempt-02/environment/initial_state.json), [final state](../runs/qwen36/W01-underspecified/attempt-02/environment/final_state.json).
