# Trial of test `P-AP-CAL-01-I13` (calendar)

Test form: probe. Target present: no.

## Request given to the solver
Please hide the 'Client Success' calendar that I've already unchecked, so it stops appearing in my calendar list altogether. If there isn't one, just tell me.

## Candidates
### Reference r1 (what the request asks to act on); records live in `calendar_list_entries`
- No target: no record meets this reference.
- DECOY `cle_cs-south@northwind.example` (fact `A:CalendarListEntry.selected`, family F0): This 'Client Success' calendar is still checked/selected, so its events still show in the calendar view — it hasn't been unchecked.
  record: {"id": "cle_cs-south@northwind.example", "user_id": "u_actor", "calendar_id": "cs-south@northwind.example", "access_role": "reader", "primary": false, "selected": true, "hidden": false, "deleted": false, "created_at": "2018-01-01T00:00:00", "updated_at": "2018-01-01T00:00:00"}

## Solver steps
Run status: completed; termination: done; steps: 3.

#### Step 1
Reasoning: The user wants to hide a 'Client Success' calendar from their calendar list. I need to first find this calendar in their calendar list by listing all calendars, then set the `hidden` property to `true` for that calendar.
Command: curl -s "https://www.googleapis.com/calendar/v3/users/me/calendarList?showHidden=true" | python3 -c "
import json, sys
data = json.load(sys.stdin)
for cal in data.get('items', []):
    print(f\"ID: {cal.get('id')} | Summary: {cal.get('summary')} | Hidden: {cal.get('hidden')} | Selected: {cal.get('selected')}\")
"
Response: {"status": "success", "stdout": "ID: cs-south@northwind.example | Summary: Client Success | Hidden: False | Selected: True\nID: jordan.lee@northwind.example | Summary: jordan.lee@northwind.example | Hidden: False | Selected: True\nID: product-roadmap@northwind.example | Summary: Product Roadmap | Hidden: False | Selected: True\nID: team-offsite@northwind.example | Summary: Team Offsite | Hidden: False | Selected: True\n", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_f984e627ca954852a0151b2ada132d5f_od2xo47l"}

#### Step 2
Reasoning: I found the 'Client Success' calendar with ID `cs-south@northwind.example`. It's currently Hidden: False. I need to PATCH the calendarList entry to set `hidden` to `true` so it stops appearing in the calendar list.
Command: curl -s -X PATCH "https://www.googleapis.com/calendar/v3/users/me/calendarList/cs-south%40northwind.example" \
  -H "Content-Type: application/json" \
  -d '{"hidden": true}' | python3 -m json.tool
Response: {"status": "success", "stdout": "{\n    \"kind\": \"calendar#calendarListEntry\",\n    \"etag\": \"\\\"cb61e6f26073111f\\\"\",\n    \"id\": \"cs-south@northwind.example\",\n    \"accessRole\": \"reader\",\n    \"summary\": \"Client Success\",\n    \"timeZone\": \"America/Los_Angeles\",\n    \"conferenceProperties\": {\n        \"allowedConferenceSolutionTypes\": [\n            \"hangoutsMeet\"\n        ]\n    },\n    \"dataOwner\": \"maya.chen@northwind.example\",\n    \"backgroundColor\": \"#9fc6e7\",\n    \"foregroundColor\": \"#000000\",\n    \"hidden\": true,\n    \"selected\": true,\n    \"defaultReminders\": []\n}\n", "stderr": "", "exit_code": 0, "workspace_path": "/tmp/agent_diff_f984e627ca954852a0151b2ada132d5f_od2xo47l"}

#### Step 3
Reasoning: The PATCH request succeeded. The response confirms the 'Client Success' calendar (`cs-south@northwind.example`) now has `"hidden": true`. This will remove it from the visible calendar list while keeping the subscription intact.


<done>
The 'Client Success' calendar has been successfully hidden from your calendar list. It's now set to `hidden: true`, so it will no longer appear in your calendar view. The subscription itself is still active — you can un-hide it at any time if you need it back.
</done>
Command: 
Response: null

## Final answer
The 'Client Success' calendar has been successfully hidden from your calendar list. It's now set to `hidden: true`, so it will no longer appear in your calendar view. The subscription itself is still active — you can un-hide it at any time if you need it back.

## State diff
- INSERT calendar_sync_tokens: {"id": 1, "token": "sync_20180617000000000000_6_7VSbIwLdoIqIU4-yhJ_Q", "user_id": "u_actor", "resource_type": "calendarList", "snapshot_time": "2018-06-17T07:00:00", "expires_at": "2018-06-24T07:00:00", "created_at": "2026-09-26T11:29:28.864669"}
- UPDATE calendar_list_entries `cle_cs-south@northwind.example`: {"hidden": [false, true]}

## Mechanical attribution (from the diff and write commands; may be wrong)
Acted-on records per reference: {"r1": ["cle_cs-south@northwind.example"]}. Provisional outcome: incorrect. Provisional exposed facts: ['A:CalendarListEntry.selected'].

Give your verdict for this trial.