DECISIONS = {"ALLOW", "DENY", "REQUIRE_HUMAN"}

def authorize(*, delegated: bool, capability_allows: bool, policy_allows: bool,
              revoked: bool = False, human_required: bool = False,
              verification_available: bool = True) -> str:
    if not verification_available or revoked:
        return "DENY"
    if human_required:
        return "REQUIRE_HUMAN"
    if delegated and capability_allows and policy_allows:
        return "ALLOW"
    return "DENY"
