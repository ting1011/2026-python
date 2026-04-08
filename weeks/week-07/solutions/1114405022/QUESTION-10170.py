"""
UVA 10170 標準解
給定起始人數 S 與查詢天數 D，找出第 D 天住宿的旅行團人數。
"""
# 只要找到最小的 n，使 S + (S+1) + ... + n >= D
# 也就是 S 到 n 的等差級數和 >= D
# 累加到第 k 團：sum = (S + n) * (n - S + 1) // 2

def find_group(S, D):
    """
    S: 起始人數, D: 查詢天數
    回傳: 第 D 天住宿的旅行團人數
    """
    n = S
    total = 0
    while True:
        total += n
        if total >= D:
            return n
        n += 1

if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        if not line.strip(): continue
        S, D = map(int, line.strip().split())
        print(find_group(S, D))
