# 高并发批量指南

> **更新频率**：on each pipeline / rate-limit / SLA change
> **同步源**：`NarratorAI-Studio/narrator-ai-cli/docs/batch-processing.md`
> **owner**：@4mYHime @ShawYu19

## TL;DR

narrator-ai-cli 单批默认上限 5 个视频/任务，超出需协商加急或拆单。约束来自人工核对工时 + 服务器渲染并发，**不是** LLM API rate limit。

## 1. 单批上限的真实理由

| 约束维度 | 实际瓶颈 |
|---------|---------|
| 人工核对工时 | 测试人员 (@ShawYu19) 单批审核工时随数量线性上升；> 5 个会跑出 SLA |
| 渲染并发 | 后端渲染队列稳定 SLA 在 5 并发以下；超过会出现单任务超期 |
| LLM API rate | 当前 OpenRouter / 备份 API 余量充足，**不是瓶颈** |
| TTS 合成 | 主流 TTS 服务在 5 并发以下稳定 |

⚠️ 客户问起为什么单批限 5：按 sku.yaml 的服务能力声明，**不要说 AI rate limit**（与商品定位冲突）。说「人工核对 + 渲染并发约束」。

## 2. 批量任务的标准流程

TODO @4mYHime —
1. 用户在 CLI 调起 `narrator-ai-cli batch --config batch.yml`
2. 后端收到批量任务，拆分为单任务 + 排队
3. 单任务并发上限 ≤ 5
4. 完成后批量打包到百度网盘
5. 测试人员审核 → 平台内回包

## 3. 超过 5 单的处理

- **加急档**：协商加急费用 + 加大并发（需 ops 审批）
- **拆单**：协商分次交付（推荐）
- **B 端走 contract**：> 50 单 / 月走 B 端报价（@823319233-wq）

## 4. 故障处理

### 部分成功部分失败

| 失败原因 | 处理 |
|---------|------|
| 单任务 LLM API timeout | 自动重试 1 次；仍失败则人工介入 |
| 渲染队列拥堵 | 自动延后；不计入 SLA 计时（用户透明） |
| 客户素材问题（缺帧 / 编码错） | 立即停批 + 通知客户补素材 |
| 后端服务异常 | 立即停批 + escalate @lxjmaster |

### 全批失败

TODO @4mYHime — 退款触发条件 + 沟通话术。

## 5. 监控指标

- 平均单批耗时（基线 < 24h）
- 单批成功率（target > 95%）
- 测试人员审核单批工时
- 客户重做请求率

## 6. 容量规划

TODO @zhaojunlucky + @lxjmaster — 季度容量预估 + 渲染服务器扩缩容触发条件。

## 相关链接

- [运维管理员手册](./ops-runbook.md)
- [进阶用户技巧](./advanced-tips.md)
- [FinOps 物料成本对账](./finops.md)

---

*Auto-synced from `NarratorAI-Studio/narrator-ai-cli/docs/batch-processing.md`.*
