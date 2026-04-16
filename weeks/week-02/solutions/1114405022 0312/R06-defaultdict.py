# R6. 多值字典 defaultdict / setdefault（1.6）

from collections import defaultdict  # 匯入 defaultdict

# 預設 value 是 list，可以直接 append
d = defaultdict(list)
d['a'].append(1); d['a'].append(2)  # d['a'] 會自動建立 list

# 預設 value 是 set，可以直接 add
d = defaultdict(set)
d['a'].add(1); d['a'].add(2)  # d['a'] 會自動建立 set

# 傳統寫法，用 setdefault
d = {}
d.setdefault('a', []).append(1)  # 若 'a' 不存在，先建立空 list 再 append
