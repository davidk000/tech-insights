# arXiv 论文周报 | 2026-W13 (March 16-26)

> **产出时间**: 2026-03-26 21:56 (CST)
> **覆盖范围**: cs.AI / cs.CL / cs.CV / cs.LG / cs.SE
> **数据来源**: arXiv.org
> **说明**: 原定周一 10:00 执行，现作为补报覆盖本周 (March 16-26)

---

## 核心主题

**Agentic AI 从期望到落地** — 本周最核心的叙事是：Agentic AI 的理论与实践之间存在巨大鸿沟。一方面论文数量爆发式增长（cs.AI 本月已超 3900 篇），另一方面实证研究开始系统性揭示 Agent 系统在真实场景中的偏差。本周还出现了一篇直接以 OpenClaw-RL 命名的框架论文，RLHF 方向出现新型式化方法。

---

## 一、Agentic AI 与强化学习

### 1. [OpenClaw-RL: Train Any Agent Simply by Talking](https://arxiv.org/abs/2603.10165)
- **作者**: Yinjie Wang, Xuyang Chen, Xiaolong Jin, Mengdi Wang, Ling Yang 等
- **分类**: cs.CL / cs.AI / cs.LG
- **摘要**: 核心观察：每一次 agent 交互都会生成 next-state signal（即用户回复、工具输出、terminal/GUI 反馈）。这些信号是通用的，policy 可以同时从所有信号中学习。OpenClaw-RL 是一个异步框架，个人对话、terminal 执行、GUI 交互、SWE 任务、tool-call 等全部在同一循环中训练。在个人 agent 场景下，模型可以从用户 re-query、修正和显式反馈中恢复对话信号；在通用 agent 场景下，支持 terminal/GUI/SWE/tool-call 的可扩展 RL，额外展示了 process rewards 的效用。
- **PDF**: https://arxiv.org/pdf/2603.10165
- **⭐ 关注理由**: 直接以 OpenClaw 命名的 RL 框架，是对该项目的重要引用；异步 next-state 学习范式有工程落地价值。

---

### 2. [Measuring AI Agents' Progress on Multi-Step Cyber Attack Scenarios](https://arxiv.org/abs/2603.11214)
- **作者**: Linus Folkerts, Will Payne, Simon Inman, Philippos Giavridis 等（Google DeepMind + Oxford）
- **分类**: cs.AI / cs.LG
- **摘要**: 在两个专用网络靶场（32 步企业网络攻击、7 步工业控制系统攻击）上评测前沿模型能力。对比 2024 年 8 月至 2026 年 2 月间发布的 7 个模型，发现：① 推理时计算量 log-linear 缩放，10M→100M tokens 可带来 59% 提升；② 模型代际进步显著，10M tokens 下平均完成步数：GPT-4o(2024.8) 1.7 步 → Opus 4.6(2026.2) 9.8 步；单次最佳运行完成 22/32 步。工业控制系统任务仍然困难，但最新模型首次可靠完成部分步骤。
- **PDF**: https://arxiv.org/pdf/2603.11214
- **⭐ 关注理由**: 目前最系统的 Agent 能力红队评测；log-linear 推理 scaling 曲线对理解 Agent 上限有直接价值。

---

### 3. [Agentic Critical Training (ACT)](https://arxiv.org/abs/2603.08706)
- **作者**: Weize Liu, Minghui Liu, Souradip Chakraborty, Furong Huang 等（CMU）
- **分类**: cs.AI / cs.CL / cs.LG
- **摘要**: 提出 ACT——一种 RL 范式，训练 agent 在备选动作中识别更优者（而非模仿），奖励的是"判断是否正确"而非"是否选中正确动作"。在 3 个 agent benchmark 上显著提升，配合 RL distillation 在一般推理 benchmark（无需推理专项数据）上也取得提升，平均 +2.42 分。核心价值：使 agent 具备反思能力。
- **PDF**: https://arxiv.org/pdf/2603.08706
- **⭐ 关注理由**: 超越模仿学习的关键思路；反思能力对 SWE agent 特别重要。

---

