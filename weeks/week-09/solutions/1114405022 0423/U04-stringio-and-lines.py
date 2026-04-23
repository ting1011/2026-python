# U04. 類檔案物件 StringIO 與逐行處理（5.6 / 5.1 逐行）
# Bloom: Understand — 知道 file-like 是鴨子型別，能把記憶體當檔案用
# 本範例示範兩件事：
# 1. 如何用 StringIO 把記憶體中的字串當成檔案操作
# 2. 如何逐行讀取檔案並做清理與重新輸出

import io
from pathlib import Path

# ── 5.6 StringIO：記憶體裡的「假檔案」 ─────────────────
# StringIO 是「字串版本的檔案物件」：
# - 介面像檔案，可以 write / read / seek / 逐行迭代
# - 內容實際存在記憶體中，不會真的寫入磁碟
# - 很適合測試、暫存、或給只接受 file-like 物件的 API 使用
buf = io.StringIO()
# print(..., file=buf) 會把輸出寫進記憶體緩衝區，而不是終端機
print("第一行", file=buf)
print("第二行", file=buf)
print("第三行", file=buf)

# getvalue() 會一次取出整個緩衝區目前累積的文字內容
text = buf.getvalue()
print("---StringIO 內容---")
print(text)

# StringIO 也能模擬讀檔行為：
# - seek(0) 把讀寫位置移回開頭
# - 接著就可以像一般檔案一樣逐行迭代
buf.seek(0)
for i, line in enumerate(buf, 1):
    # enumerate(..., 1) 從 1 開始編號，方便輸出行號
    print(i, line.rstrip())

# 為什麼有用？
# 很多標準函式庫 API 都接受 file-like 物件，例如 csv、json、logging。
# 這代表你可以把 StringIO 當成「假檔案」餵給它們，
# 不必真的建立實體檔案，寫測試時特別方便。
import csv
mem = io.StringIO()
# csv.writer 只要拿到有 write 方法的物件就能工作
writer = csv.writer(mem)
# writerow() 會自動幫你輸出 CSV 格式與換行符
writer.writerow(["name", "score"])
writer.writerow(["alice", 90])
print("---CSV in memory---")
# 直接讀出記憶體中的 CSV 字串內容
print(mem.getvalue())

# ── 5.1 延伸：逐行處理檔案（大檔友善） ─────────────────
# 先建立一個多行文字檔，作為後續逐行處理的來源
src = Path("poem.txt")
# write_text() 會直接把整段字串寫入檔案
# 這裡故意放入空行，方便示範如何過濾
src.write_text("床前明月光\n\n疑是地上霜\n\n舉頭望明月\n低頭思故鄉\n", encoding="utf-8")

# 任務：
# 1. 逐行讀取來源檔案
# 2. 過濾空白行
# 3. 為有效內容加上行號
# 4. 將結果寫到新檔
dst = Path("poem_numbered.txt")
# with 同時開啟輸入與輸出檔案：
# - fin 負責讀取 src
# - fout 負責寫入 dst
# 使用 with 可以自動關檔，避免資源遺漏
with open(src, "rt", encoding="utf-8") as fin, \
     open(dst, "wt", encoding="utf-8") as fout:
    n = 0
    for line in fin:               # 逐行讀取：一次只把一行放入記憶體
        # rstrip() 去掉行尾換行符與其他尾端空白，方便判斷是否為空行
        line = line.rstrip()
        if not line:
            # 空白行直接跳過，不寫入輸出檔
            continue               # 跳過空行
        n += 1
        # 使用格式化字串加入兩位數行號，例如 01、02、03
        print(f"{n:02d}. {line}", file=fout)

print("---加行號後---")
# read_text() 直接把整個輸出檔讀回來，便於檢查結果
print(dst.read_text(encoding="utf-8"))
