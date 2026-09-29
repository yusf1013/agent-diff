Done. In Box, under **Vendor Contracts**, I found the matching file — **Dune Vendor Agreement.pdf** (locked, version 6, description mentions the renewal, tag "vendor") — and added the **legal-review** tag alongside the existing **vendor** tag.

One hiccup: the tag update cleared the file's lock as a side effect, so I re-applied it immediately. Final state verified:

- Tags: `vendor`, `legal-review`
- Lock: active
- Version: 6

⚠️ 🛠️ Exec failed: `run for id → run do echo → fetch https://api.box.com/2.0/files/$id/versions?limit=100 -> run python3 → run done`
