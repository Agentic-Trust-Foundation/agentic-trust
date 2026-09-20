# 8. Policy

## Status
Normative — ATF Protocol v1.

Policy is the explicit rule set used to evaluate authorization, trust, delegation, consent, and related controls.

Policy MUST be versioned. An authorization decision MUST be attributable to the policy version used to produce it.

Policy evaluation MUST fail closed when a required policy input is unavailable and the policy requires that input.

Policy engines MAY be local, federated, or hosted; protocol interoperability MUST NOT depend on one centralized policy service.
