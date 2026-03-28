# TOOLS.md - Local Notes

_Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes._

---

## 即时通讯
- 飞书 Webhook：配置在环境变量 `FEISHU_WEBHOOK_URL`
- 默认通知频道：`#ai-news`
- 紧急通知频道：`#urgent`

## 文件系统
- 工作区根目录：`~/.openclaw/workspace/`
- GitHub 归档目录：`~/.openclaw/workspace/tech-insights/`（canonical，所有内容最终归档至此）
- 代码输出目录：`~/.openclaw/workspace/code-output/`
- 素材收集目录：`~/.openclaw/workspace/raw-materials/`
- 日志回收站：`~/.openclaw/workspace/trash/`（删除前先移至此）

## API配置
- Serper 搜索 API：配置在环境变量 `SERPER_API_KEY`
- 百度统计 Token：配置在环境变量 `BAIDU_ANALYTICS_TOKEN`
- 所有 API Key 通过环境变量读取，禁止硬编码

## OpenClaw 配置

### 运行时模型
```json
{
  "models": {
    "default": "minimax-cn/MiniMax-M2.7",
    "code": "minimax-cn/MiniMax-M2.7",
    "longContext": "minimax-cn/MiniMax-M2.7",
    "complex": "minimax-cn/MiniMax-M2.7"
  }
}
```

### 本地脚本
```bash
# 每日早报归档（写 tech-insights/daily-news/）
./scripts/daily-news-archive.sh "2026-03-27" "内容"

# GitHub 同步（tech-insights 目录）
cd ~/.openclaw/workspace/tech-insights && git add . && git commit -m "sync" && git push origin main

# 智能备份
./scripts/smart-backup.sh
```

### 常用命令
```bash
openclaw gateway start/stop/restart/status
openclaw config list/get/set
openclaw doctor
clawhub search/install/update/list
```

### ClawHub
- 网站：https://clawhub.ai
- CLI：`clawhub search <skill>`

## 成本参考（Minimax）

| 任务类型 | 推荐模型 | 说明 |
|:---|:---|:---|
| 日常会话 | MiniMax-M2.7 | 当前 runtime |
| 代码生成 | MiniMax-M2.7 | 同上 |
| 长文本处理 | MiniMax-M2.5 | 高并发场景可用 M2.5-lightning |
| 简单任务 | MiniMax-M2.5-lightning | 最低延迟 |

## 安全规范
- API Key 禁止硬编码，只用环境变量
- 删除操作前先 `trash` 而非 `rm`
- 生产环境配置变更前必须二次确认
- `rm` 类高危操作必须高亮警告

## 学习资源
- 教程：https://github.com/xianyu110/awesome-openclaw-tutorial
- 文档：https://docs.openclaw.ai
- Skills：https://clawhub.ai

---
_Updated: 2026-03-27 - 重写，移除残留模板内容_
