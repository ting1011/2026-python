
# U4. heap 為何能高效拿 Top-N（1.4）
# 本範例說明 heapq 如何高效取得最小值（Top-N）


import heapq  # 匯入 heapq，提供 heap（最小堆積）操作


nums = [5, 1, 9, 2]  # 一個整數列表
h = nums[:]  # 複製一份 nums，避免改動原始資料
heapq.heapify(h)  # 將 h 轉成 heap 結構，h[0] 會是最小值
# h[0] 永遠是最小值（這是 heap 的核心性質）
m = heapq.heappop(h)  # 每次 heappop 都會移除並回傳目前最小值
