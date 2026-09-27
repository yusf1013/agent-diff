I found the calendar that fits your description, but I couldn't make the change:

- **Calendar found:** `tokyo-office@northwind.example` ("Tokyo office") — the only Asia/Tokyo calendar in your account, and it contains the **All-hands event on June 21** (11:00–12:00, organized by Aiko Mori; Kenji Sato has writer access to it).
- **What happened:** When I tried to update its description to "APAC team events," the API returned **403 — "You do not have permission to update this calendar"** (retried twice, same result). Per the ACL, Kenji Sato is only a *writer* on it; the calendar's data owner is Aiko Mori, and the authenticated account lacks owner/admin rights over it.

So the calendar exists, but I'm blocked by permissions. If you have an account with owner rights (or Aiko does), the one-line change would be to update the calendar's `description` field — happy to retry if access changes.
