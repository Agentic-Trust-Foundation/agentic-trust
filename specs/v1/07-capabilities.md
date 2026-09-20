# 7. Capabilities

## Status
Normative — ATF Protocol v1.

A capability is a bounded statement of permitted operations.

Capabilities MUST be scoped to the subject and constrain at least the permitted action. Where relevant they MUST also constrain resources, conditions, amount/quantity, audience, time, or delegation depth.

Capability evaluation MUST be monotonic: combining capabilities MUST NOT create authority that is absent from all applicable authority sources.

A capability MUST NOT override revocation, expiration, delegation constraints, or an explicit deny policy.
