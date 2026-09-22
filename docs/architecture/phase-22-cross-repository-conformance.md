# Phase 22 — Cross-Repository Conformance Contract

**Status:** COMPLETE  
**Baseline:** ATF V1 frozen  
**ATF revision:** `07f3e991ae0eb10ca4d838025f345467ab6684f3`

Phase 22 establishes a reproducible ATF ↔ Agent-Pay conformance boundary without changing ATF V1 semantics.

## Canonical producer

ATF owns the canonical shared Agent-Pay contract vectors:

- path: `conformance/v1/agent-pay-contract-vectors.yaml`
- blob SHA: `11b6939b65906aa0efc768d678b2356db383f7ec`
- suite: `atf-agent-pay-cross-repository-v1`
- vector count: 15

The producer artifact is immutable for this Phase 22 evidence because consumers pin both the producer commit and artifact blob.

## Consumer contract

Agent-Pay must:

1. resolve the exact ATF revision above;
2. verify the expected Git blob SHA before parsing the artifact;
3. compare the normalized vector set with its local consumer copy;
4. fail closed on unavailable, mismatched, or altered producer evidence;
5. preserve the ATF/Agent-Pay authority boundary.

Agent-Pay may further restrict a valid authority decision through financial policy, budget, approval, or payment controls, but cannot mint or broaden ATF authority.

## Covered invariants

The shared suite covers:

- upstream authority ownership;
- explicit PAYMENT scope;
- amount/currency bounds;
- policy and approval non-expansion;
- evidence reference/version retention;
- payment versus settlement separation;
- expiry and revocation;
- audience and subject binding;
- action binding;
- replay handling;
- required evidence;
- monotonic attenuation.

## Evidence classification

Phase 22 evidence is **protocol/conformance evidence**, not production payment evidence.

It does not establish:

- live PSP or bank integration;
- card issuance;
- regulatory certification;
- HSM/vault deployment;
- production readiness.

## Change control

Changing the semantic meaning of these vectors is a V1 protocol change and requires explicit versioning. Updating the pinned producer revision is a conformance-input update and must change the recorded revision and blob digest together.

## Exit condition

An independent consumer can identify the exact ATF revision and vector artifact, verify its content identity, compare it with the local consumer copy, and fail closed on drift.
