"""UVA 10268 - 498-bis"""

import sys


def derivative_value(x: int, coeffs: list[int]) -> int:
    n = len(coeffs) - 1
    if n <= 0:
        return 0

    ans = 0
    for i, c in enumerate(coeffs[:-1]):
        power = n - i
        ans = ans * x + c * power
    return ans


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

        out.append(str(derivative_value(x, coeffs)))

    return "\n".join(out)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
