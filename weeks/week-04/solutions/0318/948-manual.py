"""UVA 948 - Fibonaccimal Base（手打版本）

這份程式保留與 AI 版相同功能，但寫法盡量直觀，方便考場手寫回憶。
"""


def fibonaccimal_base(n: int) -> str:
    """將十進位 n 轉為 fibonaccimal 字串。"""
    if n == 0:
        return "0"

    fibs = [1, 2]
    while fibs[-1] + fibs[-2] <= n:
        fibs.append(fibs[-1] + fibs[-2])
    if fibs[-1] > n:
        fibs.pop()

    remain = n
    ans = []
    for f in reversed(fibs):
        if remain >= f:
            ans.append("1")
            remain -= f
        else:
            ans.append("0")
    return "".join(ans)


def solve() -> None:
    """依 UVA 規格讀 T 筆測資並輸出結果。"""
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(f"{n} = {fibonaccimal_base(n)} (fib)")


if __name__ == "__main__":
    solve()
