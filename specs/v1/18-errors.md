# 18. Errors

## Status
Normative — ATF Protocol v1.

Protocol errors MUST be machine-readable and MUST distinguish at least invalid input, authentication failure, authorization denial, expired/revoked evidence, unavailable verification state, and unsupported protocol version.

Security-sensitive errors SHOULD avoid revealing information that enables privilege discovery or credential enumeration.

An implementation MUST NOT convert an indeterminate security decision into `ALLOW`.
