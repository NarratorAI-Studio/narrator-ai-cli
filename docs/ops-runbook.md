# 运维管理员手册

> **更新频率**：on infra / pipeline / deploy change
> **同步源**：`NarratorAI-Studio/narrator-ai-cli/docs/ops-runbook.md`
> **owner**：@zhaojunlucky @lxjmaster

## TL;DR

narrator-ai-cli 运行时依赖 narrator-ai backend（FastAPI on GridLtd-ProductDev/open-fastapi）+ 模型 API（OpenRouter / Claude / TTS / 渲染服务）+ 飞书 OAuth + 百度网盘 API。CLI 本身轻量，主要依赖在后端。

## 1. 架构概览

TODO @zhaojunlucky —
```
narrator-ai-cli (用户机器)
    ↓ HTTPS
narrator-ai backend (GridLtd-ProductDev/open-fastapi on Fly.io / Aliyun)
    ↓
[LLM API / TTS API / 渲染队列 / Redis / Postgres]
    ↓
[百度网盘 / 飞书 OAuth / SMTP]
```

## 2. 部署 / 升级流程

TODO @zhaojunlucky — 参考 `GridLtd-BizDev/twenty-crm-deploy/docs/ops-runbook.md` 同款节奏。

## 3. 监控 + 告警

- CLI 端：`marketplace.json` 版本检查 + 用户报错统计
- 后端：Prometheus / Grafana (在 GridLtd-SecOps/monitoring-configs)
- 业务：飞书《电商记录表》bitable 月度对账漂移监测

## 4. 平台合规作业

- 抖音 AI 标识合规：详见 `NarratorAI-Studio/ecommerce-listing/docs/02 §5 备用条款`
- 国家《人工智能生成合成内容标识办法》(2025-09-01)：当前不强制人工质保服务，但备用条款触发条件由 @Sylvia7799 季度 review
- 多账号风控：每店独立 IP / 设备指纹 / 浏览器配置；详见 ecommerce-listing docs/02 §3

## 5. 故障升级 + 复盘流程

TODO @zhaojunlucky —
- 24h 内复盘归档对应 Issue
- 是否升级 ADR 由 @lxjmaster 判断
- 与 GridLtd-SecOps 协同 on-call

## 6. 数据备份

TODO @zhaojunlucky —
- Postgres / Redis 备份周期
- 飞书 bitable 数据导出周期
- 用户素材 retention 政策（订单完结 7 天后清理）

## 7. 凭据轮换

凭据治理见 `dependencies.md` + Memory `reference_oas_rotation_runbook.md`。

## 相关链接

- [开发者集成 & 发版说明](./developer-integration.md)
- [第三方依赖治理](./dependencies.md)
- [FinOps 物料成本对账](./finops.md)

---

*Auto-synced from `NarratorAI-Studio/narrator-ai-cli/docs/ops-runbook.md`.*
