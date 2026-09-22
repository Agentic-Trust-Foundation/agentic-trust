# Phase 24 — Agent-to-Agent Delegation

**Status:** V2 design/implementation baseline  
**Scope:** ATF V2 delegated authority between agents  
**V1 impact:** None. ATF V1 remains frozen.

## 1. Objective
Define a machine-verifiable model for an agent to delegate a bounded subset of its authority to another agent without creating a new root of authority.

The model MUST preserve the existing ATF invariant:
> A delegated principal can never obtain more authority than its delegator possesses.

## 2. Delegation record
A V2 agent-to-agent delegation MUST identify:
- delegation_id
- delegator
- delegate
- audience or resource target
- allowed actions/capabilities
- constraints
- validity interval
- parent delegation/evidence reference
- delegation depth
- revocation reference
- evidence integrity/provenance

The record describes authority; it does not authenticate either participant.

## 3. Chain semantics
A verifier evaluates the complete relevant chain: root → agent-A → agent-B → ... → final-agent.

Effective authority is the intersection of every applicable parent scope and constraint.

A child delegation MUST be rejected when it:
- grants an action absent from the parent;
- broadens a resource/audience;
- increases an amount or other numeric bound;
- extends validity beyond the parent;
- removes a parent constraint;
- exceeds the permitted delegation depth;
- is based on an expired or revoked parent.

## 4. Sub-delegation
Sub-delegation is allowed only when the parent authority explicitly permits it.
Each hop MUST attenuate or preserve, never broaden, the effective authority.
`delegation_depth` is a safety bound, not a substitute for authorization evaluation.

## 5. Revocation
Revocation of a parent delegation invalidates dependent child delegations for authorization purposes unless an independently valid authority path remains.
A verifier MUST fail closed when required revocation status is unavailable or indeterminate under the selected assurance profile.

## 6. Binding
The final authorization decision MUST bind the effective authority to the final delegate, intended audience/resource, requested action, applicable constraints, validity interval, and verified delegation chain.
An identity match alone is insufficient.

## 7. Human approval
Human approval may satisfy an approval requirement already present in policy or authority. It MUST NOT create authority absent from the delegation chain.

## 8. Privacy and provenance
Implementations SHOULD expose stable references and integrity hashes instead of unnecessarily copying sensitive parent evidence through every hop.
The verifier MUST retain enough provenance to reconstruct the authority path used for a decision.

## 9. Compatibility
This phase defines a V2 extension. Existing V1 delegation records remain valid under V1 semantics.
V2 implementations MAY consume V1 delegations as roots, but MUST NOT reinterpret a V1 record as granting capabilities not present in it.

## 10. Acceptance gates
Phase 24 is complete when:
1. normative V2 chain semantics are documented;
2. a machine-readable schema exists;
3. positive and negative attenuation vectors exist;
4. revocation, expiry, depth, audience and subject-binding cases are covered;
5. reference validation proves monotonic attenuation;
6. Agent-Pay consumption rules preserve upstream bounds;
7. CI validates the new assets;
8. no V1 semantic contract is modified.