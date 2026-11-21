---
title: 工具呼叫與 Agent 設計模式
type: concept
sources: [08]
---

# 工具呼叫與 Agent 設計模式

## 一句話定義
吳恩達提出四個 Agent 設計模式:Reflection、Tool Use、Planning、Multiagent Collaboration;其中 Tool Use 是讓 LLM 把不擅長的事交給呼叫工具(函式)處理。[S08 p.18][S08 p.22]

## 白話解釋(給完全沒學過的人,可用講者的比喻)
- 一次寫完的 prompt 好比要人寫文章卻不能用刪除鍵、不能修改;人類喜歡「邊寫、邊試、邊改」。[S08 p.9][S08 p.10]
- 老闆(你)一句話,員工(AI Agents)動起來。[S08 p.16]
- 飲料店 ChatBot:顧客說「我想訂 20 杯麥茶」,Bot 答「沒問題!20 杯麥茶共 600 元」。[S08 p.24] LLM 不太會做精確計算、實際數據、網路搜尋,就不要再逼它,改呼叫工具。[S08 p.23]
- JSON 基本上是用文字描述「有欄位名稱的資料表單」,電腦很喜歡這種格式。[S08 p.28]
- 多 Agent 像公司:常有一位 PM 角色的 LLM 分配工作,1 號算、2 號查資訊、3 號依資訊分析理由。[S08 p.38]

## 重點
### 四個設計模式
- **Reflection**:第一個 LLM 產生初稿,第二個 LLM 評估並提供改善建議,第一個再修改,可重覆數次;「評論員」可用不同模型。[S08 p.19][S08 p.20][S08 p.21]
- **Tool Use**:不是 LLM 擅長的或不會的事,呼叫工具來幫忙。[S08 p.22]
- **Planning**:先請 LLM「想一想」、「打草稿」再正式回應。[S08 p.32][S08 p.33]
  - CoT(Chain-of-Thought)是有名的例子:有系統地拆解複雜議題、找出關聯、更完整涵蓋各面向、容易看出優先順序。[S08 p.34]
  - CoT 是讓 DeepSeek-R1 厲害的關鍵:先產生「思考」,用 `<think>` 和 `</think>` tag 包起來。[S08 p.35]
  - 此類模型目標是任何問題都能產生好思維;若只針對單一類型任務,有可能打造更好的「思考」。[S08 p.36]
- **Multiagent Collaboration**:多個 AI Agent 一起合作。[S08 p.37]

### Tool Use 的流程(以 JSON 為載體)
1. 先告訴 AI 有哪些工具(函式):`get_menu` 回傳 menu;`quote_order` 輸入品項、杯數,回傳單價、總金額、庫存是否足夠等。[S08 p.25]
2. LLM 第一階段決定要呼叫的工具,例如 `quote_order("麥茶", 20)`。[S08 p.26]
3. 工具被呼叫後回傳 JSON(ok、item_name、quantity、unit_price=30、total=600、stock=30、currency=TWD、ordered=false)。[S08 p.27]
4. 第二階段把數據放進 prompt,請 LLM 依資料回答使用者,輸出「沒問題!20 杯麥茶共 600 元」。[S08 p.29]
- 工具不一定要自己寫,許多平台可連結工具,例如上網搜尋、你的 email,甚至處理桌面檔案。[S08 p.30]

### MCP 與 A2A
- MCP(Anthropic,Model Context Protocol):與外部世界溝通;關注單一 Agent 如何規劃與使用外部工具,標準化 LLM 與外部工具、資料來源或環境的互動方式。[S08 p.31]
- A2A(Google,Agent-to-Agent):代理之間溝通;定義代理之間交換資訊、協作和協調的方式。[S08 p.31]

### Vibe Coding 與使用上的提醒
- Vibe Coding 是 Karpathy 於 2025 年 2 月在 X 發文所創的新詞。[S08 p.43]
- 原文要點:完全順從 vibes、忘了程式碼存在、一律「Accept All」不再看 diff、遇錯誤訊息就複製貼上。[S08 p.44][S08 p.45]
- 講者強調 Vibe Coding ≠ AI 輔助寫程式。[S08 p.47]
- 適合:週末好玩的小專案、給自己用且出錯不會怎樣的小工具、試做原型並與程式設計師討論。[S08 p.50]
- 不適合:要正式上線的程式(不是有 Vibe Coding 老闆就可以 fire 掉工程師)、不檢查可能出亂子的程式。[S08 p.51]
- 說 Karpathy 對 Vibe Coding 有意見是誤讀;AI 時代三種寫程式方式為純手工、人類主導加自動補全、Vibe Coding。[S08 p.52]

## 與其他概念的關係
- 工具、連接器 MCP 是 harness 的組成,見 [[ai-agent-harness]]。
- 工具呼叫是讓 LLM 補足不擅長的事,LLM 本身的運作見 [[next-token-prediction]];RAG 也被視為 Agent,見 [[rag]]。[S08 p.14]
- Planning / CoT 與 DeepSeek-R1 相關;「推理」的風險討論見 [[ai-risks]]。
- Prompt 與 Context 的做法見 [[prompt-and-system-prompt]]、[[memory-and-context]]。[S08 p.11]
- 多步驟的迴圈與圖形化流程見 [[loop]]、[[graph-workflow]](本頁不展開)。

## 來源差異或矛盾
- 無實質矛盾。注意事項:S09 p.5 提到手刻 Agent 涵蓋 Reflection、Tool Use、Planning 三項 [S09 p.5],S08 p.18 為四項,應是範圍不同,並非衝突。
- 核對狀態(2026-11-21 更新):S08 p.18-21、p.23、p.24、p.26、p.27、p.29 已由獨立審查以頁面圖片核對,內容成立(細節:p.18 只在四個模式旁標示「吳恩達」,未寫「提出」;p.23 內文為「LLM 不太會做的事,就不要再逼他了」,「改呼叫工具」是由標題【Tool Use】推得;p.24、p.29 原文為「一共 600 元」)。p.25、p.28、p.30、p.32-38、p.43-49 仍僅依文字層(未核對)。p.31、p.50-52 先前已核對。
