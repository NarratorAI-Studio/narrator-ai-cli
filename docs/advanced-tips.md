# 进阶用户技巧

> **更新频率**：on each new template / voice / pipeline trick
> **同步源**：`NarratorAI-Studio/narrator-ai-cli/docs/advanced-tips.md`
> **owner**：@LaytonLu @4mYHime

## TL;DR

适用于已经能跑通基本流程、想压缩单次成本 / 提高质量 / 解锁高级模板的进阶用户。基础用法见 `user-guide.md`。

## 1. 模板组合技

TODO @LaytonLu —
- 同一电影不同风格组合实测效果对照
- 复合模板（开场用 A 风格 + 主体用 B 风格 + 结尾 callback）
- 用户自定义模板上传与调用

## 2. 音色选择策略

63 个音色按场景挑选指南：

TODO @4mYHime —
- 喜剧风格首选音色
- 悬疑 / 恐怖风格首选音色
- 多语种文化适配（中→英、中→日 不同语种的音色推荐）
- 同一视频多音色混搭（叙述 + 角色对白）

## 3. 批量参数调优

详见 `batch-processing.md`，本节仅列「轻量批量优化」：

TODO @LaytonLu —
- 同一批量内的并发上限建议（≤ 5 单批，与 SKU 服务能力声明对齐）
- token / 解析费 优化技巧
- BGM 复用减少重新生成

## 4. 输出后处理

- 视频压缩到平台合规码率（详见 ops-runbook §4）
- SRT 时间轴精修（手工对齐工具）
- 多版本输出（短剧切片 / 长视频 / 横竖屏适配）

## 5. 与第三方工具协同

TODO @4mYHime —
- 与剪映 / Premiere 工作流交接
- 与抖音 / 视频号 / B站发布工具的元数据预填

## 6. 二创版权红线（重要）

⚠️ **必读**：解说类商品涉及二创红线，本仓库工具仅做基于客户提供且已授权的现有视频的解说稿+口播。**不做剧本改编 / 全片重剪 / 角色与剧情修改**。详情 see `NarratorAI-Studio/ecommerce-listing/sku-blueprints/movie-narration/sku.yaml`「二创版权澄清」章节。

抖音二创授权片单白名单（5 家）：优酷 / 爱奇艺 / 腾讯视频 / 芒果 / 搜狐。其他片源未授权使用属高风险。

## 7. 高阶 debug 技巧

详见 `faq-troubleshooting.md` §debug 章节。

## 相关链接

- [用户使用指南](./user-guide.md)
- [高并发批量指南](./batch-processing.md)
- [FAQ & 故障排查](./faq-troubleshooting.md)

---

*Auto-synced from `NarratorAI-Studio/narrator-ai-cli/docs/advanced-tips.md`.*
