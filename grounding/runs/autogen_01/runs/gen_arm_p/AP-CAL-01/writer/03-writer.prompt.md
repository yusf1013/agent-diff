The replica pre-checks found these problems:
- Observability: for the decoy `cle_cs-south@northwind.example` (A:CalendarListEntry.selected), none of [['cle_cs-south@northwind.example']] appears in any read of the replica, so the solver cannot see what sets it apart. Use a field the API returns, or a record the reads show.
- Write feasibility: the write call succeeded but did not change the target in `calendar_list_entries` as the effect locator expects (changed: []).

Fix scenario.json (edit it in place), then reply with a short summary of what you changed.