---
title: LLM Wiki
type: concept
sources: [07, 09, 10, 01]
---

# LLM Wiki

## 一句話定義
LLM Wiki 是 Karpathy 提出的做法:把你找的資料放進 raw,教 AI 把檔案產生/修改成 wiki 檔(內含 index.md),打造自己的 Wikipedia [S07 p.37][S09 p.33]。

## 白話解釋(給完全沒學過的人)
講者的說法是「打造你自己的 Wikipedia」:你找的資料 → raw → wiki(含 index.md) [S09 p.33]。Karpathy 原文說,用 LLM 針對感興趣的主題建立個人知識庫,token 更多花在整理知識(以 Markdown 和圖片儲存)而非操作程式碼 [S07 p.38]。Wiki 的資料都由 LLM 撰寫並維護,作者很少直接動手修改 [S07 p.40]。

## 重點
- 緣起:S07 稱為 2026 年 4 月 Karpathy 引爆的另一篇貼文 [S07 p.36](該頁僅憑文字層,未看圖,時間(未核對))。
- 資料匯入:把來源文件(文章、論文、程式碼儲存庫、資料集、圖片等)索引到 raw/,再用 LLM 逐步「編譯」出 Wiki(一系列 .md 檔),含摘要與反向連結、分類為概念、撰寫文章並串連;網頁轉 .md 用 Obsidian Web Clipper [S07 p.39]。
- Obsidian 作為 IDE 前端,檢視原始資料、編譯後的 Wiki 與衍生視覺化 [S07 p.40]。
- Q&A:Wiki 夠大(約 100 篇文章、約 40 萬字)時可問複雜問題;作者原以為需要複雜 RAG,但 LLM 自動維護索引檔和各文件簡短摘要,在此規模下也能輕鬆讀取相關資料 [S07 p.41]。
- 輸出:Markdown、Marp 投影片或 matplotlib 圖片,常「歸檔」回 Wiki,讓探索與查詢持續累積 [S07 p.42]。
- Linting:讓 LLM 對 Wiki「健檢」,找不一致資料、補缺漏、找新文章候選題材 [S07 p.43]。
- 額外工具與進一步探索:vibe coding 的 Wiki 搜尋引擎;資料擴大後可考慮合成資料與微調 [S07 p.44, p.45]。
- TLDR:收集原始資料、由 LLM 整理成 .md 維基,幾乎不手動撰寫或編輯 [S07 p.46]。
- Karpathy 的 Gist 標題 LLM Wiki,副標 "A pattern for building personal knowledge bases using LLMs" [S09 p.34]。
- Farzapedia:個人化的 wikipedia 範例,由多年日記整理成,畫面顯示 417 articles across 41 categories [S09 p.35];S07 同樣記為 417 篇文章、41 個分類 [S07 p.48]。
- 「先討論,後生成」:上週以 Karpathy 的 LLM Wiki 一句話請 AI 建 AGENTS.md 和資料夾;這週先讓 AI 訪談(一次一題、約 8-10 題,先不建任何檔案),整理需求摘要確認後才生成 AGENTS.md 與資料夾 [S10 p.29, p.31]。Karpathy 原文也說:把文件交給代理,和它一起做出適合你的版本 [S10 p.29]。
- AI 至少該問的八項:讀者、頁面類型、語言、出處多細、論文矛盾怎麼辦、一次一篇或批次、之後產出什麼、lint 檢查什麼 [S10 p.32]。
- 生成 AGENTS.md 後要逐條對照需求摘要檢查 [S10 p.33]。
- 結構:`my-wiki/`(AGENTS.md、raw/、wiki/ 含 index.md 與 log.md);raw/ 不放個資或機密 [S10 p.30, p.35]。
- 規則檔提醒:別寫太長(Antigravity 規則檔上限 12,000 字元)、只維護一份(GEMINI.md 優先序高於 AGENTS.md)、CLAUDE.md 寫 `@AGENTS.md` 共用 [S10 p.34]。
- 以 wiki 為唯一來源產出 HTML 簡報,是 Prompt / Loop / Graph 三種做法的共同實作 [S10 p.38]。
- Loop engineering 的命名(S10 p.17「2026 年 6 月由 Addy Osmani 命名」)僅依投影片,未核實 [S10 p.17](依投影片)。
- 課程脈絡:課程特色之一為「教 AI 用你的方法做事」 [S01 p.38],S09 把 LLM Wiki 作為「教 AI 整理檔案成 wiki」的範例 [S09 p.3, p.33]。

## 與其他概念的關係
- [[rag]]:S07 把 LLM Wiki 放在 RAG 與記憶之後;作者在此規模下不需複雜 RAG [S07 p.41]。
- [[memory-and-context]]:輸出歸檔回 Wiki 使探索持續累積 [S07 p.42],與長期記憶的 RAG 做法 [S07 p.33] 是不同路線(此對照為整理者歸納)。
- [[ai-agent-harness]]:AGENTS.md / CLAUDE.md 是 harness 的規則檔,wiki 專案資料夾由 agent 維護 [S09 p.16, p.22][S10 p.15]。
- [[loop]]、[[graph-workflow]]:wiki 是兩者簡報案例的內容來源 [S10 p.41, p.43]。
- [[prompt-and-system-prompt]]:「先討論後生成」是以訪談取代一句話 prompt [S10 p.31]。

## 來源差異或矛盾
- 做法差異(非矛盾):S09 只介紹概念與 Farzapedia 截圖 [S09 p.33-35];S07 逐段翻譯 Karpathy 貼文 [S07 p.38-46];S10 改為先討論再生成並實作 [S10 p.29]。
- Farzapedia 數字:S09 的 417 / 41 來自截圖 [S09 p.35],S07 同為 417 / 41 [S07 p.48],兩者一致。
- 時間點僅單一來源:Karpathy 貼文 2026 年 4 月 [S07 p.36](未核對);loop engineering 2026 年 6 月 [S10 p.17](依投影片)。
