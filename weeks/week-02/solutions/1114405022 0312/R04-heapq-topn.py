
import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.nlargest(3, nums)
heapq.nsmallest(3, nums)

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
]
heapq.nsmallest(1, portfolio, key=lambda s: s['price'])

heap = list(nums)
heapq.heapify(heap)
heapq.heappop(heap)
# R4. heapq 取 Top-N（1.4）

import heapq  # 匯入 heapq 模組

# 取出最大/最小的 N 個元素
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.nlargest(3, nums)    # 取出最大 3 個 [42, 37, 23]
heapq.nsmallest(3, nums)   # 取出最小 3 個 [-4, 1, 2]

# 取出物件中最小的（可用 key 指定欄位）
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
]
heapq.nsmallest(1, portfolio, key=lambda s: s['price'])  # 取 price 最小的那筆

# 將 list 轉成 heap 結構，然後彈出最小值
heap = list(nums)
heapq.heapify(heap)  # 轉成 heap
heapq.heappop(heap)  # 取出最小值
