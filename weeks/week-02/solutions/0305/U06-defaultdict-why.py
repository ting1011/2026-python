
# U6. defaultdict 為何比手動初始化乾淨（1.6）
# 本範例說明 defaultdict 可自動初始化，程式更簡潔

from collections import defaultdict

pairs = [('a', 1), ('a', 2), ('b', 3)]

# 手動版：每次都要判斷 key 是否存在
d = {}
for k, v in pairs:
    if k not in d:
        d[k] = []  # 若 key 不存在要先建立
    d[k].append(v)

# defaultdict：自動初始化，程式更乾淨
d2 = defaultdict(list)
for k, v in pairs:
    d2[k].append(v)
