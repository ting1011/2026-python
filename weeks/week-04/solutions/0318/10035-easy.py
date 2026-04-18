"""UVA 10035 - Easy 版"""


def carry_count_easy(a: int, b: int) -> int:
    a = str(a)[::-1]
    b = str(b)[::-1]
    carry = 0
    times = 0
    for i in range(max(len(a), len(b))):
        da = int(a[i]) if i < len(a) else 0
        db = int(b[i]) if i < len(b) else 0
        if da + db + carry >= 10:
            carry = 1
            times += 1
        else:
            carry = 0
    return times


def solve() -> None:
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        c = carry_count_easy(a, b)
        if c == 0:
            print("No carry operation.")
        elif c == 1:
            print("1 carry operation.")
        else:
            print(f"{c} carry operations.")


if __name__ == "__main__":
    solve()
