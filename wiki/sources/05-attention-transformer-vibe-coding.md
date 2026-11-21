---
title: 05 AI 怎麼記得前面說過什麼?(RNN、Attention、Transformer 與 Vibe Coding 作業)
type: source
sources: [05]
---

# 05 AI 怎麼記得前面說過什麼?

## 主題
說明神經網路如何「記得前文」:先看 RNN 把上一步的輸出(hidden states)傳回來的遞歸做法,再補線性代數(內積、列向量線性組合),接著推導 Transformer 的 QKV 注意力機制、Self-Attention、Multihead、Masked Attention、Position Encoding,以及讓 Transformer 更穩的 ResNet 式 skip connection 與各種 Normalization。最後是一份作業:用 Vibe Coding 做出互動網頁並上傳 GitHub Page。(全份共 86 頁)

## 章節脈絡
| 頁碼 | 內容 |
|---|---|
| p.1 | 封面 |
| p.2-8 | RNN 的原理(遞歸層、hidden states、矩陣寫法) |
| p.9-14 | 線性代數 101(矩陣先列後行、內積、列向量線性組合) |
| p.15-26 | QKV 注意力機制:Transformers 的誕生、Q/K/V 概念、attention 強度、softmax、最終公式 |
| p.27-30 | Self-Attention(大家輪流當 q)與矩陣 Q |
| p.31-33 | One More Thing:除以 √d_k 與 softmax 贏者通吃 |
| p.34-36 | q、k、v 如何由 x 線性轉換得到;Multihead Attention |
| p.37-40 | encoder 與 decoder 的差異;Masked Multihead Attention |
| p.41-50 | Position Encoding(進位制類比、sin/cos、時鐘比喻) |
| p.51-65 | 讓 Transformers 更穩:原版架構、ResNet、Batch/Layer Norm、RMSNorm、Dynamic Tanh |
| p.66-67 | Transformer 不只處理文字;「混入」資訊(文字生圖) |
| p.68-86 | 【作業】與 AI 討論 Vibe Coding 程式規格書:Prompt 要點、規格書、index.html、GitHub 發佈步驟 |

## 重點

### RNN 與遞歸層
- 以兩個輸入、兩個 RNN 神經元的遞歸層為例說明,專注在第一個 RNN 神經元;一開始看起來和以前的全連結層一樣。[S05 p.3]
- 不一樣的是:上次 RNN 層的輸出會再傳回來,然後才決定這次的輸出。[S05 p.4, p.5]
- 第 1 號 RNN 神經元的輸出寫成 h_t = σ(w11 x_t^1 + w21 x_t^2 + w11 h_{t-1}^1 + w21 h_{t-1}^2 + b1)。[S05 p.5]
- x_t 是「正常」輸入,h_{t-1} 是上次的 hidden states。[S05 p.6]
- 認真看,RNN 神經元就是一般的神經元;(W^X)^T · x_t 一次同時算了兩個神經元的輸入部分,hidden states 這邊(W^H)^T · h_{t-1} 基本上也一樣。[S05 p.6, p.7, p.8]

### 線性代數 101
- 矩陣最大的關鍵是「先列後行」;m × n 矩陣即 m 列 n 行。[S05 p.10]
- 若 C = AB,c_ij 是 A 矩陣第 i 列和 B 矩陣第 j 行的內積,乘法也是先列後行。[S05 p.11]
- 內積(嚴格說是 dot product)是核心:⟨u, v⟩ = u v^T。[S05 p.12]
- 一般說的線性轉換寫成 A x(x 為行向量);但 Google 超喜歡列向量(和內積),於是引發了後面的故事。[S05 p.13]
- 矩陣乘法最重要的技巧:x 向量的分量,對 A 矩陣的列向量做線性組合,即 x1·a1 + x2·a2 + ⋯ + xm·am。[S05 p.14]

