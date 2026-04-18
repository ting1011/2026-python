"""UVA 10008 - Easy 版"""


def letter_frequency_easy(lines: list[str]) -> list[tuple[str, int]]:
    cnt: dict[str, int] = {}
    for line in lines:
        for ch in line:
            if ch.isalpha():
                ch = ch.upper()
                cnt[ch] = cnt.get(ch, 0) + 1
    return sorted(cnt.items(), key=lambda x: (-x[1], x[0]))


def solve() -> None:
    n = int(input().strip())
    lines = [input() for _ in range(n)]
    for ch, c in letter_frequency_easy(lines):
        print(f"{ch} {c}")


if __name__ == "__main__":
    solve()
