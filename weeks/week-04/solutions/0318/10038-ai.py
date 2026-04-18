"""UVA 10038 - Jolly Jumpers（AI 版本）"""


def is_jolly(nums: list[int]) -> bool:
    """判斷數列是否為 Jolly Jumper。

    長度為 n 的序列，若相鄰差絕對值集合剛好等於 {1,2,...,n-1}，則為 Jolly。
    """
    n = len(nums)
    if n <= 1:
        return True

    diffs = {abs(nums[i] - nums[i - 1]) for i in range(1, n)}
    return diffs == set(range(1, n))


def solve() -> None:
    """每行格式：n a1 a2 ... an，直到 EOF。"""
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
