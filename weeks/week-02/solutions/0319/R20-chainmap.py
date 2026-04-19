# R20. ChainMap 合併映射（1.20）

# ChainMap 可把多個 dict 串在一起查詢，不會真的複製資料
from collections import ChainMap

# 兩個來源字典有部分鍵重複
a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

# 建立 ChainMap，查詢順序是由前到後（a 優先於 b）
c = ChainMap(a, b)

# x 只在 a 中，直接取得 1
print("c['x'] =", c['x'])
# z 在 a 與 b 都有，會先拿到 a 的 3
print("c['z'] =", c['z'])  # 取到 a 的 z
