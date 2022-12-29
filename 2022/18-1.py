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

cubes = defaultdict(lambda: defaultdict(lambda: defaultdict(lambda: False)))

for cube in open(0):
    x, y, z = map(int, cube.split(","))
    cubes[x][y][z] = True

print(boundaries(cubes))
