# Zenodo Release Checklist

Status: **HOLD until mathematical freeze and release metadata are operator-confirmed.**

## Required release contents

- source code snapshot;
- frozen derivation document;
- theory/assumption ledger;
- dataset manifest;
- raw-data provenance or stable external identifiers;
- transformation scripts;
- environment/dependency manifest;
- tests and receipts;
- checksums;
- README;
- CITATION.cff;
- codemeta.json;
- Zenodo metadata file;
- CHANGELOG;
- AUTHORS / contributor roles;
- license chosen explicitly by operator;
- release tag/version;
- archive manifest.

## Metadata audit

Do not copy prior draft metadata blindly.

Verify:
- title;
- creators and exact displayed names;
- ORCID(s), only if explicitly confirmed;
- affiliations, only if confirmed;
- description/abstract;
- version;
- publication date;
- resource type;
- keywords;
- related identifiers;
- GitHub URL;
- prior DOI/version relation;
- license;
- access rights;
- funding/grants only if real;
- communities only if intentionally selected.

## Current blocker

Creator identity formatting, ORCID, affiliation and license have not been confirmed in this build. They remain explicit HOLD fields rather than guessed metadata.

## Release integrity

Generate SHA-256 manifest after the final release tree is frozen. Zenodo upload package and Git tag must point to the same source state.
