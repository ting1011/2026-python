def count(n):
c = count(0)

# Understand（理解）- itertools 工具函數
# 本範例說明 Python itertools 常用工具函數的用法

from itertools import islice, dropwhile, takewhile, chain, permutations, combinations

# --- islice() 切片 ---
# islice 可對無窮迭代器或一般序列做切片
print("--- islice() 切片 ---")
def count(n):
    i = n
    while True:
        yield i  # 產生無窮遞增數列
        i += 1

c = count(0)
result = list(islice(c, 5, 10))  # 取第 5~9 個元素
print(f"islice(c, 5, 10): {result}")

# --- dropwhile() 條件跳過 ---
# dropwhile 只要條件為真就跳過，直到遇到第一個為假才開始回傳剩下元素
print("\n--- dropwhile() 條件跳過 ---")
nums = [1, 3, 5, 2, 4, 6]
result = list(dropwhile(lambda x: x < 5, nums))
print(f"dropwhile(x<5, {nums}): {result}")

# --- takewhile() 條件取用 ---
# takewhile 只要條件為真就取用，遇到第一個為假就停止
print("\n--- takewhile() 條件取用 ---")
result = list(takewhile(lambda x: x < 5, nums))
print(f"takewhile(x<5, {nums}): {result}")

# --- chain() 串聯 ---
# chain 可將多個序列串接成一個迭代器
print("\n--- chain() 串聯 ---")
a = [1, 2]
b = [3, 4]
c = [5]
print(f"chain(a, b, c): {list(chain(a, b, c))}")

# --- permutations() 排列 ---
# permutations 產生所有可能的排列（順序有差）
print("\n--- permutations() 排列 ---")
items = ["a", "b", "c"]
print(f"permutations(items):")
for p in permutations(items):
    print(f"  {p}")

print(f"permutations(items, 2):")
for p in permutations(items, 2):
    print(f"  {p}")

# --- combinations() 組合 ---
# combinations 產生所有可能的組合（順序無差）
print("\n--- combinations() 組合 ---")
print(f"combinations(items, 2):")
for c in combinations(items, 2):
    print(f"  {c}")

# --- 組合應用：密碼窮舉 ---
# 用排列與組合窮舉所有密碼可能
print("\n--- 組合應用：密碼窮舉 ---")
chars = ["A", "B", "1"]
print("2位數密碼:")
for p in permutations(chars, 2):
    print(f"  {''.join(p)}")  # 不重複排列

print("2位數密碼（可重複）:")
from itertools import combinations_with_replacement
for p in combinations_with_replacement(chars, 2):
    print(f"  {''.join(p)}")  # 可重複組合
