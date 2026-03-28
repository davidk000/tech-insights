# memory/lessons.md - 踩坑记录

> 踩过的坑，按严重程度分级
> P0=生产级故障 P1=严重延误 P2=一般问题

---

## P1 - GitHub Token 认证失败 (2026-03-26)
- **结论**: Git remote URL 内嵌 Token 才能在无交互环境下同步
- **文件**: memory/infra.md
- **教训**: `git push` 需要 SSH key 或 Token，不支持 `git push` 后手动输入密码

---

## P0 - GitHub Token 暴露在 Commit 历史中 (2026-03-28)
- **结论**: memory/infra.md 中写了 PAT token，被 GitHub Secret Scanning 检测到，push 被永久 block
- **修复**: `git reset --soft` + `git commit --amend` 合并所有 commits，重写历史消除 token commit (360a489)
- **教训**: GitHub PAT/Token 禁止写入任何文件，只通过环境变量或 git remote URL 传递；所有 token 相关内容写入后立即删除并 squash
- **文件**: memory/infra.md（P0 教训：任何 token 都不能明文写入文件）
- **预防**: 配置 git secret scanning 预检，或使用 `git-secrets` 工具

---

*Last updated: 2026-03-28*
