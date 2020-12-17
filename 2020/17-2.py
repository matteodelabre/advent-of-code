from collections import defaultdict
from itertools import product

# read initial layer
active = set()
y = 0

try:
    while True:
        x = 0

        for cell in input():
            if cell == '#':
                active.add((x, y, 0, 0))

            x += 1

        y += 1
except EOFError:
    pass

# generate the state following a given state
def iter(active):
    # count the number of neighbors of each cell
    neighbors = defaultdict(int)

    for x, y, z, w in active:
        for dx, dy, dz, dw in product(range(-1, 2), repeat=4):
            if dx != 0 or dy != 0 or dz != 0 or dw != 0:
                neighbors[(x + dx, y + dy, z + dz, w + dw)] += 1

    # generate next state
    next_active = set()

    for cell in active:
        if neighbors[cell] in (2, 3):
            next_active.add(cell)

    for cell in neighbors:
        if neighbors[cell] == 3:
            next_active.add(cell)

    return next_active

for i in range(6):
    active = iter(active)

print(len(active))
