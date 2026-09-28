Successfully moved the Web team's "Blocked" workflow state to the Mobile team. Since Linear has no direct "move state" API, I:
1. Created a new "Blocked" state (type: started, color: #f42335) on the Mobile team.
2. Moved the one issue in the Web Blocked state (WEB-2 "Payment page slow") into the new Mobile Blocked state (this was required because a state can't be archived while it contains unarchived issues).
3. Archived the Web team's old "Blocked" state.

Verification confirms the Mobile "Blocked" state is active and the Web "Blocked" state is archived, with the issue now correctly placed in Mobile's Blocked state.
