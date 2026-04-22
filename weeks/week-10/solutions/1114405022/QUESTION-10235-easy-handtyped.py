"""UVA 10235 - Simply Emirp

手打版：沿用 easy 流程，方便考場快速回憶。
"""

import math
import sys


def is_prime(n: int) -> bool:
    # 基本質數判斷模板。
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    r = int(math.isqrt(n))
    d = 3
    while d <= r:
        if n % d == 0:
            return False
        d += 2
    return True


def solve(data: str) -> str:
    lines = [line.strip() for line in data.splitlines() if line.strip()]
    out = []

    for line in lines:
        n = int(line)
        if not is_prime(n):
            out.append(f"{n} is not prime.")
            continue

        rev = int(str(n)[::-1])
        if rev != n and is_prime(rev):
            out.append(f"{n} is emirp.")
        else:
            out.append(f"{n} is prime.")

    return "\n".join(out)


def main() -> None:
    txt = sys.stdin.read()
    res = solve(txt)
    if res:
        print(res)


if __name__ == "__main__":
    main()
