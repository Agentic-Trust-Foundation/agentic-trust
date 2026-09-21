# ATF Project Status & Roadmap — V1 Final / V2 Forward Plan

**Baseline date:** 2026-09-22  
**Status:** **V1 FINAL — frozen baseline**  
**Repository:** `Agentic-Trust-Foundation/agentic-trust`

> This document is the project memory and navigation point for future work. It records what V1 contains, what was verified, what is intentionally outside V1, and what may be done next. Future contributors should start here before re-opening any V1 review.

## 1. Executive status

ATF V1 is complete as an **open protocol + schemas + conformance suite + reference implementation**.

The V1 semantic boundary is frozen. V1 is not a hosted centralized trust service, not a mandatory SaaS platform, and not a single credential/token format.

**Rule:** Do not restart a full V1 architecture/security review unless new evidence shows a regression, a security defect, a violated invariant, or a change to the V1 contract.

## 2. What V1 delivers

### Authority and trust model
- Agent identity and principal semantics.
- Credential and verification concepts.
- Explicit, bounded delegation.
- Authorization semantics with `ALLOW`, `DENY`, and `REQUIRE_HUMAN`.
- Capability and policy concepts.
- Trust and trust-domain concepts without requiring one global trust authority.
- Consent and human approval semantics.
- Revocation and fail-closed behavior.
- Provenance and auditability.
- Versioning and conformance requirements.
- Discovery as an interoperability concern, without turning ATF into a centralized registry.

### Security invariants
- Authentication is not authorization.
- Missing or indeterminate required authority fails closed.
- Delegation cannot silently exceed the delegator's authority.
- Revocation is part of the authority decision.
- Human approval cannot manufacture authority that does not already exist.
- Implementations may use different credential mechanisms when the normative semantics are preserved.

### Interoperability
- Machine-readable schemas.
- Deterministic reference semantics.
- Conformance vectors.
- Cross-repository Agent-Pay contract.
- Versioned protocol surface.
- Reference implementation and CI conformance.

## 3. ATF ↔ Agent-Pay boundary

ATF answers:

> **Is this agent/principal authorized to perform this action within this authority context?**

Agent-Pay answers:

> **Given valid authority, may this financial operation proceed under financial policy, budget, approval, and execution controls?**

ATF owns:
- identity;
- credentials;
- delegation;
- general authorization;
- capabilities;
- trust;
- consent;
- revocation;
- provenance/accountability.

Agent-Pay owns:
- financial policy;
- budgets/reservations;
- payment approvals;
- payment authentication;
- instruments/routing;
- provider execution;
- transaction lifecycle;
- ledger;
- settlement/reconciliation.

**Invariant:** Agent-Pay must never expand upstream ATF authority.

## 4. V1 verification record

The V1 baseline was hardened and verified with:
- normative release documents;
- OpenAPI/schema/conformance assets;
- PostgreSQL schema and reference implementation;
- fail-closed authorization semantics;
- explicit authority evidence verification boundary;
- cross-repository ATF/Agent-Pay conformance;
- GitHub Actions V1 conformance.

Current `main` commit:
`c349db88d95f1867164fe322df70beda69e5af1e`

The repository has subsequently only received non-semantic CI runtime maintenance on `main`; the V1 semantic baseline remains frozen.

## 5. V1 canonical documentation

Start with these in order:

1. `docs/release/v1-final-2026-09.md` — release contract and boundary.
2. `docs/architecture/agent-pay-integration-boundary.md` — ATF ↔ Agent-Pay authority boundary.
3. `specs/v1/` — normative protocol surface.
4. `schemas/v1/` — machine-readable schemas.
5. `conformance/` and `test-vectors/` — executable interoperability expectations.
6. `reference/implementation/` — reference behavior.
7. This document — project status and forward roadmap.

## 6. What is intentionally NOT V1

