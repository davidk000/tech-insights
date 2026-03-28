# AI 辅助百万行级代码库增量开发深度洞察

**主题**：Claude Code / Cursor / OpenCode 在数百万行存量代码资产上的增量开发方案
**对标**：Linux Kernel 社区实践 + Kubernetes 社区实践
**时间**：2026-03-28
**归档**：tech-insights/articles/2026/03/2026-03-28-ai-incremental-dev-insight-v2.md

---

## 0. 核心结论（先看这条）

**你的场景**：数百万行代码 + 新增需求开发 + AI 辅助

**这不是工具选择问题，是架构问题。** 百万行代码库的核心矛盾是：**人类维护者脑子里知道的东西（架构决策、依赖关系、业务规则）AI 看不到**。三大社区（Linux / K8s / 大型 monorepo 团队）解决这个问题的方式高度一致：

> **先建"项目知识图谱"，再让 AI 在图谱约束下工作。**

没有知识图谱的 AI 编程，就像没有地图的导航——局部最优、全局灾难。

---

## 1. 问题建模：你的代码库处于哪个阶段？

代码库规模不同，最优策略完全不同：

| 阶段 | 规模 | 核心矛盾 | 推荐方案 |
|:---|:---|:---|:---|
| **T1: 小型** | < 10 万行 | 上下文够用，主要解决效率 | 单 Agent，工具选型驱动 |
| **T2: 中型** | 10-50 万行 | 上下文溢出，需要选择性检索 | Rules/CLAUDE.md 分层 + 语义索引 |
| **T3: 大型** | 50-200 万行 | 模块依赖复杂，需要依赖感知 | 知识图谱 + Planner/Worker 架构 |
| **T4: 超大型** | 200 万行+ | 跨系统跨团队，需要多 Agent 协作 | Kelos 式 orchestration + 持续运行 Agent |

**你处于 T3-T4 阶段**，意味着：
- 单一 AI Agent 的上下文窗口无论如何不够用
- 必须先建立**项目结构化知识**（目录结构、模块边界、导出符号、依赖关系）
- AI 的角色是**在知识图谱约束下执行增量任务**，而非理解全貌

---

## 2. 三大社区的真实做法

### 2.1 Linux Kernel 社区：Sasha Levin 主导的 AI 治理方案

**背景**：Linux Kernel 是地球上最大的开源协作项目之一，维护者横跨数千人，数百万行 C 代码，任何变更都需要经过严格的 code review 流程。

**2025年7月，Sasha Levin（内核 maintainer）提交了 RFC patch 系列**，为内核仓库建立统一的 AI 配置体系：

**配置架构**（8 个工具统一配置）：
```bash
.aider.conf.yml              → 指向中心文档
.codeium/instructions.md     → 指向中心文档
.continue/context.md         → 指向中心文档
.cursorrules                 → 指向中心文档
.github/copilot-instructions.md → 指向中心文档
.windsurfrules               → 指向中心文档
CLAUDE.md                    → 中心规则文档
Documentation/AI/main.md     → 71 行官方规范
```

**核心规则（Documentation/AI/main.md）**：
- 必须遵循内核编码标准
- 必须遵守内核开发流程（patch → review → 迭代）
- **必须用 `Co-developed-by:` 标注 AI 生成内容**（标注格式：`Co-developed-by: Claude claude-opus-4-20250514`）
- **禁止自行添加 `Signed-off-by:`**（只有人类开发者才能签发，具法律效力）

**对增量开发的启示**：

Linux Kernel 的做法揭示了一个关键原则：**在高度复杂的协作项目里，AI 的权限必须被明确边界化**。不是"你随意改动"，而是"你在清晰的规约下执行特定任务"。

Sasha Levin 的 RFC 证明：在数百万行代码、跨数千人协作的顶级开源项目里，**AI 配置的标准化比 AI 模型的选择更重要**。

### 2.2 Kubernetes 社区：k8sgpt + kubectl-ai + Kelos 三层体系

Kubernetes 社区面对的是另一类大规模存量代码问题：云原生生态极其庞大，Operator 模式意味着代码与运行时状态深度耦合。

**k8sgpt（7.6k ⭐）**：Kubernetes 专用 AI 分析工具
- 不是帮开发者写代码，而是帮 SRE/运维分析集群问题
- 集成 Lens IDE 等主流 K8s 管理工具
- 分析集群事件、Pod 状态、HPA 行为，用自然语言解释
- 对增量开发的启示：AI 在超大型代码库上可以**专门做"理解现有系统"的工作**，而不是写代码

