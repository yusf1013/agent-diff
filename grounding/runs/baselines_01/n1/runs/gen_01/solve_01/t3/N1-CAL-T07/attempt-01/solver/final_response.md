I found the calendar — `team-kenji@northwind.example` (summary "Team calendar", data owner kenji.sato@northwind.example) — but I can't rename it:

- `PATCH /calendars/team-kenji@...` → **403 Forbidden: "You do not have permission to update this calendar"**
- The calendar's ACL is empty for my account, and I'm authenticated as `jordan.lee@northwind.example`, not Kenji. Only the calendar owner (Kenji Sato) can rename it, and I don't hold edit rights on it.

To unblock this, one of:
1. **Kenji Sato** runs the rename himself, or
2. He grants your account owner/"make changes to events" access on the calendar (I can't grant it from my side), after which I'll apply the rename immediately.

Want me to draft a message to Kenji requesting the access, or is there another account/credential I should be using?
