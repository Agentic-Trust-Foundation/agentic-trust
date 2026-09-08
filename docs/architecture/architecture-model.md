# Architecture Model

## Status

Architecture v1 — approved baseline.

## Foundation Model

Agentic Trust Foundation is designed as an open trust and delegated-authority infrastructure for the agentic internet.

The model separates authority from execution and treats identity, delegation, authorization, capability, policy, trust, revocation, and auditability as distinct but connected concerns.

```text
User / Principal
       │
       │ delegates authority
       ▼
     Agent
       │
       │ requests action / intent
       ▼
Trust & Authorization Layer
       │
       ├── Identity
       ├── Credentials
       ├── Delegation
       ├── Capability
       ├── Policy
       ├── Trust
       ├── Revocation
       └── Verification
       │
       ▼
Authorization Decision
       │
       ├── ALLOW
       ├── DENY
       └── HUMAN APPROVAL
       │
       ▼
Execution Service
       │
       ▼
Real World
```

## Protocol-First Architecture

The Foundation is not a protocol-only project and is not an implementation-only product.

The target model is:

> Protocol-first, implementation-backed, service-optional.

```text
                AGENTIC TRUST FOUNDATION
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
          PROTOCOL     REFERENCE     CONFORMANCE
                        IMPLEMENTATION   / TESTING
              │            │            │
              └────────────┼────────────┘
                           │
                           ▼
                  Optional Services
```

The open protocol is the primary artifact. A reference implementation demonstrates the protocol. A conformance suite verifies interoperability. Hosted services may exist later but are optional and must not become a mandatory central trust authority.

## Decentralized Trust Model

The Foundation must not require the entire ecosystem to rely on one centralized trust authority.

```text
                Trust Protocol
                      │
          ┌───────────┼───────────┐
          ▼           ▼           ▼
      Authority A Authority B Authority C
```

Multiple trust domains and providers may participate through interoperable protocols and federation mechanisms.

## Agent-Pay Relationship

Agent-Pay is a separate financial execution layer that consumes relevant Foundation decisions.

```text
Agent
  │
  ▼
Trust Protocol
  │
  ▼
Verify Identity / Delegation / Authorization
  │
  ▼
Agent-Pay
  │
  ▼
Spending Policy / Risk / Approval / Payment
```

The Foundation does not become a payment processor, wallet provider, or financial ledger merely because Agent-Pay consumes its authority decisions.

## Payment Intent

Payment Intent is a core operational concept of Agent-Pay. The agent expresses what it intends to purchase or pay for; Agent-Pay decides whether and how to execute it.

Payment instruments are intentionally abstracted from the agent so that Wallets, Virtual Cards, and future instruments can coexist.

## Core Rule

> Agent requests; control layers decide; execution infrastructure executes; financial systems record financial truth.