### Transformers 的誕生與 QKV 概念
- 2017 年 Google 發表 "Attention is All you Need"(Vaswani et al., NIPS 2017),介紹 transformers 架構;最主要是想取代 RNN,但從標題可知,(當時)Google 野心更大。[S05 p.16]
- Attention 的 QKV 概念:給定「先備知識」(k1…kT、v1…vT,來自 x1…xT),輸入問題 q,輸出適合這問題的結果 h。[S05 p.17]
- qt、kt、vt 都是 xt 的一個特徵代表向量。[S05 p.18]
- 直覺想法:有一段資訊(例如一段文字 x1…xT),現在有個 query q 進來,想依前面的資訊找出最適合 q 的代表向量 h。[S05 p.19]
- h = α1 v1 + α2 v2 + ⋯ + αT vT;α 是 q 和各 x_t 的相關強度,也就是 attention 的強度,基本上愛怎麼合理地算都可以。[S05 p.20]
- 計算注意力強度:a(q, k_t) = ⟨q, k_t⟩ = q k_t^T = e_t,這是 Google 最愛的方法。[S05 p.21]
- 把所有 k_i、v_i 各放入一個矩陣 K、V(深愛列向量的 Google 會這樣寫)。[S05 p.22]
- attention 強度可用簡單矩陣乘法 q · K^T 一次算完(得 e1…eT)。[S05 p.23]
- 再經 softmax 得到最後的權重係數 α1…αT。[S05 p.24]
- softmax(q · K^T) 乘上 V,就是列向量線性組合,結果為 Σ α_t v_t。[S05 p.25]
- 最終公式:Attention(q, K, V) = softmax(q · K^T) V。[S05 p.26]

### Self-Attention
- Self-Attention 的目的:Google 想一次生成(輸入 x1…xT,輸出 h1…hT)。[S05 p.27]
- 基本上是每個 x_t 再增加 q 特徵代表向量,即每個 x_t 有 q_t、k_t、v_t。[S05 p.28]
- 其實就是大家輪流當 q:h_j = Σ α_t v_t,為標準 attention 計算。[S05 p.29]
- 像 K、V 一樣把所有 q_i 放入矩陣 Q,可導出 Attention(Q, K, V) = softmax(Q K^T) V。[S05 p.30]

### One More Thing:縮放與 softmax 贏者通吃
- 前述公式和原始論文公式不同:原始論文為 softmax(QK^T / √d_k) V。[S05 p.31]
- 講者說法:Google 很尷尬地發現,用內積算 attention 強度效果沒有人家(例如訓練一個神經元去算)好;主要原因是 softmax 是「贏者通吃」,會讓權重高的比合理權重還要高很多。[S05 p.31]
- d_k = dim(k_i);講者認為這裡放一個足夠大的適當數字就可以(例如 √9487),Google 這樣寫基本上只是讓你覺得好有學問。[S05 p.31]
- 數例:輸入 3.9、3.2、1、0.3、1.1 經 softmax 得 61%、30%、3%、2%、4%(本來感覺只差一點);指數函數圖示說明為何如此。[S05 p.32]
- 先同除以 τ = √d_k,數字變為 1.74、1.43、0.45、0.13、0.49,softmax 後為 40%、29%、11%、8%、11%;把數字都拉到 0 附近,輕鬆解決問題。[S05 p.33]
- τ 不一定要是 √d_k,可以當一個 hyperparameter。[S05 p.33]

### q、k、v 的來源與 Multihead
- x_1…x_T 是 word embedding;q_t = x_t W^Q、k_t = x_t W^K、v_t = x_t W^V,即對 x_i 的線性轉換,這些矩陣是學習來的。[S05 p.34]
- 註腳:一般不用如 Word2Vec 等標準 word embedding,而是直接加 embedding 層去學。[S05 p.34]
- 令 X 為所有 x_t 疊成的矩陣,則 Q = X W^Q、K = X W^K、V = X W^V,可以一次算出來。[S05 p.35]
- attention 沒理由只有一種,可定義第 n 個 attention:Attention(X W_n^Q, X W_n^K, X W_n^V),這就是 Multihead Attention。[S05 p.36]

### Encoder 與 Decoder
- encoder 與 decoder 設計不同:encoder 為 Multi-Head (Self) Attention 加 Dense;decoder 為 Masked Multi-Head (Self) Attention、Multi-Head Attention、Dense。encoder 與 decoder 的 self-attention 都是由輸入向量自家生產 q、k、v。[S05 p.37]
- 只有 decoder 中間那層不是 self-attention:k、v 來自 encoder,q 來自前一層的 output。[S05 p.38]
- 要注意 transformer 輸入有幾個(字/詞向量),輸出就有幾個(以 Encoder 圖示)。[S05 p.39]
- Decoder 也是這樣,只是開始還沒有的輸入會被 mask 住(Masked Multihead Attention)。[S05 p.40]

