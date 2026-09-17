# Assignment W10

**Route:** Workspace Membership → User → Reaction → Message → Conversation → Conversation Membership

**Resolution mode:** multiple

**Request:** "Can you tell me what workspace roles the people hold who reacted with a 🚀 to messages posted in channels that Priya belongs to?"

*Note: Workspace membership/role has no supported write API, so this is answered as a read about observable role facts on the matched users' workspace memberships.*

| Referent | Environment facts | Interpretation |
|---|---|---|
| Diego's workspace membership | Diego reacted 🚀 to message M1 in #eng-alerts; Priya is a member of #eng-alerts; Diego holds the `member` role in Nimbus Robotics workspace | Match |
| Sana's workspace membership | Sana reacted 🚀 to message M3 in #ops; Priya is also a member of #ops; Sana additionally reacted 👍 to an unrelated message M4 in #eng-social; Sana holds the `admin` role in Nimbus Robotics workspace | Match with unrelated extra activity |
| Tom's workspace membership | Tom reacted 👍 (not 🚀) to message M1 in #eng-alerts, where Priya is a member; Tom holds `member` role | Wrong emoji only |
| Nina's workspace membership | Nina reacted 🚀 to message M2 in #eng-social; Priya is NOT a member of #eng-social; Nina holds `member` role | Wrong conversation-membership condition only (channel lacks Priya) |
| Lee's workspace membership | Lee is a member of #eng-alerts (where Priya is also a member) and has posted messages there, but has never added any reaction; Lee holds `member` role | Missing reaction relationship |
| Priya's workspace membership | Priya reacted 👀 to message M1 in #eng-alerts, and separately Priya is herself a member of #eng-alerts; Priya holds `admin` role | Reactor and channel-membership condition are satisfied by the same person incidentally, but the required 🚀 emoji is missing, so no qualifying reaction exists |