**kubectl-ai（7.4k ⭐）**：自然语言 → kubectl 命令
- 将自然语言翻译成正确的 kubectl 指令
- 解决 kubectl 命令复杂度问题（参数多、上下文敏感）
- 对增量开发的启示：对于复杂的现有系统，**AI 先"翻译"人类意图到精确操作**，再执行，这是有效的分工

**Kelos（2026年新星）**：Kubernetes-native AI Coding Agent Orchestration

这是 Kubernetes 社区对"AI 在大代码库上工作"的最新回答，核心思想是把 AI Agent 当成**基础设施**来管理：

```
传统方式：Human → AI Coding Agent（交互式终端，一次性 prompt）
Kelos 方式：Human → Kelos Controller → Autonomous AI Agent Pod（持续运行）
```

Kelos 的四个核心原语：
- **Task**：最小工作单元（"修复这个 bug"、"实现这个 feature"）
- **Workspace**：代码仓库上下文（clone、注入凭证）
- **AgentConfigs**：打包指令 + Skills + MCP 服务集成
- **TaskSpawners**：触发器（监听 GitHub Issues → 自动创建 Task）

**关键洞察**：Kelos 的 TaskSpawners 可以监听 GitHub Issue，这意味着：
- **AI Agent 可以自动认领 Issue**
- **增量任务不需要人类手动分配**，AI 自己从 Issue 池里拿任务
- 这解决了大代码库上"人类难以全面了解代码库状态"的根本矛盾

Kelos 也能开发自己——项目内部运行着多个 TaskSpawner，自动进行 issue 分类、生成实现计划、修复 bug、响应 PR 反馈。这本质上是一个**AI 原生开发团队**的原型。

**对增量开发的启示**：当你有数百万行代码，维护者只有少量人时，把 AI Agent 变成"后台 worker"而不是"交互式助手"，让它们持续工作、监听事件、自动处理，是突破人力瓶颈的关键。

### 2.3 大型 Monorepo 团队：Planner/Worker 架构

**案例：Cursor 用 Planner/Worker 架构生成百万行代码浏览器**

Cursor 团队在 2026 年公开了他们的做法：用数百个并发 AI Agent 从零构建了一个完整的 Web 浏览器，最终产物超过 100 万行代码。

核心架构：
```
Planner Agent（架构师）
  → 分析整体结构，拆解模块边界
  → 把任务分发给 Worker Agent
Worker Agent（各司其职）
  → 每个负责一个子系统（渲染引擎/网络栈/JS引擎/UI层）
  → 在自己负责的模块内工作，不越界
Verification Loop（质量门禁）
  → 每个 Worker 提交后，自动运行测试套件
  → 失败则回退，不污染主线
```

**对比测试结论**：
- GPT-5.2（快、便宜）：适合常规功能实现，Worker 层主力
- Opus 4.5（慢、贵）：适合架构规划、跨模块依赖分析、Planner 层主力

**Planner/Worker 架构的核心价值**：解决了超大型代码库上"单一 Agent 上下文不够"的根本矛盾。Planner 不写代码，只做架构决策；Worker 在约束内写代码，不需要理解全貌。

**失败的场景**（也是最有价值的教训）：
- 复杂状态逻辑：AI 对有状态系统的修改极容易引入隐藏依赖
- 跨切割面的变更（如横跨多个 Worker 边界）
- 大规模调试（出了问题不知道是哪一层引入的）

---

## 3. 操作框架：百万行代码库增量开发实操手册

### 3.1 第一阶段：建立项目知识图谱（前置必做）

**这是所有工作真正的起点**，无论你选什么工具，这一步都不能跳过。

**知识图谱包含的内容**：

| 内容 | 作用 | 生成方式 |
|:---|:---|:---|
| 模块目录树 | 理解代码库物理结构 | `find . -type d -not -path './node_modules/*' -not -path './.git/*'` |
| 导出符号表 | 每个模块对外暴露的接口 | AST 解析（tree-sitter）|
| 导入依赖链 | 模块间调用关系 | 静态分析（Ripgrep + 自定义脚本）|
| 架构决策记录 | 为什么这么设计 | 团队文档 + git log 分析 |
| 业务规则清单 | 业务层约束（AI 无法从代码推断）| 人工整理 + 文档化 |

**具体实现**（以 TypeScript monorepo 为例）：

