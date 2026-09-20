# 4. Credentials

## Status
Normative — ATF Protocol v1.

Credentials are evidence used to authenticate or establish attributes of a subject.

### Requirements
1. A credential MUST identify its issuer and subject, directly or through a verifiable binding.
2. A verifier MUST validate credential validity, intended audience or trust domain where applicable, and required cryptographic or transport protections.
3. Expired, revoked, malformed, or otherwise unverifiable credentials MUST NOT establish authority.
4. Credential verification MUST be separated from authorization policy evaluation.
5. Implementations MUST minimize disclosure to the information required for the requested decision.
