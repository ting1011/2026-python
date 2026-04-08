"""
UVA 10093 更簡易記憶版
暴力窮舉所有可能的部署組合，僅適合 N, M 很小時理解題意。
"""
# 這個方法直接用遞迴窮舉所有平原格子的選擇組合，並檢查是否互不攻擊
# 僅適合 N, M 很小時（如 3x3 以內）
def max_artillery_easy(N, M, grid):
    """
    N: 列數, M: 行數, grid: N 行 M 字元陣列
    回傳: 最多能部署的炮兵部隊數量
    """
    # 取得所有平原格子座標
    plains = [(i, j) for i in range(N) for j in range(M) if grid[i][j]=='P']
    total = len(plains)
    best = 0
    from itertools import combinations
    # 檢查一組選擇是否互不攻擊
    def valid(selected):
        for x1, y1 in selected:
            for x2, y2 in selected:
                if (x1, y1) == (x2, y2): continue
                if abs(x1-x2)<=2 and y1==y2: return False
                if abs(y1-y2)<=2 and x1==x2: return False
        return True
    # 枚舉所有可能選擇
    for k in range(total+1):
        for comb in combinations(plains, k):
            if valid(comb):
                best = max(best, k)
    return best

if __name__ == "__main__":
    N, M = map(int, input().split())
    grid = [input().strip() for _ in range(N)]
    print(max_artillery_easy(N, M, grid))
