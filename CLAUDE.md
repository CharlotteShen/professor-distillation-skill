# Claude Code Instructions

This repo publishes a reusable professor-distillation workflow. It must stay public-safe.

Follow `professor-distillation/SKILL.md` as the primary workflow. Use the reference files for details. Never add private corpora, PDFs, extracted text, EndNote files, secrets, local absolute paths, or generated research outputs.

For any implementation or release change, run:

```bash
python3 scripts/quick_validate.py professor-distillation
python3 scripts/privacy_audit.py .
```

If either command reports findings, fix them before committing or publishing.
