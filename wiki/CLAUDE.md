# Wiki Schema:生成式 AI 入門

主題:生成式 AI 入門(從神經網路、LLM 到 AI 工作流程與 Agent)。
Raw sources:`../raw/01..10*.pdf`(不可修改)。`../raw_text/NN.txt` 為按頁抽取的文字(`=== p.N ===` 分頁),
**文字層有缺字/順序亂的問題**,不能當作唯一依據。

## 結構
- `sources/NN-*.md`:每份 PDF 一頁摘要
- `concepts/*.md`:概念頁,跨來源整合
- `index.md`:內容目錄(每次 ingest 更新)
- `log.md`:append-only,格式 `## [YYYY-MM-DD] ingest|query|lint | 標題`

## 頁面格式
frontmatter:`title`、`type`(source|concept)、`sources`(如 `[04, 05]`)。
內文每個事實主張後標註出處 `[S04 p.37]`(S+來源編號、p.投影片頁碼)。

## Ingest 流程
1. 讀 `raw_text/NN.txt`;文字亂或有關鍵圖的頁面,用 Read 看 PDF 該頁圖片核對。
2. 寫 source 頁:主題、章節脈絡、重點、關鍵術語。
3. 新增或更新 concept 頁,保留各來源的出處。
4. 更新 index.md、append log.md。
5. **檢查 1(寫入前)**:每個引用的頁碼,回頭確認該頁真的有該內容;缺字處以頁面圖片核對,不得靠猜。

## Query / 簡報規則
簡報內容只能來自 wiki,每頁標註所依據的 wiki 頁面;wiki 沒有的內容不寫,需補就先 ingest。

## Lint
找矛盾、孤立頁、被提及卻沒有頁面的概念、缺出處的主張。
