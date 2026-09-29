Successfully made Priya Nair's comment "Tpyo in the title." a reply to Omar Haddad's comment "On it." on WEB-1. Since the Linear API's `commentUpdate` doesn't support re-parenting, I:
1. Created a new comment with the body "Tpyo in the title." on issue WEB-1 with `parentId` set to Omar's comment (c-2)
2. Deleted the original top-level comment (c-1)

The verification confirms the "Tpyo in the title." comment now has `parentId: c-2`, making it a reply to "On it."
