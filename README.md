# Professor Distillation Skill

A public, local-first skill for helping research students build a citation-grounded knowledge workflow around a professor's research corpus.

The skill is Codex-native through `professor-distillation/SKILL.md`, but it is plain Markdown so Claude Code and other coding agents can use the same workflow through `AGENTS.md` or `CLAUDE.md`.

## What This Is

- A workflow guide for private, local professor-corpus distillation.
- A safety contract for evidence-backed claims, retrieval, synthesis, manuscript critique, and meeting prep.
- Starter templates with synthetic examples only.
- A privacy audit gate to prevent leaking personal, private, or non-open-access corpus data.

## What This Is Not

- Not a dataset.
- Not a collection of papers, notes, extracted text, or EndNote exports.
- Not a RAG/vector system.
- Not professor impersonation.
- Not legal advice about copyright or institutional policy.

## Install For Codex

Copy or symlink the skill folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R professor-distillation ~/.codex/skills/
```

Then ask Codex to use `professor-distillation` when setting up or operating a local professor distillation workflow.

## Use With Claude Code Or Other Agents

Point the agent at this repository and ask it to follow `AGENTS.md` or `CLAUDE.md`. The actual workflow lives in:

- `professor-distillation/SKILL.md`
- `professor-distillation/references/workflow.md`
- `professor-distillation/references/evidence-contract.md`
- `professor-distillation/references/privacy-and-release.md`

## Release Gate

Before publishing or sharing a derivative repo, run:

```bash
python3 scripts/quick_validate.py professor-distillation
python3 scripts/privacy_audit.py .
git ls-files
```

The audit is intentionally conservative. If it flags a file, remove or rewrite the file before publishing.