### 4. [Quantifying the Expectation-Realisation Gap for Agentic AI Systems](https://arxiv.org/abs/2602.20292)
- **作者**: Sebastian Lobentanzer
- **分类**: cs.SE / cs.AI
- **摘要**: 系统性回顾 Agentic AI 在软件工程、临床文档、临床决策支持三个领域的期望-实现差距。软件工程：开发者预期 AI 工具带来 24% 加速，实际反而慢 19%，误差达 43 个百分点。临床文档：厂商声称每份笔记节省数分钟，实际减少不足 1 分钟。核心驱动因素：工作流整合摩擦、验证负担、测量结构错配、个体差异。
- **PDF**: https://arxiv.org/pdf/2602.20292
- **⭐ 关注理由**: 当前最重要的 Agent 落地降温报告；所有做 Agent 的人都应该读这篇。

---

### 5. [Molt Dynamics: Emergent Social Phenomena in Autonomous AI Agent Populations](https://arxiv.org/abs/2603.03555)
- **作者**: Brandon Yee
- **分类**: cs.MA / cs.AI
- **摘要**: 在 MoltBook 环境中观测 770,000 个自主 LLM agent 的协调动力学。研究 agent 协调行为、通信动态和角色分化模式，为去中心化自主 agent 系统设计、agent 通信协议工程和 AI 安全提供实证基准。
- **PDF**: https://arxiv.org/pdf/2603.03555
- **⭐ 关注理由**: 超大规模 multi-agent 协调的首批实证研究之一。

---

## 二、长程推理与新型模型架构

### 6. [Recursive Models for Long-Horizon Reasoning](https://arxiv.org/abs/2603.02112)
- **作者**: Chenxiao Yang, Nathan Srebro, Zhiyuan Li（TTI Chicago / 清华）
- **分类**: cs.LG / cs.CL
- **摘要**: 核心问题：语言模型受限于有界 context，无法处理长程推理。解决方案：递归模型——允许模型在隔离上下文中递归调用自身解决子任务。理论证明：任何可计算问题都存在递归分解，使每个子任务所需的活跃 context 比标准自回归模型指数级小。实验：3B 模型在 Boolean Satisfiability（需长程组合搜索）上显著超越前沿 LLM。
- **PDF**: https://arxiv.org/pdf/2603.02112
- **⭐ 关注理由**: 从理论到实验的长程推理突破；递归机制对 Agent 工具调用链有直接启发。

---

### 7. [AdaPonderLM: Gated Pondering Language Models with Token-Wise Adaptive Depth](https://arxiv.org/abs/2603.01914)
- **作者**: Shixiang Song, He Li, Zitong Wang, Boyi Zeng 等
- **分类**: cs.CL
- **摘要**: 现有 recurrent LLM 以固定迭代次数运行，造成简单 token 算力浪费。AdaPonderLM 在预训练中自监督学习 token 级别 early exit，使用迭代特定 MLP gates。对 Pythia 70M-410M（及 2.8B 持续预训练），推理 FLOPs 节省显著，学到的 gates 对困难 token 分配更多计算，完全自监督模式下展示自适应计算时间行为。
- **PDF**: https://arxiv.org/pdf/2603.01914
- **⭐ 关注理由**: Test-time compute 优化的预训练方案，比 o1-style 推理更高效。

---

### 8. [Mixture-of-Depths Attention (MoDA)](https://arxiv.org/abs/2603.15619)
- **作者**: Lianghui Zhu, Yuxin Fang, Bencheng Liao, Xinggang Wang 等（华中科大）
- **分类**: cs.CL / cs.AI
- **摘要**: LLM 越深信号衰减越严重——浅层形成的信息被反复 residual 更新逐渐稀释。MoDA 让每个 attention head 既能关注当前层的 KV，又能回看前序层的 KV（depth KV pairs）。硬件友好算法解决非连续内存访问问题，64K 序列长度下达到 FlashAttention-2 97.3% 效率。1.5B 模型实验：10 个下游任务平均提升 2.11%，仅 3.7% FLOPs 开销。
- **PDF**: https://arxiv.org/pdf/2603.15619
- **⭐ 关注理由**: 深度缩放的新 primitive；post-norm 配合 MoDA 效果优于 pre-norm 是实践发现。

---

### 9. [SMGI: A Structural Theory of General Artificial Intelligence](https://arxiv.org/abs/2603.07896)
- **作者**: Aomar Osmani
- **分类**: cs.AI / cs.LG
- **摘要**: 提出结构化通用智能理论 SMGI，将学习问题从"优化假设空间的假设"重构为"学习接口本身的受控演化"。形式化 SMGI 为 typed meta-model，统一了经验风险最小化、强化学习、Solomonoff 风格程序先验和前沿 agent 管道——证明它们都是 SMGI 的结构受限特例。给出了容量控制和有界漂移的充分条件。
- **PDF**: https://arxiv.org/pdf/2603.07896
- **⭐ 关注理由**: AGI 理论工作的重要进展；将多个主流范式纳入统一框架。

