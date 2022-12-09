grid = [list(map(int, line.strip())) for line in open(0)]
total = 0

for y in range(len(grid)):
    for x in range(len(grid[y])):
        total += (
            all(grid[py][x] < grid[y][x] for py in range(y))
            or all(grid[ny][x]) < grid[y][x] for ny in range(y + 1, len(grid)))
            or all(grid[y][px]) < grid[y][x] for px in range(x))
            or all(grid[y][nx]) < grid[y][x] for nx in range(x + 1, len(grid[y])))
        )

print(total)
