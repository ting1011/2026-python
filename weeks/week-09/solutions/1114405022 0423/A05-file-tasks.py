# A05. 綜合應用：僅寫新檔 + 目錄統計（5.5 / 5.13 / 5.1）
# Bloom: Apply — 把前面學到的 API 組起來解小任務
# 本範例示範兩個實用情境：
# 1. 使用 'x' 模式建立「只能新增一次」的日記檔
# 2. 遞迴統計某資料夾內所有 .py 檔案的行數與函式定義數量

from pathlib import Path
from datetime import date

# ── 任務一：日記小工具（5.5 的 'x' 模式） ──────────────
# 'x' 模式是 exclusive create：
# - 檔案不存在時才建立
# - 若檔案已存在，會直接拋出 FileExistsError
# 這很適合用在「只想新增、不想覆蓋」的場景，例如每日日記。

# 規則：每天只能建一次；同一天重複執行要提示「已存在」。
today = date.today().isoformat()          # 例如 2026-04-23
# 用日期組出日記檔名，讓每一天對應一個獨立檔案
diary = Path(f"diary-{today}.txt")

try:
    # 以 'x' 開啟：如果檔案已存在就失敗，避免不小心覆蓋舊內容
    with open(diary, "x", encoding="utf-8") as f:
        # 先寫入標題，使用 Markdown 風格方便閱讀
        f.write(f"# {today} 日記\n")
        # 再寫入正文內容
        f.write("今天學了檔案 I/O。\n")
    print(f"已建立 {diary}")
except FileExistsError:
    # 如果同一天已經建立過，就保留原內容，不重新覆蓋
    print(f"{diary} 今天已寫過，保留原內容不覆蓋")

# ── 任務二：統計某資料夾裡 .py 檔的行數 ────────────────
# 這個函式示範如何：
# 1. 遞迴搜尋資料夾底下所有 .py 檔
# 2. 逐行讀取每個檔案
# 3. 累計總行數、非空白行數、def 行數
def count_py(folder: Path):
    # total    = 全部行數
    # nonblank = 去掉空白後仍有內容的行數
    # defs     = 以 "def " 開頭的函式定義行數
    total, nonblank, defs = 0, 0, 0

    # rglob("*.py") 會遞迴搜尋 folder 底下所有副檔名為 .py 的檔案
    for p in folder.rglob("*.py"):
        # errors="replace" 的作用：遇到無法解碼的字元時不要中斷，改用替代字元
        # 這對於不同來源或編碼混雜的檔案比較安全
        with open(p, "rt", encoding="utf-8", errors="replace") as f:
            # 一次只讀一行，適合大檔案，記憶體使用量小
            for line in f:
                total += 1
                # strip() 去掉前後空白，方便判斷是否為空行或註解/def
                s = line.strip()
                if s:
                    nonblank += 1
                # 只要去掉前後空白後以 def 開頭，就視為函式定義行
                if s.startswith("def "):
                    defs += 1
    return total, nonblank, defs

# 目標目錄設為 week-04/in-class，並向上兩層再進入指定資料夾
# 這樣寫可以示範 Path 的 / 串接方式，而不必手動處理斜線
target = Path("..") / ".." / "week-04" / "in-class"
if target.exists():
    # 只有在目錄存在時才做統計，避免路徑不存在造成錯誤
    total, nonblank, defs = count_py(target)
    print(f"{target}")
    print(f"  總行數       : {total}")
    print(f"  非空白行     : {nonblank}")
    print(f"  def 起頭行數 : {defs}")
else:
    # 若示範環境沒有對應目錄，就直接提示，不讓程式崩潰
    print(f"示範目錄不存在：{target}")

# ── 課堂延伸挑戰（自行嘗試） ───────────────────────────
# 1) 把日記工具改成「附加」模式 'a'：同一天可多次追寫一行時間戳。
# 2) count_py 再多算一個「註解行（以 # 開頭）」的數字。
# 3) 把統計結果用 print(..., sep='\t', file=f) 寫到 stats.tsv。
