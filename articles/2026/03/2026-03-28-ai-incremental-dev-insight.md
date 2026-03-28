# AI 辅助增量开发工具深度洞察

**主题**：Claude Code / Cursor / OpenCode 在存量代码资产基础上的增量开发方案
**时间**：2026-03-28
**归档**：tech-insights/articles/2026/03/2026-03-28-ai-incremental-dev-insight.md

---

## 0. 一句话结论

大代码库（10万行以上）上做 AI 辅助增量开发，核心瓶颈是**上下文选择**而非模型能力。三大工具在这个命题上的路线差异显著：Claude Code 靠 CLAUDE.md 规约 + Plan Mode 解决"方向感"，Cursor 靠 Rules 文件分层 + Agent Mode 解决"边界感"，OpenCode 靠双 Agent 架构 + Auto Compact 解决"续航感"。**没有万能工具，只有适合的上下文工程策略。**

---

## 1. 存量代码资产的独特挑战

### 1.1 为什么通用 AI 编程会失败

当代码库规模超过一定阈值（通常是 10 万行、1000+ 文件），AI 编程工具面临三个结构性挑战：

| 挑战 | 表现 | 根因 |
|:---|:---|:---|
| **上下文膨胀** | Token 成本暴涨、响应延迟、模型遗忘早期约束 | 完整代码库无法塞入上下文窗口 |
| **依赖复杂性** | AI 创建新文件而非修改现有文件、路径错乱 | 无法理解模块边界和调用依赖链 |
| **知识隐含** | 架构决策、业务规则藏在 commit 历史和团队默契里 | AI 无法从代码本身推断 |

### 1.2 核心矛盾：增量需求 vs 整体理解

AI 辅助增量开发有两个方向：
- **增量优先**（Cursor / OpenCode 偏向）：只给 AI 当前任务所需的最小上下文，牺牲全局理解换取精准
- **规约优先**（Claude Code 偏向）：用项目级 CLAUDE.md 建立长期记忆，让 AI 随时间积累对项目的理解

Cursor 的实践数据（University of Chicago 研究）：引入 AI 上下文分层后，团队周均 PR 合并量提升 39%，专家级开发者功能交付速度提升 40%。

---

## 2. 三大工具的核心架构对比

### 2.1 功能定位矩阵

| 维度 | Claude Code | Cursor | OpenCode |
|:---|:---|:---|:---|
| **载体** | CLI + IDE 插件 | IDE（VS Code/JetBrains） | TUI + CLI（多表面） |
| **上下文策略** | CLAUDE.md + Auto Memory | Rules 分层 + Cursor AI Index | 双 Agent（Plan/Build）+ Auto Compact |
| **团队协作** | Plugins、Hooks、/init | .cursor/rules/（项目级） | provider-agnostic（75+ LLM） |
| **大代码库方案** | Subagents 独立上下文窗口 | @codebase 语义检索 + 分层 | Session 持久化 + 智能压缩 |
| **MCP 集成** | 原生支持，300+ 服务 | 支持 | 支持 |
| **收费模式** | Anthropic API 按量 | 订阅制 | 开源 + BYOK（自带 API Key） |

### 2.2 Claude Code：规约驱动型

**核心哲学**：让 AI 每次会话都能"自证正确"。

Claude Code 的上下文模型分为两层：
- **Intent Context**：用户的自然语言 prompt
- **State Context**：近期文件、edits、语义搜索结果、linter 诊断

关键机制：
```
探索(Plan Mode) → 规划 → 实现 → 提交
```

**CLAUDE.md 是 Claude Code 的灵魂**。它不是提示词模板，而是项目级可执行规约，需要满足：
- 只写入 AI 无法从代码推断的规则（测试命令、lint 规范、分支策略）
- 保持简短（超过 200 行会显著降效）
- 随项目演化，像代码一样 commit 到 git

**大代码库关键能力：Subagents**。将探索/安全审查/代码评审分流到独立上下文窗口，避免主会话被大量阅读内容污染。

**Hooks 系统**：将"必须发生"的动作（auto-format、guardrails）做成确定性护栏，而非依赖 AI 记得。

### 2.3 Cursor：选择性上下文型

**核心哲学**：建立 AI 与复杂系统之间的选择性接口。

Cursor 的上下文模型采用两阶段：
1. **Intent Context**：任务描述
2. **State Context**：自动检索的语义相关文件

关键发现：Cursor 的语义搜索在**命名规范一致**（如 FooService、FooRepository）和**模块边界清晰**的代码库上效果最好。

