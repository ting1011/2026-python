"""UVA 10035 - Primary Arithmetic（手打版本）"""


def carry_count(a: int, b: int) -> int:
    """用模擬直式加法的方式計算進位次數。"""
    a = str(a)[::-1]
    b = str(b)[::-1]
    carry = 0
    cnt = 0
    for i in range(max(len(a), len(b))):
        da = int(a[i]) if i < len(a) else 0
        db = int(b[i]) if i < len(b) else 0
        if da + db + carry >= 10:
            carry = 1
            cnt += 1
        else:
            carry = 0
    return cnt


def solve() -> None:
    """讀到 0 0 結束，其他每行輸出進位描述。"""
    while True:
        a, b = map(int, input().split())
        if a == 0 and b == 0:
            break
        cnt = carry_count(a, b)
        if cnt == 0:
            print("No carry operation.")
        elif cnt == 1:
            print("1 carry operation.")
        else:
            print(f"{cnt} carry operations.")


if __name__ == "__main__":
    solve()
