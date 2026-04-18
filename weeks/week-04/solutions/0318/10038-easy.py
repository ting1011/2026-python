"""UVA 10038 - Easy 版"""


def is_jolly_easy(nums: list[int]) -> bool:
    n = len(nums)
    if n <= 1:
        return True
    diffs = set()
    for i in range(1, n):
        diffs.add(abs(nums[i] - nums[i - 1]))
    return diffs == set(range(1, n))


def solve() -> None:
    while True:
        try:
            parts = input().split()
        except EOFError:
            break
        if not parts:
            continue
        nums = list(map(int, parts[1:]))
        print("Jolly" if is_jolly_easy(nums) else "Not jolly")


if __name__ == "__main__":
    solve()
