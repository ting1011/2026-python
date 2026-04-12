"""
UVA 10093 標準解
最大獨立集問題，狀態壓縮動態規劃（DP + bitmask）。
"""
# 將每一列的部署狀態用 bitmask 表示，DP[i][mask] 表示第 i 列狀態為 mask 時的最大部署數
# 需檢查同列、前一列、前兩列的攻擊範圍

def max_artillery(N, M, grid):
    """
    N: 列數, M: 行數, grid: N 行 M 字元陣列
    回傳: 最多能部署的炮兵部隊數量
    """
    # 預處理每列所有合法狀態
    valid = []
    for row in grid:
        states = []
        for mask in range(1<<M):
            ok = True
            for j in range(M):
                if (mask>>j)&1:
                    if row[j]=='H': ok=False
                    if j>=1 and (mask>>(j-1))&1: ok=False
                    if j>=2 and (mask>>(j-2))&1: ok=False
            if ok:
                states.append(mask)
        valid.append(states)
    from collections import defaultdict
    dp = [defaultdict(int) for _ in range(N+1)]
    dp[0][0]=0
    for i in range(1,N+1):
        for cur in valid[i-1]:
            for pre in dp[i-1]:
                # cur, pre 不能有同一列或相鄰列攻擊
                if (cur&pre)==0 and (cur&(pre<<1))==0 and (cur&(pre>>1))==0:
                    cnt = bin(cur).count('1')
                    dp[i][cur] = max(dp[i][cur], dp[i-1][pre]+cnt)
    return max(dp[N].values())

if __name__ == "__main__":
    N, M = map(int, input().split())
    grid = [input().strip() for _ in range(N)]
    print(max_artillery(N, M, grid))
