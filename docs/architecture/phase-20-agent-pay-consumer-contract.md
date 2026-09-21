# Phase 20 — Agent-Pay Interoperability Consumer Contract

ATF V1 remains the authority layer. Agent-Pay consumes normalized authority evidence and cannot expand it.

## Required semantic handoff

The downstream financial decision must preserve:
- requesting agent identity;
- delegating principal/delegation provenance;
- issuer and trust domain;
- explicit authorization decision;
- action and resource;
- constraints including amount/currency/purpose/time where present;
- issued/expiry interval;
- revocation state;
- stable evidence reference/version.

## Required fail-closed cases

A consumer must not authorize execution when required evidence is:
- missing or malformed;
- expired;
- revoked or indeterminate;
- bound to another subject;
- bound to another audience/trust domain;
- for another action/resource;
- outside amount/currency/time constraints;
- replayed in a way that changes the original intent.

## Boundary invariant

Agent-Pay financial policy, budget, or human approval can further restrict valid ATF authority. None can create or enlarge upstream authority.

## Verification

The canonical executable vector set is maintained in Agent-Pay:
`conformance/v1/atf-agent-pay-contract-vectors.yaml`.

This document is an integration-consumer contract, not a new ATF V1 normative protocol.