**.cursor/rules/ 文件体系**：
- `file-conventions.mdc`：文件名/变量/导出规范（auto-attach 到 .ts 文件）
- 按 glob 模式自动附加：`src/api/**/*.ts` 只加载后端规范
- 领域知识文件：路由约定、中间件顺序、错误响应格式

**Cursor Agent Mode 的正确用法**：
- 跨服务大规模重构：Agent Mode + 2-3 个参考实现 + 高层架构摘要
- 60-70% 的变更用 Tab / Inline Edit（Cmd+K）处理，Agent Mode 只留给真正多文件的改动

### 2.4 OpenCode：供给无关型

**核心哲学**：不被单一模型提供商锁定，保持灵活性。

OpenCode v1.3.3（2026-03）的核心架构：
- **Provider-agnostic**：支持 75+ LLM 提供商，包括本地 Ollama/Groq
- **双 Agent 架构**：Plan Agent（只读分析）↔ Build Agent（执行变更），通过 Tab 键切换
- **Auto Compact**：会话过长时智能压缩对话历史，保留核心记忆
- **Git-backed Session Review**：TUI 内直接可视化 diff 和文件状态

关键优势：
- 复用现有 GitHub Copilot / ChatGPT Plus 订阅（注意 ToS 风险）
- Provider 故障时秒级切换到备用模型
- 企业级 SSO 认证（GitHub Copilot Enterprise）
- Node.js 运行时支持（v1.3.0 新增）

---

## 3. 增量开发核心方案：Context Engineering

### 3.1 分层上下文架构（适用于所有工具）

```
┌─────────────────────────────────────────────┐
│  Layer 0: 全局不变式（架构约束、安全边界）   │ ← .cursor/rules/ 或 CLAUDE.md
├─────────────────────────────────────────────┤
│  Layer 1: 项目摘要（子系统概览、领域模型）   │ ← @docs-accessible summaries
├─────────────────────────────────────────────┤
│  Layer 2: 任务级上下文（目标文件、函数、diff）│ ← @file / @git / @code
├─────────────────────────────────────────────┤
│  Layer 3: 工具自动补充（linter 错误、搜索结果）│ ← 工具自动注入
└─────────────────────────────────────────────┘
```

### 3.2 RAG 检索增强：代码优先 Chunking 策略

对于超大规模代码库（100万行以上），向量检索是不可避免的。代码 RAG 的 chunking 策略与文档 RAG 有本质区别：

| 策略 | 适用场景 | 特点 |
|:---|:---|:---|
| **AST-aware Chunking** | 结构化语言（JS/TS/Python） | 按函数/类边界切分，保留语义完整性 |
| **Recursive Chunking** | 深度嵌套代码 | 按缩进/括号递归切分 |
| **语义 Chunking** | 业务逻辑复杂的代码 | 按功能单元（而非行数）切分 |
| **混合 Chunking** | 超大 monorepo | 顶层按模块，底层按函数 |

关键原则：代码的 chunk 大小应小于函数的平均长度，避免一个 chunk 横跨多个语义单元。

### 3.3 增量开发工作流：四阶段法

适用于 Claude Code（也适用于 Cursor 的 Ask/Agent 切换）：

```
阶段 1: Explore（Plan Mode）
└─ 目标：在不改代码的前提下，搞清楚现状
   工具：read / grep / @file
   验收：能画出调用链或说清数据流

阶段 2: Plan（规划）
└─ 目标：让 AI 明确"要改哪些文件、为什么、怎么验收"
   工具：claude -p "I want to add Google OAuth. What files need to change?"
   验收：输出带文件列表和风险点的执行计划

阶段 3: Implement（实现）
└─ 目标：按计划执行 + 持续验证
   工具：Edit / Write / Test
   验收：跑通测试、lint 通过

阶段 4: Commit（提交）
└─ 目标：把结果沉淀成可审查资产
   工具：git commit + PR
```

### 3.4 Scope 控制：小步快跑原则

大代码库上最大的错误是"让 AI 做太多"。正确的拆分方式：

| 错误方式 | 正确方式 |
|:---|:---|
| "给应用加上 RBAC" | 拆成 4-5 个独立 PR：migration → middleware → 路由保护 → 测试 |
| "解释认证流程" | 明确边界："从 route handler 到 DB query 的完整调用链" |
| Agent Mode 做单文件改动 | 用 Inline Edit（Cmd+K）处理，节省上下文 |

---

## 4. 团队级配置：从个人工具到团队资产

### 4.1 项目规约的版本控制

