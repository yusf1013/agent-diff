You write test requests for an AI agent that acts in a workspace on a user's behalf. You are careful with
wording: a test request must read exactly as a real user would write it, and must ask for exactly what is intended.

---

Each item below is a request that asks the agent to act on ONE record in Box. For each item:

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
3. Write `search_words`: the one to three words a user would type into Box's search box to look for these
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
  "id": "BOX-21",
  "record": "a Box folder",
  "request": "In my Favorites, add the tag audit-ready to the folder Leo Park last modified that was created in August 2026 and holds exactly two files.",
  "text_field": "name",
  "current_value": "Audit binder"
 },
 {
  "id": "BOX-23",
  "record": "a Box file",
  "request": "Add the tag renewal to the contract PDF whose description mentions the Initech renewal, that is larger than 2 MB and has at least three comments.",
  "text_field": "name",
  "current_value": "Initech MSA.pdf"
 },
 {
  "id": "BOX-24",
  "record": "a Box task",
  "request": "Move the due date to October 20, 2026 on the task pat.kim@northwind.example created on September 14 asking to check the indemnity clause.",
  "text_field": "message",
  "current_value": "Please check the indemnity clause"
 },
 {
  "id": "AR-BOX-21",
  "record": "a Box folder",
  "request": "Add the tag archive-ready to the folder that was created on June 3, 2026, that Priya Nair modified last, that's in the Legal Hold collection, and that has exactly 3 items directly in it.",
  "text_field": "name",
  "current_value": "Vendor Contracts 2024"
 },
 {
  "id": "AR-BOX-22",
  "record": "a Box file",
  "request": "In the Client Docs hub that Dana Whitfield last updated, add the tag 'renewed' to the file named 'Vendor Agreement.pdf'.",
  "text_field": "name",
  "current_value": "Vendor Agreement.pdf"
 },
 {
  "id": "AR-BOX-23",
  "record": "a Box file",
  "request": "Add the tag design-review to the PDF in the Product Specs folder whose description mentions the mobile redesign, is under 2 MB, and has exactly 3 comments on it, not counting replies.",
  "text_field": "name",
  "current_value": "Mobile Nav Redesign Spec.pdf"
 },
 {
  "id": "AR-BOX-24",
  "record": "a Box task",
  "request": "On Vendor Agreement.pdf, push the due date to July 15 for the task dana.whitfield@northwind.example created on June 3 asking for the pricing table to be redone.",
  "text_field": "message",
  "current_value": "Please redo the pricing table in Section 2."
 },
 {
  "id": "AP-BOX-01",
  "record": "a Box folder",
  "request": "Add the tag ready-for-review to the folder in the Legal Archive that holds more than 800 MB of files, has a shared link open to anyone, and was modified after August 15, 2026.",
  "text_field": "name",
  "current_value": "Discovery Production Set"
 },
 {
  "id": "AP-BOX-02",
  "record": "a Box file",
  "request": "Add the tag needs-legal-review to the file Dana Whitfield created on June 3 that got a comment from Priya Nair on June 10.",
  "text_field": "name",
  "current_value": "Vendor Agreement.pdf"
 },
 {
  "id": "AP2-BOX-01",
  "record": "a Box folder",
  "request": "Add the tag needs-audit to the folder under Client Deliverables that's larger than 2 GB, has a shared link on it, and hasn't been modified since May 1.",
  "text_field": "name",
  "current_value": "Northwind Retainer"
 },
 {
  "id": "AP2-BOX-02",
  "record": "a Box file",
  "request": "Add the tag needs-follow-up to the file in the Vendor Contracts folder that Dana Whitfield owns, that was uploaded before June 15, and that has a comment from Priya Nair posted on June 20.",
  "text_field": "name",
  "current_value": "Master Services Agreement.pdf"
 },
 {
  "id": "G4-BOX-01",
  "record": "a Box file",
  "request": "Add the tag launch-ready to the PDF in the Launch Assets folder with a top-level comment by Dana Whitfield saying 'approved for launch'.",
  "text_field": "name",
  "current_value": "Launch checklist.pdf"
 },
 {
  "id": "G4-BOX-03",
  "record": "a Box file",
  "request": "Add the tag verified to the shared spreadsheet in the Budgets folder that Maya Chen uploaded and that was last modified on June 8.",
  "text_field": "name",
  "current_value": "Q3 budget review.xlsx"
 },
 {
  "id": "G4-BOX-04",
  "record": "a Box file",
  "request": "Add the tag q3-signoff to the PDF in the Budget Reviews folder with the review task Leo Park assigned to Maya Chen that she approved.",
  "text_field": "name",
  "current_value": "Q3 budget review packet.pdf"
 },
 {
  "id": "G4-BOX-05",
  "record": "a Box file",
  "request": "Add the tag q3-close to the PDF in the Finance Reports folder owned by Maya Chen that Leo Park modified last.",
  "text_field": "name",
  "current_value": "Q3 revenue summary.pdf"
 },
 {
  "id": "G4-BOX-06",
  "record": "a Box folder",
  "request": "Add the tag launch-ready to the folder that Dana Whitfield owns, that sits directly in the Marketing folder (not in its subfolders), and that Leo Park created.",
  "text_field": "name",
  "current_value": "Summer Launch"
 },
 {
  "id": "G4-BOX-07",
  "record": "a Box hub",
  "request": "Set the description of the Product Launch hub that includes the Field Photos folder and the Launch Plan file to 'Archived launch kit'.",
  "text_field": "title",
  "current_value": "Product Launch"
 }
]
