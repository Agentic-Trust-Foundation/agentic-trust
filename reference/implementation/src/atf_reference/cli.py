import argparse
import json
from .validator import validate_document, load_core_vectors

def main() -> int:
    p = argparse.ArgumentParser(prog="atf-validate")
    sub = p.add_subparsers(dest="command", required=True)
    v = sub.add_parser("schema")
    v.add_argument("kind", choices=["authorization-request","authorization-decision","delegation","capability","error"])
    v.add_argument("file")
    args = p.parse_args()
    if args.command == "schema":
        document = json.load(open(args.file, encoding="utf-8"))
        errors = validate_document(args.kind, document)
        if errors:
            print(json.dumps({"valid": False, "errors": errors}, indent=2))
            return 1
        print(json.dumps({"valid": True}, indent=2))
        return 0
    return 2
