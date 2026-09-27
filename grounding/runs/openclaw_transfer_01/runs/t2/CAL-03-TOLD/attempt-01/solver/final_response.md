Checked the Marketing calendar (`marketing@northwind.example`) ACL, and here's the situation:

**dana.whitfield@northwind.example doesn't have her own writer rule.** Her direct access is only **reader**. However, she *does* have effective write access because there's a **domain-wide writer rule** for `northwind.example` — meaning everyone on that domain (including her, and dana.white separately) can write.

So the options are:

1. **Remove the domain writer rule** — this strips write access from *every* `northwind.example` user, not just Dana.
2. **Leave it as-is** if the domain-wide writer access is intended.

I didn't touch anything since option 1 would affect all your team members. Want me to remove the domain-level writer rule, or was Dana supposed to have individual write access that you'd rather grant/revoke per-person?
