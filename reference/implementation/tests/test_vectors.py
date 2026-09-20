from atf_reference.validator import load_core_vectors

def test_core_vectors_are_loadable():
    suite = load_core_vectors()
    assert suite["protocol"] == "atf/v1"
    assert len(suite["vectors"]) >= 10
    assert {v["expect"] for v in suite["vectors"] if v["expect"] in {"ALLOW","DENY","REQUIRE_HUMAN"}} >= {"DENY","REQUIRE_HUMAN"}
