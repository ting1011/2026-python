
# U3. deque(maxlen=N) 為何能保留最後 N 筆（1.3）
# 本範例說明 deque 設定 maxlen 後，會自動只保留最後 N 筆資料


from collections import deque  # 匯入 deque，雙端佇列，可設定最大長度


q = deque(maxlen=3)  # 建立一個最大長度為 3 的 deque
for i in [1, 2, 3, 4, 5]:  # 依序將 1~5 加入 deque
    q.append(i)  # 若超過最大長度，最舊的元素會自動被移除
# 結果只剩 [3, 4, 5]，只保留最後 3 筆資料
