---
title: RAG(檢索增強生成)
type: concept
sources: [07, 08]
---

# RAG(檢索增強生成)

## 一句話定義
RAG(Retrieval-Augmented Generation)是先找出相關資料再交給 LLM 生成回答,被定位為「一個降低錯誤的方法」[S07 p.3];講者說它其實就是在討論 Content Engineering:提供正確資訊與給清楚指引 [S07 p.5]。

## 白話解釋(給完全沒學過的人)
- 媒體標題把 RAG 比喻成大型語言模型的「小抄」[S07 p.4]。
- 講者設問:資訊可以自己貼進 prompt,但「不能叫電腦找嗎?」RAG 就是讓電腦去找 [S07 p.5]。
- 做法:把每段文字變成代表它意思的向量,問題也變成向量,誰最接近就把誰放進 prompt [S07 p.18][S07 p.19][S07 p.20]。
- 例子:問「圖書館星期日幾點關門?」,相關內容是「本館週日開放至下午五點。」,不相關的是「本館借書期限為三十天。」[S07 p.7]

## 重點
### Embedding
- 關鍵是找一個 embedding 模型:把一段文字轉成某維度的向量,這向量是該段文字的特徵代表向量、抽象意涵;它基本上就是一個語言模型 [S07 p.6]。
- 訓練時有時用對比學習:問題 q、相關內容 k⁺、不相關內容 k⁻,sim(q, k⁺) 越近越好、sim(q, k⁻) 越遠越好 [S07 p.7];損失函數寫成 ℒ(θ) = −log( e^{sim(q,k⁺)} / Σ e^{sim(q,k)} ) [S07 p.8]。
- 有些模型會用 query: / passage: 前綴區分問題與內容,但沒有通用寫法,有些模型完全沒用 [S07 p.9]。

### 資料前處理:切塊與 metadata
- 最傳統做法是把檔案全放進一個資料夾(純文字、PDF、Word 都可以)[S07 p.10]。
- 傳統 RAG 自動把文件切成文字塊(例:500 字一塊、重疊 50 字);要考慮多少字一塊、需不需要重疊 [S07 p.11]。切分考量包含塊大小、怎麼切(如法條是否一條一條切)、重疊多少 [S07 p.12]。
- 較新做法是自己切成想要的樣子:每塊含標題、metadata(資料類型、主管機關、來源網址、整理日期)、內容、檢索練習問題、提醒;標題與內容做 embedding,metadata 另外標示 [S07 p.13]。
- 實際上有兩部分:做 RAG(Embedding)的文字,與可做關鍵字搜尋的 metadata [S07 p.14]。
- Metadata 例如來源、頁數、文章標題、作者、日期、分類 [S07 p.15];需要它的例子:想知道 AI Agents 但不要某位老師的說法,就要依作者過濾 [S07 p.16]。

### 完整流程
1. 整理好的文件放進資料夾 [S07 p.17];每段文字經模型 f_θ 得到代表向量 k₁、k₂、k₃ [S07 p.18]。
2. 使用者的問題經同一模型得到 q [S07 p.19]。
3. 比較 q 與各 k 找最接近、最相關的資料放進 prompt [S07 p.20]。
4. 找出的資料通常不只一筆,可能需要重新排序,即 Reranking [S07 p.21]。
5. 可考慮補上下文,三種做法:加前一塊與後一塊;整篇文章;相關文章 [S07 p.22]。
6. 組 prompt 有兩項資訊:question 與 retrieved_chunks [S07 p.23];例如「請根據 {retriever_chunks} 裡的資訊,來回應使用者的問題: {question}」[S07 p.24](p.23-24 僅憑文字層,未逐頁看圖)。
- 講者總結以上就是現在火紅的 RAG 概念 [S07 p.25]。

### RAG 與 Agent
- S08 說 RAG 其實也是一種 AI Agent:「正確的資訊」由電腦自動找到 [S08 p.14]。
- S08 的 Context Engineering 要做的事:給正確的資訊(可能要查規定、按計算機、上網搜尋)與清楚的指引 [S08 p.11]。
- 多個 AI 幫忙時,可用 RAG 找內部相關資訊 [S08 p.15];Agent 架構圖中有 RAG1、RAG2 [S08 p.16]。

### 作業
- 打造自己的 RAG 強化對話機器人:程式 1 建向量資料庫、程式 2 實作 RAG [S07 p.50];流程要求見 [S07 p.51]。

## 與其他概念的關係
- [[prompt-and-system-prompt]]:RAG 最後一步是把檢索結果組進 prompt [S07 p.23-24],與 prompt 兩原則(資訊 + 指引)同構 [S07 p.5][S04 p.100]。
- [[memory-and-context]]:長期記憶可用 RAG 達成 [S07 p.33];也可考慮 CAG,把資訊全放進去 [S07 p.26][S07 p.27]。
- [[hallucination]]:RAG 被定位為降低錯誤的方法 [S07 p.3]。
- [[loss-and-gradient-descent]]:embedding 的對比學習有自己的損失函數 [S07 p.8]。
- [[attention-transformer]]:KV-Cache 存的是 k、v [S07 p.28],即注意力 QKV 中的 k、v [S05 p.17];見 [[memory-and-context]]。
- [[ai-agent-harness]]、[[tool-use-and-patterns]]:RAG 視為一種 Agent [S08 p.14]。
- [[llm-wiki]]:Karpathy 原以為需複雜 RAG,但約 100 篇文章、約 40 萬字的 Wiki 規模下,LLM 自維護索引與摘要也表現不錯 [S07 p.41](僅憑文字層)。

## 來源差異或矛盾
- 用詞:S07 寫 Content Engineering [S07 p.5],S08 標題拼為 Content Engineering,內文稱 Context Engineering [S08 p.11];兩者內容一致(正確資訊 + 清楚指引)。
- 其餘無矛盾。
