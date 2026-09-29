You write test requests for an AI agent that acts in a workspace on a user's behalf. You are careful with
wording: a test request must read exactly as a real user would write it, and must ask for exactly what is intended.

---

Each item below is a request that asks the agent to act on ONE record in Google Calendar. For each item:

1. Decide `plural_worthy`: could a real user plausibly ask the same thing about SEVERAL records at once, because
   several records can meet the same conditions? (Example: "Cancel the 8 a.m. meeting with Dana" -> "Cancel all the
   8 a.m. meetings with Dana" is plausible.) Answer false when the request picks out one record by something only
   one record can have (an exact unique title or name, "the most recent", "the one that...", a record the
   conditions make unique by nature), or when doing the action to several records makes no sense. Give the reason.
2. Write `plural_request`: the request rewritten to ask for every record that meets the same conditions.
   - Keep every condition of the original, word for word where you can, and add no new condition.
   - Keep the action and its values (tags, dates, names, emoji) unchanged.
   - Say it the way a user would ("every", "all", plural nouns).
   - Do not say where the records are beyond what the original says: no "including ...", "on any calendar",
     "in all channels", "hidden", "private", "archived", "subfolders", "every page", "anywhere".
   If `plural_worthy` is false, still write your best plural wording.
3. Write `search_words`: the one to three words a user would type into Google Calendar's search box to look for these
   records (content words, no search operators).
4. Write `variants`: three different values of the record's main text that a real record meeting EVERY condition of
   the request could have. Keep every word or phrase a condition needs (a quoted phrase, a topic, a file extension,
   a name the condition checks) and change the rest, so the three read like three different real records.
   The current value is given. Keep each variant about as long as the current value.

Answer with JSON: {"items": [{"id", "plural_worthy", "reason", "plural_request", "search_words", "variants"}]},
one entry per item, in the same order.

Items:
[
 {
  "id": "CAL-21",
  "record": "a Google Calendar event",
  "request": "Move the planning session that ends at 5pm on Thursday and whose description mentions the Q4 roadmap to Room 2B.",
  "text_field": "summary",
  "current_value": "Planning session"
 },
 {
  "id": "CAL-22",
  "record": "a Google Calendar calendar",
  "request": "Give Sam Rivera (sam.rivera@northwind.example) read access to the calendar whose description says it is for the London office.",
  "text_field": "summary",
  "current_value": "EMEA team"
 },
 {
  "id": "CAL-23",
  "record": "a Google Calendar event",
  "request": "Delete Friday's architecture review that Kenji Sato (kenji.sato@northwind.example) attends as an optional guest.",
  "text_field": "summary",
  "current_value": "Architecture review"
 },
 {
  "id": "CAL-24",
  "record": "a Google Calendar calendar",
  "request": "Set the description of my calendar located in Tokyo to \"APAC offsite planning\".",
  "text_field": "summary",
  "current_value": "APAC events"
 },
 {
  "id": "AR-CAL-21",
  "record": "a Google Calendar event",
  "request": "Move the client sync about finalizing the Meridian contract that ends at 3:30 pm to Room 4C.",
  "text_field": "summary",
  "current_value": "Client sync"
 },
 {
  "id": "AR-CAL-22",
  "record": "a Google Calendar calendar",
  "request": "Change the time zone to America/New_York on the Ops Rotation calendar I own whose description mentions weekend on-call coverage.",
  "text_field": "summary",
  "current_value": "Ops Rotation \u2013 NORAM"
 },
 {
  "id": "AR-CAL-23",
  "record": "a Google Calendar event",
  "request": "Move the vendor sync on Thursday that has Dana Whitfield as an optional attendee to Room 2C.",
  "text_field": "summary",
  "current_value": "Vendor sync: Packaging"
 },
 {
  "id": "AR-CAL-24",
  "record": "a Google Calendar calendar",
  "request": "Update the description of the Front Desk calendar located at Building 4, 3rd Floor to say that badge access is required after 6 pm.",
  "text_field": "summary",
  "current_value": "Front Desk"
 },
 {
  "id": "AP-CAL-01",
  "record": "an entry in the user's Google Calendar list",
  "request": "Please hide the 'Client Success' calendar that I've already unchecked, so it stops appearing in my calendar list altogether.",
  "text_field": "summary_override",
  "current_value": null
 },
 {
  "id": "AP-CAL-02",
  "record": "a Google Calendar calendar",
  "request": "Hide the Team Calendar that I have writer access to on my calendar list, and that's shared with the design team as a writer.",
  "text_field": "summary",
  "current_value": "Team Calendar"
 },
 {
  "id": "AP2-CAL-01",
  "record": "a Google Calendar calendar",
  "request": "Rename the 'Product Team' calendar that I currently have checked to 'Eng Product Sync'.",
  "text_field": "summary",
  "current_value": "Product Team"
 },
 {
  "id": "AP2-CAL-02",
  "record": "a Google Calendar calendar",
  "request": "Hide the 'Design Team' calendar in my calendar list that I've shared with Kenji Sato as a writer.",
  "text_field": "summary",
  "current_value": "Design Team"
 },
 {
  "id": "G4-CAL-01",
  "record": "a Google Calendar event",
  "request": "Move the Budget Review starting at 10am on Thursday, organized by Dana Whitfield, to Room 5B \u2014 it's blocking time on my calendar.",
  "text_field": "summary",
  "current_value": "Budget Review"
 },
 {
  "id": "G4-CAL-02",
  "record": "a Google Calendar event",
  "request": "Set the color of the sprint retrospective in Room 5B created by Kenji Sato to red.",
  "text_field": "summary",
  "current_value": "Sprint retrospective"
 },
 {
  "id": "G4-CAL-03",
  "record": "a Google Calendar event",
  "request": "On my primary calendar, move the Budget review with Maya Chen on Thursday to Room 5B.",
  "text_field": "summary",
  "current_value": "Budget review"
 },
 {
  "id": "G4-CAL-04",
  "record": "a Google Calendar event",
  "request": "Move the budget review on Friday organized by Maya Chen to Room 5B.",
  "text_field": "summary",
  "current_value": "Budget review: Q2 close"
 },
 {
  "id": "G4-CAL-05",
  "record": "a Google Calendar calendar",
  "request": "Hide the calendar I call Team Travel that's showing in my calendar list and that I own.",
  "text_field": "summary",
  "current_value": "Shared Travel Schedule"
 },
 {
  "id": "G4-CAL-06",
  "record": "a Google Calendar event",
  "request": "Move the Thursday quarterly planning lunch on Leo Park's calendar set to New York time to Room 5B.",
  "text_field": "summary",
  "current_value": "Quarterly planning lunch"
 },
 {
  "id": "G4-CAL-07",
  "record": "a Google Calendar event",
  "request": "Move the Quarterly planning meeting scheduled for this Thursday that Dana Whitfield declined to Room 5B.",
  "text_field": "summary",
  "current_value": "Quarterly planning"
 }
]
