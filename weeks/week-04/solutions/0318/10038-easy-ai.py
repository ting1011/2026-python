# UVA 10038: Jolly Jumpers（簡易版）
# 中文詳細註解

def is_jolly(nums):
    n = len(nums)
    diffs = set(abs(nums[i] - nums[i-1]) for i in range(1, n))
    return diffs == set(range(1, n))

# 測試
if __name__ == "__main__":
    print(is_jolly([1, 4, 2, 3]))  # True
