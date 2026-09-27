The replica pre-checks found these problems:
- Observability: for the decoy `9506` (R:Folder.collections), none of [['Compliance Review']] appears in any read of the replica, so the solver cannot see what sets it apart. Use a field the API returns, or a record the reads show.

Fix scenario.json (edit it in place), then reply with a short summary of what you changed.