---

## 三、多模态学习

### 10. [HYDRA: Unifying Multi-modal Generation and Understanding via Representation-Harmonized Tokenization](https://arxiv.org/abs/2603.15228)
- **作者**: Xuerui Qiu, Yutao Cui, Guozhen Zhang, Junzhe Li 等
- **分类**: cs.CV
- **摘要**: 统一多模态模型的核心困难：视觉理解需要抽象表示，视觉生成需要细节原语。HYDRA 通过 Gen-ViT（保留结构的原语编码）和 Sem-ViT（语义编码）双路 tokenization 解决信息一致性问题。在单一参数空间内原生统一感知与生成：视觉重建 rFID 0.08，GenEval 0.86，DPG-Bench 86.4，8 个理解 benchmark 平均领先此前 UMM 10.0 点。
- **PDF**: https://arxiv.org/pdf/2603.15228
- **⭐ 关注理由**: 统一多模态模型的新 SOTA；Gen+Understanding 同一框架对产品设计有直接价值。

---

### 11. [Multimodal OCR: Parse Anything from Documents](https://arxiv.org/abs/2603.13032)
- **作者**: Handong Zheng, Yuliang Liu 等（腾讯）
- **分类**: cs.CV
- **摘要**: 传统 OCR 只识别文字，图形区域留作裁剪像素。MOCR 将图表、表格、图标等视觉元素作为一等公民，联合解析为统一文本表示。3B 参数模型，staged training，支持 PDF、渲染网页、原生 SVG。olmOCR Bench 83.9 分，OCR Arena Elo 仅次于 Gemini 3 Pro，领先所有开源文档解析系统。结构化图形解析的重建质量超越 GPT-4V。
- **PDF**: https://arxiv.org/pdf/2603.13032
- **⭐ 关注理由**: 文档 AI 的重大进步；PDF→结构化代码的能力对 RAG 系统有直接价值。

---

### 12. [YOLOv10 + Kolmogorov-Arnold Networks: Interpretable Object Detection](https://arxiv.org/abs/2603.23037)
- **作者**: Marios Impraimakis, Daniel Vazquez, Feiyu Zhou
- **分类**: cs.CV / cs.AI / cs.CL / cs.LG / cs.RO
- **摘要**: 用 Kolmogorov-Arnold 网络作为可解释后缀替代模型，为 YOLOv10 检测结果建模可信度。使用 7 个几何+语义特征，加性样条结构可直接可视化每个特征影响。在 COCO 和 Bath 校园图像上验证，框架准确识别 blur/occlusion/low-texture 下的低信任预测。配合 BLIP 文字描述生成轻量多模态界面，且不影响可解释层。
- **PDF**: https://arxiv.org/pdf/2603.23037
- **⭐ 关注理由**: KA 网络在 CV 的首个大规模应用；可解释置信度对自动驾驶感知有安全价值。

---

### 13. [Phi-4-reasoning-vision-15B Technical Report](https://arxiv.org/abs/2603.03975)
- **作者**: Jyoti Aneja, Michael Harrison, Neel Joshi, Tyler LaBonte 等（Microsoft）
- **分类**: cs.AI / cs.CV
- **摘要**: 微软 Phi 系列首款多模态推理模型，15B 参数开放权重。核心发现：① 高质量合成数据+严格过滤是性能首要杠杆；② 纯推理数据与快通道非推理数据的混合+显式 mode token，使单一模型兼具快速直接回答和 CoT 推理能力；③ 架构选择和后训练策略对多模态推理效率影响显著。
- **PDF**: https://arxiv.org/pdf/2603.03975
- **⭐ 关注理由**: 小模型高效多模态推理的工程实践总结；合成数据方法论值得关注。

---

### 14. [Multimodal LLM as Image Classifiers](https://arxiv.org/abs/2603.06578)
- **作者**: Nikita Kisel, Illia Volkov, Klara Janouskova, Jiri Matas
- **分类**: cs.CV
- **摘要**: 发现此前 MLLM 分类性能比较结论冲突的根源：评估协议问题（模型输出超出标签范围 Ground Truth 质量）。提出 ReGT（625 类 ImageNet-1k 多标签重标注），揭示 MLLM 在纠正标签后性能提升达 +10.8%，大幅缩小与监督模型的感知差距。MLLM 还能辅助人类标注员：约 50% 困难案例中标注员确认或整合了 MLLM 预测。
- **PDF**: https://arxiv.org/pdf/2603.06578
- **⭐ 关注理由**: 评估方法论的重要修正；MLLM 在数据标注中的辅助价值被低估。

