# 你手打的程式（可自行修改內容）
def move_robot(commands, x, y, dir, grid, lost_set):
    dirs = 'NESW'
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    d = dirs.index(dir)
    max_x, max_y = grid
    lost = False
    for c in commands:
        if c == 'L':
            d = (d - 1) % 4
        elif c == 'R':
            d = (d + 1) % 4
        elif c == 'F':
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx <= max_x and 0 <= ny <= max_y:
                x, y = nx, ny
            else:
                if (x, y, dirs[d]) not in lost_set:
                    lost = True
                    lost_set.add((x, y, dirs[d]))
                    break
    return x, y, dirs[d], lost

if __name__ == "__main__":
    import sys
    lost_set = set()
    grid = tuple(map(int, sys.stdin.readline().split()))
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        if line.strip() == '':
            continue
        x, y, dir = line.strip().split()
        x, y = int(x), int(y)
        commands = sys.stdin.readline().strip()
        nx, ny, ndir, lost = move_robot(commands, x, y, dir, grid, lost_set)
        print(f"{nx} {ny} {ndir}{' LOST' if lost else ''}")
