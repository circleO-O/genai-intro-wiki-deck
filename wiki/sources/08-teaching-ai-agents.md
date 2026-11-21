---
title: 08 教 AI 做事的方法:AI Agent 與 Agentic Design Patterns
type: source
sources: [08]
---

# 08 教 AI 做事的方法:AI Agent 與 Agentic Design Patterns

來源:`raw/08教AI做事的方法.pdf`(共 56 頁)

## 主題
說明「AI Agent」其實就是「教 AI 用我們做事的方法做事情」,定義為 AI Model + Harness [S08 p.4];接著介紹吳恩達(Andrew Ng)提出的四個 Agent 設計模式(Reflection、Tool Use、Planning、Multiagent Collaboration)[S08 p.18],最後是進階學習(Karpathy 訪談、Vibe Coding、Hinton)[S08 p.39-55]。

## 章節脈絡
- p.1-2:標題頁與第一部分「AI Agents 教 AI 做事的方法」(章節 01)。
- p.3-7:AI Agent 的定義與地位(2025 AI 元年、Russell & Norvig 定義、本課定義、各種 Engineering 名詞、吳恩達推廣)。
- p.8-16:從單次 prompt 到 Agent:為何人類與 LLM 都需要「邊寫邊改」、Context Engineering 要做的事、RAG 也是一種 Agent、老闆(你)一句話,員工(AI Agents)動起來。
- p.17-18:第二部分「AI Agent 的設計模式」(章節 02),列出四個模式。
- p.19-21:Reflection。
- p.22-31:Tool Use(含飲料店 ChatBot 範例、JSON、MCP / A2A)。
- p.32-36:Planning(含 CoT、DeepSeek-R1)。
- p.37-38:Multiagent Collaboration。
- p.39-55:第三部分「進階學習」(章節 03):Karpathy、LLM 訓練三階段、Vibe Coding、Hinton。
- p.56:末頁(僅頁尾,無實質內容)。

