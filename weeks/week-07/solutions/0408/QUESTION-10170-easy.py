"""
UVA 10170 更簡易記憶版
直接暴力累加天數直到超過 D，適合理解題意與小型測資。
"""
def find_group_easy(S, D):
    """
    S: 起始人數, D: 查詢天數
    回傳: 第 D 天住宿的旅行團人數
    """
    n = S
    total = 0
    while total < D:
        total += n
        if total >= D:
            return n
        n += 1

if __name__ == "__main__":
    import sys
    for line in sys.stdin:
        if not line.strip(): continue
        S, D = map(int, line.strip().split())
        print(find_group_easy(S, D))
