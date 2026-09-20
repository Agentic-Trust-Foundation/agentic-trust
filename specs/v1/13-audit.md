# 13. Audit

## Status
Normative — ATF Protocol v1.

Audit records security- and authority-relevant events and decisions.

Audit records MUST be attributable to a subject/domain and timestamp and SHOULD contain decision/evidence references sufficient for reconstruction. Implementations MUST protect audit integrity against unauthorized modification and SHOULD support retention policies appropriate to the trust domain.

Audit data MUST be minimized and MUST NOT expose credentials or secrets unnecessarily.
