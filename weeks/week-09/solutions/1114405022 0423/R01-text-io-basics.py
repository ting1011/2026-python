# R01. 文本 I/O 基本式（5.1 / 5.2 / 5.3 / 5.17）
# Bloom: Remember — 會叫出 open/print 的基本參數
# 本模組演示 Python 文件 I/O 的基本操作，包括讀、寫、編碼等關鍵概念

from pathlib import Path

# ── 5.1 讀寫文本檔 ─────────────────────────────────────
# 文件寫入模式說明：
#   - 'w':  寫入模式（覆蓋原有內容）
#   - 't':  文字模式（默認值，自動處理編碼/解碼）
#   - 'wt': 組合使用文字寫入模式
# 重要：處理非英文文本時，一定要指定 encoding='utf-8' 避免亂碼

path = Path("hello.txt")  # 使用 Path 物件定義檔案路徑
# with 語句自動管理檔案資源：打開 -> 寫入 -> 自動關閉
# 即使發生異常也能確保檔案正確關閉，避免資源洩漏
with open(path, "wt", encoding="utf-8") as f:
    # 逐次寫入多行文字
    f.write("你好，Python\n")  # write() 不會自動加換行符，需要手動加 \n
    f.write("第二行\n")

# 讀回：一次讀完 vs 逐行讀
# 方式 1：f.read() - 一次性讀取整個檔案
# 優點：代碼簡單，適合小檔案（通常 < 10MB）
# 缺點：大檔案會消耗大量記憶體
with open(path, "rt", encoding="utf-8") as f:
    print(f.read())  # 一次讀完整個檔案並輸出

# 方式 2：逐行迭代 - 推薦用於大檔案
# 優點：逐行讀取，只需保存一行在記憶體中，極度節省資源
# 缺點：需要迴圈處理，代碼稍複雜
with open(path, "rt", encoding="utf-8") as f:
    for line in f:  # 檔案對象可直接迭代，每次迴圈讀一行
        # line 末尾包含 \n，rstrip() 去掉尾部空白字符（包括換行符）
        print(line.rstrip())

# ── 5.2 print 導向檔案 ─────────────────────────────────
# print() 函數的 file 參數可以改變輸出位置
# 默認：file=sys.stdout（輸出到終端）
# 指定：file=f（輸出到已開啟的檔案物件）
# 優勢：比 f.write() 方便，自動處理格式化和換行符
with open("log.txt", "wt", encoding="utf-8") as f:
    # print() 會自動在結尾加 \n，所以不需要手動加換行
    print("登入成功", file=f)  # 輸出第一行
    print("使用者:", "alice", file=f)  # 輸出第二行，自動用空格分隔參數

# ── 5.3 調整分隔符與行終止符 ───────────────────────────
# print() 的關鍵參數：
#   - sep:   分隔符（默認為空格）- 用來連接多個參數
#   - end:   行終止符（默認為 \n）- 打印最後加什麼字符
#   - *args: 解包 list/tuple 中的元素作為多個參數

fruits = ["apple", "banana", "cherry"]  # 水果列表
with open("fruits.csv", "wt", encoding="utf-8") as f:
    # *fruits 解包列表：相當於 print("apple", "banana", "cherry", ...)
    # sep="," 用逗號分隔各元素（CSV 格式）
    # end="\n" 明確指定行終止符為換行（其實是默認值）
    print(*fruits, sep=",", end="\n", file=f)

# 使用追加模式 'at' 添加新內容到現有檔案末尾
# 注意：'w' 模式會覆蓋現有內容，'a' 模式不會
with open("fruits.csv", "at", encoding="utf-8") as f:
    # end="," 改變行終止符為逗號，避免換行
    print("date", end=",", file=f)  # 輸出 "date," 不換行
    # 默認 end="\n"，所以這行會換行
    print("2026-04-23", file=f)  # 輸出 "2026-04-23" 並換行

# Path 物件的 read_text() 方法一次讀完整個檔案
print(Path("fruits.csv").read_text(encoding="utf-8"))
# 預期輸出：
# apple,banana,cherry
# date,2026-04-23

# ── 5.17 文字模式 vs 位元組模式提醒 ────────────────────
# 關鍵觀念：檔案模式決定了寫入的數據類型
#   - 文字模式 'wt'：接受 str 字符串，自動編碼為位元組
#   - 位元組模式 'wb'：接受 bytes 對象，直接寫入不編碼
# 常見錯誤：類型不匹配會拋出 TypeError

try:
    # 錯誤示範：在文字模式下嘗試寫入 bytes 對象
    with open("bad.txt", "wt", encoding="utf-8") as f:
        # b"..." 是 bytes 對象（前面有 b 前綴）
        f.write(b"bytes in text mode")  # ← 不兼容！會拋出 TypeError
except TypeError as e:
    # 捕捉錯誤並輸出錯誤信息
    print("錯誤示範:", e)  # 輸出：a bytes-like object is required, not 'str'
