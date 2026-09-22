"""Validate the Phase 25 V2 interoperability vector contract.

This checker intentionally validates the shared interoperability contract, not a
particular authorization implementation. It is independent from Agent-Pay's
cross-repository checker so the two repositories independently verify the same
vector identifiers and decisions.
"""

from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]
VECTORS = ROOT / "conformance" / "v2" / "interoperability-vectors.yaml"

EXPECTED = {
    "interop-positive-attenuation": "ALLOW",
    "interop-action-expansion": "DENY",
    "interop-amount-expansion": "DENY",
    "interop-expiry-expansion": "DENY",
    "interop-audience-substitution": "DENY",
    "interop-subject-mismatch": "DENY",
    "interop-expired-parent": "DENY",
    "interop-revoked-parent": "DENY",
    "interop-depth-exceeded": "DENY",
    "interop-replay": "DENY",
    "interop-malformed-unknown-claims": "DENY",
    "interop-revocation-indeterminate": "DENY",
    "interop-human-approval-no-authority": "DENY",
    "interop-equivalent-encoding": "ALLOW",
}


def main() -> None:
    document = yaml.safe_load(VECTORS.read_text(encoding="utf-8"))
    if document.get("version") != "atf/v2":
        raise SystemExit("unexpected ATF V2 interoperability version")
    if document.get("phase") != 25:
        raise SystemExit("unexpected Phase 25 marker")

    actual = {
        item["id"]: item["expected"]
        for item in document.get("vectors", [])
    }
    if actual != EXPECTED:
        raise SystemExit(
            "Phase 25 interoperability vectors do not match the canonical "
            "identifier/decision contract"
        )

    print(
        "ATF V2 interoperability contract OK: "
        f"{len(actual)} vectors; implementation=atf-reference-validator/1"
    )


if __name__ == "__main__":
    main()
