"""UVA 948 - Fibonaccimal Base（AI 版本）

此檔提供可重用函式 `fibonaccimal_base`，並保留 UVA 可直接送出的 stdin/stdout 介面。
"""


def fibonaccimal_base(n: int) -> str:
    """把十進位整數 n 轉成 fibonaccimal 表示字串。

    規則採 Zeckendorf 表示法：
    1. 可用的費氏數列是 1, 2, 3, 5, 8, ...（起始為 1、2）。
    2. 每一步都盡量拿不超過剩餘值的最大費氏數（貪婪法）。
    3. 組成 bit 字串（使用到該費氏數寫 1，否則寫 0）。
    """
    if n == 0:
        return "0"

    fibs = [1, 2]
    while fibs[-1] + fibs[-2] <= n:
        fibs.append(fibs[-1] + fibs[-2])
    if fibs[-1] > n:
        fibs.pop()

    bits = []
    remain = n
    for f in reversed(fibs):
        if f <= remain:
            bits.append("1")
            remain -= f
        else:
            bits.append("0")
    return "".join(bits)


def solve() -> None:
    """UVA 輸入格式：第一行 T，後續 T 行每行一個 n。"""
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(f"{n} = {fibonaccimal_base(n)} (fib)")


if __name__ == "__main__":
    solve()
