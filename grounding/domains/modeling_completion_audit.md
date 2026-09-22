# Domain modeling completion audit

This completes the previously under-documented forward and reverse checks for
Box, Calendar and Linear against the existing Slack extraction standard. It does
not replace or relax the [protocol](../protocols/conceptual_meta_model.md).

The four Slack artifacts remain the reference: the protocol, contextualization,
conceptual model and source ledger. Source enumeration alone was insufficient;
the earlier broad reverse-audit summaries overstated the evidence recorded.

## Completed work

| Existing requirement | Evidence now recorded |
|---|---|
| Contextualize source authority and boundaries | Each domain's contextualization identifies metadata, dispatch, helpers/serializers and supporting docs. Seeder metadata and relevant migration definitions were checked; platform state remains out of domain. |
| Source → model, including domain-bearing API fields | Database rows explicitly list identities, FK roles and remaining values. Every registered operation links to reviewed field mappings that distinguish stored, renamed, derived, fixed, deferred and unsupported information. Shared evidence is recorded once. |
| Model → source | Domain-specific reverse-check rows cover every entity/value fold, identity/attribute group, relationship/cardinality, diagram, qualification, derived representation and classification group, identifying source witnesses and concrete qualifications. |
| Protect against bloat | Retained the existing folds/contractions; did not turn public declarations, API wrappers, external source metadata or computed projections into new entities. Independently identified/attributed links remain distinct. |
| Validate risky mappings | Offline checks exercise real serializers and the mounted GraphQL schema; metadata checks cover columns, FK targets/cardinalities and association endpoints. Diagram notation now follows identity participation as in Slack. |

The detailed records are part of the existing ledgers:

- [Box](box/model_source_ledger.md#completion-audit-explicit-evidence-mappings)
- [Calendar](calendar/model_source_ledger.md#completion-audit-explicit-evidence-mappings)
- [Linear](linear/model_source_ledger.md#completion-audit-explicit-evidence-mappings)

`model_audit.json` is the manual annotation source for those sections. Linear's
[field accounting](linear/api_field_accounting.json) additionally assigns a
disposition to every GraphQL field declared on an ORM-mapped type. It records
declared-only fields and Python-attribute collisions explicitly; this is not an
expansion of the conceptual attribute inventory.

## Findings made explicit in this pass

- **Diagram notation:** the renderer incorrectly used solid identifying links
  everywhere. It now distinguishes key participation. No nodes, roles or
  connectivity changed.
- **Calendar API identities:** list-entry `id` is `calendar_id`; attendee `id` is
  `profile_id`; setting `id` is `setting_id`. These do not replace the records'
  storage primary keys. All corresponding fields were already preserved.
- **Defaults and views:** Calendar fallback notifications/reminders/colors and
  virtual settings, Box fixed Favorites labels, and selected-version versus
  cached-version metadata now have explicit dispositions. They do not establish
  extra persisted records or synchronize inconsistent values.
- **Linear metadata collision:** default resolution of `Attachment.metadata`
  returns inherited SQLAlchemy `MetaData`, not the stored `metadata_` value. The
  actual GraphQL schema reproduced the JSON-serialization failure offline.
  OrganizationInvite has the same alias collision; IssueSuggestion also has a
  `metadata` collision but no stored `metadata_` field.
- **Linear payload mismatch:** `issueSubscribe` returns a raw Issue where the
  schema expects IssuePayload. An offline check confirms the missing required
  `success` field. Its documented current-user fallback is also absent. These
  are interface defects, not grounds for removing the stored subscription role.
- **Other source/documentation differences:** `searchProjects` ignores teamId
  and includeComments; a Box comment handler docstring says replies expose the
  file target, while the implementation preserves and returns the parent-comment
  target. The implementation supports the already-modeled reply relationship.

## Count and change boundary

No entity, stored attribute, relationship, or published count was changed.
The [baseline](../modeling/audit_baseline.json) freezes model and route-count
file hashes and inventories. The [validation result](../modeling/audit_validation.json)
confirms those files stayed byte-for-byte unchanged while the documentation and
accounting were completed. No count-changing correction was identified for adoption.

The structural route definition is unchanged across all four domains. This audit
does not claim that Slack's historical topological capability screen and the new
domains' finer direct-read screens constitute identical capability experiments.
Their existing qualifications remain in the [comparison](route_comparison.md).
Nor does it claim that the new domains have received Slack's later ordinary-request
inclusion review. Neither difference is concealed by declaring extraction complete.

These are source-based models with targeted offline execution checks, not a
certification of every deployed schema, API operation or concatenated route. No
service was modified, no application database was queried, and no paid model calls
were made. Reproduction commands are in the [tool guide](../modeling/README.md).
