I was unable to grant Aiko Mori edit access to Maya's team calendar (`maya-team@northwind.example`, owned by maya.chen@northwind.example). The API returned a 403 "You do not have permission to modify ACL for this calendar" error because I only have **writer** access to that calendar, and modifying ACL/sharing settings requires **owner** permissions. 

To complete this, either maya.chen@northwind.example (the owner) must add Aiko Mori (likely aiko.mori@northwind.example) with the `writer` role via the calendar sharing settings, or I would need to be granted owner access to the calendar.
