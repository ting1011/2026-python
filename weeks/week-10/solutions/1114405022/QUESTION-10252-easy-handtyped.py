"""UVA 10252 - Common Permutation

手打版：沿用 easy 模板。
"""

from collections import Counter
import sys


def solve(data: str) -> str:
    lines = data.splitlines()
    out = []

    i = 0
    while i + 1 < len(lines):
        a = lines[i]
        b = lines[i + 1]
        i += 2

        # 統計字元頻率。
        ca = Counter(a)
        cb = Counter(b)

        # 取交集字元，依序輸出最小重複次數。
        parts = []
        for ch in sorted(ca.keys() & cb.keys()):
            parts.append(ch * min(ca[ch], cb[ch]))

        out.append("".join(parts))

    return "\n".join(out)


def main() -> None:
    txt = sys.stdin.read()
    ans = solve(txt)
    if ans:
        print(ans)


if __name__ == "__main__":
    main()
