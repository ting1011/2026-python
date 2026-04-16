a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}
a.keys() & b.keys()
a.keys() - b.keys()
a.items() & b.items()

c = {k: a[k] for k in a.keys() - {'z', 'w'}}

if __name__ == "__main__":
	print("a.keys() & b.keys():", a.keys() & b.keys())
	print("a.keys() - b.keys():", a.keys() - b.keys())
	print("a.items() & b.items():", a.items() & b.items())
	print("c:", c)

# R9. 兩字典相同點：keys/items 集合運算（1.9）
# 本範例說明字典的 keys/items 可做集合運算

a = {'x': 1, 'y': 2, 'z': 3}
b = {'w': 10, 'x': 11, 'y': 2}

# 1. 共同的 key
a.keys() & b.keys()  # {'x', 'y'}
# 2. a 有但 b 沒有的 key
a.keys() - b.keys()  # {'z'}
# 3. 共同的 (key, value) 對
a.items() & b.items()  # {('y', 2)}

# 4. 字典推導式，排除特定 key
c = {k: a[k] for k in a.keys() - {'z', 'w'}}  # 只保留 'x', 'y'
