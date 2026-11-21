---
title: 記憶與上下文(Context Window、短長期記憶、CAG、Context Engineering)
type: concept
sources: [07, 05, 08]
---

# 記憶與上下文

## 一句話定義
LLM 的「記憶」在外界常分為短期(這次對話)與長期(例如把過去對話做成向量資料庫的 RAG)兩種 [S07 p.31][S07 p.32][S07 p.33];要讓 LLM 看懂你的資料,可用 RAG 去找,或用 CAG(KV-Cache)把資訊全塞給它 [S07 p.26][S07 p.27];而決定放什麼資訊與指引進去,在 S08 稱為 Context Engineering [S08 p.11]。

## 白話解釋(給完全沒學過的人)
- 短期記憶就是這次的對話過程:下次再來,這次說的都忘了;更糟的是對話太長,前面的話也會忘 [S07 p.32]。
- 長期記憶像客製化機器人記得你的點點滴滴,例如記得「87」常訂的餐點現在沒賣了 [S07 p.34]。
- 講者的反思:「全部的資訊都放 Prompt 不就結了嗎?」特別是語言模型的上下文越來越長 [S07 p.26]。
- 比喻:寫文章不能用刪除鍵、不能修改,一路寫下去,對人也不容易,這是單次 prompt 的困難 [S08 p.9]。

## 重點
### 模型怎麼「記得前文」
- 因為單一個字當輸入不是函數,實際用「有記憶的」神經網路:輸入除了目前的字,還有前面字的記憶(融合成一個向量 h_{t-1})[S04 p.11](S04 為輔助來源,非本頁指定來源)。
- RNN 是上一步的輸出(hidden states)傳回來,再決定這次輸出 [S05 p.4][S05 p.5]。
- Transformer 的 Attention:給定「先備知識」(k1…kT、v1…vT,來自 x1…xT),輸入問題 q,輸出適合這問題的結果 h [S05 p.17]。
- RNN 真的一個字一個字讀;transformers 為了平行化一次做 self-attention,字的先後順序沒有真的被考慮,所以要加 position encoding [S05 p.42]。

### 短期與長期記憶
- 短期記憶 = 這次對話,過長則前面會忘 [S07 p.32]。
- 長期記憶的一個做法是 RAG:把過去完整的對話做成向量資料庫 [S07 p.33];同一系統可用兩個以上向量資料庫 [S07 p.30]。
- API 層面,對話歷史以 messages 清單輸入,回覆依這些過去記錄產生 [S06 p.77][S06 p.78](S06 為輔助來源)。

### 長上下文與 CAG(KV-Cache)
- 投影片問「話說回來真的要 RAG 嗎?」,指出上下文越來越長 [S07 p.26]。
- CAG:用 KV-Cache 技術把資訊都塞給 LLM,引用論文《Don't Do RAG: When Cache-Augmented Generation is All You Need for Knowledge Tasks》[S07 p.27]。
- KV-Cache(鍵值緩存):輸入 x₁…x_T 產生 q、k、v,其中資料的鍵值(k、v)先存起來 [S07 p.28]。
- LLM Wiki 的進一步探索:擴大後可生成合成資料並微調,讓 LLM 把資料「記」在權重裡,而非只依賴上下文視窗 [S07 p.45](僅憑文字層,未逐頁看圖)。

### Context Engineering
- 做好 Context Engineering 要做:「正確的資訊」(LLM 不知道你腦中的背景,可能要查規定、按計算機、上網搜尋)與「清楚的指引」(做什麼、輸出成什麼樣子、給誰看)[S08 p.11]。
- 名詞層次:Chat Bot 對應 Prompt Engineering 與 Context Engineering;AI Agent 對應 Harness / Loop / Graph Engineering [S08 p.5]。
- AI Agent 架構圖中除了 plan、RAG,還有 tools 與 memory [S08 p.16]。
- S07 稱 RAG 的本質是 Content Engineering,同樣是正確資訊 + 清楚指引 [S07 p.5]。

## 與其他概念的關係
- [[rag]]:長期記憶的做法之一 [S07 p.33];CAG 是 RAG 的替代考量 [S07 p.26][S07 p.27]。
- [[attention-transformer]]:KV-Cache 存的 k、v 即注意力 QKV 的 k、v [S07 p.28][S05 p.17]。
- [[neural-network]]、[[next-token-prediction]]:有記憶的網路是預測下一個字的需要 [S04 p.11]。
- [[prompt-and-system-prompt]]:prompt 與 context engineering 的練習 [S04 p.101]。
- [[llm-wiki]]:以 Markdown wiki 累積知識,是另一種讓 AI 掌握資料的方式 [S07 p.37][S07 p.42]。
- [[ai-agent-harness]]:memory 是 Agent 架構的一部分 [S08 p.16]。

## 來源差異或矛盾
- S07 p.5 稱 Content Engineering,S08 p.11 內文稱 Context Engineering(標題拼為 Content Engineering),實質內容一致。
- S07 p.26 僅提出「長上下文是否可取代 RAG」的設問,S07 p.27-28 介紹 CAG,但各頁未給出兩者優劣結論;其他來源亦無相關比較。
- S05 的摘要頁沒有提及 KV-Cache,與 S07 的連結為本頁依 QKV 定義的對照(k、v 見 [S05 p.17],緩存見 [S07 p.28])。
