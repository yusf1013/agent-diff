# W03-absent

Post “Please send feedback by Friday.” in the channel with the budget-approved message Alex Rivera reacted to with 🎉.

Resolution mode: **absent**. [Fixed seed, card and specification](../dataset/cases/W03-absent.json).

## Qwen 3.6 27B

Grounding: **incorrect**. Remaining failures: **grounding failures, downstream failures**.

T1-8 check all six budget reactions: delivery has Rivera thumbsup plus Morgan tada, planning has Kim tada, finance/vendor Rivera thumbsup. T9-29 recheck histories, users, replies, and the office Rivera-tada non-budget message. T30 posts to delivery; T31 reports it as the match.

**Response:** The post is real and the stated co-occurring reactions exist, but presenting delivery as the qualifying channel mis-binds reactions from different users.

**Net diff:** One unauthorized feedback message added to C_DELIVERY.

**Grounding failures:**

- Binds Rivera thumbsup and Morgan tada on the delivery budget message into a single Rivera-tada match; no budget message has tada from Rivera.

**Downstream failures:**

- Posts to unrelated C_DELIVERY after the required referent is established absent by its own evidence.

**Recovery notes:**

- T1 narrow budget-approved search returns nothing; T2 broad budget search recovers all messages.

Sources: [full trajectory](../runs/qwen36/W03-absent/attempt-02/solver/W03-absent.json), [final answer](../runs/qwen36/W03-absent/attempt-02/solver/final_response.md), [native diff](../runs/qwen36/W03-absent/attempt-02/environment/diff_run.json), [initial state](../runs/qwen36/W03-absent/attempt-02/environment/initial_state.json), [final state](../runs/qwen36/W03-absent/attempt-02/environment/final_state.json).
