# U6. defaultdict 為何比手動初始化乾淨（1.6）

from collections import defaultdict

# 每個 key 可能會對應多個值
pairs = [('a', 1), ('a', 2), ('b', 3)]

# 手動版：一直判斷 key 是否存在
d = {}
for k, v in pairs:
    if k not in d:
        # 第一次看到該 key 時，先建立空 list
        d[k] = []
    d[k].append(v)

# defaultdict：省掉初始化分支
# defaultdict(list) 會在 key 不存在時自動建立 []
d2 = defaultdict(list)
for k, v in pairs:
    d2[k].append(v)

print('手動初始化結果:', d)
print('defaultdict 結果:', dict(d2))