### Position Encoding
- RNN 是真的一個字一個字讀;transformers 為了平行化,一次做 self-attention,每個字的先後順序並沒有真的被考慮,所以應把位置資訊加入原來的文字 embedding,這叫 position encoding(x_t + p_t)。[S05 p.42]
- 觀察任何進位的數字系統:越高位數週期越長、頻率越低。以十進位數 [9, 4, 8, 7] 為例,各位頻率為 1/1000、1/100、1/10、1;文字表示順序相反,比較像 [7, 8, 4, 9]。[S05 p.43]
- 為了通用,想找個「奇幻進位系統」,需求:連續函數、有週期性、數值不要太大(以免影響原 embedding);很容易打 sin、cos 的主意。[S05 p.44]
- 加上 position encoding:p_t 與 x_t 同維度 d 相加;p_t 中,低位數在前、高位數在後。[S05 p.45]「低位數頻率高、高位數頻率低」的說法見 [S05 p.43, p.47](檢查 1 修正:原誤標為 p.45)。
- 原論文兩兩一組同頻率:ω_k = 1 / 10000^(2k/d);後面的頻率要越來越慢,需要 ω0 > ω1 > ⋯;註記:原論文下標通常從 1 開始,但這裡應由 0 開始才符合後面的式子。[S05 p.46]
- 原論文方式:p_t 的第 i 個分量,當 i = 2k 為 sin(ω_k · t),當 i = 2k+1 為 cos(ω_k · t);位數越高頻率越低。[S05 p.47]
- 因此 p_t = [sin(ω0 t), cos(ω0 t), sin(ω1 t), cos(ω1 t), …, sin(ω_{d/2} t), cos(ω_{d/2} t)]。[S05 p.48]
- 為什麼要加 cos?沒人規定一個位元只能用一個數字表示,(sin(ωt), cos(ωt)) 剛好是單位圓上的一點,可想成時鐘上的一個點;位元低(k=0)的時鐘快,位元高(k=d/2)的時鐘慢。[S05 p.49]
- 講者說不知 Google 的考量,但 (sin θ, cos θ) 繞一圈也是單位圓,且 θ = 0 指向一般時鐘 12 點方向,走向是順時鐘;以此回應「極座標明明是 cos 在前」的疑問。[S05 p.50]

### 讓 Transformers 更穩
- 回頭看原版 Transformers 架構,每個細節都可理解;沒說的是 transformers 用了 residual 連結與 layer normalization,這些是當年能讓神經網路更深、更穩定的最佳技術。[S05 p.52]
- ResNet 式設計:原本某層輸出是 ℓ(z),現在變成 z + ℓ(z)。[S05 p.54, p.55]
- 為什麼可以很深:設目標(正確答案)為 f(z),原本希望 ℓ(z) ≃ f(z),現在變成 z + ℓ(z) ≃ f(z),只需要學之前沒有學到的,即 ℓ(z) = f(z) − z。[S05 p.55, p.56, p.57]
- 如果 z 已經很接近正確答案 f(z),那 ℓ(z) 就不太需要再學什麼。[S05 p.57]
- 引用 Li et al.(NeurIPS 2018)Visualizing the Loss Landscape of Neural Nets:without skip 與 with skip 比較,有 skip 的 loss function 較平順。[S05 p.58]
- Batch Normalization:x̂ = (x − μ) / √(σ² + ε),y = γ x̂ + β;ε 預防除以 0,γ、β 是學習來的,需計算平均值、標準差。[S05 p.59]
- Layer Normalization(原版 transformers 的選擇):x̂_i = (x_i − μ) / √(σ² + ε),y_i = γ x̂_i + β。[S05 p.60]
- 複習 μ = (1/n) Σ x_i 與 σ = √((1/n) Σ (x_i − μ)²)。[S05 p.61]
- 仔細看 Layer Normalization:x̂ 與 γ、β 為向量,μ、σ 為純量,基本上都是 numpy 的 broadcasting 運算。[S05 p.62]
- 至此,更新的模型也知道差異是什麼了(投影片附 github.com/rasbt/LLMs-from-scratch 連結)。[S05 p.63]
- Llama 等 LLM 運用了 RMS Norm:RMS(x) = √((1/n) Σ x_i²),RMSNorm(x) = x / RMS(x) · γ,γ 為學來的向量。[S05 p.64]
- 最近 Meta 說可以不用做 Normalization(論文 Transformers without Normalization,2025/3/14):Dynamic Tanh,DyT(x) = γ · tanh(αx) + β,γ、β 是學習來的向量,α 可設為 0.5。[S05 p.65]

