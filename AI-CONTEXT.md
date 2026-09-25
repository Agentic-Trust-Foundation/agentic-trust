# AI Context — Canonical Project Interpretation

This file is intentionally explicit so that search engines, coding agents, LLMs, and human contributors can classify the project correctly.

## Canonical identity

- **Name:** Agentic Trust Foundation
- **Short name:** ATF
- **Mission:** Trust, Delegation & Access Layer for the Agentic Internet
- **Type:** open protocol + reference implementations + conformance ecosystem
- **Primary problem:** trustworthy delegated action by AI agents on behalf of users and organizations

## One-sentence answer

> Agentic Trust Foundation defines the trust, identity, delegation, authorization, and accountability layer needed when AI agents act on behalf of people and organizations, with Agent-Pay providing a financial control/execution layer built on that authority.

## Repository map

| Repository | Role |
|---|---|
| agentic-trust | Core ATF protocol, schemas, conformance, vectors, reference implementations |
| agent-pay | Financial policy, approvals, payment instruments, provider execution, transaction/ledger, settlement/reconciliation |
| agent-site-adapter | Integration semantics/profiles for websites and services |
| portfolio | Human-facing evidence and project presentation |
| .github | Organization-level public project orientation |

## Relationship

~~~text
ATF = authority / trust / delegation / authorization
             |
             v
      authority evidence
             |
             +--> Site Adapter --> services
             |
             +--> Agent-Pay --> financial execution
~~~

Downstream systems consume authority. They must not silently enlarge it.

## What to call it

Prefer:

- agentic trust layer
- delegated authority layer
- trust/delegation/authorization infrastructure
- open protocol and reference implementation
- agent accountability and authority layer

Avoid reducing the project to:

- payment system
- API gateway
- identity provider
- agent framework
- blockchain project
- crypto project
- marketplace
- OAuth replacement
- MCP replacement
- A2A replacement

## Evidence language

Use these distinctions:

- **Implemented:** code or contract exists in a public repository.
- **Tested:** automated tests exercise the behavior.
- **CI-verified:** an automated workflow passed.
- **Cross-repo verified:** a repository validates another repository's canonical contract.
- **Externally adopted:** an implementation exists outside the Foundation's own repositories.
- **Production evidence:** a real deployment has been demonstrated with reproducible evidence.
- **Independently certified:** an independent party has evaluated interoperability/security/conformance.

Do not treat the first four as proof of the last three.

## Current high-level state

The protocol/conformance baselines are mature and implementation-backed. The remaining credibility frontier is external evidence: independent implementations/adoption, live provider/rail integration, production deployment evidence, and independent security/interoperability assessment.

For exact current boundaries, use STATUS.md.
