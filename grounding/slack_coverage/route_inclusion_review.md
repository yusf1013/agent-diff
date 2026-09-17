# Slack route inclusion review

Manual inclusion review completed for all 212 candidate routes. 174 retained; groups B/C/D (38 routes) excluded from the current campaign by user decision. The scoped witnesses remain available for reconsideration. No solver, generator, or evaluator runs were launched.

This reviews the fixed 212-route inventory after the unsupported-concept/settings partition. It does not add parent/reply, repeated-type, direct-attribute or nested-block families, freeze the entire coverage space, or certify concrete generated tests. Retention means at least one faithful scoped request is supported, not every field, mode or environment for that route.

## Decisions

| Decision | Routes |
|---|---:|
| duplicate | 0 |
| exclude | 38 |
| limitation | 0 |
| pending_group | 0 |
| retain | 174 |
| unresolved | 0 |
| **Total** | **212** |

## Groups for the inclusion decision

Inverse routes remain separate requirements. Grouping related directions allows one consistent inclusion decision; it does not declare their referent selections equivalent.

| Group | Routes | Decision | Relationship pattern |
|---|---:|---|---|
| [S1](#s1) | 64 | retain | Messages, people, channels, reactions and channel memberships |
| [S2](#s2) | 26 | retain | Profile-displayed membership roles without a Workspace node |
| [S3](#s3) | 28 | retain | Workspace as channel context without workspace membership |
| [S4](#s4) | 34 | retain | Workspace is the requested or identifying endpoint |
| [A](#a) | 22 | retain | Direct workspace connection |
| [B](#b) | 6 | exclude | Affiliated person’s channel memberships |
| [C](#c) | 18 | exclude | Affiliated person’s message or reaction activity |
| [D](#d) | 14 | exclude | Channel participant’s additional memberships or activity |

## Review standard

- Preserve the selected referent, each relationship role, and same-person/message bindings. A fluent paraphrase must not silently change the route.
- Require an explicit identifying field, relation existence/count, or identity predicate supported by the model; do not invent fields such as a membership status absent from the model.
- Use ordinary bounded candidate lists and readable channel histories where necessary. Candidate handles identify the search population, not the matching answer; the focal condition must still distinguish candidate roots.
- For workspace-membership witnesses, explicitly restrict the request to the association displayed on the relevant profile. users.info provides that workspace ID and owner/admin flags; users.list is not a general cross-workspace membership listing. Do not infer primary status, single membership, or complete membership discovery.
- Use named-channel conversation projections when workspace IDs are needed; do not assume a DM response exposes every ordinary-channel field. Ensure cross-workspace histories are readable by the acting user and all necessary pages are retrieved.
- Counts are derived from real relations. A member-count response and the equivalent complete membership count are representations of one criterion, not two route families. Cardinality predicates do not require unavailable joined_at.
- Do not exclude by length, treat inverse paths as equivalent, or remove association referents merely because their identities contain endpoints.
- Classify the 60 internal-Workspace routes by the roles on either side of Workspace membership—Workspace—Conversation. Group directions together for inclusion discussion while counting them separately.
- Exclude B/C/D from this campaign following the user’s whole-group decision. Preserve all 38 request/API witnesses for reconsideration rather than label them technically impossible or semantically duplicate.
- This is manual modeling work. Mechanical validation checks the inventory, groups and sources; seed realization and runtime/API validation remain required before generated cases enter a campaign.

## By referent entity

| Referent entity | Retain | Pending group decision | Limitation | Duplicate | Exclude | Unresolved |
|---|---:|---:|---:|---:|---:|---:|
| CONVERSATION | 22 | 0 | 0 | 0 | 5 | 0 |
| CONVERSATION_MEMBERSHIP | 24 | 0 | 0 | 0 | 9 | 0 |
| MESSAGE | 23 | 0 | 0 | 0 | 8 | 0 |
| REACTION | 26 | 0 | 0 | 0 | 9 | 0 |
| USER | 24 | 0 | 0 | 0 | 0 | 0 |
| WORKSPACE | 31 | 0 | 0 | 0 | 0 | 0 |
| WORKSPACE_MEMBERSHIP | 24 | 0 | 0 | 0 | 7 | 0 |

## Group details

### S1

**Messages, people, channels, reactions and channel memberships**

Neither Workspace nor Workspace membership occurs.

Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth.

**Examples:** [R089](#r089), [R027](#r027)

**All routes:** [R009](#r009), [R010](#r010), [R013](#r013), [R014](#r014), [R015](#r015), [R016](#r016), [R017](#r017), [R018](#r018), [R021](#r021), [R022](#r022), [R023](#r023), [R024](#r024), [R027](#r027), [R028](#r028), [R036](#r036), [R037](#r037), [R040](#r040), [R041](#r041), [R042](#r042), [R045](#r045), [R051](#r051), [R052](#r052), [R055](#r055), [R056](#r056), [R057](#r057), [R058](#r058), [R061](#r061), [R067](#r067), [R068](#r068), [R071](#r071), [R072](#r072), [R077](#r077), [R078](#r078), [R081](#r081), [R082](#r082), [R083](#r083), [R088](#r088), [R089](#r089), [R092](#r092), [R093](#r093), [R098](#r098), [R099](#r099), [R102](#r102), [R107](#r107), [R108](#r108), [R111](#r111), [R117](#r117), [R118](#r118), [R121](#r121), [R122](#r122), [R123](#r123), [R126](#r126), [R133](#r133), [R134](#r134), [R137](#r137), [R138](#r138), [R139](#r139), [R140](#r140), [R143](#r143), [R144](#r144), [R145](#r145), [R146](#r146), [R147](#r147), [R150](#r150)

### S2

**Profile-displayed membership roles without a Workspace node**

Workspace membership occurs, but Workspace does not.

Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions.

**Examples:** [R073](#r073), [R203](#r203)

**All routes:** [R011](#r011), [R019](#r019), [R025](#r025), [R038](#r038), [R043](#r043), [R046](#r046), [R069](#r069), [R073](#r073), [R084](#r084), [R100](#r100), [R103](#r103), [R112](#r112), [R127](#r127), [R197](#r197), [R198](#r198), [R199](#r199), [R201](#r201), [R202](#r202), [R203](#r203), [R204](#r204), [R206](#r206), [R207](#r207), [R208](#r208), [R209](#r209), [R210](#r210), [R212](#r212)

### S3

**Workspace as channel context without workspace membership**

Workspace occurs, but Workspace membership does not. Workspace is necessarily an endpoint in this reduced graph.

Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available.

**Examples:** [R062](#r062), [R173](#r173)

**All routes:** [R001](#r001), [R029](#r029), [R053](#r053), [R059](#r059), [R062](#r062), [R079](#r079), [R090](#r090), [R094](#r094), [R109](#r109), [R119](#r119), [R124](#r124), [R135](#r135), [R141](#r141), [R148](#r148), [R165](#r165), [R166](#r166), [R167](#r167), [R169](#r169), [R170](#r170), [R171](#r171), [R172](#r172), [R173](#r173), [R174](#r174), [R176](#r176), [R177](#r177), [R178](#r178), [R179](#r179), [R181](#r181)

### S4

**Workspace is the requested or identifying endpoint**

Both Workspace and Workspace membership occur, and Workspace is an endpoint of the complete route.

Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery.

**Examples:** [R074](#r074), [R157](#r157)

**All routes:** [R012](#r012), [R020](#r020), [R026](#r026), [R039](#r039), [R044](#r044), [R047](#r047), [R070](#r070), [R074](#r074), [R085](#r085), [R101](#r101), [R104](#r104), [R113](#r113), [R128](#r128), [R151](#r151), [R152](#r152), [R153](#r153), [R154](#r154), [R155](#r155), [R156](#r156), [R157](#r157), [R158](#r158), [R159](#r159), [R160](#r160), [R161](#r161), [R162](#r162), [R163](#r163), [R164](#r164), [R168](#r168), [R175](#r175), [R180](#r180), [R182](#r182), [R200](#r200), [R205](#r205), [R211](#r211)

### A

**Direct workspace connection**

Canonical arms: membership side is [WORKSPACE_MEMBERSHIP] or [WORKSPACE_MEMBERSHIP,USER]. Conversation side stays within the conversation and its messages/reactions/memberships, optionally ending at their directly associated USER; it does not continue from that USER to another relation.

Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant.

**Examples:** [R003](#r003), [R195](#r195)

**All routes:** [R002](#r002), [R003](#r003), [R030](#r030), [R031](#r031), [R063](#r063), [R064](#r064), [R095](#r095), [R096](#r096), [R129](#r129), [R130](#r130), [R131](#r131), [R132](#r132), [R136](#r136), [R142](#r142), [R149](#r149), [R183](#r183), [R184](#r184), [R185](#r185), [R190](#r190), [R191](#r191), [R194](#r194), [R195](#r195)

### B

**Affiliated person’s channel memberships**

Canonical membership arm starts [WORKSPACE_MEMBERSHIP,USER,CONVERSATION_MEMBERSHIP]. Conversation arm is [CONVERSATION], [CONVERSATION,MESSAGE], or [CONVERSATION,MESSAGE,REACTION].

Connect a person’s channel memberships to channels/content in the workspace shown on that person’s profile. The membership can be in the same or a different channel; neither equality nor difference is implied. A scoped query is technically available, but the user chose to leave this whole group out of the current campaign. Additional relations do not require different records unless the request says so.

**Examples:** [R004](#r004), [R050](#r050)

**All routes:** [R004](#r004), [R048](#r048), [R049](#r049), [R050](#r050), [R065](#r065), [R097](#r097)

### C

**Affiliated person’s message or reaction activity**

Canonical membership arm starts [WORKSPACE_MEMBERSHIP,USER,MESSAGE] or [WORKSPACE_MEMBERSHIP,USER,REACTION], with its permitted remaining message/reaction extension. Conversation arm stays at [CONVERSATION], [CONVERSATION,CONVERSATION_MEMBERSHIP], or [CONVERSATION,MESSAGE], as permitted by the no-repeated-type source enumeration.

Connect a person’s authored-message/reaction activity to channels or content in that person’s profile-shown workspace. The activity itself need not occur in that workspace; no extra equality is assumed. A scoped query is technically available, but the user chose to leave this whole group out of the current campaign. Additional relations do not require different records unless the request says so.

**Examples:** [R005](#r005), [R033](#r033)

**All routes:** [R005](#r005), [R006](#r006), [R007](#r007), [R008](#r008), [R032](#r032), [R033](#r033), [R034](#r034), [R035](#r035), [R066](#r066), [R075](#r075), [R076](#r076), [R086](#r086), [R087](#r087), [R105](#r105), [R106](#r106), [R114](#r114), [R115](#r115), [R116](#r116)

### D

**Channel participant’s additional memberships or activity**

Canonical membership arm is [WORKSPACE_MEMBERSHIP]. Conversation arm reaches USER through CONVERSATION_MEMBERSHIP, MESSAGE authorship, or MESSAGE→REACTION contribution, then continues from that USER to at least one further MESSAGE, REACTION, or CONVERSATION_MEMBERSHIP relation.

Connect a profile-shown workspace association to one of that workspace’s channels, identify a channel participant/author/reactor, and then use a separate membership or activity of that same participant. Unlike group A, the participant is an intermediate join variable, not the endpoint. A scoped query is technically available, but the user chose to leave this whole group out of the current campaign. Additional relations do not require different records unless the request says so.

**Examples:** [R186](#r186), [R196](#r196)

**All routes:** [R054](#r054), [R060](#r060), [R080](#r080), [R091](#r091), [R110](#r110), [R120](#r120), [R125](#r125), [R186](#r186), [R187](#r187), [R188](#r188), [R189](#r189), [R192](#r192), [R193](#r193), [R196](#r196)


## Reading the rows

W = Workspace; U = User; C = Conversation; M = Message; WM = Workspace membership; CM = Conversation membership; R = Reaction. Route IDs preserve the original inventory order.

Request fragments are manual inclusion witnesses, not generated benchmark cases. Each needs a concrete seed, complete task/card specification, and runtime validation before use. Scope restrictions are part of the retained witness, not claims about arbitrary environments.

## Index

| ID | Complete route | Group | Decision | Ordinary request fragment |
|---|---|---|---|---|
| [R001](#r001) | C → W | [S3](#s3) | retain | Which of these channels belong to workspace T_BETA? |
| [R002](#r002) | C → W → WM | [A](#a) | retain | Which of these channels are in a workspace shown on an owner’s profile in this roster? |
| [R003](#r003) | C → W → WM → U | [A](#a) | retain | Which of these channels belong to the workspace shown on @tom’s profile? |
| [R004](#r004) | C → W → WM → U → CM | [B](#b) | exclude | Which candidate channels are in workspaces listed on profiles of people who belong to three of these review channels? |
| [R005](#r005) | C → W → WM → U → M | [C](#c) | exclude | Which candidate channels are in workspaces listed on profiles of people who posted about the launch in these review channels? |
| [R006](#r006) | C → W → WM → U → M → R | [C](#c) | exclude | Which candidate channels are in workspaces listed on profiles of people whose posts received a thumbs-up in these review channels? |
| [R007](#r007) | C → W → WM → U → R | [C](#c) | exclude | Which candidate channels are in workspaces listed on profiles of people who gave a thumbs-up in these review channels? |
| [R008](#r008) | C → W → WM → U → R → M | [C](#c) | exclude | Which candidate channels are in workspaces listed on profiles of people who reacted to launch posts in these review channels? |
| [R009](#r009) | C → CM | [S1](#s1) | retain | Which of these channels have three members? |
| [R010](#r010) | C → CM → U | [S1](#s1) | retain | Which of these channels include @tom? |
| [R011](#r011) | C → CM → U → WM | [S2](#s2) | retain | Which of these channels have members whose profiles identify them as workspace administrators? |
| [R012](#r012) | C → CM → U → WM → W | [S4](#s4) | retain | Which of these channels have members whose profiles list workspace T_BETA? |
| [R013](#r013) | C → CM → U → M | [S1](#s1) | retain | Which candidate channels have members who posted about the launch in these review channels? |
| [R014](#r014) | C → CM → U → M → R | [S1](#s1) | retain | Which candidate channels have members whose posts received a thumbs-up in these review channels? |
| [R015](#r015) | C → CM → U → R | [S1](#s1) | retain | Which candidate channels have members who gave a thumbs-up in these review channels? |
| [R016](#r016) | C → CM → U → R → M | [S1](#s1) | retain | Which candidate channels have members who reacted to launch posts in these review channels? |
| [R017](#r017) | C → M | [S1](#s1) | retain | Which of these channels contain launch posts? |
| [R018](#r018) | C → M → U | [S1](#s1) | retain | Which of these channels has @tom posted in? |
| [R019](#r019) | C → M → U → WM | [S2](#s2) | retain | Which of these channels contain posts by people whose profiles identify them as workspace administrators? |
| [R020](#r020) | C → M → U → WM → W | [S4](#s4) | retain | Which of these channels contain posts by people whose profiles list workspace T_BETA? |
| [R021](#r021) | C → M → U → CM | [S1](#s1) | retain | Which candidate channels have posts by people who belong to three of these review channels? |
| [R022](#r022) | C → M → U → R | [S1](#s1) | retain | Which candidate channels have posts by people who gave a thumbs-up in these review channels? |
| [R023](#r023) | C → M → R | [S1](#s1) | retain | Which of these channels contain posts with a thumbs-up reaction? |
| [R024](#r024) | C → M → R → U | [S1](#s1) | retain | Which of these channels contain posts @tom reacted to? |
| [R025](#r025) | C → M → R → U → WM | [S2](#s2) | retain | Which of these channels contain posts reacted to by people whose profiles identify them as workspace administrators? |
| [R026](#r026) | C → M → R → U → WM → W | [S4](#s4) | retain | Which of these channels contain posts reacted to by people whose profiles list workspace T_BETA? |
| [R027](#r027) | C → M → R → U → CM | [S1](#s1) | retain | Which candidate channels contain posts reacted to by people who belong to three of these review channels? |
| [R028](#r028) | CM → C | [S1](#s1) | retain | List the member entries for the audit channels whose names include engineering. |
| [R029](#r029) | CM → C → W | [S3](#s3) | retain | List the member entries for audit channels in workspace T_RESEARCH. |
| [R030](#r030) | CM → C → W → WM | [A](#a) | retain | List member entries for audit channels in workspaces where someone in the review roster is shown as an admin on their profile. |
| [R031](#r031) | CM → C → W → WM → U | [A](#a) | retain | List member entries for audit channels in the workspace shown on the profile of the roster person named Alex. |
| [R032](#r032) | CM → C → W → WM → U → M | [C](#c) | exclude | List member entries for audit channels whose workspace appears on the profile of a roster person who posted about launch in the audit histories. |
| [R033](#r033) | CM → C → W → WM → U → M → R | [C](#c) | exclude | List member entries for audit channels whose workspace appears on the profile of a roster person whose audit-history message received a thumbs-up. |
| [R034](#r034) | CM → C → W → WM → U → R | [C](#c) | exclude | List member entries for audit channels whose workspace appears on the profile of a roster person who used a thumbs-up reaction in the audit histories. |
| [R035](#r035) | CM → C → W → WM → U → R → M | [C](#c) | exclude | List member entries for audit channels whose workspace appears on the profile of a roster person who reacted to an audit-history message about launch. |
| [R036](#r036) | CM → C → M | [S1](#s1) | retain | List member entries for audit channels with messages about launch. |
| [R037](#r037) | CM → C → M → U | [S1](#s1) | retain | List member entries for audit channels where a person named Alex has posted. |
| [R038](#r038) | CM → C → M → U → WM | [S2](#s2) | retain | List member entries for audit channels containing a message by someone shown as an admin in the workspace on their profile. |
| [R039](#r039) | CM → C → M → U → WM → W | [S4](#s4) | retain | List member entries for audit channels containing a message by someone whose profile shows workspace T_RESEARCH. |
| [R040](#r040) | CM → C → M → U → R | [S1](#s1) | retain | List member entries for audit channels with a post by someone who also gave a thumbs-up in the audit histories. |
| [R041](#r041) | CM → C → M → R | [S1](#s1) | retain | List member entries for audit channels with a message that received a thumbs-up. |
| [R042](#r042) | CM → C → M → R → U | [S1](#s1) | retain | List member entries for audit channels with a message reacted to by someone named Alex. |
| [R043](#r043) | CM → C → M → R → U → WM | [S2](#s2) | retain | List member entries for audit channels with a message reacted to by someone shown as an admin in the workspace on their profile. |
| [R044](#r044) | CM → C → M → R → U → WM → W | [S4](#s4) | retain | List member entries for audit channels with a message reacted to by someone whose profile shows workspace T_RESEARCH. |
| [R045](#r045) | CM → U | [S1](#s1) | retain | List the audit-channel membership entries belonging to roster people named Alex. |
| [R046](#r046) | CM → U → WM | [S2](#s2) | retain | List the audit-channel membership entries for roster people shown as admins in the workspaces on their profiles. |
| [R047](#r047) | CM → U → WM → W | [S4](#s4) | retain | List audit-channel membership entries for roster people whose profiles show workspace T_RESEARCH. |
| [R048](#r048) | CM → U → WM → W → C | [B](#b) | exclude | List audit-channel membership entries for roster people whose profile-shown workspace contains an audit channel named security. |
| [R049](#r049) | CM → U → WM → W → C → M | [B](#b) | exclude | List audit-channel membership entries for roster people whose profile-shown workspace has an audit channel discussing launch. |
| [R050](#r050) | CM → U → WM → W → C → M → R | [B](#b) | exclude | List audit-channel membership entries for roster people whose profile-shown workspace has an audit-channel message with a thumbs-up. |
| [R051](#r051) | CM → U → M | [S1](#s1) | retain | List audit-channel membership entries for people who posted about launch in the audit histories. |
| [R052](#r052) | CM → U → M → C | [S1](#s1) | retain | List audit-channel membership entries for people who posted in the audit channel named security. |
| [R053](#r053) | CM → U → M → C → W | [S3](#s3) | retain | List audit-channel membership entries for people who posted in an audit channel belonging to T_RESEARCH. |
| [R054](#r054) | CM → U → M → C → W → WM | [D](#d) | exclude | List audit-channel membership entries for people who posted in a workspace shown on the profile of an admin in the review roster. |
| [R055](#r055) | CM → U → M → R | [S1](#s1) | retain | List audit-channel membership entries for people whose audit-history posts received a thumbs-up. |
| [R056](#r056) | CM → U → R | [S1](#s1) | retain | List audit-channel membership entries for people who used a thumbs-up reaction in the audit histories. |
| [R057](#r057) | CM → U → R → M | [S1](#s1) | retain | List audit-channel membership entries for people who reacted to an audit-history message about launch. |
| [R058](#r058) | CM → U → R → M → C | [S1](#s1) | retain | List audit-channel membership entries for people who reacted to a message in the audit channel named security. |
| [R059](#r059) | CM → U → R → M → C → W | [S3](#s3) | retain | List audit-channel membership entries for people who reacted to an audit-channel message in workspace T_RESEARCH. |
| [R060](#r060) | CM → U → R → M → C → W → WM | [D](#d) | exclude | List audit-channel membership entries for people who reacted to a message in a workspace shown on the profile of an admin in the review roster. |
| [R061](#r061) | M → C | [S1](#s1) | retain | Find the posts in #engineering among these channels. |
| [R062](#r062) | M → C → W | [S3](#s3) | retain | Find posts belonging to workspace T_BETA among these channels. |
| [R063](#r063) | M → C → W → WM | [A](#a) | retain | Find posts in channels whose workspace is shown on an owner’s profile in this roster. |
| [R064](#r064) | M → C → W → WM → U | [A](#a) | retain | Find posts in the workspace shown on @tom’s profile, among these channels. |
| [R065](#r065) | M → C → W → WM → U → CM | [B](#b) | exclude | Find posts in workspaces listed on profiles of people who belong to three of these review channels. |
| [R066](#r066) | M → C → W → WM → U → R | [C](#c) | exclude | Find posts in workspaces listed on profiles of people who gave a thumbs-up in these review channels. |
| [R067](#r067) | M → C → CM | [S1](#s1) | retain | Find posts in channels with three members among these channels. |
| [R068](#r068) | M → C → CM → U | [S1](#s1) | retain | Find posts in channels that include @tom among these channels. |
| [R069](#r069) | M → C → CM → U → WM | [S2](#s2) | retain | Find posts in channels with members whose profiles identify them as workspace administrators. |
| [R070](#r070) | M → C → CM → U → WM → W | [S4](#s4) | retain | Find posts in channels with members whose profiles list workspace T_BETA. |
| [R071](#r071) | M → C → CM → U → R | [S1](#s1) | retain | Find posts in candidate channels with members who gave a thumbs-up in these review channels. |
| [R072](#r072) | M → U | [S1](#s1) | retain | Find @tom’s posts among these channels. |
| [R073](#r073) | M → U → WM | [S2](#s2) | retain | Find posts by people whose profiles identify them as workspace administrators. |
| [R074](#r074) | M → U → WM → W | [S4](#s4) | retain | Find posts by people whose profiles list workspace T_BETA. |
| [R075](#r075) | M → U → WM → W → C | [C](#c) | exclude | Find posts by people whose profile-listed workspace has an incident-response channel in this channel list. |
| [R076](#r076) | M → U → WM → W → C → CM | [C](#c) | exclude | Find posts by people whose profile-listed workspace has a channel with three members in this channel list. |
| [R077](#r077) | M → U → CM | [S1](#s1) | retain | Find posts by people who belong to three of these review channels. |
| [R078](#r078) | M → U → CM → C | [S1](#s1) | retain | Find posts by members of #security, considering membership in these review channels. |
| [R079](#r079) | M → U → CM → C → W | [S3](#s3) | retain | Find posts by people who belong to channels in workspace T_BETA, considering this review-channel list. |
| [R080](#r080) | M → U → CM → C → W → WM | [D](#d) | exclude | Find posts by people who belong to review channels whose workspace is shown on an owner’s profile in this roster. |
| [R081](#r081) | M → U → R | [S1](#s1) | retain | Find posts by people who gave a thumbs-up in these review channels. |
| [R082](#r082) | M → R | [S1](#s1) | retain | Find posts with a thumbs-up reaction among these channels. |
| [R083](#r083) | M → R → U | [S1](#s1) | retain | Find posts @tom reacted to among these channels. |
| [R084](#r084) | M → R → U → WM | [S2](#s2) | retain | Find posts reacted to by people whose profiles identify them as workspace administrators. |
| [R085](#r085) | M → R → U → WM → W | [S4](#s4) | retain | Find posts reacted to by people whose profiles list workspace T_BETA. |
| [R086](#r086) | M → R → U → WM → W → C | [C](#c) | exclude | Find posts reacted to by people whose profile-listed workspace has an incident-response channel in this channel list. |
| [R087](#r087) | M → R → U → WM → W → C → CM | [C](#c) | exclude | Find posts reacted to by people whose profile-listed workspace has a channel with three members in this channel list. |
| [R088](#r088) | M → R → U → CM | [S1](#s1) | retain | Find posts reacted to by people who belong to three of these review channels. |
| [R089](#r089) | M → R → U → CM → C | [S1](#s1) | retain | Find posts reacted to by members of #security, considering membership in these review channels. |
| [R090](#r090) | M → R → U → CM → C → W | [S3](#s3) | retain | Find posts reacted to by people who belong to channels in workspace T_BETA, considering this review-channel list. |
| [R091](#r091) | M → R → U → CM → C → W → WM | [D](#d) | exclude | Find posts reacted to by people who belong to review channels whose workspace is shown on an owner’s profile in this roster. |
| [R092](#r092) | R → M | [S1](#s1) | retain | Reactions on messages containing the launch checklist. |
| [R093](#r093) | R → M → C | [S1](#s1) | retain | Reactions on messages in #engineering. |
| [R094](#r094) | R → M → C → W | [S3](#s3) | retain | Reactions on messages in workspace T_RESEARCH, across these channels. |
| [R095](#r095) | R → M → C → W → WM | [A](#a) | retain | Reactions in a workspace that one of these reviewers lists on their profile with an administrator role. |
| [R096](#r096) | R → M → C → W → WM → U | [A](#a) | retain | Reactions in the workspace listed on Tom's profile. |
| [R097](#r097) | R → M → C → W → WM → U → CM | [B](#b) | exclude | Reactions in workspaces represented on the profiles of reviewers who belong to at least three of the listed channels. |
| [R098](#r098) | R → M → C → CM | [S1](#s1) | retain | Reactions in channels with three members. |
| [R099](#r099) | R → M → C → CM → U | [S1](#s1) | retain | Reactions in channels that Tom belongs to. |
| [R100](#r100) | R → M → C → CM → U → WM | [S2](#s2) | retain | Reactions in channels with a member whose profile shows a workspace administrator role. |
| [R101](#r101) | R → M → C → CM → U → WM → W | [S4](#s4) | retain | Reactions in channels with a member whose profile lists workspace T_RESEARCH. |
| [R102](#r102) | R → M → U | [S1](#s1) | retain | Reactions to messages written by Tom. |
| [R103](#r103) | R → M → U → WM | [S2](#s2) | retain | Reactions to messages by people whose profiles show a workspace administrator role. |
| [R104](#r104) | R → M → U → WM → W | [S4](#s4) | retain | Reactions to messages by people whose profiles list workspace T_RESEARCH. |
| [R105](#r105) | R → M → U → WM → W → C | [C](#c) | exclude | Reactions to messages by people whose profile-listed workspace contains #engineering. |
| [R106](#r106) | R → M → U → WM → W → C → CM | [C](#c) | exclude | Reactions to messages by people whose profile-listed workspace contains one of these channels with three members. |
| [R107](#r107) | R → M → U → CM | [S1](#s1) | retain | Reactions to messages by people who belong to at least three of the listed channels. |
| [R108](#r108) | R → M → U → CM → C | [S1](#s1) | retain | Reactions to messages by members of #engineering. |
| [R109](#r109) | R → M → U → CM → C → W | [S3](#s3) | retain | Reactions to messages by people who belong to one of these channels in workspace T_RESEARCH. |
| [R110](#r110) | R → M → U → CM → C → W → WM | [D](#d) | exclude | Reactions to messages by people who belong to a listed channel in a workspace shown on an administrator reviewer's profile. |
| [R111](#r111) | R → U | [S1](#s1) | retain | Reactions added by Tom. |
| [R112](#r112) | R → U → WM | [S2](#s2) | retain | Reactions added by people whose profiles show a workspace administrator role. |
| [R113](#r113) | R → U → WM → W | [S4](#s4) | retain | Reactions added by people whose profiles list workspace T_RESEARCH. |
| [R114](#r114) | R → U → WM → W → C | [C](#c) | exclude | Reactions added by people whose profile-listed workspace contains #engineering. |
| [R115](#r115) | R → U → WM → W → C → CM | [C](#c) | exclude | Reactions added by people whose profile-listed workspace contains one of these channels with three members. |
| [R116](#r116) | R → U → WM → W → C → M | [C](#c) | exclude | Reactions added by people whose profile-listed workspace contains a launch-checklist message in one of these channels. |
| [R117](#r117) | R → U → CM | [S1](#s1) | retain | Reactions added by people who belong to at least three of the listed channels. |
| [R118](#r118) | R → U → CM → C | [S1](#s1) | retain | Reactions added by members of #engineering. |
| [R119](#r119) | R → U → CM → C → W | [S3](#s3) | retain | Reactions added by people who belong to a listed channel in workspace T_RESEARCH. |
| [R120](#r120) | R → U → CM → C → W → WM | [D](#d) | exclude | Reactions added by people who belong to a listed channel in a workspace shown on an administrator reviewer's profile. |
| [R121](#r121) | R → U → CM → C → M | [S1](#s1) | retain | Reactions added by members of a listed channel containing a launch-checklist message. |
| [R122](#r122) | R → U → M | [S1](#s1) | retain | Reactions added by people who posted a launch checklist in these channels. |
| [R123](#r123) | R → U → M → C | [S1](#s1) | retain | Reactions added by people who have posted in #engineering. |
| [R124](#r124) | R → U → M → C → W | [S3](#s3) | retain | Reactions added by people who posted in a listed channel in workspace T_RESEARCH. |
| [R125](#r125) | R → U → M → C → W → WM | [D](#d) | exclude | Reactions added by people who posted in a listed channel whose workspace is shown on an administrator reviewer's profile. |
| [R126](#r126) | R → U → M → C → CM | [S1](#s1) | retain | Reactions added by people who posted in one of these channels with three members. |
| [R127](#r127) | U → WM | [S2](#s2) | retain | Reviewers whose profiles show a workspace administrator role. |
| [R128](#r128) | U → WM → W | [S4](#s4) | retain | Reviewers whose profiles list workspace T_RESEARCH. |
| [R129](#r129) | U → WM → W → C | [A](#a) | retain | Reviewers whose profile-listed workspace contains #engineering. |
| [R130](#r130) | U → WM → W → C → CM | [A](#a) | retain | Reviewers whose profile-listed workspace contains one of these channels with three members. |
| [R131](#r131) | U → WM → W → C → M | [A](#a) | retain | Reviewers whose profile-listed workspace contains a launch-checklist message in one of these channels. |
| [R132](#r132) | U → WM → W → C → M → R | [A](#a) | retain | Reviewers whose profile-listed workspace contains a thumbs-up reaction on a message in one of these channels. |
| [R133](#r133) | U → CM | [S1](#s1) | retain | Reviewers who belong to at least three of these channels. |
| [R134](#r134) | U → CM → C | [S1](#s1) | retain | Reviewers who belong to #engineering. |
| [R135](#r135) | U → CM → C → W | [S3](#s3) | retain | Reviewers who belong to one of these channels in workspace T_RESEARCH. |
| [R136](#r136) | U → CM → C → W → WM | [A](#a) | retain | Reviewers who belong to a listed channel whose workspace is shown on an administrator contact's profile. |
| [R137](#r137) | U → CM → C → M | [S1](#s1) | retain | Reviewers who belong to one of these channels containing a launch-checklist message. |
| [R138](#r138) | U → CM → C → M → R | [S1](#s1) | retain | Reviewers who belong to one of these channels containing a message with a thumbs-up reaction. |
| [R139](#r139) | U → M | [S1](#s1) | retain | Reviewers who posted a launch checklist in these channels. |
| [R140](#r140) | U → M → C | [S1](#s1) | retain | Reviewers who have posted in #engineering. |
| [R141](#r141) | U → M → C → W | [S3](#s3) | retain | Reviewers who posted in a listed channel in workspace T_RESEARCH. |
| [R142](#r142) | U → M → C → W → WM | [A](#a) | retain | Reviewers who posted in a listed channel whose workspace is shown on an administrator contact's profile. |
| [R143](#r143) | U → M → C → CM | [S1](#s1) | retain | Reviewers who posted in one of these channels with three members. |
| [R144](#r144) | U → M → R | [S1](#s1) | retain | Reviewers whose messages in these channels received a thumbs-up reaction. |
| [R145](#r145) | U → R | [S1](#s1) | retain | Reviewers who added a thumbs-up reaction to a message in these channels. |
| [R146](#r146) | U → R → M | [S1](#s1) | retain | Reviewers who reacted to a launch-checklist message in these channels. |
| [R147](#r147) | U → R → M → C | [S1](#s1) | retain | Reviewers who reacted to a message in #engineering. |
| [R148](#r148) | U → R → M → C → W | [S3](#s3) | retain | Reviewers who reacted to a message in a listed channel in workspace T_RESEARCH. |
| [R149](#r149) | U → R → M → C → W → WM | [A](#a) | retain | Reviewers who reacted to a message in a listed channel whose workspace is shown on an administrator contact's profile. |
| [R150](#r150) | U → R → M → C → CM | [S1](#s1) | retain | Reviewers who reacted to a message in one of these channels with three members. |
| [R151](#r151) | W → WM | [S4](#s4) | retain | Among the workspace associations shown on review-roster profiles, list workspaces with at least two people shown as admins. |
| [R152](#r152) | W → WM → U | [S4](#s4) | retain | Among the workspace associations shown on review-roster profiles, list workspaces that include a person named Alex. |
| [R153](#r153) | W → WM → U → CM | [S4](#s4) | retain | List workspaces shown on review-roster profiles that have a roster person belonging to at least three audit channels. |
| [R154](#r154) | W → WM → U → CM → C | [S4](#s4) | retain | List workspaces shown on review-roster profiles that have a roster person in the audit channel named security. |
| [R155](#r155) | W → WM → U → CM → C → M | [S4](#s4) | retain | List workspaces shown on review-roster profiles that have a roster person in an audit channel discussing launch. |
| [R156](#r156) | W → WM → U → CM → C → M → R | [S4](#s4) | retain | List workspaces shown on review-roster profiles that have a roster person in an audit channel with a message receiving a thumbs-up. |
| [R157](#r157) | W → WM → U → M | [S4](#s4) | retain | List workspaces shown on review-roster profiles that have a roster person who posted about launch in the audit histories. |
| [R158](#r158) | W → WM → U → M → C | [S4](#s4) | retain | List workspaces shown on review-roster profiles that have a roster person who posted in the audit channel named security. |
| [R159](#r159) | W → WM → U → M → C → CM | [S4](#s4) | retain | List workspaces shown on review-roster profiles that have a roster person who posted in an audit channel with at least three members. |
| [R160](#r160) | W → WM → U → M → R | [S4](#s4) | retain | List workspaces shown on review-roster profiles that have a roster person whose audit-history post received a thumbs-up. |
| [R161](#r161) | W → WM → U → R | [S4](#s4) | retain | List workspaces shown on review-roster profiles that have a roster person who used a thumbs-up in the audit histories. |
| [R162](#r162) | W → WM → U → R → M | [S4](#s4) | retain | List workspaces shown on review-roster profiles that have a roster person who reacted to an audit-history message about launch. |
| [R163](#r163) | W → WM → U → R → M → C | [S4](#s4) | retain | List workspaces shown on review-roster profiles that have a roster person who reacted to a message in the audit channel named security. |
| [R164](#r164) | W → WM → U → R → M → C → CM | [S4](#s4) | retain | List workspaces shown on review-roster profiles that have a roster person who reacted to a message in an audit channel with at least three members. |
| [R165](#r165) | W → C | [S3](#s3) | retain | Among the audit channels, list workspaces with a channel named security. |
| [R166](#r166) | W → C → CM | [S3](#s3) | retain | Among the audit channels, list workspaces with a channel having at least three members. |
| [R167](#r167) | W → C → CM → U | [S3](#s3) | retain | Among the audit channels, list workspaces with a channel that includes someone named Alex. |
| [R168](#r168) | W → C → CM → U → WM | [S4](#s4) | retain | Among the audit channels, list workspaces with a channel that includes someone shown as an admin in the workspace on their profile. |
| [R169](#r169) | W → C → CM → U → M | [S3](#s3) | retain | Among the audit channels, list workspaces with a channel that includes someone who posted about launch in the audit histories. |
| [R170](#r170) | W → C → CM → U → M → R | [S3](#s3) | retain | Among the audit channels, list workspaces with a channel that includes someone whose audit-history post received a thumbs-up. |
| [R171](#r171) | W → C → CM → U → R | [S3](#s3) | retain | Among the audit channels, list workspaces with a channel that includes someone who gave a thumbs-up in the audit histories. |
| [R172](#r172) | W → C → CM → U → R → M | [S3](#s3) | retain | Among the audit channels, list workspaces with a channel that includes someone who reacted to an audit-history message about launch. |
| [R173](#r173) | W → C → M | [S3](#s3) | retain | Among the audit channels, list workspaces containing a message about launch. |
| [R174](#r174) | W → C → M → U | [S3](#s3) | retain | Among the audit channels, list workspaces containing a message by someone named Alex. |
| [R175](#r175) | W → C → M → U → WM | [S4](#s4) | retain | Among the audit channels, list workspaces containing a message by someone shown as an admin in the workspace on their profile. |
| [R176](#r176) | W → C → M → U → CM | [S3](#s3) | retain | Among the audit channels, list workspaces containing a message by someone who belongs to at least three audit channels. |
| [R177](#r177) | W → C → M → U → R | [S3](#s3) | retain | Among the audit channels, list workspaces containing a message by someone who also gave a thumbs-up in the audit histories. |
| [R178](#r178) | W → C → M → R | [S3](#s3) | retain | Among the audit channels, list workspaces containing a message with a thumbs-up reaction. |
| [R179](#r179) | W → C → M → R → U | [S3](#s3) | retain | Among the audit channels, list workspaces containing a message reacted to by someone named Alex. |
| [R180](#r180) | W → C → M → R → U → WM | [S4](#s4) | retain | Among the audit channels, list workspaces containing a message reacted to by someone shown as an admin in the workspace on their profile. |
| [R181](#r181) | W → C → M → R → U → CM | [S3](#s3) | retain | Among the audit channels, list workspaces containing a message reacted to by someone who belongs to at least three audit channels. |
| [R182](#r182) | WM → W | [S4](#s4) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries in workspace T_RESEARCH. |
| [R183](#r183) | WM → W → C | [A](#a) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace contains an audit channel named security. |
| [R184](#r184) | WM → W → C → CM | [A](#a) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit channel with at least three members. |
| [R185](#r185) | WM → W → C → CM → U | [A](#a) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit channel that includes someone named Alex. |
| [R186](#r186) | WM → W → C → CM → U → M | [D](#d) | exclude | List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit channel including someone who posted about launch in the audit histories. |
| [R187](#r187) | WM → W → C → CM → U → M → R | [D](#d) | exclude | List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit channel including someone whose audit-history post received a thumbs-up. |
| [R188](#r188) | WM → W → C → CM → U → R | [D](#d) | exclude | List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit channel including someone who gave a thumbs-up in the audit histories. |
| [R189](#r189) | WM → W → C → CM → U → R → M | [D](#d) | exclude | List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit channel including someone who reacted to an audit-history message about launch. |
| [R190](#r190) | WM → W → C → M | [A](#a) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit-channel message about launch. |
| [R191](#r191) | WM → W → C → M → U | [A](#a) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit-channel message by someone named Alex. |
| [R192](#r192) | WM → W → C → M → U → CM | [D](#d) | exclude | List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit-channel message by someone belonging to at least three audit channels. |
| [R193](#r193) | WM → W → C → M → U → R | [D](#d) | exclude | List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit-channel message by someone who also gave a thumbs-up in the audit histories. |
| [R194](#r194) | WM → W → C → M → R | [A](#a) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit-channel message with a thumbs-up reaction. |
| [R195](#r195) | WM → W → C → M → R → U | [A](#a) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit-channel message reacted to by someone named Alex. |
| [R196](#r196) | WM → W → C → M → R → U → CM | [D](#d) | exclude | List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit-channel message reacted to by someone belonging to at least three audit channels. |
| [R197](#r197) | WM → U | [S2](#s2) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people named Alex. |
| [R198](#r198) | WM → U → CM | [S2](#s2) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people in at least three audit channels. |
| [R199](#r199) | WM → U → CM → C | [S2](#s2) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people in the audit channel named security. |
| [R200](#r200) | WM → U → CM → C → W | [S4](#s4) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people in an audit channel in workspace T_RESEARCH. |
| [R201](#r201) | WM → U → CM → C → M | [S2](#s2) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people in an audit channel discussing launch. |
| [R202](#r202) | WM → U → CM → C → M → R | [S2](#s2) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people in an audit channel with a message receiving a thumbs-up. |
| [R203](#r203) | WM → U → M | [S2](#s2) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people who posted about launch in the audit histories. |
| [R204](#r204) | WM → U → M → C | [S2](#s2) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people who posted in the audit channel named security. |
| [R205](#r205) | WM → U → M → C → W | [S4](#s4) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people who posted in an audit channel in workspace T_RESEARCH. |
| [R206](#r206) | WM → U → M → C → CM | [S2](#s2) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people who posted in an audit channel with at least three members. |
| [R207](#r207) | WM → U → M → R | [S2](#s2) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people whose audit-history post received a thumbs-up. |
| [R208](#r208) | WM → U → R | [S2](#s2) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people who gave a thumbs-up in the audit histories. |
| [R209](#r209) | WM → U → R → M | [S2](#s2) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people who reacted to an audit-history message about launch. |
| [R210](#r210) | WM → U → R → M → C | [S2](#s2) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people who reacted to a message in the audit channel named security. |
| [R211](#r211) | WM → U → R → M → C → W | [S4](#s4) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people who reacted to an audit-channel message in workspace T_RESEARCH. |
| [R212](#r212) | WM → U → R → M → C → CM | [S2](#s2) | retain | List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people who reacted to a message in an audit channel with at least three members. |

## Individual reviews

### R001

**Route:** CONVERSATION → WORKSPACE

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Which of these channels belong to workspace T_BETA?

**Selection:** Team.team_id == "T_BETA" through Channel.team_id.

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count)

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R002

**Route:** CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [A](#a)

**Request:** Which of these channels are in a workspace shown on an owner’s profile in this roster?

**Selection:** Exists listed UserTeam membership with role == owner, selected by the profile team_id; its team_id equals Channel.team_id.

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The prompt supplies a finite candidate user roster by ID/link. Read the profiles to determine names, role flags, and listed workspace; do not supply those answers in the roster. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R003

**Route:** CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP → USER

**Decision:** retain

**Group:** [A](#a)

**Request:** Which of these channels belong to the workspace shown on @tom’s profile?

**Selection:** Listed profile User.username == "tom"; its selected UserTeam.team_id equals Channel.team_id.

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The prompt supplies a finite candidate user roster by ID/link. Read the profiles to determine names, role flags, and listed workspace; do not supply those answers in the roster. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R004

**Route:** CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP → USER → CONVERSATION_MEMBERSHIP

**Decision:** exclude

**Group:** [B](#b)

**Request:** Which candidate channels are in workspaces listed on profiles of people who belong to three of these review channels?

**Selection:** Exists listed UserTeam/User witness with COUNT(ChannelMember rows for that user over the review-channel scope) == 3 and UserTeam.team_id == candidate Channel.team_id.

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The prompt supplies a finite candidate user roster by ID/link. Read the profiles to determine names, role flags, and listed workspace; do not supply those answers in the roster. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. The request explicitly supplies the review-channel list used to delimit membership questions. Enumerate conversations.members for every review channel and join by user ID. COUNT is per specified user or channel, not a count over unrelated witnesses. No joined_at or complete all-workspace membership enumeration is assumed. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Excluded from the current campaign by the user’s whole-group decision for B. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R005

**Route:** CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP → USER → MESSAGE

**Decision:** exclude

**Group:** [C](#c)

**Request:** Which candidate channels are in workspaces listed on profiles of people who posted about the launch in these review channels?

**Selection:** Exists listed profile UserTeam/User and Message with Message.user_id == User.user_id and "launch" in Message.message_text; profile team_id equals candidate Channel.team_id.

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The prompt supplies a finite candidate user roster by ID/link. Read the profiles to determine names, role flags, and listed workspace; do not supply those answers in the roster. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. The request explicitly supplies the review channels whose posts/reactions qualify people. Read their histories and reactions completely; the actor has the required source-workspace access. Join reaction user IDs, message author IDs, and message IDs according to the stated roles. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Excluded from the current campaign by the user’s whole-group decision for C. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R006

**Route:** CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP → USER → MESSAGE → REACTION

**Decision:** exclude

**Group:** [C](#c)

**Request:** Which candidate channels are in workspaces listed on profiles of people whose posts received a thumbs-up in these review channels?

**Selection:** Exists profile UserTeam/User, authored Message, and MessageReaction with reaction_type == "thumbsup"; UserTeam.team_id == candidate Channel.team_id.

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The prompt supplies a finite candidate user roster by ID/link. Read the profiles to determine names, role flags, and listed workspace; do not supply those answers in the roster. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. The request explicitly supplies the review channels whose posts/reactions qualify people. Read their histories and reactions completely; the actor has the required source-workspace access. Join reaction user IDs, message author IDs, and message IDs according to the stated roles. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Excluded from the current campaign by the user’s whole-group decision for C. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R007

**Route:** CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP → USER → REACTION

**Decision:** exclude

**Group:** [C](#c)

**Request:** Which candidate channels are in workspaces listed on profiles of people who gave a thumbs-up in these review channels?

**Selection:** Exists profile UserTeam/User and MessageReaction with reaction.user_id == User.user_id and reaction_type == "thumbsup" in the review-message scope; profile team matches candidate Channel.team_id.

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The prompt supplies a finite candidate user roster by ID/link. Read the profiles to determine names, role flags, and listed workspace; do not supply those answers in the roster. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. The request explicitly supplies the review channels whose posts/reactions qualify people. Read their histories and reactions completely; the actor has the required source-workspace access. Join reaction user IDs, message author IDs, and message IDs according to the stated roles. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Excluded from the current campaign by the user’s whole-group decision for C. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R008

**Route:** CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP → USER → REACTION → MESSAGE

**Decision:** exclude

**Group:** [C](#c)

**Request:** Which candidate channels are in workspaces listed on profiles of people who reacted to launch posts in these review channels?

**Selection:** Exists profile UserTeam/User, MessageReaction by that user, and the reacted-to Message with "launch" in message_text; profile team matches candidate Channel.team_id.

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The prompt supplies a finite candidate user roster by ID/link. Read the profiles to determine names, role flags, and listed workspace; do not supply those answers in the roster. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. The request explicitly supplies the review channels whose posts/reactions qualify people. Read their histories and reactions completely; the actor has the required source-workspace access. Join reaction user IDs, message author IDs, and message IDs according to the stated roles. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Excluded from the current campaign by the user’s whole-group decision for C. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R009

**Route:** CONVERSATION → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Which of these channels have three members?

**Selection:** COUNT(ChannelMember rows with channel_id == candidate Channel.channel_id) == 3.

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time)

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R010

**Route:** CONVERSATION → CONVERSATION_MEMBERSHIP → USER

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Which of these channels include @tom?

**Selection:** Exists ChannelMember/User with User.username == "tom" and matching membership.user_id.

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R011

**Route:** CONVERSATION → CONVERSATION_MEMBERSHIP → USER → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [S2](#s2)

**Request:** Which of these channels have members whose profiles identify them as workspace administrators?

**Selection:** Exists ChannelMember/User and its profile-selected UserTeam with role in {admin, owner}.

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R012

**Route:** CONVERSATION → CONVERSATION_MEMBERSHIP → USER → WORKSPACE_MEMBERSHIP → WORKSPACE

**Decision:** retain

**Group:** [S4](#s4)

**Request:** Which of these channels have members whose profiles list workspace T_BETA?

**Selection:** Exists ChannelMember/User and its profile-selected UserTeam with Team.team_id == "T_BETA".

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R013

**Route:** CONVERSATION → CONVERSATION_MEMBERSHIP → USER → MESSAGE

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Which candidate channels have members who posted about the launch in these review channels?

**Selection:** Exists ChannelMember/User and Message authored by that user with "launch" in message_text within review channels.

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The request explicitly supplies the review channels whose posts/reactions qualify people. Read their histories and reactions completely; the actor has the required source-workspace access. Join reaction user IDs, message author IDs, and message IDs according to the stated roles. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R014

**Route:** CONVERSATION → CONVERSATION_MEMBERSHIP → USER → MESSAGE → REACTION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Which candidate channels have members whose posts received a thumbs-up in these review channels?

**Selection:** Exists ChannelMember/User, Message authored by that user, and MessageReaction on that message with reaction_type == "thumbsup".

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The request explicitly supplies the review channels whose posts/reactions qualify people. Read their histories and reactions completely; the actor has the required source-workspace access. Join reaction user IDs, message author IDs, and message IDs according to the stated roles. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R015

**Route:** CONVERSATION → CONVERSATION_MEMBERSHIP → USER → REACTION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Which candidate channels have members who gave a thumbs-up in these review channels?

**Selection:** Exists ChannelMember/User and MessageReaction by that user with reaction_type == "thumbsup" in the review-message scope.

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The request explicitly supplies the review channels whose posts/reactions qualify people. Read their histories and reactions completely; the actor has the required source-workspace access. Join reaction user IDs, message author IDs, and message IDs according to the stated roles. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R016

**Route:** CONVERSATION → CONVERSATION_MEMBERSHIP → USER → REACTION → MESSAGE

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Which candidate channels have members who reacted to launch posts in these review channels?

**Selection:** Exists ChannelMember/User, MessageReaction by that user, and its Message with "launch" in message_text.

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The request explicitly supplies the review channels whose posts/reactions qualify people. Read their histories and reactions completely; the actor has the required source-workspace access. Join reaction user IDs, message author IDs, and message IDs according to the stated roles. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R017

**Route:** CONVERSATION → MESSAGE

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Which of these channels contain launch posts?

**Selection:** Exists Message with channel_id == candidate Channel.channel_id and "launch" in message_text.

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The acting user has the workspace memberships needed to read all candidate channel histories; paginate them. This is access qualification, not a claim that channel membership implies workspace membership.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite)

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R018

**Route:** CONVERSATION → MESSAGE → USER

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Which of these channels has @tom posted in?

**Selection:** Exists Message/User with Message.channel_id == candidate Channel.channel_id and author User.username == "tom".

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The acting user has the workspace memberships needed to read all candidate channel histories; paginate them. This is access qualification, not a claim that channel membership implies workspace membership. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R019

**Route:** CONVERSATION → MESSAGE → USER → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [S2](#s2)

**Request:** Which of these channels contain posts by people whose profiles identify them as workspace administrators?

**Selection:** Exists contained Message/User and profile-selected UserTeam with role in {admin, owner}.

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The acting user has the workspace memberships needed to read all candidate channel histories; paginate them. This is access qualification, not a claim that channel membership implies workspace membership. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R020

**Route:** CONVERSATION → MESSAGE → USER → WORKSPACE_MEMBERSHIP → WORKSPACE

**Decision:** retain

**Group:** [S4](#s4)

**Request:** Which of these channels contain posts by people whose profiles list workspace T_BETA?

**Selection:** Exists contained Message/User and profile-selected UserTeam with Team.team_id == "T_BETA".

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The acting user has the workspace memberships needed to read all candidate channel histories; paginate them. This is access qualification, not a claim that channel membership implies workspace membership. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R021

**Route:** CONVERSATION → MESSAGE → USER → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Which candidate channels have posts by people who belong to three of these review channels?

**Selection:** Exists contained Message/User with COUNT(ChannelMember rows for that user over review channels) == 3.

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The acting user has the workspace memberships needed to read all candidate channel histories; paginate them. This is access qualification, not a claim that channel membership implies workspace membership. The request explicitly supplies the review-channel list used to delimit membership questions. Enumerate conversations.members for every review channel and join by user ID. COUNT is per specified user or channel, not a count over unrelated witnesses. No joined_at or complete all-workspace membership enumeration is assumed. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R022

**Route:** CONVERSATION → MESSAGE → USER → REACTION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Which candidate channels have posts by people who gave a thumbs-up in these review channels?

**Selection:** Exists contained Message/User and MessageReaction by that same user with reaction_type == "thumbsup" in review messages.

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The acting user has the workspace memberships needed to read all candidate channel histories; paginate them. This is access qualification, not a claim that channel membership implies workspace membership. The request explicitly supplies the review channels whose posts/reactions qualify people. Read their histories and reactions completely; the actor has the required source-workspace access. Join reaction user IDs, message author IDs, and message IDs according to the stated roles. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R023

**Route:** CONVERSATION → MESSAGE → REACTION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Which of these channels contain posts with a thumbs-up reaction?

**Selection:** Exists contained Message and MessageReaction on it with reaction_type == "thumbsup".

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The acting user has the workspace memberships needed to read all candidate channel histories; paginate them. This is access qualification, not a claim that channel membership implies workspace membership.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R024

**Route:** CONVERSATION → MESSAGE → REACTION → USER

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Which of these channels contain posts @tom reacted to?

**Selection:** Exists contained Message, MessageReaction on it, and reactor User.username == "tom".

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The acting user has the workspace memberships needed to read all candidate channel histories; paginate them. This is access qualification, not a claim that channel membership implies workspace membership. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R025

**Route:** CONVERSATION → MESSAGE → REACTION → USER → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [S2](#s2)

**Request:** Which of these channels contain posts reacted to by people whose profiles identify them as workspace administrators?

**Selection:** Exists contained Message, MessageReaction/User reactor, and profile-selected UserTeam with role in {admin, owner}.

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The acting user has the workspace memberships needed to read all candidate channel histories; paginate them. This is access qualification, not a claim that channel membership implies workspace membership. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R026

**Route:** CONVERSATION → MESSAGE → REACTION → USER → WORKSPACE_MEMBERSHIP → WORKSPACE

**Decision:** retain

**Group:** [S4](#s4)

**Request:** Which of these channels contain posts reacted to by people whose profiles list workspace T_BETA?

**Selection:** Exists contained Message, MessageReaction/User reactor, and profile-selected UserTeam with Team.team_id == "T_BETA".

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The acting user has the workspace memberships needed to read all candidate channel histories; paginate them. This is access qualification, not a claim that channel membership implies workspace membership. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R027

**Route:** CONVERSATION → MESSAGE → REACTION → USER → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Which candidate channels contain posts reacted to by people who belong to three of these review channels?

**Selection:** Exists contained Message, MessageReaction/User reactor, and COUNT(ChannelMember rows for that user over review channels) == 3.

**Scope:** The prompt supplies a finite candidate list of existing non-DM channels, by ID/link. Include candidates that differ on the stated criterion; supplying the pool does not supply the selected subset. Use non-null workspace IDs where workspace joins are exercised. The acting user has the workspace memberships needed to read all candidate channel histories; paginate them. This is access qualification, not a claim that channel membership implies workspace membership. The request explicitly supplies the review-channel list used to delimit membership questions. Enumerate conversations.members for every review channel and join by user ID. COUNT is per specified user or channel, not a count over unrelated witnesses. No joined_at or complete all-workspace membership enumeration is assumed. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R028

**Route:** CONVERSATION_MEMBERSHIP → CONVERSATION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** List the member entries for the audit channels whose names include engineering.

**Selection:** channels.channel_name contains engineering

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R029

**Route:** CONVERSATION_MEMBERSHIP → CONVERSATION → WORKSPACE

**Decision:** retain

**Group:** [S3](#s3)

**Request:** List the member entries for audit channels in workspace T_RESEARCH.

**Selection:** channels.team_id == T_RESEARCH

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R030

**Route:** CONVERSATION_MEMBERSHIP → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [A](#a)

**Request:** List member entries for audit channels in workspaces where someone in the review roster is shown as an admin on their profile.

**Selection:** user_teams.role in {admin,owner}, restricted to profile-shown association

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R031

**Route:** CONVERSATION_MEMBERSHIP → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP → USER

**Decision:** retain

**Group:** [A](#a)

**Request:** List member entries for audit channels in the workspace shown on the profile of the roster person named Alex.

**Selection:** users.real_name matches Alex

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R032

**Route:** CONVERSATION_MEMBERSHIP → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP → USER → MESSAGE

**Decision:** exclude

**Group:** [C](#c)

**Request:** List member entries for audit channels whose workspace appears on the profile of a roster person who posted about launch in the audit histories.

**Selection:** messages.message_text contains launch

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Excluded from the current campaign by the user’s whole-group decision for C. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R033

**Route:** CONVERSATION_MEMBERSHIP → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP → USER → MESSAGE → REACTION

**Decision:** exclude

**Group:** [C](#c)

**Request:** List member entries for audit channels whose workspace appears on the profile of a roster person whose audit-history message received a thumbs-up.

**Selection:** message_reactions.reaction_type == thumbsup

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Excluded from the current campaign by the user’s whole-group decision for C. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R034

**Route:** CONVERSATION_MEMBERSHIP → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP → USER → REACTION

**Decision:** exclude

**Group:** [C](#c)

**Request:** List member entries for audit channels whose workspace appears on the profile of a roster person who used a thumbs-up reaction in the audit histories.

**Selection:** message_reactions.reaction_type == thumbsup

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Excluded from the current campaign by the user’s whole-group decision for C. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R035

**Route:** CONVERSATION_MEMBERSHIP → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP → USER → REACTION → MESSAGE

**Decision:** exclude

**Group:** [C](#c)

**Request:** List member entries for audit channels whose workspace appears on the profile of a roster person who reacted to an audit-history message about launch.

**Selection:** messages.message_text contains launch

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Excluded from the current campaign by the user’s whole-group decision for C. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R036

**Route:** CONVERSATION_MEMBERSHIP → CONVERSATION → MESSAGE

**Decision:** retain

**Group:** [S1](#s1)

**Request:** List member entries for audit channels with messages about launch.

**Selection:** messages.message_text contains launch

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R037

**Route:** CONVERSATION_MEMBERSHIP → CONVERSATION → MESSAGE → USER

**Decision:** retain

**Group:** [S1](#s1)

**Request:** List member entries for audit channels where a person named Alex has posted.

**Selection:** users.real_name matches Alex

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R038

**Route:** CONVERSATION_MEMBERSHIP → CONVERSATION → MESSAGE → USER → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [S2](#s2)

**Request:** List member entries for audit channels containing a message by someone shown as an admin in the workspace on their profile.

**Selection:** user_teams.role in {admin,owner}, profile-shown association

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R039

**Route:** CONVERSATION_MEMBERSHIP → CONVERSATION → MESSAGE → USER → WORKSPACE_MEMBERSHIP → WORKSPACE

**Decision:** retain

**Group:** [S4](#s4)

**Request:** List member entries for audit channels containing a message by someone whose profile shows workspace T_RESEARCH.

**Selection:** user_teams.team_id == T_RESEARCH, profile-shown association

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R040

**Route:** CONVERSATION_MEMBERSHIP → CONVERSATION → MESSAGE → USER → REACTION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** List member entries for audit channels with a post by someone who also gave a thumbs-up in the audit histories.

**Selection:** message_reactions.reaction_type == thumbsup

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R041

**Route:** CONVERSATION_MEMBERSHIP → CONVERSATION → MESSAGE → REACTION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** List member entries for audit channels with a message that received a thumbs-up.

**Selection:** message_reactions.reaction_type == thumbsup

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R042

**Route:** CONVERSATION_MEMBERSHIP → CONVERSATION → MESSAGE → REACTION → USER

**Decision:** retain

**Group:** [S1](#s1)

**Request:** List member entries for audit channels with a message reacted to by someone named Alex.

**Selection:** users.real_name matches Alex

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R043

**Route:** CONVERSATION_MEMBERSHIP → CONVERSATION → MESSAGE → REACTION → USER → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [S2](#s2)

**Request:** List member entries for audit channels with a message reacted to by someone shown as an admin in the workspace on their profile.

**Selection:** user_teams.role in {admin,owner}, profile-shown association

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R044

**Route:** CONVERSATION_MEMBERSHIP → CONVERSATION → MESSAGE → REACTION → USER → WORKSPACE_MEMBERSHIP → WORKSPACE

**Decision:** retain

**Group:** [S4](#s4)

**Request:** List member entries for audit channels with a message reacted to by someone whose profile shows workspace T_RESEARCH.

**Selection:** user_teams.team_id == T_RESEARCH, profile-shown association

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R045

**Route:** CONVERSATION_MEMBERSHIP → USER

**Decision:** retain

**Group:** [S1](#s1)

**Request:** List the audit-channel membership entries belonging to roster people named Alex.

**Selection:** users.real_name matches Alex

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.members; methods.py:2029,2081; operations.py:620; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R046

**Route:** CONVERSATION_MEMBERSHIP → USER → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [S2](#s2)

**Request:** List the audit-channel membership entries for roster people shown as admins in the workspaces on their profiles.

**Selection:** user_teams.role in {admin,owner}, profile-shown association

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.members; methods.py:2029,2081; operations.py:620; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R047

**Route:** CONVERSATION_MEMBERSHIP → USER → WORKSPACE_MEMBERSHIP → WORKSPACE

**Decision:** retain

**Group:** [S4](#s4)

**Request:** List audit-channel membership entries for roster people whose profiles show workspace T_RESEARCH.

**Selection:** user_teams.team_id == T_RESEARCH, profile-shown association

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.members; methods.py:2029,2081; operations.py:620; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R048

**Route:** CONVERSATION_MEMBERSHIP → USER → WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION

**Decision:** exclude

**Group:** [B](#b)

**Request:** List audit-channel membership entries for roster people whose profile-shown workspace contains an audit channel named security.

**Selection:** channels.channel_name == security

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Excluded from the current campaign by the user’s whole-group decision for B. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R049

**Route:** CONVERSATION_MEMBERSHIP → USER → WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → MESSAGE

**Decision:** exclude

**Group:** [B](#b)

**Request:** List audit-channel membership entries for roster people whose profile-shown workspace has an audit channel discussing launch.

**Selection:** messages.message_text contains launch

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Excluded from the current campaign by the user’s whole-group decision for B. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R050

**Route:** CONVERSATION_MEMBERSHIP → USER → WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → MESSAGE → REACTION

**Decision:** exclude

**Group:** [B](#b)

**Request:** List audit-channel membership entries for roster people whose profile-shown workspace has an audit-channel message with a thumbs-up.

**Selection:** message_reactions.reaction_type == thumbsup

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Excluded from the current campaign by the user’s whole-group decision for B. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R051

**Route:** CONVERSATION_MEMBERSHIP → USER → MESSAGE

**Decision:** retain

**Group:** [S1](#s1)

**Request:** List audit-channel membership entries for people who posted about launch in the audit histories.

**Selection:** messages.message_text contains launch

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R052

**Route:** CONVERSATION_MEMBERSHIP → USER → MESSAGE → CONVERSATION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** List audit-channel membership entries for people who posted in the audit channel named security.

**Selection:** channels.channel_name == security

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R053

**Route:** CONVERSATION_MEMBERSHIP → USER → MESSAGE → CONVERSATION → WORKSPACE

**Decision:** retain

**Group:** [S3](#s3)

**Request:** List audit-channel membership entries for people who posted in an audit channel belonging to T_RESEARCH.

**Selection:** channels.team_id == T_RESEARCH

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R054

**Route:** CONVERSATION_MEMBERSHIP → USER → MESSAGE → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP

**Decision:** exclude

**Group:** [D](#d)

**Request:** List audit-channel membership entries for people who posted in a workspace shown on the profile of an admin in the review roster.

**Selection:** user_teams.role in {admin,owner}, profile-shown association

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Excluded from the current campaign by the user’s whole-group decision for D. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R055

**Route:** CONVERSATION_MEMBERSHIP → USER → MESSAGE → REACTION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** List audit-channel membership entries for people whose audit-history posts received a thumbs-up.

**Selection:** message_reactions.reaction_type == thumbsup

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R056

**Route:** CONVERSATION_MEMBERSHIP → USER → REACTION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** List audit-channel membership entries for people who used a thumbs-up reaction in the audit histories.

**Selection:** message_reactions.reaction_type == thumbsup

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.members; methods.py:2029,2081; operations.py:620; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R057

**Route:** CONVERSATION_MEMBERSHIP → USER → REACTION → MESSAGE

**Decision:** retain

**Group:** [S1](#s1)

**Request:** List audit-channel membership entries for people who reacted to an audit-history message about launch.

**Selection:** messages.message_text contains launch

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R058

**Route:** CONVERSATION_MEMBERSHIP → USER → REACTION → MESSAGE → CONVERSATION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** List audit-channel membership entries for people who reacted to a message in the audit channel named security.

**Selection:** channels.channel_name == security

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R059

**Route:** CONVERSATION_MEMBERSHIP → USER → REACTION → MESSAGE → CONVERSATION → WORKSPACE

**Decision:** retain

**Group:** [S3](#s3)

**Request:** List audit-channel membership entries for people who reacted to an audit-channel message in workspace T_RESEARCH.

**Selection:** channels.team_id == T_RESEARCH

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R060

**Route:** CONVERSATION_MEMBERSHIP → USER → REACTION → MESSAGE → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP

**Decision:** exclude

**Group:** [D](#d)

**Request:** List audit-channel membership entries for people who reacted to a message in a workspace shown on the profile of an admin in the review roster.

**Selection:** user_teams.role in {admin,owner}, profile-shown association

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Excluded from the current campaign by the user’s whole-group decision for D. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R061

**Route:** MESSAGE → CONVERSATION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Find the posts in #engineering among these channels.

**Selection:** Message.channel_id joins Channel with channel_name == "engineering".

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite)

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R062

**Route:** MESSAGE → CONVERSATION → WORKSPACE

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Find posts belonging to workspace T_BETA among these channels.

**Selection:** Message.channel_id joins Channel.team_id to Team.team_id == "T_BETA".

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite)

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R063

**Route:** MESSAGE → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [A](#a)

**Request:** Find posts in channels whose workspace is shown on an owner’s profile in this roster.

**Selection:** Message/Channel joins a profile-listed UserTeam with matching team_id and role == owner.

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. The prompt supplies a finite candidate user roster by ID/link. Read the profiles to determine names, role flags, and listed workspace; do not supply those answers in the roster. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R064

**Route:** MESSAGE → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP → USER

**Decision:** retain

**Group:** [A](#a)

**Request:** Find posts in the workspace shown on @tom’s profile, among these channels.

**Selection:** Message/Channel.team_id equals the team_id of the selected profile membership for User.username == "tom".

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. The prompt supplies a finite candidate user roster by ID/link. Read the profiles to determine names, role flags, and listed workspace; do not supply those answers in the roster. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R065

**Route:** MESSAGE → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP → USER → CONVERSATION_MEMBERSHIP

**Decision:** exclude

**Group:** [B](#b)

**Request:** Find posts in workspaces listed on profiles of people who belong to three of these review channels.

**Selection:** Message/Channel.team_id matches a listed UserTeam/User witness whose COUNT(ChannelMember rows over review channels) == 3.

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. The prompt supplies a finite candidate user roster by ID/link. Read the profiles to determine names, role flags, and listed workspace; do not supply those answers in the roster. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. The request explicitly supplies the review-channel list used to delimit membership questions. Enumerate conversations.members for every review channel and join by user ID. COUNT is per specified user or channel, not a count over unrelated witnesses. No joined_at or complete all-workspace membership enumeration is assumed. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Excluded from the current campaign by the user’s whole-group decision for B. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R066

**Route:** MESSAGE → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP → USER → REACTION

**Decision:** exclude

**Group:** [C](#c)

**Request:** Find posts in workspaces listed on profiles of people who gave a thumbs-up in these review channels.

**Selection:** Message/Channel.team_id matches listed UserTeam/User; that user contributed a MessageReaction with reaction_type == "thumbsup" in review messages.

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. The prompt supplies a finite candidate user roster by ID/link. Read the profiles to determine names, role flags, and listed workspace; do not supply those answers in the roster. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. The request explicitly supplies the review channels whose posts/reactions qualify people. Read their histories and reactions completely; the actor has the required source-workspace access. Join reaction user IDs, message author IDs, and message IDs according to the stated roles. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Excluded from the current campaign by the user’s whole-group decision for C. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R067

**Route:** MESSAGE → CONVERSATION → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Find posts in channels with three members among these channels.

**Selection:** For candidate Message, COUNT(ChannelMember rows on Message.channel_id) == 3.

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time)

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R068

**Route:** MESSAGE → CONVERSATION → CONVERSATION_MEMBERSHIP → USER

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Find posts in channels that include @tom among these channels.

**Selection:** Message/Channel joins ChannelMember/User with User.username == "tom".

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R069

**Route:** MESSAGE → CONVERSATION → CONVERSATION_MEMBERSHIP → USER → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [S2](#s2)

**Request:** Find posts in channels with members whose profiles identify them as workspace administrators.

**Selection:** Message/Channel joins ChannelMember/User and its profile-selected UserTeam with role in {admin, owner}.

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R070

**Route:** MESSAGE → CONVERSATION → CONVERSATION_MEMBERSHIP → USER → WORKSPACE_MEMBERSHIP → WORKSPACE

**Decision:** retain

**Group:** [S4](#s4)

**Request:** Find posts in channels with members whose profiles list workspace T_BETA.

**Selection:** Message/Channel joins ChannelMember/User and its profile-selected UserTeam with Team.team_id == "T_BETA".

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R071

**Route:** MESSAGE → CONVERSATION → CONVERSATION_MEMBERSHIP → USER → REACTION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Find posts in candidate channels with members who gave a thumbs-up in these review channels.

**Selection:** Message/Channel joins ChannelMember/User and a MessageReaction by that user with reaction_type == "thumbsup" in review messages.

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. The request explicitly supplies the review channels whose posts/reactions qualify people. Read their histories and reactions completely; the actor has the required source-workspace access. Join reaction user IDs, message author IDs, and message IDs according to the stated roles. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R072

**Route:** MESSAGE → USER

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Find @tom’s posts among these channels.

**Selection:** Message.user_id joins User.username == "tom".

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R073

**Route:** MESSAGE → USER → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [S2](#s2)

**Request:** Find posts by people whose profiles identify them as workspace administrators.

**Selection:** Message.user_id joins User and its profile-selected UserTeam with role in {admin, owner}.

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R074

**Route:** MESSAGE → USER → WORKSPACE_MEMBERSHIP → WORKSPACE

**Decision:** retain

**Group:** [S4](#s4)

**Request:** Find posts by people whose profiles list workspace T_BETA.

**Selection:** Message.user_id joins User and its profile-selected UserTeam with Team.team_id == "T_BETA".

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R075

**Route:** MESSAGE → USER → WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION

**Decision:** exclude

**Group:** [C](#c)

**Request:** Find posts by people whose profile-listed workspace has an incident-response channel in this channel list.

**Selection:** Message/User joins profile-selected UserTeam/Team and a scoped Channel with matching team_id and "incident response" in topic_text.

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. The request supplies a candidate channel list for the final workspace-to-channel relation. Use conversations.info on each to observe its actual workspace and topic, and conversations.members if a count is requested. It is not an exhaustive workspace channel-discovery claim. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Excluded from the current campaign by the user’s whole-group decision for C. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R076

**Route:** MESSAGE → USER → WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → CONVERSATION_MEMBERSHIP

**Decision:** exclude

**Group:** [C](#c)

**Request:** Find posts by people whose profile-listed workspace has a channel with three members in this channel list.

**Selection:** Message/User joins profile-selected UserTeam/Team and scoped Channel with matching team_id; COUNT(ChannelMember rows on that Channel) == 3.

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. The request supplies a candidate channel list for the final workspace-to-channel relation. Use conversations.info on each to observe its actual workspace and topic, and conversations.members if a count is requested. It is not an exhaustive workspace channel-discovery claim. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Excluded from the current campaign by the user’s whole-group decision for C. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R077

**Route:** MESSAGE → USER → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Find posts by people who belong to three of these review channels.

**Selection:** Message.user_id joins User with COUNT(ChannelMember rows for that user over review channels) == 3.

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. The request explicitly supplies the review-channel list used to delimit membership questions. Enumerate conversations.members for every review channel and join by user ID. COUNT is per specified user or channel, not a count over unrelated witnesses. No joined_at or complete all-workspace membership enumeration is assumed. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R078

**Route:** MESSAGE → USER → CONVERSATION_MEMBERSHIP → CONVERSATION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Find posts by members of #security, considering membership in these review channels.

**Selection:** Message/User joins ChannelMember/Channel with Channel.channel_name == "security" within review scope.

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. The request explicitly supplies the review-channel list used to delimit membership questions. Enumerate conversations.members for every review channel and join by user ID. COUNT is per specified user or channel, not a count over unrelated witnesses. No joined_at or complete all-workspace membership enumeration is assumed. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R079

**Route:** MESSAGE → USER → CONVERSATION_MEMBERSHIP → CONVERSATION → WORKSPACE

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Find posts by people who belong to channels in workspace T_BETA, considering this review-channel list.

**Selection:** Message/User joins ChannelMember/Channel with Channel.team_id == Team.team_id == "T_BETA" in review scope.

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. The request explicitly supplies the review-channel list used to delimit membership questions. Enumerate conversations.members for every review channel and join by user ID. COUNT is per specified user or channel, not a count over unrelated witnesses. No joined_at or complete all-workspace membership enumeration is assumed. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R080

**Route:** MESSAGE → USER → CONVERSATION_MEMBERSHIP → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP

**Decision:** exclude

**Group:** [D](#d)

**Request:** Find posts by people who belong to review channels whose workspace is shown on an owner’s profile in this roster.

**Selection:** Message/User joins ChannelMember/Channel; Channel.team_id matches roster profile-selected UserTeam with role == owner.

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. The request explicitly supplies the review-channel list used to delimit membership questions. Enumerate conversations.members for every review channel and join by user ID. COUNT is per specified user or channel, not a count over unrelated witnesses. No joined_at or complete all-workspace membership enumeration is assumed. The prompt supplies a finite candidate user roster by ID/link. Read the profiles to determine names, role flags, and listed workspace; do not supply those answers in the roster. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context)

**Reason:** Excluded from the current campaign by the user’s whole-group decision for D. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R081

**Route:** MESSAGE → USER → REACTION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Find posts by people who gave a thumbs-up in these review channels.

**Selection:** Message.user_id joins User and MessageReaction by that user with reaction_type == "thumbsup" in review messages.

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. The request explicitly supplies the review channels whose posts/reactions qualify people. Read their histories and reactions completely; the actor has the required source-workspace access. Join reaction user IDs, message author IDs, and message IDs according to the stated roles. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R082

**Route:** MESSAGE → REACTION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Find posts with a thumbs-up reaction among these channels.

**Selection:** Exists MessageReaction with message_id == candidate Message.message_id and reaction_type == "thumbsup".

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R083

**Route:** MESSAGE → REACTION → USER

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Find posts @tom reacted to among these channels.

**Selection:** Message joins MessageReaction/User with User.username == "tom".

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R084

**Route:** MESSAGE → REACTION → USER → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [S2](#s2)

**Request:** Find posts reacted to by people whose profiles identify them as workspace administrators.

**Selection:** Message joins MessageReaction/User and profile-selected UserTeam with role in {admin, owner}.

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R085

**Route:** MESSAGE → REACTION → USER → WORKSPACE_MEMBERSHIP → WORKSPACE

**Decision:** retain

**Group:** [S4](#s4)

**Request:** Find posts reacted to by people whose profiles list workspace T_BETA.

**Selection:** Message joins MessageReaction/User and profile-selected UserTeam with Team.team_id == "T_BETA".

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R086

**Route:** MESSAGE → REACTION → USER → WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION

**Decision:** exclude

**Group:** [C](#c)

**Request:** Find posts reacted to by people whose profile-listed workspace has an incident-response channel in this channel list.

**Selection:** Message joins MessageReaction/User, profile-selected UserTeam/Team, and scoped Channel with matching team_id and "incident response" in topic_text.

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. The request supplies a candidate channel list for the final workspace-to-channel relation. Use conversations.info on each to observe its actual workspace and topic, and conversations.members if a count is requested. It is not an exhaustive workspace channel-discovery claim. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Excluded from the current campaign by the user’s whole-group decision for C. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R087

**Route:** MESSAGE → REACTION → USER → WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → CONVERSATION_MEMBERSHIP

**Decision:** exclude

**Group:** [C](#c)

**Request:** Find posts reacted to by people whose profile-listed workspace has a channel with three members in this channel list.

**Selection:** Message joins MessageReaction/User, profile-selected UserTeam/Team, and scoped Channel; COUNT(ChannelMember rows on that channel) == 3.

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. The request supplies a candidate channel list for the final workspace-to-channel relation. Use conversations.info on each to observe its actual workspace and topic, and conversations.members if a count is requested. It is not an exhaustive workspace channel-discovery claim. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Excluded from the current campaign by the user’s whole-group decision for C. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R088

**Route:** MESSAGE → REACTION → USER → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Find posts reacted to by people who belong to three of these review channels.

**Selection:** Message joins MessageReaction/User with COUNT(ChannelMember rows for that reactor over review channels) == 3.

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. The request explicitly supplies the review-channel list used to delimit membership questions. Enumerate conversations.members for every review channel and join by user ID. COUNT is per specified user or channel, not a count over unrelated witnesses. No joined_at or complete all-workspace membership enumeration is assumed. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R089

**Route:** MESSAGE → REACTION → USER → CONVERSATION_MEMBERSHIP → CONVERSATION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Find posts reacted to by members of #security, considering membership in these review channels.

**Selection:** Message joins MessageReaction/User, ChannelMember/Channel, and Channel.channel_name == "security" in review scope.

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. The request explicitly supplies the review-channel list used to delimit membership questions. Enumerate conversations.members for every review channel and join by user ID. COUNT is per specified user or channel, not a count over unrelated witnesses. No joined_at or complete all-workspace membership enumeration is assumed. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R090

**Route:** MESSAGE → REACTION → USER → CONVERSATION_MEMBERSHIP → CONVERSATION → WORKSPACE

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Find posts reacted to by people who belong to channels in workspace T_BETA, considering this review-channel list.

**Selection:** Message joins MessageReaction/User, ChannelMember/Channel, and Team.team_id == "T_BETA" via Channel.team_id in review scope.

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. The request explicitly supplies the review-channel list used to delimit membership questions. Enumerate conversations.members for every review channel and join by user ID. COUNT is per specified user or channel, not a count over unrelated witnesses. No joined_at or complete all-workspace membership enumeration is assumed. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R091

**Route:** MESSAGE → REACTION → USER → CONVERSATION_MEMBERSHIP → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP

**Decision:** exclude

**Group:** [D](#d)

**Request:** Find posts reacted to by people who belong to review channels whose workspace is shown on an owner’s profile in this roster.

**Selection:** Message joins MessageReaction/User, ChannelMember/Channel; that Channel.team_id matches a roster profile-selected UserTeam with role == owner.

**Scope:** The prompt supplies the channels whose histories form the candidate-post pool. The acting user has access/membership required by conversations.history in those workspaces; paginate to exhaust the pool. The pool contains both qualifying and nonqualifying posts when the intended mode calls for them. The request explicitly supplies the review-channel list used to delimit membership questions. Enumerate conversations.members for every review channel and join by user ID. COUNT is per specified user or channel, not a count over unrelated witnesses. No joined_at or complete all-workspace membership enumeration is assumed. The prompt supplies a finite candidate user roster by ID/link. Read the profiles to determine names, role flags, and listed workspace; do not supply those answers in the roster. Interpret workspace membership exactly as the one displayed by users.info in that user profile. Never call it primary, infer all memberships, or treat absent profiles as proven absent users. For admin predicates use is_admin (admin or owner); for owner use is_owner. Unrestricted arbitrary-workspace membership/role variants require separate limitation analysis. User IDs must come from the supplied candidate roster, observed message authors/reaction users, or conversations.members; users.info accepts IDs and does not itself search names. Populate the intended user profile data in the construction so it is readable; do not assume users.list spans other workspaces.

**API evidence:** systematic modeling/slack-conceptual-model.md:69-111 (relationship roles/cardinalities and no extra membership consistency); conversations.info: backend/src/services/slack/api/methods.py:1727; _get_env_team_id:767; _serialize_conversation:356,465 (actual non-DM channel workspace, name/topic, optional member count); conversations.history: systematic modeling/slack-coverage-ledger.md:A07; backend/src/services/slack/database/operations.py:681 (scoped messages, author IDs, text; actor workspace membership prerequisite); conversations.members: backend/src/services/slack/api/methods.py:2029; backend/src/services/slack/database/operations.py:620 (complete paginated member IDs for known channel); model:46 (unique user/channel pair, hidden join_time); users.info: backend/src/services/slack/api/methods.py:2297; _get_env_team_id:767; _serialize_user:2373 (username and one listed workspace membership; role flags in that membership context); reactions.get: backend/src/services/slack/api/methods.py:2208 (all stored reactions grouped by emoji with complete replica user list and count); ledger:A22

**Reason:** Excluded from the current campaign by the user’s whole-group decision for D. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R092

**Route:** REACTION → MESSAGE

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reactions on messages containing the launch checklist.

**Selection:** EXISTS m: r.message_id=m.message_id AND "launch checklist" in m.message_text.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R093

**Route:** REACTION → MESSAGE → CONVERSATION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reactions on messages in #engineering.

**Selection:** EXISTS m,c: r.message_id=m.message_id AND m.channel_id=c.channel_id AND c.channel_name="engineering".

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R094

**Route:** REACTION → MESSAGE → CONVERSATION → WORKSPACE

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Reactions on messages in workspace T_RESEARCH, across these channels.

**Selection:** EXISTS m,c,w: r.message_id=m.message_id AND m.channel_id=c.channel_id AND c.team_id=w.team_id AND w.team_id="T_RESEARCH".

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R095

**Route:** REACTION → MESSAGE → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [A](#a)

**Request:** Reactions in a workspace that one of these reviewers lists on their profile with an administrator role.

**Selection:** EXISTS m,c,w,wm: r.message_id=m.message_id AND m.channel_id=c.channel_id AND c.team_id=w.team_id AND wm.team_id=w.team_id AND wm.user_id IN reviewer_roster AND wm.role IN {admin,owner}; wm is the membership used by that reviewer's profile.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R096

**Route:** REACTION → MESSAGE → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP → USER

**Decision:** retain

**Group:** [A](#a)

**Request:** Reactions in the workspace listed on Tom's profile.

**Selection:** EXISTS m,c,w,wm,u: r.message_id=m.message_id AND m.channel_id=c.channel_id AND c.team_id=w.team_id AND wm.team_id=w.team_id AND wm.user_id=u.user_id AND u.real_name="Tom"; wm is the profile-listed membership.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R097

**Route:** REACTION → MESSAGE → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP → USER → CONVERSATION_MEMBERSHIP

**Decision:** exclude

**Group:** [B](#b)

**Request:** Reactions in workspaces represented on the profiles of reviewers who belong to at least three of the listed channels.

**Selection:** EXISTS m,c,w,wm,u: r.message_id=m.message_id AND m.channel_id=c.channel_id AND c.team_id=w.team_id AND wm.team_id=w.team_id AND wm.user_id=u.user_id AND u.user_id IN reviewer_roster AND COUNT(cm WHERE cm.user_id=u.user_id AND cm.channel_id IN listed_channels)>=3; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Excluded from the current campaign by the user’s whole-group decision for B. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R098

**Route:** REACTION → MESSAGE → CONVERSATION → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reactions in channels with three members.

**Selection:** EXISTS m,c: r.message_id=m.message_id AND m.channel_id=c.channel_id AND COUNT(cm WHERE cm.channel_id=c.channel_id)=3.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R099

**Route:** REACTION → MESSAGE → CONVERSATION → CONVERSATION_MEMBERSHIP → USER

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reactions in channels that Tom belongs to.

**Selection:** EXISTS m,c,cm,u: r.message_id=m.message_id AND m.channel_id=c.channel_id AND cm.channel_id=c.channel_id AND cm.user_id=u.user_id AND u.real_name="Tom".

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R100

**Route:** REACTION → MESSAGE → CONVERSATION → CONVERSATION_MEMBERSHIP → USER → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [S2](#s2)

**Request:** Reactions in channels with a member whose profile shows a workspace administrator role.

**Selection:** EXISTS m,c,cm,u,wm: r.message_id=m.message_id AND m.channel_id=c.channel_id AND cm.channel_id=c.channel_id AND cm.user_id=u.user_id AND wm.user_id=u.user_id AND wm.role IN {admin,owner}; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R101

**Route:** REACTION → MESSAGE → CONVERSATION → CONVERSATION_MEMBERSHIP → USER → WORKSPACE_MEMBERSHIP → WORKSPACE

**Decision:** retain

**Group:** [S4](#s4)

**Request:** Reactions in channels with a member whose profile lists workspace T_RESEARCH.

**Selection:** EXISTS m,c,cm,u,wm,w: r.message_id=m.message_id AND m.channel_id=c.channel_id AND cm.channel_id=c.channel_id AND cm.user_id=u.user_id AND wm.user_id=u.user_id AND wm.team_id=w.team_id AND w.team_id="T_RESEARCH"; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R102

**Route:** REACTION → MESSAGE → USER

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reactions to messages written by Tom.

**Selection:** EXISTS m,u: r.message_id=m.message_id AND m.user_id=u.user_id AND u.real_name="Tom".

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R103

**Route:** REACTION → MESSAGE → USER → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [S2](#s2)

**Request:** Reactions to messages by people whose profiles show a workspace administrator role.

**Selection:** EXISTS m,u,wm: r.message_id=m.message_id AND m.user_id=u.user_id AND wm.user_id=u.user_id AND wm.role IN {admin,owner}; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R104

**Route:** REACTION → MESSAGE → USER → WORKSPACE_MEMBERSHIP → WORKSPACE

**Decision:** retain

**Group:** [S4](#s4)

**Request:** Reactions to messages by people whose profiles list workspace T_RESEARCH.

**Selection:** EXISTS m,u,wm,w: r.message_id=m.message_id AND m.user_id=u.user_id AND wm.user_id=u.user_id AND wm.team_id=w.team_id AND w.team_id="T_RESEARCH"; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R105

**Route:** REACTION → MESSAGE → USER → WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION

**Decision:** exclude

**Group:** [C](#c)

**Request:** Reactions to messages by people whose profile-listed workspace contains #engineering.

**Selection:** EXISTS m,u,wm,w,c: r.message_id=m.message_id AND m.user_id=u.user_id AND wm.user_id=u.user_id AND wm.team_id=w.team_id AND c.team_id=w.team_id AND c.channel_name="engineering"; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Excluded from the current campaign by the user’s whole-group decision for C. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R106

**Route:** REACTION → MESSAGE → USER → WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → CONVERSATION_MEMBERSHIP

**Decision:** exclude

**Group:** [C](#c)

**Request:** Reactions to messages by people whose profile-listed workspace contains one of these channels with three members.

**Selection:** EXISTS m,u,wm,w,c: r.message_id=m.message_id AND m.user_id=u.user_id AND wm.user_id=u.user_id AND wm.team_id=w.team_id AND c.team_id=w.team_id AND c.channel_id IN listed_channels AND COUNT(cm WHERE cm.channel_id=c.channel_id)=3; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Excluded from the current campaign by the user’s whole-group decision for C. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R107

**Route:** REACTION → MESSAGE → USER → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reactions to messages by people who belong to at least three of the listed channels.

**Selection:** EXISTS m,u: r.message_id=m.message_id AND m.user_id=u.user_id AND COUNT(cm WHERE cm.user_id=u.user_id AND cm.channel_id IN listed_channels)>=3.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R108

**Route:** REACTION → MESSAGE → USER → CONVERSATION_MEMBERSHIP → CONVERSATION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reactions to messages by members of #engineering.

**Selection:** EXISTS m,u,cm,c: r.message_id=m.message_id AND m.user_id=u.user_id AND cm.user_id=u.user_id AND cm.channel_id=c.channel_id AND c.channel_name="engineering".

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R109

**Route:** REACTION → MESSAGE → USER → CONVERSATION_MEMBERSHIP → CONVERSATION → WORKSPACE

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Reactions to messages by people who belong to one of these channels in workspace T_RESEARCH.

**Selection:** EXISTS m,u,cm,c,w: r.message_id=m.message_id AND m.user_id=u.user_id AND cm.user_id=u.user_id AND cm.channel_id=c.channel_id AND c.channel_id IN listed_channels AND c.team_id=w.team_id AND w.team_id="T_RESEARCH".

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R110

**Route:** REACTION → MESSAGE → USER → CONVERSATION_MEMBERSHIP → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP

**Decision:** exclude

**Group:** [D](#d)

**Request:** Reactions to messages by people who belong to a listed channel in a workspace shown on an administrator reviewer's profile.

**Selection:** EXISTS m,u,cm,c,w,wm: r.message_id=m.message_id AND m.user_id=u.user_id AND cm.user_id=u.user_id AND cm.channel_id=c.channel_id AND c.channel_id IN listed_channels AND c.team_id=w.team_id AND wm.team_id=w.team_id AND wm.user_id IN reviewer_roster AND wm.role IN {admin,owner}; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Excluded from the current campaign by the user’s whole-group decision for D. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R111

**Route:** REACTION → USER

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reactions added by Tom.

**Selection:** EXISTS u: r.user_id=u.user_id AND u.real_name="Tom".

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R112

**Route:** REACTION → USER → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [S2](#s2)

**Request:** Reactions added by people whose profiles show a workspace administrator role.

**Selection:** EXISTS u,wm: r.user_id=u.user_id AND wm.user_id=u.user_id AND wm.role IN {admin,owner}; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R113

**Route:** REACTION → USER → WORKSPACE_MEMBERSHIP → WORKSPACE

**Decision:** retain

**Group:** [S4](#s4)

**Request:** Reactions added by people whose profiles list workspace T_RESEARCH.

**Selection:** EXISTS u,wm,w: r.user_id=u.user_id AND wm.user_id=u.user_id AND wm.team_id=w.team_id AND w.team_id="T_RESEARCH"; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R114

**Route:** REACTION → USER → WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION

**Decision:** exclude

**Group:** [C](#c)

**Request:** Reactions added by people whose profile-listed workspace contains #engineering.

**Selection:** EXISTS u,wm,w,c: r.user_id=u.user_id AND wm.user_id=u.user_id AND wm.team_id=w.team_id AND c.team_id=w.team_id AND c.channel_name="engineering"; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Excluded from the current campaign by the user’s whole-group decision for C. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R115

**Route:** REACTION → USER → WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → CONVERSATION_MEMBERSHIP

**Decision:** exclude

**Group:** [C](#c)

**Request:** Reactions added by people whose profile-listed workspace contains one of these channels with three members.

**Selection:** EXISTS u,wm,w,c: r.user_id=u.user_id AND wm.user_id=u.user_id AND wm.team_id=w.team_id AND c.team_id=w.team_id AND c.channel_id IN listed_channels AND COUNT(cm WHERE cm.channel_id=c.channel_id)=3; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Excluded from the current campaign by the user’s whole-group decision for C. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R116

**Route:** REACTION → USER → WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → MESSAGE

**Decision:** exclude

**Group:** [C](#c)

**Request:** Reactions added by people whose profile-listed workspace contains a launch-checklist message in one of these channels.

**Selection:** EXISTS u,wm,w,c,m: r.user_id=u.user_id AND wm.user_id=u.user_id AND wm.team_id=w.team_id AND c.team_id=w.team_id AND c.channel_id IN listed_channels AND m.channel_id=c.channel_id AND "launch checklist" in m.message_text; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Excluded from the current campaign by the user’s whole-group decision for C. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R117

**Route:** REACTION → USER → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reactions added by people who belong to at least three of the listed channels.

**Selection:** EXISTS u: r.user_id=u.user_id AND COUNT(cm WHERE cm.user_id=u.user_id AND cm.channel_id IN listed_channels)>=3.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R118

**Route:** REACTION → USER → CONVERSATION_MEMBERSHIP → CONVERSATION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reactions added by members of #engineering.

**Selection:** EXISTS u,cm,c: r.user_id=u.user_id AND cm.user_id=u.user_id AND cm.channel_id=c.channel_id AND c.channel_name="engineering".

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R119

**Route:** REACTION → USER → CONVERSATION_MEMBERSHIP → CONVERSATION → WORKSPACE

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Reactions added by people who belong to a listed channel in workspace T_RESEARCH.

**Selection:** EXISTS u,cm,c,w: r.user_id=u.user_id AND cm.user_id=u.user_id AND cm.channel_id=c.channel_id AND c.channel_id IN listed_channels AND c.team_id=w.team_id AND w.team_id="T_RESEARCH".

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R120

**Route:** REACTION → USER → CONVERSATION_MEMBERSHIP → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP

**Decision:** exclude

**Group:** [D](#d)

**Request:** Reactions added by people who belong to a listed channel in a workspace shown on an administrator reviewer's profile.

**Selection:** EXISTS u,cm,c,w,wm: r.user_id=u.user_id AND cm.user_id=u.user_id AND cm.channel_id=c.channel_id AND c.channel_id IN listed_channels AND c.team_id=w.team_id AND wm.team_id=w.team_id AND wm.user_id IN reviewer_roster AND wm.role IN {admin,owner}; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Excluded from the current campaign by the user’s whole-group decision for D. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R121

**Route:** REACTION → USER → CONVERSATION_MEMBERSHIP → CONVERSATION → MESSAGE

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reactions added by members of a listed channel containing a launch-checklist message.

**Selection:** EXISTS u,cm,c,m: r.user_id=u.user_id AND cm.user_id=u.user_id AND cm.channel_id=c.channel_id AND c.channel_id IN listed_channels AND m.channel_id=c.channel_id AND "launch checklist" in m.message_text.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R122

**Route:** REACTION → USER → MESSAGE

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reactions added by people who posted a launch checklist in these channels.

**Selection:** EXISTS u,m: r.user_id=u.user_id AND m.user_id=u.user_id AND m.channel_id IN listed_channels AND "launch checklist" in m.message_text.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R123

**Route:** REACTION → USER → MESSAGE → CONVERSATION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reactions added by people who have posted in #engineering.

**Selection:** EXISTS u,m,c: r.user_id=u.user_id AND m.user_id=u.user_id AND m.channel_id=c.channel_id AND c.channel_name="engineering".

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R124

**Route:** REACTION → USER → MESSAGE → CONVERSATION → WORKSPACE

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Reactions added by people who posted in a listed channel in workspace T_RESEARCH.

**Selection:** EXISTS u,m,c,w: r.user_id=u.user_id AND m.user_id=u.user_id AND m.channel_id=c.channel_id AND c.channel_id IN listed_channels AND c.team_id=w.team_id AND w.team_id="T_RESEARCH".

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R125

**Route:** REACTION → USER → MESSAGE → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP

**Decision:** exclude

**Group:** [D](#d)

**Request:** Reactions added by people who posted in a listed channel whose workspace is shown on an administrator reviewer's profile.

**Selection:** EXISTS u,m,c,w,wm: r.user_id=u.user_id AND m.user_id=u.user_id AND m.channel_id=c.channel_id AND c.channel_id IN listed_channels AND c.team_id=w.team_id AND wm.team_id=w.team_id AND wm.user_id IN reviewer_roster AND wm.role IN {admin,owner}; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Excluded from the current campaign by the user’s whole-group decision for D. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R126

**Route:** REACTION → USER → MESSAGE → CONVERSATION → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reactions added by people who posted in one of these channels with three members.

**Selection:** EXISTS u,m,c: r.user_id=u.user_id AND m.user_id=u.user_id AND m.channel_id=c.channel_id AND c.channel_id IN listed_channels AND COUNT(cm WHERE cm.channel_id=c.channel_id)=3.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R127

**Route:** USER → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [S2](#s2)

**Request:** Reviewers whose profiles show a workspace administrator role.

**Selection:** EXISTS wm: wm.user_id=u.user_id AND wm.role IN {admin,owner}; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R128

**Route:** USER → WORKSPACE_MEMBERSHIP → WORKSPACE

**Decision:** retain

**Group:** [S4](#s4)

**Request:** Reviewers whose profiles list workspace T_RESEARCH.

**Selection:** EXISTS wm,w: wm.user_id=u.user_id AND wm.team_id=w.team_id AND w.team_id="T_RESEARCH"; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R129

**Route:** USER → WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION

**Decision:** retain

**Group:** [A](#a)

**Request:** Reviewers whose profile-listed workspace contains #engineering.

**Selection:** EXISTS wm,w,c: wm.user_id=u.user_id AND wm.team_id=w.team_id AND c.team_id=w.team_id AND c.channel_name="engineering"; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R130

**Route:** USER → WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [A](#a)

**Request:** Reviewers whose profile-listed workspace contains one of these channels with three members.

**Selection:** EXISTS wm,w,c: wm.user_id=u.user_id AND wm.team_id=w.team_id AND c.team_id=w.team_id AND c.channel_id IN listed_channels AND COUNT(cm WHERE cm.channel_id=c.channel_id)=3; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R131

**Route:** USER → WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → MESSAGE

**Decision:** retain

**Group:** [A](#a)

**Request:** Reviewers whose profile-listed workspace contains a launch-checklist message in one of these channels.

**Selection:** EXISTS wm,w,c,m: wm.user_id=u.user_id AND wm.team_id=w.team_id AND c.team_id=w.team_id AND c.channel_id IN listed_channels AND m.channel_id=c.channel_id AND "launch checklist" in m.message_text; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R132

**Route:** USER → WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → MESSAGE → REACTION

**Decision:** retain

**Group:** [A](#a)

**Request:** Reviewers whose profile-listed workspace contains a thumbs-up reaction on a message in one of these channels.

**Selection:** EXISTS wm,w,c,m,r: wm.user_id=u.user_id AND wm.team_id=w.team_id AND c.team_id=w.team_id AND c.channel_id IN listed_channels AND m.channel_id=c.channel_id AND r.message_id=m.message_id AND r.reaction_type="thumbsup"; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R133

**Route:** USER → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reviewers who belong to at least three of these channels.

**Selection:** COUNT(cm WHERE cm.user_id=u.user_id AND cm.channel_id IN listed_channels)>=3.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R134

**Route:** USER → CONVERSATION_MEMBERSHIP → CONVERSATION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reviewers who belong to #engineering.

**Selection:** EXISTS cm,c: cm.user_id=u.user_id AND cm.channel_id=c.channel_id AND c.channel_name="engineering".

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R135

**Route:** USER → CONVERSATION_MEMBERSHIP → CONVERSATION → WORKSPACE

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Reviewers who belong to one of these channels in workspace T_RESEARCH.

**Selection:** EXISTS cm,c,w: cm.user_id=u.user_id AND cm.channel_id=c.channel_id AND c.channel_id IN listed_channels AND c.team_id=w.team_id AND w.team_id="T_RESEARCH".

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R136

**Route:** USER → CONVERSATION_MEMBERSHIP → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [A](#a)

**Request:** Reviewers who belong to a listed channel whose workspace is shown on an administrator contact's profile.

**Selection:** EXISTS cm,c,w,wm: cm.user_id=u.user_id AND cm.channel_id=c.channel_id AND c.channel_id IN listed_channels AND c.team_id=w.team_id AND wm.team_id=w.team_id AND wm.user_id IN contact_roster AND wm.role IN {admin,owner}; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R137

**Route:** USER → CONVERSATION_MEMBERSHIP → CONVERSATION → MESSAGE

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reviewers who belong to one of these channels containing a launch-checklist message.

**Selection:** EXISTS cm,c,m: cm.user_id=u.user_id AND cm.channel_id=c.channel_id AND c.channel_id IN listed_channels AND m.channel_id=c.channel_id AND "launch checklist" in m.message_text.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R138

**Route:** USER → CONVERSATION_MEMBERSHIP → CONVERSATION → MESSAGE → REACTION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reviewers who belong to one of these channels containing a message with a thumbs-up reaction.

**Selection:** EXISTS cm,c,m,r: cm.user_id=u.user_id AND cm.channel_id=c.channel_id AND c.channel_id IN listed_channels AND m.channel_id=c.channel_id AND r.message_id=m.message_id AND r.reaction_type="thumbsup".

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R139

**Route:** USER → MESSAGE

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reviewers who posted a launch checklist in these channels.

**Selection:** EXISTS m: m.user_id=u.user_id AND m.channel_id IN listed_channels AND "launch checklist" in m.message_text.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R140

**Route:** USER → MESSAGE → CONVERSATION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reviewers who have posted in #engineering.

**Selection:** EXISTS m,c: m.user_id=u.user_id AND m.channel_id=c.channel_id AND c.channel_name="engineering".

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R141

**Route:** USER → MESSAGE → CONVERSATION → WORKSPACE

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Reviewers who posted in a listed channel in workspace T_RESEARCH.

**Selection:** EXISTS m,c,w: m.user_id=u.user_id AND m.channel_id=c.channel_id AND c.channel_id IN listed_channels AND c.team_id=w.team_id AND w.team_id="T_RESEARCH".

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R142

**Route:** USER → MESSAGE → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [A](#a)

**Request:** Reviewers who posted in a listed channel whose workspace is shown on an administrator contact's profile.

**Selection:** EXISTS m,c,w,wm: m.user_id=u.user_id AND m.channel_id=c.channel_id AND c.channel_id IN listed_channels AND c.team_id=w.team_id AND wm.team_id=w.team_id AND wm.user_id IN contact_roster AND wm.role IN {admin,owner}; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R143

**Route:** USER → MESSAGE → CONVERSATION → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reviewers who posted in one of these channels with three members.

**Selection:** EXISTS m,c: m.user_id=u.user_id AND m.channel_id=c.channel_id AND c.channel_id IN listed_channels AND COUNT(cm WHERE cm.channel_id=c.channel_id)=3.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R144

**Route:** USER → MESSAGE → REACTION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reviewers whose messages in these channels received a thumbs-up reaction.

**Selection:** EXISTS m,r: m.user_id=u.user_id AND m.channel_id IN listed_channels AND r.message_id=m.message_id AND r.reaction_type="thumbsup".

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R145

**Route:** USER → REACTION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reviewers who added a thumbs-up reaction to a message in these channels.

**Selection:** EXISTS r: r.user_id=u.user_id AND r.reaction_type="thumbsup" AND r.message_id IN messages_in_listed_channels.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R146

**Route:** USER → REACTION → MESSAGE

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reviewers who reacted to a launch-checklist message in these channels.

**Selection:** EXISTS r,m: r.user_id=u.user_id AND r.message_id=m.message_id AND m.channel_id IN listed_channels AND "launch checklist" in m.message_text.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R147

**Route:** USER → REACTION → MESSAGE → CONVERSATION

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reviewers who reacted to a message in #engineering.

**Selection:** EXISTS r,m,c: r.user_id=u.user_id AND r.message_id=m.message_id AND m.channel_id=c.channel_id AND c.channel_name="engineering".

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R148

**Route:** USER → REACTION → MESSAGE → CONVERSATION → WORKSPACE

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Reviewers who reacted to a message in a listed channel in workspace T_RESEARCH.

**Selection:** EXISTS r,m,c,w: r.user_id=u.user_id AND r.message_id=m.message_id AND m.channel_id=c.channel_id AND c.channel_id IN listed_channels AND c.team_id=w.team_id AND w.team_id="T_RESEARCH".

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R149

**Route:** USER → REACTION → MESSAGE → CONVERSATION → WORKSPACE → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [A](#a)

**Request:** Reviewers who reacted to a message in a listed channel whose workspace is shown on an administrator contact's profile.

**Selection:** EXISTS r,m,c,w,wm: r.user_id=u.user_id AND r.message_id=m.message_id AND m.channel_id=c.channel_id AND c.channel_id IN listed_channels AND c.team_id=w.team_id AND wm.team_id=w.team_id AND wm.user_id IN contact_roster AND wm.role IN {admin,owner}; wm is profile-listed.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion. Workspace-membership predicates concern only the membership displayed by users.info/profile (team_id and owner/admin flags), as the fragment states. They do not claim to discover every membership or a primary/default workspace. The roster/named contacts supply candidate user IDs, not their roles or workspace assignments; users.info supplies those facts. Unrestricted discovery of additional workspace memberships remains a limitation.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.info derives workspace from the addressed channel and serializes context_team_id; methods.py:767,1727 and _serialize_conversation:356; no Team-name inference.; users.info selects target user's profile membership; _get_env_team_id:767, users_info:2297, _serialize_user:2373-2440 expose team_id and owner/admin only; ledger H02,A23.

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R150

**Route:** USER → REACTION → MESSAGE → CONVERSATION → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S1](#s1)

**Request:** Reviewers who reacted to a message in one of these channels with three members.

**Selection:** EXISTS r,m,c: r.user_id=u.user_id AND r.message_id=m.message_id AND m.channel_id=c.channel_id AND c.channel_id IN listed_channels AND COUNT(cm WHERE cm.channel_id=c.channel_id)=3.

**Scope:** Candidate channels are supplied as an ordinary audit scope or discoverable within the actor's workspace; all referenced histories are readable by the actor, and channel/message/member/reaction pagination is completed. Known anchors identify candidate populations, not the matching roots. For cross-workspace witnesses, use at least two channels from different workspaces; obtain their true context_team_id through conversations.info and do not assume global list/search enumerates them. The supplied reviewer roster bounds the candidate users; a finite candidate roster is an ordinary request scope and does not reveal which users satisfy the criterion. Membership is read using conversations.members for the relevant known channels; do not infer channel membership from workspace membership. A count of memberships across listed channels counts distinct channel/user pairs; a per-channel member count counts that channel's membership rows.

**API evidence:** conversations.history and conversations.info: backend/src/services/slack/api/methods.py:1144,1727; source-derived cross-workspace history conditions in grounding/slack_coverage/workspace_scope_audit.md.; reactions.get groups by emoji and returns all participating user IDs/counts: backend/src/services/slack/api/methods.py:2208-2257; systematic modeling/slack-coverage-ledger.md A22.; User identities/names from users.info/users.list; systematic modeling/slack-coverage-ledger.md H02,A23,A24.; conversations.members: backend/src/services/slack/api/methods.py:2029-2089; derived num_members in _serialize_conversation:356 and ledger H01,A19; channel_members has unique (channel_id,user_id) identity.

**Reason:** Retain the scoped witness under group S1. Complete selectors use exposed message, user, channel, reaction and membership facts in a readable channel scope. These include useful long relations; they are not limited by edge depth. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R151

**Route:** WORKSPACE → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [S4](#s4)

**Request:** Among the workspace associations shown on review-roster profiles, list workspaces with at least two people shown as admins.

**Selection:** count(profile-shown user_teams rows with role in {admin,owner}) >= 2

**Scope:** Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R152

**Route:** WORKSPACE → WORKSPACE_MEMBERSHIP → USER

**Decision:** retain

**Group:** [S4](#s4)

**Request:** Among the workspace associations shown on review-roster profiles, list workspaces that include a person named Alex.

**Selection:** users.real_name matches Alex

**Scope:** Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R153

**Route:** WORKSPACE → WORKSPACE_MEMBERSHIP → USER → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S4](#s4)

**Request:** List workspaces shown on review-roster profiles that have a roster person belonging to at least three audit channels.

**Selection:** count(channel_members for the same user within audit channel list) >= 3

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.members; methods.py:2029,2081; operations.py:620; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R154

**Route:** WORKSPACE → WORKSPACE_MEMBERSHIP → USER → CONVERSATION_MEMBERSHIP → CONVERSATION

**Decision:** retain

**Group:** [S4](#s4)

**Request:** List workspaces shown on review-roster profiles that have a roster person in the audit channel named security.

**Selection:** channels.channel_name == security

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R155

**Route:** WORKSPACE → WORKSPACE_MEMBERSHIP → USER → CONVERSATION_MEMBERSHIP → CONVERSATION → MESSAGE

**Decision:** retain

**Group:** [S4](#s4)

**Request:** List workspaces shown on review-roster profiles that have a roster person in an audit channel discussing launch.

**Selection:** messages.message_text contains launch

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R156

**Route:** WORKSPACE → WORKSPACE_MEMBERSHIP → USER → CONVERSATION_MEMBERSHIP → CONVERSATION → MESSAGE → REACTION

**Decision:** retain

**Group:** [S4](#s4)

**Request:** List workspaces shown on review-roster profiles that have a roster person in an audit channel with a message receiving a thumbs-up.

**Selection:** message_reactions.reaction_type == thumbsup

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R157

**Route:** WORKSPACE → WORKSPACE_MEMBERSHIP → USER → MESSAGE

**Decision:** retain

**Group:** [S4](#s4)

**Request:** List workspaces shown on review-roster profiles that have a roster person who posted about launch in the audit histories.

**Selection:** messages.message_text contains launch

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R158

**Route:** WORKSPACE → WORKSPACE_MEMBERSHIP → USER → MESSAGE → CONVERSATION

**Decision:** retain

**Group:** [S4](#s4)

**Request:** List workspaces shown on review-roster profiles that have a roster person who posted in the audit channel named security.

**Selection:** channels.channel_name == security

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R159

**Route:** WORKSPACE → WORKSPACE_MEMBERSHIP → USER → MESSAGE → CONVERSATION → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S4](#s4)

**Request:** List workspaces shown on review-roster profiles that have a roster person who posted in an audit channel with at least three members.

**Selection:** count(channel_members for the authored message channel) >= 3

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R160

**Route:** WORKSPACE → WORKSPACE_MEMBERSHIP → USER → MESSAGE → REACTION

**Decision:** retain

**Group:** [S4](#s4)

**Request:** List workspaces shown on review-roster profiles that have a roster person whose audit-history post received a thumbs-up.

**Selection:** message_reactions.reaction_type == thumbsup

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R161

**Route:** WORKSPACE → WORKSPACE_MEMBERSHIP → USER → REACTION

**Decision:** retain

**Group:** [S4](#s4)

**Request:** List workspaces shown on review-roster profiles that have a roster person who used a thumbs-up in the audit histories.

**Selection:** message_reactions.reaction_type == thumbsup

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R162

**Route:** WORKSPACE → WORKSPACE_MEMBERSHIP → USER → REACTION → MESSAGE

**Decision:** retain

**Group:** [S4](#s4)

**Request:** List workspaces shown on review-roster profiles that have a roster person who reacted to an audit-history message about launch.

**Selection:** messages.message_text contains launch

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R163

**Route:** WORKSPACE → WORKSPACE_MEMBERSHIP → USER → REACTION → MESSAGE → CONVERSATION

**Decision:** retain

**Group:** [S4](#s4)

**Request:** List workspaces shown on review-roster profiles that have a roster person who reacted to a message in the audit channel named security.

**Selection:** channels.channel_name == security

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R164

**Route:** WORKSPACE → WORKSPACE_MEMBERSHIP → USER → REACTION → MESSAGE → CONVERSATION → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S4](#s4)

**Request:** List workspaces shown on review-roster profiles that have a roster person who reacted to a message in an audit channel with at least three members.

**Selection:** count(channel_members for the reacted-to message channel) >= 3

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R165

**Route:** WORKSPACE → CONVERSATION

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Among the audit channels, list workspaces with a channel named security.

**Selection:** channels.channel_name == security

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R166

**Route:** WORKSPACE → CONVERSATION → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Among the audit channels, list workspaces with a channel having at least three members.

**Selection:** count(channel_members for a channel) >= 3

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R167

**Route:** WORKSPACE → CONVERSATION → CONVERSATION_MEMBERSHIP → USER

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Among the audit channels, list workspaces with a channel that includes someone named Alex.

**Selection:** users.real_name matches Alex

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R168

**Route:** WORKSPACE → CONVERSATION → CONVERSATION_MEMBERSHIP → USER → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [S4](#s4)

**Request:** Among the audit channels, list workspaces with a channel that includes someone shown as an admin in the workspace on their profile.

**Selection:** user_teams.role in {admin,owner}, profile-shown association

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R169

**Route:** WORKSPACE → CONVERSATION → CONVERSATION_MEMBERSHIP → USER → MESSAGE

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Among the audit channels, list workspaces with a channel that includes someone who posted about launch in the audit histories.

**Selection:** messages.message_text contains launch

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R170

**Route:** WORKSPACE → CONVERSATION → CONVERSATION_MEMBERSHIP → USER → MESSAGE → REACTION

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Among the audit channels, list workspaces with a channel that includes someone whose audit-history post received a thumbs-up.

**Selection:** message_reactions.reaction_type == thumbsup

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R171

**Route:** WORKSPACE → CONVERSATION → CONVERSATION_MEMBERSHIP → USER → REACTION

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Among the audit channels, list workspaces with a channel that includes someone who gave a thumbs-up in the audit histories.

**Selection:** message_reactions.reaction_type == thumbsup

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R172

**Route:** WORKSPACE → CONVERSATION → CONVERSATION_MEMBERSHIP → USER → REACTION → MESSAGE

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Among the audit channels, list workspaces with a channel that includes someone who reacted to an audit-history message about launch.

**Selection:** messages.message_text contains launch

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R173

**Route:** WORKSPACE → CONVERSATION → MESSAGE

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Among the audit channels, list workspaces containing a message about launch.

**Selection:** messages.message_text contains launch

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.history; methods.py:1144,1228; operations.py:681; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R174

**Route:** WORKSPACE → CONVERSATION → MESSAGE → USER

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Among the audit channels, list workspaces containing a message by someone named Alex.

**Selection:** users.real_name matches Alex

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R175

**Route:** WORKSPACE → CONVERSATION → MESSAGE → USER → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [S4](#s4)

**Request:** Among the audit channels, list workspaces containing a message by someone shown as an admin in the workspace on their profile.

**Selection:** user_teams.role in {admin,owner}, profile-shown association

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R176

**Route:** WORKSPACE → CONVERSATION → MESSAGE → USER → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Among the audit channels, list workspaces containing a message by someone who belongs to at least three audit channels.

**Selection:** count(channel_members for message author within audit channel list) >= 3

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R177

**Route:** WORKSPACE → CONVERSATION → MESSAGE → USER → REACTION

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Among the audit channels, list workspaces containing a message by someone who also gave a thumbs-up in the audit histories.

**Selection:** message_reactions.reaction_type == thumbsup

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R178

**Route:** WORKSPACE → CONVERSATION → MESSAGE → REACTION

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Among the audit channels, list workspaces containing a message with a thumbs-up reaction.

**Selection:** message_reactions.reaction_type == thumbsup

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R179

**Route:** WORKSPACE → CONVERSATION → MESSAGE → REACTION → USER

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Among the audit channels, list workspaces containing a message reacted to by someone named Alex.

**Selection:** users.real_name matches Alex

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R180

**Route:** WORKSPACE → CONVERSATION → MESSAGE → REACTION → USER → WORKSPACE_MEMBERSHIP

**Decision:** retain

**Group:** [S4](#s4)

**Request:** Among the audit channels, list workspaces containing a message reacted to by someone shown as an admin in the workspace on their profile.

**Selection:** user_teams.role in {admin,owner}, profile-shown association

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R181

**Route:** WORKSPACE → CONVERSATION → MESSAGE → REACTION → USER → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S3](#s3)

**Request:** Among the audit channels, list workspaces containing a message reacted to by someone who belongs to at least three audit channels.

**Selection:** count(channel_members for reaction user within audit channel list) >= 3

**Scope:** The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S3. Use visible workspace IDs on an explicitly bounded channel corpus, preserving the candidate scope. Stored workspace names and general workspace enumeration are not assumed available. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R182

**Route:** WORKSPACE_MEMBERSHIP → WORKSPACE

**Decision:** retain

**Group:** [S4](#s4)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries in workspace T_RESEARCH.

**Selection:** user_teams.team_id == T_RESEARCH

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R183

**Route:** WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION

**Decision:** retain

**Group:** [A](#a)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace contains an audit channel named security.

**Selection:** channels.channel_name == security

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R184

**Route:** WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [A](#a)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit channel with at least three members.

**Selection:** count(channel_members for the workspace audit channel) >= 3

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R185

**Route:** WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → CONVERSATION_MEMBERSHIP → USER

**Decision:** retain

**Group:** [A](#a)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit channel that includes someone named Alex.

**Selection:** users.real_name matches Alex

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R186

**Route:** WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → CONVERSATION_MEMBERSHIP → USER → MESSAGE

**Decision:** exclude

**Group:** [D](#d)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit channel including someone who posted about launch in the audit histories.

**Selection:** messages.message_text contains launch

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Excluded from the current campaign by the user’s whole-group decision for D. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R187

**Route:** WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → CONVERSATION_MEMBERSHIP → USER → MESSAGE → REACTION

**Decision:** exclude

**Group:** [D](#d)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit channel including someone whose audit-history post received a thumbs-up.

**Selection:** message_reactions.reaction_type == thumbsup

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Excluded from the current campaign by the user’s whole-group decision for D. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R188

**Route:** WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → CONVERSATION_MEMBERSHIP → USER → REACTION

**Decision:** exclude

**Group:** [D](#d)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit channel including someone who gave a thumbs-up in the audit histories.

**Selection:** message_reactions.reaction_type == thumbsup

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Excluded from the current campaign by the user’s whole-group decision for D. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R189

**Route:** WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → CONVERSATION_MEMBERSHIP → USER → REACTION → MESSAGE

**Decision:** exclude

**Group:** [D](#d)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit channel including someone who reacted to an audit-history message about launch.

**Selection:** messages.message_text contains launch

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Excluded from the current campaign by the user’s whole-group decision for D. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R190

**Route:** WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → MESSAGE

**Decision:** retain

**Group:** [A](#a)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit-channel message about launch.

**Selection:** messages.message_text contains launch

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R191

**Route:** WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → MESSAGE → USER

**Decision:** retain

**Group:** [A](#a)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit-channel message by someone named Alex.

**Selection:** users.real_name matches Alex

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R192

**Route:** WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → MESSAGE → USER → CONVERSATION_MEMBERSHIP

**Decision:** exclude

**Group:** [D](#d)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit-channel message by someone belonging to at least three audit channels.

**Selection:** count(channel_members for downstream message author within audit channel list) >= 3

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Excluded from the current campaign by the user’s whole-group decision for D. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R193

**Route:** WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → MESSAGE → USER → REACTION

**Decision:** exclude

**Group:** [D](#d)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit-channel message by someone who also gave a thumbs-up in the audit histories.

**Selection:** message_reactions.reaction_type == thumbsup

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Excluded from the current campaign by the user’s whole-group decision for D. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R194

**Route:** WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → MESSAGE → REACTION

**Decision:** retain

**Group:** [A](#a)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit-channel message with a thumbs-up reaction.

**Selection:** message_reactions.reaction_type == thumbsup

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R195

**Route:** WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → MESSAGE → REACTION → USER

**Decision:** retain

**Group:** [A](#a)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit-channel message reacted to by someone named Alex.

**Selection:** users.real_name matches Alex

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group A. Join the profile-shown workspace association to a channel or its contained records/direct participants. A participant may be the channel member, message author or reaction contributor. Identifying that participant is part of the connection; following another relation from that participant is not in this group. The ordinary witnesses directly connect workspace affiliation to the relevant channel, contained records or directly identified participant. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R196

**Route:** WORKSPACE_MEMBERSHIP → WORKSPACE → CONVERSATION → MESSAGE → REACTION → USER → CONVERSATION_MEMBERSHIP

**Decision:** exclude

**Group:** [D](#d)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries whose workspace has an audit-channel message reacted to by someone belonging to at least three audit channels.

**Selection:** count(channel_members for reaction contributor within audit channel list) >= 3

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Excluded from the current campaign by the user’s whole-group decision for D. The scoped request and API evidence are retained for possible reconsideration. This is not a claim of technical impossibility, semantic equivalence, or universal meaninglessness.

### R197

**Route:** WORKSPACE_MEMBERSHIP → USER

**Decision:** retain

**Group:** [S2](#s2)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people named Alex.

**Selection:** users.real_name matches Alex

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R198

**Route:** WORKSPACE_MEMBERSHIP → USER → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S2](#s2)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people in at least three audit channels.

**Selection:** count(channel_members for root user within audit channel list) >= 3

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.members; methods.py:2029,2081; operations.py:620; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R199

**Route:** WORKSPACE_MEMBERSHIP → USER → CONVERSATION_MEMBERSHIP → CONVERSATION

**Decision:** retain

**Group:** [S2](#s2)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people in the audit channel named security.

**Selection:** channels.channel_name == security

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R200

**Route:** WORKSPACE_MEMBERSHIP → USER → CONVERSATION_MEMBERSHIP → CONVERSATION → WORKSPACE

**Decision:** retain

**Group:** [S4](#s4)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people in an audit channel in workspace T_RESEARCH.

**Selection:** channels.team_id == T_RESEARCH

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R201

**Route:** WORKSPACE_MEMBERSHIP → USER → CONVERSATION_MEMBERSHIP → CONVERSATION → MESSAGE

**Decision:** retain

**Group:** [S2](#s2)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people in an audit channel discussing launch.

**Selection:** messages.message_text contains launch

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R202

**Route:** WORKSPACE_MEMBERSHIP → USER → CONVERSATION_MEMBERSHIP → CONVERSATION → MESSAGE → REACTION

**Decision:** retain

**Group:** [S2](#s2)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people in an audit channel with a message receiving a thumbs-up.

**Selection:** message_reactions.reaction_type == thumbsup

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R203

**Route:** WORKSPACE_MEMBERSHIP → USER → MESSAGE

**Decision:** retain

**Group:** [S2](#s2)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people who posted about launch in the audit histories.

**Selection:** messages.message_text contains launch

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R204

**Route:** WORKSPACE_MEMBERSHIP → USER → MESSAGE → CONVERSATION

**Decision:** retain

**Group:** [S2](#s2)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people who posted in the audit channel named security.

**Selection:** channels.channel_name == security

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R205

**Route:** WORKSPACE_MEMBERSHIP → USER → MESSAGE → CONVERSATION → WORKSPACE

**Decision:** retain

**Group:** [S4](#s4)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people who posted in an audit channel in workspace T_RESEARCH.

**Selection:** channels.team_id == T_RESEARCH

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R206

**Route:** WORKSPACE_MEMBERSHIP → USER → MESSAGE → CONVERSATION → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S2](#s2)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people who posted in an audit channel with at least three members.

**Selection:** count(channel_members for root user authored-message channel) >= 3

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R207

**Route:** WORKSPACE_MEMBERSHIP → USER → MESSAGE → REACTION

**Decision:** retain

**Group:** [S2](#s2)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people whose audit-history post received a thumbs-up.

**Selection:** message_reactions.reaction_type == thumbsup

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R208

**Route:** WORKSPACE_MEMBERSHIP → USER → REACTION

**Decision:** retain

**Group:** [S2](#s2)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people who gave a thumbs-up in the audit histories.

**Selection:** message_reactions.reaction_type == thumbsup

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R209

**Route:** WORKSPACE_MEMBERSHIP → USER → REACTION → MESSAGE

**Decision:** retain

**Group:** [S2](#s2)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people who reacted to an audit-history message about launch.

**Selection:** messages.message_text contains launch

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R210

**Route:** WORKSPACE_MEMBERSHIP → USER → REACTION → MESSAGE → CONVERSATION

**Decision:** retain

**Group:** [S2](#s2)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people who reacted to a message in the audit channel named security.

**Selection:** channels.channel_name == security

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R211

**Route:** WORKSPACE_MEMBERSHIP → USER → REACTION → MESSAGE → CONVERSATION → WORKSPACE

**Decision:** retain

**Group:** [S4](#s4)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people who reacted to an audit-channel message in workspace T_RESEARCH.

**Selection:** channels.team_id == T_RESEARCH

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S4. Workspace IDs and displayed membership facts can identify the requested workspace or identify other roots by a workspace. The complete relation still matters; this is not unrestricted workspace discovery. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

### R212

**Route:** WORKSPACE_MEMBERSHIP → USER → REACTION → MESSAGE → CONVERSATION → CONVERSATION_MEMBERSHIP

**Decision:** retain

**Group:** [S2](#s2)

**Request:** List review-roster people together with their profile-shown workspaces, keeping only entries belonging to people who reacted to a message in an audit channel with at least three members.

**Selection:** count(channel_members for reacted-to message channel) >= 3

**Scope:** Return (user,workspace) membership associations shown on review-roster profiles, including observable admin/owner status if requested. This is a bounded profile-projection report, not a complete enumeration of all workspace memberships. Only the workspace association and owner/admin classification actually shown by users.info for each named roster person is in scope. The request states this profile scope. It does not demand every UserTeam row or a stable primary workspace. Candidate roster IDs are supplied; their profile answers are not. The audit channel list is supplied by ID; messages mean their complete readable histories. The actor can read those channels. Channel-member results are (channel,user) pairs, restricted to the named review roster where stated. No assumption equates conversation membership with workspace membership. Candidate user IDs must be supplied or discovered from known channel-member/message records; users.info does not resolve a real name. Workspace outputs are IDs, not unavailable stored names. All lists/histories are fully paginated.

**API evidence:** conversations.info; methods.py:1727; context_team_id projection methods.py:464; conversations.members; methods.py:2029,2081; operations.py:620; conversations.history; methods.py:1144,1228; operations.py:681; reactions.get; methods.py:2208,2234; users.info; methods.py:2297; selected target membership methods.py:767; role projection methods.py:2389; grounding/slack_coverage/workspace_scope_audit.md; no workspace listing/switch API, methods.py:3170

**Reason:** Retain the scoped witness under group S2. Use the actual owner/admin distinctions on the displayed membership or report the displayed membership pair. This does not credit discovery of every membership or guest/member distinctions. The full route selects the stated root entity; inverse routes and association outputs are not merged. Hidden terminal-field variants remain limitation cases.

## Source snapshot

- [systematic modeling/slack-conceptual-model.md](../../systematic%20modeling/slack-conceptual-model.md) — SHA-256 `d954d5fa1c6d275f249dd4b1b3985975e02a61bb7bc6215be1308aaa168d6d25`
- [systematic modeling/slack-coverage-ledger.md](../../systematic%20modeling/slack-coverage-ledger.md) — SHA-256 `91efc36304aa4a7d998ccd7b41b831728084a70a323e3c36c858dc2e6de07e5e`
- [examples/slack/testsuites/slack_docs/slack_api_full_docs.json](../../examples/slack/testsuites/slack_docs/slack_api_full_docs.json) — SHA-256 `563a4f58dba040b80451c730cac3c3b8fc33c52198b4736911b060c5dd4a4982`
- [backend/src/services/slack/api/methods.py](../../backend/src/services/slack/api/methods.py) — SHA-256 `178895e3cea2ce0db20dc5282730670d198babacf4216349706822bc32a7d673`
- [backend/src/services/slack/database/operations.py](../../backend/src/services/slack/database/operations.py) — SHA-256 `dc1cac9276f0de5dd60f0725aa7e4e24cd5f23d87aeaa746e8e42c31c583a8c7`
- [backend/src/services/slack/database/schema.py](../../backend/src/services/slack/database/schema.py) — SHA-256 `b92bcf2322428cc6a5272be999900aa873c60982b4a1886d3f4be57cc6e70aca`

The builder verifies row completeness, route identity, source hashes, and required evidence fields. It does not certify the semantic judgments or execute the proposed tasks.