```python
# build_knowledge_graph.py
import subprocess
import ast
from pathlib import Path
from collections import defaultdict

def scan_imports(repo_path):
    """扫描所有模块间的导入关系"""
    import_map = defaultdict(set)
    for py_file in Path(repo_path).rglob("*.py"):
        with open(py_file) as f:
            try:
                tree = ast.parse(f.read())
                for node in ast.walk(tree):
                    if isinstance(node, ast.ImportFrom):
                        if node.module:
                            import_map[str(py_file)].add(node.module)
            except:
                pass
    return import_map

def build_dependency_graph(import_map):
    """构建知识图谱的核心"""
    # 输出: 每个模块的入度/出度分析
    # 找出: 被最多模块依赖的模块 = 最核心的模块 = 变更风险最高的区域
    pass
```

**输出格式**：
```json
{
  "modules": {
    "auth": { "exports": ["login", "logout", "refreshToken"], "dependents": 23 },
    "billing": { "exports": ["charge", "refund"], "dependents": 8 },
    "notification": { "exports": ["send", "subscribe"], "dependents": 12 }
  },
  "high_risk_modules": ["auth"],  // 被23个模块依赖
  "isolated_modules": ["legacy-v1"]  // 没有任何依赖
}
```

**为什么这一步不可跳过**：
Bito AI Architect 在 ProtonMail monorepo（90 文件重组织，13638 文件扫描）上的成功证明了这一点——**没有知识图谱的 Agent 不会尝试大规模重构，因为不知道边界在哪**。有了知识图谱，AI 才能知道"我能动哪些文件、动了会有什么后果"。

### 3.2 第二阶段：配置工具链（基于知识图谱）

#### Claude Code 配置

```markdown
<!-- CLAUDE.md -->
## 项目概览
- 仓库规模：~300万行，主要语言 TypeScript + Go
- Monorepo 结构：apps/（4个子应用）+ packages/（8个共享包）+ services/

## 模块边界（知识图谱摘要）
- auth 模块：所有认证逻辑，被 23 个模块依赖
- billing 模块：支付逻辑，被 8 个模块依赖
- 禁止跨包直接导入：apps/* 不得直接导入其他 apps/*

## 增量开发规则
1. 每次变更范围 ≤ 3 个文件（单次 commit）
2. 涉及共享包修改时：先在共享包内写测试，再在应用中集成
3. 路由/中间件变更：先 Explore 了解当前链路再动手
4. 涉及 auth 模块的变更：视为高风险，必须有 human review

## AI 标注规则
- 所有 AI 生成代码必须加 `Co-developed-by: Claude <version>`
- 禁止自行添加 `Signed-off-by`（人类专属）

## 验证要求
- 改完后必须运行: npm test && npm run build
- 失败必须先修复再提交
```

#### Cursor 配置

```markdown
<!-- .cursor/rules/architecture.mdc -->
---
description: 架构边界与模块规则
alwaysApply: false
---

## 模块边界（强制）
- apps/api/* → 只允许调用 packages/api-client 和 packages/auth
- apps/web/* → 只允许调用 packages/ui 和 packages/api-client
- 违反模块边界的导入 → 必须在 PR 中说明原因

## .cursor/rules/subsystem-auth.mdc
---
globs: ["**/auth/**/*.ts", "**/packages/auth/**/*.ts"]
alwaysApply: true
---

## Auth 模块专项规则
- 禁止在 auth 模块外直接访问 User 表
- Session 管理统一使用 @auth/session-manager
- 所有 auth 相关变更 → 必须通知 security team（自动创建 Slack 通知）

## .cursor/rules/subsystem-billing.mdc
---
globs: ["**/billing/**/*.ts", "**/packages/billing/**/*.ts"]
alwaysApply: true
---

## Billing 模块专项规则
- 所有金额计算必须使用 @billing/decimal-utils（禁止浮点数）
- Webhook handler 必须在 webhook-v2/ 目录下，legacy/ 不可新增
```

#### OpenCode 配置

```yaml
# opencode.yaml
# 工作区配置，分离 Plan Agent 和 Build Agent

model:
  planner: claude-opus-4-5  # 架构分析用贵的
  builder: claude-sonnet-4   # 具体实现用便宜的

context:
  max_session_tokens: 100000
  auto_compact_threshold: 0.7  # 会话超过70%自动压缩

rules:
  - path: CLAUDE.md          # 项目主规约
  - path: .opencode/rules/   # 工具特定规则目录
```

### 3.3 第三阶段：增量任务执行流

**场景：给 300 万行 monorepo 增加一个新功能**

