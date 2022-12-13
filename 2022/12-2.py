from math import inf

grid = [list(line)[:-1] for line in open(0)]
n, m = len(grid), len(grid[0])
target = None

for y in range(n):
    for x in range(m):
        if grid[y][x] == "S":
            grid[y][x] = "a"
        elif grid[y][x] == "E":
            grid[y][x] = "z"
            target = (y, x)

        grid[y][x] = ord(grid[y][x]) - ord("a")

queue = [target]
depth = [[inf] * m for _ in range(n)]
depth[target[0]][target[1]] = 0

while queue:
    y, x = queue[0]
    queue = queue[1:]

    for ny, nx in ((y, x + 1), (y - 1, x), (y, x - 1), (y + 1, x)):
        if (
            0 <= ny < n and 0 <= nx < m
            and grid[ny][nx] >= grid[y][x] - 1
            and depth[ny][nx] == inf
        ):
            depth[ny][nx] = depth[y][x] + 1
            queue.append((ny, nx))

print(min(
    depth[y][x]
    for y in range(n)
    for x in range(m)
    if grid[y][x] == 0
))
