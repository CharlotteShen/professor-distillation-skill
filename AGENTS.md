# Agent Instructions

Use this repository as a public workflow skill, not as a data repository.

- Start with `professor-distillation/SKILL.md`.
- Load reference files only when the current task needs them.
- Keep all user corpus material local and private.
- Do not commit PDFs, extracted page text, EndNote libraries/exports, real paper notes, private claims, secrets, or generated outputs.
- Every substantive research claim must cite local evidence with `doc_id`, page/location when available, evidence type, confidence, and extraction quality.
- Distinguish explicit evidence, pattern, inference, and speculation.
- Treat retrieval misses as misses, not evidence of absence.
- Do not impersonate a professor or claim private knowledge.
- Warn before using equation/table/figure claims unless the relevant source pages are visually verified.

Before publishing changes, run:

```bash
python3 scripts/quick_validate.py professor-distillation
python3 scripts/privacy_audit.py .
```
