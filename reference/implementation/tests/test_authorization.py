from atf_reference.authorization import authorize

def test_allow_requires_all_authority_inputs():
    assert authorize(delegated=True, capability_allows=True, policy_allows=True) == "ALLOW"

def test_missing_delegation_denies():
    assert authorize(delegated=False, capability_allows=True, policy_allows=True) == "DENY"

def test_capability_denies():
    assert authorize(delegated=True, capability_allows=False, policy_allows=True) == "DENY"

def test_policy_denies():
    assert authorize(delegated=True, capability_allows=True, policy_allows=False) == "DENY"

def test_revocation_denies():
    assert authorize(delegated=True, capability_allows=True, policy_allows=True, revoked=True) == "DENY"

def test_human_approval_is_distinct():
    assert authorize(delegated=True, capability_allows=True, policy_allows=True, human_required=True) == "REQUIRE_HUMAN"

def test_verification_unavailable_fails_closed():
    assert authorize(delegated=True, capability_allows=True, policy_allows=True, verification_available=False) == "DENY"
