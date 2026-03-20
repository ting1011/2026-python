
# R06. 特殊數值：無窮大、NaN、分數、隨機（3.7–3.11）
# 本範例示範 float inf/nan、fractions.Fraction、random 等特殊數值用法


import math  # 匯入數學模組
import random  # 匯入隨機模組
from fractions import Fraction  # 匯入分數類型


# ── 3.7 無窮大與 NaN ──────────────────────────────────
a = float("inf")  # 正無窮大
b = float("-inf")  # 負無窮大
c = float("nan")  # 非數值（Not a Number）
print(a, b, c)  # 輸出 inf -inf nan
print(math.isinf(a))  # 判斷是否為無窮大，True
print(math.isnan(c))  # 判斷是否為 NaN，True
print(a + 45, 10 / a)  # inf 0.0，無窮大加任意數還是無窮大，除以無窮大是 0
print(a / a, a + b)  # nan nan，無窮大除以自己或正負無窮大相加都是未定義
print(c == c)  # False，NaN 不等於自己


# ── 3.8 分數運算 ──────────────────────────────────────
p = Fraction(5, 4)  # 5/4
q = Fraction(7, 16)  # 7/16
r = p * q  # 分數相乘
print(p + q)  # 27/16，分數相加
print(r.numerator, r.denominator)  # 35 64，取得分子分母
print(float(r))  # 0.546875，轉成浮點數
print(r.limit_denominator(8))  # 4/7，限制分母最大為 8 的最接近分數
print(Fraction(*(3.75).as_integer_ratio()))  # 15/4，將小數轉成最簡分數


# ── 3.11 隨機選擇 ─────────────────────────────────────
values = [1, 2, 3, 4, 5, 6]
print(random.choice(values))  # 隨機選一個元素
print(random.sample(values, 3))  # 隨機選 3 個不重複樣本
random.shuffle(values)  # 就地打亂序列
print(values)  # 打亂後的序列
print(random.randint(0, 10))  # 產生 0~10 的隨機整數
random.seed(42)  # 設定隨機種子，讓結果可重現
print(random.random())  # 產生 0~1 之間的隨機小數
