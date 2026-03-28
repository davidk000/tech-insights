# memory/infra.md - 基础设施配置

## GitHub
- **用户**: davidk000
- **PAT**: [已撤回-需重新生成]（原 token 曾嵌入 remote URL，建议立即在 GitHub Settings > Developer settings > Personal access tokens 撤销并重新生成）
- **tech-insights 仓库**: https://github.com/davidk000/tech-insights
- **默认分支**: main

## 归档规范（2026-03-27 确立）

**canonical 归档目录:** `~/.openclaw/workspace/tech-insights/`

| 类型 | 路径格式 |
|:---|:---|
| 每日资讯 | `tech-insights/daily-news/YYYY/MM/YYYY-MM-DD.md` |
| GitHub Trending | `tech-insights/daily-news/YYYY/MM/YYYY-MM-DD-github-trending.md` |
| arXiv 论文 | `tech-insights/daily-news/YYYY/MM/YYYY-MM-DD-arxiv.md` |
| 深度洞察 | `tech-insights/articles/YYYY/MM/YYYY-MM-DD-insight.md` |
| 技术报告 | `tech-insights/reports/YYYY/MM/YYYY-MM-DD-report.md` |

**归档后必须同步 GitHub:**
```bash
cd tech-insights && git add . && git commit -m "sync: YYYY-MM-DD" && git push origin main
```

## 同步记录
| 日期 | 操作 |
|:---|:---|
| 2026-03-26 | 首次同步 daily-news |
| 2026-03-27 | 确立 canonical 归档路径；迁移 daily-news 26/27；重定向脚本到 tech-insights/ |

---

*Last updated: 2026-03-27*
