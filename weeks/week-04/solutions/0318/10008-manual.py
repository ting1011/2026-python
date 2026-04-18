"""UVA 10008 - What's Cryptanalysis?（手打版本）"""


def letter_frequency(lines: list[str]) -> list[tuple[str, int]]:
    """逐字元掃描並統計字母次數。"""
    freq: dict[str, int] = {}
    for line in lines:
        for ch in line:
            if ch.isalpha():
                ch = ch.upper()
                freq[ch] = freq.get(ch, 0) + 1
    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))


def solve() -> None:
    """依題目格式讀入 n 行字串並輸出統計結果。"""
    n = int(input().strip())
    lines = [input() for _ in range(n)]
    for ch, count in letter_frequency(lines):
        print(f"{ch} {count}")


if __name__ == "__main__":
    solve()
