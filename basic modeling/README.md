# Conceptual domain models for Agent-Diff

These documents describe the four requested domains: Slack, Linear, Box, and
Calendar. GitHub is excluded. They provide the conceptual foundation for later
agentic testing: the objects an agent refers to, their identities, their
relationships, and the states that distinguish otherwise similar situations.

## Models

| Domain | Central subject | Document |
| --- | --- | --- |
| Slack | Workspace conversations and participation | [Slack](slack.md) |
| Linear | Issues, work organization, and planning | [Linear](linear.md) |
| Box | Hierarchical content, versions, and file collaboration | [Box](box.md) |
| Calendar | Calendars, scheduled events, and participation | [Calendar](calendar.md) |

## Scope and method

This is a conceptual model of **the domains represented in this repository**,
based on the checked-out service schemas and selected supporting implementation
files. It is not a claim of complete parity with the live products or a
reconstruction of the paper's formal model. No specific seed is assumed to
contain every concept described here.

Each document contains:

1. Scope and domain vocabulary.
2. A concept dictionary with relevant attributes and identities.
3. A relationship diagram and explicit cardinalities.
4. Value concepts and state dimensions.
5. Structural constraints and important semantic distinctions.
6. Supporting concepts, representation limitations, and source references.

The conceptual model describes **what exists**. Action preconditions, permission
decisions, state transitions, recovery procedures, test scenarios, coverage
matrices, and executable success assertions belong in the subsequent behavior
and testing models. Roles and access settings appear here as domain data; their
enforcement is not specified here.

## Reading conventions

- **Entity:** something with an identity that persists while its attributes change.
- **Association:** a relationship that may have its own attributes, such as a
  membership, attendance, or assignment.
- **Value concept:** descriptive data without an independent domain identity,
  such as a time interval, reaction name, or shared-link configuration.
- **Derived concept:** a useful interpretation of other objects, such as a
  thread, ancestry path, or recurring occurrence. It need not have its own row.
- **Core / supporting:** a reading hierarchy, not a claim about benchmark
  coverage or endpoint availability. Supporting concepts remain in scope where
  represented; technical infrastructure is identified separately.

Cardinalities use `1`, `0..1`, and `0..*` for exactly one, optional one, and any
number. In Mermaid, `||`, `o|`, and `o{` express those quantities. Diagrams show
selected relationships; tables explain additional relationships and qualifications.
Cardinalities express conceptual structure; any stronger assumption than the
repository guarantees is identified explicitly.

Structural constraints describe a valid arrangement of concepts. Their presence
in these documents does not imply that every constraint is enforced by the
database or API. Schema observations and proposed conceptual interpretations
are distinguished in each model's limitations section.

## Shared boundaries

The acting user is a role occupied by a domain user. The Agent-Diff API-key owner,
environment, template, run, and evaluation result belong to the platform domain;
they are not Slack, Linear, Box, or Calendar business entities.

Identities are local to a service and environment. A Slack user and a Calendar
user with the same email are not automatically one linked entity. Likewise,
attachments and external URLs do not establish cross-service relationships.

Names, titles, paths, dates, and message text help describe an entity but generally
do not replace its identity. The models preserve distinctions especially relevant
to an agent resolving a natural-language reference: a message versus its thread,
an issue versus its project, a file versus its version, and a recurring series
versus one occurrence.
