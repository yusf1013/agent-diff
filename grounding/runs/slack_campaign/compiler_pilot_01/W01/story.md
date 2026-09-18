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
