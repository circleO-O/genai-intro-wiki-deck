---
title: Graph 與 Workflow Prototype
type: concept
sources: [10, 09]
---

# Graph 與 Workflow Prototype

## 一句話定義
Graph(graph engineering)是流程由人事先畫好、節點之間不能跳關、卡住時退回特定一關的做法 [S10 p.24]。

## 白話解釋(給完全沒學過的人)
講者用學校申請流程(系辦 → 院 → 教務處)比喻:不能跳關,卡住會退回特定一關 [S10 p.24]。對比 loop 是「自己反覆改作業,改到檢查表全過」;在 loop 裡由 AI 決定下一步,在 graph 裡流程是你事先畫好的 [S10 p.24]。順利跑完的 graph,其實就是一條流水線 [S10 p.25]。

## 重點
- 三者其實都是圖:Prompt = 一個節點跑一次;Loop = 加一條「回到自己」的邊;Graph = 退回的邊可以接到任何一個節點 [S10 p.25]。
- 大圈 / 小圈:好的 graph 是大圈很少轉、小圈轉得很快。範例流程:檢索 → 大綱 → 逐頁稿 → 渲染 → 交件;小圈是錯了就在附近修,大圈是從最後一關退回起點 [S10 p.26]。
- 錯誤要在離源頭最近的地方被抓到;常常轉大圈,代表檢查該往前移 [S10 p.26]。
- 案例(主題 → HTML 簡報的 Graph 版):檢索 wiki → 覆蓋率關卡(不足則停下)→ 證據卡(平行)→ 大綱 → 人工確認 → 逐頁稿 → 忠實度檢查 → 渲染 HTML → 渲染檢查 → 交件 [S10 p.43]。
- 每一關只能看什麼、改什麼:證據卡只能看一篇論文;逐頁稿只能看大綱 + 對應卡片;渲染 HTML 只能看已通過的逐頁稿、不能改任何一個字;檢查關卡只能看成品 + 來源、不能自己動手改 [S10 p.44]。
- 錯在哪一關就退回哪一關:第 6 頁講錯只修那頁;卡片本身錯就重抽那篇的證據卡;字太多退回逐頁稿縮短;缺子題退回檢索補資料;退回路線是事先設計好的 [S10 p.45]。
- 每一格裡面還是 loop:graph 決定大流程,loop 負責每一格的反覆修正 [S10 p.46]。
- Workflow Prototype:狀態都是檔案(`topic-multimodal-rag/` 內含 sources.md、cards/、outline.md、drafts/、deck.html、report.md);流程寫成 workflow 檔放進 `.agents/workflows/`,用 `/topic-slides` 呼叫;每一道檢查關卡 = 一支腳本;每一關的產出都能打開看、放進 git、單獨重跑 [S10 p.47]。
- 三種做法對照,Graph:流程由你事先畫好;出錯退回出錯那一關;人在指定關卡介入;適合多階段、多人使用 [S10 p.48]。
- 不一定要堅持用 graph:先 Prompt,再 Loop,loop 整份重來、各階段標準不同時才拆成 Graph [S10 p.27]。
- 拆解自己的工作時的六個問題:可拆成哪些節點、每個節點的輸入輸出檔案、怎麼檢查、人在哪關介入、出錯退回哪裡、prompt/loop/graph 哪個就夠;先用紙畫 [S10 p.50]。
- 全景圖:Graph Engineering 與 Loop Engineering 同屬 AI Agent 層 [S09 p.4]。S09 該頁只列出名稱,未逐項定義 [S09 p.4]。

## 與其他概念的關係
- [[loop]]:graph 的每一格內仍是 loop;loop 是 graph 的特例(退回只回自己) [S10 p.25, p.46]。
- [[ai-agent-harness]]:Graph、Loop 與 Harness 並列為 AI Agent 的工程層次 [S09 p.4][S10 p.4]。
- [[llm-wiki]]:案例中 graph 的第一關即檢索 wiki,並限制只用 wiki 內容 [S10 p.38, p.43]。
- [[tool-use-and-patterns]]:檢查關卡以腳本執行,屬可執行檢查;「檢查一下」不算驗證 [S10 p.14, p.47]。
- [[hallucination]]:忠實度檢查、證據卡限制來源,是避免內容無來源或講反的設計 [S10 p.43, p.44](此連結為整理者歸納,來源未明稱「幻覺」)。

## 來源差異或矛盾
無。
