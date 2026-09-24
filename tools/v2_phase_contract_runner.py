#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
for p in range(35,43):
    f=ROOT/f"conformance/v2/phase-{p}/contract.json"
    c=json.loads(f.read_text())
    assert c["phase"]==p
    assert c["protocol_version"]=="atf/v2"
    rules=set(c["rules"])
    assert len(c["vectors"])==len(rules)+1
    for v in c["vectors"]:
        assert v["expected_decision"]=="DENY" if v["rule"]=="fail-closed" else v["expected_decision"]=="ALLOW"
        if v["rule"]!="fail-closed": assert v["rule"] in rules
print("ATF V2 phases 35-42: PASS")
