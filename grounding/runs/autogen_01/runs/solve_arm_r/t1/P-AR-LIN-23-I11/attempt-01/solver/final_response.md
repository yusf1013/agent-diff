I found the comment thread on **WEB-7** ("Investigate flaky checkout tests"). It's comment **c-f1** by **Sam Rivera**:

> "Payment retry attempts still time out under load; can we add a backoff?"

It was resolved on **2026-08-04** at 09:00. However, I was **unable to reopen it** through the Linear API. The `commentUpdate` mutation's input type (`CommentUpdateInput`) only exposes fields like `body`, `resolvingCommentId`, and `resolvingUserId` — there is no `resolvedAt` field to clear, and passing `null` for nullable GraphQL input fields is interpreted as "don't change" rather than "set to null." This appears to be an API limitation that prevents programmatically unresolving a comment. You'd need to reopen it from the Linear UI instead.