```
人类意图：
"在 billing 服务里增加按量付费的实时扣费功能，需要支持 Stripe webhook，
扣费失败需要自动重试，被拒绝 3 次后发通知给客户并暂停服务。"

执行流程：
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Step 1: Plan Mode（Claude Code）— 理解依赖和范围
───────────────────────────────────────────────────
> "分析 billing 服务当前架构，重点关注：
  1. webhook 处理链路（从哪里进，经过哪些模块）
  2. Stripe 现有集成（是否已有 stripe 包，版本）
  3. 重试机制（是否有统一的 retry 库，还是各模块自己实现）
  4. 通知系统（现有通知渠道有哪些）
  输出：一个具体的实现计划，列出所有需要改动的文件"

AI 输出：理解当前架构 → 识别关键依赖文件 → 输出执行计划

Step 2: 知识图谱校验（人类 + AI 共同确认）
───────────────────────────────────────────────────
- 确认涉及模块：billing（核心）、notifications（通知）、stripe-client（已有）
- 确认变更范围：3个包内改动 + 1个新文件
- 确认高风险项：billing 变动涉及 8 个下游应用 → 必须通知

Step 3: 小步实现（OpenCode Build Agent 或 Cursor Agent）
─────────────────────────────────────────────────────────
拆分 为 4 个独立 PR：

PR-1: 基础层（stripe-client 增强）
  └─ 新增 stripe/retry-client.ts，封装重试逻辑

PR-2: 核心业务（billing webhook handler）
  └─ 新增 billing/webhooks/stripe-handler.ts
  └─ 修改 billing/types.ts

PR-3: 通知集成
  └─ 修改 notifications/channels/email.ts，支持结构化通知模板

PR-4: 端到端测试 + 文档
  └─ 新增 billing/__tests__/stripe-webhook.test.ts
  └─ 更新 billing/README.md

Step 4: CI/CD 门禁（每个 PR 自动检查）
───────────────────────────────────────────────────
✓ lint + format
✓ 单元测试（覆盖新增代码）
✓ 类型检查
✓ 构建验证
✓ 变更文件数 ≤ 20（防止一次太多改动）

Step 5: Human Review + 合规检查
───────────────────────────────────────────────────
- Co-developed-by 标注检查
- 知识图谱影响范围复核（是否动了高风险模块）
- 确认 Stripe API 版本未破坏性变更
```

### 3.4 第四阶段：持续化 — 让 AI 成为"后台员工"

**这是从"工具"升级到"生产力"的临界点。**

当你有数百万行代码、多个团队、上百个服务时，交互式 AI 助手的瓶颈显现：人类每次只能做一个任务，AI 只能在被调用时工作。

Kelos 的思路提供了一种参考——在你的场景下实现类似效果：

```
触发层（TaskSpawner 等效）
  → GitHub Issue 创建 → AI Agent 自动认领
  → 代码扫描发现 TODO/FIXME → AI Agent 自动评估
  → 监控告警（PagerDuty）→ AI Agent 自动分析根因并给出修复方案

Agent 层
  → 每个 Agent 有固定 Workspace（特定服务/模块的上下文）
  → Agent 之间通过 PR/Issue 通信，而非共享内存
  → 权限受限：只读 → 可以提交 Draft PR → 需要 human review

人类层
  → 最终审批 + Code Review
  → 定义任务边界和验收标准
  → 处理 Agent 无法决策的复杂情况
```

---

## 4. 三类工具的选型决策矩阵

| 维度 | Claude Code | Cursor | OpenCode |
|:---|:---|:---|:---|
| **百万行代码首选场景** | 架构决策 + 复杂代码生成 | 日常 IDE 内增量开发 | 多供应商灵活切换 |
| **上下文策略** | CLAUDE.md + Subagents | Rules 分层 + AI Index | 双 Agent + Auto Compact |
| **知识图谱集成** | 弱（需自建） | 中（语义索引） | 弱（需自建） |
| **团队配置管理** | ✅ Plugins + Hooks | ✅ .cursor/rules/ | ✅ opencode.yaml |
| **K8s 原生集成** | ❌ | ❌ | ❌（Kelos  orchestration 层）|
| **增量开发体验** | Plan Mode 强 | Inline Edit 强 | 双 Agent 流畅 |
| **成本控制** | 中（Anthropic 定价） | 中（订阅制） | 优（BYOK，复用现有订阅）|
| **适合团队规模** | 1-50人 | 1-20人 | 任意规模（灵活性高）|

---

## 5. Linux/K8s 社区做法对你的直接借鉴

### 借鉴 1：从 Linux Kernel 学"AI 治理标准化"

Sasha Levin 的 RFC 揭示的最重要原则：**统一配置，多工具一致**。

