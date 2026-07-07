# 教授研究蒸馏 Skill

[English](README.md) | [简体中文](README.zh-CN.md)

这是一个公开的、本地优先的 skill，用来帮助研究生围绕某位教授的研究语料建立有引用依据的知识整理流程。

这个 skill 通过 `professor-distillation/SKILL.md` 原生支持 Codex；同时它全部使用普通 Markdown 编写，因此 Claude Code 和其他代码代理也可以通过 `AGENTS.md` 或 `CLAUDE.md` 使用同一套流程。

## 10 分钟开始

```bash
git clone https://github.com/CharlotteShen/professor-distillation-skill.git
cd professor-distillation-skill
mkdir -p ~/.codex/skills
cp -R professor-distillation ~/.codex/skills/
mkdir -p ~/professor-distillation-workspace
cp -R professor-distillation/assets/templates/* ~/professor-distillation-workspace/
```

可选的、已验证的 Codex Skills CLI 安装方式：

```bash
npx --yes skills add CharlotteShen/professor-distillation-skill --skill professor-distillation --global --agent codex
```

然后在你的私有工作区打开 Codex，并从这个 prompt 开始：

```text
Use the professor-distillation skill to help me set up a private professor research workspace. Start by inspecting the templates and asking what PDFs, DOI list, EndNote export, or metadata I already have. Do not copy private corpus files into this public repo.
```

## 前置条件

- 基础流程不需要 OpenAI API key。
- 不需要向量数据库、RAG 技术栈或外部服务。
- Python 3 只用于运行验证脚本和隐私审计脚本。
- 如果要做真实语料分析，你需要自己的私有 PDF、元数据、DOI 列表或 EndNote 导出。
- 授权文献或非开放获取材料必须留在私有工作区中。

## 兼容性

| 运行环境 | 使用方式 |
| --- | --- |
| Codex | 手动：把 `professor-distillation/` 复制到 `~/.codex/skills/`。CLI：`npx --yes skills add CharlotteShen/professor-distillation-skill --skill professor-distillation --global --agent codex`。 |
| Codex 项目工作区 | 在私有工作区中运行 `npx --yes skills add CharlotteShen/professor-distillation-skill --skill professor-distillation`；它会安装到 `./.agents/skills/professor-distillation`。 |
| Claude Code | 让代理读取本仓库，并遵循 `CLAUDE.md`；不要依赖尚未验证的 Claude 专用 CLI 参数。 |
| 其他代码代理 | 让代理读取 `AGENTS.md` 和 `professor-distillation/SKILL.md`；只有在你的代理支持时，才使用项目内 `.agents/skills/`。 |

避免不带 `--agent codex` 的 `skills add ... --global`：它会安装 skill，但可能对不支持全局安装的运行环境打印警告。

## 这是什么

- 面向私有教授语料库的工作流指南。
- 用于证据型 claim、检索、综合、稿件评审和组会准备的安全约束。
- 只包含合成示例的入门模板和 subagent 演示。
- 一个隐私审计门禁，用来避免泄露个人信息、私有材料或非开放获取文献内容。

## 这不是什么

- 不是数据集。
- 不包含论文、笔记、抽取文本或 EndNote 导出。
- 不是 RAG 或向量检索系统。
- 不是教授人格模拟。
- 不是关于版权或机构政策的法律建议。

## 在 Codex 中安装

