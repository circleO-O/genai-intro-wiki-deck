---
title: 10 把你的工作拆成 AI 能做的流程(Loop、Graph 與 Workflow Prototype)
type: source
sources: [10]
---

# 10 把你的工作拆成 AI 能做的流程

來源:`raw/10把你的工作拆成AI能做的流程.pdf`(共 53 頁;115-1 TAICA《生成式 AI:文字與圖像生成的原理與實務》,政治大學應用數學系 蔡炎龍)[S10 p.1]

## 主題

從「當老闆、不要讓 AI 猜」(上一單元)進一步到「當流程設計師」:把工作從單次 prompt,升級為有檢查與停止規則的 loop,再拆成事先畫好、可退回特定關卡的 graph。實作以 Coding Agent(以 Antigravity 示範)建立 LLM Wiki,再從 wiki 產出 HTML 簡報,同一件事用 Prompt、Loop、Graph 三種做法對照。核心結論:先寫好「完成的定義」,再決定要不要加 loop 或 graph [S10 p.51]。

## 章節脈絡

| 投影片頁 | 章節 |
|---|---|
| p.1 | 封面 |
| p.2-6 | 01 從老闆到流程設計師(複習、全景圖、今日路線圖) |
| p.7-15 | 02 這次換用 Coding Agent(工具、Work Agent vs Code Agent、git、AGENTS.md) |
| p.16-27 | 03 從 Prompt 到 Loop 和 Graph(觀念主體) |
| p.28-36 | 04 實作一:先討論,再建 LLM Wiki |
| p.37-48 | 05 實作二:主題 → HTML 簡報(Prompt 版、Loop 版、Graph 版、三者對照) |
| p.49-51 | 06 拆解你自己的工作 + 今天的一句話 |
| p.52-53 | 作業、Q&A |

## 重點

### 01 複習與路線圖(p.2-6)
- 上一單元「當老闆」的三件事:要什麼成品(做完拿到什麼、放哪、什麼格式)、有什麼限制(哪些可動、哪些不能動)、怎麼算做完(怎麼驗收);重點是「不要讓 AI 猜」[S10 p.3]。
- 全景圖的層次:Chat Bot 對應 Prompt Engineering 與 Context Engineering;AI Agent 對應 Harness、Loop、Graph Engineering;今天要補完最後兩格,即 Loop Engineering 與 Graph Engineering [S10 p.4]。
- 即使當了老闆,仍是自己一直盯:交辦工作 → AI 做出一版 → 你發現問題(檢查)→ 再一次;「這就是 loop」[S10 p.5]。
- 今天路線:換工具(Code Agent)→ 觀念(Prompt → Loop → Graph)→ 實作一(先討論再建 LLM Wiki)→ 實作二(主題 → HTML 簡報)→ 拆解自己的工作 [S10 p.6]。

### 02 Coding Agent(p.7-15)
- 動機:有同學發現 Gemini 的對話介面讀不到電腦裡的資料,而 Antigravity 可以 [S10 p.8]。
- Work Agent 例:ChatGPT(Work / Codex)、Claude(Chat 整合 / Code)、Gemini、OpenWorker(開源並且可用開源模型)、GrokBot(純雲端)、Muse [S10 p.9]。
- Coding Agent 例:Codex(ChatGPT)、Claude Code(Claude)、Antigravity、OpenCode [S10 p.10]。
- 一樣從一個專案資料夾開始,讓 AI 有存取權限 [S10 p.11]。
- 四套工具:Antigravity(Google,今天主示範)、Claude Code(Anthropic,有訂閱歡迎使用)、Codex(OpenAI,有訂閱歡迎使用)、OpenCode(開源,可以接任何模型);今天的做法四套工具都通用 [S10 p.12]。
- Work Agent 與 Code Agent 對照:預設看到(成品和摘要 vs 每一行修改 diff);版本控制(要自己記得 vs git 是基本盤);驗證(多半靠人讀 vs 跑測試、跑腳本);兩者都有資料夾、手冊、Skills [S10 p.13]。
- 兩個工程習慣:git(每一步都能回去,看得出 AI 改了什麼);可以執行的檢查(「做完了」不是 AI 說了算,是腳本說了算);說「檢查一下」不算驗證 [S10 p.14]。
- 員工手冊各家都看得懂:通用用 AGENTS.md,Claude Code 讀 CLAUDE.md,Gemini 讀 GEMINI.md;用 Claude Code 的同學在 CLAUDE.md 裡寫一行 `@AGENTS.md` 即可;Antigravity 也會讀 AGENTS.md,換工具不用重寫 [S10 p.15]。

