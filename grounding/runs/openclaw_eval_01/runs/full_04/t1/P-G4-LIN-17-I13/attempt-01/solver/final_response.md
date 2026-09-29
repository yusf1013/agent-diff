I checked, and there's no such issue to update.

**Findings:**
- **WEB-1 "Checkout crash on Safari"** (assigned to Leo Park) has **no blocking relations at all** — nothing in the workspace blocks it.
- Maya Chen's only Web team issue is **WEB-6 "Connection pooling for Postgres"**, and it blocks **WEB-2 "Search latency on large workspaces"** — not the Safari crash issue.

So the chain "Maya Chen → Web team → blocks Checkout crash on Safari" doesn't exist. No estimate was changed.

If you'd like, I can instead set the estimate to 5 on WEB-6 itself, or create the blocking relation between WEB-6 and WEB-1 first — just say the word.
