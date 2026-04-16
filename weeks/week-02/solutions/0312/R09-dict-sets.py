# R9. 兩字典相同點：keys/items 集合運算（1.9）
# 可用 &、- 等集合運算找出 key 或 (key, value) 的交集、差集

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

# 共同的 key
print(a.keys() & b.keys())  # {'x', 'y'}
# a 有但 b 沒有的 key
print(a.keys() - b.keys())  # {'z'}
# 共同的 (key, value) 對
print(a.items() & b.items())  # {('y', 2)}

# 字典推導式：排除特定 key
c = {k: a[k] for k in a.keys() - {'z', 'w'}}