### 03 從 Prompt 到 Loop 和 Graph(p.16-27)
- 「不要寫 prompt,寫 loop」的說法:Boris Cherny(Claude Code 負責人):「我的工作是寫 loop。」;Peter Steinberger(OpenClaw 作者):「別再對 coding agent 下 prompt,去設計替你下 prompt 的 loop。」;Addy Osmani(2026 年 6 月命名 loop engineering):「把你自己從下 prompt 的人換掉。」[S10 p.17]。
- Loop 不也是 prompt 嗎?是,差別在你寫的是什麼:寫 prompt 是「這一輪要做什麼」,寫 loop 是「一份會自己執行的規格」[S10 p.18]。
- 最早的 loop 只有一行:`while :; do cat PROMPT.md | claude ; done`,為 Geoffrey Huntley 的 Ralph loop(2025 年 7 月),同一份 PROMPT.md 每一輪重餵一次;看起來很笨但真的會動;讓它運作的是 prompt 以外的東西:重複、檢查、用檔案記進度 [S10 p.19]。
- 寫 prompt vs 寫 loop:寫的內容(這一輪要做什麼 vs 目標、完成標準、驗證、停止規則);下一步誰決定(你讀完再寫下一句 vs 系統依檢查結果決定);寫幾次(每一輪都寫 vs 寫一次跑很多輪);你的角色(黏著劑 vs 設計者、審查者)[S10 p.20]。
- 一個 loop 要寫清楚五件事:目標(要什麼成品)、限制(哪些不能動)、完成標準(怎麼算做完)、停止條件(做不到時何時停手)、觸發(什麼時候開始跑);前三件上單元就學過 [S10 p.21]。
- 檢查分兩種:程式檢查(測試有沒有過、連結斷了沒、每頁有沒有出處);AI 審查(內容有沒有忠於來源、說法有沒有講反)。不要叫 AI 審自己的作品;AI 審查要開新的對話,只給成品和來源 [S10 p.22]。
- loop 也要剎車:硬上限(最多改 3 輪)、資料不足就停(不要用自己的知識硬湊)、會花錢(一個 loop 的 token 遠多於聊天);沒人看管的 loop,就是在沒人看管下犯錯的 loop [S10 p.23]。
- Graph 改變的是「誰在控制」:Loop 是自己反覆改作業,改到檢查表全過;Graph 像學校申請流程(系辦 → 院 → 教務處),不能跳關,卡住會退回特定一關。在 loop 裡 AI 決定下一步;在 graph 裡流程是你事先畫好的 [S10 p.24]。
- 三者其實都是圖:Prompt = 一個節點跑一次;Loop = 加一條「回到自己」的邊;Graph = 退回的邊可以接到任何一個節點(圖例 A → B → C 並有虛線退回 A)。順利跑完的 graph,其實就是一條流水線 [S10 p.25]。
- 好的 graph:大圈很少轉,小圈轉得很快。範例流程:檢索 → 大綱 → 逐頁稿 → 渲染 → 交件;小圈是錯了就在附近修,很快;大圈是從最後一關退回起點,應該很少發生。錯誤要在離源頭最近的地方被抓到;常常轉大圈,代表檢查該往前移 [S10 p.26]。
- 讓問題告訴你需要多少結構:① 先用 Prompt(一次性、自己會看)→ ② 一直重複說同樣的修正時升級成 Loop → ③ loop 每次都整份重來、各階段標準不同時拆成 Graph;不一定要堅持用 graph [S10 p.27]。

