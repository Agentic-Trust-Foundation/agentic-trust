# Architecture Principles

## Status

Architecture Principles v1 — approved baseline.

These principles are non-negotiable architectural constraints for the Foundation unless a future version explicitly supersedes them.

## Principles

### P1 — Protocol First

The protocol must remain independent from any particular implementation. Implementations realize the protocol; they do not define the protocol by implementation-specific behavior.

### P2 — Open Interoperability

The Foundation exists to enable interoperability between independent agents, trust domains, organizations, merchants, services, and implementations. Vendor lock-in must not be a design requirement.

### P3 — Decentralized Trust

The Foundation must not become a single mandatory global trust authority. Multiple trust providers, authorities, and trust domains must be able to participate.

### P4 — Explicit Delegation

Agent authority must be explicitly delegated. An agent must not receive unlimited authority merely because it represents or belongs to a principal.

### P5 — Least Privilege

An agent receives only the minimum authority required for the intended purpose, scope, resource, context, and duration.

### P6 — Separation of Authority and Execution

The component that establishes or evaluates authority does not inherently own execution. Trust decisions and domain-specific execution remain separate concerns.

### P7 — Policy-Driven Architecture

Authorization and trust decisions must be driven by explicit, inspectable policy rather than hidden or hard-coded assumptions.

### P8 — Default Deny / Fail Closed

When authority, policy, credential status, or required evidence cannot be established safely, protected operations default to denial or an explicitly defined human-approval path.

### P9 — Revocability

Delegations, credentials, capabilities, trust relationships, and other authority-bearing artifacts must have a defined mechanism for invalidation or revocation where applicable.

### P10 — User Sovereignty

The principal retains control over delegated authority. Agents must not silently expand, persist, or transfer authority beyond the permissions explicitly granted to them.

### P11 — Auditability and Provenance

Security- and authority-relevant decisions must be traceable to their identities, credentials, delegation chain, policy, request, decision, execution, and outcome where applicable.

### P12 — Privacy and Data Minimization

Trust and authorization should be established with the minimum information necessary. A verifier should not receive unrelated personal or organizational data merely because it could be available.

### P13 — Human Control and Override

The architecture must support autonomous decisions as well as notification, user confirmation, and explicit human approval for operations that require additional control.

### P14 — Extensibility

The protocol must be designed for an evolving agentic internet and must not be narrowly coupled to one commerce scenario. New domains, actions, resources, credentials, and execution systems must be incorporable without redesigning the foundation.

### P15 — Vendor Neutrality

The protocol must remain independent of any particular AI model, agent vendor, cloud provider, identity provider, payment provider, or infrastructure vendor.

### P16 — Conformance over Claims

Protocol compatibility must be demonstrable through conformance requirements and testable behavior rather than vendor claims alone.

### P17 — Versioned Evolution

Protocol changes must be versioned and designed to support controlled evolution, interoperability, and compatibility across ecosystem participants.

### P18 — No Hidden Authority Escalation

Delegation chains must not silently create privilege escalation. A subject may delegate only authority that it is itself permitted to delegate, subject to applicable constraints.

## Architectural Consequence

These principles imply that the Foundation should be built as an open protocol with a reference implementation and conformance suite, while keeping hosted services optional.

They also imply a strict separation between:

- Trust policy and spending policy
- Authority and execution
- Agent identity and payment instruments
- General trust infrastructure and domain-specific IAM
- Foundation protocol and individual vendors or service providers
