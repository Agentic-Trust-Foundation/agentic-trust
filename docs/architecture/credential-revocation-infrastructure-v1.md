# Credential and Revocation Infrastructure Profile V1

V1 semantics do not require one universal credential wire format. A production deployment nevertheless needs a concrete verifier.

## Reference components
- issuer trust configuration
- JWKS/key discovery adapter
- signature/algorithm allowlist
- issuer/audience/resource validation
- time validation with bounded clock skew
- revocation/status adapter
- key rotation cache
- audit record of verification result

## Verification result
A verifier returns a structured result:
- VALID
- INVALID
- EXPIRED
- REVOKED
- UNKNOWN

UNKNOWN is fail-closed for security-sensitive authorization.

## Key lifecycle
- publish current and next keys
- overlap during rotation
- reject retired keys after policy window
- cache metadata with bounded lifetime
- emergency revocation procedure

## Privacy
Store only the evidence necessary to prove the decision. Avoid copying unnecessary credential claims into downstream payment systems.

## Boundary
This profile is an implementation pattern, not a V1 universal credential format.
