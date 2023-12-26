from collections import defaultdict
from functools import cache

direcs = {(-1, 0), (1, 0), (0, -1), (0, 1)}
grid = open(0).read().splitlines()

def around(i, j):
    return {
        (i + di, j + dj)
        for di, dj in direcs
        if (
            0 <= i + di < len(grid)
            and 0 <= j + dj < len(grid[0])
            and grid[i + di][j + dj] != "#"
        )
    }

def search(li, lj, i, j):
    distance = 1

    while True:
        neighbors = around(i, j)

        if len(neighbors) == 2:
            neighbors.discard((li, lj))
            li, lj = i, j
            i, j = next(iter(neighbors))
            distance += 1
        else:
            return (i, j), distance

begin = (0, grid[0].index("."))
goal = (len(grid) - 1, grid[-1].index("."))
graph = defaultdict(dict)

for i, line in enumerate(grid):
    for j, cell in enumerate(line):
        if cell == ".":
            neighbors = around(i, j)

            if len(neighbors) > 2 or (i, j) in (begin, goal):
                for ni, nj in neighbors:
                    found = search(i, j, ni, nj)

                    if found is not None:
                        next_node, distance = found
                        graph[(i, j)][next_node] = distance

@cache
def longest_path(at, visited):
    return max(
        (
            value + longest_path(neighbor, visited | {neighbor})
            for neighbor, value in graph[at].items()
            if neighbor not in visited
        ),
        default=0
    )

print(longest_path(begin, frozenset({begin})))
