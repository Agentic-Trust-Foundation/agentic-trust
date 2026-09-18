# Agent-Pay V1 Boundary Freeze

Agentic Trust Foundation and Agent-Pay are frozen as separate V1 responsibility
domains.

ATF remains responsible for identity, delegation, authorization, capability,
trust, consent, provenance, and revocation.

Agent-Pay remains responsible for financial control and execution.

The V1 cross-repository contract is represented by the shared vector suite:

conformance/v1/agent-pay-contract-vectors.yaml

The boundary is intentionally protocol-adapter-friendly: V1 does not freeze one
universal ATF token or signature format. Agent-Pay consumes the normalized
authority result and must not mint or expand general authorization.

Changes that move responsibility across this boundary require a new architecture
decision and must not be introduced as an incidental implementation change.
