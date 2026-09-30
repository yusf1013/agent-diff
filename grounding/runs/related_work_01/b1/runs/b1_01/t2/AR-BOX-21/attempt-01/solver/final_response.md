Here's where things landed:

**Target identified:** `Vendor Contracts 2024` (folder 9500)
- Created 2026-06-03 ✓
- Last modified by Priya Nair (2026-06-15) ✓ — the only other June 3 + Priya candidate, `Vendor Filings`, was eliminated: it has 1 item, not 3
- In the Legal Hold collection ✓
- Exactly 3 direct items: Contract A.pdf, Contract B.pdf, Contract C.pdf ✓

**Problem:** I couldn't add the tag. This Box environment has no folder-update endpoint — `PUT /folders/9500` returns **405 Method Not Allowed** (verified with plain PUT, If-Match, box-version header, name+tags body, PATCH, and a `/tags` subresource probe — all 405/404). The `tags` field is readable on folders (`tags: []`) but there's no write path exposed, unlike files, which do accept PUT.

**Cleanup:** While probing, I accidentally tagged `Contract A.pdf` (95001) to test file PUT — I've reset its tags to empty, so no side effects remain.

The folder itself is untouched and correct. If you have a different endpoint or admin access that supports `PUT /folders/{id}`, let me know and I'll retry — otherwise this account's Box API surface simply doesn't allow folder tag updates.
