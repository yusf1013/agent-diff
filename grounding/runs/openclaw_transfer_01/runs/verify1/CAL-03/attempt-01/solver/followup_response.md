Done. I removed the domain-wide writer rule on the Marketing calendar:

- `northwind.example` (domain) → **writer → reader**

Verified in the updated ACL. Dana Whitfield now has read-only access (via her own reader rule, and the domain rule no longer grants write to anyone in the company).

Two heads-ups:

1. **All other northwind.example users** also lost write access — that domain rule applied to everyone in the company. If other teammates need write access, I can add them individually.
2. **dana.white@northwind.example still has an explicit writer rule.** I only changed the domain rule (which was the one actually granting Dana Whitfield write access). If you also want to downgrade Dana White, just say so.
