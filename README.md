# Agentic Trust Foundation

> **Trust, Delegation & Access Layer for the Agentic Internet**

Agentic Trust Foundation (ATF) is an open protocol and reference-implementation effort for the **trust, identity, delegation, authorization, and accountability layer** required when AI agents act on behalf of users and organizations.

**Core principle:** ATF establishes authority; downstream systems execute within that authority.

## Start here

If you are discovering this project for the first time:

1. **[PROJECT.md](PROJECT.md)** — canonical definition, ecosystem map, boundaries, and what is / is not implemented
2. **[WHY.md](WHY.md)** — the problem ATF exists to solve and why Agent-Pay is built on top of it
3. **[AI-CONTEXT.md](AI-CONTEXT.md)** — canonical machine/LLM interpretation and repository map
4. **[STATUS.md](STATUS.md)** — current evidence boundary: implemented, verified, and still evidence-gated
5. **[GLOSSARY.md](GLOSSARY.md)** — project terminology
6. **docs/roadmap/** — historical and V2 roadmap context
7. **specs/**, **schemas/**, **conformance/**, **test-vectors/** — normative and machine-readable protocol material
8. **reference/implementation/** — reference implementations

## Ecosystem

~~~text
AGENTIC INTERNET
       |
     AGENTS
       |
   delegated authority
       |
      ATF
       |
       +----> Agent Site Adapter ----> Websites / Services
       |
       +----> Agent-Pay ------------> Financial execution
                                      |
                                      +--> Payment providers / rails
~~~

### ATF

ATF defines identity, credentials/evidence, delegation, authorization, capabilities, trust, consent, revocation, provenance, accountability, auditability, and human-control authority semantics.

### Agent-Pay

Agent-Pay is the financial control and payment execution layer built on authority established by ATF. It owns financial policy, budgets, approvals, payment instruments, provider execution, transactions/ledger, settlement, and reconciliation.

### Agent Site Adapter

Agent Site Adapter applies trust and authorization semantics to websites and services. It does not replace MCP, A2A, OAuth, ATF, payment rails, or other authoritative protocols.

## What this is not

ATF is not a blockchain, cryptocurrency, LLM/agent framework, marketplace, bank, PSP, payment processor, API gateway, mandatory hosted trust service, or replacement for OAuth/MCP/A2A.

## V1 Status

**ATF Protocol V1 is FINAL and frozen as an open protocol + schemas + conformance suite + reference implementation.**

V1 is intentionally protocol-first, implementation-backed, and service-optional.

## V2 Status

The public V2 baseline is implementation-backed with machine-readable contracts, conformance vectors, automated verification, and cross-repository validation. See STATUS.md for the distinction between internal engineering evidence and external production/adoption evidence.

## Repository Structure

~~~text
agentic-trust/
├── docs/
├── specs/v1/
├── schemas/v1/
├── conformance/
├── test-vectors/
├── reference/implementation/
├── examples/
└── tools/
~~~

## Important evidence boundary

A reference implementation, passing CI, provider simulator, or cross-repository verifier is **not** by itself proof of:

- live external PSP/bank/card-issuer integration;
- independent production deployment;
- independent security certification;
- independent interoperability adoption.

Those remain explicit evidence-gated goals.

## Documentation Order

For protocol work, read the canonical project documents first, then the release/architecture docs, specifications, schemas, conformance vectors, and reference implementation.

## License

Apache-2.0.