### 04 實作一:先討論,再建 LLM Wiki(p.28-36)
- 上週的做法:請依 Karpathy 的 LLM Wiki 建立 AGENTS.md 和資料夾;這週:先讓 AI 訪談你,整理需求,確認後才建檔。Karpathy 原文也說:把這份文件交給你的代理,和它一起做出適合你的版本 [S10 p.29]。
- 準備工作:建一個專案資料夾 → `git init` → 把 3-5 篇 LLM 論文放進 `raw/` → 用 Antigravity 開啟這個資料夾;提醒 `raw/` 不要放個資或機密文件 [S10 p.30]。
- 開場 prompt 要點:附上 Karpathy 的 LLM Wiki gist,說明要整理哪類論文;「先不要建立任何檔案」,請一次問一個問題、大約 8-10 題;問完後整理成需求摘要給我確認,確認後才生成 AGENTS.md 和資料夾 [S10 p.31]。
- AI 至少該問到的八項:讀者是誰、要哪些頁面類型、用什麼語言、出處要多細、論文互相矛盾怎麼辦、一次一篇還是批次、之後要產出什麼、lint 要檢查什麼 [S10 p.32]。
- 流程:你確認需求摘要 → AI 生成 AGENTS.md → 你逐條對照檢查(摘要裡說的,手冊裡都有寫進去嗎?)[S10 p.33]。
- 三個小提醒:別寫太長(Antigravity 規則檔上限 12,000 字元,細節拆到 skill);只維護一份(GEMINI.md 優先序比 AGENTS.md 高,兩份並存容易打架);Claude Code 的 CLAUDE.md 寫 `@AGENTS.md` 共用 [S10 p.34]。
- Ingest 1-2 篇後 commit:目錄結構 `my-wiki/`(AGENTS.md、raw/、wiki/ 含 index.md 與 log.md),`git commit -m "first ingest"`;頁面截圖為 Antigravity(Gemini)產出的架構說明,提到 raw/ → wiki/ 單向事實防線、Query 與 Lint 的知識回流與自我演進、notes/ → slides_html/ → index.html 的可視化輸出 [S10 p.35]。
- 小討論:比較上週「一句話生成」和這週「討論後生成」的 AGENTS.md 差在哪裡 [S10 p.36]。

