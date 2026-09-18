# Agent-Pay Integration Boundary

Agentic Trust Foundation (ATF) is the upstream authority layer. Agent-Pay is the
financial control and execution layer.

## ATF provides

ATF establishes and communicates identity, delegation, authorization, capability,
trust, consent, provenance, and revocation. For financial execution, ATF provides
a normalized authority context or an adapter-level equivalent.

## Agent-Pay consumes

Agent-Pay validates the normalized authority context, applies financial spending
policy, controls budgets and approvals, executes payment operations, records
transactions and ledger effects, and reconciles external settlement.

## Boundary invariants

1. Agent-Pay must not mint general authorization.
2. Authentication alone is not financial authority.
3. An Agent-Pay policy decision cannot create upstream authority.
4. A financial approval cannot expand the upstream authority bound.
5. The evidence reference and version used for a payment decision must remain reconstructable.
6. Settlement is distinct from payment execution.

V1 deliberately does not freeze a universal ATF token or signature format. Protocol
adapters may verify their own credentials and construct the normalized contract.

The shared machine-readable contract is published in
conformance/v1/agent-pay-contract-vectors.yaml.
