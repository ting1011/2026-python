"""UVA 10226 - Hardwood Species

手打版（以 easy 版本邏輯手動整理）：
- 流程固定、方便考場回憶
- 含繁體中文詳細註解
"""

from collections import Counter
import sys


def solve(data: str) -> str:
    # 統一換行符號，避免 Windows/Unix 差異讓分割失敗。
    text = data.replace("\r\n", "\n").strip()
    if not text:
        return ""

    # 第一行是測資數量。
    first_newline = text.find("\n")
    if first_newline == -1:
        return ""
    t = int(text[:first_newline].strip())

    # 其餘內容依空行切成多筆測資。
    rest = text[first_newline + 1 :].lstrip("\n")
    blocks = rest.split("\n\n") if rest else []
    blocks = blocks[:t]

    all_outputs = []

    for block in blocks:
        # 每行是一個樹種名稱，名稱可能含空白，不能再拆單字。
        trees = [line for line in block.split("\n") if line != ""]
        freq = Counter(trees)
        total = len(trees)

        # 依字典序輸出，百分比四位小數。
        lines = []
        for tree in sorted(freq.keys()):
            percent = freq[tree] * 100.0 / total
            lines.append(f"{tree} {percent:.4f}")

        all_outputs.append("\n".join(lines))

    # 多筆測資之間空一行。
    return "\n\n".join(all_outputs)


def main() -> None:
    data = sys.stdin.read()
    ans = solve(data)
    if ans:
        print(ans)


if __name__ == "__main__":
    main()