### Transformer 不只處理文字
- 不只是文字,圖像(聲音、時間序列數據)也可以用 Transformer。[S05 p.66]
- 「混入」資訊也很好用:以文字生圖 AI 為例,Q 為隨機產生「天馬行空」的想法,X(經轉換成 K、V)為代表文字「意思」的矩陣,輸出 Z 為混入文字意涵的結果。[S05 p.67]

### 作業:用 Vibe Coding 做互動網頁
- 作業:想一個有趣的應用,用 Vibe Coding 做出一個 web app,並上傳到 GitHub 讓全世界都看得到;三步:(1) 先和 AI 討論產生 App 的「規格書」,(2) 用規格書產生 index.html 網頁,(3) 用 GitHub Page 讓全世界看到作品。[S05 p.68, p.69]
- 網頁基本語言:HTML 決定網頁的內容;CSS 決定網頁的排版、字型、顏色;JavaScript 讓網頁能互動,是所有瀏覽器都懂的程式語言;網頁可以是單一檔案(基本上單一 .html 檔就可以)。[S05 p.70]
- 還記得 Prompt 只有兩個要點:正確的資訊(把該給的資料、條件講清楚,AI 不知道你腦中的背景)+ 清楚的指引(要它做什麼、輸出成什麼樣、給誰看)。[S05 p.71]
- 例子:想寫抽獎程式;重點其實是寫一份很好的「規格書」。[S05 p.72, p.73]
- Prompt 必殺技:和 AI 一起寫 prompt。[S05 p.74]
- 可跟 AI 說:想辦一個小活動,最後要抽出一個獎品給幸運得主,希望程式是單一的 HTML 檔,先不要寫程式,問我一些問題,幫我把需求釐清,或提供一些建議;來來回回討論,最後再讓 AI 把規格書寫出來。[S05 p.75]
- 程式大概是 index.html(檔名一定要叫這個)加上 assets 資料夾(圖片等可放裡面)。[S05 p.76]
- 把 index.html 拉到瀏覽器就看到 App。[S05 p.77]
- 放上網路:到 github.com 申請帳號 → 建立新的 Repo → 取名字、隨便描述、一開始先有 README → 從 Add file 上傳檔案(上傳 index.html 與 assets,一定要按 Commit)→ 準備用 GitHub Page → 發佈網頁。[S05 p.78, p.79, p.80, p.81, p.82, p.83, p.84]
- 網址格式:https://你的帳號.github.io/repo名稱/;上課示範:https://yenlung.github.io/vibe-tools/。[S05 p.85]
- p.86 為空白尾頁(僅頁尾)。[S05 p.86]

## 關鍵術語
- RNN(遞歸神經網路)/ 遞歸層:每個神經元除了「正常」輸入 x_t,還接收上次的輸出(hidden states)h_{t-1}。[S05 p.4, p.5, p.6]
- hidden states:上次 RNN 層的輸出,會傳回來參與這次運算,記為 h_{t-1}。[S05 p.4, p.6]
- 內積(dot product):⟨u, v⟩ = u v^T,矩陣乘法 c_ij 就是 A 的第 i 列與 B 的第 j 行的內積。[S05 p.11, p.12]
- 列向量線性組合:x 的分量對 A 的列向量做線性組合,是矩陣乘法最重要的技巧。[S05 p.14]
- Query / Key / Value(Q、K、V):q 是問題,k 與 v 是從先備知識 x_t 得到的特徵代表向量;輸出 h 是適合 q 的結果。[S05 p.17, p.18]
- Attention(alignment)強度:q 與 k_t 的相關強度,以內積 e_t = q k_t^T 計算,再經 softmax 成權重 α_t。[S05 p.20, p.21, p.24]
- Attention(Q, K, V):softmax(Q K^T) V(原論文為除以 √d_k)。[S05 p.30, p.31]
- Self-Attention:每個 x_t 都產生自己的 q_t、k_t、v_t,大家輪流當 q。[S05 p.28, p.29]
- softmax 贏者通吃:softmax 讓大的數字權重被放大過度。[S05 p.31, p.32]
- 縮放 τ(√d_k):在 softmax 前同除以 τ,把數字拉到 0 附近;τ 可當 hyperparameter。[S05 p.33]
- word embedding:字詞向量 x_t;此處一般直接加 embedding 層去學,而非用 Word2Vec 等標準 embedding。[S05 p.34]
- W^Q、W^K、W^V:對 x_i 做線性轉換、產生 q、k、v 的學習來矩陣。[S05 p.34, p.35]
- Multihead Attention:定義多組 (W_n^Q, W_n^K, W_n^V),得到第 n 個 attention。[S05 p.36]
- encoder / decoder:兩者設計不同;decoder 中間那層的 k、v 來自 encoder,q 來自前一層 output。[S05 p.37, p.38]
- Masked Multihead Attention:decoder 中開始時還沒有的輸入會被 mask 住。[S05 p.40]
- Position Encoding(位置編碼):加到 word embedding 的位置資訊 p_t,補回平行處理而遺失的字序。[S05 p.42]
- sin/cos 位置編碼:p_t 以 ω_k = 1/10000^(2k/d) 的 sin、cos 成對構成,低位數頻率高、高位數頻率低。[S05 p.46, p.47, p.48]
- residual 連結 / ResNet 設計:層輸出由 ℓ(z) 改為 z + ℓ(z),只需學還沒學到的 f(z) − z。[S05 p.54, p.55, p.56, p.57]
- Batch Normalization / Layer Normalization:以平均值、標準差正規化,再乘上學來的 γ 加 β;原版 transformers 選 Layer Normalization。[S05 p.59, p.60]
- RMSNorm:x 除以 RMS(x) 再乘學來的向量 γ,Llama 等 LLM 使用。[S05 p.64]
- Dynamic Tanh(DyT):DyT(x) = γ · tanh(αx) + β,用來取代 Normalization(Meta 論文)。[S05 p.65]
- Vibe Coding 規格書 / index.html / GitHub Page:先與 AI 討論出規格書,再產生 index.html,最後用 GitHub Page 發佈。[S05 p.69, p.76, p.85]

