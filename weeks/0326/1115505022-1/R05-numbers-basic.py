# R05. 數字基礎：四捨五入、進制、格式化（3.1–3.4）
# round / Decimal / format / bin / oct / hex

from decimal import Decimal, localcontext
import math

# ── 3.1 四捨五入 ──────────────────────────────────────
# round(x, n)：將 x 四捨五入到小數點後 n 位
print(round(1.27, 1))  # 1.3，四捨五入到小數第 1 位
print(round(1.25361, 3))  # 1.254，四捨五入到小數第 3 位
print(round(1.249, 14))  # 1.2，銀行家捨入（取最近偶數，非傳統四捨五入）
print(round(0.5))  # 0，0.5 會捨入到最近偶數 0
print(round(2.5))  # 2，2.5 會捨入到最近偶數 2

a = 1627731
print(round(a, -2))  # 1627700，對百位四捨五入（-2 代表到百位）

# ── 3.2 精確浮點數 ────────────────────────────────────
# 浮點數加法可能有誤差
print("->", 4.2 + 2.1-6.3)  # 6.300000000000001，浮點數精度問題
# 使用 Decimal 可避免精度誤差，適合財務計算
# Decimal 需用字串初始化，否則仍有誤差

da, db = Decimal("4.2"), Decimal("2.1")
print(da + db)  # 6.3，精確無誤差

# localcontext 可臨時設定 Decimal 精度
with localcontext() as ctx:
    ctx.prec = 3  # 設定精度為 3 位
    print(Decimal("1.3") / Decimal("1.7"))  # 0.765

# math.fsum 可修正大數+小數的精度誤差
print(math.fsum([1.23e18, 1, -1.23e18]))  # 1.0，正確結果

# ── 3.3 數字格式化 ────────────────────────────────────
x = 1234.56789
print(format(x, "0.2f"))  # '1234.57'，小數點後 2 位
print(format(x, ">10.1f"))  # '    1234.6'，右對齊，寬度 10
print(format(x, ","))  # '1,234.56789'，加千分位逗號
print(format(x, "0,.2f"))  # '1,234.57'，千分位+小數 2 位
print(format(x, "e"))  # '1.234568e+03'，科學記號

# ── 3.4 二八十六進制 ──────────────────────────────────
n = 1234
print(bin(n), oct(n), hex(n))  # 0b10011010010 0o2322 0x4d2，分別為二、八、十六進位
print(format(n, "b"), format(n, "x"))  # 10011010010 4d2，純數字格式
print(int("4d2", 16), int("2322", 8))  # 1234 1234，字串轉回十進位
