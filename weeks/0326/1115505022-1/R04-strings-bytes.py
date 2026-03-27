# R04. 位元組字串操作（2.20）
# bytes / bytearray 支援大部分字串方法，但有幾個重要差異

import re

# 建立一個 bytes 物件，內容為 ASCII 編碼的字串
# b 前綴代表這是 bytes 而非一般字串
# bytes 物件常用於處理二進位資料、網路傳輸、檔案 I/O 等
# 下面展示 bytes 的基本操作

data = b"Hello World"
print(data[0:5])  # b'Hello'，取出前 5 個位元組，結果仍為 bytes
print(data.startswith(b"Hello"))  # True，判斷是否以 b'Hello' 開頭
print(data.split())  # [b'Hello', b'World']，依空白分割，回傳 bytes 組成的 list
print(data.replace(b"Hello", b"Hello Cruel"))  # b'Hello Cruel World'，bytes 也能做取代

# 正則表達式也必須使用 bytes 模式
# rb 前綴代表 raw bytes 字串，正則表達式要用 bytes 版本
raw = b"FOO:BAR,SPAM"
print(re.split(rb"[:,]", raw))  # [b'FOO', b'BAR', b'SPAM']，以 : 或 , 分割
print(date..replace(b"Hello", b"Hi"))  # b'Hi World'，bytes 也能做取代

# 差異 1：索引回傳整數而非字元
# 一般字串索引回傳字元，bytes 索引回傳該位元組的整數值（ASCII/Unicode 編碼）
a = "Hello"
b = b"Hello"
print(a[0])  # 'H'（字元）
print(b[0])  # 72（整數，即 ord('H')）

# 差異 2：不能直接用 format()，需先編碼
# bytes 不能直接用 format 方法，需先格式化成字串再 encode 成 bytes
formatted = "{:10s} {:10d}".format("ACME", 100).encode("ascii")
print(formatted)  # b'ACME            100'
print(formatted.decode("ascii"))  # 'ACME            100'，解碼回字串
print(formatted.decode("ascii").split())  # ['ACME', '100']，解碼後再分割
