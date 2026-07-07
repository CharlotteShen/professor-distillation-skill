# Professor Distillation Skill

[English](README.md) | [简体中文](README.zh-CN.md)

A public, local-first skill for helping research students build a citation-grounded knowledge workflow around a professor's research corpus.

The skill is Codex-native through `professor-distillation/SKILL.md`, but it is plain Markdown so Claude Code and other coding agents can use the same workflow through `AGENTS.md` or `CLAUDE.md`.

## What This Is

- A workflow guide for private, local professor-corpus distillation.
- A safety contract for evidence-backed claims, retrieval, synthesis, manuscript critique, and meeting prep.
- Starter templates and a synthetic subagent demo only.
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
- `professor-distillation/references/agent-roles.md`
- `professor-distillation/references/demo-subagents.md`

## Questions And Answers

### What can this skill help me build?

It helps you build a private, local-first workflow for turning a professor's papers, theses, notes, and related materials into citation-grounded evidence records, synthesis notes, research-gap ideas, manuscript critiques, and meeting-prep packets.

### Can it analyze my professor's papers?

Yes, but the analysis should happen in your own private workspace. This public repo only provides the workflow and synthetic templates; it does not include real papers or extracted text.

### Does it use private or non-OA data?

No. The public skill contains no corpus data. If your private workspace includes licensed or non-open-access papers, keep those files, extracted text, notes, and generated claims out of public repos.

### Can it prepare meeting notes?

Yes. The workflow guides agents to prepare evidence-backed meeting briefs, likely questions, answer bullets, and do-not-overclaim cautions from your local corpus.

### Does it impersonate the professor?

No. The skill explicitly forbids impersonation and private-knowledge claims. It organizes local evidence so you can reason about patterns, gaps, and meeting questions responsibly.

### Does it require OpenAI API, RAG, or vector search?

No. The baseline is local and deterministic: Markdown, CSV, JSON/JSONL, SQLite, and page-grounded evidence. You can add other tools privately, but they are not required by this public skill.

### Can Claude Code or other agents use it?

Yes. Codex can load `professor-distillation/SKILL.md` as a skill. Claude Code and other agents can follow `AGENTS.md`, `CLAUDE.md`, and the same Markdown reference files.


### Why do subagents need enough digested papers?

A one-paper workspace can support paper-level analysis and cautious evidence lookup, but cross-paper synthesis, gap generation, manuscript critique, and meeting prep need multiple page-grounded records. The public demo labels readiness as `starter`, `usable`, or `strong` so agents do not overclaim from a thin corpus.

### What should never be committed?

Never commit PDFs, extracted page text, EndNote libraries or exports, private notes, real claim records, generated outputs, API keys, local paths, or any copyrighted/non-open-access source text.

## Release Gate

Before publishing or sharing a derivative repo, run:

```bash
python3 scripts/quick_validate.py professor-distillation
python3 scripts/privacy_audit.py .
git ls-files
```

The audit is intentionally conservative. If it flags a file, remove or rewrite the file before publishing.
