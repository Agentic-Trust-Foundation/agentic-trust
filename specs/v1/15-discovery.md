# 15. Discovery

## Status
Normative — ATF Protocol v1.

Discovery allows an agent or verifier to locate protocol metadata, identity/trust-domain information, capabilities, and supported authorization mechanisms.

Discovery metadata MUST be treated as untrusted input until independently verified. Discovery MUST NOT itself grant authority.

Implementations SHOULD advertise protocol version, supported verification mechanisms, trust domain, and endpoint metadata required for interoperability.
