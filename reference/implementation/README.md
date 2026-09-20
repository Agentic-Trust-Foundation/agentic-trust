# ATF V1 Reference Implementation

A small, modular Python reference implementation for the normative ATF Protocol V1.

## Scope

- JSON Schema validation for core V1 protocol objects
- deterministic authorization semantics
- loading the canonical V1 test-vector suite
- CLI validation

This implementation demonstrates protocol semantics; it is not a centralized trust service and does not define the protocol.

## Run

```bash
cd reference/implementation
python -m pip install -e .
pytest -q
```

CLI:

```bash
atf-validate schema authorization-request request.json
```

The implementation MUST remain replaceable and interoperable with independent implementations.
