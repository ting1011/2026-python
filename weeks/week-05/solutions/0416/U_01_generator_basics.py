
# Understand（理解）- 生成器概念
# 本範例說明 Python 生成器（generator）的基本用法與進階技巧

# frange: 產生一個浮點數範圍的生成器
def frange(start, stop, step):
    x = start
    while x < stop:
        yield x  # 使用 yield 產生序列中的下一個值
        x += step

# 將 frange 生成器轉為列表，顯示所有值
result = list(frange(0, 2, 0.5))
print(f"frange(0, 2, 0.5): {result}")

# countdown: 倒數生成器，每次產生一個數字
def countdown(n):
    print(f"Starting countdown from {n}")
    while n > 0:
        yield n  # 產生目前數字
        n -= 1
    print("Done!")  # 結束時顯示

print("\n--- 建立生成器 ---")
c = countdown(3)  # 建立生成器物件
print(f"生成器物件: {c}")

print("\n--- 逐步迭代 ---")
# 用 next() 逐步取得生成器的值
print(f"next(c): {next(c)}")
print(f"next(c): {next(c)}")
print(f"next(c): {next(c)}")

try:
    next(c)  # 沒有值時會拋出 StopIteration
except StopIteration:
    print("StopIteration!")

# fibonacci: 無限費波那契數列生成器
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b  # 更新數列

print("\n--- Fibonacci 生成器 ---")
fib = fibonacci()
for i in range(10):
    print(next(fib), end=" ")  # 取前 10 項
print()

# chain_iter: 將多個可迭代物件串接起來
def chain_iter(*iterables):
    for it in iterables:
        yield from it  # 直接產生子迭代器的所有元素

print("\n--- yield from 用法 ---")
result = list(chain_iter([1, 2], [3, 4], [5, 6]))
print(f"chain_iter: {result}")



# Node: 樹狀結構的節點類別
class Node:
    def __init__(self, value):
        self.value = value  # 節點的值
        self.children = []  # 子節點列表

    def add_child(self, node):
        self.children.append(node)  # 加入子節點

    def __iter__(self):
        return iter(self.children)  # 允許直接 for child in node

    def depth_first(self):
        yield self  # 先產生自己
        for child in self:
            yield from child.depth_first()  # 再遞迴產生所有子孫

print("\n--- 樹的深度優先遍歷 ---")
root = Node(0)
root.add_child(Node(1))
root.add_child(Node(2))
root.children[0].add_child(Node(3))
root.children[0].add_child(Node(4))

for node in root.depth_first():
    print(node.value, end=" ")  # 預期輸出: 0 1 3 4 2
print()

# flatten: 將巢狀序列攤平成一維序列
def flatten(items):
    for x in items:
        # 如果 x 是可迭代物件（但不是字串），遞迴攤平
        if hasattr(x, "__iter__") and not isinstance(x, str):
            yield from flatten(x)
        else:
            yield x  # 不是可迭代物件就直接產生

print("\n--- 巢狀序列攤平 ---")
nested = [1, [2, [3, 4]], 5]
print(f"展開: {list(flatten(nested))}")
