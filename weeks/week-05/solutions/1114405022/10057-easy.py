# UVA 10057 - AI 教學簡單版（含中文註解）
n = int(input())
for _ in range(n):
    arr = list(map(int, input().split()))
    r = arr[0]
    nums = sorted(arr[1:])
    # 找中位數
    if r % 2 == 1:
        median = nums[r // 2]
        count = nums.count(median)
        print(f"{median} {count} 1")
    else:
        m1 = nums[r // 2 - 1]
        m2 = nums[r // 2]
        # 可能的A有多少種
        ways = m2 - m1 + 1
        # 統計A出現的次數
        count = 0
        for x in nums:
            if m1 <= x <= m2:
                count += 1
        print(f"{m1} {count} {ways}")
