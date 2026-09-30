Found the folder — **Vendor Contracts 2024** (ID 9500) — created June 3, 2026, in the Legal Hold collection, last modified by Priya Nair (June 15), with exactly 3 items (Contract A/B/C.pdf).

But tagging it isn't possible: the Box API only supports tags on **files**, not folders. I tried `PUT /folders/9500` with `{"tags":["archive-ready"]}` and it returned **405 Method Not Allowed** — the Box API has no update endpoint for folders at all.

If the goal is marking it for archiving, I can instead:
- Add a description to the folder (not supported via API either, unfortunately — same limitation)
- Move it to an "Archive" collection/folder, or rename it with an "archive-ready" marker
- Tag the 3 files inside with `archive-ready`

Want me to do any of those?