```markdown
# CLAUDE.md（Claude Code）或 .cursor/rules/（Cursor）

## 目录结构
src/
├── routes/[domain]/      # 路由定义
├── controllers/[domain]/ # 控制器
├── services/             # 业务逻辑
├── repositories/         # 数据访问
└── schemas/              # Zod 验证模式

## 命名规范
- 文件名：kebab-case（user-service.ts）
- 函数/变量：camelCase
- 类/接口/类型别名：PascalCase
- 常量：UPPER_SNAKE_CASE

## 导出规范
- 优先命名导出，禁用 default export
- 每个文件一个主要导出
```

### 4.2 Hooks：不可协商的护栏

```javascript
// pre-commit hook: 自动 format + lint 改动文件
// .claude/hooks/pre-commit.sh
#!/bin/bash
for file in $(git diff --cached --name-only); do
  prettier --write "$file"
  eslint --fix "$file"
done
```

### 4.3 MCP：将外部系统接入低上下文成本

| MCP 用途 | 典型场景 |
|:---|:---|
| GitHub | 读 Issue/PR，自动化 Code Review |
| Figma | 设计师稿→代码（Uber uSpec 方案） |
| 数据库 | Schema 感知，避免生成不兼容的 ORM 代码 |
| 监控/Sentry | 错误堆栈自动分析并关联到代码位置 |

---

## 5. 技术洞察总结

### 洞察 1：上下文分层是工程问题，不是模型问题

当前模型（Claude 4 Opus / GPT-4o / Gemini 2.5）已经足够强大，瓶颈在于如何把正确的上下文在正确的时机送给模型。**代码 RAG 的 chunking 策略比 embedding 模型选择更关键**。

### 洞察 2：增量开发的"增量"不仅是代码变更粒度

真正的增量是**认知增量**：AI 需要理解"这个代码库如何演进"，而非仅知道"当前代码长什么样"。项目历史（git log）和架构决策记录（ADR）是不可或缺的上下文。

### 洞察 3：AI 辅助大代码库开发的三条路线正在收敛

- Claude Code 的 CLAUDE.md + Subagents
- Cursor 的 Rules 分层 + Agent Mode  
- OpenCode 的 Plan/Bulid Agent 分离

本质都是**把"理解项目"和"执行变更"分离**，避免模型在两者之间上下文污染。

### 洞察 4：Cursor 的实证数据具有参考价值

University of Chicago 对 24 个组织的研究表明，AI 上下文分层带来 39% 的 PR 增量且无回退峰值。这说明**问题不是 AI 能不能帮忙，而是给 AI 什么样的界面**。

### 洞察 5：OpenCode 的 provider-agnostic 策略代表企业趋势

当团队规模超过 10 人，模型选择的灵活性从"加分项"变成"必选项"。Claude Code 周末"罢工"（Anthropic 事故）时，能切到本地 Ollama 继续干活是生产力的关键差异。

---

## 6. 工具选型建议

| 团队/场景 | 推荐工具 | 理由 |
|:---|:---|:---|
| 个人开发者 / 快速原型 | OpenCode + Claude Code | 开源灵活，无供应商绑定 |
| 中型团队（5-20人）有现有 IDE | Cursor | IDE 深度集成，Rules 体系成熟 |
| 企业级 / 重视可控性 | Claude Code | 完善的 Hooks/MCP/权限体系 |
| 超大 monorepo（100万行+） | OpenCode + 自建 RAG | 需定制化 chunking 和检索策略 |
| 多云 / 混合模型团队 | OpenCode | provider-agnostic，75+ 支持 |

---

## 7. 参考文献

- Claude CN Team. "Claude Code 最佳实践：把上下文变成生产力（团队可落地长文）". claudecn.com, 2026-01-22.
- Skywork AI. "Claude Code Plugin Best Practices for Large Codebases (2025)". skywork.ai, 2025-12.
- Developer Toolkit. "Large Codebase Strategies". developertoolkit.ai, 2026-02-16.
- R. Rastiehaiev (HiBoB). "Designing AI Context Layers in Cursor for Large Codebases". aijourn.com, 2026-02-23.
- Sanj.dev. "OpenCode Deep Dive: Provider-Agnostic AI CLI in 2026 (v1.3.3)". sanj.dev, 2026-03-24.
- Zylos Research. "Monorepo Architecture: Tools, Strategies, and the AI-Driven Renaissance in 2026". zylos.ai, 2026-02-11.
- R. Hightower. "Agent Brain: A Code-First RAG System for AI Coding Assistants". Medium/Spillwave, 2026-02.
- SkillsPlayground. "Claude Code Memory: CLAUDE.md, Auto Memory & Context Management (2026 Guide)". skillsplayground.com, 2026-02.
- Morphllm. "Claude Code Best Practices: The 2026 Guide to 10x Productivity". morphllm.com, 2026-02.

---

*洞察报告完成 | 虾兵蟹将特工队 🦞*
