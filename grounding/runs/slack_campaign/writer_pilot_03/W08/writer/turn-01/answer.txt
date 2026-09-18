# Assignment W08

**Route:** Reaction → Message → User → Conversation Membership → Conversation
**Resolution mode:** single

**Request:** "Nina's a member of #beta-testers, and one of her messages picked up a 🚀 reaction somewhere — who reacted with 🚀 to it?"

| Referent | Environment facts | Interpretation |
|---|---|---|
| Priya reacted 🚀 to Nina's message in #product-launch | Nina posted "Checklist is done, ready to ship" in #product-launch; Priya reacted 🚀 to it; Nina is a member of #beta-testers | Match: full chain (reaction→message→author Nina→her membership→#beta-testers) holds |
| Priya reacted 👍 to Nina's message in #product-launch | Same message and same membership facts as above, but Priya's reaction is 👍, not 🚀 | Wrong emoji only |
| Priya reacted 🚀 to Omar's message in #product-launch | Omar posted "Deploy window confirmed" in #product-launch; Priya reacted 🚀 to it; Omar is also a member of #beta-testers | Wrong author only (message not authored by Nina, even though membership-in-#beta-testers condition is satisfied by a different user) |
| Priya reacted 🚀 to Nina's message in #product-launch | Same message and reaction as the positive case, but here Nina's only relevant membership is in #general, not #beta-testers | Wrong membership channel only |
| Priya reacted 🚀 to Nina's message in #product-launch | Same message and reaction as the positive case, but Nina has no conversation membership record for #beta-testers at all (never joined) | Missing membership relation |

*Note:* Since a reaction cannot be removed by anyone other than its own reactor, and this reaction belongs to Priya rather than the acting user, the request is framed as a read (identify the reactor) rather than a reaction-removal write.