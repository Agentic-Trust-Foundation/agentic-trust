# 5. Delegation

## Status
Normative — ATF Protocol v1.

Delegation transfers a bounded authority from a delegating principal to a subject.

A delegation MUST define, directly or by referenced policy:
- delegator
- delegate/subject
- scope or capabilities
- resource constraints where applicable
- validity interval
- delegation constraints
- issuer/evidence provenance

Delegation MUST NOT grant authority broader than the delegator possesses. A verifier MUST evaluate every relevant link in a delegation chain and MUST reject an invalid, expired, or revoked link.

Delegation is authority, not authentication. A valid identity without a valid delegation does not authorize an action.
