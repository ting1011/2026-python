
# R5. 優先佇列 PriorityQueue（1.5）
# 本範例說明如何用 heapq 實作優先權佇列

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []  # 儲存元素的 heap
        self._index = 0   # 維持先後順序
    def push(self, item, priority):
        # 優先權用負號，數字越大優先權越高
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        # 彈出優先權最高的元素
        return heapq.heappop(self._queue)[-1]
