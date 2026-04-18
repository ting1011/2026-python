"""UVA 10019 - Easy 版"""


def count_ones_easy(n: int) -> tuple[int, int]:
    b1 = bin(n).count("1")
    b2 = bin(int(str(n), 16)).count("1")
    return b1, b2


def solve() -> None:
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        a, b = count_ones_easy(n)
        print(a, b)


if __name__ == "__main__":
    solve()
