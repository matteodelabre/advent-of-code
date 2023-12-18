from heapq import heappush, heappop
from collections import namedtuple, defaultdict

Node = namedtuple("Node", ["i", "j", "direc", "moves"])
direcs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

grid = open(0).read().splitlines()

start = Node(i=0, j=0, direc=0, moves=0)
queue = [start]
dist = defaultdict(lambda: float("inf"))
dist[start] = 0

while queue:
    node = heappop(queue)

    for direc, (di, dj) in enumerate(direcs):
        if abs(direc - node.direc) == 2:
            continue

        ii = node.i + di
        jj = node.j + dj

        if not (0 <= ii < len(grid) and 0 <= jj < len(grid[0])):
            continue

        if node.moves >= 2 and direc == node.direc:
            continue

        cost = int(grid[ii][jj])
        succ = Node(
            i=ii,
            j=jj,
            direc=direc,
            moves=node.moves + 1 if direc == node.direc else 0,
        )

        if dist[node] + cost < dist[succ]:
            dist[succ] = dist[node] + cost
            heappush(queue, succ)

print(min(
    dist[node]
    for node in dist
    if node.i == len(grid) - 1 and node.j == len(grid[0]) - 1
))
