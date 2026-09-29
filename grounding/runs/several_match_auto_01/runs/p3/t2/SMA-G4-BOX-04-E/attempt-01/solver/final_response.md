I successfully added the "q3-signoff" tag to the qualifying PDFs in the "Budget Reviews" folder.

**Process:**
1. Found the "Budget Reviews" folder (ID 8100) and listed its 8 PDF files.
2. Checked the tasks on each PDF to identify those with a **review** task that **Leo Park** assigned to **Maya Chen** and that she **approved** (resolution_state = "approved").

**Qualifying files (tagged):**
- `Q3 budget review packet.pdf` (8101)
- `Q3 budget approval packet.pdf` (8109)
- `Q3 expense review packet.pdf` (8110)

**Excluded files and why:**
- `Q3 budget forecast.pdf` (8102) — resolution_state was "completed", not "approved"
- `Q3 budget actuals.pdf` (8103) — assigned to Omar Haddad, not Maya Chen
- `Q3 budget summary.pdf` (8104) — assigned to Maya Lopez, not Maya Chen
- `Q3 budget variance.pdf` (8105) — assigned by Priya Nair, not Leo Park
- `Q3 budget appendix.pdf` (8106) — Maya Chen's assignment was "incomplete"

Verified via final GET requests that all three qualifying files now show `tags: ["q3-signoff"]`.
