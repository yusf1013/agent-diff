I located the target but hit a hard blocker. Here's what I found and why I can't complete it via the API.

**Target (confirmed):**
- Issue: **WEB-1 "Checkout latency spikes"** (id `fd686c45-06f0-4ee2-a12b-ac87a9506246`)
- Top-level comment by **Maya Chen** (maya.chen@northwind.example) mentioning the rollback plan:
  - id: `e2aca69a-30c5-409a-b5c3-85af87ea9f76`
  - Body: *"The rollback plan is drafted and ready for review."* (parent = null, so it's top-level ✓)

I ruled out the look-alikes: Maya's reply *inside* Leo's thread, Maya Lopez's (a different person), and Sam Rivera's comment that merely mentions "Maya Chen's estimate." The one above is the correct match.

**The blocker:** The Linear GraphQL API does **not** expose a comment-update mutation. The only comment mutations available are `commentCreate`, `commentDelete`, `commentResolve`, and `commentUnresolve`. There's no `commentUpdate`/`commentEdit`, so there's no way to append text to an existing comment's body through the API.

I'm also authenticated as **Jordan Lee** (jordan.lee@northwind.example), not Maya Chen. The only "workaround" would be to delete Maya's comment and recreate it with "Approved." appended — but that would:
1. Destructively delete another person's original comment, and
2. Re-author it as Jordan Lee, falsely changing who wrote it.

I'm not going to do that — it would misrepresent authorship and destroy the original.

**Options:**
1. **You (or Maya) edit it in the Linear UI** — append "Approved." to the comment on WEB-1. This is the clean, correct path.
2. If you have Linear admin/API capabilities that add an edit endpoint, point me at it and I'll retry.

Want me to go ahead with anything else on this issue (e.g., post "Approved." as a *new* top-level comment from Jordan Lee instead, so the approval is on record without touching Maya's comment)?