## 重點
- 投影片引用 Russell & Norvig《Artificial Intelligence: A Modern Approach》的定義:代理人是任何能夠透過感測器感知其環境,並透過致動器對該環境採取行動的實體。[S08 p.3]
- 很多人說 2025 是 AI 元年;提問「AI Agents 到底是什麼」。[S08 p.3]
- 本課的定義:在 LLM 時代,基本上就是教 AI 用「我們做事的方法」做事情;AI Agent = AI Model + Harness。[S08 p.4]
- 名詞層次:Chat Bot 對應 Prompt Engineering、Context Engineering;AI Agent 對應 Harness Engineering、Loop Engineering、Graph Engineering(圖中 Context Engineering 位於兩個框的交界處);講者說我們會學到 AI Agent 其實只是「教 AI 做事的方法」。[S08 p.5]
- 吳恩達自 2024 年就開始推動 agentic workflows(投影片放其與 AI Fund 的影片截圖)。[S08 p.7]
- 以前對 LLM 下 prompt,LLM 直接回答、產生輸出(Prompt → LLM → Outputs)。[S08 p.8]
- 這種一次寫完的方式對人也不容易:好比要人寫一篇文章,卻不可以用刪除鍵、不能修改,一路寫下去。[S08 p.9]
- 人類喜歡「邊寫、邊試、邊改」,寫程式也是如此。[S08 p.10]
- 做好 Context Engineering 時要做不少事:「正確的資訊」——LLM 不知道你腦中的背景,該給的資料、條件要講清楚,可能要查規定、按計算機、上網搜尋;「清楚的指引」——要它做什麼、輸出成什麼樣子、給誰看,講明白。[S08 p.11]
- 此外也可能不時和 LLM 溝通、請它修改(例如指出哪個地方實際情況為何、請它改某處)。[S08 p.12]
- AI Agent 是把「本來你要做的」交給 AI 自動做完:舉凡規劃、收集資料、不斷迭代嘗試等,告訴它怎麼做,它來做。[S08 p.13]
- RAG 其實也是一種 AI Agent:「正確的資訊」這件事由電腦自動找到相關資訊;「我們已經碰過 AI Agent 了哦」。[S08 p.14]
- 現在更多事可由多個 AI 幫忙:用 RAG 找內部相關資訊、上網收集資料、按計算機檢查數字、檢查寫出來的東西。[S08 p.15]
- 圖示:老闆(你)一句 Prompt,員工(AI Agents:plan、RAG1、RAG2,加上 tools、memory)動起來,再由 LLM 產生 Outputs。[S08 p.16]
- 吳恩達的四個 Agent 設計模式:Reflection、Tool Use、Planning、Multiagent Collaboration。[S08 p.18]
- Reflection:第一個 LLM 產生初稿,第二個 LLM 進行評估並提供改善建議,然後第一個 LLM 進行修改,可重覆數次。[S08 p.19]
- Reflection 圖示:作者 LLM 產生初稿,評論員 LLM 給出評論,回饋給作者;「評論員」可用不同模型。[S08 p.20-21]
- Tool Use:不是 LLM 擅長的、或者不會的事,呼叫工具來幫忙。[S08 p.22]
- LLM 不太會做的事就不要再逼他:例如精確計算、實際數據、網路搜尋,改呼叫工具。[S08 p.23]
- 情境:打造飲料店 ChatBot,顧客說「我想訂 20 杯麥茶」,Bot 回答「沒問題!20 杯麥茶一共 600 元」。[S08 p.24]
- 第一步要告訴 AI 有哪些工具(函式)可用:`get_menu` 回傳 menu;`quote_order` 輸入品項、杯數,回傳單價、總金額、庫存是否足夠等。[S08 p.25]
- LLM 實際參與兩個階段:第一階段決定要呼叫的工具,例如 `quote_order("麥茶", 20)`。[S08 p.26]
- 工具(函式)被實際呼叫後回傳 JSON 結果(含 ok、item_name、quantity、unit_price=30、total=600、stock=30、currency=TWD、ordered=false)。[S08 p.27]
- JSON 基本上是用文字描述「有欄位名稱的資料表單」,電腦很喜歡這種格式。[S08 p.28]
- 第二階段:把這些數據放進 prompt,請 LLM 由資料回答使用者問題,輸出「沒問題!20 杯麥茶一共 600 元」。[S08 p.29]
- 工具不一定要自己寫:很多平台可連結工具,例如上網搜尋、你的 email,甚至處理你桌面的檔案。[S08 p.30]
- MCP(Anthropic,Model Context Protocol):與外部世界溝通;關注單一 Agent 如何規劃和使用外部工具的能力,是在標準化 LLM 與外部工具、資料來源或環境的互動方式。[S08 p.31]
- A2A(Google,Agent-to-Agent):代理之間溝通;著重 Agent 之間的溝通,定義了代理之間交換資訊、協作和協調的方式。[S08 p.31]
- Planning:先請 LLM「想一想」、「打草稿」再正式回應(先規劃步驟,較能完整回覆使用者需求)。[S08 p.32-33]
- Planning 的例子 CoT(Chain-of-Thought)是一種有名的方法:有系統地拆解複雜議題、找出議題間的關聯性、更完整地涵蓋各個面向、容易看出優先順序。[S08 p.34]
- CoT 是讓 DeepSeek-R1 厲害的關鍵:先產生「思考」,用 `<think>` 和 `</think>` tag 包起來。[S08 p.35]
- DeepSeek-R1 這類模型的目標是任何問題都能產生好的思維;若只針對單一類型的任務,當然有可能打造更好的「思考」,「或許我們可以做得更好」。[S08 p.36]
- Multiagent Collaboration:多個 AI Agent 一起合作。[S08 p.37]
- 常有一位如 PM 角色的 LLM 分配工作:任務拆解完成後,1 號算這個、2 號查資訊、3 號依資訊分析理由。[S08 p.38]
- 進階學習:Karpathy 訪談「AGI is Still a Decade Away」(Dwarkesh Podcast)。[S08 p.40]
- Karpathy 的重要想法:AGI 距離現在還有十年,現在的 AI 還不像真正人類實習生;人類學習不等於強化學習(RL),RL 很糟糕;模仿人類的網路(LLM)「知識壓縮」障礙。[S08 p.41]
- LLM 訓練三個階段:Pre-train(基礎模型)→ Post-train(對齊)→ Fine-tuning(圖中 Fine-tuning 與前兩者以虛線隔開)。[S08 p.42]
- Vibe Coding 為 Karpathy 於 2025 年 2 月在 X 發文所創的新詞。[S08 p.43]
- 原文要點:完全順從 vibes、忘了程式碼存在,因 LLM 太強;用語音對話,幾乎不碰鍵盤;一律「Accept All」、不再看 diff。[S08 p.44]
- 原文續:遇到錯誤訊息就複製貼上不加註解,通常就修好;程式長到超出自己理解;LLM 修不好就繞過或要求隨機更動;適合用完即丟的週末專案;「看東西、說東西、跑東西、複製貼上東西」,大致可行。[S08 p.45]
- Vibe Coding 重點五項:忘了有程式碼這件事;不要幫 AI 檢查程式碼;有錯就叫 AI 改;最高級的技巧是 Copy & Paste;完全不看程式、不改程式。[S08 p.46]
- Vibe Coding ≠ AI 輔助寫程式。[S08 p.47]
- Merriam-Webster 的定義:通過告訴 AI 程式你想要什麼,讓它為你創建產品的做法;程式設計師不需要理解程式碼如何或為何運作,且通常必須接受一定數量的錯誤和故障。[S08 p.48]
- 講者提出中文譯法問題與幾個候選:隨興程式設計法、擺爛程式設計法、耍廢式程式設計、直覺流程式設計。[S08 p.49]
- Vibe Coding 適合:週末好玩的小專案(Karpathy)、給自己使用且出錯不會怎樣的小工具、試做的原型並和程式設計師討論。[S08 p.50]
- Vibe Coding 不適合:要正式上線的程式(不是有 Vibe Coding 老闆就可以 fire 掉工程師)、不檢查可能會出亂子的程式。[S08 p.51]
- 說 Karpathy 對 Vibe Coding 有意見是誤讀:AI 時代三種寫程式方式為完全不用 LLM(純手工,Karpathy 認為不合理)、人類主導 + 自動補全、Vibe Coding(把需求用自然語言丟給 LLM 生成整段程式);且這不是該次訪談重點。[S08 p.52]
- Hinton 演講「Will AI Outsmart Human Intelligence?」影片(標題頁只有截圖)。[S08 p.53]
- 人工智慧的學派:符號式邏輯學派(logic-inspired AI)與生物學式學派(biologically-inspired AI)。[S08 p.54]
- 「AI 將會比人類聰明」:AI 已經在以與人類相同的方式理解世界;AI 將會比我們聰明,且想要控制;AI 甚至可能有主觀經驗(subjective experience)。[S08 p.55]

