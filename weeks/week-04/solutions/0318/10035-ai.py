"""UVA 10035 - Primary Arithmetic（AI 版本）"""


def carry_count(a: int, b: int) -> int:
    """回傳 a+b 的十進位直式加法中，產生進位的次數。"""
    ra = str(a)[::-1]
    rb = str(b)[::-1]
    carry = 0
    count = 0

    for i in range(max(len(ra), len(rb))):
        d1 = int(ra[i]) if i < len(ra) else 0
        d2 = int(rb[i]) if i < len(rb) else 0
        if d1 + d2 + carry >= 10:
            carry = 1
            count += 1
        else:
            carry = 0
    return count


def solve() -> None:
    """持續讀入 a, b，直到遇到 0 0 為止。"""
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        count = carry_count(a, b)
        if count == 0:
            print("No carry operation.")
        elif count == 1:
            print("1 carry operation.")
        else:
            print(f"{count} carry operations.")


if __name__ == "__main__":
    solve()
