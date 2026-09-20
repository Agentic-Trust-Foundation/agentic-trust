# ATF V2 Implementation Plan

V1 remains frozen. This document is the V2 engineering backlog.

## Workstreams
1. Cross-domain trust negotiation and trust-domain discovery.
2. Richer capability constraints and constraint propagation.
3. Delegation chains, attenuation, sub-delegation, and revocation propagation.
4. Authorization-evidence profiles and interoperability vectors.
5. Credential lifecycle, key rotation, and revocation distribution.
6. Privacy-preserving provenance.
7. Enterprise high-assurance profiles.
8. Cross-language reference implementations.

## Design rule
Reuse established security mechanisms rather than inventing a new universal credential or authentication protocol. OAuth security BCP remains a baseline, while VC and OpenID Federation are optional interoperability profiles where their models fit. V2 work must preserve the V1 invariants: authentication is not authorization, capability is not authority, and delegation cannot exceed upstream authority.

## Advanced agent-to-agent delegation
A delegated authority record must carry:
- delegator
- delegate
- audience/resource
- allowed actions
- constraints
- expiry
- delegation depth/chain reference
- revocation reference
- evidence integrity

Sub-delegation can only attenuate authority.

## Federation
Federation is a trust establishment mechanism, not a universal permission grant. V2 should support bilateral and mediated trust domains without requiring one global registry.

## Reputation/assurance
Reputation is advisory evidence. It must never silently turn into authorization. Assurance levels are policy inputs, not universal trust scores.

## Interoperability gates
- positive and negative vectors
- independent implementations
- cross-language verification
- key rotation
- revocation propagation
- clock skew
- replay
- audience substitution
- delegation attenuation
