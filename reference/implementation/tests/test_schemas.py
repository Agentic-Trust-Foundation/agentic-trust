from atf_reference.validator import validate_document

def test_valid_authorization_request():
    doc = {
        "protocol_version": "atf/v1",
        "request_id": "req-1",
        "subject": {"id": "agent-1", "type": "agent"},
        "action": "purchase",
        "resource": {"id": "merchant-1", "type": "merchant"}
    }
    assert validate_document("authorization-request", doc) == []

def test_invalid_decision_outcome():
    doc = {
        "protocol_version": "atf/v1",
        "decision_id": "dec-1",
        "request_id": "req-1",
        "outcome": "MAYBE",
        "policy_version": "policy-1"
    }
    assert validate_document("authorization-decision", doc)

def test_valid_delegation():
    doc = {
        "protocol_version": "atf/v1",
        "delegation_id": "del-1",
        "delegator": {"id": "user-1", "type": "principal"},
        "delegate": {"id": "agent-1", "type": "agent"},
        "scope": {"actions": ["purchase"]},
        "valid_from": "2026-01-01T00:00:00Z",
        "valid_until": "2027-01-01T00:00:00Z"
    }
    assert validate_document("delegation", doc) == []
