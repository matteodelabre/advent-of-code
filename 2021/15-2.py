from math import inf
from heapq import heappush, heappop

grid = []

try:
    while True:
        grid.append(list(map(int, input())))
except EOFError:
    pass

def at(y, x):
    return (
        grid[y % len(grid)][x % len(grid[0])]
        + y // len(grid) + x // len(grid) - 1
    ) % 9 + 1

h = 5 * len(grid)
w = 5 * len(grid[0])

queue = [(0, (0, 0))]
dist = [[inf] * w for _ in range(h)]
dist[0][0] = 0

while queue:
    _, (y, x) = heappop(queue)

    for i, j in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
        if 0 <= i < h and 0 <= j < w:
            alt = dist[y][x] + at(i, j)

            if alt < dist[i][j]:
                dist[i][j] = alt
                heappush(queue, (alt, (i, j)))

print(dist[-1][-1])
