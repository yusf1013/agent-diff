Deleted all Friday (June 22, 2018) architecture review events where Kenji Sato (kenji.sato@northwind.example) attends as an optional guest:

1. **"Architecture review"** (10:00–11:00) — `ev_ar_target` — Kenji Sato optional ✓ deleted
2. **"Architecture review sync"** (10:00–11:00) — `ev_ar_target_sm0v` — Kenji Sato optional ✓ deleted
3. **"Architecture review Q4"** (10:00–11:00) — `ev_ar_target_sm1v` — Kenji Sato optional ✓ deleted

Correctly left in place (did not match criteria):
- **"Architecture review: storage"** — Kenji Sato attends but as a *required* (non-optional) guest
- **"Architecture review: search"** — the optional guest is Kenji **Satou** (kenji.satou@northwind.example), a different person

All three deletions returned HTTP 204, and a follow-up list confirmed only the two non-matching events remain.
