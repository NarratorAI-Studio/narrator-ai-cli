# FAQ & 故障排查

> **更新频率**：on each new common issue / error pattern
> **同步源**：`NarratorAI-Studio/narrator-ai-cli/docs/faq-troubleshooting.md`
> **owner**：@LaytonLu @ShawYu19

## 安装类

### Q: 安装时报 Python 版本不够
A: 需要 Python 3.10+。验证：`python3 --version`。低版本升级见 https://www.python.org/downloads/。

### Q: `narrator-ai-cli --version` 报 command not found
A: TODO @LaytonLu — 补 PATH 配置 / shell rc 重载步骤 / Windows 重启终端等

### Q: pip 安装速度慢 / 无法访问 PyPI
A: TODO @LaytonLu — 国内 mirror 配置 + 离线安装包获取方式

## 认证类

### Q: API key 在哪里获取？
A: TODO @LaytonLu — 用户中心 URL + 步骤

### Q: 余额不足时怎么处理？
A: TODO @LaytonLu — 充值入口 + 客服联系方式

## 生成类

### Q: 生成超时 / 卡住
A: TODO @LaytonLu —
- 单任务正常时长区间
- 超时阈值与重试机制
- 排查步骤

### Q: 生成结果质量不如预期
A: TODO @4mYHime + @ShawYu19 —
- 检查模板选择是否匹配题材
- 检查源视频质量（分辨率 / 时长 / 字幕清晰度）
- 调音色 / 风格的 trial-and-error 建议

### Q: 多语种翻译漏行 / 错位
A: TODO @4mYHime — 排查 SRT 编码 / 时间轴对齐 / 人工核对流程

## 批量类

### Q: 批量任务部分成功部分失败
A: 详见 `batch-processing.md` §故障处理。

### Q: 单批超过 5 个被拒
A: 这是设计上的服务能力约束（人工核对工时 + 渲染并发），不是 bug。详见 `sku.yaml` § 服务能力声明。

## 平台合规类

### Q: 抖音上架被驳回「AI 一键生成」
A: 我们的产品本质是「人工质保的服务交付」，AI 是内部工具。详见 `NarratorAI-Studio/ecommerce-listing/docs/02 §5 AI 标识合规备用条款`。

### Q: 客户上传素材涉及版权 / 肖像权
A: 客户上传素材的版权 / 肖像权 / 配音权由客户负责。详情页 §5 与客服话术 §3 同步拒单口径。

## 错误码速查

TODO @LaytonLu — 完整 error code → 含义 → 处置建议表

## 反馈未在 FAQ 内的问题

请到 [NarratorAI-Studio/project-hub Issues](https://github.com/NarratorAI-Studio/project-hub/issues) 创建 issue 加 `source:user-feedback` label。

## 相关链接

- [用户使用指南](./user-guide.md)
- [运维管理员手册](./ops-runbook.md)

---

*Auto-synced from `NarratorAI-Studio/narrator-ai-cli/docs/faq-troubleshooting.md`.*