### 05 實作二:主題 → HTML 簡報(p.37-48)
- 應用情境:使用者說一個主題(例:多模態 RAG)→ AI 只用 wiki 的內容 → 成品為一份 HTML 簡報;同一個 wiki、同一個模型,要做的事也一樣,只換做法 [S10 p.38]。
- Prompt 版:一句話「根據 wiki 裡關於多模態 RAG 的內容,做一份 HTML 簡報」,AI 回答「做好了!」[S10 p.39]。
- 然後你開始一直修:第 5 頁字太多跑出畫面、這個 37% 是哪篇的、8 篇相關論文只用了 3 篇、論文 A 的結論講反了;「這裡也有 loop——只是你自己就是那個 loop」[S10 p.40]。
- Loop 版(把修正寫成 SKILL.md):目標=只用 wiki 產出 HTML 簡報;程式檢查=每頁有出處、引用頁面存在、數字找得到、8-15 頁、渲染後沒有溢出;AI 審查=新對話,只給簡報和引用頁,檢查忠實度和覆蓋率;每一輪=只修檢查報告列出的問題;停止=全過/改滿 3 輪/相關頁面少於 3 頁就一開始停下 [S10 p.41]。
- 跑起來的樣子:第 1 輪腳本 3 頁溢出、2 處沒出處,審查第 6 頁講反了;第 2 輪腳本全過,審查論文 D 沒用到;第 3 輪補進論文 D → 全過 → 交件並附檢查報告;「我只要最後看報告就好」[S10 p.42]。
- Graph 版(先畫好流程):檢索 wiki → 覆蓋率關卡(不足則停下)→ 證據卡(平行)→ 大綱 → 人工確認(退回則修大綱或補檢索)→ 逐頁稿 → 忠實度檢查(退回則只修那頁)→ 渲染 HTML → 渲染檢查(退回逐頁稿)→ 交件;圖例區分 AI 節點、人工確認、檢查關卡,橘字為退回路線 [S10 p.43]。
- 每一關只能看什麼、改什麼:證據卡只能看一篇論文、不能混入其他來源;逐頁稿只能看大綱 + 對應卡片、不能引用卡片以外的內容;渲染 HTML 只能看已通過的逐頁稿、不能改任何一個字;檢查關卡只能看成品 + 來源、不能自己動手改。「排版時想順手改句子?不行!」[S10 p.44]。
- 錯在哪一關就退回哪一關:只修那頁(第 6 頁講錯,其他 14 頁不動)、卡片本身錯(退回重抽那一篇的證據卡)、字太多(不是硬塞,退回逐頁稿縮短)、缺子題(人看大綱時發現,退回檢索補資料);退回路線是你事先設計好的 [S10 p.45]。
- 每一格裡面還是 loop:逐頁稿節點為「寫一頁 → 檢查出處 → 修」最多 2 輪;渲染節點為「產生 HTML → 截圖 → 修版面 → 再截圖」;graph 決定大流程,loop 負責每一格的反覆修正 [S10 p.46]。
- 狀態都是檔案,也是 Workflow Prototype:`topic-multimodal-rag/` 內含 sources.md、cards/、outline.md、drafts/、deck.html、report.md;把流程寫成 workflow 檔放進 `.agents/workflows/`,用 `/topic-slides` 呼叫;每一道檢查關卡 = 一支腳本;每一關的產出都能打開看、放進 git、單獨重跑 [S10 p.47]。
- 三種做法對照:流程誰決定(Prompt 你即時 / Loop AI 在規格內 / Graph 你事先畫好);出錯怎麼修(你發現、你下指令 / 整份再跑一輪 / 退回出錯那一關);人在哪裡介入(隨時 / 最後驗收 / 指定關卡);適合(一次性、自己看 / 標準明確的重複任務 / 多階段、多人使用)[S10 p.48]。

### 06 拆解你自己的工作(p.49-52)
- 畫出自己的 workflow 的六個問題:可以拆成哪幾個節點?每個節點的輸入、輸出是什麼檔案?每個節點怎麼檢查(程式、人,還是審查)?人要在哪一關介入?出錯時退回哪裡?prompt、loop 還是 graph 就夠了?先用紙畫,不要急著叫 AI 做 [S10 p.50]。
- 今天的一句話:說「檢查一下」不算驗證;說「做好一點」不算規格;先寫好「完成的定義」,再決定要不要加上 loop 或 graph [S10 p.51]。
- 作業:用「先討論、後生成」建立自己主題的 LLM Wiki,至少 ingest 5 篇;設計 Graph 或 Loop 的 workflow 並生成簡報;反思(分享建 Wiki 時特別考量的事情、分享 Graph 或 Loop 的設計、其他心得)[S10 p.52]。

## 關鍵術語

