
# Remember（記憶）- enumerate() 和 zip()
# 本範例說明 Python enumerate() 與 zip() 的常見用法

# 建立一個顏色列表
colors = ["red", "green", "blue"]

# --- enumerate() 基本用法 ---
# enumerate() 會同時取得索引與元素，非常適合 for 迴圈
print("--- enumerate() 基本用法 ---")
for i, color in enumerate(colors):
    print(f"{i}: {color}")  # i 是索引，color 是對應元素

# --- enumerate(start=1) ---
# enumerate() 可指定起始索引（如從 1 開始）
print("\n--- enumerate(start=1) ---")
for i, color in enumerate(colors, 1):
    print(f"第{i}個: {color}")  # i 從 1 開始

# --- enumerate with 檔案 ---
# 常用 enumerate 處理逐行資料（如檔案）時加上行號
print("\n--- enumerate with 檔案 ---")
lines = ["line1", "line2", "line3"]
for lineno, line in enumerate(lines, 1):
    print(f"行 {lineno}: {line}")  # lineno 是行號

# --- zip() 基本用法 ---
# zip() 可同時遍歷多個序列，依序配對
print("\n--- zip() 基本用法 ---")
names = ["Alice", "Bob", "Carol"]
scores = [90, 85, 92]
for name, score in zip(names, scores):
    print(f"{name}: {score}")  # name 與 score 配對

# --- zip() 多個序列 ---
# zip() 可同時處理三個以上序列
print("\n--- zip() 多個序列 ---")
a = [1, 2, 3]
b = [10, 20, 30]
c = [100, 200, 300]
for x, y, z in zip(a, b, c):
    print(f"{x} + {y} + {z} = {x + y + z}")

# --- zip() 長度不同 ---
# zip() 只會配對到最短序列結束
print("\n--- zip() 長度不同 ---")
x = [1, 2]
y = ["a", "b", "c"]
print(f"list(zip(x, y)): {list(zip(x, y))}")  # 只配對到 x 結束

# 若要補齊較短序列，可用 itertools.zip_longest
from itertools import zip_longest
print(f"zip_longest: {list(zip_longest(x, y, fillvalue=0))}")  # 不足補 0

# --- 建立字典 ---
# zip() 常用於將兩個序列組成鍵值對，建立字典
print("\n--- 建立字典 ---")
keys = ["name", "age", "city"]
values = ["John", "30", "NYC"]
d = dict(zip(keys, values))
print(f"dict: {d}")
