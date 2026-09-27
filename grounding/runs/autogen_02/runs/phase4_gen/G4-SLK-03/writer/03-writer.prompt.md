The replica pre-checks found these problems:
- Observability: for the decoy `1789993800.000003` (D:latest_message), none of [['2026-09-21']] appears in any read of the replica, so the solver cannot see what sets it apart. Use a field the API returns, or a record the reads show.
- Observability: for the decoy `1789994100.000004` (D:latest_message), none of [['2026-09-21']] appears in any read of the replica, so the solver cannot see what sets it apart. Use a field the API returns, or a record the reads show.

Fix scenario.json (edit it in place), then reply with a short summary of what you changed.