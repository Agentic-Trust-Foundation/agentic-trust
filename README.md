# Agentic Trust Foundation

An open interoperability layer for trust, delegated authority, policy, provenance, and accountability in the agentic internet.

## V1 Status

**ATF Protocol V1 is FINAL and frozen as an open protocol + schemas + conformance suite + reference implementation.**

The V1 baseline is intentionally protocol-first, implementation-backed, and service-optional. ATF is not a centralized global trust authority, mandatory SaaS service, or single credential/token provider.

**Project memory and complete roadmap:** `docs/roadmap/v1-complete-and-v2-roadmap-2026-09.md`

## Purpose

Agentic Trust Foundation defines open protocols and reference infrastructure for establishing and evaluating authority in interactions involving autonomous and semi-autonomous agents.

The Foundation separates **authority** from **execution** and is designed to operate across independent trust domains.

## Architecture

```text
AGENTIC INTERNET
       │
     AGENTS
       │
AGENT COMMERCE
   │         │
   ▼         ▼
ATF TRUST  AGENT-PAY
   │         │
   └────┬────┘
        ▼
    REAL WORLD
```

### Agentic Trust Foundation

Owns identity, credentials, delegation, authorization, capabilities, trust, consent, revocation, provenance, accountability, auditability, and human-approval authority semantics.

### Agent-Pay

A separate financial control/execution layer. It consumes ATF authority evidence and owns financial policy, budgets, approvals, payment instruments, provider execution, transaction/ledger, settlement, and reconciliation.

## Core Principle

> **ATF establishes authority; downstream systems execute within that authority.**

Agent-Pay must never expand upstream ATF authority.

## V1 Scope

V1 includes:

- Agent Identity and principal semantics
- Credentials and verification concepts
- Explicit bounded delegation
- Authorization outcomes: `ALLOW`, `DENY`, `REQUIRE_HUMAN`
- Capabilities and policy semantics
- Trust-domain concepts
- Consent and human approval
- Revocation and fail-closed behavior
- Provenance and auditability
- Discovery/interoperability semantics without requiring a centralized registry
- Versioning and conformance
- Machine-readable schemas
- Reference implementation
- Agent-Pay cross-repository contract

## V1 Boundary

V1 intentionally does **not** freeze:

- one universal ATF credential/token wire format;
- one hosted ATF service;
- one identity provider;
- one agent runtime;
- centralized mandatory reputation;
- mandatory SaaS infrastructure.

Those can be implementation profiles, deployment profiles, extensions, or future protocol versions.

## Repository Structure

```text
agentic-trust/
├── docs/
│   ├── roadmap/
│   ├── release/
│   ├── architecture/
│   ├── protocol/
│   ├── security/
│   └── governance/
├── specs/v1/
├── schemas/v1/
├── conformance/
├── test-vectors/
├── reference/implementation/
├── examples/
└── tools/
```

## Documentation Order

Start here before doing new work:

1. `docs/roadmap/v1-complete-and-v2-roadmap-2026-09.md`
2. `docs/release/v1-final-2026-09.md`
3. `docs/architecture/agent-pay-integration-boundary.md`
4. `specs/v1/`
5. `schemas/v1/`
6. `conformance/` and `test-vectors/`
7. `reference/implementation/`

## Status / Change Control

V1 is a stable baseline. Do **not** restart a full V1 review unless there is evidence of a regression, security defect, violated invariant, conformance failure, or intentional contract change.

Future work must be classified as documentation clarification, non-breaking hardening, optional extension/profile, or V2 semantic change.

## License

Apache-2.0.
\n## Ecosystem Projects\n\nThe public ATF protocol is part of a broader ecosystem:\n\n- **Agent Site Adapter** — public site/service integration layer built around ATF identity, capability, authentication, consent, and authorization boundaries.\n- **Agent-Pay** — separate financial control and payment execution layer.\n- **Agent-Pay Iran** — private country-specific product/deployment profile built on Agent-Pay.\n\nCross-project architecture and decisions are maintained in the private \`project-docs\` repository. Its contents are not part of the public protocol contract.\n