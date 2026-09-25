# Project Status and Evidence Boundary

**Last reviewed:** 2026-09-25

This document is an evidence boundary, not a marketing maturity score.

## Current public baselines

| Component | Protocol/conformance | Reference implementation | CI / verification | External evidence |
|---|---|---|---|---|
| ATF | V2 final baseline | Implemented | Python + independent Go verifier | Independent adoption/certification still open |
| Agent-Pay | V2 final baseline | Implemented | Final CI + ATF cross-repo gate | Live external PSP/bank integration still open |
| Agent Site Adapter | V1 final baseline | Semantic/profile reference | Automated tests/CI | Production security boundary requires deployment-specific hardening |
| Portfolio | Evidence presentation | Implemented | Typecheck/build CI | Presentation only; not an interoperability test suite |

## What has strong evidence

- normative contracts and machine-readable schemas;
- conformance vectors and contract runners;
- reference implementations;
- automated tests and CI;
- ATF ↔ Agent-Pay cross-repository contract verification;
- independent Go verification of ATF V2 phase contracts;
- provider/webhook/settlement/reconciliation reference components in Agent-Pay;
- explicit security tests for authentication/evidence/webhooks/redaction and related invariants.

## What remains evidence-gated

### 1. External provider/rail execution

A provider simulator or reference adapter demonstrates the architecture. It does not prove a live external PSP, bank, card issuer, or payment rail integration.

### 2. Independent implementation/adoption

Foundation-owned repositories demonstrate internal interoperability. They are not independent adoption.

### 3. Production deployment

A deployable reference system is not the same as independently observed production operation.

### 4. Independent security/interoperability assessment

Automated security tests are valuable evidence, but they are not a substitute for an independent assessment or certification.

## Release language

Safe claims:

- “protocol/conformance baseline”
- “reference implementation”
- “CI-verified”
- “cross-repository verified”
- “provider simulation/reference integration”

Claims requiring additional evidence:

- “production-ready”
- “live payment provider integrated”
- “independently adopted”
- “independently certified”
- “bank/PSP production integration”

## Next work should prioritize external proof

The project has already invested heavily in protocol, schema, conformance, implementation, and CI machinery. Further work should preferentially close evidence gaps rather than create additional phases for already-covered semantics.

Relevant tracked work includes real/sandbox provider integration, production deployment evidence, independent implementation, and independent security/interoperability assessment.
