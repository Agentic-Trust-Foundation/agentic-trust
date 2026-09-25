# ATF V2 Final Go Conformance Verifier

This is an independent Go implementation of the structural conformance checks for ATF V2 phases 35-42.

It intentionally does not import the Python contract runner. It reads the canonical JSON contracts from `conformance/v2/phase-*` and independently validates:

- phase and protocol version
- declared rules versus vectors
- decision vocabulary
- mandatory fail-closed negative vector

Run from the repository root:

```sh
go run ./reference/implementation/go/v2-final-conformance
```
