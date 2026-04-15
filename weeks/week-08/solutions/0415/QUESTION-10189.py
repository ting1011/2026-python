# 10189 Minesweeper
# 中文註解：模擬地雷周圍計數

dx = [-1,-1,-1,0,0,1,1,1]
dy = [-1,0,1,-1,1,-1,0,1]

case = 1
while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    field = [list(input()) for _ in range(n)]
    ans = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if field[i][j] == '*':
                ans[i][j] = '*'
                for d in range(8):
                    ni, nj = i+dx[d], j+dy[d]
                    if 0<=ni<n and 0<=nj<m and field[ni][nj] != '*':
                        if ans[ni][nj] != '*':
                            ans[ni][nj] += 1
    if case > 1:
        print()
    print(f"Field #{case}:")
    for row in ans:
        print(''.join(str(x) for x in row))
    case += 1
