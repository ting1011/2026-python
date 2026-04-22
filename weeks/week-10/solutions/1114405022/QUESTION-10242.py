"""UVA 10242 - Fourth Point !!"""

import sys


def solve_line(nums):
    p1 = (nums[0], nums[1])
    p2 = (nums[2], nums[3])
    p3 = (nums[4], nums[5])
    p4 = (nums[6], nums[7])

    if p1 == p2:
        dup, a, b = p1, p3, p4
    elif p1 == p3:
        dup, a, b = p1, p2, p4
    elif p1 == p4:
        dup, a, b = p1, p2, p3
    elif p2 == p3:
        dup, a, b = p2, p1, p4
    elif p2 == p4:
        dup, a, b = p2, p1, p3
    else:
        dup, a, b = p3, p1, p2

    x = a[0] + b[0] - dup[0]
    y = a[1] + b[1] - dup[1]
    return f"{x:.3f} {y:.3f}"


def solve(data: str) -> str:
    out = []
    for line in data.splitlines():
        if not line.strip():
            continue
        nums = list(map(float, line.split()))
        out.append(solve_line(nums))
    return "\n".join(out)


def main() -> None:
    print(solve(sys.stdin.read()))


if __name__ == "__main__":
    main()
