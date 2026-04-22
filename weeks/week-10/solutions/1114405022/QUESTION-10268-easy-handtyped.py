"""UVA 10268 - 498-bis

手打版：沿用 easy 的導函式 Horner 寫法。
"""

import sys


def calc_derivative_at_x(x: int, coeffs: list[int]) -> int:
    n = len(coeffs) - 1
    if n <= 0:
        return 0

    # 逐步做 Horner：value = value*x + 導函式下一項係數
    value = 0
    for i, c in enumerate(coeffs[:-1]):
        p = n - i
        value = value * x + c * p

    return value


def solve(data: str) -> str:
    lines = data.splitlines()
    out = []

    i = 0
    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue

        x = int(lines[i].strip())
        i += 1

        while i < len(lines) and not lines[i].strip():
            i += 1
        if i >= len(lines):
            break

        coeffs = list(map(int, lines[i].split()))
        i += 1

        out.append(str(calc_derivative_at_x(x, coeffs)))

    return "\n".join(out)


def main() -> None:
    txt = sys.stdin.read()
    ans = solve(txt)
    if ans:
        print(ans)


if __name__ == "__main__":
    main()
