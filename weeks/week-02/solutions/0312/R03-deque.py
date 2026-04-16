# R3. deque 保留最後 N 筆（1.3）
# 使用 collections.deque 來建立固定長度的佇列，適合處理滑動視窗資料

from collections import deque

q = deque(maxlen=3)  # 最多只保留 3 筆資料，超過會自動丟掉最舊的
q.append(1); q.append(2); q.append(3)
q.append(4)  # 自動丟掉最舊的 1

q = deque()
q.append(1); q.appendleft(2)  # 左邊插入
q.pop(); q.popleft()  # 右邊/左邊彈出
