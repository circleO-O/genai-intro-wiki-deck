---
title: 注意力機制與 Transformer
type: concept
sources: [04, 05]
---

# 注意力機制與 Transformer

## 一句話定義
Transformer 是 Google 想出來的「一次生成各時間點記憶」的有記憶神經網路,核心是用 Q、K、V 做 self-attention,取代必須依序計算的 RNN。[S04 p.23][S04 p.27][S05 p.16]

## 白話解釋(給完全沒學過的人)
- 搜尋式比喻:q 是「問題」,k、v 是「先備知識」,輸出 h 是「適合這個問題的結果」。[S05 p.17][S05 p.19]
- Self-attention 就是「大家輪流當 q」:每個字都對所有字問一遍,依相關強度加權混合成自己的新表示。[S05 p.29]
- 位置編碼的比喻:十進位數字越高位數變化越慢;sin/cos 成對像時鐘上的指針,位元低的時鐘快、位元高的時鐘慢。[S05 p.43][S05 p.49]
- 文字生圖的例子:Q 是隨機產生的「天馬行空」想法,K、V 來自代表文字意思的矩陣,輸出混入文字意涵。[S05 p.67]

## 重點
- RNN 的限制:每步要導入上次的記憶 h_{t-1},運算是遞迴型、必須依序算,這是它的缺點。[S04 p.24][S04 p.26] RNN 神經元本質上和一般神經元一樣,只是多了上次的輸出當輸入。[S05 p.6]
- Transformer 的誕生:2017 年 Google 發表 "Attention is All you Need",主要想取代 RNN。[S05 p.16] 做法是 x_1…x_T 一次產生 h_1…h_T。[S04 p.27][S05 p.27]
- Q、K、V:每個 x_t 經線性轉換得到 q_t、k_t、v_t,轉換矩陣是學習來的;[S04 p.28][S05 p.34] 矩陣乘法可一次算出 Q、K、V。[S05 p.35]
- 計算流程:q 與 k 的內積得 attention 強度,經 softmax 成權重 α,再加權 v 得 h。[S04 p.29][S05 p.21][S05 p.24]
- 縮放:原始論文是 softmax(QK^T/√d_k)V;講者說 softmax 是「贏者通吃」,會讓權重高的被放大過頭,所以先除以 τ=√d_k;τ 也可當 hyperparameter。[S05 p.31][S05 p.33] 數例:3.9、3.2、1、0.3、1.1 經 softmax 為 61%、30%、3%、2%、4%,除以 τ 後變 40%、29%、11%、8%、11%。[S05 p.32][S05 p.33]
- 公式說明:Attention(q,K,V)=softmax(qK^T)V、Attention(Q,K,V)=softmax(QK^T)V 等推導頁(S05 p.20-30、S04 p.28-31)只依文字層重建,尚未以頁面圖片核對(未核對)(依兩份 source 頁的「文字層異常處」說明)。已核對的是 S05 p.31 的 √d_k 說法與 p.32-34 的數值/q、k、v 定義。
- Multihead Attention:attention 沒理由只有一種,定義多組 (W_n^Q, W_n^K, W_n^V) 得到第 n 個 attention。[S05 p.36]
- Encoder 與 decoder 設計不同:encoder 為 Multi-Head Self Attention 加 Dense;decoder 另有 Masked Multi-Head Attention。[S05 p.37] Decoder 中間層的 k、v 來自 encoder、q 來自前一層 output;[S05 p.38] 尚未有的輸入會被 mask 住。[S05 p.40]
- Position Encoding:RNN 一個字一個字讀,Transformer 為了平行化一次做 self-attention,字序沒有真的被考慮,所以要把位置資訊加到 embedding。[S05 p.42] 需求是連續、週期、數值不大,因此用 sin、cos。[S05 p.44] 原論文 ω_k=1/10000^(2k/d),偶數分量 sin、奇數分量 cos,位數越高頻率越低。[S05 p.46][S05 p.47] (p_t 與 x_t 同維度相加,已用圖片核對。[S05 p.45])
- 讓 Transformer 更穩:原版用了 residual 連結與 layer normalization,是當年讓網路更深、更穩的技術。[S05 p.52] ResNet 式設計把輸出由 ℓ(z) 改成 z+ℓ(z),只需學還沒學到的部分;[S05 p.54][S05 p.55][S05 p.57] 引用論文指有 skip 的 loss 較平順。[S05 p.58]
- Normalization:Batch Norm、Layer Norm(原版選擇)、Llama 等用的 RMSNorm;[S05 p.59][S05 p.60][S05 p.64] Meta 論文(2025/3/14)提出 Dynamic Tanh 可取代 Normalization。[S05 p.65]
- 不只文字:圖像、聲音、時間序列也可用 Transformer。[S05 p.66]

## 與其他概念的關係
- 提供 [[next-token-prediction]] 所需的「記憶」;[S04 p.11][S04 p.27]
- 本身是 [[neural-network]] 的一種放法(DNN、CNN、RNN、Transformers);[S04 p.12]
- attention 權重用到 softmax,見 [[softmax-and-sampling]];穩定訓練相關見 [[loss-and-gradient-descent]];
- 實務上的「上下文」限制見 [[memory-and-context]]。

## 來源差異或矛盾
- S04 p.31 直接給帶 √d_K 的最終公式;S05 先推導不帶縮放的版本(p.30),再於 p.31 說明原論文帶 √d_k。[S04 p.31][S05 p.30][S05 p.31] 這是講解順序不同,非矛盾。
- S04 p.28 註記 Google 偏好列向量故矩陣乘在後面,S05 p.13 同樣調侃此偏好,一致。[S04 p.28][S05 p.13]
