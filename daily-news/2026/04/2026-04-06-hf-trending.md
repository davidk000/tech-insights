# HuggingFace 趋势模型简报
**日期**: 2026-04-06 (周一)
**来源**: HF Models Trending + 第三方监测
**数据截至**: 2026-04-06

---

## 一、2026年4月开源大模型最新格局

六强格局已成：Google (Gemma 4)、Alibaba (Qwen 3.6 Plus)、Meta (Llama 4)、Mistral (Small 4)、OpenAI (gpt-oss)、Zhipu AI (GLM-5)。

| 模型 | 机构 | 总参数 | 活跃参数 | 上下文 | 许可证 | 架构 |
|------|------|--------|----------|--------|--------|------|
| GLM-5 | Zhipu AI | 744B | 40B | 200K | MIT | MoE |
| Llama 4 Maverick | Meta | 400B | 17B | 1M | Llama Community | 128-expert MoE |
| Mistral Small 4 | Mistral AI | 119B | 6.5B | 256K | Apache 2.0 | 128-expert MoE |
| gpt-oss-120b | OpenAI | 117B | 5.1B | 128K | Apache 2.0 | MoE (MXFP4) |
| Llama 4 Scout | Meta | 109B | 17B | **10M** | Llama Community | 16-expert MoE |
| Qwen 3.6 Plus | Alibaba | TBD | TBD | **1M** | Apache 2.0 | Hybrid MoE + Linear Attn |
| Gemma 4 31B | Google | 31B | 31B | 256K | **Apache 2.0** | Dense |
| Gemma 4 26B-A4B | Google | 26B | 4B | 256K | Apache 2.0 | MoE |

---

## 二、本周新晋爆款

### 1. Gemma 4 (Google) — ⭐ 本周最大新闻
- **发布时间**: 2026-04-02
- **许可证**: **Apache 2.0** (首次! Google 放弃自有条款)
- **下载量**: 社区热度极高，具体数字待更新
- **四规格覆盖全场景**:
  - `31B Dense`: AIME 2026 89.2%，LiveCodeBench v6 80.0%，256K 上下文
  - `26B-A4B MoE`: 26B 总/4B 活跃，256K 上下文，推理成本大幅降低
  - `4B/2B Edge`: 128K 上下文，原生音频输入，移动端专用
- **亮点**: 首个全规格 Apache 2.0 的 Google 模型；业界最宽的产品线覆盖（手机→数据中心）；密集模型在多项 benchmark 上超越规模更大的 MoE 模型

### 2. Qwen 3.6 Plus (Alibaba) — ⭐ 1M 上下文突破
- **发布时间**: 2026-03-31
- **许可证**: Apache 2.0
- **架构创新**: Hybrid MoE + Linear Attention（线性注意力降低长序列计算成本）
- **上下文**: **1M tokens**（当前开源最高之一）
- **亮点**: 延续 Qwen 家族最强代码能力（LiveCodeBench/SWE-bench）；always-on chain-of-thought；3月底免费预览期驱动快速采用

### 3. Mistral Small 4 — 统一推理/Agent/代码
- **参数**: 119B 总 / 6.5B 活跃，128 experts，4 active per token
- **许可证**: Apache 2.0
- **差异化**: 单一模型支持 adjustable reasoning_effort ("none"→快速响应，"high"→深度推理)
- **效率**: 比 Mistral Small 3 提升 40% 吞吐量；LiveCodeBench 超越 gpt-oss，输出 token 少 20%

### 4. gpt-oss-120b (OpenAI) — OpenAI 首次开源
- **许可证**: Apache 2.0
- **架构**: MoE，MXFP4 量化（4.25 bit/参数），单卡 80GB H100 可部署
- **训练**: RL from o3 + frontier models（蒸馏路线，文本为主，STEM 强）
- **战略意义**: OpenAI 正式承认开源竞争不可逆；GPT tokenzier 生态无缝接入

---

## 三、最热门模型下载排行 (截至2026-02-20)

