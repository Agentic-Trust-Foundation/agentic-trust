# Project Boundaries

## Status

Architecture v1 — approved baseline.

## Purpose

This document defines the responsibility boundaries between Agentic Trust Foundation, Agent-Pay, Agent Commerce, and external systems.

## Agentic Trust Foundation

### Owns

- Identity and identity verification
- Authentication
- Authorization
- Delegation
- Capability
- Trust relationships and trust evidence
- Reputation
- Trust and authority policy
- Consent
- Revocation
- Provenance
- Accountability
- Auditability
- Human approval mechanisms related to authority
- Interoperability protocols and conformance

### Does not own

- Wallet balances
- Bank accounts
- Virtual cards
- Payment processing
- Payment routing
- Settlement
- Refund processing
- Financial ledgers
- Payment-specific fraud/risk systems
- Healthcare IAM
- Cloud IAM
- Enterprise IAM

## Agent-Pay

### Owns

- Funding
- Wallets
- Payment instruments
- Virtual cards
- Payment Intent
- Spending Policy
- Payment risk
- Payment approval
- Payment routing
- Payment processing
- Transaction processing
- Settlement
- Refunds
- Financial ledger
- Merchant payment integration

### Does not own

- General-purpose Agent identity
- General Agent reputation/trust network
- General-purpose delegation protocol
- General-purpose authorization
- Healthcare authorization
- Cloud authorization
- Enterprise IAM

## Agent Commerce

Agent Commerce is currently a conceptual domain rather than a third product/repository.

It represents the interactions between agents and real-world services/resources, including:

- Purchases
- Bookings
- Healthcare
- Enterprise APIs
- Cloud infrastructure
- Agent-to-agent interactions

It may use Agentic Trust Foundation, Agent-Pay, both, or neither depending on the use case.

## Core Boundary Rule

Trust and financial execution are deliberately separated:

```text
Trust Foundation:
    Can this Agent perform this action?

Agent-Pay:
    Can this Agent spend this money for this transaction, and how should it be executed?
```

Trust Policy and Spending Policy are separate concerns.

## Merchant Boundary

Merchants and other real-world service providers are external parties. They are not part of the Trust Foundation or Agent-Pay core ownership boundary.

## Agent Boundary

Agents request actions or intents. They do not receive unrestricted direct access to underlying financial or protected resources.

The control layers evaluate authority, policy, risk, and approval before execution.
