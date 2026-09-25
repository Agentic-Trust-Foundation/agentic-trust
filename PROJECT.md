# Agentic Trust Foundation — Project Definition

## 30-second definition

**Agentic Trust Foundation (ATF) is an open protocol and reference-implementation effort for the trust, identity, delegation, authorization, and accountability layer required when AI agents act on behalf of users and organizations.**

ATF establishes **who is acting, on whose authority, with what scope, under which policy, with what evidence, and with what accountability**.

ATF is designed to work alongside existing agent, identity, API, and payment protocols rather than replace them.

## The problem

An AI agent can increasingly discover services, call APIs, make purchases, book services, operate infrastructure, and delegate work to another agent.

The technical ability to perform an action is not the same as the authority to perform it.

ATF defines the trust/delegation layer for answering: is the agent authorized to perform this action, by whom, within what scope, for how long, under which policy, and with what evidence and accountability?

## Ecosystem

~~~text
USER / ORGANIZATION
        |
        v
      AGENT
        |
        | delegated authority
        v
+---------------------------+
|   AGENTIC TRUST FOUNDATION|
| identity / delegation     |
| authorization / policy    |
| trust / consent           |
| provenance / revocation   |
| accountability / audit    |
+-------------+-------------+
              |
      authority evidence
              |
      +-------+--------+
      |                |
      v                v
 SITE / API        AGENT-PAY
 ADAPTER           financial controls
      |             / payment execution
      v                |
 SERVICES / COMMERCE --+--> PAYMENT RAILS
~~~

### ATF

ATF owns trust and authority semantics: identity, credentials/evidence, delegation, authorization, capabilities, consent, revocation, provenance, accountability, and human-control semantics.

### Agent-Pay

Agent-Pay is the **financial control and payment execution layer built on authority established by ATF**. It applies financial policy, budgets, approvals, payment instruments, provider execution, transaction/ledger, settlement, and reconciliation.

**Agent-Pay must never expand upstream ATF authority.**

### Agent Site Adapter

Agent Site Adapter applies the ecosystem's trust and authorization semantics to websites and services. It is an integration layer, not a replacement for MCP, A2A, OAuth, payment rails, or ATF.

## What this project is not

ATF is not:

- a blockchain or cryptocurrency;
- an LLM or general-purpose agent framework;
- an agent marketplace;
- a bank, PSP, payment processor, or card issuer;
- an API gateway;
- a replacement for OAuth, MCP, A2A, or other protocol wire formats;
- a mandatory hosted SaaS trust service;
- a centralized global trust registry.

Agent-Pay is not a bank or payment rail. A reference implementation or sandbox provider profile is not evidence of a live external PSP/bank integration.

## What is implemented

The public ecosystem contains protocol specifications, machine-readable schemas, conformance contracts and vectors, reference implementations, security tests, CI gates, cross-repository verification, and an evidence-focused portfolio.

The current public baseline includes:

- ATF V2 final protocol/conformance baseline;
- Agent-Pay V2 final protocol/conformance baseline;
- Agent Site Adapter V1 final semantic/profile baseline;
- Python reference implementations and tests;
- an independent Go conformance verifier for ATF V2 phases 35–42;
- Agent-Pay cross-repository verification against ATF contracts;
- provider simulator/webhook/settlement/reconciliation reference components.

## What is not yet proven

The project deliberately distinguishes implementation evidence from real-world deployment evidence.

The following require additional external evidence before being described as production-ready:

- live external PSP/bank/card-issuer integration;
- production deployment evidence from an independent operator;
- independent security assessment/certification;
- independent interoperability certification/adoption outside the Foundation's own repositories.

## Canonical principle

> **ATF establishes authority; downstream systems execute within that authority.**

For the rationale, see WHY.md. For machine-readable AI/discovery context, see AI-CONTEXT.md. For terminology, see GLOSSARY.md. For the current evidence boundary, see STATUS.md.
