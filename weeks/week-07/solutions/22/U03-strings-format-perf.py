
"""
U03. 字串格式化效能與陷阱（2.14–2.20）
本檔案示範：
1. join 與 + 串接字串的效能差異
2. format_map 處理缺失鍵的技巧
3. bytes 與 str 索引的差異
"""

import timeit


# ── join 效能優於 + （2.14）──────────────────────────
# 產生 1000 個字串組成的 list
parts = [f"item{i}" for i in range(1000)]



# 壞寫法：用 + 串接字串，每次都產生新物件，效能 O(n²)
def bad_concat():
    s = ""
    for p in parts:
        s += p  # 每次建立新字串，O(n²)
    return s



# 好寫法：用 join 一次分配記憶體，效能 O(n)
def good_join():
    return "".join(parts)  # 一次分配，O(n)



# 比較兩種方法的效能
t1 = timeit.timeit(bad_concat, number=500)
t2 = timeit.timeit(good_join, number=500)
print(f"+串接: {t1:.3f}s  join: {t2:.3f}s")



# ── format_map 處理缺失鍵（2.15）─────────────────────
# 自訂 dict，遇到缺失鍵時不報錯，直接回傳 {key}
class SafeSub(dict):
    def __missing__(self, key: str) -> str:
        return "{" + key + "}"  # 缺失時保留佔位符



# 測試 format_map 缺失鍵
name = "Guido"
s = "{name} has {n} messages."
# vars() 取得目前區域變數字典
# SafeSub(vars()) 讓缺失鍵不會拋出 KeyError
print(s.format_map(SafeSub(vars())))  # 'Guido has {n} messages.'（n 不存在也不報錯）


# ── bytes 索引回傳整數（2.20）────────────────────────
# str 索引回傳字元，bytes 索引回傳整數（ASCII/Unicode 編碼）
a = "Hello"
b = b"Hello"
print(a[0])  # 'H'（字元）
print(b[0])  # 72（整數 = ord('H')）

# bytes 不能直接 format，需先格式化再 encode
print("{:10s} {:5d}".format("ACME", 100).encode("ascii"))
# b'ACME            100'
