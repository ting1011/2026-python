# R4. heapq 取 Top-N（1.4）
# 使用 heapq 取得最大/最小的 N 筆資料，適合大量資料取極值

import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
heapq.nlargest(3, nums)    # 最大的 3 筆
heapq.nsmallest(3, nums)   # 最小的 3 筆

portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
]
heapq.nsmallest(1, portfolio, key=lambda s: s['price'])  # 依 price 取最小

heap = list(nums)
heapq.heapify(heap)  # 轉成 heap 結構
heapq.heappop(heap)  # 彈出最小值
