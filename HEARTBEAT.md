# HEARTBEAT.md

> 本文件分两部分：
> - **任务定义**：定时任务的执行规范（供人工查阅）
> - **检查清单**：每30分钟执行的维护动作（OpenClaw heartbeat prompt 触发，非 cron）

---

## 定时任务定义

### 任务1：每日科技资讯推送 ⏰ 08:45

**执行方式：** exa_web_search 抓取科技媒体网站

**内容源：**
- https://www.infoq.cn/
- https://aihot.today/
- https://hnrss.org/frontpage（替代 News Minimalist 429）
- https://www.buzzing.cc/
- https://www.ifanr.com/
- https://www.smzdm.com/

**内容范围：** AI/大模型（重点含 Hugging Face 趋势模型）、互联网大厂、新产品、投融资、硬件芯片、科技热点

**推送渠道：**
- [x] 飞书私信 (ou_8cf14197155da6ce81c563783e5847bc)
- [ ] 飞书群（待配置）

**归档路径：** `daily-news/YYYY/MM/YYYY-MM-DD.md`（已tracked；原 tech-insights/ 在 gitignore 中已修复）

**执行动作：**
1. web_fetch 抓取内容 → 2. 提取标题摘要 → 3. 分类整理 → 4. 飞书推送 → 5. 归档至 daily-news/ → 6. git add + commit + push → 7. 飞书推送完成通知

---

### 任务2：GitHub Trending 追踪 ⏰ 每周一 09:00

**执行方式：** exa_web_search 抓取 GitHub Trending

**归档路径：** `daily-news/YYYY/MM/YYYY-MM-DD-github-trending.md`

**执行动作：**
1. exa_web_search 抓取 → 2. 提取项目名/描述/Star/语言 → 3. 归档至 daily-news/ → 4. git add + commit + push

---

### 任务3：arXiv 论文追踪 ⏰ 每周一 10:00

**执行方式：** exa_web_search 或 curl 直接请求 arXiv RSS

**归档路径：** `daily-news/YYYY/MM/YYYY-MM-DD-arxiv.md`

**执行动作：**
1. 抓取论文列表 → 2. 提取标题/作者/摘要/PDF链接 → 3. 筛选高相关性 → 4. 归档至 daily-news/ → 5. git add + commit + push

---

### 任务4：科技洞察总结 ⏰ 每周一 12:00

**执行方式：** exa_web_search + cto-advisor skill 生成技术洞察

**归档路径：** `articles/YYYY/MM/YYYY-MM-DD-insight.md`

**执行动作：**
1. 汇总资讯/项目/论文 → 2. 使用 cto-advisor skill 分析 → 3. 输出至 articles/ → 4. git add + commit + push

**Job ID:** `f3d90517-7796-4ecc-a828-1ce9a6fde904` ✅

---

### 任务5（新增）：Hugging Face 趋势模型追踪 ⏰ 每周一 14:00

**执行方式：** exa_web_search 搜索 Hugging Face 热门模型

**内容源：**
- exa_web_search: "site:huggingface.co/models trending top models 2026"
- exa_web_search: "Hugging Face trending LLM vision language model 2026"

**内容范围：** 当周 Hugging Face 热门模型、模型能力突破、新晋开源模型

**推送渠道：** 飞书私信（ou_8cf14197155da6ce81c563783e5847bc）

**归档路径：** `daily-news/YYYY/MM/YYYY-MM-DD-hf-trending.md`

---

### 任务6：关键词告警 ⏰ 每小时

**执行方式：** Python 脚本扫描关键词库 + 飞书推送

**内容源：**
- IT桔子 / 36kr / 虎嗅（投融资）
- 199IT / 天脉财经（半导体）
- Hacker News RSS

**关键词配置：** `~/.openclaw/config/keywords-monitor.yaml`

**执行动作：**
1. 扫描各数据源 → 2. 匹配关键词 → 3. 生成告警卡片 → 4. 飞书推送（P0/P1级）

---

### 任务6：投融资快讯 ⏰ 每日 09:00

**执行方式：** Web Scraping + 飞书推送

**内容源：**
- IT桔子
- 创投通（财联社）
- SVTR.AI

**归档路径：** `daily-news/vc/YYYY-MM-DD.md`

**执行动作：**
1. 抓取昨日投融资事件 → 2. 提取金额/轮次/行业 → 3. 飞书推送 → 4. 归档 → 5. git commit

## 每30分钟检查清单

> OpenClaw heartbeat prompt 触发（`heartbeat-check.py`），非 cron

- [ ] 检查紧急事项（消息/通知）
- [ ] 整理今日记忆（写入 memory/YYYY-MM-DD.md）
- [ ] 清理7天前日志

**持续优化：**
- [ ] 检查是否有新 skill 需要学习
- [ ] 回顾已装 skill，发现整合机会
- [ ] 测试技能组合效果
- [ ] 程序龙、调研虾、金融虾、学习虾每周持续进化

---

## ⚠️ 重要配置说明

- **heartbeat-check.py**：只读写 `data/heartbeat-state.json`，不再覆盖 HEARTBEAT.md
- **定时任务**：4 个 cron jobs 已通过 `openclaw cron` 注册，由 Gateway 调度器自动触发
- **投递渠道**：全部指定为 `channel=feishu`，避免多 channel 冲突

---

*虾兵蟹将特工队 🦞🦐🐉*
*Updated: 2026-03-27 18:44 - cron jobs 已全部配置并验证; heartbeat-check.py 已修复*
