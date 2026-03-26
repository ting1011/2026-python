# UVA 10050 - 手打版
n = int(input())
for _ in range(n):
    d = int(input())
    p = int(input())
    a = [int(input()) for _ in range(p)]
    s = set()
    for x in a:
        for i in range(x, d+1, x):
            if i % 7 != 6 and i % 7 != 0:
                s.add(i)
    print(len(s))
