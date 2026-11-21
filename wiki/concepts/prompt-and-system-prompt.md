---
title: Prompt 與 System Prompt
type: concept
sources: [04, 06]
---

# Prompt 與 System Prompt

## 一句話定義
Prompt 是下給 LLM 的指令;寫好它只有兩個重點:給「正確的資訊」與「清楚的指引」[S04 p.100][S06 p.35];在 API 與對話中,prompt 依角色分成 system(人設)、user(使用者輸入)、assistant(回應)三種 [S06 p.37][S06 p.76]。

## 白話解釋(給完全沒學過的人)
- LLM 不知道你腦中的背景,所以你要把該給的資料、條件講清楚(正確的資訊);也要講明白要它做什麼、輸出成什麼樣、給誰看(清楚的指引)[S04 p.100]。
- 對話時有「你」(user)和「AI」(assistant)兩個角色 [S06 p.36];其實還有第三個 system prompt,是 ChatGPT 的「人設」,也就是事先設定它扮演誰、怎麼回應 [S06 p.37]。
- 不會寫也不用擔心:講者的必殺技是「和 AI 一起寫 prompt」[S04 p.105]。講者的比喻是,把 AI 當「夥伴」,不要覺得它說的一定對,也不要笑它不知道你知道的東西 [S06 p.47]。

## 重點
### 兩個原則
- 寫好 prompt 只有兩個重點:正確的資訊 + 清楚的指引 [S04 p.100];S06 同樣說 prompt 兩要素是資訊與清楚的指引(例如用上面的資訊、什麼格式與風格回答問題)[S06 p.35]。
- S04 把該次作業稱為一次 Context Engineering,同時練習 prompt engineering 與 context engineering [S04 p.101]。

### 與 AI 一起寫 prompt 的五步驟(S04,以介紹 K-POP 女團 IVE 為例)
1. 先試一個陽春版 prompt(「請介紹 K-POP 女團 IVE。」,得到中規中矩、沒什麼感情的文章)[S04 p.106]。
2. 補充只有你知道的內容(從 DIVE 粉絲角度、出道即巔峰、低潮期、2025《REBEL HEART》等背景)[S04 p.107]。
3. 請 AI 訪問你:「這樣的主題,你覺得還有什麼可以釐清的地方可以問我。」[S04 p.108]
4. 請 AI 幫忙查證、補充,先打草稿(把要寫的重點整理好),最後整理成一個 prompt,以後直接用它指引 AI 寫文章 [S04 p.109]。
5. 親自閱讀並修改 prompt;AI 生成的不管是 prompt 還是成品,一定要自己好好讀 [S04 p.110]。
- 這招在 Vibe Coding 也好用:規格寫好 AI 寫程式更容易成功,不會寫程式的人先和 AI 討論再請它整理規格 [S04 p.111]。
- 作業:和 AI 設計一份可交給不同 LLM 使用的完整 prompt;最終 prompt 須自己完全讀過並修改,並至少在三個 LLM 試用 [S04 p.112][S04 p.113][S04 p.114]。
- S04 也提到 Claude Opus 的 System Prompt 很長,「真的像作文比賽」[S04 p.104](該頁內容未核對,僅依文字層)。

### system / user / assistant 與「人設」
- system 是 ChatGPT 的「人設」、user 是使用者輸入(prompt)、assistant 是回應 [S06 p.37];API 中同樣是這三種 role [S06 p.76]。
- 人設範例「員瑛式思考產生器」:請用員瑛式思考(什麼都正向思維),以第一人稱、社群貼文口吻說為什麼這是超幸運的事,並以「完全是 Lucky Vicky 呀!」結尾 [S06 p.41]。
- 加強版超長 prompt:標準指引 + 人生哲學 + 歷史參考,說話像朋友、盡量 200 字內、不要條列 [S06 p.45]。
- 製作流程:和 AI 討論、請它收集資訊 [S06 p.46];最後請 AI 用 Markdown 整理成完整 system prompt,並記得修改 [S06 p.48]。
- 小編助理:prompt 設定為臉書小編,先自我介紹並詢問,再依 [content] 與 [style] 寫貼文 [S06 p.52]。
- 選系諮商師:角色為應用數學系推廣諮商師,最後推薦一定是應數系 [S06 p.59];觀察到 ChatGPT 一接任務就「自曝身份」,講者標註「這要改!」[S06 p.60]。
- 股票分析師 prompt 被講者稱為「標準的情意分析」,並反問「你真的相信這樣的對話機器人嗎?」[S06 p.50]。

### 用 AISuite 以程式送 messages
- AISuite 提供統一用法、輕鬆切換模型、可同時用不同供應商模型 [S06 p.72]。
- `client = ai.Client()` 打開一台空白的 ChatBot [S06 p.75]。
- 對話歷史以 messages 清單輸入,每則為 `{"role": ..., "content": ...}`,依序 system、user、assistant、user… [S06 p.77]。
- 呼叫 `client.chat.completions.create(model="openai:gpt-4o", messages=messages)`,model 是模型、messages 是過去對話記錄 [S06 p.78];取回覆為 `response.choices[0].message.content` [S06 p.79]。

## 與其他概念的關係
- [[next-token-prediction]]:prompt 是 LLM 預測下一個字時的輸入(實際輸入是一堆字 x_1…x_T)[S04 p.13]。
- [[memory-and-context]]:messages 清單即把「過去的對話記錄」送進模型 [S06 p.78];prompt 中放什麼資訊屬於 Context Engineering [S04 p.101]。
- [[rag]]:RAG 的組 prompt 也是兩項資訊(question 與 retrieved_chunks)加指引 [S07 p.23-24]。
- [[hallucination]]:S06 提醒 AI 生成的都是「幻覺」,務必自己讀過 [S06 p.33],所以五步驟最後一步要自己讀 [S04 p.110]。
- [[ai-agent-harness]]:S04 指 Chat Bot 涵蓋 Prompt/Context Engineering,AI Agent 涵蓋 Harness / Loop / Graph Engineering [S04 p.101]。

## 來源差異或矛盾
- 無實質矛盾:S04 與 S06 對兩個原則的說法一致 [S04 p.100][S06 p.35]。
- 用詞小差異:S04 稱 Context Engineering [S04 p.101],S07 稱 Content Engineering [S07 p.5];S08 註明 p.11 標題拼為 Content Engineering [S08 p.11]。
