
# U3. deque(maxlen=N) 為何能保留最後 N 筆（1.3）
# 本範例說明 deque 設定 maxlen 只保留最後 N 筆資料

from collections import deque

q = deque(maxlen=3)
for i in [1, 2, 3, 4, 5]:
    q.append(i)  # 超過 3 筆會自動丟掉最舊的
# 結果只剩 [3, 4, 5]
