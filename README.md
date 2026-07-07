# Professor Distillation Skill

[English](README.md) | [简体中文](README.zh-CN.md)

A public, local-first skill for helping research students build a citation-grounded knowledge workflow around a professor's research corpus.

The skill is Codex-native through `professor-distillation/SKILL.md`, but it is plain Markdown so Claude Code and other coding agents can use the same workflow through `AGENTS.md` or `CLAUDE.md`.

## Start Here In 10 Minutes

```bash
git clone https://github.com/CharlotteShen/professor-distillation-skill.git
cd professor-distillation-skill
mkdir -p ~/.codex/skills
cp -R professor-distillation ~/.codex/skills/
mkdir -p ~/professor-distillation-workspace
cp -R professor-distillation/assets/templates/* ~/professor-distillation-workspace/
```

Optional verified Codex install with Skills CLI:

```bash
npx --yes skills add CharlotteShen/professor-distillation-skill --skill professor-distillation --global --agent codex
```

Then open Codex in your private workspace and start with:

```text
Use the professor-distillation skill to help me set up a private professor research workspace. Start by inspecting the templates and asking what PDFs, DOI list, EndNote export, or metadata I already have. Do not copy private corpus files into this public repo.
```

## Prerequisites

- No OpenAI API key is required for the baseline workflow.
- No vector database, RAG stack, or external service is required.
- Python 3 is only needed for validation and privacy-audit scripts.
- Corpus-specific analysis needs your own private PDFs, metadata, DOI list, or EndNote export.
- Licensed or non-open-access source material must stay in your private workspace.

## Compatibility

| Runtime | How to use |
| --- | --- |
| Codex | Manual: copy `professor-distillation/` to `~/.codex/skills/`. CLI: `npx --yes skills add CharlotteShen/professor-distillation-skill --skill professor-distillation --global --agent codex`. |
| Codex project workspace | From the private workspace, run `npx --yes skills add CharlotteShen/professor-distillation-skill --skill professor-distillation`; it installs to `./.agents/skills/professor-distillation`. |
| Claude Code | Point the agent at this repo and follow `CLAUDE.md`; do not rely on unverified Claude-specific CLI flags. |
| Other coding agents | Point the agent at `AGENTS.md` and `professor-distillation/SKILL.md`, or use project-local `.agents/skills/` only if your agent supports it. |

Avoid `skills add ... --global` without `--agent codex`: it installs the skill but can print agent-specific warnings for runtimes that do not support global installs.

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

Use either manual install or the verified Skills CLI command. Manual install copies into the classic Codex skills folder:

```bash
mkdir -p ~/.codex/skills
cp -R professor-distillation ~/.codex/skills/
```

The verified CLI install targets Codex globally and installs under `~/.agents/skills/`:

```bash
npx --yes skills add CharlotteShen/professor-distillation-skill --skill professor-distillation --global --agent codex
```

For one private project only, run this from that private workspace instead:

```bash
npx --yes skills add CharlotteShen/professor-distillation-skill --skill professor-distillation
```

Then ask Codex to use `professor-distillation` when setting up or operating a local professor distillation workflow.

## Use With Claude Code Or Other Agents

For Claude Code, point the agent at this repository and ask it to follow `CLAUDE.md`. For other coding agents, use `AGENTS.md` plus `professor-distillation/SKILL.md`. The actual workflow lives in:

- `professor-distillation/SKILL.md`
- `professor-distillation/references/workflow.md`
- `professor-distillation/references/evidence-contract.md`
- `professor-distillation/references/privacy-and-release.md`
- `professor-distillation/references/agent-roles.md`
- `professor-distillation/references/demo-subagents.md`

## Glossary

- `skill`: A folder of Markdown instructions and optional resources that an agent can load for a specific workflow.
- `corpus`: The private set of papers, theses, notes, metadata, and related records you want to distill.
- `claim record`: A structured evidence-backed statement with source, location, confidence, and extraction quality.
- `doc_id`: A stable local identifier for one document, used instead of relying on filenames.
- `JSONL`: A file format with one JSON object per line, useful for append-only records.
- `extraction quality`: A label for how trustworthy the extracted text is for downstream claims.
- `visual gate`: A rule requiring visual verification before making equation-, table-, or figure-level claims.
- `retrieval miss`: A failed search result that should not be treated as proof the evidence does not exist.
- `subagent`: A reusable role-card prompt for focused analysis, not an autonomous source of truth.
- `private workspace`: Your local, non-public project folder where real corpus files and outputs stay.

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

## Security And Contributions

Read `SECURITY.md` before reporting privacy-sensitive issues, and `CONTRIBUTING.md` before opening a PR. Examples and demos must stay synthetic.

## Release Gate

Before publishing or sharing a derivative repo, run:

```bash
python3 scripts/quick_validate.py professor-distillation
python3 scripts/privacy_audit.py .
git ls-files
```

The audit is intentionally conservative. If it flags a file, remove or rewrite the file before publishing.