## 例子/比喻
- 位數進位比喻:用十進位 [9, 4, 8, 7] 說明越高位數頻率越低,類比 position encoding 的各維度頻率。[S05 p.43]
- 時鐘比喻:(sin, cos) 是單位圓上的一點,可想成時鐘上的指針;位元低的時鐘快、位元高的時鐘慢;θ = 0 指向 12 點方向、順時鐘走。[S05 p.49, p.50]
- softmax 數值例:3.9、3.2、1、0.3、1.1 → 61%、30%、3%、2%、4%;同除以 √d_k 後 → 40%、29%、11%、8%、11%。[S05 p.32, p.33]
- 搜尋式比喻:q 是問題、k/v 是「先備知識」,輸出 h 是適合這問題的結果。[S05 p.17, p.19]
- ResNet:「只需要學之前沒有學到的」,已接近答案時 ℓ(z) 不太需要再學。[S05 p.56, p.57]
- 文字生圖:Q 是隨機產生的「天馬行空」想法,K、V 來自代表文字意思的矩陣,輸出 Z 混入文字意涵。[S05 p.67]
- 抽獎程式:作為 Vibe Coding 規格書的範例需求(單一 HTML 檔、抽出一個獎品給幸運得主)。[S05 p.72, p.75]
- 講者以「Google 最愛」「Google 引以為傲的公式」「讓你覺得好有學問」等語氣調侃 Google 偏好列向量、內積與 √d_k 寫法。[S05 p.13, p.21, p.30, p.31]

## 文字層異常處
文字層對多數頁面有缺字、順序亂(尤其公式、圖示與「AI怎麼記得前面說過什麼?」頁尾亂碼)。已以頁面圖片核對的頁:
- p.16(Transformers 架構圖與說明)
- p.17(QKV 圖)
- p.31(除以 √d_k 的公式與說明,文字層缺字嚴重)
- p.32、p.33(softmax 數字與百分比)
- p.34(q、k、v 公式與 word embedding 註腳)
- p.37、p.38(encoder/decoder 圖)
- p.39、p.40(輸入輸出數量與 mask 圖)
- p.42、p.43、p.44(position encoding 說明、進位制、需求清單)
- p.49、p.50(sin/cos 時鐘比喻)
- p.65(Dynamic Tanh 與論文截圖)
- p.67(混入資訊的 Q、K、V、Z 圖)
- p.69(作業三步驟)

其餘頁(多為公式與流程圖,如 p.3-8、p.20-30、p.46-48、p.53-64、p.70-85)只靠文字層與標題推得,公式細節若需精確引用應再回頭核對頁面圖片;p.45 的 p_t 與 x_t 同維度相加為依文字層與頁面標題推得,未逐頁視覺核對。
