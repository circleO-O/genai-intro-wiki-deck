# Index:生成式 AI 入門 LLM Wiki

主題:生成式 AI 入門,從神經網路、LLM 到 Agent 與工作流程。
來源:10 份課程投影片 PDF(`../raw/`)。共 10 個 source 頁、15 個 concept 頁。

## Sources(每份 PDF 一頁)
| 頁面 | 內容 |
|---|---|
| [01](sources/01-anxiety-free-ai-learning.md) | 如何不焦慮地學 AI:三種焦慮、呆萌型 AI、AI Agent 是教 AI 做事的方法、Colab 入門 |
| [02](sources/02-neural-network-function-learner.md) | 神經網路與函數學習機:one-hot/softmax、神經元、loss、梯度下降、MNIST 實作 |
| [03](sources/03-why-ai-differs-each-time.md) | AI 為什麼每次都不一樣:潛在向量 z、GAN、熵/交叉熵/KL、依機率抽樣 |
| [04](sources/04-llm-next-token-prediction.md) | LLM 猜下一個字:attention、temperature/top-k/top-p、幻覺、embedding、prompt |
| [05](sources/05-attention-transformer-vibe-coding.md) | RNN → QKV attention → Transformer、位置編碼、Vibe Coding 作業 |
| [06](sources/06-build-your-own-chatbot.md) | 打造對話機器人:本地/雲端模型、VRAM、四種 AI 風險、system prompt、AISuite |
| [07](sources/07-rag-memory-llm-wiki.md) | RAG、embedding、chunking、reranking、記憶與 LLM Wiki |
| [08](sources/08-teaching-ai-agents.md) | AI Agent = Model + Harness、四種設計模式、tool use、MCP/A2A |
| [09](sources/09-boss-agentic-work.md) | 換你當老闆:Chat → Agentic、harness 六部件、好的委派、專案資料夾與員工手冊 |
| [10](sources/10-loop-graph-workflow.md) | Loop、Graph、程式檢查 vs AI 審查、Workflow Prototype |

## Concepts(跨來源整合)
**模型怎麼運作**
- [neural-network](concepts/neural-network.md) — 神經網路是函數學習機(01, 02)
- [loss-and-gradient-descent](concepts/loss-and-gradient-descent.md) — 怎麼訓練:loss 與梯度下降(02, 03)
- [softmax-and-sampling](concepts/softmax-and-sampling.md) — 為什麼每次答案不一樣(03, 04)
- [next-token-prediction](concepts/next-token-prediction.md) — LLM 就是猜下一個字(04, 05)
- [attention-transformer](concepts/attention-transformer.md) — 注意力與 Transformer(04, 05)
- [hallucination](concepts/hallucination.md) — 幻覺是特性(04, 06)

**怎麼用模型**
- [prompt-and-system-prompt](concepts/prompt-and-system-prompt.md) — 提示詞與人設(04, 06)
- [rag](concepts/rag.md) — 檢索增強生成(07, 08)
- [memory-and-context](concepts/memory-and-context.md) — 記憶與上下文(07, 05, 08)
- [ai-risks](concepts/ai-risks.md) — 四種 AI 風險(06)

**Agent 與工作流程**
- [ai-agent-harness](concepts/ai-agent-harness.md) — AI Agent = Model + Harness(01, 08, 09)
- [tool-use-and-patterns](concepts/tool-use-and-patterns.md) — 四種設計模式與 tool use(08)
- [loop](concepts/loop.md) — 迴圈與煞車(10)
- [graph-workflow](concepts/graph-workflow.md) — 流程預先畫好的 graph(10, 09)
- [llm-wiki](concepts/llm-wiki.md) — LLM Wiki:raw → wiki(07, 09, 10, 01)

## 已知限制
- 投影片文字層缺字,各 source 頁的「文字層異常處」列出未用圖片核對的頁面;概念頁以「未核對」標記。
- 投影片本身有筆誤與未定義的名詞,見 `log.md` 的 note 條目。
