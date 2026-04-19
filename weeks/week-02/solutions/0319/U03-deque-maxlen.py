# U3. deque(maxlen=N) 為何能保留最後 N 筆（1.3）

from collections import deque

# 設定 maxlen=3，代表最多只保留 3 筆
q = deque(maxlen=3)

# 每次 append 新元素，超過容量時會自動丟掉最舊的
for i in [1, 2, 3, 4, 5]:
    q.append(i)

# 結果只剩 [3, 4, 5]
print('deque 內容:', list(q))
