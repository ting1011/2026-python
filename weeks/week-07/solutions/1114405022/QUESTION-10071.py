"""
UVA 10071 標準解
計算集合 S 中滿足 a+b+c+d+e=f 的六元組數量。
"""
# 由於 S 最多 100 個元素，暴力窮舉五重迴圈計算 a+b+c+d+e，然後檢查 f 是否在 S
# 時間複雜度 O(N^5)，N=100 時約 10^10，不可行。
# 需優化：
# 先計算所有 a+b+c 的和出現次數，再計算 d+e-f 是否能湊出。

from collections import Counter

def count_six_tuples(S):
    """
    S: List[int]，集合 S
    回傳: 滿足 a+b+c+d+e=f 的六元組數量
    """
    N = len(S)
    sum_abc = Counter()
    for a in S:
        for b in S:
            for c in S:
                sum_abc[a+b+c] += 1
    ans = 0
    for d in S:
        for e in S:
            for f in S:
                ans += sum_abc[d+e-f]
    return ans

if __name__ == "__main__":
    # 讀取輸入
    N = int(input())
    S = [int(input()) for _ in range(N)]
    print(count_six_tuples(S))
