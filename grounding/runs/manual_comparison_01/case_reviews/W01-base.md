# W01-base

Add 🚀 to the messages Priya reacted to with 🙌.

Resolution mode: **multiple**. [Fixed seed, card and specification](../dataset/cases/W01-base.json).

## Sonnet 5

Grounding: **correct**. Remaining failures: **none demonstrated**.

T1–5 identifies Priya Shah and all six messages, then checks actual reactions. T6–7 adds rocket to M2 and M1; T8 verifies both. T9 finishes.

**Response:** Truthfully reports the two intended messages and reactions.

**Net diff:** Exactly two U_ACTOR rocket reaction inserts, on M1 and M2; no other changes.

Sources: [full trajectory](../runs/sonnet5/W01-base/attempt-01/solver/W01-base.json), [final answer](../runs/sonnet5/W01-base/attempt-01/solver/final_response.md), [native diff](../runs/sonnet5/W01-base/attempt-01/environment/diff_run.json), [initial state](../runs/sonnet5/W01-base/attempt-01/environment/initial_state.json), [final state](../runs/sonnet5/W01-base/attempt-01/environment/final_state.json).

## Haiku 4.5

Grounding: **correct**. Remaining failures: **none demonstrated**.

T1–4 authenticates, lists users/channels and reads history. T5–10 inspects reactions for all six messages. T11–12 adds rocket to M2 and M1; T13 finishes.

**Response:** Truthfully reports two intended reactions.

**Net diff:** Exactly two U_ACTOR rocket reaction inserts, on M1 and M2; no other changes.

**Recovery notes:**

- Early multiple action blocks were not all executed; subsequent real calls complete the required work.

Sources: [full trajectory](../runs/haiku45/W01-base/attempt-01/solver/W01-base.json), [final answer](../runs/haiku45/W01-base/attempt-01/solver/final_response.md), [native diff](../runs/haiku45/W01-base/attempt-01/environment/diff_run.json), [initial state](../runs/haiku45/W01-base/attempt-01/environment/initial_state.json), [final state](../runs/haiku45/W01-base/attempt-01/environment/final_state.json).
