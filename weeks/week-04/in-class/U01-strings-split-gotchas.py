"""
U01. 字串分割與匹配的陷阱（2.1–2.11）
本檔案示範：
1. 使用 re.split 並保留分隔符（捕獲分組）
2. startswith 必須傳 tuple 而非 list
3. strip 只會處理字串頭尾的空白
"""

import re


# ── 捕獲分組保留分隔符（2.1）─────────────────────────
# 原始字串，包含多種分隔符
line = "asdf fjdk; afed, fjek,asdf, foo"
# 使用 re.split，正則表達式中 () 代表捕獲分組，會把分隔符也保留下來
# ; 或 , 或 空白（\s），後面可有 0 個以上空白
fields = re.split(r"(;|,|\s)\s*", line)
# 取偶數索引（0,2,4...）為實際值
values = fields[::2]  # 偶數索引 = 實際值
# 取奇數索引（1,3,5...）為分隔符，最後補空字串
delimiters = fields[1::2] + [""]
# 將值與分隔符重新組合
rebuilt = "".join(v + d for v, d in zip(values, delimiters))
print(rebuilt)  # 'asdf fjdk;afed,fjek,asdf,foo'


# ── startswith 必須傳 tuple（2.2）────────────────────
# 字串開頭判斷
url = "http://www.python.org"
# 可接受的開頭集合
choices = ["http:", "ftp:"]
try:
    # 直接傳 list 會出錯，startswith 只接受 tuple 或單一字串
    url.startswith(choices)  # type: ignore[arg-type]
except TypeError as e:
    print(f"TypeError: {e}")  # 不能傳 list！
# 正確寫法：將 list 轉成 tuple
print(url.startswith(tuple(choices)))  # True（轉成 tuple 才行）


# ── strip 只處理頭尾，不處理中間（2.11）──────────────
# 原始字串，頭尾與中間都有多餘空白
s = "  hello     world  "
# strip 只會去除頭尾空白
print(repr(s.strip()))  # 'hello     world'（中間多餘空白還在）
# replace(" ", "") 會把所有空白都移除，連詞間空白也沒了
print(repr(s.replace(" ", "")))  # 'helloworld'（過頭，連詞間空白也消）
# 用 re.sub 將多個空白取代成一個空白，並先 strip 頭尾
print(repr(re.sub(r"\s+", " ", s.strip())))  # 'hello world'（正確）

# 生成器逐行清理（高效，不預載入記憶體）
# lines 是一個字串列表，每行有多餘空白與換行
lines = ["  apple  \n", "  banana  \n"]
# 用生成器表達式，對每行做 strip，節省記憶體
for line in (l.strip() for l in lines):
    print(line)  # 依序印出 'apple' 和 'banana'
