
# R02. 正則表達式：搜尋、替換、旗標（2.4–2.8）
# 本範例示範 re.compile、findall、sub、IGNORECASE、非貪婪、DOTALL 等用法


import re  # 匯入正則表達式模組


# ── 2.4 匹配和搜尋 ────────────────────────────────────
text = "Today is 11/27/2012. PyCon starts 3/13/2013."  # 一段包含日期的字串
datepat = re.compile(r"(\d+)/(\d+)/(\d+)")  # 編譯一個正則，匹配 mm/dd/yyyy 格式


print(datepat.findall(text))  # 找出所有符合的日期，回傳所有分組
# [('11', '27', '2012'), ('3', '13', '2013')]


m = datepat.match("11/27/2012")  # 從字串開頭比對
assert m is not None
print(m.group(0), m.groups())  # group(0) 是整個匹配，groups() 是所有分組


for m in datepat.finditer(text):  # 用 finditer 逐一取得每個匹配物件
    month, day, year = m.groups()  # 拆解分組
    print(f"{year}-{month}-{day}")  # 轉成 yyyy-mm-dd 格式


# ── 2.5 搜尋和替換 ───────────────────────────────────
print(re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text))  # 用分組替換順序，結果為 'Today is 2012-11-27. PyCon starts 2013-3-13.'


# 命名群組：用名稱取代分組編號
print(
    re.sub(
        r"(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)",
        r"\g<year>-\g<month>-\g<day>",
        text,
    )
)


# re.subn 會回傳 (新字串, 替換次數)
newtext, n = re.subn(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text)
print(f"替換了 {n} 次")  # 替換了 2 次


# ── 2.6 忽略大小寫 ───────────────────────────────────
s = "UPPER PYTHON, lower python, Mixed Python"  # 包含不同大小寫的 python
print(re.findall("python", s, flags=re.IGNORECASE))  # 忽略大小寫找所有 python
# ['PYTHON', 'python', 'Python']


# ── 2.7 非貪婪（最短匹配）────────────────────────────
text2 = 'Computer says "no." Phone says "yes."'  # 兩組引號包住的字串
print(re.compile(r'"(.*)"').findall(text2))  # 貪婪：會抓到最長的，['no." Phone says "yes.']
print(re.compile(r'"(.*?)"').findall(text2))  # 非貪婪：只抓最短的，['no.', 'yes.']


# ── 2.8 多行匹配（DOTALL）────────────────────────────
code = "/* this is a\nmultiline comment */"  # 多行註解
print(re.compile(r"/\*(.*?)\*/", re.DOTALL).findall(code))  # DOTALL 讓 . 可以匹配換行
# [' this is a\nmultiline comment ']
