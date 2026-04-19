# U5. 優先佇列為何要加 index（1.5）

import heapq

class Item:
    def __init__(self, name):
        self.name = name

# 用 list 當作 heap 容器
pq = []
# 若只放 (priority, item)，同 priority 會比較 item，Item 不支援 < 會炸
# heapq.heappush(pq, (-1, Item('a')))
# heapq.heappush(pq, (-1, Item('b')))  # TypeError

# 正解：加 index 避免比較 item
# 當 priority 相同時，heapq 會比較下一欄 index，保證可比較且穩定
idx = 0
heapq.heappush(pq, (-1, idx, Item('a'))); idx += 1
heapq.heappush(pq, (-1, idx, Item('b'))); idx += 1

first = heapq.heappop(pq)
second = heapq.heappop(pq)
print('依序彈出:', first[2].name, second[2].name)
