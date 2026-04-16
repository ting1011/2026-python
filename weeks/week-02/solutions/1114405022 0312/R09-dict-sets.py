
a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

a.keys() & b.keys()
a.keys() - b.keys()
a.items() & b.items()

c = {k: a[k] for k in a.keys() - {'z', 'w'}}
# R9. 兩字典相同點：keys/items 集合運算（1.9）

# 建立兩個字典
a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

# 取兩字典的共同 key
a.keys() & b.keys()  # {'x', 'y'}
# 取 a 有但 b 沒有的 key
a.keys() - b.keys()  # {'z'}
# 取兩字典的共同 (key, value) 對
a.items() & b.items()  # {('y', 2)}

# 字典推導式，排除特定 key
c = {k: a[k] for k in a.keys() - {'z', 'w'}}  # 只保留 'x', 'y'
