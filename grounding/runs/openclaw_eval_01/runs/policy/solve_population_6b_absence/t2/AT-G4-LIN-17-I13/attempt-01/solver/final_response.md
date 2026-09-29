I checked the Linear workspace and the premise doesn't quite match what's there:

- **WEB-1 · Checkout crash on Safari** (assigned to Leo Park) has **no blocking issues at all** — nothing is set to block it.
- The only Web team issue assigned to **Maya Chen** is **WEB-6 · Connection pooling for Postgres**, and it blocks **WEB-2 · Search latency on large workspaces** — not the checkout issue.
- The full Web team issue list: WEB-1, WEB-2, WEB-6, WEB-8 (all in Todo, no other relations).

So there's no Web team issue assigned to Maya Chen that blocks the Checkout crash on Safari issue, and I didn't change anything.

What would you like to do?
1. Set the estimate to 5 on **WEB-6** (Maya's issue, if you just misremembered what it blocks),
2. Create the missing blocking relationship between WEB-6 and WEB-1 and then set the estimate, or
3. Something else — point me at the right issue and I'll update it.
