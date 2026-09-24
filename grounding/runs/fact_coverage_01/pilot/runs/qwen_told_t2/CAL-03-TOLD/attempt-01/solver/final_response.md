There is no direct **writer** ACL rule for dana.whitfield@northwind.example on the Marketing calendar. Her direct role is **reader** only.

However, she does inherit **writer** access through a **domain-level rule** that grants "writer" to everyone in `northwind.example`. Removing that domain rule would revoke write access for *all* northwind.example users, not just Dana.

If you'd like, I can:
1. **Remove the domain writer rule** for northwind.example (affects everyone in the domain), or
2. **Remove Dana's direct reader rule** as well (so she has no explicit individual access).

Let me know how you'd like to proceed.
