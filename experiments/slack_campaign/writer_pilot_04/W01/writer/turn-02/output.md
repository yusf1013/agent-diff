**Audit**

- Selection conditions (independent of the write): a message must have received a reaction whose emoji is raised_hands AND whose reactor is Priya (same reaction record, not just same message).
- Downstream operation: add 🚀 (rocket) reaction — both raised_hands (read) and rocket (write) are in the supported emoji list, so this is a valid capability match. No restriction (e.g. "own reactor only") applies to reading raised_hands or to adding a new rocket reaction.
- Qualifying roots recomputed from all facts:
  - M1: Priya 🙌 → qualifies.
  - M2: Priya 🙌 (+ unrelated Diego 👀) → qualifies, extra activity doesn't disqualify.
  - M3: Priya 👀 only → fails emoji condition (no raised_hands reaction at all).
  - M4: Diego 🙌 → fails person condition (reactor isn't Priya).
  - M5: no reactions → fails relationship existence.
  - M6: Priya 👀 and Diego 🙌 → person and emoji present but on two different reaction records, so no single reaction satisfies both → fails the joint binding.
- Condition-to-negative mapping: emoji→M3, person→M4, existence→M5, joint binding→M6. All four distinct failure types covered; no negative accidentally has a second qualifying chain elsewhere (records aren't shared across rows).
- Count check: exactly 2 qualifying roots (M1, M2), matching assigned MULTIPLE count with one plain match and one match-with-extra-activity, as required.
- No discrepancies found; original sketch stands unchanged.

**Final sketch**

Route: Message → Reaction → User
Resolution mode: multiple

**Request:** "Add a 🚀 to the messages that Priya reacted to with raised_hands."

**Selection conditions:** message received a reaction with emoji raised_hands, and that reaction's reactor is Priya.

| Referent | Environment facts | Interpretation |
|---|---|---|
| "Rocket specs draft" (M1) | Priya 🙌 (raised_hands) | Match |
| "Budget review" (M2) | Priya 🙌 (raised_hands); also Diego 👀 (unrelated) | Match with unrelated activity |
| "Vendor contract" (M3) | Priya 👀 only | Wrong emoji only |
| "Timeline update" (M4) | Diego 🙌 (raised_hands) | Wrong person only |
| "Design mockup" (M5) | No reactions; other message facts unchanged | Missing reaction relationship |
| "Marketing plan" (M6) | Priya 👀 and Diego 🙌 (raised_hands) | Person and emoji occur on different reactions |