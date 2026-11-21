---
title: AI Agent 與 Harness
type: concept
sources: [01, 08, 09]
---

# AI Agent 與 Harness

## 一句話定義
本課把 AI Agent 定義為「AI Model + Harness」,也就是教 AI 用「我們做事的方法」做事情。[S08 p.4][S09 p.3][S09 p.14]

## 白話解釋(給完全沒學過的人)
- 講者說現代 AI 模型只是「呆萌型 AI 機器人」:不會自己知道要做什麼,要告訴它輸入與輸出。[S01 p.45]
- LLM 本身只會生成文字:不會打開你的資料夾、不會建資料夾或改檔案、不能自己上網查最新資料。[S09 p.13]
- 比喻一(腦與裝備):Model 是大腦,負責「想」(理解、規劃、判斷、生成);Harness 是工作裝備,負責「做」,把模型說的「我要開這個檔案」真的執行,再把結果回報給模型。[S09 p.14]
- 比喻二(老闆與員工):純聊天時是「AI 出一張嘴,事情都你在做」,AI 還說「沒辦法,我沒手啊」;Agentic 時是「你出一張嘴,AI 來完成」。[S09 p.8][S09 p.10]
- 桌面整理例子:聊天版要把 87 個檔名一個個貼給 AI、自己建 5 個資料夾再一個個拖檔案;解法是回到 Tool Use,給 AI 可以處理檔案的工具。[S09 p.7][S09 p.8][S09 p.9]
- 比喻三(員工手冊):在專案資料夾裡寫一本「員工手冊」(CLAUDE.md / AGENTS.md)讓 AI 照著做。[S09 p.22]

## 重點
- **從 Chat 到 Agentic 的對照(五列)**:你在做的事(問問題 vs 交辦一件工作)、AI 像是(顧問 vs 員工、同事)、過程(一問一答且你全程在場 vs 多步驟自己做、你可以離開)、能碰的東西(對話框裡的文字 vs 檔案、瀏覽器、工具)、你拿到的(一段回答 vs 一份成品)。[S09 p.11]
- **為什麼需要 Agent**:一次寫完的 prompt 對人也不容易,人喜歡「邊寫、邊試、邊改」;AI Agent 是把本來你要做的(規劃、收集資料、不斷迭代嘗試等)交給 AI 自動做完。[S08 p.9][S08 p.10][S08 p.13]
- **RAG 也是一種 AI Agent**:「正確的資訊」由電腦自動找到。[S08 p.14]
- **Harness 的六個組成**:工作環境(自己的電腦/沙盒,可存檔、跑程式)、工具(讀寫檔案、終端機、瀏覽器、網路搜尋)、連接器 MCP(接上 Gmail、行事曆、雲端硬碟等 App)、技能 Skills(一個資料夾加一份 SKILL.md,教某件事的標準作業流程)、規則檔(CLAUDE.md / AGENTS.md,每次上工前先讀)、排程(時間到了自己開工)。[S09 p.16]
- **手刻 harness 與產品化 harness 的對照**:自己寫的 Python 函數當工具 vs 讀寫檔、終端機、搜尋;寫在程式裡的 system prompt vs CLAUDE.md / AGENTS.md;自己處理錯誤和重試 vs 產品幫你處理。[S09 p.15]
- **模型差不多,Harness 決定好不好用**。[S09 p.17]
- **好的交辦**:通常要說清楚三件事——要什麼成品(做完會拿到什麼、放在哪、什麼格式)、有什麼限制(哪些可以動、哪些不能動)、怎麼算做完(怎麼驗收);重點是不要讓 AI 猜測。[S09 p.18]
- **好壞交辦對照**:爛的是「幫我整理桌面。」;好的是指定資料夾、依用途分類、資料夾名稱用中文、不刪任何檔案、看不出用途的放「待確認」、動手前先給計畫、做完列出每個檔案搬到哪。[S09 p.19]
- **專案資料夾與員工手冊**:AI Agents 專案通常設一個專案資料夾讓 AI 有存取權限;手冊 Claude 專用叫 CLAUDE.md、通用叫 AGENTS.md,檔名不一定要固定,也可以叫 AI 先讀指定的手冊;這種規格書由我們和 AI 討論出來。[S09 p.21][S09 p.22]
- **為何要手冊**:專案放在同一個對話會越來越長、換電腦就讀不到;解法是每次開對話先要求讀手冊(例如「請先讀 AGENTS.md,瞭解這個專案的內容。」),不必一開始就完美,可持續改寫。[S09 p.23][S09 p.24]
- **可做專案型 Agent 的工具(投影片列出)**:ChatGPT(Work / Codex)、Claude(Chat 整合 / Code)、Gemini、OpenWorker(開源、可用開源模型)、GrokBot(純雲端)、Muse。[S09 p.20]
- **專案範例**:呆一布講義資料夾(含 CLAUDE.md)、呆一布粉專貼文工作室(含 AGENTS.md)、圖像風格轉換專案。[S09 p.26][S09 p.29][S09 p.31]
- **課程脈絡**:講者說焦慮之一是「學 AI 感覺好難」,回應是 AI Agent 其實只是「教 AI 做事的方法」。[S01 p.42]
- **名詞層次圖**:Chat Bot 涵蓋 Prompt Engineering 與 Context Engineering;AI Agent 涵蓋 Harness Engineering、Loop Engineering、Graph Engineering,Context Engineering 位於兩範圍交界。[S08 p.5][S01 p.42]
- **關於 Harness / Loop / Graph Engineering 的定義**:S08 明確說本份投影片未進一步展開定義 [S08 p.5];S09 p.4 只列出名稱、未逐項定義 [S09 p.4]。本頁因此不給這三者的定義(Harness 本身的組成見上方六要素 [S09 p.16])。

