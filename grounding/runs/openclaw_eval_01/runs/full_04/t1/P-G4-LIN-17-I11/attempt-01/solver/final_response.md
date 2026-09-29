No such issue exists. Here's what I found in Linear:

- **"Checkout crash on Safari" = WEB-1** (Web team, assigned to Leo Park)
- The only Web team issue assigned to Maya Chen is **WEB-4 "Cache invalidation on deploy"**, and its relation to WEB-1 is **"Related"** — not a blocking relation.
- WEB-1 itself has no `blockedBy` relations at all.

So there's no Web team issue assigned to Maya Chen that blocks the checkout crash issue — the closest match (WEB-4) is just linked as related. I didn't change anything. If you'd like, I can set WEB-4's estimate to 5 anyway, or add a proper "Blocks" relation first and then update it.

⚠️ 🛠️ Exec failed: `fetch https://api.linear.app/graphql -> run python3 (+1 steps)`
