# V2 Federation and Assurance

## Federation
Federation establishes relationships and metadata between entities. It does not grant operation-specific permission.

The V2 design can support trust anchors, bilateral trust, and mediated trust domains while keeping authorization contextual.

## Assurance
Assurance describes the quality and provenance of identity/credential verification. It is evidence for policy evaluation, not a universal trust score.

## Reputation
Reputation is advisory. A reputation value must never be converted implicitly into ALLOW.

## Policy
Deployments choose how assurance/reputation affect policy. Protocol semantics remain explicit and auditable.
