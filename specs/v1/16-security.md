# 16. Security

## Status
Normative — ATF Protocol v1.

Implementations MUST use secure transport and appropriate cryptographic protections for credentials and authority evidence.

The protocol follows least privilege, default deny, fail closed, explicit delegation, revocation, audience/domain binding, replay resistance where applicable, and sensitive-data minimization.

Implementations MUST NOT expose secrets or credentials to agents merely to permit an authorization decision.
