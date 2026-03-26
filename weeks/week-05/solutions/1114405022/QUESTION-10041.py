# UVA 10041 - 手打版
n = int(input())
for i in range(n):
    arr = list(map(int, input().split()))
    r = arr[0]
    s = sorted(arr[1:])
    m = s[r // 2]
    total = 0
    for h in s:
        total += abs(h - m)
    print(total)