你的数百万行代码库应该建立：
```bash
AI_ASSISTANT_CONFIG/
├── CLAUDE.md              # Claude Code 主规约
├── .cursorrules           # Cursor 规则
├── .cursor/rules/         # Cursor 分层规则
├── .opencode/             # OpenCode 配置
└── agent-rules/           # 共享规则（所有工具引用）
    ├── architecture.mdc  # 架构边界
    ├── security.mdc      # 安全规范（禁止直接 SQL、禁止明文密码）
    └── commit-format.mdc  # 提交格式（含 Co-developed-by 规范）
```

所有工具引用同一套规则，保证 AI 行为一致。

### 借鉴 2：从 Kubernetes Kelos 学"AI as Infrastructure"

当你有多个服务、多个团队时，把 AI Agent 变成：
- **不是"助手"，而是"worker"**
- 有固定的工作范围（Workspace）
- 有明确的触发机制（Issue 创建 → 自动认领）
- 有隔离环境（每个 Agent 操作独立分支，不污染主线）
- 有质量门禁（CI 必须通过才能合并）

### 借鉴 3：从 Bito AI Architect 学"知识图谱前置"

ProtonMail 案例的核心洞察：**90 文件重构能成功的关键，不是 Agent 能力更强，而是先建了依赖图谱。**

在你开始任何大规模 AI 辅助开发之前，先花 1-2 周建立代码库的知识图谱，这是回报率最高的投资。

### 借鉴 4：从 Cursor 百万行实践学"并发 Agent 架构"

当你需要做系统级大改动（如整体重构、技术栈升级），Planner/Worker 架构比任何单一工具都重要：
- Planner（强模型）：分析架构、拆解任务、制定计划
- Worker（经济模型）：执行具体模块开发
- Verification：每步完成后自动跑测试套件

---

## 6. 一个具体的启动计划

**第 0-2 周：建立知识图谱（必要前置）**
```bash
# 输出：
# 1. 模块依赖关系图（graph.json）
# 2. 高风险模块清单（被依赖次数最多的前10个模块）
# 3. 每个模块的导出符号表（exports.json）
# 4. 架构决策记录缺失报告（哪些重大决策没有文档）

# 工具选择：
# - tree-sitter（代码解析）
# - graphviz（可视化）
# - 自定义 Python 脚本
```

**第 3-4 周：AI 配置标准化**
```bash
# 输出：
# 1. CLAUDE.md（项目主规约）
# 2. .cursor/rules/（按模块分层的规则文件）
# 3. .opencode.yaml（OpenCode 配置）
# 4. Co-developed-by 规范写入提交规则

# 验证：
# - AI 在两个不同工具里对同一任务的处理是否一致
```

**第 5 周起：增量任务切入**
```bash
# 选一个具体的新需求（而非大重构）
# 用四阶段法执行（Explore → Plan → Implement → Commit）
# 记录：AI 在哪些环节有效、哪些环节需要人类介入
```

**持续优化：**
- 每完成 10 个任务后复盘：知识图谱是否需要更新？
- AI 规则是否覆盖了新发现的模式？
- 是否出现 AI 反复犯的同类错误？（如果是，需要更新 Rules）

---

## 7. 参考文献

- Sasha Levin (Linux Kernel). "RFC: Add AI coding assistant configuration to Linux kernel". LWN.net, 2025-07-25.
- Linux Kernel Documentation. "AI Coding Assistants". docs.kernel.org, 2025.
- k8sgpt-ai. "k8sgpt: Giving Kubernetes Superpowers to everyone". GitHub, 2023.
- GoogleCloudPlatform. "kubectl-ai: AI powered Kubernetes Assistant". GitHub, 2025.
- Kelos Dev Team. "Kelos: Orchestrating Autonomous AI Coding Agents on Kubernetes". DEV Community, 2026-03-15.
- Bito Inc. "The 90-file Monorepo Refactoring That Coding Agents Failed and AI Architect Nailed". Bito Blog, 2026-02.
- A. Verma. "Cursor Just Built a Web Browser with 1 Million Lines of AI-Generated Code". codercops.com, 2026-01-30.
- Flurry Lab. "Architecture and Mechanisms of Repository-Scale AI Coding Agents". Medium, 2026-02.
- B. Kampl. "In Which We Give Our AI Agent a Map (And It Stops Getting Lost)". seylox.github.io, 2026-03-05.
- R. Hightower. "Agent Brain: A Code-First RAG System for AI Coding Assistants". Spillwave, 2026-02.
- Zylos Research. "Monorepo Architecture: Tools, Strategies, and the AI-Driven Renaissance in 2026". zylos.ai, 2026-02-11.

---

*增强版洞察报告 | 虾兵蟹将特工队 🦞*
*核心升级：从"工具对比"深化到"百万行代码的架构级解决方案"*
