# Agentic Trust Foundation

An open interoperability layer for trust, delegated authority, policy, provenance, and accountability in the agentic internet.

## Purpose

Agentic Trust Foundation defines open protocols and reference infrastructure for establishing and evaluating authority in interactions involving autonomous and semi-autonomous agents.

The Foundation separates **authority** from **execution** and is designed to operate across independent trust domains rather than requiring a single centralized trust authority.

## Architecture

```text
AGENTIC INTERNET
       │
     AGENTS
       │
AGENT COMMERCE
   │         │
   ▼         ▼
TRUST     AGENT-PAY
FOUNDATION
   │         │
   └────┬────┘
        ▼
    REAL WORLD
```

### Agentic Trust Foundation

Provides identity, credentials, delegation, authorization, capabilities, trust, policy, consent, revocation, provenance, accountability, auditability, and human approval mechanisms.

### Agent-Pay

A separate financial execution layer. It consumes relevant trust and authorization decisions but owns wallets, payment instruments, spending policy, risk, payment execution, settlement, refunds, and financial ledgers.

## Design Position

> **Protocol-first, implementation-backed, service-optional.**

The Foundation is not intended to become a mandatory centralized trust provider.

## Architecture Principles

- Protocol First
- Open Interoperability
- Decentralized Trust
- Explicit Delegation
- Least Privilege
- Separation of Authority and Execution
- Policy-Driven Architecture
- Default Deny / Fail Closed
- Revocability
- User Sovereignty
- Auditability and Provenance
- Privacy and Data Minimization
- Human Control and Override
- Extensibility
- Vendor Neutrality
- Conformance over Claims
- Versioned Evolution
- No Hidden Authority Escalation

## Repository Structure

```text
agentic-trust/
├── docs/
│   ├── vision/
│   ├── architecture/
│   ├── protocol/
│   ├── security/
│   └── governance/
├── specs/
│   └── v1/
├── reference/
│   └── implementation/
├── conformance/
├── schemas/
├── examples/
├── test-vectors/
└── tools/
```

## MVP

The first protocol scope focuses on:

- Agent Identity
- Delegation
- Authorization
- Capability
- Policy
- Verification
- Revocation
- Audit

The first reference scenario is **Agent Purchase Authorization**. Payment execution remains in Agent-Pay.

## Status

Architecture v1 is established. Protocol specification, conformance requirements, and reference implementation are the next implementation-facing layers.
