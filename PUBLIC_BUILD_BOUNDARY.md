# Public Build Boundary

This repository is the **sanitized public Research Lab build**.

The private execution environment is **this working chat/private runtime plus the operator's already-held local/Drive credential stores and other private connected resources when accessible here**. It is not another GitHub repository and it is not a public branch.

The public repository must remain independently launchable without the operator's private API keys.

## Private execution environment

The private side may use, when actually accessible to the working runtime:

- provider credentials already held in the operator's local/Drive stores;
- the three Nemotron Ultra Titan seats;
- the operator-selected dedicated math-model seat;
- OmniRoute/OpenCode routing;
- private donor repositories;
- private datasets and working files;
- temporary execution receipts and intermediate analysis.

Raw credential values are never copied into the public repository.

## Public build includes

- deterministic laboratory interfaces and schemas;
- derivation ledgers and scientific-status boundaries;
- matrix/tensor attack specifications;
- public or publication-authorized visualization donors;
- public dataset adapters and provenance;
- receipts and reproducibility artifacts;
- keyless adapters/fixtures for model-routing interfaces where needed;
- sanitized outputs from private execution;
- Zenodo publication package.

## Public build excludes

- raw API keys or tokens;
- private donor source not authorized for publication;
- secret-bearing logs;
- private provider account state;
- credentialed Titan runtime state;
- private local/Drive paths or artifacts that are not approved for publication.

## Export contract

The private execution environment may export validated, sanitized, receipt-bound artifacts into this repository.

Export is one-way:

```text
PRIVATE CHAT / LOCAL-DRIVE EXECUTION
                |
                | sanitize + verify + receipt
                v
PUBLIC RESEARCH LAB REPOSITORY
```

The public repository must not require access to the operator's private credential stores or private donor repositories to reproduce the public scientific artifacts it publishes.

## Publication rule

Anything prepared for GitHub release or Zenodo must pass:

1. secret scan;
2. donor/provenance check;
3. public-license/permission check;
4. removal of private paths/account state;
5. reproducibility check in keyless/public mode;
6. checksum and release manifest generation.
