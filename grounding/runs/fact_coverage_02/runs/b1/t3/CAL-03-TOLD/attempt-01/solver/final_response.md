dana.whitfield@northwind.example does **not** have an explicit write access rule on the Marketing calendar. Their direct ACL entry grants them **reader** access only.

However, there is a **domain-wide writer rule** for `northwind.example` that grants write access to everyone in that domain, which would effectively give dana.whitfield write access as well. If you'd like to remove their effective write access, you'd need to either:
- Remove the domain-wide writer rule (which affects all northwind.example users), or
- Change dana.whitfield's rule to a different role (though this won't override the domain rule).

Let me know how you'd like to proceed.
