# 3. Identity

## Status
Normative — ATF Protocol v1.

## 3.1 Purpose
Identity establishes the subject to which authority, delegation, credentials, and authorization decisions are bound.

## 3.2 Identifiers
An ATF identifier MUST be unique within its declared trust domain and stable for the validity period of the authority that references it. Implementations MUST NOT infer authority solely from an identifier.

## 3.3 Subjects
A subject MAY be a principal, agent, organization, or service. An agent acting for a principal MUST be distinguishable from the principal.

## 3.4 Binding
Authorization MUST bind the subject to the requested action, resource, and applicable context. Authentication proves control of a credential or authenticator; it does not by itself establish authorization.

## 3.5 Interoperability
Protocol implementations MUST expose a stable identifier and sufficient verification metadata for an independent verifier to determine which trust domain issued the relevant identity evidence.
