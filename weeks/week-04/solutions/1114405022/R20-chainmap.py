
# R20. ChainMap 合併映射（1.20）
# 本範例示範如何用 ChainMap 合併多個字典，並實現類似多層查找的效果


from collections import ChainMap  # 匯入 ChainMap，可以把多個字典串接起來查找


a = {'x': 1, 'z': 3}  # 第一個字典
b = {'y': 2, 'z': 4}  # 第二個字典
c = ChainMap(a, b)  # 用 ChainMap 串接 a 和 b，查找時會先查 a，再查 b


c['x']  # 查找 'x'，只在 a 裡有，結果為 1
c['z']  # 查找 'z'，a 和 b 都有，會取 a 的 z，結果為 3
