"""UVA 948 - Easy 版

記法重點：先造費氏、再由大到小貪婪扣。
"""


def fibonaccimal_base_easy(n: int) -> str:
    if n == 0:
        return "0"

    fib = [1, 2]
    while fib[-1] + fib[-2] <= n:
        fib.append(fib[-1] + fib[-2])
    if fib[-1] > n:
        fib.pop()

    ans = ""
    for f in reversed(fib):
        if n >= f:
            ans += "1"
            n -= f
        else:
            ans += "0"
    return ans


def solve() -> None:
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        print(f"{n} = {fibonaccimal_base_easy(n)} (fib)")


if __name__ == "__main__":
    solve()
