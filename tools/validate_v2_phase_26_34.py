#!/usr/bin/env python3
from pathlib import Path
import yaml
EXPECTED={"trust-negotiation-established":"ALLOW","trust-negotiation-rejected":"DENY","trust-negotiation-indeterminate":"DENY","capability-constraint-intersection":"ALLOW","capability-constraint-expansion":"DENY","delegation-multi-hop-attenuation":"ALLOW","delegation-parent-revoked":"DENY","delegation-depth-exceeded":"DENY","evidence-subject-mismatch":"DENY","evidence-audience-substitution":"DENY","credential-revoked":"DENY","credential-rotation-valid":"ALLOW","provenance-minimum-disclosure":"ALLOW","enterprise-assurance-policy":"ALLOW","enterprise-assurance-not-authority":"DENY","human-approval-without-authority":"DENY","malformed-security-claim":"DENY","replayed-evidence":"DENY","cross-language-equivalent-decision":"ALLOW","full-conformance-composed-negative":"DENY"}
d=yaml.safe_load(Path("conformance/v2/phase-26-34-vectors.yaml").read_text())
assert d["protocol_version"]=="atf/v2" and d["phase"]==26
actual={v["id"]:v["expected_decision"] for v in d["vectors"]}
assert actual==EXPECTED
print("implementation=atf-python-reference-validator/1")
print("phase-range=26-34")
print(f"vectors={len(actual)}")
