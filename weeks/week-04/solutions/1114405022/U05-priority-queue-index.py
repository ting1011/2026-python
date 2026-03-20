
# U5. 優先佇列為何要加 index（1.5）
# 本範例說明為什麼 heapq 優先佇列要加 index，避免同 priority 時比較不可比的物件


import heapq  # 匯入 heapq，提供 heap 操作


class Item:
    def __init__(self, name):
        self.name = name  # Item 只記錄名字，沒有定義 < 運算


pq = []  # 建立一個空的優先佇列
# 若只放 (priority, item)，當 priority 相同時，heapq 會比較 item，但 Item 沒有 < 運算，會 TypeError
# heapq.heappush(pq, (-1, Item('a')))
# heapq.heappush(pq, (-1, Item('b')))  # TypeError，因為 Item 物件無法比較大小


# 正解：加 index 避免比較 item，當 priority 相同時，用 index 決定順序
idx = 0
heapq.heappush(pq, (-1, idx, Item('a'))); idx += 1  # (-1, 0, Item('a'))
heapq.heappush(pq, (-1, idx, Item('b'))); idx += 1  # (-1, 1, Item('b'))
