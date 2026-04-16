
import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]
# R5. 優先佇列 PriorityQueue（1.5）

import heapq  # 匯入 heapq 模組

# 定義一個優先佇列類別
class PriorityQueue:
    def __init__(self):
        self._queue = []  # 儲存元素的 list
        self._index = 0   # 用來確保先進先出
    def push(self, item, priority):
        # 優先權大的先出（用負號），index 保證同優先權時先進先出
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        # 取出優先權最高的元素（item 在 tuple 最後一個位置）
        return heapq.heappop(self._queue)[-1]
