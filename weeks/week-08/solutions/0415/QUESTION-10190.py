# 10190 自動傘雨量計算
# 中文註解：模擬每把傘覆蓋區間，計算未覆蓋區域的雨量

N, W, T, V = map(int, input().split())
umbrellas = []
for _ in range(N):
    x, l, v = map(int, input().split())
    umbrellas.append((x, x+l))
# 合併區間
umbrellas.sort()
merged = []
for s, e in umbrellas:
    if not merged or merged[-1][1] < s:
        merged.append([s, e])
    else:
        merged[-1][1] = max(merged[-1][1], e)
# 計算未覆蓋長度
covered = 0
for s, e in merged:
    covered += min(e, W) - max(s, 0)
covered = max(0, covered)
not_covered = max(0, W - covered)
ans = not_covered * T * V
print(f"{ans:.2f}")
