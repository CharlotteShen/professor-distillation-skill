# Contributing

Keep contributions public-safe and small.

- Use synthetic examples only.
- Do not add real corpora, private notes, DOI-derived copied text, PDFs, EndNote exports, secrets, or local absolute paths.
- Keep `professor-distillation/SKILL.md` concise and agent-facing.
- Put detailed workflow guidance in `professor-distillation/references/`.
- Run validation and privacy audit before opening a PR.

```bash
python3 scripts/quick_validate.py professor-distillation
python3 scripts/privacy_audit.py .
git ls-files
```
