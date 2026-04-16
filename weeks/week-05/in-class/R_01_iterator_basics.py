
"""
Remember（記憶）- 迭代器基礎概念
本檔案示範：
1. 迭代器協議的基本用法
2. 常見可迭代物件
3. 自訂可迭代物件與迭代器
4. 迭代器 vs 可迭代物件
5. StopIteration 用法
"""


# 1. 迭代器協議的核心方法
items = [1, 2, 3]

# iter() 會呼叫物件的 __iter__()，回傳一個迭代器
it = iter(items)
print(f"迭代器: {it}")

# next() 會呼叫迭代器的 __next__()，取得下一個元素
print(f"第一個: {next(it)}")  # 1
print(f"第二個: {next(it)}")  # 2
print(f"第三個: {next(it)}")  # 3

# 沒有更多元素時，next() 會擲出 StopIteration 例外
try:
    next(it)
except StopIteration:
    print("迭代結束!")

f = io.StringIO("line1\nline2\nline3")

# 2. 常見可迭代物件
print("\n--- 常見可迭代物件 ---")

# 列表、字串、字典、檔案等都可用 iter() 取得迭代器
print(f"列表 iter: {iter([1, 2, 3])}")
print(f"字串 iter: {iter('abc')}")
print(f"字典 iter: {iter({'a': 1, 'b': 2})}")

import io
f = io.StringIO("line1\nline2\nline3")
print(f"檔案 iter: {iter(f)}")



# 3. 自訂可迭代物件
# CountDown 是一個可迭代物件，__iter__ 回傳一個迭代器
class CountDown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        return CountDownIterator(self.start)

# CountDownIterator 是真正的迭代器，實作 __next__
class CountDownIterator:
    def __init__(self, start):
        self.current = start

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        self.current -= 1
        return self.current + 1

print("\n--- 自訂迭代器 ---")
for i in CountDown(3):
    print(i, end=" ")  # 3 2 1


# 4. 迭代器 vs 可迭代物件
print("\n\n--- 迭代器 vs 可迭代物件 ---")

# 列表是可迭代物件（有 __iter__），但不是迭代器（沒 __next__）
my_list = [1, 2, 3]
print(f"列表: 可迭代物件 ✓, 迭代器 ✗")

# 用 iter() 取得的才是迭代器
my_iter = iter(my_list)
print(f"iter(列表): 可迭代物件 ✗, 迭代器 ✓")

# 迭代器本身同時有 __iter__ 和 __next__
print(f"迭代器: 可迭代物件 ✓ (有__iter__), 迭代器 ✓ (有__next__)" )


# 5. StopIteration 例外
print("\n--- StopIteration 用法 ---")



# 手動遍歷迭代器，捕捉 StopIteration 例外
def manual_iter(items):
    it = iter(items)
    while True:
        try:
            item = next(it)
            print(f"取得: {item}")
        except StopIteration:
            break

manual_iter(["a", "b", "c"])



# next() 可給預設值，避免 StopIteration
def manual_iter_default(items):
    it = iter(items)
    while True:
        item = next(it, None)  # 預設值
        if item is None:
            break
        print(f"取得: {item}")

print("\n使用預設值:")
manual_iter_default(["a", "b", "c"])