## 關鍵術語
- AI Agent:本課定義為 AI Model + Harness,即教 AI 用「我們做事的方法」做事。[S08 p.4]
- 代理人(agent,Russell & Norvig):透過感測器感知環境、透過致動器對環境採取行動的實體。[S08 p.3]
- Harness Engineering / Loop Engineering / Graph Engineering:投影片置於 AI Agent 範圍內的三種 Engineering;本份投影片未進一步展開定義。[S08 p.5]
- Prompt Engineering / Context Engineering:對應 Chat Bot 層次。[S08 p.5]
- Context Engineering(投影片 p.11 標題拼為 Content Engineering):給正確的資訊與清楚的指引。[S08 p.11]
- RAG:由電腦自動找到相關資訊,視為一種 AI Agent。[S08 p.14]
- Agentic Design Patterns(吳恩達四模式):Reflection、Tool Use、Planning、Multiagent Collaboration。[S08 p.18]
- Reflection:一個 LLM 寫初稿、另一個評論、再修改,可重覆。[S08 p.19]
- Tool Use(工具呼叫):LLM 不擅長的事交由函式/工具處理;LLM 參與「選工具」與「用結果回答」兩階段。[S08 p.22, p.26, p.29]
- JSON:用文字描述有欄位名稱的資料表單。[S08 p.28]
- MCP(Model Context Protocol,Anthropic):標準化 LLM 與外部工具、資料來源或環境的互動方式。[S08 p.31]
- A2A(Agent-to-Agent,Google):定義代理之間交換資訊、協作和協調的方式。[S08 p.31]
- Planning:先請 LLM 想一想、打草稿再回應。[S08 p.32]
- CoT(Chain-of-Thought):有系統地拆解複雜議題的方法。[S08 p.34]
- `<think>` / `</think>`:DeepSeek-R1 用來包住「思考」的 tag。[S08 p.35]
- Multiagent Collaboration:多個 AI Agent 合作,常由 PM 角色的 LLM 分配工作。[S08 p.37-38]
- Pre-train / Post-train / Fine-tuning:LLM 訓練三階段(基礎模型 / 對齊 / 微調)。[S08 p.42]
- RL(強化學習):Karpathy 認為人類學習不等於 RL,且 RL 很糟糕。[S08 p.41]
- Vibe Coding:告訴 AI 想要什麼、讓它產生程式,不必理解程式碼,接受一定的錯誤;≠ AI 輔助寫程式。[S08 p.46-48]
- 符號式邏輯學派 / 生物學式學派:人工智慧的兩大學派。[S08 p.54]

## 例子/比喻
- 寫文章不能用刪除鍵、不能修改,一路寫下去:比喻單次 prompt 的困難。[S08 p.9]
- 老闆(你)一句話,員工(AI Agents)動起來:比喻 Agent 架構。[S08 p.16]
- 飲料店 ChatBot:訂 20 杯麥茶、單價 30、總計 600 元,示範 `get_menu` / `quote_order` 工具呼叫與 JSON。[S08 p.24-29]
- 作者 LLM 與評論員 LLM:Reflection。[S08 p.20]
- PM 角色的 LLM 分配 1、2、3 號 Agent 做事:Multiagent。[S08 p.38]
- 真正人類實習生:Karpathy 對現在 AI 的比喻。[S08 p.41]
- 老闆就可以 fire 掉工程師:反駁「有 Vibe Coding 就不需工程師」。[S08 p.51]

## 文字層異常處
文字層多處缺字、順序亂(如「方法」被抽到頁尾、「麥茶」缺字、頁碼順序錯位)。以下頁面以 PDF 圖片核對:
- p.3、p.4、p.5(定義、標題、Engineering 圖示)
- p.11、p.14、p.15(Context Engineering、RAG、多 Agent 對話)
- p.16(Agent 架構圖,圖內文字不在文字層)
- p.31(MCP / A2A 說明)
- p.41、p.42(Karpathy 想法、訓練階段圖)
- p.50-55(Vibe Coding 適用性、三種寫程式方式、Hinton、學派、AI 將比人類聰明)

其餘頁(如 p.9、p.10、p.12、p.13、p.19-30、p.32-38、p.43-49)文字層缺字,僅依文字層上下文補字,未逐頁看圖;其中的字詞(如「一個人寫一篇文章」「第一個/第二個 LLM」「麥茶」)為合理還原,可信度較高但未視覺確認。p.34、p.36 中條列順序亦由文字層還原。
