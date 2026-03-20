
# R04. 位元組字串操作（2.20）
# bytes / bytearray 支援大部分字串方法，但有幾個重要差異
# 本範例示範 bytes/bytearray 的常用操作與與 str 的差異


import re  # 匯入正則表達式模組


data = b"Hello World"  # 一個 bytes 物件
print(data[0:5])  # 取前 5 個位元組，結果 b'Hello'
print(data.startswith(b"Hello"))  # 判斷是否以 b'Hello' 開頭，True
print(data.split())  # 依空白分割，結果 [b'Hello', b'World']
print(data.replace(b"Hello", b"Hello Cruel"))  # 替換內容，結果 b'Hello Cruel World'


# 正則表達式也必須使用 bytes 模式（pattern 前加 b 或 r）
raw = b"FOO:BAR,SPAM"
print(re.split(rb"[:,]", raw))  # 以 : 或 , 分割，結果 [b'FOO', b'BAR', b'SPAM']


# 差異 1：str 索引回傳字元，bytes 索引回傳整數（ASCII/Unicode 編碼）
a = "Hello"
b = b"Hello"
print(a[0])  # 'H'（字元）
print(b[0])  # 72（整數，即 ord('H')）


# 差異 2：bytes 不能直接用 format()，需先格式化再 encode
formatted = "{:10s} {:10d}".format("ACME", 100).encode("ascii")
print(formatted)  # b'ACME            100'
