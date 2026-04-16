# UVA 10038: Jolly Jumpers
# 中文註解版（手打）

def is_jolly(nums):
    n = len(nums)
    diffs = set(abs(nums[i] - nums[i-1]) for i in range(1, n))
    return diffs == set(range(1, n))

if __name__ == "__main__":
    while True:
        try:
            parts = input().split()
            if not parts:
                break
            nums = list(map(int, parts[1:]))
            print("Jolly" if is_jolly(nums) else "Not jolly")
        except EOFError:
            break
