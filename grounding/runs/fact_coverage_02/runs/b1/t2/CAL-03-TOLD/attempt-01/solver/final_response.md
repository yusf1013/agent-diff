Dana Whitfield (dana.whitfield@northwind.example) does **not** have a direct write (writer) role on the Marketing calendar. Their individual ACL rule grants them **reader** access only.

However, there is a **domain-wide writer rule** for `northwind.example` that would grant write access to all users on that domain, including Dana. If you want to remove their write access specifically, you'd need to either:

1. **Remove the domain-wide writer rule** (`northwind.example`) — but this would affect everyone on the domain.
2. **Override it** — Unfortunately, Google Calendar's ACL model doesn't support per-user "deny" overrides against a broader rule.

Let me know how you'd like to proceed!
