I found the calendar but can't change it — here's the situation:

**Target calendar:** `kenji-team@northwind.example` ("Kenji team")
- Owned by Kenji Sato, timezone Asia/Tokyo (his only Tokyo-time calendar)
- Contains the all-hands (event `ev_ah4` around the June 21 window)

**The problem:** I only have **writer** access on it, which allows adding events but not editing calendar settings. The PATCH to update its description returned:

> 403 — "You do not have permission to update this calendar"

To fix this, Kenji Sato (or someone with full control of the calendar) would need to grant **owner** access to `jordan.lee@northwind.example`. Once that's done, I can set the description to "APAC team events" right away.

Note: the other Tokyo-time calendar (`tokyo-office`) is Aiko Mori's, not Kenji's, so it isn't the right target. Want me to do anything else in the meantime?