These are not unfinished V1 protocol semantics:
- one universal ATF token/credential wire format;
- one hosted ATF service;
- mandatory centralized trust/reputation;
- one identity provider;
- one agent runtime;
- mandatory SaaS infrastructure;
- production deployment topology;
- bank/PSP/card-provider integration;
- jurisdiction-specific certification.

These belong to implementation profiles, deployment profiles, governance work, or future protocol versions.

## 7. V1 change-control rule

Any proposed V1 change must first classify itself as one of:

1. **Documentation clarification** — no semantic change.
2. **Non-breaking implementation hardening** — behavior remains within V1 invariants.
3. **Extension/profile** — optional capability that does not redefine existing V1 meaning.
4. **V2 semantic change** — changes authority, delegation, credential semantics, wire contracts, or other normative behavior.

Only categories 1–3 may normally land without reopening the V1 contract. Category 4 requires an explicit V2 design decision.

## 8. V2 roadmap

### V2-A — Protocol extensions
- Richer cross-domain trust negotiation.
- More expressive capability constraints.
- Delegation chains and attenuation profiles.
- Stronger machine-readable policy composition.
- Interoperable authorization evidence profiles.
- Better privacy-preserving provenance/attestation options.
- Expanded human-approval semantics for long-running workflows.

### V2-B — Inter-agent delegation
- Agent-to-agent delegated authority.
- Delegation handoff and sub-delegation.
- Constraint propagation and attenuation.
- Revocation propagation.
- Cross-domain verification flows.

### V2-C — Discovery and capability exchange
- Agent/service capability discovery.
- Trust-domain discovery.
- Version/profile negotiation.
- Capability metadata without creating a mandatory registry.

### V2-D — Conformance ecosystem
- More independent implementation profiles.
- Negative/security conformance vectors.
- Cross-language reference implementations.
- Interop test harnesses.
- Compatibility matrices.

### V2-E — Operational/security profiles
- Key rotation profiles.
- Credential lifecycle profiles.
- Revocation distribution profiles.
- Privacy/security deployment profiles.
- High-assurance enterprise profiles.

## 9. Work that can proceed without changing V1

- Additional documentation and examples.
- More conformance vectors.
- More reference implementation tests.
- Security hardening that preserves V1 semantics.
- Language/runtime ports.
- Deployment examples.
- Independent interoperability experiments.
- Agent-Pay provider profiles.
- Enterprise integration profiles.

## 10. Definition of done for future protocol versions

A future version is not considered complete until it has:
- explicit scope and non-goals;
- frozen normative semantics;
- schemas;
- conformance vectors;
- reference behavior;
- negative/security tests;
- cross-project integration contract where applicable;
- documented compatibility/migration rules;
- CI evidence;
- release document;
- change-control record.

## 11. Anti-regression checklist

Before saying “V1 is broken” or restarting a full review, check:
- Did the normative V1 semantics change?
- Did a previously enforced security invariant disappear?
- Did a conformance vector fail?
- Did ATF/Agent-Pay boundary semantics change?
- Did a CI regression appear?
- Is the reported issue actually deployment-specific?
- Is it a new optional extension rather than a V1 defect?

If all answers are negative, continue from the existing baseline instead of restarting the project review.

## 12. Project map

```text
AGENTIC INTERNET
      │
    AGENTS
      │
AGENTIC TRUST FOUNDATION
      ├── Identity
      ├── Delegation
      ├── Authorization
      ├── Capability
      ├── Trust
      ├── Consent
      ├── Revocation
      ├── Provenance / Audit
      └── Human Approval
              │
              │ normalized authority
              ▼
          AGENT-PAY
              ├── Financial Policy
              ├── Budget / Reservation
              ├── Approval
              ├── Payment Execution
              ├── Instruments / Routing
              ├── Transaction / Ledger
              └── Settlement / Reconciliation
              │
              ▼
       PAYMENT / COMMERCE RAILS
```

## 13. Current next action

V1 is done and remains frozen. The next major engineering cycle should be selected deliberately from the V2 roadmap or from an implementation/deployment profile rather than by reopening the completed V1 baseline.
