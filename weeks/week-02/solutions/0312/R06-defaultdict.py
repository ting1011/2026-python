# R6. 多值字典 defaultdict / setdefault（1.6）
# defaultdict 可自動建立預設型態的 value，適合多值分組

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1); d['a'].append(2)  # d['a'] 會自動是 list

d = defaultdict(set)
d['a'].add(1); d['a'].add(2)  # d['a'] 會自動是 set

d = {}
d.setdefault('a', []).append(1)  # 傳統寫法
