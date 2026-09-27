I checked the Marketing calendar (`marketing@northwind.example`) and there's no ACL entry for **dana.whitfield@northwind.example** — so there's no write access of hers to remove.

One thing worth knowing: the calendar does have a **domain-wide writer rule** (role: writer, scope: northwind.example), which means dana *does* indirectly have write access through that rule. If you want her access removed, the options are:

1. Delete the domain-level writer rule (removes write access for **everyone** at northwind.example)
2. Leave it as-is, since there's no per-user rule to revoke

There's also a "Marketing Events" calendar — I can check its ACL too if you meant that one instead. Just say the word.
