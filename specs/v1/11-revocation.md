# 11. Revocation

## Status
Normative — ATF Protocol v1.

Revocation invalidates previously issued credentials, delegations, capabilities, consent, or trust evidence before their nominal expiry.

Verifiers MUST check applicable revocation state when the protocol context requires current validity. Revocation state SHOULD provide an issuer, subject/evidence reference, effective time, and reason or status.

If required revocation state cannot be established, the verifier MUST fail closed when freshness is security-critical.
