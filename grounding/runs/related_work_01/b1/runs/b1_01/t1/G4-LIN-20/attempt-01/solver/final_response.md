I found the target — WEB-1 "Checkout latency spikes", and Maya Chen's only top-level comment mentioning the rollback plan ("The rollback plan is drafted and ready for review.", comment `e2aca69a`).

However, the Linear API here has **no comment-edit capability** — the available comment mutations are only `commentCreate`, `commentDelete`, `commentResolve/Unresolve`. So the only way to "append" is to **delete the original comment and recreate it** with the new text.

One caveat: that would lose the original timestamp and comment ID, and it's irreversible (no un-delete). Since it's a teammate's public comment, I don't want to delete it without your OK.

How do you want to proceed?
1. **Delete + recreate** — comment text becomes "The rollback plan is drafted and ready for review. Approved." (fresh timestamp, new ID)
2. **Reply instead** — leave the original untouched and add a "Approved." reply underneath it
3. Something else
