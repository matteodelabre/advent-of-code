from collections import defaultdict

direcs = {(-1, 0): "^", (1, 0): "v", (0, -1): "<", (0, 1): ">"}
grid = open(0).read().splitlines()

def around(i, j):
    return {
        (i + di, j + dj): grid[i + di][j + dj] in symbol + "."
        for (di, dj), symbol in direcs.items()
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
            del neighbors[(li, lj)]
            li, lj = i, j
            (i, j), outward = next(iter(neighbors.items()))

            if outward:
                distance += 1
            else:
                return None
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
                for (ni, nj), outward in neighbors.items():
                    if outward:
                        found = search(i, j, ni, nj)

                        if found is not None:
                            next_node, distance = found
                            graph[(i, j)][next_node] = -distance

dist = defaultdict(lambda: float("inf"))
dist[begin] = 0

for _ in range(len(graph) - 1):
    for node in graph:
        for neighbor, value in graph[node].items():
            dist[neighbor] = min(dist[neighbor], dist[node] + value)

print(-dist[goal])
