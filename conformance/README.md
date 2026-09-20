# Conformance

The V1 conformance suite verifies implementations against the Agentic Trust Protocol semantics.

Core domains include identity, credentials, delegation, authorization, capabilities, policy, revocation, consent, provenance, and security.

Conformance is evidence-based. A result MUST identify protocol version, implementation version, vector-suite version, and applicable profile. Missing required evidence is non-conforming.

Core deterministic vectors are published in `test-vectors/v1/core.yaml` and referenced by `conformance/v1/core-vectors.yaml`.

The Agent-Pay boundary remains a separate profile under `conformance/v1/agent-pay-contract-vectors.yaml`.
