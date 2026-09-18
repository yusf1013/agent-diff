The private.selector object has root_table, scope, focal, auxiliary.
scope is a conjunction of root-field filters; [] covers every root row. Never
restrict scope to the intended answers unless the request supplies that scope.
focal and each auxiliary are queries with path (table names), joins (one per
step), and filters (conjoined node-indexed real-field comparisons). A join is
the foreign-key name table.field, usable in either direction; it must connect
the adjacent tables. Each joined tuple preserves the identities along the path.
Operations: eq, ne, in, not_in, contains_ci, lt, le, gt, ge. Values use seed types;
in/not_in require a list. Filters have {node:0,field:'message_text',op:'contains_ci',value:'rollout'};
scope filters omit node. Every query starts at root_table. Without count it
requires at least one complete matching tuple. Optional count:{node:N,op:'eq',value:3}
counts DISTINCT row handles at N in complete matching tuples, not join rows.
Count comparisons also allow ne,lt,le,gt,ge; no tuples means zero. For a direct
member count use path ['channels','channel_members'], join
['channel_members.channel_id'], count node 1. No arbitrary Python, SQL, aliases,
or invented fields. Scalar-primary-key handles are their string IDs. Composite
handles are objects of exactly the actual PK fields, e.g.
{message_id:'1712345678.000001',user_id:'U1',reaction_type:'thumbsup'}. Lists contain distinct handles.
API compatibility: every new messages.message_id must be a timestamp-like numeric
string whose float conversion is finite (e.g. '1712345678.000001'); Slack history
parses message_id as a number. Cards, reactions, parents, and handles use that
actual ID.
Example:
{"root_table":"messages","scope":[],"focal":{
 "path":["messages","message_reactions","users","channel_members","channels"],
 "joins":["message_reactions.message_id","message_reactions.user_id","channel_members.user_id","channel_members.channel_id"],
 "filters":[{"node":4,"field":"channel_name","op":"eq","value":"security"}]},
 "auxiliary":[{"path":["messages"],"joins":[],"filters":[
 {"node":0,"field":"message_text","op":"contains_ci","value":"rollout"}]}]}
