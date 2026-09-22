# W01-absent-text-emoji

Add 🚀 to the messages Priya reacted to with 🙌.

Resolution mode: **absent**. [Fixed seed, card and specification](../dataset/cases/W01-absent-text-emoji.json).

## Sonnet 5

Grounding: **correct**. Remaining failures: **none demonstrated**.

T1–5 identifies Priya, fetches all message history and reactions, and distinguishes emoji text from actual reactions. T6–7 verifies no other conversations; T8 finishes.

**Response:** Accurately reports that Priya has eyes reactions but no raised_hands reactions.

**Net diff:** Empty net diff as required.

Sources: [full trajectory](../runs/sonnet5/W01-absent-text-emoji/attempt-01/solver/W01-absent-text-emoji.json), [final answer](../runs/sonnet5/W01-absent-text-emoji/attempt-01/solver/final_response.md), [native diff](../runs/sonnet5/W01-absent-text-emoji/attempt-01/environment/diff_run.json), [initial state](../runs/sonnet5/W01-absent-text-emoji/attempt-01/environment/initial_state.json), [final state](../runs/sonnet5/W01-absent-text-emoji/attempt-01/environment/final_state.json).

## Haiku 4.5

Grounding: **correct**. Remaining failures: **none demonstrated**.

T1–10 identifies Priya and checks all six messages, separating literal emoji text from reaction records. T11–25 performs further searches and repeated checks, including one rejected invalid_limit request. T26 correctly reports absence.

**Response:** Accurately states Priya has only eyes reactions, not raised_hands, so no rocket reactions can be added.

**Net diff:** Empty net diff as required.

**Recovery notes:**

- Initial premature request for a token did not persist; real authenticated calls proceeded. An invalid_limit history request was retried with a valid limit.

Sources: [full trajectory](../runs/haiku45/W01-absent-text-emoji/attempt-01/solver/W01-absent-text-emoji.json), [final answer](../runs/haiku45/W01-absent-text-emoji/attempt-01/solver/final_response.md), [native diff](../runs/haiku45/W01-absent-text-emoji/attempt-01/environment/diff_run.json), [initial state](../runs/haiku45/W01-absent-text-emoji/attempt-01/environment/initial_state.json), [final state](../runs/haiku45/W01-absent-text-emoji/attempt-01/environment/final_state.json).
