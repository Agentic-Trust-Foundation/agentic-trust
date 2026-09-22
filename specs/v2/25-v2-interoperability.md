# Phase 25 — V2 Interoperability

**Status:** V2 interoperability design baseline  
**V1 impact:** None. V1 semantic contracts remain frozen.

## Objective

Turn the Phase 24 agent-to-agent delegation model into an explicit interoperability target across ATF and Agent-Pay without inventing a new universal credential or authentication protocol.

## Interoperability layers

1. **Semantic contract** — identical meaning for principals, authority, delegation, constraints, expiry, revocation and effective scope.
2. **Machine-readable artifacts** — versioned schemas and vectors.
3. **Verification behavior** — independent implementations must reach the same authorization result for the same vector.
4. **Security behavior** — fail closed on invalid, expired, revoked, ambiguous, replayed or audience/subject-mismatched evidence.
5. **Cross-repository binding** — Agent-Pay consumes ATF authority without expanding it.
6. **Operational variance** — transport, credential format, storage and deployment are implementation/profile choices unless made normative.

## Required V2 interoperability vectors

- positive delegation attenuation;
- action expansion;
- numeric/amount expansion;
- validity expansion;
- audience substitution;
- subject mismatch;
- expired parent;
- revoked parent;
- depth exceeded;
- replay;
- malformed/unknown claims;
- unavailable/indeterminate revocation;
- human approval without upstream authority;
- equivalent encodings producing equivalent decisions.

## Two-implementation rule

A V2 semantic feature MUST NOT be promoted to a normative interoperability requirement until at least two independent implementations can validate the same vectors and produce the same results.

The reference implementations may be different languages or independent runtimes. Merely duplicating one implementation's code or test output does not satisfy independence.

## Conformance result model

Each vector should record:

- vector identifier;
- protocol/version;
- implementation identifier/version;
- input digest;
- expected decision;
- actual decision;
- pass/fail;
- evidence reference.

## Compatibility rules

- ATF V1 and Agent-Pay V1 remain unchanged.
- V2 consumers must reject unsupported protocol versions rather than silently reinterpret them.
- Agent-Pay financial policy may further restrict a valid ATF delegation but may never broaden it.
- Provider-specific formats remain profiles.
- OAuth, VC, OpenID Federation and similar mechanisms remain optional interoperability/security profiles; this phase does not create a replacement authentication protocol.

## Acceptance gates

Phase 25 is complete only when:
1. shared V2 interoperability semantics are documented;
2. schemas/vectors are versioned;
3. both repositories expose compatible vectors;
4. conformance output has a stable evidence shape;
5. negative/fail-closed cases are covered;
6. unsupported-version behavior is defined;
7. the two-implementation gate is explicit;
8. CI validates all repository-local assets;
9. no V1 semantic contract changes.
