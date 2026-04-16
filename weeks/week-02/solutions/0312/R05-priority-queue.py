# R5. 優先佇列 PriorityQueue（1.5）
# 用 heapq 實作帶優先權的佇列，priority 越大越優先

import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0
    def push(self, item, priority):
        # 優先權高的先出（priority 越大越優先）
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1
    def pop(self):
        return heapq.heappop(self._queue)[-1]
