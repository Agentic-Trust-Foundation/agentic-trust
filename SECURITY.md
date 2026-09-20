# Security Policy

## Scope

This policy covers the Agentic Trust Foundation repository and its reference protocol artifacts and implementations.

## Reporting a vulnerability

Do not open a public GitHub issue for an undisclosed security vulnerability. Use GitHub's private vulnerability reporting/security advisory mechanism when available, or contact the repository maintainers through the private security contact configured for this project.

Please include:

- affected component and version/commit;
- reproduction steps or a minimal proof of concept;
- security impact;
- relevant logs or traces with secrets removed.

Do not include credentials, private keys, tokens, or unnecessary personal data.

## Security design expectations

The project treats identity, delegation, authorization, policy, revocation, provenance, auditability, and human approval as security-sensitive. Security claims should be backed by tests, conformance vectors, or explicit documented limitations.

The reference implementation is not a production trust service merely because it conforms to the protocol. Deployment-specific threat modeling, key management, monitoring, and operational controls remain required.
