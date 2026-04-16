
from collections import deque

q = deque(maxlen=3)
q.append(1); q.append(2); q.append(3)
q.append(4)  # 自動丟掉最舊的 1

q = deque()
q.append(1); q.appendleft(2)
q.pop(); q.popleft()
# R3. deque 保留最後 N 筆（1.3）

from collections import deque  # 匯入 deque

# 設定 deque 最多只保留 3 筆資料
q = deque(maxlen=3)
q.append(1); q.append(2); q.append(3)  # 依序加入 1, 2, 3
q.append(4)  # 加入 4 後，最舊的 1 會自動被移除，q 內容變成 [2, 3, 4]

# 不設定 maxlen，deque 可無限長
q = deque()
q.append(1); q.appendleft(2)  # appendleft 會把 2 加到最左邊
q.pop(); q.popleft()  # pop() 取出最右邊，popleft() 取出最左邊
