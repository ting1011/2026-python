"""UVA 10252 - Common Permutation"""

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

        ca = Counter(a)
        cb = Counter(b)

        common = []
        for ch in sorted(ca.keys() & cb.keys()):
            common.append(ch * min(ca[ch], cb[ch]))

        out.append("".join(common))

    return "\n".join(out)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
