Task not achievable via the Box API from this account.

Summary of investigation:
- I am authenticated as **Jordan Lee** (user id 30000000001), not Leo Park.
- The **Finance folder** (id 7100) currently has `modified_by` = Jordan Lee.
- In Box, the `modified_by` field is a **read-only** attribute. Box automatically sets it to the *authenticated user who performs the last modification*. There is no API endpoint or request parameter to assign `modified_by` to a specific user, nor a way to act as another user.

Because any modification I (Jordan Lee) make would set *me* — not Leo Park — as the last modifier, there is no API action I can take to accomplish this goal. To make Leo Park the last modifier, **Leo Park (authenticated as Leo Park)** would need to perform a modification on the Finance folder (e.g., rename it, add a tag, or move it), or a system/admin-level process would need to update the metadata. No such operation is available to me from Jordan Lee's account.
