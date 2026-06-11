# 用户使用指南

> **更新频率**：on each CLI version bump
> **同步源**：`NarratorAI-Studio/narrator-ai-cli/docs/user-guide.md`
> **owner**：@LaytonLu @4mYHime

## TL;DR

Narrator AI CLI 是一行命令安装、一句话生成电影 / 短剧解说视频的命令行工具，配合 AI agent（OpenClaw / Windsurf / WorkBuddy / Claude Code 等）使用。

**典型用法**：
```bash
narrator-ai-cli --version          # 验证安装
narrator-ai-cli login              # 首次登录
# 然后在 AI agent 内自然语言下单：
# "生成一段《黑神话：悟空》的喜剧风格解说视频"
```

## 1. 安装

**前置条件**：Python 3.10+，Git

| 平台 | 命令 |
|------|------|
| macOS / Linux | `curl -fsSL https://raw.githubusercontent.com/NarratorAI-Studio/narrator-ai-cli/main/install.py \| python3` |
| Windows (CMD/PowerShell) | `python -c "import urllib.request; exec(urllib.request.urlopen('https://raw.githubusercontent.com/NarratorAI-Studio/narrator-ai-cli/main/install.py').read())"` |

验证：`narrator-ai-cli --version`

## 2. 首次配置

TODO @LaytonLu — 补充：
- 账号注册 / 登录流程
- API key 获取方式
- 配置文件位置（macOS `~/.config/narrator-ai/`，Windows `%APPDATA%/narrator-ai/`）

## 3. 核心命令

TODO @LaytonLu — 用户场景导向列出最常用命令：
- 生成单条解说视频（指定电影 + 风格）
- 批量生产
- 查询任务状态
- 下载交付物
- 查看账户余额 / 充值
- 管理模板

## 4. 12 种解说风格 + 90+ 模板

TODO @LaytonLu — 列出当前可用风格（动作 / 喜剧 / 悬疑等）与代表模板，附在哪里查最新清单。

## 5. 多语种配音

11 种语言 / 63 个音色。详细清单 + 选择建议见 advanced-tips.md。

## 6. 交付物形态

- 视频文件（MP4，与原视频同分辨率）
- 字幕文件（SRT）
- 解说文案（DOCX，可选）
- 多语种交付（按订单选）

## 7. 与 AI Agent 集成

| Agent | 集成方式 | 文档 |
|-------|---------|------|
| OpenClaw | 内置 skill | TODO 补链接 |
| Windsurf | MCP server | TODO |
| WorkBuddy | CLI plugin | TODO |
| Claude Code | narrator-ai-cli-skill | https://github.com/NarratorAI-Studio/narrator-ai-cli-skill |

## 8. 常见使用场景

TODO @LaytonLu — 短剧解说创作者 / 自媒体 / 影视 MCN 等典型用户的端到端工作流示例。

## 9. 反馈与帮助

- 反馈：[NarratorAI-Studio/project-hub Issues](https://github.com/NarratorAI-Studio/project-hub/issues) 加 `source:user-feedback` label
- FAQ：本 docs/ 下 `faq-troubleshooting.md`
- 进阶用法：本 docs/ 下 `advanced-tips.md`

## 相关链接

- [FAQ & 故障排查](./faq-troubleshooting.md)
- [进阶用户技巧](./advanced-tips.md)
- [开发者集成](./developer-integration.md)

---

*Auto-synced from `NarratorAI-Studio/narrator-ai-cli/docs/user-guide.md`.*
