# UVA 10041 - 簡單解法
# 題目：找出一條街上所有人到某一點的總距離最小
# 解法：取中位數
n = int(input())
for _ in range(n):
    data = list(map(int, input().split()))
    r, houses = data[0], sorted(data[1:])
    median = houses[r // 2]
    print(sum(abs(h - median) for h in houses))
