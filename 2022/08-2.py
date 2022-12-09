grid = [list(map(int, line.strip())) for line in open(0)]
result = 0

for y in range(len(grid)):
    for x in range(len(grid[y])):
        fpy = fny = fpx = fnx = 0

        for py in range(y - 1, -1, -1):
            fpy += 1
            if grid[py][x] >= grid[y][x]: break

        for ny in range(y + 1, len(grid)):
            fny += 1
            if grid[ny][x] >= grid[y][x]: break

        for px in range(x - 1, -1, -1):
            fpx += 1
            if grid[y][px] >= grid[y][x]: break

        for nx in range(x + 1, len(grid[y])):
            fnx += 1
            if grid[y][nx] >= grid[y][x]: break

        result = max(result, fpy * fny * fpx * fnx)

print(result)
