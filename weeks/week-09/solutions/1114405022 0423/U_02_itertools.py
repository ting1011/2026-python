# Understand（理解）- itertools 工具函數
# 本模塊演示 Python itertools 庫中的常用高效迭代工具
# itertools 提供了許多用於創建迭代器的函數，可以用於快速高效地迭代數據

from itertools import islice, dropwhile, takewhile, chain, permutations, combinations

print("--- islice() 切片 ---")
# islice() 用途：對迭代器進行切片操作，類似於 list[start:stop:step]
# 特點：可以處理無限迭代器，返回指定範圍內的元素


def count(n):
    # 自定義生成器：從 n 開始無限遞增整數
    # 這是一個無限迭代器，會持續產生下一個數字
    i = n
    while True:
        yield i  # 產生當前值並暫停
        i += 1    # 下次調用時繼續遞增


c = count(0)  # 創建一個從 0 開始的無限計數器
# islice(c, 5, 10) 表示：跳過前 5 個元素，然後取 10-5=5 個元素
# 即取出第 5-9 位置的元素（索引）
result = list(islice(c, 5, 10))
print(f"islice(c, 5, 10): {result}")  # 輸出：[5, 6, 7, 8, 9]

print("\n--- dropwhile() 條件跳過 ---")
# dropwhile() 用途：跳過滿足條件的元素，直到遇到不滿足條件的元素
# 特點：一旦遇到不滿足條件的元素，後面的所有元素都會被保留（即使它們滿足條件）
nums = [1, 3, 5, 2, 4, 6]
# dropwhile(lambda x: x < 5, nums) 表示：
# - 1 < 5 ✓ 跳過
# - 3 < 5 ✓ 跳過  
# - 5 < 5 ✗ 停止跳過，從這裡開始收集剩下的所有元素
result = list(dropwhile(lambda x: x < 5, nums))
print(f"dropwhile(x<5, {nums}): {result}")  # 輸出：[5, 2, 4, 6]

print("\n--- takewhile() 條件取用 ---")
# takewhile() 用途：取用滿足條件的元素，直到遇到不滿足條件的元素就停止
# 特點：與 dropwhile() 相反，這個是取而不是跳
# 一旦遇到不滿足條件的元素，立即停止（後面即使有滿足條件的元素也被忽略）
result = list(takewhile(lambda x: x < 5, nums))
# takewhile(lambda x: x < 5, [1, 3, 5, 2, 4, 6]) 表示：
# - 1 < 5 ✓ 取用
# - 3 < 5 ✓ 取用
# - 5 < 5 ✗ 不滿足條件，立即停止
print(f"takewhile(x<5, {nums}): {result}")  # 輸出：[1, 3]

print("\n--- chain() 串聯 ---")
# chain() 用途：將多個可迭代對象串聯成一個長的迭代器
# 特點：比直接用 + 連接列表更高效，尤其是對大量數據或無限迭代器
# 返回一個迭代器，按順序遍歷所有輸入的可迭代對象
a = [1, 2]    # 第一個列表
b = [3, 4]    # 第二個列表
c = [5]       # 第三個列表
# chain(a, b, c) 將三個列表連接為一個流：1 -> 2 -> 3 -> 4 -> 5
print(f"chain(a, b, c): {list(chain(a, b, c))}")  # 輸出：[1, 2, 3, 4, 5]

print("\n--- permutations() 排列 ---")
# permutations() 用途：生成所有可能的排列組合
# 特點：順序重要，['a','b'] 和 ['b','a'] 是不同的排列
# 不包含重複元素，每個排列中的元素都不同
items = ["a", "b", "c"]
# permutations(items) 無指定長度時，返回完整長度（3個元素）的所有排列
# 共有 3! = 6 種排列方式
print(f"permutations(items):")
for p in permutations(items):
    print(f"  {p}")  # 輸出：(a,b,c) (a,c,b) (b,a,c) (b,c,a) (c,a,b) (c,b,a)

# permutations(items, 2) 指定長度為 2 的排列
# 從 3 個元素中選 2 個並排列：3 × 2 = 6 種
print(f"permutations(items, 2):")
for p in permutations(items, 2):
    print(f"  {p}")  # 輸出：(a,b) (a,c) (b,a) (b,c) (c,a) (c,b)

print("\n--- combinations() 組合 ---")
# combinations() 用途：生成所有可能的組合
# 特點：順序不重要，['a','b'] 和 ['b','a'] 是同一個組合（只有一個）
# 不包含重複元素，每個組合中的元素都不同
# combinations(items, 2) 表示從 3 個元素中選 2 個，共有 C(3,2) = 3 種
print(f"combinations(items, 2):")
for c in combinations(items, 2):
    print(f"  {c}")  # 輸出：(a,b) (a,c) (b,c)

print("\n--- 組合應用：密碼窮舉 ---")
# 實際應用：使用 permutations 和 combinations_with_replacement 進行密碼暴力破解演示
chars = ["A", "B", "1"]  # 可用字符集

# 使用 permutations：順序敏感，不允許重複
# permutations(chars, 2) 生成所有 2 位密碼排列
print("2位數密碼（不重複，順序敏感）:")
for p in permutations(chars, 2):
    print(f"  {''.join(p)}")  # 輸出：AB A1 BA B1 1A 1B

print("2位數密碼（允許重複，順序敏感）:")
from itertools import combinations_with_replacement

# combinations_with_replacement：允許重複字符，但會去除重複的組合
# 實際應該用 product 來模擬允許重複的排列，但這裡示例展示組合的概念
for p in combinations_with_replacement(chars, 2):
    print(f"  {''.join(p)}")  # 輸出：AA AB A1 BB B1 11
