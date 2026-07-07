# Privacy And Release Gate

## Never Publish

Do not publish:

- PDFs or scans
- extracted page text
- EndNote `.enl`, `.ris`, `.bib`, or attachment exports
- real paper notes or thesis notes
- real claim, method, equation, gap, style, or meeting records
- generated outputs
- SQLite indexes
- API keys, MinerU keys, tokens, cookies, or `.env` files
- private absolute paths or machine-local config
- professor-specific private handoffs
- non-open-access text snippets or copied passages

## Safe To Publish

Usually safe:

- generic workflow instructions
- empty templates
- synthetic examples written from scratch
- no-dependency helper scripts
- privacy audit scripts
- CI configuration that validates the public repo

## Release Checklist

Before first push or public release:

1. Start from a fresh repo with no private git history.
2. Run `git ls-files` and inspect every tracked path.
3. Run `python3 scripts/quick_validate.py professor-distillation`.
4. Run `python3 scripts/privacy_audit.py .`.
5. Confirm examples are synthetic and not adapted from private or non-open-access papers.
6. Confirm no source text, page text, PDFs, or reference-manager files are tracked.
7. Tag a release only after the audit is clean.
