# UVA 948: Fibonaccimal Base
# 題目：將一個正整數表示成費波那契數的和（每個費波那契數最多用一次）
# 中文註解版（手打）

def fibonaccimal_base(n):
    fibs = [1, 2]
    while fibs[-1] + fibs[-2] <= n:
        fibs.append(fibs[-1] + fibs[-2])
    res = []
    for f in reversed(fibs):
        if n >= f:
            res.append('1')
            n -= f
        else:
            res.append('0')
    return ''.join(res).lstrip('0')

if __name__ == "__main__":
    while True:
        try:
            n = int(input())
            print(f"{n} = {fibonaccimal_base(n)} (fib)")
        except EOFError:
            break
