I found a snag: you have **two** "Team Calendar" entries with writer access, and I can't tell them apart from the data I can see:

1. **Team Calendar** (owner: sam.rivera@northwind.example)
2. **Team Calendar** (owner: kenji.sato@northwind.example)

Both are currently visible in your calendar list, both have no events, and I don't have permission to read either calendar's sharing settings (that requires owner access), so I can't confirm which one is shared with the design team. There's no note in my memory about it either.

Which one should I hide — the **sam.rivera** one or the **kenji.sato** one? (Or if you know the calendar ID, send that.) Once you confirm, I'll hide it right away.

⚠️ 🛠️ Exec failed: `run for id → run do echo → fetch https://www.googleapis.com/calendar/v3/calendars/$id/acl -> run jq → run done`