可以使用手动安装，也可以使用已验证的 Skills CLI 命令。手动安装会复制到经典 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R professor-distillation ~/.codex/skills/
```

已验证的 CLI 安装会面向 Codex 做全局安装，并安装到 `~/.agents/skills/`：

```bash
npx --yes skills add CharlotteShen/professor-distillation-skill --skill professor-distillation --global --agent codex
```

如果只想在一个私有项目中使用，请在该私有工作区中运行：

```bash
npx --yes skills add CharlotteShen/professor-distillation-skill --skill professor-distillation
```

之后可以要求 Codex 使用 `professor-distillation` 来搭建或运行本地教授研究蒸馏流程。

## 在 Claude Code 或其他代理中使用

Claude Code 请让代理读取本仓库并遵循 `CLAUDE.md`；其他代码代理请使用 `AGENTS.md` 和 `professor-distillation/SKILL.md`。实际工作流在这些文件中：

- `professor-distillation/SKILL.md`
- `professor-distillation/references/workflow.md`
- `professor-distillation/references/evidence-contract.md`
- `professor-distillation/references/privacy-and-release.md`
- `professor-distillation/references/agent-roles.md`
- `professor-distillation/references/demo-subagents.md`

## 术语表

- `skill`：一组可被代理加载的 Markdown 指令和可选资源，用于特定工作流。
- `corpus`：你想蒸馏的私有论文、学位论文、笔记、元数据和相关记录集合。
- `claim record`：带来源、位置、置信度和抽取质量的结构化证据陈述。
- `doc_id`：一篇文档的稳定本地标识，避免依赖文件名。
- `JSONL`：每一行都是一个 JSON 对象的文件格式，适合追加式记录。
- `extraction quality`：对抽取文本可信度的标记，用来约束后续 claim。
- `visual gate`：对公式、表格或图片级 claim 先做视觉核验的规则。
- `retrieval miss`：检索没有命中，不能当作证据不存在的证明。
- `subagent`：面向特定分析角色的可复用提示卡，不是自主事实来源。
- `private workspace`：保存真实语料和输出的本地非公开项目文件夹。

## 常见问答

### 这个 skill 能帮我搭建什么？

它可以帮助你在私有工作区中，把教授的论文、学位论文、笔记和相关材料整理成有引用依据的证据记录、综合笔记、研究 gap、稿件评审意见和组会准备材料。

### 它能分析我导师或教授的论文吗？

可以，但分析应当发生在你自己的私有工作区中。这个公开仓库只提供工作流和合成模板，不包含真实论文或抽取文本。

### 它会使用私有数据或非开放获取文献吗？

不会。公开 skill 不包含任何语料数据。如果你的私有工作区中有授权文献或非开放获取论文，请不要把原文、抽取文本、笔记或 claim 记录发布到公开仓库。

### 它能准备组会材料吗？

可以。该流程会指导代理基于本地证据准备组会 brief、可能的问题、回答要点以及不要过度声称的提醒。

### 它会模仿教授本人吗？

不会。这个 skill 明确禁止人格模拟和私有知识声称。它只帮助你组织本地证据，并谨慎分析研究模式、潜在 gap 和组会问题。

### 它需要 OpenAI API、RAG 或向量检索吗？

不需要。基础流程是本地、确定性的：Markdown、CSV、JSON/JSONL、SQLite 和页码级证据。你可以在私有项目中自行扩展其他工具，但公开 skill 不依赖它们。

### Claude Code 或其他代理也能用吗？

可以。Codex 可以把 `professor-distillation/SKILL.md` 作为 skill 加载。Claude Code 和其他代理可以读取 `AGENTS.md`、`CLAUDE.md` 以及同一组 Markdown 参考文件。

### 为什么 subagent 需要足够多已经消化的论文？

只有一篇论文时，工作区最多支持单篇分析和谨慎检索；跨论文综合、研究 gap、稿件评审和组会准备需要多条页码级证据记录。公开 demo 用 `starter`、`usable`、`strong` 标记成熟度，避免代理从过薄语料中过度推断。

### 哪些内容绝对不能提交？

不要提交 PDF、抽取后的页面文本、EndNote 库或导出、私有笔记、真实 claim 记录、生成的 outputs、API key、本地路径，或任何受版权保护/非开放获取的原文片段。

## 安全和贡献

报告隐私敏感问题前请先读 `SECURITY.md`，提交 PR 前请先读 `CONTRIBUTING.md`。示例和 demo 必须保持合成数据。

## 发布门禁

发布或分享衍生仓库前，运行：

```bash
python3 scripts/quick_validate.py professor-distillation
python3 scripts/privacy_audit.py .
git ls-files
```

审计脚本会故意保守。如果它标记了某个文件，请先删除或重写该文件，再发布。
