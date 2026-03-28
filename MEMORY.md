# MEMORY.md - 长期记忆

> 核心经验与重要决策的永久记录
> 更新频率：每日提取重要决策，每周回顾整理

---

## 当前状态概览

| 项目 | 状态 | 说明 |
|:---|:---|:---|
| tech-insights 归档 | ✅ 运行中 | daily-news/articles/reports/code-output 归档至 GitHub |
| 每日科技早报 | ✅ 运行中 | 08:45 推送至飞书，归档至 tech-insights |
| 每周 GitHub/arXiv 追踪 | ⏳ 待配置cron | 每周一执行，待配置实际定时任务 |
| OpenClaw v3.2 配置 | ✅ 完成 | 2026-03-27 完成系统性优化 |

---

## 记忆分层（速查）

| 层级 | 文件 | 用途 |
|:---|:---|:---|
| 索引层 | `MEMORY.md` | 关于用户、能力概览、记忆索引 |
| 项目层 | `memory/projects.md` | 各项目当前状态与待办 |
| 基础设施层 | `memory/infra.md` | 服务器、API、部署等配置速查 |
| 教训层 | `memory/lessons.md` | 踩过的坑，按严重程度分级 |
| 日志层 | `memory/YYYY-MM-DD.md` | 每日原始记录 |

---

## 铁律

> 任何时候都不能违反的铁칙

- **每次进化前必须先备份**：`cp -r ~/.openclaw/workspace ~/.openclaw/workspace.backup-$(date +%Y%m%d-%H%M%S)` 或使用 `scripts/smart-backup.sh`

## 用户指令（优先级最高）

- **学习进化时间**：每天 23:00 - 07:00（这个时段深度学习新技能、总结经验、优化配置）
- **备份铁律**：任何配置变更/优化/安装 skill 前必须先备份

---

## 教训索引

| 时间 | 教训 | 级别 |
|:---|:---|:---|
| 2026-03-26 | Git push 需要 Token，交互式密码输入不可用 → remote URL 必须内嵌 Token | P1 |
| 2026-03-27 | heartbeat-check.py 会覆盖 HEARTBEAT.md → 已移除 update_heartbeat_md() 函数，任务定义不再被冲掉 | P1 |
| 2026-03-27 | MEMORY.md 编辑失败 → 原因：之前某次写入时字符编码损坏，write 覆盖修复 | P1 |
| 2026-03-27 | Git remote 多个分支 push 失败 → 原因：forced update 导致的 refspec 冲突，rebase 解决 | P2 |

---

## 2026-03-27 - 配置优化（结论）

**结论**: 完成 workspace 配置文件系统性优化，解决模型配置不一致、内容重复、索引缺失等问题

**核心决策**:
- canonical 归档路径 = `tech-insights/`（即 GitHub 仓库本地拷贝），workspace 下只作缓存
- SOUL.md 只放原则，AGENTS.md 才是执行细则，避免两处维护
- 每次任务完成后必须 git commit + push，网络不稳定时本地 commit 也能保存

**文件变更**: SOUL.md / AGENTS.md / HEARTBEAT.md / MEMORY.md / TOOLS.md / config/model-pools.json

---

## 2026-03-26 - GitHub 同步能力固化

- **结论**: GitHub Token 必须嵌入 remote URL，否则非交互环境无法 push
- **文件**: memory/infra.md

---

## 2026-03-19 - 虾兵蟹将特工队进化至v3.0

- **结论**: 整合 OpenClaw AI Framework v3.0，全员获得7步深度使用法、三层记忆体系、Heartbeat 维护、24小时定向学习、自我成长机制
- **来源**: GitHub - Work-Fisher/openclaw-ai-assistant-framework

---

*Last updated: 2026-03-27*
