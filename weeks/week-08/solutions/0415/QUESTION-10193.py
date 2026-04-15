# 10193 arctan 分解
# 中文註解：暴力枚舉 b, c 使 (b+c) 最小

a = int(input())
min_sum = float('inf')
for b in range(a+1, 2*a+1):
    c = a*b//(b-a)
    if (a*b) % (b-a) == 0 and c >= b:
        min_sum = min(min_sum, b+c)
        break
print(min_sum)
