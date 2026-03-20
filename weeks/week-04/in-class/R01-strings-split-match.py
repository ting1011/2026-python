
# R01. 字串分割與匹配（2.1–2.3）
# 本範例示範：re.split 多分隔符、startswith/endswith、fnmatch 通配符


import re  # 匯入正則表達式模組
from fnmatch import fnmatch, fnmatchcase  # 匯入 shell 通配符比對函式


# ── 2.1 多界定符分割 ──────────────────────────────────
line = "asdf fjdk; afed, fjek,asdf, foo"  # 一個包含多種分隔符的字串
print(re.split(r"[;,\s]\s*", line))  # 用正則分割，分隔符可為 ; , 或空白，結果為 ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']


# 非捕獲分組：分組但不保留分隔符（?:...）
print(re.split(r"(?:,|;|\s)\s*", line))  # 結果同上，不會把分隔符保留在結果中


# ── 2.2 開頭/結尾匹配 ────────────────────────────────
filename = "spam.txt"
print(filename.endswith(".txt"))  # 判斷字串是否以 .txt 結尾，True
print(filename.startswith("file:"))  # 判斷字串是否以 file: 開頭，False


# 同時檢查多種後綴：endswith 可傳 tuple（不能傳 list）
filenames = ["Makefile", "foo.c", "bar.py", "spam.c", "spam.h"]
print([name for name in filenames if name.endswith((".c", ".h"))])  # 過濾出 .c 或 .h 結尾的檔名
# ['foo.c', 'spam.c', 'spam.h']


# ── 2.3 Shell 通配符匹配 ─────────────────────────────
print(fnmatch("foo.txt", "*.txt"))  # shell 通配符比對，* 代表任意字元，True
print(fnmatch("Dat45.csv", "Dat[0-9]*"))  # [0-9]* 代表數字開頭，True


# fnmatchcase 強制區分大小寫
print(fnmatchcase("foo.txt", "*.TXT"))  # False，因為大小寫不同


addresses = ["5412 N CLARK ST", "1060 W ADDISON ST", "1039 W GRANVILLE AVE"]  # 地址列表
print([a for a in addresses if fnmatchcase(a, "* ST")])  # 過濾出以 ' ST' 結尾的地址
# ['5412 N CLARK ST', '1060 W ADDISON ST']
