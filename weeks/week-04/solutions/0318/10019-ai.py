"""UVA 10019 - Funny Encryption Method（AI 版本）"""


def count_ones(n: int) -> tuple[int, int]:
    """回傳 (b1, b2)。

    b1: n 當十進位整數時，其二進位表示中 1 的個數。
    b2: 把 n 的十進位字串視為十六進位數字後，再轉二進位計算 1 的個數。

    例如 n=265：
    - b1 = popcount(265)
    - b2 = popcount(int("265", 16))
    """
    b1 = bin(n).count("1")
    b2 = bin(int(str(n), 16)).count("1")
    return b1, b2


def solve() -> None:
    """UVA 輸入：第一行 T，接著 T 行整數。"""
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        b1, b2 = count_ones(n)
        print(f"{b1} {b2}")


if __name__ == "__main__":
    solve()
