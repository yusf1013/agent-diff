Done. Added `legal-review` to **Harbor Vendor Agreement.pdf** in Vendor Contracts (the one matching all criteria: locked, tagged `renewal`, version 6 — Beacon was version 5, so it's out).

Verified final state:
- **Tags:** `renewal`, `legal-review`
- **Lock:** active

One hiccup worth flagging: the tag update API call unexpectedly cleared the file lock, so I re-applied it immediately afterward and confirmed it's back in place. If your team was relying on that lock, it's restored to the same state it was in before.
