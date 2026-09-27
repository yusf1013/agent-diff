Found the calendar, but I couldn't change it. Here's what I found:

**Calendar:** "Tokyo office" (`tokyo-office@northwind.example`, Asia/Tokyo timezone)
- It has the **All-hands** event on **June 21** (11:00–12:00 PDT, organized by Aiko Mori) — this is the one.
- It's the only Tokyo-timezone calendar in your account, and the only calendar containing a June 21 all-hands.

**The problem:** when I tried to update its description to "APAC team events", the API returned `403: You do not have permission to update this calendar`. This is odd because the calendar's ACL lists you (`jordan.lee@northwind.example`) as **owner** — Kenji Sato is listed as writer. The permission denial came back consistently on both attempts, so it's not a transient issue; it looks like the account's actual API access doesn't match the ACL (or the owner role is restricted).

So: the calendar exists and I identified it, but I was blocked from editing it. If you have a way to re-grant/repair access on Kenji's side, I can retry immediately.
