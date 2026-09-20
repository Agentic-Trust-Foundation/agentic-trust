# AGENTS.md

## Repository mission

Agentic Trust Foundation is a protocol-first, implementation-backed, service-optional foundation for trust, delegated authority, policy, provenance, and accountability in the agentic internet.

## Working rules

- Read the relevant README, specification, and architecture documents before changing protocol behavior.
- Treat specifications and schemas as contracts.
- Preserve separation between authority decisions and execution.
- Prefer explicit, least-privilege, fail-closed behavior.
- Keep protocol artifacts deterministic and machine-readable where practical.
- Add conformance vectors for externally observable protocol behavior.
- Do not introduce a centralized mandatory trust authority unless the specification explicitly calls for it.
- Do not commit secrets or generated credentials.
- Run the narrowest relevant tests first, then the full validation gate when practical.

## Change discipline

For protocol changes, update documentation/specification, schemas, examples, and conformance coverage together. Record compatibility implications and versioning decisions.
