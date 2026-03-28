# memory/lessons.md - 踩坑记录

> 踩过的坑，按严重程度分级
> P0=生产级故障 P1=严重延误 P2=一般问题

---

## P1 - GitHub Token 认证失败 (2026-03-26)
- **结论**: Git remote URL 内嵌 Token 才能在无交互环境下同步
- **文件**: memory/infra.md
- **教训**: `git push` 需要 SSH key 或 Token，不支持 `git push` 后手动输入密码

---

*Last updated: 2026-03-26*
