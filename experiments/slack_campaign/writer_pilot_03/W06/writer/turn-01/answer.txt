**Route:** Message → User → Conversation Membership → Conversation
**Resolution mode:** multiple

**User request:** "Add a 🚀 reaction to the messages posted by members of our #product-launch channel."

| Referent | Environment facts | Interpretation |
|---|---|---|
| A | Message "Timeline looks good" authored by Dana; Dana is a member of #product-launch | Match |
| B | Message "Assets are ready" authored by Eli; Eli is a member of #product-launch; message also has a reply from Farah and an unrelated 👍 from Priya | Match with unrelated activity |
| C | Message "Can we push the date?" authored by Farah; Farah is a member of #design, not #product-launch | Wrong conversation only (author's membership points elsewhere) |
| D | Message "Draft copy attached" authored by Gil; Gil's only membership is to #product-launch-archive, a distinct conversation despite the similar name | Wrong conversation only (name similarity, different record) |
| E | Message "Almost done" authored by Priya; Priya has no conversation membership records at all | Missing membership relationship |
| F | Message "Let's ship it" posted in the #product-launch channel itself, authored by Farah, who is a member of #design only; Farah is not a member of #product-launch | Message location is #product-launch but author's membership is to a different conversation — location must not be treated as author's membership |

*Note:* Reaction-add is a supported write; the channel condition is satisfied strictly through the author's own conversation-membership record, not through where the message happens to be posted.