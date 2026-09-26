I've hidden the **Team Calendar** (`team-launch@northwind.example`) from your calendar list. You had **writer** access to it, which made it the only "Team Calendar" matching your criteria. 

One note: I was unable to independently verify the "shared with the design team as a writer" detail because the API returned a 403 when I tried to read that calendar's ACL (you have writer access, not owner-level). However, since it was the only "Team Calendar" you had writer access to, it's the right one. The calendar is now set to `hidden: true`.
