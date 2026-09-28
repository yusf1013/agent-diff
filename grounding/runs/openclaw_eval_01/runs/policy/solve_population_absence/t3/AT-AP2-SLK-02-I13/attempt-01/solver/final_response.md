I checked all channels in the workspace (both public and private, including archived ones to be safe). Here's what exists:

| Channel | Name has "incident" | Topic mentions postmortems | Archived |
|---|---|---|---|
| `engineering` | ✗ | ✗ | no |
| `incident-2019-retro` | ✓ | ✗ ("Archived project artifacts") | **yes** |
| `incident-response-archive` | ✓ | ✓ ("Postmortems and outage retros for closed incidents") | **yes** |

**No channel matches all three criteria.** The only channel whose name contains "incident" *and* whose topic mentions postmortems is `incident-response-archive` — but it's archived, so it fails your last condition (and Slack wouldn't allow inviting to it anyway).

I've held off on inviting Aisha Khan (I did confirm her user ID: `UWUIS8ZJWB4`) until you confirm which channel you actually mean. A couple of options:

1. **Unarchive** `incident-response-archive` and then invite her — say the word and I'll do both.
2. Point me at a different channel if you know of one I'm not seeing (the bot only has visibility into the three above).
