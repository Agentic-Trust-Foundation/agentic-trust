# 6. Authorization

## Status
Normative — ATF Protocol v1.

Authorization determines whether a subject may perform a requested action against a resource in a stated context.

### Request
An authorization request MUST identify the subject, action, resource or resource class, and decision context required by policy.

### Decision
The protocol defines exactly three decision outcomes:
- `ALLOW`
- `DENY`
- `REQUIRE_HUMAN`

A verifier MUST default to `DENY` when required identity, delegation, capability, policy, revocation, or evidence cannot be established.

Authentication MUST NOT be treated as authorization. Downstream execution systems MUST NOT expand an upstream ATF authorization decision.

A decision SHOULD include a stable decision identifier, policy/version reference, evidence references, validity interval, and reason code sufficient for later audit without unnecessarily exposing sensitive data.
