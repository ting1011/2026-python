
"""
U04. 數字精度的陷阱與選擇（3.1–3.7）
本檔案示範：
1. Python round() 的銀行家捨入與傳統四捨五入
2. NaN（非數值）比較的陷阱
3. float 與 Decimal 的精度與效能差異
"""

import math
import timeit
from decimal import Decimal, ROUND_HALF_UP


# ── 銀行家捨入（3.1）─────────────────────────────────
# Python round() 採用「四捨六入五取偶」：遇到 0.5 會取最接近的偶數
print(round(0.5))  # 0（不是 1！）
print(round(2.5))  # 2（不是 3！）
print(round(3.5))  # 4



# 若需傳統四捨五入（五入），用 Decimal + ROUND_HALF_UP
def trad_round(x: float, n: int = 0) -> Decimal:
    d = Decimal(str(x))  # 轉成 Decimal 物件
    fmt = Decimal("1") if n == 0 else Decimal("0." + "0" * n)  # 決定小數位數格式
    return d.quantize(fmt, rounding=ROUND_HALF_UP)  # 用傳統四捨五入



print(trad_round(0.5))  # 1
print(trad_round(2.5))  # 3


# ── NaN 無法用 == 比較（3.7）─────────────────────────
# NaN（Not a Number）有特殊性質：任何比較都為 False
c = float("nan")
print(c == c)  # False（自己不等於自己！）
print(c == float("nan"))  # False
# 正確檢查 NaN 請用 math.isnan
print(math.isnan(c))  # True（唯一正確的檢測方式）


# 範例：過濾掉 NaN
data = [1.0, float("nan"), 3.0, float("nan"), 5.0]
clean = [x for x in data if not math.isnan(x)]
print(clean)  # [1.0, 3.0, 5.0]


# ── float vs Decimal 選擇（3.2）──────────────────────
# float：運算快但有精度誤差（適合科學/工程）
print(0.1 + 0.2)  # 0.30000000000000004
print(0.1 + 0.2 == 0.3)  # False


# Decimal：精確但速度較慢（適合金融/會計）
print(Decimal("0.1") + Decimal("0.2"))  # 0.3
print(Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))  # True


# 效能比較：float 運算遠快於 Decimal
t1 = timeit.timeit(lambda: 0.1 * 999, number=100_000)
t2 = timeit.timeit(lambda: Decimal("0.1") * 999, number=100_000)
print(f"float: {t1:.3f}s  Decimal: {t2:.3f}s（Decimal 約慢 {t2 / t1:.0f} 倍）")
