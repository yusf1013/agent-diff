# Assignment W01

**Route:** Message → Reaction → User
**Resolution mode:** multiple

**Request:** "Add a ✅ to the messages Priya reacted to with a 🚀 in #product-launch."

| Referent | Environment facts | Interpretation |
|---|---|---|
| A | Message "Shipping build 4.2 to prod tonight" in #product-launch; Priya 🚀 | Match |
| B | Message "Landing page copy finalized" in #product-launch; Priya 🚀, and also Dan 👀 on the same message | Match with unrelated activity |
| C | Message "Rollback plan drafted" in #product-launch; Priya 👀 (no 🚀 from her) | Wrong emoji only |
| D | Message "QA sign-off received" in #product-launch; Wen 🚀 (Priya did not react) | Wrong person only |
| E | Message "Marketing embargo lifted" in #product-launch; no reactions at all | Missing reaction relationship |
| F | Message "Launch retro scheduled" in #product-launch; Priya 👀 and Wen 🚀 (Priya's reaction and the 🚀 reaction are different reactions) | Person and emoji occur on different reactions |
| G | Message "Beta invite list finalized" in #eng-internal (not #product-launch); Priya 🚀 | Right person/emoji, wrong container location |