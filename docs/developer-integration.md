# 开发者集成 & 发版说明

> **更新频率**：on each API change / version bump
> **同步源**：`NarratorAI-Studio/narrator-ai-cli/docs/developer-integration.md`
> **owner**：@pluckhuang @4mYHime

## TL;DR

narrator-ai-cli 是 narrator-ai 平台的 CLI 客户端。开发者可以：
1. 在 AI agent 中通过 MCP / skill 集成（推荐）
2. 直接调用 narrator-ai backend REST API
3. 嵌入 narrator-ai-cli 到自定义工作流

## 1. Endpoints

TODO @pluckhuang —
- backend base URL（prod / staging）
- 各 endpoint 用途与 schema
- 鉴权方式（API key 获取 + role）

## 2. AI Agent 集成

| Agent | 集成模式 | 仓库 |
|-------|---------|------|
| OpenClaw | 内置 skill | OpenAgentSystem |
| Windsurf | MCP server | TODO |
| WorkBuddy | CLI plugin | TODO |
| Claude Code | narrator-ai-cli-skill | https://github.com/NarratorAI-Studio/narrator-ai-cli-skill |
| Coze | coze_plugin/ | 本仓库根目录 |

## 3. CLI → 其他形态派生

按 operating model 原则：**所有派生形态必须直接由 CLI 转换**，最多加一层胶水代码。已有 / 在做的派生：

- **Gradio Web UI** — `NarratorAI-Studio/narrator-ai-gradio`
- **H5 / 飞书侧栏** — `GridLtd-ProductDev/narrator-ai-h5`
- **Coze 插件** — 本仓库 `coze_plugin/`
- **Claude Code skill** — `NarratorAI-Studio/narrator-ai-cli-skill`
- **官网集成** — `https-jieshuo.cn` (jieshuo.cn)
- **电商分销** — `NarratorAI-Studio/ecommerce-listing`（方法论 + SKU blueprint）

## 4. 版本号 + 发版

TODO @pluckhuang —
- semver 约定
- breaking change 处理
- pip 包发版流程
- changelog 维护

## 5. 版本变更日志

| 日期 | 版本 | 摘要 | PR |
|------|------|------|----|
| TODO | TODO | TODO | TODO |

## 6. CI / 自动化

| 自动化 | 状态 |
|--------|------|
| AI reviewer (oas-ai-reviewer) | ✅ (.github/workflows/ai-reviewer-gate.yml) |
| CI tests | ✅ (.github/workflows/ci.yml) |
| Lark docs sync | ✅ (.github/workflows/lark-docs-sync.yml) — 本 PR 引入 |
| Auto release on tag | TODO @zhaojunlucky |

## 相关链接

- [运维管理员手册](./ops-runbook.md)
- [第三方依赖治理](./dependencies.md)
- [narrator-ai-cli-skill](https://github.com/NarratorAI-Studio/narrator-ai-cli-skill)

---

*Auto-synced from `NarratorAI-Studio/narrator-ai-cli/docs/developer-integration.md`.*
