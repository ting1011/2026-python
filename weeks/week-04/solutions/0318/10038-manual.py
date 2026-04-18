"""UVA 10038 - Jolly Jumpers（手打版本）"""


def is_jolly(nums: list[int]) -> bool:
    """手動實作 Jolly 判斷。"""
    n = len(nums)
    if n <= 1:
        return True
    diffs = set()
    for i in range(1, n):
        diffs.add(abs(nums[i] - nums[i - 1]))
    return diffs == set(range(1, n))


def solve() -> None:
    """逐行讀入測資並輸出 Jolly/Not jolly。"""
    while True:
        try:
            parts = input().split()
        except EOFError:
            break
        if not parts:
            continue
        nums = list(map(int, parts[1:]))
        print("Jolly" if is_jolly(nums) else "Not jolly")


if __name__ == "__main__":
    solve()
