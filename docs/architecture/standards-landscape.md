# Standards Landscape

## Status

Architecture research baseline — September 2026.

## Position

Agentic Trust Foundation should compose existing open standards wherever they fit instead of recreating identity, credential, authorization, federation, or agent-communication mechanisms unnecessarily.

| Need | Direction |
|---|---|
| Identity | Identity abstraction; DID-compatible |
| Credentials | W3C Verifiable Credentials 2.0 where appropriate |
| Credential issuance | OpenID4VCI where applicable |
| Credential presentation | OpenID4VP where applicable |
| Authorization | OAuth family |
| Fine-grained authorization | OAuth Rich Authorization Requests |
| Sender-constrained tokens | DPoP for high-risk operations |
| Protected resource discovery | OAuth Protected Resource Metadata |
| Federation | OpenID Federation |
| Agent-to-agent communication | A2A |
| Agent-to-tool/resource interaction | MCP |
| Internal workload identity | SPIFFE/SPIRE |

## Important Boundary

These standards are building blocks, not replacements for the Foundation's agent-centric trust and delegation model.

The Foundation's value is the composition of:

```text
Identity
   +
Credentials
   +
Delegation
   +
Authorization
   +
Capability
   +
Policy
   +
Trust
   +
Revocation
   +
Provenance
   +
Audit
```

## Compatibility Position

The Foundation should be **compatible with** relevant standards without making every standard mandatory for every deployment. Protocol profiles can specify where a standard is required, optional, or replaceable.
