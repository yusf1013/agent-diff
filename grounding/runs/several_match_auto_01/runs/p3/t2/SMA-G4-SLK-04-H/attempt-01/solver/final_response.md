Added the 👀 (eyes) reaction to all of Maya Chen's (U_MAYA) launch checklist cards in #launch-readiness (C_LAUNCH) that list the rollback steps. Three cards qualified and were reacted to:

1. ts 1789974600.000702 — "Launch checklist card: rollback steps — 1) halt deploys 2) restore snapshot 3) verify health"
2. ts 1789989000.000001 — "Launch checklist card: rollback steps — 1) halt deploys 2) restore snapshot 3) verify health"
3. ts 1789989060.000701 — "Launch checklist card: rollback steps — 1) halt deploys 2) restore snapshot 3) verify health"

Correctly excluded:
- A plain-text rollback-steps message (ts 1789989900.000002) — not a card.
- A "Follow-up card: verification checklist" (ts 1789990800.000003) — not a launch checklist card with rollback steps.
- A "Launch checklist card: rollout steps" (ts 1789992300.000004) — lists rollout, not rollback, steps.

Each reaction was confirmed via reactions.get showing the "eyes" reaction on all three messages.
