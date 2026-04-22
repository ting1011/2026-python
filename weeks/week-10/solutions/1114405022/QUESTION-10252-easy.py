"""UVA 10252 - Common Permutation

好記版（-easy）：
- 兩行當一組
- 用 Counter 算各字元次數
- 取最小次數後排序輸出
"""

from collections import Counter
import sys


def solve(data: str) -> str:
    # 這題每兩行是一筆測資，讀到 EOF。
    lines = data.splitlines()
    ans = []

    idx = 0
    while idx + 1 < len(lines):
        s1 = lines[idx]
        s2 = lines[idx + 1]
        idx += 2

        # 分別統計兩字串中每個字元的出現次數。
        c1 = Counter(s1)
        c2 = Counter(s2)

        # 共同字元的次數 = 兩邊次數的較小值。
        parts = []
        common_chars = sorted(c1.keys() & c2.keys())
        for ch in common_chars:
            repeat = min(c1[ch], c2[ch])
            parts.append(ch * repeat)

        # 依字典序串起來就是答案。
        ans.append("".join(parts))

    return "\n".join(ans)


def main() -> None:
    text = sys.stdin.read()
    out = solve(text)
    if out:
        print(out)


if __name__ == "__main__":
    main()
