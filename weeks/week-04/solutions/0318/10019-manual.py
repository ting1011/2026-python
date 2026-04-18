"""UVA 10019 - Funny Encryption Method（手打版本）"""


def count_ones(n: int) -> tuple[int, int]:
    """計算題目要求的兩種 popcount。"""
    b1 = bin(n).count("1")
    # 題目第二個值不是逐位數相加，而是把整串視為十六進位。
    b2 = bin(int(str(n), 16)).count("1")
    return b1, b2


def solve() -> None:
    """讀入多筆測資並逐行輸出 b1、b2。"""
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        b1, b2 = count_ones(n)
        print(f"{b1} {b2}")


if __name__ == "__main__":
    solve()
