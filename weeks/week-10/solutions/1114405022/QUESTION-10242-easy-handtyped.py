"""UVA 10242 - Fourth Point !!

手打版：沿用 easy 的固定流程。
"""

import sys


def get_answer(nums):
    # 拆成四個點。
    p1 = (nums[0], nums[1])
    p2 = (nums[2], nums[3])
    p3 = (nums[4], nums[5])
    p4 = (nums[6], nums[7])

    # 找重複點 D，並取得另外兩點 A、B。
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

    # 第四點座標。
    x = a[0] + b[0] - d[0]
    y = a[1] + b[1] - d[1]
    return x, y


def solve(data: str) -> str:
    res = []
    for line in data.splitlines():
        if not line.strip():
            continue
        nums = list(map(float, line.split()))
        x, y = get_answer(nums)
        res.append(f"{x:.3f} {y:.3f}")
    return "\n".join(res)


def main() -> None:
    txt = sys.stdin.read()
    out = solve(txt)
    if out:
        print(out)


if __name__ == "__main__":
    main()
