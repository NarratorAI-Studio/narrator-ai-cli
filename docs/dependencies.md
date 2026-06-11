# 第三方依赖治理

> **更新频率**：on dependency add / remove / version pin / vendor change
> **同步源**：`NarratorAI-Studio/narrator-ai-cli/docs/dependencies.md`
> **owner**：@zhaojunlucky @lxjmaster

## TL;DR

narrator-ai-cli + backend 依赖以下第三方服务：LLM (OpenRouter / Claude) / TTS / 渲染队列 / Postgres / Redis / 飞书 OAuth / 百度网盘 / SMTP。每个依赖都需要 fallback + 凭据轮换。

## 1. 依赖清单

| 依赖 | 用途 | Primary | Backup | 凭据存放 | 治理负责人 |
|------|------|---------|--------|---------|----------|
| LLM | 解说稿生成 | OpenRouter (Claude / GPT) | Anthropic direct | Infisical | @lxjmaster |
| TTS | 配音合成 | TODO 主流 TTS 服务 | TODO | Infisical | @4mYHime |
| 视频渲染 | 视频合成 | 自建队列 | TODO | Fly.io | @zhaojunlucky |
| Postgres | 任务 + 用户数据 | Fly.io managed | TODO 备份导出 | flyctl secrets | @zhaojunlucky |
| Redis | 队列 + 缓存 | Fly.io self-hosted | TODO | flyctl secrets | @zhaojunlucky |
| 飞书 OAuth | 用户登录 | Lark/Feishu | TODO | Infisical | @lxjmaster |
| 百度网盘 | 成品交付 | 百度 | TODO 网盘备份 | Infisical | @candytan889 |
| SMTP | 邮件交付 | Stalwart on Fly.io | TODO | Infisical | @zhaojunlucky |
| Twenty CRM | 客户档案 | GridLtd-BizDev/twenty-crm-deploy | N/A | keychain | @KYBvWHxW |

## 2. 凭据轮换

详见 Memory `reference_oas_rotation_runbook.md` + `feedback_credential_overgrant.md`（DO PAT / GitHub PAT 等 issue-once-immutable 凭据，配 scope 宁多勿少）。

季度由 @zhaojunlucky 跑一次全量凭据 audit。

## 3. 版本固定

`pyproject.toml` 主要依赖：
TODO @pluckhuang — pinned version 表，版本升级影响评估

GitHub Actions third-party：必须 pin 到 40-char commit SHA，不用 mutable tag。详见 org-rules.md。

## 4. 供应商风险评估

| 风险维度 | 当前评估 | 缓解 |
|---------|---------|------|
| 单一 LLM 供应商风险 | OpenRouter 已聚合多家 | ✅ |
| TTS 单一供应商 | TODO | 评估备份 |
| Fly.io 单 region | sin region | 备份导出周期内 |
| 百度网盘 API 政策变化 | 中等 | 准备 alt 网盘备份 |

## 5. 引入新依赖的流程

TODO @lxjmaster —
1. 在 project-hub 开 RFC Issue 评估
2. 安全 review by @Sylvia7799 + @security_expert agent
3. 凭据治理 by @zhaojunlucky
4. PR 含本文档更新
5. ADR 归档（如适用）

## 6. 已弃用依赖

TODO @pluckhuang — 历史替换记录（vendor migration / lib 替换 等）。

## 相关链接

- [运维管理员手册](./ops-runbook.md)
- [开发者集成](./developer-integration.md)
- [oas 轮换 runbook (memory)](../../reference_oas_rotation_runbook.md)

---

*Auto-synced from `NarratorAI-Studio/narrator-ai-cli/docs/dependencies.md`.*
