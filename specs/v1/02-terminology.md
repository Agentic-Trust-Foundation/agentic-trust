# 2. Terminology

## Principal

An entity that can hold authority and delegate authority to an agent. A principal may be a user or another authorized entity.

## Agent

A software entity acting on behalf of a principal or another authorized entity.

## Organization

An organizational entity participating in the trust and authorization ecosystem.

## Delegation

An explicit grant of authority from one entity to another subject, constrained by scope, action, resource, context, and validity.

## Capability

A bounded statement of what an agent is permitted to do.

## Authorization Request

A structured request to perform an action against a resource under specified context and constraints.

## Authorization Decision

The result of evaluating identity, delegation, capability, policy, trust, revocation, and request context.

Allowed outcomes are:

- `ALLOW`
- `DENY`
- `REQUIRE_HUMAN`

## Trust

Evidence and policy used to determine whether an entity or relationship is sufficiently trusted for a particular context. Trust is contextual and is not required to be represented as a universal numeric score.

## Policy

Explicit rules used to evaluate authority, trust, or authorization.

## Revocation

An explicit mechanism for invalidating previously issued authority, credentials, capabilities, or trust relationships.

## Provenance

Information describing the origin and authority chain associated with an artifact, decision, or action.

## Audit Record

A traceable record of security- or authority-relevant events and decisions.
