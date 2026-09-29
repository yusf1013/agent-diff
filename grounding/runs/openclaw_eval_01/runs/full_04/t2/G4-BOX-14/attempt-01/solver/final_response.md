Done. **Harbor Vendor Agreement.pdf** in Vendor Contracts now has the `legal-review` tag added.

Summary:
- **File matched:** Harbor Vendor Agreement.pdf (ID 7101) — the only one in the folder that was locked, at version 6, and tagged `renewal` (Beacon was v5, so it didn't match).
- **Tags:** `renewal`, `legal-review`
- **State preserved:** The file is still locked (download allowed, as before), still at version 6.

One note: updating tags via the API briefly cleared the lock as a side effect, so I re-applied it immediately after — final state verified above.

⚠️ 🛠️ Exec failed: `for id in 7101 7102; do echo "=== $id versions ===" curl -s….box.com/2.0/files/$id/versions" | python3 -m json.tool done`
