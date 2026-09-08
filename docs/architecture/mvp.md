# MVP Architecture

## Goal

Demonstrate a complete agent authorization lifecycle without implementing payment processing or a centralized global trust authority.

## MVP capabilities

- Agent Identity
- Delegation
- Authorization
- Capability
- Policy
- Verification
- Revocation
- Audit

## First scenario

**Agent Purchase Authorization**

```text
USER
  │
  │ delegates authority
  ▼
AGENT
  │
  │ authorization request
  ▼
TRUST FOUNDATION
  │
  ├── Identify Agent
  ├── Verify Delegation
  ├── Evaluate Capability
  ├── Evaluate Policy
  ├── Check Revocation
  └── Authorization Decision
  │
  ├── ALLOW
  └── DENY / HUMAN APPROVAL
```

An ALLOW decision can then be consumed by Agent-Pay for financial execution.

## Explicit non-goals for MVP

- Payment processing
- Wallet implementation
- Virtual cards
- Settlement
- Global trust network
- Healthcare authorization
- Cloud authorization
- General enterprise IAM replacement

## Implementation shape

The reference implementation should initially use clear logical modules rather than forcing a microservice deployment model. Service boundaries can be introduced later when operational requirements justify them.
