There is no specific access control rule for **dana.whitfield@northwind.example** on the Marketing calendar (`marketing@northwind.example`). The current ACL rules are:

1. **domain:northwind.example** → writer (this domain-wide rule would grant dana.whitfield write access, along with all other users in the northwind.example domain)
2. **user:jordan.lee@northwind.example** → owner

If you want to remove dana.whitfield's write access specifically, you'd need to modify or remove the domain-wide `northwind.example` writer rule, which would affect all users in that domain. Let me know if you'd like me to proceed with that.
