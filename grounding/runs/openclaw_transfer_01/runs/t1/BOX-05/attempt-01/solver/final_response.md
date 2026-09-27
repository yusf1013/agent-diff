Done. Here's what I found in your Favorites and what I changed:

**Locked spreadsheets with shared links — links removed:**
- **Headcount plan.xlsx** — shared link removed ✅
- **Vendor spend.xlsx** — shared link removed ✅

**Left untouched (didn't match both criteria):**
- Travel spend.xlsx — locked, but had no shared link to remove
- Office spend.xlsx — has a shared link, but isn't locked
- Pricing.pdf — locked, but it's a PDF, not a spreadsheet
- Budget pack — a folder, not a file

One heads-up: the Box API here didn't have a dedicated "remove shared link" endpoint, so I set `shared_link: null` via the file update, which as a side effect briefly cleared the file locks — I re-applied the locks (same settings, download allowed) right after. Both files now show `shared_link: null` with their locks intact, as verified.
