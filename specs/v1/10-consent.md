# 10. Consent

## Status
Normative — ATF Protocol v1.

Consent records a principal's approval for a specified purpose, scope, and validity period.

Consent MUST NOT silently expand authority beyond the delegations, capabilities, policies, or resource constraints applicable to the subject.

Where policy requires explicit human consent, absence, expiration, withdrawal, or invalidation of consent MUST result in `DENY` or `REQUIRE_HUMAN` as defined by policy.
