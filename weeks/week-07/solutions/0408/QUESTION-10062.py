"""
UVA 10062 問題解法
根據每頭乳牛前面編號比它小的乳牛數，還原正確排列順序。
"""
# 方法：逆向思考，從最後一頭乳牛往前插入
# 使用 BIT（樹狀數組）或線段樹可達 O(N log N)，但 N <= 80000，直接用 list 也可

from typing import List

def restore_cows(order: List[int]) -> List[int]:
    """
    order: 長度 N-1，order[i] 表示第 i+1 頭牛前面有多少頭編號比它小的牛
    回傳: 長度 N，為正確排列的乳牛編號（1~N）
    """
    N = len(order) + 1
    res = [0] * N
    available = list(range(1, N+1))  # 可用的編號
    for i in range(N-1, -1, -1):
        idx = order[i-1] if i > 0 else 0
        res[i] = available.pop(idx)
    return res

if __name__ == "__main__":
    # 讀取輸入
    import sys
    lines = [line.strip() for line in sys.stdin if line.strip()]
    N = int(lines[0])
    order = list(map(int, lines[1:]))
    ans = restore_cows(order)
    for num in ans:
        print(num)
