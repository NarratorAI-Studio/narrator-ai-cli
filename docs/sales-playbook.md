# 销售作战手册

> **更新频率**：on each channel strategy / pricing change
> **同步源**：`NarratorAI-Studio/narrator-ai-cli/docs/sales-playbook.md`
> **owner**：@zaiye0 @823319233-wq @liushixuan55-create

## TL;DR

narrator-ai-cli 销售矩阵：B 端走 GridLtd-BizDev 销售人员定制 / C 端走电商平台 SKU 上架 + 内容种草 + 媒体矩阵。

## 1. 目标客户画像

TODO @zaiye0 —
- B 端：短剧出海 MCN / 影视解说工作室 / 自媒体 KOL 团队
- C 端：个人解说创作者 / 小型工作室 / 海外华人内容生产者

## 2. 渠道矩阵

| 渠道 | 流量 vs 变现 | 仓库 | 状态 |
|------|------------|------|------|
| 抖音内容种草 | 流量入口 | `leads-douyin` (lead capture) | 待 |
| 小红书内容种草 | 流量 + 变现 | `leads-xiaohongshu` + ecommerce-listing 小红书店 | 已上架 |
| 淘宝 / 闲鱼 / 拼多多 / 微信小店 | 变现 | ecommerce-listing 5 平台店 | 已上架 |
| YouTube / X / TikTok | 海外流量 | （待评估，海外暂不做）| 暂停 |
| 公众号 + 视频号 | 微信生态 | 待建 leads-公众号 | 待 |
| 知乎 / B 站 | 搜索 + 教程 | 待建 leads-zhihu / leads-bilibili | 待 |
| 主动外联 | B 端 | （narrator-ai-cli outbound 待建）| 待 |

## 3. 销售流程

按 `GridLtd-PMO/product-roadmap/phases/07-channels.md` 与 `09-outreach.md`：

```
渠道发现客户 → leads-* repo 建 issue（每客户一 issue + 标签）
            ↓
        Twenty CRM 双向同步（crm:twenty:synced）
            ↓
        销售对话 + 需求评估 + 打样
            ↓
        转化下单 → 订单进入电商记录表 bitable
            ↓
        履约 + 交付 + 售后
            ↓
        反馈进 project-hub → 客户复购 / 口碑
```

## 4. 报价策略

TODO @zaiye0 + @823319233-wq —
- B 端：按项目 / 月度 / 年度 ladder
- C 端：电商平台 SKU 标准定价（详见 ecommerce-listing sku-blueprints/*/sku.yaml）
- 折扣权限：销售个人 ≤ 5%，主管 5-15%，> 15% 走 ops 审批

## 5. 销售话术核心要点

- 强调**人工质保的服务**（不强调 AI 商品）
- 强调 **2 次免费修改 + 7 天修改窗口**
- 拒单口径见 `customer-service-script.md` template

## 6. 客户分层 + Twenty CRM stage 映射

详见 `NarratorAI-Studio/project-hub/docs/twenty-crm-onboarding.md`。

## 7. 售后 + 投诉处理

TODO @liushixuan55-create — C 端 / 公关响应流程。

## 8. 复购 + 老客户运营

TODO @zaiye0 —
- 老客户标识与 stage 跟进
- 复购促销策略
- 流失客户唤回

## 相关链接

- [FinOps 物料成本对账](./finops.md)
- [开发者集成](./developer-integration.md)
- [ecommerce-listing sku-blueprints](https://github.com/NarratorAI-Studio/ecommerce-listing/tree/main/sku-blueprints)
- [project-hub Twenty CRM onboarding](https://github.com/NarratorAI-Studio/project-hub/blob/main/docs/twenty-crm-onboarding.md)

---

*Auto-synced from `NarratorAI-Studio/narrator-ai-cli/docs/sales-playbook.md`.*
