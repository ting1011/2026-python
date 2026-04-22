"""UVA 10235 - Simply Emirp

好記版（-easy）：
1. 先判斷 n 是不是質數
2. 再把數字反轉
3. 反轉後也為質數且不等於原數 => emirp
"""

import math
import sys


def is_prime(n: int) -> bool:
    # 小於 2 一定不是質數。
    if n < 2:
        return False

    # 2 是唯一的偶質數。
    if n == 2:
        return True

    # 其他偶數都不是質數。
    if n % 2 == 0:
        return False

    # 只要檢查到 sqrt(n) 即可。
    root = int(math.isqrt(n))
    divisor = 3
    while divisor <= root:
        if n % divisor == 0:
            return False
        divisor += 2

    return True


def solve(data: str) -> str:
    # 每行一個整數，讀到 EOF 為止。
    nums = [int(x.strip()) for x in data.splitlines() if x.strip()]
    ans = []

    for n in nums:
        # 第一步：原數先判斷是不是質數。
        if not is_prime(n):
            ans.append(f"{n} is not prime.")
            continue

        # 第二步：把整數轉字串後反轉，再轉回整數。
        rev = int(str(n)[::-1])

        # 第三步：反轉後也要是質數，而且不能跟原數相同。
        if rev != n and is_prime(rev):
            ans.append(f"{n} is emirp.")
        else:
            ans.append(f"{n} is prime.")

    return "\n".join(ans)


def main() -> None:
    text = sys.stdin.read()
    output = solve(text)
    if output:
        print(output)


if __name__ == "__main__":
    main()