- Loop(loop engineering):寫一份會自己執行的規格(目標、完成標準、驗證、停止規則),寫一次、跑很多輪,由系統依檢查結果決定下一步 [S10 p.18, p.20];2026 年 6 月由 Addy Osmani 命名 [S10 p.17]。
- Ralph loop:Geoffrey Huntley 2025 年 7 月提出的最早 loop,一行 `while :; do cat PROMPT.md | claude ; done`,每輪重餵同一份 PROMPT.md [S10 p.19]。
- Graph(graph engineering):流程由人事先畫好,節點之間不能跳關,卡住時退回特定一關 [S10 p.24]。
- 五件事(loop 規格):目標、限制、完成標準、停止條件、觸發 [S10 p.21]。
- 程式檢查 vs AI 審查:前者驗證測試、連結、出處等可執行項目;後者檢查忠於來源、有沒有講反;AI 審查須開新對話、只給成品和來源 [S10 p.22]。
- 大圈 / 小圈:graph 中從最後一關退回起點為大圈(應很少發生),在附近修正為小圈(要轉得快);常轉大圈代表檢查該往前移 [S10 p.26]。
- 證據卡:graph 版中每篇論文各抽一張,平行產生,下游只能引用卡片 [S10 p.43, p.44]。
- 檢查關卡:graph 中的驗證節點,只能看成品加來源、不能自己動手改;每一道關卡對應一支腳本 [S10 p.44, p.47]。
- Work Agent / Code Agent(Coding Agent):前者預設呈現成品和摘要、多半靠人讀驗證;後者呈現每一行修改(diff)、以 git 做版本控制、以跑測試腳本驗證 [S10 p.13]。
- AGENTS.md:各家工具通用的員工手冊;CLAUDE.md 以 `@AGENTS.md` 共用,GEMINI.md 優先序較高、避免並存 [S10 p.15, p.34]。
- LLM Wiki:依 Karpathy 構想以 AGENTS.md + raw/ + wiki/(index.md、log.md)組成的知識庫 [S10 p.29, p.35]。
- Workflow Prototype:把流程寫成 workflow 檔(`.agents/workflows/`)、以 `/topic-slides` 呼叫,各關狀態皆為檔案 [S10 p.47]。
- Skill / SKILL.md:把修正寫成規格(Loop 版的目標、檢查、每輪、停止)[S10 p.41];Antigravity 規則檔過長時細節拆到 skill [S10 p.34]。
- 完成的定義:先寫好再決定要不要加 loop 或 graph [S10 p.51]。

## 例子/比喻

- 老闆一直盯:交辦工作、做出一版、發現第 5 頁字太多、再一次,以此說明 loop [S10 p.5]。
- 學校申請流程(系辦 → 院 → 教務處,不能跳關、卡住退回特定一關)比喻 graph [S10 p.24]。
- 員工手冊(AGENTS.md / CLAUDE.md / GEMINI.md)比喻各工具的規則檔 [S10 p.15]。
- 黏著劑:寫 prompt 時你的角色;寫 loop 時則為設計者、審查者 [S10 p.20]。
- 流水線:順利跑完的 graph [S10 p.25]。
- 「沒人看管的 loop,就是在沒人看管下犯錯的 loop」警語 [S10 p.23]。
- 多模態 RAG 簡報案例:Prompt 版、Loop 版(三輪修正)、Graph 版(含退回路線)三種做法對同一任務 [S10 p.38-48]。

## 文字層異常處

文字層缺字/順序亂,以下頁面已用 PDF 圖片核對(實際上 p.1-36 與 p.38-53 皆已逐頁檢視;p.37 為章節分隔頁,文字層「05. 實作二 主題 → HTML 簡報」可讀,未另行視覺核對):
- p.4:圖例文字層分散;圖中「Contex Engineering」為投影片原有拼字。
- p.5、p.6、p.13、p.14、p.15:文字層大量缺字、順序亂,已以圖片核對。
- p.12:投影片標題原文為「Gode Agent」(應為 Code Agent 之筆誤),文字層亦同。
- p.17-27:缺字(如「工作」「自己」「一」等)與順序亂,已核對圖片。
- p.25:Graph 圖例(A → B → C 與退回虛線)只能靠圖片確認。
- p.26、p.43:流程圖文字層順序混亂,以圖片核對箭頭與退回路線。
- p.31、p.32、p.33、p.34:缺字,已核對。
- p.35:左側為 Antigravity 截圖(Gemini 輸出),文字層無此段內容,以圖片讀取;細節不納入定義。
- p.40-48:缺字與順序亂(如 p.41 的檢查項目、p.44 表格、p.45 退回路線、p.47 目錄樹),已以圖片核對。
- p.50-52:缺字(如「入」「人」「生」),已核對。
