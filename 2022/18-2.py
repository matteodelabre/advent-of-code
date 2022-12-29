from math import inf
from itertools import product
from collections import defaultdict

nbhood = ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1))

def boundaries(cubes):
    return sum(
        6 - sum(cubes[x + dx][y + dy][z + dz] for dx, dy, dz in nbhood)
        for x, xslice in list(cubes.items())
        for y, xyslice in list(xslice.items())
        for z, value in list(xyslice.items())
        if value
    )

def extents(iterable):
    minimum = inf
    maximum = -inf

    for item in iterable:
        minimum = min(minimum, item)
        maximum = max(maximum, item)

    return range(minimum, maximum + 1)

def flood(cubes):
    seen = set()

    for x, xslice in list(cubes.items()):
        for y, xyslice in list(xslice.items()):
            for z, value in list(xyslice.items()):
                if value:
                    seen.add((x, y, z))

    xrange = extents(cube[0] for cube in seen)
    yrange = extents(cube[1] for cube in seen)
    zrange = extents(cube[2] for cube in seen)

    for start in product(xrange, yrange, zrange):
        if start in seen:
            continue

        block = set((start,))
        stack = [(start)]
        outside = False

        while stack and not outside:
            x, y, z = stack.pop()

            if (x, y, z) in seen:
                continue

            for dx, dy, dz in nbhood:
                nx, ny, nz = x + dx, y + dy, z + dz

                if (nx, ny, nz) not in block:
                    if nx in xrange and ny in yrange and nz in zrange:
                        block.add((nx, ny, nz))
                        stack.append((nx, ny, nz))
                    else:
                        outside = True
                        break

        if not outside:
            for x, y, z in block:
                cubes[x][y][z] = True

cubes = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: False)))

for cube in open(0):
    x, y, z = map(int, cube.split(","))
    cubes[x][y][z] = True

flood(cubes)
print(boundaries(cubes))
