
# U5. 優先佇列為何要加 index（1.5）
# 本範例說明 heapq 優先佇列為何要加 index

import heapq

class Item:
    def __init__(self, name):
        self.name = name

pq = []
# 若只放 (priority, item)，同 priority 會比較 item，Item 不支援 < 會炸
# heapq.heappush(pq, (-1, Item('a')))
# heapq.heappush(pq, (-1, Item('b')))  # TypeError

# 正解：加 index 避免比較 item，確保同 priority 依加入順序
idx = 0
heapq.heappush(pq, (-1, idx, Item('a'))); idx += 1
heapq.heappush(pq, (-1, idx, Item('b'))); idx += 1
