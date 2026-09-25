dana.whitfield@northwind.example does not have a direct write access rule on the Marketing calendar. Their explicit ACL role is **reader** (not writer). 

Note: They do inherit write access indirectly because the entire `northwind.example` domain has a **writer** rule on the calendar. If you want to remove their effective write access, you would need to change the domain-level rule or remove it — but that would affect all users in the domain, not just dana.whitfield.
