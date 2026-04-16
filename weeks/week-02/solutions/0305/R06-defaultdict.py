# R6. 多值字典 defaultdict / setdefault（1.6）

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1); d['a'].append(2)

d = defaultdict(set)
d['a'].add(1); d['a'].add(2)  # d['a'] 會自動建立空 set

d = {}
d.setdefault('a', []).append(1)

# R6. 多值字典 defaultdict / setdefault（1.6）
# 本範例說明 defaultdict 與 setdefault 的多值字典用法

from collections import defaultdict

# 1. 預設值為 list
d = defaultdict(list)
d['a'].append(1); d['a'].append(2)  # d['a'] 會自動建立空 list

# 2. 預設值為 set
d = defaultdict(set)
d['a'].add(1); d['a'].add(2)  # d['a'] 會自動建立空 set

# 3. 傳統 setdefault 寫法
d = {}
d.setdefault('a', []).append(1)  # 若 'a' 不存在則建立空 list
