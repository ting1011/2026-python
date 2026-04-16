
# R20. ChainMap 合併映射（1.20）
# 本範例說明 collections.ChainMap 合併多個字典

from collections import ChainMap

a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}
c = ChainMap(a, b)  # 先查 a，再查 b

c['x']  # 取 a 的 x
c['z']  # 取 a 的 z（若 a 沒有才會取 b 的 z）
