# Master Project Map

## Status

Architecture v1 — approved baseline.

## Overview

Agentic Trust Foundation and Agent-Pay are separate but interoperable layers within the broader Agentic Internet.

```text
                         AGENTIC INTERNET
                                │
                                ▼
                              AGENTS
                                │
                                ▼
                         AGENT COMMERCE
                                │
                   ┌────────────┴────────────┐
                   │                         │
                   ▼                         ▼
        AGENTIC TRUST FOUNDATION        AGENT-PAY
                   │                         │
                   │                         │
                   └────────────┬────────────┘
                                │
                                ▼
                           REAL WORLD
```

## Agentic Commerce

Agentic Commerce is the interaction domain where agents operate against real-world services and resources. It is currently a conceptual ecosystem/domain, not a separate software product or repository.

Examples include:

- Purchase
- Booking
- Healthcare
- Enterprise APIs
- Cloud infrastructure
- Agent-to-agent interaction

A use case may consume Agentic Trust Foundation, Agent-Pay, both, or neither.

## Agentic Trust Foundation

Authority and trust infrastructure for the agentic internet.

Core question:

> Is this Agent authorized to perform this action, who authorized it, and is that authority valid?

Primary concerns:

- User identity
- Agent identity
- Organization identity
- Authentication
- Authorization
- Delegation
- Capability
- Trust
- Verification
- Reputation
- Trust and authority policy
- Consent
- Revocation
- Provenance
- Accountability
- Auditability
- Human approval

The Foundation does not own payment execution, wallets, banking accounts, settlement, refunds, or payment-specific financial risk.

## Agent-Pay

Financial execution and spending-control infrastructure for agentic commerce.

Core question:

> Given that this Agent is authorized, can it spend this money for this transaction, under which conditions, and how should the payment be executed?

Primary concerns:

- Funding
- Wallets
- Payment instruments
- Virtual cards
- Payment Intent
- Spending Policy
- Risk
- Approval
- Payment routing
- Payment processing
- Transactions
- Settlement
- Refunds
- Ledger
- Merchant integration

Agent-Pay consumes relevant identity, delegation, authorization, and trust outputs from the Foundation.

## Fundamental Relationship

```text
Agent
  │
  │ requests action / intent
  ▼
Agentic Trust Foundation
  │
  │ authority / authorization decision
  ▼
Agent-Pay or another execution service
  │
  │ execution
  ▼
Real World
```

The guiding rule is:

> Agent requests; control layers decide; execution infrastructure executes; financial systems record financial truth.