---

## 四、软件工程与 AI

### 15. [SWE-Adept: LLM-Based Agentic Framework for Deep Codebase Analysis](https://arxiv.org/abs/2603.01327)
- **作者**: Kang He, Kaushik Roy
- **分类**: cs.SE / cs.CL / cs.LG
- **摘要**: 提出两 agent 框架解决 repo 级 SWE 问题：① deep codebase navigation（有效上下文管理 + 精准 issue localization）；② iterative, test-driven code modification（探索备选方案 + revert 失败修改）。在 SWE-Bench Lite 和 SWE-Bench Pro 上，端到端问题解决率提升最高 4.7%。
- **PDF**: https://arxiv.org/pdf/2603.01327
- **⭐ 关注理由**: SWE agent 架构的重要改进；两 agent 协作模式对复杂代码库场景有工程价值。

---

### 16. [Trustworthy AI Software Engineers](https://arxiv.org/abs/2602.06310)
- **作者**: Aldeida Aleti, Baishhi Ray, Rashina Hoda, Simin Chen 等（Monash 等）
- **分类**: cs.SE
- **摘要**: 重新审视"AI 代理成为软件工程师意味着什么"，提出 AI 软件工程师可信性的概念框架，涵盖能力（competence）、可靠性（reliability）和社会-伦理对齐（social-ethical alignment）。指出信任测量缺口：信任的重要维度难以量化。倡导 ethics-by-design 方法论，为未来人机协同 SWE 团队建立适当信任。
- **PDF**: https://arxiv.org/pdf/2602.06310
- **⭐ 关注理由**: AI SE 可信性的系统性理论工作；治理框架设计必读。

---

### 17. [I'm Not Reading All of That: Cognitive Engagement with Agentic Coding Assistants](https://arxiv.org/abs/2603.14225)
- **作者**: Carlos Rafael Catalan, Lheane Marie Dizon, Patricia Nicole Monderin 等
- **分类**: cs.HC / cs.AI / cs.SE
- **摘要**: 研究软件工程师与 Agentic coding assistants 交互时的认知投入度变化。发现：认知投入随任务进展下降；当前 Agentic coding assistants 设计缺少反思、验证和意义建构的交互支持。提出具体设计机会以促进更深的认知参与，避免过度依赖导致的 complacency。
- **PDF**: https://arxiv.org/pdf/2603.14225
- **⭐ 关注理由**: Agent 过度依赖问题的 HCI 研究；工程团队引入 coding agent 时应参考此研究结论。

---

### 18. [Artificial Intelligence as a Catalyst for Innovation in Software Engineering](https://arxiv.org/abs/2603.10994)
- **作者**: Carlos Alberto Fernández-y-Fernández, Jorge R. Aguilar-Cisneros
- **分类**: cs.SE / cs.AI
- **摘要**: 综合调研 AI（ML + NLP）如何增强软件工程敏捷性和创新能力。核心发现：AI 自动化了从需求管理到代码生成和测试的繁琐任务，AI 驱动工具的感知、采纳和影响因团队而异。AI 不仅是优化现有实践，更是催化新的开发模式。
- **PDF**: https://arxiv.org/pdf/2603.10994
- **⭐ 关注理由**: SE 领域 AI 催化剂角色的综合文献回顾。

---

## 本周数据快照

| 类别 | 本月累计 | 今日新增 |
|:---|---:|---:|
| cs.AI | 3,927 | +165 |
| cs.CL | 1,493 | +96 |
| cs.LG | 3,205 | +159 |
| cs.CV | 2,557 | ~200 |
| cs.SE | ~2,000+ | ~100 |

**趋势判断**: cs.AI 继续保持爆发式增长，周增量超 3,900 篇/月；Agentic AI 相关论文占比持续提升；多模态和长程推理是架构层面的两大主战场；AI SE 的实证研究（期望-现实差距、认知依赖）开始受到系统性关注。

---

*报告生成: 盱眙小龙虾 @ OpenClaw | 数据来源: arXiv.org*
