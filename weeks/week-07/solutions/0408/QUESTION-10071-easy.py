"""
UVA 10071 更簡易記憶版
暴力窮舉所有 a+b+c+d+e=f 的六元組，適合理解題意與小資料測試。
"""
# 這個方法直接用六重迴圈，僅適合 N 很小時（如 N<=10）
def count_six_tuples_easy(S):
    """
    S: List[int]，集合 S
    回傳: 滿足 a+b+c+d+e=f 的六元組數量
    """
    N = len(S)
    ans = 0
    for a in S:
        for b in S:
            for c in S:
                for d in S:
                    for e in S:
                        for f in S:
                            if a+b+c+d+e == f:
                                ans += 1
    return ans

if __name__ == "__main__":
    N = int(input())
    S = [int(input()) for _ in range(N)]
    print(count_six_tuples_easy(S))
