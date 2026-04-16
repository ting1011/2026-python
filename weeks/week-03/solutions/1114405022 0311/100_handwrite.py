# 你手打的程式（可自行修改內容）
def cycle_length(n):
    c = 1
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        c += 1
    return c

def max_cycle_length(i, j):
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
