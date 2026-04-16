# AI 教你的簡單版本（含詳細中文註解）
# UVA 100: The 3n + 1 problem

def cycle_length(n):
    """計算 n 的 3n+1 序列長度"""
    count = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    return count

def max_cycle_length(i, j):
    """回傳區間 [i, j] 內最大 cycle length"""
    return max(cycle_length(n) for n in range(min(i, j), max(i, j) + 1))

if __name__ == "__main__":
    while True:
        try:
            line = input()
            if not line:
                break
            i, j = map(int, line.split())
            print(i, j, max_cycle_length(i, j))
        except EOFError:
            break
