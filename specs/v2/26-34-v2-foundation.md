# V2 Phases 26–34 — Trust, Constraints, Evidence, Lifecycle, Privacy, Enterprise, Cross-Language, Conformance

V1 remains frozen. These phases extend V2 only.

## Phase 26 — Cross-Domain Trust Negotiation
Trust negotiation establishes a verifiable trust context between independent domains. It never grants authority by itself.
A negotiation record identifies initiator, responder, domain identifiers, requested trust properties, supported profiles, evidence requirements, freshness, and outcome.
Supported outcomes are `ESTABLISHED`, `REJECTED`, and `INDETERMINATE`; indeterminate verification fails closed for authorization.
No global registry or mandatory centralized trust service is required. Bilateral and mediated discovery are valid.

## Phase 27 — Rich Capability Constraints
Capabilities describe what an actor may be able to request; they do not create authority.
Constraints may cover resource, action, audience, amount, currency, region, merchant/category, time window, frequency, and context.
Effective constraints are the intersection of upstream authority and every downstream restriction. Unknown security-relevant constraints cause rejection unless an explicit profile defines safe handling.

## Phase 28 — Delegation Chains 2.0
Authority is evaluated across root → delegate → sub-delegate chains. Each child must preserve or attenuate every parent dimension.
A child cannot expand action, resource/audience, numeric bounds, validity, or delegation depth, and cannot remove a security constraint.
Parent expiry or revocation invalidates dependent authority unless an independently valid authority path exists.

## Phase 29 — Authorization Evidence Profiles
Authorization evidence is a normalized, integrity-protected statement of the authority decision inputs and provenance.
Evidence binds subject, audience/resource, action, constraints, validity, revocation state, delegation chain, and integrity metadata.
Profiles may map JWT, VC, OAuth, OpenID Federation, or other mechanisms into these semantics; ATF does not mandate one universal credential wire format.

## Phase 30 — Credential Lifecycle
Credentials and keys have explicit lifecycle states: ACTIVE, SUSPENDED, REVOKED, EXPIRED, and ROTATED.
Verification must select an acceptable current credential, reject revoked/expired credentials, and tolerate bounded clock skew only where the profile explicitly permits it.
Rotation must not silently broaden authority. Revocation distribution freshness is part of the verification result.

## Phase 31 — Privacy-Preserving Provenance
Provenance must provide accountability with minimum necessary disclosure.
Profiles should support selective disclosure, pseudonymous identifiers, integrity-preserving references, and explicit correlation-risk controls.
Privacy mechanisms cannot remove evidence required to establish authority, subject binding, or revocation status.

## Phase 32 — Enterprise High-Assurance Profile
Enterprise profiles may require stronger identity assurance, organizational boundaries, administrative delegation, policy provenance, audit evidence, and incident controls.
Assurance levels are policy inputs, not universal trust scores. Federation establishes trust context but does not grant permission.

## Phase 33 — Cross-Language Reference Implementations
At least two independent implementations must consume the same canonical vectors. A reference implementation in Go is provided alongside the existing Python implementation.
Implementations must produce equivalent normalized decisions and evidence fields for the shared vectors.

## Phase 34 — Full Conformance Suite
The suite composes identity, authorization, constraints, delegation, trust, lifecycle, provenance, interoperability, replay, revocation, and fail-closed behavior.
A V2 semantic feature is normative for interoperability only after two independent implementations validate the same vectors with equivalent results.
V1 semantics remain unchanged.

## Security invariants
Authentication is not authorization. Capability is not authority. Delegation cannot exceed upstream authority. Human approval cannot manufacture authority. Agent-Pay may restrict authority but never broaden it. Invalid, expired, revoked, ambiguous, or unverifiable authority fails closed.