## 與其他概念的關係
- 工具是 harness 的一部分,工具呼叫與設計模式見 [[tool-use-and-patterns]]。[S09 p.9][S09 p.16]
- 規則檔(CLAUDE.md / AGENTS.md)取代手刻時寫在程式裡的 system prompt,見 [[prompt-and-system-prompt]]。[S09 p.15]
- RAG 視為一種 Agent,見 [[rag]]。[S08 p.14]
- 手冊與對話過長的問題屬於上下文與記憶議題,見 [[memory-and-context]]。[S09 p.23][S09 p.24]
- 「Loop / Graph Engineering」在名詞圖中屬於 AI Agent 範圍,見 [[loop]]、[[graph-workflow]]。[S08 p.5]
- 「教 AI 把檔案整理成 wiki」的 Karpathy LLM Wiki 例子,見 [[llm-wiki]]。[S09 p.33]
- 底層模型的運作見 [[next-token-prediction]]。

## 來源差異或矛盾
- 名詞圖的描述略有不同,但未見實質矛盾:S01、S08 描述 AI Agent 涵蓋 Harness / Loop / Graph,Context Engineering 位於交界 [S01 p.42][S08 p.5];S09 p.4 則寫 AI Agent 涵蓋 Context、Harness、Loop、Graph 四層,Chat Bot 涵蓋前兩層,Context 位於重疊處 [S09 p.4]。
- 拼字:S01、S09 的圖為「Contex」(原文拼法)[S01 p.42][S09 p.4];S08 p.11 標題拼為「Content Engineering」[S08 p.11]。
- S09 p.5 說上次手刻 Agent 涵蓋 Reflection、Tool Use、Planning 三項 [S09 p.5];S08 列出四個模式(多了 Multiagent Collaboration)[S08 p.18]。
- 核對狀態:S08 p.19-30、p.32-38 等頁僅依文字層補字、未逐頁看圖核對(未核對)。本頁只引用了 S08 p.9、p.10、p.13、p.14 等,其中 p.9、p.10、p.13 屬該類(未核對);p.14 已核對圖片。[S08 p.9][S08 p.10][S08 p.13][S08 p.14]
