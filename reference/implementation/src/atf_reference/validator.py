from pathlib import Path
import json
import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[4]
SCHEMA_DIR = ROOT / "schemas" / "v1"
VECTOR_FILE = ROOT / "test-vectors" / "v1" / "core.yaml"

SCHEMA_MAP = {
    "authorization-request": "authorization-request.schema.json",
    "authorization-decision": "authorization-decision.schema.json",
    "delegation": "delegation.schema.json",
    "capability": "capability.schema.json",
    "error": "error.schema.json",
}

def validate_document(kind: str, document: dict) -> list[str]:
    if kind not in SCHEMA_MAP:
        raise ValueError(f"unsupported schema kind: {kind}")
    schema = json.loads((SCHEMA_DIR / SCHEMA_MAP[kind]).read_text())
    errors = sorted(Draft202012Validator(schema).iter_errors(document), key=lambda e: list(e.path))
    return [e.message for e in errors]

def load_core_vectors() -> dict:
    return yaml.safe_load(VECTOR_FILE.read_text())
