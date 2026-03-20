
# R05. 數字基礎：四捨五入、進制、格式化（3.1–3.4）
# 本範例示範 round、Decimal、format、bin、oct、hex 等數字處理技巧


from decimal import Decimal, localcontext  # 匯入 Decimal 進行高精度運算
import math  # 匯入數學模組


# ── 3.1 四捨五入 ──────────────────────────────────────
print(round(1.27, 1))  # 四捨五入到小數第一位，結果 1.3
print(round(1.25361, 3))  # 四捨五入到小數第三位，結果 1.254
print(round(0.5))  # 0，銀行家捨入（0.5 取最近偶數）
print(round(2.5))  # 2，銀行家捨入（2.5 取最近偶數）


a = 1627731
print(round(a, -2))  # 對百位四捨五入，結果 1627700


# ── 3.2 精確浮點數 ────────────────────────────────────
print(4.2 + 2.1)  # 浮點數加法有誤差，結果 6.300000000000001
da, db = Decimal("4.2"), Decimal("2.1")  # 用 Decimal 表示精確小數
print(da + db)  # 精確加法，結果 6.3


with localcontext() as ctx:  # 設定 Decimal 運算精度
    ctx.prec = 3
    print(Decimal("1.3") / Decimal("1.7"))  # 精度 3，結果 0.765


# math.fsum 修正大數+小數精度
print(math.fsum([1.23e18, 1, -1.23e18]))  # 精確加總，結果 1.0


# ── 3.3 數字格式化 ────────────────────────────────────
x = 1234.56789
print(format(x, "0.2f"))  # 小數點後 2 位，'1234.57'
print(format(x, ">10.1f"))  # 右對齊，寬度 10，'    1234.6'
print(format(x, ","))  # 千分位，'1,234.56789'
print(format(x, "0,.2f"))  # 千分位且小數 2 位，'1,234.57'
print(format(x, "e"))  # 科學記號，'1.234568e+03'


# ── 3.4 二八十六進制 ──────────────────────────────────
n = 1234
print(bin(n), oct(n), hex(n))  # 轉成二進位、八進位、十六進位字串
print(format(n, "b"), format(n, "x"))  # 只取純數字部分，'10011010010' '4d2'
print(int("4d2", 16), int("2322", 8))  # 由字串轉回十進位，結果 1234 1234
