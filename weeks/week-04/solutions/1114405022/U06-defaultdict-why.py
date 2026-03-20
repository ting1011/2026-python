
# U6. defaultdict 為何比手動初始化乾淨（1.6）
# 本範例說明 defaultdict 如何讓多值字典初始化更簡潔


from collections import defaultdict  # 匯入 defaultdict，可自動初始化預設值


pairs = [('a', 1), ('a', 2), ('b', 3)]  # 一組 (key, value) 配對的列表


# 手動版：每次都要判斷 key 是否存在，若不存在要先初始化
d = {}
for k, v in pairs:
    if k not in d:  # 若 key 不存在，先建立空 list
        d[k] = []
    d[k].append(v)  # 將 value 加入對應的 list


# defaultdict 版：自動初始化，省去 if 判斷
d2 = defaultdict(list)  # 當 key 不存在時，自動建立空 list
for k, v in pairs:
    d2[k].append(v)  # 直接 append，不需判斷 key 是否存在
