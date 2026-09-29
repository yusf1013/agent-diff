The rename failed — here's what's going on:

- The calendar **Team calendar** owned by Kenji Sato is `team-kenji@northwind.example`, and its **data owner is `kenji.sato@northwind.example`**.
- The account I'm authenticated as (`jordan.lee@northwind.example`) has read/write access to events (listed as "owner" in the calendar list), but the API returns **403 Forbidden** on `PATCH /calendars` — renaming the calendar itself is a data-owner-only operation.

So I can't actually rename the calendar for everyone with the current credentials. Two options:

1. **Kenji Sato renames it** (or you give me credentials/tokens for his account — not something I'd recommend).
2. **Display override on your end only** — I can set a `summaryOverride` so it shows as "Team calendar (archived)" in *your* calendar view. The underlying calendar name stays "Team calendar" for everyone else.

Want me to go with option 2 as a stopgap?
