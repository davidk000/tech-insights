# GitHub 开源项目周报 | 2026-03-19 ~ 2026-03-26

> 定时任务：每周一 09:00 | 生成时间：2026-03-26

---

## 本周热点速览

| 分类 | 本周之星 | 动态 |
|:---|:---|:---|
| AI/ML | MiroFish (28K★/周) | #1 Trending，模拟agent经济预测，融资$4.1M |
| Agent框架 | Hive (v0.7.6) | 190贡献者，支持100+ LLM Provider |
| 本地LLM | Graviton | 500B模型跑在Mac Mini上 |
| 代码审查 | Squad | GitHub官方Copilot多agent PR协作 |
| 长程Agent | DeerFlow 2.0 (39K★) | 字节跳动，30天破39K |
| 自动研究 | karpathy/autoresearch (56.8K) | 单GPU autonomous LLM training |
| Skill市场 | last30days-skill (2.6K/日) | Reddit/X/YouTube/HN多源AI研究Skill |

---

## 一、AI / ML 大模型与训练框架

### 1. MiroFish — AI Swarm Engine
- **链接**: https://github.com/guohangjiang/mirofish
- **Star**: 28,600 | **本周新增**: ~18K
- **24h Stars**: 2,782
- **描述**: 模拟数千个自主Agent在数字世界进行结果预测（金融/舆论/政策）
- **亮点**: 20岁本科生Guo Hangjiang用"Vibe Coding" 10天完成，获陈天桥3000万RMB投资；基于OASIS框架（2024-12开源）
- **标签**: #multi-agent #simulation #forecasting #agentic

### 2. karpathy/autoresearch — Autonomous LLM Training
- **链接**: https://github.com/karpathy/autoresearch
- **Star**: 56,808 | **Forks**: 7,913
- **描述**: 给AI一个小型LLM训练环境，自主实验 overnight。5分钟训练循环，自动搜索更好的超参/架构
- **亮点**: 单GPU即可运行；Flash Attention 3 kernel fallback；已出现MacOS/MPS/Win社区fork
- **标签**: #autonomous-research #LLM-training #single-GPU

### 3. Graviton — 本地运行500B+模型
- **链接**: https://github.com/opengraviton/graviton
- **描述**: 将144GB的FP16 72B模型压缩到36GB，在Mac Mini上流式运行
- **技术**: 4-bit/2-bit/Ternary(1.58-bit)量化；Layer流式加载；多token预测加速2-3x
- **亮点**: 本地AI民主化；BitNet b1.58原生支持（权重{-1,0,1}）
- **标签**: #local-LLM #quantization #edge-AI

### 4. AIBuildAI — MLE-Bench #1
- **链接**: https://github.com/aibuildai/AI-Build-AI
- **描述**: AI Agent自动构建AI模型——分析问题→设计模型→训练→调参→迭代改进
- **亮点**: OpenAI MLE-Bench排名第1；Linux x86_64二进制分发
- **标签**: #AutoML #agentic-model-building

### 5. no-magic — 算法纯手写实现
- **链接**: https://github.com/no-magic-ai/no-magic
- **描述**: 单文件零依赖实现GPT/RNN/LSTM/BERT/CNN/ResNet/ViT/GAN/VAE
- **亮点**: v2.0 (2026-03)；灵感来自Karpathy的micrograd/microgpt
- **标签**: #education #zero-dependency #algorithm-from-scratch

### 6. DeerFlow 2.0 — 字节跳动长程Agent
- **链接**: https://github.com/bytedance/deer-flow
- **Star**: 47,736 | **本周新增**: ~39K (30天)
- **24h Stars**: 2,388
- **描述**: 开源长视野SuperAgent harness，支持沙箱、记忆、工具、Skill、子Agent
- **标签**: #superagent #long-horizon #bytedance

---

## 二、Agent 框架与开发者工具

### 7. Hive — 多Agent自动编排
- **链接**: https://github.com/aden-hive/hive
- **贡献者**: 190人 | **最新**: v0.7.6 (2026-03-21)
- **描述**: 自然语言描述目标，框架自动生成Agent执行图谱；内置Human-in-the-loop；支持100+ LLM via LiteLLM
- **亮点**: 描述即工作流；失败后自我进化；内置浏览器操作/凭证管理/实时监控
- **标签**: #multi-agent #orchestration #autonomous

