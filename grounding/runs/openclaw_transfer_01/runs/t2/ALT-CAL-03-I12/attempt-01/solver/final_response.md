No rule found — I checked the ACL on the **Marketing** calendar (`marketing@northwind.example`) and there's no individual permission entry for dana.whitfield@northwind.example, so there's nothing specific to remove.

Worth knowing: the calendar does have a **domain-wide writer rule** for the whole `northwind.example` domain. That's what's actually giving Dana write access today. If you want her specifically blocked, you'd need to remove that domain rule (which would also revoke write access for everyone else at Northwind) — say the word and I'll do that instead.
