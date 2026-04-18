"""UVA 10008 - What's Cryptanalysis?（AI 版本）"""


def letter_frequency(lines: list[str]) -> list[tuple[str, int]]:
    """統計英文字母出現次數，忽略大小寫，只計算 A-Z。

    回傳格式：[(字母, 次數), ...]
    排序規則：先依次數遞減，再依字母遞增。
    """
    freq: dict[str, int] = {}
    for line in lines:
        for ch in line:
            if ch.isalpha():
                up = ch.upper()
                freq[up] = freq.get(up, 0) + 1

    return sorted(freq.items(), key=lambda item: (-item[1], item[0]))


def solve() -> None:
    """UVA 輸入：第一行 n，後續 n 行文字。"""
    n = int(input().strip())
    lines = [input() for _ in range(n)]
    for ch, count in letter_frequency(lines):
        print(f"{ch} {count}")


if __name__ == "__main__":
    solve()
