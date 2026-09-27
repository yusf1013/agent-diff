I checked the **Marketing** calendar (`marketing@northwind.example`) ACL, and there's no user-specific rule for dana.whitfield@northwind.example — so there's nothing individual to remove.

One thing worth flagging: the calendar does have a **domain-wide writer rule** (`northwind.example` → writer), which means Dana currently has write access via the domain, along with everyone else. Removing that would strip write access from the whole domain, not just her — let me know if you want me to do that, or if you'd rather just leave it.
