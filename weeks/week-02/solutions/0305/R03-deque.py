
# R3. deque 保留最後 N 筆（1.3）
# 本範例說明 collections.deque 的基本用法

from collections import deque

# 1. 設定 maxlen，僅保留最後 N 筆資料
q = deque(maxlen=3)
q.append(1); q.append(2); q.append(3)  # 目前內容 [1, 2, 3]
q.append(4)  # 超過 3 筆，自動丟掉最舊的 1，內容變 [2, 3, 4]

# 2. 雙向佇列操作

# 2. 雙向佇列操作
q = deque()
q.append(1)        # 從右邊加入 1
q.appendleft(2)    # 從左邊加入 2，內容 [2, 1]
right = q.pop()            # 從右邊移除（回傳 1）
left = q.popleft()        # 從左邊移除（回傳 2）

if __name__ == "__main__":
	q1 = deque(maxlen=3)
	q1.append(1); q1.append(2); q1.append(3)
	q1.append(4)
	print("q1 (maxlen=3) 結果:", list(q1))
	q2 = deque()
	q2.append(1)
	q2.appendleft(2)
	print("q2 append/appendleft 結果:", list(q2))
	print("q2 pop 結果:", q2.pop() if q2 else None)
	q2.append(3)
	print("q2 popleft 結果:", q2.popleft() if q2 else None)
