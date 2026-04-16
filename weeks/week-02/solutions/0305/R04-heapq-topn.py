
# R4. heapq 取 Top-N（1.4）
# 本範例說明 heapq 模組取最大/最小 N 筆資料

import heapq


# 1. 取最大/最小 N 筆
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]

# 2. 取物件序列的最小值
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
]

# 3. heapify 轉成小根堆，heappop 彈出最小值
heap = list(nums)
heapq.heapify(heap)  # 原地轉成小根堆

if __name__ == "__main__":
    print("最大3筆:", heapq.nlargest(3, nums))
    print("最小3筆:", heapq.nsmallest(3, nums))
    print("portfolio最小price:", heapq.nsmallest(1, portfolio, key=lambda s: s['price']))
    print("heappop最小值:", heapq.heappop(heap))
