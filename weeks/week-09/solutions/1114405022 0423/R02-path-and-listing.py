# R02. 路徑操作與目錄列舉（5.11 / 5.12 / 5.13）
# Bloom: Remember — 會用 pathlib 組路徑、檢查存在、列出檔案
# 本範例重點：熟悉 Path 物件的基本屬性與常見目錄掃描方式

import os
from pathlib import Path

# ── 5.11 組路徑：pathlib 是現代寫法 ────────────────────
# Path("weeks") / "week-09" 是 pathlib 推薦的組路徑方式：
# 1) 可讀性高，像在「拼路徑片段」
# 2) 跨平台，Windows/Linux/macOS 會自動使用適合的分隔符
base = Path("weeks") / "week-09"

# Path 轉字串時會印出該平台的路徑格式
print(base)              # weeks/week-09（Windows 顯示時通常是反斜線）

# 常用屬性：
# - name:   路徑最後一段名稱
# - parent: 上一層路徑
# - suffix: 副檔名（若無則為空字串）
print(base.name)         # week-09
print(base.parent)       # weeks
print(base.suffix)       # ''（無副檔名）

# 若是檔案路徑，可用 stem/suffix 拆主檔名與副檔名
f = Path("hello.txt")
print(f.stem, f.suffix)  # hello .txt

# 舊式寫法：os.path.join（仍可用，但 pathlib 更直觀）
print(os.path.join("weeks", "week-09", "README.md"))

# ── 5.12 存在判斷 ──────────────────────────────────────
# 建議在讀檔前先做存在與型別檢查，避免例外發生
p = Path("hello.txt")
print(p.exists())    # exists(): 路徑是否存在（檔案或資料夾都算）
print(p.is_file())   # is_file(): 是否為「檔案」
print(p.is_dir())    # is_dir(): 是否為「資料夾」

missing = Path("no_such_file.txt")
if not missing.exists():
    # 先判斷不存在，再決定略過或建立，避免直接 open/read 造成錯誤
    print(f"{missing} 不存在，略過讀取")

# ── 5.13 列出資料夾內容 ────────────────────────────────
here = Path(".")  # "." 代表目前工作目錄（current working directory）

# 只列當層：os.listdir 不會遞迴進入子資料夾
for name in os.listdir(here):
    print("listdir:", name)

# 只抓當層 .py：glob("*.py") 會回傳符合樣式的 Path 物件
for p in here.glob("*.py"):
    print("glob:", p)

# 遞迴抓取：rglob("*.py") 會搜尋目前路徑及所有子資料夾
# 這裡從上一層 Path("..") 開始示範
for p in Path("..").rglob("*.py"):
    print("rglob:", p)
    break  # 示範用：避免輸出過多，只印第一個結果