> 来源: Q4KM.ai / HF 官方数据

| 排名 | 模型 | 下载量 | 机构 | 亮点 |
|------|------|--------|------|------|
| 1 | Qwen2.5-7B-Instruct | **13.3M** | Alibaba | 7B 黄金标准，消费级 GPU 可跑 |
| 2 | Qwen3-0.6B | **10.2M** | Alibaba | 极致轻量，CPU 也能跑 |
| 3 | GPT-2 | 7.9M | OpenAI | 教学/轻量任务常青树 |
| 4 | Qwen2.5-1.5B-Instruct | 6.9M | Alibaba | 性价比最优生产部署 |
| 5 | Qwen2.5-3B-Instruct | 6.8M | Alibaba | 微调首选，质参比突出 |
| 6 | Llama-3.1-8B-Instruct | 5.8M | Meta | Meta 生态最强小模型 |
| 7 | gpt-oss-20B | 5.5M | OpenAI | OpenAI 开源首作 |
| 8 | Qwen2.5-0.5B-Instruct | 5.4M | Alibaba | 极速边缘推理 |
| 9 | Qwen3-4B | 5.1M | Alibaba | Qwen3 新架构入门 |
| 10 | Qwen3-8B | 4.7M | Alibaba | Qwen3 消费级旗舰 |

**关键数据**: Qwen 家族占 top 10 中的 8 席；Qwen2.5-7B-Instruct 连续霸榜

---

## 四、微调/量化方向突破

### 量化新标杆
- **QuantTrio/Qwen3.5-122B-A10B-AWQ**: 122B 模型压缩至 10B 活跃参数，AWQ 量化，显存需求大幅降低
- **unsloth/Qwen3-1.7B-Base-bnb-4bit**: 4bit 量化版，2.3万+总下载，边缘部署首选
- **SamsungSAILMontreal/Qwen3-30B-A3B-Instruct-HCSMoE**: 专家数从 128→96 的结构化压缩（硬件友好）

### 微调生态
- Qwen3-0.6B 微调模型数量激增（HF trending 页面活跃）
- Phi-4-reasoning-vision-15B (Microsoft): reasoning + vision 二合一，Qwen 架构
- OmniVLM-968M (NexaAI): 超轻量多模态，968M 参数

---

## 五、社区增长最快的项目

| 项目 | 类型 | 增长信号 |
|------|------|----------|
| Gemma 4 全系列 | 新模型发布 | 4月2日刚发布，社区热度急速上升 |
| Qwen3-Coder-30B-A3B 微调 | 编程模型 | Fine-tune trending 持续霸榜 |
| gpt-oss | OpenAI 首次开源 | 77 upvote (HF Blog)，5.5M 下载 |
| GLM-5 | 华为昇腾训练 | 744B 最大开源，硬件独立里程碑 |
| transformers v5.5.0 | 框架更新 | 2026-04-02 发布，支持所有新模型 |

---

## 六、本周核心洞察

1. **Apache 2.0 成为主流**: Gemma 4 + Mistral Small 4 + gpt-oss + Qwen 3.6 全部采用 OSI 认证许可证，企业采纳障碍大幅消除
2. **MoE 架构一统天下**: 6强中5个使用 MoE，活跃参数 5B~40B，总参数覆盖 100B~744B
3. **上下文军备竞赛**: Llama 4 Scout 10M > Qwen 3.6 Plus 1M > Mistral Small 4 256K，暴力长上下文不再是专有模型的专利
4. **Qwen 商业统治力**: 下载量 top 10 占 8 席，Apache 2.0 + 全规格覆盖策略成功
5. **华为硬件独立里程碑**: GLM-5 全程在 Ascend 芯片训练，MindSpore 框架，零 NVIDIA 依赖

---

*数据来源: HF Models Trending / Digital Applied (2026-04-03) / Q4KM.ai (2026-02-20) / HF Blog State of Open Source Spring 2026 (2026-03-17) / exa_web_search 实时检索*
