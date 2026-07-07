# 教授研究蒸馏 Skill

[English](README.md) | [简体中文](README.zh-CN.md)

这是一个公开的、本地优先的 skill，用来帮助研究生围绕某位教授的研究语料建立有引用依据的知识整理流程。

这个 skill 通过 `professor-distillation/SKILL.md` 原生支持 Codex；同时它全部使用普通 Markdown 编写，因此 Claude Code 和其他代码代理也可以通过 `AGENTS.md` 或 `CLAUDE.md` 使用同一套流程。

## 这是什么

- 面向私有教授语料库的工作流指南。
- 用于证据型 claim、检索、综合、稿件评审和组会准备的安全约束。
- 只包含合成示例的入门模板。
- 一个隐私审计门禁，用来避免泄露个人信息、私有材料或非开放获取文献内容。

## 这不是什么

- 不是数据集。
- 不包含论文、笔记、抽取文本或 EndNote 导出。
- 不是 RAG 或向量检索系统。
- 不是教授人格模拟。
- 不是关于版权或机构政策的法律建议。

## 在 Codex 中安装

把 skill 文件夹复制或软链接到 Codex skills 目录：

```bash
mkdir -p ~/.codex/skills
cp -R professor-distillation ~/.codex/skills/
```

之后可以要求 Codex 使用 `professor-distillation` 来搭建或运行本地教授研究蒸馏流程。

## 在 Claude Code 或其他代理中使用

让代理读取本仓库，并遵循 `AGENTS.md` 或 `CLAUDE.md`。实际工作流在这些文件中：

- `professor-distillation/SKILL.md`
- `professor-distillation/references/workflow.md`
- `professor-distillation/references/evidence-contract.md`
- `professor-distillation/references/privacy-and-release.md`

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

### 哪些内容绝对不能提交？

不要提交 PDF、抽取后的页面文本、EndNote 库或导出、私有笔记、真实 claim 记录、生成的 outputs、API key、本地路径，或任何受版权保护/非开放获取的原文片段。

## 发布门禁

发布或分享衍生仓库前，运行：

```bash
python3 scripts/quick_validate.py professor-distillation
python3 scripts/privacy_audit.py .
git ls-files
```

审计脚本会故意保守。如果它标记了某个文件，请先删除或重写该文件，再发布。
