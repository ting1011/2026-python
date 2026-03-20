
# R03. 字串清理、對齊、拼接與格式化（2.11–2.16）
# 本範例示範 strip、ljust、join、format、format_map、textwrap 等字串處理技巧


import textwrap  # 匯入 textwrap，用於文字自動換行


# ── 2.11 清理字元 ─────────────────────────────────────
s = "  hello world \n"  # 前後有空白與換行的字串
print(repr(s.strip()))  # 去除前後空白與換行，結果 'hello world'
print(repr(s.lstrip()))  # 去除左側空白，右側保留，結果 'hello world \n'
print("-----hello=====".strip("-="))  # 去除前後 - 與 =，結果 'hello'


# ── 2.13 字串對齊 ─────────────────────────────────────
text = "Hello World"
print(text.ljust(20))  # 靠左對齊，右側補空白
print(text.rjust(20))  # 靠右對齊，左側補空白
print(text.center(20, "*"))  # 置中，左右補 *
print(format(text, "^20"))  # 置中，左右補空白
print(format(1.2345, ">10.2f"))  # 浮點數靠右，寬度 10，小數 2 位


# ── 2.14 合併拼接 ─────────────────────────────────────
parts = ["Is", "Chicago", "Not", "Chicago?"]
print(" ".join(parts))  # 用空白合併
print(",".join(parts))  # 用逗號合併


data = ["ACME", 50, 91.1]
print(",".join(str(d) for d in data))  # 先轉字串再合併，結果 'ACME,50,91.1'


# ── 2.15 插入變量 ─────────────────────────────────────
name, n = "Guido", 37
s = "{name} has {n} messages."
print(s.format(name=name, n=n))  # 用 format 指定變數
print(s.format_map(vars()))  # 用 format_map 直接帶入區域變數
print(f"{name} has {n} messages.")  # f-string（最簡潔）


# ── 2.16 指定列寬 ─────────────────────────────────────
long_s = (
    "Look into my eyes, look into my eyes, the eyes, "
    "not around the eyes, look into my eyes, you're under."
)
print(textwrap.fill(long_s, 40))  # 每 40 字自動換行
print(textwrap.fill(long_s, 40, initial_indent="    "))  # 首行縮排
