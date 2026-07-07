# Security Policy

This repository is privacy-sensitive because users apply it to private research corpora.

Report security or privacy issues through GitHub private vulnerability reporting if it is enabled, or through a private channel chosen by the maintainer. Do not include sensitive material in public issues or pull requests.

Never post real PDFs, extracted text, EndNote libraries or exports, API keys, private notes, local absolute paths, or professor-specific private records in this public repo.

See `professor-distillation/references/privacy-and-release.md` for the release rules.

Before opening a PR, run:

```bash
python3 scripts/quick_validate.py professor-distillation
python3 scripts/privacy_audit.py .
git ls-files
```
