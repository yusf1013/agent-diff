Granted Sam Rivera (sam.rivera@northwind.example) read access (role "reader") to all three calendars whose description says it is for the London office:
- emea@northwind.example ("EMEA team")
- emea@northwind.example-sm49 ("London team")
- emea@northwind.example-sm50 ("London ops")

I excluded calendars that merely had "London" in their summary or location (e.g. the "London office" calendar whose description actually says Paris, and "UK sites" whose description says Berlin), since the task required matching on the description field. All three ACL rules were verified as successfully created.
