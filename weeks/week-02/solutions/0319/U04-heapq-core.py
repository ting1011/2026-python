# U4. heap 為何能高效拿 Top-N（1.4）

import heapq

# 原始資料
nums = [5, 1, 9, 2]

# 複製一份資料再轉成 heap，避免改動原始串列
h = nums[:]
heapq.heapify(h)

# h[0] 永遠是最小值（這是 heap 的核心性質）

# heappop 每次都彈出目前最小元素，時間複雜度為 O(log n)
m = heapq.heappop(h)  # 每次 pop 都拿到目前最小
print('heapify 後:', h)
print('彈出的最小值:', m)
print('彈出後 heap:', h)
