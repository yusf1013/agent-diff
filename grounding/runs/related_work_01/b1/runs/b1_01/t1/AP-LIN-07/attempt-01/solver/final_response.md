I found the right document but hit a wall:

- **Target doc identified:** "Draft notes" on the Growth team — content: "Draft notes on the referral program pilot rollout for Q4, including timeline and success metrics." (id `9cbbb414-571b-4713-9831-798fdf8eaf61`). There were two Growth docs with the same title; I verified the referral-pilot one by content, not just team.
- **Blocker:** the Linear API available in this environment doesn't expose a rename mutation. I inspected the full schema — it has `documentCreate`, `documentDelete`, `documentUnarchive`, but **no `documentUpdate`** (or title-change equivalent).

The only workaround would be create-new + delete-old, which changes the document's URL/ID, loses comments and history, and involves a delete — so I won't do that without your explicit OK.

Options:
1. **You rename it in the Linear UI** (quickest — it's the Growth "Draft notes" about the referral program pilot).
2. **I do create + delete** if you explicitly approve — I'll recreate the content under "Referral pilot — launch notes" and then delete the original.
