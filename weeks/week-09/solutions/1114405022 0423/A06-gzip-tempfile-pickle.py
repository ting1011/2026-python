# A06. 壓縮檔、臨時資料夾、物件序列化（5.7 / 5.19 / 5.21）
# Bloom: Apply — 能把標準庫工具組合起來解一個小任務
# 本範例一次整合三個常用標準庫：
# 1) gzip：直接讀寫壓縮檔
# 2) tempfile：建立會自動清理的臨時檔/資料夾
# 3) pickle：把 Python 物件序列化到檔案

import gzip
import pickle
import tempfile
from pathlib import Path

# ── 5.7 讀寫壓縮檔：gzip.open 幾乎和 open 一樣 ─────────
# gzip.open 的介面和 open 很像：
# - 文字模式：'rt' / 'wt'，要搭配 encoding
# - 二進位模式：'rb' / 'wb'，資料型別是 bytes

# 寫入 .gz（文字模式要記得 encoding，否則中文可能出現亂碼）
with gzip.open("notes.txt.gz", "wt", encoding="utf-8") as f:
    f.write("第一行筆記\n")
    f.write("第二行筆記\n")

# 讀回壓縮檔：可像一般文字檔一樣逐行讀取
with gzip.open("notes.txt.gz", "rt", encoding="utf-8") as f:
    for line in f:
        # rstrip() 去掉行尾換行符，輸出更乾淨
        print("gz:", line.rstrip())

# 也能用 'wb'/'rb' 處理二進位資料（例如影像、封包、序列化結果）
with gzip.open("blob.bin.gz", "wb") as f:
    # 這裡示範寫入 4 個位元組
    f.write(b"\x00\x01\x02\x03")

# 使用 Path.stat().st_size 觀察壓縮檔的實際大小（單位 bytes）
print("blob size:", Path("blob.bin.gz").stat().st_size, "bytes")

# ── 5.19 臨時檔案與資料夾：離開 with 自動清理 ──────────
# 場景：想跑小實驗、測試流程、轉檔中繼，但不想在專案留下垃圾檔案。
# TemporaryDirectory 在 with 區塊結束後會自動刪除整個資料夾。
with tempfile.TemporaryDirectory() as tmp:
    # tmp 原本是字串路徑，轉成 Path 方便後續用 / 串接
    tmp = Path(tmp)
    print("暫存資料夾:", tmp)

    # 在臨時資料夾中建立幾個文字檔
    (tmp / "a.txt").write_text("hello\n", encoding="utf-8")
    (tmp / "b.txt").write_text("world\n", encoding="utf-8")

    # 列出內容並讀回，確認資料正確寫入
    for p in tmp.iterdir():
        print("  ", p.name, "→", p.read_text(encoding="utf-8").rstrip())

# 離開 with 後，tmp 已自動刪除
print("離開後還存在嗎？", tmp.exists())  # False

# 單一臨時檔：NamedTemporaryFile
# delete=False 表示離開 with 後不要自動刪，讓我們有機會再開啟/處理
with tempfile.NamedTemporaryFile("wt", delete=False, suffix=".log",
                                 encoding="utf-8") as f:
    f.write("暫存 log\n")
    # f.name 是作業系統給的實際暫存檔路徑
    log_path = f.name
print("暫存檔位置:", log_path)
# 因為 delete=False，所以這裡要手動清理
Path(log_path).unlink()  # 用完自己刪

# ── 5.21 pickle：把 Python 物件「原樣」存檔 ────────────
# pickle 的優點：
# - 幾乎可直接保存 Python 物件結構（dict/list/tuple/部分自訂物件）
# - 讀回後型別通常可完整保留
# pickle 的限制：
# - 不適合跨語言交換資料
# - 不建議做長期/公開格式儲存（可讀性與相容性較差）
scores = {
    "alice": [90, 85, 92],
    "bob":   [70, 75, 80],
    "carol": [88, 91, 95],
}

# 注意：pickle 輸出的是 bytes，所以開檔一定要用 'wb' / 'rb'
with open("scores.pkl", "wb") as f:
    # dump: Python 物件 -> 位元組流 -> 檔案
    pickle.dump(scores, f)

with open("scores.pkl", "rb") as f:
    # load: 檔案位元組 -> Python 物件
    loaded = pickle.load(f)

print("讀回的物件:", loaded)
print("型別一致?", type(loaded) is dict)         # True
print("內容相等?", loaded == scores)              # True
print("alice 平均:", sum(loaded["alice"]) / 3)   # 89.0

# ⚠️ 安全提醒：pickle.load 會執行內嵌指令，
# 絕對不要對「來路不明」的 .pkl 檔做 load。

# ── 課堂延伸挑戰 ───────────────────────────────────────
# 1) 把 scores 存成 gzip 壓縮後的 pickle：gzip.open('scores.pkl.gz','wb')
# 2) 用 TemporaryDirectory 跑完整流程（寫→讀→比對），不在專案留任何檔
# 3) 試著 pickle 一個 lambda，觀察錯誤訊息（pickle 不能存 lambda）
