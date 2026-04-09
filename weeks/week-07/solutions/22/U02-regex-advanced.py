
"""
U02. 正則表達式進階技巧（2.4–2.6）
本檔案示範：
1. 預編譯正則表達式提升效能
2. re.sub 使用回呼函數進行進階替換
3. 替換時保持原字串大小寫風格
"""

import re
import timeit
from calendar import month_abbr


# ── 預編譯效能（2.4）──────────────────────────────────
# 測試字串，包含日期格式
text = "Today is 11/27/2012. PyCon starts 3/13/2013."
# 預先編譯正則表達式，提升多次使用時的效能
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")



# 直接用 re.findall，每次都重新編譯正則
def using_module():
    return re.findall(r"(\d+)/(\d+)/(\d+)", text)



# 用預編譯的 pattern 物件查找
def using_compiled():
    return datepat.findall(text)



# 比較兩種方法的效能
t1 = timeit.timeit(using_module, number=50_000)
t2 = timeit.timeit(using_compiled, number=50_000)
print(f"直接呼叫: {t1:.3f}s  預編譯: {t2:.3f}s")



# ── sub 回呼函數（2.5）────────────────────────────────
# re.sub 支援傳入函數，根據匹配內容動態產生替換字串
def change_date(m: re.Match) -> str:
    # m.group(1) 是月份數字，轉成英文縮寫
    mon_name = month_abbr[int(m.group(1))]
    # m.group(2) 是日期，m.group(3) 是年份
    return f"{m.group(2)} {mon_name} {m.group(3)}"



# 用 change_date 函數將日期格式替換成人類可讀格式
print(datepat.sub(change_date, text))
# 'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'



# ── 保持大小寫一致的替換（2.6）───────────────────────
# 傳入目標字串，回傳一個函數，能根據原字串的大小寫自動調整替換內容
def matchcase(word: str):
    def replace(m: re.Match) -> str:
        t = m.group()  # 取得原始匹配字串
        if t.isupper():
            return word.upper()  # 全大寫
        if t.islower():
            return word.lower()  # 全小寫
        if t[0].isupper():
            return word.capitalize()  # 首字大寫
        return word  # 其他情況直接回傳

    return replace



# 測試字串，包含不同大小寫的 'python'
s = "UPPER PYTHON, lower python, Mixed Python"
# 用 matchcase 產生的函數做替換，flags=re.IGNORECASE 代表忽略大小寫
print(re.sub("python", matchcase("snake"), s, flags=re.IGNORECASE))
# 'UPPER SNAKE, lower snake, Mixed Snake'
