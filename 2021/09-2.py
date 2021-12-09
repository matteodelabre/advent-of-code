hmap = []

try:
    while True:
        hmap.append(input())
except EOFError:
    pass

w = len(hmap[0])
h = len(hmap)

def low(i, j):
    for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        if ni < 0 or ni >= h or nj < 0 or nj >= w: continue
        if hmap[ni][nj] <= hmap[i][j]: return False
    return True

def basin(i, j, visited):
    if hmap[i][j] == "9": return

    neighbors = []

    for ni, nj in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
        if ni < 0 or ni >= h or nj < 0 or nj >= w: continue
        if (ni, nj) in visited: continue
        if hmap[ni][nj] < hmap[i][j]: return

        neighbors.append((ni, nj))

    visited.add((i, j))

    for ni, nj in neighbors:
        basin(ni, nj, visited)

sizes = []

for i in range(h):
    for j in range(w):
        if low(i, j):
            result = {(i, j)}
            basin(i, j, result)
            sizes.append(len(result))

from math import prod
print(prod(sorted(sizes)[-3:]))
