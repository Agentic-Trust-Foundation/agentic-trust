# Threat Model

## Initial scope

The Foundation protects delegated authority and authorization decisions in an environment containing autonomous and semi-autonomous agents and multiple independent trust domains.

## Primary threats

- Agent impersonation
- Credential theft
- Token replay
- Delegation abuse
- Privilege escalation
- Confused deputy
- Malicious agent
- Compromised agent
- Malicious merchant or resource provider
- Compromised trust provider
- Policy bypass
- Replay of authorization decisions
- Cross-domain trust abuse

## Security goals

1. Prevent unauthorized actions.
2. Prevent privilege escalation through delegation chains.
3. Bind authority to the intended subject, action, resource, and context.
4. Support revocation and expiration of authority.
5. Make security-relevant decisions auditable.
6. Minimize sensitive information disclosed during verification.
7. Fail closed when required authority or evidence cannot be established.

## Architectural controls

- Explicit delegation
- Least privilege
- Policy-driven authorization
- Default deny / fail closed
- Revocation
- Sender-constrained credentials/tokens where appropriate
- Provenance and auditability
- Human approval for operations requiring stronger control
- Domain separation and federation boundaries
