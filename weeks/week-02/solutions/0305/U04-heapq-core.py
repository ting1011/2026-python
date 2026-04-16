
# U4. heap 為何能高效拿 Top-N（1.4）
# 本範例說明 heapq 維持最小值的原理

import heapq

nums = [5, 1, 9, 2]
h = nums[:]
heapq.heapify(h)  # 轉成小根堆，h[0] 永遠是最小值
# h[0] 永遠是最小值（這是 heap 的核心性質）
m = heapq.heappop(h)  # 每次 pop 都拿到目前最小
