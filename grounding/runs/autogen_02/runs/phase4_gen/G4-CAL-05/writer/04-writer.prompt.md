The replica pre-checks found these problems:
- Observability: for the decoy `cle_team-travel-board@northwind.example` (A:CalendarListEntry.summary_override), none of [['cle_team-travel-board@northwind.example'], ['Travel Board']] appears in any read of the replica, so the solver cannot see what sets it apart. Use a field the API returns, or a record the reads show.
- Observability: for the decoy `cle_team-travel-ext@northwind.example` (A:CalendarListEntry.access_role), none of [['cle_team-travel-ext@northwind.example']] appears in any read of the replica, so the solver cannot see what sets it apart. Use a field the API returns, or a record the reads show.

Fix scenario.json (edit it in place), then reply with a short summary of what you changed.