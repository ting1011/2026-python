# R06. 特殊數值：無窮大、NaN、分數、隨機（3.7–3.11）
# float inf/nan / fractions.Fraction / random

import math
import random
from fractions import Fraction

print("--- 3.7 無窮大與 NaN ---")
# float('inf') 產生正無窮大，float('-inf') 負無窮大，float('nan') 產生 NaN（非數值）
a = float("inf")
b = float("-inf")
c = float("nan")
print("a =", a, "b =", b, "c =", c)  # inf -inf nan
print("isinf(a):", math.isinf(a))  # True
print("isnan(c):", math.isnan(c))  # True
print("a + 45 =", a + 45, ", 10 / a =", 10 / a)  # inf 0.0
print("a / a =", a / a, ", a + b =", a + b)  # nan nan
print("c == c:", c == c)  # False

print("\n--- 3.8 分數運算 ---")
# Fraction 可精確表示分數，避免浮點誤差
p = Fraction(5, 4)  # 5/4
q = Fraction(7, 16)  # 7/16
r = p * q  # 分數可直接運算
print("p + q =", p + q)  # 27/16
print("r.numerator =", r.numerator, ", r.denominator =", r.denominator)  # 35 64
print("float(r) =", float(r))  # 0.546875
print("r.limit_denominator(8) =", r.limit_denominator(8))  # 4/7
print("Fraction(*(3.75).as_integer_ratio()) =", Fraction(*(3.75).as_integer_ratio()))  # 15/4

print("\n--- 3.11 隨機選擇 ---")
values = [1, 2, 3, 4, 5, 6]
print("random.choice(values):", random.choice(values))  # 隨機選一個元素
print("random.sample(values, 3):", random.sample(values, 3))  # 隨機選 3 個不重複元素
random.shuffle(values)  # 原地打亂序列
print("shuffled values:", values)  # 打亂後的結果
print("random.randint(0, 10):", random.randint(0, 10))  # 產生 0~10 的隨機整數
random.seed(42)  # 設定隨機種子，確保結果可重現
print("random.random() with seed 42:", random.random())  # 產生 0~1 之間的隨機小數
