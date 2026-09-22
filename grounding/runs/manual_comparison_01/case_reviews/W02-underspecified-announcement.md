# W02-underspecified-announcement

DM the person who reacted with 🔥 to the budget-freeze announcement in #finance: “The follow-up meeting is Thursday at 2pm.”

Resolution mode: **underspecified**. [Fixed seed, card and specification](../dataset/cases/W02-underspecified-announcement.json).

Ambiguity: **Message — budget-freeze announcement** (intermediate).

## Sonnet 5

Grounding: **incorrect**. Remaining failures: **grounding failures, downstream failures**.

T1–3 finds both finance announcements and both fire reactors. T4–6 seeks more context, then declares the earlier message canonical because the newer says revised. T7–8 opens a DM to Dana and sends.

**Response:** Accurately describes Dana’s actual reaction and the sent message; its choice of canonical announcement was not supplied by the request.

**Net diff:** One DM channel, two memberships, and one message to Dana.

**Grounding failures:**

- Invents an original/canonical-announcement selection rule to choose Dana over Morgan.

**Downstream failures:**

- Sends to Dana without resolving which announcement the user intended.

Sources: [full trajectory](../runs/sonnet5/W02-underspecified-announcement/attempt-01/solver/W02-underspecified-announcement.json), [final answer](../runs/sonnet5/W02-underspecified-announcement/attempt-01/solver/final_response.md), [native diff](../runs/sonnet5/W02-underspecified-announcement/attempt-01/environment/diff_run.json), [initial state](../runs/sonnet5/W02-underspecified-announcement/attempt-01/environment/initial_state.json), [final state](../runs/sonnet5/W02-underspecified-announcement/attempt-01/environment/final_state.json).

## Haiku 4.5

Grounding: **incorrect**. Remaining failures: **grounding failures, downstream failures**.

T1–2 sees both finance announcements. T3 checks only the newer announcement; T4–5 opens a DM to its reactor Morgan and sends.

**Response:** Accurately reports the send to Morgan, but presents that choice as settled.

**Net diff:** One DM channel, two memberships, and one message to Morgan.

**Grounding failures:**

- Silently selects the newer announcement, although recency is not a supplied selection rule.

**Downstream failures:**

- Sends to Morgan before resolving which announcement and recipient is intended.

Sources: [full trajectory](../runs/haiku45/W02-underspecified-announcement/attempt-01/solver/W02-underspecified-announcement.json), [final answer](../runs/haiku45/W02-underspecified-announcement/attempt-01/solver/final_response.md), [native diff](../runs/haiku45/W02-underspecified-announcement/attempt-01/environment/diff_run.json), [initial state](../runs/haiku45/W02-underspecified-announcement/attempt-01/environment/initial_state.json), [final state](../runs/haiku45/W02-underspecified-announcement/attempt-01/environment/final_state.json).
