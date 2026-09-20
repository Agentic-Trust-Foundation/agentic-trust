# Agent-Pay Integration Boundary

**Status:** V1 integration contract guidance. This document defines the responsibility boundary and the minimum normalized authority context expected at the integration seam. It does not freeze a universal credential, token, signature, or wire format.

## Responsibility split

ATF is the upstream authority layer. It answers whether an identified agent is acting under a valid, bounded, delegated authority in a given context.

Agent-Pay is the financial control and execution layer. It answers whether a proposed financial operation satisfies its own financial controls and, when permitted, coordinates execution and records financial state.

### ATF owns

- Agent and delegating-principal identity assertions, including their issuer and trust context.
- Delegation chain and the authority granted by each relevant delegator.
- General authorization and capability scope, including resource/action restrictions.
- Authority validity, expiry, revocation, and policy conditions that belong to the upstream trust domain.
- Evidence provenance and the ability to identify the exact decision/evidence version relied upon.

### Agent-Pay owns

- Account and financial-instrument binding, funding eligibility, and payment-rail constraints.
- Financial spending policy, policy version, budgets, reservations, and approval workflow.
- Payment-intent validation, payment authorization records, provider operations, idempotency, and execution lifecycle.
- Ledger postings, settlement/reconciliation, refunds/reversals, and financial audit records.

## Normalized authority context

An ATF adapter (or equivalent trusted verifier) must provide Agent-Pay a normalized context containing, at minimum, the following semantic claims. A deployment may use different field names or encodings, but must preserve these meanings:

| Claim | Required meaning |
|---|---|
| `subject_agent` | Stable identifier of the agent requesting the operation. |
| `delegating_principal` | Principal whose authority ultimately permits the agent to act; preserve relevant delegation-chain references. |
| `issuer` / `trust_domain` | Authority that issued the evidence and the trust domain under which it was verified. |
| `decision` | Explicit allow/deny result for the requested action; missing or indeterminate means deny. |
| `action` | Explicit permitted action, such as initiating a payment, not a broad authenticated-session claim. |
| `resource` | Explicit account, beneficiary, merchant, or payment-intent scope as applicable. |
| `constraints` | Applicable limits, including amount/currency, purpose, time window, and any required conditions. Unspecified limits must not be inferred as unlimited unless the upstream contract explicitly says so. |
| `issued_at` / `expires_at` | Decision/evidence validity interval, with clock-skew handling defined by the verifier. |
| `revocation_status` | Whether the relevant authority remains valid at decision time; inability to establish required status fails closed. |
| `evidence_ref` / `evidence_version` | Stable, non-secret reference and version/digest sufficient to reconstruct what was relied upon. |

This is a semantic checklist, not a finalized JSON schema. Exact requiredness and canonical serialization must be frozen alongside the ATF V1 schema before claiming cross-implementation wire interoperability.

## Decision sequence

1. Authenticate the caller and bind the authenticated principal to the claimed agent identity. Authentication alone grants no financial authority.
2. Verify the upstream authority evidence, delegation chain, validity interval, revocation state, requested action, resource, and constraints.
3. If any required claim is absent, ambiguous, expired, revoked, unverifiable, or outside scope, deny before financial execution.
4. Evaluate Agent-Pay financial policy independently against the exact payment intent and its policy version.
5. Enforce the intersection of upstream authority and Agent-Pay controls. The effective permission is never broader than either boundary.
6. Apply budget reservation and required human approval. Approval may satisfy an Agent-Pay condition but cannot expand ATF authority.
7. Persist the decision inputs and evidence reference/version before or atomically with the financial state transition, according to the implementation's transaction model.
8. Execute through the payment-provider boundary with idempotency and explicit handling of unknown external outcomes. Record settlement as a separate assertion/event from execution success.

## Boundary invariants

1. Agent-Pay must not mint, infer, or upgrade general authorization.
2. Authentication is not financial authority.
3. An Agent-Pay policy decision cannot create upstream authority.
4. A financial approval cannot expand the upstream authority bound.
5. Effective scope is the intersection of upstream authority, payment-intent scope, account/instrument constraints, and Agent-Pay policy.
6. Missing, invalid, expired, revoked, or indeterminate required authority evidence fails closed.
7. Evidence reference, issuer/trust domain, version, and decision time used for a payment decision must remain reconstructable without storing unnecessary secrets.
8. A retry must not silently substitute a different authority decision or widen the original intent; revalidation rules must be explicit.
9. Payment execution, provider confirmation, and settlement are distinct states and must not be conflated.
10. Agent-Pay credentials or provider credentials must never be exposed to the agent merely because ATF authorized an action.

## Failure semantics

- **Deny:** explicit upstream denial, scope mismatch, invalid/expired/revoked evidence, or failed financial policy.
- **Indeterminate:** verifier cannot establish a required fact. Treat as deny for execution; retain a diagnostic reason without leaking sensitive evidence.
- **Approval required:** only when upstream authority is valid and the remaining unmet condition is an Agent-Pay approval requirement. Approval cannot repair invalid upstream authority.
- **Unknown external outcome:** provider call outcome cannot be determined. Do not report success or blindly issue a new non-idempotent operation; reconcile using provider operation identity and idempotency semantics.

## V1 interoperability boundary

V1 deliberately does not freeze a universal ATF token or signature format. Protocol adapters may verify credentials and construct this normalized contract. Before claiming interoperable conformance, implementations must agree on canonical schema, required/optional claims, identifier semantics, amount/currency representation, timestamps, revocation freshness, error codes, and evidence-reference retention.

The shared machine-readable boundary vectors are published in [`conformance/v1/agent-pay-contract-vectors.yaml`](../../conformance/v1/agent-pay-contract-vectors.yaml). These vectors currently express core invariants; they are not a substitute for the full schema and adversarial test suite.