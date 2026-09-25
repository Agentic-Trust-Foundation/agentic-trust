# ATF / Agent-Pay V2 Evidence Matrix

**Audit date:** 2026-09-25  
**Scope:** phases 35-43 and the ATF, Agent-Pay, Site Adapter, and Portfolio repositories.

This matrix records repository evidence, not claims inferred from phase names. A phase contract declaring a completion target is not itself evidence that every target is independently implemented.

| Phase | Spec/Contract | Schema/Vectors | Implementation | Tests | CI | Cross-repo | Current assessment |
|---|---|---|---|---|---|---|---|
| 35 | ATF + Agent-Pay contracts | Embedded vectors | Generic runners; Agent-Pay reference implementation exists | Reference suites + V2 runner | Workflows present | Final verifier | **Contract/conformance verified; domain implementation evidence partial** |
| 36 | Contracts present | Embedded vectors | Provider/instrument concepts exist | Reference tests | CI present | Final verifier | **Contract/conformance verified; provider execution evidence partial** |
| 37 | Contracts present | Embedded vectors | Commerce/payment API and E2E scenario exist | E2E/reference tests | CI present | Final verifier | **Reference E2E evidence; external commerce integration not proven** |
| 38 | Contracts present | Embedded vectors | Deployment-related configuration exists | CI validation | CI present | Final verifier | **Contract evidence; real production deployment not proven** |
| 39 | Security contract + vectors | Embedded vectors | JWT/OIDC/ATF evidence verification and security tests exist | Auth/evidence tests | Dependency audit in reference CI | Cross-repo checks | **Substantial implementation evidence; independent security assessment open** |
| 40 | Independent certification contract | Embedded vectors | Go independent structural verifier added in this branch | Go verifier + Python runners | Workflow update in this branch | Agent-Pay cross-repo gate exists | **In progress: independent runner exists; external certification open** |
| 41 | V2 RC contract | Embedded vectors | Release-gate contract exists | Final contract tests | Final CI exists in Agent-Pay | Cross-repo gate exists | **Release contract verified; RC evidence must be assembled** |
| 42 | ATF V2 Final contract | Embedded vectors | Final-gate contract exists | ATF validation + Agent-Pay final gate | ATF validation green on current main | Agent-Pay compares phases 35-42 | **Protocol-gate evidence present; production/certification evidence open** |
| 43 | Agent-Pay final contract + vectors | Explicit vectors | Agent-Pay reference implementation exists | Final + reference tests | v2-final workflow | Cross-repo verifier | **Final contract gate verified; real provider/settlement evidence open** |

## Verified current repository anchors

- ATF main: `afb9fc7c7d7115ef9d2e156baf57331f93d44f48`; latest observed ATF validation run succeeded; the new V2 35-42 workflow also passed its independent Go verifier.
- Agent-Pay main: `677c09794567117b0c93f636ef4895f2578605d`; V1 conformance, reference implementation, Docker smoke, V2 phases 35-42, and V2 final workflows are present. V2 Final run #7 passed the pinned ATF Go verifier.
- Agent-Site-Adapter main: `fc72890ce37c17a8aec6f68ae1b596b7789be622`; external integration profile and quickstart, package/tests/CI are present.
- Portfolio main: `fdcb3fa1406221f8ae5794dfa2ecef8d0b1c390f`; Vercel status was observed as successful.

## Remaining evidence gaps

1. A genuinely external implementation maintained outside the Agentic-Trust-Foundation organization.
2. A real/sandbox payment provider adapter exercised through the Agent-Pay API.
3. Reproducible provider webhook + idempotency + reconciliation evidence.
4. Independent security review or penetration test.
5. Independent interoperability certification by an external party.
6. Production deployment evidence: HA, key management, observability, backup/DR, and incident procedures.

## Decision rule for future work

Do not create a new phase merely to add documentation. A future phase should add at least one new independently observable capability: implementation, executable vector, security test, provider integration, deployment evidence, or external certification.
