"""UVA 10242 - Fourth Point !!

好記版（-easy）：
- 四個點中會有一個點重複出現兩次。
- 設重複點為 D，另外兩點是 A、B。
- 缺少的第四點 = A + B - D。
"""

import sys


def find_fourth_point(values):
    # 依序拆成四個座標點。
    p1 = (values[0], values[1])
    p2 = (values[2], values[3])
    p3 = (values[4], values[5])
    p4 = (values[6], values[7])

    # 找出哪一個是重複點，剩下兩個就是向量公式中的 A、B。
    if p1 == p2:
        d, a, b = p1, p3, p4
    elif p1 == p3:
        d, a, b = p1, p2, p4
    elif p1 == p4:
        d, a, b = p1, p2, p3
    elif p2 == p3:
        d, a, b = p2, p1, p4
    elif p2 == p4:
        d, a, b = p2, p1, p3
    else:
        d, a, b = p3, p1, p2

    # 向量關係：P = A + B - D
    x = a[0] + b[0] - d[0]
    y = a[1] + b[1] - d[1]
    return x, y


def solve(data: str) -> str:
    # 每行都是一組 8 個浮點數，讀到 EOF。
    outputs = []
    for line in data.splitlines():
        if not line.strip():
            continue
        nums = list(map(float, line.split()))
        x, y = find_fourth_point(nums)
        outputs.append(f"{x:.3f} {y:.3f}")

    return "\n".join(outputs)


def main() -> None:
    text = sys.stdin.read()
    ans = solve(text)
    if ans:
        print(ans)


if __name__ == "__main__":
    main()
