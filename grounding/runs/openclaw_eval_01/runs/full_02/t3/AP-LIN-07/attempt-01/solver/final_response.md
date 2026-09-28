Done. There were four docs titled "Draft notes" in the workspace, so I disambiguated by content and team:

- **Renamed** (Growth, referral program pilot): "Draft notes" → **"Referral pilot — launch notes"**
- Left untouched: a second Growth "Draft notes" (office move logistics), one on the referral pilot belonging to the **Platform** team, and one with no team assigned.

Verified via a follow-up query that only the intended document changed.

One note: the Linear API's `documentUpdate` mutation returns a broken payload in this environment (`success` comes back null on a non-nullable field, so it errors even when the write succeeds) — the rename itself is confirmed persisted, but worth flagging if you rely on that mutation's response elsewhere.
