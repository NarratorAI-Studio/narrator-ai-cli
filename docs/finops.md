# 物料成本对账 FinOps

> **更新频率**：每月对账周期 + 物料成本结构变化
> **同步源**：`NarratorAI-Studio/narrator-ai-cli/docs/finops.md`
> **owner**：@candytan889 @Fiona-Operator

## TL;DR

narrator-ai-cli 的物料成本拆分为 4 类：LLM API token / TTS 合成费 / 视频渲染编码费 / 人工核对工时。月度对账走《电商记录表》bitable 为真源，跨 5 平台收入归集 + 跨服务商成本拆分。

## 1. 物料成本结构

| 成本项 | 单位 | 来源 | bitable 字段 |
|--------|------|------|--------------|
| LLM token | 每 1k tokens | OpenRouter / 备份 | `消耗点数` |
| TTS 合成 | 每秒音频 | 主流 TTS | `成品视频费用` |
| 视频渲染 / 编码 | 每分钟 | 后端渲染队列 | `成品视频费用` |
| 人工核对工时 | 每订单 | 测试人员人天 | （隐含在毛利计算）|
| 第三方 OCR / 解析 | 每订单 | 服务商 | `解析费` |

## 2. 月度对账流程

TODO @candytan889 + @Fiona-Operator —
1. 月初拉《电商记录表》bitable 全月订单数据
2. 跨 5 平台收入归集（按 `渠道` + `操作平台` 字段）
3. 物料成本对账（LLM 账单 / TTS 账单 / 渲染队列报表）
4. 计算毛利率（target 35-55%）
5. 异常订单复盘（成本超阈值 / 退款 / 投诉）
6. 同步飞书《财务月报》文档

## 3. 税务穿透合规

国务院令第 810 号《互联网平台企业涉税信息报送规定》2025-10 已落地：
- 淘宝 / 抖音 / 拼多多 / 微信 / 快手 5 平台按季度报送商户身份与收入
- 详见 `NarratorAI-Studio/ecommerce-listing/docs/01 §5` + Issue [#18 公司主体升级](https://github.com/NarratorAI-Studio/ecommerce-listing/issues/18)

## 4. 平台抽佣率追踪

| 平台 | 抽佣率 | 时效 |
|------|--------|------|
| 闲鱼 | 鱼小铺 2025-04 + 2026-04 涨佣超 100% | 详见 ecommerce-listing docs/02 §2.1 |
| 淘宝 | ~5% 技术服务费 | 稳定 |
| 拼多多 | 6‰ 虚拟商品 | 稳定 |
| 小红书 | **0.6% 免佣窗口** | 2026-08-31 关闭 |
| 微信小店 | 1% / 100 万 GMV | 新商家 |

## 5. SKU 级毛利监测

按 `NarratorAI-Studio/ecommerce-listing/sku-blueprints/*/sku.yaml` 的 `material_cost.per_unit_rmb` 与 `pricing_tiers.*.unit_price_rmb` 计算单均毛利，月度更新 verification_log。

## 6. 异常告警

- 单 SKU 连续 3 个月毛利为负 → 进入 Portfolio 决策（Operating Model §sunset）
- 某平台毛利急降（> 1 标准差）→ docs/02 + finops 双 review

## 相关链接

- [运维管理员手册](./ops-runbook.md)
- [销售作战手册](./sales-playbook.md)
- [ecommerce-listing docs/01 §5 风险矩阵](https://github.com/NarratorAI-Studio/ecommerce-listing/blob/main/docs/01-service-commodity-fit-assessment.md)

---

*Auto-synced from `NarratorAI-Studio/narrator-ai-cli/docs/finops.md`.*
