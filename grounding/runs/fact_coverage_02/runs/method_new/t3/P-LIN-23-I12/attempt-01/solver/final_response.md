I found one resolved comment thread on **WEB-5** ("Flaky checkout test"):

- **Comment:** "Timeouts are too short on CI." — authored by **Sam Rivera**, resolved on 2026-06-01.

However, there are two issues preventing me from completing the task:

1. **Can't confirm Maya Chen resolved it:** The `resolvingUser` field on this comment is `null`, so I cannot verify that Maya Chen was the one who resolved it. The `Comment` type in the Linear API doesn't expose a `resolvedBy` field directly.

2. **Cannot reopen via API:** The `commentUpdate` mutation doesn't support clearing `resolvedAt`, and replying to the comment didn't automatically reopen the thread. There is no explicit "reopen thread" operation in the available Linear API mutations.

If you'd like, you can reopen it manually in the Linear UI by replying to the thread or using the "Reopen" button on the resolved thread.
