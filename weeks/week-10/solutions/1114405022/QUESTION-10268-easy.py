"""UVA 10268 - 498-bis

好記版（-easy）：
- 給 x 與多項式係數（由高次到低次）
- 要算 P'(x)
- 直接對導函式係數做 Horner
"""

import sys


def eval_derivative(x: int, coeffs: list[int]) -> int:
    # 若只有常數項，導數一定是 0。
    degree = len(coeffs) - 1
    if degree <= 0:
        return 0

    # 導函式係數依序是：a0*n, a1*(n-1), ...
    # 再用 Horner 法在 x 上求值。
    value = 0
    for i, coef in enumerate(coeffs[:-1]):
        power = degree - i
        value = value * x + coef * power

    return value


def solve(data: str) -> str:
    lines = data.splitlines()
    ans = []

    idx = 0
    while idx < len(lines):
        # 跳過空行，避免配對錯誤。
        if not lines[idx].strip():
            idx += 1
            continue

        # 第一行：x
        x = int(lines[idx].strip())
        idx += 1

        # 第二行：多項式係數
        while idx < len(lines) and not lines[idx].strip():
            idx += 1
        if idx >= len(lines):
            break

        coeffs = list(map(int, lines[idx].split()))
        idx += 1

        ans.append(str(eval_derivative(x, coeffs)))

    return "\n".join(ans)


def main() -> None:
    text = sys.stdin.read()
    out = solve(text)
    if out:
        print(out)


if __name__ == "__main__":
    main()
