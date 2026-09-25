# Why Agentic Trust Foundation Exists

## The short version

Agents are moving from generating information to **taking actions**.

An action can have real consequences:

~~~text
User
  |
  v
Agent
  |
  +--> read an API
  +--> change infrastructure
  +--> book a service
  +--> purchase something
  +--> pay
  +--> delegate to another agent
  |
  v
Real-world consequence
~~~

The technical ability to perform an action is not the same as the authority to perform it.

ATF exists to make delegated authority explicit, bounded, verifiable, revocable, and auditable.

## The questions ATF is designed to answer

For an agent action, systems need a common way to reason about:

1. Who is the agent?
2. Who is the user, organization, or principal behind the authority?
3. What authority was delegated?
4. Which resource or capability is covered?
5. What action is permitted?
6. What limits apply?
7. How long is the delegation valid?
8. May the agent delegate further?
9. Which policies or approvals apply?
10. What evidence proves the decision?
11. Can the authority be revoked?
12. How is the action recorded and later audited?
13. Who remains accountable when execution crosses systems or agents?

## Why payment is only one important use case

Payment makes delegated authority especially visible because money introduces explicit limits, approvals, credentials, fraud controls, transaction state, settlement, and reconciliation.

That is why Agent-Pay builds on ATF rather than replacing it.

~~~text
ATF
identity
delegation
authorization
trust
consent
revocation
provenance
accountability
        |
        v
Agent-Pay
financial policy
budget
approval
instrument
payment
ledger
settlement
reconciliation
~~~

The same authority model can also support API access, booking, enterprise services, cloud operations, healthcare workflows, and agent-to-agent delegation.

## Design position

ATF is intentionally a **layer**, not a new internet.

It should coexist with existing identity systems, authorization mechanisms, agent protocols, API protocols, payment rails, and deployment infrastructure.

The goal is interoperability around delegated authority—not forcing every participant to adopt one vendor, one credential format, one hosted service, or one agent runtime.

## Vision versus evidence

**Vision** describes what the architecture is intended to enable.

**Evidence** describes what is actually implemented and independently verified.

This distinction is a core project rule. A protocol contract, reference implementation, CI pass, simulator, or documentation page must not be presented as proof of an external production deployment.

## The intended action chain

~~~text
User
  -> Agent
  -> Delegate bounded authority
  -> Access service/API
  -> Perform action
  -> Optionally delegate further
  -> Pay / transact when authorized
  -> Record evidence
  -> Revoke / refund / reconcile when required
~~~

ATF is the trust and authority layer running through that chain.