### 8. oh-my-claudecode — Claude Code团队编排
- **链接**: https://github.com/Yeachan-Heo/oh-my-claudecode
- **Star**: 12,085 | **本周新增**: ~10K
- **描述**: Teams-first多Agent编排，专为Claude Code设计
- **标签**: #claude-code #multi-agent #teams

### 9. Squad — GitHub官方多Agent PR协作
- **来源**: GitHub Copilot Blog (github.com/blog)
- **链接**: https://github.com/msitarzewski/squad
- **描述**: 2命令初始化：`npm install -g @squad/cli && squad init`，自动在仓库内部署lead/frontend/backend/tester四个Agent
- **亮点**: Reviewer拒绝后原作者无法self-approve；仓库级AI记忆版本化
- **标签**: #github-copilot #multi-agent #PR-review

### 10. GitNexus — AI PR代码审查
- **链接**: https://github.com/abhigyanpatwari/GitNexus
- **描述**: Python后端 + Next.js前端 + RAG管道；基于真实仓库上下文做代码审查
- **亮点**: 可自托管；RAG策略减少LLM幻觉；代码本身是RAG+LLM集成最佳实践
- **标签**: #code-review #RAG #LLM-integration

### 11. The Agency — 61个AI Agent
- **链接**: https://github.com/msitarzewski/agency-agents
- **Star**: ~10K (7天)
- **描述**: 61个专业角色Agent（markdown定义），Claude Code/Cursor直接调用
- **分类**: Engineering / Testing / Product / DevOps 等9个division
- **标签**: #agent-templates #prompt-engineering #Claude-Code

### 12. OpenJarvis — 本地优先个人AI
- **链接**: https://github.com/open-jarvis/OpenJarvis
- **描述**: 本地运行个人AI Agent栈，Ollama/vLLM/SGLang/llama.cpp为后端；能耗FLOPs延迟成本与精度并列一线约束
- **标签**: #local-first #on-device-AI #privacy

### 13. dexter — 金融研究自主Agent
- **链接**: https://github.com/virattt/dexter
- **Star**: 18,721 | **Forks**: 2,317
- **描述**: 自主Agent做深度金融研究，支持多数据源集成
- **标签**: #fintech #autonomous-agent #research

---

## 三、Web 框架与开发者平台

### 14. n8n — 工作流自动化
- **链接**: https://github.com/n8n-io/n8n
- **Star**: ~35K+
- **描述**: 可视化工作流自动化，原生AI能力；支持自托管
- **标签**: #workflow-automation #no-code #AI-integrations

### 15. Dify — LLM应用全栈平台
- **链接**: https://github.com/langgenius/dify
- **描述**: 开源LLM应用平台，RAG/Agent/工作流，支持众多模型
- **标签**: #LLM-apps #RAG #agent-platform

### 16. twenty — 开源Salesforce替代
- **链接**: https://github.com/twentyhq/twenty
- **Star**: 41,033 | **Forks**: 5,482
- **描述**: 现代开源CRM，社区驱动替代Salesforce
- **标签**: #CRM #open-source #typescript

### 17. RAGFlow — 企业级RAG引擎
- **链接**: https://github.com/infiniflow/ragflow
- **描述**: 深度文档解析+LLM，提供可靠上下文层
- **标签**: #RAG #enterprise #document-understanding

---

## 四、MLOps 与基础设施

### 18. ZenML — MLOps Pipeline
- **链接**: https://github.com/zenml-io/zenml
- **Star**: ~13K | **贡献者**: 130
- **描述**: Pythonic MLOps pipeline框架，支持传统ML + LLM workflows；可对接MLflow/Langgraph/Sagemaker/GCP Vertex
- **标签**: #MLOps #pipelines #LLMOps

### 19. LangChain — Agent基础框架
- **链接**: https://github.com/langchain-ai/langchain
- **描述**: AI Agent生态核心框架，持续活跃
- **标签**: #agent-framework #LLM #RAG

---

