
# Remember（記憶）- 迭代器基礎概念
# 本範例說明 Python 迭代器（iterator）與可迭代物件（iterable）的基本用法與自訂方式


# 1. 迭代器協議的核心方法
items = [1, 2, 3]  # 建立一個列表

# iter() 會呼叫物件的 __iter__() 方法，回傳一個迭代器
it = iter(items)
print(f"迭代器: {it}")  # 顯示這是一個 list_iterator 物件

# next() 會呼叫迭代器的 __next__() 方法，依序取得元素
print(f"第一個: {next(it)}")  # 取得 1
print(f"第二個: {next(it)}")  # 取得 2
print(f"第三個: {next(it)}")  # 取得 3

# 如果沒有更多元素，next() 會拋出 StopIteration 例外
try:
    next(it)
except StopIteration:
    print("迭代結束!")  # 捕捉例外並顯示訊息


# 2. 常見可迭代物件
print("\n--- 常見可迭代物件 ---")

# 列表（list）是可迭代物件
print(f"列表 iter: {iter([1, 2, 3])}")

# 字串（str）也是可迭代物件
print(f"字串 iter: {iter('abc')}")

# 字典（dict）也是可迭代物件
print(f"字典 iter: {iter({'a': 1, 'b': 2})}")

# 檔案物件也是可迭代物件，可以逐行讀取
import io
f = io.StringIO("line1\nline2\nline3")
print(f"檔案 iter: {iter(f)}")



# 3. 自訂可迭代物件
# 定義一個倒數的可迭代物件 CountDown
class CountDown:
    def __init__(self, start):
        self.start = start  # 記錄起始數字

    def __iter__(self):
        # 回傳一個自訂的迭代器物件
        return CountDownIterator(self.start)

# 這是實際執行倒數的迭代器
class CountDownIterator:
    def __init__(self, start):
        self.current = start  # 記錄目前數字

    def __next__(self):
        # 如果倒數到 0，拋出 StopIteration
        if self.current <= 0:
            raise StopIteration
        self.current -= 1  # 每次呼叫減 1
        return self.current + 1  # 回傳目前數字

print("\n--- 自訂迭代器 ---")

# 使用 for 迴圈遍歷自訂的倒數迭代器
for i in CountDown(3):
    print(i, end=" ")  # 預期輸出: 3 2 1


# 4. 迭代器 vs 可迭代物件
print("\n\n--- 迭代器 vs 可迭代物件 ---")

# 列表是「可迭代物件」，但不是「迭代器」
my_list = [1, 2, 3]
print(f"列表: 可迭代物件 ✓, 迭代器 ✗")

# 用 iter() 取得列表的迭代器
my_iter = iter(my_list)
print(f"iter(列表): 可迭代物件 ✗, 迭代器 ✓")

# 迭代器本身同時也是可迭代物件（有 __iter__ 方法），也是迭代器（有 __next__ 方法）
print(f"迭代器: 可迭代物件 ✓ (有__iter__), 迭代器 ✓ (有__next__)")


# 5. StopIteration 例外
print("\n--- StopIteration 用法 ---")

# 手動遍歷一個可迭代物件（模擬 for 迴圈的行為）
def manual_iter(items):
    it = iter(items)  # 取得迭代器
    while True:
        try:
            item = next(it)  # 取得下一個元素
            print(f"取得: {item}")
        except StopIteration:
            break  # 沒有元素時跳出

manual_iter(["a", "b", "c"])

# 使用 next() 的預設值參數，避免拋出例外
def manual_iter_default(items):
    it = iter(items)
    while True:
        item = next(it, None)  # 若結束則回傳 None
        if item is None:
            break
        print(f"取得: {item}")

print("\n使用預設值:")
manual_iter_default(["a", "b", "c"])