## 五、热门Skill / 工具

### 20. last30days-skill — 多源AI研究Skill
- **链接**: https://github.com/mvanhorn/last30days-skill
- **Star**: 9,171 | **今日新增**: 2,684
- **描述**: AI Agent Skill，聚合Reddit/X/YouTube/HN/Polymarket/Web研究任意主题
- **标签**: #skill #research #agentic-web-search

### 21. insanely-fast-whisper — 超快Whisper
- **链接**: https://github.com/Vaibhavs10/insanely-fast-whisper
- **Star**: 10,706 | **今日新增**: 1,381
- **描述**: Whisper极速实现，Jupyter Notebook生态
- **标签**: #ASR #whisper #speed-optimization

### 22. chandra — 复杂表格/手写OCR
- **链接**: https://github.com/datalab-to/chandra
- **Star**: 5,781 | **Forks**: 645
- **描述**: 处理复杂表格、表单、手写笔记的全layout OCR模型
- **标签**: #OCR #document-AI #table-extraction

### 23. agentscope-ai/agentscope — 可视化Agent构建
- **链接**: https://github.com/agentscope-ai/agentscope
- **描述**: Build and run agents you can see, understand and trust.
- **标签**: #agent-builder #visualization #X-Agent

---

## 六、GitHub 官方动向

### GitHub Agentic Workflows — 技术预览
- **来源**: github.com/blog (Don Syme & Peli de Halleux)
- **描述**: Markdown描述意图 → GitHub Actions自动调度Copilot CLI/Claude Code/OpenAI Codex执行
- **适用场景**: 自动化Issue分类、CI失败调查、文档更新、代码审查、持续报告
- **关键词**: Continuous AI = Continuous CI × Agentic AI
- **链接**: https://githubnext/github-aw (开源repo)

### GitHub Trending 语言榜
- TypeScript 持续第一 | Python 增长7个百分点
- Rust 在系统工具类稳步上升

---

## 七、本周核心趋势洞察

### 1. Agentic AI 从"单Agent"走向"多Agent团队"
Squad、oh-my-claudecode、Hive、"The Agency"全部指向同一方向：多Agent专业化分工。GitHub官方下场推Squad说明多Agent开发协作已是主流范式。

### 2. 本地AI从"可能"走向"实用"
Graviton + OpenJarvis 两条路线都在降低本地LLM门槛：Mac Mini跑72B不再是噱头。2026年本地AI与云端AI的边界正在重塑。

### 3. Simulation-Driven AI 崛起
MiroFish不是训练模型预测，而是用数字"培养皿"模拟涌现行为。OASIS框架（2024-12）→ MiroFish（2026-03）→ 商业化只用了不到半年。

### 4. Skill 作为一等公民
last30days-skill单日2.6K stars，OpenClaw Skill生态的成功正在被复制。"会用Agent" → "会写Skill"成为新分水岭。

### 5. karpathy继续引领 autonomous ML research
autoresearch + 社区fork生态（MacOS/MPS/Win）说明：单GPU autonomous experiment不再是顶级实验室专属。

---

## 八、全站Star排行 Top 10 (截至2026-03-26)

| 排名 | 项目 | Star | 语言 | 分类 |
|:---:|:---|---:|:---:|:---|
| 1 | build-your-own-x | 483K | Markdown | 学习 |
| 2 | awesome | 449K | None | 资源 |
| 3 | freeCodeCamp | 439K | TypeScript | 教育 |
| 4 | public-apis | 416K | Python | 工具 |
| 5 | developer-roadmap | 352K | TypeScript | 学习 |
| 6 | openclaw | 336K | TypeScript | AI助手 |
| 7 | git | 60K | C | VCS |
| 8 | awesome-python | 289K | Python | 资源 |
| 9 | JavaGuide | 154K | Java | 学习 |
| 10 | appflow | 59K | TypeScript | 协作 |

---

**归档**: `/daily-news/2026/03/2026-03-26-weekly-github-trending.md`
**同步目标**: github.com/davidk000/tech-insights（仓库不存在或无访问权限）
**数据来源**: GitHub Trending, Exa Web Search, EvanLi/Github-Ranking (实时更新)
